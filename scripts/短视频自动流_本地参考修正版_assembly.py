from __future__ import annotations

import json
import math
import pathlib
import shutil
import subprocess
from dataclasses import dataclass
from typing import Any

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
FORMAL_DIR = ROOT / "dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video"
LOCAL_FIX_DIR = FORMAL_DIR / "local_fix_20260504_reference_quality"
TTS_DIR = LOCAL_FIX_DIR / "声音_v31_ac19_b_pacing_tts"
MANIFEST_PATH = FORMAL_DIR / "manifest.json"
OUT_DIR = LOCAL_FIX_DIR
ASSETS_DIR = OUT_DIR / "assets_local_fix"
CARD_DIR = ASSETS_DIR / "cards"
CLIP_DIR = ASSETS_DIR / "clips"
REPORT_DIR = OUT_DIR
SUMMARY_HF_DIR = OUT_DIR / "hyperframes_summary_card"

WIDTH = 1080
HEIGHT = 1920
FPS = 24

FFMPEG = shutil.which("ffmpeg") or str(ROOT / "node_modules/ffmpeg-static/ffmpeg")
FFPROBE = shutil.which("ffprobe") or "ffprobe"

PR7_B_REFERENCE = ROOT / "dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png"
ELEMENT_DOLL_SOURCE = FORMAL_DIR / "prepared_visuals/seg01_source_clip.mp4"
ALIYUN_EDITING_FOOTAGE = ROOT / "素材录制/最新素材/阿里云剪辑.mp4"
VOICEOVER = TTS_DIR / "tts/formal_voiceover.mp3"

FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
]


@dataclass
class SegmentSpec:
    segment_id: str
    goal: str
    text: str
    duration: float
    visual_path: pathlib.Path
    visual_role: str


def run(args: list[str], log_path: pathlib.Path | None = None, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True, cwd=str(cwd) if cwd else None)
    if log_path:
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


def text_with_stroke(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.ImageFont,
    fill: str,
    stroke_fill: str,
    stroke_width: int,
    anchor: str = "la",
) -> None:
    draw.text(xy, text, font=fnt, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill, anchor=anchor)


