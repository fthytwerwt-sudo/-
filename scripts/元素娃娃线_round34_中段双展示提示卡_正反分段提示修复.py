from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Sequence

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
PUBLIC_REPO_ROOT = pathlib.Path("/Users/fan/Documents/视频工厂")


def _load_module(module_name: str, script_name: str):
    module_path = ROOT / "scripts" / script_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = _load_module("video_full_border_jump_audit_round34", "视频全片边框与跳切审计.py")

DIST_DIR = ROOT / "dist" / "20260417_豆包的正确打开方式_vnext"
ROUND31_NAME = "round31_一镜到底录屏证据链重构"
ROUND32_NAME = "round33_正反展示提示卡补齐与风格统一"
ROUND34_NAME = "round34_中段双展示提示卡_正反分段提示修复"

ROUND31_DIR = DIST_DIR / ROUND31_NAME
ROUND32_DIR = DIST_DIR / ROUND32_NAME
ROUND34_DIR = DIST_DIR / ROUND34_NAME
INPUTS_DIR = ROUND34_DIR / "inputs"
RENDERS_DIR = ROUND34_DIR / "renders"
AUDIT_DIR = ROUND34_DIR / "audit"
PROBLEM_DIR = AUDIT_DIR / "problem_windows"
LATEST_REVIEW_PACK_DIR = ROOT / "dist" / "latest_review_pack"

ROUND31_FULL = ROUND31_DIR / "renders" / "主持壳正式正片_round31_一镜到底录屏证据链重构.mp4"
ROUND32_FULL = ROUND32_DIR / "renders" / "主持壳正式正片_round33_正反展示提示卡补齐与风格统一.mp4"
ROUND32_MIDDLE_PREVIEW = ROUND32_DIR / "renders" / "中段preview_round33_正反提示卡补齐与风格统一.mp4"

ROUND34_FULL = RENDERS_DIR / "主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4"
ROUND34_MIDDLE_PREVIEW = RENDERS_DIR / "中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4"
ROUND34_BEFORE_AFTER = AUDIT_DIR / "round33_vs_round34_中段提示卡_before_after.mp4"
ROUND34_CUT_SHEET = AUDIT_DIR / "cut_contact_sheet.jpg"
ROUND34_BORDER_SHEET = AUDIT_DIR / "border_residue_contact_sheet.jpg"
ROUND34_JUMP_SHEET = AUDIT_DIR / "jump_cut_contact_sheet.jpg"
ROUND34_BORDER_REPORT = AUDIT_DIR / "full_border_residue_report.md"
ROUND34_JUMP_REPORT = AUDIT_DIR / "full_jump_cut_report.md"
ROUND34_AUDIT_MD = AUDIT_DIR / "round34_中段双展示提示卡_正反分段提示修复_audit.md"
ROUND34_SUMMARY = AUDIT_DIR / "summary.json"
ROUND34_PLAN = INPUTS_DIR / "01_round34_card_style_plan.json"
ROUND34_TIMELINE = INPUTS_DIR / "timeline.json"
ROUND34_CUT_MAP = INPUTS_DIR / "cut_map.md"
ROUND34_REVIEW_MANIFEST = INPUTS_DIR / "review_manifest.md"

NEGATIVE_CARD_FRAME = AUDIT_DIR / "反面展示提示卡_单帧.png"
POSITIVE_CARD_FRAME = AUDIT_DIR / "正面展示提示卡_单帧.png"
CARD_PAIR_FRAME = AUDIT_DIR / "正反提示卡_并排对比.png"
ROUND34_PROBLEM_30_32 = PROBLEM_DIR / "30_32s.mp4"
ROUND34_PROBLEM_30_32_FRAMES = PROBLEM_DIR / "30_32s_frames.jpg"
ROUND34_PROBLEM_30_40 = PROBLEM_DIR / "30_40s.mp4"
REFERENCE_IMAGE_SOURCE = pathlib.Path("/Users/fan/Desktop/截屏2026-04-25 18.11.07.png")
REFERENCE_IMAGE_COPY = INPUTS_DIR / "图二参考图.png"
REFERENCE_IMAGE_META: dict[str, Any] = {}

TARGET_WIDTH = 720
TARGET_HEIGHT = 1280
FPS = 25.0
CARD_SECONDS = 1.6
BASE_CROSSFADE_SECONDS = 0.16
PRIMARY_CROSSFADE_SECONDS = 0.22

ALI_API_CALLED = False
HOST_AVATAR_REGENERATED = False
RAW_RECORDINGS_MODIFIED = False
HOST_SHELL_REBUILT = False
JUDGMENT_CARD_REBUILT = False
PROMPT_TAIL_REBUILT = False
MIDDLE_EVIDENCE_RECORDINGS_TRIMMED = False
NEW_EXPLANATION_CARDS_ADDED = False
POSITIVE_PROMPT_CARD_ADDED = True

CARD_STYLE_TOKENS = {
    "canvas_size": "720x1280",
    "background_top": "#FFE0EF",
    "background_bottom": "#FFF8FC",
    "panel_fill": "#FFF7FB",
    "panel_border": "#EFA3C4",
    "title_fill": "#FFF7FB",
    "title_stroke": "#D86693",
    "subtitle_fill": "#8D4869",
    "shadow": "#C95E8A",
    "petal": "#F6AFC9",
    "branch": "#B97885",
    "highlight": "#FFFFFF",
}

CARD_COPY = {
    "negative": {
        "title": "《反面展示》",
        "subtitle": "先看旧做法：一句糊话，结果怎么变泛",
    },
    "positive": {
        "title": "《正面展示》",
        "subtitle": "再看工作包后：结果怎么一步步落成",
    },
}


def round3(value: float) -> float:
    return round(value, 3)


