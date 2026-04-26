from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import re
import shutil
import subprocess
import time
import wave
from typing import Any

import requests
import websockets


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATE = "20260426"
OUTPUT_DIR = (
    ROOT
    / "dist"
    / "voice_trials"
    / f"{DATE}_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis"
)
SAMPLE_CANDIDATES = [
    pathlib.Path("/Users/fan/Documents/视频工厂/素材录制/语音样本 2"),
    pathlib.Path("/Users/fan/Documents/视频工厂/素材录制/语音样本2"),
    pathlib.Path("/Users/fan/Documents/视频工厂/素材录制/语音样本_2"),
    pathlib.Path("/Users/fan/Documents/视频工厂/素材录制/语音样本-2"),
]
SAMPLE_SEARCH_DIR = pathlib.Path("/Users/fan/Documents/视频工厂/素材录制")
CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
PREFERRED_NAME_BASE = "vfsample20426"
SAMPLE_RATE = 24000
CROP_START_SECONDS = 2.0
CROP_DURATION_SECONDS = 17.0

TEMP_TRIAL_TEXT = """其实我觉得，最容易卡住的地方，不是工具不会用。
是你一开始不知道该怎么问。
如果前面那句话问对了，后面的结果会顺很多。
所以重点不是换一个工具，而是先把问题说清楚。"""
TTS_INPUT_TEXT = " ".join(TEMP_TRIAL_TEXT.splitlines())
TTS_INSTRUCTIONS = """请参考新样本里的说话方式，保持自然口语、真人分享感和解释型节奏。
语气要平实亲近，不要播音腔，不要广告腔，不要夸张带货，也不要刻意表演。
请在约 15 秒内自然说完，停顿清楚但不要拖沓。"""


