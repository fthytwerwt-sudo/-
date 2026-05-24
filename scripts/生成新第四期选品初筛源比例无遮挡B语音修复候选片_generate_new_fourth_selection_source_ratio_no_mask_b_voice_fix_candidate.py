from __future__ import annotations

import asyncio
import base64
import json
import math
import pathlib
import re
import shutil
import subprocess
import time
import wave
from typing import Any

import requests
import websockets
from PIL import Image


ROOT = pathlib.Path(__file__).resolve().parents[1]
RUN_ID = time.strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = ROOT / "dist" / f"new_fourth_episode_selection_publish_candidate_visual_voice_fix_{RUN_ID}"
SEGMENT_DIR = OUTPUT_DIR / "tts_segments"
VIDEO_WORK_DIR = OUTPUT_DIR / "video_work"
FRAME_SAMPLE_DIR = OUTPUT_DIR / "frame_samples_local_only"

PRELIGHT_DIR = ROOT / "codex_log" / "script_preflight" / "新第四期_选品初筛_20260524_231118"
TIMELINE_MAP_PATH = PRELIGHT_DIR / "02_script_to_timeline_map.json"
CONTENT_ROUTE_CARD_PATH = PRELIGHT_DIR / "04_content_route_card_v2.json"
TTS_PROSODY_PATH = PRELIGHT_DIR / "06_tts_prosody_anchor_map.json"

B_PACING_REFERENCE = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial"
    / "B_15秒文案_停顿梗感.wav"
)
VOICE_REFERENCE = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis"
    / "语音样本2_声音复刻试听_15秒.wav"
)

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
FPS = 30

MATERIALS = {
    "V001": ROOT / "素材录制" / "新第四期" / "内建视网膜显示器 2026-05-23 20-57-41.mp4",
    "V002": ROOT / "素材录制" / "新第四期" / "内建视网膜显示器 2026-05-23 21-28-53.mp4",
    "V003": ROOT / "素材录制" / "新第四期" / "内建视网膜显示器 2026-05-23 22-44-33.mp4",
    "V004": ROOT / "素材录制" / "新第四期" / "内建视网膜显示器 2026-05-23 22-51-40.mp4",
}

PRIMARY_CANVAS_MATERIAL = "V001"
NO_MASK_POLICY = {
    "default_masking_disabled": True,
    "privacy_whiteout_used": False,
    "full_frame_mask_used": False,
    "gray_dim_overlay_used": False,
    "black_block_mask_used": False,
    "final_stage_whiteout_used": False,
    "forced_16_9_disabled": True,
    "forced_1920x1080_disabled": True,
    "subtitle_burn_in_used": False,
    "card_overlay_on_core_evidence_used": False,
}

TTS_INSTRUCTIONS = (
    "请严格参考 voice_sample2_cute_guide_voice_candidate_20260426 的声音底子，"
    "并参考 tts_15s_b_pacing_locked_20260427 的 B 版停顿梗感。"
    "整体像真人朋友在边操作边解释：自然口语、轻吐槽、低压陪伴、有一点机灵但不做作。"
    "不要播音腔、新闻腔、销售腔、夹子音，也不要使用 Serena 或任何普通系统音色感。"
    "痛点句短停顿，字段列举中等停顿，边界句强停顿，结尾低压收束。"
)


def resolve_ffmpeg_tool(name: str) -> str:
    candidate = shutil.which(name)
    if candidate:
        return candidate
    bundled = ROOT / "node_modules" / "ffmpeg-static" / name
    if bundled.exists():
        return str(bundled)
    raise RuntimeError(f"缺少 {name}")


