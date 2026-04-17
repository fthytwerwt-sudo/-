from __future__ import annotations

import json
import math
import pathlib
import shutil
import subprocess
import wave
from dataclasses import dataclass
from typing import Any

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "dist" / "20260417_豆包的正确打开方式_vnext"
LOCAL_REVIEW_DIR = OUTPUT_DIR / "local_review"
ASSET_DIR = OUTPUT_DIR / "素材"
SEGMENT_DIR = OUTPUT_DIR / "segments"
TTS_DIR = OUTPUT_DIR / "tts"
TEMP_DIR = OUTPUT_DIR / "tmp"

NEGATIVE_SOURCE = ROOT / "素材录制" / "反面" / "录制于 2026-04-16 22.41.32.mp4"
POSITIVE_SOURCE = ROOT / "素材录制" / "正面" / "录制于 2026-04-16 23.03.53.mp4"

WIDTH = 1080
HEIGHT = 1920
FPS = 25
GAP_SECONDS = 0.28
TAIL_CARD_SECONDS = 2.8

VOICE_NAME = "Flo (中文（中国大陆）)"
VOICE_RATE = 188
VOICE_ROUTE_PROVIDER = "macos_say_fallback"
VOICE_ROUTE_STATUS = "blocked"
VOICE_ROUTE_BLOCKED_REASON = (
    "当前仍使用 macOS `say` 的 `Flo (中文（中国大陆）)` 试配，"
    "没有切到豆包语音合成 2.0 主路线，也没有 Azure 兜底实现。"
)
HOST_ROUTE_PROVIDER = "static_voxel_panel_loop"
HOST_ROUTE_STATUS = "blocked"
HOST_ROUTE_BLOCKED_REASON = (
    "当前开头 / 结尾主持壳仍是 `PIL` 单张体素图生成后用 ffmpeg `-loop 1` 直接成段，"
    "没有真实嘴型、没有音频驱动、没有主持感级别的动态层。"
)

PIXEL_ORANGE = "#E58439"
PIXEL_GOLD = "#F5C04A"
PIXEL_STONE = "#1F2A33"
PIXEL_SKY = "#A9D1E8"
PIXEL_GRASS = "#4C8A58"
PIXEL_PANEL = "#F2E1BE"
PIXEL_PANEL_DARK = "#33281F"
PIXEL_PAPER = "#FFF8EE"
PIXEL_CREAM = "#F5EFE3"
PIXEL_WHITE = "#FFFDF8"


@dataclass(frozen=True)
class SegmentSpec:
    segment_id: str
    block_id: str
    block_name: str
    carrier: str
    asset_source: str
    voiceover_text: str
    caption_text: str
    visual_kind: str
    image_name: str | None = None
    source_video: pathlib.Path | None = None
    excerpts: tuple[tuple[float, float], ...] = ()
    role: str = "process"
    eyebrow: str = ""
    headline: str = ""
    support: str = ""
    detail: str = ""
    chips: tuple[str, ...] = ()
    accent: str = PIXEL_ORANGE
    background: str = PIXEL_CREAM
    silent_seconds: float | None = None
    visual_note: str = ""