def resolve_ffmpeg() -> str:
    candidates = [
        shutil.which("ffmpeg"),
        str(ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"),
        "/Users/fan/Documents/视频工厂/node_modules/ffmpeg-static/ffmpeg",
    ]
    for candidate in candidates:
        if candidate and pathlib.Path(candidate).exists():
            return candidate
    raise RuntimeError("缺少 ffmpeg：系统 PATH 与 bundled ffmpeg-static 均未命中")


def run_command(args: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\n"
            + "STDOUT:\n" + completed.stdout + "\n\n"
            + "STDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def write_json(path: pathlib.Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
    if not voice:
        return ""
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


def locate_sample() -> dict[str, Any]:
    searched = [str(path) for path in SAMPLE_CANDIDATES]
    suffixes = {".mp4", ".mov", ".m4a", ".wav"}
    for candidate in SAMPLE_CANDIDATES:
        if candidate.is_file():
            return {"path": candidate, "searched": searched, "selection": "direct_file_exact_path"}
        if candidate.is_dir():
            files = [path for path in candidate.rglob("*") if path.is_file() and path.suffix.lower() in suffixes]
            files.sort(key=lambda path: path.stat().st_mtime, reverse=True)
            if not files:
                raise RuntimeError(f"定位到目录但未找到音视频文件：{candidate}")
            return {
                "path": files[0],
                "searched": searched,
                "selection": "directory_latest_audio_video_file",
                "directory_candidates": [str(path) for path in files],
            }

    patterns = ["*语音样本 2*", "*语音样本2*", "*语音样本_2*", "*语音样本-2*"]
    found: list[pathlib.Path] = []
    for pattern in patterns:
        found.extend(SAMPLE_SEARCH_DIR.rglob(pattern))
    found_unique = sorted(set(found), key=lambda path: path.stat().st_mtime if path.exists() else 0, reverse=True)
    audio_video_files: list[pathlib.Path] = []
    for path in found_unique:
        if path.is_file() and path.suffix.lower() in suffixes:
            audio_video_files.append(path)
        elif path.is_dir():
            nested = [item for item in path.rglob("*") if item.is_file() and item.suffix.lower() in suffixes]
            nested.sort(key=lambda item: item.stat().st_mtime, reverse=True)
            audio_video_files.extend(nested)
    if not audio_video_files:
        raise RuntimeError("未找到用户新样本“语音样本 2”，不得回退使用旧样本")
    audio_video_files = sorted(set(audio_video_files), key=lambda path: path.stat().st_mtime, reverse=True)
    return {
        "path": audio_video_files[0],
        "searched": searched + [str(SAMPLE_SEARCH_DIR)],
        "selection": "search_latest_matching_audio_video_file",
        "search_candidates": [str(path) for path in audio_video_files],
    }


def parse_ffmpeg_input(text: str) -> dict[str, Any]:
    info: dict[str, Any] = {}
    duration_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", text)
    if duration_match:
        hours, minutes, seconds = duration_match.groups()
        info["duration_seconds"] = round(int(hours) * 3600 + int(minutes) * 60 + float(seconds), 3)
    bitrate_match = re.search(r"Duration:.*?bitrate:\s*([^,\n]+)", text, flags=re.S)
    if bitrate_match:
        info["bitrate"] = bitrate_match.group(1).strip()
    container_match = re.search(r"Input #0,\s*([^,]+(?:,[^,]+)*),\s*from", text)
    if container_match:
        info["container"] = container_match.group(1).strip()
    video_match = re.search(r"Stream #0:\d+.*Video:\s*([^,\n]+)", text)
    if video_match:
        info["video_codec"] = video_match.group(1).strip()
    audio_line = next((line for line in text.splitlines() if "Audio:" in line and "Stream #0:" in line), "")
    audio_match = re.search(r"Audio:\s*([^,\n]+)", audio_line)
    if audio_match:
        info["audio_codec"] = audio_match.group(1).strip()
        sample_rate_match = re.search(r"(\d+)\s*Hz", audio_line)
        channels_match = re.search(r"Hz,\s*([^,\n]+)", audio_line)
        audio_bitrate_match = re.search(r",\s*([0-9]+ kb/s)", audio_line)
        if sample_rate_match:
            info["sample_rate"] = int(sample_rate_match.group(1))
        if channels_match:
            info["channels"] = channels_match.group(1).strip()
        if audio_bitrate_match:
            info["audio_bitrate"] = audio_bitrate_match.group(1)
    return info


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


def parse_silencedetect(text: str) -> list[dict[str, float | str]]:
    events: list[dict[str, float | str]] = []
    for line in text.splitlines():
        start_match = re.search(r"silence_start:\s*([0-9.]+)", line)
        end_match = re.search(r"silence_end:\s*([0-9.]+).*silence_duration:\s*([0-9.]+)", line)
        if start_match:
            events.append({"type": "silence_start", "time": float(start_match.group(1))})
        if end_match:
            events.append(
                {
                    "type": "silence_end",
                    "time": float(end_match.group(1)),
                    "duration": float(end_match.group(2)),
                }
            )
    return events


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


def extract_audio_assets(ffmpeg: str, sample_path: pathlib.Path) -> dict[str, Any]:
    analysis_copy = OUTPUT_DIR / "语音样本2_分析副本.m4a"
    clone_input = OUTPUT_DIR / "语音样本2_复刻输入_10-20秒.wav"
    asr_input = OUTPUT_DIR / "语音样本2_转写输入_24k_mono.wav"
    run_command(
        [ffmpeg, "-hide_banner", "-y", "-i", str(sample_path), "-vn", "-c:a", "copy", str(analysis_copy)],
        OUTPUT_DIR / "extract_analysis_copy.txt",
    )
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{CROP_START_SECONDS:.3f}",
            "-t",
            f"{CROP_DURATION_SECONDS:.3f}",
            "-i",
            str(sample_path),
            "-vn",
            "-ar",
            str(SAMPLE_RATE),
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(clone_input),
        ],
        OUTPUT_DIR / "extract_clone_input.txt",
    )
    shutil.copy2(clone_input, asr_input)
    return {
        "analysis_copy": {
            "path": rel(analysis_copy),
            "absolute_path": str(analysis_copy),
            "file_size_bytes": analysis_copy.stat().st_size,
        },
        "clone_input": read_wave_info(clone_input),
        "asr_input": read_wave_info(asr_input),
        "crop": {
            "start_seconds": CROP_START_SECONDS,
            "duration_seconds": CROP_DURATION_SECONDS,
            "reason": "silencedetect 未检出明显静音；选择避开首尾的连续片段作为 10-20 秒复刻输入",
        },
    }


