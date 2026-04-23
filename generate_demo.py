from __future__ import annotations

import argparse
import json
import math
import pathlib
import re
import shutil
import subprocess
import tempfile
import unicodedata
import wave
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parent
CASE_PATH = ROOT / "cases" / "demo.md"
DIST_DIR = ROOT / "dist" / "demo"
NO_ZOOM_VALIDATION_DIR = ROOT / "dist" / "20260424_不放大完整可读_no_zoom_completeness"
GAP_SECONDS = 0.25
TARGET_SECONDS = 15.0
VOICE_NAME = "Tingting"
VOICE_RATES = [220, 240, 265, 280, 300]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 1920
CARD_MARGIN_X = 96
CARD_Y = 320
CARD_HEIGHT = CANVAS_HEIGHT - 760
CARD_PADDING_X = 64
CARD_PADDING_TOP = 160
CARD_PADDING_BOTTOM = 96
BODY_TEXT_WIDTH = CANVAS_WIDTH - (CARD_MARGIN_X * 2) - (CARD_PADDING_X * 2)
BODY_AVAILABLE_HEIGHT = CARD_HEIGHT - CARD_PADDING_TOP - CARD_PADDING_BOTTOM
MIN_READABLE_BODY_FONT_SIZE = 34
LEAD_BODY_FONT_SIZE = 42
DEFAULT_BODY_FONT_SIZE = 38
BODY_LINE_HEIGHT_RATIO = 1.34
LAYOUT_METRICS_FILENAME = "布局指标_layout_metrics.json"
REVIEW_DIR_NAME = "1x默认视图_review_frames"


def parse_case_markdown(path: pathlib.Path) -> dict[str, Any]:
    """Parse the fixed markdown input into a small structured dictionary."""
    raw_sections: dict[str, list[str]] = {}
    current_heading: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            current_heading = line[2:].strip()
            raw_sections[current_heading] = []
            continue
        if line.startswith("## "):
            current_heading = line[3:].strip()
            raw_sections[current_heading] = []
            continue
        if current_heading is not None:
            raw_sections[current_heading].append(line)

    def section_text(name: str) -> str:
        lines = [line.strip() for line in raw_sections.get(name, []) if line.strip()]
        return "\n".join(lines)

    video_params: dict[str, str] = {}
    for line in raw_sections.get("视频参数", []):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        key, value = stripped[2:].split("：", 1)
        video_params[key.strip()] = value.strip()

    return {
        "title": section_text("标题"),
        "video_params": video_params,
        "target_user": section_text("目标用户"),
        "original_problem": section_text("原始问题"),
        "key_action": section_text("关键动作"),
        "before_after": [
            line.strip()
            for line in section_text("前后变化").splitlines()
            if line.strip()
        ],
        "result": section_text("结果"),
        "cta": section_text("CTA"),
    }


def simplify_problem(problem: str) -> str:
    """Compress the raw problem statement into natural narration."""
    if "说不清" in problem:
        return "想法很多，但目标和需求说不清"
    return problem.replace("导致项目推进很慢", "").strip("，。 ")


def spoken_result(result: str) -> str:
    """Make the result sentence sound a little more natural for TTS."""
    return result.replace("15分钟", "十五分钟")


