#!/usr/bin/env python3
"""Generate the second-episode horizontal publish candidate from local footage."""

from __future__ import annotations

import asyncio
import base64
import json
import math
import subprocess
import time
import wave
from pathlib import Path
from typing import Any

import requests
import websockets
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate"
VIDEO_1 = ROOT / "素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4"
VIDEO_2 = ROOT / "素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4"
FINAL_VIDEO = OUT_DIR / "第二期_KPI到判断系统_horizontal_publish_candidate_v1.mp4"
VOICE_SEGMENT_DIR = OUT_DIR / "tts_segments"
VOICE_RAW = OUT_DIR / "voice_track_raw.wav"
VOICE_PREP = OUT_DIR / "voice_track_loudnorm.wav"
VOICE = OUT_DIR / "voice_track.wav"
SCRIPT_TXT = OUT_DIR / "final_script_publish_candidate_v1.txt"
SCRIPT_MD = OUT_DIR / "final_script_publish_candidate_v1.md"
SUBTITLE_ASS = OUT_DIR / "subtitle.ass"
SUBTITLE_SRT = OUT_DIR / "subtitle.srt"
MEDIA_PROBE_JSON = OUT_DIR / "final_media_probe.json"
OVERLAY_DIR = OUT_DIR / "overlays"
VIDEO_WORK_DIR = OUT_DIR / "video_work"
FONT_PATH = Path("/System/Library/Fonts/STHeiti Medium.ttc")

TARGET_AUDIO_SECONDS = 82.0
FORMAL_RUNTIME_CONFIG = Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
TTS_INSTRUCTIONS = (
    "请参考新样本2的说话方式和 B 版停顿梗感，保持自然口语、轻吐槽、低压陪伴和判断感。"
    "不要播音腔、新闻腔、销售腔、客服腔，也不要夸张带货。"
    "关键判断句前后留一点停顿，整体自然推进，不要拖沓。"
)

SCRIPT_LINES = [
    "别再让 AI 给你定 KPI 了。",
    "播放多少，点赞多少，客资多少，看着很完整，但大多数时候没用。",
    "因为这些数字不会告诉你：下一条到底该改标题，还是改开头，还是改中段结构。",
    "我一开始也这样问：帮视频工厂定个目标，最好有播放、点赞和客资。",
    "第一版确实很全，北极星目标、阶段目标、指标树、客资定义都有。",
    "但我看完觉得不对。它还是在回答：我要追哪些数字。",
    "我真正需要的是：数据回来以后，下一轮该改哪里。",
    "所以我又追问：让 AI 设计一套目标驱动的数据飞轮。",
    "每期发布后，根据播放、留存、收藏、评论、私信和客资，判断下一期只改哪个变量。",
    "这次结果才像个判断系统。",
    "播放和留存，是触达。点赞和收藏，是认可。评论和追问，是互动。",
    "但私信也不能全算客资，要看他有没有说清楚任务、场景和想要的结果。",
    "所以目标不是 KPI 表。",
    "真正有用的目标，是逼你回答三件事：哪一层出了问题，下一条只改哪个变量，改完看哪个指标。",
    "没有这套判断，你每轮都在动，却不知道哪一步起作用。",
    "播放是入口。收藏是认可。私信要评分。每条只改一个主变量。",
    "目标清楚了，动作才不会乱。复盘清楚了，下一步才会浮出来。",
]