SEGMENTS: list[SegmentSpec] = [
    SegmentSpec(
        segment_id="seg01_hook",
        block_id="block_01",
        block_name="开头判断",
        carrier="API 生成真人",
        asset_source="api_generated_style_shell",
        voiceover_text=(
            "豆包给你出的方案，你有没有觉得——\n"
            "能看，但用不了？\n"
            "最后你还是自己重写了一遍？\n\n"
            "这不是豆包的问题。\n"
            "是你问的方式，就决定了它只能给你那种结果。"
        ),
        caption_text=(
            "豆包给你出的方案，你有没有觉得——\n"
            "能看，但用不了？\n"
            "最后你还是自己重写了一遍？\n\n"
            "这不是豆包的问题。\n"
            "是你问的方式，就决定了它只能给你那种结果。"
        ),
        visual_kind="image",
        image_name="开头人物壳_hook_shell.png",
        role="hook",
        eyebrow="错误示范型开头",
        headline="不是豆包不行\n是你第一句话就问错了",
        support="同一份资料，直接开写，只会先拿到能看但难改的东西。",
        detail="开头人物壳只负责点破判断，不替代中段证据。",
        chips=("能看，但用不了", "第一句话就问错了"),
        accent=PIXEL_ORANGE,
        background="#F4E4C9",
        visual_note="Minecraft-inspired 原创体素方块风人物壳，开头承担判断进入。",
    ),
    SegmentSpec(
        segment_id="seg02_negative",
        block_id="block_02",
        block_name="反面步骤",
        carrier="用户录制素材",
        asset_source="素材录制/反面",
        voiceover_text=(
            "同样上传一份资料，\n"
            "你直接问\"给我一份方案\"，\n"
            "它出来的东西通常是这样的：\n"
            "三四段，每段都有内容，\n"
            "但没有一句是你能直接拿去用的。\n"
            "没有判断，\n"
            "没有真实结构，\n"
            "看起来挺完整，\n"
            "但你根本不知道从哪里改起。"
        ),
        caption_text=(
            "同样上传一份资料，你直接问\"给我一份方案\"，它出来的东西通常是这样的：\n"
            "三四段，每段都有内容，但没有一句是你能直接拿去用的。\n"
            "没有判断，没有真实结构，看起来挺完整，但你根本不知道从哪里改起。"
        ),
        visual_kind="video",
        source_video=NEGATIVE_SOURCE,
        excerpts=((25.0, 30.0), (35.0, 40.0), (40.0, 45.0), (50.0, 56.0), (60.0, 66.0)),
        role="process",
        eyebrow="反面录屏",
        headline="直接问“给我一份方案”",
        support="观众必须先看见这堆文字长什么样，才知道为什么后面要分两步。",
        detail="这里保留真实录屏证据，不加重游戏化花活。",
        chips=("看起来挺完整", "但你根本不知道从哪里改起", "没有先压判断"),
        accent="#D96B2B",
        background="#F8F0E8",
        visual_note="真实展示反面输出的长段落 / 表格 / 清单，证明‘有内容，但不好改’。",
    ),
    SegmentSpec(
        segment_id="seg03_positive_strategy",
        block_id="block_03",
        block_name="正面步骤第一段",
        carrier="用户录制素材",
        asset_source="素材录制/正面",
        voiceover_text=(
            "正确的方式是分两步。\n\n"
            "第一步，\n"
            "先让它当方案顾问，\n"
            "不是让它写，\n"
            "是让它先帮你想清楚：\n"
            "这个项目最核心的问题在哪，\n"
            "方案的主逻辑怎么走，\n"
            "哪些东西必须先定下来。\n\n"
            "同样那份资料，\n"
            "这一步做完，\n"
            "出来的才是你能继续改的初稿——\n"
            "不是能看，\n"
            "是能用。"
        ),
        caption_text=(
            "正确的方式是分两步。第一步，先让它当方案顾问，不是让它写，\n"
            "是让它先帮你想清楚：这个项目最核心的问题在哪，方案的主逻辑怎么走，哪些东西必须先定下来。\n"
            "同样那份资料，这一步做完，出来的才是你能继续改的初稿——不是能看，是能用。"
        ),
        visual_kind="video",
        source_video=POSITIVE_SOURCE,
        excerpts=((0.0, 6.0), (30.0, 45.0), (45.0, 60.0), (60.0, 75.0), (90.0, 105.0), (105.0, 120.0)),
        role="process",
        eyebrow="正面录屏 1/2",
        headline="第一步：先让它当方案顾问",
        support="先诊断核心问题，再压主结构，同样一份资料才会开始像能改的初稿。",
        detail="重点是看见一句策略判断、当前问题诊断、主结构和核心逻辑。",
        chips=("一句策略判断", "当前问题诊断", "主结构 / 核心逻辑"),
        accent="#2F8C6B",
        background="#ECF8F2",
        visual_note="同一份资料下，保留‘一句策略判断 / 当前问题诊断 / 主结构’的真实屏幕结果。",
    ),
    SegmentSpec(
        segment_id="seg04_xml_bridge",
        block_id="block_04",
        block_name="正面步骤第二段",
        carrier="用户录制素材",
        asset_source="素材录制/正面",
        voiceover_text=(
            "第二步，\n"
            "再拿这版方案让它做 PPT。\n\n"
            "但不是一句\"帮我做个PPT\"，\n"
            "而是让它一页一页往下压：\n"
            "每页讲什么，\n"
            "哪页最重要，\n"
            "图和文字怎么配。"
        ),
        caption_text=(
            "第二步，再拿这版方案让它做 PPT。\n"
            "但不是一句\"帮我做个PPT\"，而是让它一页一页往下压：每页讲什么，哪页最重要，图和文字怎么配。"
        ),
        visual_kind="video",
        source_video=POSITIVE_SOURCE,
        excerpts=((270.0, 280.0), (280.0, 290.0), (300.0, 310.0), (310.0, 320.0), (330.0, 340.0)),
        role="process",
        eyebrow="正面录屏 2/2",
        headline="先过 XML，再继续做 PPT",
        support="不要求观众懂 XML，只要看懂这里是结构化桥梁。",
        detail="把‘XML 出现 -> 复制 -> 再粘贴回豆包’这一步完整录到。",
        chips=("XML 出现", "复制 / 粘回", "继续生成 PPT"),
        accent="#3F7AE5",
        background="#EEF3FF",
        visual_note="真实录到 XML 出现、复制、再贴回豆包的动作，中间层不扩写原理。",
    ),
    SegmentSpec(
        segment_id="seg05_ppt_result",
        block_id="block_04",
        block_name="正面步骤第二段",
        carrier="用户录制素材",
        asset_source="素材录制/正面",
        voiceover_text=(
            "你前面那版方案如果没压清，\n"
            "后面PPT再精美，\n"
            "也只是把空壳做得更像样。"
        ),
        caption_text=(
            "你前面那版方案如果没压清，后面PPT再精美，也只是把空壳做得更像样。"
        ),
        visual_kind="video",
        source_video=POSITIVE_SOURCE,
        excerpts=((580.0, 600.0), (620.0, 640.0), (660.0, 680.0), (700.0, 720.0)),
        role="process",
        eyebrow="PPT 结果",
        headline="现在屏幕上已经能看到页结构",
        support="这时才是‘有标题、有页结构’，不是一页一坨字。",
        detail="用最终 PPT 结果把‘两步工作流’收成可见差值。",
        chips=("有标题", "有页结构", "不是一页一坨字"),
        accent="#B96A24",
        background="#FFF3E7",
        visual_note="保留 PPT 结果页与缩略图列表，让观众看懂‘一页一页压下来’的结果。",
    ),
    SegmentSpec(
        segment_id="seg06_summary_card",
        block_id="block_05",
        block_name="结果收束",
        carrier="少量 PPT / 总结卡",
        asset_source="generated_summary_card",
        voiceover_text=(
            "所以豆包的正确打开方式就两步：\n"
            "先压方案，\n"
            "再压PPT。\n"
            "先让内容变成能交的初稿，\n"
            "再让初稿变成能汇报的结构。"
        ),
        caption_text=(
            "所以豆包的正确打开方式就两步：先压方案，再压PPT。\n"
            "先让内容变成能交的初稿，再让初稿变成能汇报的结构。"
        ),
        visual_kind="image",
        image_name="总结卡_summary_card.png",
        role="process",
        eyebrow="两步工作流",
        headline="先压方案\n再压 PPT",
        support="先让内容变成能交的初稿，再让初稿变成能汇报的结构。",
        detail="总结卡只负责收清流程，不替代真实录屏证据。",
        chips=("先压方案", "再压 PPT", "先能交，再汇报"),
        accent=PIXEL_GOLD,
        background=PIXEL_PANEL,
        visual_note="Minecraft-inspired 原创体素方块风总结卡，只收两步工作流。",
    ),
    SegmentSpec(
        segment_id="seg07_close_shell",
        block_id="block_06",
        block_name="结尾收束",
        carrier="API 生成真人",
        asset_source="api_generated_style_shell",
        voiceover_text=(
            "你现在就可以试一次——\n"
            "同一份资料，\n"
            "先别急着问方案，\n"
            "先问它这一句话：\n"
            "\"你觉得这份资料里最核心的问题是什么？\"\n\n"
            "就这一句，\n"
            "结果就不一样了。"
        ),
        caption_text=(
            "你现在就可以试一次——同一份资料，先别急着问方案，\n"
            "先问它这一句话：\"你觉得这份资料里最核心的问题是什么？\"\n"
            "就这一句，结果就不一样了。"
        ),
        visual_kind="image",
        image_name="结尾人物壳_close_shell.png",
        role="outcome",
        eyebrow="最小动作",
        headline="就试这一句",
        support="先别急着问方案，先问核心问题。",
        detail="结尾人物壳只收住动作，不做第二轮讲解。",
        chips=("你觉得这份资料里最核心的问题是什么？", "就这一句，结果就不一样了"),
        accent=PIXEL_ORANGE,
        background="#F3E7D0",
        visual_note="Minecraft-inspired 原创体素方块风结尾人物壳，像游戏向导一样低压收束。",
    ),
    SegmentSpec(
        segment_id="seg08_prompt_tail",
        block_id="block_07",
        block_name="Prompt 引用尾卡",
        carrier="少量 PPT / 尾卡面板",
        asset_source="generated_prompt_tail_card",
        voiceover_text="",
        caption_text="",
        visual_kind="image",
        image_name="Prompt引用尾卡_prompt_tail.png",
        role="outcome",
        eyebrow="Prompt 引用尾卡",
        headline="第一步：先让它当顾问\n第二步：再让它当 PPT 助手",
        support="只做产品单元引用，不重复主叙事。",
        detail="",
        chips=("第一步：先让它当顾问", "第二步：再让它当 PPT 助手"),
        accent=PIXEL_GOLD,
        background=PIXEL_PANEL,
        silent_seconds=TAIL_CARD_SECONDS,
        visual_note="Minecraft-inspired 原创体素方块风尾卡，只保留两行产品单元引用。",
    ),
]


