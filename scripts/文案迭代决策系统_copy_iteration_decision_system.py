#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent

COPY_DIR = Path("review_loop/copy_iteration")
V003_DIR = COPY_DIR / "V003"

COPY_REGISTRY_PATH = COPY_DIR / "copy_registry.json"
LATEST_REPORT_JSON = COPY_DIR / "latest_copy_iteration_report.json"
LATEST_REPORT_MD = COPY_DIR / "latest_copy_iteration_report.md"

V003_RAW_PATH = V003_DIR / "V003_copy_v1_raw.md"
V003_RECORD_PATH = V003_DIR / "V003_copy_v1_record.json"
V003_STRUCTURE_PATH = V003_DIR / "V003_copy_structure_map.json"
V003_DECISION_PATH = V003_DIR / "V003_copy_iteration_decision.json"
V003_BRIEF_PATH = V003_DIR / "V003_next_copy_revision_brief.md"

OPERATION_REPORT_PATH = Path("review_loop/decision_engine/latest_operation_decision_report.json")
FINAL_USER_OPERATION_RESULT_PATH = Path("review_loop/decision_engine/final_user_operation_result.md")
V003_OPERATION_RECORD_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_发布后灰度数据记录_post_publish_gray_test_record.md"
)
V003_DATA_SNAPSHOT_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_早期数据快照_early_interim_snapshot.json"
)
V003_OPERATION_DECISION_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_operation_decision_result.md"
)

SCRIPT_PATH = Path("scripts/文案迭代决策系统_copy_iteration_decision_system.py")

RAW_COPY = """第三期
别再让ai给你定kpi了。播放多少、点赞多少、克资多少，看着很完整，但大多数时候没用，因为这些数字不会告诉你下一条到底该改标题，还是改开头，还是改中段结构。我一开始也这样问，帮视频工厂定个目标，最好有播放、点赞和克资。第一版确实很全，北极星目标、阶段目标、指标数、刻字定义都有，但我看完觉得不对，他还是在回答我要追哪些数字。我真正需要的是数据回来以后，下一轮该改哪里。所以我又追问，让ai设计一套目标驱动的数据飞轮，每期发布后，根据播放、留存、收藏、评论、私信和克兹，判断下一期只改哪个变量，这次结果才像个判断系统。播放和留存是触达，点赞和收藏是认可，评论和追问是互动。但私信也不能全算克资，要看他有没有说清楚任务场景和想要的结果。所以，目标不是kpi表，真正有用的目标是逼你回答三件事哪一层出了问题，下一条只改哪个变量，改完看哪个指标。没有这套判断，你每轮都在动，却不知道哪一步起作用。播放是入口，收藏是认可，私信要评分，每条只改一个主变量，目标清楚了，动作才不会乱，复盘清楚了，下一步才会浮出来。

"""

PROBLEM_LAYERS = [
    "opening_packaging",
    "bridge_3_8s",
    "middle_structure",
    "evidence_expression",
    "tone_and_language",
    "topic_angle",
    "target_audience",
]

