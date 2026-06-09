#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DATA_KEYWORDS = [
    "播放",
    "点赞",
    "收藏",
    "2 秒跳出",
    "2秒跳出",
    "3 秒留存",
    "3秒留存",
    "5 秒完播",
    "5秒完播",
    "完播率",
    "平均观看",
    "主页访问",
    "评论",
    "私信",
    "有效咨询",
    "客资",
]

REAL_METRIC_PATTERNS = [
    re.compile(r"(播放量?|点赞|收藏|评论|主页访问|私信|有效咨询|客资)\s*[：: ]+\s*\d"),
    re.compile(r"(完播率|留存率|跳出率|平均观看)\s*[：: ]+\s*\d"),
    re.compile(r"\d+(?:\.\d+)?%"),
]

PROTECTED_VISUAL_ROLES = {"middle_evidence", "opening_evidence", "ending_support"}

CARD_PRIORITY = {
    "data_result_card": 100,
    "key_judgment_card": 90,
    "judgment_card": 90,
    "ending_summary_card": 80,
    "boundary_card": 70,
    "summary_card": 60,
    "process_summary_card": 50,
    "result_diff_card": 50,
    "prompt_tail_card": 30,
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def group_id(group: dict[str, Any]) -> str:
    return str(group.get("line_group_id") or group.get("id") or "")


def group_text(group: dict[str, Any]) -> str:
    parts = [
        str(group.get("narration_text") or group.get("text") or ""),
        str(group.get("line_group_goal") or ""),
        str(group.get("card_text") or group.get("card_text_if_any") or ""),
    ]
    return "\n".join(part for part in parts if part)


def visual_role(group: dict[str, Any]) -> str:
    return str(group.get("visual_role") or "")


def required_material(group: dict[str, Any]) -> str:
    return str(group.get("required_material") or "")


def normalize_card_role(group: dict[str, Any]) -> str:
    role = str(group.get("card_role") or "")
    if role in {"", "none", "no_card"} and required_material(group) == "generated_card":
        role = visual_role(group)
    if role == "summary_card" and visual_role(group) == "ending_summary_card":
        return "ending_summary_card"
    return role


def parse_clock(value: str) -> float | None:
    match = re.match(r"^(\d{2}):(\d{2}):(\d{2}),(\d{3})$", value.strip())
    if not match:
        return None
    hours, minutes, seconds, millis = [int(part) for part in match.groups()]
    return hours * 3600 + minutes * 60 + seconds + millis / 1000


def parse_timeline_slot(slot: str) -> tuple[float | None, float | None]:
    if not slot or "-" not in slot:
        return None, None
    start_raw, end_raw = slot.split("-", 1)
    return parse_clock(start_raw), parse_clock(end_raw)


def group_start(group: dict[str, Any]) -> float:
    start, _ = parse_timeline_slot(str(group.get("timeline_slot") or ""))
    return start if start is not None else 0.0


def group_end(group: dict[str, Any]) -> float:
    _, end = parse_timeline_slot(str(group.get("timeline_slot") or ""))
    return end if end is not None else group_start(group)


def calculate_duration(line_groups: list[dict[str, Any]], override: float | None = None) -> float:
    if override is not None:
        return float(override)
    ends = [group_end(group) for group in line_groups]
    return max(ends) if ends else 0.0


def card_budget_gate(video_duration: float) -> dict[str, Any]:
    if video_duration <= 90:
        max_main_cards = 3
        optional_extra = False
    elif video_duration <= 180:
        max_main_cards = 4
        optional_extra = "1 only if data_result_card is missing and evidence supports it"
    else:
        max_main_cards = 6
        optional_extra = False
    return {
        "video_duration": round(video_duration, 3),
        "max_main_cards": max_main_cards,
        "optional_extra_card_allowed": optional_extra,
        "min_gap_between_main_cards_sec": 25,
        "hard_min_gap_sec": 18,
        "no_back_to_back_generated_cards": True,
        "priority_order": [
            "data_result_card",
            "key_judgment_card",
            "ending_summary_card",
            "boundary_card",
            "process_summary_card",
        ],
    }


def has_data_keyword(text: str) -> bool:
    return any(keyword in text for keyword in DATA_KEYWORDS)


def has_real_metric_values(groups: list[dict[str, Any]]) -> bool:
    for group in groups:
        if group.get("real_metric_values"):
            return True
        text = group_text(group)
        if any(pattern.search(text) for pattern in REAL_METRIC_PATTERNS):
            return True
    return False


def has_diagnosis_or_judgment(groups: list[dict[str, Any]]) -> bool:
    text = "\n".join(group_text(group) for group in groups)
    signals = ["判断", "问题", "不能", "不是", "不够", "误判", "怀疑", "风险", "不硬猜", "待确认", "缺失", "废了"]
    return any(signal in text for signal in signals)


def has_next_variable_or_action(groups: list[dict[str, Any]]) -> bool:
    text = "\n".join(group_text(group) for group in groups)
    signals = ["下一条只改", "下一轮", "只改", "变量", "先改", "改完看", "动作"]
    return any(signal in text for signal in signals)


def has_strong_next_variable_signal(groups: list[dict[str, Any]]) -> bool:
    text = "\n".join(group_text(group) for group in groups)
    signals = ["下一条只改", "下一轮", "只改", "先改", "改完看"]
    return any(signal in text for signal in signals)


def has_validation_metric(groups: list[dict[str, Any]]) -> bool:
    text = "\n".join(group_text(group) for group in groups)
    if "validation_metric" in text or "改完看" in text:
        return True
    return has_data_keyword(text) and any(signal in text for signal in ["指标", "留存", "完播", "平均观看"])


def has_explicit_data_result_phrase(groups: list[dict[str, Any]]) -> bool:
    text = "\n".join(group_text(group) for group in groups)
    signals = ["改完看", "下一条先改", "下一条只改", "先改哪个变量"]
    return any(signal in text for signal in signals)


def data_source_unclear(groups: list[dict[str, Any]]) -> bool:
    unclear_values = {"unclear", "unknown", "missing", "source_unclear", "unverified"}
    for group in groups:
        status = str(group.get("data_source_status") or "").strip().lower()
        if status in unclear_values:
            return True
    return False


def classify_group(group: dict[str, Any]) -> str:
    role = normalize_card_role(group)
    text = group_text(group)
    if role == "boundary_card" or any(signal in text for signal in ["待确认", "缺失", "不会乱猜", "不硬猜", "不是保证"]):
        return "boundary_cluster"
    if has_data_keyword(text) or any(signal in text for signal in ["变量", "指标", "数据", "字段"]):
        return "data_cluster"
    if any(signal in text for signal in ["判断", "不能", "不是", "误判", "问题"]):
        return "judgment_cluster"
    if role in {"summary_card", "ending_summary_card"} or any(signal in text for signal in ["总结", "收束", "留下", "解决"]):
        return "summary_cluster"
    if any(signal in text for signal in ["第一步", "第二步", "第三步", "第四步", "第五步", "第六步", "流程", "配置"]):
        return "process_cluster"
    return "no_card_cluster"


def build_card_cluster_map(line_groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    clusters: list[dict[str, Any]] = []
    current_type = ""
    current_groups: list[dict[str, Any]] = []

    def flush() -> None:
        if not current_groups or current_type == "no_card_cluster":
            return
        cluster_index = len(clusters) + 1
        line_group_ids = [group_id(group) for group in current_groups]
        clusters.append(
            {
                "cluster_id": f"card_cluster_{cluster_index:03d}",
                "line_group_ids": line_group_ids,
                "cluster_type": current_type,
                "key_information": " / ".join(group_text(group).splitlines()[0] for group in current_groups if group_text(group))[:220],
                "candidate_card_type": candidate_card_type_for_cluster(current_type),
                "merge_reason": "contiguous_line_groups_share_copy_function",
                "selected_or_dropped": "pending_budget_and_evidence_check",
                "reason": "cluster_merge_rule groups 1-5 line_groups before card selection",
            }
        )

    for group in line_groups:
        next_type = classify_group(group)
        if next_type != current_type or len(current_groups) >= 5:
            flush()
            current_type = next_type
            current_groups = [group]
        else:
            current_groups.append(group)
    flush()
    return clusters


def candidate_card_type_for_cluster(cluster_type: str) -> str:
    return {
        "data_cluster": "data_result_card",
        "judgment_cluster": "judgment_card",
        "boundary_cluster": "boundary_card",
        "summary_cluster": "summary_card",
        "process_cluster": "process_summary_card",
    }.get(cluster_type, "no_card")


def find_best_data_window(line_groups: list[dict[str, Any]]) -> dict[str, Any] | None:
    best: dict[str, Any] | None = None
    for start_index in range(len(line_groups)):
        for length in range(1, 6):
            window = line_groups[start_index : start_index + length]
            if len(window) != length:
                continue
            if any(required_material(group) == "generated_card" or normalize_card_role(group) not in {"", "none", "no_card"} for group in window):
                continue
            text = "\n".join(group_text(group) for group in window)
            has_data = has_data_keyword(text)
            has_real = has_real_metric_values(window)
            has_judgment = has_diagnosis_or_judgment(window)
            has_next = has_next_variable_or_action(window)
            has_strong_next = has_strong_next_variable_signal(window)
            has_validation = has_validation_metric(window)
            has_explicit_result = has_explicit_data_result_phrase(window)
            score = sum([has_data, has_real, has_judgment, has_next, has_validation])
            if not has_data or score < 3:
                continue
            candidate = {
                "line_group_ids": [group_id(group) for group in window],
                "start_sec": group_start(window[0]),
                "end_sec": group_end(window[-1]),
                "has_real_metric_values": has_real,
                "has_diagnosis_or_judgment": has_judgment,
                "has_next_variable_or_action": has_next,
                "has_strong_next_variable_signal": has_strong_next,
                "has_explicit_data_result_phrase": has_explicit_result,
                "has_validation_metric": has_validation,
                "data_source_clear": not data_source_unclear(window),
                "score": score,
                "key_information": " / ".join(group_text(group).splitlines()[0] for group in window if group_text(group))[:260],
            }
            if best is None or (
                int(candidate["has_real_metric_values"]),
                int(candidate["has_explicit_data_result_phrase"]),
                int(candidate["has_strong_next_variable_signal"]),
                candidate["score"],
                length,
            ) > (
                int(best["has_real_metric_values"]),
                int(best["has_explicit_data_result_phrase"]),
                int(best["has_strong_next_variable_signal"]),
                best["score"],
                len(best["line_group_ids"]),
            ):
                best = candidate
    return best


def evaluate_data_result_card(line_groups: list[dict[str, Any]]) -> dict[str, Any] | None:
    window = find_best_data_window(line_groups)
    if not window:
        return None
    required_ok = (
        window["has_real_metric_values"]
        and window["has_diagnosis_or_judgment"]
        and window["has_next_variable_or_action"]
        and window["has_validation_metric"]
        and window["data_source_clear"]
    )
    if required_ok:
        status = "selected"
        reason = "real_metrics_plus_judgment_next_variable_and_validation_metric"
    elif not window["data_source_clear"]:
        status = "candidate_blocked_data_source_unclear"
        reason = "data_source_unclear_boundary_or_pending_only"
    elif not window["has_real_metric_values"]:
        status = "candidate_blocked_missing_real_metric_values"
        reason = "metric_names_or_workflow_fields_are_not_real_metric_values"
    else:
        status = "candidate_dropped_missing_required_trigger"
        reason = "data_result_card_requires_real_metrics_judgment_next_variable_and_validation_metric"
    return {
        "card_type": "data_result_card",
        "line_group_ids": window["line_group_ids"],
        "start_sec": round(window["start_sec"], 3),
        "end_sec": round(window["end_sec"], 3),
        "selected_or_dropped": status,
        "reason": reason,
        "output_shape": {
            "原始数据": "required_real_metric_values",
            "AI 判断": "required_problem_layer_and_boundary",
            "下一条只改": "required_primary_variable",
            "改完看": "required_validation_metrics",
        },
        "trigger_check": {
            "real_metric_values": window["has_real_metric_values"],
            "diagnosis_or_judgment": window["has_diagnosis_or_judgment"],
            "next_variable_or_action": window["has_next_variable_or_action"],
            "validation_metric": window["has_validation_metric"],
            "data_source_clear": window["data_source_clear"],
        },
        "key_information": window["key_information"],
    }


def extract_existing_cards(line_groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for group in line_groups:
        role = normalize_card_role(group)
        if role in {"", "none", "no_card"}:
            continue
        if "card" not in role:
            continue
        cards.append(
            {
                "line_group_id": group_id(group),
                "card_type": role,
                "current_visual_role": visual_role(group),
                "timeline_slot": str(group.get("timeline_slot") or ""),
                "start_sec": round(group_start(group), 3),
                "end_sec": round(group_end(group), 3),
                "function": str(group.get("line_group_goal") or ""),
                "source": "existing_card",
                "evidence_window_safe": not (
                    visual_role(group) in PROTECTED_VISUAL_ROLES and required_material(group) != "generated_card"
                ),
            }
        )
    return cards


def apply_evidence_window_protection(cards: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    selected: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    for card in cards:
        if card.get("evidence_window_safe", True):
            selected.append(card)
        else:
            blocked_card = dict(card)
            blocked_card["selected_or_dropped"] = "dropped"
            blocked_card["reason"] = "card_interrupts_key_evidence"
            blocked.append(blocked_card)
    return selected, blocked


def priority(card: dict[str, Any]) -> int:
    return CARD_PRIORITY.get(str(card.get("card_type") or ""), 0)


def apply_budget_and_spacing(cards: list[dict[str, Any]], budget: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    selected = sorted(cards, key=lambda card: (-priority(card), float(card.get("start_sec") or 0)))
    dropped: list[dict[str, Any]] = []
    selected = selected[: int(budget["max_main_cards"])]
    if len(cards) > len(selected):
        kept_ids = {card_identity(card) for card in selected}
        for card in cards:
            if card_identity(card) not in kept_ids:
                dropped_card = dict(card)
                dropped_card["selected_or_dropped"] = "dropped"
                dropped_card["reason"] = "over_budget_lower_priority"
                dropped.append(dropped_card)

    spacing_warnings: list[dict[str, Any]] = []
    selected_by_time = sorted(selected, key=lambda card: float(card.get("start_sec") or 0))
    for previous, current in zip(selected_by_time, selected_by_time[1:]):
        gap = float(current.get("start_sec") or 0) - float(previous.get("end_sec") or previous.get("start_sec") or 0)
        warning = {
            "previous": card_identity(previous),
            "current": card_identity(current),
            "gap_sec": round(gap, 3),
        }
        if gap < float(budget["hard_min_gap_sec"]):
            lower = current if priority(previous) >= priority(current) else previous
            if lower in selected:
                selected.remove(lower)
            dropped_card = dict(lower)
            dropped_card["selected_or_dropped"] = "dropped"
            dropped_card["reason"] = "hard_min_gap_violation_lower_priority"
            dropped.append(dropped_card)
            warning["status"] = "hard_gap_drop"
        elif gap < float(budget["min_gap_between_main_cards_sec"]):
            warning["status"] = "soft_spacing_warning"
        else:
            warning["status"] = "passed"
        spacing_warnings.append(warning)
    return sorted(selected, key=lambda card: float(card.get("start_sec") or 0)), dropped, spacing_warnings


def card_identity(card: dict[str, Any]) -> str:
    if card.get("line_group_id"):
        return str(card["line_group_id"])
    return "+".join(str(item) for item in card.get("line_group_ids", []))


def build_recommendation(
    existing_cards: list[dict[str, Any]],
    data_card: dict[str, Any] | None,
    selected_cards: list[dict[str, Any]],
    dropped_cards: list[dict[str, Any]],
    clusters: list[dict[str, Any]],
) -> dict[str, Any]:
    selected_ids = {card_identity(card) for card in selected_cards}
    keep = [card for card in existing_cards if card_identity(card) in selected_ids]
    replace: list[dict[str, Any]] = []
    process_cards = [card for card in existing_cards if card.get("card_type") == "process_summary_card"]
    if data_card and process_cards:
        replace.append(
            {
                "from": process_cards[0]["line_group_id"],
                "from_card_type": "process_summary_card",
                "to": "data_result_card",
                "status": data_card["selected_or_dropped"],
                "reason": data_card["reason"],
                "data_result_line_group_ids": data_card["line_group_ids"],
            }
        )
    merge = [
        {
            "cluster_id": cluster["cluster_id"],
            "line_group_ids": cluster["line_group_ids"],
            "candidate_card_type": cluster["candidate_card_type"],
            "reason": cluster["merge_reason"],
        }
        for cluster in clusters
        if len(cluster["line_group_ids"]) > 1 and cluster["cluster_type"] != "no_card_cluster"
    ]
    return {
        "keep": keep,
        "merge": merge,
        "replace": replace,
        "drop": dropped_cards,
        "add_data_result_card_candidate": data_card,
    }


def run_card_decision(
    line_groups: list[dict[str, Any]],
    *,
    video_duration_override: float | None = None,
    content_route_card: dict[str, Any] | None = None,
) -> dict[str, Any]:
    video_duration = calculate_duration(line_groups, video_duration_override)
    budget = card_budget_gate(video_duration)
    existing_cards = extract_existing_cards(line_groups)
    clusters = build_card_cluster_map(line_groups)
    data_card = evaluate_data_result_card(line_groups)

    candidate_cards = list(existing_cards)
    pre_dropped_cards: list[dict[str, Any]] = []
    if data_card and data_card["selected_or_dropped"] == "selected":
        candidate_cards.append(
            {
                "card_type": "data_result_card",
                "line_group_ids": data_card["line_group_ids"],
                "start_sec": data_card["start_sec"],
                "end_sec": data_card["end_sec"],
                "function": "data_result_card_priority",
                "source": "card_decision_helper",
                "evidence_window_safe": True,
            }
        )
        remaining_candidates: list[dict[str, Any]] = []
        for card in candidate_cards:
            if card.get("card_type") == "process_summary_card":
                dropped_card = dict(card)
                dropped_card["selected_or_dropped"] = "dropped"
                dropped_card["reason"] = "data_result_card_priority_replaces_process_summary_card"
                pre_dropped_cards.append(dropped_card)
            else:
                remaining_candidates.append(card)
        candidate_cards = remaining_candidates

    evidence_safe_cards, evidence_blocked = apply_evidence_window_protection(candidate_cards)
    selected_cards, budget_dropped, spacing_warnings = apply_budget_and_spacing(evidence_safe_cards, budget)
    dropped_cards = pre_dropped_cards + evidence_blocked + budget_dropped

    current_card_types = [card["card_type"] for card in existing_cards]
    recommendation = build_recommendation(existing_cards, data_card, selected_cards, dropped_cards, clusters)
    return {
        "card_decision_dry_run": {
            "video_duration": round(video_duration, 3),
            "card_budget": budget,
            "detected_clusters": clusters,
            "candidate_cards": candidate_cards,
            "selected_cards": selected_cards,
            "dropped_or_merged_cards": dropped_cards,
            "spacing_warnings": spacing_warnings,
            "reasons": {
                "selection_policy": "data_result_card > key_judgment_card > ending_summary_card > boundary_card > process_summary_card",
                "sentence_level_cards_forbidden": True,
                "cluster_merge_rule_applied": True,
            },
            "evidence_window_protection_result": {
                "status": "passed" if not evidence_blocked else "blocked_cards_dropped",
                "blocked_cards": evidence_blocked,
                "protected_visual_roles": sorted(PROTECTED_VISUAL_ROLES),
            },
            "hyperframes_unchanged_check": {
                "visual_route_changed": False,
                "motion_route_changed": False,
                "skin_changed": False,
                "existing_hyperframes_fields_preserved": True,
                "content_route_card_read": content_route_card is not None,
            },
        },
        "fourth_episode_card_decision_dry_run": {
            "original_cards": existing_cards,
            "new_rule_selected_cards": selected_cards,
            "recommended_adjustment": recommendation,
            "keep": recommendation["keep"],
            "merge": recommendation["merge"],
            "replace": recommendation["replace"],
            "drop": recommendation["drop"],
            "add_data_result_card_candidate": data_card,
            "reason": "data_result_card requires real metric values; process_summary_card is lower priority when supported data exists",
            "total_card_count_after_rule": len(selected_cards),
            "evidence_window_protection_result": "passed" if not evidence_blocked else "blocked_cards_dropped",
            "hyperframes_unchanged_check": "passed_no_visual_motion_skin_change",
            "no_video_regenerated": True,
            "current_problem": {
                "missing_card_types": ["data_result_card"] if "data_result_card" not in current_card_types else [],
                "over_card_risk": "low" if len(existing_cards) <= budget["max_main_cards"] else "high",
                "under_card_risk": "data_result_card_missing_or_pending",
            },
        },
    }


def evaluate_card_visual_route(route: dict[str, Any]) -> dict[str, Any]:
    """Validate route-layer card decisions without generating media."""
    visual_base_route = route.get("visual_base_route")
    text_authority_route = route.get("text_authority_route")
    motion_wrapper_route = route.get("motion_wrapper_route", "none")
    hyperframes_runtime_status = route.get("hyperframes_runtime_status")
    image2_text_status = route.get("image2_generated_text_status", "not_used_for_final_text")
    overlay_available = bool(route.get("post_overlay_locked_copy_check"))
    social_style_status = route.get("social_editorial_card_v1_status", "pass")

    blocked_reasons: list[str] = []
    human_review_required = False

    if visual_base_route == "image2_visual_base_route_candidate" and image2_text_status == "mismatch" and not overlay_available:
        blocked_reasons.append("image2_text_semantic_mismatch_unfixable")
    if route.get("generated_fake_data_or_claim"):
        blocked_reasons.append("generated_fake_data_or_claim")
    if route.get("evidence_window_covered"):
        blocked_reasons.append("evidence_window_covered")
    if route.get("third_party_asset_detected"):
        blocked_reasons.append("third_party_asset_detected")
    if social_style_status == "deviation":
        human_review_required = True
        blocked_reasons.append("social_editorial_card_v1_deviation")
    if not route.get("post_overlay_readability_check", True):
        blocked_reasons.append("post_overlay_readability_check_missing")
    if motion_wrapper_route == "HyperFrames_motion_wrapper" and hyperframes_runtime_status in {"missing", "not_found", "not_verified", None}:
        blocked_reasons.append("hyperframes_motion_wrapper_selected_but_runtime_missing")

    return {
        "card_visual_route_selected": True,
        "visual_base_route": visual_base_route,
        "text_authority_route": text_authority_route,
        "motion_wrapper_route": motion_wrapper_route,
        "image2_visual_only_not_text_authority": visual_base_route == "image2_visual_base_route_candidate",
        "hyperframes_runtime_gate_required": motion_wrapper_route == "HyperFrames_motion_wrapper",
        "blocked": bool(blocked_reasons),
        "blocked_reasons": blocked_reasons,
        "human_review_required": human_review_required,
    }


def load_line_groups(path: Path) -> list[dict[str, Any]]:
    payload = read_json(path)
    if isinstance(payload, dict):
        line_groups = payload.get("line_groups")
        if isinstance(line_groups, list):
            return line_groups
    if isinstance(payload, list):
        return payload
    raise ValueError(f"line_groups_not_found:{path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run card budget and data_result_card decisions.")
    parser.add_argument("--timeline", required=True, type=Path)
    parser.add_argument("--content-route-card", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--video-duration", type=float)
    args = parser.parse_args()

    line_groups = load_line_groups(args.timeline)
    content_route_card = read_json(args.content_route_card) if args.content_route_card else None
    report = run_card_decision(
        line_groups,
        video_duration_override=args.video_duration,
        content_route_card=content_route_card,
    )
    if args.output:
        write_json(args.output, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
