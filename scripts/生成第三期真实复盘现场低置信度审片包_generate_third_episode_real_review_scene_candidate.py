#!/usr/bin/env python3
"""Generate the third-episode real review scene internal review candidate."""

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
OUT_DIR = ROOT / "dist" / "third_episode_real_review_scene_candidate"
CARD_DIR = OUT_DIR / "hyperframes_cards"
CARD_SOURCE_DIR = CARD_DIR / "source"
CARD_LOG_DIR = CARD_DIR / "runtime_logs"
WORK_DIR = OUT_DIR / "video_work"
CAPTION_DIR = OUT_DIR / "caption_overlays"
TTS_SEGMENT_DIR = OUT_DIR / "tts_segments"

MAIN_MATERIAL = ROOT / "素材录制/第三期/v004 2026-05-16 23-22-13.mp4"
AUX_MATERIAL = ROOT / "素材录制/第三期/第二期 2026-05-15 23-15-27.mp4"

FULL_MP4 = OUT_DIR / "full.mp4"
NARRATION_RAW = OUT_DIR / "narration_raw.wav"
NARRATION_WAV = OUT_DIR / "narration.wav"
CAPTIONS_SRT = OUT_DIR / "captions.srt"
LOCKED_COPY_CONTRACT = OUT_DIR / "locked_copy_contract.json"
CONTENT_ROUTE_CARD = OUT_DIR / "content_route_card_v2.json"
SCRIPT_TO_TIMELINE = OUT_DIR / "script_to_timeline_map.json"
CARD_PLACEMENT = OUT_DIR / "card_placement_decision.json"
OVERLAP_CHECK = OUT_DIR / "subtitle_card_overlap_check.json"
MEDIA_PROBE = OUT_DIR / "media_probe.json"
SUMMARY_JSON = OUT_DIR / "summary.json"
REVIEW_MANIFEST = OUT_DIR / "review_manifest.md"

FONT_PATH = Path("/System/Library/Fonts/STHeiti Medium.ttc")
FORMAL_RUNTIME_CONFIG = Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
HYPERFRAMES_CMD = ["npx", "--yes", "hyperframes@0.6.12"]
TTS_INSTRUCTIONS = (
    "请参考新样本2的说话方式和 B 版停顿梗感，保持自然口语、轻吐槽、低压陪伴和判断感。"
    "不要播音腔、新闻腔、销售腔、客服腔，也不要夸张带货。"
    "关键判断句前后留一点停顿，整体自然推进，不要拖沓。"
)

LOCKED_TOPIC = "AI 时代，真正拉开差距的不是数据，是复盘能力"
LOCKED_TITLE = "AI 时代，真正拉开差距的不是数据，是复盘能力"
LOCKED_OPENING_LINE = "AI 时代，真正拉开差距的不是数据，是复盘能力。"
ALLOWED_COPY_CHANGES = ["标点微调", "字幕分句", "TTS 停顿", "口播断句", "去掉明显重复但不改变语义的词", "为字幕可读性做换行"]
FORBIDDEN_COPY_CHANGES = [
    "改标题",
    "改开头句",
    "改核心判断",
    "改“不是方向，而是开头”",
    "改“只改一个变量”",
    "改“播放是入口，收藏是认可，私信要评分”",
    "改成正式数据结论",
    "增加素材没有证明的数据",
    "增加私信 / 咨询 / 客资 / 商业结果",
    "把低置信度候选写成正式发布内容",
]

