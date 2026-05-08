from __future__ import annotations

import copy
import json
import pathlib
import shutil
import subprocess
import sys
import urllib.request
import wave
from dataclasses import dataclass
from typing import Any

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_api_demo_core import (
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    STATUS_BLOCKED,
    STATUS_SUCCESS,
    VisualGenerationError,
    _build_visual_asset_output_path,
    _download_binary_file,
    _execute_aliyun_visual_generation_task,
    _extract_aliyun_image_result_url,
    _extract_aliyun_video_result_url,
    _looks_like_timeout_message,
    _poll_aliyun_visual_task,
    _resolve_visual_candidate_pool,
    _sanitize_message,
    _upload_file_to_aliyun_temp_storage,
    _urlopen_json_request,
    load_formal_config,
)


BASE_DIR = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "host_motion_asset_gate_round5"
)
ASSETS_DIR = BASE_DIR / "assets"
DETECT_DIR = BASE_DIR / "detect_probe"
AUDIT_DIR = BASE_DIR / "audit"
TMP_DIR = BASE_DIR / "tmp"
S2V_DIR = BASE_DIR / "s2v_probe"
PREVIEW_DIR = S2V_DIR / "preview_frames"

SUMMARY_JSON = AUDIT_DIR / "round5_detect_summary.json"
SUMMARY_MD = AUDIT_DIR / "最小闸门审计_round5.md"
CONTACT_SHEET_PATH = AUDIT_DIR / "s2v_smoke_contact_sheet.jpg"

SOURCE_AUDIO = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "tts"
    / "seg01_hook.wav"
)
TRIMMED_AUDIO = TMP_DIR / "audio_hook_excerpt_2p6s.wav"
TRIM_SECONDS = 2.6

WAN27_PRIMARY_MODEL = "wan2.7-image-pro"
WAN27_FALLBACK_MODEL = "wan2.7-image"
WAN_S2V_MODEL = "wan2.2-s2v"
WAN_S2V_DETECT_MODEL = "wan2.2-s2v-detect"
WAN27_SIZE = "1152*2048"
S2V_RESOLUTION = "480P"


@dataclass(frozen=True)
class CandidateSpec:
    candidate_id: str
    label: str
    design_goal: str
    prompt: str


CANDIDATES = [
    CandidateSpec(
        candidate_id="候选A_round5_软脸主持肖像",
        label="候选A｜软脸主持肖像",
        design_goal="沿候选C继续降玩偶感，做更稳定的卡通数字人脸。",
        prompt=(
            "vertical 9:16 portrait, original presenter mascot, close-up head and shoulders, front-facing, "
            "large smooth face, animated-film style humanlike eyes with white sclera, iris and pupil, "
            "clear natural eyebrows, visible nose with nostrils, soft natural lips, gentle confident host smile, "
            "orange presenter jacket with subtle voxel-inspired seams only, soft brown hair with no face obstruction, "
            "cream studio background, stylized 3D cartoon digital-host portrait, not photorealistic, not realistic human, "
            "not toy doll, not baby doll, not game screenshot, no text, no props, no watermark."
        ),
    ),
    CandidateSpec(
        candidate_id="候选B_round5_大脸卡通数字人",
        label="候选B｜大脸卡通数字人",
        design_goal="进一步放大脸部占比，让 detect 几乎只看脸。",
        prompt=(
            "vertical 9:16 portrait, passport-style centered cartoon digital host portrait, face fills nearly 80 percent of frame, "
            "strong front face, smooth cheeks, bright humanlike eyes with visible whites and iris, clear nose and nostrils, "
            "defined lips, subtle smile, little shoulder area, orange collar visible, clean ivory background, "
            "original mascot host, gentle presenter look, stylized 3D, non-photorealistic, not pixel art, no text, no watermark."
        ),
    ),
    CandidateSpec(
        candidate_id="候选C_round5_去玩偶化主持脸",
        label="候选C｜去玩偶化主持脸",
        design_goal="继续弱化玩偶感和贴图感，保留 inspired 色彩与服装。",
        prompt=(
            "vertical 9:16 portrait, original explainer host character, smooth cartoon face with realistic cartoon proportions, "
            "front-facing bust portrait, clear eyelids, iris, eyebrows, nose bridge, nostrils and lips, "
            "orange host outfit with minimal voxel-inspired trim, brown hair pulled away from face, "
            "professional but cute presenter feeling, cream clean background, stylized 3D portrait, "
            "not photorealistic, not realistic human, not toy doll, not plastic doll, no text, no watermark."
        ),
    ),
    CandidateSpec(
        candidate_id="候选D_round5_动漫数字人主持版",
        label="候选D｜动漫数字人主持版",
        design_goal="若前三张仍失败，进一步靠近 detect 友好的动漫数字人肖像。",
        prompt=(
            "vertical 9:16 portrait, original anime-style digital host mascot, strong centered front face, "
            "clean facial anatomy, visible whites of eyes, iris, pupils, eyelashes, eyebrows, defined nose and lips, "
            "warm gentle smile, orange presenter costume with tiny voxel-inspired details only on clothing edges, "
            "clean cream background, premium stylized character portrait, not photorealistic, not real person, no text, no watermark."
        ),
    ),
    CandidateSpec(
        candidate_id="候选E_round5_最强过检优先版",
        label="候选E｜最强过检优先版",
        design_goal="如果前四张都失败，再做一张几乎只服务 detect 的卡通数字人肖像。",
        prompt=(
            "vertical 9:16 portrait, original non-realistic digital host portrait optimized for talking-avatar detection, "
            "very large centered face, almost no body, symmetrical front view, smooth skin shading, visible sclera iris pupils, "
            "clear eyebrows, realistic-cartoon nose with nostrils, clear lips, neutral smile, no hair covering forehead or cheeks, "
            "small hint of orange collar only, ivory background, stylized but detection-friendly cartoon portrait, "
            "not photorealistic, not toy doll, no text, no watermark."
        ),
    ),
]


