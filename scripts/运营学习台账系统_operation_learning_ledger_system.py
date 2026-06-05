#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent

LEDGER_DIR = Path("review_loop/learning_ledger")
README_PATH = LEDGER_DIR / "README.md"
METRIC_EVENT_LOG_PATH = LEDGER_DIR / "metric_event_log.jsonl"
EPISODE_VARIABLE_REGISTRY_PATH = LEDGER_DIR / "episode_variable_registry.json"
EPISODE_SIGNAL_SUMMARY_PATH = LEDGER_DIR / "episode_signal_summary.md"
OPERATION_LEARNING_MEMORY_PATH = LEDGER_DIR / "operation_learning_memory.md"
CURRENT_COPY_REVISION_HANDOFF_PATH = LEDGER_DIR / "current_copy_revision_handoff.md"
NEXT_EPISODE_BET_CARD_PATH = LEDGER_DIR / "next_episode_bet_card.md"
FIRST_CLOSED_LOOP_REPORT_PATH = LEDGER_DIR / "first_closed_loop_report.md"
LATEST_REPORT_JSON_PATH = LEDGER_DIR / "latest_operation_learning_report.json"
LATEST_REPORT_MD_PATH = LEDGER_DIR / "latest_operation_learning_report.md"
MANIFEST_PATH = LEDGER_DIR / "learning_ledger_manifest.json"

OPERATION_RECORDS_INDEX_PATH = Path("review_loop/operation_records_index.md")
COPY_REGISTRY_PATH = Path("review_loop/copy_iteration/copy_registry.json")

V003_SNAPSHOT_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_post_72h_pre_7d_snapshot.json"
)
V004_SNAPSHOT_PATH = Path(
    "review_loop/records/V004_全自动制作方式_public_ai_video_20260517/"
    "V004_interim_17h_snapshot.json"
)
V005_OPERATION_RECORD_PATH = Path(
    "review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/"
    "V005_发布后运营数据记录_post_publish_operation_record.md"
)
V005_SNAPSHOT_PATH = Path(
    "review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/"
    "V005_between_24h_and_72h_snapshot.json"
)
V005_STRUCTURE_MAP_PATH = Path("review_loop/copy_iteration/V005/V005_copy_structure_map.json")
V005_COPY_NOTES_PATH = Path("review_loop/copy_iteration/V005/V005_copy_notes.md")

REQUIRED_LEDGER_OUTPUTS = [
    README_PATH,
    METRIC_EVENT_LOG_PATH,
    EPISODE_VARIABLE_REGISTRY_PATH,
    EPISODE_SIGNAL_SUMMARY_PATH,
    OPERATION_LEARNING_MEMORY_PATH,
    CURRENT_COPY_REVISION_HANDOFF_PATH,
    NEXT_EPISODE_BET_CARD_PATH,
    FIRST_CLOSED_LOOP_REPORT_PATH,
    LATEST_REPORT_JSON_PATH,
    LATEST_REPORT_MD_PATH,
    MANIFEST_PATH,
]

V005_GOOD_METRICS = [
    "play_count",
    "like_count",
    "like_rate",
    "cover_click_rate",
    "recommendation_page",
]
V005_BAD_OR_WEAK_METRICS = [
    "average_watch_time",
    "completion_rate",
    "two_second_bounce_rate",
    "five_second_completion_rate",
    "favorite_rate",
]
V005_MISSING_METRICS = [
    "3s_retention",
    "profile_visit_count",
    "dm_count",
    "effective_dm_count",
    "effective_consult_count",
    "clear_need_customer_count",
]

METRIC_ALIASES = {
    "3s_retention": "three_second_retention",
}