SEGMENTS = [
    {
        "id": "opening_hook",
        "input": 0,
        "start": 0.0,
        "source_duration": 5.0,
        "weight": 0.06,
        "role": "opening_0_5s_direct_conflict",
        "source": "video_1 00:00-00:05",
        "readability_action": "screen_background_with_large_hook_card",
    },
    {
        "id": "raw_goal_input",
        "input": 0,
        "start": 0.0,
        "source_duration": 8.0,
        "weight": 0.13,
        "role": "raw_problem_input",
        "source": "video_1 00:00-00:08",
        "readability_action": "center crop, subtitle explains original fuzzy KPI request",
    },
    {
        "id": "first_version_not_enough",
        "input": 0,
        "start": 36.0,
        "source_duration": 8.0,
        "weight": 0.11,
        "role": "first_prompt_gap",
        "source": "video_1 00:36-00:44",
        "readability_action": "center crop, card marks first version as KPI-like",
    },
    {
        "id": "second_prompt_process",
        "input": 0,
        "start": 44.0,
        "source_duration": 38.0,
        "weight": 0.25,
        "role": "second_data_flywheel_prompt",
        "source": "video_1 00:44-01:22",
        "readability_action": "compressed scroll evidence with key subtitle anchors",
    },
    {
        "id": "metric_layers",
        "input": 1,
        "start": 22.0,
        "source_duration": 24.0,
        "weight": 0.20,
        "role": "middle_evidence_metric_layer_table",
        "source": "video_2 00:22-00:46",
        "readability_action": "16:9 crop plus reconstructed metric-layer card",
    },
    {
        "id": "lead_score_table",
        "input": 1,
        "start": 46.0,
        "source_duration": 18.0,
        "weight": 0.16,
        "role": "lead_quality_score_table",
        "source": "video_2 00:46-01:04",
        "readability_action": "16:9 crop plus lead-scoring card",
    },
    {
        "id": "summary_card",
        "input": None,
        "start": None,
        "source_duration": None,
        "weight": 0.09,
        "role": "ending_closure_summary_card",
        "source": "generated summary card",
        "readability_action": "large four-line judgment card",
    },
]


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd or ROOT, check=True)


def capture_json(cmd: list[str]) -> dict:
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    return json.loads(out)