def ensure_tools_exist() -> None:
    required = ["say", "afconvert"]
    missing = [tool for tool in required if shutil.which(tool) is None]
    if missing:
        raise RuntimeError(f"缺少系统命令：{', '.join(missing)}")


def resolve_ffmpeg() -> str:
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    bundled = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("缺少 ffmpeg，可先安装项目依赖再运行。")


def run_command(args: list[str], *, cwd: pathlib.Path | None = None) -> None:
    subprocess.run(args, check=True, cwd=cwd)


def seconds_to_srt(value: float) -> str:
    milliseconds = max(0, int(round(value * 1000)))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for path in candidates:
        if pathlib.Path(path).exists():
            try:
                index = 0 if not bold else 2
                return ImageFont.truetype(path, size=size, index=index)
            except OSError:
                try:
                    return ImageFont.truetype(path, size=size)
                except OSError:
                    continue
    return ImageFont.load_default()


def draw_centered_multiline(
    draw: ImageDraw.ImageDraw,
    text: str,
    *,
    box: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
    spacing: int = 8,
) -> None:
    left, top, right, bottom = box
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing, align="center")
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = left + (right - left - width) / 2
    y = top + (bottom - top - height) / 2
    draw.multiline_text((x, y), text, font=font, fill=fill, spacing=spacing, align="center")


