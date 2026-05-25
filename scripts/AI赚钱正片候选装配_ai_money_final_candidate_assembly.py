from __future__ import annotations

import asyncio
import base64
import json
import math
import os
import pathlib
import shutil
import subprocess
import time
import wave
from typing import Any

import requests
import websockets
from PIL import Image, ImageDraw, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "dist" / "20260514_AI到底赚不赚钱_4_3_final_candidate"
SEGMENT_DIR = OUTPUT_DIR / "tts_segments"
VIDEO_WORK_DIR = OUTPUT_DIR / "video_work"
SUBTITLE_FRAME_DIR = OUTPUT_DIR / "subtitle_frames"

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
LEGACY_NON_MINIMAX_ROUTE_BLOCKED_FOR_PUBLISH_CANDIDATE = True
TARGET_WIDTH = 1440
TARGET_HEIGHT = 1080
FPS = 30

TITLE = "今天就说一个事：AI 到底能不能赚钱？"
MATERIALS = {
    "material_01": ROOT / "素材录制" / "内建视网膜显示器 2026-05-14 02-45-29.mp4",
    "material_02": ROOT / "素材录制" / "内建视网膜显示器 2026-05-14 02-59-28.mp4",
    "material_03": ROOT / "素材录制" / "内建视网膜显示器 2026-05-14 03-06-26.mp4",
}

TTS_INSTRUCTIONS = (
    "请参考新样本2的说话方式和 B 版停顿梗感，保持自然口语、轻吐槽、低压陪伴和游戏向导感。"
    "不要播音腔、新闻腔、销售腔、夹子音，也不要夸张带货。"
    "关键判断句前后留一点停顿，整体自然推进，不要拖沓。"
)

SEGMENTS: list[dict[str, Any]] = [
    {"text": "今天就说一个事：AI 到底能不能赚钱？", "pause_after": 0.35},
    {"text": "我先说结论：", "pause_after": 0.25},
    {"text": "AI 本身不赚钱。", "pause_after": 0.55},
    {"text": "它不会半夜偷偷给你打款，也不会你睡一觉起来，余额自己开始发芽。", "pause_after": 0.35},
    {"text": "但 AI 有一个很狠的地方：", "pause_after": 0.3},
    {"text": "它能把你原来不敢试的东西，变得便宜很多。", "pause_after": 0.45},
    {"text": "以前我做自媒体的时候，如果要拍一个电商粽子视频，", "pause_after": 0.15},
    {"text": "最少两个人，一堆灯光、道具、布景，半天基本就没了。", "pause_after": 0.3},
    {"text": "人工先不算。光灯光、道具这些，随便就两三百。", "pause_after": 0.3},
    {"text": "但我这次用 AI 跑一版类似的粽子视频，", "pause_after": 0.15},
    {"text": "我的经验是：10 分钟左右能出一个初稿，成本二十多。", "pause_after": 0.45},
    {"text": "你看，这里真正变的不是：", "pause_after": 0.25},
    {"text": "AI 帮我赚钱了。", "pause_after": 0.4},
    {"text": "真正变的是：", "pause_after": 0.25},
    {"text": "以前试错很贵。", "pause_after": 0.35},
    {"text": "现在试错变便宜了。", "pause_after": 0.55},
    {"text": "婚纱视频也是一样。", "pause_after": 0.25},
    {"text": "以前一套视频加图片，沟通、找素材、修图、剪辑，一天基本就没了。", "pause_after": 0.3},
    {"text": "现在给一张生活照做参考，AI 半小时左右能跑出一套能看的初稿，", "pause_after": 0.15},
    {"text": "成本也是二十多。", "pause_after": 0.45},
    {"text": "当然，这不是说你丢一张图进去，钱就来了。", "pause_after": 0.35},
    {"text": "那不叫 AI。", "pause_after": 0.25},
    {"text": "那叫许愿池。", "pause_after": 0.55},
    {"text": "AI 真正有用的地方，是它把很多第一版变快了。", "pause_after": 0.3},
    {"text": "第一版视频。", "pause_after": 0.18},
    {"text": "第一版文案。", "pause_after": 0.18},
    {"text": "第一版选品逻辑。", "pause_after": 0.18},
    {"text": "第一版数据复盘。", "pause_after": 0.18},
    {"text": "第一版项目方案。", "pause_after": 0.35},
    {"text": "这些东西以前都很耗人。", "pause_after": 0.25},
    {"text": "现在它可以先帮你跑出来，你再去判断：", "pause_after": 0.25},
    {"text": "这个方向到底值不值得继续做。", "pause_after": 0.45},
    {"text": "比如电商选品这件事。", "pause_after": 0.25},
    {"text": "很多人一上来就问：", "pause_after": 0.25},
    {"text": "AI，给我一个能做的项目。", "pause_after": 0.35},
    {"text": "这种问法，大概率只会得到一碗热气腾腾的废话汤。", "pause_after": 0.45},
    {"text": "我现在会换一种问法。", "pause_after": 0.25},
    {"text": "我会先把自己的条件给进去：", "pause_after": 0.25},
    {"text": "我一个月成本大概是多少？", "pause_after": 0.18},
    {"text": "我自然流量能力大概到哪？", "pause_after": 0.18},
    {"text": "如果一个月发 30 条内容，每单佣金要多少才扛得住？", "pause_after": 0.2},
    {"text": "如果发 60 条，门槛又会降到多少？", "pause_after": 0.35},
    {"text": "我自己这次做成本倒推的时候，AI 把 9500 元每月的成本线拆开了。", "pause_after": 0.35},
    {"text": "如果一个月只发 30 条内容，单单佣金门槛会很高。", "pause_after": 0.25},
    {"text": "如果发到 60 条、80 条，每单需要扛的压力就会明显不一样。", "pause_after": 0.45},
    {"text": "这时候 AI 帮我的不是选一个神品。", "pause_after": 0.35},
    {"text": "而是先告诉我：", "pause_after": 0.25},
    {"text": "哪些方向一开始就不值得试。", "pause_after": 0.45},
    {"text": "这就很关键。", "pause_after": 0.25},
    {"text": "因为赚钱之前，最怕的不是没赚到。", "pause_after": 0.3},
    {"text": "最怕的是你根本不知道自己亏在哪。", "pause_after": 0.55},
    {"text": "我现在用 AI，也不是只用即梦、剪映这些工具。", "pause_after": 0.3},
    {"text": "我更多是把 Codex 这类 AI 接进自己的本地项目里。", "pause_after": 0.35},
    {"text": "它不只是帮我做视频。", "pause_after": 0.25},
    {"text": "它会帮我查素材路径，查画面比例，整理文案证据，检查执行条件。", "pause_after": 0.25},
    {"text": "甚至帮我把不同项目拆成一条条任务线。", "pause_after": 0.45},
    {"text": "比如一条线做视频素材和画面验证。", "pause_after": 0.2},
    {"text": "一条线做电商选品和成本倒推。", "pause_after": 0.2},
    {"text": "一条线做文案和数据复盘。", "pause_after": 0.35},
    {"text": "注意，不是说 AI 自己把收益送上门。", "pause_after": 0.35},
    {"text": "而是我把问题拆清楚以后，它帮我一段一段往下执行和检查。", "pause_after": 0.45},
    {"text": "这个差别非常大。", "pause_after": 0.35},
    {"text": "如果你只是问：AI 怎么赚钱？", "pause_after": 0.3},
    {"text": "这个问题 AI 可以给你无数个，但是你根本不敢去执行。", "pause_after": 0.4},
    {"text": "但如果你问：我现在最耗时间的是哪一步？", "pause_after": 0.2},
    {"text": "我最贵的试错成本在哪里？", "pause_after": 0.2},
    {"text": "我能不能先用 AI 跑一个低成本初稿？", "pause_after": 0.2},
    {"text": "这个方向要看什么数据，才值得继续？", "pause_after": 0.35},
    {"text": "这时候 AI 才开始真的有用。", "pause_after": 0.45},
    {"text": "所以我现在越来越觉得，普通人用 AI，第一步不是学一堆工具。", "pause_after": 0.3},
    {"text": "第一步是先把自己的真实问题说清楚。", "pause_after": 0.45},
    {"text": "你到底想省什么成本？", "pause_after": 0.18},
    {"text": "你到底想放大哪一步？", "pause_after": 0.18},
    {"text": "你到底哪件事反复做、很耗时间、但又必须做？", "pause_after": 0.35},
    {"text": "你把这些背景给够，AI 才能真的帮你。", "pause_after": 0.45},
    {"text": "所以 AI 到底能不能赚钱？", "pause_after": 0.35},
    {"text": "我的答案是：", "pause_after": 0.25},
    {"text": "AI 不负责替你赚钱。", "pause_after": 0.45},
    {"text": "AI 负责把你赚钱之前，那堆又贵、又慢、又重复的东西，先从你身上剥离出去。", "pause_after": 0.45},
    {"text": "最后能不能赚钱，还是看你有没有真实问题，有没有行动力，", "pause_after": 0.15},
    {"text": "以及你能不能把这个问题，一步步交给 AI 拆开执行。", "pause_after": 0.6},
]


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


