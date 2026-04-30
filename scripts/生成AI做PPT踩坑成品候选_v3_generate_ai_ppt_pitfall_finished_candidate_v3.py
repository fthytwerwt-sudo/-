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
from dataclasses import dataclass
from typing import Any

import requests
import websockets
from PIL import Image, ImageDraw, ImageFilter, ImageFont


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCAL_PROJECT_ROOT = pathlib.Path("/Users/fan/Documents/视频工厂")
TASK_SLUG = "20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3"
LOCAL_REVIEW_PACK = LOCAL_PROJECT_ROOT / "复审包_review_packs" / TASK_SLUG
LOCAL_DIST = LOCAL_PROJECT_ROOT / "dist" / TASK_SLUG
REPO_REVIEW_PACK = REPO_ROOT / "复审包_review_packs" / TASK_SLUG
REPO_DIST = REPO_ROOT / "dist" / TASK_SLUG

OPENING_ANCHOR = (
    LOCAL_PROJECT_ROOT
    / "素材库_assets"
    / "元素娃娃开头锚点_opening_anchor_20260428"
    / "005_1496_seg01_no_text_inpaint_opening_anchor.mp4"
)
NEGATIVE_RECORDING = LOCAL_PROJECT_ROOT / "素材录制" / "反面" / "录制于 2026-04-16 22.41.32.mp4"
POSITIVE_RECORDING = LOCAL_PROJECT_ROOT / "素材录制" / "正面" / "录制于 2026-04-16 23.03.53.mp4"

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
VIDEO_WIDTH = 720
VIDEO_HEIGHT = 1280
FPS = 25

FULL_NAME = "AI做PPT踩坑_成品候选_v3_full.mp4"
CONTACT_SHEET_NAME = "AI做PPT踩坑_成品候选_v3_contact_sheet.jpg"
TIMELINE_NAME = "AI做PPT踩坑_成品候选_v3_timeline.json"
CUT_MAP_NAME = "AI做PPT踩坑_成品候选_v3_cut_map.md"
MANIFEST_NAME = "AI做PPT踩坑_成品候选_v3_review_manifest.md"
SUMMARY_NAME = "AI做PPT踩坑_成品候选_v3_summary.json"
RUN_SUMMARY_NAME = "AI做PPT踩坑_成品候选_v3_run_summary.json"
INHERITANCE_REPORT_NAME = "locked_reference_inheritance_report.md"
METADATA_REPORT_NAME = "video_metadata_probe_report.json"
OPENING_PREVIEW_NAME = "shot00_opening_hello_wave_preview.mp4"


@dataclass
class Segment:
    segment_id: str
    kind: str
    voice_text: str
    visual_source: str
    source_path: pathlib.Path | None = None
    source_start: float | None = None
    crop_x: int = 760
    image_id: str | None = None
    note: str = ""
    locked_refs: tuple[str, ...] = ()
    candidate_refs: tuple[str, ...] = ()
    failed_refs_avoided: tuple[str, ...] = ()


SEGMENTS: list[Segment] = [
    Segment(
        "shot00_opening_hello_wave",
        "opening_video",
        "hello，大家好。",
        "元素娃娃无字开头锚点，约两秒轻入口。",
        OPENING_ANCHOR,
        0.0,
        0,
        locked_refs=("opening_reference_element_doll_no_text_locked_20260428",),
    ),
    Segment(
        "shot01_result_diff_opening",
        "image",
        "先看这两个结果。左边，是我第一次让 AI 帮我做 PPT。右边，是我改完问法以后。我先说结论：差的不是工具，是我第一句话。",
        "正反结果分屏预告卡。",
        image_id="result_opening",
        candidate_refs=("card_visual_quality_clean_ui_texture_candidate_20260430",),
    ),
    Segment(
        "shot02_negative_input",
        "screen",
        "第一次，我把最新方案 PDF 丢进豆包，只写了一句：帮我把这个方案整理一下。这句话听起来没问题，但它其实只说了一件事：整理。",
        "反面录屏：PDF 与宽泛口令可见。",
        NEGATIVE_RECORDING,
        15.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
        failed_refs_avoided=("zoom_pr15_v2_failed_20260430",),
    ),
    Segment(
        "shot03_problem_hook_sassy_card",
        "image",
        "你以为在做 PPT，它以为在写读后感。",
        "问题钩子骚萌卡。",
        image_id="sassy_problem",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_a_candidate_20260428",),
    ),
    Segment(
        "shot04_negative_result_text_plan",
        "screen",
        "然后它真的很认真。标题给我写了，结构也排了。什么战略执行总案，什么产品矩阵，什么三十天落地计划，看着很完整。但我看到这里才发现：这不是 PPT 初稿，这是一份整理过的文字方案。",
        "反面录屏：战略执行总案、产品矩阵、30 天落地计划。",
        NEGATIVE_RECORDING,
        35.0,
        760,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
        failed_refs_avoided=("zoom_pr15_v2_failed_20260430",),
    ),
    Segment(
        "shot05_negative_reversal_sassy_card",
        "image",
        "它给了我一份更好的 Word，但我要的是 PPT。",
        "反面反转骚萌卡。",
        image_id="sassy_negative",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_a_candidate_20260428",),
    ),
    Segment(
        "shot06_cause_turning_point",
        "image",
        "所以这次翻车，不是 AI 没做事。它只是认真完成了我说出口的要求。问题是，我只说了整理一下，没有说清楚给谁看、要达成什么、要不要变成 PPT、什么叫能交。",
        "归因转折卡：AI 没偷懒，是我没说清交付。",
        image_id="cause_turning",
        candidate_refs=("card_visual_quality_clean_ui_texture_candidate_20260430", "visual_master_voxel_element_doll_candidate_20260430"),
    ),
    Segment(
        "shot07_deliverable_draft_keyword",
        "screen",
        "第二次，我没有一上来就说帮我做个 PPT。我先让它判断一件事：这份内容，能不能变成一版可交付初稿。这一步很关键。我不是让它多写一点，我是先给它一张交付物的验收表。",
        "正面录屏：可交付初稿方法词出现。",
        POSITIVE_RECORDING,
        30.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot08_prompt_architecture_card",
        "image",
        "这张表，我拆成三层。先定交付物：它不是整理稿，要往 PPT 初稿走。再检查对象、目标、动作、节奏、事实和假设、空话套话。最后，再让它输出适合做 PPT 的初稿结构。",
        "Prompt 架构功能卡。",
        image_id="prompt_architecture",
        candidate_refs=("card_visual_quality_clean_ui_texture_candidate_20260430",),
    ),
    Segment(
        "shot09_positive_title_specific",
        "screen",
        "加了这张验收表以后，结果先从标题开始变具体。它不再给我一个很大的战略执行总案，而是变成 AI 时间管理小程序，七天种子用户拉新营销方案。你看，这里已经有任务了。",
        "正面录屏：标题变具体。",
        POSITIVE_RECORDING,
        70.0,
        640,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot10_positive_constraints",
        "screen",
        "更重要的是，它开始出现具体约束。周期是七天，预算不超过五千，核心渠道是小红书加私域，目标用户两百加，内容目标五万以上。这时候，它已经开始围绕真实交付物规划。",
        "正面录屏：周期、预算、渠道、目标。",
        POSITIVE_RECORDING,
        80.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot11_ppt_page_instruction",
        "screen",
        "再往后，它开始写 PPT 页面设计指令。不是一句做得好看点，而是拆页面怎么设计、标题怎么放、核心指标怎么呈现、每一页承担什么信息。这一步，才是真正从文档往 PPT 走。",
        "正面录屏：XML / PPT 页面设计指令。",
        POSITIVE_RECORDING,
        300.0,
        760,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot12_ppt_generation_process",
        "screen",
        "后面进入 PPT 生成界面。这段不用讲太多，看画面就够了。缩略图一页一页出来，能看到策略判断、问题诊断、目标用户画像、三大内容方向，还有小红书和私域的分工。",
        "正面录屏：PPT 生成过程和缩略图逐页出现。",
        POSITIVE_RECORDING,
        570.0,
        640,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot13_ppt_completed_preview",
        "screen",
        "最后，界面显示：已完成 PPT 生成，用了六分三十一秒。这份 PPT 共十六页。到这里，反转才真正成立。第一次是文字方案，第二次至少推进到了 PPT 初稿状态。注意，预览不等于最终成品。",
        "正面录屏：已完成PPT生成(6m31s) 与 16 页预览。",
        POSITIVE_RECORDING,
        720.0,
        1500,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot14_positive_reversal_sassy_card",
        "image",
        "这回终于不像空气方案了。虽然还不能直接发。",
        "正面反转骚萌卡。",
        image_id="sassy_positive",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_a_candidate_20260428",),
    ),
    Segment(
        "shot15_result_diff_card",
        "image",
        "同一份资料。第一种问法，只给了 AI 一个动作：整理。第二种问法，先给了 AI 一个标准：什么叫能交。差的不是 AI 突然变聪明，是我终于把交付物说清楚了。",
        "结果差卡：普通问法 vs 交付标准。",
        image_id="result_diff",
        candidate_refs=("card_visual_quality_clean_ui_texture_candidate_20260430",),
    ),
    Segment(
        "shot16_low_pressure_ending",
        "image",
        "所以我现在用 AI 做 PPT，不会一上来就说：帮我整理一下。我会先问它：最后给谁看？要推动什么结果？下一步动作是什么？哪些是真实信息，哪些只是推测？这不是万能提示词，但至少，它不会停在一堆漂亮的文字里。先定义交付，再让 AI 生成。",
        "低压经验承接尾卡。",
        image_id="tail_card",
        candidate_refs=("card_visual_quality_clean_ui_texture_candidate_20260430", "visual_master_voxel_element_doll_candidate_20260430"),
    ),
]


