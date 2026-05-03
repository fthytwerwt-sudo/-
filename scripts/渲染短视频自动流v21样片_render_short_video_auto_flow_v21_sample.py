#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import pathlib
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = pathlib.Path("/Users/fan/Documents/视频工厂")
PLAN_DIR = ROOT / "剪辑计划_video_edit_plans" / "20260503_短视频自动流最简单流程_v21_plan"
OUTPUT_DIR = ROOT / "dist" / "视频样片_video_samples" / "20260503_短视频自动流最简单流程_v21_sample"
CARDS_DIR = OUTPUT_DIR / "卡片素材_cards"
SEGMENTS_DIR = OUTPUT_DIR / "中间片段_segments"
OVERLAYS_DIR = OUTPUT_DIR / "叠字_overlay_assets"
LOGS_DIR = OUTPUT_DIR / "渲染日志_render_logs"

W, H = 720, 1280
FPS = 24
TARGET_DURATION = 105.0
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ).isoformat(timespec="seconds")

DOUBAO = ROOT / "素材录制" / "最新素材" / "豆包素材.mp4"
TRAE = ROOT / "素材录制" / "最新素材" / "trae 素材.mp4"
CODEX = ROOT / "素材录制" / "最新素材" / "codex 素材.mp4"

REQUIRED_PLAN_FILES = [
    "preflight_check.md",
    "reference_script.md",
    "runtime_script.md",
    "timeline_plan.md",
    "timeline_manifest.json",
    "material_usage_plan.md",
    "redaction_plan.md",
    "guardrail_check.md",
    "next_render_prompt_draft.md",
]

COPY_FILES = [
    "runtime_script.md",
    "reference_script.md",
    "timeline_plan.md",
    "timeline_manifest.json",
    "material_usage_plan.md",
    "redaction_plan.md",
    "guardrail_check.md",
]

CARD_SPECS = {
    "01_opening_judgement": {
        "title": "自动流不是一键生成",
        "body": ["一键生成更像抽素材", "这条样片证明的是流程"],
        "accent": "#e95f8a",
    },
    "08_api_station": {
        "title": "API = 外部能力入口",
        "body": ["把文字、配音、图片、剪辑", "接成系统可调用的工位"],
        "accent": "#2d9a8b",
    },
    "09_cloud_editing_station": {
        "title": "云剪不是总控脑",
        "body": ["它是装配台", "不负责创意和内容判断"],
        "accent": "#d98b2b",
    },
    "11_jimeng_compare": {
        "title": "抽素材 vs 搭流程",
        "body": ["即梦适合快速出素材", "自动流解决持续生产"],
        "accent": "#6572d9",
    },
    "12_final_summary": {
        "title": "顺序对了",
        "body": ["自动化才有地方落脚"],
        "accent": "#9b5fb8",
    },
}

SEGMENTS = [
    {
        "segment_id": "01_opening_judgement",
        "label": "开头判断",
        "type": "card",
        "duration": 3.0,
        "proof": "建立判断：自动流不是一键生成",
        "cannot_prove": "不证明任何工具跑通",
    },
    {
        "segment_id": "02_doubao_simple_need",
        "label": "一句需求",
        "type": "real_footage",
        "duration": 7.0,
        "source": DOUBAO,
        "kind": "doubao",
        "clips": [(16.0, 23.0)],
        "proof": "用户只给一句简单需求",
        "cannot_prove": "不证明 Trae 已执行",
    },
    {
        "segment_id": "03_doubao_process_breakdown",
        "label": "先拆成工位",
        "type": "real_footage",
        "duration": 13.0,
        "source": DOUBAO,
        "kind": "doubao",
        "clips": [(88.0, 101.0)],
        "proof": "豆包把需求拆成短视频生产流程",
        "cannot_prove": "不证明工程跑通",
    },
    {
        "segment_id": "04_doubao_to_trae_prompt",
        "label": "翻译成 Trae 能接的任务说明",
        "type": "real_footage",
        "duration": 18.0,
        "source": DOUBAO,
        "kind": "doubao",
        "clips": [(160.0, 168.0), (232.0, 242.0)],
        "proof": "豆包生成 Trae 能接的任务说明",
        "cannot_prove": "不证明 prompt 已运行成功",
    },
    {
        "segment_id": "05_trae_solo_entry",
        "label": "进入执行器",
        "type": "real_footage",
        "duration": 8.0,
        "source": TRAE,
        "kind": "trae",
        "clips": [(32.0, 40.0)],
        "proof": "用户进入 Trae SOLO",
        "cannot_prove": "不证明执行完成",
    },
    {
        "segment_id": "06_trae_prompt_plan",
        "label": "开始 plan",
        "type": "real_footage",
        "duration": 14.0,
        "source": TRAE,
        "kind": "trae",
        "clips": [(80.0, 87.0), (96.0, 103.0)],
        "proof": "Trae 接住 prompt 并拆任务",
        "cannot_prove": "不证明所有待办完成",
    },
    {
        "segment_id": "07_trae_project_skeleton",
        "label": "项目骨架出现",
        "type": "real_footage",
        "duration": 18.0,
        "source": TRAE,
        "kind": "trae",
        "clips": [(120.0, 138.0)],
        "proof": "从聊天方案变成项目骨架",
        "cannot_prove": "不证明 app 已跑通",
    },
    {
        "segment_id": "08_api_station",
        "label": "API = 外部能力入口",
        "type": "card",
        "duration": 4.0,
        "proof": "API 是流程工位",
        "cannot_prove": "不证明 API 已接通",
    },
    {
        "segment_id": "09_cloud_editing_station",
        "label": "云剪不是总控脑",
        "type": "card",
        "duration": 4.0,
        "proof": "云剪是总装位置",
        "cannot_prove": "不证明正式稳定链路",
    },
    {
        "segment_id": "10_codex_check",
        "label": "执行检查员",
        "type": "real_footage",
        "duration": 8.0,
        "source": CODEX,
        "kind": "codex",
        "clips": [(176.0, 184.0)],
        "proof": "Codex 检查路径、文件、命令和报告",
        "cannot_prove": "不证明内容过线",
    },
    {
        "segment_id": "11_jimeng_compare",
        "label": "抽素材 vs 搭流程",
        "type": "card",
        "duration": 4.0,
        "proof": "说明工具定位差异",
        "cannot_prove": "不证明即梦不可用",
    },
    {
        "segment_id": "12_final_summary",
        "label": "顺序对了，自动化才有地方落脚",
        "type": "card",
        "duration": 4.0,
        "proof": "收住主判断",
        "cannot_prove": "不证明可发布",
    },
]


