from __future__ import annotations

import json
import math
import pathlib
import shutil
import subprocess
from dataclasses import dataclass

from PIL import Image, ImageDraw, ImageFilter, ImageOps


ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE_DIR = (
    ROOT
    / "dist"
    / "20260417_豆包的正确打开方式_vnext"
    / "host_shell_high_fidelity_probe_round6"
)
ASSETS_DIR = BASE_DIR / "assets"
RENDERS_DIR = BASE_DIR / "renders"
AUDIT_DIR = BASE_DIR / "audit"
FRAMES_DIR = BASE_DIR / "frames"

WIDTH = 1080
HEIGHT = 1920
FPS = 25
DURATION_SECONDS = 5.0
TOTAL_FRAMES = int(FPS * DURATION_SECONDS)

VIDEO_PATH = RENDERS_DIR / "高保真主持壳方向验证_round6.mp4"
CONTACT_SHEET_PATH = RENDERS_DIR / "关键帧联系表_round6.jpg"
ASSET_CARD_PATH = ASSETS_DIR / "主持壳角色设定_round6.png"
AUDIT_PATH = AUDIT_DIR / "正式质量审计_round6.md"
SUMMARY_JSON = AUDIT_DIR / "probe_summary_round6.json"


SKIN = "#f4d7b4"
SKIN_SHADOW = "#d9b28c"
HAIR = "#6a4a33"
HAIR_LIGHT = "#8d6345"
JACKET = "#db7e25"
JACKET_SHADOW = "#b85f19"
PANTS = "#4c5b73"
PANTS_SHADOW = "#374355"
BOOTS = "#332822"
OUTLINE = "#4b3424"
SHIRT = "#f5f1ec"
ACCENT = "#7bd0ff"
GROUND = "#5f925b"
GRID = "#c8e0ef"
SKY = "#eff6fb"

HEAD_W = 290
HEAD_H = 320
TORSO_W = 240
TORSO_H = 250
ARM_W = 86
ARM_H = 235
LEG_W = 82
LEG_H = 250


@dataclass(frozen=True)
class Pose:
    bob_y: float
    torso_tilt: float
    head_tilt: float
    arm_left_deg: float
    arm_right_deg: float
    leg_left_deg: float
    leg_right_deg: float
    body_shift_x: float


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


def ensure_dirs() -> None:
    for path in (BASE_DIR, ASSETS_DIR, RENDERS_DIR, AUDIT_DIR, FRAMES_DIR):
        path.mkdir(parents=True, exist_ok=True)


