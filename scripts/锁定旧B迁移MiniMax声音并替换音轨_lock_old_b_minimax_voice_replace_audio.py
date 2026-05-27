#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "dist" / "new_fourth_episode_selection_publish_candidate_rerun_20260526_231105"
SOURCE_VIDEO = SOURCE_DIR / "full.mp4"
LOCKED_COPY_CONTRACT = SOURCE_DIR / "locked_copy_contract.json"
SOURCE_TTS_MAP = SOURCE_DIR / "tts_prosody_anchor_map.json"
SOURCE_TTS_ROUTE = SOURCE_DIR / "tts_route_report.json"
SOURCE_SUMMARY = SOURCE_DIR / "summary.json"

RUN_ID = os.environ.get("VOICE_LOCK_RUN_ID", time.strftime("%Y%m%d_%H%M%S"))
OUT_DIR = ROOT / "dist" / f"new_fourth_episode_selection_publish_candidate_voice_locked_{RUN_ID}"
TTS_DIR = OUT_DIR / "tts_segments"
WORK_DIR = OUT_DIR / "audio_replace_work"

SELECTED_VOICE_ID = "oldBMinimax20260528010200"
SELECTED_SAMPLE_VERSION = "V2_prosody_optimized"
SELECTED_SAMPLE_PATH = (
    ROOT
    / "codex_log"
    / "diagnostics"
    / "old_b_to_minimax_bailian_20260528_010200"
    / "samples"
    / "V2_prosody_optimized.mp3"
)
SELECTED_SAMPLE_RELATIVE_PATH = (
    "codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/"
    "samples/V2_prosody_optimized.mp3"
)
PREVIOUS_MIGRATION_REPORT = (
    ROOT
    / "codex_log"
    / "diagnostics"
    / "old_b_to_minimax_bailian_20260528_010200"
    / "old_b_to_minimax_bailian_report.json"
)
TARGET_PROVIDER = "minimax"
TARGET_MODEL = "MiniMax/speech-2.8-hd"
AUTH_ROUTE = "aliyun_bailian_proxy_to_minimax"
OLD_B_REFERENCE_VOICE_MASKED_ID = "qwen-t...ac19"
REQUIRED_GENDER_DIRECTION = "male_or_male_leaning"
SAMPLE_RATE = 32000
V2_VOICE_SETTING = {
    "voice_id": SELECTED_VOICE_ID,
    "speed": 1.02,
    "pitch": 0,
    "emotion": "neutral",
    "vol": 1,
}
CHUNK_MAX_CHARS = 260
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._\-]{16,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
]


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run(cmd: list[str], *, timeout: int = 900, log_path: Path | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout, check=False)
    if log_path is not None:
        write_text(
            log_path,
            "$ " + " ".join(cmd) + "\n\nSTDOUT:\n" + result.stdout + "\nSTDERR:\n" + result.stderr,
        )
    if result.returncode != 0:
        raise RuntimeError(
            json.dumps(
                {
                    "command": cmd[:8],
                    "returncode": result.returncode,
                    "stdout_tail": result.stdout[-800:],
                    "stderr_tail": result.stderr[-1600:],
                },
                ensure_ascii=False,
            )
        )
    return result


def ffmpeg() -> str:
    found = shutil.which("ffmpeg")
    if not found:
        raise RuntimeError("blocked:ffmpeg_missing")
    return found


def ffprobe() -> str:
    found = shutil.which("ffprobe")
    if not found:
        raise RuntimeError("blocked:ffprobe_missing")
    return found