FORBIDDEN_STATUS_PATTERNS = {
    "content_validation_advanced": ["content_validation = passed", "content_validation: passed"],
    "send_ready_advanced": ["send_ready = true", "send_ready: true"],
    "current_data_goal_anchor_ready": ["current_data_goal_anchor ready", "anchor_instance_status: \"ready\""],
    "next_formal_video_execution_prompt_generated": [
        "正式下一条视频执行 prompt 已生成",
        "next_formal_video_execution_prompt_generated: true",
    ],
    "target_audience_changed": ["allow_target_audience_change\": true"],
    "topic_direction_changed": ["allow_topic_direction_change\": true", "core_topic_direction changed"],
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
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def metric_value(operation_report: dict[str, Any], metric_name: str) -> Any:
    v003 = next(record for record in operation_report["records_processed"] if record["video_id"] == "V003")
    metric = v003.get("normalized_metrics", {}).get(metric_name, {})
    return metric.get("value")


def metric_number(operation_report: dict[str, Any], metric_name: str) -> float | None:
    v003 = next(record for record in operation_report["records_processed"] if record["video_id"] == "V003")
    metric = v003.get("normalized_metrics", {}).get(metric_name, {})
    value = metric.get("percent_value")
    if value is None:
        value = metric.get("numeric_value")
    return float(value) if isinstance(value, (int, float)) else None


def ensure_raw_copy(root: Path) -> None:
    raw_path = root / V003_RAW_PATH
    if raw_path.exists():
        existing = raw_path.read_text(encoding="utf-8")
        if existing != RAW_COPY:
            if existing.rstrip("\n") == RAW_COPY.rstrip("\n"):
                raw_path.write_text(RAW_COPY, encoding="utf-8")
                return
            raise RuntimeError("V003 raw copy exists but does not match locked source text")
        return
    write_text(root, V003_RAW_PATH, RAW_COPY)


def build_copy_record() -> dict[str, Any]:
    suspected_typos = [
        {
            "original_text": "克资",
            "suspected_normalized_text": "客资",
            "note": "疑似“客资”误写；raw 原文保留，不在 raw 中改写。",
            "action": "mark_only_do_not_modify_raw",
        },
        {
            "original_text": "刻字定义",
            "suspected_normalized_text": "客资定义",
            "note": "结合上下文疑似“客资定义”误写；raw 原文保留。",
            "action": "mark_only_do_not_modify_raw",
        },
        {
            "original_text": "克兹",
            "suspected_normalized_text": "客资",
            "note": "疑似“客资”误写；raw 原文保留。",
            "action": "mark_only_do_not_modify_raw",
        },
    ]
    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V003_RAW_PATH),
        "linked_operation_record": rel(V003_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V003_DATA_SNAPSHOT_PATH),
        "linked_operation_decision_report": rel(V003_OPERATION_DECISION_PATH),
        "copy_quality_notes": [
            "开头直接进入 KPI 概念，真实数据冲突出现得不够早。",
            "前 3-8 秒承接没有先交代观众为什么要继续看。",
            "数据飞轮、KPI、北极星目标等项目内部语言密度偏高。",
            "核心判断可保留，但应先用真实数据证据承接。",
        ],
        "suspected_typos": suspected_typos,
        "normalized_notes": [
            "客资相关词只在备注中规范化；raw 文案不改。",
            "下一版只允许低置信度准备 opening_0_3s 和 bridge_3_8s。",
        ],
        "current_data_window": "interim_36h_snapshot",
        "data_confidence": "low",
        "formal_revision_allowed": False,
        "formal_copy_revision_allowed": False,
        "low_confidence_prepare_allowed": True,
        "raw_copy_sha256": sha256_text(RAW_COPY),
        "status_boundary": {
            "raw_copy_modified": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
        },
    }


def build_copy_registry() -> dict[str, Any]:
    entry = {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V003_RAW_PATH),
        "record_path": rel(V003_RECORD_PATH),
        "structure_map_path": rel(V003_STRUCTURE_PATH),
        "decision_path": rel(V003_DECISION_PATH),
        "next_copy_revision_brief_path": rel(V003_BRIEF_PATH),
        "linked_operation_record": rel(V003_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V003_DATA_SNAPSHOT_PATH),
        "linked_decision_report": rel(V003_OPERATION_DECISION_PATH),
        "publish_status": "published_in_formal_operation",
        "data_window": "interim_36h_snapshot",
        "current_revision_status": "low_confidence_prepare_only",
    }
    return {
        "registry_version": "copy_iteration_registry_v1",
        "system_name": "copy_iteration_decision_system",
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        "records": [entry],
        "status_boundary": {
            "formal_copy_revision_allowed": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
        },
    }