def public_path(path: pathlib.Path) -> str:
    try:
        return str(PUBLIC_REPO_ROOT / path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def ensure_dirs() -> None:
    for directory in (ROUND34_DIR, INPUTS_DIR, RENDERS_DIR, AUDIT_DIR, PROBLEM_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def ensure_reference_image() -> None:
    if not REFERENCE_IMAGE_SOURCE.exists() or REFERENCE_IMAGE_SOURCE.stat().st_size == 0:
        raise RuntimeError(f"blocked_missing_reference_image: {REFERENCE_IMAGE_SOURCE}")
    with Image.open(REFERENCE_IMAGE_SOURCE) as image:
        width, height = image.size
    if width <= 0 or height <= 0:
        raise RuntimeError(f"blocked_unreadable_reference_image: {REFERENCE_IMAGE_SOURCE}")
    REFERENCE_IMAGE_COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REFERENCE_IMAGE_SOURCE, REFERENCE_IMAGE_COPY)
    REFERENCE_IMAGE_META.clear()
    REFERENCE_IMAGE_META.update(
        {
            "source": str(REFERENCE_IMAGE_SOURCE),
            "copied_to": public_path(REFERENCE_IMAGE_COPY),
            "width": width,
            "height": height,
            "status": "已确认：图二参考图可读取，作为粉色樱花柔和展示牌风格参考。",
        }
    )


def run_ffmpeg(args: Sequence[str]) -> None:
    subprocess.run([AUDIT.resolve_ffmpeg(), "-hide_banner", "-loglevel", "error", *args], check=True)


def require_source_files() -> None:
    required = [ROUND31_FULL, ROUND32_FULL, ROUND32_MIDDLE_PREVIEW]
    missing = [path for path in required if not path.exists() or path.stat().st_size == 0]
    if missing:
        raise RuntimeError("blocked_missing_round33_or_round31_sources: " + " | ".join(str(path) for path in missing))


def round31_source_duration() -> float:
    return AUDIT.read_media_duration_seconds(ROUND31_FULL)


def _hex_to_rgb(hex_value: str) -> tuple[int, int, int]:
    value = hex_value.lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))  # type: ignore[return-value]


def load_card_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        ("/System/Library/Fonts/Hiragino Sans GB.ttc", 2 if bold else 0),
        ("/System/Library/Fonts/STHeiti Medium.ttc", 1),
        ("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 0),
    ]
    for candidate, index in candidates:
        try:
            return ImageFont.truetype(candidate, size=size, index=index)
        except Exception:
            continue
    return AUDIT.load_font(size, bold=bold)


def fit_card_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    start_size: int,
    *,
    min_size: int,
    bold: bool = False,
    stroke_width: int = 0,
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for size in range(start_size, min_size - 1, -2):
        font = load_card_font(size, bold=bold)
        bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
        if bbox[2] - bbox[0] <= max_width:
            return font
    return load_card_font(min_size, bold=bold)


def _gradient_background() -> Image.Image:
    top = _hex_to_rgb(CARD_STYLE_TOKENS["background_top"])
    bottom = _hex_to_rgb(CARD_STYLE_TOKENS["background_bottom"])
    image = Image.new("RGB", (TARGET_WIDTH, TARGET_HEIGHT))
    pixels = image.load()
    for y in range(TARGET_HEIGHT):
        ratio = y / max(1, TARGET_HEIGHT - 1)
        color = tuple(int(top[channel] * (1 - ratio) + bottom[channel] * ratio) for channel in range(3))
        for x in range(TARGET_WIDTH):
            pixels[x, y] = color
    return image


def _draw_soft_highlight(canvas: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int, int]) -> None:
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius // 2))
    canvas.alpha_composite(overlay)


def _draw_petal(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float, angle: float, fill: tuple[int, int, int]) -> None:
    length = int(26 * scale)
    width = int(13 * scale)
    points: list[tuple[int, int]] = []
    for idx in range(20):
        theta = 2 * math.pi * idx / 20
        px = math.cos(theta) * width
        py = math.sin(theta) * length
        rotated_x = px * math.cos(angle) - py * math.sin(angle)
        rotated_y = px * math.sin(angle) + py * math.cos(angle)
        points.append((int(x + rotated_x), int(y + rotated_y)))
    draw.polygon(points, fill=fill)
    draw.line((x, y, int(x + math.sin(angle) * length * 0.45), int(y - math.cos(angle) * length * 0.45)), fill=(238, 136, 172), width=max(1, int(scale * 2)))


def _draw_branch(draw: ImageDraw.ImageDraw, start: tuple[int, int], direction: int) -> None:
    branch = _hex_to_rgb(CARD_STYLE_TOKENS["branch"])
    x0, y0 = start
    points = []
    for step in range(7):
        x = x0 + direction * step * 30
        y = y0 + int(math.sin(step / 1.4) * 22) + step * 14
        points.append((x, y))
    draw.line(points, fill=branch, width=4, joint="curve")
    petal = _hex_to_rgb(CARD_STYLE_TOKENS["petal"])
    for idx, (x, y) in enumerate(points[1:-1], start=1):
        _draw_petal(draw, x + direction * 16, y - 12, 0.7, direction * 0.6 + idx * 0.15, petal)
        if idx % 2:
            _draw_petal(draw, x - direction * 10, y + 10, 0.55, direction * -0.8, (255, 205, 222))


def _draw_lace_border(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int) -> None:
    x0, y0, x1, y1 = box
    border = _hex_to_rgb(CARD_STYLE_TOKENS["panel_border"])
    lace_fill = (255, 237, 246)
    draw.rounded_rectangle(box, radius=radius, fill=_hex_to_rgb(CARD_STYLE_TOKENS["panel_fill"]), outline=border, width=4)
    inset = 18
    draw.rounded_rectangle((x0 + inset, y0 + inset, x1 - inset, y1 - inset), radius=radius - 10, outline=(248, 197, 216), width=2)
    for x in range(x0 + 42, x1 - 42, 30):
        draw.ellipse((x - 8, y0 + 16, x + 8, y0 + 32), fill=lace_fill, outline=(248, 197, 216), width=1)
        draw.ellipse((x - 8, y1 - 32, x + 8, y1 - 16), fill=lace_fill, outline=(248, 197, 216), width=1)
    for y in range(y0 + 52, y1 - 52, 34):
        draw.ellipse((x0 + 16, y - 8, x0 + 32, y + 8), fill=lace_fill, outline=(248, 197, 216), width=1)
        draw.ellipse((x1 - 32, y - 8, x1 - 16, y + 8), fill=lace_fill, outline=(248, 197, 216), width=1)


def _draw_bow(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float) -> None:
    x, y = center
    fill = (249, 168, 199)
    outline = (208, 100, 140)
    w = int(62 * scale)
    h = int(42 * scale)
    draw.ellipse((x - w - 8, y - h, x - 8, y + h), fill=fill, outline=outline, width=2)
    draw.ellipse((x + 8, y - h, x + w + 8, y + h), fill=fill, outline=outline, width=2)
    draw.rounded_rectangle((x - 15, y - 17, x + 15, y + 17), radius=8, fill=(255, 221, 234), outline=outline, width=2)
    draw.line((x - w + 10, y - 8, x - 18, y), fill=(255, 231, 240), width=3)
    draw.line((x + 18, y, x + w - 10, y - 8), fill=(255, 231, 240), width=3)