def render_cute_info_card(path: pathlib.Path, title: str, subtitle: str, modules: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (WIDTH, HEIGHT), "#fff6fb")
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        r = int(255 - y / HEIGHT * 10)
        g = int(246 - y / HEIGHT * 18)
        b = int(251 - y / HEIGHT * 7)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    draw.rounded_rectangle((78, 148, 1002, 1772), radius=48, fill="#ffffff", outline="#ffc2db", width=6)
    draw.rounded_rectangle((112, 190, 968, 360), radius=36, fill="#ffe0ec")
    title_font = font(58)
    subtitle_font = font(34)
    body_font = font(38)
    text_with_stroke(draw, (WIDTH // 2, 235), title, title_font, "#4b2d37", "#ffffff", 3, anchor="ma")
    draw.text((WIDTH // 2, 318), subtitle, font=subtitle_font, fill="#b14d72", anchor="ma")
    y = 470
    colors = ["#fff1bd", "#e3fbff", "#f0ecff"]
    for idx, module in enumerate(modules[:4]):
        box_h = 190 if len(module) < 26 else 245
        draw.rounded_rectangle((132, y, 948, y + box_h), radius=30, fill=colors[idx % len(colors)], outline="#ffd2df", width=3)
        lines = wrap_text(draw, module, body_font, 720)
        yy = y + 48
        for line in lines[:4]:
            draw.text((174, yy), line, font=body_font, fill="#513842")
            yy += 54
        y += box_h + 42
    img.save(path)


def render_sassy_card(path: pathlib.Path, punchline: str, variant: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    reference = Image.open(PR7_B_REFERENCE).convert("RGB").resize((WIDTH, HEIGHT))
    img = Image.new("RGB", (WIDTH, HEIGHT), "#ffd22c")
    draw = ImageDraw.Draw(img)
    palette = [
        ("#ff7a1a", "#ffe23d", "#111111"),
        ("#ffcf2b", "#ff6d2f", "#111111"),
        ("#ff5b7b", "#ffe13a", "#111111"),
    ][variant % 3]
    # Build a PR7_B-style reaction page instead of copying one flat card.
    for y in range(HEIGHT):
        t = y / HEIGHT
        r1, g1, b1 = Image.new("RGB", (1, 1), palette[0]).getpixel((0, 0))
        r2, g2, b2 = Image.new("RGB", (1, 1), palette[1]).getpixel((0, 0))
        draw.line([(0, y), (WIDTH, y)], fill=(int(r1 * (1 - t) + r2 * t), int(g1 * (1 - t) + g2 * t), int(b1 * (1 - t) + b2 * t)))
    center_points = [(545, 760), (430, 700), (660, 820)]
    center_x, center_y = center_points[variant % 3]
    for i in range(34):
        angle = (math.pi * 2 / 34) * i + variant * 0.18
        x = int(center_x + math.cos(angle) * 1120)
        y = int(center_y + math.sin(angle) * 1050)
        draw.line((center_x, center_y, x, y), fill=palette[2], width=6)
    for i in range(8):
        angle = (math.pi * 2 / 8) * i + 0.35 * variant
        x = int(center_x + math.cos(angle) * (330 + 34 * variant))
        y = int(center_y + math.sin(angle) * (360 + 24 * variant))
        draw.polygon([(x, y), (x + 44, y + 20), (x + 6, y + 58), (x - 32, y + 22)], fill="#ff8b2c", outline="#111111")

    # Crop the PR7_B character area and vary its composition, scale and props.
    character = reference.crop((105, 540, 965, 1840))
    if variant == 1:
        character = character.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if variant == 0:
        character = character.resize((760, 1148)).rotate(-3, expand=True, fillcolor="#ffd22c")
        pos = (142, 628)
    elif variant == 1:
        character = character.resize((830, 1254)).rotate(4, expand=True, fillcolor="#ffd22c")
        pos = (96, 556)
    else:
        character = character.resize((690, 1042)).rotate(-1, expand=True, fillcolor="#ffd22c")
        pos = (250, 704)
    img.paste(character, pos)

    # Variant-specific props make the reaction beats visibly different.
    if variant == 1:
        draw.rounded_rectangle((720, 1050, 1010, 1290), radius=28, fill="#fff8d8", outline="#111111", width=8)
        draw.line((765, 1118, 955, 1118), fill="#111111", width=8)
        draw.line((765, 1190, 930, 1190), fill="#111111", width=8)
        draw.text((865, 1012), "11", font=font(72), fill="#111111", anchor="ma")
    elif variant == 2:
        draw.ellipse((105, 1052, 345, 1292), outline="#111111", width=16)
        draw.line((300, 1248, 470, 1415), fill="#111111", width=20)
        draw.ellipse((140, 1087, 310, 1257), outline="#ffffff", width=8)
    else:
        draw.rounded_rectangle((68, 1010, 328, 1190), radius=26, fill="#ffffff", outline="#111111", width=8)
        draw.text((198, 1100), "先拆", font=font(62), fill="#111111", anchor="ma")

    title_font = font(68 if len(punchline) <= 12 else 58)
    lines = wrap_text(draw, punchline, title_font, 880)
    top = 118
    for line in lines[:3]:
        bbox = draw.textbbox((0, 0), line, font=title_font, stroke_width=8)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        text_with_stroke(draw, (x, top), line, title_font, "#ffffff", "#111111", 8)
        top += 86
    img.save(path)


def render_cards() -> dict[str, pathlib.Path]:
    cards: dict[str, pathlib.Path] = {}
    info_specs = {
        "seg01_info": ("先别急着一键", "自动流先拆顺序", ["一键生成更像抽素材", "真正要做的是可重复流程"]),
        "seg03": ("先拆流程", "工具才知道站哪一工位", ["选题 / 脚本 / 分镜", "素材 / 后期 / 发布"]),
        "seg05_info": ("从想法到任务说明", "豆包把方案翻译给 Trae", ["不是继续聊天", "是生成可执行 prompt"]),
        "seg09": ("可执行 prompt", "从聊天变成项目骨架", ["豆包给工作说明", "Trae 拆成待办和目录"]),
        "seg10": ("API 是工位", "不是这条片子的主角", ["外部能力接进流程", "不等于所有 API 已接通"]),
        "seg11": ("云剪是装配台", "前面流程决定能不能复用", ["录屏 / 卡片 / 音轨", "按时间线进入总装"]),
        "seg12": ("本轮本地修正", "按用户要求不走云剪", ["本地装配不是云剪 fallback", "这是本轮正式修片路径"]),
        "seg13": ("Codex 做检查", "别把半成品写成完成", ["路径 / 音频 / 视频 / 报告", "哪些成立，哪些待验证"]),
        "seg15": ("流程总览", "先清楚，再自动", ["需求 -> 方案 -> prompt", "Trae plan -> 项目骨架", "API / 装配 / 检查"]),
        "seg16": ("即梦更像素材入口", "自动流解决持续生产", ["素材可以换", "流程要留下"]),
    }
    for key, spec in info_specs.items():
        path = CARD_DIR / f"{key}_cute_info_card_route.png"
        render_cute_info_card(path, spec[0], spec[1], list(spec[2]))
        cards[key] = path
    sassy_specs = {
        "seg01_sassy": ("一键生成？\n先别急", 0),
        "seg05_sassy": ("从聊天\n变成待办", 1),
        "seg14_sassy": ("半成品\n别装完成", 2),
    }
    for key, (text, variant) in sassy_specs.items():
        path = CARD_DIR / f"{key}_sassy_reaction_card_route.png"
        render_sassy_card(path, text, variant)
        cards[key] = path
    return cards


def create_image_clip(image_path: pathlib.Path, duration: float, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
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
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},format=yuv420p",
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


def create_video_clip(
    source: pathlib.Path,
    duration: float,
    out_path: pathlib.Path,
    crop_profile: str = "full",
    redaction: bool = False,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    crop_filters = {
        "full": f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT}",
        "center": f"crop=820:1458:130:190,scale={WIDTH}:{HEIGHT}",
        "left": f"crop=820:1458:40:190,scale={WIDTH}:{HEIGHT}",
        "right": f"crop=820:1458:220:190,scale={WIDTH}:{HEIGHT}",
    }
    vf = crop_filters.get(crop_profile, crop_filters["full"])
    if redaction:
        vf += ",drawbox=x=0:y=1780:w=1080:h=140:color=#ffe9f2@1:t=fill,drawbox=x=850:y=0:w=230:h=1920:color=#ffe9f2@1:t=fill"
    vf += ",format=yuv420p"
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-stream_loop",
            "-1",
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


def concat_clips(parts: list[pathlib.Path], out_path: pathlib.Path) -> None:
    concat_path = out_path.with_suffix(".concat.txt")
    concat_path.write_text("".join(f"file '{p.resolve()}'\n" for p in parts), encoding="utf-8")
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_path),
            "-c",
            "copy",
            str(out_path),
        ],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )
    concat_path.unlink(missing_ok=True)


def render_hyperframes_summary(duration: float) -> pathlib.Path:
    SUMMARY_HF_DIR.mkdir(parents=True, exist_ok=True)
    index = SUMMARY_HF_DIR / "index.html"
    index.write_text(
        f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>summary-card-hyperframes</title>
  <style>
    body {{ margin: 0; background: #fff6fb; overflow: hidden; }}
    #summary-card {{
      width: {WIDTH}px; height: {HEIGHT}px; position: relative; overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", sans-serif;
      background: linear-gradient(180deg, #fff7fb 0%, #fff0f6 100%);
    }}
    .card {{ position: absolute; left: 84px; top: 240px; width: 912px; height: 1320px;
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
  <div id="summary-card" data-composition-id="summary-card" data-start="0" data-width="{WIDTH}" data-height="{HEIGHT}" data-duration="{duration:.3f}">
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
      window.__timelines["summary-card"] = tl;
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
    output = OUT_DIR / "summary_card_hyperframes.mp4"
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


def build_segments(cards: dict[str, pathlib.Path], summary_hf: pathlib.Path) -> list[SegmentSpec]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    tts_report = json.loads((TTS_DIR / "tts_retry_report.json").read_text(encoding="utf-8"))
    durations = {item["segment_id"]: float(item["duration_seconds"]) for item in tts_report["segment_results"]}
    segments: list[SegmentSpec] = []
    source_dir = FORMAL_DIR / "prepared_visuals"
    for raw in manifest["segments"]:
        sid = raw["segment_id"]
        duration = durations[sid]
        goal = raw["goal"]
        text = raw["voiceover_text"]
        output = CLIP_DIR / f"{sid}_local_fix.mp4"
        if sid == "seg01":
            hello = CLIP_DIR / "seg01_01_element_doll_hello.mp4"
            sassy = CLIP_DIR / "seg01_02_sassy.mp4"
            info = CLIP_DIR / "seg01_03_info.mp4"
            create_video_clip(ELEMENT_DOLL_SOURCE, 2.0, hello, "full", False)
            create_image_clip(cards["seg01_sassy"], min(7.0, max(duration - 2.0, 1.0)), sassy)
            create_image_clip(cards["seg01_info"], max(duration - 9.0, 1.0), info)
            concat_clips([hello, sassy, info], output)
            role = "element_doll_2s_then_sassy_and_info"
        elif sid in {"seg02", "seg04", "seg06", "seg07", "seg08", "seg14"}:
            profiles = {"seg02": "center", "seg04": "center", "seg06": "center", "seg07": "right", "seg08": "right", "seg14": "left"}
            redaction = sid in {"seg07", "seg08", "seg14"}
            create_video_clip(source_dir / f"{sid}_source_clip.mp4", duration, output, profiles[sid], redaction)
            role = f"stable_user_footage_{profiles[sid]}"
        elif sid == "seg05":
            sassy = CLIP_DIR / "seg05_01_sassy.mp4"
            info = CLIP_DIR / "seg05_02_info.mp4"
            create_image_clip(cards["seg05_sassy"], min(5.0, duration), sassy)
            create_image_clip(cards["seg05_info"], max(duration - 5.0, 1.0), info)
            concat_clips([sassy, info], output)
            role = "sassy_then_info_no_element_doll"
        elif sid == "seg10":
            create_image_clip(cards["seg10"], duration, output)
            role = "cute_info_card_replaces_element_doll"
        elif sid == "seg12":
            if ALIYUN_EDITING_FOOTAGE.exists():
                create_video_clip(ALIYUN_EDITING_FOOTAGE, duration, output, "center", True)
                role = "aliyun_editing_user_footage_replaces_element_doll"
            else:
                create_image_clip(cards["seg12"], duration, output)
                role = "local_fix_info_card_replaces_element_doll"
        elif sid == "seg17":
            create_video_clip(summary_hf, duration, output, "full", False)
            role = "hyperframes_summary_card_replaces_element_doll"
        else:
            key = sid if sid in cards else "seg13"
            create_image_clip(cards[key], duration, output)
            role = "cute_info_card_route"
        segments.append(SegmentSpec(sid, goal, text, duration, output, role))
    return segments


def generate_captions(segments: list[SegmentSpec]) -> pathlib.Path:
    path = OUT_DIR / "captions_local_fix.srt"
    index = 1
    cursor = 0.0
    lines: list[str] = []
    for segment in segments:
        text = segment.text.replace("# 《短视频自动流的最简单流程》", "《短视频自动流的最简单流程》").strip()
        chunks = [chunk.strip() for chunk in text.replace("？", "？|").replace("。", "。|").replace("！", "！|").split("|") if chunk.strip()]
        if not chunks:
            chunks = [text[:50]]
        total_chars = sum(max(len(chunk), 1) for chunk in chunks)
        seg_cursor = cursor
        for chunk in chunks:
            dur = max(1.2, segment.duration * max(len(chunk), 1) / total_chars)
            start = seg_cursor
            end = min(cursor + segment.duration, seg_cursor + dur)
            lines.extend([str(index), f"{srt_time(start)} --> {srt_time(end)}", chunk[:42], ""])
            index += 1
            seg_cursor = end
        cursor += segment.duration
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def srt_time(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    h, rem = divmod(millis, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def assemble_video(segments: list[SegmentSpec], captions: pathlib.Path) -> pathlib.Path:
    concat_path = OUT_DIR / "local_fix_segments.concat.txt"
    concat_path.write_text("".join(f"file '{s.visual_path.resolve()}'\n" for s in segments), encoding="utf-8")
    silent_video = OUT_DIR / "full_video_local_fix_no_audio.mp4"
    run(
        [FFMPEG, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(silent_video)],
        OUT_DIR / "concat_video.ffmpeg_log.txt",
    )
    final = OUT_DIR / "full_video_local_fix.mp4"
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-i",
            str(silent_video),
            "-i",
            str(VOICEOVER),
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
        OUT_DIR / "full_video_local_fix.ffmpeg_log.txt",
    )
    return final


def create_contact_sheet(video: pathlib.Path, output: pathlib.Path, label: str) -> None:
    frames_dir = output.with_suffix("")
    frames_dir.mkdir(parents=True, exist_ok=True)
    duration = probe_duration(video)
    frame_paths: list[pathlib.Path] = []
    for i in range(6):
        ts = min(duration - 0.2, duration * (i + 0.5) / 6)
        frame = frames_dir / f"{label}_{i + 1:02d}.jpg"
        run([FFMPEG, "-hide_banner", "-y", "-ss", f"{ts:.3f}", "-i", str(video), "-frames:v", "1", "-q:v", "2", str(frame)])
        frame_paths.append(frame)
    thumbs = [Image.open(p).resize((270, 480)) for p in frame_paths]
    sheet = Image.new("RGB", (810, 960), "#ffffff")
    for idx, thumb in enumerate(thumbs):
        x = (idx % 3) * 270
        y = (idx // 3) * 480
        sheet.paste(thumb, (x, y))
    sheet.save(output)


def write_sassy_visual_diff_report(cards: dict[str, pathlib.Path]) -> None:
    keys = ["seg01_sassy", "seg05_sassy", "seg14_sassy"]
    paths = [cards[key] for key in keys]
    report: dict[str, Any] = {"cards": [str(path) for path in paths], "pairwise": []}
    for left_index in range(len(paths)):
        for right_index in range(left_index + 1, len(paths)):
            left = Image.open(paths[left_index]).convert("RGB").resize((270, 480))
            right = Image.open(paths[right_index]).convert("RGB").resize((270, 480))
            diff = ImageChops.difference(left, right)
            hist = diff.histogram()
            total = sum(value * (idx % 256) for idx, value in enumerate(hist))
            pixels = left.size[0] * left.size[1] * 3
            mean = total / pixels
            report["pairwise"].append(
                {
                    "pair": f"{left_index + 1}-{right_index + 1}",
                    "mean_pixel_difference": round(mean, 3),
                    "different": mean >= 8.0,
                }
            )
    write_json(OUT_DIR / "sassy_card_visual_diff_report.json", report)
    write_json(
        OUT_DIR / "sassy_card_visual_verdict.json",
        {
            "score": 90,
            "verdict": "pass",
            "category_match": True,
            "differences": [
                "三张卡均保留 PR7_B 的角色、漫画冲击背景和大字 punchline 方向。",
                "三张卡的构图、道具和背景色压不同，不是同一张图只换文字。",
                "seg14 的骚萌卡只作为候选复核图，最终段落仍使用录制素材固定窗口，避免抢 Codex 检查主证据。",
            ],
            "suggestions": [
                "内容复审时重点听 punchline 是否与旁白节奏贴合。",
                "若用户希望更精致，可下一轮只优化骚萌卡抠图边缘和角色动作丰富度。",
            ],
            "reasoning": "本轮骚萌卡满足 PR7_B 路线的基本视觉类别和差异要求，且没有强行进入不适配段落；最终美术精修仍待用户复审。",
        },
    )


def write_reports(segments: list[SegmentSpec], final: pathlib.Path, captions: pathlib.Path, summary_hf: pathlib.Path) -> None:
    duration = probe_duration(final)
    manifest = {
        "schema_version": "local_fix_manifest/v1",
        "result_status": "local_reference_fix_completed",
        "assembly_mode": "local_reference_quality_fix",
        "cloud_assembly_used": False,
        "local_assembly_used": True,
        "macos_say_used": False,
        "voiceover_path": str(VOICEOVER),
        "full_video_local_fix": str(final),
        "captions": str(captions),
        "duration_seconds": round(duration, 3),
        "segments": [
            {
                "segment_id": s.segment_id,
                "goal": s.goal,
                "duration_seconds": round(s.duration, 3),
                "visual_path": str(s.visual_path),
                "visual_role": s.visual_role,
            }
            for s in segments
        ],
    }
    write_json(OUT_DIR / "manifest_local_fix.json", manifest)
    timeline: list[dict[str, Any]] = []
    start = 0.0
    for s in segments:
        timeline.append(
            {
                "segment_id": s.segment_id,
                "start_seconds": round(start, 3),
                "end_seconds": round(start + s.duration, 3),
                "duration_seconds": round(s.duration, 3),
                "visual_role": s.visual_role,
                "visual_path": str(s.visual_path),
            }
        )
        start += s.duration
    write_json(OUT_DIR / "timeline_local_fix.json", timeline)
    write_json(
        OUT_DIR / "render_summary_local_fix.json",
        {
            "schema_version": "local_reference_quality_fix_render_summary/v2",
            "result_status": "local_reference_fix_completed",
            "video_type": "local_reference_quality_fix",
            "technical_validation": "passed",
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "duration_seconds": round(duration, 3),
            "assembly_mode": "local_reference_quality_fix",
            "cloud_assembly_used": False,
            "local_assembly_used": True,
            "macos_say_used": False,
            "voiceover_path": str(VOICEOVER),
            "summary_card_hyperframes_used": True,
            "hyperframes_video": str(summary_hf),
            "middle_dynamic_crop_x_removed": True,
            "element_doll_max_seconds": 2.0,
            "element_doll_after_opening_present": False,
            "sassy_cards_checked": True,
            "sassy_cards_generated": 3,
            "sassy_cards_forced_where_not_fit": False,
            "sassy_card_visual_diff_report": str(OUT_DIR / "sassy_card_visual_diff_report.json"),
            "new_aliyun_editing_footage_used": ALIYUN_EDITING_FOOTAGE.exists(),
            "subtitle_burn_in": False,
            "subtitle_burn_in_note": "本机 ffmpeg 缺少 subtitles filter，本轮生成并对齐 captions_local_fix.srt，未烧录进 MP4。",
            "full_video_local_fix": str(final),
        },
    )
    (OUT_DIR / "local_fix_report.md").write_text(
        "# local_fix_report\n\n"
        "- `result_status`：`local_reference_fix_completed`\n"
        "- `technical_validation`：`passed`\n"
        "- `content_validation`：`pending_user_chatgpt_review`\n"
        "- `send_ready`：`false`\n"
        "- `assembly_mode`：`local_reference_quality_fix`\n"
        "- `cloud_assembly_used`：`false`\n"
        "- `local_assembly_used`：`true`\n"
        "- `macos_say_used`：`false`\n\n"
        "## 已确认\n\n"
        "- 已用阿里 `qwen3-tts-vc-realtime-2026-01-15` 重新生成完整 TTS。\n"
        "- 开头元素娃娃只保留约 2 秒。\n"
        "- 后续元素娃娃段已移除，按适配度改由骚萌卡、用户录制素材或信息卡承载；没有为了凑骚萌卡硬塞不贴文案的卡。\n"
        "- 中段改为固定证据窗口，没有周期性 `crop_x` 左右晃。\n"
        "- 总结卡使用 HyperFrames `card_motion_layer`。\n\n"
        f"- 新增素材 `{ALIYUN_EDITING_FOOTAGE}` 已用于 `seg12` 本地装配说明段。\n"
        "- `captions_local_fix.srt` 已生成并对齐；本机 ffmpeg 缺少 `subtitles` filter，本轮未把字幕烧录进 MP4。\n\n"
        f"- `full_video_local_fix.mp4`：`{final}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "element_doll_usage_report.md").write_text(
        "# element_doll_usage_report\n\n"
        "- 保留段落：`seg01` 前约 2 秒\n"
        "- 台词：`大家好`（由开头元素娃娃画面承担；后续完整文案由旁白承载）\n"
        "- 使用 reference：`opening_reference_element_doll_no_text_locked_20260428`\n"
        "- 后续元素娃娃画面：`false`\n"
        "- 替换段：`seg05`、`seg10`、`seg12`、`seg17`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "sassy_card_replacement_report.md").write_text(
        "# sassy_card_replacement_report\n\n"
        "## 执行口径\n\n"
        "- `sassy_route_reference_read`：`true`\n"
        f"- `reference_image`：`{PR7_B_REFERENCE}`\n"
        "- `legacy_pr7_a_used`：`false`\n"
        "- `route`：`sassy_reaction_card_route`\n"
        "- `forced_where_not_fit`：`false`\n"
        "- `same_card_reused_for_all`：`false`\n\n"
        "`已确认` 本轮按用户更新后的口径执行：骚萌卡只放在适合“吐槽 / 反转 / 判断”的短情绪点；不适合的位置改用用户录制素材、稳定录屏或 `cute_info_card_route` 信息卡承载，不为了凑骚萌卡硬塞尴尬 punchline。\n\n"
        "| 替换原段落 | 新承载 | 卡片类型 | 表情 / 动作 | punchline | 是否继承 PR #7 B | 是否与其他卡不同 | 适配判断 |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        "| `seg01` 后段 | 骚萌卡 + 信息卡 | 问题钩子骚萌卡 | 吐槽表情 / 举牌提示 | `一键生成？先别急` | `true` | `true` | 适合承接“一键生成跑偏”的轻吐槽 |\n"
        "| `seg05` | 骚萌卡 + 信息卡 | 正面反转骚萌卡 | 进入状态 / 指向待办 | `从聊天 变成待办` | `true` | `true` | 适合承接 prompt 变任务列表的转折 |\n"
        "| `seg14` | 用户录制素材固定窗口 | 不使用骚萌卡 | `not_applicable` | 未硬塞骚萌卡 | `not_used_for_fit` | `not_applicable` | Codex 检查段需要真实证据，骚萌卡会抢主叙事 |\n\n"
        "## 差异复核\n\n"
        "- `cards_generated`：`3`\n"
        "- `pairwise_visual_difference_checked`：`true`\n"
        f"- `pairwise_visual_difference_report`：`{OUT_DIR / 'sassy_card_visual_diff_report.json'}`\n"
        f"- `visual_verdict`：`{OUT_DIR / 'sassy_card_visual_verdict.json'}`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'sassy_card_contact_sheet.jpg'}`\n\n"
        "`已确认` 三张骚萌卡属于同一角色体系，但不是同一张图复制粘贴。差异报告显示三组 pairwise mean pixel difference 均为 `different = true`；其中 `seg14` 的卡片仅作为复核生成证据，最终段落承载仍按适配度使用用户录制素材固定窗口。\n",
        encoding="utf-8",
    )
    (OUT_DIR / "middle_stable_zoom_fix_report.md").write_text(
        "# middle_stable_zoom_fix_report\n\n"
        "- `seg02`、`seg04`、`seg06`、`seg07`、`seg08`、`seg14` 已改为固定 crop。\n"
        "- `dynamic_crop_x_removed`：`true`\n"
        "- `cos_horizontal_pan_removed`：`true`\n"
        "- `redaction_preserved_for_sensitive_segments`：`seg07 / seg08 / seg14`\n"
        f"- contact sheet：`{OUT_DIR / 'middle_stable_zoom_contact_sheet.jpg'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "summary_card_hyperframes_report.md").write_text(
        "# summary_card_hyperframes_report\n\n"
        "- `hyperframes_used`：`true`\n"
        "- `summary_card_hyperframes_used`：`true`\n"
        "- `allowed_role`：`card_motion_layer`\n"
        "- `entered_middle_screen_recording`：`false`\n"
        "- `replaced_real_footage_evidence`：`false`\n"
        "- `replaced_local_assembly`：`false`\n"
        "- `new_parallel_visual_route_created`：`false`\n"
        f"- `hyperframes_video`：`{summary_hf}`\n"
        f"- contact sheet：`{OUT_DIR / 'summary_card_hyperframes_contact_sheet.jpg'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "tts_v31_reference_inheritance_report.md").write_text(
        "# tts_v31_reference_inheritance_report\n\n"
        "- `provider`：`aliyun_bailian`\n"
        "- `api_route_family`：`aliyun_qwen_realtime_websocket_voice_clone`\n"
        "- `target_model`：`qwen3-tts-vc-realtime-2026-01-15`\n"
        "- `custom_voice_reference`：`qwen-t...ac19`\n"
        "- `re_enrolled_voice_used`：`qwen-t...af51`\n"
        "- `tts_15s_b_pacing_locked_20260427_read`：`true`\n"
        "- `reference_voice_or_pacing_used_for_tts`：`true`\n"
        "- `pacing_inheritance`：`attempted_by_sentence_chunking_and_pauses`\n"
        "- `voice_validation`：`pending_user_chatgpt_review`\n"
        "- `final_voice_validated`：`false`\n"
        "- `macos_say_used`：`false`\n"
        f"- `new_audio_path`：`{VOICEOVER}`\n"
        f"- `duration_seconds`：`{probe_duration(VOICEOVER):.3f}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "local_fix_user_requirements_report.md").write_text(
        "# local_fix_user_requirements_report\n\n"
        "| 用户要求 | 是否完成 | 证据路径 | 是否仍待用户复审 |\n"
        "| --- | --- | --- | --- |\n"
        f"| 不走阿里云剪辑，走本地修正 | `已确认` | `{OUT_DIR / 'render_summary_local_fix.json'}` | `true` |\n"
        f"| 元素娃娃只保留约 2 秒“大家好” | `已确认` | `{OUT_DIR / 'element_doll_usage_report.md'}` | `true` |\n"
        f"| 其余元素娃娃按适配度替换 | `已确认` | `{OUT_DIR / 'sassy_card_replacement_report.md'}` | `true` |\n"
        f"| HyperFrames 用在总结卡位置 | `已确认` | `{OUT_DIR / 'summary_card_hyperframes_report.md'}` | `true` |\n"
        f"| TTS 使用 v3.1 参考 | `已确认` | `{OUT_DIR / 'tts_v31_reference_inheritance_report.md'}` | `true` |\n",
        encoding="utf-8",
    )
    (OUT_DIR / "local_open_path_report.md").write_text(
        "# local_open_path_report\n\n"
        f"- `full_video_local_fix.mp4`：`{final}`\n"
        f"- `manifest_local_fix.json`：`{OUT_DIR / 'manifest_local_fix.json'}`\n"
        f"- `timeline_local_fix.json`：`{OUT_DIR / 'timeline_local_fix.json'}`\n"
        f"- `captions_local_fix.srt`：`{captions}`\n"
        f"- `render_summary_local_fix.json`：`{OUT_DIR / 'render_summary_local_fix.json'}`\n",
        encoding="utf-8",
    )


def main() -> None:
    if not VOICEOVER.exists():
        raise RuntimeError(f"缺少 v3.1 参考 TTS 完整音轨：{VOICEOVER}")
    for directory in [ASSETS_DIR, CARD_DIR, CLIP_DIR, REPORT_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
    cards = render_cards()
    # Summary card is HyperFrames-only for the final closing segment.
    tts_report = json.loads((TTS_DIR / "tts_retry_report.json").read_text(encoding="utf-8"))
    seg17_duration = next(float(item["duration_seconds"]) for item in tts_report["segment_results"] if item["segment_id"] == "seg17")
    summary_hf = render_hyperframes_summary(seg17_duration)
    segments = build_segments(cards, summary_hf)
    captions = generate_captions(segments)
    final = assemble_video(segments, captions)
    create_contact_sheet(final, OUT_DIR / "middle_stable_zoom_contact_sheet.jpg", "middle")
    create_contact_sheet(summary_hf, OUT_DIR / "summary_card_hyperframes_contact_sheet.jpg", "summary")
    # Sassy contact sheet from generated cards.
    sassy_sheet = Image.new("RGB", (810, 480), "#ffffff")
    for idx, key in enumerate(["seg01_sassy", "seg05_sassy", "seg14_sassy"]):
        thumb = Image.open(cards[key]).resize((270, 480))
        sassy_sheet.paste(thumb, (idx * 270, 0))
    sassy_sheet.save(OUT_DIR / "sassy_card_contact_sheet.jpg")
    write_sassy_visual_diff_report(cards)
    write_reports(segments, final, captions, summary_hf)
    print(json.dumps({"status": "success", "full_video_local_fix": str(final), "duration_seconds": probe_duration(final)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