def attempt_dashscope_asr(api_key: str, input_wav: pathlib.Path) -> dict[str, Any]:
    debug_path = OUTPUT_DIR / "语音样本2_ASR_attempt_debug_sanitized.json"
    try:
        import dashscope
        from dashscope.audio.asr import Recognition
    except Exception as exc:  # pragma: no cover - depends on local runtime
        result = {
            "status": "skipped",
            "reason": "dashscope SDK unavailable",
            "error": repr(exc),
            "transcript_text": "",
        }
        write_json(debug_path, result)
        return result

    dashscope.api_key = api_key
    model_attempts = ["paraformer-realtime-v2", "paraformer-realtime-v1"]
    attempts: list[dict[str, Any]] = []
    transcript_text = ""
    sentences: Any = None
    for model in model_attempts:
        started = time.time()
        try:
            recognizer = Recognition(
                model=model,
                format="wav",
                sample_rate=SAMPLE_RATE,
                callback=None,
                api_key=api_key,
            )
            response = recognizer.call(str(input_wav), disfluency_removal_enabled=False)
            sentence_payload = response.get_sentence()
            text_parts: list[str] = []
            if isinstance(sentence_payload, list):
                for sentence in sentence_payload:
                    text = sentence.get("text") if isinstance(sentence, dict) else None
                    if text:
                        text_parts.append(text)
            elif isinstance(sentence_payload, dict) and sentence_payload.get("text"):
                text_parts.append(sentence_payload["text"])
            transcript_text = "\n".join(text_parts).strip()
            sentences = sentence_payload
            attempts.append(
                {
                    "model": model,
                    "status_code": getattr(response, "status_code", None),
                    "request_id": getattr(response, "request_id", None),
                    "code": getattr(response, "code", None),
                    "message": getattr(response, "message", None),
                    "elapsed_seconds": round(time.time() - started, 3),
                    "sentence_count": len(sentence_payload) if isinstance(sentence_payload, list) else int(bool(sentence_payload)),
                    "transcript_nonempty": bool(transcript_text),
                }
            )
            if transcript_text:
                break
        except Exception as exc:  # pragma: no cover - external API path
            attempts.append(
                {
                    "model": model,
                    "status": "failed",
                    "elapsed_seconds": round(time.time() - started, 3),
                    "error": repr(exc),
                }
            )

    result = {
        "provider": "aliyun_bailian_dashscope_asr",
        "status": "transcribed" if transcript_text else "failed_or_empty",
        "input_audio": read_wave_info(input_wav),
        "model_attempts": attempts,
        "transcript_text": transcript_text,
        "sentences": sentences if transcript_text else None,
    }
    write_json(debug_path, result)
    if transcript_text:
        transcript_path = OUTPUT_DIR / "语音样本2_转写文本_transcript.md"
        transcript_path.write_text(
            "# 语音样本2 转写文本 Transcript\n\n"
            "## 状态\n\n"
            "- `已确认` 该文本由 DashScope ASR 自动转写生成，需用户 / ChatGPT 复审。\n"
            "- `已确认` 本文件保留自动转写原文，不按普通总结改写。\n\n"
            "## 转写原文\n\n"
            "```text\n"
            f"{transcript_text}\n"
            "```\n",
            encoding="utf-8",
        )
        result["transcript_path"] = rel(transcript_path)
        write_json(debug_path, result)
    return result