def segment(
    segment_id: str,
    original_text: str,
    copy_function: str,
    viewer_question_answered: str,
    data_feedback_target: list[str],
    likely_issue_if_metric_bad: str,
    can_modify_if_problem_layer: list[str],
    must_keep: list[str],
    forbidden_change: list[str],
) -> dict[str, Any]:
    return {
        "segment_id": segment_id,
        "original_text": original_text,
        "copy_function": copy_function,
        "viewer_question_answered": viewer_question_answered,
        "data_feedback_target": data_feedback_target,
        "likely_issue_if_metric_bad": likely_issue_if_metric_bad,
        "can_modify_if_problem_layer": can_modify_if_problem_layer,
        "must_keep": must_keep,
        "forbidden_change": forbidden_change,
    }


def build_structure_map() -> dict[str, Any]:
    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "source_path": rel(V003_RAW_PATH),
        "structure_version": "copy_structure_map_v1",
        "current_assessment": {
            "opening_too_conceptual": True,
            "enters_kpi_and_data_flywheel_too_fast": True,
            "missing_real_data_conflict": True,
            "has_internal_project_language": True,
            "viewer_scene_insufficient": True,
            "core_claim_keepable": True,
            "assessment_confidence": "low",
            "assessment_boundary": "只能用于准备开头和 3-8 秒承接，不能判定选题方向或目标人群失败。",
        },
        "segments": [
            segment(
                "opening_0_3s",
                "第三期\n别再让ai给你定kpi了。播放多少、点赞多少、克资多少，看着很完整，但大多数时候没用，",
                "抛出反常识判断，试图阻断观众继续用 KPI 表思考。",
                "为什么我不该只看 KPI？",
                ["2s_bounce", "3s_retention"],
                "2s 跳出高时，说明开头像概念判断，缺少真实冲突和观众代入。",
                ["opening_packaging"],
                ["不要再让 AI 只给 KPI 表", "目标要服务下一步动作"],
                ["不得改成换人群", "不得改核心方向", "不得加入素材没有的数据承诺"],
            ),
            segment(
                "bridge_3_8s",
                "因为这些数字不会告诉你下一条到底该改标题，还是改开头，还是改中段结构。",
                "解释开头判断和下一步行动之间的关系。",
                "这些数据为什么没法指导下一条？",
                ["5s_completion", "average_watch_time"],
                "5s 完播弱时，说明承接没有快速把问题落到观众具体困境。",
                ["bridge_3_8s", "opening_packaging"],
                ["下一条只改哪个变量的核心问题"],
                ["不得扩写成全文重写", "不得改变 offer / 承接口径"],
            ),
            segment(
                "problem_setup",
                "我一开始也这样问，帮视频工厂定个目标，最好有播放、点赞和克资。",
                "建立作者旧做法和观众常见误区。",
                "作者之前是怎么错用 AI 的？",
                ["average_watch_time", "comment_count"],
                "如果中段观看弱，可能是旧做法交代太抽象。",
                ["middle_structure", "tone_and_language"],
                ["我一开始也这样问的自曝视角"],
                ["不得把作者经验改成外部权威说教"],
            ),
            segment(
                "negative_example",
                "第一版确实很全，北极星目标、阶段目标、指标数、刻字定义都有，但我看完觉得不对，他还是在回答我要追哪些数字。",
                "展示旧系统的完整但无用。",
                "第一版为什么看起来完整但仍不对？",
                ["average_watch_time", "favorite_rate"],
                "如果收藏弱，可能是反面示例缺少可复用结构。",
                ["middle_structure", "evidence_expression", "tone_and_language"],
                ["看起来完整但不能指导下一步的反差"],
                ["不得删除反面示例", "不得把疑似错字写进 normalized raw"],
            ),
            segment(
                "turning_point",
                "我真正需要的是数据回来以后，下一轮该改哪里。所以我又追问，",
                "从追数字转向追判断系统。",
                "真正的问题到底是什么？",
                ["5s_completion", "average_watch_time"],
                "承接弱时，转折点可能来得太晚或力度不足。",
                ["bridge_3_8s", "middle_structure"],
                ["数据回来以后下一轮该改哪里"],
                ["不得改成商业承诺", "不得改成新人群判断"],
            ),
            segment(
                "positive_system",
                "让ai设计一套目标驱动的数据飞轮，每期发布后，根据播放、留存、收藏、评论、私信和克兹，判断下一期只改哪个变量，这次结果才像个判断系统。",
                "给出新系统的正解形态。",
                "什么样的 AI 目标系统才有用？",
                ["favorite_rate", "average_watch_time"],
                "如果收藏有信号但观看弱，可能要提前压缩为更易懂的结果预览。",
                ["middle_structure", "evidence_expression"],
                ["目标驱动数据飞轮", "每期只改一个变量"],
                ["不得写成系统已经验证成功", "不得生成下一条正式执行 prompt"],
            ),
            segment(
                "metric_explanation",
                "播放和留存是触达，点赞和收藏是认可，评论和追问是互动。",
                "把指标分层解释给观众。",
                "每类指标分别说明什么？",
                ["favorite_rate", "comment_count"],
                "如果互动弱，可能是指标解释仍偏概念，没有引出观众提问。",
                ["evidence_expression", "tone_and_language"],
                ["播放/留存/收藏/评论的层级关系"],
                ["不得把点赞等同于客资", "不得把收藏直接写成商业成立"],
            ),
            segment(
                "lead_quality_boundary",
                "但私信也不能全算克资，要看他有没有说清楚任务场景和想要的结果。",
                "划清客资质量边界。",
                "什么样的私信才有需求质量？",
                ["dm_count", "effective_dm_count", "effective_consult_count"],
                "需求侧字段缺失时，只能保留规则，不得判定商业验证。",
                ["evidence_expression"],
                ["私信要看任务场景和结果"],
                ["不得把所有私信都算客资", "不得在缺数据时写有效咨询成立"],
            ),
            segment(
                "core_claim",
                "所以，目标不是kpi表，真正有用的目标是逼你回答三件事哪一层出了问题，下一条只改哪个变量，改完看哪个指标。",
                "输出整条文案的核心判断。",
                "真正有用的目标要逼我回答什么？",
                ["favorite_rate", "average_watch_time"],
                "如果收藏弱且多样本重复，才考虑核心表达或选题角度问题。",
                ["evidence_expression", "tone_and_language", "topic_angle"],
                ["哪一层出问题", "只改哪个变量", "改完看哪个指标"],
                ["不得在 V003 早期数据下判方向失败", "不得全文重写"],
            ),
            segment(
                "summary_rules",
                "没有这套判断，你每轮都在动，却不知道哪一步起作用。播放是入口，收藏是认可，私信要评分，每条只改一个主变量，",
                "把行动规则压缩成可记住的总结。",
                "我应该记住哪些复盘规则？",
                ["favorite_rate", "comment_count", "average_watch_time"],
                "如果尾段弱，可能是规则密度高，需要更口语化。",
                ["tone_and_language", "middle_structure"],
                ["播放是入口", "收藏是认可", "私信要评分", "每条只改一个主变量"],
                ["不得改成多变量同时测试", "不得改动核心规则"],
            ),
            segment(
                "ending_takeaway",
                "目标清楚了，动作才不会乱，复盘清楚了，下一步才会浮出来。",
                "以一句人话收束价值。",
                "这套判断最终带来什么？",
                ["completion_rate", "average_watch_time"],
                "如果结尾完播弱，可能是前文承接不足，结尾本身不优先大改。",
                ["tone_and_language"],
                ["目标清楚动作不乱", "复盘清楚下一步浮出来"],
                ["不得加重销售承接", "不得生成正式下一条执行 prompt"],
            ),
        ],
    }


