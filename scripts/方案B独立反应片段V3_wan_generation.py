from __future__ import annotations

import argparse
import copy
import json
import os
import pathlib
import shutil
import subprocess
import sys
from typing import Any

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_api_demo_core import (
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    STATUS_SUCCESS,
    _execute_aliyun_visual_generation_task,
    _extract_aliyun_image_result_url,
    _extract_aliyun_video_result_url,
    _nested_get,
    _poll_aliyun_visual_task,
    _sanitize_message,
    load_formal_config,
)


OFFICIAL_HISTORY_CONFIG_PATH = (
    pathlib.Path.home() / ".config" / "video-factory" / "formal_api_demo.local.toml"
)
OUT_DIR = (
    ROOT
    / "dist"
    / "prototypes"
    / "20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3"
)
STATIC_IMAGE_PATH = OUT_DIR / "方案B独立反应页_static_reaction_page.png"
RAW_IMAGE_PATH = OUT_DIR / "方案B独立反应页_static_reaction_page_raw_from_wan.png"
RAW_REACTION_CLIP_PATH = OUT_DIR / "方案B独立反应片段_reaction_clip_raw_from_wan.mp4"
REACTION_CLIP_PATH = OUT_DIR / "方案B独立反应片段_reaction_clip.mp4"
PREVIEW_PATH = OUT_DIR / "方案B独立反应15秒预览_scheme_b_standalone_reaction_v3.mp4"
CONTACT_SHEET_PATH = OUT_DIR / "方案B独立反应15秒预览_contact_sheet.jpg"
BEFORE_AFTER_CONTACT_SHEET_PATH = OUT_DIR / "方案B独立反应15秒预览_before_after_contact_sheet.jpg"
PREVIEW_REPORT_PATH = OUT_DIR / "方案B独立反应V3说明_preview_report.md"
PROMPTS_PATH = OUT_DIR / "方案B独立反应V3_prompts.json"
SUMMARY_PATH = OUT_DIR / "run_summary.json"
ATTEMPTS_PATH = OUT_DIR / "wan_generation_attempts_sanitized.json"
PREFLIGHT_PATH = OUT_DIR / "official_config_preflight_sanitized.json"
IMAGE_RESULT_PATH = OUT_DIR / "image_generation_result_sanitized.json"

SOURCE_VIDEO = ROOT / "dist" / "latest_review_pack" / "middle_preview.mp4"
SOURCE_START_SECONDS = 1.6
SEGMENT_A_SECONDS = 4.5
REACTION_SECONDS = 1.5
SEGMENT_B_SECONDS = 9.0
FPS = 25

IMAGE_MODEL = "wan2.7-image-pro"
VIDEO_MODEL = "wan2.7-i2v"

IMAGE_PROMPT = """Vertical 9:16 high quality stylized 3D cartoon reaction page, original cute-but-not-childish digital guide mascot / tiny project host character, big head small body, polished commercial illustration quality, full page standalone insert.
The character is in a funny meltdown reaction: both hands holding head, one X-shaped eye, one spiral eye, huge open mouth, harmless exaggerated face squash, collapse tears, sweat drops, tiny abstract question mark and exclamation mark symbols above the head, panicked and helpless body language.
The character body and outfit must be completely plain and blank: no chest text, no shirt letters, no badge, no emblem, no logo, no English letters, no "AI", no visible words or marks anywhere on the character. Use a smooth simple mascot body instead of a labeled shirt.
No real person, no existing IP, no copyrighted character, no meme copy, no platform UI, no TikTok UI, no social app icons, no logos. The only text in the entire image should be the two Chinese punchline lines.
Background is a standalone orange and yellow burst reaction page with dynamic speed lines and punchy visual energy, not a screen recording overlay, not a transparent sticker, not a corner sticker.
Put two large Chinese punchline lines near the top in bold rounded lettering: 方案很满 / 用起来空. Keep the composition clean and readable.
Style keywords: premium 3D mascot illustration, expressive comedy reaction, original character, high detail clean rendering, vivid orange-yellow burst background, 720x1280 vertical social video insert, no watermark."""

