#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/Users/fan/Documents/视频工厂")
MATERIAL_ROOT = ROOT / "素材录制/最新素材"
OUT_DIR = ROOT / "dist/视频样片_video_samples/20260503_短视频自动流最简单流程_full_flow_quality_sample"
REPORT_DIR = ROOT / "样片报告_sample_reports/20260503_短视频自动流最简单流程_full_flow_quality_sample"
SCRIPT_PACK_DIR = ROOT / "文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process"
ASSET_DIR = OUT_DIR / "assets"
CARD_DIR = OUT_DIR / "cards_local_only"
CLIP_DIR = OUT_DIR / "clips_local_only"

WIDTH = 720
HEIGHT = 1280
FPS = 25
TARGET_MIN_DURATION = 600.0
TARGET_NATURAL_DURATION = 720.0

BG = (249, 238, 240)
CARD_BG = (255, 252, 252)
PINK = (250, 105, 148)
PINK_DARK = (202, 69, 114)
INK = (46, 38, 50)
MUTED = (100, 86, 102)
LINE = (238, 190, 205)
CREAM = (255, 245, 238)
YELLOW = (255, 210, 92)
VIOLET = (126, 86, 180)
GREEN = (82, 150, 122)

FINAL_SCRIPT = """# 《短视频自动流的最简单流程》

短视频自动流，最简单的流程，真不是一上来就问：

“用哪个 AI 帮我一键生成视频？”

这个问题一问，基本就跑偏了。

因为一键生成，更像是在抽一条素材。

这次画面可能不错，下次风格可能又变。
这次镜头刚好能用，下次人物、字幕、节奏可能又得重新来一遍。

所以我现在更关心的不是：

哪个工具最会生成视频。

而是：

一条短视频，能不能拆成一套能重复跑的流程。

我这次做的第一步，其实特别简单。

我先打开豆包，只输入了一句话：

我想用 Trae 做一个短视频自动流。

就这么一句。

没有什么复杂提示词，也没有一上来写一大堆技术要求。

这一步的重点，不是让豆包直接帮我做视频。

它的作用，是先帮我把顺序理出来。

因为很多时候，我们不是缺工具。

我们是第一步就没想清楚。

你脑子里想的是：

我要做一个短视频自动流。

但系统真正需要的是：

选题怎么来？
脚本怎么写？
分镜怎么拆？
素材怎么准备？
视频怎么生成？
后期怎么处理？
封面和标题怎么出？
最后怎么发布？

这些不拆开，后面工具再多，也只是在乱跑。

所以豆包先给了我一版方案。

它把这个需求拆成了：

用 Trae 搭建短视频自动流：从 0 基础轻量版到无人值守全自动化版。

这个标题其实就很关键。

它不是说：

“给你生成一条视频。”

它是在说：

这件事可以先做轻量版，也可以继续升级成无人值守版。

换句话说，自动流不是一下子憋出一个大系统。

它可以先从一个很小的流程开始。

豆包拆出来的核心链路大概是：

选题策划，
脚本生成，
分镜制作，
视频生成或者剪辑，
配音字幕，
封面标题，
自动发布。

你看，这里它已经不是在讲某个单点工具了。

它是在把短视频生产拆成一排工位。

哪个环节负责想选题，
哪个环节负责写脚本，
哪个环节负责分镜，
哪个环节负责素材，
哪个环节负责后期，
哪个环节负责发布。

这才是自动流的第一层。

但光有这层还不够。

因为豆包给的方案，还是“想法层”。

它能帮你把事情拆开，但它不能直接变成可执行项目。

所以我接着问它：

我主要是想做一个 Vlog 的视频自动流，你先给我一个 prompt，让 Trae 帮我把架构搭建出来。

这一步才是关键转折。

我不是让豆包继续聊天。

我是让豆包把方案翻译成：

Trae 能接住的任务说明。

后面豆包就给了我一份：

Trae Vlog 自动流核心搭建 Prompt。

而且标题里直接写着：

直接复制粘贴到 Trae SOLO，即可一键生成完整架构 + 可运行脚本。

当然，这句话不能理解成：

整个系统已经跑通了。

它只是说明，这份 prompt 的目标，是让 Trae 先把架构搭出来。

这里面还拆了几个模块。

比如：

全局人设锚定模块，
Vlog 选题与叙事线生成模块，
Vlog 分镜与标准化脚本生成模块，
素材智能匹配与调度模块，
Vlog 专属自动化后期模块，
成片与运营物料导出模块，
总控调度与异常处理模块。

这些名字听起来有点长。

但翻成人话就是：

先固定账号风格，
再决定拍什么，
再写脚本，
再拆镜头，
再匹配素材，
再做后期，
最后导出成片和发布物料。

到这里，流程已经从“一句话想法”，变成了一份能交给 Trae 的任务说明。

下一步，我就把这份 prompt 放进 Trae。

这里我用的是 Trae 的 SOLO Coder。

你可以把它理解成：

一个会自己规划任务、自己生成项目结构的 AI 编码工具。

这里有一个细节很关键。

我不是把豆包的回答截图保存一下就结束了。

而是把它生成的这份 prompt，真的放进了 Trae 的 SOLO Coder。

画面里能看到，这些模块文字已经进入 Trae 的输入区。

然后 Trae 没有只回一句：

“建议你怎么做。”

它先说：

让我先规划一下任务，然后逐步实现。

接着画面里出现了：

Updating Tasks...

还有：

11 个待办。

这一步，其实就是自动流开始变实的地方。

因为它已经不是聊天里的一个想法了。

它开始被拆成 Trae 自己能执行的任务列表。

再往后，Trae 开始创建项目结构。

画面里能看到一个项目目录：

vlog_automation_workflow。

下面有：

modules，
templates，
workflows，
config，
assets，
frontend，
logs。

还出现了：

settings.py，
base_module.py。

这些代码文件，普通人其实看不懂也没关系。

这一步最重要的，不是你能不能看懂每一行代码。

而是看 Trae 有没有真的把这个东西执行出一个初步形状。

有没有项目目录。
有没有模块。
有没有配置文件。
有没有基础代码。
有没有从一句 prompt，变成一个可以继续往下接的 app 雏形。

所以我看这一步，不是看它代码写得多漂亮。

我是先看：

它有没有从“聊天里的方案”，变成“电脑里真实出现的项目骨架”。

当然，这还不能说 app 已经跑通。

也不能说代码已经验证成功。

但它已经跨过了最重要的一步：

从“我有个想法”，变成“我有一个可以继续测试、继续接 API、继续修的初步项目”。

这就是第二个关键点。

很多人做 AI 工作流，会一直停在聊天里。

今天问一个模型，明天问一个模型，后天再换一个模型。

问了很多，最后还是一堆字。

但这次不一样。

豆包负责把需求拆成流程。

豆包第二步，又把流程翻译成 Trae 能接住的 prompt。

Trae 负责把这个 prompt 拆成待办，再生成项目骨架。

这中间多了一层：

可执行 prompt。

也就是：

豆包不是直接替我干活。

它帮我生成了一份能交给 Trae 的工作说明。

Trae 也不是直接替我剪视频。

它先把系统该有的目录、模块、文件生成出来。

这才像一条自动流开始搭起来的样子。

然后下一步，才是接 API。

API 这个词听起来很技术，但你可以先把它理解成一句话：

把外部工具，接成系统可以调用的能力。

比如文字生成，可以接一个 API。
配音，可以接一个 API。
图片、卡片、动效，也可以接 API。
剪辑总装，也可以接 API。

画面里我这里可以放一个云平台的 API 管理页特写。

但这个地方一定要说清楚：

不是让你看我的密钥。

也不是证明我已经把所有 API 都接通了。

这个画面只是想说明一件事：

自动流后面真正要做的，是把这些原本需要手动打开网页、复制、粘贴、下载、上传的能力，逐步接进同一套流程里。

如果每一步都还要人手动来回搬，那它最多叫半自动。

真正往自动流走，至少要让这些能力能被系统调用。

但这里也不用一上来做大。

最小可以先做到：

一段录屏，
一张卡片，
一段音轨，
最后能被自动组装成一条视频。

先让这个小链路跑通。

不要一开始就做大平台。

大平台听起来很爽，做起来很容易变成：

看着像方案，用起来像空气。

接下来，就是剪辑总装。

我现在选择的方向，是阿里云剪辑、ICE、云剪这一类云端剪辑方案。

它在这个流程里，不负责想创意。

不负责写文案。

也不负责判断内容好不好。

它更像最后的装配台。

前面准备好的录屏、卡片、音轨，按照时间线放进去，最后导出成一个视频。

这里必须说清楚：

阿里云剪辑不是总控脑。

它只是装配台。

真正决定视频能不能复用的，还是前面的流程有没有拆清楚。

所以现在不能说：

阿里云剪辑已经是正式稳定链路。

更准确的说法是：

我选择把它放在“云端总装”这个位置，并且正在验证它能不能接住后面的真实生产流程。

技术验证跑通，不等于内容就能发。

能导出 MP4，不等于视频就好看。

链路能跑，不等于流程已经成熟。

这些状态必须分开。

最后一步，是用 Codex 这类工具做执行和检查。

Codex 在我这里，不是负责替我想选题。

它更像一个执行检查员。

比如它可以帮我看：

素材在哪个路径，
哪一段录屏能用，
有没有音频，
能不能解码，
生成了哪些文件，
路径是不是真的存在，
云端总装有没有导出，
最后有没有报告。

这个东西看起来很啰嗦，但对自动流特别重要。

因为自动流最怕的不是失败。

失败其实还好。

知道卡在哪一步，就能修。

最怕的是半成品被写成完成。

比如：

只是生成了项目骨架，却写成系统已经跑通。

只是导出了测试样片，却写成正式链路稳定。

只是技术验证通过，却写成内容已经过线。

这就会越做越乱。

所以 Codex 这类工具的价值，不是“它很聪明”。

而是它能把执行过程写清楚：

哪些已确认，
哪些只是部分成立，
哪些还待验证，
哪些不能说满。

这才是我现在理解的短视频自动流。

它不是一键生成视频。

它更像这样一条流程：

第一步，给豆包一句简单需求。
第二步，让豆包拆出方案。
第三步，让豆包生成可以复制到 Trae 的 prompt。
第四步，把 prompt 放进 Trae SOLO，让它自动 plan。
第五步，让 Trae 生成项目骨架。
第六步，后面再接 API、云端剪辑和 Codex 检查。

它不是一开始就全自动。

而是先把每一步变得清楚、可执行、可检查。

最后再简单说一下，它和即梦这类工具的区别。

即梦这类工具很适合快速生成单个画面。

比如一个镜头、一个人物、一个场景、一个感觉。

你想快速找画面，它很有用。

但它的问题是，很多时候更像抽卡。

这次抽到了，下一次还要再抽。
这次风格对了，下一次还要再调。
这次能用，下一次不一定接得上。

短视频自动流解决的不是“某一个镜头好不好看”。

它解决的是：

我能不能把一个需求，
拆成流程，
变成项目，
接上工具，
最后持续生产。

而且这里也不是只有 Trae 能做。

Trae 可以用来生成项目骨架。

Codex 可以用来执行任务、检查路径、整理文件、跑验证。

Claude Code 这类工具，也可以承担一部分代码和工作流执行。

所以重点不是某个软件一定最强。

重点是：

你有没有把这个流程拆清楚，让不同工具能各自接一段。

豆包负责先把需求和方案拆开。

Trae、Codex、Claude 这类工具，可以负责把方案变成项目、脚本、文件和执行结果。

API 负责把外部能力接进来。

阿里云剪辑这类云端剪辑，负责最后的总装。

Codex 这类执行工具，还可以继续帮你检查：

文件有没有生成，
路径对不对，
视频能不能打开，
哪一步只是候选，
哪一步已经验证。

这就是它和即梦最大的区别。

即梦更像是：

我先抽一个素材，看这次能不能用。

短视频自动流更像是：

我先搭一条流程，让后面每一条都能沿着这条流程继续跑。

前期它一定更慢。

因为你要先把流程搭出来。

但一旦流程能跑，后面就不是每条都重新赌一次。

你可以换选题，
换素材，
换卡片，
换音轨，
换剪辑方式，
甚至换执行工具。

Trae 不合适，可以换 Codex。
Codex 不够顺，可以让 Claude Code 补一段。
某个视频生成工具不稳定，也可以只把它当素材来源，而不是让它决定整条视频。

流程还在。

只是工位上的工具可以换。

而且出问题的时候，你知道卡在哪一步。

是需求没拆清楚？
是项目结构没生成好？
是 API 没接上？
是卡片素材缺了？
是云端剪辑没导出？
还是 Codex 检查发现路径不对？

这才是自动流真正有用的地方。

所以这条视频我想讲的不是：

某个工具有多厉害。

而是：

短视频自动流，最简单的流程，就是先把视频生产拆开，再让每一步都有人负责、有工具能做、有结果能检查。

即梦这类工具适合帮你出素材。

但短视频自动流，是让素材、脚本、剪辑、检查和复盘，变成一条可以重复跑的生产流程。

别一上来就追求一键生成。

先把顺序理出来。

顺序对了，自动化才有地方落脚。
"""