def create_prompt_card_image(kind: str, output_path: pathlib.Path) -> None:
    copy = CARD_COPY[kind]
    canvas = _gradient_background().convert("RGBA")
    _draw_soft_highlight(canvas, (210, 220), 190, (255, 255, 255, 86))
    _draw_soft_highlight(canvas, (540, 900), 250, (255, 213, 234, 78))
    draw = ImageDraw.Draw(canvas)

    draw.rounded_rectangle((70, 40, 650, 360), radius=42, fill=(255, 255, 255, 50))
    for x in (118, 274, 430, 586):
        draw.line((x, 62, x, 336), fill=(255, 255, 255, 80), width=3)
    draw.rounded_rectangle((0, 1010, TARGET_WIDTH, 1280), radius=0, fill=(246, 210, 190, 48))

    for x, y, scale, angle in [
        (96, 160, 0.85, 0.7),
        (590, 170, 0.7, -0.5),
        (112, 1024, 0.65, -0.9),
        (612, 1040, 0.78, 0.8),
        (360, 226, 0.48, 0.2),
        (486, 1116, 0.46, -0.4),
        (196, 930, 0.45, 0.3),
        (532, 944, 0.42, -0.6),
    ]:
        _draw_petal(draw, x, y, scale, angle, _hex_to_rgb(CARD_STYLE_TOKENS["petal"]))

    _draw_branch(draw, (82, 132), 1)
    _draw_branch(draw, (646, 168), -1)

    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((86, 314, 650, 916), radius=58, fill=(192, 87, 126, 52))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas.alpha_composite(shadow)
    draw = ImageDraw.Draw(canvas)

    draw.rounded_rectangle((50, 84, 670, 1198), radius=58, outline=(250, 188, 214), width=3)
    _draw_lace_border(draw, (78, 288, 642, 904), 58)
    draw.line((528, 292, 640, 404), fill=(255, 237, 246), width=10)
    for offset in range(0, 132, 18):
        draw.arc((520 + offset // 3, 292 + offset, 650 + offset // 3, 422 + offset), 170, 250, fill=(248, 197, 216), width=2)
    _draw_bow(draw, (585, 314), 0.72)

    for x, y, radius in [(168, 338, 6), (552, 430, 5), (142, 824, 4), (578, 812, 6), (360, 950, 5), (310, 452, 4), (420, 458, 4)]:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(255, 255, 255, 190))

    title = copy["title"]
    title_font = fit_card_font(draw, title, 510, 86, min_size=64, bold=True, stroke_width=4)
    bbox = draw.textbbox((0, 0), title, font=title_font, stroke_width=4)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (TARGET_WIDTH - text_w) // 2
    y = 556 - text_h // 2
    draw.text((x + 4, y + 8), title, font=title_font, fill=(201, 94, 138, 90), stroke_width=4, stroke_fill=(201, 94, 138, 70))
    draw.text(
        (x, y),
        title,
        font=title_font,
        fill=_hex_to_rgb(CARD_STYLE_TOKENS["title_fill"]),
        stroke_width=4,
        stroke_fill=_hex_to_rgb(CARD_STYLE_TOKENS["title_stroke"]),
    )

    subtitle = copy["subtitle"]
    subtitle_font = fit_card_font(draw, subtitle, 520, 33, min_size=26, bold=False)
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_w = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_h = subtitle_bbox[3] - subtitle_bbox[1]
    subtitle_x = (TARGET_WIDTH - subtitle_w) // 2
    subtitle_y = 684
    draw.rounded_rectangle(
        (92, subtitle_y - 22, 628, subtitle_y + subtitle_h + 32),
        radius=28,
        fill=(255, 245, 250),
        outline=(246, 188, 213),
        width=2,
    )
    draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill=_hex_to_rgb(CARD_STYLE_TOKENS["subtitle_fill"]))

    draw.arc((178, 760, 542, 872), start=198, end=342, fill=(245, 176, 204), width=3)
    for x0 in (248, 304, 360, 416):
        _draw_petal(draw, x0, 830, 0.42, 0.1, (255, 204, 222))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output_path)


def create_card_pair_image(output_path: pathlib.Path) -> None:
    negative = Image.open(NEGATIVE_CARD_FRAME).convert("RGB").resize((360, 640), Image.Resampling.LANCZOS)
    positive = Image.open(POSITIVE_CARD_FRAME).convert("RGB").resize((360, 640), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (760, 720), (255, 243, 249))
    draw = ImageDraw.Draw(canvas)
    canvas.paste(negative, (20, 56))
    canvas.paste(positive, (380, 56))
    draw.text((28, 22), "round34 正反提示卡并排对比", font=load_card_font(28, bold=True), fill=(149, 70, 105))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=94)


def render_card_video(image_path: pathlib.Path, duration_seconds: float, output_path: pathlib.Path) -> None:
    run_ffmpeg(
        [
            "-y",
            "-loop",
            "1",
            "-t",
            f"{duration_seconds:.3f}",
            "-i",
            str(image_path),
            "-f",
            "lavfi",
            "-t",
            f"{duration_seconds:.3f}",
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=48000",
            "-vf",
            f"scale={TARGET_WIDTH}:{TARGET_HEIGHT},setsar=1,format=yuv420p",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(output_path),
        ]
    )


def card_video_paths(temp_dir: pathlib.Path) -> dict[str, pathlib.Path]:
    create_prompt_card_image("negative", NEGATIVE_CARD_FRAME)
    create_prompt_card_image("positive", POSITIVE_CARD_FRAME)
    create_card_pair_image(CARD_PAIR_FRAME)
    negative_video = temp_dir / "negative_prompt_card.mp4"
    positive_video = temp_dir / "positive_prompt_card.mp4"
    render_card_video(NEGATIVE_CARD_FRAME, CARD_SECONDS, negative_video)
    render_card_video(POSITIVE_CARD_FRAME, CARD_SECONDS, positive_video)
    return {
        "negative_prompt_card": negative_video,
        "positive_prompt_card": positive_video,
    }


