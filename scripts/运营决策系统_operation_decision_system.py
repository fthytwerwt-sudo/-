#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent

DECISION_DIR = Path("review_loop/decision_engine")
INDEX_PATH = Path("review_loop/operation_records_index.md")
CURRENT_TARGET_PATH = Path("codex_log/current_operation_target.md")
CURRENT_ANCHOR_PATH = Path("codex_log/current_data_goal_anchor.md")

SCHEMA_PATH = DECISION_DIR / "operation_decision_schema.json"
THRESHOLD_PATH = DECISION_DIR / "threshold_config_stage_hypothesis.json"
CLASSIFICATION_RULES_PATH = DECISION_DIR / "sample_classification_rules.json"

SYNTHESIS_JSON = DECISION_DIR / "V001_V002_V003_operation_synthesis_report.json"
SYNTHESIS_MD = DECISION_DIR / "V001_V002_V003_operation_synthesis_report.md"
LATEST_REPORT_JSON = DECISION_DIR / "latest_operation_decision_report.json"
LATEST_REPORT_MD = DECISION_DIR / "latest_operation_decision_report.md"
FINAL_USER_REPORT_MD = DECISION_DIR / "final_user_operation_result.md"

COPY_ITERATION_REPORT_JSON = Path("review_loop/copy_iteration/latest_copy_iteration_report.json")
COPY_ITERATION_REPORT_MD = Path("review_loop/copy_iteration/latest_copy_iteration_report.md")
V003_NEXT_COPY_REVISION_BRIEF_MD = Path(
    "review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md"
)
COPY_ITERATION_SCRIPT = Path("scripts/文案迭代决策系统_copy_iteration_decision_system.py")

V003_RESULT_JSON = (
    Path("review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514")
    / "V003_operation_decision_result.json"
)
V003_RESULT_MD = (
    Path("review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514")
    / "V003_operation_decision_result.md"
)
V003_LATEST_SNAPSHOT_JSON = (
    Path("review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514")
    / "V003_post_72h_pre_7d_snapshot.json"
)

FORBIDDEN_STATUS_PATTERNS = {
    "content_validation": [
        "content_validation = passed",
        "content_validation: passed",
        "content_validation：passed",
    ],
    "send_ready": ["send_ready = true", "send_ready: true", "send_ready：true"],
    "publish_status_success": [
        "publish_status_success = true",
        "publish_status: success",
        "publish_status：success",
    ],
    "voice_validation": [
        "voice_validation = passed",
        "voice_validation: passed",
        "voice_validation：passed",
    ],
    "final_voice_validated": [
        "final_voice_validated = true",
        "final_voice_validated: true",
        "final_voice_validated：true",
    ],
    "visual_master_locked": [
        "visual_master_locked = true",
        "visual_master_locked: true",
        "visual_master_locked：true",
    ],
}

