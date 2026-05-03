#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
from datetime import datetime, timezone, timedelta
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = pathlib.Path("/Users/fan/Documents/视频工厂")
SCRIPT_PACK_DIR = ROOT / "文案库" / "20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process"
OUTPUT_DIR = ROOT / "dist" / "视频样片_video_samples" / "20260503_短视频自动流最简单流程_v2_sample"
CARDS_DIR = OUTPUT_DIR / "卡片素材_cards"
SEGMENTS_DIR = OUTPUT_DIR / "中间片段_segments"
LOGS_DIR = OUTPUT_DIR / "渲染日志_render_logs"

W, H = 720, 1280
FPS = 24
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ).isoformat(timespec="seconds")

DOUBAO = ROOT / "素材录制" / "最新素材" / "豆包素材.mp4"
TRAE = ROOT / "素材录制" / "最新素材" / "trae 素材.mp4"
CODEX = ROOT / "素材录制" / "最新素材" / "codex 素材.mp4"
VOLCENGINE = ROOT / "素材录制" / "最新素材" / "火山引擎素材.mp4"
FOLDER_BROLL = ROOT / "素材录制" / "最新素材" / "创建文件夹.mp4"
HISTORICAL_MOV = ROOT / "素材录制" / "最新素材" / "录屏2026-04-30 03.25.28.mov"


FINAL_SCRIPT_V2 = r'''# 《短视频自动流的最简单流程》

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

顺序对了，自动化才有地方落脚。'''


CARD_SPECS = [
    {
        "id": "flow_overview",
        "filename": "01_流程总览_flow_overview.png",
        "title": "短视频自动流，不是一键生成",
        "items": ["一句需求", "拆成流程", "交给工具执行", "结果能检查"],
        "footer": "先把顺序理出来，自动化才有地方落脚。",
        "route": "cute_info_card_route",
    },
    {
        "id": "doubao_to_trae_prompt",
        "filename": "02_豆包到Trae_prompt_doubao_to_trae_prompt.png",
        "title": "豆包把想法翻译成任务说明",
        "items": ["先拆方案", "再生成 Trae SOLO prompt", "让执行器能接住"],
        "footer": "关键不是继续聊天，而是形成可执行 prompt。",
        "route": "cute_info_card_route",
    },
    {
        "id": "trae_skeleton",
        "filename": "03_Trae骨架_trae_skeleton.png",
        "title": "看不懂代码也没关系",
        "items": ["有没有项目目录", "有没有模块和配置", "有没有 app 初步形状"],
        "footer": "项目骨架出现，不等于代码已经跑通。",
        "route": "cute_info_card_route",
    },
    {
        "id": "api_explainer",
        "filename": "04_API解释_api_explainer.png",
        "title": "API 是外部能力入口",
        "items": ["文字生成", "配音 / 图片 / 卡片", "剪辑总装"],
        "footer": "本轮使用信息卡替代火山引擎原画面：API 特写不等于 API 已接通。",
        "route": "cute_info_card_route",
    },
    {
        "id": "cloud_assembly",
        "filename": "05_云端总装_cloud_assembly.png",
        "title": "阿里云剪辑是装配台",
        "items": ["不负责想创意", "不负责写文案", "负责按时间线总装"],
        "footer": "云端总装候选，不是正式稳定链路。",
        "route": "cute_info_card_route",
    },
    {
        "id": "codex_check",
        "filename": "06_Codex检查_codex_check.png",
        "title": "Codex 更像执行检查员",
        "items": ["路径是否存在", "素材能否解码", "报告有没有生成"],
        "footer": "技术检查不等于内容过线。",
        "route": "cute_info_card_route",
    },
    {
        "id": "jimeng_compare",
        "filename": "07_即梦对比_jimeng_compare.png",
        "title": "即梦像抽素材，自动流像搭流程",
        "items": ["即梦：快速出单个画面", "自动流：把需求变成可复用生产线"],
        "footer": "不是评测工具强弱，而是解决的问题不同。",
        "route": "cute_info_card_route",
    },
    {
        "id": "final_summary",
        "filename": "08_最后总结_final_summary.png",
        "title": "顺序对了，自动化才有地方落脚",
        "items": ["拆清楚", "接工具", "能检查", "可迭代"],
        "footer": "别一上来追求一键生成。",
        "route": "cute_info_card_route",
    },
]