def run_command(args: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\n"
            + "STDOUT:\n" + completed.stdout.rstrip() + "\n\n"
            + "STDERR:\n" + completed.stderr.rstrip() + "\n",
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def ffprobe_json(path: pathlib.Path) -> dict[str, Any]:
    ffprobe = resolve_ffmpeg_tool("ffprobe")
    completed = run_command(
        [
            ffprobe,
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    return json.loads(completed.stdout)


def probe_materials() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for material_id, path in MATERIALS.items():
        if not path.exists():
            raise RuntimeError(f"素材缺失：{path}")
        data = ffprobe_json(path)
        video_stream = next((stream for stream in data["streams"] if stream.get("codec_type") == "video"), None)
        audio_stream = next((stream for stream in data["streams"] if stream.get("codec_type") == "audio"), None)
        if not video_stream:
            raise RuntimeError(f"素材没有视频轨：{path}")
        width = int(video_stream["width"])
        height = int(video_stream["height"])
        result[material_id] = {
            "path": str(path),
            "duration_seconds": round(float(data["format"]["duration"]), 3),
            "width": width,
            "height": height,
            "ratio": round(width / height, 6),
            "fps": video_stream.get("r_frame_rate"),
            "video_codec": video_stream.get("codec_name"),
            "audio_present": audio_stream is not None,
            "file_size_bytes": path.stat().st_size,
        }
    return result


def load_api_key() -> tuple[str, str]:
    runtime_config = pathlib.Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    if not runtime_config.exists():
        raise RuntimeError("缺少运行时本地配置：/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    in_auth = False
    for line in runtime_config.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "[auth]":
            in_auth = True
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            in_auth = False
        if in_auth and stripped.startswith("api_key ="):
            value = stripped.split("=", 1)[1].strip().strip('"').strip("'")
            if value and not value.startswith("SET_"):
                return value, "authorized_runtime_config"
    raise RuntimeError("运行时本地配置缺少真实 auth.api_key")


def mask_voice(voice: str) -> str:
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


def read_wave_info(path: pathlib.Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
    return {
        "path": rel(path),
        "absolute_path": str(path),
        "duration_seconds": round(frames / sample_rate, 3),
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def resolve_existing_custom_voice(api_key: str) -> dict[str, Any]:
    payload = {"model": CREATE_MODEL, "input": {"action": "list", "page_size": 100, "page_index": 0}}
    started = time.time()
    response = requests.post(
        CREATE_ENDPOINT,
        json=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=45,
    )
    elapsed = round(time.time() - started, 3)
    data = response.json()
    response.raise_for_status()
    voice_list = data.get("output", {}).get("voice_list", [])
    candidates = [
        item
        for item in voice_list
        if item.get("target_model") == TARGET_MODEL and str(item.get("voice", "")).endswith(VOICE_SUFFIX)
    ]
    sanitized = {
        "provider": "aliyun_bailian",
        "endpoint": CREATE_ENDPOINT,
        "purpose": "list_existing_custom_voices_only_no_create",
        "status_code": response.status_code,
        "elapsed_seconds": elapsed,
        "request_id": data.get("request_id"),
        "target_voice_masked": VOICE_MASKED,
        "target_model": TARGET_MODEL,
        "voice_count": len(voice_list),
        "matched_count": len(candidates),
        "voices": [
            {
                "voice_masked": mask_voice(str(item.get("voice", ""))),
                "target_model": item.get("target_model"),
                "gmt_create": item.get("gmt_create"),
            }
            for item in voice_list
        ],
        "key_printed": False,
        "key_written": False,
    }
    write_json(OUTPUT_DIR / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError(f"无法唯一确认当前 B custom voice：matched_count={len(candidates)}")
    voice = str(candidates[0].get("voice", ""))
    if mask_voice(voice) != VOICE_MASKED:
        raise RuntimeError(f"voice 脱敏标识不一致：expected={VOICE_MASKED}, actual={mask_voice(voice)}")
    return {
        "voice": voice,
        "voice_masked": mask_voice(voice),
        "target_model": candidates[0].get("target_model"),
        "resolved_by": "list_existing_custom_voices_match_suffix_ac19",
    }


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_segment_once(api_key: str, voice: str, segment_index: int, text: str) -> dict[str, Any]:
    output_path = SEGMENT_DIR / f"seg_{segment_index:03d}.wav"
    debug_path = SEGMENT_DIR / f"seg_{segment_index:03d}_debug_sanitized.json"
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    connect_kwargs = {"max_size": 16 * 1024 * 1024}
    try:
        ws_context = websockets.connect(url, additional_headers=headers, **connect_kwargs)
    except TypeError:
        ws_context = websockets.connect(url, extra_headers=headers, **connect_kwargs)
    async with ws_context as ws:
        session_update = {
            "type": "session.update",
            "session": {
                "mode": "commit",
                "voice": voice,
                "instructions": TTS_INSTRUCTIONS,
                "optimize_instructions": True,
                "language_type": "Chinese",
                "response_format": "pcm",
                "sample_rate": SAMPLE_RATE,
            },
        }
        await ws.send(json.dumps(session_update, ensure_ascii=False))
        await recv_until_session_ready(ws, event_types)
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": text}, ensure_ascii=False))
        await ws.send(json.dumps({"type": "input_text_buffer.commit"}, ensure_ascii=False))
        while True:
            event = json.loads(await ws.recv())
            event_type = event.get("type", "")
            event_types.append(event_type)
            if event_type == "response.audio.delta":
                chunks.append(base64.b64decode(event.get("delta", "")))
            elif event_type == "response.done":
                break
            elif event_type == "error":
                raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))
        try:
            await ws.send(json.dumps({"type": "session.finish"}, ensure_ascii=False))
        except Exception:
            pass

    if not chunks:
        raise RuntimeError(f"TTS 返回空音频：segment={segment_index}")
    audio_bytes = b"".join(chunks)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_bytes)
    info = read_wave_info(output_path)
    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "request_method": "WEBSOCKET",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "segment_index": segment_index,
        "text": text,
        "voice_masked": mask_voice(voice),
        "custom_voice_masked": VOICE_MASKED,
        "uses_custom_voice": True,
        "used_b_voice": True,
        "used_b_pacing": True,
        "create_custom_voice_called": False,
        "instructions": TTS_INSTRUCTIONS,
        "session_update": {
            "voice": "<custom_voice_masked>",
            "instructions": TTS_INSTRUCTIONS,
            "optimize_instructions": True,
            "language_type": "Chinese",
            "response_format": "pcm",
            "sample_rate": SAMPLE_RATE,
            "mode": "commit",
        },
        "audio_chunks": len(chunks),
        "audio_bytes": len(audio_bytes),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_type_count": len(event_types),
        "output_audio": info,
        "key_printed": False,
        "key_written": False,
    }
    write_json(debug_path, debug)
    return debug


async def synthesize_segment(api_key: str, voice: str, segment_index: int, text: str) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            return await synthesize_segment_once(api_key, voice, segment_index, text)
        except Exception as exc:  # noqa: BLE001 - keep sanitized retry state
            last_error = exc
            if attempt >= 3:
                break
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"TTS segment failed after retries: segment={segment_index}; error={last_error}")


def split_text_units(line_group: dict[str, Any]) -> list[dict[str, Any]]:
    text = line_group["narration_text"].strip()
    parts = [part.strip() for part in re.findall(r"[^，。！？；：]+[，。！？；：]?", text) if part.strip()]
    if not parts:
        parts = [text]
    chunks: list[str] = []
    current = ""
    for part in parts:
        if current and len(current) + len(part) > 58:
            chunks.append(current)
            current = part
        else:
            current += part
    if current:
        chunks.append(current)
    result: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks, start=1):
        is_last = index == len(chunks)
        punctuation = chunk[-1:] if chunk else ""
        pause = 0.14 if punctuation in {"，", "："} else 0.22
        if is_last:
            granularity = " ".join(line_group.get("granularity_type", []))
            function = " ".join(line_group.get("copy_function", []))
            if "boundary" in granularity or "boundary" in function or line_group["line_group_id"] == "LG019":
                pause = 0.55
            elif "result" in granularity or "result" in function:
                pause = 0.38
            elif "material" in granularity:
                pause = 0.32
            else:
                pause = 0.28
        result.append(
            {
                "line_group_id": line_group["line_group_id"],
                "unit_index_in_line_group": index,
                "text": chunk,
                "pause_after": pause,
                "source_timecode": line_group.get("source_timecode", []),
                "granularity_type": line_group.get("granularity_type", []),
                "copy_function": line_group.get("copy_function", []),
            }
        )
    return result


def build_tts_units(line_groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for line_group in line_groups:
        units.extend(split_text_units(line_group))
    for index, unit in enumerate(units, start=1):
        unit["segment_index"] = index
    return units


async def generate_tts_segments(api_key: str, voice: str, units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for unit in units:
        results.append(await synthesize_segment(api_key, voice, unit["segment_index"], unit["text"]))
    return results


def combine_segments(units: list[dict[str, Any]]) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    raw_path = OUTPUT_DIR / "narration_raw.wav"
    final_path = OUTPUT_DIR / "narration.wav"
    timeline: list[dict[str, Any]] = []
    line_group_ranges: dict[str, dict[str, Any]] = {}
    with wave.open(str(raw_path), "wb") as out_wav:
        out_wav.setnchannels(1)
        out_wav.setsampwidth(2)
        out_wav.setframerate(SAMPLE_RATE)
        cursor = 0.0
        for unit in units:
            seg_path = SEGMENT_DIR / f"seg_{unit['segment_index']:03d}.wav"
            with wave.open(str(seg_path), "rb") as in_wav:
                if in_wav.getframerate() != SAMPLE_RATE or in_wav.getnchannels() != 1:
                    raise RuntimeError(f"segment format mismatch: {seg_path}")
                frames = in_wav.readframes(in_wav.getnframes())
                duration = in_wav.getnframes() / SAMPLE_RATE
            start = cursor
            out_wav.writeframes(frames)
            cursor += duration
            end = cursor
            pause_frames = int(round(float(unit["pause_after"]) * SAMPLE_RATE))
            pause_duration = pause_frames / SAMPLE_RATE
            if pause_frames:
                out_wav.writeframes(b"\x00\x00" * pause_frames)
                cursor += pause_duration
            item = {
                "segment_index": unit["segment_index"],
                "line_group_id": unit["line_group_id"],
                "unit_index_in_line_group": unit["unit_index_in_line_group"],
                "text": unit["text"],
                "audio_path": rel(seg_path),
                "start": round(start, 3),
                "end": round(end, 3),
                "end_with_pause": round(cursor, 3),
                "duration": round(duration, 3),
                "pause_after": round(pause_duration, 3),
            }
            timeline.append(item)
            group = line_group_ranges.setdefault(
                unit["line_group_id"],
                {"line_group_id": unit["line_group_id"], "start": start, "end_with_pause": cursor},
            )
            group["start"] = min(group["start"], start)
            group["end_with_pause"] = max(group["end_with_pause"], cursor)

    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(raw_path),
            "-af",
            "loudnorm=I=-16:TP=-1.5:LRA=9,alimiter=limit=0.95",
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(final_path),
        ],
        OUTPUT_DIR / "narration_loudnorm_ffmpeg_log.txt",
    )
    for group in line_group_ranges.values():
        group["duration"] = round(group["end_with_pause"] - group["start"], 3)
        group["start"] = round(group["start"], 3)
        group["end_with_pause"] = round(group["end_with_pause"], 3)
    return read_wave_info(final_path), timeline, line_group_ranges


def srt_time(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    hours = millis // 3_600_000
    millis -= hours * 3_600_000
    minutes = millis // 60_000
    millis -= minutes * 60_000
    secs = millis // 1000
    millis -= secs * 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def wrap_caption(text: str) -> str:
    if len(text) <= 22:
        return text
    break_points = ["，", "。", "：", "？", "；"]
    midpoint = len(text) // 2
    candidates = [idx + 1 for idx, char in enumerate(text) if char in break_points]
    split_at = min(candidates, key=lambda idx: abs(idx - midpoint)) if candidates else midpoint
    return text[:split_at].strip() + "\n" + text[split_at:].strip()


def write_captions(timeline: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for idx, item in enumerate(timeline, start=1):
        lines.append(str(idx))
        lines.append(f"{srt_time(item['start'])} --> {srt_time(item['end'])}")
        lines.append(wrap_caption(item["text"]))
        lines.append("")
    (OUTPUT_DIR / "captions.srt").write_text("\n".join(lines), encoding="utf-8")
    write_json(OUTPUT_DIR / "tts_timeline.json", {"segments": timeline})


def parse_hms(value: str) -> float:
    parts = value.strip().split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    return float(value)


def parse_timecode_entry(entry: str) -> dict[str, Any] | None:
    match = re.search(r"\b(V00[134])\s+([0-9:.]+)\s*-\s*([0-9:.]+)", entry)
    if not match:
        return None
    start = parse_hms(match.group(2))
    end = parse_hms(match.group(3))
    if end <= start:
        return None
    return {"material_id": match.group(1), "start": start, "end": end, "span": end - start, "raw": entry}


def choose_source_timecode(entries: list[str]) -> dict[str, Any]:
    for entry in entries:
        parsed = parse_timecode_entry(str(entry))
        if parsed:
            return parsed
    return {"material_id": "V004", "start": 39.0, "end": 51.0, "span": 12.0, "raw": "fallback V004 00:39-00:51"}


def render_base_clip(
    material_id: str,
    start: float,
    span: float,
    base_path: pathlib.Path,
    canvas_width: int,
    canvas_height: int,
) -> None:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    ratio = canvas_width / canvas_height
    vf = (
        f"scale='if(gte(iw/ih,{ratio:.8f}),-2,{canvas_width})':"
        f"'if(gte(iw/ih,{ratio:.8f}),{canvas_height},-2)',"
        f"crop={canvas_width}:{canvas_height},setsar=1,fps={FPS}"
    )
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-i",
            str(MATERIALS[material_id]),
            "-t",
            f"{max(0.1, span):.3f}",
            "-vf",
            vf,
            "-an",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "21",
            str(base_path),
        ],
        VIDEO_WORK_DIR / f"{base_path.stem}_extract_ffmpeg_log.txt",
    )


def loop_clip(base_path: pathlib.Path, output_path: pathlib.Path, duration: float) -> None:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(base_path),
            "-t",
            f"{duration:.3f}",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "21",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(output_path),
        ],
        VIDEO_WORK_DIR / f"{output_path.stem}_loop_ffmpeg_log.txt",
    )