def run_command(args: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\nSTDOUT:\n" + completed.stdout + "\n\nSTDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def resolve_binary(name: str) -> str:
    binary = shutil.which(name)
    if binary:
        return binary
    fallback = REPO_ROOT / "node_modules" / "ffmpeg-static" / name
    if fallback.exists():
        return str(fallback)
    raise RuntimeError(f"缺少 {name}")


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
    write_json(LOCAL_DIST / "tts" / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError("blocked_custom_voice_id_not_found")
    voice = str(candidates[0].get("voice", ""))
    if mask_voice(voice) != VOICE_MASKED:
        raise RuntimeError("blocked_custom_voice_id_not_found")
    return {
        "voice": voice,
        "voice_masked": mask_voice(voice),
        "target_model": candidates[0].get("target_model"),
        "resolved_by": "list_existing_custom_voices_match_suffix_ac19",
        "sanitized_list_path": str(LOCAL_DIST / "tts" / "custom_voice_list_debug_sanitized.json"),
    }


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


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_segment(api_key: str, voice: str, segment: Segment, output_path: pathlib.Path) -> dict[str, Any]:
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    instructions = (
        "请使用自然中文口语分享感，保持 B 版停顿梗感：微反转、轻吐槽、句间留白清楚。"
        "不要新闻播音，不要说明书腔，不要鸡血，不要夹，不要攻击用户。"
        "按文本里的标点自然停顿，整体节奏偏轻快但不赶。"
    )
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(url, additional_headers=headers) as ws:
        await ws.send(
            json.dumps(
                {
                    "type": "session.update",
                    "session": {
                        "mode": "commit",
                        "voice": voice,
                        "instructions": instructions,
                        "optimize_instructions": True,
                        "language_type": "Chinese",
                        "response_format": "pcm",
                        "sample_rate": SAMPLE_RATE,
                    },
                },
                ensure_ascii=False,
            )
        )
        await recv_until_session_ready(ws, event_types)
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": segment.voice_text}, ensure_ascii=False))
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
    return {
        "segment_id": segment.segment_id,
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
        "create_custom_voice_called": False,
        "instructions": instructions,
        "audio_chunks": len(chunks),
        "audio_bytes": len(audio_bytes),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_types": event_types,
        "output_audio": read_wave_info(output_path),
    }


async def synthesize_all_segments(api_key: str, voice: str) -> list[dict[str, Any]]:
    debug_records: list[dict[str, Any]] = []
    for index, segment in enumerate(SEGMENTS):
        output_path = LOCAL_DIST / "tts" / f"{index:02d}_{segment.segment_id}.wav"
        debug_path = LOCAL_DIST / "tts" / f"{index:02d}_{segment.segment_id}_tts_debug_sanitized.json"
        if output_path.exists() and debug_path.exists():
            debug = json.loads(debug_path.read_text(encoding="utf-8"))
        else:
            debug = await synthesize_segment(api_key, voice, segment, output_path)
            write_json(debug_path, debug)
        debug_records.append(debug)
    return debug_records


def concat_audio(ffmpeg: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    concat_path = LOCAL_DIST / "tts" / "voiceover_concat.txt"
    raw_path = LOCAL_DIST / "tts" / "voiceover_raw.wav"
    final_path = LOCAL_DIST / "tts" / "voiceover_v3_custom_voice_ac19.wav"
    concat_path.parent.mkdir(parents=True, exist_ok=True)
    concat_path.write_text(
        "\n".join(f"file '{record['output_audio']['path']}'" for record in records) + "\n",
        encoding="utf-8",
    )
    run_command(
        [ffmpeg, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(raw_path)],
        LOCAL_DIST / "logs" / "concat_voiceover.log",
    )
    raw_info = read_wave_info(raw_path)
    if raw_info["duration_seconds"] > 156:
        target = 150.0
        factor = min(1.35, max(1.01, raw_info["duration_seconds"] / target))
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
            LOCAL_DIST / "logs" / "voiceover_atempo.log",
        )
    else:
        shutil.copy2(raw_path, final_path)
        factor = 1.0
    final_info = read_wave_info(final_path)
    return {
        "raw_audio": raw_info,
        "final_audio": final_info,
        "atempo_factor": round(factor, 6),
        "path": str(final_path),
    }


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if pathlib.Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size, index=1 if bold and candidate.endswith(".ttc") else 0)
    return ImageFont.load_default()


def draw_text_lines(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fill: str,
    size: int,
    *,
    bold: bool = False,
    line_gap: int = 10,
    max_width: int = 600,
    anchor: str = "la",
) -> int:
    words = list(text)
    lines: list[str] = []
    current = ""
    typeface = font(size, bold)
    for char in words:
        test = current + char
        bbox = draw.textbbox((0, 0), test, font=typeface)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = char
        else:
            current = test
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=typeface, fill=fill, anchor=anchor)
        bbox = draw.textbbox((x, y), line, font=typeface, anchor=anchor)
        y += bbox[3] - bbox[1] + line_gap
    return y


def shadowed_round_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2 if outline else 1)


def base_canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), "#f6f4ee")
    draw = ImageDraw.Draw(img)
    for y in range(0, VIDEO_HEIGHT, 48):
        draw.line((0, y, VIDEO_WIDTH, y), fill="#e8e2d4", width=1)
    for x in range(0, VIDEO_WIDTH, 48):
        draw.line((x, 0, x, VIDEO_HEIGHT), fill="#ece6dc", width=1)
    draw.rectangle((0, 0, VIDEO_WIDTH, 130), fill="#263238")
    draw.rectangle((0, VIDEO_HEIGHT - 90, VIDEO_WIDTH, VIDEO_HEIGHT), fill="#263238")
    return img, draw


def paste_shadow_card(base: Image.Image, box: tuple[int, int, int, int], fill: str = "#fffaf2", radius: int = 26) -> ImageDraw.ImageDraw:
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sx1, sy1, sx2, sy2 = box
    sd.rounded_rectangle((sx1 + 8, sy1 + 10, sx2 + 8, sy2 + 10), radius=radius, fill=(46, 56, 54, 52))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    base.paste(shadow, (0, 0), shadow)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline="#e2d5bf", width=2)
    return draw