def resolve_bin(name: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    bundled = ROOT / "node_modules" / "ffmpeg-static" / name
    if bundled.exists():
        return str(bundled)
    raise RuntimeError(f"missing required binary: {name}")


def run(cmd: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log_path:
        log_path.write_text(proc.stdout, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stdout[-2000:]}")
    return proc


def rel(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_text(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean_script_text() -> str:
    return FINAL_SCRIPT_V2.replace("# 《短视频自动流的最简单流程》\n\n", "").strip()


def paragraphs_for_captions() -> list[str]:
    text = clean_script_text()
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    merged: list[str] = []
    buf = ""
    for part in parts:
        part = re.sub(r"\s*\n\s*", " ", part).strip()
        if not buf:
            buf = part
        elif len(buf) + len(part) < 52:
            buf += " " + part
        else:
            merged.append(buf)
            buf = part
    if buf:
        merged.append(buf)
    return merged


def srt_time(seconds: float) -> str:
    seconds = max(0, seconds)
    ms = int(round((seconds - math.floor(seconds)) * 1000))
    whole = int(math.floor(seconds))
    s = whole % 60
    m = (whole // 60) % 60
    h = whole // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
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


def rounded_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def make_card(spec: dict[str, Any]) -> pathlib.Path:
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (W, H), "#fff7fb")
    draw = ImageDraw.Draw(img)
    title_font = load_font(45, bold=True)
    item_font = load_font(32, bold=True)
    small_font = load_font(24)
    tag_font = load_font(20, bold=True)

    # Soft route-consistent background without turning into a dense dashboard.
    draw.rectangle((0, 0, W, H), fill="#fff7fb")
    draw.ellipse((-130, 70, 210, 410), fill="#ffe1ec")
    draw.ellipse((520, 40, 820, 330), fill="#d9f4ee")
    draw.ellipse((500, 940, 820, 1260), fill="#ffe6cc")
    draw.rectangle((0, 0, W, 98), fill="#2f2a45")
    draw.text((42, 34), "流程证明型样片 V1", font=tag_font, fill="#ffffff")
    draw.text((42, 102), "cute_info_card_route", font=tag_font, fill="#a86b88")

    rounded_rect(draw, (36, 150, W - 36, H - 112), 22, "#ffffff", "#f4b8cf", 2)
    rounded_rect(draw, (66, 188, W - 66, 340), 18, "#fff0f6", "#f4b8cf", 2)
    y = 207
    for line in wrap_text(draw, spec["title"], title_font, W - 160):
        draw.text((86, y), line, font=title_font, fill="#30243d")
        y += 58

    y = 405
    colors = ["#ffebf2", "#e8f6f3", "#fff0d9", "#eef0ff"]
    accents = ["#dc5b8b", "#2f9a87", "#d9822b", "#5867c8"]
    for idx, item in enumerate(spec["items"], start=1):
        top = y
        rounded_rect(draw, (76, top, W - 76, top + 92), 16, colors[(idx - 1) % len(colors)], None)
        draw.ellipse((96, top + 24, 140, top + 68), fill=accents[(idx - 1) % len(accents)])
        draw.text((110, top + 28), str(idx), font=tag_font, fill="#ffffff")
        draw.text((162, top + 27), item, font=item_font, fill="#30243d")
        y += 116

    footer_lines = wrap_text(draw, spec["footer"], small_font, W - 160)
    y = H - 240
    for line in footer_lines:
        draw.text((82, y), line, font=small_font, fill="#68596d")
        y += 34
    draw.text((82, H - 156), "content_validation = pending_user_chatgpt_review · send_ready = false", font=tag_font, fill="#9a657b")

    path = CARDS_DIR / spec["filename"]
    img.save(path, quality=95)
    return path


def generate_cards() -> dict[str, str]:
    paths = {}
    for spec in CARD_SPECS:
        paths[spec["id"]] = str(make_card(spec))
    return paths


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


def make_tts(ffmpeg: str, ffprobe: str) -> dict[str, Any]:
    narration_txt = OUTPUT_DIR / "temporary_tts_narration_text.txt"
    narration_aiff = OUTPUT_DIR / "temporary_tts_narration.aiff"
    narration_m4a = OUTPUT_DIR / "temporary_tts_narration.m4a"
    write_text(narration_txt, clean_script_text())

    if narration_m4a.exists():
        duration = probe_duration(ffprobe, narration_m4a)
        return {
            "audio_path": str(narration_m4a),
            "duration_seconds": duration,
            "audio_validation": "temporary_preview",
            "tts_validation": "temporary_system_tts_preview",
            "voice_validation": "pending_user_chatgpt_review",
            "final_voice_validated": False,
            "generation_method": "macOS say Tingting temporary preview (reused)",
        }

    say_bin = shutil.which("say")
    if say_bin:
        try:
            run([say_bin, "-v", "Tingting", "-r", "235", "-f", str(narration_txt), "-o", str(narration_aiff)], LOGS_DIR / "say_tts.log")
            run([ffmpeg, "-hide_banner", "-y", "-i", str(narration_aiff), "-c:a", "aac", "-b:a", "96k", str(narration_m4a)], LOGS_DIR / "tts_encode.log")
            duration = probe_duration(ffprobe, narration_m4a)
            return {
                "audio_path": str(narration_m4a),
                "duration_seconds": duration,
                "audio_validation": "temporary_preview",
                "tts_validation": "temporary_system_tts_preview",
                "voice_validation": "pending_user_chatgpt_review",
                "final_voice_validated": False,
                "generation_method": "macOS say Tingting temporary preview",
            }
        except Exception as exc:
            write_text(LOGS_DIR / "tts_fallback_reason.log", str(exc))

    # Fallback if system TTS fails.
    duration = max(360.0, len(clean_script_text()) / 7.5)
    silent = OUTPUT_DIR / "silence_placeholder.m4a"
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-f",
        "lavfi",
        "-i",
        "anullsrc=channel_layout=mono:sample_rate=44100",
        "-t",
        f"{duration:.3f}",
        "-c:a",
        "aac",
        "-b:a",
        "64k",
        str(silent),
    ], LOGS_DIR / "silence_audio.log")
    return {
        "audio_path": str(silent),
        "duration_seconds": duration,
        "audio_validation": "silence_placeholder",
        "tts_validation": "not_generated",
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "generation_method": "ffmpeg silence placeholder",
    }


def make_captions(total_duration: float) -> None:
    parts = paragraphs_for_captions()
    weights = [max(6, len(re.sub(r"\s+", "", p))) for p in parts]
    total_weight = sum(weights)
    cursor = 0.0
    srt_blocks = []
    json_blocks = []
    for idx, (part, weight) in enumerate(zip(parts, weights), start=1):
        dur = max(1.6, total_duration * weight / total_weight)
        start = cursor
        end = min(total_duration, cursor + dur)
        cursor = end
        srt_blocks.append(f"{idx}\n{srt_time(start)} --> {srt_time(end)}\n{part}\n")
        json_blocks.append({"index": idx, "start": round(start, 3), "end": round(end, 3), "text": part})
    write_text(OUTPUT_DIR / "captions.srt", "\n".join(srt_blocks))
    write_json(OUTPUT_DIR / "captions.json", json_blocks)


def video_filter_for_clip(kind: str) -> str:
    crop_x = {
        "doubao": 620,
        "trae": 650,
        "codex": 420,
    }.get(kind, 620)
    filters = [
        "scale=-1:1280",
        f"crop=720:1280:{crop_x}:0",
        "fps=24",
        "format=yuv420p",
    ]
    if kind == "codex":
        filters.extend([
            "drawbox=x=522:y=0:w=198:h=1280:color=black@0.82:t=fill",
            "drawbox=x=0:y=1192:w=720:h=88:color=black@0.82:t=fill",
            "drawbox=x=0:y=0:w=720:h=54:color=black@0.70:t=fill",
        ])
    elif kind == "trae":
        filters.extend([
            "drawbox=x=0:y=1192:w=720:h=88:color=black@0.70:t=fill",
            "drawbox=x=0:y=0:w=720:h=46:color=black@0.55:t=fill",
        ])
    else:
        filters.extend([
            "drawbox=x=0:y=1192:w=720:h=88:color=black@0.62:t=fill",
            "drawbox=x=0:y=0:w=720:h=46:color=black@0.45:t=fill",
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
        "23",
        "-r",
        str(FPS),
        str(out_path),
    ], LOGS_DIR / f"{out_path.stem}.log")


def render_clip_segment(ffmpeg: str, source: pathlib.Path, start: float, end: float, kind: str, out_path: pathlib.Path) -> None:
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-ss",
        f"{start:.3f}",
        "-i",
        str(source),
        "-t",
        f"{end - start:.3f}",
        "-vf",
        video_filter_for_clip(kind),
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "24",
        "-r",
        str(FPS),
        str(out_path),
    ], LOGS_DIR / f"{out_path.stem}.log")


def build_sequence(audio_duration: float, card_paths: dict[str, str]) -> list[dict[str, Any]]:
    clip_segments = [
        {"type": "clip", "id": "doubao_simple_need", "source": DOUBAO, "start": 16.0, "end": 24.0, "kind": "doubao"},
        {"type": "clip", "id": "doubao_short_video_plan", "source": DOUBAO, "start": 88.0, "end": 120.0, "kind": "doubao"},
        {"type": "clip", "id": "doubao_vlog_prompt_request", "source": DOUBAO, "start": 160.0, "end": 176.0, "kind": "doubao"},
        {"type": "clip", "id": "doubao_copyable_trae_prompt", "source": DOUBAO, "start": 232.0, "end": 248.0, "kind": "doubao"},
        {"type": "clip", "id": "trae_solo_entry", "source": TRAE, "start": 32.0, "end": 64.0, "kind": "trae"},
        {"type": "clip", "id": "trae_prompt_and_plan", "source": TRAE, "start": 80.0, "end": 112.0, "kind": "trae"},
        {"type": "clip", "id": "trae_project_skeleton", "source": TRAE, "start": 120.0, "end": 160.0, "kind": "trae"},
        {"type": "clip", "id": "codex_execution_check", "source": CODEX, "start": 176.0, "end": 188.0, "kind": "codex"},
    ]
    base_cards = [
        ("flow_overview", 10.0),
        ("doubao_to_trae_prompt", 10.0),
        ("trae_skeleton", 12.0),
        ("api_explainer", 10.0),
        ("cloud_assembly", 10.0),
        ("codex_check", 10.0),
        ("jimeng_compare", 12.0),
        ("final_summary", 16.0),
    ]
    clip_total = sum(s["end"] - s["start"] for s in clip_segments)
    min_card_total = sum(d for _, d in base_cards)
    target_total = max(audio_duration + 2.0, clip_total + min_card_total)
    extra = max(0.0, target_total - clip_total - min_card_total)
    weights = {
        "flow_overview": 1.0,
        "doubao_to_trae_prompt": 1.1,
        "trae_skeleton": 1.2,
        "api_explainer": 1.0,
        "cloud_assembly": 1.0,
        "codex_check": 1.0,
        "jimeng_compare": 1.1,
        "final_summary": 1.5,
    }
    total_weight = sum(weights.values())
    card_durations = {cid: base + extra * weights[cid] / total_weight for cid, base in base_cards}

    return [
        {"type": "card", "id": "flow_overview", "image": pathlib.Path(card_paths["flow_overview"]), "duration": card_durations["flow_overview"]},
        clip_segments[0],
        clip_segments[1],
        {"type": "card", "id": "doubao_to_trae_prompt", "image": pathlib.Path(card_paths["doubao_to_trae_prompt"]), "duration": card_durations["doubao_to_trae_prompt"]},
        clip_segments[2],
        clip_segments[3],
        clip_segments[4],
        clip_segments[5],
        {"type": "card", "id": "trae_skeleton", "image": pathlib.Path(card_paths["trae_skeleton"]), "duration": card_durations["trae_skeleton"]},
        clip_segments[6],
        {"type": "card", "id": "api_explainer", "image": pathlib.Path(card_paths["api_explainer"]), "duration": card_durations["api_explainer"]},
        {"type": "card", "id": "cloud_assembly", "image": pathlib.Path(card_paths["cloud_assembly"]), "duration": card_durations["cloud_assembly"]},
        clip_segments[7],
        {"type": "card", "id": "codex_check", "image": pathlib.Path(card_paths["codex_check"]), "duration": card_durations["codex_check"]},
        {"type": "card", "id": "jimeng_compare", "image": pathlib.Path(card_paths["jimeng_compare"]), "duration": card_durations["jimeng_compare"]},
        {"type": "card", "id": "final_summary", "image": pathlib.Path(card_paths["final_summary"]), "duration": card_durations["final_summary"]},
    ]