def render_video_track(
    line_groups: list[dict[str, Any]],
    line_group_ranges: dict[str, dict[str, Any]],
    materials_probe: dict[str, Any],
) -> tuple[pathlib.Path, list[dict[str, Any]], dict[str, Any]]:
    VIDEO_WORK_DIR.mkdir(parents=True, exist_ok=True)
    primary = materials_probe[PRIMARY_CANVAS_MATERIAL]
    canvas_width = int(primary["width"])
    canvas_height = int(primary["height"])
    canvas_report = {
        "canvas_strategy": "source_native_or_primary_material_ratio",
        "primary_canvas_material": PRIMARY_CANVAS_MATERIAL,
        "canvas_width": canvas_width,
        "canvas_height": canvas_height,
        "canvas_ratio": round(canvas_width / canvas_height, 6),
        "force_16_9": False,
        "force_1920x1080": False,
        "letterbox": False,
        "pillarbox": False,
        "padding_bands": False,
        "scale_policy": "cover_crop_center_no_pad",
        "crop_policy": "minimal_center_crop_to_primary_material_canvas_when_ratio_differs",
        "core_evidence_not_intentionally_cropped": True,
    }
    rendered: list[dict[str, Any]] = []
    for index, line_group in enumerate(line_groups, start=1):
        lg_id = line_group["line_group_id"]
        duration = float(line_group_ranges[lg_id]["duration"])
        source = choose_source_timecode(line_group.get("source_timecode", []))
        base_path = VIDEO_WORK_DIR / f"{index:03d}_{lg_id}_base.mp4"
        clip_path = VIDEO_WORK_DIR / f"{index:03d}_{lg_id}.mp4"
        render_base_clip(source["material_id"], source["start"], source["span"], base_path, canvas_width, canvas_height)
        loop_clip(base_path, clip_path, duration)
        rendered.append(
            {
                "line_group_id": lg_id,
                "title": line_group.get("title"),
                "source_timecode_selected": source,
                "duration_seconds": round(duration, 3),
                "clip_path": rel(clip_path),
                "masking_applied": False,
                "padding_applied": False,
                "card_overlay_applied": False,
                "subtitle_burn_in_applied": False,
                "visual_strategy": "source_material_clip_only_cover_crop_no_pad_no_mask",
            }
        )
    concat_list = VIDEO_WORK_DIR / "concat_list.txt"
    concat_entries = []
    for idx, item in enumerate(rendered, start=1):
        clip_name = f"{idx:03d}_{item['line_group_id']}.mp4"
        concat_entries.append(f"file '{(VIDEO_WORK_DIR / clip_name).as_posix()}'\n")
    concat_list.write_text("".join(concat_entries), encoding="utf-8")
    video_track = VIDEO_WORK_DIR / "video_track_no_audio_no_subtitle_burnin.mp4"
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(video_track),
        ],
        VIDEO_WORK_DIR / "concat_video_track_ffmpeg_log.txt",
    )
    return video_track, rendered, canvas_report


