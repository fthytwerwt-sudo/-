#!/usr/bin/env python3
from __future__ import annotations

import argparse
import binascii
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_api_demo_cloud_assembly import (
    CloudAssemblyError,
    _build_object_key,
    _build_oss_signed_get_url,
    _upload_file_to_oss,
)
from formal_api_demo_core import DEFAULT_FORMAL_LOCAL_CONFIG_PATH, load_formal_config


OUTPUT_ROOT = ROOT / "codex_log" / "diagnostics"
DEFAULT_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

DASHSCOPE_MINIMAX_ENDPOINT = (
    "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
)
DASHSCOPE_MODEL = "MiniMax/speech-2.8-hd"
FORMAL_EXAMPLE_CONFIG = ROOT / "config" / "formal_api_demo.example.toml"

REFERENCE_AUDIO_1 = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial"
    / "B_15秒文案_停顿梗感.wav"
)
REFERENCE_AUDIO_2 = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis"
    / "语音样本2_声音复刻试听_15秒.wav"
)

SAMPLE_TEXT = (
    "朋友们，现在做带货，最贵的不是拍视频。\n"
    "最贵的是前面测错商品的成本。\n"
    "所以我不会让 AI 直接说哪个品能爆。\n"
    "我会先让它把商品卡拆成表，把风险写出来，再决定要不要继续测。"
)

SAMPLE_SPECS = [
    {
        "sample_id": "V1_identity_match",
        "goal": "尽量贴旧 B 音色",
        "speed": 1.00,
        "emotion": "neutral",
        "pause_style": "保持旧 B 停顿感",
        "text": SAMPLE_TEXT,
    },
    {
        "sample_id": "V2_prosody_optimized",
        "goal": "音色不变，优化停顿、句尾、上扬",
        "speed": 1.02,
        "emotion": "neutral",
        "pause_style": "语义边界更清楚",
        "text": (
            "朋友们，现在做带货，最贵的不是拍视频。\n\n"
            "最贵的是，前面测错商品的成本。\n\n"
            "所以我不会让 AI 直接说，哪个品能爆。\n"
            "我会先让它把商品卡拆成表，把风险写出来，再决定要不要继续测。"
        ),
    },
    {
        "sample_id": "V3_emotion_rich",
        "goal": "音色不变，增加轻吐槽、判断感、自然起伏",
        "speed": 1.00,
        "emotion": "happy",
        "pause_style": "关键句更有空间",
        "text": (
            "朋友们，现在做带货，最贵的不是拍视频。\n\n"
            "最贵的是，前面测错商品的成本。\n"
            "所以我不会让 AI 直接说，哪个品能爆。\n\n"
            "我会先让它把商品卡拆成表，把风险写出来，再决定要不要继续测。"
        ),
    },
]

OFFICIAL_BAILIAN_DOCS = [
    "https://help.aliyun.com/zh/model-studio/mini-clone-api",
]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Use Aliyun Bailian proxy to clone old-B reference audio into MiniMax short samples."
    )
    parser.add_argument(
        "--timestamp",
        default=DEFAULT_TIMESTAMP,
        help="Timestamp suffix. Defaults to current YYYYMMDD_HHMMSS.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="HTTP request timeout in seconds.",
    )
    parser.add_argument(
        "--signed-url-expires",
        type=int,
        default=3600,
        help="OSS signed GET URL expiry seconds. URL query is never written to reports.",
    )
    parser.add_argument(
        "--skip-api",
        action="store_true",
        help="Build a capability report without calling Bailian MiniMax APIs.",
    )
    return parser.parse_args(argv)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _nested_get(payload: dict[str, Any], *keys: str) -> Any:
    current: Any = payload
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def read_wave_info(path: Path) -> dict[str, Any]:
    info: dict[str, Any] = {"path": rel(path), "exists": path.exists(), "decode_ok": False}
    if not path.exists():
        return info
    with wave.open(str(path), "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        info.update(
            {
                "decode_ok": True,
                "size_bytes": path.stat().st_size,
                "channels": wav_file.getnchannels(),
                "sample_rate": rate,
                "frames": frames,
                "duration_seconds": round(frames / rate, 3) if rate else 0,
                "sample_width_bytes": wav_file.getsampwidth(),
                "format": "wav",
            }
        )
    return info


def load_runtime_config() -> dict[str, Any]:
    return load_formal_config(FORMAL_EXAMPLE_CONFIG, DEFAULT_FORMAL_LOCAL_CONFIG_PATH)