def ensure_base_records(root: Path) -> None:
    ensure_raw_copy(root)
    write_json(root, V003_RECORD_PATH, build_copy_record())
    write_json(root, V003_STRUCTURE_PATH, build_structure_map())
    write_json(root, COPY_REGISTRY_PATH, build_copy_registry())


def infer_copy_decision(operation_report: dict[str, Any]) -> dict[str, Any]:
    operation_state = operation_report.get("current_project_state", {})
    next_decision = operation_report.get("next_episode_decision", {})
    partial_data = operation_state.get("current_data_goal_anchor_status") == "partial_data_recorded"
    two_second_bounce = metric_number(operation_report, "two_second_bounce_rate")
    five_second_completion = metric_number(operation_report, "five_second_completion_rate")
    favorite_rate = metric_number(operation_report, "favorite_rate")
    recommendation_page = metric_number(operation_report, "traffic_source_recommendation_page")
    average_watch_time = metric_value(operation_report, "average_watch_time")

    if partial_data:
        formal_copy_revision_allowed = False
        low_confidence_prepare_allowed = True
    else:
        formal_copy_revision_allowed = bool(next_decision.get("can_enter_next_episode_execution"))
        low_confidence_prepare_allowed = not formal_copy_revision_allowed

    problem_layer = "opening_packaging"
    supporting_problem_layers = ["bridge_3_8s"]
    rule_trace = [
        "current_operation_report says V003 is partial_data_recorded -> formal_copy_revision = blocked",
        "recommendation_page is high and 2s_bounce is high -> prioritize opening_packaging",
        "5s_completion is weak -> allow low-confidence bridge_3_8s preparation",
        "favorite_rate has a small positive signal -> do not jump to topic_angle failure",
    ]

    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "decision_version": "copy_iteration_decision_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_paths": {
            "operation_report": rel(OPERATION_REPORT_PATH),
            "final_user_operation_result": rel(FINAL_USER_OPERATION_RESULT_PATH),
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "copy_record": rel(V003_RECORD_PATH),
            "structure_map": rel(V003_STRUCTURE_PATH),
        },
        "data_window": "interim_36h_snapshot",
        "data_confidence": "low",
        "operation_decision_status": next_decision.get("decision_status"),
        "problem_layer": problem_layer,
        "problem_layer_candidates": PROBLEM_LAYERS,
        "supporting_problem_layers": supporting_problem_layers,
        "confidence": "low",
        "formal_copy_revision_allowed": formal_copy_revision_allowed,
        "low_confidence_prepare_allowed": low_confidence_prepare_allowed,
        "revision_scope": ["opening_0_3s", "bridge_3_8s"],
        "forbidden_changes": [
            "target_user",
            "topic_direction",
            "offer",
            "whole_script_rewrite",
            "formal_next_video_execution_prompt",
        ],
        "validation_metric": [
            "2s_bounce",
            "3s_retention",
            "5s_completion",
            "average_watch_time",
        ],
        "next_action": "prepare_candidate_opening_revision_brief_only",
        "allow_topic_direction_change": False,
        "allow_target_audience_change": False,
        "require_multiple_samples_for_topic_angle": True,
        "require_7_to_10_failed_samples_for_target_audience_change": True,
        "data_triggers": {
            "play_count": metric_value(operation_report, "play_count"),
            "recommendation_page": metric_value(operation_report, "traffic_source_recommendation_page"),
            "two_second_bounce_rate": metric_value(operation_report, "two_second_bounce_rate"),
            "five_second_completion_rate": metric_value(operation_report, "five_second_completion_rate"),
            "completion_rate": metric_value(operation_report, "completion_rate"),
            "average_watch_time": average_watch_time,
            "favorite_count": metric_value(operation_report, "favorite_count"),
            "favorite_rate": metric_value(operation_report, "favorite_rate"),
            "missing_fields": next_decision.get("missing_data", []),
        },
        "numeric_trace": {
            "recommendation_page_percent": recommendation_page,
            "two_second_bounce_percent": two_second_bounce,
            "five_second_completion_percent": five_second_completion,
            "favorite_rate_percent": favorite_rate,
        },
        "rule_trace": rule_trace,
        "must_not_output": [
            "target_audience_error",
            "topic_direction_failure",
            "whole_script_rewrite",
            "formal_next_video_execution",
            "formal_copy_revision_ready",
        ],
        "status_boundary": {
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "target_audience_changed": False,
            "topic_direction_changed": False,
        },
    }