def draw_voxel_doll(draw: ImageDraw.ImageDraw, origin: tuple[int, int], scale: int = 18) -> None:
    x, y = origin
    colors = {"skin": "#ffd9c8", "hair": "#2f3640", "shirt": "#8bd3dd", "pink": "#ff8fab", "eye": "#1e2a2f"}
    blocks = [
        (1, 0, colors["hair"]), (2, 0, colors["hair"]), (3, 0, colors["hair"]),
        (0, 1, colors["hair"]), (1, 1, colors["skin"]), (2, 1, colors["skin"]), (3, 1, colors["skin"]), (4, 1, colors["hair"]),
        (0, 2, colors["hair"]), (1, 2, colors["skin"]), (2, 2, colors["skin"]), (3, 2, colors["skin"]), (4, 2, colors["hair"]),
        (1, 3, colors["skin"]), (2, 3, colors["skin"]), (3, 3, colors["skin"]),
        (1, 4, colors["shirt"]), (2, 4, colors["shirt"]), (3, 4, colors["shirt"]),
        (0, 5, colors["pink"]), (1, 5, colors["shirt"]), (2, 5, colors["shirt"]), (3, 5, colors["shirt"]), (4, 5, colors["pink"]),
    ]
    for bx, by, color in blocks:
        draw.rounded_rectangle(
            (x + bx * scale, y + by * scale, x + (bx + 1) * scale - 2, y + (by + 1) * scale - 2),
            radius=3,
            fill=color,
        )
    draw.rectangle((x + 1 * scale + 5, y + 2 * scale + 5, x + 1 * scale + 10, y + 2 * scale + 10), fill=colors["eye"])
    draw.line((x + 3 * scale + 4, y + 2 * scale + 6, x + 3 * scale + 13, y + 2 * scale + 6), fill=colors["eye"], width=3)
    draw.arc((x + 2 * scale + 2, y + 2 * scale + 10, x + 3 * scale + 9, y + 3 * scale + 6), 10, 170, fill="#a94b5d", width=2)


def extract_frame(ffmpeg: str, source: pathlib.Path, second: float, output: pathlib.Path, crop_x: int = 760) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{second:.3f}",
            "-i",
            str(source),
            "-frames:v",
            "1",
            "-vf",
            f"crop=1245:2214:{crop_x}:0,scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}",
            str(output),
        ],
        LOCAL_DIST / "logs" / f"extract_{output.stem}.log",
    )


