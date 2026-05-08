from __future__ import annotations

import json
import pathlib
import shutil
import subprocess
import sys
import wave
from dataclasses import dataclass
from typing import Any

from PIL import Image, ImageDraw, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_api_demo_core import (
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    _execute_aliyun_liveportrait_detect,
    _execute_aliyun_liveportrait_video_generation,
    _execute_aliyun_wan_image_generation,
    _resolve_visual_candidate_pool,
    load_formal_config,
)


BASE_DIR = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "host_motion_asset_gate_round2"
)
ASSETS_DIR = BASE_DIR / "assets"
DETECT_DIR = BASE_DIR / "detect_probe"
LIVEPORTRAIT_DIR = BASE_DIR / "liveportrait_probe"
AUDIT_DIR = BASE_DIR / "audit"
TMP_DIR = BASE_DIR / "tmp"

SOURCE_AUDIO = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "tts"
    / "seg01_hook.wav"
)
TRIMMED_AUDIO = LIVEPORTRAIT_DIR / "audio_hook_excerpt_3p4s.wav"
LIVEPORTRAIT_PREVIEW_DIR = LIVEPORTRAIT_DIR / "preview_frames"
CONTACT_SHEET_PATH = AUDIT_DIR / "liveportrait_contact_sheet.jpg"
SUMMARY_JSON = AUDIT_DIR / "asset_gate_summary.json"
SUMMARY_MD = AUDIT_DIR / "最小闸门审计_round2.md"

TRIM_SECONDS = 3.4


@dataclass(frozen=True)
class CandidateSpec:
    candidate_id: str
    label: str
    prompt: str
    design_goal: str


CANDIDATES = [
    CandidateSpec(
        candidate_id="候选A_正脸主持娃娃",
        label="候选A｜正脸主持娃娃",
        design_goal="优先保证正脸识别、五官清楚、detect 友好。",
        prompt=(
            "9:16 vertical portrait, a cute original host doll facing the camera, upper body close-up, "
            "clear frontal face, large open eyes, visible nose, clear mouth, gentle smile, head larger than body, "
            "orange top, dark blue lower clothing, warm brown hair, soft studio light, clean beige background, "
            "high-quality stylized 3D mascot render, original character, inspired by voxel aesthetics only, "
            "subtle blocky hair edges and costume panels, but the face is rounded and human-face-friendly, "
            "not realistic human, not photorealistic, no text, no props, no watermark, centered composition."
        ),
    ),
    CandidateSpec(
        candidate_id="候选B_软体素主持娃娃",
        label="候选B｜软体素主持娃娃",
        design_goal="保留更强的体素来源感，但仍把脸做成人脸友好的主持娃娃。",
        prompt=(
            "9:16 vertical portrait, adorable original guide doll host, front-facing half-body portrait, "
            "clear symmetrical face, big bright eyes, visible nose bridge, small clear lips, cute presenter expression, "
            "soft 2.5D / stylized 3D illustration quality, original Minecraft-inspired vibe without copying any official assets, "
            "voxel-inspired costume blocks, square silhouette hints, orange hoodie, brown hair, soft cream background, "
            "face occupies a large portion of the frame, clean portrait for lip-sync detect, no text, no props, no watermark."
        ),
    ),
]


def ensure_dirs() -> None:
    for path in (
        BASE_DIR,
        ASSETS_DIR,
        DETECT_DIR,
        LIVEPORTRAIT_DIR,
        AUDIT_DIR,
        TMP_DIR,
        LIVEPORTRAIT_PREVIEW_DIR,
    ):
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


def build_provider_snapshot(config: dict[str, Any], local_config_path: str | None) -> dict[str, Any]:
    return {
        "local_config_path": local_config_path,
        "provider": {
            "name": config.get("provider", {}).get("name"),
            "region": config.get("provider", {}).get("region"),
        },
        "image_generation": {
            "enabled": config.get("image_generation", {}).get("enabled"),
            "model": config.get("image_generation", {}).get("model"),
            "candidates": _resolve_visual_candidate_pool(config, resource_kind="image_generation"),
        },
        "video_generation": {
            "enabled": config.get("video_generation", {}).get("enabled"),
            "model": config.get("video_generation", {}).get("model"),
            "candidates": _resolve_visual_candidate_pool(config, resource_kind="video_generation"),
        },
        "portrait_detect": {
            "enabled": config.get("portrait_detect", {}).get("enabled"),
            "model": config.get("portrait_detect", {}).get("model"),
        },
        "portrait_video_generation": {
            "enabled": config.get("portrait_video_generation", {}).get("enabled"),
            "model": config.get("portrait_video_generation", {}).get("model"),
        },
    }


def trim_audio_excerpt(source: pathlib.Path, destination: pathlib.Path, seconds: float) -> dict[str, Any]:
    if not source.exists():
        raise RuntimeError(f"缺少最小测试音频：{source}")
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


def copy_asset(source: pathlib.Path, destination: pathlib.Path) -> pathlib.Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination


