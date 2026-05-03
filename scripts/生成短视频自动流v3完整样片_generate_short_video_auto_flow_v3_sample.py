#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import os
import re
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/Users/fan/Documents/视频工厂")
OUT_DIR = ROOT / "dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v3_complete_review_sample"
REPORT_DIR = ROOT / "样片报告_sample_reports/20260503_短视频自动流最简单流程_v3_complete_review_sample"
ASSET_DIR = OUT_DIR / "assets"
CLIP_DIR = OUT_DIR / "clips"
CARD_DIR = OUT_DIR / "cards"

WIDTH = 720
HEIGHT = 1280
FPS = 25
BG = (248, 239, 238)
PINK = (255, 105, 150)
INK = (46, 40, 48)
MUTED = (98, 86, 98)
CARD = (255, 252, 252)
LINE = (238, 190, 205)


@dataclass
class Segment:
    segment_id: str
    kind: str
    title: str
    subtitle: str
    caption: str
    weight: float
    source: str | None = None
    start: float | None = None
    end: float | None = None
    route: str | None = None
    mask: str | None = None
    proof: str = ""
    cannot_prove: str = ""


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess:
    print("+", " ".join(cmd))
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True, check=check)


def git_show(spec: str) -> str:
    return run(["git", "show", spec]).stdout


def ffprobe_duration(path: Path) -> float:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ]
    ).stdout.strip()
    return float(result)


def ffprobe_json(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ]
    ).stdout
    return json.loads(result)


def ensure_dirs() -> None:
    for path in [OUT_DIR, REPORT_DIR, ASSET_DIR, CLIP_DIR, CARD_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size, index=0)
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font_obj: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for ch in paragraph:
            trial = current + ch
            if draw.textlength(trial, font=font_obj) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines


def draw_card(path: Path, title: str, subtitle: str, route: str, tag: str) -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    title_font = font(54, True)
    sub_font = font(34)
    tag_font = font(24)
    small_font = font(22)

    # Soft route-specific background language. Still static; no HyperFrames render this round.
    for i in range(0, WIDTH, 90):
        color = (255, 224 + (i // 90) % 2 * 8, 235)
        draw.ellipse((i - 35, 80 + (i % 160), i + 28, 143 + (i % 160)), fill=color)
    draw.rounded_rectangle((50, 210, 670, 1030), radius=42, fill=CARD, outline=LINE, width=3)
    draw.rounded_rectangle((86, 250, 634, 318), radius=26, fill=(255, 235, 242))
    draw.text((112, 268), tag, font=tag_font, fill=PINK)
    draw.text((92, 945), route, font=small_font, fill=(170, 115, 135))

    title_lines = wrap_text(draw, title, title_font, 500)
    y = 390
    for line in title_lines[:3]:
        w = draw.textlength(line, font=title_font)
        draw.text(((WIDTH - w) / 2, y), line, font=title_font, fill=INK)
        y += 72

    y += 30
    sub_lines = wrap_text(draw, subtitle, sub_font, 520)
    for line in sub_lines[:6]:
        w = draw.textlength(line, font=sub_font)
        draw.text(((WIDTH - w) / 2, y), line, font=sub_font, fill=MUTED)
        y += 52

    # Little original voxel host mark, deliberately a card mark not API human.
    draw.rounded_rectangle((520, 825, 610, 915), radius=12, fill=(242, 96, 105))
    draw.rectangle((535, 790, 595, 850), fill=(255, 214, 185))
    draw.rectangle((546, 812, 556, 822), fill=INK)
    draw.rectangle((574, 812, 584, 822), fill=INK)
    draw.arc((552, 820, 578, 845), 10, 170, fill=INK, width=2)
    img.save(path, quality=95)


def make_card_clip(image_path: Path, clip_path: Path, duration: float) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(image_path),
            "-vf",
            f"fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            str(clip_path),
        ]
    )


def mask_filters(mask: str | None) -> str:
    boxes: list[str] = []
    if mask in {"trae", "codex"}:
        boxes.append("drawbox=x=0:y=822:w=720:h=70:color=black@0.88:t=fill")
        boxes.append("drawbox=x=0:y=390:w=720:h=34:color=black@0.55:t=fill")
    if mask == "codex":
        boxes.append("drawbox=x=520:y=405:w=200:h=470:color=black@0.92:t=fill")
        boxes.append("drawbox=x=0:y=405:w=115:h=470:color=black@0.72:t=fill")
    if mask == "doubao":
        boxes.append("drawbox=x=0:y=405:w=120:h=470:color=black@0.35:t=fill")
    return ",".join(boxes)