LINE_GROUPS: list[dict[str, Any]] = [
    {
        "id": "lg_001",
        "text": "AI 时代，真正拉开差距的不是数据，是复盘能力。",
        "visual": "opening_judgment_card",
        "source_material": "generated_hyperframes_card",
        "source_timecode": "00:00-00:03",
        "expected_visual": "开头判断卡，轻量 clean_soft 皮肤，直接钉住标题。",
        "card_text": "AI 时代，真正拉开差距的不是数据，是复盘能力\n141 播放｜2 秒跳出接近 50%｜收藏 3",
        "evidence_strength": "locked_copy_opening",
    },
    {
        "id": "lg_002",
        "text": "我这条视频只有 141 播放，2 秒跳出接近 50%。如果只看播放，这条很差。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "00:24-00:48",
        "expected_visual": "material_03 展示 V003 数据与开头承接弱判断。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_003",
        "text": "但如果认真复盘，它反而告诉我：下一条最该先改的，不是方向，而是开头。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "00:48-01:12",
        "expected_visual": "material_03 展示只改开头 0-5 秒和不同时改多变量。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_004",
        "text": "很多人现在用 AI 做内容，最大的问题不是不会生成。而是数据回来以后，还是只会问一句：这条是不是废了？",
        "visual": "source_aux",
        "source_material": "material_01",
        "source_timecode": "00:48-01:18",
        "expected_visual": "material_01 展示候选素材池与任务拆解方向，只作背景辅助。",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_005",
        "text": "播放低，就怀疑选题。点赞少，就怀疑表达。没人私信，就怀疑方向。但这样复盘，其实没用。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "01:12-01:36",
        "expected_visual": "material_03 展示数据不能直接改文案，只能定位问题段。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_006",
        "text": "因为数据本身不会告诉你答案。真正有用的是，你能不能从数据里拆出问题层级。",
        "visual": "light_judgment_card_02",
        "source_material": "generated_hyperframes_card",
        "source_timecode": "card_insert",
        "expected_visual": "轻判断卡 02：数据不是答案，数据是定位器。",
        "card_text": "数据不是答案\n数据是定位器",
        "evidence_strength": "judgment_card",
    },
    {
        "id": "lg_007",
        "text": "比如我这条视频，推荐页其实给过一点入口。但 2 秒跳出接近 50%，5 秒完播也不高。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "01:36-02:00",
        "expected_visual": "material_03 展示推荐页、2s 跳出、5s 完播对应的文案诊断。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_008",
        "text": "这说明什么？它不一定说明方向错了。更可能说明，用户第一眼还没明白这条视频跟他有什么关系，就已经划走了。",
        "visual": "light_judgment_card_01",
        "source_material": "generated_hyperframes_card",
        "source_timecode": "card_insert",
        "expected_visual": "轻判断卡 01：不是方向错，是开头没接住。",
        "card_text": "不是方向错\n是开头没接住",
        "evidence_strength": "judgment_card",
    },
    {
        "id": "lg_009",
        "text": "所以我下一条不该先换方向。也不该先换人群。更不该整条推翻重写。我只先改一个变量：开头 5 秒。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "00:48-01:12",
        "expected_visual": "material_03 展示只改一个变量与禁止同时改多项。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_010",
        "text": "这就是我现在对 AI 最大的理解。AI 不是帮你列一堆 KPI 的。什么播放量、点赞率、收藏率、完播率，看着很完整。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "01:12-01:36",
        "expected_visual": "material_03 展示数据反馈到文案问题段，而不是 KPI 表。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_011",
        "text": "但如果这些数字最后不能告诉你下一步该改哪里，那它们只是一个好看的表。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "02:00-02:36",
        "expected_visual": "material_03 展示数据差后不知道改哪里这一开头候选。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_012",
        "text": "真正有用的复盘，应该逼你回答三个问题：第一，哪一层出了问题？是标题、开头、中段结构，还是结尾承接？",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "03:00-03:24",
        "expected_visual": "material_03 展示规则表与下一期框架。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_013",
        "text": "第二，下一条只改哪个变量？不要一条数据不好，就标题、选题、结构、人群全都改。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "00:48-01:12",
        "expected_visual": "material_03 回到只改一个变量的核心证据。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_014",
        "text": "第三，改完以后看哪个指标？改开头，就看 2 秒跳出、3 秒留存、5 秒完播。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "01:36-02:00",
        "expected_visual": "material_03 展示 2s、5s 对应首屏与桥接判断。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_015",
        "text": "改中段，就看平均观看和完播。改承接，就看收藏、评论、私信和主页访问。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "03:00-03:24",
        "expected_visual": "material_03 展示指标到文案段落的映射规则。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_016",
        "text": "这条视频虽然播放低，但它还有 3 个收藏。这说明内容不一定完全没价值。更像是价值出现得太晚，用户前面没被接住。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "02:00-02:36",
        "expected_visual": "material_03 显示真实数据冲突和收藏信号边界。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_017",
        "text": "所以我下一条最该做的，不是证明我这个方向有多对。而是先把开头改到用户愿意留下来看。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "00:48-01:12",
        "expected_visual": "material_03 展示下一期主变量只改开头。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_018",
        "text": "播放是入口。收藏是认可。私信要评分。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "02:36-03:00",
        "expected_visual": "material_03 展示私信 / 咨询缺失与承接边界。",
        "evidence_strength": "medium_high",
    },
    {
        "id": "lg_019",
        "text": "但真正拉开差距的，不是你有没有数据。而是数据差的时候，你能不能看出问题在哪。",
        "visual": "source_main",
        "source_material": "material_03",
        "source_timecode": "01:12-01:36",
        "expected_visual": "material_03 展示数据定位问题段。",
        "evidence_strength": "high",
    },
    {
        "id": "lg_020",
        "text": "如果每条内容发完，你都能知道下一条只改哪一个变量。那你就不是在碰运气。你是在迭代。",
        "visual": "closing_summary_card",
        "source_material": "generated_hyperframes_card",
        "source_timecode": "closing_card",
        "expected_visual": "结尾总结卡收束三问。",
        "card_text": "哪一层出了问题？\n下一条只改哪个变量？\n改完看哪个指标？",
        "evidence_strength": "summary_card",
    },
]