def build_demo_plan(case: dict[str, Any]) -> dict[str, Any]:
    """Build a fixed three-slide PPT-style narration plan."""
    title = case["title"]
    target_user = case["target_user"]
    problem = simplify_problem(case["original_problem"])
    action = case["key_action"].rstrip("。")
    result = spoken_result(case["result"]).rstrip("。")
    before_after = case["before_after"]

    prefix = "很多 AI 项目" if "AI" in f"{title}{target_user}" else "很多这类项目"
    sentence_one = f"{prefix}卡住，不是没想法，而是{problem}。"
    sentence_two = f"{action}。"
    sentence_three = f"结果是{result}。"

    slides = [
        {
            "title": title,
            "body": f"目标用户：{target_user}\n当前问题：{problem}",
            "accent": "#2563EB",
            "background": "#F5F7FB",
            "badge": "demo案例",
            "footer": "AI配音 / demo案例",
        },
        {
            "title": "关键动作",
            "body": action,
            "accent": "#0F766E",
            "background": "#F4FBF9",
            "badge": "PPT讲解",
            "footer": "AI配音 / demo案例",
        },
        {
            "title": "结果变化",
            "body": "\n".join(
                [
                    before_after[0] if before_after else "",
                    before_after[1] if len(before_after) > 1 else "",
                    case["result"],
                ]
            ).strip(),
            "accent": "#7C3AED",
            "background": "#F8F5FF",
            "badge": "结果页",
            "footer": "AI配音 / demo案例",
        },
    ]

    captions = [{"text": text} for text in [sentence_one, sentence_two, sentence_three]]
    script = "\n".join(
        [
            f"第1页：{sentence_one}",
            f"第2页：{sentence_two}",
            f"第3页：{sentence_three}",
        ]
    )

    slides, layout_metrics = enforce_no_zoom_completeness(slides)

    return {
        "slides": slides,
        "captions": captions,
        "script": script,
        "narration": [sentence_one, sentence_two, sentence_three],
        "layout_metrics": layout_metrics,
    }


def text_display_units(text: str) -> float:
    """Estimate rendered text width without depending on platform font APIs."""
    units = 0.0
    for character in text:
        if character == "\n":
            continue
        if unicodedata.east_asian_width(character) in {"F", "W"}:
            units += 2.0
        elif character.isspace():
            units += 0.7
        else:
            units += 1.0
    return units


def wrapped_line_count(text: str, font_size: int, max_width: int = BODY_TEXT_WIDTH) -> int:
    """Return a conservative 1x line count for no-zoom layout checks."""
    units_per_line = max(1, int(max_width / (font_size * 0.54)))
    return max(1, math.ceil(text_display_units(text) / units_per_line))


def body_item_height(text: str, item_index: int, font_size: int | None = None) -> int:
    """Estimate the actual height a body item needs after wrapping."""
    resolved_font_size = font_size or (LEAD_BODY_FONT_SIZE if item_index == 0 else DEFAULT_BODY_FONT_SIZE)
    line_count = wrapped_line_count(text, resolved_font_size)
    single_line_height = 120 if item_index == 0 else 96
    if line_count == 1:
        return single_line_height
    return math.ceil(line_count * resolved_font_size * BODY_LINE_HEIGHT_RATIO) + 36


def body_height_for_lines(lines: list[str]) -> int:
    """Estimate body stack height using the same first-line emphasis as the renderer."""
    return sum(body_item_height(line, index) for index, line in enumerate(lines))


def sentence_units(text: str) -> list[str]:
    """Split a long logical line into sentence-like complete units."""
    pieces = [piece.strip() for piece in re.split(r"(?<=[。！？；;.!?])", text) if piece.strip()]
    if pieces:
        return pieces
    return [text]


def split_overlong_unit(text: str, available_height: int) -> list[str]:
    """Split one item only when a single logical unit cannot fit at readable size."""
    pieces = sentence_units(text)
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        candidate = f"{current}{piece}" if current else piece
        if body_item_height(candidate, 0, MIN_READABLE_BODY_FONT_SIZE) <= available_height:
            current = candidate
            continue
        if current:
            chunks.append(current)
            current = piece
        else:
            chunks.append(piece)
            current = ""
    if current:
        chunks.append(current)
    return chunks or [text]


def split_body_lines_for_safe_area(lines: list[str]) -> list[list[str]]:
    """Split body text before rendering so every shot is complete at 1x."""
    chunks: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        candidates = [line]
        if body_item_height(line, 0, MIN_READABLE_BODY_FONT_SIZE) > BODY_AVAILABLE_HEIGHT:
            candidates = split_overlong_unit(line, BODY_AVAILABLE_HEIGHT)

        for candidate in candidates:
            next_chunk = [*current, candidate]
            if current and body_height_for_lines(next_chunk) > BODY_AVAILABLE_HEIGHT:
                chunks.append(current)
                current = [candidate]
            else:
                current = next_chunk

    if current:
        chunks.append(current)
    return chunks or [[]]