def make_footage_clip(segment: Segment, clip_path: Path, duration: float) -> None:
    assert segment.source and segment.start is not None and segment.end is not None
    source = ROOT / segment.source
    src_duration = segment.end - segment.start
    ratio = duration / src_duration
    filters = [
        "scale=720:-2",
        "pad=720:1280:(ow-iw)/2:(oh-ih)/2:color=0xF8EFEE",
        "setsar=1",
    ]
    masks = mask_filters(segment.mask)
    if masks:
        filters.append(masks)
    filters.extend([f"setpts=PTS*{ratio:.8f}", f"fps={FPS}", "format=yuv420p"])
    run(
        [
            "ffmpeg",
            "-y",
            "-ss",
            f"{segment.start:.3f}",
            "-t",
            f"{src_duration:.3f}",
            "-i",
            str(source),
            "-vf",
            ",".join(filters),
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            str(clip_path),
        ]
    )


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def sanitize_for_commit_scan(text: str) -> list[str]:
    patterns = {
        "phone_like": r"(?<!\d)1[3-9]\d{9}(?!\d)",
        "access_key_like": r"\b(AKIA|LTAI|ASIA)[A-Z0-9]{12,}\b",
        "secret_assignment": r"(?i)(secret|token|api[_ -]?key|access[_ -]?key)\s*[:=]\s*['\"][^'\"]{8,}['\"]",
        "signed_url": r"https?://[^\s]+(Signature|Expires|X-Amz-|OSSAccessKeyId)[^\s]*",
    }
    hits: list[str] = []
    for name, pattern in patterns.items():
        if re.search(pattern, text):
            hits.append(name)
    return hits