def ensure_dirs() -> None:
    for path in (BASE_DIR, ASSETS_DIR, DETECT_DIR, AUDIT_DIR, TMP_DIR, S2V_DIR, PREVIEW_DIR):
        path.mkdir(parents=True, exist_ok=True)


def resolve_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg
    bundled = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("缺少 ffmpeg，可先安装依赖或补齐 ffmpeg-static。")


def run_command(args: list[str]) -> None:
    subprocess.run(args, check=True)


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_runtime_config() -> dict[str, Any]:
    bundle = load_formal_config(FORMAL_EXAMPLE_CONFIG_PATH, DEFAULT_FORMAL_LOCAL_CONFIG_PATH)
    if not bundle["has_local_config"]:
        raise RuntimeError(f"缺少正式本地配置：{DEFAULT_FORMAL_LOCAL_CONFIG_PATH}")
    return bundle


def trim_audio_excerpt(source: pathlib.Path, destination: pathlib.Path, seconds: float) -> dict[str, Any]:
    if not source.exists():
        raise RuntimeError(f"缺少测试音频：{source}")
    with wave.open(str(source), "rb") as src:
        params = src.getparams()
        frame_rate = src.getframerate()
        frame_count = min(src.getnframes(), int(frame_rate * seconds))
        frames = src.readframes(frame_count)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(destination), "wb") as dst:
        dst.setparams(params)
        dst.writeframes(frames)
    return {
        "source_audio": str(source),
        "trimmed_audio": str(destination),
        "trim_seconds": round(frame_count / float(frame_rate), 3),
    }


def normalize_asset_for_review(source: pathlib.Path, destination: pathlib.Path) -> pathlib.Path:
    image = Image.open(source).convert("RGB")
    canvas = ImageOps.fit(image, (1080, 1920), method=Image.Resampling.LANCZOS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination)
    return destination


def build_model_override_config(config: dict[str, Any], model_name: str) -> dict[str, Any]:
    effective = copy.deepcopy(config)
    effective.setdefault("image_generation", {})
    effective["image_generation"]["enabled"] = True
    effective["image_generation"]["model"] = model_name
    effective["image_generation"]["style_profile"] = "host_round5_detect_friendly"
    effective["image_generation_pool"] = {
        "primary": {
            "label": f"Round5 {model_name}",
            "priority": 10,
            "enabled": True,
            "provider": effective.get("provider", {}).get("name"),
            "region": effective.get("provider", {}).get("region"),
            "api_key": effective.get("auth", {}).get("api_key"),
            "model": model_name,
            "style_profile": "host_round5_detect_friendly",
        }
    }
    return effective