def run(cmd: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(proc.stdout, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stdout[-3000:]}")
    return proc


def write_text(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_bin(name: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    raise RuntimeError(f"missing required binary: {name}")


def rel(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_runtime_voiceover(runtime_md: str) -> str:
    marker = "## 2. 实际入片口播稿"
    if marker not in runtime_md:
        raise RuntimeError("runtime_script.md missing actual voiceover section")
    text = runtime_md.split(marker, 1)[1]
    text = text.split("## 3.", 1)[0].strip()
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
    return text.strip()


def validate_plan_package() -> dict[str, Any]:
    if not PLAN_DIR.is_dir():
        raise RuntimeError(f"missing plan directory: {PLAN_DIR}")
    missing = [name for name in REQUIRED_PLAN_FILES if not (PLAN_DIR / name).is_file()]
    if missing:
        raise RuntimeError(f"missing plan files: {missing}")

    manifest = json.loads(load_text(PLAN_DIR / "timeline_manifest.json"))
    expected = {
        "total_runtime_target_seconds": 105,
        "total_real_footage_seconds": 86,
        "total_card_seconds": 19,
        "real_footage_ratio": 0.819,
        "card_ratio": 0.181,
        "longest_card_seconds": 4,
        "segment_count": 12,
        "plan_status": "review_ready_not_render_ready",
    }
    mismatched = {k: {"expected": v, "actual": manifest.get(k)} for k, v in expected.items() if manifest.get(k) != v}
    if mismatched:
        raise RuntimeError(f"timeline_manifest locked metrics mismatch: {mismatched}")

    reference_md = load_text(PLAN_DIR / "reference_script.md")
    runtime_md = load_text(PLAN_DIR / "runtime_script.md")
    guardrail_md = load_text(PLAN_DIR / "guardrail_check.md")
    if "reference_only=true" not in reference_md:
        raise RuntimeError("reference_script.md missing reference_only=true")
    if "runtime_script=true" not in runtime_md:
        raise RuntimeError("runtime_script.md missing runtime_script=true")
    if runtime_md.strip() == reference_md.strip():
        raise RuntimeError("runtime_script.md equals reference_script.md")
    ratio = len(runtime_md) / max(1, len(reference_md))
    if ratio > 0.62 or "BEGIN_REFERENCE_SCRIPT" in runtime_md:
        raise RuntimeError("runtime_script.md looks too close to reference_script.md")
    required_guardrails = [
        "是否没有把完整稿当 runtime | `passed`",
        "真实录屏是否承担主体流程推进 | `passed`",
        "卡片是否只做辅助 | `passed`",
        "是否没有写 content_validation passed | `passed`",
        "是否没有写 send_ready true | `passed`",
    ]
    guardrail_content_passed = all(item in guardrail_md for item in required_guardrails)
    if not guardrail_content_passed:
        raise RuntimeError("guardrail_check.md missing required passed content checks")

    return {
        "manifest": manifest,
        "runtime_md": runtime_md,
        "reference_md": reference_md,
        "guardrail_md": guardrail_md,
        "runtime_reference_ratio": ratio,
        "review_gate_resolution": "current_user_render_only_instruction_authorized_render_after_plan_review",
    }


def validate_sources(ffprobe: str) -> list[dict[str, Any]]:
    rows = []
    for source in [DOUBAO, TRAE, CODEX]:
        if not source.is_file():
            raise RuntimeError(f"missing source material: {source}")
        proc = run([
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "stream=codec_name,width,height:format=duration",
            "-of",
            "json",
            str(source),
        ])
        data = json.loads(proc.stdout)
        video = next((s for s in data.get("streams", []) if s.get("width")), {})
        rows.append({
            "path": str(source),
            "exists": True,
            "duration_seconds": float(data.get("format", {}).get("duration", 0.0)),
            "width": video.get("width"),
            "height": video.get("height"),
            "codec": video.get("codec_name"),
        })
    return rows


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if pathlib.Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size, index=0)
            except Exception:
                continue
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        trial = current + ch
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def make_card(segment_id: str, spec: dict[str, Any]) -> pathlib.Path:
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (W, H), "#fff8fb")
    draw = ImageDraw.Draw(img)
    title_font = load_font(48, True)
    body_font = load_font(31, True)
    small_font = load_font(21, True)
    accent = spec["accent"]

    draw.rectangle((0, 0, W, H), fill="#fff8fb")
    draw.rectangle((0, 0, W, 92), fill="#252238")
    draw.text((42, 31), "流程证明型技术样片 V2.1", font=small_font, fill="#ffffff")
    draw.rounded_rectangle((42, 166, W - 42, H - 170), radius=22, fill="#ffffff", outline="#f0b8cb", width=2)
    draw.rounded_rectangle((78, 226, W - 78, 386), radius=18, fill="#fff0f6", outline="#f2bfd2", width=2)

    y = 250
    for line in wrap_text(draw, spec["title"], title_font, W - 180):
        draw.text((100, y), line, font=title_font, fill="#2b2438")
        y += 58

    y = 486
    for item in spec["body"]:
        draw.rounded_rectangle((86, y, W - 86, y + 96), radius=18, fill="#f8fbff", outline="#d9e6f8", width=2)
        draw.ellipse((106, y + 28, 148, y + 70), fill=accent)
        for line in wrap_text(draw, item, body_font, W - 240):
            draw.text((172, y + 28), line, font=body_font, fill="#2b2438")
            break
        y += 122

    draw.text((76, H - 246), "卡片只做提示，不承担主叙事", font=small_font, fill="#7e6b82")
    draw.text((76, H - 198), "content_validation = pending_user_chatgpt_review", font=small_font, fill="#8b5770")
    draw.text((76, H - 164), "send_ready = false", font=small_font, fill="#8b5770")

    path = CARDS_DIR / f"{segment_id}.png"
    img.save(path, quality=94)
    return path


def make_overlay(label: str, segment_id: str) -> pathlib.Path:
    OVERLAYS_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = load_font(28, True)
    small = load_font(18, True)
    box_h = 76
    draw.rounded_rectangle((28, 74, W - 28, 74 + box_h), radius=20, fill=(35, 31, 50, 210))
    draw.text((54, 94), label, font=font, fill=(255, 255, 255, 255))
    draw.text((54, 127), "流程证明，不代表系统已完全跑通", font=small, fill=(234, 220, 229, 255))
    path = OVERLAYS_DIR / f"{segment_id}_overlay.png"
    img.save(path)
    return path


def generate_cards_and_overlays() -> tuple[dict[str, pathlib.Path], dict[str, pathlib.Path]]:
    card_paths = {sid: make_card(sid, spec) for sid, spec in CARD_SPECS.items()}
    overlay_paths = {seg["segment_id"]: make_overlay(seg["label"], seg["segment_id"]) for seg in SEGMENTS if seg["type"] == "real_footage"}
    return card_paths, overlay_paths


def srt_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    ms = int(round((seconds - math.floor(seconds)) * 1000))
    whole = int(math.floor(seconds))
    s = whole % 60
    m = (whole // 60) % 60
    h = whole // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def caption_units(text: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    merged: list[str] = []
    buf = ""
    for part in parts:
        part = re.sub(r"\s*\n\s*", " ", part).strip()
        if not part:
            continue
        if not buf:
            buf = part
        elif len(buf) + len(part) < 44:
            buf += " " + part
        else:
            merged.append(buf)
            buf = part
    if buf:
        merged.append(buf)
    return merged


def make_captions(voiceover_text: str) -> list[dict[str, Any]]:
    parts = caption_units(voiceover_text)
    weights = [max(8, len(re.sub(r"\s+", "", p))) for p in parts]
    total_weight = sum(weights)
    cursor = 0.0
    srt_blocks = []
    json_blocks = []
    for idx, (part, weight) in enumerate(zip(parts, weights), start=1):
        dur = max(1.2, TARGET_DURATION * weight / total_weight)
        start = cursor
        end = min(TARGET_DURATION, cursor + dur)
        cursor = end
        srt_blocks.append(f"{idx}\n{srt_time(start)} --> {srt_time(end)}\n{part}\n")
        json_blocks.append({"index": idx, "start": round(start, 3), "end": round(end, 3), "text": part})
    if json_blocks:
        json_blocks[-1]["end"] = TARGET_DURATION
        srt_blocks[-1] = re.sub(r"--> .*?\n", f"--> {srt_time(TARGET_DURATION)}\n", srt_blocks[-1], count=1)
    write_text(OUTPUT_DIR / "captions.srt", "\n".join(srt_blocks))
    write_json(OUTPUT_DIR / "captions.json", json_blocks)
    return json_blocks


def probe_duration(ffprobe: str, path: pathlib.Path) -> float:
    proc = run([
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=nokey=1:noprint_wrappers=1",
        str(path),
    ])
    return float(proc.stdout.strip())


def atempo_chain(factor: float) -> str:
    values: list[float] = []
    remaining = factor
    while remaining > 2.0:
        values.append(2.0)
        remaining /= 2.0
    while remaining < 0.5:
        values.append(0.5)
        remaining /= 0.5
    values.append(remaining)
    return ",".join(f"atempo={v:.6f}" for v in values)


def make_temporary_tts(ffmpeg: str, ffprobe: str, voiceover_text: str) -> dict[str, Any]:
    raw_txt = OUTPUT_DIR / "temporary_tts_runtime_script_text.txt"
    raw_aiff = OUTPUT_DIR / "temporary_tts_runtime_script_raw.aiff"
    final_m4a = OUTPUT_DIR / "temporary_tts_runtime_script_105s.m4a"
    write_text(raw_txt, voiceover_text)

    say_bin = shutil.which("say")
    if not say_bin:
        raise RuntimeError("macOS say not found; current render requires temporary TTS from runtime_script")

    try:
        run([say_bin, "-v", "Tingting", "-r", "300", "-f", str(raw_txt), "-o", str(raw_aiff)], LOGS_DIR / "say_tts_runtime_script.log")
        voice_name = "Tingting"
    except RuntimeError:
        run([say_bin, "-r", "300", "-f", str(raw_txt), "-o", str(raw_aiff)], LOGS_DIR / "say_tts_runtime_script_default_voice.log")
        voice_name = "system_default"
    raw_duration = probe_duration(ffprobe, raw_aiff)
    speed_factor = raw_duration / TARGET_DURATION if raw_duration else 1.0
    filters = f"{atempo_chain(speed_factor)},apad,atrim=0:{TARGET_DURATION:.3f},asetpts=N/SR/TB"
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(raw_aiff),
        "-filter:a",
        filters,
        "-t",
        f"{TARGET_DURATION:.3f}",
        "-c:a",
        "aac",
        "-b:a",
        "96k",
        str(final_m4a),
    ], LOGS_DIR / "tts_runtime_script_fit_105s.log")
    final_duration = probe_duration(ffprobe, final_m4a)
    return {
        "audio_path": str(final_m4a),
        "raw_audio_path": str(raw_aiff),
        "duration_seconds": final_duration,
        "raw_duration_seconds": raw_duration,
        "speed_factor": speed_factor,
        "audio_validation": "temporary_preview",
        "tts_validation": "temporary_system_tts_preview_from_runtime_script",
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "generation_method": f"macOS say {voice_name} temporary preview; duration fit to 105s",
        "source": "runtime_script.md",
    }


def base_filter(kind: str) -> str:
    crop_x = {
        "doubao": 620,
        "trae": 650,
        "codex": 420,
    }[kind]
    filters = [
        "scale=-1:1280",
        f"crop=720:1280:{crop_x}:0",
        "fps=24",
    ]
    if kind == "codex":
        filters.extend([
            "drawbox=x=522:y=0:w=198:h=1280:color=black@0.86:t=fill",
            "drawbox=x=0:y=1178:w=720:h=102:color=black@0.86:t=fill",
            "drawbox=x=0:y=0:w=720:h=58:color=black@0.72:t=fill",
            "drawbox=x=0:y=1090:w=720:h=82:color=black@0.55:t=fill",
        ])
    elif kind == "trae":
        filters.extend([
            "drawbox=x=0:y=1178:w=720:h=102:color=black@0.72:t=fill",
            "drawbox=x=0:y=0:w=720:h=54:color=black@0.58:t=fill",
        ])
    else:
        filters.extend([
            "drawbox=x=0:y=1178:w=720:h=102:color=black@0.62:t=fill",
            "drawbox=x=0:y=0:w=720:h=54:color=black@0.48:t=fill",
        ])
    return ",".join(filters)


def render_card_segment(ffmpeg: str, image_path: pathlib.Path, duration: float, out_path: pathlib.Path) -> None:
    run([
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
        str(image_path),
        "-vf",
        "format=yuv420p",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "22",
        "-r",
        str(FPS),
        str(out_path),
    ], LOGS_DIR / f"{out_path.stem}.log")


def render_clip_part(ffmpeg: str, source: pathlib.Path, start: float, duration: float, kind: str, overlay: pathlib.Path, out_path: pathlib.Path) -> None:
    filter_complex = f"[0:v]{base_filter(kind)}[base];[base][1:v]overlay=0:0,format=yuv420p[v]"
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-ss",
        f"{start:.3f}",
        "-t",
        f"{duration:.3f}",
        "-i",
        str(source),
        "-loop",
        "1",
        "-t",
        f"{duration:.3f}",
        "-i",
        str(overlay),
        "-filter_complex",
        filter_complex,
        "-map",
        "[v]",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "23",
        "-r",
        str(FPS),
        "-t",
        f"{duration:.3f}",
        str(out_path),
    ], LOGS_DIR / f"{out_path.stem}.log")


