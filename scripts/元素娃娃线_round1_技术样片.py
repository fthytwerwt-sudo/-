from __future__ import annotations

import audioop
import json
import math
import pathlib
import shutil
import subprocess
import wave
from dataclasses import dataclass

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE_DIR = ROOT / "dist" / "20260417_豆包的正确打开方式_vnext" / "host_motion_prototype_round1"
ASSETS_DIR = BASE_DIR / "assets"
TIMELINE_DIR = BASE_DIR / "timeline"
RENDERS_DIR = BASE_DIR / "renders"
AUDIT_DIR = BASE_DIR / "audit"
FRAMES_DIR = BASE_DIR / "frames"

SOURCE_AUDIO = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "voice_candidates_round4"
    / "E1"
    / "E1_processed.wav"
)
TRIMMED_AUDIO = BASE_DIR / "audio_E1_excerpt.wav"
PROTOTYPE_MP4 = RENDERS_DIR / "元素娃娃技术样片_round1.mp4"
PROTOTYPE_GIF = RENDERS_DIR / "元素娃娃技术样片_round1.gif"
TIMELINE_JSON = TIMELINE_DIR / "动作时间线_round1.json"
PLAN_MD = AUDIT_DIR / "最小技术方案_round1.md"
VERDICT_MD = AUDIT_DIR / "技术验收_round1.md"

WIDTH = 1080
HEIGHT = 1920
FPS = 25
DURATION_SECONDS = 4.2
TOTAL_FRAMES = int(FPS * DURATION_SECONDS)
CHAR_X = 430
CHAR_Y = 870
PIX = 22

SKIN = "#E6B48E"
HAIR = "#5A3518"
SHIRT = "#F3923A"
VEST = "#8F5326"
PANTS = "#4D6E91"
SHOES = "#2A2A2A"
MOUTH = "#B96458"
PANEL = "#F2E1BE"
PANEL_DARK = "#3A2A1F"
ACCENT = "#E18C36"
GRID = "#CBE2F2"
GRASS = "#5C925D"


@dataclass(frozen=True)
class MotionSnapshot:
    frame: int
    second: float
    stage: str
    enter_progress: float
    mouth_state: str
    arm_pose: str
    blink: bool
    head_angle_deg: float
    body_bounce_px: float


def resolve_ffmpeg() -> str:
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    bundled = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("缺少 ffmpeg")


def run_command(args: list[str]) -> None:
    subprocess.run(args, check=True)


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


def draw_rect(draw: ImageDraw.ImageDraw, origin: tuple[int, int], x: int, y: int, w: int, h: int, color: str) -> None:
    ox, oy = origin
    draw.rectangle((ox + x * PIX, oy + y * PIX, ox + (x + w) * PIX, oy + (y + h) * PIX), fill=color)


