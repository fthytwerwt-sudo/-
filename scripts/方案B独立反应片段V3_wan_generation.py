from __future__ import annotations

import copy
import json
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
    _sanitize_message,
    load_formal_config,
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
SUMMARY_PATH = OUT_DIR / "run_summary.json"
ATTEMPTS_PATH = OUT_DIR / "wan_generation_attempts_sanitized.json"

SOURCE_VIDEO = ROOT / "dist" / "latest_review_pack" / "middle_preview.mp4"
SOURCE_START_SECONDS = 1.6
SEGMENT_A_SECONDS = 4.5
REACTION_SECONDS = 1.5
SEGMENT_B_SECONDS = 9.0
FPS = 25

IMAGE_MODELS = ["wan2.7-image-pro", "wan2.7-image"]
VIDEO_MODEL = "wan2.7-i2v"

IMAGE_PROMPT = """Vertical 9:16 high quality anime-styled 3D cartoon reaction page, original cute AI guide character, big head small body, not a child, not a toy, polished commercial illustration quality.
The character is in a funny meltdown reaction: both hands holding head, one X-shaped eye, one spiral eye, huge open mouth, exaggerated but harmless face distortion, big collapse tears, sweat drops, small !? symbols above head, panicked posture.
No real person, no existing IP, no copyrighted character, no meme copy, no platform UI, no TikTok UI, no logos, no letters on the body, absolutely no "AI" text on the chest or clothing.
Background is a standalone orange and yellow comic burst reaction page with dynamic speed lines and punchy visual energy, not a screen recording overlay, not a transparent sticker, not a corner sticker.
Include exactly two large readable Chinese text lines near the top: 方案很满 / 用起来空. Bold rounded display lettering, high contrast, clean composition.
Full page reaction insert, cinematic social video quality, 720x1280 composition, vivid but not low-fidelity, no watermark."""

VIDEO_PROMPT = """Animate this standalone reaction page as a short punchline clip. Keep the same original AI guide character and composition. Add a quick bounce, tiny shake, moving speed lines, tears wobbling, and text popping slightly. No camera travel, no new logos, no platform UI, no recording overlay. Keep the Chinese text readable: 方案很满 / 用起来空. Funny meltdown reaction, energetic but clean."""


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def load_config() -> dict[str, Any]:
    bundle = load_formal_config(FORMAL_EXAMPLE_CONFIG_PATH, DEFAULT_FORMAL_LOCAL_CONFIG_PATH)
    if not bundle["has_local_config"]:
        raise RuntimeError(f"missing local config: {DEFAULT_FORMAL_LOCAL_CONFIG_PATH}")
    return bundle["config"]


def has_secret(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "SET_IN_LOCAL_FILE" not in value


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
    for model in IMAGE_MODELS:
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
            }
            break
    return {"result": final_result, "attempts": attempts}, source_url


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
            "size": "720*1280",
            "duration": 2,
            "prompt_extend": True,
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


def ffmpeg_probe(ffmpeg: str, path: pathlib.Path) -> str:
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", str(path)],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return proc.stdout


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {
        "task": "方案B独立反应片段V3",
        "status": "started",
        "fact_source": {
            "round": "round34_中段双展示提示卡_正反分段提示修复",
            "base_video": str(SOURCE_VIDEO),
        },
        "api_route": {
            "provider": "aliyun_bailian_dashscope",
            "image_models": IMAGE_MODELS,
            "video_model": VIDEO_MODEL,
            "local_config_path": str(DEFAULT_FORMAL_LOCAL_CONFIG_PATH),
        },
        "outputs": {},
        "verification": {},
    }
    attempts: dict[str, Any] = {"image_attempts": [], "video_attempt": None}
    try:
        config = load_config()
        api_key_present = has_secret(_nested_get(config, "auth", "api_key"))
        summary["api_route"]["api_key_present"] = api_key_present
        if not api_key_present:
            summary["status"] = "blocked"
            summary["blocked_reason"] = "missing_auth_api_key"
            write_json(SUMMARY_PATH, summary)
            return 2

        image_outcome, seed_url = generate_static_image(config)
        attempts["image_attempts"] = image_outcome["attempts"]
        summary["image_generation"] = {
            k: v
            for k, v in image_outcome["result"].items()
            if k not in {"source_url"}
        }
        if image_outcome["result"].get("status") != STATUS_SUCCESS or not seed_url:
            summary["status"] = "blocked"
            summary["blocked_reason"] = "image_generation_failed"
            write_json(ATTEMPTS_PATH, attempts)
            write_json(SUMMARY_PATH, summary)
            return 3

        video_outcome = generate_reaction_video(config, seed_url)
        attempts["video_attempt"] = video_outcome["attempt"]
        summary["video_generation"] = {
            k: v
            for k, v in video_outcome["result"].items()
            if k not in {"source_url"}
        }
        if video_outcome["result"].get("status") != STATUS_SUCCESS:
            summary["status"] = "blocked"
            summary["blocked_reason"] = "video_generation_failed"
            write_json(ATTEMPTS_PATH, attempts)
            write_json(SUMMARY_PATH, summary)
            return 4

        ffmpeg = resolve_ffmpeg()
        normalize_reaction_clip(ffmpeg)
        assemble_preview(ffmpeg)
        make_contact_sheet(ffmpeg)
        preview_size = PREVIEW_PATH.stat().st_size
        reaction_size = REACTION_CLIP_PATH.stat().st_size
        summary["status"] = "generated_pending_review"
        summary["outputs"] = {
            "static_reaction_page": str(STATIC_IMAGE_PATH),
            "raw_static_reaction_page": str(RAW_IMAGE_PATH),
            "reaction_clip": str(REACTION_CLIP_PATH),
            "raw_reaction_clip": str(RAW_REACTION_CLIP_PATH),
            "preview_video": str(PREVIEW_PATH),
            "contact_sheet": str(CONTACT_SHEET_PATH),
            "attempts_sanitized": str(ATTEMPTS_PATH),
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
            "uses_round34_base": True,
            "reaction_clip_is_standalone_segment": True,
            "no_local_program_character_drawing": True,
        }
        write_json(ATTEMPTS_PATH, attempts)
        write_json(SUMMARY_PATH, summary)
        return 0
    except Exception as exc:  # noqa: BLE001 - sanitized handoff artifact for failed provider calls.
        try:
            sanitized_message = _sanitize_message(str(exc), locals().get("config", {}))
        except Exception:
            sanitized_message = str(exc)
        summary["status"] = "blocked"
        summary["blocked_reason"] = "exception"
        summary["error_message"] = sanitized_message
        write_json(ATTEMPTS_PATH, attempts)
        write_json(SUMMARY_PATH, summary)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