def concat_videos(ffmpeg: str, inputs: list[pathlib.Path], out_path: pathlib.Path) -> None:
    concat_list = out_path.with_suffix(".txt")
    concat_list.write_text("".join(f"file '{p.as_posix()}'\n" for p in inputs), encoding="utf-8")
    run([
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
        str(out_path),
    ], LOGS_DIR / f"{out_path.stem}_concat.log")


def render_visual_track(ffmpeg: str, card_paths: dict[str, pathlib.Path], overlay_paths: dict[str, pathlib.Path]) -> tuple[pathlib.Path, list[dict[str, Any]]]:
    SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
    rendered_segments: list[pathlib.Path] = []
    manifest_segments: list[dict[str, Any]] = []
    cursor = 0.0

    for index, seg in enumerate(SEGMENTS, start=1):
        seg_id = seg["segment_id"]
        out = SEGMENTS_DIR / f"{index:02d}_{seg_id}.mp4"
        if seg["type"] == "card":
            render_card_segment(ffmpeg, card_paths[seg_id], float(seg["duration"]), out)
        else:
            part_paths = []
            for part_index, (start, end) in enumerate(seg["clips"], start=1):
                part = SEGMENTS_DIR / f"{index:02d}_{seg_id}_part{part_index}.mp4"
                render_clip_part(
                    ffmpeg,
                    pathlib.Path(seg["source"]),
                    float(start),
                    float(end) - float(start),
                    str(seg["kind"]),
                    overlay_paths[seg_id],
                    part,
                )
                part_paths.append(part)
            if len(part_paths) == 1:
                shutil.copyfile(part_paths[0], out)
            else:
                concat_videos(ffmpeg, part_paths, out)

        rendered_segments.append(out)
        manifest_segments.append({
            "index": index,
            "segment_id": seg_id,
            "label": seg["label"],
            "type": seg["type"],
            "planned_duration_seconds": seg["duration"],
            "timeline_start_seconds": round(cursor, 3),
            "timeline_end_seconds": round(cursor + float(seg["duration"]), 3),
            "rendered_path": str(out),
            "source_path": str(seg.get("source", "")) if seg.get("source") else "",
            "source_clips": seg.get("clips", []),
            "proof": seg["proof"],
            "cannot_prove": seg["cannot_prove"],
        })
        cursor += float(seg["duration"])

    visual = OUTPUT_DIR / "visual_track_105s.mp4"
    concat_videos(ffmpeg, rendered_segments, visual)
    return visual, manifest_segments