def build_clip_specs(source_duration: float, cards: dict[str, pathlib.Path]) -> list[dict[str, Any]]:
    return [
        {
            "clip_id": "shot01_intro_host",
            "carrier": "API生成真人",
            "input_path": ROUND31_FULL,
            "source_start": 0.000,
            "duration_seconds": 10.424,
            "source": f"{public_path(ROUND31_FULL)} 0.000s-10.424s",
            "note": "沿用 round31 / round30 开头主持壳，不重新生成元素娃娃。",
        },
        {
            "clip_id": "shot02_negative_prompt_card",
            "carrier": "卡片",
            "input_path": cards["negative_prompt_card"],
            "source_start": 0.000,
            "duration_seconds": CARD_SECONDS,
            "source": "round34 generated 9:16 prompt card",
            "note": "《反面展示》提示卡，图二粉色樱花柔和展示牌风格，副标题仅提示即将进入反面真实录屏，1.6s。",
        },
        {
            "clip_id": "shot03_negative_recording",
            "carrier": "用户录制素材",
            "input_path": ROUND31_FULL,
            "source_start": 11.424,
            "duration_seconds": 8.400,
            "source": "素材录制/反面/录制于 2026-04-16 22.41.32.mp4 32.000s-40.400s",
            "note": "反面连续录屏，证据链保持不变。",
        },
        {
            "clip_id": "shot04_positive_prompt_card",
            "carrier": "卡片",
            "input_path": cards["positive_prompt_card"],
            "source_start": 0.000,
            "duration_seconds": CARD_SECONDS,
            "source": "round34 generated 9:16 prompt card",
            "note": "《正面展示》提示卡，插入于反面录屏和正面录屏之间，副标题仅提示即将进入正面真实录屏，1.6s。",
        },
        {
            "clip_id": "shot05_positive_recording",
            "carrier": "用户录制素材",
            "input_path": ROUND31_FULL,
            "source_start": 19.824,
            "duration_seconds": 16.000,
            "source": "素材录制/正面/录制于 2026-04-16 23.03.53.mp4 610.000s-626.000s",
            "note": "正面连续录屏，30-32 秒仍落在这一镜头内部。",
        },
        {
            "clip_id": "shot06_result_diff_card",
            "carrier": "卡片",
            "input_path": ROUND31_FULL,
            "source_start": 35.824,
            "duration_seconds": 1.500,
            "source": "round31 result_diff_card",
            "note": "结果差提示卡保留，不新增解释卡。",
        },
        {
            "clip_id": "shot07_clean_host",
            "carrier": "API生成真人",
            "input_path": ROUND31_FULL,
            "source_start": 38.620,
            "duration_seconds": 5.336,
            "source": f"{public_path(ROUND31_FULL)} 38.620s-43.956s",
            "note": "回场主持壳沿用干净源片段，不重新生成。",
        },
        {
            "clip_id": "shot08_judgment_card",
            "carrier": "judgment_card",
            "input_path": ROUND31_FULL,
            "source_start": 43.956,
            "duration_seconds": 6.080,
            "source": f"{public_path(ROUND31_FULL)} 43.956s-50.036s",
            "note": "结尾总结卡保持信息密度不变。",
        },
        {
            "clip_id": "shot09_prompt_tail",
            "carrier": "Prompt引用尾卡",
            "input_path": ROUND31_FULL,
            "source_start": 50.036,
            "duration_seconds": max(0.0, round3(source_duration - 50.036)),
            "source": f"{public_path(ROUND31_FULL)} 50.036s-end",
            "note": "Prompt 引用尾卡不承担主叙事和中段证据。",
        },
    ]


def transition_durations_for(clips: Sequence[dict[str, Any]]) -> list[float]:
    durations: list[float] = []
    for index in range(len(clips) - 1):
        from_id = clips[index]["clip_id"]
        to_id = clips[index + 1]["clip_id"]
        if from_id == "shot06_result_diff_card" and to_id == "shot07_clean_host":
            durations.append(PRIMARY_CROSSFADE_SECONDS)
        else:
            durations.append(BASE_CROSSFADE_SECONDS)
    return durations