def draw_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    fill: str,
    outline: str,
    width: int = 6,
    radius: int = 34,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_voxel_character(draw: ImageDraw.ImageDraw, *, x: int, y: int, scale: int = 28) -> None:
    skin = "#E6B48E"
    hair = "#5A3518"
    shirt = "#F3923A"
    vest = "#8F5326"
    pants = "#3C5C7A"
    shoes = "#2A2A2A"

    def rect(px: int, py: int, w: int, h: int, color: str) -> None:
        draw.rectangle((x + px * scale, y + py * scale, x + (px + w) * scale, y + (py + h) * scale), fill=color)

    rect(2, 0, 6, 1, hair)
    rect(1, 1, 8, 4, skin)
    rect(1, 1, 2, 2, hair)
    rect(7, 1, 2, 2, hair)
    rect(2, 2, 1, 1, "#1D1D1D")
    rect(6, 2, 1, 1, "#1D1D1D")
    rect(4, 3, 2, 1, "#C26A5B")
    rect(2, 5, 6, 3, shirt)
    rect(3, 8, 4, 2, vest)
    rect(1, 6, 1, 3, skin)
    rect(8, 6, 1, 3, skin)
    rect(3, 10, 2, 3, pants)
    rect(5, 10, 2, 3, pants)
    rect(3, 13, 2, 1, shoes)
    rect(5, 13, 2, 1, shoes)


def create_voxel_scene(path: pathlib.Path, *, mode: str) -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), PIXEL_SKY)
    draw = ImageDraw.Draw(image)

    for y in range(0, HEIGHT, 80):
        tone = 180 + int(35 * math.sin(y / 170))
        draw.rectangle((0, y, WIDTH, y + 80), fill=(tone - 20, tone + 15, tone + 35))

    draw.rectangle((0, 1320, WIDTH, HEIGHT), fill=PIXEL_GRASS)
    for x in range(0, WIDTH, 72):
        height = 30 + (x // 72 % 4) * 18
        draw.rectangle((x, 1280 - height, x + 42, 1280), fill="#5A824D")
    for y in range(0, HEIGHT, 96):
        draw.line((0, y, WIDTH, y), fill=(255, 255, 255, 20), width=2)
    for x in range(0, WIDTH, 96):
        draw.line((x, 0, x, HEIGHT), fill=(255, 255, 255, 20), width=2)

    draw_panel(draw, (110, 180, 970, 1490), fill=PIXEL_PANEL, outline="#B77B35", width=8, radius=42)
    draw_panel(draw, (140, 220, 940, 430), fill="#F8EFD7", outline="#D99C48", width=6, radius=30)
    draw_panel(draw, (530, 520, 930, 1210), fill="#2F241D", outline="#8A5A2A", width=6, radius=30)

    for idx, color in enumerate(["#D96B2B", "#F3B13D", "#5A8B4E"]):
        draw.rounded_rectangle((170 + idx * 150, 258, 290 + idx * 150, 308), radius=18, fill=color)

    if mode == "hook":
        draw_voxel_character(draw, x=180, y=520, scale=32)
        label = "豆包的正确打开方式"
        note = "先别直接让它写"
    elif mode == "close":
        draw_voxel_character(draw, x=600, y=520, scale=32)
        label = "先问核心问题"
        note = "再往下做方案 / PPT"
        draw_panel(draw, (150, 620, 480, 1100), fill="#FFF7E8", outline="#C98C40", width=6, radius=30)
        for idx, text in enumerate(["核心问题", "主逻辑", "页结构"]):
            draw.rounded_rectangle((185, 690 + idx * 130, 445, 780 + idx * 130), radius=24, fill="#F5E3BC")
            draw.text((220, 720 + idx * 130), text, font=load_font(34, bold=True), fill=PIXEL_PANEL_DARK)
    elif mode == "summary":
        label = "两步工作流"
        note = "先压方案，再压 PPT"
        draw_panel(draw, (170, 540, 910, 1320), fill=PIXEL_PAPER, outline="#C78E42", width=8, radius=38)
        steps = [("01", "先压方案"), ("02", "再压 PPT")]
        for idx, (num, text) in enumerate(steps):
            left = 220 + idx * 320
            draw.rounded_rectangle((left, 710, left + 250, 1040), radius=28, fill="#F8E3B7", outline="#D99B48", width=6)
            draw.text((left + 82, 760), num, font=load_font(72, bold=True), fill=PIXEL_ORANGE)
            draw_centered_multiline(
                draw,
                text,
                box=(left + 20, 855, left + 230, 980),
                font=load_font(42, bold=True),
                fill=PIXEL_PANEL_DARK,
                spacing=6,
            )
    elif mode == "tail":
        label = "Prompt 引用尾卡"
        note = "只引用产品单元，不抢主叙事"
        draw_panel(draw, (150, 540, 930, 1320), fill=PIXEL_PAPER, outline="#C78E42", width=8, radius=38)
        lines = ["第一步：先让它当顾问", "第二步：再让它当 PPT 助手"]
        for idx, text in enumerate(lines):
            top = 720 + idx * 200
            draw.rounded_rectangle((210, top, 870, top + 118), radius=28, fill="#F8E3B7", outline="#D99B48", width=6)
            draw_centered_multiline(
                draw,
                text,
                box=(240, top + 12, 840, top + 106),
                font=load_font(40, bold=True),
                fill=PIXEL_PANEL_DARK,
                spacing=4,
            )
    else:
        raise ValueError(f"未知体素场景：{mode}")

    font_title = load_font(56, bold=True)
    font_note = load_font(30, bold=False)
    draw.text((174, 255), label, font=font_title, fill=PIXEL_PANEL_DARK)
    draw.text((176, 334), note, font=font_note, fill="#6C5437")
    draw.text((565, 560), "Minecraft-inspired 原创体素方块风", font=load_font(30, bold=True), fill=PIXEL_GOLD)

    image = image.filter(ImageFilter.GaussianBlur(radius=0.2))
    image.save(path)


def ensure_shell_images() -> dict[str, pathlib.Path]:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    mapping = {
        "开头人物壳_hook_shell.png": "hook",
        "结尾人物壳_close_shell.png": "close",
        "总结卡_summary_card.png": "summary",
        "Prompt引用尾卡_prompt_tail.png": "tail",
    }
    result: dict[str, pathlib.Path] = {}
    for filename, mode in mapping.items():
        output = ASSET_DIR / filename
        create_voxel_scene(output, mode=mode)
        result[filename] = output
    return result


def synthesize_voice(text: str, output_stem: str) -> tuple[pathlib.Path, float]:
    TTS_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    aiff_path = TEMP_DIR / f"{output_stem}.aiff"
    wav_path = TTS_DIR / f"{output_stem}.wav"
    run_command(["say", "-v", VOICE_NAME, "-r", str(VOICE_RATE), text, "-o", str(aiff_path)])
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
    with wave.open(str(wav_path), "rb") as handle:
        duration = handle.getnframes() / float(handle.getframerate())
    return wav_path, duration


def create_silence(output_stem: str, seconds: float) -> tuple[pathlib.Path, float]:
    TTS_DIR.mkdir(parents=True, exist_ok=True)
    wav_path = TTS_DIR / f"{output_stem}.wav"
    frame_rate = 22050
    sample_width = 2
    channels = 1
    frame_count = int(frame_rate * seconds)
    silence = b"\x00" * frame_count * sample_width * channels
    with wave.open(str(wav_path), "wb") as handle:
        handle.setnchannels(channels)
        handle.setsampwidth(sample_width)
        handle.setframerate(frame_rate)
        handle.writeframes(silence)
    return wav_path, seconds


def concatenate_audio(audio_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    if not audio_paths:
        raise RuntimeError("没有可拼接的音频片段")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(audio_paths[0]), "rb") as first:
        params = first.getparams()
        silence_frame_count = int(params.framerate * GAP_SECONDS)
        silence = b"\x00" * silence_frame_count * params.sampwidth * params.nchannels
    with wave.open(str(output_path), "wb") as output:
        output.setparams(params)
        for index, audio_path in enumerate(audio_paths):
            with wave.open(str(audio_path), "rb") as current:
                output.writeframes(current.readframes(current.getnframes()))
            if index < len(audio_paths) - 1:
                output.writeframes(silence)


def build_concat_clip(
    ffmpeg: str,
    *,
    source_video: pathlib.Path,
    excerpts: tuple[tuple[float, float], ...],
    output_path: pathlib.Path,
) -> dict[str, Any]:
    filter_parts: list[str] = []
    labels: list[str] = []
    clip_duration = 0.0
    for index, (start, end) in enumerate(excerpts):
        label = f"v{index}"
        filter_parts.append(
            f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS[{label}]"
        )
        labels.append(f"[{label}]")
        clip_duration += end - start
    filter_parts.append(f"{''.join(labels)}concat=n={len(excerpts)}:v=1:a=0[vout]")
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(source_video),
            "-filter_complex",
            ";".join(filter_parts),
            "-map",
            "[vout]",
            "-an",
            "-r",
            str(FPS),
            str(output_path),
        ]
    )
    return {
        "clip_path": str(output_path),
        "source_video": str(source_video),
        "excerpts": [{"start_seconds": start, "end_seconds": end} for start, end in excerpts],
        "source_total_seconds": round(clip_duration, 3),
    }