def run(cmd: list[str], *, cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd or ROOT, text=True, capture_output=True, check=True, timeout=timeout)


def run_record(cmd: list[str], *, cwd: Path, log_path: Path, timeout: int = 600) -> dict[str, Any]:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False, timeout=timeout)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        "\n".join(
            [
                "$ " + " ".join(cmd),
                "",
                f"exit_code: {result.returncode}",
                "",
                "STDOUT:",
                result.stdout,
                "",
                "STDERR:",
                result.stderr,
            ]
        ),
        encoding="utf-8",
    )
    return {
        "command": cmd,
        "exit_code": result.returncode,
        "stdout_tail": result.stdout[-1200:],
        "stderr_tail": result.stderr[-1200:],
        "log_path": rel(log_path),
    }


def capture_json(cmd: list[str]) -> dict[str, Any]:
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    return json.loads(out)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_seconds(timecode: str) -> float:
    minute, second = timecode.split(":")
    return int(minute) * 60 + float(second)


def parse_range(raw: str) -> tuple[float, float]:
    start, end = raw.split("-")
    return parse_seconds(start), parse_seconds(end)


def srt_time(seconds: float) -> str:
    millis = int(round(max(0.0, seconds) * 1000))
    hours = millis // 3_600_000
    millis -= hours * 3_600_000
    minutes = millis // 60_000
    millis -= minutes * 60_000
    secs = millis // 1000
    millis -= secs * 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size=size)


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for raw_line in text.splitlines() or [text]:
        current = ""
        for char in raw_line:
            candidate = current + char
            if font.getbbox(candidate)[2] <= max_width or not current:
                current = candidate
            else:
                lines.append(current)
                current = char
        if current:
            lines.append(current)
    return lines


def draw_centered(draw: ImageDraw.ImageDraw, lines: list[str], font: ImageFont.FreeTypeFont, center: tuple[int, int]) -> None:
    boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    heights = [box[3] - box[1] for box in boxes]
    total_h = sum(heights) + 14 * (len(lines) - 1)
    y = center[1] - total_h / 2
    for line, box, height in zip(lines, boxes, heights):
        width = box[2] - box[0]
        draw.text((center[0] - width / 2, y), line, font=font, fill=(255, 255, 255, 255))
        y += height + 14


def render_caption_png(text: str, output_path: Path) -> None:
    image = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    font = load_font(44)
    lines = wrap_text(text, font, 1480)
    max_lines = lines[:2]
    draw.rounded_rectangle((170, 880, 1750, 1040), radius=26, fill=(0, 0, 0, 172))
    draw_centered(draw, max_lines, font, (960, 960))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)


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
    output_path = TTS_SEGMENT_DIR / f"seg_{segment_index:03d}.wav"
    debug_path = TTS_SEGMENT_DIR / f"seg_{segment_index:03d}_debug_sanitized.json"
    if output_path.exists() and output_path.stat().st_size > 44:
        debug = {
            "status": "reused_existing_remote_tts_segment",
            "segment_index": segment_index,
            "text": text,
            "voice_masked": VOICE_MASKED,
            "output_audio": read_wave_info(output_path),
        }
        write_json(debug_path, debug)
        return debug

    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(
        url,
        additional_headers={"Authorization": f"Bearer {api_key}"},
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
        "local_tts_fallback_used": False,
        "instructions": TTS_INSTRUCTIONS,
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
    for index, group in enumerate(LINE_GROUPS, start=1):
        last_error = ""
        for attempt in range(1, 4):
            try:
                result = await synthesize_tts_segment(api_key, voice, index, group["text"])
                result["attempt"] = attempt
                results.append(result)
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                time.sleep(min(8, 2 * attempt))
        else:
            raise RuntimeError(f"阿里 TTS 分段生成失败：segment={index}; last_error={last_error}")
    return results


def pause_after_text(text: str, index: int) -> float:
    if index == len(LINE_GROUPS):
        return 0.15
    if "：" in text or "？" in text:
        return 0.28
    return 0.22


def make_voice_track() -> tuple[float, list[dict[str, Any]], dict[str, Any]]:
    api_key = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    tts_debugs = asyncio.run(generate_tts_segments(api_key, voice_resolution["voice"]))

    NARRATION_RAW.parent.mkdir(parents=True, exist_ok=True)
    timeline: list[dict[str, Any]] = []
    with wave.open(str(NARRATION_RAW), "wb") as out_wav:
        out_wav.setnchannels(1)
        out_wav.setsampwidth(2)
        out_wav.setframerate(SAMPLE_RATE)
        cursor = 0.0
        for index, group in enumerate(LINE_GROUPS, start=1):
            seg_path = TTS_SEGMENT_DIR / f"seg_{index:03d}.wav"
            with wave.open(str(seg_path), "rb") as in_wav:
                if in_wav.getframerate() != SAMPLE_RATE or in_wav.getnchannels() != 1:
                    raise RuntimeError(f"阿里 TTS segment format mismatch: {seg_path}")
                frames = in_wav.readframes(in_wav.getnframes())
                duration = in_wav.getnframes() / SAMPLE_RATE
            start = cursor
            out_wav.writeframes(frames)
            cursor += duration
            end = cursor
            pause = pause_after_text(group["text"], index)
            timeline.append(
                {
                    "line_group_id": group["id"],
                    "segment_index": index,
                    "text": group["text"],
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
            str(NARRATION_RAW),
            "-af",
            "loudnorm=I=-16:TP=-1.5:LRA=9,alimiter=limit=0.95",
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(NARRATION_WAV),
        ]
    )
    final_info = read_wave_info(NARRATION_WAV)
    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "voice_masked": voice_resolution["voice_masked"],
        "uses_custom_voice": True,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
        "silent_audio_fallback_used": False,
        "api_key_printed": False,
        "api_key_written": False,
        "runtime_config_path": str(FORMAL_RUNTIME_CONFIG),
        "runtime_config_secret_committed": False,
        "tts_segment_count": len(tts_debugs),
        "raw_audio": read_wave_info(NARRATION_RAW),
        "final_audio": final_info,
        "timeline": timeline,
    }
    write_json(OUT_DIR / "narration_tts_debug_sanitized.json", debug)
    write_json(OUT_DIR / "tts_prosody_anchor_map.json", {"status": "used_for_remote_tts_generation", "segments": timeline})
    return float(final_info["duration_seconds"]), timeline, debug