VIDEO_PROMPT = """Animate this standalone reaction page as a short punchline clip. Keep the same original AI guide character and composition. Add a quick bounce, tiny shake, moving speed lines, tears wobbling, and text popping slightly. No camera travel, no new logos, no platform UI, no recording overlay. Keep the Chinese text readable: 方案很满 / 用起来空. Funny meltdown reaction, energetic but clean."""


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="方案 B 独立 reaction V3 万相生成与装配")
    parser.add_argument(
        "--mode",
        choices=["image", "video-preview"],
        default="image",
        help="image 只做 preflight + wan2.7-image-pro；video-preview 复用已生成静态图继续 i2v 和 15 秒预览。",
    )
    parser.add_argument(
        "--local-config",
        type=pathlib.Path,
        default=OFFICIAL_HISTORY_CONFIG_PATH,
        help="显式指定历史成功 DashScope 本地配置；默认使用 ~/.config/video-factory/formal_api_demo.local.toml。",
    )
    return parser


def resolve_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg
    candidate = (
        pathlib.Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "python"
        / "lib"
        / "python3.12"
        / "site-packages"
        / "imageio_ffmpeg"
        / "binaries"
        / "ffmpeg-macos-aarch64-v7.1"
    )
    if candidate.exists():
        return str(candidate)
    raise RuntimeError("ffmpeg not found")


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def read_json_if_exists(path: pathlib.Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def secret_shape(value: Any) -> dict[str, Any]:
    if not has_secret(value):
        return {"present": False, "prefix_type": "none", "length_range": "none"}
    text = str(value).strip()
    if text.startswith("sk-"):
        prefix_type = "sk_dashscope_like"
    elif text.startswith("LTAI"):
        prefix_type = "aliyun_access_key_id_like"
    else:
        prefix_type = "unknown_or_nonstandard"
    length = len(text)
    if length < 20:
        length_range = "<20"
    elif length < 40:
        length_range = "20-39"
    elif length < 80:
        length_range = "40-79"
    else:
        length_range = ">=80"
    return {
        "present": True,
        "prefix_type": prefix_type,
        "length_range": length_range,
    }


def load_config_bundle(local_config_path: pathlib.Path) -> dict[str, Any]:
    resolved = local_config_path.expanduser().resolve()
    bundle = load_formal_config(FORMAL_EXAMPLE_CONFIG_PATH, resolved)
    if not bundle["has_local_config"]:
        raise RuntimeError(f"missing local config: {resolved}")
    bundle["resolved_local_config_path"] = str(resolved)
    return bundle


def has_secret(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "SET_IN_LOCAL_FILE" not in value


def build_preflight(bundle: dict[str, Any], expected_config_path: pathlib.Path) -> dict[str, Any]:
    config = bundle["config"]
    actual_path = pathlib.Path(str(bundle.get("resolved_local_config_path") or bundle.get("local_config_path")))
    expected_path = expected_config_path.expanduser().resolve()
    api_key_shape = secret_shape(_nested_get(config, "auth", "api_key"))
    preflight = {
        "status": "pass",
        "expected_config_path": str(expected_path),
        "actual_config_path": str(actual_path),
        "config_path_matches_expected": actual_path == expected_path,
        "has_local_config": bool(bundle.get("has_local_config")),
        "provider": _nested_get(config, "provider", "name"),
        "region": _nested_get(config, "provider", "region"),
        "auth_api_key": api_key_shape,
        "image_generation_model_from_config": _nested_get(config, "image_generation", "model"),
        "video_generation_model_from_config": _nested_get(config, "video_generation", "model"),
        "forced_image_model": IMAGE_MODEL,
        "forced_video_model": VIDEO_MODEL,
        "official_i2v_reference": {
            "url": "https://help.aliyun.com/zh/model-studio/image-to-video-general-api-reference",
            "endpoint": "/services/aigc/video-generation/video-synthesis",
            "media_type": "first_frame",
            "parameter_resolution": "720P",
            "duration_range_seconds": "[2,15]",
        },
        "env_FORMAL_API_DEMO_LOCAL_CONFIG_set": bool(os.environ.get("FORMAL_API_DEMO_LOCAL_CONFIG")),
        "key_leakage": False,
    }
    failures: list[str] = []
    if actual_path != expected_path:
        failures.append("config_path_not_applied")
    if preflight["provider"] != "aliyun_bailian":
        failures.append("provider_not_aliyun_bailian")
    if not api_key_shape["present"]:
        failures.append("auth_api_key_missing")
    if api_key_shape["prefix_type"] != "sk_dashscope_like":
        failures.append("auth_api_key_not_dashscope_like")
    if failures:
        preflight["status"] = "blocked"
        preflight["failures"] = failures
    else:
        preflight["failures"] = []
    return preflight


def image_config_for(config: dict[str, Any], model: str) -> dict[str, Any]:
    effective = copy.deepcopy(config)
    effective.setdefault("provider", {})["name"] = "aliyun_bailian"
    effective.setdefault("image_generation", {})
    effective["image_generation"]["enabled"] = True
    effective["image_generation"]["model"] = model
    effective["image_generation"]["style_profile"] = "scheme_b_full_page_reaction_v3"
    return effective


def video_config_for(config: dict[str, Any]) -> dict[str, Any]:
    effective = copy.deepcopy(config)
    effective.setdefault("provider", {})["name"] = "aliyun_bailian"
    effective.setdefault("video_generation", {})
    effective["video_generation"]["enabled"] = True
    effective["video_generation"]["model"] = VIDEO_MODEL
    effective["video_generation"]["style_profile"] = "scheme_b_full_page_reaction_v3"
    return effective


def generate_static_image(config: dict[str, Any]) -> tuple[dict[str, Any], str | None]:
    attempts: list[dict[str, Any]] = []
    source_url: str | None = None
    final_result: dict[str, Any] = {"status": "blocked", "failure_reason": "not_started"}
    model = IMAGE_MODEL
    effective = image_config_for(config, model)
    payload = {
        "model": model,
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": IMAGE_PROMPT}],
                }
            ]
        },
        "parameters": {
            "size": "1152*2048",
            "n": 1,
            "watermark": False,
            "thinking_mode": True,
        },
    }
    result = _execute_aliyun_visual_generation_task(
        config=effective,
        output_dir=OUT_DIR,
        segment_id=f"scheme_b_v3_static_{model}",
        asset_kind="image",
        create_relative_path="/services/aigc/image-generation/generation",
        payload=payload,
        result_url_extractor=_extract_aliyun_image_result_url,
        default_extension=".png",
    )
    attempts.append(
        {
            "kind": "image",
            "model": model,
            "status": result.get("status"),
            "failure_reason": result.get("failure_reason"),
            "blocked_reason": result.get("blocked_reason"),
            "error_code": result.get("error_code"),
            "http_status_code": result.get("http_status_code"),
            "request_id": result.get("request_id"),
            "task_id": result.get("task_id"),
            "endpoint": "https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation",
        }
    )
    final_result = result
    if result.get("status") == STATUS_SUCCESS and result.get("asset_path"):
        generated = pathlib.Path(result["asset_path"])
        shutil.copyfile(generated, RAW_IMAGE_PATH)
        image = Image.open(generated).convert("RGB")
        fitted = ImageOps.fit(image, (720, 1280), method=Image.Resampling.LANCZOS)
        fitted.save(STATIC_IMAGE_PATH, quality=96)
        source_url = result.get("source_url")
        final_result = {
            **result,
            "selected_model": model,
            "asset_path": str(STATIC_IMAGE_PATH),
            "raw_asset_path": str(RAW_IMAGE_PATH),
            "image_size": list(fitted.size),
        }
    return {"result": final_result, "attempts": attempts}, source_url


