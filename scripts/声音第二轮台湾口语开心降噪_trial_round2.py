from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import shutil
import subprocess
import sys
import time
import wave
from typing import Any

import requests
import websockets


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "dist" / "voice_trials" / "20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial"
PREVIOUS_TRIAL_DIR = ROOT / "dist" / "voice_trials" / "20260425_round28_voice_clone_trial"
CLONE_INPUT_PATH = PREVIOUS_TRIAL_DIR / "语音样本_复刻输入_10-20秒.wav"
CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
CURRENT_VOICE_MASK = "qwen-t...de43"
CURRENT_VOICE_SUFFIX = "de43"
B_PREFERRED_NAME = "vfr2tw0426c"
SAMPLE_RATE = 24000

VOICE_TRIAL_TEXT = """其实最花时间的，不是做汇报页啦。
是你一开始，第一句话就卡住了。
后来我换成调好的提示词，整个空转时间就少很多。
差别不在豆包本身，是那一段提示词真的有帮上忙。"""
TTS_INPUT_TEXT = " ".join(VOICE_TRIAL_TEXT.splitlines())

INSTRUCTIONS = """整体语气更开心、更轻快，像台湾女生在轻松带朋友看一个好用的小技巧。
声音要有笑意，句尾可以自然上扬，但不要夸张卖货，不要娃娃音，不要综艺腔。
节奏比上一版稍微活一点，停顿自然，听起来像真人分享，不像机器播报。
请使用自然的台湾普通话口吻，不要大陆播音腔。
发音自然、亲切、带一点笑意，不要刻意拖音。"""
DURATION_CONTROL_HINT = "请在不赶、不夸张的前提下，把这段控制在 14 秒左右讲完。"
SYNTHESIS_INSTRUCTIONS = INSTRUCTIONS + "\n" + DURATION_CONTROL_HINT