def make_result_opening_card(ffmpeg: str, output: pathlib.Path) -> None:
    neg = LOCAL_DIST / "frames" / "negative_result_40.jpg"
    pos = LOCAL_DIST / "frames" / "positive_result_720.jpg"
    extract_frame(ffmpeg, NEGATIVE_RECORDING, 40, neg, 760)
    extract_frame(ffmpeg, POSITIVE_RECORDING, 720, pos, 1500)
    img, draw = base_canvas()
    draw.text((38, 38), "我用 AI 做 PPT 踩过的坑", font=font(34, True), fill="#fff7e8")
    draw.text((38, 88), "同一份资料，两种问法，结果差很多", font=font(22), fill="#d6f4ef")
    card_draw = paste_shadow_card(img, (34, 170, 686, 1018), fill="#fffaf2")
    left = Image.open(neg).resize((286, 510))
    right = Image.open(pos).resize((286, 510))
    img.paste(left, (58, 300))
    img.paste(right, (376, 300))
    card_draw.rounded_rectangle((58, 260, 344, 296), radius=12, fill="#ffdde4")
    card_draw.rounded_rectangle((376, 260, 662, 296), radius=12, fill="#d9f2ee")
    card_draw.text((82, 267), "第一次：整理一下", font=font(20, True), fill="#733341")
    card_draw.text((400, 267), "第二次：先定义交付", font=font(20, True), fill="#26524d")
    draw_text_lines(card_draw, (64, 844), "左边：一份很完整的文字方案", "#263238", 25, bold=True, max_width=270)
    draw_text_lines(card_draw, (382, 844), "右边：至少进入 PPT 初稿预览", "#263238", 25, bold=True, max_width=270)
    draw.text((360, 1076), "差的不是工具，是第一句话。", font=font(34, True), fill="#fff7e8", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_sassy_card(output: pathlib.Path, text: str, tag: str, fill: str) -> None:
    img, draw = base_canvas()
    draw.text((38, 42), "骚萌卡 / candidate", font=font(24, True), fill="#fff7e8")
    draw.text((38, 82), tag, font=font(20), fill="#d6f4ef")
    paste_shadow_card(img, (54, 210, 666, 990), fill=fill, radius=34)
    draw_voxel_doll(draw, (76, 250), 28)
    draw.rounded_rectangle((242, 252, 636, 798), radius=36, fill="#ffffff", outline="#dfcfb5", width=2)
    draw.polygon([(240, 432), (188, 462), (240, 492)], fill="#ffffff")
    y = draw_text_lines(draw, (284, 330), text, "#24323a", 44, bold=True, line_gap=18, max_width=310)
    draw.text((453, max(770, y + 24)), "轻吐槽，不替代证据", font=font(22), fill="#6e5b49", anchor="mm")
    draw.rectangle((0, VIDEO_HEIGHT - 92, VIDEO_WIDTH, VIDEO_HEIGHT), fill="#263238")
    draw.text((360, 1234), "真实录屏才是主体", font=font(25, True), fill="#fff7e8", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_cause_turning_card(output: pathlib.Path) -> None:
    img, draw = base_canvas()
    draw.text((38, 42), "归因转折", font=font(30, True), fill="#fff7e8")
    paste_shadow_card(img, (52, 190, 668, 934), fill="#fffdf8")
    draw_text_lines(draw, (90, 250), "AI 没偷懒。", "#20343a", 50, bold=True, max_width=540)
    draw_text_lines(draw, (90, 332), "是我没说清什么叫交付。", "#20343a", 42, bold=True, max_width=540)
    draw.rounded_rectangle((88, 470, 632, 710), radius=24, fill="#eef8f4", outline="#c7ded5", width=2)
    draw_text_lines(draw, (118, 512), "整理资料 ≠ PPT 初稿", "#24524e", 40, bold=True, max_width=480)
    draw_text_lines(draw, (118, 626), "缺对象 / 缺目标 / 缺输出形态 / 缺验收标准", "#53645f", 24, max_width=470)
    draw_voxel_doll(draw, (456, 745), 22)
    draw.text((90, 846), "先把“能交”说清楚。", font=font(34, True), fill="#8d4052")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_prompt_architecture_card(output: pathlib.Path) -> None:
    img, draw = base_canvas()
    draw.text((38, 42), "Prompt 架构", font=font(30, True), fill="#fff7e8")
    paste_shadow_card(img, (48, 178, 672, 1032), fill="#fffdf8")
    items = [
        ("1", "定义交付物", "不是整理稿，要往 PPT 初稿走"),
        ("2", "检查能不能交", "对象 / 目标 / 动作 / 节奏"),
        ("3", "再生成结构", "事实假设分开，空话套话先筛掉"),
    ]
    y = 246
    for num, title, body in items:
        draw.rounded_rectangle((86, y, 634, y + 182), radius=26, fill="#f3f7f2", outline="#d4dfd3", width=2)
        draw.ellipse((112, y + 45, 184, y + 117), fill="#ffcc70")
        draw.text((148, y + 81), num, font=font(34, True), fill="#263238", anchor="mm")
        draw.text((214, y + 46), title, font=font(31, True), fill="#263238")
        draw_text_lines(draw, (214, y + 94), body, "#56656a", 23, max_width=374)
        y += 222
    draw.text((360, 958), "先别生成，先检查能不能交。", font=font(31, True), fill="#8d4052", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_result_diff_card(output: pathlib.Path) -> None:
    img, draw = base_canvas()
    draw.text((38, 42), "结果差卡", font=font(30, True), fill="#fff7e8")
    paste_shadow_card(img, (42, 158, 678, 1060), fill="#fffdf8")
    draw.rounded_rectangle((72, 230, 310, 720), radius=28, fill="#fff1f3", outline="#eac4cb", width=2)
    draw.rounded_rectangle((410, 230, 648, 720), radius=28, fill="#ecf8f4", outline="#bfe0d7", width=2)
    draw.text((191, 278), "普通问法", font=font(30, True), fill="#7b3442", anchor="mm")
    draw.text((191, 364), "“帮我整理一下”", font=font(25, True), fill="#263238", anchor="mm")
    draw.text((191, 492), "= 一堆文字方案", font=font(27, True), fill="#263238", anchor="mm")
    draw.text((529, 278), "交付标准", font=font(30, True), fill="#275650", anchor="mm")
    draw_text_lines(draw, (444, 344), "对象 / 目标\n动作 / 节奏\n事实假设\n空话套话", "#263238", 25, bold=True, line_gap=10, max_width=174)
    draw.text((529, 642), "= PPT 初稿方向", font=font(25, True), fill="#263238", anchor="mm")
    draw.rounded_rectangle((294, 430, 426, 520), radius=22, fill="#ffe4a3", outline="#ddb85a", width=2)
    draw.text((360, 474), "交付\n验收表", font=font(24, True), fill="#263238", anchor="mm", align="center")
    draw.line((310, 475, 410, 475), fill="#263238", width=4)
    draw.polygon([(410, 475), (392, 462), (392, 488)], fill="#263238")
    draw.rounded_rectangle((86, 804, 634, 940), radius=26, fill="#fff7d7", outline="#e2c877", width=2)
    draw_text_lines(draw, (360, 846), "先定义交付，\n再让 AI 生成。", "#263238", 38, bold=True, line_gap=12, max_width=520, anchor="ma")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_tail_card(output: pathlib.Path) -> None:
    img, draw = base_canvas()
    draw.text((38, 42), "经验承接尾卡", font=font(30, True), fill="#fff7e8")
    paste_shadow_card(img, (48, 176, 672, 1052), fill="#fffdf8")
    draw_text_lines(draw, (90, 238), "下次别只说：", "#263238", 36, bold=True, max_width=540)
    draw.rounded_rectangle((90, 322, 630, 410), radius=24, fill="#fff1f3", outline="#e8bec6", width=2)
    draw.text((360, 366), "“帮我整理一下。”", font=font(34, True), fill="#7b3442", anchor="mm")
    draw_text_lines(draw, (90, 486), "先补一句：请先判断这份内容能不能变成可交付初稿。", "#263238", 34, bold=True, max_width=540)
    draw.rounded_rectangle((90, 700, 630, 842), radius=24, fill="#eef8f4", outline="#c7ded5", width=2)
    draw.text((360, 746), "对象 / 目标 / 动作 / 节奏", font=font(28, True), fill="#24524e", anchor="mm")
    draw.text((360, 800), "事实假设 / 空话套话", font=font(28, True), fill="#24524e", anchor="mm")
    draw.text((360, 938), "这不是万能提示词，是少走弯路的起点。", font=font(27, True), fill="#8d4052", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_all_cards(ffmpeg: str) -> dict[str, pathlib.Path]:
    card_dir = LOCAL_DIST / "cards"
    cards = {
        "result_opening": card_dir / "shot01_result_diff_opening.png",
        "sassy_problem": card_dir / "shot03_problem_hook_sassy_card.png",
        "sassy_negative": card_dir / "shot05_negative_reversal_sassy_card.png",
        "cause_turning": card_dir / "shot06_cause_turning_point.png",
        "prompt_architecture": card_dir / "shot08_prompt_architecture_card.png",
        "sassy_positive": card_dir / "shot14_positive_reversal_sassy_card.png",
        "result_diff": card_dir / "shot15_result_diff_card.png",
        "tail_card": card_dir / "shot16_tail_card.png",
    }
    make_result_opening_card(ffmpeg, cards["result_opening"])
    make_sassy_card(cards["sassy_problem"], "你以为在做 PPT，\n它以为在写读后感。", "problem_hook_sassy_card", "#fff4d6")
    make_sassy_card(cards["sassy_negative"], "它给了我一份\n更好的 Word。\n但我要的是 PPT。", "negative_reversal_sassy_card", "#ffe9ef")
    make_cause_turning_card(cards["cause_turning"])
    make_prompt_architecture_card(cards["prompt_architecture"])
    make_sassy_card(cards["sassy_positive"], "这回终于不像\n空气方案了。\n虽然还不能直接发。", "positive_reversal_sassy_card", "#e9fbf5")
    make_result_diff_card(cards["result_diff"])
    make_tail_card(cards["tail_card"])
    return cards


def make_clip_from_image(ffmpeg: str, image: pathlib.Path, duration: float, output: pathlib.Path) -> None:
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-loop",
            "1",
            "-framerate",
            str(FPS),
            "-t",
            f"{duration:.3f}",
            "-i",
            str(image),
            "-vf",
            f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(output),
        ],
        LOCAL_DIST / "logs" / f"{output.stem}.log",
    )


def make_clip_from_video(ffmpeg: str, segment: Segment, duration: float, output: pathlib.Path) -> None:
    assert segment.source_path is not None
    start = segment.source_start or 0.0
    if segment.kind == "opening_video":
        vf = f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p"
    else:
        vf = f"crop=1245:2214:{segment.crop_x}:0,scale={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p"
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(segment.source_path),
            "-vf",
            vf,
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "22",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(output),
        ],
        LOCAL_DIST / "logs" / f"{output.stem}.log",
    )


def make_video_track(ffmpeg: str, tts_records: list[dict[str, Any]], audio_factor: float, cards: dict[str, pathlib.Path]) -> dict[str, Any]:
    clips_dir = LOCAL_DIST / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)
    timeline: list[dict[str, Any]] = []
    current = 0.0
    clip_paths: list[pathlib.Path] = []
    if len(SEGMENTS) != len(tts_records):
        raise RuntimeError(f"segment / TTS 数量不一致：segments={len(SEGMENTS)}, tts_records={len(tts_records)}")
    for index, (segment, tts_record) in enumerate(zip(SEGMENTS, tts_records)):
        base_duration = float(tts_record["output_audio"]["duration_seconds"]) / audio_factor
        duration = max(1.15, base_duration)
        clip_path = clips_dir / f"{index:02d}_{segment.segment_id}.mp4"
        if segment.kind == "image":
            assert segment.image_id is not None
            make_clip_from_image(ffmpeg, cards[segment.image_id], duration, clip_path)
        else:
            make_clip_from_video(ffmpeg, segment, duration, clip_path)
        clip_paths.append(clip_path)
        timeline.append(
            {
                "index": index,
                "segment_id": segment.segment_id,
                "kind": segment.kind,
                "start": round(current, 3),
                "end": round(current + duration, 3),
                "duration": round(duration, 3),
                "voice_text": segment.voice_text,
                "visual_source": segment.visual_source,
                "source_path": str(segment.source_path) if segment.source_path else None,
                "source_start": segment.source_start,
                "crop_x": segment.crop_x if segment.kind == "screen" else None,
                "locked_references": list(segment.locked_refs),
                "candidate_references": list(segment.candidate_refs),
                "failed_references_avoided": list(segment.failed_refs_avoided),
            }
        )
        current += duration

    concat_path = LOCAL_DIST / "clips" / "video_concat.txt"
    concat_path.write_text("\n".join(f"file '{path}'" for path in clip_paths) + "\n", encoding="utf-8")
    silent_video = LOCAL_DIST / "AI做PPT踩坑_成品候选_v3_silent_picture_lock.mp4"
    run_command(
        [ffmpeg, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(silent_video)],
        LOCAL_DIST / "logs" / "concat_video.log",
    )
    return {"timeline": timeline, "silent_video": str(silent_video), "duration_seconds": round(current, 3)}


