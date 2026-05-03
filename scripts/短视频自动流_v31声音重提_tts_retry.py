from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import re
import shutil
import subprocess
import time
import uuid
import wave
from typing import Any

import requests
import websockets


ROOT = pathlib.Path(__file__).resolve().parents[1]
FORMAL_OUTPUT_DIR = (
    ROOT
    / "dist"
    / "完整成片_full_videos"
    / "20260503_短视频自动流最简单流程_full_reference_quality_video"
)
OUTPUT_DIR = FORMAL_OUTPUT_DIR / "local_fix_20260504_reference_quality" / "声音_v31_ac19_b_pacing_tts"
MANIFEST_PATH = FORMAL_OUTPUT_DIR / "manifest.json"

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
REFERENCE_SOURCE_VOICE_MASKED = "qwen-t...ac19"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
RE_ENROLLED_VOICE_RUNTIME_PATH = OUTPUT_DIR / "re_enroll_voice" / "re_enrolled_voice_untracked_runtime.json"

V31_B_PACING_INSTRUCTIONS = (
    "请参考新样本2的说话方式，保持自然口语、轻吐槽和熟人式分享感。\n"
    "语气不要太嗨，不要夸张带货，不要综艺腔。\n"
    "“陪资料加班”“看着像方案，用起来像空气”这些地方可以稍微停一下，让梗自然落地。\n"
    "本轮是完整片重提音轨，不能压缩文案；每个短块按 B 版停顿梗感执行，"
    "句间停顿清楚，但不要拖沓。"
)
VC_SESSION_CONFIG_NOTE = (
    "qwen3-tts-vc-realtime-2026-01-15 是声音复刻模型。"
    "根据阿里官方文档，instructions / optimize_instructions 只适用于 "
    "qwen3-tts-instruct-flash-realtime；本脚本用 ac19 custom voice 合成，"
    "再通过分句、chunk 间停顿和整体节奏控制继承 B 版停顿梗感。"
)
MAX_SYNTH_RETRIES = 3