def render_image_segment(
    ffmpeg: str,
    *,
    image_path: pathlib.Path,
    audio_path: pathlib.Path,
    duration_seconds: float,
    output_path: pathlib.Path,
) -> None:
    run_command(
        [
            ffmpeg,
            "-y",
            "-loop",
            "1",
            "-framerate",
            str(FPS),
            "-i",
            str(image_path),
            "-i",
            str(audio_path),
            "-t",
            f"{duration_seconds:.3f}",
            "-vf",
            f"scale={WIDTH}:{HEIGHT},format=yuv420p",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            str(output_path),
        ]
    )


def render_video_segment(
    ffmpeg: str,
    *,
    clip_path: pathlib.Path,
    audio_path: pathlib.Path,
    duration_seconds: float,
    output_path: pathlib.Path,
) -> None:
    filter_graph = (
        "[0:v]crop=1800:1450:(iw-1800)/2:(ih-1450)/2[crop];"
        "[crop]split=2[fgsrc][bgsrc];"
        f"[bgsrc]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{HEIGHT},boxblur=20:8[bg];"
        f"[fgsrc]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease[fg];"
        f"[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]"
    )
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(clip_path),
            "-i",
            str(audio_path),
            "-t",
            f"{duration_seconds:.3f}",
            "-filter_complex",
            filter_graph,
            "-map",
            "[v]",
            "-map",
            "1:a",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            str(output_path),
        ]
    )