def render_next_brief(decision: dict[str, Any]) -> str:
    triggers = decision["data_triggers"]
    missing = triggers.get("missing_fields", [])
    return "\n".join(
        [
            "# V003 下一版文案修改简报",
            "",
            "> 本简报给 ChatGPT 读取；它不是正式下一条视频执行 prompt，也不是 Codex 最终定稿。",
            "",
            "## 1. 当前判断",
            "当前不是换方向，也不是换人群，而是低置信度准备开头 0-3 秒和 3-8 秒承接。",
            "",
            "## 2. 数据触发原因",
            f"- 2s 跳出：{triggers.get('two_second_bounce_rate')}",
            "- 3s 留存：missing",
            f"- 5s 完播：{triggers.get('five_second_completion_rate')}",
            f"- 完播率：{triggers.get('completion_rate')}",
            f"- 平均观看：{triggers.get('average_watch_time')}",
            f"- 收藏：{triggers.get('favorite_count')} / 收藏率 {triggers.get('favorite_rate')}",
            "- 缺失数据：" + "、".join(missing),
            "",
            "## 3. 这版文案好的地方",
            "- 核心观点成立：目标不是 KPI 表，而是逼出下一步动作。",
            "- “播放是入口，收藏是认可，私信要评分”可保留。",
            "- “每条只改一个主变量”可保留。",
            "- “哪一层出了问题，下一条只改哪个变量，改完看哪个指标”是本条最有价值的判断。",
            "",
            "## 4. 这版文案不好的地方",
            "- 开头太像概念判断，观众还没看到真实冲突就进入 KPI 讨论。",
            "- 太快进入 KPI / 数据飞轮 / 北极星目标等内部语言。",
            "- 缺少 V003 真实数据冲突作为开场证据。",
            "- 观众代入不足，没有先说“为什么你看了数据还是不知道下一条改哪”。",
            "- 客资相关词疑似有错字：`克资`、`刻字定义`、`克兹`，只在备注修正，不改 raw 原文。",
            "",
            "## 5. 下一版只改哪里",
            "- 开头 0-3 秒",
            "- 3-8 秒承接",
            "",
            "## 6. 哪些不能动",
            "- 不改目标用户。",
            "- 不改核心选题方向。",
            "- 不改中段核心判断。",
            "- 不改承接 / offer。",
            "- 不做全文重写。",
            "",
            "## 7. 给 ChatGPT 的改稿指令",
            "下一版先把开头从“别再让 AI 给你定 KPI”改成真实数据冲突切入，优先用 V003 的 141 播放、2s 跳出 50%、收藏 3 作为开场证据，再转入“AI 真正有用的是判断下一条先改哪”。不要重写全片，只重写开头和 3-8 秒承接。",
            "",
            "## 8. 改完看什么指标",
            "- 2s bounce",
            "- 3s retention",
            "- 5s completion",
            "- average_watch_time",
            "",
        ]
    )


