from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
from typing import Dict, List


@dataclasses.dataclass
class BriefBundle:
    title: str
    sections: Dict[str, str]

    def get(self, key: str, default: str) -> str:
        value = self.sections.get(key, "").strip()
        return value or default

    def recording_items(self) -> List[str]:
        raw = self.get("4段核心录制素材", "")
        items: List[str] = []
        for line in raw.splitlines():
            cleaned = line.strip().lstrip("-").strip()
            if not cleaned:
                continue
            if cleaned[0].isdigit() and "." in cleaned:
                cleaned = cleaned.split(".", 1)[1].strip()
            items.append(cleaned)
        return items[:4] if items else [
            "原始糊话输入",
            "主 prompt 执行过程",
            "修结果 prompt 补强动作",
            "前后差值与总结收束",
        ]


def parse_markdown_sections(text: str) -> BriefBundle:
    title = "未命名工作台"
    sections: Dict[str, str] = {}
    current_key: str | None = None
    buffer: List[str] = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("# ") and title == "未命名工作台":
            title = line[2:].strip() or title
            continue
        if line.startswith("## "):
            if current_key is not None:
                sections[current_key] = "\n".join(buffer).strip()
            current_key = line[3:].strip()
            buffer = []
            continue
        if current_key is not None:
            buffer.append(line)

    if current_key is not None:
        sections[current_key] = "\n".join(buffer).strip()

    return BriefBundle(title=title, sections=sections)


def load_brief(path: pathlib.Path) -> BriefBundle:
    return parse_markdown_sections(path.read_text(encoding="utf-8"))