USER_FEEDBACK = [
    "情绪上面还不够开心的那种。",
    "需要把口语改成台湾的口音。",
    "现在生成的环境音有点吵，需要降噪。",
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
            + "STDOUT:\n" + completed.stdout + "\n\n"
            + "STDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def load_api_key() -> str:
    runtime_config = pathlib.Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    if not runtime_config.exists():
        raise RuntimeError("缺少运行时本地配置：/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    for line in runtime_config.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("api_key ="):
            value = stripped.split("=", 1)[1].strip().strip('"')
            if value and not value.startswith("SET_"):
                return value
    raise RuntimeError("运行时本地配置缺少真实 api_key")


def mask_voice(voice: str) -> str:
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


def write_json(path: pathlib.Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_wave_info(path: pathlib.Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
    return {
        "path": str(path.relative_to(ROOT)),
        "duration_seconds": round(frames / sample_rate, 3),
        "format": "wav",
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


def parse_volumedetect(log_text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in log_text.splitlines():
        if "mean_volume:" in line:
            result["mean_volume"] = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            result["max_volume"] = line.split("max_volume:", 1)[1].strip()
    return result


def parse_loudnorm(log_text: str) -> dict[str, Any]:
    start = log_text.rfind("{")
    end = log_text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return {}
    try:
        return json.loads(log_text[start : end + 1])
    except json.JSONDecodeError:
        return {}


def list_custom_voices(api_key: str) -> str:
    payload = {
        "model": CREATE_MODEL,
        "input": {"action": "list", "page_size": 20, "page_index": 0},
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
    voice_list = data.get("output", {}).get("voice_list", [])
    sanitized = {
        "status_code": response.status_code,
        "elapsed_seconds": elapsed,
        "request_id": data.get("request_id"),
        "voice_count": len(voice_list),
        "voices": [
            {
                "voice_masked": mask_voice(item.get("voice", "")),
                "target_model": item.get("target_model"),
                "gmt_create": item.get("gmt_create"),
            }
            for item in voice_list
        ],
    }
    write_json(OUTPUT_DIR / "custom_voice_list_debug_sanitized.json", sanitized)
    response.raise_for_status()
    for item in voice_list:
        voice = item.get("voice", "")
        if item.get("target_model") == TARGET_MODEL and voice.startswith("qwen-t") and voice.endswith(CURRENT_VOICE_SUFFIX):
            return voice
    raise RuntimeError(f"未能从 custom voice 列表匹配当前音色 {CURRENT_VOICE_MASK}")


def create_custom_voice(api_key: str, audio_path: pathlib.Path) -> str:
    audio_data = base64.b64encode(audio_path.read_bytes()).decode("ascii")
    payload = {
        "model": CREATE_MODEL,
        "input": {
            "action": "create",
            "target_model": TARGET_MODEL,
            "preferred_name": B_PREFERRED_NAME,
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
    data = response.json()
    output = data.get("output", {})
    voice = output.get("voice", "")
    sanitized = {
        "provider": "aliyun_bailian",
        "request_method": "POST",
        "endpoint": CREATE_ENDPOINT,
        "status_code": response.status_code,
        "elapsed_seconds": elapsed,
        "create_payload": {
            "model": CREATE_MODEL,
            "input": {
                "action": "create",
                "target_model": TARGET_MODEL,
                "preferred_name": B_PREFERRED_NAME,
                "audio": {"data": "data:audio/wav;base64,<omitted>"},
                "language": "zh",
            },
        },
        "input_audio": read_wave_info(audio_path),
        "response": {
            "request_id": data.get("request_id"),
            "code": data.get("code"),
            "message": data.get("message"),
            "output": {
                "target_model": output.get("target_model"),
                "voice_masked": mask_voice(voice) if voice else None,
            },
            "usage": data.get("usage"),
        },
    }
    write_json(OUTPUT_DIR / "B_重建音色_create_custom_voice_request_debug_sanitized.json", sanitized)
    response.raise_for_status()
    if not voice:
        raise RuntimeError("create_custom_voice 成功响应中未返回 voice")
    return voice


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_voice_clone(
    *,
    api_key: str,
    voice: str,
    output_wav_path: pathlib.Path,
    request_debug_path: pathlib.Path,
    label: str,
) -> dict[str, Any]:
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
                "instructions": SYNTHESIS_INSTRUCTIONS,
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

    output_wav_path.parent.mkdir(parents=True, exist_ok=True)
    audio_bytes = b"".join(chunks)
    with wave.open(str(output_wav_path), "wb") as wav_file:
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
        "instructions": SYNTHESIS_INSTRUCTIONS,
        "voice_trial_text": VOICE_TRIAL_TEXT,
        "tts_input_text": TTS_INPUT_TEXT,
        "session_update": {
            "voice": "<custom_voice_masked>",
            "instructions": SYNTHESIS_INSTRUCTIONS,
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
        "output_audio": read_wave_info(output_wav_path),
        "label": label,
    }
    write_json(request_debug_path, debug)
    return debug


def denoise_audio(ffmpeg: str, input_path: pathlib.Path, output_path: pathlib.Path, log_path: pathlib.Path) -> None:
    filter_graph = "afftdn=nf=-24,highpass=f=70,lowpass=f=11000"
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(input_path),
            "-af",
            filter_graph,
            "-ar",
            str(SAMPLE_RATE),
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(output_path),
        ],
        log_path,
    )


def tempo_adjust_audio(
    ffmpeg: str,
    input_path: pathlib.Path,
    output_path: pathlib.Path,
    log_path: pathlib.Path,
    target_duration_seconds: float = 14.2,
) -> dict[str, Any]:
    input_info = read_wave_info(input_path)
    factor = max(1.0, input_info["duration_seconds"] / target_duration_seconds)
    if factor <= 1.0001:
        shutil.copy2(input_path, output_path)
        log_path.write_text(
            f"tempo adjustment skipped: input duration {input_info['duration_seconds']}s already <= target {target_duration_seconds}s\n",
            encoding="utf-8",
        )
    else:
        run_command(
            [
                ffmpeg,
                "-y",
                "-i",
                str(input_path),
                "-af",
                f"atempo={factor:.6f}",
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(output_path),
            ],
            log_path,
        )
    output_info = read_wave_info(output_path)
    return {
        "input": input_info,
        "output": output_info,
        "target_duration_seconds": target_duration_seconds,
        "atempo_factor": round(factor, 6),
        "log": str(log_path.relative_to(ROOT)),
    }


def validate_audio(ffmpeg: str, path: pathlib.Path, prefix: str) -> dict[str, Any]:
    decode_log = OUTPUT_DIR / f"{prefix}_ffmpeg_decode_check.txt"
    volume_log = OUTPUT_DIR / f"{prefix}_volumedetect.txt"
    loudnorm_log = OUTPUT_DIR / f"{prefix}_loudnorm_measure.txt"
    run_command([ffmpeg, "-hide_banner", "-y", "-i", str(path), "-f", "null", "-"], decode_log)
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    loudnorm = run_command(
        [ffmpeg, "-hide_banner", "-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        loudnorm_log,
    )
    info = read_wave_info(path)
    return {
        **info,
        "decode_status": "通过",
        "volumedetect": parse_volumedetect(volume.stderr),
        "loudnorm": parse_loudnorm(loudnorm.stderr),
        "logs": {
            "decode": str(decode_log.relative_to(ROOT)),
            "volumedetect": str(volume_log.relative_to(ROOT)),
            "loudnorm": str(loudnorm_log.relative_to(ROOT)),
        },
    }


def write_readme(summary: dict[str, Any]) -> None:
    validation_rows = []
    for item in summary["validation_results"]:
        loudnorm = item.get("loudnorm", {})
        validation_rows.append(
            "| `{path}` | `{duration:.2f}s` | `{codec}` | `{sample_rate} Hz` | `{channels}` | `{mean}` | `{lufs}` | `{status}` |".format(
                path=item["path"],
                duration=item["duration_seconds"],
                codec=item["codec"],
                sample_rate=item["sample_rate"],
                channels=item["channels"],
                mean=item.get("volumedetect", {}).get("mean_volume", "n/a"),
                lufs=loudnorm.get("input_i", "n/a"),
                status=item["decode_status"],
            )
        )
    lines = [
        "# 台湾口语开心降噪声音试配 Taiwan Happy Denoise Trial",
        "",
        "## 本轮目标",
        "",
        "- `已确认` 本轮只生成《视频工厂》声音第二轮最小对照 trial。",
        "- `已确认` 不修改视频、不替换全片音轨、不生成新视频 round。",
        "- `已确认` 本轮目标是 A / B 两组 10-15 秒声音对照音频，并保留原始输出与轻降噪输出。",
        "",
        "## 用户反馈原文",
        "",
        "1. 情绪上面还不够开心的那种。",
        "2. 需要把口语改成台湾的口音。",
        "3. 现在生成的环境音有点吵，需要降噪。",
        "",
        "## 本轮 voice_trial_text",
        "",
        "```text",
        VOICE_TRIAL_TEXT,
        "```",
        "",
        "## 本轮 instructions",
        "",
        "```text",
        SYNTHESIS_INSTRUCTIONS,
        "```",
        "",
        "## A / B 版本差异",
        "",
        "- A 版：沿用当前 custom voice，使用台湾口语文本 + 开心轻快 instructions 生成；输出后做轻降噪。",
        "- B 版：先对复刻输入样本做轻降噪，再重新创建测试 custom voice；使用同一台湾口语文本 + 同一 instructions 生成；输出后做轻降噪。",
        "",
        "## 使用的 model / voice / target_model",
        "",
        f"- 创建模型 model：`{CREATE_MODEL}`",
        f"- 目标合成模型 target_model：`{TARGET_MODEL}`",
        f"- 合成模型 model：`{TARGET_MODEL}`",
        f"- A 版 voice：`{summary['a_voice_masked']}`（脱敏）",
        f"- B 版 voice：`{summary['b_voice_masked']}`（脱敏）",
        f"- B 版 preferred_name：`{B_PREFERRED_NAME}`",
        "- 是否重新创建 custom voice：A 版 `no`；B 版 `yes`。",
        "- 是否做输入样本降噪：A 版 `no`；B 版 `yes`。",
        "- 是否做输出后降噪：A 版 `yes`；B 版 `yes`。",
        "",
        "## 输出文件路径",
        "",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav`（未降噪，节奏校准到 10-15 秒）",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_API原始_未节奏校准.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav`（未降噪，节奏校准到 10-15 秒）",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_复刻输入样本_轻降噪.wav`",
        "",
        "说明：API 直出因固定文案较长，未稳定落在 10-15 秒；本轮保留 API 直出审计文件，同时用 `atempo` 生成未降噪节奏校准版作为正式 10-15 秒对照 trial。",
        "",
        "## 验证结果",
        "",
        "| 文件 | duration | codec | sample_rate | channels | mean_volume | loudnorm.input_i | ffmpeg 解码 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
        *validation_rows,
        "",
        "## 脱敏请求与验证记录",
        "",
        "- `custom_voice_list_debug_sanitized.json`",
        "- `A_voice_clone_tts_request_debug_sanitized.json`",
        "- `B_重建音色_create_custom_voice_request_debug_sanitized.json`",
        "- `B_voice_clone_tts_request_debug_sanitized.json`",
        "- `run_summary.json`",
        "",
        "## 当前状态",
        "",
        "- `technical_generation`：通过。",
        "- `voice_validation_status`：待验证。",
        "- 当前状态：待用户 / ChatGPT 听感复审。",
        "- `content_validation`：仍待用户 / ChatGPT 最终复审。",
        "- `full_content_validation`：仍待用户 / ChatGPT 最终复审。",
        "- `send_ready`：仍为 `no`。",
        "",
        "## 禁止误写",
        "",
        "- 本轮 trial 不等于声音通过。",
        "- 本轮 custom voice 不等于最终音色。",
        "- 本轮不替换全片音轨。",
        "- 本轮不改变 `content_validation`。",
        "- 本轮不改变 `send_ready`。",
        "- 本轮未修改 `dist/latest_review_pack/full.mp4`。",
        "- 本轮未修改 `dist/latest_review_pack/middle_preview.mp4`。",
        "",
    ]
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_dated_log(summary: dict[str, Any]) -> None:
    lines = [
        "# 20260426 台湾口语开心降噪声音试配",
        "",
        "## 本轮目标",
        "",
        "- 只生成《视频工厂》声音第二轮最小对照 trial。",
        "- 不修改视频、不替换全片音轨、不改变内容验证状态。",
        "- 生成 A / B 两组 10-15 秒声音对照音频，每组保留原始输出和轻降噪输出。",
        "",
        "## 用户反馈原文",
        "",
        "1. 情绪上面还不够开心的那种。",
        "2. 需要把口语改成台湾的口音。",
        "3. 现在生成的环境音有点吵，需要降噪。",
        "",
        "## 执行前已确认事实",
        "",
        "- `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`。",
        "- `technical_validation = 通过`。",
        "- `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`。",
        "- `content_validation = 待用户 / ChatGPT 最终复审`。",
        "- `full_content_validation = 待用户 / ChatGPT 最终复审`。",
        "- `send_ready = no`。",
        "- 上一轮 custom voice 脱敏标识为 `qwen-t...de43`，本轮 A 版沿用该 custom voice。",
        "",
        "## skill 检查",
        "",
        "- `已确认` 当前仓库本地 `skills/` 目录不存在。",
        "- `已确认` 全局 `~/.codex/skills` 未找到直接的 audio / TTS / ffmpeg / denoise 专用 skill。",
        "- `已确认` 全局命中并读取 `verification-before-completion`，本轮按其要求先定义验证证据、再运行验证、再报告状态。",
        "- `已确认` 因本轮涉及指定 worktree，也读取并遵守 `using-git-worktrees` 的隔离与安全确认要点。",
        "",
        "## 实际读取",
        "",
        "- `AGENTS.md`",
        "- `codex_source/00_codex_readme.md`",
        "- `codex_source/01_execution_rules.md`",
        "- `codex_log/latest.md`",
        "- `codex_log/current_publish_target.md`",
        "- `codex_log/current_publish_target_light_evidence.md`",
        "- `dist/latest_review_pack/summary.json`",
        "- `dist/latest_review_pack/review_manifest.md`",
        "- `codex_log/20260425_语音样本_audio_reference_report.md`",
        "- `codex_log/20260425_round28_声音试配失败排查.md`",
        "- `codex_log/20260425_round28_声音复刻最小试配.md`",
        "- `dist/voice_trials/20260425_round28_voice_clone_trial/README.md`",
        "- `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`",
        "- `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`",
        "",
        "## 实际改动",
        "",
        "- 新增脚本：`scripts/声音第二轮台湾口语开心降噪_trial_round2.py`。",
        "- 新增输出目录：`dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`。",
        "- 新增本日志：`codex_log/20260426_台湾口语开心降噪声音试配.md`。",
        "- 后续同步刷新：`codex_log/latest.md`。",
        "",
        "## 实际执行",
        "",
        "- A 版沿用当前 custom voice，使用台湾口语文本 + 开心轻快 instructions 生成原始输出，并做输出后轻降噪。",
        "- B 版先对复刻输入样本做轻降噪，再重新创建测试 custom voice，使用同一文本 + 同一 instructions 生成原始输出，并做输出后轻降噪。",
        f"- 创建模型 model：`{CREATE_MODEL}`。",
        f"- 目标合成模型 target_model：`{TARGET_MODEL}`。",
        f"- 合成模型 model：`{TARGET_MODEL}`。",
        f"- A 版 voice：`{summary['a_voice_masked']}`（脱敏）。",
        f"- B 版 voice：`{summary['b_voice_masked']}`（脱敏）。",
        "",
        "## 输出文件",
        "",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_API原始_未节奏校准.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav`",
        "- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_复刻输入样本_轻降噪.wav`",
        "",
        "## 当前结果",
        "",
        "- `technical_generation`：通过。",
        "- `voice_validation_status`：待验证。",
        "- `content_validation`：待用户 / ChatGPT 最终复审。",
        "- `full_content_validation`：待用户 / ChatGPT 最终复审。",
        "- `send_ready`：no。",
        "",
        "## 验证结果",
        "",
        "| 文件 | duration | codec | sample_rate | channels | mean_volume | loudnorm.input_i | ffmpeg 解码 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in summary["validation_results"]:
        loudnorm = item.get("loudnorm", {})
        lines.append(
            "| `{path}` | `{duration:.2f}s` | `{codec}` | `{sample_rate} Hz` | `{channels}` | `{mean}` | `{lufs}` | `{status}` |".format(
                path=item["path"],
                duration=item["duration_seconds"],
                codec=item["codec"],
                sample_rate=item["sample_rate"],
                channels=item["channels"],
                mean=item.get("volumedetect", {}).get("mean_volume", "n/a"),
                lufs=loudnorm.get("input_i", "n/a"),
                status=item["decode_status"],
            )
        )
    lines.extend(
        [
            "",
            "## 明确未改",
            "",
            "- 未修改 `dist/latest_review_pack/full.mp4`。",
            "- 未修改 `dist/latest_review_pack/middle_preview.mp4`。",
            "- 未替换任何当前成片音轨。",
            "- 未生成新视频 round。",
            "- 未上传原始 55MB MP4。",
            "- 未把 custom voice 写成最终音色。",
            "- 未把 `voice_validation_status` 写成通过。",
            "- 未把 `content_validation` 写成通过。",
            "- 未把 `send_ready` 写成 yes。",
            "",
            "## 下一步目标",
            "",
            "- 用户 / ChatGPT 只听审本轮 A / B 两组原始与轻降噪 trial。",
            "- 听感复审前，不进入全片音轨替换，不写最终音色，不写声音通过。",
            "",
        ]
    )
    (ROOT / "codex_log" / "20260426_台湾口语开心降噪声音试配.md").write_text("\n".join(lines), encoding="utf-8")


async def main_async() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not CLONE_INPUT_PATH.exists():
        raise RuntimeError(f"缺少复刻输入样本：{CLONE_INPUT_PATH}")
    api_key = load_api_key()
    ffmpeg = resolve_ffmpeg()

    current_voice = list_custom_voices(api_key)
    b_input_denoised = OUTPUT_DIR / "B_复刻输入样本_轻降噪.wav"
    denoise_audio(ffmpeg, CLONE_INPUT_PATH, b_input_denoised, OUTPUT_DIR / "B_复刻输入样本_轻降噪_ffmpeg.txt")
    b_voice = create_custom_voice(api_key, b_input_denoised)

    a_api_raw = OUTPUT_DIR / "A_沿用音色_台湾口语开心_API原始_未节奏校准.wav"
    a_raw = OUTPUT_DIR / "A_沿用音色_台湾口语开心_原始.wav"
    a_denoised = OUTPUT_DIR / "A_沿用音色_台湾口语开心_轻降噪.wav"
    b_api_raw = OUTPUT_DIR / "B_重建音色_台湾口语开心_API原始_未节奏校准.wav"
    b_raw = OUTPUT_DIR / "B_重建音色_台湾口语开心_原始.wav"
    b_denoised = OUTPUT_DIR / "B_重建音色_台湾口语开心_轻降噪.wav"

    a_debug = await synthesize_voice_clone(
        api_key=api_key,
        voice=current_voice,
        output_wav_path=a_api_raw,
        request_debug_path=OUTPUT_DIR / "A_voice_clone_tts_request_debug_sanitized.json",
        label="A_沿用音色",
    )
    a_tempo = tempo_adjust_audio(ffmpeg, a_api_raw, a_raw, OUTPUT_DIR / "A_沿用音色_台湾口语开心_节奏校准_ffmpeg.txt")
    denoise_audio(ffmpeg, a_raw, a_denoised, OUTPUT_DIR / "A_沿用音色_台湾口语开心_轻降噪_ffmpeg.txt")

    b_debug = await synthesize_voice_clone(
        api_key=api_key,
        voice=b_voice,
        output_wav_path=b_api_raw,
        request_debug_path=OUTPUT_DIR / "B_voice_clone_tts_request_debug_sanitized.json",
        label="B_重建音色",
    )
    b_tempo = tempo_adjust_audio(ffmpeg, b_api_raw, b_raw, OUTPUT_DIR / "B_重建音色_台湾口语开心_节奏校准_ffmpeg.txt")
    denoise_audio(ffmpeg, b_raw, b_denoised, OUTPUT_DIR / "B_重建音色_台湾口语开心_轻降噪_ffmpeg.txt")

    validation_targets = [
        ("A_沿用音色_台湾口语开心_原始", a_raw),
        ("A_沿用音色_台湾口语开心_轻降噪", a_denoised),
        ("B_重建音色_台湾口语开心_原始", b_raw),
        ("B_重建音色_台湾口语开心_轻降噪", b_denoised),
    ]
    validation_results = [validate_audio(ffmpeg, path, prefix) for prefix, path in validation_targets]
    duration_ok = all(10.0 <= item["duration_seconds"] <= 15.0 for item in validation_results)
    summary = {
        "technical_generation": "通过",
        "duration_requirement": "通过" if duration_ok else "失败",
        "user_feedback": USER_FEEDBACK,
        "voice_trial_text": VOICE_TRIAL_TEXT,
        "instructions": SYNTHESIS_INSTRUCTIONS,
        "model": TARGET_MODEL,
        "create_model": CREATE_MODEL,
        "target_model": TARGET_MODEL,
        "a_voice_masked": mask_voice(current_voice),
        "b_voice_masked": mask_voice(b_voice),
        "b_preferred_name": B_PREFERRED_NAME,
        "a_request": a_debug,
        "b_request": b_debug,
        "tempo_adjustment": {"A": a_tempo, "B": b_tempo},
        "input_denoise": read_wave_info(b_input_denoised),
        "validation_results": validation_results,
        "state": {
            "voice_validation_status": "待验证",
            "content_validation": "待用户 / ChatGPT 最终复审",
            "full_content_validation": "待用户 / ChatGPT 最终复审",
            "send_ready": "no",
        },
        "unchanged": [
            "dist/latest_review_pack/full.mp4",
            "dist/latest_review_pack/middle_preview.mp4",
            "current full audio track",
            "content_validation",
            "send_ready",
        ],
    }
    write_json(OUTPUT_DIR / "run_summary.json", summary)
    write_readme(summary)
    write_dated_log(summary)
    print(json.dumps({"output_dir": str(OUTPUT_DIR), "duration_requirement": summary["duration_requirement"]}, ensure_ascii=False, indent=2))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