def build_latest_report(decision: dict[str, Any]) -> dict[str, Any]:
    return {
        "system_name": "copy_iteration_decision_system",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "current_copy_version": "V003_copy_v1 / v1_raw",
        "current_data_window": "interim_36h_snapshot",
        "current_problem_layer": decision["problem_layer"],
        "confidence": decision["confidence"],
        "revision_scope_allowed": decision["revision_scope"],
        "keep_items": [
            "核心观点：目标不是 KPI 表，而是下一步动作判断系统。",
            "播放是入口，收藏是认可，私信要评分。",
            "每条只改一个主变量。",
        ],
        "forbidden_items": decision["forbidden_changes"],
        "when_continue_copy_revision": "补齐 72h / 7d 或下一轮同类样本后，若 2s/3s/5s 仍弱，继续调 opening_packaging 和 bridge_3_8s。",
        "when_adjust_topic_angle": "只有多个正常分发样本在开头、结构、语气测试后仍收藏/评论/需求信号持续弱，才进入 topic_angle 判断。",
        "when_allow_new_target_audience": "必须 7-10 个正常样本经过开头、结构、语气测试仍失败后，才允许讨论 target_audience 变化。",
        "chatgpt_read_first": rel(V003_BRIEF_PATH),
        "paths": {
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "v003_raw_copy": rel(V003_RAW_PATH),
            "v003_copy_record": rel(V003_RECORD_PATH),
            "v003_structure_map": rel(V003_STRUCTURE_PATH),
            "v003_copy_iteration_decision": rel(V003_DECISION_PATH),
            "v003_next_copy_revision_brief": rel(V003_BRIEF_PATH),
            "latest_copy_iteration_report_md": rel(LATEST_REPORT_MD),
            "script_path": rel(SCRIPT_PATH),
        },
        "status_boundary": decision["status_boundary"],
    }