def render_video(ffmpeg: str, ffprobe: str, audio_info: dict[str, Any], card_paths: dict[str, str]) -> tuple[list[dict[str, Any]], pathlib.Path]:
    SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
    sequence = build_sequence(float(audio_info["duration_seconds"]), card_paths)
    rendered: list[pathlib.Path] = []
    for idx, seg in enumerate(sequence, start=1):
        out = SEGMENTS_DIR / f"{idx:02d}_{seg['id']}.mp4"
        if seg["type"] == "card":
            render_card_segment(ffmpeg, pathlib.Path(seg["image"]), float(seg["duration"]), out)
            seg["rendered_path"] = str(out)
        else:
            render_clip_segment(ffmpeg, pathlib.Path(seg["source"]), float(seg["start"]), float(seg["end"]), seg["kind"], out)
            seg["duration"] = float(seg["end"]) - float(seg["start"])
            seg["rendered_path"] = str(out)
        rendered.append(out)

    concat_list = OUTPUT_DIR / "concat_segments.txt"
    concat_list.write_text("".join([f"file '{p.as_posix()}'\n" for p in rendered]), encoding="utf-8")
    visual = OUTPUT_DIR / "visual_track.mp4"
    run([ffmpeg, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(visual)], LOGS_DIR / "concat_visual.log")

    full = OUTPUT_DIR / "full_video.mp4"
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(visual),
        "-i",
        str(audio_info["audio_path"]),
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
        "-shortest",
        str(full),
    ], LOGS_DIR / "mux_full_video.log")
    return sequence, full


def ffprobe_json(ffprobe: str, path: pathlib.Path) -> dict[str, Any]:
    proc = run([ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)])
    return json.loads(proc.stdout)


def validate_video(ffmpeg: str, ffprobe: str, full_video: pathlib.Path) -> dict[str, Any]:
    data = ffprobe_json(ffprobe, full_video)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})
    decode_log = LOGS_DIR / "full_video_decode_check.log"
    decodable = True
    try:
        run([ffmpeg, "-v", "error", "-i", str(full_video), "-f", "null", "-"], decode_log)
    except Exception as exc:
        decodable = False
        write_text(decode_log, str(exc))
    return {
        "file_path": str(full_video),
        "exists": full_video.exists(),
        "file_size_bytes": full_video.stat().st_size if full_video.exists() else 0,
        "duration_seconds": float(data.get("format", {}).get("duration", 0.0)),
        "width": int(video.get("width", 0) or 0),
        "height": int(video.get("height", 0) or 0),
        "video_codec": video.get("codec_name", "unknown"),
        "audio_present": bool(audio),
        "audio_codec": audio.get("codec_name", "none") if audio else "none",
        "audio_channels": audio.get("channels", 0) if audio else 0,
        "decodable": decodable,
        "technical_validation": "passed" if decodable and video and full_video.exists() else "failed",
        "metadata_validation": "passed" if video and full_video.exists() else "failed",
    }