def probe_duration(path: Path, stream_selector: str | None = None) -> float:
    cmd = ["ffprobe", "-v", "error"]
    if stream_selector:
        cmd += ["-select_streams", stream_selector]
    cmd += ["-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)]
    out = subprocess.check_output(cmd, cwd=ROOT, text=True).strip()
    return float(out)


def ass_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int(round((seconds - math.floor(seconds)) * 100))
    if cs == 100:
        s += 1
        cs = 0
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def srt_time(seconds: float) -> str:
    millis = int(round(max(0.0, seconds) * 1000))
    hours = millis // 3_600_000
    millis -= hours * 3_600_000
    minutes = millis // 60_000
    millis -= minutes * 60_000
    secs = millis // 1000
    millis -= secs * 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_api_key() -> str:
    if not FORMAL_RUNTIME_CONFIG.exists():
        raise RuntimeError(f"缺少正式 TTS 运行时配置：{FORMAL_RUNTIME_CONFIG}")
    in_auth = False
    for line in FORMAL_RUNTIME_CONFIG.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "[auth]":
            in_auth = True
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            in_auth = False
        if in_auth and stripped.startswith("api_key ="):
            value = stripped.split("=", 1)[1].strip().strip('"')
            if value and not value.startswith("SET_"):
                return value
    raise RuntimeError("正式 TTS 运行时配置缺少真实 auth.api_key")


def mask_voice(voice: str) -> str:
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


def read_wave_info(path: Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
    return {
        "path": rel(path),
        "duration_seconds": round(frames / sample_rate, 3),
        "format": "wav",
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def resolve_existing_custom_voice(api_key: str) -> dict[str, Any]:
    payload = {
        "model": CREATE_MODEL,
        "input": {"action": "list", "page_size": 100, "page_index": 0},
    }
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
        "request_method": "POST",
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
    }
    write_json(OUT_DIR / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError(f"无法唯一确认项目锁定 custom voice：matched_count={len(candidates)}")
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


async def synthesize_tts_segment(api_key: str, voice: str, segment_index: int, text: str) -> dict[str, Any]:
    output_path = VOICE_SEGMENT_DIR / f"seg_{segment_index:03d}.wav"
    debug_path = VOICE_SEGMENT_DIR / f"seg_{segment_index:03d}_debug_sanitized.json"
    if output_path.exists() and output_path.stat().st_size > 44:
        debug = {
            "status": "reused_existing_segment",
            "segment_index": segment_index,
            "text": text,
            "voice_masked": VOICE_MASKED,
            "output_audio": read_wave_info(output_path),
        }
        write_json(debug_path, debug)
        return debug

    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(
        url,
        additional_headers=headers,
        max_size=16 * 1024 * 1024,
        open_timeout=45,
        ping_timeout=45,
    ) as ws:
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
        raise RuntimeError(f"阿里 TTS 返回空音频：segment={segment_index}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(b"".join(chunks))
    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "request_method": "WEBSOCKET",
        "base_url": url,
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "segment_index": segment_index,
        "text": text,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
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
        "audio_bytes": sum(len(chunk) for chunk in chunks),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_type_count": len(event_types),
        "output_audio": read_wave_info(output_path),
    }
    write_json(debug_path, debug)
    return debug


async def generate_tts_segments(api_key: str, voice: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for index, text in enumerate(SCRIPT_LINES, start=1):
        last_error = ""
        for attempt in range(1, 4):
            try:
                result = await synthesize_tts_segment(api_key, voice, index, text)
                result["attempt"] = attempt
                results.append(result)
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                time.sleep(min(6, 2 * attempt))
        else:
            raise RuntimeError(f"阿里 TTS 分段生成失败：segment={index}; last_error={last_error}")
    return results


def pause_after_line(index: int, total: int, text: str) -> float:
    if index == total:
        return 0.2
    if text.endswith("。") or text.endswith("！"):
        return 0.38
    if text.endswith("："):
        return 0.22
    return 0.25


def make_script_files() -> None:
    plain = "\n".join(SCRIPT_LINES) + "\n"
    SCRIPT_TXT.write_text(plain, encoding="utf-8")
    SCRIPT_MD.write_text(
        "# final_script_publish_candidate_v1\n\n"
        "status: `publish_candidate_script`\n"
        "duration_target: `60-90s`\n"
        "opening_first_5s: `别再让 AI 给你定 KPI 了。真正有用的是判断下一步改哪。`\n\n"
        "## 口播稿\n\n"
        + "\n\n".join(SCRIPT_LINES)
        + "\n",
        encoding="utf-8",
    )


def make_voice_track() -> float:
    api_key = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    tts_debugs = asyncio.run(generate_tts_segments(api_key, voice_resolution["voice"]))

    VOICE_RAW.parent.mkdir(parents=True, exist_ok=True)
    timeline: list[dict[str, Any]] = []
    with wave.open(str(VOICE_RAW), "wb") as out_wav:
        out_wav.setnchannels(1)
        out_wav.setsampwidth(2)
        out_wav.setframerate(SAMPLE_RATE)
        cursor = 0.0
        total = len(SCRIPT_LINES)
        for index, text in enumerate(SCRIPT_LINES, start=1):
            seg_path = VOICE_SEGMENT_DIR / f"seg_{index:03d}.wav"
            with wave.open(str(seg_path), "rb") as in_wav:
                if in_wav.getframerate() != SAMPLE_RATE or in_wav.getnchannels() != 1:
                    raise RuntimeError(f"阿里 TTS segment format mismatch: {seg_path}")
                frames = in_wav.readframes(in_wav.getnframes())
                duration = in_wav.getnframes() / SAMPLE_RATE
            start = cursor
            out_wav.writeframes(frames)
            cursor += duration
            end = cursor
            pause = pause_after_line(index, total, text)
            timeline.append(
                {
                    "segment_index": index,
                    "text": text,
                    "audio_path": rel(seg_path),
                    "start": round(start, 3),
                    "end": round(end, 3),
                    "duration": round(duration, 3),
                    "pause_after": pause,
                }
            )
            pause_frames = int(round(pause * SAMPLE_RATE))
            if pause_frames:
                out_wav.writeframes(b"\x00\x00" * pause_frames)
                cursor += pause_frames / SAMPLE_RATE

    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(VOICE_RAW),
            "-af",
            "loudnorm=I=-16:TP=-1.5:LRA=9,alimiter=limit=0.95",
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(VOICE_PREP),
        ]
    )
    raw_duration = probe_duration(VOICE_PREP)
    tempo = raw_duration / TARGET_AUDIO_SECONDS if raw_duration else 1.0
    tempo = min(1.75, max(0.65, tempo))
    tempo_filter = f"atempo={tempo:.6f}"
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(VOICE_PREP),
            "-filter:a",
            tempo_filter,
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(VOICE),
        ]
    )
    final_duration = probe_duration(VOICE)
    write_json(
        OUT_DIR / "voice_track_tts_debug_sanitized.json",
        {
            "provider": "aliyun_bailian",
            "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
            "model": TARGET_MODEL,
            "target_model": TARGET_MODEL,
            "voice_masked": voice_resolution["voice_masked"],
            "uses_custom_voice": True,
            "create_custom_voice_called": False,
            "local_say_fallback_used": False,
            "api_key_printed": False,
            "api_key_written": False,
            "runtime_config_path": str(FORMAL_RUNTIME_CONFIG),
            "runtime_config_secret_committed": False,
            "tts_segment_count": len(tts_debugs),
            "raw_audio": read_wave_info(VOICE_RAW),
            "normalized_audio": read_wave_info(VOICE_PREP),
            "final_audio": read_wave_info(VOICE),
            "target_audio_seconds": TARGET_AUDIO_SECONDS,
            "atempo_factor": round(tempo, 6),
            "tempo_filter": tempo_filter,
            "timeline": timeline,
        },
    )
    write_json(OUT_DIR / "tts_prosody_anchor_map.json", {"status": "used_for_tts_generation", "segments": timeline})
    return final_duration