def render_latest_report_md(report: dict[str, Any]) -> str:
    lines = [
        "# 最新文案迭代报告",
        "",
        "## 当前结论",
        f"- 当前文案版本：`{report['current_copy_version']}`",
        f"- 当前数据窗口：`{report['current_data_window']}`",
        f"- 当前问题层级：`{report['current_problem_layer']}`",
        f"- 置信度：`{report['confidence']}`",
        "- 本轮只允许改：`opening_0_3s + bridge_3_8s`",
        "- 当前不允许：全文重写、换选题方向、换目标人群、生成正式下一条视频执行 prompt。",
        "",
        "## 保留项",
    ]
    lines.extend(f"- {item}" for item in report["keep_items"])
    lines.extend(["", "## 禁止项"])
    lines.extend(f"- `{item}`" for item in report["forbidden_items"])
    lines.extend(
        [
            "",
            "## 什么时候继续调文案",
            report["when_continue_copy_revision"],
            "",
            "## 什么时候调选题方向",
            report["when_adjust_topic_angle"],
            "",
            "## 什么时候允许打新人群",
            report["when_allow_new_target_audience"],
            "",
            "## ChatGPT 下一步读取",
            f"- `{report['chatgpt_read_first']}`",
            "",
            "## 状态边界",
        ]
    )
    for key, value in report["status_boundary"].items():
        lines.append(f"- {key}: `{str(value).lower()}`")
    lines.append("")
    return "\n".join(lines)


def build_and_write(root: Path) -> dict[str, Any]:
    operation_report = load_json(root, OPERATION_REPORT_PATH)
    read_text(root, FINAL_USER_OPERATION_RESULT_PATH)
    ensure_base_records(root)

    copy_record = load_json(root, V003_RECORD_PATH)
    structure_map = load_json(root, V003_STRUCTURE_PATH)
    registry = load_json(root, COPY_REGISTRY_PATH)
    decision = infer_copy_decision(operation_report)

    write_json(root, V003_DECISION_PATH, decision)
    write_text(root, V003_BRIEF_PATH, render_next_brief(decision))
    latest_report = build_latest_report(decision)
    write_json(root, LATEST_REPORT_JSON, latest_report)
    write_text(root, LATEST_REPORT_MD, render_latest_report_md(latest_report))

    validation = validate_outputs(root)
    validation["records_loaded"] = {
        "copy_record": copy_record["copy_id"],
        "structure_segments": len(structure_map["segments"]),
        "registry_records": len(registry["records"]),
    }
    return validation