def source_url_from_completed_image_task(config: dict[str, Any]) -> str:
    image_result = read_json_if_exists(IMAGE_RESULT_PATH, {})
    task_id = image_result.get("task_id")
    if not task_id:
        raise RuntimeError(f"missing image task_id in {IMAGE_RESULT_PATH}")
    task_payload = _poll_aliyun_visual_task(
        config=config,
        task_id=task_id,
        asset_kind="image",
    )
    source_url = _extract_aliyun_image_result_url(task_payload)
    if not source_url:
        raise RuntimeError("completed image task did not return source url")
    return source_url


def generate_reaction_video(config: dict[str, Any], seed_image_url: str) -> dict[str, Any]:
    effective = video_config_for(config)
    payload = {
        "model": VIDEO_MODEL,
        "input": {
            "prompt": VIDEO_PROMPT,
            "media": [
                {
                    "type": "first_frame",
                    "url": seed_image_url,
                }
            ],
        },
        "parameters": {
            "resolution": "720P",
            "duration": 2,
            "prompt_extend": True,
            "watermark": False,
        },
    }
    result = _execute_aliyun_visual_generation_task(
        config=effective,
        output_dir=OUT_DIR,
        segment_id="scheme_b_v3_reaction_clip_wan_i2v",
        asset_kind="video",
        create_relative_path="/services/aigc/video-generation/video-synthesis",
        payload=payload,
        result_url_extractor=_extract_aliyun_video_result_url,
        default_extension=".mp4",
    )
    sanitized = {
        "kind": "video",
        "model": VIDEO_MODEL,
        "status": result.get("status"),
        "failure_reason": result.get("failure_reason"),
        "blocked_reason": result.get("blocked_reason"),
        "error_code": result.get("error_code"),
        "http_status_code": result.get("http_status_code"),
        "request_id": result.get("request_id"),
        "task_id": result.get("task_id"),
    }
    if result.get("status") == STATUS_SUCCESS and result.get("asset_path"):
        generated = pathlib.Path(result["asset_path"])
        shutil.copyfile(generated, RAW_REACTION_CLIP_PATH)
        result = {
            **result,
            "selected_model": VIDEO_MODEL,
            "raw_asset_path": str(RAW_REACTION_CLIP_PATH),
        }
    return {"result": result, "attempt": sanitized}