def slide_title_with_part(title: str, part_index: int, split_count: int) -> str:
    """Keep each split shot self-contained without relying on zoom or hidden context."""
    if split_count <= 1:
        return title
    cleaned_title = re.sub(r"[（(](上半|下半|\d+/\d+)[）)]", "", title).strip()
    return f"{cleaned_title}（{part_index}/{split_count}）"


def layout_metrics_for_slide(
    slide: dict[str, Any],
    body_lines: list[str],
    *,
    source_slide_index: int,
    split_required: bool,
    split_count: int,
) -> dict[str, Any]:
    """Build the persisted no_zoom_completeness layout record."""
    text_total_height = 56 + 180 + body_height_for_lines(body_lines) + 86 + 96
    safe_area_available_height = BODY_AVAILABLE_HEIGHT
    overflow = body_height_for_lines(body_lines) > safe_area_available_height
    return {
        "source_slide_index": source_slide_index,
        "canvas_size": {"width": CANVAS_WIDTH, "height": CANVAS_HEIGHT},
        "safe_area": {
            "x": CARD_MARGIN_X + CARD_PADDING_X,
            "y": CARD_Y + CARD_PADDING_BOTTOM,
            "width": BODY_TEXT_WIDTH,
            "height": BODY_AVAILABLE_HEIGHT,
        },
        "title_bbox": {"x": 96, "y": CANVAS_HEIGHT - 460, "width": CANVAS_WIDTH - 192, "height": 180},
        "body_bbox": {
            "x": CARD_MARGIN_X + CARD_PADDING_X,
            "y": CARD_Y + CARD_PADDING_BOTTOM,
            "width": BODY_TEXT_WIDTH,
            "height": body_height_for_lines(body_lines),
        },
        "footer_bbox": {"x": 96, "y": 150, "width": CANVAS_WIDTH - 192, "height": 86},
        "text_total_height": text_total_height,
        "safe_area_available_height": safe_area_available_height,
        "overflow": overflow,
        "split_required": split_required,
        "split_count": split_count,
        "min_readable_body_font_size": MIN_READABLE_BODY_FONT_SIZE,
        "zoom_used_for_completeness": False,
        "title": slide["title"],
        "badge": slide["badge"],
        "footer": slide["footer"],
    }