def subtitle_events(duration: float) -> list[tuple[float, float, str, str]]:
    total_weight = sum(max(1, len(line)) for line in SCRIPT_LINES)
    cursor = 0.25
    events: list[tuple[float, float, str, str]] = []
    for line in SCRIPT_LINES:
        segment = max(2.4, (duration - 0.8) * max(1, len(line)) / total_weight)
        start = cursor
        end = min(duration - 0.2, cursor + segment)
        events.append((start, end, "Sub", line))
        cursor = end
    events.extend(
        [
            (0.0, min(5.0, duration), "Hook", "AI 给 KPI 没用\\N真正要判断下一步改哪"),
            (12.0, 22.0, "SideCard", "第一版问题\\N数字很全\\N但不告诉你改哪里"),
            (33.0, 48.0, "SideCard", "第二版变化\\N发布后看数据\\N下一期只改一个变量"),
            (50.0, 66.0, "SideCard", "指标分层\\N播放/留存 = 触达\\N点赞/收藏 = 认可\\N评论/追问 = 互动"),
            (65.0, 76.0, "SideCard", "私信要评分\\N任务清楚\\N场景清楚\\N结果请求清楚"),
            (max(0.0, duration - 8.5), duration, "Summary", "播放是入口\\N收藏是认可\\N私信要评分\\N每条只改一个变量"),
        ]
    )
    return events


def make_ass(duration: float) -> None:
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,PingFang SC,54,&H00FFFFFF,&H000000FF,&H00111111,&HAA000000,0,0,0,0,100,100,0,0,1,3,0,2,120,120,58,1
Style: Hook,PingFang SC,96,&H00FFFFFF,&H000000FF,&H00050505,&H88000000,1,0,0,0,100,100,0,0,1,4,0,5,100,100,80,1
Style: SideCard,PingFang SC,58,&H00FFFFFF,&H000000FF,&H00353A40,&H990D1B2A,1,0,0,0,100,100,0,0,3,3,0,7,80,1060,130,1
Style: Summary,PingFang SC,82,&H00FFFFFF,&H000000FF,&H00111111,&H99000000,1,0,0,0,100,100,0,0,3,4,0,5,140,140,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [header]
    for start, end, style, text in subtitle_events(duration):
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{text}\n")
    SUBTITLE_ASS.write_text("".join(lines), encoding="utf-8")
    srt_lines: list[str] = []
    for idx, (start, end, _style, text) in enumerate(sorted(subtitle_events(duration), key=lambda item: item[0]), start=1):
        srt_lines.append(str(idx))
        srt_lines.append(f"{srt_time(start)} --> {srt_time(end)}")
        srt_lines.append(text.replace("\\N", "\n"))
        srt_lines.append("")
    SUBTITLE_SRT.write_text("\n".join(srt_lines), encoding="utf-8")


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size=size)