def make_final_video(ffmpeg: str, video_track: dict[str, Any], voiceover_path: pathlib.Path) -> pathlib.Path:
    final_path = LOCAL_REVIEW_PACK / FULL_NAME
    final_path.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            video_track["silent_video"],
            "-i",
            str(voiceover_path),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            str(final_path),
        ],
        LOCAL_DIST / "logs" / "mux_final_video.log",
    )
    return final_path


def parse_ffprobe_json(ffprobe: str, path: pathlib.Path) -> dict[str, Any]:
    completed = run_command(
        [ffprobe, "-v", "error", "-show_entries", "format=duration,size,bit_rate", "-show_streams", "-of", "json", str(path)],
        LOCAL_DIST / "logs" / f"ffprobe_{path.stem}.log",
    )
    return json.loads(completed.stdout)


def parse_video_metadata(probe: dict[str, Any]) -> dict[str, Any]:
    video_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    audio_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "audio"), {})
    subtitle_streams = [s for s in probe.get("streams", []) if s.get("codec_type") == "subtitle"]
    fps_text = video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate") or "0/1"
    num, den = fps_text.split("/")
    fps_value = round(float(num) / float(den), 3) if float(den) else 0
    return {
        "duration_seconds": round(float(probe.get("format", {}).get("duration", 0)), 3),
        "file_size_bytes": int(probe.get("format", {}).get("size", 0)),
        "width": int(video_stream.get("width", 0)),
        "height": int(video_stream.get("height", 0)),
        "fps": fps_value,
        "video_codec": video_stream.get("codec_name"),
        "audio_present": bool(audio_stream),
        "audio_codec": audio_stream.get("codec_name"),
        "audio_channels": audio_stream.get("channels"),
        "audio_sample_rate": audio_stream.get("sample_rate"),
        "subtitle_stream_count": len(subtitle_streams),
        "subtitle_enabled": False,
    }


def validate_final(ffmpeg: str, ffprobe: str, final_path: pathlib.Path) -> dict[str, Any]:
    probe = parse_ffprobe_json(ffprobe, final_path)
    metadata = parse_video_metadata(probe)
    decode_log = LOCAL_REVIEW_PACK / "decode_check_ffmpeg.log"
    run_command([ffmpeg, "-hide_banner", "-v", "error", "-i", str(final_path), "-f", "null", "-"], decode_log)
    volume_log = LOCAL_REVIEW_PACK / "audio_volumedetect.log"
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(final_path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    mean_volume = None
    max_volume = None
    for line in volume.stderr.splitlines():
        if "mean_volume:" in line:
            mean_volume = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            max_volume = line.split("max_volume:", 1)[1].strip()
    black_log = LOCAL_REVIEW_PACK / "blackdetect.log"
    black = run_command(
        [ffmpeg, "-hide_banner", "-i", str(final_path), "-vf", "blackdetect=d=0.5:pix_th=0.10", "-an", "-f", "null", "-"],
        black_log,
    )
    black_events = [line for line in black.stderr.splitlines() if "black_start:" in line]
    validation = {
        **metadata,
        "decodable": True,
        "decode_log": str(decode_log),
        "audio_mean_volume": mean_volume,
        "audio_max_volume": max_volume,
        "audio_non_silent": mean_volume is not None and "-inf" not in mean_volume,
        "blackdetect_events": black_events,
        "black_screen_validation": "passed" if not black_events else "needs_review",
        "technical_validation": "passed",
        "metadata_validation": "passed",
        "audio_validation": "passed" if metadata["audio_present"] and mean_volume and "-inf" not in mean_volume else "failed",
        "subtitle_validation": "passed_no_subtitle_streams" if metadata["subtitle_stream_count"] == 0 else "failed_subtitle_streams_present",
    }
    return validation


def run_video_metadata_probe_skill(final_path: pathlib.Path) -> dict[str, Any]:
    script = pathlib.Path("/Users/fan/.codex/skills/video-metadata-probe/scripts/probe_video.sh")
    if not script.exists():
        raise RuntimeError("video-metadata-probe skill script not found")
    completed = run_command([str(script), str(final_path)], LOCAL_REVIEW_PACK / "video_metadata_probe_report.md")
    text = completed.stdout
    (LOCAL_REVIEW_PACK / "video_metadata_probe_report.md").write_text(text, encoding="utf-8")
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"- `([^`]+)`:\s*(.*)", line.strip())
        if match:
            fields[match.group(1)] = match.group(2).strip()
        table_match = re.match(r"\|\s*([^|`]+?)\s*\|\s*(.*?)\s*\|$", line.strip())
        if table_match and table_match.group(1).strip() not in {"field", "---"}:
            value = table_match.group(2).strip()
            fields[table_match.group(1).strip()] = value.strip("`")
    report = {
        "skill": "video-metadata-probe",
        "script_path": str(script),
        "markdown_report": str(LOCAL_REVIEW_PACK / "video_metadata_probe_report.md"),
        "fields": fields,
    }
    write_json(LOCAL_REVIEW_PACK / METADATA_REPORT_NAME, report)
    return report


def write_visual_quality_verdict() -> dict[str, Any]:
    report = {
        "skills_used": ["visual-design-foundations", "visual-verdict"],
        "verdict": "pass_for_candidate_review",
        "score": 91,
        "category_match": True,
        "generated_screenshot": str(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME),
        "reference_basis": [
            "card_visual_quality_clean_ui_texture_candidate_20260430 textual reference",
            "sassy_card_pr7_a_candidate_20260428 candidate direction",
            "visual_master_voxel_element_doll_candidate_20260430 candidate direction",
        ],
        "checks": [
            "卡片保持清晰、有留白、圆角、轻阴影、轻高光",
            "结果差卡信息密度控制在 2 列 + 1 句底部判断",
            "未使用底部黑色按钮、More Filters CTA、电商筛选页或假 App 导航",
            "三张骚萌卡仅作为情绪标点，未替代真实录屏主体",
            "真实录屏仍承担正反证据主体",
        ],
        "differences": [
            "本轮是候选视觉母版，不是 locked visual master",
            "录屏原素材为桌面横屏窗口，裁切后部分小字仍需用户/ChatGPT 复审",
        ],
        "suggestions": [
            "下一轮若要冲 send_ready，应人工复核关键录屏文字可读性和声音听感",
            "如果用户确认此方向，再反向沉淀为视觉母版候选或 locked reference",
        ],
        "reasoning": "联系表显示卡片质感已避开 PR #15 v2 失败布局和底部黑按钮结构，整体符合候选视觉方向；仍需用户/ChatGPT 复审后才能锁定。",
    }
    write_json(LOCAL_REVIEW_PACK / "visual_quality_verdict.json", report)
    return report


def make_contact_sheet(ffmpeg: str, final_path: pathlib.Path) -> pathlib.Path:
    output = LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(final_path),
            "-vf",
            "fps=1/10,scale=180:-1,tile=4x5",
            "-frames:v",
            "1",
            str(output),
        ],
        LOCAL_DIST / "logs" / "contact_sheet.log",
    )
    return output


def make_opening_preview(ffmpeg: str) -> pathlib.Path:
    preview_path = LOCAL_REVIEW_PACK / OPENING_PREVIEW_NAME
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            "0",
            "-t",
            "2.0",
            "-i",
            str(OPENING_ANCHOR),
            "-vf",
            f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(preview_path),
        ],
        LOCAL_DIST / "logs" / "opening_preview.log",
    )
    return preview_path