def load_bailian_key(config: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    env_names = [
        "DASHSCOPE_API_KEY",
        "BAILIAN_API_KEY",
        "ALIYUN_BAILIAN_API_KEY",
        "ALIYUN_API_KEY",
    ]
    for env_name in env_names:
        value = os.environ.get(env_name, "").strip()
        if value:
            return value, f"process_env:{env_name}", {
                "auth_key_present": True,
                "detected_env_name": env_name,
                "detected_source": f"process_env:{env_name}",
                "authorized_runtime_config_checked": False,
                "api_key_printed": False,
                "api_key_written": False,
            }

    runtime_key = str(_nested_get(config, "auth", "api_key") or "").strip()
    return runtime_key, (
        "authorized_runtime_config:formal_api_demo.local.toml" if runtime_key else "none"
    ), {
        "auth_key_present": bool(runtime_key),
        "detected_env_name": "authorized_runtime_config:[auth].api_key" if runtime_key else "",
        "detected_source": "authorized_runtime_config:formal_api_demo.local.toml"
        if runtime_key
        else "none",
        "authorized_runtime_config_checked": True,
        "authorized_runtime_config_exists": DEFAULT_FORMAL_LOCAL_CONFIG_PATH.exists(),
        "authorized_runtime_config_in_repo": False,
        "api_key_printed": False,
        "api_key_written": False,
    }


def sanitize_text(text: str, secrets: list[str]) -> str:
    sanitized = text
    for secret in secrets:
        if secret:
            sanitized = sanitized.replace(secret, "[REDACTED_SECRET]")
    sanitized = re.sub(r"sk-[A-Za-z0-9_\-]{8,}", "[REDACTED_SECRET]", sanitized)
    sanitized = re.sub(r"Bearer\s+[A-Za-z0-9._\-]+", "Bearer [REDACTED_SECRET]", sanitized)
    sanitized = re.sub(
        r"(OSSAccessKeyId" + r"=)[^&\s]+",
        r"\1[REDACTED_OSS_ACCESS_KEY_ID]",
        sanitized,
    )
    sanitized = re.sub(r"(Signature" + r"=)[^&\s]+", r"\1[REDACTED_SIGNATURE]", sanitized)
    return sanitized


def redact_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    redacted_query = "[REDACTED_SIGNED_QUERY]" if parsed.query else ""
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, redacted_query, ""))


def post_json(
    url: str,
    key: str,
    payload: dict[str, Any],
    timeout: int,
    secrets: list[str],
) -> dict[str, Any]:
    started = time.time()
    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            timeout=timeout,
        )
    except requests.RequestException as exc:
        return {
            "ok": False,
            "http_status_code": None,
            "elapsed_seconds": round(time.time() - started, 3),
            "json": {},
            "error_sanitized": sanitize_text(str(exc), secrets),
        }
    try:
        data = response.json()
    except ValueError:
        data = {"raw_text": response.text[:1200]}
    return {
        "ok": True,
        "http_status_code": response.status_code,
        "elapsed_seconds": round(time.time() - started, 3),
        "json": data,
    }


def dashscope_base_resp(data: dict[str, Any]) -> dict[str, Any]:
    output = data.get("output") if isinstance(data.get("output"), dict) else {}
    base_resp = output.get("base_resp") if isinstance(output.get("base_resp"), dict) else {}
    return base_resp


def extract_dashscope_audio(data: dict[str, Any]) -> tuple[str, dict[str, Any], str, str]:
    output = data.get("output") if isinstance(data.get("output"), dict) else {}
    base_resp = output.get("base_resp") if isinstance(output.get("base_resp"), dict) else {}
    payload = output.get("data") if isinstance(output.get("data"), dict) else {}
    audio_hex = payload.get("audio") if isinstance(payload.get("audio"), str) else ""
    extra_info = output.get("extra_info") if isinstance(output.get("extra_info"), dict) else {}
    trace_id = output.get("trace_id") if isinstance(output.get("trace_id"), str) else ""
    return audio_hex, extra_info, trace_id, str(base_resp.get("status_msg", ""))