def enforce_no_zoom_completeness(slides: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Ensure every slide can show its full body in the default 1x view."""
    rendered_slides: list[dict[str, Any]] = []
    layout_metrics: list[dict[str, Any]] = []

    for source_index, slide in enumerate(slides):
        body_lines = [line.strip() for line in slide["body"].splitlines() if line.strip()]
        body_chunks = split_body_lines_for_safe_area(body_lines)
        split_count = len(body_chunks)
        split_required = split_count > 1

        for part_index, chunk in enumerate(body_chunks, start=1):
            split_slide = {
                **slide,
                "title": slide_title_with_part(slide["title"], part_index, split_count),
                "body": "\n".join(chunk),
                "source_slide_index": source_index,
                "split_part_index": part_index,
                "split_count": split_count,
            }
            metrics = layout_metrics_for_slide(
                split_slide,
                chunk,
                source_slide_index=source_index,
                split_required=split_required,
                split_count=split_count,
            )
            split_slide["no_zoom_layout_metrics"] = metrics
            rendered_slides.append(split_slide)
            layout_metrics.append(metrics)

    return rendered_slides, layout_metrics


def build_no_zoom_validation_plan() -> dict[str, Any]:
    """Build a tall screenshot-like block that must split before rendering."""
    slide = {
        "title": "当前在看：完整承接路径",
        "body": "\n".join(
            [
                "先交代这拍在验证什么：不是继续压缩文案，而是检查默认视图能不能完整承接。",
                "第一层信息：用户原始输入要先被拆成目标、边界、步骤和交付物，不能只给半截。",
                "第二层信息：正确做法标签必须跟主体正文同时出现，不能只剩标签还看不到证据。",
                "第三层信息：完整承接路径要说明从输入到工作包正文，再到录制计划和回审清单。",
                "第四层信息：如果正文高度超过安全显示区，必须先拆成多拍，再进入渲染。",
                "第五层信息：每一拍都要保留完整标题和上下文，不能只留下上半或下半的残片。",
                "第六层信息：zoom 只能让字更舒服，不能用来补救默认视图里已经被裁掉的信息。",
                "第七层信息：标题、标签、正文、底部说明都要参与高度计算，装饰层也不能遮挡。",
                "第八层信息：技术生成成功不等于内容完整可读，两种 validation 必须分开记录。",
                "最终判断：1x 默认视图完整显示才算本拍通过，否则只能进入人工复审或继续拆拍。",
            ]
        ),
        "accent": "#0F766E",
        "background": "#F4FBF9",
        "badge": "正确做法",
        "footer": "这块信息太高时，必须拆两拍才能保证完整可读",
    }
    slides, layout_metrics = enforce_no_zoom_completeness([slide])
    return {
        "slides": slides,
        "captions": [],
        "script": "",
        "narration": [],
        "layout_metrics": layout_metrics,
    }


def ensure_tools_exist() -> None:
    """Fail early with a clear message if a required macOS tool is missing."""
    for tool_name in ["say", "afconvert", "swift"]:
        if shutil.which(tool_name) is None:
            raise RuntimeError(f"缺少系统命令：{tool_name}")


def run_command(args: list[str]) -> None:
    """Run a command and surface stderr directly if it fails."""
    subprocess.run(args, check=True)


def resolve_ffmpeg() -> str:
    """Resolve an ffmpeg binary from PATH or the local npm dependency."""
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg

    bundled_ffmpeg = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled_ffmpeg.exists():
        return str(bundled_ffmpeg)

    raise RuntimeError("缺少 ffmpeg，可通过 npm install 安装本项目依赖后再运行。")


def wav_duration_seconds(path: pathlib.Path) -> float:
    """Read the duration from a PCM wave file."""
    with wave.open(str(path), "rb") as handle:
        return handle.getnframes() / float(handle.getframerate())


def synthesize_segments(
    narration: list[str],
    rate: int,
    workdir: pathlib.Path,
) -> list[pathlib.Path]:
    """Generate one AIFF and one WAV per sentence for timing control."""
    wav_paths: list[pathlib.Path] = []

    for index, text in enumerate(narration, start=1):
        aiff_path = workdir / f"segment_{index}.aiff"
        wav_path = workdir / f"segment_{index}.wav"
        run_command(["say", "-v", VOICE_NAME, "-r", str(rate), text, "-o", str(aiff_path)])
        run_command(
            [
                "afconvert",
                "-f",
                "WAVE",
                "-d",
                "LEI16@22050",
                str(aiff_path),
                str(wav_path),
            ]
        )
        wav_paths.append(wav_path)

    return wav_paths


def pick_best_voice_rate(narration: list[str], workdir: pathlib.Path) -> tuple[int, list[pathlib.Path], list[float]]:
    """Pick the speaking rate whose total duration lands closest to 15 seconds."""
    best_rate = VOICE_RATES[0]
    best_paths: list[pathlib.Path] = []
    best_durations: list[float] = []
    best_distance = math.inf

    for rate in VOICE_RATES:
        rate_dir = workdir / f"rate_{rate}"
        rate_dir.mkdir(parents=True, exist_ok=True)
        wav_paths = synthesize_segments(narration, rate, rate_dir)
        durations = [wav_duration_seconds(path) for path in wav_paths]
        total_duration = sum(durations) + GAP_SECONDS * (len(durations) - 1)
        distance = abs(total_duration - TARGET_SECONDS)

        if distance < best_distance:
            best_rate = rate
            best_paths = wav_paths
            best_durations = durations
            best_distance = distance

    return best_rate, best_paths, best_durations


def concatenate_wavs(input_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    """Concatenate WAV files with short silence gaps between sentences."""
    if not input_paths:
        raise RuntimeError("没有可拼接的音频片段")

    with wave.open(str(input_paths[0]), "rb") as first_input:
        params = first_input.getparams()
        silence_frame_count = int(params.framerate * GAP_SECONDS)
        silence = b"\x00" * silence_frame_count * params.sampwidth * params.nchannels

    with wave.open(str(output_path), "wb") as output:
        output.setparams(params)
        for index, path in enumerate(input_paths):
            with wave.open(str(path), "rb") as current:
                output.writeframes(current.readframes(current.getnframes()))
            if index < len(input_paths) - 1:
                output.writeframes(silence)


def build_voice(narration: list[str], output_dir: pathlib.Path) -> dict[str, Any]:
    """Generate a final MP3 voice track and precise segment timings."""
    ensure_tools_exist()
    ffmpeg_path = resolve_ffmpeg()
    with tempfile.TemporaryDirectory(prefix="demo_voice_") as temp_dir:
        temp_root = pathlib.Path(temp_dir)
        rate, wav_paths, segment_durations = pick_best_voice_rate(narration, temp_root)
        wav_output = output_dir / "voice.wav"
        mp3_output = output_dir / "voice.mp3"
        concatenate_wavs(wav_paths, wav_output)
        run_command(
            [
                ffmpeg_path,
                "-y",
                "-i",
                str(wav_output),
                "-codec:a",
                "libmp3lame",
                "-b:a",
                "128k",
                str(mp3_output),
            ]
        )
        total_duration = wav_duration_seconds(wav_output)

    return {
        "rate": rate,
        "segment_durations": segment_durations,
        "total_duration": total_duration,
        "wav_path": wav_output,
        "mp3_path": mp3_output,
    }


def seconds_to_srt(value: float) -> str:
    """Format seconds as an SRT timestamp."""
    milliseconds = round(value * 1000)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def write_script_and_captions(
    plan: dict[str, Any],
    voice_info: dict[str, Any],
    output_dir: pathlib.Path,
) -> list[dict[str, Any]]:
    """Write script.txt and captions.srt based on measured audio timing."""
    (output_dir / "script.txt").write_text(plan["script"], encoding="utf-8")

    current = 0.0
    caption_rows: list[str] = []
    caption_entries: list[dict[str, Any]] = []
    durations = voice_info["segment_durations"]

    for index, (caption, duration) in enumerate(zip(plan["captions"], durations), start=1):
        start = current
        end = start + duration
        caption_entries.append(
            {
                "text": caption["text"],
                "start": start,
                "end": end,
                "slide_duration": duration + (GAP_SECONDS if index < len(durations) else 0.0),
            }
        )
        caption_rows.extend(
            [
                str(index),
                f"{seconds_to_srt(start)} --> {seconds_to_srt(end)}",
                caption["text"],
                "",
            ]
        )
        current = end + (GAP_SECONDS if index < len(durations) else 0.0)

    (output_dir / "captions.srt").write_text("\n".join(caption_rows).strip() + "\n", encoding="utf-8")
    return caption_entries


def write_manifest(
    plan: dict[str, Any],
    caption_entries: list[dict[str, Any]],
    voice_info: dict[str, Any],
    output_dir: pathlib.Path,
) -> pathlib.Path:
    """Write the slide manifest consumed by the Swift video builder."""
    slides = []
    caption_durations = {
        index: caption["slide_duration"]
        for index, caption in enumerate(caption_entries)
    }
    split_counts: dict[int, int] = {}
    for slide in plan["slides"]:
        source_index = int(slide.get("source_slide_index", len(split_counts)))
        split_counts[source_index] = max(split_counts.get(source_index, 0), int(slide.get("split_count", 1)))

    for slide_index, slide in enumerate(plan["slides"]):
        source_index = int(slide.get("source_slide_index", slide_index))
        total_duration = caption_durations.get(source_index, 2.0)
        split_count = max(1, split_counts.get(source_index, 1))
        slides.append({**slide, "duration": total_duration / split_count})

    review_dir = output_dir / "local_review" / REVIEW_DIR_NAME
    metrics_path = output_dir / LAYOUT_METRICS_FILENAME
    metrics_path.write_text(
        json.dumps({"layout_metrics": plan.get("layout_metrics", [])}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    manifest = {
        "width": CANVAS_WIDTH,
        "height": CANVAS_HEIGHT,
        "fps": 10,
        "audioPath": str((output_dir / "voice.mp3").resolve()),
        "outputPath": str((output_dir / "final.mp4").resolve()),
        "reviewImageDir": str(review_dir.resolve()),
        "slides": slides,
        "totalDuration": voice_info["total_duration"],
        "layoutMetricsPath": str(metrics_path.resolve()),
    }
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest_path


def write_review_only_manifest(plan: dict[str, Any], output_dir: pathlib.Path) -> pathlib.Path:
    """Write a manifest that asks Swift to emit 1x review frames only."""
    review_dir = output_dir / REVIEW_DIR_NAME
    metrics_path = output_dir / LAYOUT_METRICS_FILENAME
    metrics_path.write_text(
        json.dumps({"layout_metrics": plan.get("layout_metrics", [])}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    slides = []
    for slide in plan["slides"]:
        slides.append({**slide, "duration": 2.0})

    manifest = {
        "width": CANVAS_WIDTH,
        "height": CANVAS_HEIGHT,
        "fps": 10,
        "audioPath": "",
        "outputPath": str((output_dir / "review_only.mp4").resolve()),
        "reviewImageDir": str(review_dir.resolve()),
        "reviewOnly": True,
        "slides": slides,
        "totalDuration": len(slides) * 2.0,
        "layoutMetricsPath": str(metrics_path.resolve()),
    }
    manifest_path = output_dir / "验证清单_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest_path


def build_video(manifest_path: pathlib.Path) -> bool:
    """Attempt to render final.mp4 via the bundled Swift AVFoundation helper."""
    swift_path = ROOT / "video_builder.swift"
    if not swift_path.exists():
        return False

    try:
        run_command(["swift", str(swift_path), str(manifest_path)])
    except subprocess.CalledProcessError:
        return False

    return (DIST_DIR / "final.mp4").exists()


def build_review_frames(manifest_path: pathlib.Path) -> bool:
    """Render review-only 1x frames for the no-zoom validation fixture."""
    swift_path = ROOT / "video_builder.swift"
    if not swift_path.exists():
        return False

    try:
        run_command(["swift", str(swift_path), str(manifest_path)])
    except subprocess.CalledProcessError:
        return False

    return (manifest_path.parent / REVIEW_DIR_NAME).exists()


def generate_no_zoom_validation_fixture() -> None:
    """Generate the minimum human-reviewable no_zoom_completeness artifact set."""
    NO_ZOOM_VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    plan = build_no_zoom_validation_plan()
    manifest_path = write_review_only_manifest(plan, NO_ZOOM_VALIDATION_DIR)
    if not build_review_frames(manifest_path):
        raise RuntimeError("未能生成 no_zoom_completeness 1x review 图")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--layout-fixture",
        action="store_true",
        help="只生成 no_zoom_completeness 的 1x review 图和 layout_metrics，不跑配音。",
    )
    args = parser.parse_args()

    if args.layout_fixture:
        generate_no_zoom_validation_fixture()
        return

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    case = parse_case_markdown(CASE_PATH)
    plan = build_demo_plan(case)
    voice_info = build_voice(plan["narration"], DIST_DIR)
    caption_entries = write_script_and_captions(plan, voice_info, DIST_DIR)
    manifest_path = write_manifest(plan, caption_entries, voice_info, DIST_DIR)
    if build_video(manifest_path):
        pathlib.Path(voice_info["wav_path"]).unlink(missing_ok=True)
        manifest_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
