from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import shutil
import subprocess
import time
import wave
from typing import Any

import requests
import websockets


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATE = "20260427"
OUTPUT_DIR = ROOT / "dist" / "voice_trials" / f"{DATE}_十五秒文案语速停顿试配_15s_copy_pacing_trial"

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000

VERSION_SPECS = {
    "A": {
        "label": "15秒文案_自然节奏",
        "text_file": "A_15秒文案_自然节奏.txt",
        "raw_audio_file": "A_15秒文案_自然节奏_API原始.wav",
        "audio_file": "A_15秒文案_自然节奏.wav",
        "request_debug_file": "A_voice_clone_tts_request_debug_sanitized.json",
        "text": (
            "我发现，做方案最痛苦的不是 PPT。\n"
            "是你坐了一下午，资料开着，咖啡也开着，就第一行没开。\n"
            "最后憋出一句：建议提升用户体验。\n"
            "它永远不会错，也永远没用。\n"
            "Prompt 调对，豆包才给能接着改的初稿。"
        ),
        "instructions": (
            "请参考新样本2的说话方式，保持自然口语、真人分享感和解释型节奏。\n"
            "语气平实亲近，不要播音腔，不要广告腔，不要刻意表演。\n"
            "整体节奏稍微利落一点，但不要赶。\n"
            "重点句“永远不会错，也永远没用”要有一点轻吐槽感。\n"
            "请控制在 15 秒左右自然说完。"
        ),
        "style_goal": "更直接，信息更清楚，微反转保留，用于判断短内容自然度。",
    },
    "B": {
        "label": "15秒文案_停顿梗感",
        "text_file": "B_15秒文案_停顿梗感.txt",
        "raw_audio_file": "B_15秒文案_停顿梗感_API原始.wav",
        "audio_file": "B_15秒文案_停顿梗感.wav",
        "request_debug_file": "B_voice_clone_tts_request_debug_sanitized.json",
        "text": (
            "你以为做方案慢，是 PPT 难。\n"
            "其实不是，是你在陪资料加班。\n"
            "屏幕开着，文档开着，第一行死活不动。\n"
            "你问豆包写方案，它也努力，给一堆看着像方案、用起来像空气的东西。\n"
            "Prompt 调对，才有能接着改的初稿。"
        ),
        "instructions": (
            "请参考新样本2的说话方式，保持自然口语、轻吐槽和熟人式分享感。\n"
            "语气不要太嗨，不要夸张带货，不要综艺腔。\n"
            "“陪资料加班”“看着像方案，用起来像空气”这些地方可以稍微停一下，让梗自然落地。\n"
            "整体控制在 15 到 17 秒之间，停顿清楚，但不要拖沓。"
        ),
        "style_goal": "停顿更清楚，梗感略强，用于判断轻吐槽和留白是否适配声音。",
    },
}

FORBIDDEN_COPY_TERMS = [
    "从哪打",
    "开门钥匙",
    "把路铲出来",
    "一团雾",
    "强势赋能",
    "精准击穿",
    "底层逻辑",
    "高效闭环",
    "抓手",
    "撬动",
]


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
            + "STDOUT:\n" + completed.stdout.rstrip() + "\n\n"
            + "STDERR:\n" + completed.stderr.rstrip() + "\n",
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


def validate_copy_texts() -> dict[str, Any]:
    results: dict[str, Any] = {}
    for version, spec in VERSION_SPECS.items():
        text = spec["text"]
        compact = "".join(text.split())
        forbidden_hits = [term for term in FORBIDDEN_COPY_TERMS if term in text]
        results[version] = {
            "character_count_without_whitespace": len(compact),
            "line_count": len(text.splitlines()),
            "forbidden_terms": forbidden_hits,
            "status": "通过" if not forbidden_hits and 70 <= len(compact) <= 125 else "需复核",
        }
        if forbidden_hits:
            raise RuntimeError(f"{version} 文案命中禁用词：{forbidden_hits}")
    return results