def normalize_asset_for_review(source: pathlib.Path, destination: pathlib.Path) -> pathlib.Path:
    image = Image.open(source).convert("RGB")
    canvas = ImageOps.fit(image, (1080, 1920), method=Image.Resampling.LANCZOS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination)
    return destination


def generate_candidate_asset(
    *,
    config: dict[str, Any],
    candidate: CandidateSpec,
) -> dict[str, Any]:
    result = _execute_aliyun_wan_image_generation(
        config=config,
        output_dir=BASE_DIR,
        segment_id=candidate.candidate_id,
        prompt=candidate.prompt,
    )
    raw_output = pathlib.Path(result["asset_path"]) if result.get("asset_path") else None
    asset_record = {
        "candidate_id": candidate.candidate_id,
        "label": candidate.label,
        "design_goal": candidate.design_goal,
        "prompt": candidate.prompt,
        "image_generation": result,
        "raw_asset_path": "",
        "review_asset_path": "",
    }
    if result.get("status") == "success" and raw_output is not None and raw_output.exists():
        raw_asset = copy_asset(raw_output, ASSETS_DIR / f"{candidate.candidate_id}_raw.png")
        review_asset = normalize_asset_for_review(
            raw_asset,
            ASSETS_DIR / f"{candidate.candidate_id}_review_1080x1920.png",
        )
        asset_record["raw_asset_path"] = str(raw_asset)
        asset_record["review_asset_path"] = str(review_asset)
    return asset_record


def run_detect_probe(config: dict[str, Any], asset_record: dict[str, Any]) -> dict[str, Any]:
    image_path = pathlib.Path(asset_record["review_asset_path"] or asset_record["raw_asset_path"])
    if not image_path.exists():
        result = {
            "status": "blocked",
            "blocked_reason": "detect 输入资产不存在",
            "failure_reason": "detect_input_missing",
            "error_message": "detect 输入资产不存在",
        }
    else:
        result = _execute_aliyun_liveportrait_detect(config=config, image_path=image_path)
    path = DETECT_DIR / f"{asset_record['candidate_id']}_detect.json"
    write_json(path, result)
    return {
        "candidate_id": asset_record["candidate_id"],
        "image_path": str(image_path),
        "result_path": str(path),
        "result": result,
    }


def extract_liveportrait_preview_frames(ffmpeg: str, video_path: pathlib.Path) -> list[str]:
    captures = [0.25, 1.6, 3.0]
    outputs: list[str] = []
    for index, second in enumerate(captures, start=1):
        frame_path = LIVEPORTRAIT_PREVIEW_DIR / f"frame_{index:02d}.jpg"
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
                str(frame_path),
            ]
        )
        outputs.append(str(frame_path))
    return outputs


def build_contact_sheet(frame_paths: list[str], destination: pathlib.Path) -> str:
    images = [Image.open(path).convert("RGB") for path in frame_paths]
    width = 420
    height = 747
    canvas = Image.new("RGB", (width * len(images), height + 110), "#f2eadf")
    draw = ImageDraw.Draw(canvas)
    for index, image in enumerate(images):
        fitted = ImageOps.fit(image, (width, height), method=Image.Resampling.LANCZOS)
        canvas.paste(fitted, (index * width, 0))
        draw.rectangle((index * width, height, (index + 1) * width, height + 110), fill="#fff8ef")
        draw.text((index * width + 24, height + 34), f"frame {index + 1}", fill="#5f4634")
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, quality=92)
    return str(destination)


def run_liveportrait_probe(
    *,
    config: dict[str, Any],
    ffmpeg: str,
    asset_record: dict[str, Any],
) -> dict[str, Any]:
    audio_info = trim_audio_excerpt(SOURCE_AUDIO, TRIMMED_AUDIO, TRIM_SECONDS)
    image_path = pathlib.Path(asset_record["review_asset_path"] or asset_record["raw_asset_path"])
    result = _execute_aliyun_liveportrait_video_generation(
        config=config,
        output_dir=LIVEPORTRAIT_DIR,
        segment_id=asset_record["candidate_id"],
        image_path=image_path,
        audio_path=TRIMMED_AUDIO,
    )
    result_path = LIVEPORTRAIT_DIR / f"{asset_record['candidate_id']}_liveportrait.json"
    write_json(result_path, result)
    preview_frames: list[str] = []
    contact_sheet = ""
    generation_path = pathlib.Path(result["generation"]["asset_path"]) if result.get("generation", {}).get("asset_path") else None
    if result.get("status") == "success" and generation_path is not None and generation_path.exists():
        preview_frames = extract_liveportrait_preview_frames(ffmpeg, generation_path)
        contact_sheet = build_contact_sheet(preview_frames, CONTACT_SHEET_PATH)
    return {
        "candidate_id": asset_record["candidate_id"],
        "audio_info": audio_info,
        "result_path": str(result_path),
        "result": result,
        "preview_frames": preview_frames,
        "contact_sheet": contact_sheet,
    }