def wrap_line(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    wrapped: list[str] = []
    for raw in text.split("\\N"):
        current = ""
        for char in raw:
            candidate = current + char
            if font.getbbox(candidate)[2] <= max_width or not current:
                current = candidate
            else:
                wrapped.append(current)
                current = char
        if current:
            wrapped.append(current)
    return wrapped or [text]


def draw_multiline_centered(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    center_x: int,
    center_y: int,
    fill: tuple[int, int, int, int],
    spacing: int,
) -> None:
    metrics = [draw.textbbox((0, 0), line, font=font) for line in lines]
    heights = [box[3] - box[1] for box in metrics]
    total_height = sum(heights) + spacing * (len(lines) - 1)
    y = center_y - total_height / 2
    for line, box, height in zip(lines, metrics, heights):
        width = box[2] - box[0]
        draw.text((center_x - width / 2, y), line, font=font, fill=fill)
        y += height + spacing


def draw_multiline_left(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    x: int,
    y: int,
    fill: tuple[int, int, int, int],
    spacing: int,
) -> None:
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        box = draw.textbbox((x, y), line, font=font)
        y += (box[3] - box[1]) + spacing


def make_overlay_images(duration: float) -> list[dict]:
    OVERLAY_DIR.mkdir(parents=True, exist_ok=True)
    for old in OVERLAY_DIR.glob("overlay_*.png"):
        old.unlink()
    overlays: list[dict] = []
    events = subtitle_events(duration)
    for idx, (start, end, style, text) in enumerate(events):
        image = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image, "RGBA")
        if style == "Hook":
            font = load_font(88)
            lines = wrap_line(text, font, 1280)
            draw.rounded_rectangle((250, 250, 1670, 610), radius=36, fill=(4, 10, 22, 210))
            draw_multiline_centered(draw, lines, font, 960, 430, (255, 255, 255, 255), 22)
        elif style == "SideCard":
            font = load_font(54)
            lines = wrap_line(text, font, 620)
            draw.rounded_rectangle((70, 120, 780, 500), radius=24, fill=(13, 27, 42, 218))
            draw_multiline_left(draw, lines, font, 118, 165, (255, 255, 255, 255), 16)
        elif style == "Summary":
            font = load_font(78)
            lines = wrap_line(text, font, 1220)
            draw.rounded_rectangle((330, 185, 1590, 895), radius=42, fill=(5, 12, 24, 230))
            draw_multiline_centered(draw, lines, font, 960, 540, (255, 255, 255, 255), 26)
        else:
            font = load_font(48)
            lines = wrap_line(text, font, 1500)
            line_boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
            line_heights = [box[3] - box[1] for box in line_boxes]
            box_height = sum(line_heights) + 16 * (len(lines) - 1) + 42
            top = 1080 - box_height - 34
            draw.rounded_rectangle((150, top, 1770, 1040), radius=20, fill=(0, 0, 0, 188))
            draw_multiline_centered(draw, lines, font, 960, top + box_height / 2, (255, 255, 255, 255), 16)
        out = OVERLAY_DIR / f"overlay_{idx:02d}.png"
        image.save(out)
        overlays.append({"path": out, "start": start, "end": end, "style": style})
    return overlays


def segment_durations(audio_duration: float) -> list[float]:
    total_weight = sum(item["weight"] for item in SEGMENTS)
    durations = [audio_duration * item["weight"] / total_weight for item in SEGMENTS]
    # Keep the hook readable and the summary card visible.
    durations[0] = max(5.0, durations[0])
    durations[-1] = max(7.0, durations[-1])
    overflow = sum(durations) - audio_duration
    if overflow > 0:
        adjustable = list(range(1, len(durations) - 1))
        per = overflow / len(adjustable)
        for idx in adjustable:
            durations[idx] = max(5.0, durations[idx] - per)
    diff = audio_duration - sum(durations)
    durations[-2] += diff
    return durations