def _write_text(path: pathlib.Path, content: str, force: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        raise FileExistsError(f"{path} 已存在，若要覆盖请传 --force")
    path.write_text(content.strip() + "\n", encoding="utf-8")


def _json_result(**kwargs) -> str:
    return json.dumps(kwargs, ensure_ascii=False, indent=2)


def build_work_package_markdown(bundle: BriefBundle) -> str:
    return f"""
# 02_工作包正文

## 场景名称
{bundle.get("场景名称", bundle.title)}

## 当前任务一句话
{bundle.get("用户一句糊话", "待补充用户一句糊话")}

## 工作包定位
- 当前项目中心价值：`场景化专业输出工作包`
- 当前视频角色：`证明壳 / 入口壳`
- 当前工作包角色：`产品单元`
- 当前主线结构不变：`API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`

## 交付目标
{bundle.get("交付目标", "待补充交付目标")}

## 失败现场
{bundle.get("失败现场", "待补充失败现场")}

## vNext 外壳要求
- 开头人物壳：{bundle.get("开头人物壳", "Minecraft-inspired 原创体素方块风")}
- 结尾总结壳：{bundle.get("结尾总结壳", "Minecraft-inspired 原创体素方块风")}
- 视觉限制：只允许 inspired 原创体素方块风，不得复用官方 `logo / fonts / textures / images / models / sounds`
- 结尾总结后允许新增一张 `Prompt 引用尾卡`，但它只承担产品单元引用，不抢主叙事

## 三层 prompt 包入口
1. 第1层：主 prompt
2. 第2层：修结果 prompt
3. 第3层：展示与尾卡 prompt

## 4 段核心录制素材
1. {bundle.recording_items()[0]}
2. {bundle.recording_items()[1]}
3. {bundle.recording_items()[2]}
4. {bundle.recording_items()[3]}

## 结果差证明点
- 普通输入时：目标、边界、动作顺序容易缺位
- 工作包输入后：更像真实可交付物初稿
- 视频里要证明的不是“AI 很强”，而是“这套工作包让返工下降”
"""


def build_prompt_pack_markdown(bundle: BriefBundle) -> str:
    tail_card_reference = bundle.get(
        "Prompt 引用尾卡要引用什么",
        "主 prompt 的判断点 + 修结果 prompt 的补强动作",
    )
    return f"""
# 03_Prompt包

## 场景名称
{bundle.get("场景名称", bundle.title)}

## 第1层：主 prompt
- 目标：把一句糊话压成更像可交付物的工作包初稿
- 输入结构：
  - 场景目标
  - 交付对象
  - 边界限制
  - 验收判断
  - 输出格式
- 默认提示词骨架：
```text
你现在是这条《视频工厂》场景工作包的首轮压稿助手。
请把下面这句糊话，压成更像真实可交付物的初稿。

场景：{bundle.get("场景名称", bundle.title)}
用户一句糊话：{bundle.get("用户一句糊话", "待补")}
交付目标：{bundle.get("交付目标", "待补")}

输出时必须写清：
1. 目标
2. 边界
3. 关键判断点
4. 动作顺序
5. 输出格式
```

## 第2层：修结果 prompt
- 目标：把“看起来对但不能交”的版本继续修成更稳的专业初稿
- 默认补强方向：
  - 缺判断口径时补判断
  - 缺动作顺序时补顺序
  - 缺交付格式时补模板
  - 缺风险提醒时补边界
- 默认提示词骨架：
```text
不要重写成另一篇，请只修：
1. 判断口径是否清楚
2. 动作顺序是否可执行
3. 输出格式是否像真实交付物
4. 是否还有高返工风险
```

## 第3层：展示与尾卡 prompt
- 目标：服务视频展示、总结卡与 `Prompt 引用尾卡`
- 开头人物壳与结尾总结壳默认统一为：{bundle.get("开头人物壳", "Minecraft-inspired 原创体素方块风")}
- 默认提示词骨架：
```text
请把这条工作包压成适合视频结尾展示的 3 到 5 个判断点。
风格要求：
1. 口语短句
2. 游戏向导式低压表达
3. 适配 Minecraft-inspired 原创体素方块风总结卡
4. 不使用任何官方资产名词或素材指令
```

## Prompt 引用尾卡
- 引用目标：{tail_card_reference}
- 作用：只承担“产品单元引用”，不重复主叙事
- 尾卡结构：
  - 这套工作包解决什么问题
  - 主 prompt 在压什么
  - 修结果 prompt 在补什么
  - 用户下一步最小动作是什么
"""


def build_recording_plan_markdown(bundle: BriefBundle) -> str:
    items = bundle.recording_items()
    return f"""
# 04_录制计划

## 当前录制减负原则
- 人只录 4 段核心素材
- AI 先把 `场景简报 -> 工作包正文 -> Prompt 包 -> 结果差提示` 整理出来
- 开头人物壳、结尾总结壳、`Prompt 引用尾卡` 的视觉提示词由 AI 先给

## 4 段核心录制素材

### 核心素材 1
- 素材名：{items[0]}
- 目标：证明原始问题真的模糊
- 必出镜：原始糊话 / 原始输入

### 核心素材 2
- 素材名：{items[1]}
- 目标：证明主 prompt 如何压出第一版结构
- 必出镜：主 prompt 输入结构 + 第一版输出

### 核心素材 3
- 素材名：{items[2]}
- 目标：证明修结果 prompt 如何把“看起来对”修成“更像能交”
- 必出镜：修结果动作 + 补强后的关键变化

### 核心素材 4
- 素材名：{items[3]}
- 目标：证明前后差值与最终收束
- 必出镜：普通输入 vs 工作包输入差值 + 总结句

## 非录制项
- 开头人物壳：{bundle.get("开头人物壳", "Minecraft-inspired 原创体素方块风")}
- 结尾总结壳：{bundle.get("结尾总结壳", "Minecraft-inspired 原创体素方块风")}
- `Prompt 引用尾卡`：由 AI 先生成结构和提示词，再由人决定是否微调
"""


def build_review_checklist_markdown(bundle: BriefBundle) -> str:
    return f"""
# 05_回审清单

## 结构核验
- [ ] 主线仍是 `API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`
- [ ] 开头人物壳只承担判断进入，不替代中段证据
- [ ] 结尾总结卡后新增的 `Prompt 引用尾卡` 没有抢主叙事

## 视觉核验
- [ ] 开头人物壳使用 {bundle.get("开头人物壳", "Minecraft-inspired 原创体素方块风")}
- [ ] 结尾总结壳使用 {bundle.get("结尾总结壳", "Minecraft-inspired 原创体素方块风")}
- [ ] 没有复用任何官方 `logo / fonts / textures / images / models / sounds`

## Prompt 包核验
- [ ] 已交付第1层主 prompt
- [ ] 已交付第2层修结果 prompt
- [ ] 已交付第3层展示与尾卡 prompt
- [ ] 已交付 `Prompt 引用尾卡`

## 录制核验
- [ ] 只要求 4 段核心录制素材
- [ ] 每段素材都有明确证明点
- [ ] 结果差证明点已经写清

## 结论
- 当前样板目标：能直接给用户上手
- 当前不承诺：已经直接产出最终成片
"""


def build_result_diff_markdown(bundle: BriefBundle) -> str:
    return f"""
# 06_结果差对比

## 场景
{bundle.get("场景名称", bundle.title)}

## 普通输入
- 只有一句糊话
- 容易缺目标、边界、判断口径
- 输出看起来长，但不能直接交

## 工作包输入
- 主 prompt 先压目标、边界、输出格式
- 修结果 prompt 再补判断与风险
- 展示与尾卡 prompt 负责视频引用与收束

## 视频里要证明的差值
1. 普通输入：像草稿
2. 工作包输入：更像可交付物初稿
3. 用户返工量：明显下降
"""


def build_execution_log_markdown(bundle: BriefBundle) -> str:
    return f"""
# 工作台执行日志

## 场景
{bundle.get("场景名称", bundle.title)}

## 当前状态
- technical_validation: pending
- content_validation: pending
- next_action: 待补真实录制素材或继续补强 prompt

## 本轮生成物
- 02_工作包正文.md
- 03_Prompt包.md
- 04_录制计划.md
- 05_回审清单.md
- 06_结果差对比.md

## 备注
- 当前只代表工作台模板已生成，不代表最终样片已完成
"""


def write_workspace_from_brief(
    brief_path: pathlib.Path,
    workspace: pathlib.Path,
    force: bool,
) -> dict[str, object]:
    bundle = load_brief(brief_path)
    outputs = {
        "02_工作包正文.md": build_work_package_markdown(bundle),
        "03_Prompt包.md": build_prompt_pack_markdown(bundle),
        "04_录制计划.md": build_recording_plan_markdown(bundle),
        "05_回审清单.md": build_review_checklist_markdown(bundle),
    }
    created: list[str] = []
    for filename, content in outputs.items():
        path = workspace / filename
        _write_text(path, content, force=force)
        created.append(str(path))
    return {"status": "success", "created": created, "title": bundle.title}


def rewrite_recording_plan(
    workspace: pathlib.Path,
    force: bool,
) -> dict[str, object]:
    brief_path = workspace / "01_场景简报.md"
    bundle = load_brief(brief_path)
    output_path = workspace / "04_录制计划.md"
    _write_text(output_path, build_recording_plan_markdown(bundle), force=force)
    return {"status": "success", "output": str(output_path)}


def write_result_diff(
    workspace: pathlib.Path,
    output_path: pathlib.Path,
    force: bool,
) -> dict[str, object]:
    bundle = load_brief(workspace / "01_场景简报.md")
    _write_text(output_path, build_result_diff_markdown(bundle), force=force)
    return {"status": "success", "output": str(output_path)}


def write_execution_log(
    workspace: pathlib.Path,
    output_path: pathlib.Path,
    force: bool,
) -> dict[str, object]:
    bundle = load_brief(workspace / "01_场景简报.md")
    _write_text(output_path, build_execution_log_markdown(bundle), force=force)
    return {"status": "success", "output": str(output_path)}


def parser_with_force(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--force", action="store_true")
    return parser


def print_result(result: dict[str, object]) -> None:
    print(_json_result(**result))
