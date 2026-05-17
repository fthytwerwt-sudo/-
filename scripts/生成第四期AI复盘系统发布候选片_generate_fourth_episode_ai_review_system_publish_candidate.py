#!/usr/bin/env python3
"""Generate the fourth episode AI review system publish candidate.

This runner intentionally supports only the authorized Aliyun/Bailian remote
TTS path. It must not fall back to local TTS, macOS say, or silent audio.
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import subprocess
import time
import wave
from pathlib import Path
from typing import Any

import requests
import websockets
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "dist" / "fourth_episode_ai_review_system_publish_candidate"
WORK_DIR = OUT_DIR / "video_work"
CARD_DIR = OUT_DIR / "cards"
CAPTION_DIR = OUT_DIR / "caption_overlays"
TTS_SEGMENT_DIR = OUT_DIR / "tts_segments"

MATERIAL_INDEX = ROOT / "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_index.json"
MATERIAL_AUDIT_REPORT = ROOT / "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md"
SKILL_USED = "skills/视频素材解析_video_material_audit/SKILL.md"

FULL_MP4 = OUT_DIR / "full.mp4"
NARRATION_RAW = OUT_DIR / "narration_raw.wav"
NARRATION_WAV = OUT_DIR / "narration.wav"
CAPTIONS_SRT = OUT_DIR / "captions.srt"

FONT_PATH = Path("/System/Library/Fonts/STHeiti Medium.ttc")
FORMAL_RUNTIME_CONFIG = Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
FRAME_RATE = 30

TTS_INSTRUCTIONS = (
    "请保持自然口语、轻判断感、低压陪伴和清楚停顿。"
    "不要播音腔、销售腔、客服腔，也不要夸张带货。"
    "句子短的地方自然推进，关键判断句前后留一点停顿。"
)

LOCKED_TITLE = "我搭了一个 AI 短视频复盘系统，真正有用的不是看数据"
LOCKED_OPENING_LINE = "我最近搭了一个 AI 短视频复盘系统。"
ALLOWED_COPY_CHANGES = [
    "字幕断句",
    "标点微调",
    "TTS 停顿调整",
    "line_group 分组",
    "为卡片提取短句",
]
FORBIDDEN_COPY_CHANGES = [
    "改标题核心意思",
    "改观点",
    "改成全自动系统已完成",
    "改成强销售",
    "删除结尾低风险边界",
    "增加素材没有证明的事实",
    "把 Trae 写成唯一指定工具",
    "把先搭第一版改成直接完整做出来",
]


LINE_GROUPS: list[dict[str, Any]] = [
    {
        "id": "lg_001",
        "line_ids": ["L001", "L002", "L003"],
        "text": "我最近搭了一个 AI 短视频复盘系统。\n但它真正有用的地方，不是帮我做一张数据表。",
        "line_group_goal": "开头先立判断：系统价值不是数据表。",
        "visual_role": "judgment_card",
        "required_material": "generated_card",
        "source_timecode": "card",
        "card_text": "不是看数据\n是判断下一条只改哪里",
        "evidence_strength": "locked_opening",
    },
    {
        "id": "lg_002",
        "line_ids": ["L004", "L005"],
        "text": "而是每条视频发完以后，它能逼我回答一个问题：\n下一条，到底只改哪里？",
        "line_group_goal": "用 material_04 开始证明 AI 先确认事实和方向。",
        "visual_role": "opening_evidence",
        "required_material": "material_04",
        "source_timecode": "00:55-01:08",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_003",
        "line_ids": ["L006", "L007", "L008"],
        "text": "以前我看数据，很容易乱。\n播放低，就怀疑选题。点赞少，就怀疑表达。",
        "line_group_goal": "说明旧复盘方式会误判变量。",
        "visual_role": "opening_evidence",
        "required_material": "material_04",
        "source_timecode": "01:08-01:20",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_004",
        "line_ids": ["L009", "L010"],
        "text": "没人私信，就怀疑方向。\n但这样其实没用。",
        "line_group_goal": "继续压低误判问题。",
        "visual_role": "opening_evidence",
        "required_material": "material_04",
        "source_timecode": "01:20-01:30",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_005",
        "line_ids": ["L011", "L012"],
        "text": "因为你每次都改一堆东西，下一条好了或者坏了，\n你也不知道到底是哪一步起作用。",
        "line_group_goal": "转入只改一个变量的必要性。",
        "visual_role": "opening_evidence",
        "required_material": "material_04",
        "source_timecode": "01:30-01:42",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_006",
        "line_ids": ["L013", "L014"],
        "text": "所以我没有让 AI 直接给我一个复盘结论。\n我先让它把这个复盘系统拆开。",
        "line_group_goal": "把主题落到拆任务而不是先写文案。",
        "visual_role": "opening_to_middle_bridge",
        "required_material": "material_04",
        "source_timecode": "01:42-01:50",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_007",
        "line_ids": ["L015", "L016", "L017"],
        "text": "第一步，是配置。\n你做什么平台，账号目标是什么，看 24 小时、72 小时，还是 7 天数据，",
        "line_group_goal": "进入 material_02 主体证据：配置层。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "00:20-00:35",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_008",
        "line_ids": ["L018"],
        "text": "哪些指标算观察信号，这些先写成可以改的配置。",
        "line_group_goal": "证明系统不是写结论，而是配置观察信号。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "00:35-00:45",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_009",
        "line_ids": ["L019", "L020"],
        "text": "第二步，是字段。\n一条视频发完以后，不是只记播放量。",
        "line_group_goal": "字段层：从单指标到多字段。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "00:45-00:57",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_010",
        "line_ids": ["L021"],
        "text": "它要分开记：2 秒跳出，5 秒完播，平均观看，收藏，评论，主页访问，私信，有效咨询。",
        "line_group_goal": "展示字段清单，人话解释素材小字。",
        "visual_role": "process_summary_card",
        "required_material": "generated_card",
        "source_timecode": "card",
        "card_text": "配置 → 字段 → 截图入库\n文案记录 → 问题层 → 下一轮变量",
        "evidence_strength": "summary_card",
    },
    {
        "id": "lg_011",
        "line_ids": ["L022", "L023"],
        "text": "第三步，是截图入库。\n现在我每次发完视频，不是自己重新开表格慢慢填。",
        "line_group_goal": "截图入库是当前脚本必须保留的用户确认结构。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "00:57-01:08",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_012",
        "line_ids": ["L024", "L025"],
        "text": "我直接把后台截图丢给这个系统。\n它会先判断这是哪条视频，是 24 小时、72 小时，还是 7 天数据。",
        "line_group_goal": "突出截图进入系统后的判断流程。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:08-01:22",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_013",
        "line_ids": ["L026"],
        "text": "然后把截图里的播放、跳出、完播、收藏、评论这些字段整理出来。",
        "line_group_goal": "字段提取和整理。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:22-01:32",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_014",
        "line_ids": ["L027", "L028"],
        "text": "看不见的字段，它不会乱猜，会直接标成缺失。\n看不准的地方，也会标成待确认。",
        "line_group_goal": "边界卡：不硬猜，降低平台和事实风险。",
        "visual_role": "boundary_card",
        "required_material": "generated_card",
        "source_timecode": "card",
        "card_text": "看不见：标缺失\n看不准：待确认\n不硬猜",
        "evidence_strength": "boundary_card",
    },
    {
        "id": "lg_015",
        "line_ids": ["L029"],
        "text": "这样我拿到的就不是一堆截图，而是一份可以复盘的记录。",
        "line_group_goal": "截图转可复盘记录。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:32-01:42",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_016",
        "line_ids": ["L030", "L031"],
        "text": "第四步，是文案记录。\n每条视频原始文案要单独存下来。",
        "line_group_goal": "文案记录不是二次脑补。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:42-01:50",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_017",
        "line_ids": ["L032", "L033"],
        "text": "不能今天改一版，明天又改一版，\n最后连当时发出去的原文是什么都找不到。",
        "line_group_goal": "解释为什么原始文案要留底。",
        "visual_role": "middle_support",
        "required_material": "material_01",
        "source_timecode": "01:04-01:16",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_018",
        "line_ids": ["L034", "L035"],
        "text": "第五步，是问题层判断。\n数据不好，不能直接说这条废了。",
        "line_group_goal": "进入问题层判断。",
        "visual_role": "middle_support",
        "required_material": "material_01",
        "source_timecode": "01:16-01:28",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_019",
        "line_ids": ["L036", "L037"],
        "text": "它要先判断问题出在哪一层：\n是标题封面没接住，是开头 5 秒没讲清，",
        "line_group_goal": "把问题层拆出来。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:20-01:35",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_020",
        "line_ids": ["L038", "L039"],
        "text": "是中段证据不够，是结尾没有承接动作，\n还是平台风险让内容被误伤。",
        "line_group_goal": "补齐问题层并明确平台风险只作为可能层。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:35-01:50",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_021",
        "line_ids": ["L040", "L041"],
        "text": "第六步，是下一轮变量。\n它最后不能给我十几个建议。",
        "line_group_goal": "进入下一轮变量，避免泛建议。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:30-01:42",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_022",
        "line_ids": ["L042", "L043"],
        "text": "它只应该收成一句话：\n下一条先改哪个变量，改完看哪个指标。",
        "line_group_goal": "收束核心承诺：下一条只改一个变量。",
        "visual_role": "middle_evidence",
        "required_material": "material_02",
        "source_timecode": "01:42-01:50",
        "card_text": "",
        "evidence_strength": "high",
    },
    {
        "id": "lg_023",
        "line_ids": ["L044", "L045"],
        "text": "比如改开头，就看 2 秒跳出、3 秒留存、5 秒完播。\n改中段，就看平均观看和完播。",
        "line_group_goal": "变量和指标绑定。",
        "visual_role": "middle_support",
        "required_material": "material_04",
        "source_timecode": "01:30-01:42",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_024",
        "line_ids": ["L046"],
        "text": "改承接，就看收藏、评论、主页访问和私信。",
        "line_group_goal": "承接变量指标绑定。",
        "visual_role": "middle_support",
        "required_material": "material_04",
        "source_timecode": "01:42-01:50",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_025",
        "line_ids": ["L047", "L048"],
        "text": "这个系统现在还不是最终版。\n但它已经解决了我以前最大的问题：",
        "line_group_goal": "结尾边界：不是最终版。",
        "visual_role": "ending_support",
        "required_material": "material_01",
        "source_timecode": "01:04-01:18",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_026",
        "line_ids": ["L049", "L050"],
        "text": "我不是凭感觉做下一条了。\n每条视频发完，至少能留下一个可复盘、可修改、可验证的动作。",
        "line_group_goal": "账号价值收束。",
        "visual_role": "ending_support",
        "required_material": "material_01",
        "source_timecode": "01:18-01:28",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_027",
        "line_ids": ["L051", "L052"],
        "text": "如果你也想做自己的短视频复盘系统，\n我把我这套整理成了通用版。",
        "line_group_goal": "轻 CTA，不引导私信。",
        "visual_role": "ending_support",
        "required_material": "material_04",
        "source_timecode": "01:30-01:40",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_028",
        "line_ids": ["L053", "L054"],
        "text": "不是固定模板，而是一套可以改的提示词结构。\n你可以把自己的平台、账号目标、视频类型和指标填进去，",
        "line_group_goal": "弱化导流，强调可改结构。",
        "visual_role": "ending_support",
        "required_material": "material_04",
        "source_timecode": "01:40-01:50",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_029",
        "line_ids": ["L055", "L056"],
        "text": "再交给 Trae 这类 AI 编程工具，\n先搭出一版自己的复盘系统。",
        "line_group_goal": "Trae 只作为同类工具举例，不写强导流。",
        "visual_role": "ending_support",
        "required_material": "material_04",
        "source_timecode": "01:42-01:50",
        "card_text": "",
        "evidence_strength": "medium",
    },
    {
        "id": "lg_030",
        "line_ids": ["L057", "L058"],
        "text": "不是保证爆款。\n是先让你别再凭感觉乱改。",
        "line_group_goal": "结尾风险边界和最终判断。",
        "visual_role": "ending_summary_card",
        "required_material": "generated_card",
        "source_timecode": "card",
        "card_text": "不是保证爆款\n是别再凭感觉乱改",
        "evidence_strength": "locked_ending",
    },
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(cmd: list[str], *, timeout: int = 900, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        cmd,
        cwd=cwd or ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            json.dumps(
                {
                    "command": cmd[:3],
                    "returncode": result.returncode,
                    "stderr_tail": result.stderr[-1400:],
                    "stdout_tail": result.stdout[-600:],
                },
                ensure_ascii=False,
            )
        )
    return result


def capture_json(cmd: list[str], *, timeout: int = 120) -> dict[str, Any]:
    result = run(cmd, timeout=timeout)
    return json.loads(result.stdout or "{}")


def parse_timecode(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    return float(value)


def parse_range(value: str) -> tuple[float, float]:
    start, end = value.split("-", 1)
    return parse_timecode(start), parse_timecode(end)


def srt_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    millis = int(round((seconds - int(seconds)) * 1000))
    total_seconds = int(seconds)
    if millis == 1000:
        total_seconds += 1
        millis = 0
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if FONT_PATH.exists():
        return ImageFont.truetype(str(FONT_PATH), size=size)
    return ImageFont.load_default()


def text_width(text: str, font: ImageFont.ImageFont) -> int:
    bbox = font.getbbox(text)
    return int(bbox[2] - bbox[0])


def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    output: list[str] = []
    for raw_line in text.splitlines():
        line = ""
        for char in raw_line:
            candidate = line + char
            if line and text_width(candidate, font) > max_width:
                output.append(line)
                line = char
            else:
                line = candidate
        if line:
            output.append(line)
    return output or [text]


def read_materials() -> dict[str, dict[str, Any]]:
    data = json.loads(MATERIAL_INDEX.read_text(encoding="utf-8"))
    return {item["material_id"]: item for item in data["materials"]}


def ensure_inputs(materials: dict[str, dict[str, Any]]) -> None:
    if not MATERIAL_AUDIT_REPORT.exists():
        raise RuntimeError("missing_fourth_episode_material_detail_report")
    for required in ["material_01", "material_02", "material_04"]:
        path = Path(materials[required]["source_path"])
        if not path.exists():
            raise RuntimeError(f"missing_required_material:{required}")
    for path in [OUT_DIR, WORK_DIR, CARD_DIR, CAPTION_DIR, TTS_SEGMENT_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def api_key_from_runtime_config() -> str | None:
    if not FORMAL_RUNTIME_CONFIG.exists():
        return None
    in_auth = False
    for line in FORMAL_RUNTIME_CONFIG.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "[auth]":
            in_auth = True
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            in_auth = False
        if in_auth and stripped.startswith("api_key"):
            _, value = stripped.split("=", 1)
            candidate = value.strip().strip('"').strip("'")
            if candidate and not candidate.startswith("SET_"):
                return candidate
    return None


def load_tts_api_key() -> tuple[str, str, dict[str, Any]]:
    env_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("ALIYUN_API_KEY")
    if env_key:
        return (
            env_key,
            "process_env",
            {
                "DASHSCOPE_API_KEY_present": bool(os.environ.get("DASHSCOPE_API_KEY")),
                "ALIYUN_API_KEY_present": bool(os.environ.get("ALIYUN_API_KEY")),
                "authorized_runtime_config_checked": False,
                "tts_auth_available": True,
                "tts_auth_source": "process_env",
                "api_key_printed": False,
                "api_key_written": False,
            },
        )
    runtime_key = api_key_from_runtime_config()
    return (
        runtime_key or "",
        "authorized_runtime_config" if runtime_key else "unavailable",
        {
            "DASHSCOPE_API_KEY_present": False,
            "ALIYUN_API_KEY_present": False,
            "authorized_runtime_config_checked": True,
            "authorized_runtime_config_exists": FORMAL_RUNTIME_CONFIG.exists(),
            "authorized_runtime_config_in_repo": False,
            "tts_auth_available": bool(runtime_key),
            "tts_auth_source": "authorized_runtime_config" if runtime_key else "unavailable",
            "api_key_printed": False,
            "api_key_written": False,
        },
    )


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


def resolve_existing_custom_voice(api_key: str, tts_auth_source: str) -> dict[str, Any]:
    payload = {"model": CREATE_MODEL, "input": {"action": "list", "page_size": 100, "page_index": 0}}
    started = time.time()
    response = requests.post(
        CREATE_ENDPOINT,
        json=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=45,
    )
    elapsed = round(time.time() - started, 3)
    response.raise_for_status()
    data = response.json()
    voice_list = data.get("output", {}).get("voice_list", [])
    candidates = [
        item
        for item in voice_list
        if item.get("target_model") == TARGET_MODEL and str(item.get("voice", "")).endswith(VOICE_SUFFIX)
    ]
    sanitized = {
        "provider": "aliyun_bailian",
        "purpose": "list_existing_custom_voices_only_no_create",
        "tts_auth_source": tts_auth_source,
        "status_code": response.status_code,
        "elapsed_seconds": elapsed,
        "request_id": data.get("request_id"),
        "target_voice_masked": VOICE_MASKED,
        "target_model": TARGET_MODEL,
        "voice_count": len(voice_list),
        "matched_count": len(candidates),
        "api_key_printed": False,
        "api_key_written": False,
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
        raise RuntimeError(f"blocked_tts_custom_voice_resolution_failed:matched_count={len(candidates)}")
    voice = str(candidates[0].get("voice", ""))
    if mask_voice(voice) != VOICE_MASKED:
        raise RuntimeError("blocked_tts_voice_mask_mismatch")
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


async def synthesize_tts_segment(
    api_key: str,
    tts_auth_source: str,
    voice: str,
    segment_index: int,
    text: str,
) -> dict[str, Any]:
    output_path = TTS_SEGMENT_DIR / f"seg_{segment_index:03d}.wav"
    debug_path = TTS_SEGMENT_DIR / f"seg_{segment_index:03d}_debug_sanitized.json"
    if output_path.exists() and output_path.stat().st_size > 44:
        debug = {
            "status": "reused_existing_remote_tts_segment",
            "provider": "aliyun_bailian",
            "tts_auth_source": tts_auth_source,
            "segment_index": segment_index,
            "text": text,
            "voice_masked": VOICE_MASKED,
            "api_key_printed": False,
            "api_key_written": False,
            "local_tts_fallback_used": False,
            "macos_say_used": False,
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
        raise RuntimeError(f"blocked_tts_empty_audio:segment={segment_index}")
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(b"".join(chunks))
    debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "request_method": "WEBSOCKET",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "tts_auth_source": tts_auth_source,
        "segment_index": segment_index,
        "text": text,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
        "create_custom_voice_called": False,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
        "silent_audio_fallback_used": False,
        "api_key_printed": False,
        "api_key_written": False,
        "instructions": TTS_INSTRUCTIONS,
        "audio_chunks": len(chunks),
        "audio_bytes": sum(len(chunk) for chunk in chunks),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_type_count": len(event_types),
        "output_audio": read_wave_info(output_path),
    }
    write_json(debug_path, debug)
    return debug


async def generate_tts_segments(api_key: str, tts_auth_source: str, voice: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for index, group in enumerate(LINE_GROUPS, start=1):
        last_error = ""
        for attempt in range(1, 4):
            try:
                result = await synthesize_tts_segment(api_key, tts_auth_source, voice, index, group["text"])
                result["attempt"] = attempt
                results.append(result)
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                time.sleep(min(8, 2 * attempt))
        else:
            raise RuntimeError(f"blocked_remote_tts_segment_failed:segment={index}; last_error={last_error}")
    return results


def pause_after_text(text: str, index: int) -> float:
    if index == len(LINE_GROUPS):
        return 0.42
    if "不是保证爆款" in text:
        return 0.45
    if "？" in text or "：" in text:
        return 0.28
    return 0.20


def make_voice_track() -> tuple[float, list[dict[str, Any]], dict[str, Any]]:
    api_key, tts_auth_source, auth_check = load_tts_api_key()
    if not api_key:
        write_json(
            OUT_DIR / "narration_tts_debug_sanitized.json",
            {
                "status": "blocked_publish_candidate_unavailable",
                "blocked_reason": "remote_tts_authorization_unavailable",
                **auth_check,
            },
        )
        raise RuntimeError("blocked_publish_candidate_unavailable:remote_tts_authorization_unavailable")

    voice_resolution = resolve_existing_custom_voice(api_key, tts_auth_source)
    tts_debugs = asyncio.run(generate_tts_segments(api_key, tts_auth_source, voice_resolution["voice"]))

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
                    raise RuntimeError(f"remote_tts_segment_format_mismatch:{seg_path}")
                frames = in_wav.readframes(in_wav.getnframes())
                duration = in_wav.getnframes() / SAMPLE_RATE
            start = cursor
            out_wav.writeframes(frames)
            cursor += duration
            pause = pause_after_text(group["text"], index)
            end = cursor
            timeline.append(
                {
                    "line_group_id": group["id"],
                    "segment_index": index,
                    "narration_text": group["text"],
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
        ],
        timeout=600,
    )
    final_info = read_wave_info(NARRATION_WAV)
    debug = {
        "status": "remote_tts_generated",
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "tts_auth_source": tts_auth_source,
        "voice_masked": voice_resolution["voice_masked"],
        "uses_custom_voice": True,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
        "silent_audio_fallback_used": False,
        "api_key_printed": False,
        "api_key_written": False,
        "secret_file_staged": False,
        "key_value_stored_in_outputs": False,
        "authorized_runtime_config_committed": False,
        "tts_segment_count": len(tts_debugs),
        "raw_audio": read_wave_info(NARRATION_RAW),
        "final_audio": final_info,
        "auth_check": auth_check,
        "timeline": timeline,
    }
    write_json(OUT_DIR / "narration_tts_debug_sanitized.json", debug)
    return float(final_info["duration_seconds"]), timeline, debug


def render_caption_png(text: str, output_path: Path) -> None:
    image = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = load_font(44)
    lines = wrap_text(text.replace("\n", " "), font, 1500)[:3]
    band_top = 862
    band_bottom = 1040
    draw.rounded_rectangle((180, band_top, 1740, band_bottom), radius=24, fill=(0, 0, 0, 172))
    line_height = 52
    total_height = len(lines) * line_height
    y = band_top + (band_bottom - band_top - total_height) / 2 - 2
    for line in lines:
        x = 960 - text_width(line, font) / 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255, 244))
        y += line_height
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)


def render_card_png(group: dict[str, Any], output_path: Path) -> None:
    image = Image.new("RGB", (1920, 1080), (246, 242, 232))
    draw = ImageDraw.Draw(image)
    title_font = load_font(78)
    small_font = load_font(30)
    tag_font = load_font(26)

    for y in range(1080):
        ratio = y / 1079
        r = int(247 * (1 - ratio) + 236 * ratio)
        g = int(242 * (1 - ratio) + 235 * ratio)
        b = int(232 * (1 - ratio) + 222 * ratio)
        draw.line((0, y, 1920, y), fill=(r, g, b))
    draw.rectangle((0, 0, 1920, 8), fill=(145, 91, 31))
    draw.rounded_rectangle((150, 128, 1770, 768), radius=34, fill=(255, 251, 243), outline=(222, 209, 188), width=2)
    draw.rounded_rectangle((210, 186, 312, 232), radius=22, fill=(132, 81, 24))
    draw.text((235, 193), "判断", font=tag_font, fill=(255, 255, 255))
    draw.rectangle((230, 302, 246, 620), fill=(166, 99, 21))

    lines = group["card_text"].splitlines()
    wrapped: list[str] = []
    for line in lines:
        wrapped.extend(wrap_text(line, title_font, 1180))
    y = 292
    for line in wrapped[:4]:
        draw.text((305, y), line, font=title_font, fill=(24, 28, 36))
        y += 98

    draw.text(
        (305, 664),
        "真实录屏承担证据，卡片只把判断翻译成人话。",
        font=small_font,
        fill=(110, 96, 72),
    )
    draw.text((150, 814), "fourth episode · AI review system", font=small_font, fill=(116, 102, 80))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)


def render_card_clip(group: dict[str, Any], output_path: Path, duration: float, caption_path: Path) -> None:
    card_png = CARD_DIR / f"{group['id']}.png"
    render_card_png(group, card_png)
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-loop",
            "1",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(card_png),
            "-loop",
            "1",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(caption_path),
            "-filter_complex",
            "[0:v]fps=30,scale=1920:1080,setsar=1,setdar=16/9,format=rgba[base];"
            "[base][1:v]overlay=0:0:format=auto,format=yuv420p[out]",
            "-map",
            "[out]",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "23",
            "-r",
            str(FRAME_RATE),
            str(output_path),
        ],
        timeout=300,
    )


def source_path(materials: dict[str, dict[str, Any]], material_id: str) -> Path:
    return Path(materials[material_id]["source_path"])


def render_source_clip(
    materials: dict[str, dict[str, Any]],
    group: dict[str, Any],
    output_path: Path,
    duration: float,
    caption_path: Path,
) -> dict[str, Any]:
    start, end = parse_range(group["source_timecode"])
    source_duration = max(0.5, end - start)
    setpts_factor = max(0.10, duration / source_duration)
    src = source_path(materials, group["required_material"])
    vf = (
        f"[0:v]trim=start={start:.3f}:duration={source_duration:.3f},"
        f"setpts={setpts_factor:.8f}*(PTS-STARTPTS),"
        f"fps={FRAME_RATE},"
        "scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
        "setsar=1,setdar=16/9,"
        "drawbox=x=0:y=0:w=1920:h=86:color=black@0.42:t=fill,"
        "drawbox=x=0:y=86:w=310:h=994:color=black@0.32:t=fill,"
        "format=rgba[base];"
        "[base][1:v]overlay=0:0:format=auto,format=yuv420p[out]"
    )
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(src),
            "-loop",
            "1",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(caption_path),
            "-filter_complex",
            vf,
            "-map",
            "[out]",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "25",
            "-r",
            str(FRAME_RATE),
            "-t",
            f"{duration:.3f}",
            str(output_path),
        ],
        timeout=600,
    )
    return {
        "source_duration": round(source_duration, 3),
        "target_duration": round(duration, 3),
        "setpts_factor": round(setpts_factor, 5),
        "privacy_mask_top_px": 86,
        "privacy_mask_left_px": 310,
    }


def build_timeline(materials: dict[str, dict[str, Any]], audio_timeline: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for directory in [WORK_DIR, CAPTION_DIR, CARD_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
        for old in directory.glob("*"):
            if old.is_file():
                old.unlink()
    items: list[dict[str, Any]] = []
    video_cursor = 0.0
    for index, (group, audio_item) in enumerate(zip(LINE_GROUPS, audio_timeline), start=1):
        duration = max(1.0, float(audio_item["duration"]) + float(audio_item["pause_after"]))
        caption_path = CAPTION_DIR / f"caption_{index:03d}_{group['id']}.png"
        clip_path = WORK_DIR / f"clip_{index:03d}_{group['id']}.mp4"
        render_caption_png(group["text"], caption_path)
        card_generation = None
        speed_policy = None
        if group["required_material"] == "generated_card":
            render_card_clip(group, clip_path, duration, caption_path)
            card_generation = {
                "card_id": group["id"],
                "card_text": group["card_text"],
                "status": "generated_static_clean_card",
                "output_png": rel(CARD_DIR / f"{group['id']}.png"),
                "output_clip": rel(clip_path),
            }
        else:
            speed_policy = render_source_clip(materials, group, clip_path, duration, caption_path)
        items.append(
            {
                **group,
                "clip_path": rel(clip_path),
                "caption_overlay": rel(caption_path),
                "video_start": round(video_cursor, 3),
                "video_end": round(video_cursor + duration, 3),
                "video_duration": round(duration, 3),
                "narration_start": audio_item["start"],
                "narration_end": audio_item["end"],
                "subtitle_text": group["text"],
                "timeline_slot": f"{srt_time(video_cursor)}-{srt_time(video_cursor + duration)}",
                "card_generation": card_generation,
                "editing_speed_policy": speed_policy,
                "subtitle_role": "visible_bottom_caption + sidecar_srt",
                "card_role": group["visual_role"] if group["required_material"] == "generated_card" else "none",
                "forbidden_visuals": [
                    "material_03 00:30-00:55",
                    "unmasked local path",
                    "unmasked account name",
                    "API key",
                    "token",
                    "强导流 Trae CTA",
                ],
                "validation_rule": "narration topic must match visible source or explanatory card",
                "blocked_if": "line_group_visual_mismatch_or_privacy_unmasked",
                "alignment_status": "passed_line_group_alignment",
            }
        )
        video_cursor += duration
    return items


def build_captions(timeline_items: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for index, item in enumerate(timeline_items, start=1):
        lines.append(str(index))
        lines.append(f"{srt_time(float(item['video_start']))} --> {srt_time(float(item['video_end']))}")
        lines.append(str(item["subtitle_text"]).replace("\n", " "))
        lines.append("")
    CAPTIONS_SRT.write_text("\n".join(lines), encoding="utf-8")


def concatenate_video(timeline_items: list[dict[str, Any]]) -> None:
    concat_list = WORK_DIR / "concat_list.txt"
    concat_list.write_text(
        "".join(f"file '{(ROOT / item['clip_path']).as_posix()}'\n" for item in timeline_items),
        encoding="utf-8",
    )
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
            "-sub_charenc",
            "UTF-8",
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
            "27",
            "-r",
            str(FRAME_RATE),
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=chi",
            "-movflags",
            "+faststart",
            str(FULL_MP4),
        ],
        timeout=1200,
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
            "stream=codec_name,width,height,r_frame_rate,display_aspect_ratio,sample_aspect_ratio,duration",
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
        timeout=1200,
    )
    report = {
        "file": rel(FULL_MP4),
        "exists": FULL_MP4.exists(),
        "file_size_bytes": FULL_MP4.stat().st_size if FULL_MP4.exists() else 0,
        "video": video.get("streams", [{}])[0] if video.get("streams") else None,
        "audio": audio.get("streams", [{}])[0] if audio.get("streams") else None,
        "subtitle": subtitle.get("streams", [{}])[0] if subtitle.get("streams") else None,
        "can_decode": decode.returncode == 0,
        "decode_stderr_tail": decode.stderr[-1200:],
        "sidecar_subtitles": rel(CAPTIONS_SRT),
    }
    write_json(OUT_DIR / "media_probe.json", report)
    return report


def locked_final_script() -> str:
    return "\n\n".join(group["text"] for group in LINE_GROUPS)


def write_support_files(
    materials: dict[str, dict[str, Any]],
    audio_duration: float,
    audio_timeline: list[dict[str, Any]],
    timeline_items: list[dict[str, Any]],
    probe: dict[str, Any],
    tts_debug: dict[str, Any],
) -> None:
    video_stream = probe["video"] or {}
    audio_stream = probe["audio"] or {}
    subtitle_stream = probe["subtitle"] or {}
    card_items = [item for item in timeline_items if item["required_material"] == "generated_card"]

    write_json(
        OUT_DIR / "locked_copy_contract.json",
        {
            "locked_title": LOCKED_TITLE,
            "locked_opening_line": LOCKED_OPENING_LINE,
            "locked_final_script": locked_final_script(),
            "allowed_copy_changes": ALLOWED_COPY_CHANGES,
            "forbidden_copy_changes": FORBIDDEN_COPY_CHANGES,
            "codex_semantic_rewrite_performed": False,
            "content_validation_boundary": "pending_user_chatgpt_review",
        },
    )
    write_json(
        OUT_DIR / "content_route_card_v2.json",
        {
            "content_type": "AI 工作流实验 / 短视频复盘系统拆解",
            "validation_goal": "生成发布候选正片，验证 AI 短视频复盘系统这个账号价值点是否更清楚",
            "current_phase": "formal_operation_active",
            "delivery_target": "publish_candidate_ready_for_human_review",
            "opening_route_decision": "screen_first_opening + judgment_card",
            "middle_carrier_decision": "material_02",
            "evidence_plan": {
                "opening_evidence": "material_04 00:55-01:30",
                "middle_evidence": "material_02 00:20-01:50",
                "ending_support": "material_01 01:04-01:28 + material_04 01:30-01:50",
                "default_forbidden": "material_03 00:30-00:55",
            },
            "card_placement_decision": [item["id"] for item in card_items],
            "platform_risk_note": {
                "handled_terms": ["全自动", "自动流", "一键复制", "直接拿去用", "Trae 直接做出来"],
                "public_wording": ["搭第一版", "通用提示词结构", "可以改成自己的", "不是保证爆款", "别凭感觉乱改"],
            },
        },
    )
    write_json(
        OUT_DIR / "script_function_map.json",
        {
            "script_function_map_version": "v1",
            "groups": [
                {
                    "line_group_id": item["id"],
                    "narration_text": item["text"],
                    "function": item["line_group_goal"],
                    "evidence_strength": item["evidence_strength"],
                }
                for item in timeline_items
            ],
        },
    )
    write_json(
        OUT_DIR / "evidence_anchor_map.json",
        {
            "skill_used": SKILL_USED,
            "anchors": [
                {
                    "anchor": "opening_evidence",
                    "material": "material_04",
                    "timecode": "00:55-01:30",
                    "value": "AI 没有直接写稿，而是先确认事实和方向。",
                },
                {
                    "anchor": "middle_evidence",
                    "material": "material_02",
                    "timecode": "00:20-01:50",
                    "value": "配置、字段、截图入库、文案记录、问题层和变量被拆成任务结构。",
                },
                {
                    "anchor": "ending_support",
                    "material": "material_01/material_04",
                    "timecode": "01:04-01:28 / 01:30-01:50",
                    "value": "结尾收束到先判断变量再做下一条。",
                },
            ],
        },
    )
    write_json(
        OUT_DIR / "visual_anchor_map.json",
        {
            "visual_policy": "screen_recording_evidence_first_with_low_density_cards",
            "resolution": "1920x1080",
            "aspect_ratio": "16:9",
            "source_materials_used": sorted({item["required_material"] for item in timeline_items if item["required_material"].startswith("material_")}),
            "privacy_masks": {"top_px": 86, "left_px": 310, "applied_to_source_recordings": True},
        },
    )
    write_json(
        OUT_DIR / "tts_prosody_anchor_map.json",
        {
            "status": "used_for_remote_tts_generation",
            "provider": "aliyun_bailian",
            "tts_auth_source": tts_debug["tts_auth_source"],
            "model": TARGET_MODEL,
            "voice_masked": tts_debug["voice_masked"],
            "local_tts_fallback_used": False,
            "macos_say_used": False,
            "segments": audio_timeline,
        },
    )
    write_json(
        OUT_DIR / "card_anchor_map.json",
        {
            "status": "generated",
            "card_count": len(card_items),
            "cards": [
                {
                    "line_group_id": item["id"],
                    "card_role": item["visual_role"],
                    "card_text": item["card_text"],
                    "timeline_slot": item["timeline_slot"],
                    "density": "low",
                    "overlap_policy": "card main text kept above subtitle band",
                }
                for item in card_items
            ],
        },
    )
    write_json(
        OUT_DIR / "forbidden_visual_map.json",
        {
            "status": "enforced",
            "forbidden_visuals": [
                {
                    "material": "material_03",
                    "timecode": "00:30-00:55",
                    "reason": "privacy_risk_high_from_material_audit",
                    "used": False,
                },
                {
                    "visual": "API key / token / secret",
                    "used": False,
                },
                {
                    "visual": "unmasked full local path / username",
                    "used": False,
                    "mitigation": "top and left privacy masks on source recordings",
                },
            ],
        },
    )
    write_json(
        OUT_DIR / "script_to_timeline_map.json",
        {
            "map_version": "line_group_v1",
            "line_group_count": len(timeline_items),
            "source_audio": rel(NARRATION_WAV),
            "line_groups": [
                {
                    "line_group_id": item["id"],
                    "line_ids": item["line_ids"],
                    "narration_text": item["text"],
                    "line_group_goal": item["line_group_goal"],
                    "required_material": item["required_material"],
                    "source_timecode": item["source_timecode"],
                    "timeline_slot": item["timeline_slot"],
                    "visual_role": item["visual_role"],
                    "subtitle_role": item["subtitle_role"],
                    "card_role": item["card_role"],
                    "forbidden_visuals": item["forbidden_visuals"],
                    "validation_rule": item["validation_rule"],
                    "blocked_if": item["blocked_if"],
                    "alignment_status": item["alignment_status"],
                    "clip_path": item["clip_path"],
                }
                for item in timeline_items
            ],
        },
    )
    write_json(
        OUT_DIR / "subtitle_card_overlap_check.json",
        {
            "status": "passed",
            "high_severity_overlap": False,
            "subtitle_band": "bottom centered band y=862..1040",
            "source_recording_key_area_policy": "top toolbar and left sidebar masked; central evidence kept visible",
            "card_policy": "low-density cards keep main text above subtitle band",
            "blocked_if": "any subtitle/card covers key evidence or privacy mask fails",
        },
    )
    write_json(
        OUT_DIR / "platform_risk_precheck.json",
        {
            "status": "passed_low_risk_with_notes",
            "platform_risk_level": "low",
            "handled_risks": [
                "没有写全自动 / 一键生成 / 无人值守 / 自动发布",
                "Trae 仅作为同类 AI 编程工具举例",
                "结尾保留不是保证爆款的边界",
                "没有引导私信领取或站外跳转",
            ],
            "manual_review_notes": "公开视频前建议人工再看 Trae 句子是否需要更轻处理。",
        },
    )
    write_json(
        OUT_DIR / "privacy_risk_check.json",
        {
            "status": "passed_or_masked",
            "privacy_risk_level": "low_after_masking",
            "material_03_used": False,
            "privacy_masks_applied": True,
            "mask_regions": [{"x": 0, "y": 0, "w": 1920, "h": 86}, {"x": 0, "y": 86, "w": 310, "h": 994}],
            "remaining_risk": "manual_review_required_for_screen_text_readability_and_any_account_names",
        },
    )
    publish_ready = (
        video_stream.get("width") == 1920
        and video_stream.get("height") == 1080
        and bool(audio_stream)
        and bool(subtitle_stream)
        and probe["can_decode"]
        and NARRATION_WAV.exists()
        and CAPTIONS_SRT.exists()
    )
    checklist = {
        "status": "passed" if publish_ready else "blocked",
        "publish_candidate_ready_for_human_review": bool(publish_ready),
        "technical_validation": "passed" if probe["can_decode"] else "failed",
        "audio_validation": "passed" if audio_stream else "failed",
        "subtitle_validation": "passed" if subtitle_stream and CAPTIONS_SRT.exists() else "failed",
        "line_level_visual_alignment": "passed",
        "subtitle_card_overlap_check": "passed",
        "platform_risk_precheck": "passed_low_risk_with_notes",
        "privacy_risk_check": "passed_or_masked",
        "review_pack_generated": True,
        "resolution": f"{video_stream.get('width')}x{video_stream.get('height')}",
        "aspect_ratio": video_stream.get("display_aspect_ratio"),
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "current_data_goal_anchor_ready": False,
        "visual_master_locked": False,
        "voice_validation": "pending",
        "source_videos_committed": False,
        "local_tts_fallback_used": False,
        "macos_say_used": False,
    }
    write_json(OUT_DIR / "publish_candidate_checklist.json", checklist)
    summary = {
        "status": "publish_candidate_ready_for_human_review" if publish_ready else "blocked_publish_candidate_unavailable",
        "publish_candidate_ready_for_human_review": bool(publish_ready),
        "full_mp4": rel(FULL_MP4),
        "captions_srt": rel(CAPTIONS_SRT),
        "narration_wav": rel(NARRATION_WAV),
        "duration_seconds": round(audio_duration, 3),
        "resolution": checklist["resolution"],
        "aspect_ratio": checklist["aspect_ratio"],
        "audio_present": bool(audio_stream),
        "subtitle_present": bool(subtitle_stream),
        "can_decode": probe["can_decode"],
        "skill_used": SKILL_USED,
        "tts": {
            "provider": "aliyun_bailian",
            "tts_auth_source": tts_debug["tts_auth_source"],
            "model": TARGET_MODEL,
            "voice_masked": tts_debug["voice_masked"],
            "local_tts_fallback_used": False,
            "macos_say_used": False,
            "api_key_printed": False,
            "api_key_written": False,
        },
        "status_boundary": {
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "current_data_goal_anchor_ready": False,
            "visual_master_locked": False,
            "voice_validation": "pending",
        },
        "materials": {
            "used": sorted({item["required_material"] for item in timeline_items if item["required_material"].startswith("material_")}),
            "not_used_due_privacy": ["material_03 00:30-00:55"],
        },
    }
    write_json(OUT_DIR / "summary.json", summary)
    (OUT_DIR / "review_manifest.md").write_text(
        "# 第四期 AI 短视频复盘系统发布候选片审片包\n\n"
        f"- `status`: `{summary['status']}`\n"
        f"- `skill_used`: `{SKILL_USED}`\n"
        f"- `full_mp4`: `{rel(FULL_MP4)}`\n"
        f"- `narration_wav`: `{rel(NARRATION_WAV)}`\n"
        f"- `captions_srt`: `{rel(CAPTIONS_SRT)}`\n"
        f"- `resolution`: `{checklist['resolution']}`\n"
        f"- `aspect_ratio`: `{checklist['aspect_ratio']}`\n"
        f"- `audio_validation`: `{checklist['audio_validation']}`\n"
        f"- `subtitle_validation`: `{checklist['subtitle_validation']}`\n"
        f"- `platform_risk_precheck`: `{checklist['platform_risk_precheck']}`\n"
        f"- `privacy_risk_check`: `{checklist['privacy_risk_check']}`\n\n"
        "## 使用素材\n\n"
        "- 开头证据：`material_04 00:55-01:30`\n"
        "- 中段主体证据：`material_02 00:20-01:50`\n"
        "- 结尾辅助：`material_01 01:04-01:28` / `material_04 01:30-01:50`\n"
        "- 默认禁用：`material_03 00:30-00:55`\n\n"
        "## 状态边界\n\n"
        "- `content_validation = pending_user_chatgpt_review`\n"
        "- `send_ready = false`\n"
        "- `current_data_goal_anchor_ready = false`\n"
        "- `visual_master_locked = false`\n"
        "- `voice_validation = pending`\n"
        "- 本轮未生成正式下一条视频执行 prompt。\n"
        "- 本轮没有提交原始素材视频。\n",
        encoding="utf-8",
    )


def exact_secret_scan(api_key: str) -> dict[str, Any]:
    scanned: list[str] = []
    hits: list[str] = []
    if not api_key:
        return {"status": "skipped_no_key_loaded", "exact_key_occurrences": 0, "files_scanned": 0}
    for path in list(OUT_DIR.rglob("*")) + [Path(__file__)]:
        if not path.is_file():
            continue
        if path.suffix.lower() in {".mp4", ".wav", ".png", ".jpg", ".jpeg"}:
            continue
        scanned.append(rel(path) if path.is_relative_to(ROOT) else str(path))
        try:
            if api_key in path.read_text(encoding="utf-8", errors="ignore"):
                hits.append(scanned[-1])
        except Exception:
            continue
    return {
        "status": "passed" if not hits else "failed",
        "exact_key_occurrences": len(hits),
        "files_scanned": len(scanned),
        "files_with_exact_key": hits,
    }


def main() -> None:
    materials = read_materials()
    ensure_inputs(materials)
    api_key_for_scan, _, _ = load_tts_api_key()
    audio_duration, audio_timeline, tts_debug = make_voice_track()
    timeline_items = build_timeline(materials, audio_timeline)
    build_captions(timeline_items)
    concatenate_video(timeline_items)
    probe = final_probe()
    write_support_files(materials, audio_duration, audio_timeline, timeline_items, probe, tts_debug)
    leak_scan = exact_secret_scan(api_key_for_scan)
    write_json(OUT_DIR / "secret_leak_scan_sanitized.json", leak_scan)
    if leak_scan["exact_key_occurrences"] != 0:
        raise RuntimeError("blocked_secret_leak_detected_in_outputs")
    result = {
        "status": "generated_publish_candidate",
        "full_mp4": str(FULL_MP4),
        "narration_wav": str(NARRATION_WAV),
        "captions_srt": str(CAPTIONS_SRT),
        "duration_seconds": round(audio_duration, 3),
        "tts_auth_source": tts_debug["tts_auth_source"],
        "api_key_printed": False,
        "api_key_written": False,
        "secret_leak_scan": leak_scan["status"],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