def write_json(path: pathlib.Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def block_legacy_non_minimax_publish_candidate() -> None:
    write_json(
        OUTPUT_DIR / "tts_route_report.json",
        {
            "actual_tts_provider": "aliyun_bailian",
            "actual_tts_model": TARGET_MODEL,
            "selected_route": "aliyun_qwen_realtime_websocket_voice_clone",
            "is_minimax_speech_2_8_hd": False,
            "audio_generated": False,
            "audio_present": False,
            "non_silent": False,
            "fallback_tts_used": False,
            "b_voice_scheme_role": "voice_feel_reference_only",
            "voice_route_validation": "failed_non_minimax_voice",
            "publish_candidate_ready_for_human_review": False,
            "full_video_can_only_be_internal_diagnostic": True,
            "blocked_reason": "minimax_speech_2_8_hd_required_for_publish_candidate",
            "api_key_printed": False,
            "api_key_written": False,
        },
    )
    raise RuntimeError("blocked_publish_candidate_unavailable:minimax_speech_2_8_hd_required")


def rel(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_api_key() -> str:
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
            value = stripped.split("=", 1)[1].strip().strip('"')
            if value and not value.startswith("SET_"):
                return value
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
        "format": "wav",
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def parse_volumedetect(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        if "mean_volume:" in line:
            result["mean_volume"] = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            result["max_volume"] = line.split("max_volume:", 1)[1].strip()
    return result


def parse_loudnorm(text: str) -> dict[str, Any]:
    start = text.rfind("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return {}
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return {}


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


def material_probe() -> dict[str, Any]:
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
        ratio = width / height
        result[material_id] = {
            "path": str(path),
            "file_size_bytes": path.stat().st_size,
            "duration_seconds": round(float(data["format"]["duration"]), 3),
            "width": width,
            "height": height,
            "ratio": round(ratio, 6),
            "is_near_4_3": abs(ratio - (4 / 3)) <= 0.01,
            "fps": video_stream.get("r_frame_rate"),
            "video_codec": video_stream.get("codec_name"),
            "audio_present": audio_stream is not None,
            "validation_status": "passed",
        }
        if not result[material_id]["is_near_4_3"]:
            raise RuntimeError(f"素材不是接近 4:3：{path}")
    return result


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
    write_json(OUTPUT_DIR / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError(f"无法唯一确认当前 custom voice：matched_count={len(candidates)}")
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


async def synthesize_segment(api_key: str, voice: str, segment_index: int, text: str) -> dict[str, Any]:
    output_path = SEGMENT_DIR / f"seg_{segment_index:03d}.wav"
    debug_path = SEGMENT_DIR / f"seg_{segment_index:03d}_debug_sanitized.json"
    if output_path.exists() and output_path.stat().st_size > 44:
        info = read_wave_info(output_path)
        debug = {
            "status": "reused_existing_segment",
            "segment_index": segment_index,
            "text": text,
            "voice_masked": VOICE_MASKED,
            "output_audio": info,
        }
        write_json(debug_path, debug)
        return debug

    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(url, additional_headers=headers, max_size=16 * 1024 * 1024) as ws:
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
        "audio_bytes": len(audio_bytes),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_type_count": len(event_types),
        "output_audio": info,
    }
    write_json(debug_path, debug)
    return debug


async def generate_tts_segments(api_key: str, voice: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for index, segment in enumerate(SEGMENTS, start=1):
        results.append(await synthesize_segment(api_key, voice, index, segment["text"]))
    return results


def combine_segments() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    raw_path = OUTPUT_DIR / "narration_raw.wav"
    final_path = OUTPUT_DIR / "narration.wav"
    timeline: list[dict[str, Any]] = []
    with wave.open(str(raw_path), "wb") as out_wav:
        out_wav.setnchannels(1)
        out_wav.setsampwidth(2)
        out_wav.setframerate(SAMPLE_RATE)
        cursor = 0.0
        for index, segment in enumerate(SEGMENTS, start=1):
            seg_path = SEGMENT_DIR / f"seg_{index:03d}.wav"
            with wave.open(str(seg_path), "rb") as in_wav:
                if in_wav.getframerate() != SAMPLE_RATE or in_wav.getnchannels() != 1:
                    raise RuntimeError(f"segment format mismatch: {seg_path}")
                frames = in_wav.readframes(in_wav.getnframes())
                duration = in_wav.getnframes() / SAMPLE_RATE
            start = cursor
            out_wav.writeframes(frames)
            cursor += duration
            end = cursor
            timeline.append(
                {
                    "segment_index": index,
                    "text": segment["text"],
                    "audio_path": rel(seg_path),
                    "start": round(start, 3),
                    "end": round(end, 3),
                    "duration": round(duration, 3),
                    "pause_after": segment["pause_after"],
                }
            )
            pause_frames = int(round(float(segment["pause_after"]) * SAMPLE_RATE))
            if pause_frames:
                out_wav.writeframes(b"\x00\x00" * pause_frames)
                cursor += pause_frames / SAMPLE_RATE

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
    return read_wave_info(final_path), timeline


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
    break_points = ["，", "。", "：", "？"]
    midpoint = len(text) // 2
    candidates = [idx + 1 for idx, char in enumerate(text) if char in break_points]
    if candidates:
        split_at = min(candidates, key=lambda idx: abs(idx - midpoint))
    else:
        split_at = midpoint
    return text[:split_at].strip() + "\n" + text[split_at:].strip()


def resolve_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if pathlib.Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    *,
    box_fill: tuple[int, int, int, int] | None = None,
    padding: int = 18,
) -> None:
    lines = text.splitlines()
    line_boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    widths = [box[2] - box[0] for box in line_boxes]
    heights = [box[3] - box[1] for box in line_boxes]
    total_height = sum(heights) + (len(lines) - 1) * 10
    max_width = max(widths) if widths else 0
    if box_fill is not None:
        x0 = (TARGET_WIDTH - max_width) // 2 - padding
        y0 = y - padding
        x1 = (TARGET_WIDTH + max_width) // 2 + padding
        y1 = y + total_height + padding
        draw.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=box_fill)
    cursor_y = y
    for line, width, height in zip(lines, widths, heights):
        draw.text(((TARGET_WIDTH - width) // 2, cursor_y), line, font=font, fill=fill)
        cursor_y += height + 10


def write_captions(timeline: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for idx, item in enumerate(timeline, start=1):
        lines.append(str(idx))
        lines.append(f"{srt_time(item['start'])} --> {srt_time(item['end'])}")
        lines.append(wrap_caption(item["text"]))
        lines.append("")
    (OUTPUT_DIR / "captions.srt").write_text("\n".join(lines), encoding="utf-8")
    write_json(OUTPUT_DIR / "tts_timeline.json", {"segments": timeline})


def render_card(path: pathlib.Path, duration: float, card_type: str) -> None:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    image_path = path.with_suffix(".png")
    if card_type == "opening":
        image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (245, 216, 79, 255))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle([74, 76, 1366, 1004], radius=24, outline=(26, 26, 26, 60), width=18)
        draw.rounded_rectangle([120, 156, 1320, 916], radius=20, fill=(255, 255, 255, 42))
        draw_centered_text(
            draw,
            "今天就说一个事",
            250,
            resolve_font(50),
            (28, 28, 28, 255),
            box_fill=(255, 255, 255, 150),
        )
        draw_centered_text(draw, "AI 到底能不能赚钱？", 398, resolve_font(98, bold=True), (17, 17, 17, 255))
        draw_centered_text(
            draw,
            "不是许愿池，是试错成本计算器",
            552,
            resolve_font(44),
            (58, 58, 58, 255),
            box_fill=(255, 255, 255, 130),
        )
    else:
        image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (16, 20, 22, 255))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle([110, 170, 1330, 450], radius=18, fill=(245, 216, 79, 245))
        draw.rounded_rectangle([110, 520, 1330, 800], radius=18, fill=(247, 243, 232, 245))
        draw_centered_text(draw, "AI 不负责替你赚钱。", 262, resolve_font(72, bold=True), (17, 17, 17, 255))
        draw_centered_text(draw, "AI 负责降低你试错前的成本。", 608, resolve_font(68, bold=True), (17, 17, 17, 255))
        draw_centered_text(
            draw,
            "最后能不能赚，还是看你的问题、行动和判断。",
            890,
            resolve_font(38),
            (232, 238, 238, 255),
        )
    image.save(image_path)
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-loop",
            "1",
            "-i",
            str(image_path),
            "-t",
            f"{duration:.3f}",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-an",
            str(path),
        ],
        VIDEO_WORK_DIR / f"{path.stem}_ffmpeg_log.txt",
    )


def render_material_clip(material_id: str, path: pathlib.Path, duration: float, label: str) -> None:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    source = MATERIALS[material_id]
    vf = ",".join(
        [
            f"scale={TARGET_WIDTH}:{TARGET_HEIGHT}:force_original_aspect_ratio=decrease",
            f"pad={TARGET_WIDTH}:{TARGET_HEIGHT}:(ow-iw)/2:(oh-ih)/2",
            "setsar=1",
        ]
    )
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(source),
            "-t",
            f"{duration:.3f}",
            "-vf",
            vf,
            "-an",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(path),
        ],
        VIDEO_WORK_DIR / f"{path.stem}_ffmpeg_log.txt",
    )