def create_custom_voice(api_key: str, audio_path: pathlib.Path) -> dict[str, Any]:
    audio_data = base64.b64encode(audio_path.read_bytes()).decode("ascii")
    preferred_names = [
        PREFERRED_NAME_BASE,
        f"vfs2{int(time.time()) % 100000000}",
        f"vf{int(time.time()) % 100000000}",
    ]
    attempts: list[dict[str, Any]] = []
    for preferred_name in preferred_names:
        payload = {
            "model": CREATE_MODEL,
            "input": {
                "action": "create",
                "target_model": TARGET_MODEL,
                "preferred_name": preferred_name,
                "audio": {"data": f"data:audio/wav;base64,{audio_data}"},
                "language": "zh",
            },
        }
        started = time.time()
        response = requests.post(
            CREATE_ENDPOINT,
            json=payload,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            timeout=90,
        )
        elapsed = round(time.time() - started, 3)
        try:
            data = response.json()
        except json.JSONDecodeError:
            data = {"raw_text": response.text[:1000]}
        output = data.get("output", {}) if isinstance(data, dict) else {}
        voice = output.get("voice", "")
        attempt = {
            "preferred_name": preferred_name,
            "status_code": response.status_code,
            "elapsed_seconds": elapsed,
            "request_id": data.get("request_id") if isinstance(data, dict) else None,
            "code": data.get("code") if isinstance(data, dict) else None,
            "message": data.get("message") if isinstance(data, dict) else None,
            "voice_masked": mask_voice(voice) if voice else None,
            "target_model": output.get("target_model"),
        }
        attempts.append(attempt)
        if response.ok and voice:
            debug = {
                "provider": "aliyun_bailian",
                "endpoint": CREATE_ENDPOINT,
                "request_method": "POST",
                "model": CREATE_MODEL,
                "target_model": TARGET_MODEL,
                "preferred_name": preferred_name,
                "input_audio": read_wave_info(audio_path),
                "create_payload_sanitized": {
                    "model": CREATE_MODEL,
                    "input": {
                        "action": "create",
                        "target_model": TARGET_MODEL,
                        "preferred_name": preferred_name,
                        "audio": {"data": "data:audio/wav;base64,<omitted>"},
                        "language": "zh",
                    },
                },
                "attempts": attempts,
                "final_voice_masked": mask_voice(voice),
            }
            write_json(OUTPUT_DIR / "voice_clone_request_debug_sanitized.json", debug)
            return {"voice": voice, "voice_masked": mask_voice(voice), "preferred_name": preferred_name, "debug": debug}

    debug = {
        "provider": "aliyun_bailian",
        "endpoint": CREATE_ENDPOINT,
        "request_method": "POST",
        "model": CREATE_MODEL,
        "target_model": TARGET_MODEL,
        "input_audio": read_wave_info(audio_path),
        "attempts": attempts,
        "final_status": "failed",
    }
    write_json(OUTPUT_DIR / "voice_clone_request_debug_sanitized.json", debug)
    raise RuntimeError("create_custom_voice 失败，详见 voice_clone_request_debug_sanitized.json")


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_trial(api_key: str, voice: str, output_path: pathlib.Path) -> dict[str, Any]:
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(url, additional_headers=headers) as ws:
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
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": TTS_INPUT_TEXT}, ensure_ascii=False))
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

    output_path.parent.mkdir(parents=True, exist_ok=True)
    audio_bytes = b"".join(chunks)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_bytes)
    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "request_method": "WEBSOCKET",
        "base_url": url,
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
        "uses_serena": False,
        "uses_previous_ab_voice": False,
        "instructions": TTS_INSTRUCTIONS,
        "trial_text_status": "临时试配文案，不代表样本文案风格原文",
        "voice_trial_text": TEMP_TRIAL_TEXT,
        "tts_input_text": TTS_INPUT_TEXT,
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
        "event_types": event_types,
        "output_audio": read_wave_info(output_path),
    }
    write_json(OUTPUT_DIR / "voice_clone_tts_request_debug_sanitized.json", debug)
    return debug