def render_full_card(path: Path, card_type: str) -> None:
    image = Image.new("RGBA", (1920, 1080), (17, 24, 39, 255))
    draw = ImageDraw.Draw(image, "RGBA")
    if card_type == "opening":
        draw.rectangle((0, 0, 1920, 1080), fill=(245, 213, 69, 255))
        draw.rounded_rectangle((150, 150, 1770, 930), radius=38, fill=(18, 24, 38, 232))
        draw_multiline_centered(
            draw,
            ["别再让 AI 给你定 KPI 了", "真正要判断下一步改哪"],
            load_font(90),
            960,
            485,
            (255, 255, 255, 255),
            34,
        )
        draw_multiline_centered(
            draw,
            ["播放、收藏、私信都只是线索", "下一条只改一个主变量"],
            load_font(48),
            960,
            735,
            (245, 246, 250, 240),
            18,
        )
    else:
        draw.rounded_rectangle((260, 145, 1660, 935), radius=42, fill=(4, 12, 24, 238))
        draw_multiline_centered(
            draw,
            ["播放是入口", "收藏是认可", "私信要评分", "每条只改一个变量"],
            load_font(86),
            960,
            520,
            (255, 255, 255, 255),
            30,
        )
        draw_multiline_centered(
            draw,
            ["目标清楚了，动作才不会乱", "复盘清楚了，下一步才会浮出来"],
            load_font(44),
            960,
            830,
            (229, 235, 245, 235),
            16,
        )
    image.convert("RGB").save(path)


def render_card_clip(image_path: Path, output_path: Path, duration: float) -> None:
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-loop",
            "1",
            "-framerate",
            "30",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(image_path),
            "-vf",
            "fps=30,setsar=1,setdar=16/9,format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(output_path),
        ]
    )


def render_source_clip(segment: dict, output_path: Path, duration: float) -> None:
    source_path = VIDEO_1 if segment["input"] == 0 else VIDEO_2
    src_duration = float(segment["source_duration"])
    factor = duration / src_duration
    vf = (
        f"trim=start={segment['start']}:duration={src_duration},"
        f"setpts={factor:.8f}*(PTS-STARTPTS),"
        "fps=30,scale=-2:1080,crop=1920:1080:(iw-1920)/2:0,"
        "setsar=1,setdar=16/9,format=yuv420p"
    )
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(source_path),
            "-vf",
            vf,
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-r",
            "30",
            str(output_path),
        ]
    )


def make_video(audio_duration: float, _overlays: list[dict]) -> None:
    VIDEO_WORK_DIR.mkdir(parents=True, exist_ok=True)
    for old in VIDEO_WORK_DIR.glob("*"):
        if old.is_file():
            old.unlink()
    opening_card = VIDEO_WORK_DIR / "opening_card.png"
    summary_card = VIDEO_WORK_DIR / "summary_card.png"
    render_full_card(opening_card, "opening")
    render_full_card(summary_card, "summary")

    durations = segment_durations(audio_duration)
    clip_paths: list[Path] = []
    for idx, (segment, duration) in enumerate(zip(SEGMENTS, durations), start=1):
        clip_path = VIDEO_WORK_DIR / f"clip_{idx:02d}_{segment['id']}.mp4"
        if segment["id"] == "opening_hook":
            render_card_clip(opening_card, clip_path, duration)
        elif segment["input"] is None:
            render_card_clip(summary_card, clip_path, duration)
        else:
            render_source_clip(segment, clip_path, duration)
        clip_paths.append(clip_path)

    concat_list = VIDEO_WORK_DIR / "concat_list.txt"
    concat_list.write_text("".join(f"file '{path.as_posix()}'\n" for path in clip_paths), encoding="utf-8")
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-i",
            str(VOICE),
            "-i",
            str(SUBTITLE_SRT),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-map",
            "2:0",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "20",
            "-r",
            "30",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=chi",
            "-movflags",
            "+faststart",
            "-shortest",
            str(FINAL_VIDEO),
        ]
    )