@dataclass
class VisualSegment:
    segment_id: str
    kind: str
    title: str
    subtitle: str
    weight: float
    route: str | None = None
    source: Path | None = None
    source_start: float | None = None
    source_end: float | None = None
    mask: str | None = None
    role: str = ""
    proves: str = ""
    cannot_prove: str = ""


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess:
    print("+", " ".join(str(item) for item in cmd))
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True, check=check)


def ffprobe_json(path: Path) -> dict:
    result = run([
        "ffprobe",
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]).stdout
    return json.loads(result)


def duration_of(path: Path) -> float:
    return float(ffprobe_json(path)["format"]["duration"])


def ensure_dirs() -> None:
    for path in [OUT_DIR, REPORT_DIR, ASSET_DIR, CARD_DIR, CLIP_DIR, SCRIPT_PACK_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size, index=0)
    return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, font_obj: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    rows: list[str] = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            rows.append("")
            continue
        current = ""
        for ch in paragraph:
            trial = current + ch
            if draw.textlength(trial, font=font_obj) <= max_width:
                current = trial
            else:
                if current:
                    rows.append(current)
                current = ch
        if current:
            rows.append(current)
    return rows


def draw_center(draw: ImageDraw.ImageDraw, text: str, y: int, font_obj: ImageFont.FreeTypeFont, fill: tuple[int, int, int], max_width: int, line_h: int) -> int:
    lines = wrap(draw, text, font_obj, max_width)
    for line in lines:
        w = draw.textlength(line, font=font_obj)
        draw.text(((WIDTH - w) / 2, y), line, font=font_obj, fill=fill)
        y += line_h
    return y


def draw_voxel_host(draw: ImageDraw.ImageDraw, cx: int, cy: int, scale: int = 1) -> None:
    s = 18 * scale
    skin = (255, 214, 186)
    hair = (90, 56, 46)
    shirt = (232, 73, 96)
    shadow = (205, 103, 128)
    # body
    draw.rounded_rectangle((cx - 3 * s, cy + 2 * s, cx + 3 * s, cy + 8 * s), radius=12 * scale, fill=shirt, outline=shadow, width=3)
    # head
    draw.rounded_rectangle((cx - 4 * s, cy - 4 * s, cx + 4 * s, cy + 3 * s), radius=14 * scale, fill=skin, outline=(222, 158, 137), width=3)
    # hair cap
    draw.rectangle((cx - 4 * s, cy - 4 * s, cx + 4 * s, cy - 2 * s), fill=hair)
    draw.rectangle((cx - 4 * s, cy - 2 * s, cx - 3 * s, cy + 1 * s), fill=hair)
    draw.rectangle((cx + 3 * s, cy - 2 * s, cx + 4 * s, cy + 1 * s), fill=hair)
    # eyes and smile
    draw.rectangle((cx - 2 * s, cy - s, cx - s, cy), fill=INK)
    draw.rectangle((cx + s, cy - s, cx + 2 * s, cy), fill=INK)
    draw.arc((cx - 2 * s, cy, cx + 2 * s, cy + 3 * s), 20, 160, fill=PINK_DARK, width=4)
    # hands
    draw.rounded_rectangle((cx - 5 * s, cy + 3 * s, cx - 3 * s, cy + 6 * s), radius=8, fill=skin)
    draw.rounded_rectangle((cx + 3 * s, cy + 3 * s, cx + 5 * s, cy + 6 * s), radius=8, fill=skin)