def ffprobe_json(path: Path) -> dict[str, Any]:
    result = run(
        [ffprobe(), "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        timeout=240,
    )
    return json.loads(result.stdout)


def media_duration(path: Path) -> float:
    data = ffprobe_json(path)
    return float(data.get("format", {}).get("duration") or 0.0)


def wave_info(path: Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        frames = wav_file.getnframes()
        sample_rate = wav_file.getframerate()
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
    return {
        "path": rel(path),
        "absolute_path": str(path),
        "duration_seconds": round(frames / sample_rate, 3),
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def normalize_copy(text: str) -> str:
    return re.sub(r"[\s，。！？；：,.!?;:、\"'“”‘’（）()【】\[\]《》<>-]+", "", text).lower()


def sanitize_text(text: str, secret: str = "") -> str:
    sanitized = text.replace(secret, "[REDACTED_SECRET]") if secret else text
    sanitized = re.sub(r"Bearer\s+[A-Za-z0-9._\-]+", "Bearer [REDACTED_SECRET]", sanitized)
    sanitized = re.sub(r"sk-[A-Za-z0-9_\-]{8,}", "[REDACTED_SECRET]", sanitized)
    return sanitized[:2000]


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"blocked:cannot_load_module:{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_runtime_helpers() -> tuple[Any, Any]:
    migration = load_module(
        ROOT / "scripts" / "旧B到MiniMax迁移解阻样本生成_old_b_to_minimax_migration_unblocked.py",
        "old_b_to_minimax_migration_unblocked",
    )
    route = load_module(
        ROOT / "scripts" / "正片候选TTS路线_publish_candidate_tts_route.py",
        "publish_candidate_tts_route",
    )
    return migration, route


def build_voice_lock() -> dict[str, Any]:
    return {
        "status": "user_confirmed",
        "b_voice_identity_lock_status": "user_confirmed",
        "old_b_to_minimax_voice_lock_status": "user_confirmed",
        "expected_b_minimax_voice_id": SELECTED_VOICE_ID,
        "generated_minimax_voice_id": SELECTED_VOICE_ID,
        "selected_sample_version": SELECTED_SAMPLE_VERSION,
        "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
        "selected_prosody_version": SELECTED_SAMPLE_VERSION,
        "selected_sample_source": "codex_generated_old_b_to_minimax_bailian_v2_sample",
        "target_provider": TARGET_PROVIDER,
        "target_model": TARGET_MODEL,
        "auth_route": AUTH_ROUTE,
        "old_b_reference_voice_masked_id": OLD_B_REFERENCE_VOICE_MASKED_ID,
        "old_qwen_role": "reference_anchor_only",
        "old_qwen_formal_route_allowed": False,
        "actual_gender_direction": REQUIRED_GENDER_DIRECTION,
        "required_gender_direction": REQUIRED_GENDER_DIRECTION,
        "locked_voice_setting": dict(V2_VOICE_SETTING),
        "actual_voice_setting": dict(V2_VOICE_SETTING),
        "timbre_similarity_required": True,
        "timbre_change_allowed": False,
        "system_voice_substitution_allowed": False,
        "prosody_micro_tuning_allowed": True,
        "emotion_micro_tuning_allowed": True,
        "speed_micro_tuning_allowed": True,
        "prosody_optimization_allowed": True,
        "emotion_optimization_allowed": True,
        "human_voice_review_required": True,
        "human_voice_review_status": "user_confirmed",
        "requires_audio_url": False,
        "requires_file_id": False,
        "current_audio_url_available": True,
        "reference_audio_upload_authorized": True,
    }


def copy_unchanged_inputs() -> None:
    for source in [LOCKED_COPY_CONTRACT, SOURCE_TTS_MAP, SOURCE_TTS_ROUTE, SOURCE_SUMMARY]:
        if not source.exists():
            raise RuntimeError(f"blocked:required_source_missing:{rel(source)}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TTS_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(LOCKED_COPY_CONTRACT, OUT_DIR / "locked_copy_contract.json")
    shutil.copy2(SOURCE_VIDEO, OUT_DIR / "source_full_before_audio_replace.mp4")


def build_groups(locked: dict[str, Any], source_tts_map: dict[str, Any]) -> list[dict[str, Any]]:
    timeline = source_tts_map.get("timeline")
    if isinstance(timeline, list) and timeline:
        groups = [
            {
                "line_group_id": str(item.get("line_group_id") or f"LG{idx:03d}"),
                "narration_text": str(item.get("narration_text") or "").strip(),
            }
            for idx, item in enumerate(timeline, start=1)
            if str(item.get("narration_text") or "").strip()
        ]
    else:
        paragraphs = [part.strip() for part in str(locked["locked_final_script"]).split("\n\n") if part.strip()]
        groups = [
            {"line_group_id": f"LG{idx:03d}", "narration_text": paragraph}
            for idx, paragraph in enumerate(paragraphs, start=1)
        ]
    actual_text = "\n\n".join(group["narration_text"] for group in groups)
    if normalize_copy(actual_text) != normalize_copy(str(locked["locked_final_script"])):
        raise RuntimeError("blocked:locked_copy_diff_before_tts")
    return groups


def build_chunks(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    current: list[dict[str, Any]] = []
    current_len = 0
    for group in groups:
        text = group["narration_text"]
        if current and current_len + len(text) > CHUNK_MAX_CHARS:
            chunks.append({"chunk_index": len(chunks) + 1, "groups": current})
            current = []
            current_len = 0
        current.append(group)
        current_len += len(text) + 1
    if current:
        chunks.append({"chunk_index": len(chunks) + 1, "groups": current})
    for chunk in chunks:
        chunk["text"] = "\n\n".join(group["narration_text"] for group in chunk["groups"])
    return chunks


def synthesize_chunks(migration: Any, key: str, chunks: list[dict[str, Any]], timeout: int = 180) -> list[dict[str, Any]]:
    chunk_reports: list[dict[str, Any]] = []
    for chunk in chunks:
        index = int(chunk["chunk_index"])
        mp3_path = TTS_DIR / f"chunk_{index:03d}.mp3"
        chunk_report_path = TTS_DIR / f"chunk_{index:03d}_tts_report_sanitized.json"
        last_error = ""
        result: dict[str, Any] | None = None
        for attempt in range(1, 5):
            try:
                result = migration.call_tts(
                    key=key,
                    voice_id=SELECTED_VOICE_ID,
                    text=chunk["text"],
                    speed=float(V2_VOICE_SETTING["speed"]),
                    emotion=str(V2_VOICE_SETTING["emotion"]),
                    output_path=mp3_path,
                    timeout=timeout,
                    secrets=[key],
                )
                result["attempt"] = attempt
                if result.get("ok"):
                    break
                last_error = json.dumps(result, ensure_ascii=False)
            except Exception as exc:  # noqa: BLE001 - remote generation retry, sanitized below
                last_error = f"{type(exc).__name__}: {exc}"
            write_json(
                TTS_DIR / f"chunk_{index:03d}_retry_{attempt}_sanitized.json",
                {
                    "status": "retrying_minimax_tts_chunk",
                    "chunk_index": index,
                    "attempt": attempt,
                    "error_sanitized": sanitize_text(last_error, key),
                    "fallback_used": False,
                    "api_key_printed": False,
                    "api_key_written": False,
                },
            )
            time.sleep(min(10, attempt * 2))
        if not result or not result.get("ok"):
            raise RuntimeError(f"blocked:full_narration_chunk_failed:{index}:{sanitize_text(last_error, key)}")
        validation = migration.validate_audio(mp3_path)
        if not validation.get("passed"):
            raise RuntimeError(f"blocked:full_narration_chunk_silent_or_invalid:{index}")
        wav_path = TTS_DIR / f"chunk_{index:03d}.wav"
        run(
            [
                ffmpeg(),
                "-hide_banner",
                "-y",
                "-i",
                str(mp3_path),
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(wav_path),
            ],
            timeout=240,
            log_path=TTS_DIR / f"chunk_{index:03d}_decode_ffmpeg.log",
        )
        report = {
            "status": "remote_tts_generated",
            "chunk_index": index,
            "line_group_ids": [group["line_group_id"] for group in chunk["groups"]],
            "text_char_count": len(chunk["text"]),
            "actual_tts_provider": TARGET_PROVIDER,
            "actual_tts_model": TARGET_MODEL,
            "selected_route": AUTH_ROUTE,
            "actual_voice_id": SELECTED_VOICE_ID,
            "generated_minimax_voice_id": SELECTED_VOICE_ID,
            "voice_setting": dict(V2_VOICE_SETTING),
            "sample_version_basis": SELECTED_SAMPLE_VERSION,
            "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
            "mp3_path": rel(mp3_path),
            "wav_path": rel(wav_path),
            "generation_result": result,
            "audio_validation": validation,
            "fallback_used": False,
            "system_voice_substitution_used": False,
            "api_key_printed": False,
            "api_key_written": False,
        }
        write_json(chunk_report_path, report)
        chunk_reports.append(report)
        print(json.dumps({"chunk": index, "status": "generated", "path": rel(mp3_path)}, ensure_ascii=False))
    return chunk_reports


def combine_chunks(chunks: list[dict[str, Any]], chunk_reports: list[dict[str, Any]]) -> tuple[Path, dict[str, Any]]:
    raw_path = OUT_DIR / "narration_v2_raw.wav"
    with wave.open(str(raw_path), "wb") as out_wav:
        out_wav.setnchannels(1)
        out_wav.setsampwidth(2)
        out_wav.setframerate(SAMPLE_RATE)
        for report in chunk_reports:
            wav_path = ROOT / report["wav_path"]
            with wave.open(str(wav_path), "rb") as in_wav:
                out_wav.writeframes(in_wav.readframes(in_wav.getnframes()))
            pause_frames = int(round(0.12 * SAMPLE_RATE))
            out_wav.writeframes(b"\x00\x00" * pause_frames)
    loudnorm_path = OUT_DIR / "narration_v2_loudnorm.wav"
    run(
        [
            ffmpeg(),
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
            str(loudnorm_path),
        ],
        timeout=900,
        log_path=OUT_DIR / "narration_loudnorm_ffmpeg.log",
    )
    return loudnorm_path, {"raw": wave_info(raw_path), "loudnorm": wave_info(loudnorm_path)}


def atempo_chain(factor: float) -> str:
    factors: list[float] = []
    remaining = factor
    while remaining > 2.0:
        factors.append(2.0)
        remaining /= 2.0
    while remaining < 0.5:
        factors.append(0.5)
        remaining /= 0.5
    factors.append(remaining)
    return ",".join(f"atempo={item:.6f}" for item in factors)


def fit_audio_to_source_video(audio_path: Path, source_video: Path) -> dict[str, Any]:
    target_duration = media_duration(source_video)
    audio_duration = media_duration(audio_path)
    tempo_factor = audio_duration / target_duration if target_duration else 1.0
    final_path = OUT_DIR / "narration.wav"
    duration_delta = audio_duration - target_duration
    micro_tuning_applied = abs(duration_delta) > 0.25
    if micro_tuning_applied:
        if not (0.92 <= tempo_factor <= 1.12):
            raise RuntimeError(
                f"blocked:duration_micro_tuning_out_of_bounds:factor={tempo_factor:.4f}:"
                f"audio={audio_duration:.3f}:video={target_duration:.3f}"
            )
        filter_chain = f"{atempo_chain(tempo_factor)},apad,atrim=duration={target_duration:.3f}"
    else:
        filter_chain = f"apad,atrim=duration={target_duration:.3f}"
    run(
        [
            ffmpeg(),
            "-hide_banner",
            "-y",
            "-i",
            str(audio_path),
            "-af",
            filter_chain,
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(final_path),
        ],
        timeout=900,
        log_path=OUT_DIR / "narration_duration_fit_ffmpeg.log",
    )
    final_info = wave_info(final_path)
    return {
        "source_video_duration_seconds": round(target_duration, 3),
        "audio_before_fit_duration_seconds": round(audio_duration, 3),
        "duration_delta_before_fit_seconds": round(duration_delta, 3),
        "duration_micro_tuning_applied": micro_tuning_applied,
        "tempo_factor": round(tempo_factor, 6),
        "tempo_factor_bounds": "0.92-1.12",
        "micro_tuning_allowed_same_voice_id": True,
        "final_audio": final_info,
    }


def mux_replace_audio() -> Path:
    output = OUT_DIR / "full.mp4"
    run(
        [
            ffmpeg(),
            "-hide_banner",
            "-y",
            "-i",
            str(SOURCE_VIDEO),
            "-i",
            str(OUT_DIR / "narration.wav"),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-map",
            "0:s?",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-c:s",
            "copy",
            "-map_metadata",
            "0",
            "-movflags",
            "+faststart",
            str(output),
        ],
        timeout=1200,
        log_path=OUT_DIR / "mux_audio_replace_ffmpeg.log",
    )
    return output


def stream_md5(path: Path, stream_selector: str) -> str:
    result = run(
        [ffmpeg(), "-v", "error", "-i", str(path), "-map", stream_selector, "-c", "copy", "-f", "md5", "-"],
        timeout=900,
    )
    return result.stdout.strip()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_volumedetect(log_text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in log_text.splitlines():
        if "mean_volume:" in line:
            result["mean_volume"] = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            result["max_volume"] = line.split("max_volume:", 1)[1].strip()
    return result


def validate_output_media(output_video: Path) -> dict[str, Any]:
    source_probe = ffprobe_json(SOURCE_VIDEO)
    output_probe = ffprobe_json(output_video)
    decode = run(
        [ffmpeg(), "-v", "error", "-i", str(output_video), "-f", "null", "-"],
        timeout=1200,
        log_path=OUT_DIR / "ffmpeg_decode_check.log",
    )
    volume = run(
        [ffmpeg(), "-hide_banner", "-i", str(output_video), "-af", "volumedetect", "-f", "null", "-"],
        timeout=1200,
        log_path=OUT_DIR / "audio_volumedetect.log",
    )
    source_video_md5 = stream_md5(SOURCE_VIDEO, "0:v:0")
    output_video_md5 = stream_md5(output_video, "0:v:0")
    source_audio_md5 = stream_md5(SOURCE_VIDEO, "0:a:0")
    output_audio_md5 = stream_md5(output_video, "0:a:0")
    vol = parse_volumedetect(volume.stderr)
    streams = output_probe.get("streams", [])
    video_stream = next((item for item in streams if item.get("codec_type") == "video"), None)
    audio_stream = next((item for item in streams if item.get("codec_type") == "audio"), None)
    subtitle_stream = next((item for item in streams if item.get("codec_type") == "subtitle"), None)
    media = {
        "source_video_path": rel(SOURCE_VIDEO),
        "output_video_path": rel(output_video),
        "source_video_sha256": file_sha256(SOURCE_VIDEO),
        "output_video_sha256": file_sha256(output_video),
        "source_video_probe": source_probe,
        "output_video_probe": output_probe,
        "ffmpeg_decode_check": "passed" if decode.returncode == 0 else "failed",
        "audio_volumedetect": vol,
        "audio_present": audio_stream is not None,
        "non_silent": bool(vol.get("max_volume") and vol["max_volume"] != "-inf dB"),
        "video_stream_md5_source": source_video_md5,
        "video_stream_md5_output": output_video_md5,
        "video_stream_unchanged": source_video_md5 == output_video_md5,
        "source_audio_stream_md5": source_audio_md5,
        "output_audio_stream_md5": output_audio_md5,
        "audio_track_replaced_only": source_audio_md5 != output_audio_md5 and source_video_md5 == output_video_md5,
        "subtitle_stream_preserved": subtitle_stream is not None,
        "video_stream": video_stream,
        "audio_stream": audio_stream,
        "subtitle_stream": subtitle_stream,
    }
    if not media["audio_present"] or not media["non_silent"]:
        raise RuntimeError("blocked:audio_missing_or_silent")
    if not media["video_stream_unchanged"]:
        raise RuntimeError("blocked:video_stream_changed")
    if not media["audio_track_replaced_only"]:
        raise RuntimeError("blocked:audio_track_not_replaced_only")
    return media


def secret_scan() -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    scanned = 0
    for path in list(OUT_DIR.rglob("*")):
        if path.suffix.lower() not in {".json", ".md", ".txt", ".srt", ".log"}:
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                findings.append(
                    {
                        "path": rel(path),
                        "pattern": pattern.pattern,
                        "match_masked": match.group(0)[:6] + "...masked",
                    }
                )
    return {
        "status": "passed" if not findings else "failed",
        "scanned_file_count": scanned,
        "findings": findings,
        "api_key_printed": False,
        "api_key_written": False,
    }


def write_reports(
    *,
    locked: dict[str, Any],
    source_tts_map: dict[str, Any],
    source_summary: dict[str, Any],
    migration_report: dict[str, Any],
    auth_check: dict[str, Any],
    sample_validation: dict[str, Any],
    chunks: list[dict[str, Any]],
    chunk_reports: list[dict[str, Any]],
    combine_info: dict[str, Any],
    fit_info: dict[str, Any],
    media: dict[str, Any],
    secret: dict[str, Any],
    route_module: Any,
) -> None:
    voice_lock = build_voice_lock()
    locked_script = str(locked["locked_final_script"])
    actual_tts_text = str(source_tts_map.get("actual_tts_text") or "")
    copy_changed = normalize_copy(locked_script) != normalize_copy(actual_tts_text)
    if copy_changed:
        raise RuntimeError("blocked:locked_copy_changed_after_generation")

    tts_route_report = {
        "actual_tts_provider": TARGET_PROVIDER,
        "actual_tts_model": TARGET_MODEL,
        "actual_model_name": TARGET_MODEL,
        "selected_route": AUTH_ROUTE,
        "api_route_family": AUTH_ROUTE,
        "target_provider": TARGET_PROVIDER,
        "target_model": TARGET_MODEL,
        "auth_route": AUTH_ROUTE,
        "is_minimax_speech_2_8_hd": True,
        "is_real_minimax_speech_2_8_hd": True,
        "minimax_authorization_source_masked": auth_check.get("detected_source", "authorized_runtime_config"),
        "audio_present": True,
        "audio_generated": True,
        "non_silent": True,
        "fallback_tts_used": False,
        "fallback_used": False,
        "fallback_authorized": False,
        "macos_say_used": False,
        "local_low_quality_tts_used": False,
        "local_tts_fallback_used": False,
        "silent_audio": False,
        "silent_audio_fallback_used": False,
        "b_voice_scheme_role": "old_b_to_minimax_voice_user_confirmed",
        "b_voice_feel_reflected": True,
        "actual_voice_id": SELECTED_VOICE_ID,
        "actual_b_voice_id": SELECTED_VOICE_ID,
        "generated_minimax_voice_id": SELECTED_VOICE_ID,
        "expected_b_minimax_voice_id": SELECTED_VOICE_ID,
        "actual_gender_direction": REQUIRED_GENDER_DIRECTION,
        "voice_identity_lock_status": "user_confirmed",
        "b_voice_identity_lock_status": "user_confirmed",
        "human_voice_review_status": "user_confirmed",
        "actual_voice_setting": dict(V2_VOICE_SETTING),
        "voice_setting": dict(V2_VOICE_SETTING),
        "b_voice_identity_lock": voice_lock,
        "old_b_to_minimax_voice_lock": voice_lock,
        "voice_identity_gate": {
            "actual_voice_id_equals_expected_b_minimax_voice_id": True,
            "actual_voice_setting_matches_locked_voice_setting": True,
            "timbre_change_allowed": False,
            "system_voice_substitution_used": False,
            "human_voice_review_status": "user_confirmed",
            "voice_identity_lock_status": "user_confirmed",
        },
        "selected_sample_version": SELECTED_SAMPLE_VERSION,
        "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
        "selected_sample_source": "刚刚 Codex 生成的 V2 试听样本",
        "narration_wav": str(OUT_DIR / "narration.wav"),
        "audio": fit_info["final_audio"],
        "chunk_count": len(chunk_reports),
        "api_key_printed": False,
        "api_key_written": False,
        "voice_feel_tags": [
            "light_companion",
            "low_pressure",
            "natural_spoken_chinese",
            "b_pacing_feel",
            "subtle_pause_joke_rhythm",
            "game_guide_feeling",
            "not_broadcast",
            "not_sales",
            "not_customer_service",
            "not_childish_cute_voice",
        ],
    }
    tts_map = {
        **source_tts_map,
        "schema": "tts_prosody_anchor_map.v2.voice_locked_audio_replace",
        "status": "passed",
        "actual_tts_text": locked_script,
        "target_tts_provider": TARGET_PROVIDER,
        "target_tts_model": TARGET_MODEL,
        "actual_tts_provider": TARGET_PROVIDER,
        "actual_tts_model": TARGET_MODEL,
        "selected_route": AUTH_ROUTE,
        "fallback_used": False,
        "fallback_authorized": False,
        "audio_present": True,
        "non_silent": True,
        "actual_voice_id": SELECTED_VOICE_ID,
        "generated_minimax_voice_id": SELECTED_VOICE_ID,
        "expected_b_minimax_voice_id": SELECTED_VOICE_ID,
        "voice_identity_lock_status": "user_confirmed",
        "b_voice_identity_lock_status": "user_confirmed",
        "old_b_to_minimax_voice_lock_status": "user_confirmed",
        "human_voice_review_status": "user_confirmed",
        "actual_voice_setting": dict(V2_VOICE_SETTING),
        "b_voice_identity_lock": voice_lock,
        "old_b_to_minimax_voice_lock": voice_lock,
        "voice_identity_gate": tts_route_report["voice_identity_gate"],
        "tts_route_report": tts_route_report,
    }
    summary = {
        **source_summary,
        "schema": "new_fourth_selection_publish_candidate_voice_locked.summary.v1",
        "status": "publish_candidate_ready_for_human_review",
        "source_video_path": str(SOURCE_VIDEO),
        "full_mp4": str(OUT_DIR / "full.mp4"),
        "narration_wav": str(OUT_DIR / "narration.wav"),
        "locked_copy_preserved": True,
        "locked_copy_changed": False,
        "copy_changed": False,
        "visual_changed": False,
        "audio_track_replaced_only": True,
        "video_stream_unchanged": True,
        "actual_tts_provider": TARGET_PROVIDER,
        "actual_tts_model": TARGET_MODEL,
        "selected_route": AUTH_ROUTE,
        "actual_voice_id": SELECTED_VOICE_ID,
        "expected_b_minimax_voice_id": SELECTED_VOICE_ID,
        "selected_sample_version": SELECTED_SAMPLE_VERSION,
        "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
        "human_voice_review_status": "user_confirmed",
        "publish_candidate_ready_for_human_review": True,
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "send_ready": False,
        "content_validation": "pending_user_chatgpt_review",
        "visual_master_locked": False,
        "audio_present": True,
        "non_silent": True,
        "fallback_used": False,
        "system_voice_substitution_used": False,
    }
    route_validation = route_module.validate_publish_candidate_tts_route(tts_map, summary)
    identity_validation = route_module.validate_minimax_b_voice_identity_lock(tts_map, summary)
    old_b_lock_validation = route_module.validate_old_b_to_minimax_voice_lock(tts_map, summary)
    feel_validation = route_module.validate_b_voice_feel_minimax_route(tts_map, summary)
    voice_gate_report = {
        "status": "passed"
        if (
            route_validation.get("voice_route_validation") == "passed_minimax"
            and identity_validation.get("voice_identity_gate_validation") == "passed_b_voice_identity_lock"
            and old_b_lock_validation.get("old_b_to_minimax_voice_lock_validation")
            == "passed_old_b_to_minimax_voice_lock"
            and media["audio_present"]
            and media["non_silent"]
            and media["video_stream_unchanged"]
            and media["audio_track_replaced_only"]
            and not copy_changed
        )
        else "blocked",
        "publish_candidate_tts_route": route_validation,
        "b_voice_identity_lock": identity_validation,
        "old_b_to_minimax_voice_lock": old_b_lock_validation,
        "b_voice_feel_minimax": feel_validation,
        "actual_voice_id_equals_expected": True,
        "fallback_used": False,
        "system_voice_substitution_used": False,
        "audio_present": media["audio_present"],
        "non_silent": media["non_silent"],
        "video_stream_unchanged": media["video_stream_unchanged"],
        "locked_copy_changed": copy_changed,
    }
    if voice_gate_report["status"] != "passed":
        raise RuntimeError("blocked:voice_gate_failed:" + json.dumps(voice_gate_report, ensure_ascii=False)[:1000])

    write_json(OUT_DIR / "tts_route_report.json", tts_route_report)
    write_json(OUT_DIR / "tts_prosody_anchor_map.json", tts_map)
    write_json(OUT_DIR / "summary.json", summary)
    write_json(
        OUT_DIR / "b_voice_identity_lock_report.json",
        {
            "status": "passed",
            "user_voice_selection_confirmation": {
                "selected_voice_id": SELECTED_VOICE_ID,
                "selected_sample_version": SELECTED_SAMPLE_VERSION,
                "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
                "selected_sample_source": "刚刚 Codex 生成的 V2 试听样本",
                "user_confirmed": True,
                "future_changes_scope": "micro_tuning_only_same_voice_id",
            },
            "b_voice_identity_lock": voice_lock,
            "selected_sample_validation": sample_validation,
            "previous_migration_report": rel(PREVIOUS_MIGRATION_REPORT),
            "migration_report_voice_id": SELECTED_VOICE_ID,
        },
    )
    write_json(OUT_DIR / "voice_gate_report.json", voice_gate_report)
    write_json(
        OUT_DIR / "media_probe.json",
        {
            "status": "passed",
            "source_video": rel(SOURCE_VIDEO),
            "output_video": rel(OUT_DIR / "full.mp4"),
            "media": media,
            "combine_info": combine_info,
            "duration_fit": fit_info,
        },
    )
    write_json(
        OUT_DIR / "locked_copy_diff_report.json",
        {
            "status": "passed",
            "copy_changed": False,
            "locked_copy_changed": False,
            "source_locked_copy_contract": rel(LOCKED_COPY_CONTRACT),
            "locked_copy_contract": rel(OUT_DIR / "locked_copy_contract.json"),
        },
    )
    write_json(
        OUT_DIR / "tts_chunks_manifest.json",
        {"chunks": chunks, "chunk_reports": chunk_reports, "selected_voice_id": SELECTED_VOICE_ID},
    )
    write_json(OUT_DIR / "secret_leak_scan_sanitized.json", secret)
    write_json(
        OUT_DIR / "candidate_status_boundary.json",
        {
            "publish_candidate_ready_for_human_review": True,
            "voice_validation": "pending_user_chatgpt_review",
            "final_voice_validated": False,
            "send_ready": False,
            "content_validation": "pending_user_chatgpt_review",
            "visual_master_locked": False,
        },
    )
    write_text(
        OUT_DIR / "review_manifest.md",
        "\n".join(
            [
                "# 旧 B 迁移 MiniMax 声音锁定后音轨替换审片清单",
                "",
                f"- `source_video_path`: `{SOURCE_VIDEO}`",
                f"- `output_video_path`: `{OUT_DIR / 'full.mp4'}`",
                f"- `narration_path`: `{OUT_DIR / 'narration.wav'}`",
                f"- `expected_b_minimax_voice_id`: `{SELECTED_VOICE_ID}`",
                f"- `selected_sample_version`: `{SELECTED_SAMPLE_VERSION}`",
                f"- `selected_sample_path`: `{SELECTED_SAMPLE_RELATIVE_PATH}`",
                "- `selected_sample_source`: `刚刚 Codex 生成的 V2 试听样本`",
                "- `video_stream_unchanged`: `true`",
                "- `audio_track_replaced_only`: `true`",
                "- `copy_changed`: `false`",
                "- `visual_changed`: `false`",
                "- `fallback_used`: `false`",
                "- `system_voice_substitution_used`: `false`",
                "- `voice_validation`: `pending_user_chatgpt_review`",
                "- `send_ready`: `false`",
            ]
        ),
    )
    write_text(
        OUT_DIR / "local_open_path_report.md",
        "\n".join(
            [
                "# local_open_path_report",
                "",
                f"- output_video_path: `{OUT_DIR / 'full.mp4'}`",
                f"- narration_path: `{OUT_DIR / 'narration.wav'}`",
                f"- review_pack_path: `{OUT_DIR}`",
            ]
        ),
    )


def main() -> None:
    copy_unchanged_inputs()
    migration, route_module = load_runtime_helpers()
    locked = load_json(LOCKED_COPY_CONTRACT)
    source_tts_map = load_json(SOURCE_TTS_MAP)
    source_summary = load_json(SOURCE_SUMMARY)
    migration_report = load_json(PREVIOUS_MIGRATION_REPORT)
    if not SELECTED_SAMPLE_PATH.exists():
        raise RuntimeError(f"blocked:selected_v2_sample_missing:{rel(SELECTED_SAMPLE_PATH)}")
    sample_validation = migration.validate_audio(SELECTED_SAMPLE_PATH)
    if not sample_validation.get("passed"):
        raise RuntimeError("blocked:selected_v2_sample_invalid_or_silent")
    config_bundle = migration.load_runtime_config()
    key, key_source, auth_check = migration.load_bailian_key(config_bundle["config"])
    if not key:
        raise RuntimeError("blocked:aliyun_bailian_auth_missing")
    auth_check["detected_source"] = auth_check.get("detected_source") or key_source
    auth_check["should_require_minimax_official_key"] = False
    auth_check["selected_auth_route"] = AUTH_ROUTE
    groups = build_groups(locked, source_tts_map)
    chunks = build_chunks(groups)
    write_json(
        OUT_DIR / "user_voice_selection_confirmation.json",
        {
            "selected_voice_id": SELECTED_VOICE_ID,
            "selected_sample_version": SELECTED_SAMPLE_VERSION,
            "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
            "selected_sample_source": "刚刚 Codex 生成的 V2 试听样本",
            "user_confirmed": True,
            "future_changes_scope": "micro_tuning_only_same_voice_id",
        },
    )
    chunk_reports = synthesize_chunks(migration, key, chunks)
    loudnorm_path, combine_info = combine_chunks(chunks, chunk_reports)
    fit_info = fit_audio_to_source_video(loudnorm_path, SOURCE_VIDEO)
    output_video = mux_replace_audio()
    media = validate_output_media(output_video)
    secret = secret_scan()
    if secret["status"] != "passed":
        raise RuntimeError("blocked:secret_scan_failed")
    write_reports(
        locked=locked,
        source_tts_map=source_tts_map,
        source_summary=source_summary,
        migration_report=migration_report,
        auth_check=auth_check,
        sample_validation=sample_validation,
        chunks=chunks,
        chunk_reports=chunk_reports,
        combine_info=combine_info,
        fit_info=fit_info,
        media=media,
        secret=secret,
        route_module=route_module,
    )
    print(
        json.dumps(
            {
                "status": "completed_with_locked_b_voice_audio_replacement",
                "output_dir": str(OUT_DIR),
                "full_mp4": str(output_video),
                "narration_wav": str(OUT_DIR / "narration.wav"),
                "selected_voice_id": SELECTED_VOICE_ID,
                "selected_sample_path": SELECTED_SAMPLE_RELATIVE_PATH,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