def write_script_file(segments: list[dict[str, Any]]) -> pathlib.Path:
    script_path = OUTPUT_DIR / "script.txt"
    lines = ["题目：《豆包的正确打开方式》", ""]
    for index, item in enumerate(segments, start=1):
        lines.append(
            f"第{index}段｜{item['block_name']}｜{item['carrier']}\n"
            f"口播：{item['voiceover_text'] or '（静默尾卡）'}\n"
            f"画面：{item['visual_note']}"
        )
        lines.append("")
    script_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return script_path


def write_captions(segments: list[dict[str, Any]]) -> pathlib.Path:
    captions_path = OUTPUT_DIR / "captions.srt"
    rows: list[str] = []
    index = 1
    cursor = 0.0
    for segment in segments:
        start = cursor
        end = cursor + segment["duration_seconds"]
        caption_text = segment["caption_text"].strip()
        if caption_text:
            rows.extend(
                [
                    str(index),
                    f"{seconds_to_srt(start)} --> {seconds_to_srt(end)}",
                    caption_text,
                    "",
                ]
            )
            index += 1
        cursor = end + GAP_SECONDS
    captions_path.write_text("\n".join(rows).strip() + "\n", encoding="utf-8")
    return captions_path


def concat_segments(ffmpeg: str, segment_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    concat_list = TEMP_DIR / "segments_concat.txt"
    concat_list.write_text(
        "\n".join(f"file '{path.resolve().as_posix()}'" for path in segment_paths) + "\n",
        encoding="utf-8",
    )
    run_command(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(output_path),
        ]
    )


def burn_review_subtitles(ffmpeg: str, *, clean_video: pathlib.Path, output_path: pathlib.Path) -> None:
    subtitles_filter = "subtitles=captions.srt"
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(clean_video),
            "-vf",
            subtitles_filter,
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "copy",
            str(output_path),
        ],
        cwd=OUTPUT_DIR,
    )


def export_review_frames(ffmpeg: str, *, video_path: pathlib.Path) -> list[str]:
    frame_dir = LOCAL_REVIEW_DIR / "review_frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    captures = [1.0, 12.0, 27.0, 42.0, 56.0, 70.0, 84.0]
    paths: list[str] = []
    for index, second in enumerate(captures, start=1):
        output = frame_dir / f"review_{index:02d}.jpg"
        run_command(
            [
                ffmpeg,
                "-y",
                "-ss",
                f"{second:.2f}",
                "-i",
                str(video_path),
                "-frames:v",
                "1",
                "-update",
                "1",
                str(output),
            ]
        )
        paths.append(str(output))
    return paths


def build_route_plan(segments: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "video_factory_vnext_route_plan/v1",
        "title": "豆包的正确打开方式",
        "task_object": "《豆包的正确打开方式》vNext",
        "route_profile": "api_human_user_footage_light_ppt_local_review",
        "video_route_strategy": "hook_shell + negative proof + positive two-step + summary + shell close + prompt tail",
        "constraints": {
            "copy_rule": "文案主干使用用户给定的 Perplexity 版本，不改核心措辞",
            "timing_rule": "不写死总时长，按素材与口播自然反推",
            "style_rule": "Minecraft-inspired inspired-only 原创体素方块风，不复用任何官方资产",
            "voice_route": {
                "provider": VOICE_ROUTE_PROVIDER,
                "voice_name": VOICE_NAME,
                "voice_rate": VOICE_RATE,
                "status": VOICE_ROUTE_STATUS,
                "blocked_reason": VOICE_ROUTE_BLOCKED_REASON,
                "current_implementation": "macOS say -> AIFF -> WAV",
            },
            "host_route": {
                "provider": HOST_ROUTE_PROVIDER,
                "status": HOST_ROUTE_STATUS,
                "blocked_reason": HOST_ROUTE_BLOCKED_REASON,
                "current_implementation": "PIL draw -> PNG -> ffmpeg -loop 1",
            },
        },
        "source_materials": {
            "negative": str(NEGATIVE_SOURCE),
            "positive": str(POSITIVE_SOURCE),
        },
        "material_mapping": {
            "negative": {
                "status": "部分成立",
                "source": str(NEGATIVE_SOURCE),
                "matched_input_on_screen": "帮我把这个方案整理一下",
                "used_for": "反面证明：画面里有长段落、表格和执行清单，但没有先压核心问题与主结构。",
                "missing_exact_evidence": [
                    "未在现有负面录屏中定位到“建议关注用户体验 / 建议加强品牌认知”这类原句。"
                ],
            },
            "positive_step_1": {
                "status": "已确认",
                "source": str(POSITIVE_SOURCE),
                "used_for": "一句策略判断 / 当前问题诊断 / 主结构 / 核心逻辑",
                "time_anchor_seconds": [0, 30, 45, 60, 90, 105],
            },
            "positive_xml_bridge": {
                "status": "已确认",
                "source": str(POSITIVE_SOURCE),
                "used_for": "XML 出现 -> 复制 -> 再粘贴回豆包",
                "time_anchor_seconds": [270, 280, 300, 310, 330],
            },
            "positive_ppt_result": {
                "status": "已确认",
                "source": str(POSITIVE_SOURCE),
                "used_for": "PPT 结果页、缩略图列表、最终页结构",
                "time_anchor_seconds": [580, 620, 660, 700],
            },
        },
        "blocks": [
            {
                "block_id": block_id,
                "block_name": segments_for_block[0]["block_name"],
                "carrier": segments_for_block[0]["carrier"],
                "segments": [
                    {
                        "segment_id": item["segment_id"],
                        "voiceover_text": item["voiceover_text"],
                        "caption_text": item["caption_text"],
                        "role": item["role"],
                        "accent": item["accent"],
                        "background": item["background"],
                        "visual_note": item["visual_note"],
                        "audio_duration_seconds": item["duration_seconds"],
                        "clip_plan": item.get("clip_plan"),
                        "rendered_asset": item["rendered_segment_path"],
                    }
                    for item in segments_for_block
                ],
            }
            for block_id in dict.fromkeys(item["block_id"] for item in segments)
            for segments_for_block in [[entry for entry in segments if entry["block_id"] == block_id]]
        ],
    }