def normalize_reaction_clip(ffmpeg: str) -> None:
    run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(RAW_REACTION_CLIP_PATH),
            "-t",
            str(REACTION_SECONDS),
            "-vf",
            f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            str(REACTION_CLIP_PATH),
        ]
    )


def make_source_segment(ffmpeg: str, start: float, duration: float, output: pathlib.Path) -> None:
    run(
        [
            ffmpeg,
            "-y",
            "-ss",
            f"{start:.3f}",
            "-i",
            str(SOURCE_VIDEO),
            "-t",
            f"{duration:.3f}",
            "-vf",
            f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            output.as_posix(),
        ]
    )


def assemble_preview(ffmpeg: str) -> None:
    segment_a = OUT_DIR / "tmp_录屏片段A_negative_before.mp4"
    segment_b = OUT_DIR / "tmp_录屏片段B_mainline_after.mp4"
    concat_list = OUT_DIR / "tmp_concat_list.txt"
    make_source_segment(ffmpeg, SOURCE_START_SECONDS, SEGMENT_A_SECONDS, segment_a)
    make_source_segment(
        ffmpeg,
        SOURCE_START_SECONDS + SEGMENT_A_SECONDS,
        SEGMENT_B_SECONDS,
        segment_b,
    )
    concat_list.write_text(
        "\n".join(
            [
                f"file '{segment_a.as_posix()}'",
                f"file '{REACTION_CLIP_PATH.as_posix()}'",
                f"file '{segment_b.as_posix()}'",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    run(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(PREVIEW_PATH),
        ]
    )
    for temp_path in (segment_a, segment_b, concat_list):
        temp_path.unlink(missing_ok=True)


def make_contact_sheet(ffmpeg: str) -> None:
    frame_dir = OUT_DIR / "contact_frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    times = [0.8, 3.8, 4.65, 5.35, 6.2, 9.6, 11.4, 14.4]
    frames: list[pathlib.Path] = []
    for index, timestamp in enumerate(times):
        out = frame_dir / f"frame_{index:02d}_{timestamp:.2f}s.jpg"
        run(
            [
                ffmpeg,
                "-y",
                "-ss",
                f"{timestamp:.3f}",
                "-i",
                str(PREVIEW_PATH),
                "-frames:v",
                "1",
                "-update",
                "1",
                "-q:v",
                "2",
                str(out),
            ]
        )
        frames.append(out)
    thumbs = [Image.open(path).convert("RGB").resize((180, 320), Image.Resampling.LANCZOS) for path in frames]
    sheet = Image.new("RGB", (180 * 4, 320 * 2), "white")
    for index, thumb in enumerate(thumbs):
        x = (index % 4) * 180
        y = (index // 4) * 320
        sheet.paste(thumb, (x, y))
    sheet.save(CONTACT_SHEET_PATH, quality=92)
    shutil.rmtree(frame_dir, ignore_errors=True)


def make_before_after_contact_sheet(ffmpeg: str) -> None:
    frame_dir = OUT_DIR / "before_after_frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    frame_specs = [
        ("before_recording", PREVIEW_PATH, 3.6),
        ("standalone_reaction", PREVIEW_PATH, 5.0),
        ("after_recording", PREVIEW_PATH, 7.2),
    ]
    frames: list[pathlib.Path] = []
    for index, (label, source, timestamp) in enumerate(frame_specs):
        out = frame_dir / f"{index:02d}_{label}.jpg"
        run(
            [
                ffmpeg,
                "-y",
                "-ss",
                f"{timestamp:.3f}",
                "-i",
                str(source),
                "-frames:v",
                "1",
                "-update",
                "1",
                "-q:v",
                "2",
                str(out),
            ]
        )
        frames.append(out)
    thumbs = [Image.open(path).convert("RGB").resize((240, 426), Image.Resampling.LANCZOS) for path in frames]
    sheet = Image.new("RGB", (240 * 3, 426), "white")
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, (index * 240, 0))
    sheet.save(BEFORE_AFTER_CONTACT_SHEET_PATH, quality=92)
    shutil.rmtree(frame_dir, ignore_errors=True)


def ffmpeg_probe(ffmpeg: str, path: pathlib.Path) -> str:
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", str(path)],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return proc.stdout


def ffprobe_json(path: pathlib.Path) -> dict[str, Any]:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return {"available": False}
    proc = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration:stream=width,height,codec_type",
            "-of",
            "json",
            str(path),
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        return {"available": True, "error": proc.stderr.strip()}
    return {"available": True, "payload": json.loads(proc.stdout)}


def build_summary(mode: str, config_path: pathlib.Path) -> dict[str, Any]:
    return {
        "task": "方案B独立反应片段V3",
        "mode": mode,
        "status": "started",
        "fact_source": {
            "round": "round34_中段双展示提示卡_正反分段提示修复",
            "base_video": str(SOURCE_VIDEO),
        },
        "api_route": {
            "provider": "aliyun_bailian_dashscope",
            "image_model": IMAGE_MODEL,
            "video_model": VIDEO_MODEL,
            "expected_local_config_path": str(config_path.expanduser().resolve()),
            "actual_local_config_path": "",
        },
        "outputs": {},
        "verification": {},
        "state_boundary": {
            "full_mp4_modified": False,
            "latest_review_pack_modified": False,
            "content_validation_modified": False,
            "send_ready_modified": False,
            "final_scheme_b_position_confirmed": False,
        },
    }


def write_prompts() -> None:
    write_json(
        PROMPTS_PATH,
        {
            "image_model": IMAGE_MODEL,
            "video_model": VIDEO_MODEL,
            "image_prompt": IMAGE_PROMPT,
            "video_prompt": VIDEO_PROMPT,
        },
    )


def image_failure_block_reason(result: dict[str, Any]) -> str:
    if result.get("http_status_code") == 401 or result.get("error_code") == "HTTP401":
        return "blocked_correct_config_still_invalid"
    if result.get("http_status_code") in {403, 404}:
        return "blocked_model_permission_or_account_scope"
    return "image_generation_failed"


def write_preview_report(summary: dict[str, Any]) -> None:
    lines = [
        "# 方案 B 独立反应片段 V3 说明",
        "",
        "## 本轮性质",
        "",
        "- 本轮只是技术预览 / 生成链路验证，不代表方案 B 最终口径。",
        "- 本轮不代表 `content_validation` 通过，不代表 `send_ready` 更新。",
        "- 本轮不修改正式 `full.mp4`，不修改 `dist/latest_review_pack/`。",
        "",
        "## 配置预检",
        "",
        f"- `actual_config_path`: `{summary.get('preflight', {}).get('actual_config_path', '')}`",
        f"- `provider`: `{summary.get('preflight', {}).get('provider', '')}`",
        f"- `region`: `{summary.get('preflight', {}).get('region', '')}`",
        f"- `auth_api_key`: `{summary.get('preflight', {}).get('auth_api_key', {})}`",
        "",
        "## 生成状态",
        "",
        f"- `status`: `{summary.get('status', '')}`",
        f"- `blocked_reason`: `{summary.get('blocked_reason', '')}`",
        f"- `image_model`: `{IMAGE_MODEL}`",
        f"- `video_model`: `{VIDEO_MODEL}`",
        "",
        "## 输出",
        "",
    ]
    for key, value in summary.get("outputs", {}).items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## 边界",
            "",
            "- 未泄露 key。",
            "- 未提交本地私有配置。",
            "- 未本地绘图兜底。",
            "- 未改正式正片。",
            "- 未改 `send_ready`。",
        ]
    )
    PREVIEW_REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = build_parser().parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_prompts()
    expected_config = args.local_config.expanduser().resolve()
    summary: dict[str, Any] = build_summary(args.mode, expected_config)
    attempts: dict[str, Any] = {"image_attempts": [], "video_attempt": None}
    try:
        bundle = load_config_bundle(expected_config)
        config = bundle["config"]
        preflight = build_preflight(bundle, expected_config)
        write_json(PREFLIGHT_PATH, preflight)
        summary["preflight"] = preflight
        summary["api_route"]["actual_local_config_path"] = preflight["actual_config_path"]
        if preflight["status"] != "pass":
            summary["status"] = "blocked"
            summary["blocked_reason"] = "blocked_config_path_not_applied"
            summary["outputs"] = {
                "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
                "prompts": str(PROMPTS_PATH),
                "preview_report": str(PREVIEW_REPORT_PATH),
            }
            write_json(SUMMARY_PATH, summary)
            write_preview_report(summary)
            return 2

        if args.mode == "image":
            image_outcome, seed_url = generate_static_image(config)
            attempts["image_attempts"] = image_outcome["attempts"]
            summary["image_generation"] = {
                k: v
                for k, v in image_outcome["result"].items()
                if k not in {"source_url"}
            }
            if image_outcome["result"].get("status") != STATUS_SUCCESS or not seed_url:
                summary["status"] = "blocked"
                summary["blocked_reason"] = image_failure_block_reason(image_outcome["result"])
                summary["outputs"] = {
                    "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
                    "prompts": str(PROMPTS_PATH),
                    "attempts_sanitized": str(ATTEMPTS_PATH),
                    "preview_report": str(PREVIEW_REPORT_PATH),
                }
                write_json(ATTEMPTS_PATH, attempts)
                write_json(SUMMARY_PATH, summary)
                write_preview_report(summary)
                return 3

            summary["status"] = "partial_success_image_generated_pending_visual_check"
            summary["outputs"] = {
                "static_reaction_page": str(STATIC_IMAGE_PATH),
                "raw_static_reaction_page": str(RAW_IMAGE_PATH),
                "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
                "image_generation_result_sanitized": str(IMAGE_RESULT_PATH),
                "prompts": str(PROMPTS_PATH),
                "attempts_sanitized": str(ATTEMPTS_PATH),
                "preview_report": str(PREVIEW_REPORT_PATH),
            }
            summary["verification"] = {
                "static_image_exists": STATIC_IMAGE_PATH.exists(),
                "static_image_size": list(Image.open(STATIC_IMAGE_PATH).size),
                "no_local_program_character_drawing": True,
                "i2v_not_started_until_visual_check": True,
            }
            write_json(ATTEMPTS_PATH, attempts)
            write_json(
                IMAGE_RESULT_PATH,
                {
                    k: v
                    for k, v in image_outcome["result"].items()
                    if k not in {"source_url"}
                },
            )
            write_json(SUMMARY_PATH, summary)
            write_preview_report(summary)
            return 0

        attempts = read_json_if_exists(ATTEMPTS_PATH, attempts)
        summary["image_generation"] = read_json_if_exists(IMAGE_RESULT_PATH, {})
        seed_url = source_url_from_completed_image_task(config)
        video_outcome = generate_reaction_video(config, seed_url)
        attempts["video_attempt"] = video_outcome["attempt"]
        summary["video_generation"] = {
            k: v
            for k, v in video_outcome["result"].items()
            if k not in {"source_url"}
        }
        if video_outcome["result"].get("status") != STATUS_SUCCESS:
            summary["status"] = "partial_success_image_only"
            summary["blocked_reason"] = "video_generation_failed"
            summary["outputs"] = {
                "static_reaction_page": str(STATIC_IMAGE_PATH),
                "raw_static_reaction_page": str(RAW_IMAGE_PATH),
                "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
                "image_generation_result_sanitized": str(IMAGE_RESULT_PATH),
                "prompts": str(PROMPTS_PATH),
                "attempts_sanitized": str(ATTEMPTS_PATH),
                "preview_report": str(PREVIEW_REPORT_PATH),
            }
            write_json(ATTEMPTS_PATH, attempts)
            write_json(SUMMARY_PATH, summary)
            write_preview_report(summary)
            return 4

        ffmpeg = resolve_ffmpeg()
        normalize_reaction_clip(ffmpeg)
        provider_video_asset_path = summary["video_generation"].get("asset_path", "")
        summary["video_generation"]["provider_asset_path"] = provider_video_asset_path
        summary["video_generation"]["asset_path"] = str(REACTION_CLIP_PATH)
        assemble_preview(ffmpeg)
        make_contact_sheet(ffmpeg)
        make_before_after_contact_sheet(ffmpeg)
        preview_size = PREVIEW_PATH.stat().st_size
        reaction_size = REACTION_CLIP_PATH.stat().st_size
        summary["status"] = "technical_preview_generated"
        summary["outputs"] = {
            "static_reaction_page": str(STATIC_IMAGE_PATH),
            "raw_static_reaction_page": str(RAW_IMAGE_PATH),
            "reaction_clip": str(REACTION_CLIP_PATH),
            "raw_reaction_clip": str(RAW_REACTION_CLIP_PATH),
            "preview_video": str(PREVIEW_PATH),
            "contact_sheet": str(CONTACT_SHEET_PATH),
            "before_after_contact_sheet": str(BEFORE_AFTER_CONTACT_SHEET_PATH),
            "attempts_sanitized": str(ATTEMPTS_PATH),
            "image_generation_result_sanitized": str(IMAGE_RESULT_PATH),
            "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
            "prompts": str(PROMPTS_PATH),
            "preview_report": str(PREVIEW_REPORT_PATH),
        }
        summary["video_properties"] = {
            "preview_duration_seconds": 15.0,
            "preview_resolution": "720x1280",
            "preview_file_size_bytes": preview_size,
            "reaction_clip_duration_seconds": REACTION_SECONDS,
            "reaction_clip_resolution": "720x1280",
            "reaction_clip_file_size_bytes": reaction_size,
            "preview_audio": "silent_preview",
        }
        summary["edit_structure"] = {
            "segment_a": "round34 middle_preview recording excerpt",
            "reaction_clip": "standalone generated Wan i2v clip, inserted as its own segment",
            "segment_b": "round34 middle_preview mainline continuation",
            "is_overlay": False,
        }
        summary["verification"] = {
            "ffmpeg_preview_probe": ffmpeg_probe(ffmpeg, PREVIEW_PATH).splitlines()[:12],
            "ffmpeg_reaction_probe": ffmpeg_probe(ffmpeg, REACTION_CLIP_PATH).splitlines()[:12],
            "ffprobe_preview": ffprobe_json(PREVIEW_PATH),
            "ffprobe_reaction_clip": ffprobe_json(REACTION_CLIP_PATH),
            "uses_round34_base": True,
            "reaction_clip_is_standalone_segment": True,
            "no_local_program_character_drawing": True,
            "not_overlay_compositing": True,
        }
        write_json(ATTEMPTS_PATH, attempts)
        write_json(SUMMARY_PATH, summary)
        write_preview_report(summary)
        return 0
    except Exception as exc:  # noqa: BLE001 - sanitized handoff artifact for failed provider calls.
        try:
            sanitized_message = _sanitize_message(str(exc), locals().get("config", {}))
        except Exception:
            sanitized_message = str(exc)
        summary["status"] = "blocked"
        summary["blocked_reason"] = "exception"
        summary["error_message"] = sanitized_message
        summary["outputs"] = {
            "official_config_preflight_sanitized": str(PREFLIGHT_PATH),
            "prompts": str(PROMPTS_PATH),
            "attempts_sanitized": str(ATTEMPTS_PATH),
            "preview_report": str(PREVIEW_REPORT_PATH),
        }
        write_json(ATTEMPTS_PATH, attempts)
        write_json(SUMMARY_PATH, summary)
        write_preview_report(summary)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