def write_text_files() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for spec in VERSION_SPECS.values():
        (OUTPUT_DIR / spec["text_file"]).write_text(spec["text"] + "\n", encoding="utf-8")


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
        item for item in voice_list
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
        raise RuntimeError(f"无法唯一确认当前新样本2 custom voice：matched_count={len(candidates)}")
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


async def synthesize_version(api_key: str, voice: str, version: str, spec: dict[str, str]) -> dict[str, Any]:
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    output_path = OUTPUT_DIR / spec["raw_audio_file"]
    started = time.time()
    async with websockets.connect(url, additional_headers=headers) as ws:
        session_update = {
            "type": "session.update",
            "session": {
                "mode": "commit",
                "voice": voice,
                "instructions": spec["instructions"],
                "optimize_instructions": True,
                "language_type": "Chinese",
                "response_format": "pcm",
                "sample_rate": SAMPLE_RATE,
            },
        }
        await ws.send(json.dumps(session_update, ensure_ascii=False))
        await recv_until_session_ready(ws, event_types)
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": " ".join(spec["text"].splitlines())}, ensure_ascii=False))
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
        "create_custom_voice_called": False,
        "instructions": spec["instructions"],
        "voice_trial_text": spec["text"],
        "tts_input_text": " ".join(spec["text"].splitlines()),
        "session_update": {
            "voice": "<custom_voice_masked>",
            "instructions": spec["instructions"],
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
        "version": version,
    }
    write_json(OUTPUT_DIR / spec["request_debug_file"], debug)
    return debug


def maybe_adjust_tempo(ffmpeg: str, version: str, spec: dict[str, str], raw_info: dict[str, Any]) -> dict[str, Any]:
    raw_path = OUTPUT_DIR / spec["raw_audio_file"]
    final_path = OUTPUT_DIR / spec["audio_file"]
    duration = float(raw_info["duration_seconds"])
    if 13.0 <= duration <= 18.0:
        shutil.copy2(raw_path, final_path)
        return {
            "applied": False,
            "reason": "API 原始输出已在 13-18 秒范围内",
            "raw_audio": read_wave_info(raw_path),
            "final_audio": read_wave_info(final_path),
        }

    target_duration = 15.0 if version == "A" else 16.0
    factor = max(0.5, min(2.0, duration / target_duration))
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
        OUTPUT_DIR / f"{version}_atempo_adjust.txt",
    )
    return {
        "applied": True,
        "reason": "API 原始输出不在 13-18 秒范围内，保留 API 原始文件并生成节奏校准试听版",
        "target_duration_seconds": target_duration,
        "atempo_factor": round(factor, 6),
        "raw_audio": read_wave_info(raw_path),
        "final_audio": read_wave_info(final_path),
    }