def build_manifest(segments: list[dict[str, Any]], *, script_path: pathlib.Path, captions_path: pathlib.Path) -> dict[str, Any]:
    total_duration = 0.0
    timeline: list[dict[str, Any]] = []
    for item in segments:
        start = total_duration
        end = start + item["duration_seconds"]
        timeline.append(
            {
                "segment_id": item["segment_id"],
                "block_id": item["block_id"],
                "start_seconds": round(start, 3),
                "end_seconds": round(end, 3),
                "duration_seconds": round(item["duration_seconds"], 3),
            }
        )
        total_duration = end + GAP_SECONDS
    total_duration = max(0.0, total_duration - GAP_SECONDS)

    return {
        "schema_version": "video_factory_vnext_manifest/v1",
        "title": "豆包的正确打开方式",
        "output_dir": str(OUTPUT_DIR),
        "status": "blocked",
        "technical_validation": "passed",
        "content_validation": "blocked",
        "assembly_mode": "local_ffmpeg_review",
        "host_route": {
            "provider": HOST_ROUTE_PROVIDER,
            "status": HOST_ROUTE_STATUS,
            "technical_validation": "passed_local_render_only",
            "content_validation": "blocked",
            "blocked_reason": HOST_ROUTE_BLOCKED_REASON,
            "current_implementation": "PIL draw -> PNG -> ffmpeg -loop 1",
        },
        "voice_route": {
            "provider": VOICE_ROUTE_PROVIDER,
            "voice_name": VOICE_NAME,
            "voice_rate": VOICE_RATE,
            "status": VOICE_ROUTE_STATUS,
            "technical_validation": "passed_local_render_only",
            "content_validation": "blocked",
            "blocked_reason": VOICE_ROUTE_BLOCKED_REASON,
            "current_implementation": "macOS say -> AIFF -> WAV",
        },
        "artifacts": {
            "script": str(script_path),
            "captions": str(captions_path),
            "route_plan": str(OUTPUT_DIR / "route_plan.json"),
            "manifest": str(OUTPUT_DIR / "manifest.json"),
            "result_summary": str(OUTPUT_DIR / "result_summary.json"),
            "final_review_clean": str(LOCAL_REVIEW_DIR / "final_review_clean.mp4"),
            "final_review": str(LOCAL_REVIEW_DIR / "final_review.mp4"),
        },
        "segments": segments,
        "timeline": {
            "planned_total_duration_seconds": round(total_duration, 3),
            "gap_seconds_between_segments": GAP_SECONDS,
            "segments": timeline,
        },
        "notes": [
            "文案主干沿用用户提供的 Perplexity 版本，只做 block / segment、壳图、总结卡和尾卡补全。",
            "中段证据全部来自 `素材录制/*` 真实录屏。",
            "负面录屏可证明‘有内容但难改’，但未定位到用户点名的那两句泛空表达原文。",
            "当前输出目录已经切回本轮正式对象，但主持壳与声音路线都仍未达到 content_validation V1 合格线。",
        ],
    }


def build_result_summary(manifest: dict[str, Any], route_plan: dict[str, Any], review_frames: list[str]) -> dict[str, Any]:
    return {
        "schema_version": "video_factory_vnext_result_summary/v1",
        "stage": "local_review",
        "overall_status": "blocked",
        "generation_status": "success",
        "assembly_status": "success",
        "technical_validation": "passed",
        "content_validation": "blocked",
        "user_acceptance": "rejected_current_round",
        "send_ready": False,
        "artifact_paths": manifest["artifacts"],
        "review_frames": review_frames,
        "host_route": manifest["host_route"],
        "voice_route": manifest["voice_route"],
        "known_issues": [
            "当前开头 / 结尾主持壳仍是静态体素图循环成段，抽帧 0.2s 与 4.0s 可见主画面不变，不能冒充真实动态主持娃娃。",
            "声音路线当前使用 macOS `say` 的 `Flo (中文（中国大陆）)` 试配，只能算本地可渲染，不代表最低可听线达标。",
            "负面录屏的真实输入是“帮我把这个方案整理一下”，不是用户文字里点名的“给我一份方案”。",
            "负面录屏未定位到“建议关注用户体验 / 建议加强品牌认知”这类原句，只能用长段落 + 表格 + 无先诊断结构来证明差值。",
        ],
        "remaining_blockers": [
            HOST_ROUTE_BLOCKED_REASON,
            VOICE_ROUTE_BLOCKED_REASON,
            "如果要把这条内容升级到完全对齐用户口径，仍需要一段更明确的反面录屏，把“直接问方案 -> 空泛输出”录得更准。",
        ],
        "content_validation_v1": {
            "dynamic_host": {
                "status": "blocked",
                "reason": HOST_ROUTE_BLOCKED_REASON,
            },
            "voice": {
                "status": "blocked",
                "reason": VOICE_ROUTE_BLOCKED_REASON,
            },
            "materials": {
                "status": "部分成立",
                "reason": "正面 / XML / PPT 真实素材已对齐；反面录屏仍缺用户点名的最精确原句证据。",
            },
        },
        "route_summary": {
            "block_count": len(route_plan["blocks"]),
            "segment_count": len(manifest["segments"]),
            "source_materials": route_plan["source_materials"],
        },
    }