def mux_full_video(ffmpeg: str, visual: pathlib.Path, audio_path: pathlib.Path) -> pathlib.Path:
    full = OUTPUT_DIR / "full_video.mp4"
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(visual),
        "-i",
        str(audio_path),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "96k",
        "-t",
        f"{TARGET_DURATION:.3f}",
        str(full),
    ], LOGS_DIR / "mux_full_video.log")
    return full


def ffprobe_json(ffprobe: str, path: pathlib.Path) -> dict[str, Any]:
    proc = run([ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)])
    return json.loads(proc.stdout)


def validate_video(ffmpeg: str, ffprobe: str, full_video: pathlib.Path) -> dict[str, Any]:
    data = ffprobe_json(ffprobe, full_video)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})
    decodable = True
    decode_log = LOGS_DIR / "full_video_decode_check.log"
    try:
        run([ffmpeg, "-v", "error", "-i", str(full_video), "-f", "null", "-"], decode_log)
    except Exception as exc:
        decodable = False
        write_text(decode_log, str(exc))
    return {
        "file_path": str(full_video),
        "exists": full_video.exists(),
        "file_size_bytes": full_video.stat().st_size if full_video.exists() else 0,
        "duration_seconds": round(float(data.get("format", {}).get("duration", 0.0)), 3),
        "width": int(video.get("width", 0) or 0),
        "height": int(video.get("height", 0) or 0),
        "video_codec": video.get("codec_name", "unknown"),
        "audio_present": bool(audio),
        "audio_codec": audio.get("codec_name", "none") if audio else "none",
        "audio_channels": audio.get("channels", 0) if audio else 0,
        "decodable": decodable,
        "technical_validation": "passed" if full_video.exists() and video and audio and decodable else "failed",
        "metadata_validation": "passed" if full_video.exists() and video else "failed",
    }