def validate_audio(ffmpeg: str, version: str, path: pathlib.Path) -> dict[str, Any]:
    decode_log = OUTPUT_DIR / f"{version}_ffmpeg_decode_check.txt"
    volume_log = OUTPUT_DIR / f"{version}_volumedetect.txt"
    loudnorm_log = OUTPUT_DIR / f"{version}_loudnorm_measure.txt"
    run_command([ffmpeg, "-hide_banner", "-y", "-i", str(path), "-f", "null", "-"], decode_log)
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    loudnorm = run_command(
        [ffmpeg, "-hide_banner", "-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        loudnorm_log,
    )
    info = read_wave_info(path)
    duration_ok = 13.0 <= float(info["duration_seconds"]) <= 18.0
    return {
        **info,
        "decode_status": "通过",
        "duration_range_status": "通过" if duration_ok else "失败",
        "volumedetect": parse_volumedetect(volume.stderr),
        "loudnorm": parse_loudnorm(loudnorm.stderr),
        "logs": {
            "decode": rel(decode_log),
            "volumedetect": rel(volume_log),
            "loudnorm": rel(loudnorm_log),
        },
    }


def build_readme(summary: dict[str, Any]) -> str:
    rows = []
    for version in ["A", "B"]:
        validation = summary["versions"][version]["validation"]
        rows.append(
            "| {version} | `{duration:.2f}s` | `{codec}` | `{sample_rate} Hz` | `{channels}` | `{mean}` | `{lufs}` | `{decode}` |".format(
                version=version,
                duration=validation["duration_seconds"],
                codec=validation["codec"],
                sample_rate=validation["sample_rate"],
                channels="mono" if validation["channels"] == 1 else validation["channels"],
                mean=validation.get("volumedetect", {}).get("mean_volume", "n/a"),
                lufs=validation.get("loudnorm", {}).get("input_i", "n/a"),
                decode=validation["decode_status"],
            )
        )
    return "\n".join(
        [
            "# 十五秒文案语速停顿试配 15s Copy Pacing Trial",
            "",
            "## 本轮目标",
            "",
            "- `已确认` 本轮只做《视频工厂》声音文案适配试听。",
            "- `已确认` 不换音色、不重做 voice cloning、不重新裁剪 / 上传样本、不替换全片音轨。",
            "- `已确认` 生成 A / B 两条 15 秒左右试听，用于判断语速、停顿和文案搭配。",
            "",
            "## 用户确认状态",
            "",
            "- 新样本2的音色底子可以继续用。",
            "- 后续主要调语速、停顿和文案搭配。",
            "- 用户喜欢“微反转 + 说话带梗 + 自然口语”。",
            "- 已避开 `下一步从哪打`，使用真人更自然的表达。",
            "",
            "## A / B 文案全文",
            "",
            "### A 版：自然节奏",
            "",
            "```text",
            VERSION_SPECS["A"]["text"],
            "```",
            "",
            "### B 版：停顿梗感",
            "",
            "```text",
            VERSION_SPECS["B"]["text"],
            "```",
            "",
            "## A / B 风格差异",
            "",
            "- A 版：更直接，信息更清楚，微反转保留，适合判断短内容自然度。",
            "- B 版：停顿更清楚，梗感略强，适合判断轻吐槽和留白是否适配声音。",
            "",
            "## model / voice / instructions",
            "",
            f"- synthesis model：`{TARGET_MODEL}`",
            f"- target_model：`{TARGET_MODEL}`",
            f"- create model：`{CREATE_MODEL}`（本轮未调用 create）",
            f"- voice：`{VOICE_MASKED}`（脱敏）",
            "- 是否重新 create_custom_voice：`no`",
            "- 是否使用 Serena：`no`",
            "- 是否使用上一轮 A / B custom voice：`no`",
            "- language_type：`Chinese`",
            "- response_format：`pcm`",
            "- sample_rate：`24000`",
            "- optimize_instructions：`true`",
            "",
            "### A instructions",
            "",
            "```text",
            VERSION_SPECS["A"]["instructions"],
            "```",
            "",
            "### B instructions",
            "",
            "```text",
            VERSION_SPECS["B"]["instructions"],
            "```",
            "",
            "## atempo",
            "",
            f"- A 版是否使用 atempo：`{str(summary['versions']['A']['tempo_adjustment']['applied']).lower()}`",
            f"- B 版是否使用 atempo：`{str(summary['versions']['B']['tempo_adjustment']['applied']).lower()}`",
            "",
            "## 输出文件路径",
            "",
            "- `A_15秒文案_自然节奏.txt`",
            "- `B_15秒文案_停顿梗感.txt`",
            "- `A_15秒文案_自然节奏.wav`",
            "- `B_15秒文案_停顿梗感.wav`",
            "- `A_voice_clone_tts_request_debug_sanitized.json`",
            "- `B_voice_clone_tts_request_debug_sanitized.json`",
            "- `run_summary.json`",
            "",
            "## 技术验证结果",
            "",
            "| 版本 | duration | codec | sample_rate | channels | mean_volume | loudnorm.input_i | ffmpeg 解码 |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## 当前状态",
            "",
            "- `technical_generation`：通过。",
            "- `copy_pacing_status`：待用户听审。",
            "- `voice_validation_status`：待用户 / ChatGPT 听感复审。",
            "- `content_validation`：待用户 / ChatGPT 最终复审。",
            "- `send_ready`：no。",
            "",
            "## 禁止误写",
            "",
            "- 本轮不等于声音通过。",
            "- 本轮不等于最终音色已定。",
            "- 本轮不等于文案最终定稿。",
            "- 本轮不可替换全片音轨。",
            "- 本轮不改变 `content_validation`。",
            "- 本轮不改变 `send_ready`。",
            "- 本轮未修改 `dist/latest_review_pack/full.mp4`。",
            "- 本轮未修改 `dist/latest_review_pack/middle_preview.mp4`。",
            "",
        ]
    )


async def main_async() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg = resolve_ffmpeg()
    api_key = load_api_key()
    copy_checks = validate_copy_texts()
    write_text_files()
    voice_resolution = resolve_existing_custom_voice(api_key)
    versions: dict[str, Any] = {}
    for version, spec in VERSION_SPECS.items():
        debug = await synthesize_version(api_key, voice_resolution["voice"], version, spec)
        tempo_adjustment = maybe_adjust_tempo(ffmpeg, version, spec, debug["output_audio"])
        validation = validate_audio(ffmpeg, version, OUTPUT_DIR / spec["audio_file"])
        if validation["duration_range_status"] != "通过":
            raise RuntimeError(f"{version} 输出时长不在 13-18 秒范围内：{validation['duration_seconds']}s")
        versions[version] = {
            "label": spec["label"],
            "style_goal": spec["style_goal"],
            "text": spec["text"],
            "text_file": rel(OUTPUT_DIR / spec["text_file"]),
            "instructions": spec["instructions"],
            "tts_debug": debug,
            "tempo_adjustment": tempo_adjustment,
            "validation": validation,
            "final_audio": rel(OUTPUT_DIR / spec["audio_file"]),
            "raw_audio": rel(OUTPUT_DIR / spec["raw_audio_file"]),
        }

    summary = {
        "run_date": DATE,
        "project": "视频工厂",
        "task": "十五秒文案语速停顿试配",
        "technical_generation": "通过",
        "copy_pacing_status": "待用户听审",
        "voice_validation_status": "待用户 / ChatGPT 听感复审",
        "content_validation": "待用户 / ChatGPT 最终复审",
        "full_content_validation": "待用户 / ChatGPT 最终复审",
        "send_ready": "no",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "create_model": CREATE_MODEL,
        "create_custom_voice_called": False,
        "voice_masked": VOICE_MASKED,
        "voice_resolution": {key: value for key, value in voice_resolution.items() if key != "voice"},
        "uses_serena": False,
        "uses_previous_ab_voice": False,
        "language_type": "Chinese",
        "response_format": "pcm",
        "sample_rate": SAMPLE_RATE,
        "optimize_instructions": True,
        "copy_checks": copy_checks,
        "versions": versions,
        "outputs": {
            "output_dir": rel(OUTPUT_DIR),
            "readme": rel(OUTPUT_DIR / "README.md"),
            "run_summary": rel(OUTPUT_DIR / "run_summary.json"),
            "custom_voice_list": rel(OUTPUT_DIR / "custom_voice_list_debug_sanitized.json"),
        },
        "forbidden_actions_preserved": {
            "modified_full_mp4": False,
            "modified_middle_preview_mp4": False,
            "replaced_full_audio_track": False,
            "generated_new_video_round": False,
            "create_custom_voice_called": False,
            "used_serena": False,
            "used_previous_ab_voice": False,
            "marked_voice_passed": False,
            "marked_content_validation_passed": False,
            "marked_send_ready_yes": False,
        },
    }
    (OUTPUT_DIR / "README.md").write_text(build_readme(summary), encoding="utf-8")
    write_json(OUTPUT_DIR / "run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main_async())
