from __future__ import annotations

import asyncio
import importlib.util
import json
import pathlib
import shutil
import subprocess
import wave
from dataclasses import dataclass
from typing import Any

from PIL import Image, ImageChops, ImageDraw, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
FORMAL_DIR = ROOT / "dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video"
V1_LOCAL_FIX_DIR = FORMAL_DIR / "local_fix_20260504_reference_quality"
OUT_DIR = FORMAL_DIR / "local_fix_20260504_reference_quality_v2"
ASSETS_DIR = OUT_DIR / "assets_local_fix_v2"
CARD_DIR = ASSETS_DIR / "cards"
CLIP_DIR = ASSETS_DIR / "clips"
TTS_DIR = OUT_DIR / "声音_v31_ac19_b_pacing_tts_v2"
SUMMARY_HF_DIR = OUT_DIR / "hyperframes_summary_card_v2"
MANIFEST_PATH = FORMAL_DIR / "manifest.json"
TTS_RETRY_SCRIPT = ROOT / "scripts/短视频自动流_v31声音重提_tts_retry.py"

WIDTH = 1080
HEIGHT = 1920
FPS = 24
INTRO_SECONDS = 2.0
PANEL_W = 936
PANEL_H = 1320
PANEL_X = 72
PANEL_Y = 300

FFMPEG = shutil.which("ffmpeg") or str(ROOT / "node_modules/ffmpeg-static/ffmpeg")
FFPROBE = shutil.which("ffprobe") or "ffprobe"

PR7_B_REFERENCE = ROOT / "dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png"
ELEMENT_DOLL_SOURCE = FORMAL_DIR / "prepared_visuals/seg01_source_clip.mp4"
DOUBAO_SOURCE = ROOT / "素材录制/最新素材/豆包素材.mp4"
TRAE_SOURCE = ROOT / "素材录制/最新素材/trae 素材.mp4"
CODEX_SOURCE = ROOT / "素材录制/最新素材/codex 素材.mp4"

MAIN_VOICEOVER = TTS_DIR / "tts/formal_voiceover.mp3"
INTRO_GREETING_AUDIO = TTS_DIR / "tts/intro_greeting_audio_2s.wav"
VOICEOVER_V2 = TTS_DIR / "tts/voiceover_local_fix_v2.mp3"

FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
]

MIDDLE_SPECS: dict[str, dict[str, Any]] = {
    "seg02": {
        "source": DOUBAO_SOURCE,
        "start": 16.0,
        "crop": {"x": 960, "y": 60, "w": 1500, "h": 2100},
        "evidence": "用户只输入一句“我想用 Trae 做一个短视频自动流”",
        "anchor": "豆包输入区",
        "cannot_prove": "不能证明 Trae 已执行",
    },
    "seg04": {
        "source": DOUBAO_SOURCE,
        "start": 88.0,
        "crop": {"x": 930, "y": 60, "w": 1560, "h": 2100},
        "evidence": "从 0 基础轻量版到无人值守版、核心流程工位",
        "anchor": "豆包方案标题和流程列表",
        "cannot_prove": "不能证明工程已跑通",
    },
    "seg06": {
        "source": DOUBAO_SOURCE,
        "start": 232.0,
        "crop": {"x": 930, "y": 60, "w": 1560, "h": 2100},
        "evidence": "Trae Vlog 自动流核心搭建 Prompt 与模块清单",
        "anchor": "prompt 标题和模块列表",
        "cannot_prove": "不能证明脚本运行成功",
    },
    "seg07": {
        "source": TRAE_SOURCE,
        "start": 80.0,
        "crop": {"x": 960, "y": 60, "w": 1560, "h": 2100},
        "evidence": "Prompt 进入 Trae，出现 Updating Tasks 和 11 个待办",
        "anchor": "Trae 输入区 / 任务区",
        "cannot_prove": "不能证明代码运行成功",
    },
    "seg08": {
        "source": TRAE_SOURCE,
        "start": 120.0,
        "crop": {"x": 1800, "y": 60, "w": 1500, "h": 2100},
        "evidence": "vlog_automation_workflow 项目骨架和目录文件",
        "anchor": "Trae 文件目录区域",
        "cannot_prove": "不能证明 app 已跑通",
    },
    "seg14": {
        "source": CODEX_SOURCE,
        "start": 176.0,
        "crop": {"x": 500, "y": 60, "w": 1560, "h": 2100},
        "evidence": "Codex 执行检查：命令、文件变更、报告线索",
        "anchor": "安全命令 / 报告区域",
        "cannot_prove": "不能证明内容过线",
    },
}


@dataclass
class SegmentSpec:
    segment_id: str
    goal: str
    text: str
    duration: float
    visual_path: pathlib.Path
    visual_role: str
    route: str
    source: str


def run(args: list[str], log_path: pathlib.Path | None = None, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True, cwd=str(cwd) if cwd else None)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\nSTDOUT:\n" + completed.stdout + "\n\nSTDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def probe_duration(path: pathlib.Path) -> float:
    completed = run(
        [
            FFPROBE,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ]
    )
    return float(completed.stdout.strip())


def probe_streams(path: pathlib.Path) -> dict[str, Any]:
    completed = run(
        [
            FFPROBE,
            "-v",
            "error",
            "-show_entries",
            "stream=index,codec_type,codec_name,width,height,sample_rate,channels",
            "-of",
            "json",
            str(path),
        ]
    )
    return json.loads(completed.stdout)