def build_summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# 元素娃娃线 round2｜资产与 detect 闸门验证",
        "",
        "## connected_provider_recheck",
        "",
        f"- `已确认` 正式本地配置：`{summary['provider_snapshot']['local_config_path']}`",
        f"- `已确认` `image_generation.model = {summary['provider_snapshot']['image_generation']['model']}`",
        f"- `已确认` `video_generation.model = {summary['provider_snapshot']['video_generation']['model']}`",
        f"- `已确认` `portrait_detect.model = {summary['provider_snapshot']['portrait_detect']['model']}`",
        f"- `已确认` `portrait_video_generation.model = {summary['provider_snapshot']['portrait_video_generation']['model']}`",
        "",
        "## asset_candidates",
        "",
    ]
    for asset in summary["asset_candidates"]:
        lines.extend(
            [
                f"- `{asset['candidate_id']}`",
                f"  - `image_generation.status = {asset['image_generation'].get('status', '')}`",
                f"  - `review_asset_path = {asset.get('review_asset_path', '') or 'missing'}`",
            ]
        )
    lines.extend(["", "## detect_results", ""])
    for detect in summary["detect_results"]:
        result = detect["result"]
        lines.extend(
            [
                f"- `{detect['candidate_id']}`",
                f"  - `status = {result.get('status', '')}`",
                f"  - `blocked_reason = {result.get('blocked_reason', '')}`",
            ]
        )
    lines.extend(
        [
            "",
            "## liveportrait_probe",
            "",
            f"- `status = {summary['liveportrait_probe'].get('result', {}).get('status', 'skipped')}`",
            f"- `result_path = {summary['liveportrait_probe'].get('result_path', 'skipped')}`",
            f"- `contact_sheet = {summary['liveportrait_probe'].get('contact_sheet', '') or 'not_generated'}`",
            "",
            "## stop_line",
            "",
            f"- `ability_gate = {summary['ability_gate']}`",
            f"- `stop_line_triggered = {summary['stop_line_triggered']}`",
            "",
            "## note",
            "",
            "- `待验证` 本文件只记录自动执行结果；是否摆脱“图片动起来 / gif 感”，仍需基于导出视频与预览帧做人工判读。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    ensure_dirs()
    ffmpeg = resolve_ffmpeg()
    config_bundle = load_runtime_config()
    config = config_bundle["config"]

    summary: dict[str, Any] = {
        "schema_version": "video_factory_host_motion_asset_gate_round2/v1",
        "provider_snapshot": build_provider_snapshot(config, config_bundle["local_config_path"]),
        "asset_candidates": [],
        "detect_results": [],
        "liveportrait_probe": {},
        "ability_gate": "not_started",
        "stop_line_triggered": "",
    }

    image_generation_failed = False
    for candidate in CANDIDATES:
        asset_record = generate_candidate_asset(config=config, candidate=candidate)
        summary["asset_candidates"].append(asset_record)
        if asset_record["image_generation"].get("status") != "success":
            image_generation_failed = True

    if all(asset["image_generation"].get("status") != "success" for asset in summary["asset_candidates"]):
        summary["ability_gate"] = "blocked"
        summary["stop_line_triggered"] = "image_generation_unavailable_or_failed"
        write_json(SUMMARY_JSON, summary)
        SUMMARY_MD.write_text(build_summary_markdown(summary), encoding="utf-8")
        return 0

    detect_success_assets: list[dict[str, Any]] = []
    for asset in summary["asset_candidates"]:
        if asset["image_generation"].get("status") != "success":
            continue
        detect_record = run_detect_probe(config, asset)
        summary["detect_results"].append(detect_record)
        if detect_record["result"].get("status") == "success":
            detect_success_assets.append(asset)

    if not detect_success_assets:
        summary["ability_gate"] = "blocked"
        summary["stop_line_triggered"] = "all_detect_failed"
        write_json(SUMMARY_JSON, summary)
        SUMMARY_MD.write_text(build_summary_markdown(summary), encoding="utf-8")
        return 0

    selected_asset = detect_success_assets[0]
    liveportrait_probe = run_liveportrait_probe(
        config=config,
        ffmpeg=ffmpeg,
        asset_record=selected_asset,
    )
    summary["liveportrait_probe"] = liveportrait_probe
    if liveportrait_probe["result"].get("status") == "success":
        summary["ability_gate"] = "passed_for_asset_gate_pending_manual_verdict"
        summary["stop_line_triggered"] = ""
    else:
        summary["ability_gate"] = "blocked"
        summary["stop_line_triggered"] = "liveportrait_failed_after_detect_pass"

    if image_generation_failed and summary["ability_gate"] != "blocked":
        summary["partial_failure_note"] = "至少 1 个候选资产的 image_generation 未成功，但仍存在可继续验证的通过候选。"

    write_json(SUMMARY_JSON, summary)
    SUMMARY_MD.write_text(build_summary_markdown(summary), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