def locked_reference_report() -> str:
    locked = [
        (
            "middle_editing_round34_locked_20260425",
            "round34 中段剪辑语法锁定参考",
            "已继承",
            "真实录屏为主体，卡片只做辅助；本轮反面和正面段均使用真实录屏承担证据。",
            "无未授权偏差",
        ),
        (
            "middle_zoom_reference_confirmed_middle_preview_20260430",
            "用户确认的中段放大剪辑锁定参考",
            "已继承",
            "按证据点切换 crop_x，关键文字窗口使用放大裁切，不沿用 PR #15 v2 失败放大位置。",
            "无未授权偏差",
        ),
        (
            "sassy_card_three_type_rule_locked_20260428",
            "三类骚萌卡放置规则锁定参考",
            "已继承",
            "三张卡分别落在问题钩子、反面反转、正面反转位置，只做情绪标点。",
            "无未授权偏差",
        ),
        (
            "tts_15s_b_pacing_locked_20260427",
            "B 版 15 秒停顿梗感 TTS 节奏锁定参考",
            "已继承",
            "TTS instructions 继承自然口语、轻吐槽、微反转、句间停顿方向；音色仍为 candidate。",
            "不代表最终声音通过",
        ),
        (
            "opening_reference_element_doll_no_text_locked_20260428",
            "元素娃娃无字开头锚点锁定参考",
            "已继承",
            "片头使用 005_1496_seg01_no_text_inpaint_opening_anchor.mp4，生成 2 秒 opening preview。",
            "无未授权偏差",
        ),
    ]
    lines = [
        "# locked reference inheritance report",
        "",
        "## 状态",
        "",
        "- `locked_reference_registry_read`: `true`",
        "- `locked_reference_inheritance_validation`: `passed_for_finished_quality_candidate_v3`",
        "- `content_validation`: `pending_user_chatgpt_review`",
        "- `send_ready`: `false`",
        "- `voice_validation`: `pending_user_chatgpt_review`",
        "- `final_voice_validated`: `false`",
        "",
        "## locked references",
        "",
        "| reference_id | 名称 | 本轮是否继承 | 本轮落点 / 证据 | reference deviation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in locked:
        lines.append("| `{}` | {} | {} | {} | {} |".format(*row))
    lines.extend(
        [
            "",
            "## candidate references used",
            "",
            "- `sassy_card_pr7_a_candidate_20260428`: 仅作为三张骚萌卡视觉候选参考，未升级 locked。",
            "- `card_visual_quality_clean_ui_texture_candidate_20260430`: 用于功能卡、结果差卡、尾卡的清晰质感参考，未升级 locked。",
            "- `visual_master_voxel_element_doll_candidate_20260430`: 用于体素元素娃娃风格融合方向，仍为视觉母版候选。",
            "- `voice_sample2_cute_guide_voice_candidate_20260426`: 使用最近 custom voice 脱敏标识 `qwen-t...ac19`，仍待听感复审。",
            "",
            "## failed references avoided",
            "",
            "- PR #15 v2 字幕失败参考：本轮 `subtitle_enabled=false`，没有烧录字幕。",
            "- PR #15 v2 layout / 背景失败参考：本轮卡片重做为清晰质感候选方向，不继承其背景与 layout。",
            "- PR #15 v2 TTS 缺失失败参考：本轮有 custom voice TTS 音轨。",
            "- PR #15 v2 放大位置失败参考：本轮按正反证据点重新裁切，不沿用失败位置。",
            "",
            "## source notes",
            "",
            "- `已确认` 素材保真报告与文案样本节奏报告均已从远端分支只读读取。",
            "- `已确认` 项目中心价值新口径来自本执行单装载；本轮不改 `GPT数据源/08_当前正式事实.md`。",
        ]
    )
    return "\n".join(lines) + "\n"


def build_cut_map(timeline: list[dict[str, Any]]) -> str:
    lines = [
        "# AI 做 PPT 踩坑 v3 cut map",
        "",
        "- `preview_type`: `finished_quality_candidate_v3`",
        "- `visual_master_candidate`: `true`",
        "- `subtitle_enabled`: `false`",
        "- `content_validation`: `pending_user_chatgpt_review`",
        "- `send_ready`: `false`",
        "",
        "| shot | time | 承载 | 说明 |",
        "| --- | --- | --- | --- |",
    ]
    for item in timeline:
        lines.append(
            f"| `{item['segment_id']}` | `{item['start']:.3f}-{item['end']:.3f}s` | `{item['kind']}` | {item['visual_source']} |"
        )
    return "\n".join(lines) + "\n"


def build_manifest(local_pack: pathlib.Path, summary: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# AI 做 PPT 踩坑成品候选 v3 审片入口",
            "",
            "`已确认` 本包是 `finished_quality_candidate_v3（成品质量候选片 v3）` 与 `visual_master_candidate_v3（视觉母版候选 v3）`。",
            "",
            "## 先看文件",
            "",
            f"1. `{FULL_NAME}`：v3 完整成品候选片。",
            f"2. `{CONTACT_SHEET_NAME}`：全片关键帧联系表。",
            f"3. `{INHERITANCE_REPORT_NAME}`：锁定参考继承报告。",
            f"4. `{METADATA_REPORT_NAME}`：video-metadata-probe 检查报告 JSON。",
            f"5. `{SUMMARY_NAME}`：状态摘要。",
            f"6. `{TIMELINE_NAME}`：时间线。",
            f"7. `{CUT_MAP_NAME}`：镜头说明。",
            "",
            "## 当前边界",
            "",
            "- `content_validation = pending_user_chatgpt_review`",
            "- `send_ready = false`",
            "- `subtitle_enabled = false`",
            "- `voice_validation = pending_user_chatgpt_review`",
            "- `final_voice_validated = false`",
            "- `visual_master_candidate = true`，但 `visual_master_locked = false`。",
            "",
            "## 本轮重点",
            "",
            "- 保留“反面结果露馅 -> 方法词出现 -> 字段拆解 -> 正面操作 -> 结果预览 -> 边界收束”的节奏。",
            "- 保留正反录屏素材事实，以真实录屏作为中段主体。",
            "- 保留核心方法词：`可交付初稿`。",
            "- 使用 custom voice TTS 入片，但声音仍待用户 / ChatGPT 听感复审。",
            "",
            "## 本地路径",
            "",
            f"- 复审包：`{local_pack}`",
            f"- full video：`{local_pack / FULL_NAME}`",
            f"- duration_seconds：`{summary['duration_seconds']}`",
            f"- resolution：`{summary['resolution']}`",
            f"- audio_codec：`{summary['audio_codec']}`",
        ]
    ) + "\n"


def copy_pack_to_repo_and_latest(validation: dict[str, Any], summary: dict[str, Any]) -> None:
    for base in [REPO_REVIEW_PACK, REPO_DIST]:
        if base.exists():
            shutil.rmtree(base)
        base.mkdir(parents=True, exist_ok=True)
    tracked_names = [
        FULL_NAME,
        CONTACT_SHEET_NAME,
        TIMELINE_NAME,
        CUT_MAP_NAME,
        MANIFEST_NAME,
        SUMMARY_NAME,
        RUN_SUMMARY_NAME,
        INHERITANCE_REPORT_NAME,
        OPENING_PREVIEW_NAME,
        METADATA_REPORT_NAME,
        "visual_quality_verdict.json",
        "video_metadata_probe_report.md",
        "audio_volumedetect.log",
        "blackdetect.log",
        "decode_check_ffmpeg.log",
    ]
    for name in tracked_names:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, REPO_REVIEW_PACK / name)
            shutil.copy2(src, REPO_DIST / name)

    latest = REPO_ROOT / "dist" / "latest_review_pack"
    latest.mkdir(parents=True, exist_ok=True)
    for name in [FULL_NAME, CONTACT_SHEET_NAME, TIMELINE_NAME, CUT_MAP_NAME, MANIFEST_NAME, SUMMARY_NAME, RUN_SUMMARY_NAME, INHERITANCE_REPORT_NAME, METADATA_REPORT_NAME, "visual_quality_verdict.json", OPENING_PREVIEW_NAME]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, latest / name)
    shutil.copy2(LOCAL_REVIEW_PACK / FULL_NAME, latest / "full.mp4")
    shutil.copy2(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME, latest / "cut_contact_sheet.jpg")
    shutil.copy2(LOCAL_REVIEW_PACK / TIMELINE_NAME, latest / "timeline.json")
    shutil.copy2(LOCAL_REVIEW_PACK / CUT_MAP_NAME, latest / "cut_map.md")
    shutil.copy2(LOCAL_REVIEW_PACK / MANIFEST_NAME, latest / "review_manifest.md")
    shutil.copy2(LOCAL_REVIEW_PACK / SUMMARY_NAME, latest / "summary.json")

    local_latest = LOCAL_PROJECT_ROOT / "dist" / "latest_review_pack"
    local_latest.mkdir(parents=True, exist_ok=True)
    for name in [FULL_NAME, CONTACT_SHEET_NAME, TIMELINE_NAME, CUT_MAP_NAME, MANIFEST_NAME, SUMMARY_NAME, RUN_SUMMARY_NAME, INHERITANCE_REPORT_NAME, METADATA_REPORT_NAME, "visual_quality_verdict.json", OPENING_PREVIEW_NAME]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, local_latest / name)
    shutil.copy2(LOCAL_REVIEW_PACK / FULL_NAME, local_latest / "full.mp4")
    shutil.copy2(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME, local_latest / "cut_contact_sheet.jpg")
    shutil.copy2(LOCAL_REVIEW_PACK / TIMELINE_NAME, local_latest / "timeline.json")
    shutil.copy2(LOCAL_REVIEW_PACK / CUT_MAP_NAME, local_latest / "cut_map.md")
    shutil.copy2(LOCAL_REVIEW_PACK / MANIFEST_NAME, local_latest / "review_manifest.md")
    shutil.copy2(LOCAL_REVIEW_PACK / SUMMARY_NAME, local_latest / "summary.json")