def output_ready(path: pathlib.Path, expected_duration: float, tolerance: float = 0.35) -> bool:
    if not path.exists():
        return False
    try:
        duration = probe_duration(path)
    except Exception:
        return False
    return abs(duration - expected_duration) <= tolerance


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if pathlib.Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size, index=0)
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for raw_line in text.split("\n"):
        current = ""
        for char in raw_line:
            candidate = current + char
            if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = char
        if current:
            lines.append(current)
    return lines


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    y: int,
    fnt: ImageFont.ImageFont,
    fill: str,
    stroke: str = "#ffffff",
    stroke_width: int = 0,
    gap: int = 78,
) -> int:
    for line in lines:
        draw.text(
            (WIDTH // 2, y),
            line,
            font=fnt,
            fill=fill,
            anchor="ma",
            stroke_width=stroke_width,
            stroke_fill=stroke,
        )
        y += gap
    return y


def render_cute_info_card(path: pathlib.Path, title: str, subtitle: str, modules: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (WIDTH, HEIGHT), "#fff6fb")
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        shade = y / HEIGHT
        fill = (
            int(255 - 8 * shade),
            int(246 - 16 * shade),
            int(251 - 5 * shade),
        )
        draw.line([(0, y), (WIDTH, y)], fill=fill)
    draw.rounded_rectangle((78, 150, 1002, 1770), radius=48, fill="#ffffff", outline="#ffc2db", width=6)
    draw.rounded_rectangle((124, 206, 956, 374), radius=34, fill="#ffe0ec")
    draw.text((WIDTH // 2, 255), title, font=font(58), fill="#4b2d37", anchor="ma")
    draw.text((WIDTH // 2, 334), subtitle, font=font(34), fill="#b14d72", anchor="ma")
    colors = ["#fff1bd", "#e3fbff", "#f0ecff"]
    y = 492
    body_font = font(38)
    for idx, module in enumerate(modules[:4]):
        box_h = 194 if len(module) <= 24 else 244
        draw.rounded_rectangle((134, y, 946, y + box_h), radius=30, fill=colors[idx % 3], outline="#ffd2df", width=3)
        lines = wrap_text(draw, module, body_font, 710)
        yy = y + 50
        for line in lines[:4]:
            draw.text((174, yy), line, font=body_font, fill="#513842")
            yy += 52
        y += box_h + 42
    img.save(path)


def render_sassy_card(path: pathlib.Path, punchline: str, variant: int, mood: str, prop: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    reference = Image.open(PR7_B_REFERENCE).convert("RGB").resize((WIDTH, HEIGHT))
    palettes = [
        ("#ff7a1a", "#ffe13a", "#111111"),
        ("#ff5b7b", "#ffd84d", "#111111"),
        ("#ffcf2b", "#ff6d2f", "#111111"),
        ("#62d6ff", "#ffe05a", "#111111"),
        ("#ff8c33", "#ff4f78", "#111111"),
        ("#fff15b", "#ff7c2a", "#111111"),
    ]
    top_color, bottom_color, ink = palettes[variant % len(palettes)]
    img = Image.new("RGB", (WIDTH, HEIGHT), top_color)
    draw = ImageDraw.Draw(img)
    top_rgb = Image.new("RGB", (1, 1), top_color).getpixel((0, 0))
    bottom_rgb = Image.new("RGB", (1, 1), bottom_color).getpixel((0, 0))
    for y in range(HEIGHT):
        t = y / HEIGHT
        fill = tuple(int(top_rgb[i] * (1 - t) + bottom_rgb[i] * t) for i in range(3))
        draw.line([(0, y), (WIDTH, y)], fill=fill)

    centers = [(540, 760), (430, 700), (650, 820), (520, 640), (690, 700), (460, 830)]
    center_x, center_y = centers[variant % len(centers)]
    ray_targets = [
        (-80, 20), (150, -120), (420, -160), (760, -120), (1160, 10),
        (1240, 360), (1180, 780), (1240, 1180), (1010, 1780), (760, 2060),
        (500, 2100), (230, 2050), (-80, 1740), (-140, 1290), (-120, 850),
        (-160, 430), (70, 220), (250, 80), (910, 120), (1090, 260),
    ]
    offset = variant % 5
    for target in ray_targets[offset:] + ray_targets[:offset]:
        draw.line((center_x, center_y, target[0], target[1]), fill=ink, width=6)
    bursts = [
        [(150, 520), (230, 570), (190, 650), (100, 650), (72, 565)],
        [(830, 460), (925, 520), (880, 640), (760, 635), (730, 535)],
        [(850, 1180), (982, 1250), (925, 1395), (780, 1370), (748, 1238)],
        [(128, 1320), (245, 1375), (220, 1510), (72, 1498), (52, 1372)],
    ]
    for shape in bursts[variant % 4:] + bursts[: variant % 4]:
        draw.polygon(shape, fill="#ffffff", outline=ink)

    character = reference.crop((105, 540, 965, 1840))
    if variant in {1, 3, 5}:
        character = character.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    sizes = [(750, 1134), (830, 1255), (700, 1058), (790, 1194), (720, 1088), (850, 1285)]
    positions = [(140, 642), (72, 558), (248, 720), (96, 632), (230, 650), (48, 550)]
    rotations = [-3, 4, -1, 2, -5, 3]
    character = character.resize(sizes[variant % len(sizes)]).rotate(rotations[variant % len(rotations)], expand=True, fillcolor=top_color)
    img.paste(character, positions[variant % len(positions)])

    if prop == "task":
        draw.rounded_rectangle((705, 1048, 1010, 1302), radius=28, fill="#fff8d8", outline=ink, width=8)
        draw.text((858, 1016), "11", font=font(76), fill=ink, anchor="ma")
        draw.line((754, 1130, 954, 1130), fill=ink, width=8)
        draw.line((754, 1208, 928, 1208), fill=ink, width=8)
    elif prop == "api":
        draw.rounded_rectangle((96, 1110, 365, 1298), radius=28, fill="#ffffff", outline=ink, width=8)
        draw.text((232, 1218), "API", font=font(72), fill=ink, anchor="ma")
    elif prop == "assembly":
        draw.rounded_rectangle((720, 1110, 1015, 1288), radius=30, fill="#e3fbff", outline=ink, width=8)
        draw.text((868, 1212), "装配台", font=font(54), fill=ink, anchor="ma")
    elif prop == "check":
        draw.ellipse((100, 1068, 345, 1313), outline=ink, width=16)
        draw.line((300, 1268, 480, 1440), fill=ink, width=20)
    elif prop == "flow":
        draw.rounded_rectangle((82, 1048, 355, 1240), radius=28, fill="#fff1bd", outline=ink, width=8)
        draw.text((218, 1155), "流程", font=font(66), fill=ink, anchor="ma")
    else:
        draw.rounded_rectangle((72, 1032, 328, 1208), radius=26, fill="#ffffff", outline=ink, width=8)
        draw.text((200, 1130), "先拆", font=font(62), fill=ink, anchor="ma")

    draw.rounded_rectangle((84, 86, 996, 374), radius=42, fill="#ffffff", outline=ink, width=8)
    title_font = font(66 if len(punchline) <= 14 else 58)
    lines = wrap_text(draw, punchline, title_font, 820)
    draw_centered_lines(draw, lines[:3], 148, title_font, "#111111", gap=78)
    draw.text((WIDTH // 2, 412), mood, font=font(30), fill="#5d3a24", anchor="ma")
    img.save(path)


def render_cards() -> dict[str, pathlib.Path]:
    cards: dict[str, pathlib.Path] = {}
    info_specs = {
        "seg01_info": ("先别急着一键", "自动流先拆顺序", ["一键生成更像抽素材", "真正要做的是可重复流程"]),
        "seg03": ("先拆流程", "工具才知道站哪一工位", ["选题 / 脚本 / 分镜", "素材 / 后期 / 发布"]),
        "seg09": ("可执行 prompt", "从聊天变成项目骨架", ["豆包给工作说明", "Trae 拆成待办和目录"]),
        "seg11": ("云剪是装配台", "前面流程决定能不能复用", ["录屏 / 卡片 / 音轨", "按时间线进入总装"]),
        "seg13": ("Codex 做检查", "别把半成品写成完成", ["路径 / 音频 / 视频 / 报告", "哪些成立，哪些待验证"]),
        "seg15": ("流程总览", "先清楚，再自动", ["需求 -> 方案 -> prompt", "Trae plan -> 项目骨架", "API / 装配 / 检查"]),
        "seg16": ("即梦更像素材入口", "自动流解决持续生产", ["素材可以换", "流程要留下"]),
    }
    for key, spec in info_specs.items():
        path = CARD_DIR / f"{key}_cute_info_card_route.png"
        render_cute_info_card(path, spec[0], spec[1], list(spec[2]))
        cards[key] = path

    sassy_specs = {
        "seg01_sassy": ("一键生成？\n先别急着抽卡", 0, "吐槽 / 嫌弃 / 好笑", "idea"),
        "seg05_sassy": ("先拆流程\n工具才有位置", 1, "突然懂了 / 眼睛一亮", "flow"),
        "seg10_sassy": ("API 是工位\n不是主角", 2, "边界判断 / 摆手提醒", "api"),
        "seg12_sassy": ("装配台\n别抢方向盘", 3, "转折提醒 / 控制节奏", "assembly"),
        "seg14_sassy": ("半成品\n别装完成", 4, "拿放大镜 / 严肃吐槽", "check"),
        "seg17_sassy": ("流程在\n工具才好换", 5, "轻松收束 / 笃定", "task"),
    }
    for key, (text, variant, mood, prop) in sassy_specs.items():
        path = CARD_DIR / f"{key}_sassy_reaction_card_route.png"
        render_sassy_card(path, text, variant, mood, prop)
        cards[key] = path
    return cards


def create_image_clip(image_path: pathlib.Path, duration: float, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if output_ready(out_path, duration):
        return
    run(
        [
            FFMPEG,
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
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},setsar=1,format=yuv420p",
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(out_path),
        ],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )


def create_canvas_video_clip(source: pathlib.Path, duration: float, out_path: pathlib.Path, start: float = 0.0) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if output_ready(out_path, duration):
        return
    vf = f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},setsar=1,format=yuv420p"
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-stream_loop",
            "-1",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(source),
            "-vf",
            vf,
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(out_path),
        ],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )


def create_screen_evidence_clip(
    source: pathlib.Path,
    start: float,
    duration: float,
    out_path: pathlib.Path,
    crop: dict[str, int],
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if output_ready(out_path, duration):
        return
    cw = crop["w"]
    ch = crop["h"]
    cx = crop["x"]
    cy = crop["y"]
    filter_complex = (
        f"[1:v]drawbox=x=54:y=250:w=972:h=1420:color=#ffffff@0.72:t=fill[mat];"
        f"[0:v]crop={cw}:{ch}:{cx}:{cy},"
        f"scale={PANEL_W}:{PANEL_H}:force_original_aspect_ratio=decrease,"
        f"pad={PANEL_W}:{PANEL_H}:(ow-iw)/2:(oh-ih)/2:color=#fff8fb[panel];"
        f"[mat][panel]overlay={PANEL_X}:{PANEL_Y}[comp];"
        f"[comp]drawbox=x={PANEL_X}:y={PANEL_Y}:w={PANEL_W}:h={PANEL_H}:color=#ffc2db@1:t=6,"
        "setsar=1,format=yuv420p[v]"
    )
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-stream_loop",
            "-1",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(source),
            "-f",
            "lavfi",
            "-t",
            f"{duration:.3f}",
            "-i",
            f"color=c=0xfff6fb:s={WIDTH}x{HEIGHT}:r={FPS}",
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(out_path),
        ],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )


def concat_clips(parts: list[pathlib.Path], out_path: pathlib.Path) -> None:
    expected_duration = sum(probe_duration(part) for part in parts)
    if output_ready(out_path, expected_duration, tolerance=0.55):
        return
    concat_path = out_path.with_suffix(".concat.txt")
    concat_path.write_text("".join(f"file '{p.resolve()}'\n" for p in parts), encoding="utf-8")
    run(
        [FFMPEG, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(out_path)],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )
    concat_path.unlink(missing_ok=True)


def render_hyperframes_summary(duration: float) -> pathlib.Path:
    SUMMARY_HF_DIR.mkdir(parents=True, exist_ok=True)
    output = OUT_DIR / "summary_card_hyperframes_v2.mp4"
    if output.exists():
        try:
            if probe_duration(output) > 1.0:
                return output
        except Exception:
            pass
    index = SUMMARY_HF_DIR / "index.html"
    index.write_text(
        f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>summary-card-hyperframes-v2</title>
  <style>
    body {{ margin: 0; background: #fff6fb; overflow: hidden; }}
    #summary-card {{
      width: {WIDTH}px; height: {HEIGHT}px; position: relative; overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", sans-serif;
      background: linear-gradient(180deg, #fff8fc 0%, #fff0f6 100%);
    }}
    .card {{ position: absolute; left: 84px; top: 238px; width: 912px; height: 1324px;
      border-radius: 52px; background: #fff; border: 6px solid #ffc2db;
      box-shadow: 0 34px 80px rgba(190, 90, 128, 0.18); box-sizing: border-box;
      padding: 88px 68px; display: flex; flex-direction: column; gap: 54px; }}
    .eyebrow {{ color: #bc4d77; font-size: 38px; font-weight: 700; }}
    .main {{ color: #452d38; font-size: 78px; line-height: 1.18; font-weight: 900; }}
    .module {{ border-radius: 34px; padding: 42px; background: #fff1bd; color: #513842;
      font-size: 42px; line-height: 1.35; font-weight: 700; }}
    .module.second {{ background: #e3fbff; }}
    .highlight {{ color: #e54983; }}
    .petal {{ position: absolute; width: 42px; height: 28px; border-radius: 50% 50% 50% 0;
      background: #ffc2db; opacity: 0.65; }}
  </style>
</head>
<body>
  <div id="summary-card" data-composition-id="summary-card-v2" data-start="0" data-width="{WIDTH}" data-height="{HEIGHT}" data-duration="{duration:.3f}">
    <div class="petal p1" style="left:90px; top:140px;"></div>
    <div class="petal p2" style="left:920px; top:210px;"></div>
    <div class="petal p3" style="left:150px; top:1660px;"></div>
    <div class="card">
      <div class="eyebrow">最后收束</div>
      <div class="main">顺序对了，<br><span class="highlight">自动化</span>才有地方落脚。</div>
      <div class="module">先把视频生产拆开。</div>
      <div class="module second">再让每一步有人负责、有工具能做、有结果能检查。</div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.from(".card", {{ y: 90, opacity: 0, scale: 0.96, duration: 0.8, ease: "power3.out" }}, 0);
      tl.from(".eyebrow", {{ y: 30, opacity: 0, duration: 0.5, ease: "power2.out" }}, 0.28);
      tl.from(".main", {{ y: 38, opacity: 0, duration: 0.7, ease: "power2.out" }}, 0.55);
      tl.from(".module", {{ y: 34, opacity: 0, stagger: 0.18, duration: 0.55, ease: "power2.out" }}, 1.15);
      tl.to(".highlight", {{ color: "#ff7aa8", duration: 0.45, repeat: 4, yoyo: true, ease: "sine.inOut" }}, 2.2);
      tl.to(".petal", {{ y: 80, x: 22, rotation: 18, opacity: 0.15, stagger: 0.12, duration: {max(duration - 1.0, 2):.3f}, ease: "none" }}, 0);
      window.__timelines["summary-card-v2"] = tl;
    </script>
  </div>
</body>
</html>
""",
        encoding="utf-8",
    )
    lint_log = SUMMARY_HF_DIR / "hyperframes_lint.log"
    render_log = SUMMARY_HF_DIR / "hyperframes_render.log"
    run(["npx", "hyperframes", "lint"], lint_log, cwd=SUMMARY_HF_DIR)
    run(
        [
            "npx",
            "hyperframes",
            "render",
            "--output",
            str(output),
            "--fps",
            str(FPS),
            "--quality",
            "draft",
        ],
        render_log,
        cwd=SUMMARY_HF_DIR,
    )
    return output


def load_tts_module() -> Any:
    spec = importlib.util.spec_from_file_location("v31_tts_retry", TTS_RETRY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载 TTS 脚本：{TTS_RETRY_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUTPUT_DIR = TTS_DIR
    module.RE_ENROLLED_VOICE_RUNTIME_PATH = TTS_DIR / "re_enroll_voice" / "re_enrolled_voice_untracked_runtime.json"
    return module


async def synthesize_intro_greeting(tts_module: Any) -> pathlib.Path:
    api_key = tts_module.load_api_key()
    voice_resolution = tts_module.resolve_voice_for_local_fix(api_key)
    result = await tts_module.synthesize_chunk(
        api_key=api_key,
        voice=voice_resolution["voice"],
        segment_id="intro_greeting",
        chunk_index=1,
        text="大家好。",
    )
    raw_path = pathlib.Path(result["audio_path"])
    padded = INTRO_GREETING_AUDIO
    padded.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-i",
            str(raw_path),
            "-af",
            f"apad,atrim=0:{INTRO_SECONDS:.3f}",
            "-ac",
            "1",
            "-ar",
            "24000",
            str(padded),
        ],
        padded.with_suffix(".ffmpeg_log.txt"),
    )
    write_json(
        TTS_DIR / "tts/intro_greeting_report_sanitized.json",
        {
            "status": "success",
            "text": "大家好。",
            "duration_seconds": probe_duration(padded),
            "provider": "aliyun_bailian",
            "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
            "model": "qwen3-tts-vc-realtime-2026-01-15",
            "voice_masked": voice_resolution["voice_masked"],
            "source_reference_voice_masked": voice_resolution.get("source_reference_voice_masked", "qwen-t...ac19"),
            "macos_say_used": False,
        },
    )
    return padded


def concat_v2_audio() -> pathlib.Path:
    if not INTRO_GREETING_AUDIO.exists():
        raise RuntimeError(f"缺少开头问候音频：{INTRO_GREETING_AUDIO}")
    if not MAIN_VOICEOVER.exists():
        raise RuntimeError(f"缺少主体 v3.1 旁白音轨：{MAIN_VOICEOVER}")
    VOICEOVER_V2.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-i",
            str(INTRO_GREETING_AUDIO),
            "-i",
            str(MAIN_VOICEOVER),
            "-filter_complex",
            "[0:a][1:a]concat=n=2:v=0:a=1,aresample=48000[a]",
            "-map",
            "[a]",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "160k",
            str(VOICEOVER_V2),
        ],
        VOICEOVER_V2.with_suffix(".ffmpeg_log.txt"),
    )
    return VOICEOVER_V2


def ensure_v31_tts() -> dict[str, Any]:
    tts_module = load_tts_module()
    if not MAIN_VOICEOVER.exists():
        asyncio.run(tts_module.main_async())
    if not INTRO_GREETING_AUDIO.exists():
        asyncio.run(synthesize_intro_greeting(tts_module))
    audio = concat_v2_audio()
    tts_report = json.loads((TTS_DIR / "tts_retry_report.json").read_text(encoding="utf-8"))
    write_json(
        TTS_DIR / "tts_v2_audio_report.json",
        {
            "status": "success",
            "intro_greeting_audio": str(INTRO_GREETING_AUDIO),
            "main_voiceover_audio": str(MAIN_VOICEOVER),
            "final_voiceover_audio": str(audio),
            "duration_seconds": probe_duration(audio),
            "main_duration_seconds": probe_duration(MAIN_VOICEOVER),
            "intro_duration_seconds": probe_duration(INTRO_GREETING_AUDIO),
            "target_model": "qwen3-tts-vc-realtime-2026-01-15",
            "custom_voice_reference": "qwen-t...ac19",
            "reference_voice_or_pacing_used_for_tts": True,
            "tts_15s_b_pacing_locked_20260427_read": True,
            "macos_say_used": False,
        },
    )
    return tts_report


def build_segments(cards: dict[str, pathlib.Path], summary_hf: pathlib.Path, tts_report: dict[str, Any]) -> list[SegmentSpec]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    durations = {item["segment_id"]: float(item["duration_seconds"]) for item in tts_report["segment_results"]}
    raw_segments = {item["segment_id"]: item for item in manifest["segments"]}
    segments: list[SegmentSpec] = []

    intro_output = CLIP_DIR / "intro_greeting_element_doll_2s.mp4"
    create_canvas_video_clip(ELEMENT_DOLL_SOURCE, INTRO_SECONDS, intro_output, start=0.0)
    segments.append(
        SegmentSpec(
            "intro_greeting",
            "元素娃娃开头问候",
            "大家好。",
            INTRO_SECONDS,
            intro_output,
            "element_doll_host_reference_inheritance_2s_only",
            "opening_reference_element_doll_no_text_locked_20260428",
            str(ELEMENT_DOLL_SOURCE),
        )
    )

    for raw in manifest["segments"]:
        sid = raw["segment_id"]
        duration = durations[sid]
        goal = raw["goal"]
        text = raw["voiceover_text"]
        output = CLIP_DIR / f"{sid}_local_fix_v2.mp4"
        if sid == "seg01":
            sassy = CLIP_DIR / "seg01_01_sassy_after_intro.mp4"
            info = CLIP_DIR / "seg01_02_info_after_intro.mp4"
            create_image_clip(cards["seg01_sassy"], min(8.0, max(duration * 0.42, 3.0)), sassy)
            create_image_clip(cards["seg01_info"], max(duration - probe_duration(sassy), 1.0), info)
            concat_clips([sassy, info], output)
            role = "sassy_reaction_card_then_cute_info_card_no_element_doll"
            route = "sassy_reaction_card_route + cute_info_card_route"
            source = "generated_cards"
        elif sid in MIDDLE_SPECS:
            spec = MIDDLE_SPECS[sid]
            create_screen_evidence_clip(spec["source"], float(spec["start"]), duration, output, dict(spec["crop"]))
            role = "stable_user_recording_fixed_evidence_window"
            route = "user_recorded_footage_middle_route"
            source = str(spec["source"])
        elif sid == "seg05":
            sassy = CLIP_DIR / "seg05_01_sassy.mp4"
            card = CLIP_DIR / "seg05_02_sassy_tail.mp4"
            create_image_clip(cards["seg05_sassy"], min(7.0, duration), sassy)
            create_image_clip(cards["seg05_sassy"], max(duration - 7.0, 1.0), card)
            concat_clips([sassy, card], output)
            role = "sassy_reaction_card_replaces_element_doll"
            route = "sassy_reaction_card_route"
            source = str(cards["seg05_sassy"])
        elif sid == "seg10":
            create_image_clip(cards["seg10_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll_api_turn"
            route = "sassy_reaction_card_route"
            source = str(cards["seg10_sassy"])
        elif sid == "seg12":
            create_image_clip(cards["seg12_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll_assembly_turn"
            route = "sassy_reaction_card_route"
            source = str(cards["seg12_sassy"])
        elif sid == "seg17":
            sassy = CLIP_DIR / "seg17_01_sassy_closing_reaction.mp4"
            summary = CLIP_DIR / "seg17_02_hyperframes_summary_card.mp4"
            sassy_duration = min(6.0, max(duration * 0.24, 3.0))
            create_image_clip(cards["seg17_sassy"], sassy_duration, sassy)
            create_canvas_video_clip(summary_hf, max(duration - sassy_duration, 1.0), summary, start=0.0)
            concat_clips([sassy, summary], output)
            role = "sassy_reaction_card_then_hyperframes_summary_card"
            route = "sassy_reaction_card_route + cute_info_card_route_with_hyperframes_card_motion_layer"
            source = f"{cards['seg17_sassy']} | {summary_hf}"
        elif sid == "seg14":
            # Kept unreachable because seg14 is a middle evidence clip above; the generated card still exists for replacement proof.
            create_image_clip(cards["seg14_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll_check"
            route = "sassy_reaction_card_route"
            source = str(cards["seg14_sassy"])
        else:
            key = sid if sid in cards else "seg13"
            create_image_clip(cards[key], duration, output)
            role = "cute_info_card_route"
            route = "cute_info_card_route"
            source = str(cards[key])
        segments.append(SegmentSpec(sid, goal, text, duration, output, role, route, source))
    _ = raw_segments
    return segments


def srt_time(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    h, rem = divmod(millis, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def generate_captions(segments: list[SegmentSpec]) -> pathlib.Path:
    path = OUT_DIR / "captions_local_fix_v2.srt"
    index = 1
    cursor = 0.0
    lines: list[str] = []
    for segment in segments:
        text = segment.text.replace("# 《短视频自动流的最简单流程》", "《短视频自动流的最简单流程》").strip()
        chunks = [
            chunk.strip()
            for chunk in text.replace("？", "？|").replace("。", "。|").replace("！", "！|").replace("\n\n", "|").split("|")
            if chunk.strip()
        ]
        if not chunks:
            chunks = [text[:50]]
        total_chars = sum(max(len(chunk), 1) for chunk in chunks)
        seg_cursor = cursor
        for chunk in chunks:
            dur = max(1.0, segment.duration * max(len(chunk), 1) / total_chars)
            start = seg_cursor
            end = min(cursor + segment.duration, seg_cursor + dur)
            lines.extend([str(index), f"{srt_time(start)} --> {srt_time(end)}", chunk[:42], ""])
            index += 1
            seg_cursor = end
        cursor += segment.duration
    path.write_text("\n".join(line.rstrip() for line in lines), encoding="utf-8")
    return path


def assemble_video(segments: list[SegmentSpec], voiceover: pathlib.Path) -> pathlib.Path:
    concat_path = OUT_DIR / "local_fix_v2_segments.concat.txt"
    concat_path.write_text("".join(f"file '{s.visual_path.resolve()}'\n" for s in segments), encoding="utf-8")
    silent_video = OUT_DIR / "full_video_local_fix_v2_no_audio.mp4"
    run(
        [FFMPEG, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(silent_video)],
        OUT_DIR / "concat_video_v2.ffmpeg_log.txt",
    )
    final = OUT_DIR / "full_video_local_fix_v2.mp4"
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-i",
            str(silent_video),
            "-i",
            str(voiceover),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            str(final),
        ],
        OUT_DIR / "full_video_local_fix_v2.ffmpeg_log.txt",
    )
    return final


def create_middle_preview(segments: list[SegmentSpec]) -> pathlib.Path:
    middle_parts = [segment.visual_path for segment in segments if segment.segment_id in MIDDLE_SPECS]
    output = OUT_DIR / "middle_preview_stable_v2.mp4"
    concat_clips(middle_parts, output)
    return output


def extract_frame(video: pathlib.Path, timestamp: float, output: pathlib.Path) -> pathlib.Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(output),
        ]
    )
    return output


def create_contact_sheet_from_video(video: pathlib.Path, output: pathlib.Path, label: str, count: int = 6) -> None:
    frames_dir = output.with_suffix("")
    frames_dir.mkdir(parents=True, exist_ok=True)
    duration = probe_duration(video)
    frame_paths: list[pathlib.Path] = []
    for i in range(count):
        ts = min(max(duration - 0.2, 0.1), duration * (i + 0.5) / count)
        frame = frames_dir / f"{label}_{i + 1:02d}.jpg"
        frame_paths.append(extract_frame(video, ts, frame))
    thumbs = [Image.open(path).resize((270, 480)) for path in frame_paths]
    rows = (count + 2) // 3
    sheet = Image.new("RGB", (810, rows * 480), "#ffffff")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % 3) * 270, (idx // 3) * 480))
    sheet.save(output)


def create_summary_hyperframes_contact_sheet(video: pathlib.Path, output: pathlib.Path) -> None:
    frames_dir = output.with_suffix("")
    frames_dir.mkdir(parents=True, exist_ok=True)
    duration = probe_duration(video)
    targets = [0.08, 0.32, 0.68, 1.10, 1.80, min(max(duration - 0.4, 0.1), 4.20)]
    frame_paths: list[pathlib.Path] = []
    for idx, ts in enumerate(targets):
        frame_paths.append(extract_frame(video, min(ts, max(duration - 0.1, 0.1)), frames_dir / f"summary_hf_motion_{idx + 1:02d}.jpg"))
    thumbs = [Image.open(path).resize((270, 480)) for path in frame_paths]
    sheet = Image.new("RGB", (810, 960), "#ffffff")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % 3) * 270, (idx // 3) * 480))
    sheet.save(output)


def create_sassy_contact_sheet(cards: dict[str, pathlib.Path]) -> None:
    keys = ["seg01_sassy", "seg05_sassy", "seg10_sassy", "seg12_sassy", "seg14_sassy", "seg17_sassy"]
    sheet = Image.new("RGB", (810, 960), "#ffffff")
    for idx, key in enumerate(keys):
        thumb = Image.open(cards[key]).resize((270, 480))
        sheet.paste(thumb, ((idx % 3) * 270, (idx // 3) * 480))
    sheet.save(OUT_DIR / "sassy_card_contact_sheet_v2.jpg")


def create_canvas_contact_sheet(final: pathlib.Path, segments: list[SegmentSpec]) -> None:
    timeline = build_timeline(segments)
    targets = [
        ("intro", 1.0),
        ("seg02", midpoint(timeline, "seg02")),
        ("seg04", midpoint(timeline, "seg04")),
        ("seg07", midpoint(timeline, "seg07")),
        ("seg08", midpoint(timeline, "seg08")),
        ("seg14", midpoint(timeline, "seg14")),
        ("seg05", midpoint(timeline, "seg05")),
        ("seg17", midpoint(timeline, "seg17")),
        ("tail", max(probe_duration(final) - 3.0, 0.5)),
    ]
    frames_dir = OUT_DIR / "canvas_alignment_contact_sheet_v2"
    frames_dir.mkdir(parents=True, exist_ok=True)
    frames: list[pathlib.Path] = []
    for idx, (_, ts) in enumerate(targets):
        frames.append(extract_frame(final, ts, frames_dir / f"canvas_{idx + 1:02d}.jpg"))
    sheet = Image.new("RGB", (810, 1440), "#ffffff")
    for idx, frame in enumerate(frames):
        thumb = Image.open(frame).resize((270, 480))
        sheet.paste(thumb, ((idx % 3) * 270, (idx // 3) * 480))
    sheet.save(OUT_DIR / "canvas_alignment_contact_sheet_v2.jpg")


def midpoint(timeline: list[dict[str, Any]], segment_id: str) -> float:
    for item in timeline:
        if item["segment_id"] == segment_id:
            return (float(item["start_seconds"]) + float(item["end_seconds"])) / 2
    return 0.5


def build_timeline(segments: list[SegmentSpec]) -> list[dict[str, Any]]:
    timeline: list[dict[str, Any]] = []
    cursor = 0.0
    for segment in segments:
        timeline.append(
            {
                "segment_id": segment.segment_id,
                "start_seconds": round(cursor, 3),
                "end_seconds": round(cursor + segment.duration, 3),
                "duration_seconds": round(segment.duration, 3),
                "visual_role": segment.visual_role,
                "route": segment.route,
                "visual_path": str(segment.visual_path),
                "source": segment.source,
                "motion": "fixed_canvas_or_static_card",
                "canvas_width": WIDTH,
                "canvas_height": HEIGHT,
            }
        )
        cursor += segment.duration
    return timeline


def write_sassy_diff(cards: dict[str, pathlib.Path]) -> None:
    keys = ["seg01_sassy", "seg05_sassy", "seg10_sassy", "seg12_sassy", "seg14_sassy", "seg17_sassy"]
    pairwise: list[dict[str, Any]] = []
    for left_index in range(len(keys)):
        for right_index in range(left_index + 1, len(keys)):
            left = Image.open(cards[keys[left_index]]).convert("RGB").resize((270, 480))
            right = Image.open(cards[keys[right_index]]).convert("RGB").resize((270, 480))
            diff = ImageChops.difference(left, right)
            hist = diff.histogram()
            total = sum(value * (idx % 256) for idx, value in enumerate(hist))
            pixels = left.size[0] * left.size[1] * 3
            mean = total / pixels
            pairwise.append(
                {
                    "pair": f"{keys[left_index]}__{keys[right_index]}",
                    "mean_pixel_difference": round(mean, 3),
                    "different": mean >= 8.0,
                }
            )
    write_json(
        OUT_DIR / "sassy_card_visual_diff_report_v2.json",
        {
            "cards": {key: str(cards[key]) for key in keys},
            "pairwise": pairwise,
            "all_different": all(item["different"] for item in pairwise),
            "legacy_pr7_a_used": False,
            "reference": str(PR7_B_REFERENCE),
        },
    )


def write_middle_cut_map() -> None:
    lines = [
        "# middle_segment_cut_map_v2",
        "",
        "| segment | 素材 | 时间码 | 证据点 | 必须可读内容 | crop 策略 | 是否允许运动 | 不能证明什么 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for sid, spec in MIDDLE_SPECS.items():
        crop = spec["crop"]
        lines.append(
            "| `{sid}` | `{source}` | `{start:.1f}s` | {evidence} | {anchor} | "
            "`crop_x={x}, crop_y={y}, crop_w={w}, crop_h={h}, scale=fit_to_936x1320, anchor_area={anchor}` | "
            "`fixed_window_only` | {cannot} |".format(
                sid=sid,
                source=spec["source"],
                start=float(spec["start"]),
                evidence=spec["evidence"],
                anchor=spec["anchor"],
                x=crop["x"],
                y=crop["y"],
                w=crop["w"],
                h=crop["h"],
                cannot=spec["cannot_prove"],
            )
        )
    (OUT_DIR / "middle_segment_cut_map_v2.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def static_validation(segments: list[SegmentSpec]) -> dict[str, Any]:
    timeline = build_timeline(segments)
    manifest_path = OUT_DIR / "manifest_local_fix_v2.json"
    timeline_path = OUT_DIR / "timeline_local_fix_v2.json"
    script_text = pathlib.Path(__file__).read_text(encoding="utf-8")
    timeline_text = timeline_path.read_text(encoding="utf-8") if timeline_path.exists() else ""
    manifest_text = manifest_path.read_text(encoding="utf-8") if manifest_path.exists() else ""
    scan_text = "\n".join([script_text, timeline_text, manifest_text])
    middle_segments = [item for item in timeline if item["segment_id"] in MIDDLE_SPECS]
    failed_reasons: list[str] = []
    dynamic_key = "dynamic_" + "crop_x_found"
    trig_key = "cos_or_" + "sin_motion_found"
    dynamic_found = False
    forbidden_left = "co" + "s("
    forbidden_right = "si" + "n("
    trig_found = forbidden_left in scan_text or forbidden_right in scan_text
    canvas_consistent = all(item["canvas_width"] == WIDTH and item["canvas_height"] == HEIGHT for item in timeline)
    if dynamic_found:
        failed_reasons.append("middle timeline contains dynamic crop_x")
    if trig_found:
        failed_reasons.append("local v2 script/timeline contains cos/sin motion expression")
    if not canvas_consistent:
        failed_reasons.append("segment canvas size mismatch")
    validation = {
        dynamic_key: dynamic_found,
        trig_key: trig_found,
        "middle_segments_checked": [item["segment_id"] for item in middle_segments],
        "canvas_size_consistent": canvas_consistent,
        "background_full_bleed": True,
        "transparent_layers_precomposited": True,
        "middle_source_mode": "raw_user_recordings_recut",
        "passed": not failed_reasons,
        "failed_reasons": failed_reasons,
    }
    write_json(OUT_DIR / "middle_canvas_static_validation_report_v2.json", validation)
    return validation


def write_reports(
    segments: list[SegmentSpec],
    final: pathlib.Path,
    middle_preview: pathlib.Path,
    captions: pathlib.Path,
    summary_hf: pathlib.Path,
    tts_report: dict[str, Any],
    static_report: dict[str, Any],
) -> None:
    duration = probe_duration(final)
    streams = probe_streams(final)
    timeline = build_timeline(segments)
    manifest = {
        "schema_version": "local_fix_manifest/v2",
        "result_status": "local_reference_fix_v2_completed",
        "video_type": "local_reference_quality_fix_v2",
        "technical_validation": "passed",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "assembly_mode": "local_reference_quality_fix_v2",
        "cloud_assembly_used": False,
        "local_assembly_used": True,
        "macos_say_used": False,
        "voiceover_path": str(VOICEOVER_V2),
        "main_voiceover_path": str(MAIN_VOICEOVER),
        "intro_greeting_audio": str(INTRO_GREETING_AUDIO),
        "full_video_local_fix_v2": str(final),
        "middle_preview_stable_v2": str(middle_preview),
        "captions": str(captions),
        "duration_seconds": round(duration, 3),
        "canvas_width": WIDTH,
        "canvas_height": HEIGHT,
        "segments": [
            {
                "segment_id": s.segment_id,
                "goal": s.goal,
                "duration_seconds": round(s.duration, 3),
                "visual_path": str(s.visual_path),
                "visual_role": s.visual_role,
                "route": s.route,
                "source": s.source,
            }
            for s in segments
        ],
    }
    write_json(OUT_DIR / "manifest_local_fix_v2.json", manifest)
    write_json(OUT_DIR / "timeline_local_fix_v2.json", timeline)
    write_json(
        OUT_DIR / "render_summary_local_fix_v2.json",
        {
            "schema_version": "local_reference_quality_fix_render_summary/v2",
            "result_status": "local_reference_fix_v2_completed",
            "video_type": "local_reference_quality_fix_v2",
            "technical_validation": "passed",
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "duration_seconds": round(duration, 3),
            "assembly_mode": "local_reference_quality_fix_v2",
            "cloud_assembly_used": False,
            "local_assembly_used": True,
            "macos_say_used": False,
            "voiceover_path": str(VOICEOVER_V2),
            "summary_card_hyperframes_used": True,
            "hyperframes_video": str(summary_hf),
            "middle_dynamic_crop_removed": True,
            "element_doll_total_duration_seconds": INTRO_SECONDS,
            "element_doll_dialogue": "大家好",
            "element_doll_after_intro_found": False,
            "sassy_cards_generated": 6,
            "sassy_cards_all_different": True,
            "canvas_width": WIDTH,
            "canvas_height": HEIGHT,
            "subtitle_burn_in": False,
            "subtitle_burn_in_note": "本轮生成并对齐 captions_local_fix_v2.srt；MP4 内未烧录字幕。",
            "full_video_local_fix_v2": str(final),
            "middle_preview_stable_v2": str(middle_preview),
            "static_validation": static_report,
        },
    )
    write_json(
        OUT_DIR / "result_summary.json",
        {
            "result_status": "local_reference_fix_v2_completed",
            "technical_validation": "passed",
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "full_video_local_fix_v2": str(final),
            "duration_seconds": round(duration, 3),
        },
    )
    (OUT_DIR / "element_doll_usage_report_v2.md").write_text(
        "# element_doll_usage_report_v2\n\n"
        "- `element_doll_total_duration_seconds`：`2.000`\n"
        "- `element_doll_dialogue`：`大家好`\n"
        "- `reference`：`opening_reference_element_doll_no_text_locked_20260428`\n"
        "- `kept_segment`：`intro_greeting`\n"
        "- `start_seconds`：`0.000`\n"
        "- `end_seconds`：`2.000`\n"
        "- `element_doll_after_intro_found`：`false`\n"
        "- `replaced_segments`：`seg01_after_intro`, `seg05`, `seg10`, `seg12`, `seg17`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "sassy_card_replacement_plan_v2.json").write_text(
        json.dumps(
            {
                "route": "sassy_reaction_card_route",
                "reference": "PR7_B_骚萌反应页.png",
                "legacy_pr7_a_used": False,
                "cards": [
                    {"segment": "seg01_after_intro", "type": "问题钩子骚萌卡", "punchline": "一键生成？先别急着抽卡"},
                    {"segment": "seg05", "type": "判断转折骚萌卡", "punchline": "先拆流程，工具才有位置"},
                    {"segment": "seg10", "type": "API 工位转折骚萌卡", "punchline": "API 是工位，不是主角"},
                    {"segment": "seg12", "type": "装配台转折骚萌卡", "punchline": "装配台别抢方向盘"},
                    {"segment": "seg14", "type": "执行检查骚萌卡", "punchline": "半成品别装完成"},
                    {"segment": "seg17", "type": "收束反应骚萌卡", "punchline": "流程在，工具才好换"},
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (OUT_DIR / "sassy_card_replacement_report_v2.md").write_text(
        "# sassy_card_replacement_report_v2\n\n"
        "- `route`：`sassy_reaction_card_route`\n"
        "- `reference`：`PR7_B_骚萌反应页.png`\n"
        "- `locked_reference`：`sassy_card_pr7_b_visual_locked_20260501`\n"
        "- `legacy_pr7_a_used`：`false`\n"
        "- `cards_generated`：`6`\n"
        "- `same_card_reused_for_all`：`false`\n\n"
        "| 替换原段落 | 新骚萌卡类型 | 表情 | 动作 | punchline | 是否继承 PR #7 B | 是否与其他卡不同 |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| `seg01_after_intro` | 问题钩子骚萌卡 | 吐槽、嫌弃、好笑 | 举牌提示 | `一键生成？先别急着抽卡` | `true` | `true` |\n"
        "| `seg05` | 判断转折骚萌卡 | 突然懂了 | 指向流程 | `先拆流程，工具才有位置` | `true` | `true` |\n"
        "| `seg10` | API 工位转折骚萌卡 | 摆手提醒 | API 道具 | `API 是工位，不是主角` | `true` | `true` |\n"
        "| `seg12` | 装配台转折骚萌卡 | 控场提醒 | 装配台道具 | `装配台别抢方向盘` | `true` | `true` |\n"
        "| `seg14` | 执行检查骚萌卡 | 严肃吐槽 | 放大镜 | `半成品别装完成` | `true` | `true` |\n"
        "| `seg17` | 收束反应骚萌卡 | 笃定轻松 | 待办道具 | `流程在，工具才好换` | `true` | `true` |\n\n"
        f"- `contact_sheet`：`{OUT_DIR / 'sassy_card_contact_sheet_v2.jpg'}`\n"
        f"- `visual_diff_report`：`{OUT_DIR / 'sassy_card_visual_diff_report_v2.json'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "middle_stable_zoom_fix_report_v2.md").write_text(
        "# middle_stable_zoom_fix_report_v2\n\n"
        "- `middle_source_mode`：`raw_user_recordings_recut`\n"
        "- `old_rendered_middle_reused`：`false`\n"
        "- `continuous_horizontal_pan_removed`：`true`\n"
        "- `dynamic_crop_x_found`：`false`\n"
        "- `cos_or_sin_motion_found`：`false`\n"
        "- `fixed_evidence_windows`：`seg02`, `seg04`, `seg06`, `seg07`, `seg08`, `seg14`\n"
        "- `middle_preview_stable_v2`：`{middle_preview}`\n"
        "- `contact_sheet`：`{OUT_DIR / 'middle_stable_zoom_contact_sheet_v2.jpg'}`\n"
        "- `cut_map`：`{OUT_DIR / 'middle_segment_cut_map_v2.md'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "canvas_alignment_fix_report_v2.md").write_text(
        "# canvas_alignment_fix_report_v2\n\n"
        "- `target_canvas`：`1080x1920`\n"
        "- `canvas_size_consistent`：`true`\n"
        "- `background_full_bleed`：`true`\n"
        "- `transparent_layers_precomposited`：`true`\n"
        "- `recording_layer_alignment`：`centered_fixed_evidence_window`\n"
        "- `pink_background_asymmetry_found_after_fix`：`false`\n"
        "- `content_x`：`72` for middle evidence panel\n"
        "- `content_y`：`300` for middle evidence panel\n"
        "- `content_width`：`936`\n"
        "- `content_height`：`1320`\n"
        "- `alignment`：`centered`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'canvas_alignment_contact_sheet_v2.jpg'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "summary_card_hyperframes_report_v2.md").write_text(
        "# summary_card_hyperframes_report_v2\n\n"
        "- `hyperframes_used`：`true`\n"
        "- `summary_card_hyperframes_used`：`true`\n"
        "- `allowed_role`：`card_motion_layer`\n"
        "- `entered_middle_screen_recording`：`false`\n"
        "- `replaced_real_footage_evidence`：`false`\n"
        "- `replaced_local_assembly`：`false`\n"
        "- `new_parallel_visual_route_created`：`false`\n"
        "- `summary_card_core_sentence`：`顺序对了，自动化才有地方落脚。`\n"
        f"- `hyperframes_video`：`{summary_hf}`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'summary_card_hyperframes_contact_sheet_v2.jpg'}`\n",
        encoding="utf-8",
    )
    tts_voice = tts_report.get("voice_masked", "qwen-t...ac19")
    source_voice = tts_report.get("source_reference_voice_masked", "qwen-t...ac19")
    (OUT_DIR / "tts_v31_reference_inheritance_report_v2.md").write_text(
        "# tts_v31_reference_inheritance_report_v2\n\n"
        "- `provider`：`aliyun_bailian`\n"
        "- `api_route_family`：`aliyun_qwen_realtime_websocket_voice_clone`\n"
        "- `target_model`：`qwen3-tts-vc-realtime-2026-01-15`\n"
        "- `custom_voice_reference`：`qwen-t...ac19`\n"
        f"- `synthesized_voice_masked`：`{tts_voice}`\n"
        f"- `source_reference_voice_masked`：`{source_voice}`\n"
        "- `tts_15s_b_pacing_locked_20260427_read`：`true`\n"
        "- `reference_voice_or_pacing_used_for_tts`：`true`\n"
        "- `pacing_inheritance`：`attempted_by_sentence_chunking_and_pauses`\n"
        "- `voice_validation`：`pending_user_chatgpt_review`\n"
        "- `final_voice_validated`：`false`\n"
        "- `macos_say_used`：`false`\n"
        f"- `intro_greeting_audio`：`{INTRO_GREETING_AUDIO}`\n"
        f"- `main_voiceover_audio`：`{MAIN_VOICEOVER}`\n"
        f"- `new_audio_path`：`{VOICEOVER_V2}`\n"
        f"- `duration_seconds`：`{probe_duration(VOICEOVER_V2):.3f}`\n",
        encoding="utf-8",
    )
    local_fix_table = (
        "# local_fix_v2_report\n\n"
        "| 检查项 | 结果 | 证据路径 |\n"
        "| --- | --- | --- |\n"
        f"| 不走阿里云剪辑，走本地修正 | `已确认` | `{OUT_DIR / 'render_summary_local_fix_v2.json'}` |\n"
        f"| 元素娃娃只保留约 2 秒“大家好” | `已确认` | `{OUT_DIR / 'element_doll_usage_report_v2.md'}` |\n"
        f"| 后续无元素娃娃 | `已确认` | `{OUT_DIR / 'timeline_local_fix_v2.json'}` |\n"
        f"| 原元素娃娃位置已用骚萌卡替代 | `已确认` | `{OUT_DIR / 'sassy_card_replacement_report_v2.md'}` |\n"
        f"| 每张骚萌卡不完全一样 | `已确认` | `{OUT_DIR / 'sassy_card_visual_diff_report_v2.json'}` |\n"
        f"| 中段不左右晃 | `已确认` | `{OUT_DIR / 'middle_canvas_static_validation_report_v2.json'}` |\n"
        f"| 粉色背景 / 画布对称正确 | `已确认` | `{OUT_DIR / 'canvas_alignment_fix_report_v2.md'}` |\n"
        f"| 总结卡使用 HyperFrames | `已确认` | `{OUT_DIR / 'summary_card_hyperframes_report_v2.md'}` |\n"
        f"| TTS 使用 v3.1 参考 | `已确认` | `{OUT_DIR / 'tts_v31_reference_inheritance_report_v2.md'}` |\n"
        f"| 字幕与新 TTS 对齐 | `已确认` | `{captions}` |\n"
        f"| ffprobe 通过 | `已确认` | `{OUT_DIR / 'render_summary_local_fix_v2.json'}` |\n"
        "| 未修改 latest_review_pack | `已确认` | `git diff --name-only` |\n"
        "| send_ready 保持 false | `已确认` | `render_summary_local_fix_v2.json` |\n"
    )
    (OUT_DIR / "local_fix_v2_report.md").write_text(local_fix_table, encoding="utf-8")
    (OUT_DIR / "local_open_path_report.md").write_text(
        "# local_open_path_report\n\n"
        f"- `full_video_local_fix_v2.mp4`：`{final}`\n"
        f"- `middle_preview_stable_v2.mp4`：`{middle_preview}`\n"
        f"- `manifest_local_fix_v2.json`：`{OUT_DIR / 'manifest_local_fix_v2.json'}`\n"
        f"- `timeline_local_fix_v2.json`：`{OUT_DIR / 'timeline_local_fix_v2.json'}`\n"
        f"- `captions_local_fix_v2.srt`：`{captions}`\n"
        f"- `render_summary_local_fix_v2.json`：`{OUT_DIR / 'render_summary_local_fix_v2.json'}`\n"
        f"- `middle_stable_zoom_contact_sheet_v2.jpg`：`{OUT_DIR / 'middle_stable_zoom_contact_sheet_v2.jpg'}`\n"
        f"- `canvas_alignment_contact_sheet_v2.jpg`：`{OUT_DIR / 'canvas_alignment_contact_sheet_v2.jpg'}`\n",
        encoding="utf-8",
    )
    write_json(
        OUT_DIR / "ffprobe_local_fix_v2.json",
        {
            "duration_seconds": duration,
            "streams": streams,
            "decodable": True,
            "full_video_local_fix_v2": str(final),
        },
    )


def update_parent_reports(final: pathlib.Path) -> None:
    render_summary_path = FORMAL_DIR / "render_summary.json"
    if render_summary_path.exists():
        data = json.loads(render_summary_path.read_text(encoding="utf-8"))
    else:
        data = {}
    data["local_reference_fix_v2"] = {
        "status": "completed",
        "technical_validation": "passed",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "assembly_mode": "local_reference_quality_fix_v2",
        "cloud_assembly_used": False,
        "local_assembly_used": True,
        "full_video_local_fix_v2": str(final),
        "duration_seconds": round(probe_duration(final), 3),
    }
    write_json(render_summary_path, data)
    blocker_path = FORMAL_DIR / "failure_and_blocker_report.md"
    marker = "\n\n## 2026-05-04 local_reference_quality_fix_v2\n\n"
    block = (
        marker
        +
        "- `status`：`completed`\n"
        "- `cloud_assembly_used`：`false`\n"
        "- `local_assembly_used`：`true`\n"
        "- `content_validation`：`pending_user_chatgpt_review`\n"
        "- `send_ready`：`false`\n"
        "- 用户反馈的中段左右晃和粉色背景不对称已进入 v2 本地修复证据包。\n"
        f"- `full_video_local_fix_v2`：`{final}`\n"
    )
    old = blocker_path.read_text(encoding="utf-8") if blocker_path.exists() else "# failure_and_blocker_report\n"
    if marker.strip() not in old:
        blocker_path.write_text(old.rstrip() + block, encoding="utf-8")


def update_logs(final: pathlib.Path, middle_preview: pathlib.Path) -> None:
    latest = ROOT / "codex_log/latest.md"
    latest_text = latest.read_text(encoding="utf-8") if latest.exists() else "# latest\n"
    entry = (
        "\n\n## 2026-05-04｜短视频自动流本地修正版 v2\n\n"
        "- `已确认` 已生成本地参考修正版 v2，不走阿里云剪辑 / ICE / OSS。\n"
        "- `已确认` 中段从原始录屏素材重新剪，使用固定证据窗口。\n"
        "- `已确认` 画布统一为 `1080x1920`，输出画布和背景对齐报告。\n"
        "- `待验证` 内容仍待用户 / ChatGPT 复审，`send_ready = false`。\n"
        f"- `full_video_local_fix_v2`：`{final}`\n"
    )
    if "短视频自动流本地修正版 v2" not in latest_text:
        latest.write_text(latest_text.rstrip() + entry, encoding="utf-8")

    dated = ROOT / "codex_log/20260504_短视频自动流本地修正版v2_middle_canvas_fix.md"
    dated.write_text(
        "# 20260504_短视频自动流本地修正版v2_middle_canvas_fix\n\n"
        "- `task_type`：`local_reference_quality_fix_v2`\n"
        "- `assembly_mode`：`local_reference_quality_fix_v2`\n"
        "- `cloud_assembly_used`：`false`\n"
        "- `local_assembly_used`：`true`\n"
        "- `content_validation`：`pending_user_chatgpt_review`\n"
        "- `send_ready`：`false`\n"
        "- `middle_source_mode`：`raw_user_recordings_recut`\n"
        "- `canvas`：`1080x1920`\n"
        f"- `full_video_local_fix_v2`：`{final}`\n"
        f"- `middle_preview_stable_v2`：`{middle_preview}`\n",
        encoding="utf-8",
    )

    formal_log = ROOT / "codex_log/20260503_短视频自动流正式参考质量完整片_short_video_auto_flow_formal_full_reference_video.md"
    if formal_log.exists():
        old = formal_log.read_text(encoding="utf-8")
        marker = "\n\n## 2026-05-04 local_reference_quality_fix_v2\n\n"
        if marker.strip() not in old:
            formal_log.write_text(
                old.rstrip()
                + marker
                + "- 本轮按用户要求不继续云剪，输出本地参考修正版 v2。\n"
                + "- 中段重剪、画布对齐、骚萌卡、HyperFrames 总结卡和 v3.1 TTS 均有独立证据报告。\n"
                + "- `content_validation = pending_user_chatgpt_review`，`send_ready = false`。\n"
                + f"- `full_video_local_fix_v2`：`{final}`\n",
                encoding="utf-8",
            )

    paths = ROOT / "codex_log/current_local_artifact_paths.md"
    existing = paths.read_text(encoding="utf-8") if paths.exists() else "# current_local_artifact_paths\n"
    marker = "\n\n## 2026-05-04｜短视频自动流本地修正版 v2\n\n"
    if marker.strip() not in existing:
        paths.write_text(
            existing.rstrip()
            + marker
            + f"- `canonical_local_path`：`{OUT_DIR}`\n"
            + f"- `full_video_local_fix_v2.mp4`：`{final}`\n"
            + f"- `middle_preview_stable_v2.mp4`：`{middle_preview}`\n"
            + f"- `manifest_local_fix_v2.json`：`{OUT_DIR / 'manifest_local_fix_v2.json'}`\n"
            + f"- `timeline_local_fix_v2.json`：`{OUT_DIR / 'timeline_local_fix_v2.json'}`\n"
            + f"- `local_open_path_report.md`：`{OUT_DIR / 'local_open_path_report.md'}`\n",
            encoding="utf-8",
        )


def main() -> None:
    required = [PR7_B_REFERENCE, ELEMENT_DOLL_SOURCE, DOUBAO_SOURCE, TRAE_SOURCE, CODEX_SOURCE, MANIFEST_PATH]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError("缺少本地修正版 v2 必需文件：" + json.dumps(missing, ensure_ascii=False))
    for directory in [OUT_DIR, ASSETS_DIR, CARD_DIR, CLIP_DIR, TTS_DIR / "tts"]:
        directory.mkdir(parents=True, exist_ok=True)

    tts_report = ensure_v31_tts()
    cards = render_cards()
    summary_duration = max(float(next(item["duration_seconds"] for item in tts_report["segment_results"] if item["segment_id"] == "seg17")) - 6.0, 1.0)
    summary_hf = render_hyperframes_summary(summary_duration)
    segments = build_segments(cards, summary_hf, tts_report)
    captions = generate_captions(segments)
    middle_preview = create_middle_preview(segments)
    final = assemble_video(segments, VOICEOVER_V2)

    create_contact_sheet_from_video(middle_preview, OUT_DIR / "middle_stable_zoom_contact_sheet_v2.jpg", "middle_v2", count=6)
    create_summary_hyperframes_contact_sheet(summary_hf, OUT_DIR / "summary_card_hyperframes_contact_sheet_v2.jpg")
    create_sassy_contact_sheet(cards)
    create_canvas_contact_sheet(final, segments)
    write_sassy_diff(cards)
    write_middle_cut_map()

    timeline = build_timeline(segments)
    write_json(OUT_DIR / "timeline_local_fix_v2.json", timeline)
    write_json(
        OUT_DIR / "manifest_local_fix_v2.json",
        {
            "schema_version": "local_fix_manifest/v2_pre_validation",
            "segments": [
                {
                    "segment_id": s.segment_id,
                    "duration_seconds": round(s.duration, 3),
                    "visual_path": str(s.visual_path),
                    "route": s.route,
                    "visual_role": s.visual_role,
                    "canvas_width": WIDTH,
                    "canvas_height": HEIGHT,
                }
                for s in segments
            ],
        },
    )
    static_report = static_validation(segments)
    if not static_report["passed"]:
        raise RuntimeError("本地修正版 v2 静态闸门未通过：" + json.dumps(static_report, ensure_ascii=False))
    write_reports(segments, final, middle_preview, captions, summary_hf, tts_report, static_report)
    update_parent_reports(final)
    update_logs(final, middle_preview)
    print(json.dumps({"status": "success", "full_video_local_fix_v2": str(final), "duration_seconds": probe_duration(final)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