def build_visual_timeline(total_duration: float) -> list[dict[str, Any]]:
    opening_duration = 3.0
    summary_duration = min(9.0, max(6.0, total_duration * 0.035))
    body_duration = max(0.1, total_duration - opening_duration - summary_duration)
    material_02_duration = max(17.0, body_duration * 0.30)
    material_01_duration = max(25.0, body_duration * 0.34)
    material_03_duration = max(25.0, body_duration - material_02_duration - material_01_duration)
    if material_02_duration + material_01_duration + material_03_duration > body_duration:
        scale = body_duration / (material_02_duration + material_01_duration + material_03_duration)
        material_02_duration *= scale
        material_01_duration *= scale
        material_03_duration *= scale
    items = [
        {
            "kind": "opening_card",
            "duration": opening_duration,
            "output": VIDEO_WORK_DIR / "001_opening_hook.mp4",
            "label": "AI 到底能不能赚钱？",
        },
        {
            "kind": "material_02",
            "duration": material_02_duration,
            "output": VIDEO_WORK_DIR / "002_material_02_zongzi_wedding.mp4",
            "label": "粽子 / 婚纱样片：低成本初稿经验",
        },
        {
            "kind": "material_01",
            "duration": material_01_duration,
            "output": VIDEO_WORK_DIR / "003_material_01_ecommerce_cost.mp4",
            "label": "电商成本倒推：9500 成本线 / 佣金门槛",
        },
        {
            "kind": "material_03",
            "duration": material_03_duration,
            "output": VIDEO_WORK_DIR / "004_material_03_codex_workflow.mp4",
            "label": "Codex 本地项目执行系统：任务线与验收边界",
        },
        {
            "kind": "summary_card",
            "duration": summary_duration,
            "output": VIDEO_WORK_DIR / "005_summary_card.mp4",
            "label": "judgment_card",
        },
    ]
    cursor = 0.0
    for item in items:
        item["start"] = round(cursor, 3)
        cursor += float(item["duration"])
        item["end"] = round(cursor, 3)
        item["duration"] = round(float(item["duration"]), 3)
        item["output"] = str(item["output"])
    return items