def maybe_tempo_adjust(ffmpeg: str, raw_path: pathlib.Path, final_path: pathlib.Path) -> dict[str, Any]:
    raw_info = read_wave_info(raw_path)
    duration = raw_info["duration_seconds"]
    if 13.0 <= duration <= 16.5:
        shutil.copy2(raw_path, final_path)
        adjustment = {
            "applied": False,
            "reason": "API 原始输出已在约 15 秒范围内",
            "raw": raw_info,
            "final": read_wave_info(final_path),
        }
    else:
        target = 15.0
        factor = max(0.5, min(2.0, duration / target))
        run_command(
            [
                ffmpeg,
                "-hide_banner",
                "-y",
                "-i",
                str(raw_path),
                "-af",
                f"atempo={factor:.6f}",
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(final_path),
            ],
            OUTPUT_DIR / "trial_tempo_adjust.txt",
        )
        adjustment = {
            "applied": True,
            "reason": "API 原始输出未落在约 15 秒范围内，生成节奏校准版作为正式试听 trial",
            "target_duration_seconds": target,
            "atempo_factor": round(factor, 6),
            "raw": raw_info,
            "final": read_wave_info(final_path),
        }
    return adjustment


def validate_audio(ffmpeg: str, path: pathlib.Path) -> dict[str, Any]:
    decode_log = OUTPUT_DIR / "ffmpeg_decode_check.txt"
    volume_log = OUTPUT_DIR / "volumedetect.txt"
    loudnorm_log = OUTPUT_DIR / "loudnorm_measure.txt"
    run_command([ffmpeg, "-hide_banner", "-y", "-i", str(path), "-f", "null", "-"], decode_log)
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    loudnorm = run_command(
        [ffmpeg, "-hide_banner", "-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        loudnorm_log,
    )
    return {
        **read_wave_info(path),
        "decode_status": "通过",
        "volumedetect": parse_volumedetect(volume.stderr),
        "loudnorm": parse_loudnorm(loudnorm.stderr),
        "logs": {
            "decode": rel(decode_log),
            "volumedetect": rel(volume_log),
            "loudnorm": rel(loudnorm_log),
        },
    }


def analyze_sample(ffmpeg: str, sample_path: pathlib.Path) -> dict[str, Any]:
    decode_log = OUTPUT_DIR / "sample_ffmpeg_decode_check.txt"
    volume_log = OUTPUT_DIR / "sample_volumedetect.txt"
    loudnorm_log = OUTPUT_DIR / "sample_loudnorm_measure.txt"
    silence_log = OUTPUT_DIR / "sample_silencedetect.txt"
    decode = run_command([ffmpeg, "-hide_banner", "-y", "-i", str(sample_path), "-f", "null", "-"], decode_log)
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(sample_path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    loudnorm = run_command(
        [ffmpeg, "-hide_banner", "-i", str(sample_path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        loudnorm_log,
    )
    silence = run_command(
        [ffmpeg, "-hide_banner", "-i", str(sample_path), "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
        silence_log,
    )
    stat = sample_path.stat()
    return {
        "path": str(sample_path),
        "file_name": sample_path.name,
        "file_size_bytes": stat.st_size,
        "mtime_epoch": stat.st_mtime,
        "ffmpeg_info": parse_ffmpeg_input(decode.stderr),
        "decode_status": "通过",
        "volumedetect": parse_volumedetect(volume.stderr),
        "loudnorm": parse_loudnorm(loudnorm.stderr),
        "silencedetect": {
            "threshold": "-35dB",
            "min_duration_seconds": 0.25,
            "events": parse_silencedetect(silence.stderr),
        },
        "logs": {
            "decode": rel(decode_log),
            "volumedetect": rel(volume_log),
            "loudnorm": rel(loudnorm_log),
            "silencedetect": rel(silence_log),
        },
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg = resolve_ffmpeg()
    api_key = load_api_key()
    located = locate_sample()
    sample_path = located["path"]
    sample_analysis = analyze_sample(ffmpeg, sample_path)
    extracted = extract_audio_assets(ffmpeg, sample_path)
    clone_input_path = pathlib.Path(extracted["clone_input"]["absolute_path"])
    asr_result = attempt_dashscope_asr(api_key, pathlib.Path(extracted["asr_input"]["absolute_path"]))
    voice_result = create_custom_voice(api_key, clone_input_path)
    raw_trial_path = OUTPUT_DIR / "语音样本2_声音复刻试听_API原始.wav"
    final_trial_path = OUTPUT_DIR / "语音样本2_声音复刻试听_15秒.wav"
    tts_debug = asyncio.run(synthesize_trial(api_key, voice_result["voice"], raw_trial_path))
    tempo_adjustment = maybe_tempo_adjust(ffmpeg, raw_trial_path, final_trial_path)
    validation = validate_audio(ffmpeg, final_trial_path)
    summary = {
        "run_date": DATE,
        "project": "视频工厂",
        "task": "语音样本2复刻与文案风格解析",
        "technical_generation": "通过",
        "voice_validation_status": "待验证",
        "copy_style_status": "待记录" if not asr_result.get("transcript_text") else "转写已生成 / 待高保真记录",
        "content_validation": "待用户 / ChatGPT 最终复审",
        "full_content_validation": "待用户 / ChatGPT 最终复审",
        "send_ready": "no",
        "ffmpeg": ffmpeg,
        "sample_location": {**located, "path": str(sample_path)},
        "sample_analysis": sample_analysis,
        "extracted_assets": extracted,
        "asr": asr_result,
        "model": TARGET_MODEL,
        "create_model": CREATE_MODEL,
        "target_model": TARGET_MODEL,
        "preferred_name": voice_result["preferred_name"],
        "voice_masked": voice_result["voice_masked"],
        "trial_text_status": "临时试配文案，不代表样本文案风格原文",
        "trial_text": TEMP_TRIAL_TEXT,
        "instructions": TTS_INSTRUCTIONS,
        "tts_debug": {
            **tts_debug,
            "voice_masked": voice_result["voice_masked"],
        },
        "tempo_adjustment": tempo_adjustment,
        "trial_validation": validation,
        "outputs": {
            "output_dir": rel(OUTPUT_DIR),
            "analysis_copy": extracted["analysis_copy"]["path"],
            "clone_input": extracted["clone_input"]["path"],
            "raw_trial": rel(raw_trial_path),
            "trial": rel(final_trial_path),
            "create_request_sanitized": rel(OUTPUT_DIR / "voice_clone_request_debug_sanitized.json"),
            "tts_request_sanitized": rel(OUTPUT_DIR / "voice_clone_tts_request_debug_sanitized.json"),
            "ffmpeg_decode_check": rel(OUTPUT_DIR / "ffmpeg_decode_check.txt"),
            "volumedetect": rel(OUTPUT_DIR / "volumedetect.txt"),
            "loudnorm_measure": rel(OUTPUT_DIR / "loudnorm_measure.txt"),
        },
        "forbidden_actions_preserved": {
            "modified_full_mp4": False,
            "modified_middle_preview_mp4": False,
            "replaced_full_audio_track": False,
            "generated_new_video_round": False,
            "marked_voice_passed": False,
            "marked_content_validation_passed": False,
            "marked_send_ready_yes": False,
            "used_previous_ab_trial_as_basis": False,
        },
    }
    write_json(OUTPUT_DIR / "run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