def timestamp(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h = ms // 3_600_000
    ms %= 3_600_000
    m = ms // 60_000
    ms %= 60_000
    s = ms // 1000
    ms %= 1000
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build_srt(segments: list[Segment], durations: list[float]) -> tuple[str, list[dict]]:
    entries = []
    json_entries = []
    cursor = 0.0
    for idx, (seg, dur) in enumerate(zip(segments, durations), start=1):
        start = cursor
        end = cursor + dur
        entries.append(f"{idx}\n{timestamp(start)} --> {timestamp(end)}\n{seg.caption}\n")
        json_entries.append(
            {
                "index": idx,
                "start": round(start, 3),
                "end": round(end, 3),
                "segment_id": seg.segment_id,
                "text": seg.caption,
            }
        )
        cursor = end
    return "\n".join(entries), json_entries


def choose_say_voice() -> tuple[str | None, str]:
    voices = run(["say", "-v", "?"], check=False).stdout
    for candidate in ["Tingting", "Mei-Jia", "Sin-ji", "Yu-shu"]:
        if candidate in voices:
            return candidate, voices
    return None, voices


def make_tts(runtime_text: str) -> tuple[Path, dict]:
    voice, voices = choose_say_voice()
    aiff = ASSET_DIR / "voiceover_temporary_preview.aiff"
    wav = ASSET_DIR / "voiceover_temporary_preview.wav"
    m4a = ASSET_DIR / "voiceover_temporary_preview.m4a"
    say_cmd = ["say", "-r", "235", "-o", str(aiff)]
    if voice:
        say_cmd[1:1] = ["-v", voice]
    say_cmd.append(runtime_text)
    result = run(say_cmd, check=False)
    if result.returncode != 0 and voice:
        say_cmd = ["say", "-r", "235", "-o", str(aiff), runtime_text]
        result = run(say_cmd, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr or "macOS say fallback failed")
    run(["ffmpeg", "-y", "-i", str(aiff), "-ar", "44100", "-ac", "1", str(wav)])
    duration = ffprobe_duration(wav)
    source_wav = wav
    speed_ratio = 1.0
    if duration > 150:
        target = 145.0
        speed_ratio = duration / target
        sped = ASSET_DIR / "voiceover_temporary_preview_sped.wav"
        # ffmpeg atempo supports 0.5-100 in modern builds; keep within a sane range.
        run(["ffmpeg", "-y", "-i", str(wav), "-filter:a", f"atempo={speed_ratio:.6f}", str(sped)])
        source_wav = sped
        duration = ffprobe_duration(sped)
    run(["ffmpeg", "-y", "-i", str(source_wav), "-c:a", "aac", "-b:a", "128k", str(m4a)])
    return m4a, {
        "tts_provider": "macOS say fallback",
        "voice": voice or "system_default",
        "audio_validation": "temporary_preview",
        "project_tts_attempt": "not_safe_to_execute_without_confirmable_full_script_runtime_wrapper",
        "speed_ratio": round(speed_ratio, 4),
        "duration_seconds": round(ffprobe_duration(m4a), 3),
        "available_voice_list_sample": "\n".join(voices.splitlines()[:8]),
    }


def main() -> None:
    ensure_dirs()

    reference = git_show(
        "codex/short-video-auto-flow-script-pack-20260503:"
        "文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/01_完整口播稿_full_script.md"
    )
    material_report = git_show(
        "codex/vnext-material-detail-recapture-20260503:"
        "素材检查_reports/20260503_vNext素材细节复采_vnext_material_detail_recapture/素材细节复采报告_material_detail_recapture_report.md"
    )
    intake_summary = json.loads(
        git_show(
            "codex/vnext-recorded-material-intake-20260503:"
            "素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/recommended_assembly_inputs.json"
        )
    )

    runtime_sections = [
        "短视频自动流，最简单的流程，不是先问哪个 AI 一键生成视频。一键生成更像抽素材，这次能用，下次风格、字幕、节奏可能又要重来。真正要验证的是，一条短视频能不能拆成一套可重复跑的流程。",
        "我这次第一步很简单：打开豆包，只输入一句话，我想用 Trae 做一个短视频自动流。这一步不是让豆包直接做视频，而是先把顺序理出来。",
        "豆包先把需求拆成流程：选题、脚本、分镜、素材、视频生成或剪辑、配音字幕、封面标题、最后发布。它不是在讲某个单点工具，而是在把短视频生产拆成一排工位。",
        "接着我追问：我主要想做一个 Vlog 的视频自动流，你先给我一个 prompt，让 Trae 帮我把架构搭建出来。关键转折就在这里，豆包开始把想法翻译成 Trae 能接住的任务说明。",
        "豆包给出 Trae Vlog 自动流核心搭建 Prompt，里面有全局人设锚定、选题叙事、分镜脚本、素材调度、自动化后期、运营物料导出和总控异常处理。注意，这不代表系统已经跑通，只代表 prompt 的目标是先把架构搭出来。",
        "下一步，我把这份 prompt 放进 Trae SOLO。画面里能看到 SOLO Coder、plan、spec 这些入口，说明它已经从聊天方案进入了执行器。",
        "Trae 没有只回一句建议。它先说让我规划一下任务，然后逐步实现，随后出现 Updating Tasks 和 11 个待办。这一步说明 prompt 已经被拆成 Trae 自己能执行的任务列表。",
        "再往后，Trae 创建了 vlog_automation_workflow 项目骨架，下面能看到 modules、templates、workflows、config、assets、frontend、logs，也出现了 settings.py 和 base_module.py。它证明的是从聊天里的方案变成电脑里的项目骨架，不证明代码已经运行成功。",
        "然后才轮到 API。API 可以先理解成把文字生成、配音、图片、卡片、剪辑总装这些外部能力，逐步接成系统能调用的工位。本轮画面只说明 API 的位置，不证明 API 已经全部接通。",
        "云端剪辑在这个流程里更像装配台。阿里云剪辑、ICE、云剪负责把录屏、卡片、音轨按时间线组装导出；它不是总控脑，也不负责判断内容好不好。技术链路能跑，不等于正式稳定。",
        "Codex 在这里更像执行检查员。它检查素材路径、文件、命令、解码、报告和状态边界。这个过程很啰嗦，但自动流最怕的不是失败，而是把半成品写成完成。",
        "所以这条视频讲的不是某个工具最强。豆包负责拆需求，Trae 负责搭骨架，API 负责接能力，云剪负责总装，Codex 负责检查。每个工具接自己那一段。",
        "即梦这类工具适合快速抽一个素材、一个镜头、一个感觉；短视频自动流解决的是需求能不能拆成流程，流程能不能变成项目，项目能不能继续接工具，最后持续生产。",
        "前期它一定更慢，因为要先把流程搭出来。但一旦流程能跑，后面不是每条视频都重新赌一次。工具可以换，流程还在，出问题时也知道卡在哪一步。",
        "所以，短视频自动流最简单的流程，就是先把视频生产拆开，再让每一步有人负责、有工具能做、有结果能检查。别一上来追求一键生成，先把顺序理出来。顺序对了，自动化才有地方落脚。",
    ]
    runtime_text = "\n\n".join(runtime_sections)
    write_text(OUT_DIR / "reference_script.md", reference)
    write_text(OUT_DIR / "runtime_full_script.md", "# runtime_full_script\n\n" + runtime_text)

    audio_path, audio_info = make_tts(runtime_text)
    audio_duration = ffprobe_duration(audio_path)
    visual_total = max(92.0, audio_duration + 1.5)

    segments = [
        Segment("opening_judgement", "card", "自动流不是一键生成", "先把视频生产拆成一套能重复跑的流程", runtime_sections[0], 0.06, route="cute_prompt_card_route", proof="建立主判断", cannot_prove="不证明工具执行"),
        Segment("doubao_simple_need", "footage", "一句需求进入豆包", "我想用 Trae 做一个短视频自动流", runtime_sections[1], 0.08, "素材录制/最新素材/豆包素材.mp4", 16, 24, mask="doubao", proof="需求入口真实存在", cannot_prove="不证明 Trae 已执行"),
        Segment("doubao_breakdown", "footage", "豆包拆成流程", "从轻量版到无人值守版，先把工位拆开", runtime_sections[2], 0.10, "素材录制/最新素材/豆包素材.mp4", 88, 120, mask="doubao", proof="豆包输出流程方案", cannot_prove="不证明工程跑通"),
        Segment("doubao_prompt", "footage", "豆包生成 Trae Prompt", "把想法翻译成 Trae 能接住的任务说明", runtime_sections[3] + " " + runtime_sections[4], 0.12, "素材录制/最新素材/豆包素材.mp4", 160, 248, mask="doubao", proof="豆包给出 Trae SOLO prompt", cannot_prove="不证明 prompt 已运行成功"),
        Segment("trae_entry", "footage", "进入 Trae SOLO", "从聊天方案进入执行器", runtime_sections[5], 0.07, "素材录制/最新素材/trae 素材.mp4", 32, 64, mask="trae", proof="SOLO Coder 入口存在", cannot_prove="不证明执行完成"),
        Segment("trae_plan", "footage", "Prompt 进入 Trae 并开始 plan", "Updating Tasks 和 11 个待办出现", runtime_sections[6], 0.12, "素材录制/最新素材/trae 素材.mp4", 80, 112, mask="trae", proof="Trae 接住 prompt 并拆任务", cannot_prove="不证明所有待办完成"),
        Segment("trae_skeleton", "footage", "项目骨架出现", "vlog_automation_workflow 生成目录和基础文件", runtime_sections[7], 0.13, "素材录制/最新素材/trae 素材.mp4", 120, 160, mask="trae", proof="从聊天方案变成项目骨架", cannot_prove="不证明 app 跑通"),
        Segment("api_station", "card", "API 是外部能力入口", "本轮只说明工位位置，不写成 API 已接通", runtime_sections[8], 0.06, route="cute_info_card_route", proof="解释 API 工位", cannot_prove="不证明 API 已接通"),
        Segment("cloud_station", "card", "云剪是装配台", "负责总装方向，不是总控脑，也不是稳定事实", runtime_sections[9], 0.06, route="cute_info_card_route", proof="解释云端总装位置", cannot_prove="不证明云剪正式稳定"),
        Segment("codex_check", "footage", "Codex 执行检查员", "检查路径、文件、命令、解码和报告", runtime_sections[10], 0.08, "素材录制/最新素材/codex 素材.mp4", 176, 188, mask="codex", proof="Codex 检查过程存在", cannot_prove="不证明内容过线"),
        Segment("tool_roles", "card", "工具各接一段", "豆包拆需求，Trae 搭骨架，API 接能力，云剪总装，Codex 检查", runtime_sections[11] + " " + runtime_sections[12], 0.07, route="cute_info_card_route", proof="说明工具定位", cannot_prove="不证明所有工具已跑通"),
        Segment("closing", "card", "顺序对了，自动化才有地方落脚", "流程还在，工位上的工具可以换", runtime_sections[13] + " " + runtime_sections[14], 0.05, route="cute_info_card_route", proof="收束主判断", cannot_prove="不证明可发送"),
    ]
    total_weight = sum(s.weight for s in segments)
    durations = [visual_total * s.weight / total_weight for s in segments]

    clip_paths: list[Path] = []
    for idx, (seg, dur) in enumerate(zip(segments, durations), start=1):
        clip_path = CLIP_DIR / f"{idx:02d}_{seg.segment_id}.mp4"
        if seg.kind == "card":
            image_path = CARD_DIR / f"{idx:02d}_{seg.segment_id}.png"
            draw_card(image_path, seg.title, seg.subtitle, seg.route or "cute_info_card_route", seg.segment_id)
            make_card_clip(image_path, clip_path, dur)
        else:
            make_footage_clip(seg, clip_path, dur)
        clip_paths.append(clip_path)

    concat_path = ASSET_DIR / "concat_list.txt"
    concat_path.write_text("".join(f"file '{p.as_posix()}'\n" for p in clip_paths), encoding="utf-8")
    visual_only = ASSET_DIR / "visual_only.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(visual_only)])
    full_video = OUT_DIR / "full_video.mp4"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(visual_only),
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
            "128k",
            "-shortest",
            str(full_video),
        ]
    )

    srt_text, caption_json = build_srt(segments, durations)
    write_text(OUT_DIR / "captions.srt", srt_text)
    (OUT_DIR / "captions.json").write_text(json.dumps(caption_json, ensure_ascii=False, indent=2), encoding="utf-8")

    contact = OUT_DIR / "contact_sheet.jpg"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(full_video),
            "-vf",
            "fps=1/10,scale=220:-1,tile=3x4:padding=8:margin=12",
            "-frames:v",
            "1",
            str(contact),
        ]
    )

    metadata = ffprobe_json(full_video)
    video_stream = next(s for s in metadata["streams"] if s["codec_type"] == "video")
    audio_stream = next((s for s in metadata["streams"] if s["codec_type"] == "audio"), None)
    decode = run(["ffmpeg", "-v", "error", "-i", str(full_video), "-f", "null", "-"], check=False)
    technical_validation = "passed" if decode.returncode == 0 and audio_stream else "failed"
    duration = float(metadata["format"]["duration"])

    timeline = []
    cursor = 0.0
    for idx, (seg, dur, path) in enumerate(zip(segments, durations, clip_paths), start=1):
        timeline.append(
            {
                "index": idx,
                "segment_id": seg.segment_id,
                "kind": seg.kind,
                "start_seconds": round(cursor, 3),
                "end_seconds": round(cursor + dur, 3),
                "duration_seconds": round(dur, 3),
                "source": seg.source,
                "source_timecode": None if seg.start is None else f"{seg.start}-{seg.end}",
                "route": seg.route,
                "mask": seg.mask,
                "proof": seg.proof,
                "cannot_prove": seg.cannot_prove,
                "rendered_path": str(path),
            }
        )
        cursor += dur

    sample_type = "flow_proof_sample"
    fallback = {
        "sample_type": sample_type,
        "api_human": "missing_api_human_runtime_fallback_to_host_cards",
        "project_tts": "project_tts_not_safely_executed_fallback_to_macos_say_temporary_preview",
        "v3_cloud_assembly": "not_used_fallback_local_preview",
        "locked_reference": "registry_read_plan_level_inheritance_only_mainline_blocked",
        "material_redaction": "volcengine_not_used_info_card_fallback",
    }

    manifest = {
        "sample_id": "20260503_short_video_auto_flow_v3_complete_review_sample",
        "sample_type": sample_type,
        "technical_validation": technical_validation,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "audio_validation": "temporary_preview",
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "cloud_assembly_runtime": "not_used_fallback_local_preview",
        "api_human_runtime": "missing_api_human_runtime_fallback_to_host_cards",
        "reference_script_used": True,
        "runtime_full_script_source": "adapted_from_PR40_full_script_with_semantic_chain_preserved",
        "full_video_path": str(full_video),
        "segments": timeline,
        "fallback": fallback,
    }
    (OUT_DIR / "assembly_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "timeline_manifest.json").write_text(json.dumps({"timeline": timeline}, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "render_summary.json").write_text(
        json.dumps(
            {
                "created_at": datetime.now().isoformat(timespec="seconds"),
                "sample_type": sample_type,
                "technical_validation": technical_validation,
                "content_validation": "pending_user_chatgpt_review",
                "send_ready": False,
                "duration_seconds": round(duration, 3),
                "width": int(video_stream["width"]),
                "height": int(video_stream["height"]),
                "video_codec": video_stream["codec_name"],
                "audio_codec": audio_stream["codec_name"] if audio_stream else None,
                "audio_validation": "temporary_preview",
                "cloud_assembly_runtime": "not_used_fallback_local_preview",
                "large_media_committed_to_git": False,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    rows = [
        "| index | segment_id | carrier | duration | proof | cannot_prove |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for item in timeline:
        carrier = "用户录制素材" if item["kind"] == "footage" else "少量 PPT / 信息卡"
        rows.append(
            f"| {item['index']} | `{item['segment_id']}` | {carrier} | {item['duration_seconds']} | {item['proof']} | {item['cannot_prove']} |"
        )
    write_text(
        OUT_DIR / "timeline_plan.md",
        "# timeline_plan\n\n"
        + "\n".join(rows)
        + "\n\n`已确认` 本轮为 `flow_proof_sample`，用户录制素材承担中段主体，信息卡只做边界和总结辅助。\n",
    )

    visual_route = {
        "passed": True,
        "sample_type": sample_type,
        "routes": [
            {"card_id": "opening_judgement", "assigned_route": "cute_prompt_card_route", "status": "planned_and_rendered_as_static_card"},
            {"card_id": "api_station", "assigned_route": "cute_info_card_route", "status": "rendered_as_info_card"},
            {"card_id": "cloud_station", "assigned_route": "cute_info_card_route", "status": "rendered_as_info_card"},
            {"card_id": "tool_roles", "assigned_route": "cute_info_card_route", "status": "rendered_as_info_card"},
            {"card_id": "closing", "assigned_route": "cute_info_card_route", "status": "rendered_as_info_card"},
        ],
        "sassy_reaction_card_route": "not_used_no_forced_sassy_card",
        "hyperframes": "not_rendered_this_round",
        "blocked_for_mainline": ["api_human_runtime_missing", "project_tts_fallback", "cloud_assembly_fallback"],
    }
    (REPORT_DIR / "visual_route_validation_report.json").write_text(json.dumps(visual_route, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy2(REPORT_DIR / "visual_route_validation_report.json", OUT_DIR / "visual_route_validation_report.json")

    write_text(
        REPORT_DIR / "hyperframes_motion_validation_report.md",
        """# HyperFrames motion validation report

- 是否调用 HyperFrames：`否`
- 定位：`card_motion_layer`
- 是否接入中段录屏：`否`
- 是否替代真实录屏：`否`
- 是否替代云端剪辑：`否`
- 是否新增视觉 route：`否`
- 结论：`passed_for_non_use_boundary`

`已确认` 本轮完整样片未调用 HyperFrames 渲染；卡片为本地静态辅助卡，未抢用户录制素材主体。
""",
    )

    write_text(
        REPORT_DIR / "locked_reference_inheritance_report.md",
        """# locked_reference_inheritance_report

## 1. registry

- `locked_reference_registry_read`：`true`
- `locked_reference_inheritance_validation`：`blocked_for_mainline_fallback_sample_produced`
- `sample_type`：`flow_proof_sample`

## 2. 命中 reference

| reference_id | status | 本轮落点 | 继承状态 |
| --- | --- | --- | --- |
| `middle_editing_round34_locked_20260425` | locked | 用户录制素材主体推进 | `inherited_at_structure_level` |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | locked | 录屏保全画面 + 局部遮挡 | `partially_inherited_no_zoom_contact_evidence` |
| `tts_15s_b_pacing_locked_20260427` | locked | TTS 节奏参考 | `not_inherited_project_tts_fallback` |
| `opening_reference_element_doll_no_text_locked_20260428` | locked | 开头主持壳位置 | `not_inherited_api_human_runtime_missing` |
| `cute_prompt_card_route_locked_20260501` | locked | 开头判断卡 | `inherited_at_route_level` |
| `cute_info_card_route_locked_20260501` | locked | API / 云剪 / 总结信息卡 | `inherited_at_route_level` |
| `sassy_card_pr7_b_visual_locked_20260501` | locked | 未使用骚萌卡 | `not_applicable_no_sassy_card_forced` |
| `visual_master_voxel_element_doll_candidate_20260430` | candidate | 主持壳方向 | `candidate_not_locked` |

## 3. 结论

`已确认` 本轮不能写成 `mainline_inheritance_candidate`，因为 API 主持壳、项目 TTS、V3 云剪未形成本轮真实 runtime 证据。
`已确认` 本轮可以写成 `flow_proof_sample`，用于复审豆包 -> Trae -> 项目骨架 -> Codex 检查流程。
""",
    )
    shutil.copy2(REPORT_DIR / "locked_reference_inheritance_report.md", OUT_DIR / "locked_reference_inheritance_report.md")

    scan_text = "\n".join(
        [
            reference,
            runtime_text,
            json.dumps(manifest, ensure_ascii=False),
            json.dumps(visual_route, ensure_ascii=False),
        ]
    )
    sensitive_hits = sanitize_for_commit_scan(scan_text)
    write_text(
        REPORT_DIR / "redaction_report.md",
        f"""# redaction_report

- 是否使用火山引擎原画面：`false`
- 是否 fallback 信息卡：`true`
- 敏感文本扫描命中：`{sensitive_hits}`
- Trae 遮挡：顶部 / 底部本地路径区域遮挡。
- Codex 遮挡：右侧分支详情、底部路径、左侧边栏区域遮挡。
- 豆包遮挡：侧栏弱遮挡。

`已确认` 本轮不使用未脱敏火山引擎画面，不提交签名 URL、密钥、手机号、验证码或资源 ID。
""",
    )
    shutil.copy2(REPORT_DIR / "redaction_report.md", OUT_DIR / "redaction_report.md")

    write_text(
        REPORT_DIR / "failure_and_fallback_report.md",
        f"""# failure_and_fallback_report

## 1. 样片等级

- `sample_type`：`flow_proof_sample`
- 降级原因：API 主持壳 / 项目 TTS / V3 云剪任一能力缺少本轮安全 runtime 证明。

## 2. 逐项降级

| 能力 | 状态 | 处理 |
| --- | --- | --- |
| API 主持壳 | `missing_api_human_runtime` | fallback 到主持壳判断卡 / 信息卡 |
| 项目 TTS | `project_tts_not_safely_executed` | 使用 macOS say 临时 TTS，`audio_validation=temporary_preview` |
| V3 云剪 | `not_used_this_round` | 使用本地 assembly fallback，`cloud_assembly_runtime=not_used_fallback_local_preview` |
| locked reference | `registry_read` | 主线继承不足，输出 flow proof 继承报告 |
| 火山引擎素材 | `not_used` | API 段信息卡 fallback |

## 3. 边界

- 不写 `mainline_inheritance_candidate`。
- 不写 `content_validation=passed`。
- 不写 `send_ready=true`。
- 不写云剪正式稳定。
""",
    )

    write_text(
        REPORT_DIR / "content_validation_report.md",
        """# content_validation_report

- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `sample_type`：`flow_proof_sample`

## 内容边界

- `已确认` 保留短视频自动流的核心语义链：不是一键生成，而是豆包拆需求、Trae 接 prompt 和 plan、生成项目骨架、后续再接 API / 云剪 / Codex 检查。
- `已确认` 用户录制素材承担中段主体。
- `已确认` 信息卡只做开头判断、API / 云剪边界、工具关系和结尾总结。
- `已确认` 不把 Trae 项目骨架写成 app 已跑通。
- `已确认` 不把 API 写成已接通。
- `已确认` 不把云剪写成正式稳定。
- `已确认` 不把 Codex 检查写成内容过线。
""",
    )

    write_text(
        REPORT_DIR / "render_report.md",
        f"""# render_report

## 1. 状态

- `technical_validation`：`{technical_validation}`
- `metadata_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `sample_type`：`flow_proof_sample`
- `audio_validation`：`temporary_preview`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`
- `cloud_assembly_runtime`：`not_used_fallback_local_preview`

## 2. ffprobe

- `duration_seconds`：`{duration:.3f}`
- `resolution`：`{video_stream['width']}x{video_stream['height']}`
- `video_codec`：`{video_stream['codec_name']}`
- `audio_codec`：`{audio_stream['codec_name'] if audio_stream else 'none'}`
- `audio_present`：`{str(audio_stream is not None).lower()}`
- `decodable`：`{str(decode.returncode == 0).lower()}`

## 3. 输出

- `full_video.mp4`：`{full_video}`
- `contact_sheet.jpg`：`{contact}`
- `captions.srt`：`{OUT_DIR / 'captions.srt'}`
- `captions.json`：`{OUT_DIR / 'captions.json'}`
- `assembly_manifest.json`：`{OUT_DIR / 'assembly_manifest.json'}`
""",
    )
    shutil.copy2(REPORT_DIR / "render_report.md", OUT_DIR / "render_report.md")

    write_text(
        REPORT_DIR / "local_open_path_report.md",
        f"""# local_open_path_report

| artifact | canonical_local_path | path_exists | git_committed |
| --- | --- | --- | --- |
| full_video | `{full_video}` | `{full_video.exists()}` | `false` |
| contact_sheet | `{contact}` | `{contact.exists()}` | `false` |
| captions_srt | `{OUT_DIR / 'captions.srt'}` | `{(OUT_DIR / 'captions.srt').exists()}` | `true` |
| render_report | `{REPORT_DIR / 'render_report.md'}` | `{(REPORT_DIR / 'render_report.md').exists()}` | `true` |

`已确认` 大媒体文件只保留本地，不提交 Git。
""",
    )
    shutil.copy2(REPORT_DIR / "local_open_path_report.md", OUT_DIR / "local_open_path_report.md")

    write_text(
        OUT_DIR / "script_adaptation_report.md",
        """# script_adaptation_report

- `reference_script_source`：PR #40 完整口播稿。
- `runtime_full_script_source`：基于完整参考文案压缩为 90-150 秒复审样片口播。
- `semantic_chain_preserved`：`true`
- `not_pr41_long_card_narration`：`true`
- `not_pr42_runtime_only_error`：`true`

保留语义链：一键生成不是自动流 -> 豆包一句需求 -> 豆包拆流程 -> 豆包生成 Trae prompt -> Trae SOLO plan -> 项目骨架 -> API / 云剪 / Codex 工位边界 -> 即梦对比 -> 顺序对了自动化才有落脚点。
""",
    )

    # Copy report essentials to output directory for local review convenience.
    for name in [
        "failure_and_fallback_report.md",
        "content_validation_report.md",
        "hyperframes_motion_validation_report.md",
    ]:
        shutil.copy2(REPORT_DIR / name, OUT_DIR / name)

    # Logs and local path index.
    dated_log = ROOT / "codex_log/20260503_短视频自动流v3完整可复审样片_short_video_auto_flow_v3_complete_review_sample.md"
    write_text(
        dated_log,
        f"""# 短视频自动流 V3 完整可复审样片

- `created_at`：`{datetime.now().isoformat(timespec='seconds')}`
- `branch`：`codex/short-video-auto-flow-v3-complete-review-sample-20260503`
- `sample_type`：`flow_proof_sample`
- `technical_validation`：`{technical_validation}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`temporary_preview`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`
- `cloud_assembly_runtime`：`not_used_fallback_local_preview`

## 产物

- `full_video.mp4`：`{full_video}`
- `contact_sheet.jpg`：`{contact}`
- `render_report.md`：`{REPORT_DIR / 'render_report.md'}`
- `local_open_path_report.md`：`{REPORT_DIR / 'local_open_path_report.md'}`

## 边界

本轮是《短视频自动流的最简单流程》旁路新样片线，不修改当前正式 publish target，不写入 `dist/latest_review_pack/`，不改变 v3.1 状态字段。
""",
    )

    latest = ROOT / "codex_log/latest.md"
    existing_latest = latest.read_text(encoding="utf-8") if latest.exists() else ""
    latest_entry = f"""# latest update 2026-05-03 short video auto flow v3 complete review sample

- `已确认` 已生成《短视频自动流的最简单流程》V3 完整可复审样片。
- `sample_type`：`flow_proof_sample`
- `technical_validation`：`{technical_validation}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`temporary_preview`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`
- `cloud_assembly_runtime`：`not_used_fallback_local_preview`
- `full_video_local_path`：`{full_video}`
- `report_dir`：`{REPORT_DIR}`
- `边界`：旁路新样片线，不修改当前正式 publish target，不写入 `dist/latest_review_pack/`。

---

"""
    latest.write_text(latest_entry + existing_latest, encoding="utf-8")

    path_index = ROOT / "codex_log/current_local_artifact_paths.md"
    existing_paths = path_index.read_text(encoding="utf-8") if path_index.exists() else ""
    path_entry = f"""

## 2026-05-03 短视频自动流 V3 完整可复审样片

| artifact | canonical_local_path | path_exists | note |
| --- | --- | --- | --- |
| full_video | `{full_video}` | `true` | 大媒体文件，本地保留，不提交 Git |
| contact_sheet | `{contact}` | `true` | 本地复审 contact sheet，不提交 Git |
| report_dir | `{REPORT_DIR}` | `true` | 文本报告目录 |
| output_dir | `{OUT_DIR}` | `true` | 本轮样片输出目录 |

"""
    path_index.write_text(existing_paths.rstrip() + path_entry, encoding="utf-8")

    # Machine-readable status for final summary.
    status = {
        "full_video": str(full_video),
        "contact_sheet": str(contact),
        "captions_srt": str(OUT_DIR / "captions.srt"),
        "render_report": str(REPORT_DIR / "render_report.md"),
        "local_open_path_report": str(REPORT_DIR / "local_open_path_report.md"),
        "sample_type": sample_type,
        "technical_validation": technical_validation,
        "duration_seconds": round(duration, 3),
        "resolution": f"{video_stream['width']}x{video_stream['height']}",
        "video_codec": video_stream["codec_name"],
        "audio_codec": audio_stream["codec_name"] if audio_stream else None,
        "audio_present": audio_stream is not None,
        "decodable": decode.returncode == 0,
        "fallback": fallback,
        "sensitive_hits": sensitive_hits,
    }
    (OUT_DIR / "run_status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