def resolve_ffmpeg() -> str:
    candidates = [
        shutil.which("ffmpeg"),
        str(ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"),
        "/Users/fan/Documents/视频工厂/node_modules/ffmpeg-static/ffmpeg",
    ]
    for candidate in candidates:
        if candidate and pathlib.Path(candidate).exists():
            return str(candidate)
    raise RuntimeError("缺少 ffmpeg：系统 PATH 与 bundled ffmpeg-static 均未命中")


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


def sanitize_error(error: BaseException) -> dict[str, str]:
    return {
        "error_type": type(error).__name__,
        "error_message": str(error),
    }


def make_event(type_name: str, **payload: Any) -> dict[str, Any]:
    return {"event_id": f"event_{uuid.uuid4().hex}", "type": type_name, **payload}


def mask_voice(voice: str) -> str:
    if not voice:
        return ""
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


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


def read_wave_info(path: pathlib.Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
    return {
        "path": str(path),
        "duration_seconds": round(frames / sample_rate, 3),
        "format": "wav",
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def probe_duration(path: pathlib.Path) -> float:
    completed = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )
    return round(float(completed.stdout.strip()), 3)


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
    write_json(OUTPUT_DIR / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError(f"无法唯一确认 v3.1 custom voice：matched_count={len(candidates)}")
    voice = str(candidates[0].get("voice", ""))
    if mask_voice(voice) != VOICE_MASKED:
        raise RuntimeError(f"voice 脱敏标识不一致：expected={VOICE_MASKED}, actual={mask_voice(voice)}")
    return {
        "voice": voice,
        "voice_masked": mask_voice(voice),
        "target_model": candidates[0].get("target_model"),
        "resolved_by": "list_existing_custom_voices_match_suffix_ac19",
    }


def resolve_voice_for_local_fix(api_key: str) -> dict[str, Any]:
    existing_voice = resolve_existing_custom_voice(api_key)
    if RE_ENROLLED_VOICE_RUNTIME_PATH.exists():
        runtime = json.loads(RE_ENROLLED_VOICE_RUNTIME_PATH.read_text(encoding="utf-8"))
        voice = runtime.get("voice")
        voice_masked = runtime.get("voice_masked") or mask_voice(str(voice))
        if not voice or not str(voice).startswith("qwen-t"):
            raise RuntimeError(f"重建 voice runtime 文件格式异常：{RE_ENROLLED_VOICE_RUNTIME_PATH}")
        sanitized = {
            "provider": "aliyun_bailian",
            "purpose": "use_re_enrolled_reference_voice_for_local_fix",
            "source_reference_voice_masked": REFERENCE_SOURCE_VOICE_MASKED,
            "re_enrolled_voice_masked": voice_masked,
            "preferred_name": runtime.get("preferred_name"),
            "target_model": runtime.get("target_model"),
            "resolved_by": "re_enrolled_from_voice_sample_2_after_existing_custom_voice_channel_failed",
            "full_voice_value_written_to_git": False,
            "existing_reference_voice_list_check": {
                key: value for key, value in existing_voice.items() if key != "voice"
            },
        }
        write_json(OUTPUT_DIR / "re_enrolled_voice_resolution_sanitized.json", sanitized)
        return {
            "voice": voice,
            "voice_masked": voice_masked,
            "source_reference_voice_masked": REFERENCE_SOURCE_VOICE_MASKED,
            "target_model": runtime.get("target_model") or TARGET_MODEL,
            "resolved_by": "re_enrolled_from_voice_sample_2_after_existing_custom_voice_channel_failed",
        }
    return {
        **existing_voice,
        "source_reference_voice_masked": REFERENCE_SOURCE_VOICE_MASKED,
    }


def load_manifest_segments() -> list[dict[str, Any]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    segments = manifest.get("segments", [])
    if not segments:
        raise RuntimeError(f"manifest 没有可用 segments：{MANIFEST_PATH}")
    return [
        {
            "segment_id": item["segment_id"],
            "voiceover_text": item["voiceover_text"],
        }
        for item in segments
    ]


def normalize_tts_text(text: str) -> str:
    cleaned = text.replace("# 《短视频自动流的最简单流程》", "《短视频自动流的最简单流程》")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def split_text(text: str, max_chars: int = 90) -> list[str]:
    sentences = [item.strip() for item in re.split(r"(?<=[。！？?；;：:])", text) if item.strip()]
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if len(sentence) > max_chars:
            if current:
                chunks.append(current.strip())
                current = ""
            parts = [part.strip() for part in re.split(r"(?<=[，,、])", sentence) if part.strip()]
            for part in parts:
                if len(part) > max_chars:
                    for index in range(0, len(part), max_chars):
                        chunks.append(part[index : index + max_chars].strip())
                elif not current:
                    current = part
                elif len(current) + len(part) + 1 <= max_chars:
                    current += " " + part
                else:
                    chunks.append(current.strip())
                    current = part
            continue
        if not current:
            current = sentence
        elif len(current) + len(sentence) + 1 <= max_chars:
            current += " " + sentence
        else:
            chunks.append(current.strip())
            current = sentence
    if current:
        chunks.append(current.strip())
    return chunks


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type == "session.updated":
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_chunk(
    *,
    api_key: str,
    voice: str,
    segment_id: str,
    chunk_index: int,
    text: str,
) -> dict[str, Any]:
    chunk_dir = OUTPUT_DIR / "chunks" / segment_id
    chunk_dir.mkdir(parents=True, exist_ok=True)
    output_path = chunk_dir / f"{segment_id}_part{chunk_index:02d}.wav"
    debug_path = chunk_dir / f"{segment_id}_part{chunk_index:02d}_debug_sanitized.json"
    if output_path.exists() and debug_path.exists():
        try:
            debug = json.loads(debug_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            debug = {}
        if (
            debug.get("tts_input_text") == text
            and debug.get("local_pacing_reference") == V31_B_PACING_INSTRUCTIONS
            and debug.get("instructions_sent_to_api") is None
        ):
            return {
                "status": "success",
                "audio_path": str(output_path),
                "duration_seconds": probe_duration(output_path),
                "skipped_existing": True,
            }

    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(url, additional_headers={"Authorization": f"Bearer {api_key}"}) as ws:
        await ws.send(
            json.dumps(
                make_event(
                    "session.update",
                    session={
                        "mode": "commit",
                        "voice": voice,
                        "language_type": "Chinese",
                        "response_format": "pcm",
                        "sample_rate": SAMPLE_RATE,
                    },
                ),
                ensure_ascii=False,
            )
        )
        await recv_until_session_ready(ws, event_types)
        await ws.send(json.dumps(make_event("input_text_buffer.append", text=text), ensure_ascii=False))
        await ws.send(json.dumps(make_event("input_text_buffer.commit"), ensure_ascii=False))
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
            await ws.send(json.dumps(make_event("session.finish"), ensure_ascii=False))
        except Exception:
            pass

    audio_bytes = b"".join(chunks)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_bytes)

    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
        "create_custom_voice_called": False,
        "instructions_sent_to_api": None,
        "local_pacing_reference": V31_B_PACING_INSTRUCTIONS,
        "vc_session_config_note": VC_SESSION_CONFIG_NOTE,
        "segment_id": segment_id,
        "chunk_index": chunk_index,
        "tts_input_text": text,
        "audio_chunks": len(chunks),
        "audio_bytes": len(audio_bytes),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_types": event_types,
        "output_audio": read_wave_info(output_path),
    }
    write_json(debug_path, debug)
    return {
        "status": "success",
        "audio_path": str(output_path),
        "duration_seconds": debug["output_audio"]["duration_seconds"],
        "debug_path": str(debug_path),
        "skipped_existing": False,
    }


def concat_audio(ffmpeg: str, input_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    concat_path = output_path.with_suffix(".concat.txt")
    concat_path.write_text(
        "".join(f"file '{path.resolve()}'\n" for path in input_paths),
        encoding="utf-8",
    )
    try:
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
                str(concat_path),
                "-ac",
                "1",
                "-ar",
                str(SAMPLE_RATE),
                str(output_path),
            ],
            output_path.with_suffix(".ffmpeg_log.txt"),
        )
    finally:
        concat_path.unlink(missing_ok=True)


def encode_mp3(ffmpeg: str, input_path: pathlib.Path, output_path: pathlib.Path) -> None:
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(input_path),
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "128k",
            str(output_path),
        ],
        output_path.with_suffix(".ffmpeg_log.txt"),
    )