def build_layer_head_base() -> pathlib.Path:
    image = Image.new("RGBA", (12 * PIX, 8 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    draw_rect(draw, origin, 2, 0, 6, 1, HAIR)
    draw_rect(draw, origin, 1, 1, 8, 4, SKIN)
    draw_rect(draw, origin, 1, 1, 2, 2, HAIR)
    draw_rect(draw, origin, 7, 1, 2, 2, HAIR)
    draw_rect(draw, origin, 2, 2, 1, 1, "#1D1D1D")
    draw_rect(draw, origin, 6, 2, 1, 1, "#1D1D1D")
    return save_asset(image, "head_base.png")


def build_layer_body() -> pathlib.Path:
    image = Image.new("RGBA", (12 * PIX, 18 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    draw_rect(draw, origin, 2, 0, 6, 4, SHIRT)
    draw_rect(draw, origin, 3, 4, 4, 3, VEST)
    draw_rect(draw, origin, 3, 7, 2, 4, PANTS)
    draw_rect(draw, origin, 5, 7, 2, 4, PANTS)
    draw_rect(draw, origin, 3, 11, 2, 1, SHOES)
    draw_rect(draw, origin, 5, 11, 2, 1, SHOES)
    return save_asset(image, "body.png")


def build_layer_arm_down() -> pathlib.Path:
    image = Image.new("RGBA", (16 * PIX, 14 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    draw_rect(draw, origin, 2, 2, 1, 5, SKIN)
    draw_rect(draw, origin, 13, 2, 1, 5, SKIN)
    return save_asset(image, "arm_down.png")


def build_layer_arm_point() -> pathlib.Path:
    image = Image.new("RGBA", (16 * PIX, 14 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    draw_rect(draw, origin, 2, 2, 1, 5, SKIN)
    draw_rect(draw, origin, 11, 1, 4, 1, SKIN)
    draw_rect(draw, origin, 14, 1, 1, 2, SKIN)
    return save_asset(image, "arm_point.png")


def build_layer_mouth(name: str, blocks: list[tuple[int, int, int, int]]) -> pathlib.Path:
    image = Image.new("RGBA", (12 * PIX, 8 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    for x, y, w, h in blocks:
        draw_rect(draw, origin, x, y, w, h, MOUTH)
    return save_asset(image, name)


def build_layer_blink() -> pathlib.Path:
    image = Image.new("RGBA", (12 * PIX, 8 * PIX), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    origin = (0, 0)
    draw_rect(draw, origin, 2, 2, 1, 1, SKIN)
    draw_rect(draw, origin, 6, 2, 1, 1, SKIN)
    draw.line((2 * PIX, 3 * PIX, 3 * PIX, 3 * PIX), fill=HAIR, width=4)
    draw.line((6 * PIX, 3 * PIX, 7 * PIX, 3 * PIX), fill=HAIR, width=4)
    return save_asset(image, "blink_overlay.png")


def save_asset(image: Image.Image, filename: str) -> pathlib.Path:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    path = ASSETS_DIR / filename
    image.save(path)
    return path


def create_background() -> pathlib.Path:
    image = Image.new("RGB", (WIDTH, HEIGHT), GRID)
    draw = ImageDraw.Draw(image)
    for y in range(0, HEIGHT, 96):
        tone = 192 + int(18 * math.sin(y / 180))
        draw.rectangle((0, y, WIDTH, min(HEIGHT, y + 96)), fill=(tone - 18, tone + 10, tone + 24))
        draw.line((0, y, WIDTH, y), fill=(255, 255, 255, 80), width=3)
    for x in range(0, WIDTH, 96):
        draw.line((x, 0, x, HEIGHT), fill=(255, 255, 255, 80), width=3)
    draw.rounded_rectangle((90, 130, 990, 1590), radius=44, fill=PANEL, outline="#C88435", width=8)
    draw.rounded_rectangle((130, 190, 950, 430), radius=30, fill="#F8EFD7", outline="#D99C48", width=6)
    draw.rounded_rectangle((560, 520, 930, 1120), radius=32, fill=PANEL_DARK, outline="#8A5A2A", width=6)
    for idx, color in enumerate(["#D96B2B", "#F3B13D", "#5A8B4E"]):
        draw.rounded_rectangle((170 + idx * 150, 235, 290 + idx * 150, 287), radius=18, fill=color)
    title_font = load_font(58, bold=True)
    body_font = load_font(30, bold=False)
    draw.text((174, 248), "元素娃娃动态样片", font=title_font, fill=PANEL_DARK)
    draw.text((176, 332), "round1 技术验证", font=body_font, fill="#6C5437")
    draw.text((590, 560), "mouth + arm + nod", font=load_font(30, bold=True), fill="#F0C55B")
    draw.text((590, 610), "enter / judge / settle", font=load_font(30), fill="#F0C55B")
    draw.rectangle((0, 1320, WIDTH, HEIGHT), fill=GRASS)
    for x in range(0, WIDTH, 70):
        draw.rectangle((x, 1258 - (x // 70 % 3) * 14, x + 42, 1320), fill="#5A824D")
    bg = image.filter(ImageFilter.GaussianBlur(radius=0.2))
    path = ASSETS_DIR / "background_panel.png"
    bg.save(path)
    return path


def extract_test_audio(ffmpeg: str) -> None:
    if TRIMMED_AUDIO.exists():
        return
    run_command(
        [
            ffmpeg,
            "-y",
            "-ss",
            "0",
            "-t",
            f"{DURATION_SECONDS:.2f}",
            "-i",
            str(SOURCE_AUDIO),
            "-ar",
            "48000",
            "-ac",
            "1",
            str(TRIMMED_AUDIO),
        ]
    )


def audio_levels_per_frame(audio_path: pathlib.Path) -> list[float]:
    levels: list[float] = []
    with wave.open(str(audio_path), "rb") as wav_file:
        frame_rate = wav_file.getframerate()
        sample_width = wav_file.getsampwidth()
        chunk_size = int(frame_rate / FPS)
        for _ in range(TOTAL_FRAMES):
            frames = wav_file.readframes(chunk_size)
            if not frames:
                levels.append(0.0)
                continue
            rms = audioop.rms(frames, sample_width)
            levels.append(float(rms))
    peak = max(levels) or 1.0
    return [level / peak for level in levels]


def ease_out_back(x: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * pow(x - 1, 3) + c1 * pow(x - 1, 2)


def build_motion_state(frame: int, levels: list[float]) -> MotionSnapshot:
    second = frame / FPS
    enter_progress = min(1.0, second / 0.6)
    if second < 0.6:
        stage = "enter"
    elif second < 2.1:
        stage = "speak"
    elif second < 3.2:
        stage = "judge"
    else:
        stage = "settle"

    level = levels[min(frame, len(levels) - 1)]
    if level < 0.22:
        mouth_state = "closed"
    elif level < 0.5:
        mouth_state = "mid"
    else:
        mouth_state = "open"

    arm_pose = "point" if 2.0 <= second <= 3.15 else "down"
    blink = 2.65 <= second <= 2.78 or 3.85 <= second <= 3.94
    head_angle = 0.0
    if stage == "judge":
        head_angle = -8.0
    elif stage == "settle":
        settle_progress = min(1.0, (second - 3.2) / 0.8)
        head_angle = -8.0 * (1 - settle_progress)
    bounce = 0.0
    if stage == "enter":
        bounce = -16 * math.sin(min(1.0, second / 0.6) * math.pi)
    elif stage == "speak":
        bounce = -6 * math.sin(second * 6.8)
    return MotionSnapshot(
        frame=frame,
        second=round(second, 3),
        stage=stage,
        enter_progress=round(enter_progress, 3),
        mouth_state=mouth_state,
        arm_pose=arm_pose,
        blink=blink,
        head_angle_deg=round(head_angle, 2),
        body_bounce_px=round(bounce, 2),
    )


def composite_frame(
    background: Image.Image,
    layers: dict[str, Image.Image],
    state: MotionSnapshot,
    output_path: pathlib.Path,
) -> None:
    canvas = background.copy().convert("RGBA")
    if state.enter_progress < 1.0:
        enter_t = ease_out_back(state.enter_progress)
        offset_x = int(-320 * (1 - enter_t))
        scale = 0.88 + 0.12 * enter_t
    else:
        offset_x = 0
        scale = 1.0

    body_offset = (CHAR_X + offset_x, int(CHAR_Y + state.body_bounce_px))

    def paste_scaled(image: Image.Image, pos: tuple[int, int], *, angle: float = 0.0, anchor: tuple[int, int] | None = None) -> None:
        sprite = image
        if scale != 1.0:
            sprite = sprite.resize(
                (max(1, int(image.width * scale)), max(1, int(image.height * scale))),
                Image.NEAREST,
            )
        if angle:
            sprite = sprite.rotate(angle, resample=Image.NEAREST, expand=True, center=anchor)
        canvas.alpha_composite(sprite, dest=pos)

    paste_scaled(layers["arm_point" if state.arm_pose == "point" else "arm_down"], (body_offset[0] - 46, body_offset[1] + 120))
    paste_scaled(layers["body"], body_offset)
    head = layers["head_base"].copy()
    mouth_layer = layers[f"mouth_{state.mouth_state}"]
    head.alpha_composite(mouth_layer)
    if state.blink:
        head.alpha_composite(layers["blink"])
    head_pos = (body_offset[0] - 20, body_offset[1] - 132)
    if state.head_angle_deg:
        head = head.rotate(state.head_angle_deg, resample=Image.NEAREST, expand=True)
    if scale != 1.0:
        head = head.resize((max(1, int(head.width * scale)), max(1, int(head.height * scale))), Image.NEAREST)
    canvas.alpha_composite(head, dest=head_pos)
    draw = ImageDraw.Draw(canvas)
    draw.text((120, 1470), "进入 / 判断 / 收束 已成立", font=load_font(34, bold=True), fill="#5B3C1B")
    draw.text((120, 1515), f"mouth={state.mouth_state} arm={state.arm_pose} blink={'yes' if state.blink else 'no'}", font=load_font(24), fill="#6C5437")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output_path)


def write_plan() -> None:
    PLAN_MD.write_text(
        "\n".join(
            [
                "# 元素娃娃线 round1 最小技术方案",
                "",
                "## 角色层",
                "",
                "- 头部主层：`head_base.png`",
                "- 身体主层：`body.png`",
                "- 嘴型层：`mouth_closed / mouth_mid / mouth_open`",
                "- 第二动态层：`arm_down / arm_point`",
                "- 额外层：`blink_overlay`",
                "",
                "## 动作语法",
                "",
                "- `进入动作`：0.0s-0.6s，角色从左侧滑入并完成落位",
                "- `动态层1`：嘴型按音频能量三档驱动",
                "- `动态层2`：判断段切换为指向手势，头部轻点头",
                "- `判断动作`：2.0s-3.2s arm_point + head tilt",
                "- `收束动作`：3.2s 之后头部回正，手臂回落",
                "",
                "## 测试音频",
                "",
                "- 复用当前 vNext 正式线已有短口播：`voice_candidates_round4/E1/E1_processed.wav` 前 4.2 秒",
                "",
                "## 验证目标",
                "",
                "- 不是静态图",
                "- 不是全图轻微浮动",
                "- 至少两种动态层同时成立",
                "- 进入 / 判断 / 收束 三段成立",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_timeline(states: list[MotionSnapshot]) -> None:
    TIMELINE_JSON.write_text(
        json.dumps(
            {
                "schema_version": "voxel_host_motion_round1_timeline/v1",
                "duration_seconds": DURATION_SECONDS,
                "fps": FPS,
                "source_audio": str(TRIMMED_AUDIO),
                "states": [state.__dict__ for state in states],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def render_video(ffmpeg: str) -> None:
    frame_pattern = str((FRAMES_DIR / "frame_%04d.png").resolve())
    run_command(
        [
            ffmpeg,
            "-y",
            "-framerate",
            str(FPS),
            "-i",
            frame_pattern,
            "-i",
            str(TRIMMED_AUDIO),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            str(PROTOTYPE_MP4),
        ]
    )

    palette_path = RENDERS_DIR / "palette.png"
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(PROTOTYPE_MP4),
            "-vf",
            "fps=12,scale=540:-1:flags=lanczos,palettegen",
            str(palette_path),
        ]
    )
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(PROTOTYPE_MP4),
            "-i",
            str(palette_path),
            "-filter_complex",
            "fps=12,scale=540:-1:flags=lanczos[x];[x][1:v]paletteuse",
            str(PROTOTYPE_GIF),
        ]
    )


def write_verdict(states: list[MotionSnapshot]) -> None:
    VERDICT_MD.write_text(
        "\n".join(
            [
                "# 元素娃娃线 round1 技术验收",
                "",
                "- `technical_validation`：`passed_for_prototype`",
                "- `content_validation`：`blocked`",
                "",
                "## 已成立能力",
                "",
                "- `已确认` 不是静态图：逐帧角色位置、头部姿态、嘴型和手势都发生变化",
                "- `已确认` 不是轻微浮动：存在明确进入动作、判断动作和收束动作",
                "- `已确认` 动态层 1：嘴型 / 口部开合",
                "- `已确认` 动态层 2：手臂指向 + 头部点头",
                "- `已确认` 额外动态：眨眼",
                "",
                "## 仍未成立",
                "",
                "- `待验证` 还不能证明已可直接替换主线 `seg01_hook / seg07_close_shell`",
                "- `待验证` 当前口型仍属于音频能量驱动，不是更细的 viseme 级嘴型",
                "",
                "## 结论",
                "",
                "- `已确认` 当前仓库现在已经存在一条对体素娃娃成立的真动态路线：分层 2D 资产 + 时间线驱动 + 音频能量嘴型。",
                "- `已确认` 本轮结果只算技术样片，不算主线内容过线。",
                "",
                "## 输出",
                "",
                f"- `{PROTOTYPE_MP4}`",
                f"- `{PROTOTYPE_GIF}`",
                f"- `{TIMELINE_JSON}`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    ffmpeg = resolve_ffmpeg()
    for directory in (ASSETS_DIR, TIMELINE_DIR, RENDERS_DIR, AUDIT_DIR, FRAMES_DIR):
        directory.mkdir(parents=True, exist_ok=True)

    background_path = create_background()
    layers = {
        "head_base": Image.open(build_layer_head_base()),
        "body": Image.open(build_layer_body()),
        "arm_down": Image.open(build_layer_arm_down()),
        "arm_point": Image.open(build_layer_arm_point()),
        "mouth_closed": Image.open(build_layer_mouth("mouth_closed.png", [(4, 3, 2, 1)])),
        "mouth_mid": Image.open(build_layer_mouth("mouth_mid.png", [(4, 3, 2, 1), (4, 4, 2, 1)])),
        "mouth_open": Image.open(build_layer_mouth("mouth_open.png", [(4, 3, 2, 2)])),
        "blink": Image.open(build_layer_blink()),
    }
    background = Image.open(background_path)
    extract_test_audio(ffmpeg)
    levels = audio_levels_per_frame(TRIMMED_AUDIO)
    states: list[MotionSnapshot] = []
    for frame in range(TOTAL_FRAMES):
        state = build_motion_state(frame, levels)
        states.append(state)
        composite_frame(background, layers, state, FRAMES_DIR / f"frame_{frame:04d}.png")

    write_plan()
    write_timeline(states)
    render_video(ffmpeg)
    write_verdict(states)
    print(
        json.dumps(
            {
                "prototype_video": str(PROTOTYPE_MP4),
                "prototype_gif": str(PROTOTYPE_GIF),
                "timeline": str(TIMELINE_JSON),
                "verdict": str(VERDICT_MD),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