def execute_wan27_image_generation(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    prompt: str,
    model_name: str,
) -> dict[str, Any]:
    effective = build_model_override_config(config, model_name)
    payload = {
        "model": model_name,
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}],
                }
            ]
        },
        "parameters": {
            "size": WAN27_SIZE,
            "n": 1,
            "watermark": False,
            "thinking_mode": True,
        },
    }
    result = _execute_aliyun_visual_generation_task(
        config=effective,
        output_dir=output_dir,
        segment_id=segment_id,
        asset_kind="image",
        create_relative_path="/services/aigc/image-generation/generation",
        payload=payload,
        result_url_extractor=_extract_aliyun_image_result_url,
        default_extension=".png",
    )
    result["model_name"] = model_name
    result["request_payload"] = {
        "model": model_name,
        "parameters": payload["parameters"],
    }
    return result


def generate_candidate_asset(
    *,
    config: dict[str, Any],
    candidate: CandidateSpec,
) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    success_result: dict[str, Any] | None = None
    for model_name in (WAN27_PRIMARY_MODEL, WAN27_FALLBACK_MODEL):
        result = execute_wan27_image_generation(
            config=config,
            output_dir=BASE_DIR,
            segment_id=f"{candidate.candidate_id}_{model_name}",
            prompt=candidate.prompt,
            model_name=model_name,
        )
        attempts.append(result)
        if result.get("status") == "success":
            success_result = result
            break
    record = {
        "candidate_id": candidate.candidate_id,
        "label": candidate.label,
        "design_goal": candidate.design_goal,
        "prompt": candidate.prompt,
        "attempts": attempts,
        "final_status": success_result.get("status") if success_result else attempts[-1].get("status", "failed"),
        "selected_model": success_result.get("model_name", "") if success_result else "",
        "raw_asset_path": "",
        "review_asset_path": "",
    }
    if success_result and success_result.get("asset_path"):
        raw_source = pathlib.Path(success_result["asset_path"])
        raw_asset = ASSETS_DIR / f"{candidate.candidate_id}_{success_result['model_name']}_raw.png"
        raw_asset.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(raw_source, raw_asset)
        review_asset = normalize_asset_for_review(
            raw_asset,
            ASSETS_DIR / f"{candidate.candidate_id}_{success_result['model_name']}_review_1080x1920.png",
        )
        record["raw_asset_path"] = str(raw_asset)
        record["review_asset_path"] = str(review_asset)
    return record


def execute_wan_s2v_detect(
    *,
    config: dict[str, Any],
    image_path: pathlib.Path,
) -> dict[str, Any]:
    detect_result = {
        "status": "not_started",
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "request_id": None,
        "source_image_url": None,
    }
    try:
        image_upload = _upload_file_to_aliyun_temp_storage(
            config=config,
            model=WAN_S2V_DETECT_MODEL,
            source_path=image_path,
        )
        detect_result["source_image_url"] = image_upload["oss_url"]
        payload = {
            "model": WAN_S2V_DETECT_MODEL,
            "input": {
                "image_url": image_upload["oss_url"],
            },
        }
        request = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/face-detect",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {config.get('auth', {}).get('api_key')}",
                "Content-Type": "application/json",
                "X-DashScope-OssResourceResolve": "enable",
            },
            method="POST",
        )
        response_payload = _urlopen_json_request(
            request,
            error_cls=VisualGenerationError,
            invalid_json_message="wan2.2-s2v-detect returned invalid JSON payload",
        )
        detect_result["request_id"] = response_payload.get("request_id")
        if response_payload.get("output", {}).get("check_pass") or response_payload.get("output", {}).get("pass"):
            detect_result["status"] = STATUS_SUCCESS
            detect_result["humanoid"] = response_payload.get("output", {}).get("humanoid")
            return detect_result
        message = response_payload.get("output", {}).get("message") or "wan2.2-s2v-detect did not pass."
        detect_result.update(
            {
                "status": STATUS_BLOCKED,
                "blocked_reason": message,
                "failure_reason": "wan_s2v_detect_rejected",
                "error_message": message,
                "humanoid": response_payload.get("output", {}).get("humanoid"),
            }
        )
        return detect_result
    except VisualGenerationError as exc:
        message = _sanitize_message(str(exc), config)
        status = STATUS_BLOCKED if _looks_like_timeout_message(message) else exc.status
        detect_result.update(
            {
                "status": status,
                "blocked_reason": message if status == STATUS_BLOCKED else "",
                "failure_reason": exc.failure_reason or "wan_s2v_detect_request_failed",
                "error_message": message,
            }
        )
        return detect_result