def write_audio_hex(path: Path, audio_hex: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        audio_bytes = bytes.fromhex(audio_hex)
    except ValueError as exc:
        raise RuntimeError("audio_hex_decode_failed") from exc
    if not audio_bytes:
        raise RuntimeError("empty_audio_bytes")
    path.write_bytes(audio_bytes)


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def ffprobe_audio(path: Path) -> dict[str, Any]:
    result = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    if result.returncode != 0:
        return {"passed": False, "stderr": result.stderr[-1000:]}
    data = json.loads(result.stdout)
    audio_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    duration = float(data.get("format", {}).get("duration") or (audio_stream or {}).get("duration") or 0)
    return {
        "passed": bool(audio_stream),
        "duration_seconds": round(duration, 3),
        "codec_name": audio_stream.get("codec_name") if audio_stream else "",
        "sample_rate": int(audio_stream.get("sample_rate", 0)) if audio_stream else 0,
        "channels": int(audio_stream.get("channels", 0)) if audio_stream else 0,
        "bit_rate": data.get("format", {}).get("bit_rate", ""),
        "file_size_bytes": path.stat().st_size,
    }


def ffmpeg_decode(path: Path) -> dict[str, Any]:
    result = run_command(["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"])
    return {"passed": result.returncode == 0, "stderr_tail": result.stderr[-1000:]}


def non_silent_check(path: Path) -> dict[str, Any]:
    result = run_command(["ffmpeg", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"])
    text = result.stderr
    match = re.search(r"mean_volume:\s+(-?inf|-?\d+(?:\.\d+)?) dB", text)
    mean_volume = match.group(1) if match else ""
    passed = bool(mean_volume and mean_volume != "-inf")
    return {"passed": passed, "mean_volume_db": mean_volume, "stderr_tail": text[-1200:]}


def validate_audio(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"passed": False, "reason": "file_missing", "non_silent": False}
    probe = ffprobe_audio(path)
    decode = ffmpeg_decode(path)
    non_silent = non_silent_check(path)
    return {
        "passed": bool(probe.get("passed") and decode.get("passed") and non_silent.get("passed")),
        "ffprobe": probe,
        "decode": decode,
        "non_silent_check": {
            "passed": non_silent.get("passed"),
            "mean_volume_db": non_silent.get("mean_volume_db"),
        },
        "non_silent": bool(non_silent.get("passed")),
    }


def upload_reference_audio(
    path: Path,
    *,
    config: dict[str, Any],
    run_id: str,
    expires_seconds: int,
    reference_id: str,
) -> dict[str, Any]:
    object_key = _build_object_key(
        _nested_get(config, "aliyun_oss", "prefix_temp")
        or _nested_get(config, "aliyun_oss", "prefix_raw")
        or "video-factory/tmp",
        run_id,
        f"old_b_to_minimax_bailian/reference_audio/{reference_id}_{path.name}",
    )
    _upload_file_to_oss(path, object_key, config)
    signed_url = _build_oss_signed_get_url(config, object_key, expires_seconds)
    return {
        "reference_audio_id": reference_id,
        "local_path": rel(path),
        "uploaded": True,
        "object_key": object_key,
        "audio_url": signed_url,
        "audio_url_redacted": redact_url(signed_url),
        "audio_url_logged": False,
        "file_id": None,
    }


def call_voice_clone(
    *,
    key: str,
    audio_url: str,
    requested_voice_id: str,
    text: str,
    output_path: Path,
    timeout: int,
    secrets: list[str],
) -> dict[str, Any]:
    payload = {
        "model": DASHSCOPE_MODEL,
        "input": {
            "action": "voice_clone",
            "voice_id": requested_voice_id,
            "audio_url": audio_url,
            "text": text.replace("\n", " "),
            "need_noise_reduction": True,
            "need_volume_normalization": True,
            "language_boost": "Chinese",
            "aigc_watermark": False,
        },
    }
    result = post_json(DASHSCOPE_MINIMAX_ENDPOINT, key, payload, timeout, secrets)
    data = result.get("json", {})
    base_resp = dashscope_base_resp(data)
    output = data.get("output") if isinstance(data.get("output"), dict) else {}
    status_code = base_resp.get("status_code")
    voice_id = output.get("voice_id") if isinstance(output.get("voice_id"), str) else ""
    demo_audio = output.get("demo_audio") if isinstance(output.get("demo_audio"), str) else ""
    if result.get("http_status_code") != 200 or status_code not in (0, None) or not demo_audio:
        return {
            "ok": False,
            "http_status_code": result.get("http_status_code"),
            "base_resp_status_code": status_code,
            "base_resp_status_msg": base_resp.get("status_msg"),
            "request_id": data.get("request_id"),
            "elapsed_seconds": result.get("elapsed_seconds"),
            "error_sanitized": sanitize_text(json.dumps(data, ensure_ascii=False)[:1600], secrets),
        }
    voice_id = voice_id or requested_voice_id

    if demo_audio.startswith("http://") or demo_audio.startswith("https://"):
        with urllib.request.urlopen(demo_audio, timeout=timeout) as response:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(response.read())
    elif re.fullmatch(r"[0-9a-fA-F]+", demo_audio or ""):
        write_audio_hex(output_path, demo_audio)
    else:
        return {
            "ok": False,
            "http_status_code": result.get("http_status_code"),
            "base_resp_status_code": status_code,
            "base_resp_status_msg": "voice_clone_succeeded_but_demo_audio_missing",
            "request_id": data.get("request_id"),
            "elapsed_seconds": result.get("elapsed_seconds"),
            "generated_voice_id": voice_id,
        }

    return {
        "ok": True,
        "http_status_code": result.get("http_status_code"),
        "base_resp_status_code": status_code,
        "base_resp_status_msg": base_resp.get("status_msg"),
        "request_id": data.get("request_id"),
        "elapsed_seconds": result.get("elapsed_seconds"),
        "generated_voice_id": voice_id,
        "sample_path": rel(output_path),
        "demo_audio_url_redacted": redact_url(demo_audio),
    }


def call_tts(
    *,
    key: str,
    voice_id: str,
    text: str,
    speed: float,
    emotion: str,
    output_path: Path,
    timeout: int,
    secrets: list[str],
) -> dict[str, Any]:
    payload = {
        "model": DASHSCOPE_MODEL,
        "input": {
            "text": text,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": speed,
                "vol": 1,
                "pitch": 0,
                "emotion": emotion,
            },
            "audio_setting": {
                "sample_rate": 32000,
                "bitrate": 128000,
                "format": "mp3",
                "channel": 1,
            },
            "language_boost": "Chinese",
            "output_format": "hex",
            "subtitle_enable": False,
            "aigc_watermark": False,
        },
    }
    result = post_json(DASHSCOPE_MINIMAX_ENDPOINT, key, payload, timeout, secrets)
    data = result.get("json", {})
    base_resp = dashscope_base_resp(data)
    audio_hex, extra_info, trace_id, status_msg = extract_dashscope_audio(data)
    if result.get("http_status_code") != 200 or base_resp.get("status_code") != 0 or not audio_hex:
        return {
            "ok": False,
            "http_status_code": result.get("http_status_code"),
            "base_resp_status_code": base_resp.get("status_code"),
            "base_resp_status_msg": status_msg or base_resp.get("status_msg"),
            "trace_id": trace_id,
            "elapsed_seconds": result.get("elapsed_seconds"),
            "error_sanitized": sanitize_text(json.dumps(data, ensure_ascii=False)[:1600], secrets),
        }
    try:
        write_audio_hex(output_path, audio_hex)
    except (RuntimeError, binascii.Error) as exc:
        return {
            "ok": False,
            "base_resp_status_msg": str(exc),
            "trace_id": trace_id,
            "elapsed_seconds": result.get("elapsed_seconds"),
        }
    return {
        "ok": True,
        "http_status_code": result.get("http_status_code"),
        "base_resp_status_code": base_resp.get("status_code"),
        "base_resp_status_msg": status_msg,
        "trace_id": trace_id,
        "elapsed_seconds": result.get("elapsed_seconds"),
        "sample_path": rel(output_path),
        "extra_info": extra_info,
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    output_dir = OUTPUT_ROOT / f"old_b_to_minimax_bailian_{args.timestamp}"
    samples_dir = output_dir / "samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    run_id = f"old-b-to-minimax-bailian-{args.timestamp}"

    config_bundle = load_runtime_config()
    config = config_bundle["config"]
    key, key_source, auth_check = load_bailian_key(config)
    secrets = [key]
    reference_audio_probe = [read_wave_info(REFERENCE_AUDIO_1), read_wave_info(REFERENCE_AUDIO_2)]
    reference_audio_loaded = all(item.get("decode_ok") for item in reference_audio_probe)
    oss_config_present = all(
        bool(_nested_get(config, "aliyun_oss", field))
        for field in ("bucket", "endpoint", "bucket_domain", "access_key_id", "access_key_secret")
    )

    report: dict[str, Any] = {
        "task_result": {
            "status": "blocked",
            "video_generated": False,
            "audio_generated": False,
            "tts_api_called": False,
            "copy_changed": False,
            "current_video_modified": False,
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "output_dir": rel(output_dir),
        "auth_route_recheck": {
            "previous_blocker": "minimax_official_api_key_missing",
            "user_correction": "use_aliyun_bailian_api_key",
            "should_require_minimax_official_key": False,
            "selected_auth_route": "aliyun_bailian_proxy_to_minimax",
            "aliyun_bailian_auth_available": bool(key),
            "detected_env_name": auth_check.get("detected_env_name", ""),
            "detected_source": auth_check.get("detected_source", key_source),
            "api_key_printed": False,
            "api_key_written": False,
        },
        "route_arbitration": {
            "old_qwen_role": "reference_anchor_only",
            "minimax_role": "final_generation_provider",
            "auth_route": "aliyun_bailian_proxy_to_minimax",
            "selected_route": "old_b_to_minimax_via_aliyun_bailian",
            "system_voice_candidates_allowed": False,
            "old_qwen_formal_route_allowed": False,
        },
        "aliyun_bailian_auth_check": {
            **auth_check,
            "can_call_bailian_proxy": False,
        },
        "bailian_minimax_clone_capability": {
            "supports_minimax_tts": True,
            "supports_reference_audio": True,
            "supports_voice_clone": True,
            "accepts_local_file": False,
            "requires_audio_url": True,
            "supports_file_upload": False,
            "returns_voice_id": False,
            "accepts_requested_voice_id": True,
            "generated_voice_id_source": "input.voice_id accepted; output.voice_id not echoed in the 20260528 call",
            "evidence_path": OFFICIAL_BAILIAN_DOCS,
            "evidence_summary": "阿里百炼 MiniMax 语音克隆 API 使用 DashScope endpoint，input.action=voice_clone，audio_url 必须是 http/https URL；本轮成功响应返回 output.demo_audio，但未回显 output.voice_id，因此使用请求体 input.voice_id 作为 generated_minimax_voice_id。",
        },
        "reference_audio_probe": reference_audio_probe,
        "reference_audio_inputs": [],
        "reference_audio_upload_authorized": True,
        "current_audio_url_available": False,
        "audio_url_created": False,
        "generated_minimax_voice_id": None,
        "upload_strategy": {
            "selected": "upload_to_user_controlled_oss",
            "reason": "百炼 MiniMax clone 需要 audio_url；项目已有用户可控 OSS 配置时上传参考音频并生成签名 URL，报告只写脱敏 URL。",
            "audio_url_created": False,
            "file_id_created": False,
            "reference_audio_committed_to_git": False,
        },
        "generated_samples": [],
        "old_b_to_minimax_voice_lock": {
            "status": "pending_bailian_clone_generation",
            "old_b_reference_audio_path": [rel(REFERENCE_AUDIO_1), rel(REFERENCE_AUDIO_2)],
            "old_b_reference_voice_masked_id": "qwen-t...ac19",
            "target_provider": "minimax",
            "target_model": DASHSCOPE_MODEL,
            "auth_route": "aliyun_bailian_proxy_to_minimax",
            "generated_minimax_voice_id": None,
            "timbre_similarity_required": True,
            "prosody_optimization_allowed": True,
            "emotion_optimization_allowed": True,
            "timbre_change_allowed": False,
            "system_voice_substitution_allowed": False,
            "human_voice_review_required": True,
            "human_voice_review_status": "pending_user_review",
        },
        "status_boundary": {
            "full_narration_regenerated": False,
            "current_video_modified": False,
            "copy_changed": False,
            "voice_validation": "not_advanced",
            "send_ready": False,
        },
        "blocked_detail": {
            "blocked_reason": [],
            "next_required_user_action": "",
            "forbidden_fallback": [
                "MiniMax 系统音色候选",
                "旧 Qwen 正式路线",
                "macOS say",
                "Serena",
                "本地 TTS",
            ],
        },
    }

    blocked_reasons: list[str] = []
    if not reference_audio_loaded:
        blocked_reasons.append("reference_audio_unreadable")
    if not key:
        blocked_reasons.append("aliyun_bailian_auth_missing")
    if not oss_config_present:
        blocked_reasons.append("oss_audio_url_upload_config_missing")
    if args.skip_api:
        blocked_reasons.append("api_call_skipped_by_flag")

    if blocked_reasons:
        report["blocked_detail"]["blocked_reason"] = blocked_reasons
        if "aliyun_bailian_auth_missing" in blocked_reasons:
            report["blocked_detail"]["next_required_user_action"] = (
                "配置阿里百炼 / DashScope API Key；不需要 MINIMAX_API_KEY。"
            )
        elif "oss_audio_url_upload_config_missing" in blocked_reasons:
            report["blocked_detail"]["next_required_user_action"] = (
                "补齐用户可控 OSS 上传配置或提供可访问 audio_url。"
            )
        report["old_b_to_minimax_voice_lock"]["status"] = "blocked_before_generation"
        return report

    try:
        reference_inputs = [
            upload_reference_audio(
                REFERENCE_AUDIO_1,
                config=config,
                run_id=run_id,
                expires_seconds=args.signed_url_expires,
                reference_id="reference_audio_1",
            ),
            upload_reference_audio(
                REFERENCE_AUDIO_2,
                config=config,
                run_id=run_id,
                expires_seconds=args.signed_url_expires,
                reference_id="reference_audio_2",
            ),
        ]
    except CloudAssemblyError as exc:
        report["blocked_detail"]["blocked_reason"] = [exc.failure_reason or "reference_audio_upload_failed"]
        report["blocked_detail"]["next_required_user_action"] = (
            "检查用户可控 OSS 上传权限；不回退系统音色。"
        )
        report["upload_strategy"]["upload_error_sanitized"] = sanitize_text(str(exc), secrets)
        report["old_b_to_minimax_voice_lock"]["status"] = "blocked_reference_audio_upload_failed"
        return report

    report["reference_audio_inputs"] = [
        {key_: value for key_, value in item.items() if key_ != "audio_url"}
        for item in reference_inputs
    ]
    report["upload_strategy"]["audio_url_created"] = True
    report["current_audio_url_available"] = True
    report["audio_url_created"] = True

    requested_voice_id = f"oldBMinimax{args.timestamp.replace('_', '')}"
    clone_output_path = samples_dir / "V1_identity_match.mp3"
    clone_result = call_voice_clone(
        key=key,
        audio_url=reference_inputs[0]["audio_url"],
        requested_voice_id=requested_voice_id,
        text=SAMPLE_SPECS[0]["text"],
        output_path=clone_output_path,
        timeout=args.timeout,
        secrets=secrets + [reference_inputs[0]["audio_url"], reference_inputs[1]["audio_url"]],
    )
    report["task_result"]["tts_api_called"] = True
    report["aliyun_bailian_auth_check"]["can_call_bailian_proxy"] = bool(
        clone_result.get("http_status_code") == 200
    )

    if not clone_result.get("ok"):
        report["blocked_detail"]["blocked_reason"] = ["bailian_proxy_minimax_voice_clone_call_failed"]
        report["blocked_detail"]["next_required_user_action"] = (
            "百炼代理 clone 调用失败；需检查账号是否开通 MiniMax 语音克隆或 audio_url 访问策略。"
        )
        report["bailian_minimax_clone_capability"]["last_call_result"] = clone_result
        report["old_b_to_minimax_voice_lock"]["status"] = "blocked_bailian_clone_failed"
        return report

    generated_voice_id = str(clone_result.get("generated_voice_id") or requested_voice_id)
    report["generated_minimax_voice_id"] = generated_voice_id
    clone_validation = validate_audio(clone_output_path)
    samples = [
        {
            **SAMPLE_SPECS[0],
            "sample_path": rel(clone_output_path),
            "generated_voice_id": generated_voice_id,
            "generated_minimax_voice_id": generated_voice_id,
            "target_provider": "minimax",
            "target_model": DASHSCOPE_MODEL,
            "auth_route": "aliyun_bailian_proxy_to_minimax",
            "reference_audio_used": True,
            "reference_audio_id": "reference_audio_1",
            "prosody_version": "V1_identity_match",
            "voice_setting": {
                "voice_id": generated_voice_id,
                "speed": SAMPLE_SPECS[0]["speed"],
                "pitch": 0,
                "emotion": SAMPLE_SPECS[0]["emotion"],
                "vol": 1,
            },
            "same_voice_id_required": True,
            "timbre_change_allowed": False,
            "generation_call": {
                "ok": clone_result.get("ok"),
                "request_id": clone_result.get("request_id"),
                "base_resp_status_code": clone_result.get("base_resp_status_code"),
                "base_resp_status_msg": clone_result.get("base_resp_status_msg"),
                "elapsed_seconds": clone_result.get("elapsed_seconds"),
            },
            "audio_validation": clone_validation,
            "non_silent": clone_validation.get("non_silent"),
            "status": "generated" if clone_validation.get("passed") else "generated_but_validation_failed",
        }
    ]

    for spec in SAMPLE_SPECS[1:]:
        time.sleep(1)
        output_path = samples_dir / f"{spec['sample_id']}.mp3"
        tts_result = call_tts(
            key=key,
            voice_id=generated_voice_id,
            text=spec["text"],
            speed=float(spec["speed"]),
            emotion=str(spec["emotion"]),
            output_path=output_path,
            timeout=args.timeout,
            secrets=secrets + [reference_inputs[0]["audio_url"], reference_inputs[1]["audio_url"]],
        )
        validation = validate_audio(output_path) if tts_result.get("ok") else {
            "passed": False,
            "non_silent": False,
        }
        samples.append(
            {
                **spec,
                "sample_path": rel(output_path) if output_path.exists() else None,
                "generated_voice_id": generated_voice_id,
                "generated_minimax_voice_id": generated_voice_id,
                "target_provider": "minimax",
                "target_model": DASHSCOPE_MODEL,
                "auth_route": "aliyun_bailian_proxy_to_minimax",
                "reference_audio_used": True,
                "reference_audio_id": "reference_audio_1",
                "prosody_version": spec["sample_id"],
                "voice_setting": {
                    "voice_id": generated_voice_id,
                    "speed": spec["speed"],
                    "pitch": 0,
                    "emotion": spec["emotion"],
                    "vol": 1,
                },
                "same_voice_id_required": True,
                "timbre_change_allowed": False,
                "generation_call": {
                    key_: value
                    for key_, value in tts_result.items()
                    if key_ not in {"error_sanitized", "extra_info"}
                },
                "error_sanitized": tts_result.get("error_sanitized", ""),
                "audio_validation": validation,
                "non_silent": validation.get("non_silent"),
                "status": "generated"
                if tts_result.get("ok") and validation.get("passed")
                else "generation_failed",
            }
        )

    report["generated_samples"] = samples
    all_generated = all(item.get("status") == "generated" for item in samples)
    all_non_silent = all(bool(item.get("non_silent")) for item in samples)
    if all_generated and all_non_silent:
        report["task_result"]["status"] = "completed_with_old_b_minimax_samples_via_bailian"
        report["task_result"]["audio_generated"] = True
        report["old_b_to_minimax_voice_lock"]["status"] = "pending_user_review"
        report["old_b_to_minimax_voice_lock"]["generated_minimax_voice_id"] = generated_voice_id
        report["blocked_detail"]["blocked_reason"] = []
        report["blocked_detail"]["next_required_user_action"] = "试听 V1/V2/V3，选择一个或全部拒绝。"
    else:
        report["blocked_detail"]["blocked_reason"] = ["sample_generation_or_non_silent_validation_failed"]
        report["blocked_detail"]["next_required_user_action"] = (
            "检查失败样本的 generation_call / audio_validation；不得回退系统音色。"
        )
        report["old_b_to_minimax_voice_lock"]["status"] = "blocked_sample_generation_failed"
        report["old_b_to_minimax_voice_lock"]["generated_minimax_voice_id"] = generated_voice_id
    return report


def render_markdown(report: dict[str, Any]) -> str:
    refs = "\n".join(
        f"- `{item['path']}`: exists={item['exists']}, decode_ok={item['decode_ok']}, "
        f"duration={item.get('duration_seconds')}, sample_rate={item.get('sample_rate')}"
        for item in report["reference_audio_probe"]
    )
    uploads = "\n".join(
        f"- `{item['reference_audio_id']}`: uploaded={item['uploaded']}, "
        f"audio_url={item.get('audio_url_redacted')}, file_id={item.get('file_id')}"
        for item in report.get("reference_audio_inputs", [])
    ) or "- 未上传"
    samples = "\n".join(
        f"| {item.get('sample_id')} | {item.get('status')} | {item.get('generated_minimax_voice_id')} | "
        f"`{item.get('sample_path')}` | {item.get('non_silent')} | {item.get('prosody_version')} |"
        for item in report.get("generated_samples", [])
    ) or "| - | - | - | - | - | - |"
    blocked = ", ".join(report["blocked_detail"].get("blocked_reason") or [])
    return f"""# 旧 B 到 MiniMax 百炼代理迁移报告

## 任务结果

```text
status: {report['task_result']['status']}
audio_generated: {str(report['task_result']['audio_generated']).lower()}
tts_api_called: {str(report['task_result']['tts_api_called']).lower()}
video_generated: false
copy_changed: false
current_video_modified: false
```

## 授权路线复核

- `previous_blocker`: `minimax_official_api_key_missing`
- `should_require_minimax_official_key`: `false`
- `selected_auth_route`: `aliyun_bailian_proxy_to_minimax`
- `aliyun_bailian_auth_available`: `{report['auth_route_recheck']['aliyun_bailian_auth_available']}`
- `detected_env_name`: `{report['auth_route_recheck']['detected_env_name']}`
- `api_key_printed`: `false`
- `api_key_written`: `false`

## 百炼 MiniMax 克隆能力

- `supports_minimax_tts`: `true`
- `supports_reference_audio`: `true`
- `supports_voice_clone`: `true`
- `accepts_local_file`: `false`
- `requires_audio_url`: `true`
- `supports_file_upload`: `false`
- `returns_voice_id`: `{report['bailian_minimax_clone_capability']['returns_voice_id']}`
- `accepts_requested_voice_id`: `{report['bailian_minimax_clone_capability']['accepts_requested_voice_id']}`
- `evidence_path`: `{', '.join(report['bailian_minimax_clone_capability']['evidence_path'])}`

## 参考音频读取

{refs}

## 上传输入

{uploads}

## 样本状态

| sample_id | status | generated_minimax_voice_id | sample_path | non_silent | prosody_version |
| --- | --- | --- | --- | --- | --- |
{samples}

## 状态边界

- `full_narration_regenerated`: `false`
- `current_video_modified`: `false`
- `copy_changed`: `false`
- `voice_validation`: `not_advanced`
- `send_ready`: `false`
- `system_voice_candidates_allowed`: `false`
- `old_qwen_formal_route_allowed`: `false`

## 阻断 / 下一步

- `blocked_reason`: `{blocked}`
- `next_required_user_action`: `{report['blocked_detail'].get('next_required_user_action', '')}`

用户下一步只需要试听已生成样本，选择一个候选或全部拒绝；未经试听确认，不能写 `user_confirmed`。
"""


def render_review_table(report: dict[str, Any]) -> str:
    rows = "\n".join(
        "| {sample_id} | {voice_id} | `{sample_path}` | {prosody_version} | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待用户选择 | pending_user_review |".format(
            sample_id=item.get("sample_id"),
            voice_id=item.get("generated_minimax_voice_id") or "-",
            sample_path=item.get("sample_path") or "-",
            prosody_version=item.get("prosody_version") or "-",
        )
        for item in report.get("generated_samples", [])
    ) or "| - | - | - | - | - | - | - | - | - | - | - | blocked |"
    return """# voice_candidate_review_table_old_b_minimax

本表只用于旧 B 参考音频迁移到 MiniMax 后的人工试听复审。所有样本必须以旧 B 音色相似度为第一判断，不能把系统音色、男声方向或情绪更强直接等同于旧 B。

| candidate_id（候选 ID） | voice_id（声音 ID） | sample_path（试听路径） | prosody_version（韵律版本） | similar_to_old_b（是否像旧 B，待人工判断） | pause_feel（停顿感，待人工判断） | emotional_richness（情绪丰富度，待人工判断） | upward_tone（上扬感，待人工判断） | too_system_voice（是否系统音色替代，待人工判断） | non_silent（是否非静音，待复核） | user_choice（用户选择） | lock_status（锁定状态） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""" + rows + "\n"


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    output_dir = OUTPUT_ROOT / f"old_b_to_minimax_bailian_{args.timestamp}"
    report = build_report(args)
    write_json(output_dir / "old_b_to_minimax_bailian_report.json", report)
    write_text(output_dir / "old_b_to_minimax_bailian_report.md", render_markdown(report))
    write_text(output_dir / "voice_candidate_review_table_old_b_minimax.md", render_review_table(report))
    write_json(
        output_dir / "voice_candidate_review_table_old_b_minimax.json",
        {
            "status": "pending_user_review"
            if report["task_result"]["status"] == "completed_with_old_b_minimax_samples_via_bailian"
            else "blocked",
            "generated_voice_id": report["old_b_to_minimax_voice_lock"].get(
                "generated_minimax_voice_id"
            ),
            "candidates": report.get("generated_samples", []),
        },
    )
    print(
        json.dumps(
            {
                "status": report["task_result"]["status"],
                "output_dir": rel(output_dir),
                "generated_voice_id": report["old_b_to_minimax_voice_lock"].get(
                    "generated_minimax_voice_id"
                ),
                "blocked_reason": report["blocked_detail"].get("blocked_reason", []),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