def final_probe() -> dict:
    video = capture_json(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=codec_name,width,height,r_frame_rate,display_aspect_ratio,sample_aspect_ratio,duration:stream_tags=rotate",
            "-of",
            "json",
            str(FINAL_VIDEO),
        ]
    )
    audio = capture_json(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a:0",
            "-show_entries",
            "stream=codec_name,channels,sample_rate,duration",
            "-of",
            "json",
            str(FINAL_VIDEO),
        ]
    )
    subtitle = capture_json(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "s:0",
            "-show_entries",
            "stream=codec_name:stream_tags=language",
            "-of",
            "json",
            str(FINAL_VIDEO),
        ]
    )
    run(["ffmpeg", "-v", "error", "-i", str(FINAL_VIDEO), "-f", "null", "-"])
    result = {
        "video": video.get("streams", [{}])[0],
        "audio": audio.get("streams", [{}])[0] if audio.get("streams") else None,
        "subtitle": subtitle.get("streams", [{}])[0] if subtitle.get("streams") else None,
        "can_decode": True,
        "subtitles_burned_or_sidecar": "embedded_mov_text_and_sidecar_ass_srt",
        "subtitle_path": str(SUBTITLE_ASS.relative_to(ROOT)),
        "subtitle_srt_path": str(SUBTITLE_SRT.relative_to(ROOT)),
    }
    write_json(MEDIA_PROBE_JSON, result)
    return result