def execute_wan_s2v_probe(
    *,
    config: dict[str, Any],
    image_path: pathlib.Path,
    audio_path: pathlib.Path,
    segment_id: str,
) -> dict[str, Any]:
    detect_result = execute_wan_s2v_detect(config=config, image_path=image_path)
    if detect_result.get("status") != STATUS_SUCCESS:
        return {
            "status": detect_result.get("status", STATUS_BLOCKED),
            "task_id": None,
            "request_id": detect_result.get("request_id"),
            "asset_path": None,
            "source_url": None,
            "blocked_reason": detect_result.get("blocked_reason", ""),
            "failure_reason": detect_result.get("failure_reason", ""),
            "error_message": detect_result.get("error_message", ""),
            "payload": {
                "model": WAN_S2V_MODEL,
                "parameters": {
                    "resolution": S2V_RESOLUTION,
                },
            },
            "detect": detect_result,
            "input_image_url": detect_result.get("source_image_url", ""),
            "input_audio_url": "",
        }
    image_upload = _upload_file_to_aliyun_temp_storage(
        config=config,
        model=WAN_S2V_MODEL,
        source_path=image_path,
    )
    audio_upload = _upload_file_to_aliyun_temp_storage(
        config=config,
        model=WAN_S2V_MODEL,
        source_path=audio_path,
    )
    payload = {
        "model": WAN_S2V_MODEL,
        "input": {
            "image_url": image_upload["oss_url"],
            "audio_url": audio_upload["oss_url"],
        },
        "parameters": {
            "resolution": S2V_RESOLUTION,
        },
    }
    try:
        request = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/video-synthesis/",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {config.get('auth', {}).get('api_key')}",
                "Content-Type": "application/json",
                "X-DashScope-Async": "enable",
                "X-DashScope-OssResourceResolve": "enable",
            },
            method="POST",
        )
        create_payload = _urlopen_json_request(
            request,
            error_cls=VisualGenerationError,
            invalid_json_message="wan2.2-s2v create returned invalid JSON payload",
        )
        task_id = create_payload.get("output", {}).get("task_id")
        request_id = create_payload.get("request_id")
        if not task_id:
            raise VisualGenerationError(
                "wan2.2-s2v create response missing task_id",
                failure_reason="wan_s2v_task_id_missing",
            )
        task_payload = _poll_aliyun_visual_task(
            config=config,
            task_id=task_id,
            asset_kind="wan_s2v_video",
        )
        request_id = request_id or task_payload.get("request_id")
        result_url = _extract_aliyun_video_result_url(task_payload)
        if not result_url:
            raise VisualGenerationError(
                "wan2.2-s2v task succeeded but missing result url",
                failure_reason="wan_s2v_result_url_missing",
            )
        output_path = _build_visual_asset_output_path(
            output_dir=S2V_DIR,
            segment_id=segment_id,
            asset_kind="video",
            source_url=result_url,
            default_extension=".mp4",
        )
        _download_binary_file(
            result_url,
            output_path,
            error_cls=VisualGenerationError,
            empty_error_message="wan2.2-s2v video download is empty",
            empty_error_code="WanS2VEmptyVideo",
        )
        result = {
            "status": STATUS_SUCCESS,
            "task_id": task_id,
            "request_id": request_id,
            "asset_path": str(output_path),
            "source_url": result_url,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
        }
    except VisualGenerationError as exc:
        message = _sanitize_message(str(exc), config)
        is_timeout = _looks_like_timeout_message(message)
        status = STATUS_BLOCKED if is_timeout else exc.status
        result = {
            "status": status,
            "task_id": None,
            "request_id": None,
            "asset_path": None,
            "source_url": None,
            "blocked_reason": message if status == STATUS_BLOCKED else "",
            "failure_reason": exc.failure_reason or ("wan_s2v_timeout" if is_timeout else "wan_s2v_request_failed"),
            "error_message": message,
        }
    result["payload"] = {
        "model": WAN_S2V_MODEL,
        "parameters": payload["parameters"],
    }
    result["detect"] = detect_result
    result["input_image_url"] = image_upload["oss_url"]
    result["input_audio_url"] = audio_upload["oss_url"]
    return result