SIGNAL_LAYERS = {
    "play_count": "traffic",
    "cover_click_rate": "traffic",
    "recommendation_page": "traffic",
    "average_watch_time": "retention",
    "completion_rate": "retention",
    "two_second_bounce_rate": "retention",
    "five_second_completion_rate": "retention",
    "3s_retention": "retention",
    "like_count": "interaction",
    "like_rate": "interaction",
    "favorite_rate": "value",
    "profile_visit_count": "lead",
    "dm_count": "lead",
    "effective_dm_count": "lead",
    "effective_consult_count": "commercial",
    "clear_need_customer_count": "commercial",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(root: Path, path: Path) -> str:
    return (root / path).read_text(encoding="utf-8")


def write_text(root: Path, path: Path, content: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def load_json(root: Path, path: Path) -> dict[str, Any]:
    return json.loads(read_text(root, path))


def write_json(root: Path, path: Path, payload: dict[str, Any]) -> None:
    write_text(root, path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace(",", "")
    digits = []
    started = False
    for char in text:
        if char.isdigit() or char in ".-":
            digits.append(char)
            started = True
        elif started:
            break
    if not digits:
        return None
    try:
        return float("".join(digits))
    except ValueError:
        return None


def metric_value(snapshot: dict[str, Any], metric_name: str) -> dict[str, Any]:
    key = METRIC_ALIASES.get(metric_name, metric_name)

    def walk(node: Any) -> dict[str, Any] | None:
        if isinstance(node, dict):
            if key in node:
                raw = node[key]
                if isinstance(raw, dict) and "value" in raw:
                    return raw
                return {
                    "value": raw,
                    "source_status": "extracted_from_structured_snapshot",
                    "confidence": "medium",
                    "source_screenshot_path": None,
                }
            for value in node.values():
                found = walk(value)
                if found is not None:
                    return found
        return None

    found = walk(snapshot)
    if found is None:
        return {
            "value": None,
            "source_status": "missing",
            "confidence": "none",
            "source_screenshot_path": None,
        }
    return found


def metric_unit(metric_name: str, value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        if "%" in value:
            return "%"
        if "秒" in value:
            return "秒"
    if metric_name.endswith("_rate") or metric_name in {
        "cover_click_rate",
        "completion_rate",
        "two_second_bounce_rate",
        "five_second_completion_rate",
        "recommendation_page",
    }:
        return "%"
    if metric_name.endswith("_count") or metric_name == "play_count":
        return "count"
    return ""


def threshold_reference(metric_name: str) -> str:
    mapping = {
        "play_count": "小样本阶段基础测试流量门槛仍看 7d 6000；当前只看入口信号。",
        "like_count": "点赞是认可弱信号，不等于需求成立。",
        "like_rate": "点赞率上升是互动正信号，不等于内容通过。",
        "cover_click_rate": "封面点击率用于判断题眼和包装是否打开入口。",
        "recommendation_page": "推荐页占比高说明平台给入口，不等于充分验证。",
        "average_watch_time": "平均观看用于判断承接和中段价值是否稳住。",
        "completion_rate": "完播率低说明全片承接弱。",
        "two_second_bounce_rate": "2s 跳出用于判断第一眼和 0-3 秒承接。",
        "five_second_completion_rate": "5s 完播用于判断 3-8 秒承接。",
        "favorite_rate": "收藏率用于判断可复用价值信号。",
        "3s_retention": "3s 留存缺失时不能精确定位开头短板。",
        "profile_visit_count": "主页访问用于判断账号兴趣承接。",
        "dm_count": "私信用于需求信号观察，需质量评分。",
        "effective_dm_count": "有效私信才可进入需求层判断。",
        "effective_consult_count": "有效咨询是商业层前置信号。",
        "clear_need_customer_count": "清晰需求客户才可观察服务/工作包机会。",
    }
    return mapping.get(metric_name, "")


def why_it_matters(metric_name: str) -> str:
    mapping = {
        "play_count": "判断题眼、封面和平台入口是否打开。",
        "like_count": "判断观众对表达的轻认可。",
        "like_rate": "避免只看绝对点赞数，观察触达后的认可比例。",
        "cover_click_rate": "直接服务下一期是否保留包装题眼。",
        "recommendation_page": "确认播放提升是否主要来自推荐入口。",
        "average_watch_time": "判断大题眼后是否真的留住观众。",
        "completion_rate": "判断全片是否过长或承接断裂。",
        "two_second_bounce_rate": "判断第一眼和前 0-3 秒是否接住观众。",
        "five_second_completion_rate": "判断 3-8 秒是否给出继续看的理由。",
        "favorite_rate": "判断内容有没有可复用价值。",
        "3s_retention": "缺失会降低开头诊断置信度。",
        "profile_visit_count": "缺失会阻断账号承接判断。",
        "dm_count": "缺失会阻断需求信号判断。",
        "effective_dm_count": "缺失会阻断有效需求判断。",
        "effective_consult_count": "缺失会阻断咨询质量判断。",
        "clear_need_customer_count": "缺失会阻断商业验证判断。",
    }
    return mapping.get(metric_name, "用于运营学习台账留痕。")


def build_event(
    *,
    video_id: str,
    snapshot_label: str,
    review_window: str,
    metric_name: str,
    metric_info: dict[str, Any],
    source_path: Path,
    signal_direction: str,
    created_at: str,
) -> dict[str, Any]:
    value = metric_info.get("value")
    source_status = metric_info.get("source_status", "unknown")
    confidence = metric_info.get("confidence", "medium")
    if value is None and source_status not in {"uncertain_need_human_check", "not_applicable"}:
        source_status = "missing"
        confidence = "none"
    return {
        "event_id": f"{video_id}_{snapshot_label}_{metric_name}",
        "video_id": video_id,
        "snapshot_label": snapshot_label,
        "review_window": review_window,
        "metric_name": metric_name,
        "metric_value": value,
        "metric_unit": metric_unit(metric_name, value),
        "source_status": source_status,
        "source_path": rel(source_path),
        "confidence": confidence,
        "signal_direction": signal_direction,
        "signal_layer": SIGNAL_LAYERS.get(metric_name, "neutral"),
        "threshold_reference": threshold_reference(metric_name),
        "why_it_matters": why_it_matters(metric_name),
        "created_at": created_at,
    }


def build_metric_events(root: Path, created_at: str) -> list[dict[str, Any]]:
    v003 = load_json(root, V003_SNAPSHOT_PATH)
    v004 = load_json(root, V004_SNAPSHOT_PATH)
    v005 = load_json(root, V005_SNAPSHOT_PATH)
    events: list[dict[str, Any]] = []

    events.append(
        build_event(
            video_id="V001",
            snapshot_label="historical_incomplete",
            review_window="historical_reference_only",
            metric_name="historical_data_completeness",
            metric_info={
                "value": None,
                "source_status": "historical_incomplete_no_structured_snapshot",
                "confidence": "low",
            },
            source_path=OPERATION_RECORDS_INDEX_PATH,
            signal_direction="missing",
            created_at=created_at,
        )
    )
    events.append(
        build_event(
            video_id="V002",
            snapshot_label="policy_limited_abnormal_sample",
            review_window="abnormal_policy_limited",
            metric_name="normal_distribution_attribution",
            metric_info={
                "value": "excluded",
                "source_status": "policy_limited_abnormal_sample",
                "confidence": "high",
            },
            source_path=OPERATION_RECORDS_INDEX_PATH,
            signal_direction="neutral",
            created_at=created_at,
        )
    )

    for video_id, snapshot, path, metric_names in [
        (
            "V003",
            v003,
            V003_SNAPSHOT_PATH,
            ["play_count", "average_watch_time", "two_second_bounce_rate", "five_second_completion_rate", "favorite_rate"],
        ),
        (
            "V004",
            v004,
            V004_SNAPSHOT_PATH,
            ["play_count", "average_watch_time", "two_second_bounce_rate", "five_second_completion_rate", "favorite_rate"],
        ),
    ]:
        for metric_name in metric_names:
            info = metric_value(snapshot, metric_name)
            direction = "weak" if metric_name in {"play_count", "average_watch_time"} else "bad"
            events.append(
                build_event(
                    video_id=video_id,
                    snapshot_label=snapshot["snapshot_label"],
                    review_window=snapshot["review_window"],
                    metric_name=metric_name,
                    metric_info=info,
                    source_path=path,
                    signal_direction=direction,
                    created_at=created_at,
                )
            )

    for metric_name in V005_GOOD_METRICS:
        events.append(
            build_event(
                video_id="V005",
                snapshot_label=v005["snapshot_label"],
                review_window=v005["review_window"],
                metric_name=metric_name,
                metric_info=metric_value(v005, metric_name),
                source_path=V005_SNAPSHOT_PATH,
                signal_direction="good",
                created_at=created_at,
            )
        )
    for metric_name in V005_BAD_OR_WEAK_METRICS:
        events.append(
            build_event(
                video_id="V005",
                snapshot_label=v005["snapshot_label"],
                review_window=v005["review_window"],
                metric_name=metric_name,
                metric_info=metric_value(v005, metric_name),
                source_path=V005_SNAPSHOT_PATH,
                signal_direction="bad" if metric_name != "favorite_rate" else "weak",
                created_at=created_at,
            )
        )
    for metric_name in V005_MISSING_METRICS:
        events.append(
            build_event(
                video_id="V005",
                snapshot_label=v005["snapshot_label"],
                review_window=v005["review_window"],
                metric_name=metric_name,
                metric_info=metric_value(v005, metric_name),
                source_path=V005_SNAPSHOT_PATH,
                signal_direction="missing",
                created_at=created_at,
            )
        )
    events.append(
        build_event(
            video_id="V005",
            snapshot_label=v005["snapshot_label"],
            review_window=v005["review_window"],
            metric_name="whether_V005_should_replace_current_operation_target",
            metric_info={
                "value": None,
                "source_status": "uncertain_need_human_check",
                "confidence": "low",
            },
            source_path=V005_SNAPSHOT_PATH,
            signal_direction="uncertain",
            created_at=created_at,
        )
    )
    return events


def build_episode_registry(root: Path, created_at: str) -> dict[str, Any]:
    copy_registry = load_json(root, COPY_REGISTRY_PATH)
    copy_records = {
        item["video_id"]: item for item in copy_registry.get("records", []) if "video_id" in item
    }
    return {
        "schema": "operation_learning_ledger.episode_variable_registry.v1",
        "generated_at": created_at,
        "source_files": {
            "operation_records_index": rel(OPERATION_RECORDS_INDEX_PATH),
            "copy_registry": rel(COPY_REGISTRY_PATH),
        },
        "markdown_field_extraction_policy": {
            "structured_snapshot_json_wins": True,
            "markdown_extract_may_not_override_structured_json": True,
            "V001_markdown_extract_disabled": True,
        },
        "episodes": [
            {
                "video_id": "V001",
                "role": "historical_reference_only",
                "action": "mark_historical_incomplete",
                "deep_backfill": False,
                "normal_attribution_eligible": False,
                "markdown_metric_extract_allowed": False,
                "learning_use": "历史边界和旧流程对照，不生成假指标。",
            },
            {
                "video_id": "V002",
                "role": "policy_limited_abnormal_sample",
                "action": "record_interest_signal_but_exclude_from_normal_attribution",
                "deep_backfill": False,
                "normal_attribution_eligible": False,
                "normal_attribution_excluded_reason": "policy_limited_abnormal_sample",
                "copy_id": copy_records.get("V002", {}).get("copy_id", "V002_copy_v1"),
                "learning_use": "可提示兴趣和平台风险表达，不能当正常自然分发样本归因。",
            },
            {
                "video_id": "V003",
                "role": "previous_current_operation_target",
                "action": "use_existing_post_72h_pre_7d_snapshot",
                "deep_backfill": False,
                "copy_id": copy_records.get("V003", {}).get("copy_id", "V003_copy_v1"),
                "snapshot_path": rel(V003_SNAPSHOT_PATH),
                "normal_attribution_eligible": True,
                "attribution_confidence": "low",
                "known_signal": "留存相对 V005 更好但入口弱，仍缺 7d 和需求侧字段。",
            },
            {
                "video_id": "V004",
                "role": "latest_sample_pre_24h_before_V005",
                "action": "use_existing_interim_17h_snapshot",
                "deep_backfill": False,
                "copy_id": copy_records.get("V004", {}).get("copy_id", "V004_copy_v1"),
                "snapshot_path": rel(V004_SNAPSHOT_PATH),
                "normal_attribution_eligible": True,
                "attribution_confidence": "low",
                "known_signal": "早期入口弱，收藏为 0，不足以判方向失败。",
            },
            {
                "video_id": "V005",
                "role": "latest_sent_video_current_learning_sample",
                "action": "use_existing_between_24h_and_72h_snapshot_and_raw_copy",
                "deep_backfill": False,
                "copy_id": "V005_copy_v1",
                "primary_variable_guess": "topic_eye_and_packaging",
                "attribution_confidence": "medium_low",
                "known_changed_elements": [
                    "Codex 赚钱题眼",
                    "封面文字：还是不赚钱",
                    "真实三项目经历",
                    "诚实边界：Codex 解决执行成本，不是赚钱结果",
                ],
                "known_effective_signals": [
                    "播放显著提升",
                    "点赞绝对量和点赞率提升",
                    "封面点击率出现明显信号",
                ],
                "known_failed_or_weak_signals": [
                    "2s 跳出仍高",
                    "平均观看只有 8 秒",
                    "5s 完播下降",
                    "收藏率低于 V003",
                ],
                "not_allowed_conclusions": [
                    "不能写内容通过",
                    "不能写方向成立",
                    "不能写商业验证成立",
                ],
                "human_contribution_note": "当前最强有效信号主要来自用户自己的选题 / 题眼 / 包装判断，系统必须捕捉并机制化，而不是把功劳归给自动复盘系统。",
                "snapshot_path": rel(V005_SNAPSHOT_PATH),
                "structure_map_path": rel(V005_STRUCTURE_MAP_PATH),
                "copy_notes_path": rel(V005_COPY_NOTES_PATH),
            },
        ],
    }


def render_readme() -> str:
    return """# 运营学习台账 learning_ledger

复盘不是报告终点。

复盘必须产出下一期创作判断。

每次复盘后，ChatGPT 写文案前必须读取：

1. `current_copy_revision_handoff.md`
2. `next_episode_bet_card.md`
3. `operation_learning_memory.md`
4. 最新一期 `copy_structure_map`

## 本目录解决的问题

- 把数据回填从描述性记录推进到可统计学习台账。
- 把单期变量和指标好坏留痕。
- 把跨期学习写成 ChatGPT 文案前的必读输入。
- 把下一期创作下注从泛泛建议变成可验证假设。

## 硬边界

- 不深度补旧截图。
- 不用 Markdown 粗抽字段覆盖结构化 JSON。
- 不生成下一期完整正式文案。
- 不生成下一条正式视频执行 prompt。
- 不推进内容通过、方向成立或商业验证成立。
"""


def render_episode_signal_summary() -> str:
    return """# 单期信号总结 episode_signal_summary

## V001

### 当前角色
- 历史运营样本，只作为旧阶段参考。

### 当前处理
- 标记 `historical_incomplete`。
- 不深度补旧截图。
- 不从 Markdown 粗抽字段生成假指标。

### 不能下的结论
- 不能写内容通过。
- 不能写方向成立。
- 不能写商业验证成立。

## V002

### 当前角色
- `policy_limited_abnormal_sample`。

### 好信号
- 异常样本中存在兴趣信号，可作为平台风险和题眼观察材料。

### 不能下的结论
- 不能进入正常自然分发归因。
- 不能写内容失败。
- 不能把高收藏写成内容通过。

## V003

### 好信号
- 收藏率相对 V005 更高，说明可复用价值曾出现小样本信号。
- 5s 完播和平均观看好于 V005。

### 坏信号
- 播放入口弱。
- 72h 后没有明显二次增长。
- 评论、私信、有效咨询等需求侧字段缺失。

### 初步解释
- V003 更像价值表达有一点信号，但题眼、封面或开头入口没有打开。

## V004

### 好信号
- 推荐页仍给过入口。

### 坏信号
- 播放弱。
- 收藏为 0。
- 仍是 pre_24h 早期样本，不能判方向失败。

### 初步解释
- V004 可作为开头复盘类表达的早期弱样本，不适合作为当前下注主依据。

## V005

### 好信号
- 播放量明显高于 V003 / V004。
- 点赞数和点赞率明显提升。
- 封面点击率出现明显正信号。
- 推荐页占比高，说明平台给了更大的初始推荐入口。

### 坏信号
- 平均观看只有 8 秒。
- 2s 跳出高于 V003 / V004。
- 5s 完播低于 V003 / V004。
- 收藏率低于 V003，说明可复用价值或中段承接还没稳。

### 缺失信号
- 3s 留存缺失。
- 主页访问缺失。
- 私信 / 有效咨询 / 清晰需求客户缺失。

### 初步解释
- V005 更像“题眼和封面包装打开流量”，不是内容承接全面变好。
- 当前不能直接说方向成立，只能说 Codex + 赚钱 / 普通人题眼值得保留并继续验证。
- 当前最强有效信号主要来自用户自己的选题、题眼和包装判断，系统必须把它机制化。

### 下次保留
- 保留 Codex + 赚钱 / 普通人 / 真实项目经验这个外层题眼。
- 保留诚实边界：不能替你赚钱，但能降低试错成本。

### 下次只优先改
- 前 0-8 秒承接。
- 把大题眼压到一个具体证明场景，例如剪辑成本 / API 成本 / 数据复盘成本中的一个。

### 不能下的结论
- 不能写内容通过。
- 不能写商业验证成立。
- 不能写方向成立。
"""


def render_operation_learning_memory() -> str:
    return """# 运营学习记忆

## 已观察到的低置信度有效信号

- “Codex + 普通人赚钱”比“流程优化 / 本地文件 / 全自动制作方式”更能打开播放入口。
- 用户自己提出的 V005 选题和文案带来了目前最明显的播放提升。
- 说明用户的新媒体题眼直觉是当前系统必须捕捉和放大的关键资产。

## 已观察到的问题

- 大题眼能拉人，但如果前 8 秒没有快速落到具体证明场景，留存会掉。
- 播放提升不等于收藏提升。
- 点赞提升不等于需求成立。
- 数据回填不进入文案交接，就不会形成正反馈循环。

## ChatGPT 必须承担的责任

- 不能只解释数据。
- 必须在下一期选题和文案前给出建设性下注。
- 必须指出：押什么、不押什么、为什么、验证什么。
- 必须把用户自己的有效内容直觉机制化，而不是用流程把它磨平。

## 下一次文案必须读取

- `review_loop/learning_ledger/next_episode_bet_card.md`
- `review_loop/learning_ledger/current_copy_revision_handoff.md`
- `review_loop/learning_ledger/episode_signal_summary.md`
- `review_loop/copy_iteration/V005/V005_copy_structure_map.json`
"""


def render_next_episode_bet_card() -> str:
    return """# 下一期创作下注卡 next_episode_bet_card

## 1. 当前下注结论

下一期不换大方向，不重新做泛 Codex 教程。

建议保留：

- Codex
- 普通人赚钱
- 真实项目经验
- 诚实边界：不能替你赚钱，但能降低试错成本

下一期只改一个主变量：

- 把大题眼压到一个具体证明场景
- 优先验证前 0-8 秒承接

## 2. 为什么这样下注

V005 好信号来自题眼和包装：

- 播放上升
- 点赞上升
- 封面点击出现信号
- 平台给了更大推荐入口

V005 坏信号来自承接：

- 平均观看短
- 2s 跳出高
- 5s 完播弱
- 收藏率不强

所以不能换大方向，而要把下一期收窄到具体场景。

## 3. 下一期候选方向排序

### A. 主推方向：Codex 怎么降低剪辑成本

选择理由：

- 普通人最容易理解剪辑成本。
- 和用户当前视频工厂项目强相关。
- 有真实画面证据。
- 能承接“不是直接赚钱，而是降低执行成本”。

### B. 备选方向：Codex 怎么用 API 降低生成成本

选择理由：

- 更偏技术和成本拆解。
- 适合放在第二条，不适合作为下一条首选。
- 观众门槛比剪辑成本高。

### C. 延后方向：Codex 怎么做电商自动化

选择理由：

- 太容易被理解成赚钱教程。
- 当前商业和需求侧数据不足。
- 等建立信任后再讲。

## 4. 下一期不改什么

- 不改目标用户。
- 不改“普通人使用 AI 工具”的大方向。
- 不改诚实边界。
- 不同时讲剪辑、API、电商、vlog。
- 不做完整教程合集。
- 不把 Codex 说成赚钱机器。

## 5. 下一期文案必须解决的问题

开头 0-3 秒：

- 必须比 V005 更快落到具体成本。
- 不能停留在“Codex 能不能赚钱”的大问题。

3-8 秒承接：

- 必须告诉观众：这一条只讲一个具体场景。
- 必须让观众知道继续看能得到什么。

中段：

- 必须展示真实成本下降路径。
- 不能泛泛讲“提高效率”。

## 6. 发布后验证指标

如果下一期是“剪辑成本”方向，重点看：

- 2s 跳出是否低于 V005 的 54.68%
- 5s 完播是否高于 V005 的 22.45%
- 平均观看是否高于 V005 的 8 秒
- 收藏率是否高于 V005 的 0.79%
- 评论是否出现“想看怎么做 / 怎么用 / 求流程”类需求

## 7. 输赢判断

如果播放继续高，但留存仍低：

- 说明题眼仍有效，但开头承接仍失败。

如果留存提升但收藏不提升：

- 说明表达更顺了，但具体价值还不够可复用。

如果收藏提升：

- 说明具体场景开始产生实用价值信号。

如果评论 / 私信出现：

- 进入需求信号观察，但不得直接写商业验证成立。
"""


def render_current_copy_revision_handoff() -> str:
    return """# 当前文案修改交接卡 current_copy_revision_handoff

## 当前最新可学习样本

- latest_learning_sample: V005
- data_window: between_24h_and_72h_snapshot
- confidence: low_to_medium
- human_review_required: true

## 本轮保留项

- Codex + 普通人赚钱的题眼
- 真实项目经验
- 诚实边界
- 不是赚钱机器，而是降低执行成本

## 本轮只允许优先改

- 前 0-8 秒承接
- 将大题眼压缩到一个具体证明场景
- 主推：Codex 降低剪辑成本

## 本轮不要改

- 不换目标用户
- 不换大方向
- 不改成纯教程
- 不改成电商赚钱教程
- 不同时讲多个场景
- 不生成完整正式文案

## ChatGPT 写下一版文案时必须做到

1. 先给创作下注，不要只给泛泛建议。
2. 明确押什么，不押什么。
3. 明确下一条只验证一个主变量。
4. 明确这条继承 V005 的什么有效信号。
5. 明确这条修复 V005 的什么失败信号。
6. 明确发布后看哪些指标判断输赢。

## 必须避免的误读

- V005 播放高，不等于内容通过。
- V005 点赞高，不等于需求成立。
- V005 收藏率低，说明可复用价值仍待提升。
- V005 留存弱，说明前 8 秒承接必须优化。
"""


def render_first_closed_loop_report(created_at: str) -> str:
    return f"""# 第一次运营复盘正反馈闭环报告 first_closed_loop_report

## 本轮结论

本轮不是旧视频数据回填，也不是下一期正式文案生成。

本轮完成的是第一次复盘正反馈闭环整理：

```text
数据回填
-> 指标好坏留痕
-> 单期变量登记
-> 跨期学习台账
-> 下一期创作下注卡
-> 文案层交接卡
-> ChatGPT 写下一期文案前强制读取
-> 下一期发布后再验证下注是否成立
```

## included_episodes

- V001: historical_reference_only / historical_incomplete
- V002: policy_limited_abnormal_sample / excluded_from_normal_attribution
- V003: previous_current_operation_target / post_72h_pre_7d_snapshot
- V004: latest_sample_pre_24h_before_V005 / interim_17h_snapshot
- V005: latest_sent_video_current_learning_sample / between_24h_and_72h_snapshot

## 为什么这是第一次闭环

- 旧系统能生成复盘报告，但没有强制输出下一期创作下注。
- 旧文案迭代报告仍停在 V003，没有把 V005 的题眼与承接信号接入文案层。
- 本轮首次把 V001-V005 转成可持续学习台账，并产出 `next_episode_bet_card` 与 `current_copy_revision_handoff`。

## V005 学习结论

- 好信号主要来自用户自己的选题、题眼和包装判断：Codex + 普通人赚钱 + 真实项目经验 + 诚实边界。
- 坏信号主要来自前 0-8 秒承接和具体价值落点不足。
- 当前只允许低置信度创作准备，不允许内容通过、方向成立或商业验证成立。

## 本轮没有做什么

- 没有深度补旧截图。
- 没有重读所有旧视频 OCR。
- 没有生成下一期完整正式文案。
- 没有生成下一条正式视频执行 prompt。
- 没有推进任何 forbidden status。

## generated_at

- {created_at}
"""


def build_latest_report_json(
    created_at: str, events: list[dict[str, Any]], registry: dict[str, Any]
) -> dict[str, Any]:
    v005_events = [event for event in events if event["video_id"] == "V005"]
    return {
        "schema": "operation_learning_ledger.latest_report.v1",
        "generated_at": created_at,
        "status": "learning_ledger_generated_pending_git_sync",
        "closed_loop_artifacts_generated": True,
        "closed_loop_completion_claim_allowed_by_artifacts": closed_loop_completion_status(ROOT)[
            "completed_allowed"
        ]
        if (ROOT / NEXT_EPISODE_BET_CARD_PATH).exists()
        else False,
        "included_episodes": ["V001", "V002", "V003", "V004", "V005"],
        "latest_learning_sample": "V005",
        "V005_learning_result": {
            "good_signals": [
                "play_count=1514",
                "like_count=50",
                "like_rate=3.30%",
                "cover_click_rate=7.14%",
                "recommendation_page=96.1%",
            ],
            "bad_signals": [
                "average_watch_time=8秒",
                "completion_rate=0.62%",
                "two_second_bounce_rate=54.68%",
                "five_second_completion_rate=22.45%",
                "favorite_rate=0.79%",
            ],
            "missing_signals": V005_MISSING_METRICS,
            "uncertain_signals": [
                "whether_V005_should_replace_current_operation_target",
                "exact_review_window_from_platform_page",
            ],
            "preliminary_learning": "V005 更像题眼和封面包装打开流量，不是内容承接全面变好；下一期保留大题眼，只改前 0-8 秒承接并压到具体证明场景。",
            "not_allowed_conclusions": [
                "不能写内容通过",
                "不能写方向成立",
                "不能写商业验证成立",
            ],
        },
        "ChatGPT_creative_judgment_responsibility": {
            "must_output_next_time": [
                "押什么",
                "不押什么",
                "为什么",
                "验证什么",
                "继承 V005 哪个有效信号",
                "修复 V005 哪个失败信号",
            ],
            "must_not_output_only": "泛泛建议或纯数据解释",
            "required_inputs": [
                rel(NEXT_EPISODE_BET_CARD_PATH),
                rel(CURRENT_COPY_REVISION_HANDOFF_PATH),
                rel(OPERATION_LEARNING_MEMORY_PATH),
                rel(V005_STRUCTURE_MAP_PATH),
            ],
        },
        "event_count": len(events),
        "V005_event_count": len(v005_events),
        "episode_registry_count": len(registry["episodes"]),
    }


def render_latest_report_md(created_at: str) -> str:
    return f"""# 最新运营学习报告 latest_operation_learning_report

## status

- learning_ledger_generated_pending_git_sync
- generated_at: {created_at}

## 核心修复

- V005 已进入最新学习样本。
- V001-V005 已进入学习台账。
- `next_episode_bet_card` 已生成。
- `current_copy_revision_handoff` 已生成。
- ChatGPT 下一次写文案前必须先输出创作下注，不能只解释数据。

## 下一期低置信度下注

- 不换大方向。
- 保留 Codex + 普通人赚钱 + 真实项目经验 + 诚实边界。
- 只改一个主变量：前 0-8 秒承接。
- 主推方向：Codex 怎么降低剪辑成本。

## 状态边界

- 不生成下一期完整正式文案。
- 不生成下一条正式视频执行 prompt。
- 不推进内容通过。
- 不推进方向成立。
- 不推进商业验证成立。
"""


def build_manifest(created_at: str) -> dict[str, Any]:
    return {
        "schema": "operation_learning_ledger.manifest.v1",
        "generated_at": created_at,
        "ledger_dir": rel(LEDGER_DIR),
        "required_outputs": [rel(path) for path in REQUIRED_LEDGER_OUTPUTS],
        "required_next_copy_inputs": [
            rel(NEXT_EPISODE_BET_CARD_PATH),
            rel(CURRENT_COPY_REVISION_HANDOFF_PATH),
            rel(OPERATION_LEARNING_MEMORY_PATH),
            rel(V005_STRUCTURE_MAP_PATH),
        ],
        "machine_readable_outputs": [
            rel(METRIC_EVENT_LOG_PATH),
            rel(EPISODE_VARIABLE_REGISTRY_PATH),
            rel(LATEST_REPORT_JSON_PATH),
            rel(MANIFEST_PATH),
        ],
        "markdown_outputs": [
            rel(README_PATH),
            rel(EPISODE_SIGNAL_SUMMARY_PATH),
            rel(OPERATION_LEARNING_MEMORY_PATH),
            rel(CURRENT_COPY_REVISION_HANDOFF_PATH),
            rel(NEXT_EPISODE_BET_CARD_PATH),
            rel(FIRST_CLOSED_LOOP_REPORT_PATH),
            rel(LATEST_REPORT_MD_PATH),
        ],
        "closed_loop_completion_requirements": {
            "metric_event_log": rel(METRIC_EVENT_LOG_PATH),
            "episode_variable_registry": rel(EPISODE_VARIABLE_REGISTRY_PATH),
            "next_episode_bet_card": rel(NEXT_EPISODE_BET_CARD_PATH),
            "current_copy_revision_handoff": rel(CURRENT_COPY_REVISION_HANDOFF_PATH),
            "operation_learning_memory": rel(OPERATION_LEARNING_MEMORY_PATH),
        },
        "not_generated": [
            "formal_next_video_execution_prompt",
            "full_next_episode_script",
        ],
    }


def closed_loop_completion_status(root: Path = ROOT) -> dict[str, Any]:
    required = [
        METRIC_EVENT_LOG_PATH,
        EPISODE_VARIABLE_REGISTRY_PATH,
        NEXT_EPISODE_BET_CARD_PATH,
        CURRENT_COPY_REVISION_HANDOFF_PATH,
        OPERATION_LEARNING_MEMORY_PATH,
    ]
    missing = [rel(path) for path in required if not (root / path).exists()]
    return {
        "completed_allowed": not missing,
        "blocked_reason": "missing_required_learning_artifacts" if missing else "",
        "missing_required_outputs": missing,
    }


def run_operation_learning_ledger_system(root: Path = ROOT) -> dict[str, Any]:
    created_at = now_utc()
    read_text(root, OPERATION_RECORDS_INDEX_PATH)
    load_json(root, COPY_REGISTRY_PATH)
    read_text(root, V005_OPERATION_RECORD_PATH)
    load_json(root, V005_SNAPSHOT_PATH)
    load_json(root, V005_STRUCTURE_MAP_PATH)
    read_text(root, V005_COPY_NOTES_PATH)

    events = build_metric_events(root, created_at)
    registry = build_episode_registry(root, created_at)

    write_text(root, README_PATH, render_readme())
    write_text(
        root,
        METRIC_EVENT_LOG_PATH,
        "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in events),
    )
    write_json(root, EPISODE_VARIABLE_REGISTRY_PATH, registry)
    write_text(root, EPISODE_SIGNAL_SUMMARY_PATH, render_episode_signal_summary())
    write_text(root, OPERATION_LEARNING_MEMORY_PATH, render_operation_learning_memory())
    write_text(root, NEXT_EPISODE_BET_CARD_PATH, render_next_episode_bet_card())
    write_text(root, CURRENT_COPY_REVISION_HANDOFF_PATH, render_current_copy_revision_handoff())
    write_text(root, FIRST_CLOSED_LOOP_REPORT_PATH, render_first_closed_loop_report(created_at))
    latest_json = build_latest_report_json(created_at, events, registry)
    write_json(root, LATEST_REPORT_JSON_PATH, latest_json)
    write_text(root, LATEST_REPORT_MD_PATH, render_latest_report_md(created_at))
    manifest = build_manifest(created_at)
    write_json(root, MANIFEST_PATH, manifest)

    return {
        "status": "generated",
        "ledger_dir": rel(LEDGER_DIR),
        "created_at": created_at,
        "event_count": len(events),
        "outputs": [rel(path) for path in REQUIRED_LEDGER_OUTPUTS],
        "completion_status": closed_loop_completion_status(root),
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate operation learning ledger outputs.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    parse_args(argv)
    result = run_operation_learning_ledger_system(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