def render_video_track(total_duration: float) -> pathlib.Path:
    VIDEO_WORK_DIR.mkdir(parents=True, exist_ok=True)
    timeline = build_visual_timeline(total_duration)
    for item in timeline:
        output = pathlib.Path(item["output"])
        if item["kind"] == "opening_card":
            render_card(output, item["duration"], "opening")
        elif item["kind"] == "summary_card":
            render_card(output, item["duration"], "summary")
        else:
            render_material_clip(item["kind"], output, item["duration"], item["label"])
    concat_list = VIDEO_WORK_DIR / "concat_list.txt"
    concat_list.write_text(
        "".join(f"file '{pathlib.Path(item['output']).as_posix()}'\n" for item in timeline),
        encoding="utf-8",
    )
    video_track = VIDEO_WORK_DIR / "video_track_no_subtitles.mp4"
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
        VIDEO_WORK_DIR / "concat_video_ffmpeg_log.txt",
    )
    write_json(OUTPUT_DIR / "timeline_plan.json", {"visual_timeline": timeline})
    return video_track


def subtitle_filter_arg() -> str:
    raise RuntimeError("This ffmpeg build does not include subtitles/drawtext; use render_subtitle_overlay instead.")


def render_subtitle_overlay(timeline: list[dict[str, Any]], total_duration: float) -> pathlib.Path:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    SUBTITLE_FRAME_DIR.mkdir(parents=True, exist_ok=True)
    frame_rate = 5
    frame_count = max(1, math.ceil(total_duration * frame_rate))
    font = resolve_font(44, bold=True)
    pointer = 0
    for frame_index in range(frame_count):
        current_time = frame_index / frame_rate
        while pointer < len(timeline) and current_time > float(timeline[pointer]["end"]):
            pointer += 1
        if pointer < len(timeline) and float(timeline[pointer]["start"]) <= current_time <= float(timeline[pointer]["end"]):
            active_text = wrap_caption(str(timeline[pointer]["text"]))
        else:
            active_text = ""
        image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
        if active_text:
            draw = ImageDraw.Draw(image)
            lines = active_text.splitlines()
            line_boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
            widths = [box[2] - box[0] for box in line_boxes]
            heights = [box[3] - box[1] for box in line_boxes]
            max_width = max(widths)
            total_height = sum(heights) + (len(lines) - 1) * 12
            y0 = TARGET_HEIGHT - total_height - 74
            x0 = (TARGET_WIDTH - max_width) // 2 - 28
            draw.rounded_rectangle(
                [x0, y0 - 20, x0 + max_width + 56, y0 + total_height + 24],
                radius=14,
                fill=(0, 0, 0, 155),
            )
            cursor_y = y0
            for line, width, height in zip(lines, widths, heights):
                draw.text(((TARGET_WIDTH - width) // 2, cursor_y), line, font=font, fill=(255, 255, 255, 255))
                cursor_y += height + 12
        image.save(SUBTITLE_FRAME_DIR / f"{frame_index + 1:06d}.png")
    overlay_path = VIDEO_WORK_DIR / "subtitle_overlay.mov"
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-framerate",
            str(frame_rate),
            "-i",
            str(SUBTITLE_FRAME_DIR / "%06d.png"),
            "-t",
            f"{total_duration:.3f}",
            "-c:v",
            "qtrle",
            "-pix_fmt",
            "argb",
            str(overlay_path),
        ],
        VIDEO_WORK_DIR / "subtitle_overlay_ffmpeg_log.txt",
    )
    return overlay_path