def validate_outputs(root: Path) -> dict[str, Any]:
    output_paths = [
        COPY_REGISTRY_PATH,
        V003_RAW_PATH,
        V003_RECORD_PATH,
        V003_STRUCTURE_PATH,
        V003_DECISION_PATH,
        V003_BRIEF_PATH,
        LATEST_REPORT_JSON,
        LATEST_REPORT_MD,
    ]
    missing = [rel(path) for path in output_paths if not (root / path).exists()]
    if missing:
        raise RuntimeError("Missing copy iteration outputs: " + ", ".join(missing))

    raw = read_text(root, V003_RAW_PATH)
    if raw != RAW_COPY:
        raise RuntimeError("V003 raw copy was modified")

    parsed_json = []
    for path in [COPY_REGISTRY_PATH, V003_RECORD_PATH, V003_STRUCTURE_PATH, V003_DECISION_PATH, LATEST_REPORT_JSON]:
        load_json(root, path)
        parsed_json.append(rel(path))

    record = load_json(root, V003_RECORD_PATH)
    structure = load_json(root, V003_STRUCTURE_PATH)
    decision = load_json(root, V003_DECISION_PATH)
    latest = load_json(root, LATEST_REPORT_JSON)

    required_segments = {
        "opening_0_3s",
        "bridge_3_8s",
        "problem_setup",
        "negative_example",
        "turning_point",
        "positive_system",
        "metric_explanation",
        "lead_quality_boundary",
        "core_claim",
        "summary_rules",
        "ending_takeaway",
    }
    actual_segments = {item["segment_id"] for item in structure["segments"]}
    missing_segments = sorted(required_segments - actual_segments)
    if missing_segments:
        raise RuntimeError("Missing structure segments: " + ", ".join(missing_segments))

    if not record["suspected_typos"]:
        raise RuntimeError("suspected typos were not recorded")
    if decision["problem_layer"] != "opening_packaging":
        raise RuntimeError("V003 problem_layer must remain opening_packaging")
    if decision["confidence"] != "low":
        raise RuntimeError("V003 confidence must remain low")
    if decision["formal_copy_revision_allowed"]:
        raise RuntimeError("formal copy revision must be blocked for V003 interim data")
    if not decision["low_confidence_prepare_allowed"]:
        raise RuntimeError("low confidence preparation must be allowed")
    if decision["allow_target_audience_change"] or decision["allow_topic_direction_change"]:
        raise RuntimeError("target audience or topic direction change was incorrectly allowed")
    if latest["status_boundary"]["next_formal_video_execution_prompt_generated"]:
        raise RuntimeError("formal next video execution prompt must not be generated")

    scan_texts = "\n".join(
        read_text(root, path)
        for path in [V003_DECISION_PATH, V003_BRIEF_PATH, LATEST_REPORT_JSON, LATEST_REPORT_MD]
        if (root / path).exists()
    ).lower()
    forbidden_scan = {
        key: any(pattern.lower() in scan_texts for pattern in patterns)
        for key, patterns in FORBIDDEN_STATUS_PATTERNS.items()
    }
    if any(forbidden_scan.values()):
        raise RuntimeError(f"Forbidden status phrase found: {forbidden_scan}")

    return {
        "outputs_exist": [rel(path) for path in output_paths],
        "json_parse_passed": parsed_json,
        "raw_copy_sha256": sha256_text(raw),
        "raw_copy_matches_locked_source": True,
        "suspected_typos_count": len(record["suspected_typos"]),
        "structure_segment_count": len(structure["segments"]),
        "problem_layer": decision["problem_layer"],
        "confidence": decision["confidence"],
        "formal_copy_revision_allowed": decision["formal_copy_revision_allowed"],
        "low_confidence_prepare_allowed": decision["low_confidence_prepare_allowed"],
        "revision_scope": decision["revision_scope"],
        "forbidden_status_scan": forbidden_scan,
        "forbidden_status_advanced": False,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build copy iteration decision outputs from operation data.")
    parser.add_argument("--root", default=str(ROOT), help="Repository root")
    parser.add_argument("--validate-only", action="store_true", help="Validate existing outputs without rewriting")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.validate_only:
        validation = validate_outputs(root)
    else:
        validation = build_and_write(root)
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    return 0 if not validation["forbidden_status_advanced"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