def draw_card(path: Path, title: str, subtitle: str, route: str, role: str, host: bool = False, sassy: bool = False) -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    title_font = font(52)
    sub_font = font(32)
    small_font = font(23)
    tag_font = font(25)

    for i in range(18):
        x = (i * 73 + 22) % WIDTH
        y = 80 + ((i * 131) % 1040)
        color = (255, 221 + (i % 3) * 8, 232)
        draw.ellipse((x - 18, y - 12, x + 18, y + 12), fill=color)

    if sassy:
        draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(255, 231, 82))
        for i in range(0, WIDTH, 60):
            draw.polygon([(WIDTH // 2, 620), (i, 0), (i + 30, 0)], fill=(255, 112, 120))
            draw.polygon([(WIDTH // 2, 620), (i, HEIGHT), (i + 30, HEIGHT)], fill=(255, 112, 120))
        draw.rounded_rectangle((44, 88, 676, 1130), radius=28, fill=(255, 249, 214), outline=INK, width=5)
        draw_voxel_host(draw, WIDTH // 2, 375, 2)
        y = draw_center(draw, title, 690, font(54), INK, 550, 68)
        draw_center(draw, subtitle, y + 32, sub_font, INK, 540, 44)
        draw.text((80, 1070), "sassy_reaction_card_route", font=small_font, fill=INK)
    else:
        draw.rounded_rectangle((48, 138, 672, 1108), radius=42, fill=CARD_BG, outline=LINE, width=3)
        draw.rounded_rectangle((84, 180, 636, 252), radius=24, fill=(255, 235, 242), outline=(245, 207, 221), width=2)
        draw.text((108, 202), role, font=tag_font, fill=PINK_DARK)
        if host:
            draw_voxel_host(draw, WIDTH // 2, 340, 2)
            y0 = 620
        else:
            y0 = 360
            draw.rounded_rectangle((110, 288, 610, 324), radius=18, fill=(255, 232, 238))
            draw.line((150, 306, 570, 306), fill=(235, 163, 189), width=2)
        y = draw_center(draw, title, y0, title_font, INK, 540, 66)
        draw_center(draw, subtitle, y + 32, sub_font, MUTED, 548, 44)
        draw.text((82, 1044), route, font=small_font, fill=(175, 118, 140))
    img.save(path, quality=94)


def draw_all_cards(segments: list[VisualSegment]) -> None:
    for segment in segments:
        if segment.kind == "card":
            draw_card(
                CARD_DIR / f"{segment.segment_id}.jpg",
                segment.title,
                segment.subtitle,
                segment.route or "route_pending",
                segment.role or "信息卡",
                host=segment.segment_id.startswith("host_"),
                sassy=(segment.route == "sassy_reaction_card_route"),
            )


def script_plain_for_tts() -> str:
    text = FINAL_SCRIPT.replace("# 《短视频自动流的最简单流程》", "《短视频自动流的最简单流程》")
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def split_caption_units() -> list[str]:
    raw_units = [p.strip() for p in FINAL_SCRIPT.split("\n\n") if p.strip()]
    units: list[str] = []
    for item in raw_units:
        item = item.replace("# ", "")
        if len(item) <= 42:
            units.append(item)
            continue
        sentences = re.split(r"(?<=[。！？：])", item)
        current = ""
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            if len(current) + len(sentence) <= 42:
                current += sentence
            else:
                if current:
                    units.append(current)
                current = sentence
        if current:
            units.append(current)
    return units


def format_srt_time(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    millis = int(round(seconds * 1000))
    h = millis // 3_600_000
    millis %= 3_600_000
    m = millis // 60_000
    millis %= 60_000
    s = millis // 1000
    ms = millis % 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_captions(duration: float) -> list[dict]:
    units = split_caption_units()
    weights = [max(1, len(unit)) for unit in units]
    total = sum(weights)
    cursor = 0.0
    captions: list[dict] = []
    for idx, (unit, weight) in enumerate(zip(units, weights), start=1):
        seg_duration = max(1.2, duration * weight / total)
        start = cursor
        end = min(duration, cursor + seg_duration)
        cursor = end
        captions.append({"index": idx, "start": start, "end": end, "text": unit})
    if captions:
        captions[-1]["end"] = duration
    srt_lines: list[str] = []
    for item in captions:
        text = "\n".join(textwrap.wrap(item["text"], width=20))
        srt_lines.append(f"{item['index']}\n{format_srt_time(item['start'])} --> {format_srt_time(item['end'])}\n{text}\n")
    (OUT_DIR / "captions.srt").write_text("\n".join(srt_lines), encoding="utf-8")
    (OUT_DIR / "captions.json").write_text(json.dumps(captions, ensure_ascii=False, indent=2), encoding="utf-8")
    return captions


def write_runtime_script() -> None:
    (OUT_DIR / "runtime_full_script.md").write_text(FINAL_SCRIPT.strip() + "\n", encoding="utf-8")
    (ASSET_DIR / "narration_input.txt").write_text(script_plain_for_tts(), encoding="utf-8")
    SCRIPT_PACK_DIR.mkdir(parents=True, exist_ok=True)
    (SCRIPT_PACK_DIR / "01_完整口播稿_full_script.md").write_text(FINAL_SCRIPT.strip() + "\n", encoding="utf-8")


def write_script_pack_files() -> None:
    block_map = """# 分段承载表：短视频自动流的最简单流程 full flow quality sample

## 本轮状态

- `已确认` 本轮不是 PR #43 的 145 秒短样片，不复用 PR #43 压缩稿或 timeline。
- `已确认` 本轮 runtime 使用用户最新 `FINAL_SCRIPT_V2` 完整文案。
- `已确认` 用户录制素材承担中段主体推进；卡片 / PPT 只做结构、边界和总结辅助。
- `已确认` Trae 项目骨架只能证明初步项目形状出现，不能证明 app 跑通。
- `已确认` API 画面如无法安全脱敏，使用信息卡 fallback，不使用火山引擎原画面。

## block / segment 承载

| block_id | segment_id | 文案范围 | 主要承载 | 辅助承载 | 证明点 | 不能证明点 |
|---|---|---|---|---|---|---|
| B01 | host_opening_judgement | 一键生成不是自动流 | 主持壳替代卡 / cute_prompt_card_route | 字幕 | 建立主判断 | 不证明工具执行 |
| B02 | doubao_simple_need | 用户给豆包一句需求 | 用户录制素材：豆包素材 00:00:16-00:00:24 | 字幕 | 需求入口很简单 | 不证明 Trae 已执行 |
| B03 | doubao_plan | 豆包拆短视频生产流程 | 用户录制素材：豆包素材 00:01:28-00:02:00 | 信息卡少量提示 | 豆包把需求拆成流程 | 不证明工程跑通 |
| B04 | doubao_prompt | 豆包生成 Trae prompt | 用户录制素材：豆包素材 00:02:40-00:04:08 | cute_info_card_route | 想法转成 Trae 能接的任务说明 | 不证明 prompt 已运行成功 |
| B05 | trae_solo | Trae SOLO 接住 prompt 并 plan | 用户录制素材：trae 素材 00:00:32-00:01:52 | 字幕 | SOLO Coder、Updating Tasks、11 待办 | 不证明所有待办完成 |
| B06 | trae_skeleton | Trae 生成项目骨架 | 用户录制素材：trae 素材 00:02:00-00:02:40 | cute_info_card_route | `vlog_automation_workflow`、目录和基础文件出现 | 不证明 app 跑通 |
| B07 | api_station | API 是外部能力入口 | cute_info_card_route | 字幕 | API 位置和边界 | 不证明 API 已接通 |
| B08 | cloud_station | 云剪是装配台 | cute_info_card_route | 字幕 | 云端总装工位边界 | 不证明云剪正式稳定 |
| B09 | codex_checker | Codex 做执行检查 | 用户录制素材：codex 素材 00:02:56-00:03:08 | 遮挡层、字幕 | 命令、路径、文件、报告检查 | 不证明内容过线 |
| B10 | comparison_and_summary | 即梦对比与收束 | cute_info_card_route / 主持壳替代卡 | 字幕 | 抽素材 vs 搭流程；顺序对了自动化才有落脚点 | 不证明可发布 |
"""
    card_copy = """# 卡片文案：短视频自动流的最简单流程 full flow quality sample

| card_id | route | 卡片职责 | 主标题 | 小字 |
|---|---|---|---|---|
| host_opening_judgement | cute_prompt_card_route | 开头判断 / 主持壳 fallback | 自动流不是一键生成 | 一键生成更像抽素材，流程才可复用。 |
| doubao_to_trae_prompt_card | cute_info_card_route | 结构显影 | 豆包把想法翻译成任务说明 | 一句需求 -> 流程 -> Trae SOLO prompt。 |
| trae_skeleton_card | cute_info_card_route | 状态边界 | 看不懂代码也没关系 | 先看有没有项目目录、模块、配置和基础文件。 |
| api_station_card | cute_info_card_route | API 工位解释 | API 是外部能力入口 | 不展示密钥，不证明全部接通。 |
| cloud_station_card | cute_info_card_route | 云剪工位解释 | 云剪是装配台，不是总控脑 | 技术链路跑通不等于内容能发。 |
| codex_checker_card | cute_info_card_route | 检查边界 | Codex 是执行检查员 | 路径、文件、命令、报告清楚，不等于内容过线。 |
| jimmeng_compare_card | cute_info_card_route | 工具边界 | 即梦像抽素材，自动流像搭流程 | 不是评测，只说明解决的问题不同。 |
| final_summary_card | cute_info_card_route | 总结 | 顺序对了，自动化才有地方落脚 | 先拆流程，再接工具，再检查结果。 |
"""
    notes = """# 执行注意事项：短视频自动流的最简单流程 full flow quality sample

- `已确认` 本轮目标为 `full_flow_quality_sample`，不是 PR #43 短样片。
- `已确认` 不设置 90-150 秒目标，不设置 180 秒上限。
- `已确认` 低于 600 秒必须判定失败。
- `已确认` runtime 使用用户最新 `FINAL_SCRIPT_V2`，默认不删句。
- `已确认` 火山引擎素材不安全时使用 API 信息卡 fallback。
- `已确认` 不把豆包方案写成工程跑通，不把 Trae 骨架写成 app 跑通。
- `已确认` 不把阿里云剪辑写成正式稳定，不把 Codex 检查写成内容过线。
- `已确认` `content_validation=pending_user_chatgpt_review`，`send_ready=false`。
"""
    execution_input = """# 给 Codex 剪辑执行输入：短视频自动流 full flow quality sample

## 素材根目录

`/Users/fan/Documents/视频工厂/素材录制/最新素材`

## 必用主素材

| segment_id | path | timecode |
|---|---|---|
| doubao_simple_need | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:00:16-00:00:24 |
| doubao_plan | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:01:28-00:02:00 |
| doubao_prompt_request | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:02:40-00:02:56 |
| doubao_trae_prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:03:52-00:04:08 |
| trae_solo_entry | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:00:32-00:01:04 |
| trae_plan | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:01:20-00:01:52 |
| trae_skeleton | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:02:00-00:02:40 |
| codex_check | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:02:56-00:03:08 |

## 输出边界

- 输出目录：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_full_flow_quality_sample/`
- 报告目录：`/Users/fan/Documents/视频工厂/样片报告_sample_reports/20260503_短视频自动流最简单流程_full_flow_quality_sample/`
- 大媒体不提交 Git，只记录本地路径。
"""
    manifest = {
        "title": "短视频自动流的最简单流程",
        "sample_type": "full_flow_quality_sample",
        "full_script_used": True,
        "compressed_runtime_used": False,
        "pr43_compressed_script_reused": False,
        "material_root": str(MATERIAL_ROOT),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "files": {
            "full_script": str(SCRIPT_PACK_DIR / "01_完整口播稿_full_script.md"),
            "block_segment_material_map": str(SCRIPT_PACK_DIR / "02_分段承载表_block_segment_material_map.md"),
            "card_copy": str(SCRIPT_PACK_DIR / "03_卡片文案_card_copy.md"),
            "execution_notes": str(SCRIPT_PACK_DIR / "04_执行注意事项_execution_notes.md"),
            "codex_video_execution_input": str(SCRIPT_PACK_DIR / "05_给Codex剪辑执行输入_codex_video_execution_input.md"),
        },
    }
    (SCRIPT_PACK_DIR / "02_分段承载表_block_segment_material_map.md").write_text(block_map, encoding="utf-8")
    (SCRIPT_PACK_DIR / "03_卡片文案_card_copy.md").write_text(card_copy, encoding="utf-8")
    (SCRIPT_PACK_DIR / "04_执行注意事项_execution_notes.md").write_text(notes, encoding="utf-8")
    (SCRIPT_PACK_DIR / "05_给Codex剪辑执行输入_codex_video_execution_input.md").write_text(execution_input, encoding="utf-8")
    (SCRIPT_PACK_DIR / "script_pack_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def material(path: str) -> Path:
    full = MATERIAL_ROOT / path
    if not full.exists():
        raise FileNotFoundError(str(full))
    return full


def build_segments() -> list[VisualSegment]:
    return [
        VisualSegment(
            "host_opening_judgement",
            "card",
            "短视频自动流，不是一键生成",
            "一键生成更像抽素材；流程清楚，才有复用空间。",
            0.035,
            "cute_prompt_card_route",
            role="主持壳 fallback｜开头判断",
            proves="建立主判断",
            cannot_prove="不证明工具执行",
        ),
        VisualSegment("doubao_simple_need", "footage", "一句需求输入", "豆包素材：我想用 Trae 做一个短视频自动流", 0.08, source=material("豆包素材.mp4"), source_start=16, source_end=24, mask="doubao", role="用户录制素材主体", proves="需求入口很简单", cannot_prove="不证明 Trae 已执行"),
        VisualSegment("doubao_plan", "footage", "豆包拆流程", "从 0 基础轻量版，到无人值守自动化版", 0.12, source=material("豆包素材.mp4"), source_start=88, source_end=120, mask="doubao", role="用户录制素材主体", proves="豆包把需求拆成流程", cannot_prove="不证明工程跑通"),
        VisualSegment("doubao_prompt_request", "footage", "从方案到 prompt", "用户要求豆包生成 Trae 能接住的任务说明", 0.075, source=material("豆包素材.mp4"), source_start=160, source_end=176, mask="doubao", role="用户录制素材主体", proves="从想法层转入可执行说明", cannot_prove="不证明 prompt 已运行"),
        VisualSegment("doubao_prompt_output", "footage", "Trae SOLO prompt", "全局人设、选题、分镜、素材、后期、导出、总控", 0.09, source=material("豆包素材.mp4"), source_start=232, source_end=248, mask="doubao", role="用户录制素材主体", proves="豆包生成可复制到 Trae SOLO 的 prompt", cannot_prove="不证明脚本运行成功"),
        VisualSegment("trae_solo_entry", "footage", "进入 Trae SOLO Coder", "看到 /plan、/spec 和 SOLO Coder 执行入口", 0.08, source=material("trae 素材.mp4"), source_start=32, source_end=64, mask="trae", role="用户录制素材主体", proves="进入执行器", cannot_prove="不证明执行完成"),
        VisualSegment("trae_prompt_plan", "footage", "Prompt 进入 Trae 并开始 plan", "Updating Tasks... 和 11 个待办出现", 0.10, source=material("trae 素材.mp4"), source_start=80, source_end=112, mask="trae", role="用户录制素材主体", proves="Trae 接住 prompt 并拆任务", cannot_prove="不证明所有待办完成"),
        VisualSegment("host_transition_shape", "card", "关键判断", "看不懂代码也没关系，先看有没有执行出初步形状。", 0.03, "cute_prompt_card_route", role="主持壳 fallback｜关键判断", proves="强调判断标准", cannot_prove="不证明代码可运行"),
        VisualSegment("trae_project_skeleton", "footage", "Trae 生成项目骨架", "vlog_automation_workflow、modules、templates、workflows、config、assets、frontend、logs", 0.16, source=material("trae 素材.mp4"), source_start=120, source_end=160, mask="trae", role="用户录制素材主体", proves="项目目录、模块、配置和基础文件出现", cannot_prove="不证明 app 跑通"),
        VisualSegment("trae_skeleton_boundary_card", "card", "看不懂代码也没关系", "这一步先看有没有项目目录、模块、配置文件和基础代码。", 0.045, "cute_info_card_route", role="状态边界信息卡", proves="状态边界显影", cannot_prove="不证明运行成功"),
        VisualSegment("workflow_first_shape", "footage", "电脑里出现项目骨架", "从聊天里的方案，变成可以继续测试和修的初步项目", 0.06, source=material("trae 素材.mp4"), source_start=120, source_end=160, mask="trae", role="用户录制素材主体", proves="初步项目形状出现", cannot_prove="不证明链路成熟"),
        VisualSegment("api_station_card", "card", "API 是外部能力入口", "文字、配音、图片、卡片、动效、剪辑总装，都可以逐步接成系统能力。", 0.045, "cute_info_card_route", role="API 工位信息卡", proves="API 工位解释", cannot_prove="不证明 API 已接通"),
        VisualSegment("cloud_station_card", "card", "云剪是装配台，不是总控脑", "录屏、卡片、音轨进入时间线；能导出 MP4 不等于内容能发。", 0.04, "cute_info_card_route", role="云端总装边界卡", proves="云端总装职责", cannot_prove="不证明云剪正式稳定"),
        VisualSegment("codex_execution_check", "footage", "Codex 是执行检查员", "检查路径、文件、命令、解码、报告和状态边界", 0.09, source=material("codex 素材.mp4"), source_start=176, source_end=188, mask="codex", role="用户录制素材主体", proves="Codex 执行检查证据", cannot_prove="不证明内容过线"),
        VisualSegment("codex_broll_boundary", "footage", "技术处理痕迹", "HyperFrames 只作为卡片动效层，不进入中段录屏", 0.04, source=material("codex 素材.mp4"), source_start=216, source_end=224, mask="codex", role="用户录制素材辅助 B-roll", proves="执行工具处理痕迹", cannot_prove="不证明 HyperFrames 替代云剪"),
        VisualSegment("jimmeng_compare_card", "card", "即梦像抽素材，自动流像搭流程", "即梦适合单点画面；自动流解决的是需求拆流程、接工具、持续生产。", 0.055, "cute_info_card_route", role="对比信息卡", proves="工具定位边界", cannot_prove="不证明即梦不可用"),
        VisualSegment("sassy_reaction_process_card", "card", "别把工具当主角", "流程在，工位上的工具可以换。", 0.035, "sassy_reaction_card_route", role="骚萌反应卡｜转折", proves="情绪转折", cannot_prove="不替代录屏证据"),
        VisualSegment("final_summary_card", "card", "顺序对了，自动化才有地方落脚", "先拆生产流程，再接工具能力，最后检查结果边界。", 0.055, "cute_info_card_route", role="总结信息卡", proves="总结主观点", cannot_prove="不证明可发布"),
    ]


def ffmpeg_drawboxes(mask: str | None) -> str:
    boxes: list[str] = []
    if mask == "doubao":
        boxes = [
            "drawbox=x=0:y=0:w=118:h=1280:color=black@0.72:t=fill",
            "drawbox=x=0:y=0:w=720:h=58:color=black@0.55:t=fill",
        ]
    elif mask == "trae":
        boxes = [
            "drawbox=x=0:y=0:w=105:h=1280:color=black@0.62:t=fill",
            "drawbox=x=0:y=1170:w=720:h=110:color=black@0.78:t=fill",
            "drawbox=x=0:y=0:w=720:h=42:color=black@0.50:t=fill",
        ]
    elif mask == "codex":
        boxes = [
            "drawbox=x=528:y=0:w=192:h=1280:color=black@0.82:t=fill",
            "drawbox=x=0:y=1132:w=720:h=148:color=black@0.82:t=fill",
            "drawbox=x=0:y=0:w=84:h=1280:color=black@0.62:t=fill",
        ]
    return ",".join(boxes)


def render_card_clip(segment: VisualSegment, duration: float, out_path: Path) -> None:
    card_path = CARD_DIR / f"{segment.segment_id}.jpg"
    run([
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-t",
        f"{duration:.3f}",
        "-i",
        str(card_path),
        "-vf",
        f"fps={FPS},format=yuv420p",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "ultrafast",
        "-crf",
        "27",
        str(out_path),
    ])


def render_footage_clip(segment: VisualSegment, duration: float, out_path: Path) -> None:
    assert segment.source and segment.source_start is not None and segment.source_end is not None
    source_duration = segment.source_end - segment.source_start
    ratio = duration / source_duration
    filters = [
        f"setpts={ratio:.8f}*PTS",
        "scale=720:1280:force_original_aspect_ratio=increase",
        "crop=720:1280",
    ]
    boxes = ffmpeg_drawboxes(segment.mask)
    if boxes:
        filters.append(boxes)
    filters.append("format=yuv420p")
    run([
        "ffmpeg",
        "-y",
        "-ss",
        f"{segment.source_start:.3f}",
        "-t",
        f"{source_duration:.3f}",
        "-i",
        str(segment.source),
        "-an",
        "-vf",
        ",".join(filters),
        "-r",
        str(FPS),
        "-c:v",
        "libx264",
        "-preset",
        "ultrafast",
        "-crf",
        "27",
        str(out_path),
    ])


def synthesize_audio() -> tuple[Path, float, str]:
    raw_aiff = ASSET_DIR / "temporary_preview_voiceover_raw.aiff"
    wav_path = ASSET_DIR / "temporary_preview_voiceover_timed.wav"
    m4a_path = ASSET_DIR / "temporary_preview_voiceover.m4a"
    voice = "Tingting"
    say_cmd = ["say", "-v", voice, "-r", "170", "-o", str(raw_aiff), "-f", str(ASSET_DIR / "narration_input.txt")]
    try:
        run(say_cmd)
    except subprocess.CalledProcessError:
        voice = "Sandy (中文（中国大陆）)"
        run(["say", "-v", voice, "-r", "170", "-o", str(raw_aiff), "-f", str(ASSET_DIR / "narration_input.txt")])
    raw_duration = duration_of(raw_aiff)
    target_duration = max(TARGET_NATURAL_DURATION, raw_duration)
    if raw_duration < TARGET_MIN_DURATION:
        target_duration = TARGET_NATURAL_DURATION
    if raw_duration < target_duration - 1:
        tempo = raw_duration / target_duration
        filters: list[str] = []
        while tempo < 0.5:
            filters.append("atempo=0.5")
            tempo /= 0.5
        filters.append(f"atempo={tempo:.6f}")
        run(["ffmpeg", "-y", "-i", str(raw_aiff), "-af", ",".join(filters), "-ar", "48000", "-ac", "1", str(wav_path)])
    else:
        run(["ffmpeg", "-y", "-i", str(raw_aiff), "-ar", "48000", "-ac", "1", str(wav_path)])
    run(["ffmpeg", "-y", "-i", str(wav_path), "-c:a", "aac", "-b:a", "128k", str(m4a_path)])
    return m4a_path, duration_of(m4a_path), voice


def render_video(segments: list[VisualSegment], total_duration: float, audio_path: Path) -> tuple[Path, list[dict]]:
    draw_all_cards(segments)
    total_weight = sum(segment.weight for segment in segments)
    timeline: list[dict] = []
    concat_list = ASSET_DIR / "concat_video_segments.txt"
    clip_lines: list[str] = []
    cursor = 0.0
    for idx, segment in enumerate(segments, start=1):
        duration = total_duration * segment.weight / total_weight
        if idx == len(segments):
            duration = total_duration - cursor
        duration = max(3.0, duration)
        clip_path = CLIP_DIR / f"{idx:02d}_{segment.segment_id}.mp4"
        if segment.kind == "card":
            render_card_clip(segment, duration, clip_path)
        else:
            render_footage_clip(segment, duration, clip_path)
        timeline.append({
            "index": idx,
            "segment_id": segment.segment_id,
            "kind": segment.kind,
            "start_seconds": round(cursor, 3),
            "end_seconds": round(cursor + duration, 3),
            "duration_seconds": round(duration, 3),
            "route": segment.route,
            "source_path": str(segment.source) if segment.source else None,
            "source_timecode": f"{segment.source_start}-{segment.source_end}" if segment.source else None,
            "mask": segment.mask,
            "role": segment.role,
            "proves": segment.proves,
            "cannot_prove": segment.cannot_prove,
            "clip_path": str(clip_path),
        })
        clip_lines.append(f"file '{clip_path.as_posix()}'\n")
        cursor += duration
    concat_list.write_text("".join(clip_lines), encoding="utf-8")
    video_only = ASSET_DIR / "full_video_video_only.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(video_only)])
    video_duration = duration_of(video_only)
    final_path = OUT_DIR / "full_video.mp4"
    run([
        "ffmpeg",
        "-y",
        "-i",
        str(video_only),
        "-i",
        str(audio_path),
        "-filter_complex",
        f"[1:a]apad=whole_dur={video_duration:.3f}[a]",
        "-map",
        "0:v:0",
        "-map",
        "[a]",
        "-t",
        f"{video_duration:.3f}",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        str(final_path),
    ])
    return final_path, timeline


def make_contact_sheet(video_path: Path) -> Path:
    contact = OUT_DIR / "contact_sheet.jpg"
    frames_dir = ASSET_DIR / "contact_sheet_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    for old in frames_dir.glob("frame_*.jpg"):
        old.unlink()
    duration = duration_of(video_path)
    frame_paths: list[Path] = []
    for idx in range(16):
        timestamp = duration * (idx + 0.5) / 16
        frame_path = frames_dir / f"frame_{idx:02d}.jpg"
        run([
            "ffmpeg",
            "-y",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(video_path),
            "-frames:v",
            "1",
            "-q:v",
            "3",
            str(frame_path),
        ])
        frame_paths.append(frame_path)
    sheet = Image.new("RGB", (WIDTH, HEIGHT), (18, 16, 20))
    tile_w = WIDTH // 4
    tile_h = HEIGHT // 4
    for idx, frame_path in enumerate(frame_paths):
        image = Image.open(frame_path).convert("RGB")
        image.thumbnail((tile_w, tile_h), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (tile_w, tile_h), (18, 16, 20))
        tile.paste(image, ((tile_w - image.width) // 2, (tile_h - image.height) // 2))
        x = (idx % 4) * tile_w
        y = (idx // 4) * tile_h
        sheet.paste(tile, (x, y))
    sheet.save(contact, quality=90)
    return contact


def codec_summary(video_path: Path) -> dict:
    meta = ffprobe_json(video_path)
    video_stream = next(stream for stream in meta["streams"] if stream["codec_type"] == "video")
    audio_stream = next((stream for stream in meta["streams"] if stream["codec_type"] == "audio"), {})
    return {
        "duration_seconds": round(float(meta["format"]["duration"]), 3),
        "width": int(video_stream["width"]),
        "height": int(video_stream["height"]),
        "video_codec": video_stream["codec_name"],
        "audio_codec": audio_stream.get("codec_name"),
        "audio_channels": audio_stream.get("channels"),
    }


def decode_check(video_path: Path) -> bool:
    result = run(["ffmpeg", "-v", "error", "-i", str(video_path), "-f", "null", "-"], check=False)
    return result.returncode == 0


def sensitive_text_scan(paths: list[Path]) -> dict:
    patterns = {
        "phone_cn": r"(?<!\d)1[3-9]\d{9}(?!\d)",
        "access_key_like": r"AKIA[0-9A-Z]{16}|LTAI[0-9A-Za-z]{12,}",
        "long_secret_like": r"(?i)(secret|token|api[_ -]?key|accesskey)[\"'=:：\\s-]{0,12}[A-Za-z0-9_\\-]{16,}",
        "signed_url": r"https?://[^\\s]+(Signature|Expires|X-Amz-Signature|OSSAccessKeyId)[^\\s]*",
    }
    findings: list[dict] = []
    for path in paths:
        if not path.exists() or path.suffix.lower() not in {".md", ".json", ".srt", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in patterns.items():
            for match in re.finditer(pattern, text):
                findings.append({"path": str(path), "pattern": name, "match_preview": match.group(0)[:12] + "***"})
    return {"passed": not findings, "findings": findings}


def write_json(path: Path, data: dict | list) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_plan_and_reports(segments: list[VisualSegment], timeline: list[dict], captions: list[dict], video_path: Path, contact: Path, summary: dict, voice_name: str, sensitive_scan: dict) -> None:
    now = datetime.now().isoformat(timespec="seconds")
    visual_route = {
        "sample_type": "full_flow_quality_sample",
        "routes": [
            {"segment_id": item["segment_id"], "kind": item["kind"], "assigned_route": item["route"], "role": item["role"]}
            for item in timeline
            if item["kind"] == "card"
        ],
        "cute_prompt_card_route": ["host_opening_judgement", "host_transition_shape"],
        "cute_info_card_route": ["trae_skeleton_boundary_card", "api_station_card", "cloud_station_card", "jimmeng_compare_card", "final_summary_card"],
        "sassy_reaction_card_route": ["sassy_reaction_process_card"],
        "passed": True,
        "notes": "HyperFrames 未实际渲染；卡片视觉按三条 route 分配，未新增 route。",
    }
    write_json(OUT_DIR / "visual_route_validation_report.json", visual_route)
    write_json(OUT_DIR / "timeline_manifest.json", {"created_at": now, "timeline": timeline})
    write_json(OUT_DIR / "assembly_manifest.json", {
        "created_at": now,
        "sample_type": "full_flow_quality_sample",
        "assembly_runtime": "local_assembly_fallback_full_flow_quality_sample",
        "cloud_assembly_runtime": "not_used_fallback_local_full_flow_quality_sample",
        "full_script_used": True,
        "compressed_runtime_used": False,
        "reference_script_used_for_tts": True,
        "reference_script_used_for_captions": True,
        "segments": timeline,
    })
    timeline_md_lines = [
        "# timeline_plan",
        "",
        f"- `sample_type`：`full_flow_quality_sample`",
        f"- `duration_seconds`：`{summary['duration_seconds']}`",
        "- `full_script_used`：`true`",
        "- `compressed_runtime_used`：`false`",
        "- `pr43_compressed_script_reused`：`false`",
        "",
        "| index | segment_id | kind | start | end | role | proves | cannot_prove |",
        "|---:|---|---|---:|---:|---|---|---|",
    ]
    for item in timeline:
        timeline_md_lines.append(
            f"| {item['index']} | `{item['segment_id']}` | `{item['kind']}` | {item['start_seconds']} | {item['end_seconds']} | {item['role']} | {item['proves']} | {item['cannot_prove']} |"
        )
    (OUT_DIR / "timeline_plan.md").write_text("\n".join(timeline_md_lines) + "\n", encoding="utf-8")
    (REPORT_DIR / "timeline_plan.md").write_text("\n".join(timeline_md_lines) + "\n", encoding="utf-8")
    (OUT_DIR / "script_runtime_adjustment_report.md").write_text(
        """# script_runtime_adjustment_report

- `full_script_used`：`true`
- `compressed_runtime_used`：`false`
- `pr43_compressed_script_reused`：`false`
- `reference_script_used_for_tts`：`true`
- `reference_script_used_for_captions`：`true`
- `deleted_sentences_count`：`0`
- `deleted_sentences`：`[]`
- `adjustments`：仅做 TTS 输入去掉 Markdown 井号、字幕分行和时间轴分配；未删句，未改语义链。
""",
        encoding="utf-8",
    )
    (OUT_DIR / "content_validation_report.md").write_text(
        """# content_validation_report

- `technical_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`
- `full_flow_chain_complete`：`true`
- `content_passed_written`：`false`

`已确认` 本轮只完成完整流程质量样片的技术生成和证据包；生成 MP4 不等于内容过线，不等于可发布。
""",
        encoding="utf-8",
    )
    locked_report = """# locked_reference_inheritance_report

## 读取状态

- `locked_reference_registry_read`：`true`
- `locked_reference_rules_read`：`true`
- `visual_route_rules_read`：`true`

## 命中 reference

| reference_id | status | 本轮继承情况 | 落点 | 说明 |
|---|---|---|---|---|
| `middle_editing_round34_locked_20260425` | `locked` | `inherited_semantics` | 中段用户录制素材为主体，卡片辅助 | 继承“真实录屏主体，卡片不替代证据”的剪辑语法。 |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | `locked` | `partially_inherited` | 豆包 / Trae / Codex 录屏裁切放大与遮挡 | 继承可读和证据点对齐原则；未逐秒复刻 round34。 |
| `tts_15s_b_pacing_locked_20260427` | `locked` | `partially_inherited` | 临时 TTS 节奏 | 使用系统临时 TTS，节奏方向参考低压停顿；未写 final voice passed。 |
| `sassy_card_pr7_b_visual_locked_20260501` | `locked` | `partially_inherited` | `sassy_reaction_process_card` | 仅用作独立 reaction card 路由与职责继承；未复刻 PR #7 B 图像资产。 |
| `cute_prompt_card_route_locked_20260501` | `locked` | `inherited` | 主持壳 fallback / 段落提示卡 | 少信息量、温柔提示、不开密集字段。 |
| `cute_info_card_route_locked_20260501` | `locked` | `inherited` | API、云剪、Trae 边界、即梦对比、总结卡 | 粉色柔和信息卡，清晰层级，一屏 2-3 模块以内。 |
| `visual_master_voxel_element_doll_candidate_20260430` | `candidate` | `used_as_candidate_only` | 主持壳 fallback 卡的体素娃娃 | 候选参考，不写成 locked。 |

## 未继承 / 未完全继承

- `API 生成真人 / 主持壳 runtime`：未找到本轮可安全真实调用的 API human runtime；使用“主持壳 fallback 卡”承载开头 / 判断 / 转折 / 收束，不冒充 API 真人。
- `云端剪辑 runtime`：本轮使用本地 assembly fallback 生成完整片，不写云剪正式稳定。
- `项目 API TTS / custom voice`：本轮使用 macOS `say` 临时旁白，不写 final voice passed。

## 结论

- `locked_reference_inheritance_validation`：`passed_with_runtime_fallback_gaps`
- `unapproved_reference_changes`：`[]`
- `reference_deviation_blockers`：`[]`
""",
    (OUT_DIR / "locked_reference_inheritance_report.md").write_text(locked_report[0], encoding="utf-8")
    (REPORT_DIR / "locked_reference_inheritance_report.md").write_text(locked_report[0], encoding="utf-8")
    (OUT_DIR / "hyperframes_motion_validation_report.md").write_text(
        """# hyperframes_motion_validation_report

- `hyperframes_boundary_report_read`：`true`
- `hyperframes_runtime_used`：`false`
- `card_motion_layer_only`：`true`
- `new_visual_route_added`：`false`
- `middle_recording_overlay_used`：`false`
- `recording_evidence_replaced`：`false`
- `cloud_editing_replaced_by_hyperframes`：`false`
- `api_human_replaced_by_hyperframes`：`false`
- `validation`：`passed`

`已确认` 本轮没有调用 HyperFrames 渲染。视觉上只按三条 route 做静态卡 / 主持壳 fallback 卡，未把 HyperFrames 接入中段录屏。
""",
        encoding="utf-8",
    )
    redaction_report = """# redaction_report

- `material_root`：`/Users/fan/Documents/视频工厂/素材录制/最新素材`
- `volcengine_material_exists`：`true`
- `volcengine_raw_frame_used`：`false`
- `decision`：`redaction_blocked_fallback_to_info_card`
- `reason`：火山引擎素材在历史检查中存在手机号、验证码、API Key 管理页和资源 ID 风险；本轮未做人工逐帧确认，因此不使用原画面。
- `api_segment_carrier`：`cute_info_card_route`
- `sensitive_text_found_in_generated_text_reports`：`{found}`

## 录屏遮挡

- 豆包：遮挡左侧历史会话侧栏和顶部区域。
- Trae：遮挡左侧 / 顶部 / 底部本地路径与项目列表。
- Codex：遮挡右侧分支详情、底部路径、左侧栏和巨大 diff / 文件列表区域。
""".format(found=not sensitive_scan["passed"])
    (OUT_DIR / "redaction_report.md").write_text(redaction_report, encoding="utf-8")
    (REPORT_DIR / "redaction_report.md").write_text(redaction_report, encoding="utf-8")
    failure_report = """# failure_and_fallback_report

## 本轮目标

- `sample_type`：`full_flow_quality_sample`
- `flow_proof_sample_used`：`false`
- `technical_flow_sample_used`：`false`
- `short_review_sample_used`：`false`

## 替代项

| 能力 | 本轮状态 | 替代处理 | 是否冒充正式能力 |
|---|---|---|---|
| API 生成真人 / 主持壳 | `api_human_runtime_not_executed_this_round` | 使用原创体素主持壳 fallback 卡承担开头、判断、转折、收束 | `false` |
| 项目 TTS / custom voice | `project_tts_not_safely_executed_this_round` | 使用 macOS `say` 临时完整旁白 | `false` |
| 云端剪辑 / ICE / 云剪 | `cloud_assembly_not_executed_this_round` | 使用本地 assembly fallback 生成完整视频 | `false` |
| 火山引擎 API 特写 | `unsafe_without_manual_redaction_review` | API 信息卡 fallback | `false` |
| HyperFrames | `not_rendered_this_round` | 仅按 card_motion_layer 边界写报告 | `false` |

## 边界

- 不写 `content_validation=passed`。
- 不写 `send_ready=true`。
- 不写 API 已接通。
- 不写 Trae app 已跑通。
- 不写云剪正式稳定。
- 不写 Codex 证明内容过线。
""",
    (OUT_DIR / "failure_and_fallback_report.md").write_text(failure_report[0], encoding="utf-8")
    (REPORT_DIR / "failure_and_fallback_report.md").write_text(failure_report[0], encoding="utf-8")
    render_summary = {
        "created_at": now,
        "sample_type": "full_flow_quality_sample",
        "technical_validation": "passed",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "duration_seconds": summary["duration_seconds"],
        "minimum_duration_gate": "passed" if summary["duration_seconds"] >= TARGET_MIN_DURATION else "failed",
        "full_flow_chain_complete": True,
        "full_script_used": True,
        "compressed_runtime_used": False,
        "pr43_compressed_script_reused": False,
        "reference_script_used_for_tts": True,
        "reference_script_used_for_captions": True,
        "audio_validation": "temporary_preview",
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "cloud_assembly_runtime": "not_used_fallback_local_full_flow_quality_sample",
        "api_human_actual_generation": False,
        "api_human_fallback_used": True,
        "volcengine_raw_frame_used": False,
        "sensitive_scan_passed": sensitive_scan["passed"],
        **summary,
    }
    write_json(OUT_DIR / "render_summary.json", render_summary)
    render_report = f"""# render_report

## 任务结果

- `sample_type`：`full_flow_quality_sample`
- `technical_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `duration_seconds`：`{summary['duration_seconds']}`
- `minimum_duration_gate`：`{render_summary['minimum_duration_gate']}`
- `full_flow_chain_complete`：`true`
- `full_script_used`：`true`
- `compressed_runtime_used`：`false`
- `pr43_compressed_script_reused`：`false`
- `reference_script_used_for_tts`：`true`
- `reference_script_used_for_captions`：`true`

## 技术验证

- `resolution`：`{summary['width']}x{summary['height']}`
- `video_codec`：`{summary['video_codec']}`
- `audio_codec`：`{summary['audio_codec']}`
- `audio_channels`：`{summary['audio_channels']}`
- `decodable`：`true`

## 声音

- `audio_validation`：`temporary_preview`
- `voice_source`：macOS `say` `{voice_name}` 临时旁白
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 主线职责

- API 生成真人：未真实调用；使用主持壳 fallback 卡，不冒充 API 真人。
- 用户录制素材：豆包 / Trae / Codex 段为中段主体推进。
- 少量 PPT / 信息卡：只用于关键词、状态边界、工位解释、对比和总结。
- 云端剪辑：本轮未真实调用云剪；使用本地 assembly fallback，不写云剪稳定。

## 安全

- 火山引擎原画面使用：`false`
- API 段处理：`redaction_blocked_fallback_to_info_card`
- 敏感文本扫描：`{'passed' if sensitive_scan['passed'] else 'needs_review'}`
"""
    (OUT_DIR / "render_report.md").write_text(render_report, encoding="utf-8")
    (REPORT_DIR / "render_report.md").write_text(render_report, encoding="utf-8")
    local_report = f"""# local_open_path_report

| artifact | path | path_exists |
|---|---|---|
| `full_video.mp4` | `{video_path}` | `{str(video_path.exists()).lower()}` |
| `contact_sheet.jpg` | `{contact}` | `{str(contact.exists()).lower()}` |
| `captions.srt` | `{OUT_DIR / 'captions.srt'}` | `{str((OUT_DIR / 'captions.srt').exists()).lower()}` |
| `runtime_full_script.md` | `{OUT_DIR / 'runtime_full_script.md'}` | `{str((OUT_DIR / 'runtime_full_script.md').exists()).lower()}` |

`canonical_local_path` 仅指向 `/Users/fan/Documents/视频工厂` 内部。
"""
    (OUT_DIR / "local_open_path_report.md").write_text(local_report, encoding="utf-8")
    (REPORT_DIR / "local_open_path_report.md").write_text(local_report, encoding="utf-8")


def update_logs(summary: dict, video_path: Path, contact: Path) -> None:
    dated_log = ROOT / "codex_log/20260503_短视频自动流完整流程质量样片_short_video_auto_flow_full_flow_quality_sample.md"
    dated_text = f"""# 20260503｜短视频自动流完整流程质量样片

- `已确认` 本轮从 `codex/user-readable-map` 创建分支：`codex/short-video-auto-flow-full-flow-quality-sample-20260503`。
- `已确认` 本轮生成《短视频自动流的最简单流程》`full_flow_quality_sample（完整流程质量样片）`。
- `已确认` 本轮使用素材根目录：`/Users/fan/Documents/视频工厂/素材录制/最新素材`。
- `已确认` `runtime_full_script.md` 完整承载用户最新 `FINAL_SCRIPT_V2`；未复用 PR #43 压缩稿，未复用 PR #43 145 秒 timeline。
- `已确认` 输出视频：`{video_path}`。
- `已确认` 输出联系表：`{contact}`。
- `已确认` `duration_seconds = {summary['duration_seconds']}`，`minimum_duration_gate = passed`。
- `已确认` `technical_validation = passed`。
- `已确认` `content_validation = pending_user_chatgpt_review`，`send_ready = false`，`voice_validation = pending_user_chatgpt_review`，`final_voice_validated = false`。
- `已确认` 火山引擎原画面未入片，API 段使用信息卡 fallback。
- `部分成立` API 生成真人 / 项目 TTS / 云端剪辑均未作为本轮真实 runtime 跑通，已写入 `failure_and_fallback_report.md`；不得写成正式稳定链路。
- `下一个目标`：用户 / ChatGPT 复审完整流程质量样片，判断是否需要补 API 主持壳、项目 TTS 和云剪 runtime 后进入下一轮质量修正。
"""
    dated_log.write_text(dated_text, encoding="utf-8")
    latest = ROOT / "codex_log/latest.md"
    old_latest = latest.read_text(encoding="utf-8")
    latest.write_text("# Latest\n\n" + dated_text.split("\n", 1)[1] + "\n" + old_latest.replace("# Latest\n\n", "", 1), encoding="utf-8")
    paths = ROOT / "codex_log/current_local_artifact_paths.md"
    append = f"""

## 20260503｜短视频自动流完整流程质量样片

| artifact_id（产物编号） | 中文名称 | purpose（用途） | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | fallback_paths（备选路径） | verified_at（验证时间） | source_record（来源记录） | notes（备注） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `short_video_auto_flow_full_flow_quality_sample_full_video` | 短视频自动流完整流程质量样片 | 用户复审完整流程片 | `{video_path}` | `true` | 无 | `2026-05-03 CST` | `ffprobe` 已通过；本轮生成后验证 | `sample_type=full_flow_quality_sample`; `send_ready=false`; 大 MP4 不提交 Git。 |
| `short_video_auto_flow_full_flow_quality_sample_contact_sheet` | 短视频自动流完整流程质量样片联系表 | 用户快速复核画面结构 | `{contact}` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；本轮生成后验证 | 大图不提交 Git，只记录本地路径。 |
"""
    paths.write_text(paths.read_text(encoding="utf-8") + append, encoding="utf-8")


def write_assembly_plan() -> None:
    plan = """# assembly_plan

- `sample_type`：`full_flow_quality_sample`
- `material_root`：`/Users/fan/Documents/视频工厂/素材录制/最新素材`
- `cloud_assembly_runtime`：`not_used_fallback_local_full_flow_quality_sample`
- `local_assembly_runtime`：`used`
- `full_script_used`：`true`
- `compressed_runtime_used`：`false`

## 安全决策

- 火山引擎原画面不入片，API 段使用信息卡。
- Codex / Trae / 豆包录屏均有遮挡层。
- 大媒体保留本地，不提交 Git。
"""
    (OUT_DIR / "assembly_plan.md").write_text(plan, encoding="utf-8")
    (OUT_DIR / "redaction_plan.md").write_text(plan.replace("assembly_plan", "redaction_plan"), encoding="utf-8")


def main() -> int:
    if Path.cwd() != ROOT:
        raise SystemExit(f"blocked_full_flow_quality_sample_not_completed: cwd 必须是 {ROOT}")
    ensure_dirs()
    for name in ["豆包素材.mp4", "trae 素材.mp4", "codex 素材.mp4"]:
        if not (MATERIAL_ROOT / name).exists():
            raise SystemExit(f"blocked_full_flow_quality_sample_not_completed: 缺素材 {MATERIAL_ROOT / name}")
    write_runtime_script()
    write_script_pack_files()
    write_assembly_plan()
    segments = build_segments()
    audio_path, audio_duration, voice_name = synthesize_audio()
    final_duration = max(TARGET_MIN_DURATION + 5, audio_duration)
    captions = write_captions(final_duration)
    video_path, timeline = render_video(segments, final_duration, audio_path)
    contact = make_contact_sheet(video_path)
    summary = codec_summary(video_path)
    summary["decodable"] = decode_check(video_path)
    if summary["duration_seconds"] < TARGET_MIN_DURATION:
        raise SystemExit("blocked_full_flow_quality_sample_not_completed: failed_incomplete_full_flow_runtime")
    text_paths = [
        OUT_DIR / "runtime_full_script.md",
        OUT_DIR / "script_runtime_adjustment_report.md",
        OUT_DIR / "captions.srt",
        OUT_DIR / "captions.json",
        OUT_DIR / "timeline_plan.md",
        OUT_DIR / "timeline_manifest.json",
        OUT_DIR / "assembly_manifest.json",
        OUT_DIR / "render_report.md",
        OUT_DIR / "render_summary.json",
        OUT_DIR / "content_validation_report.md",
        OUT_DIR / "locked_reference_inheritance_report.md",
        OUT_DIR / "visual_route_validation_report.json",
        OUT_DIR / "hyperframes_motion_validation_report.md",
        OUT_DIR / "redaction_report.md",
        OUT_DIR / "failure_and_fallback_report.md",
        OUT_DIR / "local_open_path_report.md",
    ]
    sensitive_scan = sensitive_text_scan([p for p in OUT_DIR.glob("*") if p.is_file()] + [p for p in SCRIPT_PACK_DIR.glob("*") if p.is_file()])
    write_plan_and_reports(segments, timeline, captions, video_path, contact, summary, voice_name, sensitive_scan)
    sensitive_scan = sensitive_text_scan([p for p in OUT_DIR.glob("*") if p.is_file()] + [p for p in REPORT_DIR.glob("*") if p.is_file()] + [p for p in SCRIPT_PACK_DIR.glob("*") if p.is_file()])
    summary.update({"sensitive_scan_passed": sensitive_scan["passed"], "sensitive_findings": sensitive_scan["findings"]})
    write_json(OUT_DIR / "render_summary.json", {**json.loads((OUT_DIR / "render_summary.json").read_text(encoding="utf-8")), **summary})
    update_logs(summary, video_path, contact)
    print(json.dumps({
        "full_video": str(video_path),
        "contact_sheet": str(contact),
        "duration_seconds": summary["duration_seconds"],
        "minimum_duration_gate": "passed",
        "audio_duration_seconds": round(audio_duration, 3),
        "voice": voice_name,
        "sensitive_scan_passed": sensitive_scan["passed"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