def compute_clip_positions(clips: Sequence[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    fades = transition_durations_for(clips)
    positioned: list[dict[str, Any]] = []
    for index, clip in enumerate(clips):
        duration = round3(float(clip["duration_seconds"]))
        if index == 0:
            output_start = 0.0
        else:
            output_start = round3(float(positioned[index - 1]["output_end"]) - fades[index - 1])
        output_end = round3(output_start + duration)
        prev_fade = fades[index - 1] if index > 0 else 0.0
        next_fade = fades[index] if index < len(clips) - 1 else 0.0
        positioned.append(
            {
                **clip,
                "clip_index": index,
                "duration_seconds": duration,
                "output_start": output_start,
                "output_end": output_end,
                "pure_start": round3(output_start + prev_fade),
                "pure_end": round3(output_end - next_fade),
            }
        )

    transitions: list[dict[str, Any]] = []
    for index, fade in enumerate(fades):
        from_clip = positioned[index]
        transitions.append(
            {
                "transition_id": f"transition_{index + 1:02d}",
                "from_clip": from_clip["clip_id"],
                "to_clip": positioned[index + 1]["clip_id"],
                "start_seconds": round3(float(from_clip["output_end"]) - fade),
                "end_seconds": round3(float(from_clip["output_end"])),
                "duration_seconds": fade,
            }
        )
    return positioned, transitions


def filter_for_sequence(clips: Sequence[dict[str, Any]], output_path: pathlib.Path) -> None:
    args = ["-y"]
    for clip in clips:
        args.extend(["-i", str(clip["input_path"])])

    filters: list[str] = []
    for index, clip in enumerate(clips):
        start = float(clip["source_start"])
        duration = float(clip["duration_seconds"])
        filters.append(
            f"[{index}:v]trim=start={start:.3f}:duration={duration:.3f},"
            f"setpts=PTS-STARTPTS,fps={FPS:.3f},scale={TARGET_WIDTH}:{TARGET_HEIGHT},setsar=1,format=yuv420p[v{index}]"
        )
        filters.append(
            f"[{index}:a]atrim=start={start:.3f}:duration={duration:.3f},asetpts=PTS-STARTPTS,"
            "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
            f"[a{index}]"
        )

    fades = transition_durations_for(clips)
    current_video = "v0"
    current_audio = "a0"
    current_duration = float(clips[0]["duration_seconds"])
    for index, fade in enumerate(fades, start=1):
        offset = round3(current_duration - fade)
        next_video = f"vx{index}"
        next_audio = f"ax{index}"
        filters.append(
            f"[{current_video}][v{index}]xfade=transition=fade:duration={fade:.3f}:offset={offset:.3f},format=yuv420p[{next_video}]"
        )
        filters.append(f"[{current_audio}][a{index}]acrossfade=d={fade:.3f}:c1=tri:c2=tri[{next_audio}]")
        current_video = next_video
        current_audio = next_audio
        current_duration = round3(current_duration + float(clips[index]["duration_seconds"]) - fade)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    run_ffmpeg(
        [
            *args,
            "-filter_complex",
            ";".join(filters),
            "-map",
            f"[{current_video}]",
            "-map",
            f"[{current_audio}]",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(output_path),
        ]
    )


def render_round34_full(clips: Sequence[dict[str, Any]]) -> None:
    filter_for_sequence(clips, ROUND34_FULL)


def render_round34_middle_preview(clips: Sequence[dict[str, Any]]) -> None:
    middle_ids = {
        "shot02_negative_prompt_card",
        "shot03_negative_recording",
        "shot04_positive_prompt_card",
        "shot05_positive_recording",
        "shot06_result_diff_card",
    }
    middle_clips = [clip for clip in clips if clip["clip_id"] in middle_ids]
    filter_for_sequence(middle_clips, ROUND34_MIDDLE_PREVIEW)


def extract_clip(source: pathlib.Path, start: float, duration: float, output: pathlib.Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run_ffmpeg(
        [
            "-y",
            "-ss",
            f"{start:.3f}",
            "-i",
            str(source),
            "-t",
            f"{duration:.3f}",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )


def create_before_after_compare() -> None:
    ROUND34_BEFORE_AFTER.parent.mkdir(parents=True, exist_ok=True)
    run_ffmpeg(
        [
            "-y",
            "-ss",
            "10.000",
            "-i",
            str(ROUND32_FULL),
            "-ss",
            "10.000",
            "-i",
            str(ROUND34_FULL),
            "-t",
            "30.000",
            "-filter_complex",
            (
                "[0:v]scale=360:640:force_original_aspect_ratio=decrease,"
                "pad=360:640:(ow-iw)/2:(oh-ih)/2:black,setsar=1[v0];"
                "[1:v]scale=360:640:force_original_aspect_ratio=decrease,"
                "pad=360:640:(ow-iw)/2:(oh-ih)/2:black,setsar=1[v1];"
                "[v0][v1]hstack=inputs=2[vout]"
            ),
            "-map",
            "[vout]",
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "21",
            str(ROUND34_BEFORE_AFTER),
        ]
    )


def create_window_frame_sheet(source: pathlib.Path, start: float, end: float, step: float, output: pathlib.Path, title: str) -> None:
    frame_dir = output.parent / f"{output.stem}_frames"
    times = AUDIT.build_time_grid(start, end, step)
    samples = AUDIT.extract_frames(source, times, frame_dir, prefix=output.stem)
    AUDIT.create_contact_sheet(
        [sample.path for sample in samples],
        [f"{sample.time_seconds:.1f}s" for sample in samples],
        output,
        title=title,
        columns=5,
    )
    shutil.rmtree(frame_dir, ignore_errors=True)


def create_problem_windows_and_sheets() -> None:
    extract_clip(ROUND34_FULL, 30.0, 10.0, ROUND34_PROBLEM_30_40)
    extract_clip(ROUND34_FULL, 30.0, 2.0, ROUND34_PROBLEM_30_32)
    create_window_frame_sheet(
        ROUND34_FULL,
        30.0,
        32.0,
        0.2,
        ROUND34_PROBLEM_30_32_FRAMES,
        "round34 30-32s 高频抽帧联系表",
    )


def cut_points(clips: Sequence[dict[str, Any]], final_duration: float) -> list[float]:
    _, transitions = compute_clip_positions(clips)
    candidates: list[float] = []
    for transition in transitions:
        candidates.append(float(transition["start_seconds"]))
        candidates.append(float(transition["end_seconds"]))
    return [round3(value) for value in candidates if 0.0 < value < final_duration]


def is_crossfade_boundary(second: float, clips: Sequence[dict[str, Any]]) -> bool:
    _, transitions = compute_clip_positions(clips)
    for transition in transitions:
        start = float(transition["start_seconds"])
        end = float(transition["end_seconds"])
        if start - 0.04 <= second <= end + 0.04:
            return True
    return False


def run_final_audit(clips: Sequence[dict[str, Any]]) -> dict[str, Any]:
    final_duration = AUDIT.read_media_duration_seconds(ROUND34_FULL)
    payload = AUDIT.audit_video(
        ROUND34_FULL,
        AUDIT_DIR / "round34_final_scan",
        cut_points=cut_points(clips, final_duration),
        high_frequency_start=10.0,
        high_frequency_end=40.0,
        high_frequency_step=0.2,
        border_sheet_path=ROUND34_BORDER_SHEET,
        jump_sheet_path=ROUND34_JUMP_SHEET,
    )
    shutil.copyfile(ROUND34_JUMP_SHEET, ROUND34_CUT_SHEET)
    final_scan_dir = AUDIT_DIR / "round34_final_scan"
    if (final_scan_dir / "full_border_residue_report.md").exists():
        shutil.copyfile(final_scan_dir / "full_border_residue_report.md", ROUND34_BORDER_REPORT)
    if (final_scan_dir / "full_jump_cut_report.md").exists():
        shutil.copyfile(final_scan_dir / "full_jump_cut_report.md", ROUND34_JUMP_REPORT)
    shutil.rmtree(final_scan_dir / "border_residue_probe_frames", ignore_errors=True)
    shutil.rmtree(final_scan_dir / "jump_cut_probe_frames", ignore_errors=True)
    return payload


def build_timeline(clips: Sequence[dict[str, Any]], final_duration: float) -> list[dict[str, Any]]:
    positioned, transitions = compute_clip_positions(clips)
    segments: list[dict[str, Any]] = []
    for index, clip in enumerate(positioned):
        pure_start = float(clip["pure_start"])
        pure_end = min(float(clip["pure_end"]), final_duration)
        if pure_end > pure_start:
            segments.append(
                {
                    "segment_id": clip["clip_id"],
                    "start_seconds": round3(pure_start),
                    "end_seconds": round3(pure_end),
                    "carrier": clip["carrier"],
                    "source": clip["source"],
                    "note": clip["note"],
                }
            )
        if index < len(transitions):
            transition = transitions[index]
            start = float(transition["start_seconds"])
            end = min(float(transition["end_seconds"]), final_duration)
            if end > start:
                segments.append(
                    {
                        "segment_id": transition["transition_id"],
                        "start_seconds": round3(start),
                        "end_seconds": round3(end),
                        "carrier": "轻过渡",
                        "source": f"{transition['from_clip']} -> {transition['to_clip']}",
                        "note": f"{transition['duration_seconds']:.2f}s crossfade，用于降低硬切 / 跳屏感。",
                    }
                )
    if segments:
        segments[-1]["end_seconds"] = round3(final_duration)
    return [segment for segment in segments if segment["end_seconds"] > segment["start_seconds"]]


def write_timeline_json(clips: Sequence[dict[str, Any]], final_duration: float) -> list[dict[str, Any]]:
    segments = build_timeline(clips, final_duration)
    payload = {
        "round": ROUND34_NAME,
        "baseline_round": ROUND32_NAME,
        "segments": segments,
    }
    ROUND34_TIMELINE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return segments


def write_cut_map(segments: Sequence[dict[str, Any]]) -> None:
    lines = [
        "# round34 cut map",
        "",
        "`已确认` 本审片包指向 `round34_中段双展示提示卡_正反分段提示修复`。",
        "",
        "| shot | 成片时间 | 承载方式 | 文件来源 | 审片判断 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for segment in segments:
        lines.append(
            f"| {segment['segment_id']} | {segment['start_seconds']:.3f}s-{segment['end_seconds']:.3f}s "
            f"| {segment['carrier']} | {segment['source']} | {segment['note']} |"
        )
    lines.extend(
        [
            "",
            "## round34 修复说明",
            "",
            "- `已确认` 原段首提示卡已替换为《反面展示》提示卡。",
            "- `已确认` 已在反面录屏之后、正面录屏之前新增《正面展示》提示卡。",
            f"- `已确认` 两张提示卡均为 9:16 竖屏展示牌，时长 `{CARD_SECONDS:.1f}s`。",
            f"- `已确认` 中段主要切点使用 `{BASE_CROSSFADE_SECONDS:.2f}s` 轻 crossfade，结果差卡回主持壳使用 `{PRIMARY_CROSSFADE_SECONDS:.2f}s` 轻 crossfade。",
            "- `已确认` 反面录屏和正面录屏源片段未裁短、未重录、未替换。",
            "- `已确认` 结果差提示卡、主持壳、judgment_card、Prompt 引用尾卡均未重做。",
            "- `未发生` 阿里 API 调用、元素娃娃重生成、原始录屏修改、额外解释卡新增。",
            "- `待验证` 内容最终是否过线仍需用户 / ChatGPT 人工复审。",
        ]
    )
    ROUND34_CUT_MAP.write_text("\n".join(lines) + "\n", encoding="utf-8")


def border_findings(payload: dict[str, Any]) -> list[float]:
    return [round3(float(item["time_seconds"])) for item in payload.get("border_findings", [])]


def jump_validation(payload: dict[str, Any], clips: Sequence[dict[str, Any]]) -> str:
    probes = payload.get("jump_cut_probes", [])
    high_risks = [
        probe
        for probe in probes
        if probe.get("risk_level") == "high" and not is_crossfade_boundary(float(probe.get("cut_seconds", 0.0)), clips)
    ]
    return "通过" if not high_risks else "待验证"


def write_plan(clips: Sequence[dict[str, Any]], final_duration: float) -> None:
    payload = {
        "round": ROUND34_NAME,
            "baseline_round": ROUND32_NAME,
            "goal": "只做 latest_review_pack 的中段局部修复：按图二风格重构《反面展示》《正面展示》两张 9:16 提示卡，不重构整条视频。",
            "visual_plan": {
            "reference_image_status": REFERENCE_IMAGE_META.get("status", "待验证：图二参考图尚未写入元数据。"),
            "reference_image": REFERENCE_IMAGE_META,
            "canvas": CARD_STYLE_TOKENS["canvas_size"],
            "duration_seconds": CARD_SECONDS,
            "crossfade_seconds": BASE_CROSSFADE_SECONDS,
            "title_layout": "center_large_readable",
            "card_copy": CARD_COPY,
            "adopted_elements": ["图二横图参考", "粉色主色", "樱花花瓣", "小花枝", "细线边框", "蕾丝花边感", "右上角蝴蝶结", "圆角展示牌", "中心大标题", "一句副标题", "柔和光感", "少量高光粒子"],
            "rejected_elements": ["图一橙色网格说明页", "横图拉伸", "上下加黑边", "PPT 大纲页", "正反同卡说明", "大段正文", "bullet list", "卡片退后，证据向前"],
            "tokens": CARD_STYLE_TOKENS,
        },
        "structure": {
            "inserted_positive_prompt_card": True,
            "negative_prompt_card_seconds": CARD_SECONDS,
            "positive_prompt_card_seconds": CARD_SECONDS,
            "final_duration_seconds": round3(final_duration),
        },
        "prohibited_actions": {
            "ali_api_called": ALI_API_CALLED,
            "host_avatar_regenerated": HOST_AVATAR_REGENERATED,
            "raw_recordings_modified": RAW_RECORDINGS_MODIFIED,
            "host_shell_rebuilt": HOST_SHELL_REBUILT,
            "judgment_card_rebuilt": JUDGMENT_CARD_REBUILT,
            "prompt_tail_rebuilt": PROMPT_TAIL_REBUILT,
            "new_explanation_cards_added": NEW_EXPLANATION_CARDS_ADDED,
        },
        "clips": [
            {
                "clip_id": clip["clip_id"],
                "duration_seconds": clip["duration_seconds"],
                "source": clip["source"],
                "note": clip["note"],
            }
            for clip in clips
        ],
    }
    ROUND34_PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_summary(final_duration: float, middle_duration: float, audit_payload: dict[str, Any], jump_status: str) -> dict[str, Any]:
    border_times = border_findings(audit_payload)
    border_status = "通过" if not border_times else "待验证"
    technical_status = "通过" if border_status == "通过" and jump_status == "通过" else "待验证"
    blockers = ["用户 / ChatGPT 尚未完成 round34 内容最终复审，send_ready 必须保持 no。"]
    if border_times:
        blockers.append("round34 复扫仍检出绿色边框候选：" + ", ".join(f"{second:.3f}s" for second in border_times))
    if jump_status != "通过":
        blockers.append("round34 跳切连续性仍需人工复核高风险切点，不能写 content_validation 通过。")
    summary = {
        "round": ROUND34_NAME,
        "baseline_round": ROUND32_NAME,
        "border_residue_validation": border_status,
        "jump_cut_validation": jump_status,
        "technical_validation": f"{technical_status}：round34 已生成 full/middle/before_after/problem window，正反提示卡已补齐并完成边框残留与跳切连续性扫描。",
        "content_validation": "待用户 / ChatGPT 最终复审",
        "send_ready": False,
        "whole_video_duration_seconds": round3(final_duration),
        "middle_preview_duration_seconds": round3(middle_duration),
        "repair_scope": {
            "negative_prompt_card_seconds": CARD_SECONDS,
            "positive_prompt_card_seconds": CARD_SECONDS,
            "base_crossfade_seconds": BASE_CROSSFADE_SECONDS,
            "primary_crossfade_seconds": PRIMARY_CROSSFADE_SECONDS,
            "reference_image_read": bool(REFERENCE_IMAGE_META),
            "negative_prompt_card_title": CARD_COPY["negative"]["title"],
            "negative_prompt_card_subtitle": CARD_COPY["negative"]["subtitle"],
            "positive_prompt_card_title": CARD_COPY["positive"]["title"],
            "positive_prompt_card_subtitle": CARD_COPY["positive"]["subtitle"],
            "positive_prompt_card_added": POSITIVE_PROMPT_CARD_ADDED,
            "middle_evidence_recordings_trimmed": MIDDLE_EVIDENCE_RECORDINGS_TRIMMED,
            "new_explanation_cards_added": NEW_EXPLANATION_CARDS_ADDED,
            "ali_api_called": ALI_API_CALLED,
            "host_avatar_regenerated": HOST_AVATAR_REGENERATED,
            "host_shell_rebuilt": HOST_SHELL_REBUILT,
            "judgment_card_rebuilt": JUDGMENT_CARD_REBUILT,
            "prompt_tail_rebuilt": PROMPT_TAIL_REBUILT,
            "raw_recordings_modified": RAW_RECORDINGS_MODIFIED,
        },
        "round34_border_findings_seconds": border_times,
        "artifacts": {
            "full": public_path(ROUND34_FULL),
            "middle_preview": public_path(ROUND34_MIDDLE_PREVIEW),
            "before_after": public_path(ROUND34_BEFORE_AFTER),
            "negative_prompt_card_frame": public_path(NEGATIVE_CARD_FRAME),
            "positive_prompt_card_frame": public_path(POSITIVE_CARD_FRAME),
            "prompt_card_pair": public_path(CARD_PAIR_FRAME),
            "reference_image_copy": public_path(REFERENCE_IMAGE_COPY),
            "problem_30_32": public_path(ROUND34_PROBLEM_30_32),
            "problem_30_32_frames": public_path(ROUND34_PROBLEM_30_32_FRAMES),
            "border_report": public_path(ROUND34_BORDER_REPORT),
            "jump_report": public_path(ROUND34_JUMP_REPORT),
            "cut_contact_sheet": public_path(ROUND34_CUT_SHEET),
        },
        "remaining_blockers": blockers,
    }
    ROUND34_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def write_review_manifest(summary: dict[str, Any]) -> None:
    lines = [
        "# latest_review_pack 审片入口",
        "",
        "`已确认` 本包指向 `round34_中段双展示提示卡_正反分段提示修复`。",
        "",
        "- 仓库相对路径：`dist/latest_review_pack/`",
        "- 本地绝对路径：`/Users/fan/Documents/视频工厂/dist/latest_review_pack/`",
        "",
        "## 本轮先看顺序",
        "",
        "1. 先看 `反面展示提示卡_单帧.png`、`正面展示提示卡_单帧.png`、`正反提示卡_并排对比.png`",
        "   - 判断正反提示卡是否统一参考图二的粉色樱花柔和展示牌风格，且为 9:16 竖屏重构。",
        "2. 再看 `middle_preview.mp4`",
        "   - 确认中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。",
        "3. 再看 `problem_windows/30_32s.mp4`",
        "   - 确认 30-32 秒仍在正面真实录屏内部，新增正面提示卡没有替代证据。",
        "4. 再看 `cut_contact_sheet.jpg`",
        "   - 判断正反提示卡前后轻过渡是否降低跳屏感。",
        "5. 最后看 `full.mp4`",
        "   - 判断全片节奏；用户确认前不能写可发。",
        "",
        "## 文件清单与中文备注",
        "",
        "| 文件 | 中文备注 |",
        "| --- | --- |",
        "| `full.mp4` | round34 最新完整正片。 |",
        "| `middle_preview.mp4` | round34 中段预览，用于快速检查正反提示卡与证据链。 |",
        "| `before_after.mp4` | round33 与 round34 中段对比视频。 |",
        "| `图二参考图.png` | 用户本轮同步的图二参考图副本，只用于证明风格参考来源。 |",
        "| `cut_contact_sheet.jpg` | 按镜头切点抽帧，方便判断跳屏、风格断裂、卡片过短。 |",
        "| `反面展示提示卡_单帧.png` | 反面展示提示卡单帧图。 |",
        "| `正面展示提示卡_单帧.png` | 正面展示提示卡单帧图。 |",
        "| `正反提示卡_并排对比.png` | 两张提示卡并排对比图。 |",
        "| `problem_windows/30_32s.mp4` | 30-32 秒问题窗口。 |",
        "| `problem_windows/30_32s_frames.jpg` | 30-32 秒高频抽帧联系表。 |",
        "| `audit/full_border_residue_report.md` | 全片边框残留扫描报告。 |",
        "| `audit/full_jump_cut_report.md` | 全片跳切连续性扫描报告。 |",
        "| `audit/border_residue_contact_sheet.jpg` | 全片边框残留抽帧联系表。 |",
        "| `audit/jump_cut_contact_sheet.jpg` | 全片跳切抽帧联系表。 |",
        "| `timeline.json` | round34 每个 segment / shot 的时间轴、承载方式、文件来源。 |",
        "| `cut_map.md` | round34 逐镜头说明。 |",
        "| `summary.json` | 写明 `technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`。 |",
        "| `review_manifest.md` | 给 ChatGPT 的审片入口。 |",
        "",
        "## 不得写成已完成的结论",
        "",
        "- `content_validation` 不能因为技术扫描通过就写成通过。",
        "- `send_ready` 必须保持 `no`，除非用户人工最终确认。",
        "- 不得说云端剪辑链路已稳定跑通。",
        "- 不得把提示卡写成中段主体证据；中段主体仍必须是用户真实录屏。",
        "",
        "## 当前 validation",
        "",
        f"- `border_residue_validation`: {summary['border_residue_validation']}",
        f"- `jump_cut_validation`: {summary['jump_cut_validation']}",
        f"- `technical_validation`: {summary['technical_validation']}",
        f"- `content_validation`: {summary['content_validation']}",
        "- `send_ready`: no",
    ]
    ROUND34_REVIEW_MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_audit_md(summary: dict[str, Any]) -> None:
    lines = [
        "# round34 中段双展示提示卡_正反分段提示修复审计",
        "",
        "## 已确认",
        "",
        "- 已确认图二参考图可读取，并复制到本轮 inputs 目录。",
        "- 已保留《反面展示》提示卡在反面真实录屏之前，《正面展示》提示卡在反面真实录屏之后、正面真实录屏之前。",
        "- 已将《反面展示》《正面展示》两张提示卡重构为 720x1280 竖屏粉色樱花柔和展示牌风格。",
        f"- 两张提示卡时长均为 `{CARD_SECONDS:.1f}s`，位于 1.2-2.0s 合格区间。",
        f"- 中段切点使用 `{BASE_CROSSFADE_SECONDS:.2f}s` 轻 crossfade。",
        "- 反面录屏和正面录屏源片段未裁短、未替换、未重录。",
        "- 未调用阿里 API，未重新生成元素娃娃，未重做主持壳、结尾总结卡或 Prompt 尾卡。",
        "",
        "## 视觉方案",
        "",
        "- 画布：720x1280，9:16 竖屏。",
        "- 主色：粉色柔和渐变。",
        "- 装饰：樱花花瓣、小花枝、细线边框、蕾丝花边感、柔和光斑与少量高光粒子。",
        "- 排版：中心大标题 + 一句短副标题，浅色内填、粉色描边、轻微阴影，无正文、无 bullet list。",
        f"- 图二参考图：{REFERENCE_IMAGE_META.get('source', REFERENCE_IMAGE_SOURCE)}，读取尺寸 {REFERENCE_IMAGE_META.get('width', '待验证')}x{REFERENCE_IMAGE_META.get('height', '待验证')}。",
        "- 未采用横图拉伸、上下加黑边、图一橙色说明页或正反同卡说明。",
        "",
        "## validation",
        "",
        f"- `border_residue_validation`: {summary['border_residue_validation']}",
        f"- `jump_cut_validation`: {summary['jump_cut_validation']}",
        f"- `technical_validation`: {summary['technical_validation']}",
        f"- `content_validation`: {summary['content_validation']}",
        "- `send_ready`: no",
    ]
    ROUND34_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_latest_review_pack() -> None:
    if LATEST_REVIEW_PACK_DIR.exists():
        shutil.rmtree(LATEST_REVIEW_PACK_DIR)
    (LATEST_REVIEW_PACK_DIR / "problem_windows").mkdir(parents=True, exist_ok=True)
    (LATEST_REVIEW_PACK_DIR / "audit").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROUND34_FULL, LATEST_REVIEW_PACK_DIR / "full.mp4")
    shutil.copyfile(ROUND34_MIDDLE_PREVIEW, LATEST_REVIEW_PACK_DIR / "middle_preview.mp4")
    shutil.copyfile(ROUND34_BEFORE_AFTER, LATEST_REVIEW_PACK_DIR / "before_after.mp4")
    shutil.copyfile(ROUND34_CUT_SHEET, LATEST_REVIEW_PACK_DIR / "cut_contact_sheet.jpg")
    shutil.copyfile(NEGATIVE_CARD_FRAME, LATEST_REVIEW_PACK_DIR / "反面展示提示卡_单帧.png")
    shutil.copyfile(POSITIVE_CARD_FRAME, LATEST_REVIEW_PACK_DIR / "正面展示提示卡_单帧.png")
    shutil.copyfile(CARD_PAIR_FRAME, LATEST_REVIEW_PACK_DIR / "正反提示卡_并排对比.png")
    shutil.copyfile(REFERENCE_IMAGE_COPY, LATEST_REVIEW_PACK_DIR / "图二参考图.png")
    shutil.copyfile(ROUND34_PROBLEM_30_32, LATEST_REVIEW_PACK_DIR / "problem_windows" / "30_32s.mp4")
    shutil.copyfile(ROUND34_PROBLEM_30_32_FRAMES, LATEST_REVIEW_PACK_DIR / "problem_windows" / "30_32s_frames.jpg")
    shutil.copyfile(ROUND34_BORDER_REPORT, LATEST_REVIEW_PACK_DIR / "audit" / "full_border_residue_report.md")
    shutil.copyfile(ROUND34_JUMP_REPORT, LATEST_REVIEW_PACK_DIR / "audit" / "full_jump_cut_report.md")
    shutil.copyfile(ROUND34_BORDER_SHEET, LATEST_REVIEW_PACK_DIR / "audit" / "border_residue_contact_sheet.jpg")
    shutil.copyfile(ROUND34_JUMP_SHEET, LATEST_REVIEW_PACK_DIR / "audit" / "jump_cut_contact_sheet.jpg")
    shutil.copyfile(ROUND34_TIMELINE, LATEST_REVIEW_PACK_DIR / "timeline.json")
    shutil.copyfile(ROUND34_CUT_MAP, LATEST_REVIEW_PACK_DIR / "cut_map.md")
    shutil.copyfile(ROUND34_SUMMARY, LATEST_REVIEW_PACK_DIR / "summary.json")
    shutil.copyfile(ROUND34_REVIEW_MANIFEST, LATEST_REVIEW_PACK_DIR / "review_manifest.md")


def main() -> None:
    ensure_dirs()
    ensure_reference_image()
    require_source_files()
    with tempfile.TemporaryDirectory(prefix="round34_cards_") as temp_str:
        temp_dir = pathlib.Path(temp_str)
        cards = card_video_paths(temp_dir)
        clips = build_clip_specs(round31_source_duration(), cards)
        render_round34_full(clips)
        render_round34_middle_preview(clips)
        create_before_after_compare()
        create_problem_windows_and_sheets()
        audit_payload = run_final_audit(clips)
        final_duration = AUDIT.read_media_duration_seconds(ROUND34_FULL)
        middle_duration = AUDIT.read_media_duration_seconds(ROUND34_MIDDLE_PREVIEW)
        write_plan(clips, final_duration)
        segments = write_timeline_json(clips, final_duration)
        write_cut_map(segments)
        jump_status = jump_validation(audit_payload, clips)
        summary = write_summary(final_duration, middle_duration, audit_payload, jump_status)
        write_review_manifest(summary)
        write_audit_md(summary)
        update_latest_review_pack()


if __name__ == "__main__":
    main()