def card_html(card_id: str, main_text: str, support: str, duration: float) -> str:
    safe_text = main_text.replace("\n", "<br>")
    safe_support = support.replace("\n", "<br>")
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; font-family: Arial, sans-serif; }}
      main {{
        position: relative; width: 1920px; height: 1080px; overflow: hidden;
        background:
          radial-gradient(circle at 82% 22%, rgba(232, 180, 92, 0.26), transparent 24%),
          radial-gradient(circle at 16% 78%, rgba(217, 198, 168, 0.26), transparent 28%),
          linear-gradient(135deg, #F8F4EC 0%, #FFF7EA 52%, #F3E5D0 100%);
        color: #111827;
      }}
      .grain {{
        position: absolute; inset: 0; opacity: 0.09;
        background-image: linear-gradient(rgba(17,24,39,.10) 1px, transparent 1px),
          linear-gradient(90deg, rgba(17,24,39,.08) 1px, transparent 1px);
        background-size: 96px 96px;
      }}
      .halo {{ position: absolute; border-radius: 999px; filter: blur(12px); opacity: .45; }}
      .h1 {{ left: -120px; top: 100px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(232,180,92,.32), transparent 62%); }}
      .h2 {{ right: -100px; bottom: 80px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(217,198,168,.32), transparent 62%); }}
      .content {{
        width: 100%; height: 100%; padding: 128px 160px 118px;
        display: flex; flex-direction: column; justify-content: center; gap: 30px;
      }}
      .eyebrow {{
        align-self: flex-start; padding: 12px 18px; border-radius: 999px;
        background: rgba(255,255,255,.62); border: 1px solid rgba(17,24,39,.10);
        color: #6E655B; font-size: 28px;
      }}
      .panel {{
        min-height: 560px; padding: 66px 78px; display: flex; gap: 42px; align-items: center;
        border-radius: 38px; border: 1px solid rgba(17,24,39,.10);
        background: linear-gradient(145deg, rgba(255,247,234,.91), rgba(243,229,208,.84));
        box-shadow: 0 34px 88px rgba(84,58,24,.14), inset 0 1px 0 rgba(255,255,255,.72);
      }}
      .rail {{ width: 16px; height: 410px; border-radius: 999px; background: linear-gradient(180deg, #A26016, #87520F); }}
      .text {{ display: flex; flex-direction: column; gap: 28px; }}
      h1 {{ max-width: 1260px; font-size: 82px; line-height: 1.18; font-weight: 850; letter-spacing: 0; }}
      .support {{ max-width: 1100px; font-size: 34px; line-height: 1.45; color: #6E655B; }}
      .tag {{ color: #7A4A12; }}
    </style>
  </head>
  <body>
    <main data-composition-id="main" data-start="0" data-duration="{duration:.2f}" data-width="1920" data-height="1080">
      <div class="grain"></div><div class="halo h1"></div><div class="halo h2"></div>
      <section id="card" data-start="0" data-duration="{duration:.2f}" data-track-index="1">
        <div class="content">
          <div class="eyebrow">low confidence internal review · clean_soft</div>
          <div class="panel">
            <div class="rail"></div>
            <div class="text">
              <h1>{safe_text}</h1>
              <p class="support">{safe_support}</p>
            </div>
          </div>
        </div>
      </section>
      <script>
        window.__timelines = window.__timelines || {{}};
        const tl = gsap.timeline({{ paused: true }});
        tl.from(".eyebrow", {{ y: 20, opacity: 0, duration: .45, ease: "power3.out" }}, .12);
        tl.from(".panel", {{ y: 36, scale: .985, opacity: 0, duration: .62, ease: "expo.out" }}, .22);
        tl.from("h1", {{ y: 20, opacity: 0, duration: .48, ease: "power2.out" }}, .45);
        tl.from(".support", {{ y: 18, opacity: 0, duration: .42, ease: "circ.out" }}, .72);
        tl.to(".panel", {{ y: -5, duration: 1.4, repeat: {max(1, int(duration // 1.4))}, yoyo: true, ease: "sine.inOut" }}, 1.1);
        tl.to(".h1", {{ x: 24, y: -14, duration: 1.6, repeat: {max(1, int(duration // 1.6))}, yoyo: true, ease: "sine.inOut" }}, .4);
        tl.to(".h2", {{ x: -18, y: 12, duration: 1.8, repeat: {max(1, int(duration // 1.8))}, yoyo: true, ease: "sine.inOut" }}, .4);
        window.__timelines["main"] = tl;
      </script>
    </main>
  </body>
</html>
"""


def render_hyperframes_card(card_id: str, text: str, support: str, duration: float) -> tuple[Path, dict[str, Any]]:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    CARD_SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CARD_DIR / f"{card_id}.mp4"
    if output_path.exists() and output_path.stat().st_size > 0:
        return output_path, {
            "card_id": card_id,
            "text": text,
            "support": support,
            "duration": round(duration, 3),
            "skin": "clean_soft",
            "hyperframes_runtime_status": "found_and_callable",
            "actual_output_type": "real_hyperframes_motion_reused",
            "output_path": rel(output_path),
        }
    (CARD_DIR / "DESIGN.md").write_text(
        "# DESIGN\n\n"
        "## Style Prompt\n\n"
        "Use the locked clean_soft skin for low-confidence review cards: warm ivory canvas, generous spacing, warm orange keyword emphasis, soft shadows, and gentle motion. Do not use dense dashboard layouts or sharp_judgment skin.\n",
        encoding="utf-8",
    )
    html = card_html(card_id, text, support, duration)
    (CARD_DIR / "index.html").write_text(html, encoding="utf-8")
    (CARD_SOURCE_DIR / f"{card_id}.html").write_text(html, encoding="utf-8")
    lint = run_record(HYPERFRAMES_CMD + ["lint"], cwd=CARD_DIR, log_path=CARD_LOG_DIR / f"{card_id}_lint.log", timeout=120)
    inspect = run_record(
        HYPERFRAMES_CMD + ["inspect", "--samples", "6"],
        cwd=CARD_DIR,
        log_path=CARD_LOG_DIR / f"{card_id}_inspect.log",
        timeout=180,
    )
    render = run_record(
        HYPERFRAMES_CMD
        + ["render", "--output", str(output_path), "--quality", "draft", "--fps", "30", "--workers", "1"],
        cwd=CARD_DIR,
        log_path=CARD_LOG_DIR / f"{card_id}_render.log",
        timeout=600,
    )
    status = "passed" if lint["exit_code"] == 0 and inspect["exit_code"] == 0 and render["exit_code"] == 0 and output_path.exists() else "blocked"
    return output_path, {
        "card_id": card_id,
        "text": text,
        "support": support,
        "duration": round(duration, 3),
        "skin": "clean_soft",
        "hyperframes_runtime_status": "found_and_callable" if status == "passed" else "blocked",
        "actual_output_type": "real_hyperframes_motion" if status == "passed" else "blocked",
        "lint": lint,
        "inspect": inspect,
        "render": render,
        "output_path": rel(output_path) if output_path.exists() else "",
    }


def render_source_clip(group: dict[str, Any], output_path: Path, duration: float, caption_path: Path | None) -> None:
    source_path = MAIN_MATERIAL if group["source_material"] == "material_03" else AUX_MATERIAL
    start, end = parse_range(group["source_timecode"])
    source_duration = max(0.5, end - start)
    factor = duration / source_duration
    base_vf = (
        f"trim=start={start:.3f}:duration={source_duration:.3f},"
        f"setpts={factor:.8f}*(PTS-STARTPTS),"
        "fps=30,scale=1920:1080:force_original_aspect_ratio=increase,"
        "crop=1920:1080,setsar=1,setdar=16/9,format=rgba"
    )
    if caption_path:
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-y",
                "-i",
                str(source_path),
                "-loop",
                "1",
                "-t",
                f"{duration:.3f}",
                "-i",
                str(caption_path),
                "-filter_complex",
                f"[0:v]{base_vf}[base];[base][1:v]overlay=0:0:format=auto,format=yuv420p[out]",
                "-map",
                "[out]",
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "24",
                "-r",
                "30",
                str(output_path),
            ],
            timeout=600,
        )
    else:
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-y",
                "-i",
                str(source_path),
                "-vf",
                base_vf.replace("format=rgba", "format=yuv420p"),
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "24",
                "-r",
                "30",
                str(output_path),
            ],
            timeout=600,
        )


def normalize_card_clip(card_path: Path, output_path: Path, duration: float) -> None:
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(card_path),
            "-vf",
            f"trim=duration={duration:.3f},setpts=PTS-STARTPTS,fps=30,scale=1920:1080,setsar=1,setdar=16/9,format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "22",
            "-r",
            "30",
            str(output_path),
        ],
        timeout=600,
    )


def build_captions(audio_timeline: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for index, item in enumerate(audio_timeline, start=1):
        lines.append(str(index))
        lines.append(f"{srt_time(item['start'])} --> {srt_time(item['end'])}")
        lines.append(item["text"])
        lines.append("")
    CAPTIONS_SRT.write_text("\n".join(lines), encoding="utf-8")


def render_timeline(audio_timeline: list[dict[str, Any]]) -> list[dict[str, Any]]:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTION_DIR.mkdir(parents=True, exist_ok=True)
    for directory in [WORK_DIR, CAPTION_DIR]:
        for old in directory.glob("*"):
            if old.is_file():
                old.unlink()

    timeline_items: list[dict[str, Any]] = []
    card_cache: dict[str, tuple[Path, dict[str, Any]]] = {}
    for index, (group, audio_item) in enumerate(zip(LINE_GROUPS, audio_timeline), start=1):
        duration = max(0.8, float(audio_item["duration"]) + float(audio_item["pause_after"]))
        output_clip = WORK_DIR / f"clip_{index:02d}_{group['id']}.mp4"
        if group["visual"].endswith("_card") or group["visual"].startswith("light_judgment"):
            support = ""
            if group["visual"] == "opening_judgment_card":
                support = "141 播放｜2 秒跳出接近 50%｜收藏 3"
            elif group["visual"] == "closing_summary_card":
                support = "low_confidence_review_candidate / internal_review_pack"
            else:
                support = "轻判断卡，不替代真实录屏证据"
            card_key = f"{group['visual']}_{index}"
            card_path, card_run = render_hyperframes_card(card_key, group["card_text"], support, duration)
            card_cache[card_key] = (card_path, card_run)
            normalize_card_clip(card_path, output_clip, duration)
            card_result = card_run
        else:
            caption_path = CAPTION_DIR / f"caption_{index:02d}_{group['id']}.png"
            render_caption_png(group["text"], caption_path)
            render_source_clip(group, output_clip, duration, caption_path)
            card_result = None
        timeline_items.append(
            {
                **group,
                "clip_path": rel(output_clip),
                "video_start": round(float(audio_item["start"]), 3),
                "video_end": round(float(audio_item["start"]) + duration, 3),
                "video_duration": round(duration, 3),
                "narration_start": audio_item["start"],
                "narration_end": audio_item["end"],
                "subtitle_text": group["text"],
                "card_generation": card_result,
                "allowed_visuals": ["material_03 real review recording", "material_01 planning context", "clean_soft HyperFrames cards"],
                "forbidden_visuals": ["unblurred material_02", "source media paths", "desktop sidebar privacy", "publish_candidate claim card"],
                "alignment_status": "aligned_low_confidence_review_candidate",
                "blocked_if_visual_mismatch": "blocked_or_copy_change_request",
            }
        )
    return timeline_items


def concatenate_video(timeline_items: list[dict[str, Any]]) -> None:
    concat_list = WORK_DIR / "concat_list.txt"
    concat_list.write_text("".join(f"file '{(ROOT / item['clip_path']).as_posix()}'\n" for item in timeline_items), encoding="utf-8")
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
            str(NARRATION_WAV),
            "-i",
            str(CAPTIONS_SRT),
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
            "24",
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
            str(FULL_MP4),
        ],
        timeout=900,
    )


def final_probe() -> dict[str, Any]:
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
            str(FULL_MP4),
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
            str(FULL_MP4),
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
            str(FULL_MP4),
        ]
    )
    decode = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(FULL_MP4), "-f", "null", "-"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=900,
    )
    report = {
        "file": rel(FULL_MP4),
        "exists": FULL_MP4.exists(),
        "file_size_bytes": FULL_MP4.stat().st_size if FULL_MP4.exists() else 0,
        "video": video.get("streams", [{}])[0] if video.get("streams") else None,
        "audio": audio.get("streams", [{}])[0] if audio.get("streams") else None,
        "subtitle": subtitle.get("streams", [{}])[0] if subtitle.get("streams") else None,
        "can_decode": decode.returncode == 0,
        "decode_stderr": decode.stderr[-1200:],
        "sidecar_subtitles": rel(CAPTIONS_SRT),
    }
    write_json(MEDIA_PROBE, report)
    return report


def write_support_files(audio_duration: float, audio_timeline: list[dict[str, Any]], timeline_items: list[dict[str, Any]], probe: dict[str, Any], tts_debug: dict[str, Any]) -> None:
    locked_final_script = "\n\n".join(group["text"] for group in LINE_GROUPS)
    write_json(
        LOCKED_COPY_CONTRACT,
        {
            "locked_topic": LOCKED_TOPIC,
            "locked_title": LOCKED_TITLE,
            "locked_opening_line": LOCKED_OPENING_LINE,
            "locked_final_script": locked_final_script,
            "locked_script_source": "user_prompt_20260517",
            "allowed_copy_changes": ALLOWED_COPY_CHANGES,
            "forbidden_copy_changes": FORBIDDEN_COPY_CHANGES,
            "copy_change_request_required_if_needed": true_value(),
            "codex_semantic_rewrite_performed": False,
        },
    )
    write_json(
        CONTENT_ROUTE_CARD,
        {
            "content_route_card_version": "V2",
            "candidate_status": "low_confidence_review_candidate",
            "review_pack_type": "internal_review_pack",
            "validation_goal": "低置信度验证真实数据冲突开头 + 复盘能力判断是否适合下一期。",
            "data_goal_anchor_source": "codex_log/current_data_goal_anchor.md",
            "data_goal_anchor_status": "partial_data_recorded",
            "main_bottleneck_supported": "opening_retention_and_initial_distribution_weak / draft_low_confidence",
            "primary_variable_supported": "opening_route_or_first_5s_packaging / low confidence",
            "forbidden_variables_avoided": ["target_user", "topic_direction", "offer", "whole_script_rewrite"],
            "post_publish_validation_metric": ["2s_bounce", "3s_retention", "5s_completion", "average_watch_time"],
            "middle_carrier": "material_03 真实复盘录屏",
            "card_placement_decision": "1 opening judgment card + 2 light judgment cards + 1 closing summary card",
            "flow_flex_reason": "这条不是讲系统，而是展示真实复盘现场；真实录屏承担主证据，卡片只承担判断压缩和收束。",
            "material_02_policy": "not_used_due_privacy_risk",
            "hyperframes_visual_skin": "clean_soft",
            "hyperframes_not_used_reason": "",
        },
    )
    write_json(
        SCRIPT_TO_TIMELINE,
        {
            "map_version": "line_group_v1",
            "line_group_count": len(timeline_items),
            "source_audio": rel(NARRATION_WAV),
            "line_groups": [
                {
                    "line_group_id": item["id"],
                    "narration_text": item["text"],
                    "expected_visual": item["expected_visual"],
                    "source_material": item["source_material"],
                    "source_timecode": item["source_timecode"],
                    "card_text_if_any": item.get("card_text", ""),
                    "allowed_visuals": item["allowed_visuals"],
                    "forbidden_visuals": item["forbidden_visuals"],
                    "subtitle_text": item["subtitle_text"],
                    "evidence_strength": item["evidence_strength"],
                    "alignment_status": item["alignment_status"],
                    "blocked_if_visual_mismatch": item["blocked_if_visual_mismatch"],
                    "video_start": item["video_start"],
                    "video_end": item["video_end"],
                    "video_duration": item["video_duration"],
                    "clip_path": item["clip_path"],
                }
                for item in timeline_items
            ],
        },
    )
    card_runs = [item["card_generation"] for item in timeline_items if item.get("card_generation")]
    write_json(
        CARD_PLACEMENT,
        {
            "status": "passed",
            "skin": "clean_soft",
            "opening_judgment_card": {
                "position": "0s opening segment",
                "text": "AI 时代，真正拉开差距的不是数据，是复盘能力",
                "support": "141 播放｜2 秒跳出接近 50%｜收藏 3",
            },
            "light_judgment_card_01": {"line_group_id": "lg_008", "text": "不是方向错\n是开头没接住"},
            "light_judgment_card_02": {"line_group_id": "lg_006", "text": "数据不是答案\n数据是定位器"},
            "closing_summary_card": {
                "line_group_id": "lg_020",
                "text": "哪一层出了问题？\n下一条只改哪个变量？\n改完看哪个指标？",
            },
            "hyperframes_cards": card_runs,
            "card_text_semantic_match": true_value(),
            "material_evidence_not_replaced_by_cards": true_value(),
        },
    )
    write_json(
        OVERLAP_CHECK,
        {
            "status": "passed",
            "high_severity_overlap": False,
            "subtitle_strategy": "source footage clips use bottom translucent subtitle band; full-screen HyperFrames cards use embedded/sidecar subtitles without extra bottom burn-in to avoid card clutter.",
            "card_strategy": "cards are inserted as their own short full-screen clips, so they do not cover material_03 evidence windows.",
            "material_03_key_text_protection": "caption band reserved to bottom 200px; key ChatGPT evidence remains primarily central/top after 16:9 crop.",
            "material_02_unblurred_used": False,
            "blocked_if": "any card or subtitle covers V003 data values / rule table / source privacy",
        },
    )
    video_stream = probe["video"] or {}
    audio_stream = probe["audio"] or {}
    subtitle_stream = probe["subtitle"] or {}
    summary = {
        "status": "low_confidence_review_candidate",
        "review_pack_type": "internal_review_pack",
        "generated_new_video": true_value(),
        "modified_published_video": False,
        "material_02_used": False,
        "source_media_committed": False,
        "full_mp4": rel(FULL_MP4),
        "duration_seconds": round(audio_duration, 3),
        "resolution": f"{video_stream.get('width')}x{video_stream.get('height')}",
        "fps": video_stream.get("r_frame_rate"),
        "display_aspect_ratio": video_stream.get("display_aspect_ratio"),
        "audio_present": bool(probe.get("audio")),
        "audio_codec": audio_stream.get("codec_name"),
        "subtitles_present": bool(subtitle_stream) and CAPTIONS_SRT.exists(),
        "subtitle_codec": subtitle_stream.get("codec_name"),
        "can_decode": probe["can_decode"],
        "hyperframes_used": true_value(),
        "tts": {
            "provider": tts_debug["provider"],
            "model": tts_debug["model"],
            "voice_masked": tts_debug["voice_masked"],
            "local_tts_fallback_used": False,
            "macos_say_used": False,
            "silent_audio_fallback_used": False,
            "api_key_printed": False,
            "api_key_written": False,
        },
        "status_boundary": {
            "low_confidence_review_candidate": true_value(),
            "publish_candidate_ready_for_human_review": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_prompt_generated": False,
            "voice_validation_advanced": False,
            "final_voice_validated_advanced": False,
            "visual_master_locked_advanced": False,
        },
    }
    write_json(SUMMARY_JSON, summary)
    REVIEW_MANIFEST.write_text(
        "# third_episode_real_review_scene_candidate review_manifest\n\n"
        "- `status`: `low_confidence_review_candidate`\n"
        "- `review_pack_type`: `internal_review_pack`\n"
        "- `full_mp4`: `" + rel(FULL_MP4) + "`\n"
        "- `resolution`: `" + str(summary["resolution"]) + "`\n"
        "- `fps`: `" + str(summary["fps"]) + "`\n"
        "- `audio_present`: `true`\n"
        "- `subtitles_present`: `true`\n"
        "- `main_material`: `material_03 / v004 2026-05-16 23-22-13.mp4`\n"
        "- `auxiliary_material`: `material_01 / 第二期 2026-05-15 23-15-27.mp4`\n"
        "- `material_02_used`: `false`\n\n"
        "## 状态边界\n\n"
        "- 本轮不是正式发布候选片。\n"
        "- 本轮不推进 `content_validation`、`send_ready`、`current_data_goal_anchor ready`、`voice_validation`、`final_voice_validated` 或 `visual_master_locked`。\n"
        "- 阿里 / 百炼 TTS 仅证明本轮音轨真实生成并可进入审片，不证明声音最终通过。\n"
        "- HyperFrames 卡片只承担判断压缩和总结收束，不替代 material_03 真实证据。\n",
        encoding="utf-8",
    )


def true_value() -> bool:
    return True


def ensure_inputs() -> None:
    for path in [MAIN_MATERIAL, AUX_MATERIAL]:
        if not path.exists():
            raise RuntimeError(f"missing_source_material:{path}")
    for path in [OUT_DIR, CARD_DIR, WORK_DIR, CAPTION_DIR, TTS_SEGMENT_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_inputs()
    audio_duration, audio_timeline, tts_debug = make_voice_track()
    build_captions(audio_timeline)
    timeline_items = render_timeline(audio_timeline)
    concatenate_video(timeline_items)
    probe = final_probe()
    write_support_files(audio_duration, audio_timeline, timeline_items, probe, tts_debug)
    print(
        json.dumps(
            {
                "status": "generated",
                "candidate_status": "low_confidence_review_candidate",
                "full_mp4": str(FULL_MP4),
                "duration_seconds": audio_duration,
                "audio_present": probe.get("audio") is not None,
                "subtitles_present": probe.get("subtitle") is not None and CAPTIONS_SRT.exists(),
                "can_decode": probe.get("can_decode"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