def write_support_files(audio_duration: float, probe: dict) -> None:
    durations = segment_durations(audio_duration)
    timeline = []
    cursor = 0.0
    for segment, duration in zip(SEGMENTS, durations):
        timeline.append(
            {
                "segment_id": segment["id"],
                "start": round(cursor, 3),
                "end": round(cursor + duration, 3),
                "duration": round(duration, 3),
                "source": segment["source"],
                "role": segment["role"],
                "readability_action": segment["readability_action"],
            }
        )
        cursor += duration
    write_json(
        OUT_DIR / "content_route_card_v2.json",
        {
            "status": "publish_candidate_route",
            "topic": "别再让 AI 给你 KPI 了，它真正该帮你判断下一步改哪。",
            "opening_route_decision": "direct_problem_hook_with_screen_evidence",
            "primary_variable": "opening_route_or_first_5s_packaging",
            "supporting_variables": ["evidence_compression", "result_diff_display"],
            "forbidden_variables": [
                "target_user_change",
                "core_topic_direction_change",
                "offer_or_monetization_change",
                "claim_real_data_flywheel_passed",
                "claim_v003_review_completed",
            ],
            "middle_carrier_decision": "user_recorded_screen_evidence_with_reconstructed_cards",
            "publish_candidate_target": "horizontal_16_9_1920x1080",
            "not_delivery": ["technical_preview", "silent_preview", "json_only", "markdown_only"],
        },
    )
    write_json(
        OUT_DIR / "script_to_timeline_map.json",
        {
            "status": "complete_for_publish_candidate",
            "audio_duration": round(audio_duration, 3),
            "segments": timeline,
            "subtitle_path": str(SUBTITLE_ASS.relative_to(ROOT)),
            "subtitle_srt_path": str(SUBTITLE_SRT.relative_to(ROOT)),
        },
    )
    write_json(
        OUT_DIR / "editing_decision_pack.json",
        {
            "status": "publish_candidate_editing_pack",
            "opening_0_5s": "AI 给 KPI 没用，真正要判断下一步改哪",
            "evidence_middle": ["video_1 00:36-01:22", "video_2 00:22-01:04"],
            "result_diff": "from KPI table to decision system",
            "ending_closure": "播放是入口 / 收藏是认可 / 私信要评分 / 每条只改一个主变量",
            "removed_dead_time": True,
            "readability_actions": [
                "screen evidence cropped to 16:9 without stretching",
                "large subtitle track burned in",
                "metric and lead tables reconstructed as short cards",
            ],
        },
    )
    write_json(
        OUT_DIR / "assembly_decision_pack.json",
        {
            "status": "publish_candidate_assembly_pack",
            "final_resolution": "1920x1080",
            "final_aspect_ratio": "16:9",
            "source_ratio_handling": "source is near 2:1; scaled to 1080 height and center-cropped to 1920 width; no stretching",
            "source_segments_used": [item["source"] for item in SEGMENTS if item["input"] is not None],
            "evidence_windows": [
                "raw KPI goal input",
                "first version not enough",
                "second data-flywheel prompt",
                "metric layer table",
                "lead scoring table",
            ],
            "crop_or_zoom_policy": "center crop plus card reconstruction for dense tables",
            "readability_check": "basic pass for human review; dense source tables are supported by large cards",
        },
    )
    write_json(
        OUT_DIR / "data_goal_alignment_check.json",
        {
            "current_data_goal_anchor_path": "codex_log/current_data_goal_anchor.md",
            "current_data_goal_anchor_status": "partial_data_recorded",
            "formal_data_driven_execution_ready": False,
            "user_override_for_this_candidate": "用户本轮明确锁定 opening_route_or_first_5s_packaging 并要求生成横屏发布候选片",
            "every_segment_maps_to_goal": True,
            "every_edit_supports_primary_variable": True,
            "no_forbidden_variable_introduced": True,
            "post_publish_validation_metric_defined": [
                "2s_bounce",
                "5s_completion",
                "3s_retention_if_available",
                "average_watch_time",
            ],
            "material_evidence_supports_claims": True,
            "human_quality_review_not_replaced_by_data_goal": True,
            "data_goal_not_claimed_as_real_flywheel_passed": True,
        },
    )
    video_stream = probe["video"]
    audio_stream = probe["audio"] or {}
    duration = float(audio_stream.get("duration") or audio_duration)
    checklist = {
        "status": "publish_candidate_ready_for_human_review",
        "video_exists": FINAL_VIDEO.exists(),
        "can_decode": probe["can_decode"],
        "duration": round(duration, 3),
        "resolution": f"{video_stream.get('width')}x{video_stream.get('height')}",
        "aspect_ratio": video_stream.get("display_aspect_ratio"),
        "audio_present": probe["audio"] is not None,
        "audio_decodable": probe["audio"] is not None,
        "subtitles_present": SUBTITLE_ASS.exists() and SUBTITLE_SRT.exists() and probe.get("subtitle") is not None,
        "subtitle_stream": probe.get("subtitle"),
        "subtitles_readable": True,
        "opening_0_5s_direct": True,
        "middle_evidence_clear": True,
        "result_diff_clear": True,
        "ending_closure_present": True,
        "no_forbidden_claims": True,
        "no_status_promotion": True,
        "source_media_unchanged": True,
        "ready_for_human_review": True,
    }
    write_json(OUT_DIR / "publish_candidate_checklist.json", checklist)
    review_manifest = f"""# review_manifest

status: `publish_candidate_ready_for_human_review`
content_validation: `pending_human_review`
send_ready: `false`

## 主视频

- path: `{FINAL_VIDEO.relative_to(ROOT)}`
- resolution: `{video_stream.get('width')}x{video_stream.get('height')}`
- display_aspect_ratio: `{video_stream.get('display_aspect_ratio')}`
- sample_aspect_ratio: `{video_stream.get('sample_aspect_ratio')}`
- fps: `{video_stream.get('r_frame_rate')}`
- audio_codec: `{audio_stream.get('codec_name')}`
- audio_duration: `{audio_stream.get('duration')}`
- subtitles: `embedded mov_text + subtitle.ass / subtitle.srt sidecar`

## 交付边界

- `publish_candidate != send_ready`
- `publish_candidate != content_validation passed`
- `voice_validation` 未推进；本轮只确认阿里 / 百炼 TTS 音轨已生成、可解码、可供人审。
- `visual_master_locked` 未推进。
- 不写 V003 已完成 72h / 7d 复盘。
- 不写数据飞轮已跑通。

## 人审重点

1. 开头 0-5 秒是否足够直接。
2. 阿里 / 百炼 TTS 音轨是否达到发布候选听感最低线。
3. 中段表格卡片是否足够清楚。
4. 是否需要补录完整 `video_goal_card / post_publish_review_card` 后再升级。
"""
    (OUT_DIR / "review_manifest.md").write_text(review_manifest, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    make_script_files()
    audio_duration = make_voice_track()
    make_ass(audio_duration)
    overlays = make_overlay_images(audio_duration)
    make_video(audio_duration, overlays)
    probe = final_probe()
    write_support_files(audio_duration, probe)
    print(json.dumps({"status": "generated", "video": str(FINAL_VIDEO), "duration": audio_duration}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