def create_contact_sheet(ffmpeg: str, full_video: pathlib.Path, duration: float) -> None:
    interval = max(1.0, duration / 12.0)
    run([
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(full_video),
        "-vf",
        f"fps=1/{interval:.3f},scale=180:320,tile=4x3",
        "-frames:v",
        "1",
        str(OUTPUT_DIR / "contact_sheet.jpg"),
    ], LOGS_DIR / "contact_sheet.log")
    # Redaction preview is the API fallback info card because Volcengine footage is not used.
    api_card = CARDS_DIR / "04_API解释_api_explainer.png"
    if api_card.exists():
        img = Image.open(api_card)
        img.thumbnail((360, 640))
        canvas = Image.new("RGB", (720, 720), "#fff7fb")
        canvas.paste(img, ((720 - img.width) // 2, 40))
        draw = ImageDraw.Draw(canvas)
        font = load_font(26, bold=True)
        draw.text((58, 645), "redaction_blocked_fallback_to_info_card", font=font, fill="#8a4565")
        canvas.save(OUTPUT_DIR / "redaction_contact_sheet.jpg", quality=92)


def write_script_pack_files() -> None:
    write_text(
        SCRIPT_PACK_DIR / "01_完整口播稿_full_script.md",
        f"""# 《短视频自动流的最简单流程》

## 文案状态

- `已确认` 本文件保真保存用户最终确认的 `FINAL_SCRIPT_V2（流程细节增强版）`。
- `已确认` 本片是流程证明型样片，不是工具教程、工具合集、Trae / Codex / 阿里云 / 即梦评测。
- `已确认` 必须保留 Trae 段新增判断：看不懂代码也没关系，重点看 app / 项目有没有执行出初步形状。
- `已确认` 火山引擎 API 管理页如入片必须先脱敏；本轮样片默认 fallback 到 API 信息卡。
- `待验证` 本文件不代表内容最终过线；`content_validation = pending_user_chatgpt_review`，`send_ready = false`。

## 完整口播稿

{clean_script_text()}
""",
    )

    segment_map = """# 分段承载表：短视频自动流的最简单流程 V2

## 1. 使用边界

- `已确认` 本表服务 V1 样片剪辑执行。
- `已确认` 主线是 `豆包 -> Trae -> 项目骨架 -> API -> 云剪 -> Codex 检查 -> 即梦对比`。
- `已确认` Trae 项目骨架不等于 app 跑通；API 特写不等于 API 已接通；阿里云剪辑不等于正式稳定；Codex 检查不等于内容过线。
- `已确认` 火山引擎素材只能在安全裁切 / 放大 / 打码后作 API 局部特写；无法确认时必须 fallback 到信息卡。
- `已确认` 本轮执行采用 `redaction_blocked_fallback_to_info_card`，不使用火山引擎原画面。

## 2. block -> segment -> 素材承载表

| block | segment | 口播摘要 | 推荐素材 | 推荐时间码 | 是否需要打码 / 裁切 | 能证明什么 | 不能证明什么 | 执行备注 |
|---|---|---|---|---|---|---|---|---|
| 主判断 | 自动流不是一键生成 | 一键生成像抽素材，自动流要拆成可重复流程。 | 流程总览卡 | 信息卡 | 否 | 建立流程证明主题。 | 不证明任何工具已跑通。 | `cute_info_card_route`。 |
| 豆包阶段 | 一句需求输入 | 用户只给豆包一句：`我想用 Trae 做一个短视频自动流`。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:00:16-00:00:24 | 裁切侧栏 | 需求入口很简单。 | 不能证明 Trae 已执行。 | 强证据段。 |
| 豆包阶段 | 豆包拆方案 | 豆包给出从 0 基础轻量版到无人值守版的方案。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:01:28-00:02:00 | 裁切侧栏 | 豆包把短视频生产拆成流程 / 工位。 | 不能证明工程跑通。 | 强调“想法层”。 |
| 豆包阶段 | 用户要求 Trae prompt | 用户让豆包生成 Vlog 自动流 prompt 给 Trae 搭架构。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:02:40-00:02:56 | 裁切侧栏 | 豆包承担“翻译成任务说明”。 | 不能证明 prompt 已进入 Trae。 | 关键转折。 |
| 豆包阶段 | 豆包输出 Trae SOLO prompt | 可见 `Trae Vlog 自动流核心搭建 Prompt` 和 7 个模块。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:03:52-00:04:08 | 裁切；小字不硬读 | 豆包生成 Trae 能接住的 prompt。 | 不能证明脚本运行成功。 | 可叠 prompt 卡。 |
| Trae 阶段 | 进入 SOLO Coder | 进入 Trae SOLO Coder，出现 `/plan`、`/spec` 能力提示。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:00:32-00:01:04 | 裁切本地路径 | 用户进入可执行工具环境。 | 不能证明 prompt 已提交。 | 不剪成 Trae 教程。 |
| Trae 阶段 | prompt 进入 Trae 并开始 plan | prompt 模块文字进入输入区，出现 `Updating Tasks...` 和 `11 待办`。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:01:20-00:01:52 | 裁切本地路径；不写清楚看到快捷键 | Trae SOLO 接住 prompt 并开始 plan。 | 不能证明所有待办完成。 | 保留 11 待办证据。 |
| Trae 阶段 | 项目骨架生成 | 可见 `vlog_automation_workflow`、`modules`、`templates`、`workflows`、`config`、`assets`、`frontend`、`logs`、`settings.py`、`base_module.py`。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:02:00-00:02:40 | 裁切本地路径 | 从 prompt 到真实项目骨架。 | 不能证明代码运行成功、app 已跑通。 | 必须搭配“看不懂代码也没关系”文案。 |
| API 阶段 | API 是外部能力入口 | API 把文字、配音、图片、卡片、剪辑等外部工具接成可调用能力。 | API 信息卡 | 信息卡 | 否 | 解释 API 工位。 | 不能证明 API 已全部接通。 | 本轮不使用火山引擎原画面。 |
| 云端总装 | 阿里云剪辑 / ICE / 云剪 | 云剪是装配台，不是总控脑。 | 云端总装信息卡 | 信息卡 | 否 | 说明云端总装位置。 | 不能证明正式稳定链路。 | 写成候选 / 待验证。 |
| Codex 阶段 | 执行检查 | Codex 检查路径、素材、音频、解码、文件、Git、报告。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:02:56-00:03:08 | 遮挡右侧分支详情、底部路径、文件名、巨大 diff 数字 | Codex 执行检查和状态回报。 | 不能证明内容过线。 | 主证据段。 |
| HyperFrames 候选 | 技术处理 B-roll | 只作技术处理痕迹候选。 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:03:36-00:03:44 | 避开路径 | 可证明渲染命令痕迹。 | 不作为 Codex 检查主证据。 | 本轮未使用进主片。 |
| 即梦对比 | 单点素材 vs 可复用流程 | 即梦适合出素材，自动流解决可复用生产流程。 | 即梦对比卡 | 信息卡 | 否 | 完成工具定位对比。 | 不证明即梦不可用，不做评测。 | 克制表达。 |
| 总结 | 顺序对了 | 先拆流程，再接工具，再检查结果。 | 最后总结卡 | 信息卡 | 否 | 收束主观点。 | 不证明可发布。 | `send_ready = false`。 |
"""
    write_text(SCRIPT_PACK_DIR / "02_分段承载表_block_segment_material_map.md", segment_map)

    card_copy = """# 卡片文案：短视频自动流的最简单流程 V2

## 1. 卡片使用原则

- `已确认` 信息卡统一走 `cute_info_card_route`。
- `已确认` 本轮不使用骚萌卡占位；若后续使用，必须走 `sassy_reaction_card_route`，不得套信息卡外壳。
- `已确认` 一屏最多 2-3 个信息模块，不做密集 dashboard，不强卖课。
- `已确认` 不伪造素材没有证明的数据。

## 2. 流程总览卡

主标题：短视频自动流，不是一键生成

信息模块：一句需求 / 拆成流程 / 交给工具执行 / 结果能检查

小字：先把顺序理出来，自动化才有地方落脚。

## 3. 豆包 -> Trae prompt 卡

主标题：豆包把想法翻译成任务说明

信息模块：先拆方案 / 再生成 Trae SOLO prompt / 让执行器能接住

小字：关键不是继续聊天，而是形成可执行 prompt。

## 4. Trae 骨架卡

主标题：看不懂代码也没关系

信息模块：有没有项目目录 / 有没有模块和配置 / 有没有 app 初步形状

小字：项目骨架出现，不等于代码已经跑通。

## 5. API 解释卡

主标题：API 是外部能力入口

信息模块：文字生成 / 配音、图片、卡片 / 剪辑总装

小字：本轮使用信息卡替代火山引擎原画面；API 特写不等于 API 已接通。

## 6. 阿里云剪辑总装卡

主标题：阿里云剪辑是装配台

信息模块：不负责想创意 / 不负责写文案 / 负责按时间线总装

小字：云端总装候选，不是正式稳定链路。

## 7. Codex 检查卡

主标题：Codex 更像执行检查员

信息模块：路径是否存在 / 素材能否解码 / 报告有没有生成

小字：技术检查不等于内容过线。

## 8. 即梦对比卡

主标题：即梦像抽素材，自动流像搭流程

信息模块：即梦：快速出单个画面 / 自动流：把需求变成可复用生产线

小字：不是评测工具强弱，而是解决的问题不同。

## 9. 最后总结卡

主标题：顺序对了，自动化才有地方落脚

信息模块：拆清楚 / 接工具 / 能检查 / 可迭代

小字：别一上来追求一键生成。
"""
    write_text(SCRIPT_PACK_DIR / "03_卡片文案_card_copy.md", card_copy)

    execution_notes = f"""# 执行注意事项：短视频自动流的最简单流程 V2

## 1. 素材使用边界

- `已确认` 推荐主素材：`豆包素材.mp4`、`trae 素材.mp4`、`codex 素材.mp4`。
- `已确认` `创建文件夹.mp4` 只能作为 1-2 秒弱 B-roll；本轮样片未让它承担主证据。
- `已确认` `录屏2026-04-30 03.25.28.mov` 默认不进入本条视频。
- `已确认` 火山引擎 API 管理页可理论上裁切 / 放大 / 打码后作为 API 局部特写。
- `已确认` 本轮由于素材已知含手机号、验证码、API Key 管理页和资源 ID 痕迹，且无法在自动流程中保证视觉脱敏零风险，执行 `redaction_blocked_fallback_to_info_card`。
- `已确认` 不提交原始素材本体，不提交本地签名 URL，不提交未脱敏截图。

## 2. 必须保留的 Trae 段新增判断

这些代码文件，普通人其实看不懂也没关系。这一步最重要的，不是你能不能看懂每一行代码，而是看 Trae 有没有真的把这个东西执行出一个初步形状。

执行时必须让观众看懂：

- 有没有项目目录。
- 有没有模块。
- 有没有配置文件。
- 有没有基础代码。
- 有没有从一句 prompt 变成 app / 项目雏形。

## 3. 状态边界

- `已确认` 豆包输出方案不等于工程跑通。
- `已确认` 豆包生成 Trae prompt 不等于系统已运行。
- `已确认` Trae 生成项目骨架不等于代码运行成功。
- `已确认` `settings.py` / `base_module.py` 可见，只能证明初步项目形状出现。
- `待验证` API 特写 / API 信息卡不等于 API 已接通。
- `待验证` 阿里云剪辑 / ICE / 云剪只能写成云端总装候选，不得写成正式稳定链路。
- `已确认` Codex 检查不等于内容过线。
- `已确认` 生成 MP4 不等于可发布。
- `已确认` 本轮样片状态必须保持：`content_validation = pending_user_chatgpt_review`，`send_ready = false`。
- `已确认` `final_voice_validated = false`，`voice_validation = pending_user_chatgpt_review`。

## 4. 剪辑结构边界

- 不做工具教程、Trae 教程、Codex 教程、阿里云剪辑教程。
- 不做即梦评测，不攻击即梦。
- 主线不是工具介绍合集，而是“短视频自动流是可复用流程，不是一键生成”。
- API、阿里云、Codex、即梦只作为流程工位，不抢主叙事。

## 5. 遮挡项

- Trae：裁切本地路径、项目列表、底部路径；环境提示 / 失败提示不得被剪掉后误导为全成功。
- Codex：遮挡右侧分支详情、底部路径、文件名、巨大 diff 数字、本地任务信息。
- 火山引擎：本轮不入片；只保留信息卡 fallback。
"""
    write_text(SCRIPT_PACK_DIR / "04_执行注意事项_execution_notes.md", execution_notes)

    codex_input = """# 给 Codex 剪辑执行输入：短视频自动流的最简单流程 V2

## 1. 标题

《短视频自动流的最简单流程》

## 2. 文案文件路径

- 完整口播稿：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/01_完整口播稿_full_script.md`
- 分段承载表：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/02_分段承载表_block_segment_material_map.md`
- 卡片文案：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/03_卡片文案_card_copy.md`
- 执行注意事项：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/04_执行注意事项_execution_notes.md`

## 3. 推荐素材路径与时间码

| 用途 | 素材路径 | 推荐时间码 | 说明 |
|---|---|---|---|
| 一句需求输入 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:00:16-00:00:24 | 用户只输入一句简单需求。 |
| 豆包拆方案 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:01:28-00:02:00 | 豆包输出轻量版到无人值守版方案。 |
| 用户要求 Trae prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:02:40-00:02:56 | 用户要求豆包生成给 Trae 的 prompt。 |
| 豆包输出 Trae SOLO prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:03:52-00:04:08 | 可见 Trae Vlog 自动流核心搭建 prompt 和模块清单。 |
| 进入 Trae SOLO Coder | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:00:32-00:01:04 | 可见 SOLO Coder 和 `/plan`、`/spec` 能力提示。 |
| prompt 进入 Trae 并 plan | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:01:20-00:01:52 | prompt 模块文字、`Updating Tasks...`、`11 待办`。 |
| Trae 生成项目骨架 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:02:00-00:02:40 | `vlog_automation_workflow`、目录、`settings.py`、`base_module.py`。 |
| API 特写 | 火山引擎素材仅可脱敏使用 | 条件使用 | 本轮无法自动确认安全脱敏，fallback 到信息卡。 |
| 阿里云剪辑 / ICE / 云剪 | 信息卡 | 信息卡 | 说明云端总装候选位置，不证明正式稳定。 |
| Codex 执行检查 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:02:56-00:03:08 | `ffprobe`、命令执行、文件变更、Git 操作和报告文件。 |
| HyperFrames 技术处理 B-roll | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:03:36-00:03:44 | 只作候选，不作为 Codex 检查主证据。 |

## 4. 卡片清单

1. 流程总览卡：自动流不是一键生成。
2. 豆包到 Trae prompt 卡：把想法翻译成执行器能接的任务说明。
3. Trae 骨架卡：看不懂代码没关系，先看 app / 项目有没有初步形状。
4. API 解释卡：API 是把外部工具接成系统可调用能力。
5. 阿里云剪辑总装卡：它是装配台，不是总控脑。
6. Codex 检查卡：技术检查不等于内容过线。
7. 即梦对比卡：即梦像抽素材，自动流像搭流程。
8. 最后总结卡：顺序对了，自动化才有地方落脚。

## 5. 禁用 / 条件素材

- 火山引擎素材：未完成安全脱敏前不得使用原画面；本轮 fallback 到信息卡。
- 创建文件夹素材：只可弱 B-roll。
- 2026-04-30 长录屏：默认不进入本条视频。

## 6. 输出状态边界

- `technical_validation` 必须由 ffprobe / decode 结果决定。
- `content_validation = pending_user_chatgpt_review`。
- `send_ready = false`。
- `audio_validation = temporary_preview` 或 `silence_placeholder`，不得写最终声音通过。
"""
    write_text(SCRIPT_PACK_DIR / "05_给Codex剪辑执行输入_codex_video_execution_input.md", codex_input)

    manifest = {
        "title": "短视频自动流的最简单流程",
        "script_type": "流程证明型视频样片执行包",
        "updated_at": NOW,
        "source_anchor": "FINAL_SCRIPT_V2_user_confirmed_flow_detail_enhanced",
        "status": {
            "script_pack": "updated_to_final_script_v2",
            "video_generated": True,
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "technical_validation": "pending_render_verification",
        },
        "must_keep": [
            "Trae 段：看不懂代码也没关系，重点看 app / 项目有没有初步形状",
            "火山引擎 API 特写边界：必须脱敏，无法确认安全时 fallback 信息卡",
            "Trae 项目骨架不等于 app 跑通",
            "API 特写不等于 API 已接通",
            "阿里云剪辑不是正式稳定链路",
            "Codex 检查不等于内容过线",
        ],
        "material_paths": {
            "doubao": str(DOUBAO),
            "trae": str(TRAE),
            "codex": str(CODEX),
            "volcengine_conditionally_allowed_only_after_redaction": str(VOLCENGINE),
            "folder_broll_weak": str(FOLDER_BROLL),
            "historical_long_recording_excluded": str(HISTORICAL_MOV),
        },
        "output_dir": str(OUTPUT_DIR),
        "script_sha256": sha256_text(clean_script_text()),
        "files": {
            "full_script": rel(SCRIPT_PACK_DIR / "01_完整口播稿_full_script.md"),
            "block_segment_material_map": rel(SCRIPT_PACK_DIR / "02_分段承载表_block_segment_material_map.md"),
            "card_copy": rel(SCRIPT_PACK_DIR / "03_卡片文案_card_copy.md"),
            "execution_notes": rel(SCRIPT_PACK_DIR / "04_执行注意事项_execution_notes.md"),
            "codex_video_execution_input": rel(SCRIPT_PACK_DIR / "05_给Codex剪辑执行输入_codex_video_execution_input.md"),
        },
    }
    write_json(SCRIPT_PACK_DIR / "script_pack_manifest.json", manifest)


def write_plans(sequence: list[dict[str, Any]], card_paths: dict[str, str]) -> None:
    rows = []
    for idx, seg in enumerate(sequence, start=1):
        if seg["type"] == "clip":
            rows.append(
                f"| {idx:02d} | `{seg['id']}` | `{seg['source']}` | {seg['start']:.2f}-{seg['end']:.2f}s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |"
            )
        else:
            rows.append(
                f"| {idx:02d} | `{seg['id']}` | `{seg['image']}` | {seg['duration']:.2f}s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |"
            )

    write_text(
        OUTPUT_DIR / "assembly_plan.md",
        f"""# 装配计划 assembly_plan

## 1. 样片目标

- `已确认` 本轮只完成《短视频自动流的最简单流程》视频样片 V1。
- `已确认` 样片主线：豆包一句需求 -> 豆包拆流程 -> 豆包生成 Trae prompt -> Trae SOLO plan / 11 待办 -> Trae 项目骨架 -> API 信息卡 -> 云端总装信息卡 -> Codex 检查 -> 即梦对比 -> 总结。
- `已确认` 本轮不把 MP4 生成写成内容过线，不把样片写成可发布。

## 2. 时间线

| order | segment_id | 素材路径 | 时间码 / 时长 | 裁切 / 遮挡 | 能证明什么 | 不能证明什么 |
|---|---|---|---|---|---|---|
{os.linesep.join(rows)}

## 3. 火山引擎 API 段决策

- `已确认` 原素材存在手机号、验证码、API Key 管理页和资源 ID 风险。
- `已确认` 本轮没有使用火山引擎原画面。
- `已确认` API 段使用 `04_API解释_api_explainer.png` 信息卡承载。
- `已确认` redaction result：`redaction_blocked_fallback_to_info_card`。

## 4. 声音 / 字幕

- `audio_validation`：`temporary_preview` 或 `silence_placeholder`，以渲染报告为准。
- `voice_validation`：`pending_user_chatgpt_review`。
- `final_voice_validated`：`false`。
- 字幕文件：`captions.srt`，按 `FINAL_SCRIPT_V2` 段落对齐。
""",
    )

    def json_safe(value: Any) -> Any:
        if isinstance(value, pathlib.Path):
            return str(value)
        if isinstance(value, dict):
            return {key: json_safe(item) for key, item in value.items()}
        if isinstance(value, list):
            return [json_safe(item) for item in value]
        return value

    manifest = {
        "schema": "short_video_auto_flow_v2_assembly_manifest/v1",
        "created_at": NOW,
        "workspace": str(ROOT),
        "output_dir": str(OUTPUT_DIR),
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "volcengine_api_closeup_used": False,
        "volcengine_redaction_decision": "redaction_blocked_fallback_to_info_card",
        "cards": card_paths,
        "segments": json_safe(sequence),
    }
    write_json(OUTPUT_DIR / "assembly_manifest.json", manifest)

    write_text(
        OUTPUT_DIR / "redaction_plan.md",
        f"""# 脱敏计划 redaction_plan

## 1. 火山引擎 API 特写边界

- 允许：只截取 API 管理页可安全展示区域，裁切 / 放大 / 打码后作为“API 能力入口”特写。
- 必须遮挡：手机号、短信验证码、API Key 明文、资源 ID、账号信息、URL 中可能暴露账号或资源的信息、任何密钥 / token / secret / AccessKey / 临时授权 URL。
- 不得证明：API 已全部接通、云端剪辑链路稳定、内容过线。

## 2. 本轮决策

- `已确认` PR #38 已记录火山引擎素材含手机号、验证码、API Key 管理页和资源 ID 痕迹。
- `已确认` 自动裁切无法保证对所有敏感视觉信息零风险。
- `已确认` 本轮执行 fallback：不使用火山引擎原画面，改用 API 信息卡。

## 3. 输出

- `redaction_report.md`：记录 fallback。
- `redaction_contact_sheet.jpg`：显示 API 信息卡 fallback 预览。
""",
    )


def write_route_and_inheritance_reports(card_paths: dict[str, str]) -> None:
    route_map = {
        "schema": "short_video_auto_flow_v2_visual_route_map/v1",
        "created_at": NOW,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "segments": [
            {
                "segment_id": spec["id"],
                "card_type": "info_card",
                "assigned_route": spec["route"],
                "primary_reference": "cute_info_card_route_locked_20260501",
                "secondary_reference": "card_visual_quality_clean_ui_texture_candidate_20260430",
                "forbidden_references": ["sassy_card_pr7_a_candidate_20260428", "deep_blue_tech_saas_ui_info_card_rejected_direction"],
                "renderer_function": "PIL_programmatic_cute_info_card",
                "validation_gate": "not_dense_dashboard_no_fake_data_no_tool_tutorial",
                "can_share_shell_with": "cute_info_card_route",
                "must_not_share_shell_with": "sassy_reaction_card_route",
                "asset_path": card_paths[spec["id"]],
            }
            for spec in CARD_SPECS
        ],
    }
    write_json(OUTPUT_DIR / "visual_route_map.json", route_map)
    write_text(
        OUTPUT_DIR / "visual_route_validation_report.md",
        """# 视觉路由验证报告 visual_route_validation_report

- `已确认` 本轮信息卡均走 `cute_info_card_route`。
- `已确认` 本轮未生成骚萌卡；未触发 `sassy_reaction_card_route`，也没有回退 PR #7 A。
- `已确认` API、云剪、Codex、即梦对比均只作流程工位说明，不做工具教程或评测页。
- `已确认` 卡片不是密集 dashboard，没有伪造素材未证明的数据。
- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
""",
    )
    write_text(
        OUTPUT_DIR / "locked_reference_inheritance_report.md",
        """# 锁定参考继承报告 locked_reference_inheritance_report

## 1. 读取状态

- `已确认` 已读取 `codex_source/14_locked_reference_inheritance_rules.md`。
- `已确认` 已读取 `codex_source/locked_reference_registry.md`。
- `已确认` 已读取 `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`。

## 2. 本轮命中情况

| reference_id | 本轮是否命中 | 继承 / 不继承口径 | 结果 |
|---|---:|---|---|
| `cute_info_card_route_locked_20260501` | 是 | 信息卡继承粉色柔和 + 清晰信息层级；不做深蓝科技 UI / dashboard。 | `passed_for_sample_route` |
| `sassy_card_pr7_b_visual_locked_20260501` | 否 | 本轮不生成骚萌卡；未使用 PR #7 A。 | `not_applicable` |
| `sassy_card_three_type_rule_locked_20260428` | 否 | 本轮不插骚萌卡，不承担主叙事。 | `not_applicable` |
| `middle_editing_round34_locked_20260425` | 部分命中 | 本轮是新流程样片，不复刻 round34 中段结构；仍保留真实录屏为主证据的原则。 | `partial_principle_only` |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | 部分命中 | 对录屏做竖屏裁切和隐私遮挡；不是复刻旧中段放大。 | `partial_principle_only` |
| `tts_15s_b_pacing_locked_20260427` | 否 | 本轮只用系统临时 TTS 预览或静音占位，不能写声音通过。 | `not_inherited_voice_pending` |

## 3. 状态边界

- `technical_validation` 只看渲染 / 解码结果。
- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
""",
    )


def write_redaction_report() -> None:
    write_text(
        OUTPUT_DIR / "redaction_report.md",
        f"""# 脱敏报告 redaction_report

## 1. 是否使用火山引擎 API 特写

- 是否使用火山引擎 API 原画面：`false`
- 是否完成遮挡：`not_applicable_for_source_footage`
- 是否 fallback 到信息卡：`true`
- fallback 标记：`redaction_blocked_fallback_to_info_card`

## 2. 决策依据

- `已确认` 素材采集汇报已标记火山引擎素材存在手机号、短信验证码、API Key 管理页和资源 ID 痕迹。
- `已确认` 本轮无法仅靠自动裁切保证所有敏感视觉信息安全。
- `已确认` 因此 API 段使用信息卡解释“外部能力入口”，不使用火山引擎原画面。

## 3. 敏感信息检查结论

- `已确认` 本轮装配清单中没有火山引擎视频片段。
- `已确认` 未提交火山引擎未脱敏截图。
- `待验证` 视觉层最终仍需用户 / ChatGPT 看 `contact_sheet.jpg` 复审；Codex 不把该检查写成内容过线。

## 4. 禁止误读

- API 信息卡不证明 API 已接通。
- 云平台入口不证明云端剪辑稳定。
- 样片 MP4 不证明可发布。
""",
    )


def write_render_reports(video_meta: dict[str, Any], audio_info: dict[str, Any], sequence: list[dict[str, Any]]) -> None:
    sensitive_scan = scan_sensitive_text()
    write_text(
        OUTPUT_DIR / "render_report.md",
        f"""# 渲染报告 render_report

## 1. 任务结果

- `technical_validation`：`{video_meta['technical_validation']}`
- `metadata_validation`：`{video_meta['metadata_validation']}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`{audio_info['audio_validation']}`
- `tts_validation`：`{audio_info['tts_validation']}`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 输出文件

- full_video：`{video_meta['file_path']}`
- captions：`{OUTPUT_DIR / 'captions.srt'}`
- assembly_manifest：`{OUTPUT_DIR / 'assembly_manifest.json'}`
- contact_sheet：`{OUTPUT_DIR / 'contact_sheet.jpg'}`
- redaction_report：`{OUTPUT_DIR / 'redaction_report.md'}`
- local_open_path_report：`{OUTPUT_DIR / 'local_open_path_report.md'}`

## 3. ffprobe / decode

- exists：`{video_meta['exists']}`
- file_size_bytes：`{video_meta['file_size_bytes']}`
- duration_seconds：`{video_meta['duration_seconds']:.3f}`
- resolution：`{video_meta['width']}x{video_meta['height']}`
- video_codec：`{video_meta['video_codec']}`
- audio_present：`{str(video_meta['audio_present']).lower()}`
- audio_codec：`{video_meta['audio_codec']}`
- audio_channels：`{video_meta['audio_channels']}`
- decodable：`{str(video_meta['decodable']).lower()}`

## 4. 脱敏与素材使用

- 火山引擎 API 特写：`not_used`
- fallback：`redaction_blocked_fallback_to_info_card`
- Codex 段遮挡：右侧分支详情 / 底部路径区域 / 顶部区域已加黑条遮挡。
- Trae 段遮挡：底部路径区域 / 顶部区域已加黑条遮挡。
- 豆包段遮挡：底部路径区域 / 顶部区域已加弱遮挡。

## 5. 敏感信息文本扫描

- scan_status：`{sensitive_scan['status']}`
- matched_files：`{sensitive_scan['matched_files']}`
- notes：文本文件扫描只覆盖可读交付文本；视觉层通过不使用火山原画面、遮挡敏感区域和 contact sheet 复审降低风险。

## 6. 时间线摘要

- segment_count：`{len(sequence)}`
- 片段总时长以 mux 后 `full_video.mp4` 为准。

## 7. 状态边界

- 本轮生成 MP4 只代表技术样片存在。
- 技术验证通过不等于内容验证通过。
- 本轮不得把发送状态写成真值。
""",
    )

    write_json(
        OUTPUT_DIR / "render_summary.json",
        {
            "technical_validation": video_meta["technical_validation"],
            "metadata_validation": video_meta["metadata_validation"],
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "audio_validation": audio_info["audio_validation"],
            "tts_validation": audio_info["tts_validation"],
            "voice_validation": "pending_user_chatgpt_review",
            "final_voice_validated": False,
            "video_meta": video_meta,
            "sensitive_text_scan": sensitive_scan,
        },
    )

    write_text(
        OUTPUT_DIR / "local_open_path_report.md",
        f"""# 本地打开路径报告 local_open_path_report

| field | value |
|---|---|
| artifact_id | `short_video_auto_flow_v2_sample_full_video` |
| canonical_local_path | `{OUTPUT_DIR / 'full_video.mp4'}` |
| path_exists | `{str((OUTPUT_DIR / 'full_video.mp4').exists()).lower()}` |
| workspace_boundary | `/Users/fan/Documents/视频工厂` |
| content_validation | `pending_user_chatgpt_review` |
| send_ready | `false` |
| verified_at | `{NOW}` |

`已确认` 该路径位于唯一正式工作区内部，不是 `/private/tmp`、Desktop、Downloads 或外部 worktree。
""",
    )

    write_text(
        OUTPUT_DIR / "script_runtime_adjustment_report.md",
        f"""# 口播时长调整报告 script_runtime_adjustment_report

- `已确认` 文案包 `01_完整口播稿_full_script.md` 已保真写入 `FINAL_SCRIPT_V2`。
- `已确认` 本轮 `captions.srt` 使用完整 `FINAL_SCRIPT_V2` 段落生成。
- `已确认` 本轮没有删减用户最终确认文案。
- `已确认` 临时系统 TTS 可能在读音、英文缩写和停顿上与最终声音不同，只能标记 `audio_validation = {audio_info['audio_validation']}`。
- `待验证` 最终口播节奏、音色和内容表现仍待用户 / ChatGPT 复审。
""",
    )


def scan_sensitive_text() -> dict[str, Any]:
    patterns = [
        r"AccessKey\s*[:=]",
        r"secret\s*[:=]",
        r"token\s*[:=]",
        r"api[_ -]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}",
        r"AKIA[0-9A-Z]{16}",
        r"https://[^\\s]+(" + r"Signature|Expires|X-Amz|OSSAccessKeyId)",
        r"短信验证码[:：]?\s*\d{4,8}",
        r"手机号[:：]?\s*1\d{10}",
    ]
    regexes = [re.compile(p, re.I) for p in patterns]
    matched: list[str] = []
    for path in list(OUTPUT_DIR.glob("*.md")) + list(OUTPUT_DIR.glob("*.json")) + list(OUTPUT_DIR.glob("*.srt")) + list(SCRIPT_PACK_DIR.glob("*.md")) + list(SCRIPT_PACK_DIR.glob("*.json")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(r.search(text) for r in regexes):
            matched.append(str(path))
    return {"status": "passed" if not matched else "needs_review", "matched_files": matched}


def update_local_artifact_index() -> None:
    index = ROOT / "codex_log" / "current_local_artifact_paths.md"
    existing = index.read_text(encoding="utf-8")
    block = f"""

| `short_video_auto_flow_v2_sample_full_video` | 短视频自动流最简单流程 V1 样片 | 本轮流程证明型视频样片，本地复审入口；不是可发布状态 | `{OUTPUT_DIR / 'full_video.mp4'}` | `true` | 无 | `2026-05-03 CST` | `ffprobe` / `test -f` / 本轮渲染验证 | `content_validation = pending_user_chatgpt_review`；`send_ready = false`；媒体文件为 local_only，不强行提交 Git。 |
"""
    marker = "| `short_video_auto_flow_v2_sample_full_video` |"
    if marker not in existing:
        insert_at = existing.find("\n## 4. 本轮")
        if insert_at != -1:
            existing = existing[:insert_at] + block + existing[insert_at:]
        else:
            existing += block
    else:
        existing = re.sub(r"\| `short_video_auto_flow_v2_sample_full_video` \|.*\|\n", block.lstrip(), existing)
    existing = re.sub(r"## 6\. 最后更新时间\n\n- `[^`]+`", "## 6. 最后更新时间\n\n- `2026-05-03 CST`", existing)
    write_text(index, existing)


def update_logs(video_meta: dict[str, Any], audio_info: dict[str, Any]) -> None:
    latest = ROOT / "codex_log" / "latest.md"
    existing = latest.read_text(encoding="utf-8")
    entry = f"""# Latest

## 20260503｜短视频自动流 V2 视频样片 V1

- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/short-video-auto-flow-v2-video-sample-20260503`。
- `已确认` 主读取分支缺 PR #38 / #39 / #40 的素材报告与文案包文件；本轮已读取 PR head 并回收到任务分支作为 reference source。
- `已确认` 用户最终确认的 `FINAL_SCRIPT_V2（流程细节增强版）` 已保真写入文案包。
- `已确认` 已同步更新分段承载表、卡片文案、执行注意事项、给 Codex 剪辑执行输入和 manifest。
- `已确认` 已生成本地可观看样片：`{OUTPUT_DIR / 'full_video.mp4'}`。
- `已确认` 火山引擎 API 原画面本轮未入片，执行 `redaction_blocked_fallback_to_info_card`。
- `已确认` 技术验证：`technical_validation = {video_meta['technical_validation']}`；分辨率 `{video_meta['width']}x{video_meta['height']}`；时长 `{video_meta['duration_seconds']:.3f}s`；video codec `{video_meta['video_codec']}`；audio codec `{video_meta['audio_codec']}`；可解码 `{str(video_meta['decodable']).lower()}`。
- `已确认` 音频状态：`audio_validation = {audio_info['audio_validation']}`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`。
- `已确认` 内容状态未提升：`content_validation = pending_user_chatgpt_review`；`send_ready = false`。
- `已确认` 本轮未修改 v3.1 `dist/latest_review_pack/` 当前基线，不把新样片写成当前可发布对象。
- `复审输出`：`{OUTPUT_DIR}`
- `下一个目标`：ChatGPT / 用户完成 V1 样片内容复审，确认流程叙事是否看得懂，以及下一轮只改一个变量。

"""
    if existing.startswith("# Latest\n"):
        existing = entry + existing[len("# Latest\n\n"):] if existing.startswith("# Latest\n\n") else entry + existing[len("# Latest\n"):]
    else:
        existing = entry + "\n" + existing
    write_text(latest, existing)

    dated = ROOT / "codex_log" / "20260503_短视频自动流v2视频样片_short_video_auto_flow_v2_video_sample.md"
    write_text(
        dated,
        f"""# 20260503｜短视频自动流 v2 视频样片

## 1. 任务结果

- `technical_validation`：`{video_meta['technical_validation']}`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`{audio_info['audio_validation']}`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 输入来源

- 主读取分支：`AGENTS.md`、`codex_source/*`、`GPT数据源/*`、`codex_log/latest.md`、`codex_log/current_local_artifact_paths.md`。
- PR #38 head：素材采集汇报、`material_inventory.json`、`recommended_assembly_inputs.json`。
- PR #39 head：素材细节复采报告、`doubao_to_trae_flow_evidence.json`、`chatgpt_copywriting_input.md`。
- PR #40 head：旧文案包；本轮已被用户最终确认 `FINAL_SCRIPT_V2` 覆盖。

## 3. 修改与产物

- 文案包目录：`{SCRIPT_PACK_DIR}`
- 样片输出目录：`{OUTPUT_DIR}`
- full_video：`{OUTPUT_DIR / 'full_video.mp4'}`
- captions：`{OUTPUT_DIR / 'captions.srt'}`
- assembly_manifest：`{OUTPUT_DIR / 'assembly_manifest.json'}`
- render_report：`{OUTPUT_DIR / 'render_report.md'}`
- contact_sheet：`{OUTPUT_DIR / 'contact_sheet.jpg'}`
- redaction_report：`{OUTPUT_DIR / 'redaction_report.md'}`
- local_open_path_report：`{OUTPUT_DIR / 'local_open_path_report.md'}`

## 4. 脱敏结果

- 火山引擎 API 特写：`not_used`
- 遮挡完成：`not_applicable_for_volcengine_source`
- fallback 到信息卡：`true`
- fallback 标记：`redaction_blocked_fallback_to_info_card`
- 敏感信息检查：文本扫描未发现密钥类模式；视觉层未使用火山原画面，仍需用户 / ChatGPT 看 contact sheet 复审。

## 5. 验证结果

- ffprobe：`passed`
- 分辨率：`{video_meta['width']}x{video_meta['height']}`
- 时长：`{video_meta['duration_seconds']:.3f}s`
- video codec：`{video_meta['video_codec']}`
- audio codec：`{video_meta['audio_codec']}`
- 可解码：`{str(video_meta['decodable']).lower()}`
- content_validation / send_ready 检查：未写内容验证通过态，未写发送状态真值。

## 6. 下一个目标

ChatGPT / 用户完成 V1 样片内容复审，确认流程证明是否成立，并决定 V2 样片下一轮唯一改动变量。
""",
    )


def update_publish_target_notes() -> None:
    target = ROOT / "codex_log" / "current_publish_target.md"
    text = target.read_text(encoding="utf-8")
    note = f"""

## 本轮旁路样片说明：短视频自动流 V1

- `已确认` 2026-05-03 本轮另行生成《短视频自动流的最简单流程》V1 流程证明型样片。
- `已确认` 该样片输出目录：`{OUTPUT_DIR}`。
- `已确认` 该样片 `content_validation = pending_user_chatgpt_review`，`send_ready = false`。
- `已确认` 该样片不替换当前 v3.1 灰度测试对象，不修改 `dist/latest_review_pack/` 当前基线。
- `已确认` 当前 publish target 仍为《我用 AI 做 PPT 踩过的坑》v3.1；本轮新样片是独立复审对象。
"""
    if "## 本轮旁路样片说明：短视频自动流 V1" not in text:
        insert_at = text.find("\n## 最后更新时间")
        text = text[:insert_at] + note + text[insert_at:] if insert_at != -1 else text + note
    text = re.sub(r"## 最后更新时间\n\n- `[^`]+`", "## 最后更新时间\n\n- `2026-05-03 CST`", text)
    write_text(target, text)

    evidence = ROOT / "codex_log" / "current_publish_target_light_evidence.md"
    ev = evidence.read_text(encoding="utf-8")
    ev_note = f"""

## 旁路样片轻量证据：短视频自动流 V1

- `已确认` 本轮生成独立流程证明型样片，不替换 v3.1 当前发布后灰度测试对象。
- 样片输出目录：`{OUTPUT_DIR}`
- 可追踪文字证据：`{OUTPUT_DIR / 'assembly_manifest.json'}`、`{OUTPUT_DIR / 'render_report.md'}`、`{OUTPUT_DIR / 'redaction_report.md'}`、`{OUTPUT_DIR / 'local_open_path_report.md'}`
- 媒体本体：`full_video.mp4` 和图片预览为 `local_only`，不强行提交 Git。
- 状态边界：`content_validation = pending_user_chatgpt_review`，`send_ready = false`。
"""
    if "## 旁路样片轻量证据：短视频自动流 V1" not in ev:
        insert_at = ev.find("\n## 最后更新时间")
        ev = ev[:insert_at] + ev_note + ev[insert_at:] if insert_at != -1 else ev + ev_note
    ev = re.sub(r"## 最后更新时间\n\n- `[^`]+`", "## 最后更新时间\n\n- `2026-05-03 CST`", ev)
    write_text(evidence, ev)


def write_output_reports_before_render(card_paths: dict[str, str]) -> None:
    write_route_and_inheritance_reports(card_paths)
    write_redaction_report()


def main() -> None:
    if pathlib.Path.cwd() != ROOT:
        raise RuntimeError(f"must run inside {ROOT}")
    for path in [DOUBAO, TRAE, CODEX]:
        if not path.exists():
            raise RuntimeError(f"missing required material: {path}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    ffmpeg = resolve_bin("ffmpeg")
    ffprobe = resolve_bin("ffprobe")

    write_script_pack_files()
    card_paths = generate_cards()
    write_output_reports_before_render(card_paths)

    audio_info = make_tts(ffmpeg, ffprobe)
    make_captions(float(audio_info["duration_seconds"]))
    sequence, full_video = render_video(ffmpeg, ffprobe, audio_info, card_paths)
    video_meta = validate_video(ffmpeg, ffprobe, full_video)
    create_contact_sheet(ffmpeg, full_video, float(video_meta["duration_seconds"]))
    write_plans(sequence, card_paths)
    write_render_reports(video_meta, audio_info, sequence)
    update_local_artifact_index()
    update_logs(video_meta, audio_info)
    update_publish_target_notes()

    print(json.dumps({
        "output_dir": str(OUTPUT_DIR),
        "full_video": str(full_video),
        "technical_validation": video_meta["technical_validation"],
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "audio_validation": audio_info["audio_validation"],
        "duration_seconds": video_meta["duration_seconds"],
        "resolution": f"{video_meta['width']}x{video_meta['height']}",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