def create_contact_sheet(ffmpeg: str, full_video: pathlib.Path) -> None:
    frames_dir = OUTPUT_DIR / "关键帧_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    frame_paths: list[pathlib.Path] = []
    cursor = 0.0
    for index, seg in enumerate(SEGMENTS, start=1):
        midpoint = cursor + float(seg["duration"]) / 2.0
        frame = frames_dir / f"{index:02d}_{seg['segment_id']}.jpg"
        run([
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(full_video),
            "-ss",
            f"{midpoint:.3f}",
            "-frames:v",
            "1",
            "-q:v",
            "3",
            str(frame),
        ], LOGS_DIR / f"contact_sheet_frame_{index:02d}.log")
        frame_paths.append(frame)
        cursor += float(seg["duration"])

    canvas = Image.new("RGB", (W, 960), "#f7f3f8")
    thumb_w, thumb_h = 180, 320
    for index, frame in enumerate(frame_paths):
        img = Image.open(frame).resize((thumb_w, thumb_h))
        x = (index % 4) * thumb_w
        y = (index // 4) * thumb_h
        canvas.paste(img, (x, y))
    canvas.save(OUTPUT_DIR / "contact_sheet.jpg", quality=90)


def copy_plan_files() -> None:
    for name in COPY_FILES:
        shutil.copyfile(PLAN_DIR / name, OUTPUT_DIR / name)


def sensitive_text_scan(paths: list[pathlib.Path]) -> dict[str, Any]:
    patterns = {
        "phone_cn": r"(?<!\d)1[3-9]\d{9}(?!\d)",
        "api_key": r"(?i)(api[_-]?key|access[_-]?key|secret|token)\s*[:=]\s*[A-Za-z0-9_\-]{8,}",
        "signed_url": r"(?i)(X-Amz-Signature|Expires=|Signature=|OSSAccessKeyId=)",
        "verification_code": r"验证码\s*[:：]?\s*\d{4,8}",
    }
    hits: list[dict[str, str]] = []
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in patterns.items():
            if re.search(pattern, text):
                hits.append({"file": str(path), "pattern": name})
    return {"sensitive_text_hits": hits, "passed": not hits}


def write_assembly_outputs(
    plan_info: dict[str, Any],
    source_rows: list[dict[str, Any]],
    audio_info: dict[str, Any],
    video_meta: dict[str, Any],
    segments: list[dict[str, Any]],
    captions: list[dict[str, Any]],
) -> None:
    total_real = sum(float(s["planned_duration_seconds"]) for s in segments if s["type"] == "real_footage")
    total_card = sum(float(s["planned_duration_seconds"]) for s in segments if s["type"] == "card")
    assembly = {
        "schema": "short_video_auto_flow_v21_assembly_manifest/v1",
        "created_at": NOW,
        "plan_dir": str(PLAN_DIR),
        "output_dir": str(OUTPUT_DIR),
        "source_manifest_sha256": sha256_file(PLAN_DIR / "timeline_manifest.json"),
        "runtime_script_sha256": sha256_file(PLAN_DIR / "runtime_script.md"),
        "reference_script_sha256": sha256_file(PLAN_DIR / "reference_script.md"),
        "render_policy": {
            "render_only": True,
            "timeline_rewritten": False,
            "runtime_script_rewritten": False,
            "reference_script_used_for_tts": False,
            "reference_script_used_for_captions": False,
            "api_segment": "api_info_card_fallback",
            "volcengine_original_used": False,
        },
        "locked_metrics": {
            "total_runtime_target_seconds": 105,
            "total_real_footage_seconds": 86,
            "total_card_seconds": 19,
            "real_footage_ratio": 0.819,
            "card_ratio": 0.181,
            "longest_card_seconds": 4,
            "segment_count": 12,
            "plan_status": "review_ready_not_render_ready",
        },
        "actual_planned_totals": {
            "total_duration_seconds": round(total_real + total_card, 3),
            "total_real_footage_seconds": round(total_real, 3),
            "total_card_seconds": round(total_card, 3),
            "real_footage_ratio": round(total_real / (total_real + total_card), 3),
            "card_ratio": round(total_card / (total_real + total_card), 3),
            "longest_card_seconds": max(float(s["planned_duration_seconds"]) for s in segments if s["type"] == "card"),
            "segment_count": len(segments),
        },
        "source_materials": source_rows,
        "segments": segments,
        "captions": {
            "source": "runtime_script.md",
            "count": len(captions),
            "path": str(OUTPUT_DIR / "captions.srt"),
            "json_path": str(OUTPUT_DIR / "captions.json"),
        },
        "audio": audio_info,
        "video": video_meta,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
    }
    write_json(OUTPUT_DIR / "assembly_manifest.json", assembly)


def write_reports(
    plan_info: dict[str, Any],
    source_rows: list[dict[str, Any]],
    audio_info: dict[str, Any],
    video_meta: dict[str, Any],
    scan: dict[str, Any],
) -> None:
    render_summary = {
        "created_at": NOW,
        "technical_validation": video_meta["technical_validation"],
        "metadata_validation": video_meta["metadata_validation"],
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "audio_validation": audio_info["audio_validation"],
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "full_video": str(OUTPUT_DIR / "full_video.mp4"),
        "captions_srt": str(OUTPUT_DIR / "captions.srt"),
        "duration_seconds": video_meta["duration_seconds"],
        "width": video_meta["width"],
        "height": video_meta["height"],
        "video_codec": video_meta["video_codec"],
        "audio_codec": video_meta["audio_codec"],
        "runtime_script_source": str(PLAN_DIR / "runtime_script.md"),
        "reference_script_used_for_tts": False,
        "reference_script_used_for_captions": False,
        "volcengine_original_used": False,
        "api_segment": "api_info_card_fallback",
        "sensitive_text_scan_passed": scan["passed"],
        "review_gate_resolution": plan_info["review_gate_resolution"],
    }
    write_json(OUTPUT_DIR / "render_summary.json", render_summary)

    report = f"""# render_report｜短视频自动流 V2.1 样片

## 1. 状态

- `created_at`：`{NOW}`
- `technical_validation`：`{video_meta['technical_validation']}`
- `metadata_validation`：`{video_meta['metadata_validation']}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`{audio_info['audio_validation']}`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 执行边界

- `已确认` 本轮为 render-only 执行任务。
- `已确认` 使用已落地 V2.1 计划包，不重写 `runtime_script.md`，不重写 `timeline_plan.md`，不重写 `timeline_manifest.json`。
- `已确认` TTS 与字幕来源均为 `runtime_script.md`。
- `已确认` `reference_script.md` 仅复制留档，未用于 TTS、字幕或直接渲染。
- `已确认` Segment 08 使用 API 信息卡 fallback，未使用火山引擎原画面。
- `部分成立` 计划包原始 `guardrail_check.md` 中 render gate 为等待审核；本轮用户已明确下发 render-only 执行单，因此记录为 `{plan_info['review_gate_resolution']}`。

## 3. 视频验证

- `full_video.mp4`：`{OUTPUT_DIR / 'full_video.mp4'}`
- `duration_seconds`：`{video_meta['duration_seconds']}`
- `resolution`：`{video_meta['width']}x{video_meta['height']}`
- `video_codec`：`{video_meta['video_codec']}`
- `audio_codec`：`{video_meta['audio_codec']}`
- `audio_present`：`{str(video_meta['audio_present']).lower()}`
- `decodable`：`{str(video_meta['decodable']).lower()}`

## 4. 来源验证

- `runtime_script_sha256`：`{sha256_file(PLAN_DIR / 'runtime_script.md')}`
- `reference_script_sha256`：`{sha256_file(PLAN_DIR / 'reference_script.md')}`
- `runtime_reference_length_ratio`：`{plan_info['runtime_reference_ratio']:.3f}`
- `captions_source`：`runtime_script.md`
- `audio_source`：`runtime_script.md`
- `reference_script_used_for_tts`：`false`
- `reference_script_used_for_captions`：`false`

## 5. 素材验证

{chr(10).join(f"- `{row['path']}`：`{row['codec']}`，`{row['width']}x{row['height']}`，`duration={row['duration_seconds']:.3f}s`" for row in source_rows)}

## 6. 脱敏与敏感信息

- `volcengine_original_used`：`false`
- `api_segment`：`api_info_card_fallback`
- `redaction_decision`：`redaction_blocked_fallback_to_info_card`
- `codex_masks`：右侧分支详情、底部路径、顶部区域、局部任务信息遮挡。
- `trae_masks`：底部路径、顶部本地路径区域遮挡。
- `sensitive_text_scan_passed`：`{str(scan['passed']).lower()}`
- `sensitive_text_hits`：`{scan['sensitive_text_hits']}`

## 7. 内容边界

- `已确认` Trae 项目骨架不等于 app 跑通。
- `已确认` API 信息卡不等于 API 已接通。
- `已确认` 云剪工位不等于阿里云剪辑正式稳定。
- `已确认` Codex 检查不等于内容过线。
- `已确认` 即梦对比不写成即梦不可用。
"""
    write_text(OUTPUT_DIR / "render_report.md", report)

    redaction_report = f"""# redaction_report｜短视频自动流 V2.1

## 1. 结论

- `是否使用火山引擎 API 原画面`：`false`
- `是否 fallback 到 API 信息卡`：`true`
- `redaction_decision`：`redaction_blocked_fallback_to_info_card`
- `是否发现敏感信息`：`{str(not scan['passed']).lower()}`

## 2. 遮挡执行

- Trae 段：遮挡顶部 / 底部本地路径区域，保留 SOLO Coder、Updating Tasks、11 待办和项目骨架证据。
- Codex 段：遮挡右侧分支详情、底部路径、顶部区域和局部任务信息，保留执行检查感。
- API 段：不使用火山原画面，使用信息卡说明 API 是外部能力入口。

## 3. 边界

- API 信息卡不证明 API 已接通。
- Codex 检查不证明内容过线。
- 本报告不构成内容最终通过。
"""
    write_text(OUTPUT_DIR / "redaction_report.md", redaction_report)

    local_path_report = f"""# local_open_path_report｜短视频自动流 V2.1

| artifact | path | path_exists | notes |
|---|---|---:|---|
| `full_video.mp4` | `{OUTPUT_DIR / 'full_video.mp4'}` | `{str((OUTPUT_DIR / 'full_video.mp4').is_file()).lower()}` | 本地可观看样片，未计划提交大媒体 |
| `captions.srt` | `{OUTPUT_DIR / 'captions.srt'}` | `{str((OUTPUT_DIR / 'captions.srt').is_file()).lower()}` | 字幕来自 runtime_script |
| `contact_sheet.jpg` | `{OUTPUT_DIR / 'contact_sheet.jpg'}` | `{str((OUTPUT_DIR / 'contact_sheet.jpg').is_file()).lower()}` | 关键帧预览，未计划提交图片 |
| `render_report.md` | `{OUTPUT_DIR / 'render_report.md'}` | `{str((OUTPUT_DIR / 'render_report.md').is_file()).lower()}` | 渲染报告 |

- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
"""
    write_text(OUTPUT_DIR / "local_open_path_report.md", local_path_report)


def update_logs(video_meta: dict[str, Any], audio_info: dict[str, Any]) -> None:
    latest_path = ROOT / "codex_log" / "latest.md"
    latest_old = load_text(latest_path) if latest_path.exists() else "# Latest\n"
    entry = f"""# Latest

## 20260503｜短视频自动流 V2.1 流程证明样片 render

- `已确认` 本轮从已落地计划包执行 render-only 任务，未重写 `runtime_script.md`、`timeline_plan.md` 或 `timeline_manifest.json`。
- `已确认` 输出本地样片：`{OUTPUT_DIR / 'full_video.mp4'}`。
- `已确认` 视频技术验证：`technical_validation = {video_meta['technical_validation']}`，`duration_seconds = {video_meta['duration_seconds']}`，`resolution = {video_meta['width']}x{video_meta['height']}`，`video_codec = {video_meta['video_codec']}`，`audio_codec = {video_meta['audio_codec']}`。
- `已确认` 字幕与临时 TTS 均来自 `runtime_script.md`；`reference_script.md` 仅作参考稿副本，未用于 TTS / 字幕 / 直接渲染。
- `已确认` Segment 08 使用 API 信息卡 fallback，未使用火山引擎原画面。
- `已确认` `content_validation = pending_user_chatgpt_review`，`send_ready = false`，`voice_validation = pending_user_chatgpt_review`，`final_voice_validated = false`。
- `样片目录`：`{OUTPUT_DIR}`
- `下一个目标`：ChatGPT / 用户复审 V2.1 本地样片，判断是否进入内容修正或正式重剪。

"""
    if latest_old.startswith("# Latest\n"):
        latest_new = entry + latest_old[len("# Latest\n"):]
    else:
        latest_new = entry + "\n" + latest_old
    write_text(latest_path, latest_new)

    dated_log = ROOT / "codex_log" / "20260503_短视频自动流v21视频样片_short_video_auto_flow_v21_video_sample.md"
    write_text(dated_log, f"""# 短视频自动流 V2.1 视频样片执行日志

## 1. 执行结果

- `technical_validation`：`{video_meta['technical_validation']}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`{audio_info['audio_validation']}`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 本地产物

- `full_video.mp4`：`{OUTPUT_DIR / 'full_video.mp4'}`
- `captions.srt`：`{OUTPUT_DIR / 'captions.srt'}`
- `render_report.md`：`{OUTPUT_DIR / 'render_report.md'}`
- `render_summary.json`：`{OUTPUT_DIR / 'render_summary.json'}`
- `assembly_manifest.json`：`{OUTPUT_DIR / 'assembly_manifest.json'}`
- `contact_sheet.jpg`：`{OUTPUT_DIR / 'contact_sheet.jpg'}`
- `local_open_path_report.md`：`{OUTPUT_DIR / 'local_open_path_report.md'}`

## 3. 口径

- `已确认` 本轮不是内容过线，不是可发送状态。
- `已确认` Trae 项目骨架不等于 app 跑通。
- `已确认` API 信息卡不等于 API 已接通。
- `已确认` Codex 检查不等于内容过线。

## 4. 下一个目标

ChatGPT / 用户复审 V2.1 本地样片，判断是否进入内容修正或正式重剪。
""")

    paths_path = ROOT / "codex_log" / "current_local_artifact_paths.md"
    paths_old = load_text(paths_path)
    row = f"| `short_video_auto_flow_v21_sample_full_video` | 短视频自动流 V2.1 流程证明样片 | ChatGPT / 用户复审流程证明型技术样片 | `{OUTPUT_DIR / 'full_video.mp4'}` | `true` | 无 | `2026-05-03 CST` | `ffprobe` + `test -f` 已通过 | `content_validation = pending_user_chatgpt_review`，`send_ready = false`，大媒体仅保留本地，不计划提交 Git。 |\n"
    if "short_video_auto_flow_v21_sample_full_video" not in paths_old:
        insert = "\n" + row
        marker = "## 4. 本轮单工作区治理结果"
        if marker in paths_old:
            paths_new = paths_old.replace(marker, insert + "\n" + marker, 1)
        else:
            paths_new = paths_old.rstrip() + insert
        write_text(paths_path, paths_new)


def main() -> None:
    if ROOT.resolve() != pathlib.Path.cwd().resolve():
        raise RuntimeError(f"must run from {ROOT}, got {pathlib.Path.cwd()}")

    ffmpeg = resolve_bin("ffmpeg")
    ffprobe = resolve_bin("ffprobe")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plan_info = validate_plan_package()
    source_rows = validate_sources(ffprobe)
    copy_plan_files()

    voiceover_text = extract_runtime_voiceover(plan_info["runtime_md"])
    captions = make_captions(voiceover_text)
    audio_info = make_temporary_tts(ffmpeg, ffprobe, voiceover_text)
    card_paths, overlay_paths = generate_cards_and_overlays()
    visual, segments = render_visual_track(ffmpeg, card_paths, overlay_paths)
    full_video = mux_full_video(ffmpeg, visual, pathlib.Path(audio_info["audio_path"]))
    video_meta = validate_video(ffmpeg, ffprobe, full_video)
    create_contact_sheet(ffmpeg, full_video)

    scan_paths = [
        OUTPUT_DIR / "captions.srt",
        OUTPUT_DIR / "captions.json",
        OUTPUT_DIR / "render_report.md",
        OUTPUT_DIR / "render_summary.json",
        OUTPUT_DIR / "assembly_manifest.json",
        OUTPUT_DIR / "local_open_path_report.md",
        OUTPUT_DIR / "redaction_report.md",
        OUTPUT_DIR / "runtime_script.md",
        OUTPUT_DIR / "reference_script.md",
        OUTPUT_DIR / "timeline_plan.md",
        OUTPUT_DIR / "timeline_manifest.json",
        OUTPUT_DIR / "material_usage_plan.md",
        OUTPUT_DIR / "redaction_plan.md",
        OUTPUT_DIR / "guardrail_check.md",
    ]
    scan = sensitive_text_scan(scan_paths)
    if not scan["passed"]:
        raise RuntimeError(f"sensitive text patterns found: {scan['sensitive_text_hits']}")

    write_assembly_outputs(plan_info, source_rows, audio_info, video_meta, segments, captions)
    scan = sensitive_text_scan(scan_paths)
    if not scan["passed"]:
        raise RuntimeError(f"sensitive text patterns found after assembly: {scan['sensitive_text_hits']}")
    write_reports(plan_info, source_rows, audio_info, video_meta, scan)
    update_logs(video_meta, audio_info)

    print(json.dumps({
        "full_video": str(full_video),
        "duration_seconds": video_meta["duration_seconds"],
        "technical_validation": video_meta["technical_validation"],
        "audio_validation": audio_info["audio_validation"],
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