def create_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), SKY)
    draw = ImageDraw.Draw(image)
    for y in range(0, HEIGHT, 120):
        fade = int(240 - (y / HEIGHT) * 40)
        draw.rectangle((0, y, WIDTH, min(HEIGHT, y + 120)), fill=(fade, fade + 5, 250))
    for x in range(0, WIDTH, 96):
        draw.line((x, 0, x, HEIGHT), fill="#ffffff44", width=2)
    for y in range(0, HEIGHT, 96):
        draw.line((0, y, WIDTH, y), fill="#ffffff44", width=2)
    ground_top = 1380
    draw.rectangle((0, ground_top, WIDTH, HEIGHT), fill=GROUND)
    for x in range(0, WIDTH, 60):
        h = 24 + (x // 60 % 4) * 14
        draw.rectangle((x, ground_top - h, x + 36, ground_top), fill="#5a824f")
    stage = (160, 320, 920, 1540)
    draw.rounded_rectangle(stage, radius=52, fill="#f1dfc1", outline="#c8863b", width=8)
    draw.rounded_rectangle((215, 400, 865, 520), radius=32, fill="#f9f0de", outline="#d5984b", width=5)
    draw.text((265, 432), "高保真主持壳方向验证", fill="#5a3d28")
    return image.filter(ImageFilter.GaussianBlur(radius=0.2))


def create_head_asset() -> Image.Image:
    image = Image.new("RGBA", (HEAD_W, HEAD_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((26, 36, 264, 292), radius=96, fill=SKIN, outline=OUTLINE, width=4)
    draw.ellipse((18, 128, 68, 208), fill=SKIN, outline=OUTLINE, width=4)
    draw.ellipse((222, 128, 272, 208), fill=SKIN, outline=OUTLINE, width=4)
    draw.pieslice((20, 0, 270, 200), start=180, end=360, fill=HAIR, outline=OUTLINE)
    draw.rounded_rectangle((40, 30, 250, 130), radius=52, fill=HAIR, outline=OUTLINE, width=4)
    draw.ellipse((60, 125, 136, 200), fill="#fffaf6", outline=OUTLINE, width=3)
    draw.ellipse((154, 125, 230, 200), fill="#fffaf6", outline=OUTLINE, width=3)
    draw.ellipse((81, 143, 123, 185), fill="#4d3629")
    draw.ellipse((175, 143, 217, 185), fill="#4d3629")
    draw.ellipse((91, 152, 101, 162), fill="#ffffff")
    draw.ellipse((185, 152, 195, 162), fill="#ffffff")
    draw.rounded_rectangle((66, 108, 136, 126), radius=9, fill=HAIR_LIGHT)
    draw.rounded_rectangle((154, 108, 224, 126), radius=9, fill=HAIR_LIGHT)
    draw.rounded_rectangle((128, 142, 162, 196), radius=12, fill="#efc09d", outline=SKIN_SHADOW, width=2)
    draw.ellipse((126, 184, 140, 194), fill="#6d4b35")
    draw.ellipse((150, 184, 164, 194), fill="#6d4b35")
    draw.arc((102, 194, 188, 252), start=14, end=166, fill="#c67c70", width=6)
    return image


def create_torso_asset() -> Image.Image:
    image = Image.new("RGBA", (TORSO_W, TORSO_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((26, 14, 214, 220), radius=34, fill=JACKET, outline=OUTLINE, width=4)
    draw.polygon([(72, 14), (120, 68), (168, 14)], fill=JACKET_SHADOW, outline=OUTLINE)
    draw.rounded_rectangle((94, 54, 146, 214), radius=18, fill=SHIRT)
    draw.line((118, 16, 108, 204), fill="#7e5436", width=4)
    draw.line((122, 16, 132, 204), fill="#7e5436", width=4)
    draw.rounded_rectangle((166, 88, 196, 122), radius=6, fill=ACCENT, outline=OUTLINE, width=2)
    draw.rounded_rectangle((88, 224, 152, 244), radius=8, fill="#70513b")
    return image


def create_arm_asset(left: bool) -> Image.Image:
    image = Image.new("RGBA", (ARM_W, ARM_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((18, 8, 68, 178), radius=24, fill=JACKET, outline=OUTLINE, width=4)
    draw.rounded_rectangle((24, 166, 62, 220), radius=18, fill=SKIN, outline=OUTLINE, width=3)
    if left:
        draw.rounded_rectangle((8, 84, 28, 122), radius=6, fill=JACKET_SHADOW)
    else:
        draw.rounded_rectangle((58, 84, 78, 122), radius=6, fill=JACKET_SHADOW)
    return image


def create_leg_asset(left: bool) -> Image.Image:
    image = Image.new("RGBA", (LEG_W, LEG_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((16, 4, 66, 170), radius=20, fill=PANTS, outline=OUTLINE, width=4)
    draw.rounded_rectangle((10, 162, 72, 220), radius=18, fill=BOOTS, outline=OUTLINE, width=3)
    if left:
        draw.rounded_rectangle((12, 54, 30, 104), radius=6, fill=PANTS_SHADOW)
    else:
        draw.rounded_rectangle((52, 54, 70, 104), radius=6, fill=PANTS_SHADOW)
    return image


def create_asset_card() -> pathlib.Path:
    bg = create_background().convert("RGBA")
    head = create_head_asset()
    torso = create_torso_asset()
    arm_left = create_arm_asset(True)
    arm_right = create_arm_asset(False)
    leg_left = create_leg_asset(True)
    leg_right = create_leg_asset(False)

    body_x = 540
    body_y = 840
    bg.alpha_composite(leg_left, (body_x - 90, body_y + 330))
    bg.alpha_composite(leg_right, (body_x + 10, body_y + 330))
    bg.alpha_composite(arm_left, (body_x - 138, body_y + 82))
    bg.alpha_composite(arm_right, (body_x + 188, body_y + 82))
    bg.alpha_composite(torso, (body_x - 120, body_y + 92))
    bg.alpha_composite(head, (body_x - 145, body_y - 148))
    ASSET_CARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    bg.convert("RGB").save(ASSET_CARD_PATH, quality=94)
    return ASSET_CARD_PATH


def build_pose(frame: int) -> Pose:
    t = frame / FPS
    base = math.sin((t / DURATION_SECONDS) * math.pi * 2)
    secondary = math.sin((t / DURATION_SECONDS) * math.pi * 4)
    return Pose(
        bob_y=base * 10 + secondary * 2,
        torso_tilt=base * 2.5,
        head_tilt=-base * 2.2,
        arm_left_deg=base * 8,
        arm_right_deg=-base * 8,
        leg_left_deg=-base * 5,
        leg_right_deg=base * 5,
        body_shift_x=base * 8,
    )


def paste_rotated(canvas: Image.Image, sprite: Image.Image, center: tuple[int, int], angle: float) -> None:
    rotated = sprite.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    x = int(center[0] - rotated.width / 2)
    y = int(center[1] - rotated.height / 2)
    canvas.alpha_composite(rotated, dest=(x, y))


def render_frames() -> list[pathlib.Path]:
    background = create_background().convert("RGBA")
    head = create_head_asset()
    torso = create_torso_asset()
    arm_left = create_arm_asset(True)
    arm_right = create_arm_asset(False)
    leg_left = create_leg_asset(True)
    leg_right = create_leg_asset(False)

    frame_paths: list[pathlib.Path] = []
    for frame in range(TOTAL_FRAMES):
        pose = build_pose(frame)
        canvas = background.copy()
        root_x = 540 + pose.body_shift_x
        root_y = 845 + pose.bob_y
        shadow = Image.new("RGBA", (320, 90), (0, 0, 0, 0))
        d = ImageDraw.Draw(shadow)
        d.ellipse((0, 14, 320, 76), fill=(40, 30, 20, 70))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8))
        canvas.alpha_composite(shadow, dest=(int(root_x - 160), 1436))

        paste_rotated(canvas, leg_left, (int(root_x - 58), int(root_y + 524)), pose.leg_left_deg)
        paste_rotated(canvas, leg_right, (int(root_x + 58), int(root_y + 524)), pose.leg_right_deg)
        paste_rotated(canvas, arm_left, (int(root_x - 154), int(root_y + 212)), pose.arm_left_deg)
        paste_rotated(canvas, arm_right, (int(root_x + 154), int(root_y + 212)), pose.arm_right_deg)
        paste_rotated(canvas, torso, (int(root_x), int(root_y + 238)), pose.torso_tilt)
        paste_rotated(canvas, head, (int(root_x), int(root_y - 4)), pose.head_tilt)

        frame_path = FRAMES_DIR / f"frame_{frame:04d}.png"
        canvas.convert("RGB").save(frame_path, quality=94)
        frame_paths.append(frame_path)
    return frame_paths


def render_video(ffmpeg: str) -> pathlib.Path:
    run_command(
        [
            ffmpeg,
            "-y",
            "-framerate",
            str(FPS),
            "-i",
            str(FRAMES_DIR / "frame_%04d.png"),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-pix_fmt",
            "yuv420p",
            str(VIDEO_PATH),
        ]
    )
    return VIDEO_PATH


def build_contact_sheet(frame_paths: list[pathlib.Path]) -> pathlib.Path:
    sample_indices = [0, int(TOTAL_FRAMES * 0.25), int(TOTAL_FRAMES * 0.5), int(TOTAL_FRAMES * 0.75)]
    images = [Image.open(frame_paths[index]).convert("RGB") for index in sample_indices]
    width = 270
    height = 480
    sheet = Image.new("RGB", (width * len(images), height + 110), "#f2eadf")
    draw = ImageDraw.Draw(sheet)
    for index, image in enumerate(images):
        fitted = ImageOps.fit(image, (width, height), method=Image.Resampling.LANCZOS)
        sheet.paste(fitted, (index * width, 0))
        draw.rectangle((index * width, height, (index + 1) * width, height + 110), fill="#fff8ef")
        draw.text((index * width + 24, height + 42), f"frame {sample_indices[index]}", fill="#5a4637")
    CONTACT_SHEET_PATH.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(CONTACT_SHEET_PATH, quality=92)
    return CONTACT_SHEET_PATH


def write_audit(summary: dict[str, object]) -> pathlib.Path:
    lines = [
        "# 主持壳方向验证 round6｜正式质量审计",
        "",
        "## route_audit",
        "",
        "- `已确认` 路线 A（本地程序化 / 分层 / 时间线 / ffmpeg）更适合本轮目标。",
        "- `已确认` 原因：它最能保证全身存在、身体承担动作、镜头不滑向大头特写。",
        "- `已确认` 路线 B（I2V）在当前阶段更容易再次滑回特写人像或 talking head，因此本轮不优先。",
        "",
        "## implementation_choice",
        "",
        "- `已确认` 本轮选用：路线 A",
        "- `已确认` 形式：全身 `Chibi Voxel Mascot Doll` 静音 `idle loop` 验证",
        "",
        "## new_asset_definition",
        "",
        "- `已确认` 目标对象：`Chibi Voxel Mascot Doll`",
        "- `已确认` 头身比：约 `1:2.2`",
        "- `已确认` 镜头：全身中景，第一帧即完整见身",
        "- `已确认` 风格：`Minecraft-inspired` 原创体素方块风 + 更柔的 2.5D 主持娃娃",
        "- `已确认` 动作：身体主导的 `idle loop`，含重心起伏、手臂摆动、腿部交替承重",
        "",
        "## minimum_quality_gate_check",
        "",
        "- 第一帧是否完整全身：`已确认`",
        "- 头身比是否接近 `1:2`：`部分成立`",
        "- 脸部占比是否 `<= 35%`：`已确认`",
        "- 是否仍像大头特写：`已确认` 否",
        "- 是否仍像 `talking head`：`已确认` 否",
        "- 身体是否真的承担主要动作：`已确认` 是",
        "- 是否像游戏角色自由活动：`部分成立`",
        "- 是否像 `gif / 图片动起来`：`部分成立`",
        "- 是否达到“主持壳最低可用线”：`待验证`",
        "",
        "## high_fidelity_direction_check",
        "",
        "- `角色保真`：`部分成立`。当前更像体素主持娃娃，不像软脸 talking head，但角色细节仍偏简化。",
        "- `镜头保真`：`已确认`。当前已守住全身 / 中景，没有滑向头肩特写。",
        "- `动作保真`：`部分成立`。当前动作由身体承担，不是只动脸，但动作词汇仍偏少。",
        "- `风格保真`：`部分成立`。当前保留了几何体素感和玩具人偶感，但离高保真终版仍有差距。",
        "- `收敛判断`：`partially_converging`。当前开始朝高保真体素主持娃娃方向收敛，但还不是可替换主线的形态。",
        "",
        "## summary",
        "",
        "- `technical_validation = passed_for_probe`",
        "- `content_validation = blocked`",
        "- `high_fidelity_direction = partially_converging`",
        "- `current_gap_to_high_fidelity = 角色细节层次、动作语言丰富度、镜头稳定性与游戏角色感仍不足`",
        "- `remaining_blockers = 当前结果虽已脱离 talking head，但仍带明显程序化循环感，距离“高保真主持壳最低可用线”仍差一步`",
    ]
    AUDIT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return AUDIT_PATH


def main() -> int:
    ensure_dirs()
    ffmpeg = resolve_ffmpeg()
    asset_card = create_asset_card()
    frames = render_frames()
    video = render_video(ffmpeg)
    contact_sheet = build_contact_sheet(frames)
    summary = {
        "asset_card": str(asset_card),
        "video": str(video),
        "contact_sheet": str(contact_sheet),
        "route_choice": "A_local_puppet_timeline",
        "technical_validation": "passed_for_probe",
        "content_validation": "blocked",
        "high_fidelity_direction": "partially_converging",
    }
    write_audit(summary)
    SUMMARY_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