def extract_preview_frames(ffmpeg: str, video_path: pathlib.Path) -> list[str]:
    captures = [0.2, 0.9, 1.6, 2.3]
    outputs: list[str] = []
    for index, second in enumerate(captures, start=1):
        frame_path = PREVIEW_DIR / f"frame_{index:02d}.jpg"
        run_command(
            [
                ffmpeg,
                "-y",
                "-ss",
                f"{second:.2f}",
                "-i",
                str(video_path),
                "-frames:v",
                "1",
                "-update",
                "1",
                str(frame_path),
            ]
        )
        outputs.append(str(frame_path))
    return outputs


def build_contact_sheet(frame_paths: list[str], destination: pathlib.Path) -> str:
    images = [Image.open(path).convert("RGB") for path in frame_paths]
    width = 360
    height = 640
    canvas = Image.new("RGB", (width * len(images), height + 120), "#efe6da")
    for index, image in enumerate(images):
        fitted = ImageOps.fit(image, (width, height), method=Image.Resampling.LANCZOS)
        canvas.paste(fitted, (index * width, 0))
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, quality=92)
    return str(destination)


def round4_delta_direction() -> list[str]:
    return [
        "继续沿候选C方向走，但脸更像卡通数字人肖像，而不是玩偶 / 娃娃。",
        "继续放大脸部占比，减少肩颈和衣服面积，让 detect 更聚焦脸。",
        "继续增强眼白、虹膜、鼻孔、唇形可识别度。",
        "继续减少脸部方块切面和硬边，但把体素来源感保留在发型与服装上。",
    ]


def build_provider_snapshot(config: dict[str, Any], local_config_path: str | None) -> dict[str, Any]:
    return {
        "local_config_path": local_config_path,
        "provider": {
            "name": config.get("provider", {}).get("name"),
            "region": config.get("provider", {}).get("region"),
        },
        "current_image_candidates": _resolve_visual_candidate_pool(config, resource_kind="image_generation"),
        "round5_route": {
            "primary_image_model": WAN27_PRIMARY_MODEL,
            "fallback_image_model": WAN27_FALLBACK_MODEL,
            "s2v_detect_model": WAN_S2V_DETECT_MODEL,
            "s2v_model": WAN_S2V_MODEL,
        },
    }


def build_summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# 元素娃娃线 round5｜s2v detect 过检优化",
        "",
        "## round4_delta_direction",
        "",
    ]
    for item in summary["round4_delta_direction"]:
        lines.append(f"- {item}")
    lines.extend(["", "## asset_candidate_changes", ""])
    for candidate in summary["asset_candidates"]:
        lines.append(f"- `{candidate['candidate_id']}`")
        lines.append(f"  - `final_status = {candidate['final_status']}`")
        lines.append(f"  - `selected_model = {candidate.get('selected_model') or 'none'}`")
        lines.append(f"  - `design_goal = {candidate['design_goal']}`")
        lines.append(f"  - `review_asset_path = {candidate.get('review_asset_path') or 'missing'}`")
    lines.extend(["", "## detect_probe_result", ""])
    for detect in summary["detect_results"]:
        lines.append(f"- `{detect['candidate_id']}`")
        lines.append(f"  - `status = {detect['result'].get('status', '')}`")
        lines.append(f"  - `failure_reason = {detect['result'].get('failure_reason', '')}`")
        lines.append(f"  - `blocked_reason = {detect['result'].get('blocked_reason', '')}`")
    lines.extend(["", "## optional_s2v_smoke_test", ""])
    if summary.get("s2v_smoke_test"):
        smoke = summary["s2v_smoke_test"]
        lines.append(f"- `status = {smoke['result'].get('status', '')}`")
        lines.append(f"  - `video_path = {smoke['result'].get('asset_path', '') or 'missing'}`")
        lines.append(f"  - `contact_sheet = {smoke.get('contact_sheet', '') or 'not_generated'}`")
    else:
        lines.append("- `status = skipped`")
    return "\n".join(lines) + "\n"