def main() -> int:
    ensure_tools_exist()
    ffmpeg = resolve_ffmpeg()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    TTS_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    shell_images = ensure_shell_images()

    rendered_segments: list[dict[str, Any]] = []
    audio_paths: list[pathlib.Path] = []

    for index, spec in enumerate(SEGMENTS, start=1):
        if spec.silent_seconds is not None:
            audio_path, duration_seconds = create_silence(spec.segment_id, spec.silent_seconds)
        else:
            audio_path, duration_seconds = synthesize_voice(spec.voiceover_text, spec.segment_id)
        audio_paths.append(audio_path)

        rendered_segment_path = SEGMENT_DIR / f"{index:02d}_{spec.segment_id}.mp4"
        clip_plan: dict[str, Any] | None = None

        if spec.visual_kind == "image":
            image_path = shell_images[spec.image_name or ""]
            render_image_segment(
                ffmpeg,
                image_path=image_path,
                audio_path=audio_path,
                duration_seconds=duration_seconds,
                output_path=rendered_segment_path,
            )
        elif spec.visual_kind == "video":
            clip_path = TEMP_DIR / f"{spec.segment_id}_curated.mp4"
            clip_plan = build_concat_clip(
                ffmpeg,
                source_video=spec.source_video or NEGATIVE_SOURCE,
                excerpts=spec.excerpts,
                output_path=clip_path,
            )
            render_video_segment(
                ffmpeg,
                clip_path=clip_path,
                audio_path=audio_path,
                duration_seconds=duration_seconds,
                output_path=rendered_segment_path,
            )
        else:
            raise RuntimeError(f"未知 visual_kind：{spec.visual_kind}")

        rendered_segments.append(
            {
                "segment_id": spec.segment_id,
                "block_id": spec.block_id,
                "block_name": spec.block_name,
                "carrier": spec.carrier,
                "asset_source": spec.asset_source,
                "voiceover_text": spec.voiceover_text,
                "caption_text": spec.caption_text,
                "visual_kind": spec.visual_kind,
                "role": spec.role,
                "eyebrow": spec.eyebrow,
                "headline": spec.headline,
                "support": spec.support,
                "detail": spec.detail,
                "chips": list(spec.chips),
                "accent": spec.accent,
                "background": spec.background,
                "visual_note": spec.visual_note,
                "audio_path": str(audio_path),
                "duration_seconds": round(duration_seconds, 3),
                "rendered_segment_path": str(rendered_segment_path),
                "clip_plan": clip_plan,
            }
        )

    combined_audio_path = TTS_DIR / "voiceover_combined.wav"
    concatenate_audio(audio_paths, combined_audio_path)

    script_path = write_script_file(rendered_segments)
    captions_path = write_captions(rendered_segments)
    route_plan = build_route_plan(rendered_segments)
    manifest = build_manifest(rendered_segments, script_path=script_path, captions_path=captions_path)

    clean_video = LOCAL_REVIEW_DIR / "final_review_clean.mp4"
    review_video = LOCAL_REVIEW_DIR / "final_review.mp4"

    concat_segments(
        ffmpeg,
        [pathlib.Path(item["rendered_segment_path"]) for item in rendered_segments],
        clean_video,
    )
    burn_review_subtitles(ffmpeg, clean_video=clean_video, output_path=review_video)
    review_frames = export_review_frames(ffmpeg, video_path=clean_video)

    manifest["voice_route"]["combined_audio_path"] = str(combined_audio_path)

    route_plan_path = OUTPUT_DIR / "route_plan.json"
    manifest_path = OUTPUT_DIR / "manifest.json"
    result_summary_path = OUTPUT_DIR / "result_summary.json"

    route_plan_path.write_text(json.dumps(route_plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result_summary = build_result_summary(manifest, route_plan, review_frames)
    result_summary_path.write_text(json.dumps(result_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "output_dir": str(OUTPUT_DIR),
                "final_review_clean": str(clean_video),
                "final_review": str(review_video),
                "script": str(script_path),
                "captions": str(captions_path),
                "route_plan": str(route_plan_path),
                "manifest": str(manifest_path),
                "result_summary": str(result_summary_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