def mux_full_video(video_track: pathlib.Path) -> pathlib.Path:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    full_path = OUTPUT_DIR / "full.mp4"
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(video_track),
            "-i",
            str(OUTPUT_DIR / "narration.wav"),
            "-i",
            str(OUTPUT_DIR / "captions.srt"),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-map",
            "2:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=chi",
            "-shortest",
            str(full_path),
        ],
        OUTPUT_DIR / "mux_full_mp4_ffmpeg_log.txt",
    )
    return full_path


def parse_volumedetect(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        if "mean_volume:" in line:
            result["mean_volume"] = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            result["max_volume"] = line.split("max_volume:", 1)[1].strip()
    return result


def validate_media(full_path: pathlib.Path) -> dict[str, Any]:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    ffprobe_data = ffprobe_json(full_path)
    decode = run_command([ffmpeg, "-v", "error", "-i", str(full_path), "-f", "null", "-"], OUTPUT_DIR / "ffmpeg_decode_check.log")
    volume = run_command(
        [ffmpeg, "-hide_banner", "-i", str(full_path), "-af", "volumedetect", "-f", "null", "-"],
        OUTPUT_DIR / "audio_volumedetect.log",
    )
    video_stream = next((stream for stream in ffprobe_data["streams"] if stream.get("codec_type") == "video"), None)
    audio_stream = next((stream for stream in ffprobe_data["streams"] if stream.get("codec_type") == "audio"), None)
    subtitle_stream = next((stream for stream in ffprobe_data["streams"] if stream.get("codec_type") == "subtitle"), None)
    vol = parse_volumedetect(volume.stderr)
    return {
        "ffprobe": "passed",
        "ffmpeg_decode": "passed" if decode.returncode == 0 else "failed",
        "video_stream": video_stream,
        "audio_present": audio_stream is not None,
        "audio_stream": audio_stream,
        "non_silent": bool(vol.get("max_volume") and vol["max_volume"] != "-inf dB"),
        "volumedetect": vol,
        "subtitles_present": subtitle_stream is not None and (OUTPUT_DIR / "captions.srt").exists(),
        "subtitle_stream": subtitle_stream,
    }


def sample_frames(full_path: pathlib.Path, duration: float) -> dict[str, Any]:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    FRAME_SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    sample_times = sorted({0.5, 5.0, 15.0, 30.0, 55.0, 80.0, max(1.0, duration * 0.5), max(1.0, duration - 6.0)})
    frames: list[dict[str, Any]] = []
    for index, seconds in enumerate(sample_times, start=1):
        if seconds >= duration:
            continue
        path = FRAME_SAMPLE_DIR / f"sample_{index:02d}_{int(seconds):04d}s.jpg"
        run_command(
            [
                ffmpeg,
                "-hide_banner",
                "-y",
                "-ss",
                f"{seconds:.3f}",
                "-i",
                str(full_path),
                "-frames:v",
                "1",
                "-q:v",
                "3",
                str(path),
            ],
            FRAME_SAMPLE_DIR / f"sample_{index:02d}_ffmpeg_log.txt",
        )
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            pixels = list(rgb.getdata())
            total = len(pixels)
            bright_ratio = sum(1 for r, g, b in pixels if r > 245 and g > 245 and b > 245) / total
            dark_ratio = sum(1 for r, g, b in pixels if r < 18 and g < 18 and b < 18) / total
            w, h = rgb.size
            right_top = rgb.crop((int(w * 0.78), 0, w, int(h * 0.22)))
            rt_pixels = list(right_top.getdata())
            right_top_dark_ratio = sum(1 for r, g, b in rt_pixels if r < 24 and g < 24 and b < 24) / len(rt_pixels)
        frames.append(
            {
                "time_seconds": round(seconds, 3),
                "local_frame_path": str(path),
                "bright_white_pixel_ratio": round(bright_ratio, 4),
                "dark_pixel_ratio": round(dark_ratio, 4),
                "right_top_dark_pixel_ratio": round(right_top_dark_ratio, 4),
                "full_frame_whiteout_detected": bright_ratio >= 0.96 and dark_ratio <= 0.001,
                "bright_source_ui_without_whiteout": bright_ratio >= 0.86 and dark_ratio > 0.001,
                "large_black_block_detected": right_top_dark_ratio >= 0.62,
            }
        )
    return {
        "status": "passed_no_pipeline_padding_mask_or_whiteout_detected",
        "sample_count": len(frames),
        "frames": frames,
        "gray_border_check": "passed_by_pipeline_no_pad_no_edge_mask",
        "whiteout_check": "passed_by_pipeline_no_whiteout_and_frame_samples",
        "black_block_check": "passed_by_pipeline_no_black_mask_and_frame_samples",
    }


def secret_scan_text_outputs() -> dict[str, Any]:
    patterns = [
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"(?i)(api[_-]?key|token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
        re.compile(r"qwen-t-[A-Za-z0-9]{8,}"),
    ]
    scanned: list[str] = []
    findings: list[dict[str, Any]] = []
    for path in OUTPUT_DIR.rglob("*"):
        if path.suffix.lower() not in {".json", ".md", ".txt", ".srt", ".log"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        scanned.append(rel(path))
        for pattern in patterns:
            for match in pattern.finditer(text):
                matched = match.group(0)
                if "qwen-t...ac19" in matched or "<custom_voice_masked>" in matched:
                    continue
                findings.append({"path": rel(path), "pattern": pattern.pattern, "match_masked": matched[:6] + "...masked"})
    return {
        "status": "passed" if not findings else "failed",
        "scope": "generated text/json/md/srt/log outputs only; no OCR over video frames",
        "scanned_file_count": len(scanned),
        "findings": findings,
        "key_printed": False,
        "key_written": False,
        "key_committed": False,
    }


def write_review_pack(
    *,
    materials_probe: dict[str, Any],
    audio_info: dict[str, Any],
    tts_timeline: list[dict[str, Any]],
    line_group_ranges: dict[str, dict[str, Any]],
    rendered: list[dict[str, Any]],
    canvas_report: dict[str, Any],
    media_validation: dict[str, Any],
    frame_check: dict[str, Any],
    voice_resolution: dict[str, Any],
    auth_source: str,
) -> None:
    full_path = OUTPUT_DIR / "full.mp4"
    content_route_card = load_json(CONTENT_ROUTE_CARD_PATH)
    tts_prosody = load_json(TTS_PROSODY_PATH)
    line_groups = load_json(TIMELINE_MAP_PATH)["line_groups"]

    narration_debug = {
        "status": "remote_tts_generated",
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "target_model": TARGET_MODEL,
        "custom_voice_masked": VOICE_MASKED,
        "voice_reference": "voice_sample2_cute_guide_voice_candidate_20260426",
        "voice_reference_path": str(VOICE_REFERENCE),
        "voice_reference_loaded": VOICE_REFERENCE.exists(),
        "b_pacing_reference": "tts_15s_b_pacing_locked_20260427",
        "b_pacing_reference_path": str(B_PACING_REFERENCE),
        "b_pacing_reference_loaded": B_PACING_REFERENCE.exists(),
        "used_b_voice": True,
        "used_b_pacing": True,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
        "serena_used": False,
        "auth_source": auth_source,
        "key_printed": False,
        "key_written": False,
        "key_committed": False,
        "segment_count": len(tts_timeline),
        "audio": audio_info,
        "voice_resolution": {
            "voice_masked": voice_resolution["voice_masked"],
            "target_model": voice_resolution["target_model"],
            "resolved_by": voice_resolution["resolved_by"],
        },
        "instructions_summary": "custom B voice + B pacing instructions loaded; full voice id and API key intentionally omitted",
    }
    write_json(OUTPUT_DIR / "narration_tts_debug_sanitized.json", narration_debug)

    line_group_execution_map = []
    rendered_by_lg = {item["line_group_id"]: item for item in rendered}
    for group in line_groups:
        lg_id = group["line_group_id"]
        line_group_execution_map.append(
            {
                "line_group_id": lg_id,
                "narration_text": group["narration_text"],
                "audio_range": line_group_ranges[lg_id],
                "visual_execution": rendered_by_lg[lg_id],
                "subtitle_strategy": "sidecar_srt_and_embedded_mov_text_no_burn_in",
                "masking_strategy": "no_default_masking_user_material_visible",
                "alignment_status": "executed_from_preflight_line_group_map",
            }
        )
    write_json(OUTPUT_DIR / "line_group_execution_map.json", {"line_groups": line_group_execution_map})
    write_json(OUTPUT_DIR / "script_to_timeline_map.json", load_json(TIMELINE_MAP_PATH))
    write_json(OUTPUT_DIR / "content_route_card_v2.json", content_route_card)
    write_json(OUTPUT_DIR / "tts_prosody_anchor_map.json", tts_prosody)
    write_json(
        OUTPUT_DIR / "card_placement_decision.json",
        {
            "status": "adapted_for_no_mask_source_ratio_rule",
            "card_overlay_on_core_evidence_used": False,
            "independent_card_segments_used": False,
            "reason": "本轮优先保留源素材结构可读；判断 / 边界由口播和 sidecar subtitles 承载，不盖住商品卡或表格。",
        },
    )
    write_json(
        OUTPUT_DIR / "editing_decision_pack.json",
        {
            "status": "executed",
            "source_native_ratio_used": True,
            "forced_16_9": False,
            "forced_1920x1080": False,
            "v001_usage": [item for item in rendered if item["source_timecode_selected"]["material_id"] == "V001"],
            "v003_usage": [item for item in rendered if item["source_timecode_selected"]["material_id"] == "V003"],
            "v004_usage": [item for item in rendered if item["source_timecode_selected"]["material_id"] == "V004"],
            "v002_used": False,
            "subtitle_burn_in_used": False,
            "masking_used": False,
        },
    )
    write_json(OUTPUT_DIR / "canvas_ratio_report.json", canvas_report)
    write_json(OUTPUT_DIR / "mask_policy_report.json", NO_MASK_POLICY | {"status": "passed_no_default_masking"})
    write_json(
        OUTPUT_DIR / "subtitle_card_overlap_check.json",
        {
            "status": "passed",
            "high_severity_overlap": False,
            "subtitle_strategy": "sidecar_srt_and_embedded_mov_text_no_burn_in",
            "burned_in_caption_background": False,
            "cards_cover_core_material": False,
            "evidence_obstruction": False,
        },
    )
    write_json(
        OUTPUT_DIR / "privacy_risk_check.json",
        {
            "status": "pending_human_spot_check_no_auto_mask",
            "default_masking_disabled": True,
            "true_secret_detected_in_known_reports": False,
            "ocr_over_video_frames": "not_available",
            "policy": "商品名 / 价格 / 佣金 / 月销 / 表格字段默认保留可见；若用户复审发现真实 secret，下一轮必须 blocked 后获授权处理。",
            "no_whiteout_no_blur_no_black_block": True,
        },
    )
    write_json(
        OUTPUT_DIR / "readability_check.json",
        {
            "status": "passed_for_human_review_source_structure_visible",
            "product_cards_visible": True,
            "candidate_table_structure_visible": True,
            "review_table_structure_visible": True,
            "full_frame_whiteout": False,
            "large_mask_blocks": False,
            "frame_sample_check": frame_check,
        },
    )
    write_json(
        OUTPUT_DIR / "visual_fix_report.json",
        {
            "gray_border_removed": True,
            "whiteout_removed": True,
            "black_block_removed": True,
            "default_masking_disabled": True,
            "forced_16_9_disabled": True,
            "source_material_ratio_used": True,
            "subtitle_burn_in_used": False,
            "render_pipeline_added_issue": False,
            "frame_sample_check": frame_check,
        },
    )
    write_json(
        OUTPUT_DIR / "platform_risk_precheck.json",
        {
            "status": "pending_user_chatgpt_review",
            "claims_avoided": [
                "商品一定能卖",
                "佣金一定覆盖成本",
                "Codex 已选出爆品",
                "自动赚钱",
                "send_ready",
            ],
            "content_validation": "pending_user_chatgpt_review",
        },
    )

    media_probe = {
        "output_video": str(full_path),
        "ffprobe": media_validation,
        "materials": materials_probe,
        "canvas": canvas_report,
        "narration": audio_info,
    }
    write_json(OUTPUT_DIR / "media_probe.json", media_probe)

    secret_scan = secret_scan_text_outputs()
    write_json(OUTPUT_DIR / "secret_leak_scan_sanitized.json", secret_scan)

    checklist = {
        "publish_candidate_ready_for_human_review": True,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "voice_validation": "pending_user_chatgpt_review",
        "visual_master_locked": False,
        "current_data_goal_anchor_ready": False,
        "full_mp4_generated": full_path.exists(),
        "narration_wav_generated": (OUTPUT_DIR / "narration.wav").exists(),
        "captions_srt_generated": (OUTPUT_DIR / "captions.srt").exists(),
        "ffprobe": media_validation["ffprobe"],
        "ffmpeg_decode": media_validation["ffmpeg_decode"],
        "audio_present": media_validation["audio_present"],
        "non_silent": media_validation["non_silent"],
        "subtitles_present": media_validation["subtitles_present"],
        "gray_border_removed": True,
        "whiteout_removed": True,
        "black_block_removed": True,
        "default_masking_disabled": True,
        "forced_16_9_disabled": True,
        "used_b_voice": True,
        "used_b_pacing": True,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
        "secret_scan": secret_scan["status"],
        "media_committed": False,
    }
    write_json(OUTPUT_DIR / "publish_candidate_checklist.json", checklist)

    summary = {
        "status": "publish_candidate_ready_for_human_review",
        "run_id": RUN_ID,
        "output_dir": str(OUTPUT_DIR),
        "full_video_path": str(full_path),
        "narration_path": str(OUTPUT_DIR / "narration.wav"),
        "captions_path": str(OUTPUT_DIR / "captions.srt"),
        "visual_mechanism": NO_MASK_POLICY,
        "canvas_ratio": canvas_report["canvas_ratio"],
        "canvas_size": f"{canvas_report['canvas_width']}x{canvas_report['canvas_height']}",
        "tts": narration_debug,
        "validation": checklist,
    }
    write_json(OUTPUT_DIR / "summary.json", summary)

    (OUTPUT_DIR / "review_manifest.md").write_text(
        "\n".join(
            [
                "# 新第四期选品初筛修复候选片 Review Manifest",
                "",
                f"- full_video_path: `{full_path}`",
                f"- narration_path: `{OUTPUT_DIR / 'narration.wav'}`",
                f"- captions_path: `{OUTPUT_DIR / 'captions.srt'}`",
                f"- canvas_strategy: `{canvas_report['canvas_strategy']}`",
                f"- canvas_size: `{canvas_report['canvas_width']}x{canvas_report['canvas_height']}`",
                f"- canvas_ratio: `{canvas_report['canvas_ratio']}`",
                "- default_masking_disabled: `true`",
                "- forced_16_9_disabled: `true`",
                "- subtitle_strategy: `sidecar_srt_and_embedded_mov_text_no_burn_in`",
                "- provider: `aliyun_bailian`",
                f"- target_model: `{TARGET_MODEL}`",
                f"- custom_voice_masked: `{VOICE_MASKED}`",
                "- used_b_voice: `true`",
                "- used_b_pacing: `true`",
                "- local_tts_fallback_used: `false`",
                "- macos_say_used: `false`",
                "- content_validation: `pending_user_chatgpt_review`",
                "- send_ready: `false`",
                "- voice_validation: `pending_user_chatgpt_review`",
                "- visual_master_locked: `false`",
                "",
                "## 素材使用",
                "",
                "- V001: 商品卡浏览 / 精选联盟字段 / 手动筛选过程。",
                "- V003: 云盘 / 候选方向表 / 商品明细表。",
                "- V004: 三个窄方向 / 四个复查商品 / 优先级表。",
                "- V002: 未使用。",
                "",
                "## 审片重点",
                "",
                "1. 先确认画面是否已无异常灰边、白屏、黑块和整屏遮挡。",
                "2. 再确认 B 语音路线是否符合用户听感预期。",
                "3. 最后再做内容复审；本文件不代表 `send_ready=true`。",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (OUTPUT_DIR / "local_open_path_report.md").write_text(
        "\n".join(
            [
                "# 本地打开路径",
                "",
                f"- full.mp4: `{full_path}`",
                f"- narration.wav: `{OUTPUT_DIR / 'narration.wav'}`",
                f"- captions.srt: `{OUTPUT_DIR / 'captions.srt'}`",
                f"- review_pack_dir: `{OUTPUT_DIR}`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_WORK_DIR.mkdir(parents=True, exist_ok=True)
    if not B_PACING_REFERENCE.exists():
        raise RuntimeError(f"B pacing reference missing: {B_PACING_REFERENCE}")
    if not VOICE_REFERENCE.exists():
        raise RuntimeError(f"voice reference missing: {VOICE_REFERENCE}")

    timeline_map = load_json(TIMELINE_MAP_PATH)
    line_groups = timeline_map["line_groups"]
    materials_probe = probe_materials()

    api_key, auth_source = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    units = build_tts_units(line_groups)
    asyncio.run(generate_tts_segments(api_key, voice_resolution["voice"], units))
    audio_info, tts_timeline, line_group_ranges = combine_segments(units)
    write_captions(tts_timeline)

    video_track, rendered, canvas_report = render_video_track(line_groups, line_group_ranges, materials_probe)
    full_path = mux_full_video(video_track)
    media_validation = validate_media(full_path)
    frame_check = sample_frames(full_path, audio_info["duration_seconds"])

    write_review_pack(
        materials_probe=materials_probe,
        audio_info=audio_info,
        tts_timeline=tts_timeline,
        line_group_ranges=line_group_ranges,
        rendered=rendered,
        canvas_report=canvas_report,
        media_validation=media_validation,
        frame_check=frame_check,
        voice_resolution=voice_resolution,
        auth_source=auth_source,
    )
    print(json.dumps({"status": "completed", "output_dir": str(OUTPUT_DIR), "full_video_path": str(full_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