def main() -> int:
    ensure_dirs()
    ffmpeg = resolve_ffmpeg()
    bundle = load_runtime_config()
    config = bundle["config"]

    summary: dict[str, Any] = {
        "schema_version": "video_factory_host_motion_asset_gate_round5/v1",
        "provider_snapshot": build_provider_snapshot(config, bundle["local_config_path"]),
        "round4_delta_direction": round4_delta_direction(),
        "asset_candidates": [],
        "detect_results": [],
        "selected_detect_pass_candidate_id": "",
        "audio_probe": {},
        "s2v_smoke_test": None,
        "technical_validation": "blocked",
        "content_validation": "blocked",
    }

    audio_info = trim_audio_excerpt(SOURCE_AUDIO, TRIMMED_AUDIO, TRIM_SECONDS)
    summary["audio_probe"] = audio_info

    detect_pass_candidate: dict[str, Any] | None = None
    for candidate in CANDIDATES:
        asset_record = generate_candidate_asset(config=config, candidate=candidate)
        summary["asset_candidates"].append(asset_record)
        if asset_record["final_status"] != "success" or not asset_record["raw_asset_path"]:
            summary["detect_results"].append(
                {
                    "candidate_id": asset_record["candidate_id"],
                    "result": {
                        "status": "blocked",
                        "failure_reason": "asset_generation_failed",
                        "blocked_reason": "资产未成功生成，未进入 detect",
                        "error_message": "",
                    },
                }
            )
            continue
        detect_result = execute_wan_s2v_detect(
            config=config,
            image_path=pathlib.Path(asset_record["raw_asset_path"]),
        )
        detect_path = DETECT_DIR / f"{asset_record['candidate_id']}_detect.json"
        write_json(detect_path, detect_result)
        summary["detect_results"].append(
            {
                "candidate_id": asset_record["candidate_id"],
                "result": detect_result,
                "result_path": str(detect_path),
            }
        )
        if detect_result.get("status") == STATUS_SUCCESS:
            detect_pass_candidate = asset_record
            summary["selected_detect_pass_candidate_id"] = asset_record["candidate_id"]
            break

    if detect_pass_candidate is None:
        summary["technical_validation"] = "blocked"
        summary["content_validation"] = "blocked"
        summary["stop_line_triggered"] = "all_round5_assets_failed_s2v_detect"
        write_json(SUMMARY_JSON, summary)
        SUMMARY_MD.write_text(build_summary_markdown(summary), encoding="utf-8")
        return 0

    smoke_result = execute_wan_s2v_probe(
        config=config,
        image_path=pathlib.Path(detect_pass_candidate["raw_asset_path"]),
        audio_path=TRIMMED_AUDIO,
        segment_id=detect_pass_candidate["candidate_id"],
    )
    smoke_record: dict[str, Any] = {
        "selected_candidate_id": detect_pass_candidate["candidate_id"],
        "result": smoke_result,
        "preview_frames": [],
        "contact_sheet": "",
    }
    if smoke_result.get("status") == STATUS_SUCCESS and smoke_result.get("asset_path"):
        preview_frames = extract_preview_frames(ffmpeg, pathlib.Path(smoke_result["asset_path"]))
        smoke_record["preview_frames"] = preview_frames
        smoke_record["contact_sheet"] = build_contact_sheet(preview_frames, CONTACT_SHEET_PATH)
    summary["s2v_smoke_test"] = smoke_record
    summary["technical_validation"] = "passed_for_detect_gate"
    summary["content_validation"] = "blocked"
    if smoke_result.get("status") == STATUS_SUCCESS:
        summary["smoke_test_status"] = "success"
    else:
        summary["smoke_test_status"] = smoke_result.get("status", "skipped")

    write_json(SUMMARY_JSON, summary)
    SUMMARY_MD.write_text(build_summary_markdown(summary), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