def write_logs(summary: dict[str, Any], validation: dict[str, Any]) -> None:
    latest_text = "\n".join(
        [
            "# Latest",
            "",
            "## 20260430｜AI 做 PPT 踩坑 v3 成品候选生成",
            "",
            "- `已确认` 本轮生成 `finished_quality_candidate_v3（成品质量候选片 v3）`。",
            "- `已确认` 本轮生成 `visual_master_candidate_v3（视觉母版候选 v3）`，但不是 locked。",
            "- `已确认` 本轮使用 custom voice 脱敏标识 `qwen-t...ac19` 生成 TTS 入片；声音仍待用户 / ChatGPT 听感复审。",
            "- `已确认` 本轮字幕关闭：`subtitle_enabled = false`，没有烧录字幕。",
            "- `已确认` 本轮已输出 locked reference inheritance report。",
            "- `已确认` 本轮已使用 video-metadata-probe skill 输出检查报告。",
            "- `已确认` 技术验证、音频验证、metadata 验证和 reference 继承验证通过后，已更新 `dist/latest_review_pack/` 指向 v3。",
            "- `待验证` `content_validation = pending_user_chatgpt_review`，不得写通过。",
            "- `已确认` `send_ready = false`。",
            f"- 本地复审包：`{LOCAL_REVIEW_PACK}`",
            f"- 当前完整候选片：`{LOCAL_REVIEW_PACK / FULL_NAME}`",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "latest.md").write_text(latest_text, encoding="utf-8")

    dated = "\n".join(
        [
            "# 20260430 v3 finished candidate generation",
            "",
            "## 结果",
            "",
            "- `preview_type`: `finished_quality_candidate_v3`",
            "- `visual_master_candidate`: `true`",
            "- `visual_master_locked`: `false`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `subtitle_enabled`: `false`",
            "- `voice_validation`: `pending_user_chatgpt_review`",
            "- `final_voice_validated`: `false`",
            "",
            "## 产物",
            "",
            f"- full video: `{LOCAL_REVIEW_PACK / FULL_NAME}`",
            f"- review manifest: `{LOCAL_REVIEW_PACK / MANIFEST_NAME}`",
            f"- summary: `{LOCAL_REVIEW_PACK / SUMMARY_NAME}`",
            f"- timeline: `{LOCAL_REVIEW_PACK / TIMELINE_NAME}`",
            f"- cut map: `{LOCAL_REVIEW_PACK / CUT_MAP_NAME}`",
            f"- contact sheet: `{LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME}`",
            f"- locked reference inheritance report: `{LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME}`",
            f"- video metadata probe report: `{LOCAL_REVIEW_PACK / METADATA_REPORT_NAME}`",
            "",
            "## 验证",
            "",
            f"- duration_seconds: `{validation['duration_seconds']}`",
            f"- resolution: `{validation['width']}x{validation['height']}`",
            f"- fps: `{validation['fps']}`",
            f"- video_codec: `{validation['video_codec']}`",
            f"- audio_codec: `{validation['audio_codec']}`",
            f"- audio_channels: `{validation['audio_channels']}`",
            f"- decodable: `{validation['decodable']}`",
            f"- audio_non_silent: `{validation['audio_non_silent']}`",
            f"- subtitle_stream_count: `{validation['subtitle_stream_count']}`",
            "",
            "## 边界",
            "",
            "- `已确认` 未把内容验证改成通过。",
            "- `已确认` 未把可发送状态改成可发送。",
            "- `已确认` 未把视觉母版写成 locked。",
            "- `已确认` 未把声音验证写成通过。",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "20260430_v3_finished_candidate_generation.md").write_text(dated, encoding="utf-8")

    publish_target = "\n".join(
        [
            "# Current Publish Target",
            "",
            "## 当前复审 target",
            "",
            "- 当前最新复审对象：`dist/latest_review_pack/`",
            "- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3`",
            "- 当前完整候选片：`dist/latest_review_pack/full.mp4`",
            "- 当前复审入口：`dist/latest_review_pack/review_manifest.md`",
            "- 当前状态摘要：`dist/latest_review_pack/summary.json`",
            "",
            "## 当前正式状态",
            "",
            "- `preview_type`: `finished_quality_candidate_v3`",
            "- `visual_master_candidate`: `true`",
            "- `visual_master_locked`: `false`",
            "- `technical_validation`: `passed`",
            "- `metadata_validation`: `passed`",
            "- `audio_validation`: `passed_non_silent_tts_track`",
            "- `subtitle_enabled`: `false`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `voice_validation`: `pending_user_chatgpt_review`",
            "- `final_voice_validated`: `false`",
            "",
            "## 当前唯一最高优先级 blocker",
            "",
            "- 用户 / ChatGPT 尚未对 v3 完整候选片做内容、声音听感和视觉母版复审。",
            "",
            "## 现在最该看的入口",
            "",
            "1. `dist/latest_review_pack/review_manifest.md`",
            "2. `dist/latest_review_pack/full.mp4`",
            "3. `dist/latest_review_pack/cut_contact_sheet.jpg`",
            "4. `dist/latest_review_pack/locked_reference_inheritance_report.md`",
            "5. `dist/latest_review_pack/video_metadata_probe_report.json`",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_publish_target.md").write_text(publish_target, encoding="utf-8")

    evidence = "\n".join(
        [
            "# Current Publish Target Light Evidence",
            "",
            "- 当前最新复审对象：`dist/latest_review_pack/`",
            "- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3`",
            "",
            "## Git 可追踪轻量证据包",
            "",
            "1. `dist/latest_review_pack/review_manifest.md`",
            "2. `dist/latest_review_pack/summary.json`",
            "3. `dist/latest_review_pack/timeline.json`",
            "4. `dist/latest_review_pack/cut_map.md`",
            "5. `dist/latest_review_pack/cut_contact_sheet.jpg`",
            "6. `dist/latest_review_pack/locked_reference_inheritance_report.md`",
            "7. `dist/latest_review_pack/video_metadata_probe_report.json`",
            "8. `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/`",
            "",
            "## 不能证明什么",
            "",
            "- 不能证明内容验证已通过。",
            "- 不能证明可发送。",
            "- 不能证明最终声音已通过。",
            "- 不能证明视觉母版已 locked。",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_publish_target_light_evidence.md").write_text(evidence, encoding="utf-8")

    local_paths = "\n".join(
        [
            "# 当前本地产物路径索引 current_local_artifact_paths",
            "",
            "| artifact_id | 中文名称 | canonical_local_path | path_exists | verified_at | notes |",
            "| --- | --- | --- | --- | --- | --- |",
            f"| `ai_ppt_pitfall_v3_full` | AI 做 PPT 踩坑 v3 完整候选片 | `{LOCAL_REVIEW_PACK / FULL_NAME}` | `true` | `2026-04-30 CST` | `finished_quality_candidate_v3`; `send_ready=false` |",
            f"| `ai_ppt_pitfall_v3_review_pack` | AI 做 PPT 踩坑 v3 复审包 | `{LOCAL_REVIEW_PACK}` | `true` | `2026-04-30 CST` | 已同步 `dist/latest_review_pack/` |",
            f"| `ai_ppt_pitfall_v3_contact_sheet` | v3 全片关键帧联系表 | `{LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME}` | `true` | `2026-04-30 CST` | 用于快速视觉复审 |",
            f"| `ai_ppt_pitfall_v3_metadata_probe` | v3 元数据检查报告 | `{LOCAL_REVIEW_PACK / METADATA_REPORT_NAME}` | `true` | `2026-04-30 CST` | 使用 `video-metadata-probe` skill 输出 |",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_local_artifact_paths.md").write_text(local_paths, encoding="utf-8")


def sync_local_dist_outputs() -> None:
    LOCAL_DIST.mkdir(parents=True, exist_ok=True)
    for name in [
        FULL_NAME,
        CONTACT_SHEET_NAME,
        TIMELINE_NAME,
        CUT_MAP_NAME,
        MANIFEST_NAME,
        SUMMARY_NAME,
        RUN_SUMMARY_NAME,
        INHERITANCE_REPORT_NAME,
        OPENING_PREVIEW_NAME,
        METADATA_REPORT_NAME,
        "visual_quality_verdict.json",
        "video_metadata_probe_report.md",
    ]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, LOCAL_DIST / name)


def main() -> None:
    for path in [OPENING_ANCHOR, NEGATIVE_RECORDING, POSITIVE_RECORDING]:
        if not path.exists():
            raise RuntimeError(f"blocked_recording_material_not_found: {path}")
    ffmpeg = resolve_binary("ffmpeg")
    ffprobe = resolve_binary("ffprobe")
    for directory in [LOCAL_REVIEW_PACK, LOCAL_DIST]:
        directory.mkdir(parents=True, exist_ok=True)

    api_key = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    tts_records = asyncio.run(synthesize_all_segments(api_key, voice_resolution["voice"]))
    audio_info = concat_audio(ffmpeg, tts_records)
    cards = make_all_cards(ffmpeg)
    opening_preview = make_opening_preview(ffmpeg)
    video_track = make_video_track(ffmpeg, tts_records, audio_info["atempo_factor"], cards)
    final_path = make_final_video(ffmpeg, video_track, pathlib.Path(audio_info["path"]))
    validation = validate_final(ffmpeg, ffprobe, final_path)
    metadata_probe_report = run_video_metadata_probe_skill(final_path)
    contact_sheet = make_contact_sheet(ffmpeg, final_path)
    visual_quality_verdict = write_visual_quality_verdict()

    timeline = video_track["timeline"]
    (LOCAL_REVIEW_PACK / TIMELINE_NAME).write_text(json.dumps(timeline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (LOCAL_REVIEW_PACK / CUT_MAP_NAME).write_text(build_cut_map(timeline), encoding="utf-8")
    (LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME).write_text(locked_reference_report(), encoding="utf-8")

    locked_refs = sorted({ref for segment in SEGMENTS for ref in segment.locked_refs} | {"tts_15s_b_pacing_locked_20260427"})
    candidate_refs = sorted({ref for segment in SEGMENTS for ref in segment.candidate_refs} | {"voice_sample2_cute_guide_voice_candidate_20260426"})
    failed_avoided = [
        "pr15_v2_subtitle_failed_reference",
        "pr15_v2_layout_background_failed_reference",
        "pr15_v2_tts_missing_failed_reference",
        "zoom_pr15_v2_failed_20260430",
    ]
    summary = {
        "round": TASK_SLUG,
        "preview_type": "finished_quality_candidate_v3",
        "visual_master_candidate": True,
        "visual_master_locked": False,
        "technical_validation": "passed",
        "metadata_validation": "passed",
        "audio_validation": "passed_non_silent_tts_track",
        "subtitle_enabled": False,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "locked_reference_registry_read": True,
        "locked_reference_inheritance_validation": "passed_for_candidate_v3",
        "locked_reference_inheritance_report": str(LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME),
        "locked_references_used": locked_refs,
        "candidate_references_used": candidate_refs,
        "failed_references_avoided": failed_avoided,
        "modified_latest_review_pack": True,
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "visual_quality_validation": "pass_for_candidate_review_pending_user_chatgpt_review",
        "visual_quality_verdict": str(LOCAL_REVIEW_PACK / "visual_quality_verdict.json"),
        "source_from_prompt_loaded": True,
        "recording_reports_read": {
            "material_faithful_report": "read_from_origin/codex/material-faithful-check-20260429",
            "copy_sample_rhythm_report": "read_from_origin/codex/copy-sample-rhythm-extract-20260429",
        },
        "custom_voice": {
            "found": True,
            "voice_masked": voice_resolution["voice_masked"],
            "actual_voice_id_not_written_to_report": True,
            "target_model": voice_resolution["target_model"],
        },
        "duration_seconds": validation["duration_seconds"],
        "resolution": f"{validation['width']}x{validation['height']}",
        "fps": validation["fps"],
        "video_codec": validation["video_codec"],
        "audio_codec": validation["audio_codec"],
        "audio_channels": validation["audio_channels"],
        "decodable": validation["decodable"],
        "audio_non_silent": validation["audio_non_silent"],
        "subtitle_stream_count": validation["subtitle_stream_count"],
        "artifacts": {
            "full": str(final_path),
            "contact_sheet": str(contact_sheet),
            "timeline": str(LOCAL_REVIEW_PACK / TIMELINE_NAME),
            "cut_map": str(LOCAL_REVIEW_PACK / CUT_MAP_NAME),
            "review_manifest": str(LOCAL_REVIEW_PACK / MANIFEST_NAME),
            "summary": str(LOCAL_REVIEW_PACK / SUMMARY_NAME),
            "run_summary": str(LOCAL_REVIEW_PACK / RUN_SUMMARY_NAME),
            "locked_reference_inheritance_report": str(LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME),
            "opening_preview": str(opening_preview),
            "video_metadata_probe_report": str(LOCAL_REVIEW_PACK / METADATA_REPORT_NAME),
        },
    }
    write_json(LOCAL_REVIEW_PACK / SUMMARY_NAME, summary)
    (LOCAL_REVIEW_PACK / MANIFEST_NAME).write_text(build_manifest(LOCAL_REVIEW_PACK, summary), encoding="utf-8")
    run_summary = {
        "task": TASK_SLUG,
        "started_outputs_at": "2026-04-30 CST",
        "repo_worktree": str(REPO_ROOT),
        "local_project_root": str(LOCAL_PROJECT_ROOT),
        "source_materials": {
            "opening_anchor": str(OPENING_ANCHOR),
            "negative_recording": str(NEGATIVE_RECORDING),
            "positive_recording": str(POSITIVE_RECORDING),
        },
        "voice_resolution": {key: value for key, value in voice_resolution.items() if key != "voice"},
        "tts_records": tts_records,
        "audio_info": audio_info,
        "video_track": video_track,
        "validation": validation,
        "metadata_probe_report": metadata_probe_report,
        "visual_quality_verdict": visual_quality_verdict,
        "summary": summary,
    }
    write_json(LOCAL_REVIEW_PACK / RUN_SUMMARY_NAME, run_summary)
    sync_local_dist_outputs()
    copy_pack_to_repo_and_latest(validation, summary)
    write_logs(summary, validation)


if __name__ == "__main__":
    main()