FORMAL_ATTRIBUTION_REQUIRED_FIELDS = {
    "72h_final_data",
    "7d_final_data",
    "3s_retention",
    "profile_visit_count",
    "dm_count",
    "effective_dm_count",
    "effective_consult_count",
    "clear_need_customer_count",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(root: Path, path: Path) -> str:
    return (root / path).read_text(encoding="utf-8")


def load_json(root: Path, path: Path) -> dict[str, Any]:
    return json.loads(read_text(root, path))


def write_json(root: Path, path: Path, payload: dict[str, Any]) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(root: Path, path: Path, content: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def parse_percent(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value)
    match = re.search(r"(-?\d+(?:\.\d+)?)\s*%", text)
    if match:
        return float(match.group(1))
    return None


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace(",", "")
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    if match:
        return float(match.group(0))
    return None


def parse_index_records(index_text: str) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    for line in index_text.splitlines():
        if not line.startswith("| V"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] == "video_id":
            continue
        path_match = re.search(r"`([^`]+)`", cells[2])
        records[cells[0]] = {
            "video_id": cells[0],
            "title": cells[1],
            "record_path": path_match.group(1) if path_match else cells[2],
            "status": cells[3].strip("`"),
            "data_completeness": cells[4],
        }
    return records


def extract_line_value(text: str, names: list[str]) -> str | None:
    for name in names:
        pattern = rf"[-*]?\s*{re.escape(name)}\s*[：:]\s*([^\n|]+)"
        match = re.search(pattern, text)
        if match:
            value = match.group(1).strip()
            if value and not value.startswith("missing") and value != "-":
                return value
    return None


def metric(value: Any, source_status: str, confidence: str = "medium") -> dict[str, Any]:
    return {
        "value": value,
        "numeric_value": parse_number(value),
        "percent_value": parse_percent(value),
        "source_status": source_status,
        "confidence": confidence,
    }


def missing_metric() -> dict[str, Any]:
    return {
        "value": None,
        "numeric_value": None,
        "percent_value": None,
        "source_status": "missing",
        "confidence": "none",
    }


def metric_value(record: dict[str, Any], key: str, default: Any = "missing") -> Any:
    return record.get("normalized_metrics", {}).get(key, {}).get("value", default)


def snapshot_phrase(record: dict[str, Any]) -> str:
    label = str(record.get("snapshot_label") or "unknown_snapshot")
    if label == "post_72h_pre_7d_snapshot":
        return f"{label}（72h 后 / 7d 前补录，非 7d final）"
    hours = "约 65 小时" if "65h" in label else "约 37 小时" if "36h" in label else "当前"
    if label.startswith("interim_"):
        return f"{label}（{hours}中间数据，非 final）"
    return label


def is_interim_snapshot(record: dict[str, Any]) -> bool:
    label = str(record.get("snapshot_label", ""))
    return label.startswith("interim_") or label == "post_72h_pre_7d_snapshot"


def normalize_v003(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    core = snapshot.get("core_metrics", {})
    metrics: dict[str, dict[str, Any]] = {}
    for key, value in core.items():
        metrics[key] = metric(value, "extracted_from_screenshot", "high")
    for key, value in snapshot.get("traffic_sources", {}).items():
        metrics[f"traffic_source_{key}"] = metric(value, "extracted_from_screenshot", "high")
    for field in snapshot.get("missing_fields", []):
        metrics.setdefault(field, missing_metric())
    return metrics


def normalize_markdown_record(video_id: str, text: str) -> dict[str, dict[str, Any]]:
    fields = {
        "play_count": ["play_count（播放量）", "播放量", "24h_play_count", "72h_play_count", "7d_play_count"],
        "like_count": ["like_count（点赞数）", "点赞数"],
        "favorite_count": ["favorite_count（收藏数）", "收藏数"],
        "like_rate": ["like_rate（点赞率）", "点赞率"],
        "favorite_rate": ["favorite_rate（收藏率）", "收藏率"],
        "completion_rate": ["completion_rate", "完播率"],
        "average_watch_time": ["average_watch_time", "平均观看时长"],
        "profile_visit_count": ["profile_visit_count"],
        "dm_count": ["dm_count", "私信 / 咨询数（可选）"],
        "effective_dm_count": ["effective_dm_count"],
        "effective_consult_count": ["effective_consult_count"],
        "3s_retention": ["3s_retention", "前 3 秒留存（可选）"],
        "comment_count": ["comment_count", "评论数（可选）"],
        "new_follow_count": ["new_follow_count", "转粉数（可选）"],
    }
    normalized: dict[str, dict[str, Any]] = {}
    for key, names in fields.items():
        value = extract_line_value(text, names)
        normalized[key] = metric(value, "user_provided_or_markdown_extract", "medium") if value else missing_metric()

    if video_id == "V002":
        for key, label in {
            "play_count": "play_count（播放量）",
            "like_count": "like_count（点赞数）",
            "favorite_count": "favorite_count（收藏数）",
            "like_rate": "like_rate（点赞率）",
            "favorite_rate": "favorite_rate（收藏率）",
        }.items():
            row = re.search(rf"\|\s*{re.escape(label)}\s*\|\s*([^|]+)\|", text)
            if row:
                normalized[key] = metric(row.group(1).strip(), "user_provided_or_calculated_from_fields", "medium")
    return normalized


def load_record(
    root: Path,
    index_entry: dict[str, str],
    classification_rules: dict[str, Any],
) -> dict[str, Any]:
    video_id = index_entry["video_id"]
    record_path = Path(index_entry["record_path"])
    record_text = read_text(root, record_path)
    rule = classification_rules["sample_classes"].get(video_id, {})

    structured_snapshot_path = None
    structured_snapshot: dict[str, Any] | None = None
    structured_match = re.search(r"structured_snapshot(?:_path)?[：:]\s*`?([^`\n]+?\.json)`?", record_text)
    if structured_match:
        structured_snapshot_path = Path(structured_match.group(1).strip())
    elif video_id == "V003":
        structured_snapshot_path = Path(
            "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
            "V003_早期数据快照_early_interim_snapshot.json"
        )

    if video_id == "V003" and (root / V003_LATEST_SNAPSHOT_JSON).exists():
        structured_snapshot_path = V003_LATEST_SNAPSHOT_JSON

    if structured_snapshot_path and (root / structured_snapshot_path).exists():
        structured_snapshot = load_json(root, structured_snapshot_path)

    if video_id == "V003" and structured_snapshot:
        normalized_metrics = normalize_v003(structured_snapshot)
        missing_fields = structured_snapshot.get("missing_fields", [])
        uncertain_fields = structured_snapshot.get("uncertain_fields", [])
        data_confidence = structured_snapshot.get("data_confidence", "low")
        review_window = structured_snapshot.get("review_window", "between_24h_and_72h")
        snapshot_label = structured_snapshot.get("snapshot_label", "interim_36h_snapshot")
    else:
        normalized_metrics = normalize_markdown_record(video_id, record_text)
        missing_fields = [key for key, value in normalized_metrics.items() if value["source_status"] == "missing"]
        uncertain_fields = re.findall(r"uncertain[_a-zA-Z]*|待验证|待回填|待用户回填", record_text)
        data_confidence = "low" if missing_fields else "medium"
        review_window = "unknown_or_missing"
        snapshot_label = "markdown_record_only"

    base_normal_attribution_eligible = bool(rule.get("normal_attribution_eligible", False))
    normal_attribution_eligible = base_normal_attribution_eligible
    normal_attribution_blocked_reason = None
    if video_id == "V003" and (
        snapshot_label.startswith("interim_")
        or FORMAL_ATTRIBUTION_REQUIRED_FIELDS.intersection(set(missing_fields))
    ):
        normal_attribution_eligible = False
        normal_attribution_blocked_reason = (
            "current_target_partial_data_waiting_72h_7d_and_required_lead_fields"
        )

    return {
        "video_id": video_id,
        "title": index_entry["title"],
        "record_path": rel(record_path),
        "record_read": True,
        "record_status_from_index": index_entry["status"],
        "record_status_rule": rule.get("classification", index_entry["status"]),
        "sample_role": rule.get("sample_role", "unknown"),
        "normal_attribution_candidate": base_normal_attribution_eligible,
        "normal_attribution_eligible": normal_attribution_eligible,
        "normal_attribution_blocked_reason": normal_attribution_blocked_reason,
        "allowed_uses": rule.get("allowed_uses", []),
        "forbidden_uses": rule.get("forbidden_uses", []),
        "data_completeness": index_entry["data_completeness"],
        "data_confidence": data_confidence,
        "review_window": review_window,
        "snapshot_label": snapshot_label,
        "structured_snapshot_path": rel(structured_snapshot_path) if structured_snapshot_path else None,
        "structured_snapshot_read": structured_snapshot is not None,
        "normalized_metrics": normalized_metrics,
        "missing_fields": sorted(set(missing_fields)),
        "uncertain_fields": sorted(set(uncertain_fields)),
    }


def data_quality(record: dict[str, Any]) -> dict[str, Any]:
    video_id = record["video_id"]
    missing_count = len(record["missing_fields"])
    uncertain_count = len(record["uncertain_fields"])
    if video_id == "V001":
        score = 0.15
        label = "historical_incomplete"
    elif video_id == "V002":
        score = 0.45
        label = "abnormal_partial"
    elif video_id == "V003":
        score = 0.55
        label = "partial_snapshot_low_confidence"
    else:
        score = 0.0
        label = "unknown"
    v003_note = f"当前目标样本，最新为 {snapshot_phrase(record)}，不能做 7d final 复盘。"
    return {
        "quality_label": label,
        "quality_score_0_to_1": score,
        "missing_field_count": missing_count,
        "uncertain_field_count": uncertain_count,
        "usable_for_normal_distribution_attribution": record["normal_attribution_eligible"],
        "quality_note": {
            "V001": "历史样本，核心窗口数据多为空，只能作为旧阶段参考。",
            "V002": "平台审核减推污染样本，有兴趣信号但不能进入正常自然分发归因。",
            "V003": v003_note,
        }.get(video_id, "未知样本。"),
    }


def signal_from_play(play_count: float | None, thresholds: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    if play_count is None:
        return {"status": "blocked_by_missing_data", "reason": "missing_play_count"}
    if record["video_id"] == "V002":
        return {
            "status": "excluded_from_normal_distribution_judgment",
            "reason": "policy_limited_abnormal_sample",
            "observed_value": play_count,
        }
    if record["video_id"] == "V003" and is_interim_snapshot(record):
        return {
            "status": "draft_low_confidence",
            "bucket": "partial_snapshot_under_1000",
            "observed_value": play_count,
            "reason": f"{record['snapshot_label']}_not_final_7d",
        }
    if play_count < thresholds["single_video_play_thresholds"]["fail"]["max_exclusive"]:
        bucket = "fail"
    elif play_count < thresholds["single_video_play_thresholds"]["baseline_observe"]["max_exclusive"]:
        bucket = "baseline_observe"
    elif play_count < thresholds["single_video_play_thresholds"]["positive_signal"]["max_exclusive"]:
        bucket = "positive_signal"
    else:
        bucket = "breakout_observe"
    return {
        "status": "checked",
        "bucket": bucket,
        "observed_value": play_count,
        "meaning": thresholds["single_video_play_thresholds"][bucket]["meaning"],
    }


def check_thresholds(record: dict[str, Any], thresholds: dict[str, Any]) -> dict[str, Any]:
    metrics = record["normalized_metrics"]
    play_count = metrics.get("play_count", missing_metric()).get("numeric_value")
    completion_rate = metrics.get("completion_rate", missing_metric()).get("percent_value")
    five_second_completion = metrics.get("five_second_completion_rate", missing_metric()).get("percent_value")
    two_second_bounce = metrics.get("two_second_bounce_rate", missing_metric()).get("percent_value")
    favorite_rate = metrics.get("favorite_rate", missing_metric()).get("percent_value")
    like_rate = metrics.get("like_rate", missing_metric()).get("percent_value")
    comment_count = metrics.get("comment_count", missing_metric()).get("numeric_value")

    retention_missing = completion_rate is None and five_second_completion is None and two_second_bounce is None
    if retention_missing:
        retention_signal = {"status": "blocked_by_missing_data", "reason": "missing_retention_fields"}
    else:
        weak = (
            (completion_rate is not None and completion_rate < thresholds["retention_thresholds"]["completion_rate_weak_max_percent"])
            or (
                five_second_completion is not None
                and five_second_completion < thresholds["retention_thresholds"]["five_second_completion_weak_max_percent"]
            )
            or (
                two_second_bounce is not None
                and two_second_bounce >= thresholds["retention_thresholds"]["two_second_bounce_weak_min_percent"]
            )
        )
        retention_signal = {
            "status": "draft_low_confidence" if record["video_id"] == "V003" else "checked",
            "bucket": "weak" if weak else "not_weak_from_available_fields",
            "completion_rate": completion_rate,
            "five_second_completion_rate": five_second_completion,
            "two_second_bounce_rate": two_second_bounce,
        }

    if favorite_rate is None:
        value_signal = {"status": "blocked_by_missing_data", "reason": "missing_favorite_rate"}
    elif favorite_rate >= thresholds["value_signal_thresholds"]["favorite_rate_strong_min_percent"]:
        value_signal = {"status": "draft_low_confidence", "bucket": "positive_value_signal", "favorite_rate": favorite_rate}
    elif favorite_rate >= thresholds["value_signal_thresholds"]["favorite_rate_weak_min_percent"]:
        value_signal = {"status": "draft_low_confidence", "bucket": "weak_positive_signal", "favorite_rate": favorite_rate}
    else:
        value_signal = {"status": "checked", "bucket": "weak", "favorite_rate": favorite_rate}

    interaction_signal = {
        "status": "blocked_by_missing_data" if like_rate is None and comment_count is None else "checked",
        "like_rate": like_rate,
        "comment_count": comment_count,
        "bucket": "weak_public_feedback" if (comment_count in (0, None)) else "has_public_feedback",
    }

    required_lead_fields = thresholds["required_for_formal_next_episode_decision"]["lead_fields"]
    missing_lead_fields = [field for field in required_lead_fields if field in record["missing_fields"]]
    lead_signal = {
        "status": "blocked_by_missing_data" if missing_lead_fields else "checked",
        "missing_fields": missing_lead_fields,
    }
    commercial_signal = {
        "status": "blocked_by_missing_data",
        "reason": "no_effective_consult_or_paid_signal_recorded",
    }

    return {
        "play_signal": signal_from_play(play_count, thresholds, record),
        "retention_signal": retention_signal,
        "value_signal": value_signal,
        "interaction_signal": interaction_signal,
        "lead_signal": lead_signal,
        "commercial_signal": commercial_signal,
    }


def infer_bottleneck(record: dict[str, Any], threshold_result: dict[str, Any]) -> dict[str, Any]:
    video_id = record["video_id"]
    if video_id == "V001":
        return {
            "status": "historical_reference_only",
            "candidate_bottleneck": None,
            "reason": "historical_record_data_incomplete",
        }
    if video_id == "V002":
        return {
            "status": "abnormal_sample_excluded_from_normal_distribution_judgment",
            "candidate_bottleneck": "platform_policy_packaging_risk",
            "reason": "policy_distribution_limited",
        }
    missing = set(record["missing_fields"])
    if video_id == "V003":
        metrics = record["normalized_metrics"]
        return {
            "status": "draft_low_confidence",
            "candidate_bottleneck": "opening_retention_and_initial_distribution_weak",
            "evidence": [
                f"snapshot_label={record['snapshot_label']}",
                f"play_count={metric_value(record, 'play_count')}",
                f"two_second_bounce_rate={metric_value(record, 'two_second_bounce_rate')}",
                f"five_second_completion_rate={metric_value(record, 'five_second_completion_rate')}",
                f"completion_rate={metric_value(record, 'completion_rate')}",
                f"recommendation_page={metric_value(record, 'traffic_source_recommendation_page')}",
            ],
            "blocked_for_formal_conclusion_by": sorted(
                missing.intersection(
                    {
                        "3s_retention",
                        "profile_visit_count",
                        "dm_count",
                        "effective_dm_count",
                        "effective_consult_count",
                        "72h_final_data",
                        "7d_final_data",
                    }
                )
            ),
        }
    return {"status": "unknown", "candidate_bottleneck": None}


def synthesize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_id = {record["video_id"]: record for record in records}
    v003 = by_id.get("V003", {})
    v003_snapshot = snapshot_phrase(v003) if v003 else "unknown"
    valid_samples = [
        record["video_id"]
        for record in records
        if record["normal_attribution_eligible"] and record["video_id"] == "V003"
    ]
    excluded_samples = [
        record["video_id"]
        for record in records
        if not record["normal_attribution_eligible"]
    ]
    return {
        "records_seen": [record["video_id"] for record in records],
        "what_is_observed": [
            "V001 提供旧阶段历史样本入口，但核心数据不完整。",
            "V002 提供平台审核减推异常样本，可用于平台风险表达参考，不能用于正常自然流量归因。",
            f"V003 提供当前目标的 {v003_snapshot}：触达很小、前 5 秒承接弱、收藏有小正信号、需求侧字段缺失。",
        ],
        "what_is_not_proven": [
            "未证明内容方向成立。",
            "未证明内容方向失败。",
            "未证明商业验证成立。",
            "未证明数据飞轮已经跑通。",
            "未证明可以进入下一条正式视频执行。",
        ],
        "valid_samples_for_normal_attribution": valid_samples,
        "samples_not_for_normal_attribution": sorted(set(excluded_samples)),
        "current_largest_gap": "缺 V003 7d final 与需求侧字段，无法从低播放直接归因到内容方向或商业价值。",
        "distance_to_north_star_goal": [
            "缺稳定高质量需求信号。",
            "缺有效私信 / 有效咨询 / 清晰需求客户。",
            "缺可重复的同类内容样本。",
            "缺 post-publish review 后的唯一变量验证闭环。",
        ],
        "per_record_summary": {
            video_id: {
                "can_explain": record["summary"]["can_explain"],
                "cannot_explain": record["summary"]["cannot_explain"],
                "data_quality": record["data_quality"],
                "next_value": record["summary"]["next_value"],
            }
            for video_id, record in by_id.items()
        },
    }


def per_record_summary(record: dict[str, Any]) -> dict[str, Any]:
    video_id = record["video_id"]
    if video_id == "V001":
        return {
            "can_explain": "它能说明旧 V001 是历史运营样本，路径保留为 legacy 证据。",
            "cannot_explain": "不能说明当前方向成立/失败，也不能判断下一轮变量。",
            "next_value": "作为历史边界与旧流程对照，防止旧 gray_test 口径覆盖当前运营目标。",
        }
    if video_id == "V002":
        return {
            "can_explain": "它能说明平台风险表达会污染分发，并显示小样本兴趣信号。",
            "cannot_explain": "不能作为正常自然流量失败样本，也不能证明内容通过。",
            "next_value": "用于下一轮规避平台风险表达，但不进入正常归因统计。",
        }
    if video_id == "V003":
        return {
            "can_explain": f"它能说明当前目标已有 {snapshot_phrase(record)}：低播放、开头承接弱、小收藏信号、需求侧缺失。",
            "cannot_explain": "不能说明 7d 结果，不能决定方向失败，不能生成正式下一期执行。",
            "next_value": "补齐关键字段后可作为下一轮唯一变量判断的主样本。",
        }
    return {"can_explain": "unknown", "cannot_explain": "unknown", "next_value": "unknown"}


def decide_next_episode(records: list[dict[str, Any]], thresholds: dict[str, Any]) -> dict[str, Any]:
    current = next(record for record in records if record["video_id"] == "V003")
    missing_required = sorted(
        set(thresholds["required_for_formal_next_episode_decision"]["minimum_fields"]).intersection(
            set(current["missing_fields"])
        )
    )
    if missing_required or is_interim_snapshot(current):
        missing_text = "、".join(missing_required) if missing_required else "关键复盘字段"
        return {
            "decision_status": "blocked_for_formal_next_episode_execution",
            "can_enter_next_episode_execution": False,
            "confidence": "low",
            "blocked_reason": f"V003 仍是 {current['snapshot_label']}，缺 {missing_text}，不能生成正式下一条视频执行 prompt。",
            "missing_data": missing_required,
            "low_confidence_draft": {
                "next_primary_variable": "opening_route_or_first_5s_packaging",
                "supporting_variables": ["evidence_compression", "result_diff_display"],
                "forbidden_variables": [
                    "target_user",
                    "core_topic_direction",
                    "offer_or_monetization",
                    "multi_variable_rewrite",
                ],
                "next_content_direction": "只允许准备开头/前 5 秒包装的对照假设，不进入正式制作。",
                "next_video_structure_direction": "准备 opening_0_3s 与 bridge_3_8s 的候选结构草稿，等待 7d 与需求侧字段后再裁决。",
                "post_publish_validation_metric": [
                    "2s_bounce",
                    "5s_completion",
                    "3s_retention_if_available",
                    "average_watch_time",
                ],
            },
        }
    return {
        "decision_status": "formal_recommendation_allowed",
        "can_enter_next_episode_execution": True,
        "confidence": "medium",
        "next_primary_variable": "opening_route_or_first_5s_packaging",
    }


def load_copy_iteration_linkage(root: Path) -> dict[str, Any]:
    if not (root / COPY_ITERATION_REPORT_JSON).exists():
        return {
            "status": "missing",
            "required_when": "需要文案迭代判断、ChatGPT 汇报文案好坏或准备低置信度开头/承接简报时。",
            "run_to_generate": f"python3 {rel(COPY_ITERATION_SCRIPT)}",
            "latest_copy_iteration_report_json": rel(COPY_ITERATION_REPORT_JSON),
            "latest_copy_iteration_report_md": rel(COPY_ITERATION_REPORT_MD),
            "next_copy_revision_brief_path": rel(V003_NEXT_COPY_REVISION_BRIEF_MD),
            "decision_boundary": "缺文案迭代报告时，运营决策系统只能判断能否进入下一期，不能替 ChatGPT 输出文案修改简报。",
        }
    copy_report = load_json(root, COPY_ITERATION_REPORT_JSON)
    return {
        "status": "available",
        "latest_copy_iteration_report_json": rel(COPY_ITERATION_REPORT_JSON),
        "latest_copy_iteration_report_md": rel(COPY_ITERATION_REPORT_MD),
        "next_copy_revision_brief_path": str(copy_report.get("chatgpt_read_first") or rel(V003_NEXT_COPY_REVISION_BRIEF_MD)),
        "script_path": str(copy_report.get("paths", {}).get("script_path") or rel(COPY_ITERATION_SCRIPT)),
        "current_copy_version": copy_report.get("current_copy_version"),
        "current_data_window": copy_report.get("current_data_window"),
        "current_problem_layer": copy_report.get("current_problem_layer"),
        "confidence": copy_report.get("confidence"),
        "revision_scope_allowed": copy_report.get("revision_scope_allowed", []),
        "formal_copy_revision_allowed": False,
        "low_confidence_prepare_allowed": True,
        "status_boundary": copy_report.get("status_boundary", {}),
        "decision_boundary": "当前只允许 ChatGPT 读取 brief 后低置信度准备开头和 3-8 秒承接，不生成正式下一条视频执行 prompt。",
    }


def build_reports(root: Path) -> dict[str, Any]:
    threshold_config = load_json(root, THRESHOLD_PATH)
    classification_rules = load_json(root, CLASSIFICATION_RULES_PATH)
    index_text = read_text(root, INDEX_PATH)
    current_target_text = read_text(root, CURRENT_TARGET_PATH)
    current_anchor_text = read_text(root, CURRENT_ANCHOR_PATH)
    records_from_index = parse_index_records(index_text)

    required_ids = ["V001", "V002", "V003"]
    missing_records = [video_id for video_id in required_ids if video_id not in records_from_index]
    if missing_records:
        raise RuntimeError(f"Missing records in operation index: {', '.join(missing_records)}")

    records = [load_record(root, records_from_index[video_id], classification_rules) for video_id in required_ids]
    for record in records:
        record["data_quality"] = data_quality(record)
        record["threshold_check"] = check_thresholds(record, threshold_config)
        record["bottleneck_inference"] = infer_bottleneck(record, record["threshold_check"])
        record["summary"] = per_record_summary(record)

    synthesis = synthesize(records)
    next_decision = decide_next_episode(records, threshold_config)

    anchor_status_match = re.search(r'anchor_instance_status:\s*"([^"]+)"', current_anchor_text)
    anchor_instance_status = anchor_status_match.group(1) if anchor_status_match else "unknown"

    status_boundary = {
        "content_validation_advanced": False,
        "send_ready_advanced": False,
        "publish_status_success_advanced": False,
        "voice_validation_advanced": False,
        "final_voice_validated_advanced": False,
        "visual_master_locked_advanced": False,
        "current_data_goal_anchor_ready": anchor_instance_status == "ready",
        "next_formal_video_execution_prompt_generated": False,
    }
    copy_iteration_linkage = load_copy_iteration_linkage(root)
    v003_record = next(record for record in records if record["video_id"] == "V003")

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "system_name": "operation_decision_system",
        "source_of_truth": {
            "operation_records_index": rel(INDEX_PATH),
            "current_operation_target": rel(CURRENT_TARGET_PATH),
            "current_data_goal_anchor": rel(CURRENT_ANCHOR_PATH),
        },
        "current_project_state": {
            "formal_operation_active": "formal_operation_active" in current_target_text,
            "data_driven_operation_iteration": "data_driven_operation_iteration" in current_target_text,
            "current_data_goal_anchor_status": "partial_data_recorded"
            if "partial_data_recorded" in current_anchor_text
            else "unknown",
        },
        "records_processed": records,
        "cross_record_synthesis": synthesis,
        "next_episode_decision": next_decision,
        "copy_iteration_linkage": copy_iteration_linkage,
        "final_user_result": {
            "one_sentence_conclusion": f"当前系统已能自动读三期记录并给出判断：V003 最新为 {snapshot_phrase(v003_record)}，只能继续补数据和低置信度准备，不能进入下一期正式执行。",
            "current_primary_bottleneck": "opening_retention_and_initial_distribution_weak / draft_low_confidence",
            "can_enter_next_episode_execution": next_decision["can_enter_next_episode_execution"],
            "blocked_reason_if_not": next_decision.get("blocked_reason"),
            "recommended_next_route": "先补 V003 7d、3s_retention、V003 单条视频主页访问、私信、有效私信、有效咨询和清晰需求客户；补齐后重跑本系统，再决定唯一主变量。",
            "copy_iteration_entry": copy_iteration_linkage,
        },
        "status_boundary": status_boundary,
    }

    validate_report(report)
    return report


def validate_report(report: dict[str, Any]) -> None:
    record_ids = [record["video_id"] for record in report["records_processed"]]
    for video_id in ["V001", "V002", "V003"]:
        if video_id not in record_ids:
            raise RuntimeError(f"{video_id} was not processed")
    status_by_id = {record["video_id"]: record["record_status_rule"] for record in report["records_processed"]}
    if status_by_id["V002"] != "policy_limited_abnormal_operation_sample":
        raise RuntimeError("V002 was not classified as abnormal sample")
    if status_by_id["V003"] != "current_operation_target":
        raise RuntimeError("V003 was not classified as current operation target")
    if report["status_boundary"]["current_data_goal_anchor_ready"]:
        raise RuntimeError("current_data_goal_anchor appears ready, expected not ready")
    if report["status_boundary"]["next_formal_video_execution_prompt_generated"]:
        raise RuntimeError("formal next video execution prompt must not be generated")


def render_synthesis_md(report: dict[str, Any]) -> str:
    synthesis = report["cross_record_synthesis"]
    lines = [
        "# V001 / V002 / V003 运营三期归纳报告",
        "",
        "## 1. 三期总体结论",
    ]
    lines.extend(f"- {item}" for item in synthesis["what_is_observed"])
    lines.append("")
    lines.append("## 2. 还不能证明什么")
    lines.extend(f"- {item}" for item in synthesis["what_is_not_proven"])
    lines.append("")
    lines.append("## 3. 每期样本归纳")
    for record in report["records_processed"]:
        lines.extend(
            [
                f"### {record['video_id']}｜{record['title']}",
                f"- sample_classification: `{record['record_status_rule']}`",
                f"- data_quality: `{record['data_quality']['quality_label']}`",
                f"- 能说明：{record['summary']['can_explain']}",
                f"- 不能说明：{record['summary']['cannot_explain']}",
                f"- 对下一期价值：{record['summary']['next_value']}",
                f"- 正常归因可用：{str(record['normal_attribution_eligible']).lower()}",
                f"- 正常归因阻断原因：{record.get('normal_attribution_blocked_reason') or 'none'}",
                "",
            ]
        )
    lines.extend(
        [
            "## 4. 当前整体缺口",
            f"- {synthesis['current_largest_gap']}",
            "",
            "## 5. 距离北极星目标仍缺",
        ]
    )
    lines.extend(f"- {item}" for item in synthesis["distance_to_north_star_goal"])
    lines.append("")
    return "\n".join(lines)


def render_v003_md(report: dict[str, Any]) -> str:
    v003 = next(record for record in report["records_processed"] if record["video_id"] == "V003")
    decision = report["next_episode_decision"]
    snapshot = snapshot_phrase(v003)
    lines = [
        "# V003 运营决策结果",
        "",
        "## 1. 样本身份",
        "- `current_operation_target（当前运营目标）`",
        f"- 当前最新数据窗口：`{snapshot}`。",
        "",
        "## 2. 当前可用信号",
        f"- 播放量 {metric_value(v003, 'play_count')}，仍是极小样本。",
        f"- 2s 跳出率 {metric_value(v003, 'two_second_bounce_rate')}，5s 完播率 {metric_value(v003, 'five_second_completion_rate')}，完播率 {metric_value(v003, 'completion_rate')}。",
        f"- 收藏率 {metric_value(v003, 'favorite_rate')}，只能记为小正信号，不能写方向成立。",
        "- 评论、分享、私信、有效咨询侧仍没有可判断证据。",
        "",
        "## 3. 当前短板草稿",
        f"- `{v003['bottleneck_inference']['candidate_bottleneck']}`",
        "- 置信度：`low / draft_low_confidence`",
        "",
        "## 4. 下一期正式执行判断",
        f"- can_enter_next_episode_execution: `{str(decision['can_enter_next_episode_execution']).lower()}`",
        f"- blocked_reason: {decision.get('blocked_reason')}",
        "",
        "## 5. 缺失数据",
    ]
    lines.extend(f"- `{item}`" for item in decision.get("missing_data", []))
    lines.extend(
        [
            "",
            "## 6. 允许准备 / 不允许动作",
            "- 允许：准备开头路线、前 5 秒包装、证据压缩的低置信度候选假设。",
            "- 不允许：生成正式下一条视频执行 prompt，不允许进入新视频制作，不允许把 V003 写 ready。",
            "",
        ]
    )
    return "\n".join(lines)


def render_latest_report_md(report: dict[str, Any]) -> str:
    decision = report["next_episode_decision"]
    lines = [
        "# 最新运营决策系统报告",
        "",
        "## 系统结论",
        report["final_user_result"]["one_sentence_conclusion"],
        "",
        "## records_processed",
    ]
    for record in report["records_processed"]:
        lines.append(
            f"- {record['video_id']}: `{record['record_status_rule']}` / `{record['data_quality']['quality_label']}`"
        )
    lines.extend(
        [
            "",
            "## next_episode_decision",
            f"- decision_status: `{decision['decision_status']}`",
            f"- can_enter_next_episode_execution: `{str(decision['can_enter_next_episode_execution']).lower()}`",
            f"- confidence: `{decision['confidence']}`",
            f"- blocked_reason: {decision.get('blocked_reason')}",
            "",
            "## status_boundary",
        ]
    )
    for key, value in report["status_boundary"].items():
        lines.append(f"- {key}: `{value}`")
    copy_link = report.get("copy_iteration_linkage", {})
    lines.extend(
        [
            "",
            "## copy_iteration_linkage",
            f"- status: `{copy_link.get('status', 'missing')}`",
            f"- latest_copy_iteration_report: `{copy_link.get('latest_copy_iteration_report_md', rel(COPY_ITERATION_REPORT_MD))}`",
            f"- next_copy_revision_brief: `{copy_link.get('next_copy_revision_brief_path', rel(V003_NEXT_COPY_REVISION_BRIEF_MD))}`",
            f"- boundary: {copy_link.get('decision_boundary', '缺文案迭代报告时需要先运行 copy iteration system。')}",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def render_final_user_report_md(report: dict[str, Any]) -> str:
    decision = report["next_episode_decision"]
    missing = decision.get("missing_data", [])
    v003 = next(record for record in report["records_processed"] if record["video_id"] == "V003")
    lines = [
        "# 最终用户运营结果",
        "",
        "## 一句话结论",
        f"当前还不能进入下一期正式执行：V003 最新为 {snapshot_phrase(v003)}，系统判断只能继续补数据，并允许低置信度准备开头/前 5 秒方向草稿。",
        "",
        "## 三期样本归纳",
        "- V001：历史运营样本，只能保留为旧阶段参考；核心数据不完整，不能参与当前归因。",
        "- V002：平台审核减推异常样本，可提示平台风险表达问题；不能当作正常自然流量失败。",
        f"- V003：当前运营目标，已有 {snapshot_phrase(v003)} 的低置信度信号；还不是 7d final。",
        "",
        "## 当前最可能短板",
        "- `opening_retention_and_initial_distribution_weak（开头留存与初始分发承接弱）`，但仍是 `draft_low_confidence（低置信度草稿）`。",
        "",
        "## 当前证据不足项",
    ]
    lines.extend(f"- `{item}`" for item in missing)
    lines.extend(
        [
            "",
            "## 下一期是否可以进入正式执行",
            "- 不可以。",
            "- 原因：缺 7d、3s 留存、V003 单条视频主页访问、私信、有效私信、有效咨询和清晰需求客户等关键字段。",
            "",
            "## 如果不能执行，缺哪些数据",
        ]
    )
    lines.extend(f"- `{item}`" for item in missing)
    lines.extend(
        [
            "",
            "## 如果只能低置信度准备，允许准备什么，不允许做什么",
            "- 允许准备：开头路线、前 5 秒包装、证据压缩、结果差展示的候选方案。",
            "- 不允许做：正式下一条视频执行 prompt、新视频制作、状态升级、商业验证结论、方向成立结论。",
            "",
            "## 当前最稳路线",
            "先补 V003 的 7d 数据和需求侧字段，再重跑 `scripts/运营决策系统_operation_decision_system.py`。补齐前只做低置信度准备，不消耗下一期正式执行机会。",
            "",
            "## 文案迭代入口",
            f"- 最新文案迭代报告：`{report.get('copy_iteration_linkage', {}).get('latest_copy_iteration_report_md', rel(COPY_ITERATION_REPORT_MD))}`",
            f"- V003 下一版文案修改简报：`{report.get('copy_iteration_linkage', {}).get('next_copy_revision_brief_path', rel(V003_NEXT_COPY_REVISION_BRIEF_MD))}`",
            "- 当前下一步不是正式做新片，也不是直接改成最终稿。",
            "- 只允许低置信度准备 V003 的开头 0-3 秒和 3-8 秒承接。",
            "- 具体文案改稿由 ChatGPT 读取 `V003_next_copy_revision_brief.md` 后完成；Codex 只负责记录、结构化和报告。",
            "",
            "## 用户不用看的中间过程已由系统处理",
            "系统已经读取三期记录、分类样本、标准化指标、检查阈值、排除异常样本、生成三期归纳，并自动阻断了下一期正式执行。",
            "",
        ]
    )
    return "\n".join(lines)


def write_reports(root: Path, report: dict[str, Any]) -> None:
    write_json(root, SYNTHESIS_JSON, report["cross_record_synthesis"])
    write_text(root, SYNTHESIS_MD, render_synthesis_md(report))
    write_json(root, LATEST_REPORT_JSON, report)
    write_text(root, LATEST_REPORT_MD, render_latest_report_md(report))
    write_text(root, FINAL_USER_REPORT_MD, render_final_user_report_md(report))

    v003 = next(record for record in report["records_processed"] if record["video_id"] == "V003")
    v003_result = {
        "video_id": "V003",
        "record": v003,
        "next_episode_decision": report["next_episode_decision"],
        "status_boundary": report["status_boundary"],
    }
    write_json(root, V003_RESULT_JSON, v003_result)
    write_text(root, V003_RESULT_MD, render_v003_md(report))


def validate_output_files(root: Path) -> dict[str, Any]:
    paths = [
        SYNTHESIS_JSON,
        SYNTHESIS_MD,
        LATEST_REPORT_JSON,
        LATEST_REPORT_MD,
        FINAL_USER_REPORT_MD,
        V003_RESULT_JSON,
        V003_RESULT_MD,
    ]
    parsed_json = []
    missing_paths = []
    for path in paths:
        full_path = root / path
        if not full_path.exists():
            missing_paths.append(rel(path))
            continue
        if path.suffix == ".json":
            json.loads(full_path.read_text(encoding="utf-8"))
            parsed_json.append(rel(path))
    if missing_paths:
        raise RuntimeError(f"Missing output files: {', '.join(missing_paths)}")
    latest = load_json(root, LATEST_REPORT_JSON)
    validate_report(latest)
    return {
        "outputs_exist": [rel(path) for path in paths],
        "json_parse_passed": parsed_json,
        "records_processed": [record["video_id"] for record in latest["records_processed"]],
        "v002_abnormal": next(record for record in latest["records_processed"] if record["video_id"] == "V002")[
            "record_status_rule"
        ]
        == "policy_limited_abnormal_operation_sample",
        "v003_partial_data_recorded": latest["current_project_state"]["current_data_goal_anchor_status"]
        == "partial_data_recorded",
        "next_formal_video_execution_prompt_generated": latest["status_boundary"][
            "next_formal_video_execution_prompt_generated"
        ],
    }


def scan_for_forbidden_status(root: Path) -> dict[str, bool]:
    scan_paths = [
        CURRENT_ANCHOR_PATH,
        CURRENT_TARGET_PATH,
        Path("GPT数据源/08_当前正式事实.md"),
        LATEST_REPORT_MD,
        FINAL_USER_REPORT_MD,
    ]
    result: dict[str, bool] = {}
    for status, patterns in FORBIDDEN_STATUS_PATTERNS.items():
        found = False
        for path in scan_paths:
            text = read_text(root, path) if (root / path).exists() else ""
            lowered = text.lower()
            if any(pattern.lower() in lowered for pattern in patterns):
                found = True
                break
        result[status] = found
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build operation decision reports from repo operation records.")
    parser.add_argument("--root", default=str(ROOT), help="Repository root")
    parser.add_argument("--validate-only", action="store_true", help="Validate generated outputs without rewriting")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.validate_only:
        validation = validate_output_files(root)
    else:
        report = build_reports(root)
        write_reports(root, report)
        validation = validate_output_files(root)
    forbidden_scan = scan_for_forbidden_status(root)
    validation["forbidden_status_scan"] = forbidden_scan
    validation["forbidden_status_advanced"] = any(forbidden_scan.values())
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    if validation["forbidden_status_advanced"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