async def main_async() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg = resolve_ffmpeg()
    api_key = load_api_key()
    voice_resolution = resolve_voice_for_local_fix(api_key)
    segments = load_manifest_segments()

    segment_results: list[dict[str, Any]] = []
    segment_mp3_paths: list[pathlib.Path] = []
    for segment in segments:
        segment_id = segment["segment_id"]
        segment_wav = OUTPUT_DIR / "tts" / f"segment_{segment_id}.wav"
        segment_mp3 = OUTPUT_DIR / "tts" / f"segment_{segment_id}.mp3"
        if segment_wav.exists() and segment_mp3.exists():
            duration = probe_duration(segment_mp3)
            chunk_paths = sorted((OUTPUT_DIR / "chunks" / segment_id).glob(f"{segment_id}_part*.wav"))
            segment_mp3_paths.append(segment_mp3)
            segment_results.append(
                {
                    "segment_id": segment_id,
                    "status": "success",
                    "audio_path": str(segment_mp3),
                    "raw_wav_path": str(segment_wav),
                    "request_id": None,
                    "failure_reason": "",
                    "error_message": "",
                    "selected_candidate_id": "v31_custom_voice_ac19_b_pacing",
                    "fallback_events": [],
                    "duration_seconds": duration,
                    "chunk_count": len(chunk_paths),
                    "chunk_results": [
                        {
                            "status": "success",
                            "audio_path": str(path),
                            "duration_seconds": probe_duration(path),
                            "skipped_existing": True,
                        }
                        for path in chunk_paths
                    ],
                    "skipped_existing_segment": True,
                }
            )
            print(json.dumps({"segment_id": segment_id, "duration_seconds": duration, "chunks": len(chunk_paths), "skipped_existing_segment": True}, ensure_ascii=False))
            continue
        text = normalize_tts_text(segment["voiceover_text"])
        text_chunks = split_text(text)
        chunk_results: list[dict[str, Any]] = []
        chunk_paths: list[pathlib.Path] = []
        for index, chunk_text in enumerate(text_chunks, start=1):
            last_error: BaseException | None = None
            result: dict[str, Any] | None = None
            for attempt in range(1, MAX_SYNTH_RETRIES + 1):
                try:
                    result = await synthesize_chunk(
                        api_key=api_key,
                        voice=voice_resolution["voice"],
                        segment_id=segment_id,
                        chunk_index=index,
                        text=chunk_text,
                    )
                    break
                except Exception as error:
                    last_error = error
                    write_json(
                        OUTPUT_DIR
                        / "chunks"
                        / segment_id
                        / f"{segment_id}_part{index:02d}_failure_attempt{attempt}_debug_sanitized.json",
                        {
                            "provider": "aliyun_bailian",
                            "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
                            "model": TARGET_MODEL,
                            "voice_masked": voice_resolution["voice_masked"],
                            "source_reference_voice_masked": voice_resolution.get("source_reference_voice_masked"),
                            "segment_id": segment_id,
                            "chunk_index": index,
                            "attempt": attempt,
                            "max_attempts": MAX_SYNTH_RETRIES,
                            "instructions_sent_to_api": None,
                            "local_pacing_reference": V31_B_PACING_INSTRUCTIONS,
                            "vc_session_config_note": VC_SESSION_CONFIG_NOTE,
                            "tts_input_text_length": len(chunk_text),
                            "error": sanitize_error(error),
                            "macos_say_used": False,
                            "old_tts_fallback_used": False,
                        },
                    )
                    await asyncio.sleep(2 * attempt)
            if result is None:
                raise RuntimeError(
                    f"v3.1 TTS synthesis failed after {MAX_SYNTH_RETRIES} attempts: "
                    f"segment_id={segment_id}, chunk_index={index}, error={last_error}"
                )
            chunk_results.append(result)
            chunk_paths.append(pathlib.Path(result["audio_path"]))

        concat_audio(ffmpeg, chunk_paths, segment_wav)
        encode_mp3(ffmpeg, segment_wav, segment_mp3)
        duration = probe_duration(segment_mp3)
        segment_mp3_paths.append(segment_mp3)
        segment_results.append(
            {
                "segment_id": segment_id,
                "status": "success",
                "audio_path": str(segment_mp3),
                "raw_wav_path": str(segment_wav),
                "request_id": None,
                "failure_reason": "",
                "error_message": "",
                "selected_candidate_id": "v31_custom_voice_ac19_b_pacing",
                "fallback_events": [],
                "duration_seconds": duration,
                "chunk_count": len(text_chunks),
                "chunk_results": chunk_results,
            }
        )
        print(json.dumps({"segment_id": segment_id, "duration_seconds": duration, "chunks": len(text_chunks)}, ensure_ascii=False))

    full_wav = OUTPUT_DIR / "tts" / "formal_voiceover_v31_reference_voice.wav"
    full_mp3 = OUTPUT_DIR / "tts" / "formal_voiceover.mp3"
    concat_audio(ffmpeg, [path.with_suffix(".wav") for path in segment_mp3_paths], full_wav)
    encode_mp3(ffmpeg, full_wav, full_mp3)
    full_duration = probe_duration(full_mp3)
    report = {
        "schema_version": "formal_tts_retry_report/v31_ac19_b_pacing_v1",
        "attempt": "v31_ac19_20260504",
        "status": "success",
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "create_model": CREATE_MODEL,
        "voice_masked": voice_resolution["voice_masked"],
        "source_reference_voice_masked": voice_resolution.get("source_reference_voice_masked"),
        "voice_resolution": {key: value for key, value in voice_resolution.items() if key != "voice"},
        "uses_custom_voice": True,
        "create_custom_voice_called": False,
        "uses_cosyvoice_old_a": False,
        "v31_reference_voice_inheritance": "voice_sample_2_re_enrolled_custom_voice_plus_b_pacing",
        "re_enrolled_voice_used": voice_resolution["voice_masked"] != REFERENCE_SOURCE_VOICE_MASKED,
        "instructions_sent_to_api": None,
        "local_pacing_reference": V31_B_PACING_INSTRUCTIONS,
        "vc_session_config_note": VC_SESSION_CONFIG_NOTE,
        "full_script_used": True,
        "compressed_runtime_used": False,
        "reference_script_used_for_tts": True,
        "reference_voice_used_for_tts": True,
        "audio_path": str(full_mp3),
        "raw_wav_path": str(full_wav),
        "duration_seconds": full_duration,
        "segment_audio_paths": [str(path) for path in segment_mp3_paths],
        "segment_results": segment_results,
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "macos_say_used": False,
    }
    write_json(OUTPUT_DIR / "tts_retry_report.json", report)
    (OUTPUT_DIR / "README.md").write_text(
        "# v3.1 声音标准重提 TTS\n\n"
        "- status：success\n"
        "- provider：aliyun_bailian\n"
        "- api_route_family：aliyun_qwen_realtime_websocket_voice_clone\n"
        f"- model：{TARGET_MODEL}\n"
        f"- source_reference_voice_masked：{voice_resolution.get('source_reference_voice_masked')}\n"
        f"- synthesized_voice_masked：{voice_resolution['voice_masked']}\n"
        "- reference：语音样本 2 重新 enrollment custom voice + B 版停顿梗感\n"
        "- final_voice_validated：false\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "success", "audio_path": str(full_mp3), "duration_seconds": full_duration}, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main_async())