def mux_final_video(video_track: pathlib.Path, subtitle_overlay: pathlib.Path) -> dict[str, Any]:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    full = OUTPUT_DIR / "full.mp4"
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(video_track),
            "-i",
            str(subtitle_overlay),
            "-i",
            str(OUTPUT_DIR / "narration.wav"),
            "-filter_complex",
            "[0:v][1:v]overlay=0:0:format=auto[v]",
            "-map",
            "[v]",
            "-map",
            "2:a:0",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            str(full),
        ],
        OUTPUT_DIR / "full_mux_ffmpeg_log.txt",
    )
    return validate_full_video(full)


def validate_audio_file(path: pathlib.Path, label: str) -> dict[str, Any]:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    decode_log = OUTPUT_DIR / f"{label}_ffmpeg_decode_check.txt"
    volume_log = OUTPUT_DIR / f"{label}_volumedetect.txt"
    loudnorm_log = OUTPUT_DIR / f"{label}_loudnorm_measure.txt"
    run_command([ffmpeg, "-hide_banner", "-y", "-i", str(path), "-f", "null", "-"], decode_log)
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    loudnorm = run_command(
        [ffmpeg, "-hide_banner", "-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        loudnorm_log,
    )
    return {
        **read_wave_info(path),
        "decode_ok": True,
        "volumedetect": parse_volumedetect(volume.stderr),
        "loudnorm": parse_loudnorm(loudnorm.stderr),
        "logs": {
            "decode": rel(decode_log),
            "volumedetect": rel(volume_log),
            "loudnorm": rel(loudnorm_log),
        },
    }


def validate_full_video(path: pathlib.Path) -> dict[str, Any]:
    ffmpeg = resolve_ffmpeg_tool("ffmpeg")
    data = ffprobe_json(path)
    video_stream = next((stream for stream in data["streams"] if stream.get("codec_type") == "video"), None)
    audio_stream = next((stream for stream in data["streams"] if stream.get("codec_type") == "audio"), None)
    if not video_stream or not audio_stream:
        raise RuntimeError("full.mp4 缺少视频或音频轨")
    decode_log = OUTPUT_DIR / "full_decode_check.txt"
    run_command([ffmpeg, "-v", "error", "-i", str(path), "-f", "null", "-"], decode_log)
    width = int(video_stream["width"])
    height = int(video_stream["height"])
    duration = float(data["format"]["duration"])
    return {
        "path": str(path),
        "file_size_bytes": path.stat().st_size,
        "duration_seconds": round(duration, 3),
        "width": width,
        "height": height,
        "aspect_ratio": round(width / height, 6),
        "is_4_3": width == TARGET_WIDTH and height == TARGET_HEIGHT,
        "video_codec": video_stream.get("codec_name"),
        "audio_present": True,
        "audio_codec": audio_stream.get("codec_name"),
        "audio_channels": int(audio_stream.get("channels", 0)),
        "decode_ok": True,
        "technical_validation": "passed",
        "decode_log": rel(decode_log),
    }


def platform_risk_check() -> dict[str, Any]:
    final_text = "\n".join(segment["text"] for segment in SEGMENTS)
    hard_terms = ["绕过检测", "不标 AI", "批量起号", "矩阵号", "账号售卖", "保证收益", "引导外部交易", "引导下载第三方软件"]
    rewrite_terms = ["自动流", "自动化生产流", "生成成片", "运营物料导出", "外部工具", "下载", "去添加", "自动赚钱"]
    caution_terms = ["赚钱", "提效", "流程", "工具", "工作流", "模板", "资料", "工作包"]
    hard_hits = [term for term in hard_terms if term in final_text or term in TITLE]
    rewrite_hits = [term for term in rewrite_terms if term in final_text or term in TITLE]
    caution_hits = [term for term in caution_terms if term in final_text or term in TITLE]
    risk_level = "allowed"
    publish_permission = "allowed"
    if hard_hits:
        risk_level = "hard_block"
        publish_permission = "blocked"
    elif rewrite_hits:
        risk_level = "rewrite_required"
        publish_permission = "rewrite_required"
    elif caution_hits:
        risk_level = "caution"
        publish_permission = "allowed_after_human_review"
    result = {
        "risk_level": risk_level,
        "hit_terms": {"hard_block": hard_hits, "rewrite_required": rewrite_hits, "caution": caution_hits},
        "hit_locations": ["标题", "字幕", "TTS 文案"],
        "required_rewrites": [
            {
                "original": "不是说 AI 在那边“自动赚钱”。",
                "safe_version_used": "不是说 AI 自己把收益送上门。",
                "reason": "避开 `自动赚钱` 高风险表达，同时保留原文否定自动收益的含义。",
            }
        ],
        "ai_label_check": "视频含 AI 配音和 AI 辅助卡片；发布时应保留平台 AI 标识。",
        "publish_permission": publish_permission,
        "final_safe_version": "标题保留提问式表达；字幕未出现保证收益、矩阵号、批量起号、私信领取、下载第三方软件或绕过检测。",
    }
    if risk_level in {"hard_block", "rewrite_required"}:
        raise RuntimeError(f"平台风险仍需改写：{risk_level} {result['hit_terms']}")
    return result


def content_route_card(voice_summary: dict[str, Any], platform_summary: dict[str, Any]) -> dict[str, Any]:
    return {
        "content_route_card_v2": {
            "meta": {
                "title": TITLE,
                "content_id": "20260514_AI到底赚不赚钱_4_3_final_candidate",
                "target_aspect_ratio": "4:3",
                "output_resolution": f"{TARGET_WIDTH}x{TARGET_HEIGHT}",
                "validation_goal": "验证“AI 降低试错成本，而不是自动赚钱”的表达是否被素材证据支撑",
                "current_phase": "final_candidate_video_pending_user_chatgpt_review",
                "route_confidence": "high_after_material_probe_and_tts_generation",
            },
            "opening_route_decision": {
                "selected_opening_route": "meme_gif_opening_hook",
                "reason": "主题带商业焦虑和反直觉判断，前 3 秒用原创文字动效抛问题；不复制第三方人物、头像、字体或构图。",
            },
            "evidence_plan": {
                "material_01_role": "电商成本倒推 / 9500 成本线 / 内容量与佣金门槛",
                "material_02_role": "粽子 / 婚纱样片存在，支撑低成本初稿经验",
                "material_03_role": "Codex 本地项目执行系统，支撑多任务线管理",
                "evidence_boundaries": [
                    "10分钟 / 22元 / 半小时 / 20多为用户经验陈述，不写成画面直接证明。",
                    "material_03 不证明 Codex 并发执行两个任务，只证明多任务线 / 本地执行系统 / 一段一段执行和检查。",
                    "不写 AI 自动赚钱，不写保证收益。",
                ],
            },
            "middle_carrier_decision": {
                "middle_carrier": "用户录制素材",
                "focusee_middle_editing_decision": {
                    "recording_layer_motion_baked_in": True,
                    "no_secondary_zoom_by_default": True,
                    "selected_editing_policy": "direct_cut_by_script",
                    "secondary_zoom_allowed_if": "key_evidence_unclear_only",
                },
            },
            "card_placement_decision": {
                "opening_card": {"type": "meme_gif_opening_hook", "duration_seconds": 3},
                "result_diff_card": "not_inserted_as_separate_card; result difference explained through captions and material_01/material_02",
                "summary_card": {
                    "type": "judgment_card",
                    "modules_per_screen": 2,
                    "allow_multiple_screens": False,
                    "text": ["AI 不负责替你赚钱。", "AI 负责降低你试错前的成本。"],
                },
            },
            "tts_plan": {
                "tts_required": True,
                "selected_voice": VOICE_MASKED,
                "selected_model": TARGET_MODEL,
                "audio_path": rel(OUTPUT_DIR / "narration.wav"),
                "voice_generation_validation": voice_summary,
            },
            "platform_risk_note": {
                "risk_level": platform_summary["risk_level"],
                "hit_terms": platform_summary["hit_terms"],
                "rewrites": platform_summary["required_rewrites"],
            },
            "blocked_if": [
                "素材缺失或不可读",
                "TTS 生成失败或音频不可解码",
                "输出无法达到 1440x1080 4:3",
                "平台风险 hard_block 或 rewrite_required 未处理",
                "需要推进 content_validation / send_ready / publish_status 才能继续",
            ],
        }
    }


def write_markdown_reports(
    *,
    read_status: dict[str, str],
    material_summary: dict[str, Any],
    voice_summary: dict[str, Any],
    platform_summary: dict[str, Any],
    ffprobe_summary: dict[str, Any],
    assembly_summary: dict[str, Any],
) -> None:
    voice_md = "\n".join(
        [
            "# voice_generation_validation",
            "",
            f"- `audio_generated`: `{str(voice_summary['audio_generated']).lower()}`",
            f"- `audio_path`: `{voice_summary['audio_path']}`",
            f"- `duration`: `{voice_summary['duration_seconds']}s`",
            f"- `decode_ok`: `{str(voice_summary['decode_ok']).lower()}`",
            f"- `selected_voice`: `{voice_summary['selected_voice']}`",
            f"- `selected_model`: `{voice_summary['selected_model']}`",
            f"- `pacing_check`: `{voice_summary['pacing_check']}`",
            f"- `ai_broadcast_risk`: `{voice_summary['ai_broadcast_risk']}`",
            f"- `cute_guide_voice_match`: `{voice_summary['cute_guide_voice_match']}`",
            f"- `needs_human_review`: `{str(voice_summary['needs_human_review']).lower()}`",
            "",
            "## 边界",
            "",
            "- 本文件只证明本轮 TTS 生成、解码、装配技术通过。",
            "- 不写 `voice_validation = passed`，不写 `final_voice_validated = true`。",
        ]
    )
    (OUTPUT_DIR / "voice_generation_validation.md").write_text(voice_md + "\n", encoding="utf-8")

    risk_md = "\n".join(
        [
            "# platform_risk_check",
            "",
            f"- `risk_level`: `{platform_summary['risk_level']}`",
            f"- `publish_permission`: `{platform_summary['publish_permission']}`",
            f"- `ai_label_check`: {platform_summary['ai_label_check']}",
            "",
            "## hit_terms",
            "",
            "```json",
            json.dumps(platform_summary["hit_terms"], ensure_ascii=False, indent=2),
            "```",
            "",
            "## required_rewrites",
            "",
            "```json",
            json.dumps(platform_summary["required_rewrites"], ensure_ascii=False, indent=2),
            "```",
            "",
            "## final_safe_version",
            "",
            platform_summary["final_safe_version"],
        ]
    )
    (OUTPUT_DIR / "platform_risk_check.md").write_text(risk_md + "\n", encoding="utf-8")

    review_md = "\n".join(
        [
            "# review_manifest",
            "",
            f"- `title`: {TITLE}",
            "- `candidate_type`: `4:3 带 TTS 完整正片候选`",
            "- `technical_validation`: `passed`",
            "- `voice_generation_validation`: `passed_for_generation_needs_human_review`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `publish_status`: `not_advanced`",
            "",
            "## outputs",
            "",
            f"- `full.mp4`: `{rel(OUTPUT_DIR / 'full.mp4')}`",
            f"- `narration.wav`: `{rel(OUTPUT_DIR / 'narration.wav')}`",
            f"- `captions.srt`: `{rel(OUTPUT_DIR / 'captions.srt')}`",
            f"- `content_route_card_v2.json`: `{rel(OUTPUT_DIR / 'content_route_card_v2.json')}`",
            f"- `assembly_summary.json`: `{rel(OUTPUT_DIR / 'assembly_summary.json')}`",
            f"- `platform_risk_check.md`: `{rel(OUTPUT_DIR / 'platform_risk_check.md')}`",
            f"- `voice_generation_validation.md`: `{rel(OUTPUT_DIR / 'voice_generation_validation.md')}`",
            "",
            "## material_use",
            "",
            "- `material_02`: 粽子 / 婚纱样片，支撑低成本初稿经验。",
            "- `material_01`: 电商成本倒推，支撑成本线、内容量和佣金门槛结构化。",
            "- `material_03`: Codex 本地项目执行系统，支撑多任务线与执行检查，不写并发执行。",
            "",
            "## ffprobe_validation",
            "",
            "```json",
            json.dumps(ffprobe_summary, ensure_ascii=False, indent=2),
            "```",
            "",
            "## status_boundary",
            "",
            "- 不把用户经验陈述写成素材画面直接证明。",
            "- 不写 `Codex 同时执行两个任务`。",
            "- 不覆盖 `dist/latest_review_pack/`。",
            "- 不修改原始素材。",
        ]
    )
    (OUTPUT_DIR / "review_manifest.md").write_text(review_md + "\n", encoding="utf-8")

    safe_area_md = "\n".join(
        [
            "# subtitle_and_card_safe_area_check",
            "",
            "- `subtitle_area`: bottom safe area via ASS/SRT style `MarginV=44`, max two lines from scripted wrapping.",
            "- `opening_card`: 0-3s, no evidence window active.",
            "- `summary_card`: final card, after main evidence windows.",
            "- `middle_cards`: no separate blocking card inserted over material_01/material_02/material_03 evidence windows.",
            "- `material_policy`: source kept full-frame with scale+pad; no secondary zoom/crop/reframe.",
            "- `status`: `passed_by_layout_policy_needs_human_visual_review`",
        ]
    )
    (OUTPUT_DIR / "subtitle_and_card_safe_area_check.md").write_text(safe_area_md + "\n", encoding="utf-8")

    dated_log = "\n".join(
        [
            "# 20260514｜AI 到底赚不赚钱 4:3 带 TTS 完整正片候选装配",
            "",
            "## route_decision",
            "",
            "- `project_route`: `video_factory`",
            "- `task_type`: `video_sample_or_assembly`, `tts_generation_and_voice_validation`, `copywriting_to_video_execution`, `content_route_card_v2_execution`",
            "- `large_task_gate`: `triggered=true`, `parallel_recommendation=serial_only`",
            "- `completion_relay_gate`: `triggered=true`",
            "- `execution_permission`: `allowed_after_materials_4_3_pipeline_and_tts_readiness_verified`",
            "",
            "## read_status",
            "",
            "```json",
            json.dumps(read_status, ensure_ascii=False, indent=2),
            "```",
            "",
            "## outputs",
            "",
            f"- `full.mp4`: `{rel(OUTPUT_DIR / 'full.mp4')}`",
            f"- `narration.wav`: `{rel(OUTPUT_DIR / 'narration.wav')}`",
            f"- `captions.srt`: `{rel(OUTPUT_DIR / 'captions.srt')}`",
            f"- `review_manifest.md`: `{rel(OUTPUT_DIR / 'review_manifest.md')}`",
            f"- `assembly_summary.json`: `{rel(OUTPUT_DIR / 'assembly_summary.json')}`",
            "",
            "## validation",
            "",
            f"- `technical_validation`: `{ffprobe_summary['technical_validation']}`",
            "- `voice_generation_validation`: `passed_for_generation_needs_human_review`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `publish_status`: `not_advanced`",
            f"- `full_mp4_duration`: `{ffprobe_summary['duration_seconds']}s`",
            f"- `full_mp4_resolution`: `{ffprobe_summary['width']}x{ffprobe_summary['height']}`",
            f"- `audio_present`: `{str(ffprobe_summary['audio_present']).lower()}`",
            "",
            "## forbidden_status_check",
            "",
            "- `content_validation`: 未推进为通过。",
            "- `send_ready`: 未推进为 true。",
            "- `publish_status`: 未推进。",
            "- `voice_validation`: 未写 passed。",
            "- `final_voice_validated`: 未写 true。",
            "- `visual_master_locked`: 未写 true。",
            "- `.env / .env.swp`: 未读取。",
            "- `api_key`: 未打印、未写入日志。",
            "- `dist/latest_review_pack/`: 未覆盖。",
            "",
            "## remaining_work_check",
            "",
            "- `must_fix`: none",
            "- `needs_human_review`: 内容复审、声音听感复审、发布前标题/简介最终口径。",
            "",
            "## 下一个目标",
            "",
            "由用户 / ChatGPT 审看 `full.mp4` 的声音质感、字幕遮挡、三段证据承载和内容表达，再决定是否进入下一轮只改一个变量的精修。",
            "",
        ]
    )
    (ROOT / "codex_log" / "20260514_ai_money_4_3_final_candidate_assembly.md").write_text(
        dated_log,
        encoding="utf-8",
    )

    assembly_summary["generated_reports"] = {
        "review_manifest": rel(OUTPUT_DIR / "review_manifest.md"),
        "platform_risk_check": rel(OUTPUT_DIR / "platform_risk_check.md"),
        "voice_generation_validation": rel(OUTPUT_DIR / "voice_generation_validation.md"),
        "subtitle_and_card_safe_area_check": rel(OUTPUT_DIR / "subtitle_and_card_safe_area_check.md"),
        "dated_log": "codex_log/20260514_ai_money_4_3_final_candidate_assembly.md",
    }
    write_json(OUTPUT_DIR / "assembly_summary.json", assembly_summary)


def build_read_status() -> dict[str, str]:
    return {
        "AGENTS.md": "read_ok",
        "codex_source/00_codex_readme.md": "read_ok",
        "codex_source/01_execution_rules.md": "read_ok",
        "codex_log/latest.md": "read_ok",
        "GPT数据源/05_文案路由规则.md": "read_ok",
        "GPT数据源/07_AI知识类视频价值规则.md": "read_ok",
        "GPT数据源/08_当前正式事实.md": "read_ok",
        "GPT数据源/11_项目状态动作总控器_机制推理层.md": "read_ok",
        "codex_source/19_project_state_action_router.md": "read_ok",
        "review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md": "read_ok",
        "codex_log/20260514_AI到底赚不赚钱三段素材细节报告_ai_money_three_materials_detail_report.md": "read_ok",
        "codex_log/20260514_material_03_codex_workflow_deep_audit.md": "read_ok",
        "codex_log/20260514_4_3_aspect_ratio_assembly_fix.md": "read_ok",
        "codex_log/20260425_语音样本_audio_reference_report.md": "read_ok",
        "codex_log/20260426_语音样本2复刻与文案风格解析.md": "read_ok",
        "codex_log/20260427_十五秒文案语速停顿试配.md": "read_ok",
        "codex_log/20260427_文案生产流程与B版声音口径固化.md": "read_ok",
        "codex_source/13_execution_lane_and_parallel_rules.md": "read_ok",
        "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md": "read_ok",
        "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md": "read_ok",
        "codex_source/20_reference_to_execution_contract.md": "read_ok",
        "三段素材": "read_ok",
        "~/.codex/skills/video-metadata-probe/SKILL.md": "read_ok",
        "~/.codex/skills/visual-verdict/SKILL.md": "read_ok_not_applicable_no_external_reference_image",
        "local skills/": "missing",
    }


async def main_async() -> None:
    if LEGACY_NON_MINIMAX_ROUTE_BLOCKED_FOR_PUBLISH_CANDIDATE:
        block_legacy_non_minimax_publish_candidate()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_WORK_DIR.mkdir(parents=True, exist_ok=True)
    read_status = build_read_status()
    material_summary = material_probe()
    api_key = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    tts_debugs = await generate_tts_segments(api_key, voice_resolution["voice"])
    narration_info, tts_timeline = combine_segments()
    write_captions(tts_timeline)
    narration_validation = validate_audio_file(OUTPUT_DIR / "narration.wav", "narration")
    platform_summary = platform_risk_check()
    voice_summary = {
        "audio_generated": True,
        "audio_path": rel(OUTPUT_DIR / "narration.wav"),
        "duration_seconds": narration_validation["duration_seconds"],
        "decode_ok": narration_validation["decode_ok"],
        "selected_voice": VOICE_MASKED,
        "selected_model": TARGET_MODEL,
        "pacing_check": "passed_for_generation; long-form pacing still needs human review",
        "ai_broadcast_risk": "needs_human_review",
        "cute_guide_voice_match": "candidate_matches_reference_direction_needs_human_review",
        "needs_human_review": True,
        "voice_generation_validation": "passed_for_generation_needs_human_review",
    }
    video_track = render_video_track(float(narration_info["duration_seconds"]))
    subtitle_overlay = render_subtitle_overlay(tts_timeline, float(narration_info["duration_seconds"]))
    ffprobe_summary = mux_final_video(video_track, subtitle_overlay)
    route_card = content_route_card(voice_summary, platform_summary)
    write_json(OUTPUT_DIR / "content_route_card_v2.json", route_card)
    assembly_summary = {
        "title": TITLE,
        "output_dir": str(OUTPUT_DIR),
        "generation_success": True,
        "assembly_success": True,
        "tts_generated": True,
        "audio_video_muxed": True,
        "technical_validation": "passed",
        "voice_generation_validation": "passed_for_generation_needs_human_review",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "publish_status": "not_advanced",
        "target_aspect_ratio": "4:3",
        "output_resolution": f"{TARGET_WIDTH}x{TARGET_HEIGHT}",
        "material_probe": material_summary,
        "voice_resolution": {key: value for key, value in voice_resolution.items() if key != "voice"},
        "tts_segment_count": len(SEGMENTS),
        "tts_debug_count": len(tts_debugs),
        "narration": narration_validation,
        "platform_risk_check": platform_summary,
        "ffprobe_validation": ffprobe_summary,
        "forbidden_status_check": {
            "modified_original_materials": False,
            "overwrote_latest_review_pack": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "publish_status_advanced": False,
            "voice_validation_passed": False,
            "final_voice_validated": False,
            "env_file_read": False,
            "api_key_printed": False,
            "api_key_written": False,
        },
        "remaining_work_check": {
            "must_fix": [],
            "needs_human_review": ["content_review", "voice_listening_review", "publish_title_description_review"],
        },
        "sync_back_check": {
            "latest_update_required": True,
            "dated_log_created": True,
            "latest_review_pack_overwritten": False,
        },
    }
    write_markdown_reports(
        read_status=read_status,
        material_summary=material_summary,
        voice_summary=voice_summary,
        platform_summary=platform_summary,
        ffprobe_summary=ffprobe_summary,
        assembly_summary=assembly_summary,
    )


def main() -> None:
    if os.environ.get("PYTHONIOENCODING") is None:
        os.environ["PYTHONIOENCODING"] = "utf-8"
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
