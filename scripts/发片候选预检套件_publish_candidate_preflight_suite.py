#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from 正片候选TTS路线_publish_candidate_tts_route import (
    B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE,
    REQUIRED_MINIMAX_MODELS,
    validate_b_voice_feel_minimax_route,
    validate_publish_candidate_tts_route,
)
from 素材解析包复用闸门_material_parse_pack_reuse_gate import run_material_parse_pack_reuse_gate
from 素材证据闸门_material_evidence_gate import run_material_evidence_gate


ROOT = Path(__file__).resolve().parents[1]

GATES = [
    "material_parse_pack_reuse_preflight",
    "material_evidence_gate_preflight",
    "line_level_alignment_preflight",
    "line_visual_tolerance_preflight",
    "near_equivalent_material_substitution_preflight",
    "tts_route_and_prosody_preflight",
    "publish_candidate_voice_gate",
    "b_voice_feel_minimax_preflight",
    "card_decision_preflight",
    "forbidden_action_preflight",
    "visual_evidence_readability_preflight",
    "locked_copy_diff_preflight",
    "publish_candidate_user_standard_preflight",
    "completion_truth_preflight",
]

REPORT_FILENAMES = {
    "material_parse_pack_reuse_preflight": "material_parse_pack_reuse_report",
    "material_evidence_gate_preflight": "material_evidence_gate_preflight_report",
    "line_level_alignment_preflight": "line_level_alignment_report",
    "line_visual_tolerance_preflight": "line_visual_tolerance_report",
    "near_equivalent_material_substitution_preflight": "near_equivalent_material_substitution_report",
    "tts_route_and_prosody_preflight": "tts_route_and_prosody_report",
    "publish_candidate_voice_gate": "tts_route_report",
    "b_voice_feel_minimax_preflight": "b_voice_feel_minimax_report",
    "card_decision_preflight": "card_decision_preflight_report",
    "forbidden_action_preflight": "forbidden_action_audit",
    "visual_evidence_readability_preflight": "visual_evidence_readability_report",
    "locked_copy_diff_preflight": "locked_copy_diff_report",
    "publish_candidate_user_standard_preflight": "publish_candidate_user_standard_report",
    "completion_truth_preflight": "completion_truth_preflight_report",
}

CARD_TYPES = [
    "judgment_card",
    "summary_card",
    "result_diff_card",
    "boundary_card",
    "prompt_tail_card",
]

FORBIDDEN_ACTIONS = [
    "changed_locked_title",
    "changed_locked_opening_line",
    "changed_locked_final_script_semantics",
    "removed_required_judgment_card",
    "removed_required_boundary_card",
    "changed_tts_route_without_authorization",
    "used_fallback_without_authorization",
    "added_default_mask_or_whiteout",
    "changed_source_ratio_without_authorization",
    "card_replaced_user_recording_evidence",
    "generated_technical_preview_as_delivery",
    "wrote_completed_with_missing_inventory",
    "advanced_content_validation",
    "advanced_send_ready",
    "advanced_voice_validation",
    "advanced_visual_master_locked",
]

REVIEW_PACK_REQUIRED_PREFLIGHT_REPORTS = [
    "publish_candidate_preflight_report.json",
    "publish_candidate_preflight_report.md",
    "material_parse_pack_reuse_report.json",
    "material_parse_pack_reuse_report.md",
    "material_evidence_gate_preflight_report.json",
    "material_evidence_gate_preflight_report.md",
    "material_evidence_contract.json",
    "line_group_evidence_gate_report.json",
    "auto_storyboard_preflight_report.json",
    "line_level_alignment_report.json",
    "line_visual_tolerance_report.json",
    "near_equivalent_material_substitution_report.json",
    "tts_route_and_prosody_report.json",
    "tts_route_report.json",
    "tts_route_report.md",
    "b_voice_feel_minimax_report.json",
    "card_decision_preflight_report.json",
    "forbidden_action_audit.json",
    "visual_evidence_readability_report.json",
    "locked_copy_diff_report.json",
    "publish_candidate_user_standard_report.json",
    "completion_truth_preflight_report.json",
]

CORE_EVIDENCE_LINE_TYPES = {
    "product_card_field",
    "candidate_table",
    "detail_table",
    "review_table",
    "product_review_priority",
    "boundary_statement",
    "result_diff",
    "next_action",
    "cost_or_commission_claim",
    "risk_claim",
}
ALLOWED_MINOR_FLAWS = {
    "tiny_timing_imperfection",
    "minor_non_core_visual_transition_issue",
    "slight_subtitle_pacing_issue_not_affecting_understanding",
    "small_aesthetic_imperfection_not_affecting_publish",
}
FORBIDDEN_MAJOR_FLAWS = {
    "locked_copy_changed",
    "title_changed",
    "voice_route_wrong",
    "fallback_tts_used",
    "silent_audio",
    "line_visual_whole_video_drift",
    "core_evidence_mismatch",
    "subtitle_blocks_core_evidence",
    "card_blocks_core_evidence",
    "gray_border_or_black_border_obvious",
    "whiteout_or_black_block_present",
    "full_frame_mask_or_unapproved_redaction",
    "only_internal_diagnostic",
    "only_technical_preview",
    "only_json_or_markdown_package",
    "no_review_pack",
    "no_preflight_suite",
    "completion_claim_without_validation",
}
LINE_VISUAL_TOLERANCE_RULE = {
    "status": "active",
    "applies_to": [
        "locked_copy_video_execution",
        "publish_candidate_delivery",
        "video_repair_execution",
        "final_script_to_video",
    ],
    "tolerance_policy": {
        "max_near_equivalent_ratio": 0.05,
        "max_consecutive_near_equivalent_groups": 1,
        "whole_video_drift_allowed": False,
        "core_evidence_mismatch_allowed": False,
    },
    "allowed_near_equivalent_if": [
        "line_group_is_non_core_evidence",
        "visual_proves_same_claim",
        "material_role_is_same_or_stronger",
        "viewer_inference_is_unchanged",
        "no_change_to_locked_copy_meaning",
        "no_change_from_review_to_recommendation",
        "no_change_from_initial_screening_to_final_decision",
        "no_new_commercial_claim",
    ],
    "forbidden_near_equivalent_if": [
        "line_group_is_core_evidence",
        "line_group_is_boundary_statement",
        "line_group_is_result_diff",
        "line_group_is_product_or_table_proof",
        "visual_changes_claim",
        "visual_requires_guessing",
        "material_only_thematically_related",
        "mismatch_repeats_across_multiple_sections",
    ],
    "core_evidence_line_types": sorted(CORE_EVIDENCE_LINE_TYPES),
    "required_report": [
        "line_visual_alignment_report",
        "near_equivalent_material_substitution_report",
    ],
    "blocked_if": [
        "near_equivalent_ratio > 0.05",
        "core_evidence_mismatch_count > 0",
        "whole_video_drift_detected = true",
        "visual_requires_guessing = true",
        "replacement_material_not_extremely_close = true",
        "user_material_needed_but_missing = true",
    ],
}


def read_json(path: Path | None, label: str) -> tuple[Any | None, list[str]]:
    if path is None:
        return None, [f"{label}_missing"]
    if not path.exists():
        return None, [f"{label}_missing:{rel(path)}"]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"{label}_json_parse_error:{exc}"]


def read_text(path: Path | None, label: str) -> tuple[str, list[str]]:
    if path is None:
        return "", [f"{label}_missing"]
    if not path.exists():
        return "", [f"{label}_missing:{rel(path)}"]
    try:
        return path.read_text(encoding="utf-8"), []
    except UnicodeDecodeError as exc:
        return "", [f"{label}_decode_error:{exc}"]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(path: Path, report: dict[str, Any]) -> None:
    lines = [
        f"# {report.get('gate_name', report.get('schema', 'preflight_report'))}",
        "",
        f"- `status`: `{report.get('status')}`",
        f"- `check_depth`: `{report.get('check_depth')}`",
    ]
    reasons = report.get("blocked_reasons") or []
    if reasons:
        lines.append("- `blocked_reasons`:")
        lines.extend(f"  - `{reason}`" for reason in reasons)
    warnings = report.get("warnings") or []
    if warnings:
        lines.append("- `warnings`:")
        lines.extend(f"  - `{warning}`" for warning in warnings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def line_groups_from_timeline(timeline: Any) -> list[dict[str, Any]]:
    if not isinstance(timeline, dict):
        return []
    candidates = [
        timeline.get("line_groups"),
        timeline.get("script_to_timeline_map", {}).get("line_groups")
        if isinstance(timeline.get("script_to_timeline_map"), dict)
        else None,
        timeline.get("timeline", {}).get("line_groups")
        if isinstance(timeline.get("timeline"), dict)
        else None,
    ]
    for candidate in candidates:
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return []


def flatten_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(flatten_text(item) for item in value)
    if isinstance(value, dict):
        return "\n".join(f"{key}:{flatten_text(item)}" for key, item in value.items())
    return str(value)


def normalize_copy(text: str) -> str:
    text = str(text)
    text = re.sub(r"<break[^>]*>", "", text, flags=re.I)
    text = re.sub(r"\b(pause|break|silence)\s*[:=]?\s*\d+(\.\d+)?s?\b", "", text, flags=re.I)
    text = re.sub(r"(停顿|停顿时长|静音)\s*[:=：]?\s*\d+(\.\d+)?秒?", "", text)
    text = text.replace("≠", "不等于").replace("＝", "等于").replace("=", "等于")
    text = re.sub(r"[\s，。！？；：,.!?;:、\"'“”‘’（）()【】\[\]《》<>《》「」『』\-—_/\\\\|·]+", "", text)
    return text.lower()


def compact_copy(text: str) -> str:
    return re.sub(r"\s+", "", str(text or "").strip())


def sentence_units(text: str) -> list[str]:
    units: list[str] = []
    for line in str(text or "").replace("\r\n", "\n").split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = re.findall(r"[^。！？!?；;]+[。！？!?；;]?", line)
        if not parts:
            parts = [line]
        units.extend(part.strip() for part in parts if part.strip())
    return units


def extract_timeline_narration(timeline: Any) -> str:
    return "\n".join(flatten_text(group.get("narration_text")) for group in line_groups_from_timeline(timeline))


def parse_srt_text(text: str) -> str:
    lines: list[str] = []
    for raw in str(text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.isdigit():
            continue
        if "-->" in line:
            continue
        lines.append(line)
    return "\n".join(lines)


def parse_ass_text(text: str) -> str:
    lines: list[str] = []
    for raw in str(text or "").splitlines():
        line = raw.strip()
        if not line.startswith("Dialogue:"):
            continue
        fields = line.split(",", 9)
        dialogue_text = fields[-1] if fields else line
        dialogue_text = re.sub(r"\{[^}]*\}", "", dialogue_text)
        dialogue_text = dialogue_text.replace(r"\N", "\n").replace(r"\n", "\n").replace(r"\h", " ")
        lines.append(dialogue_text)
    return "\n".join(lines)


def extract_tts_input_text(tts_map: Any, tts_route_report: Any) -> str:
    texts: list[str] = []
    if isinstance(tts_route_report, dict):
        reports = tts_route_report.get("segment_reports")
        if isinstance(reports, list):
            for item in reports:
                if isinstance(item, dict):
                    text = item.get("tts_text") or item.get("text") or item.get("narration_text")
                    if text:
                        texts.append(flatten_text(text))
        if not texts:
            text = tts_route_report.get("actual_tts_text") or tts_route_report.get("tts_text")
            if text:
                texts.append(flatten_text(text))
    if not texts and isinstance(tts_map, dict):
        anchors = tts_map.get("anchors")
        if isinstance(anchors, list):
            for item in anchors:
                if isinstance(item, dict):
                    text = item.get("tts_text") or item.get("narration_text")
                    if text:
                        texts.append(flatten_text(text))
        if not texts:
            text = tts_map.get("actual_tts_text") or tts_map.get("tts_text")
            if text:
                texts.append(flatten_text(text))
    return "\n".join(texts)


def card_text_entries(card_placement: Any) -> list[dict[str, Any]]:
    if not isinstance(card_placement, dict):
        return []
    groups = card_placement.get("card_groups")
    if groups is None:
        groups = card_placement.get("cards")
    if not isinstance(groups, list):
        return []
    entries: list[dict[str, Any]] = []
    for index, group in enumerate(groups):
        if not isinstance(group, dict):
            continue
        card_text = group.get("card_text")
        values: list[str] = []
        if isinstance(card_text, dict):
            for key in ["title", "subtitle", "body", "footer"]:
                if card_text.get(key):
                    values.append(flatten_text(card_text.get(key)))
            columns = card_text.get("columns")
            if isinstance(columns, list):
                values.extend(flatten_text(item) for item in columns)
        elif card_text:
            values.append(flatten_text(card_text))
        entries.append(
            {
                "index": index,
                "line_group_id": str(group.get("line_group_id") or group.get("id") or ""),
                "card_role": str(group.get("card_role") or group.get("type") or ""),
                "text_values": [value for value in values if value],
            }
        )
    return entries


def timeline_text_by_group(timeline: Any) -> dict[str, str]:
    bound: dict[str, str] = {}
    for index, group in enumerate(line_groups_from_timeline(timeline), start=1):
        group_id = str(group.get("line_group_id") or group.get("id") or f"group_{index}")
        bound[group_id] = flatten_text(group.get("narration_text"))
    return bound


def primary_title_card_text(card_placement: Any) -> str:
    entries = card_text_entries(card_placement)
    if not entries:
        return ""
    title_cards = [entry for entry in entries if "title_card" in entry["card_role"]]
    if not title_cards:
        return ""
    first = title_cards[0]
    return "\n".join(first["text_values"])


def compare_locked_text(
    *,
    subcheck: str,
    locked_text: str,
    actual_text: str,
    missing_reason: str,
    diff_type_when_equal: str,
) -> dict[str, Any]:
    locked_norm = normalize_copy(locked_text)
    actual_norm = normalize_copy(actual_text)
    if not actual_norm:
        return {
            "status": "blocked",
            "diff_type": "missing_actual_text",
            "allowed": False,
            "failure_type": missing_reason,
            "missing_text": compact_copy(locked_text),
        }
    if locked_norm == actual_norm:
        return {
            "status": "passed",
            "diff_type": diff_type_when_equal,
            "allowed": True,
            "failure_type": "",
            "missing_text": "",
        }

    missing_units = [unit for unit in sentence_units(locked_text) if normalize_copy(unit) and normalize_copy(unit) not in actual_norm]
    failure_type = "unauthorized_semantic_copy_change"
    failure_prefix = {
        "subtitle_copy_match": "subtitle",
        "ass_copy_match": "ass",
        "tts_input_copy_match": "tts_input",
        "script_to_timeline_match": "script_to_timeline",
    }.get(subcheck, subcheck.replace("_match", ""))
    if actual_norm and locked_norm.startswith(actual_norm):
        failure_type = f"{failure_prefix}_truncates_locked_copy"
    elif missing_units:
        failure_type = f"{failure_prefix}_missing_locked_copy_text"
    return {
        "status": "blocked",
        "diff_type": "unauthorized_semantic_copy_change",
        "allowed": False,
        "failure_type": failure_type,
        "missing_text": compact_copy("".join(missing_units)),
        "missing_units": missing_units,
        "locked_normalized_length": len(locked_norm),
        "actual_normalized_length": len(actual_norm),
    }


def compare_opening_prefix(locked_opening: str, actual_text: str, failure_type: str) -> dict[str, Any]:
    opening_norm = normalize_copy(locked_opening)
    actual_norm = normalize_copy(actual_text)
    if not opening_norm:
        return {"status": "blocked", "diff_type": "missing_locked_opening_line", "allowed": False, "failure_type": "locked_opening_line_missing"}
    if not actual_norm:
        return {"status": "blocked", "diff_type": "missing_actual_text", "allowed": False, "failure_type": failure_type}
    if actual_norm.startswith(opening_norm):
        return {"status": "passed", "diff_type": "allowed_linebreak_diff", "allowed": True, "failure_type": ""}
    return {
        "status": "blocked",
        "diff_type": "unauthorized_opening_line_change",
        "allowed": False,
        "failure_type": failure_type,
        "actual_start": actual_text[:80],
    }


def compare_title_card(locked_title: str, card_placement: Any) -> dict[str, Any]:
    title_text = primary_title_card_text(card_placement)
    title_norm = normalize_copy(locked_title)
    actual_norm = normalize_copy(title_text)
    if not title_norm:
        return {"status": "blocked", "diff_type": "missing_locked_title", "allowed": False, "failure_type": "locked_title_missing"}
    if not actual_norm:
        return {"status": "blocked", "diff_type": "title_card_text_missing", "allowed": False, "failure_type": "title_card_text_missing"}
    if title_norm in actual_norm:
        return {"status": "passed", "diff_type": "allowed_card_context_with_locked_title", "allowed": True, "failure_type": "", "actual_title_card_text": title_text}
    return {
        "status": "blocked",
        "diff_type": "unauthorized_title_change",
        "allowed": False,
        "failure_type": "unauthorized_title_change",
        "actual_title_card_text": title_text,
    }


def validate_card_text_semantics(locked_script: str, locked_title: str, locked_opening: str, timeline: Any, card_placement: Any) -> dict[str, Any]:
    entries = card_text_entries(card_placement)
    if not entries:
        return {"status": "blocked", "diff_type": "card_text_source_missing", "allowed": False, "failure_type": "card_text_source_missing", "overreach": []}

    locked_norm = normalize_copy("\n".join([locked_script, locked_title, locked_opening]))
    bound_text = timeline_text_by_group(timeline)
    overreach: list[dict[str, Any]] = []
    checked: list[dict[str, Any]] = []
    claim_signals = ["赚钱", "不赚钱", "保本", "90", "自动化", "结果", "结论", "生产力", "成本", "转化", "跑通"]

    for entry in entries:
        group_norm = normalize_copy(bound_text.get(entry["line_group_id"], ""))
        matched_value_count = 0
        unmatched_values: list[str] = []
        for value in entry["text_values"]:
            value_norm = normalize_copy(value)
            if not value_norm:
                continue
            if value_norm in locked_norm or (group_norm and value_norm in group_norm):
                matched_value_count += 1
                continue
            is_short_label = len(value_norm) <= 12 and not any(signal in value for signal in claim_signals)
            has_bound_match = matched_value_count > 0
            if is_short_label or has_bound_match:
                continue
            unmatched_values.append(value)
        if unmatched_values:
            overreach.append(
                {
                    "line_group_id": entry["line_group_id"],
                    "card_role": entry["card_role"],
                    "unmatched_text": unmatched_values,
                }
            )
        checked.append(
            {
                "line_group_id": entry["line_group_id"],
                "card_role": entry["card_role"],
                "text_value_count": len(entry["text_values"]),
                "matched_value_count": matched_value_count,
            }
        )

    return {
        "status": "blocked" if overreach else "passed",
        "diff_type": "generated_card_overreach" if overreach else "allowed_non_semantic_card_labels_or_locked_excerpts",
        "allowed": not overreach,
        "failure_type": "generated_card_overreach" if overreach else "",
        "overreach": overreach,
        "checked_cards": checked,
    }


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "passed", "pass", "1"}
    return bool(value)


def blocked_report(gate_name: str, reasons: list[str], **extra: Any) -> dict[str, Any]:
    return {
        "schema": f"{gate_name}.v1",
        "gate_name": gate_name,
        "status": "blocked" if reasons else "passed",
        "check_depth": extra.pop("check_depth", "structural_check_only"),
        "blocked_reasons": sorted(set(reasons)),
        "warnings": extra.pop("warnings", []),
        **extra,
    }


def resolve_repo_path(value: Any) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(str(value))
    if path.is_absolute():
        return path
    return ROOT / path


def material_report_from_parse_pack(path: Path | None) -> tuple[Path | None, list[str]]:
    pack, errors = read_json(path, "material_parse_pack")
    if errors:
        return None, errors
    if not isinstance(pack, dict):
        return None, ["material_parse_pack_invalid"]
    material_report = resolve_repo_path(pack.get("material_detail_report_path"))
    if material_report is None:
        return None, ["material_detail_report_path_missing_in_parse_pack"]
    return material_report, []


def material_evidence_gate_preflight(
    *,
    material_report: Path | None,
    material_parse_pack: Path | None,
    timeline: Path | None,
    content_route_card: Path | None,
    output_dir: Path,
) -> dict[str, Any]:
    reasons: list[str] = []
    resolved_material_report = material_report
    parse_pack_errors: list[str] = []
    if resolved_material_report is None:
        resolved_material_report, parse_pack_errors = material_report_from_parse_pack(material_parse_pack)
        reasons.extend(parse_pack_errors)
    if resolved_material_report is None:
        reasons.append("material_detail_report_missing")
    elif not resolved_material_report.exists():
        reasons.append(f"material_detail_report_missing:{rel(resolved_material_report)}")
    if timeline is None:
        reasons.append("script_to_timeline_map_missing")
    elif not timeline.exists():
        reasons.append(f"script_to_timeline_map_missing:{rel(timeline)}")
    if reasons:
        return blocked_report(
            "material_evidence_gate_preflight",
            reasons,
            check_depth="implemented_no_render",
            checked_inputs={
                "material_detail_report": rel(resolved_material_report) if resolved_material_report else "",
                "material_parse_pack": rel(material_parse_pack) if material_parse_pack else "",
                "script_to_timeline_map": rel(timeline) if timeline else "",
                "content_route_card": rel(content_route_card) if content_route_card else "",
            },
        )

    try:
        result = run_material_evidence_gate(
            material_report=resolved_material_report,
            timeline=timeline,
            content_route_card=content_route_card,
            output_dir=output_dir,
        )
    except Exception as exc:
        return blocked_report(
            "material_evidence_gate_preflight",
            [f"material_evidence_gate_error:{exc}"],
            check_depth="implemented_no_render",
            checked_inputs={
                "material_detail_report": rel(resolved_material_report),
                "script_to_timeline_map": rel(timeline),
                "content_route_card": rel(content_route_card) if content_route_card else "",
            },
        )

    preflight = result.get("auto_storyboard_preflight_report", {}).get("auto_storyboard_preflight_report", {})
    blocked_reasons = list(preflight.get("blocked_reasons") or [])
    if preflight.get("auto_edit_allowed") is not True:
        blocked_reasons.append("material_evidence_auto_edit_not_allowed")
    return blocked_report(
        "material_evidence_gate_preflight",
        blocked_reasons,
        check_depth="implemented_no_render",
        checked_inputs={
            "material_detail_report": rel(resolved_material_report),
            "script_to_timeline_map": rel(timeline),
            "content_route_card": rel(content_route_card) if content_route_card else "",
        },
        auto_edit_allowed=bool(preflight.get("auto_edit_allowed")),
        total_line_groups=preflight.get("total_line_groups", 0),
        high_risk_line_groups=preflight.get("high_risk_line_groups", []),
        output_files=[
            "material_evidence_contract.json",
            "line_group_evidence_gate_report.json",
            "auto_storyboard_preflight_report.json",
        ],
    )


def line_level_alignment_preflight(timeline: Any, path: Path | None) -> dict[str, Any]:
    reasons: list[str] = []
    warnings = ["semantic visual A/B judgment requires future visual probe; this script checks declared fields and known statuses."]
    if timeline is None:
        reasons.append("script_to_timeline_map_missing")
        return blocked_report(
            "line_level_alignment_preflight",
            reasons,
            checked_input=rel(path) if path else "",
            warnings=warnings,
        )

    groups = line_groups_from_timeline(timeline)
    if not groups:
        reasons.append("script_to_timeline_map_missing_or_no_line_groups")
    if len(groups) < 2:
        reasons.append("only_paragraph_level_mapping")

    required = [
        "line_group_id",
        "line_ids",
        "narration_text",
        "required_material",
        "source_timecode",
        "expected_visual",
        "actual_visual_observed",
        "allowed_visuals",
        "forbidden_visuals",
        "evidence_strength",
        "alignment_status",
        "mismatch_reason",
        "repair_action",
    ]
    missing_by_group: dict[str, list[str]] = {}
    mismatch_groups: list[str] = []
    for index, group in enumerate(groups, start=1):
        group_id = str(group.get("line_group_id") or group.get("id") or f"group_{index}")
        missing = [field for field in required if field not in group or group.get(field) in ("", None, [])]
        if missing:
            missing_by_group[group_id] = missing
        status = str(group.get("alignment_status") or "").lower()
        if any(token in status for token in ["mismatch", "failed", "blocked", "unresolved"]):
            mismatch_groups.append(group_id)
        evidence = str(group.get("evidence_strength") or "").lower()
        text = flatten_text(group.get("narration_text"))
        if any(signal in text for signal in ["证明", "数据", "结论", "最适合", "一定"]) and evidence in {"", "low", "weak", "not_evidence"}:
            reasons.append(f"key_claim_without_evidence:{group_id}")

    if missing_by_group:
        reasons.append("required_line_group_fields_missing")
    if mismatch_groups:
        reasons.append("visual_mismatch_unresolved")

    return blocked_report(
        "line_level_alignment_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        line_group_count=len(groups),
        missing_by_group=missing_by_group,
        mismatch_groups=mismatch_groups,
        warnings=warnings,
    )


def _line_group_type(group: dict[str, Any]) -> str:
    return str(group.get("line_group_type") or group.get("claim_type") or group.get("evidence_type") or "")


def _is_core_evidence_line(group: dict[str, Any]) -> bool:
    group_type = _line_group_type(group)
    if truthy(group.get("is_core_evidence")):
        return True
    return group_type in CORE_EVIDENCE_LINE_TYPES


def _is_near_equivalent(group: dict[str, Any]) -> bool:
    text = flatten_text(
        [
            group.get("visual_match_type"),
            group.get("alignment_status"),
            group.get("evidence_match_status"),
        ]
    ).lower()
    return "near_equivalent" in text or "near equivalent" in text


def _whole_video_drift_detected(timeline: Any, groups: list[dict[str, Any]]) -> bool:
    if isinstance(timeline, dict) and truthy(timeline.get("whole_video_drift_detected")):
        return True
    return any(truthy(group.get("whole_video_drift_detected")) for group in groups)


def build_near_equivalent_material_substitution_report(timeline: Any) -> tuple[dict[str, Any], list[str]]:
    groups = line_groups_from_timeline(timeline)
    total = len(groups)
    exact_match_count = 0
    near_equivalent_count = 0
    core_evidence_mismatch_count = 0
    consecutive = 0
    consecutive_max = 0
    substitutions: list[dict[str, Any]] = []
    reasons: list[str] = []

    for index, group in enumerate(groups, start=1):
        near = _is_near_equivalent(group)
        if near:
            near_equivalent_count += 1
            consecutive += 1
            consecutive_max = max(consecutive_max, consecutive)
        else:
            consecutive = 0
            status = flatten_text([group.get("visual_match_type"), group.get("alignment_status")]).lower()
            if "exact" in status or "passed" in status:
                exact_match_count += 1

        if not near:
            continue

        group_id = str(group.get("line_group_id") or group.get("id") or f"group_{index}")
        group_type = _line_group_type(group)
        is_core = _is_core_evidence_line(group)
        if is_core:
            core_evidence_mismatch_count += 1

        visual_requires_guessing = truthy(group.get("visual_requires_guessing"))
        user_material_needed = truthy(group.get("user_material_needed_but_missing"))
        extremely_close = truthy(group.get("replacement_material_extremely_close")) or bool(group.get("why_extremely_close"))
        claim_preserved = truthy(group.get("claim_preserved"))
        viewer_inference_preserved = truthy(group.get("viewer_inference_preserved"))
        allowed = (
            not is_core
            and extremely_close
            and claim_preserved
            and viewer_inference_preserved
            and not visual_requires_guessing
            and not user_material_needed
        )
        blocked_reasons: list[str] = []
        if is_core:
            blocked_reasons.append("core_evidence_mismatch")
        if not extremely_close:
            blocked_reasons.append("replacement_material_not_extremely_close")
        if not claim_preserved:
            blocked_reasons.append("claim_not_preserved")
        if not viewer_inference_preserved:
            blocked_reasons.append("viewer_inference_changed")
        if visual_requires_guessing:
            blocked_reasons.append("visual_requires_guessing")
        if user_material_needed:
            blocked_reasons.append("user_material_needed_but_missing")

        substitutions.append(
            {
                "line_group_id": group_id,
                "original_required_visual": group.get("expected_visual") or group.get("required_material") or "",
                "substitute_visual_used": group.get("substitute_visual_used") or group.get("actual_visual_observed") or "",
                "substitute_material_id": group.get("substitute_material_id") or group.get("material_id") or "",
                "substitute_timecode": group.get("substitute_timecode") or group.get("source_timecode") or "",
                "line_group_type": group_type,
                "is_core_evidence": is_core,
                "why_extremely_close": group.get("why_extremely_close") or "",
                "claim_preserved": claim_preserved,
                "viewer_inference_preserved": viewer_inference_preserved,
                "risk": "low" if allowed else "blocked",
                "allowed": allowed,
                "blocked_reason": blocked_reasons,
            }
        )

    near_ratio = round(near_equivalent_count / total, 4) if total else 0.0
    whole_drift = _whole_video_drift_detected(timeline, groups)
    if near_ratio > 0.05:
        reasons.append("near_equivalent_ratio_gt_0_05")
    if consecutive_max > 1:
        reasons.append("consecutive_near_equivalent_groups_gt_1")
    if core_evidence_mismatch_count > 0:
        reasons.append("core_evidence_mismatch_count_gt_0")
    if whole_drift:
        reasons.append("whole_video_drift_detected")
    if any("visual_requires_guessing" in item["blocked_reason"] for item in substitutions):
        reasons.append("visual_requires_guessing")
    if any("replacement_material_not_extremely_close" in item["blocked_reason"] for item in substitutions):
        reasons.append("replacement_material_not_extremely_close")
    if any("user_material_needed_but_missing" in item["blocked_reason"] for item in substitutions):
        reasons.append("user_material_needed_but_missing")
    if any("claim_not_preserved" in item["blocked_reason"] for item in substitutions):
        reasons.append("claim_not_preserved")
    if any("viewer_inference_changed" in item["blocked_reason"] for item in substitutions):
        reasons.append("viewer_inference_changed")

    report = {
        "total_line_group_count": total,
        "exact_match_count": exact_match_count,
        "near_equivalent_count": near_equivalent_count,
        "near_equivalent_ratio": near_ratio,
        "consecutive_near_equivalent_max": consecutive_max,
        "core_evidence_mismatch_count": core_evidence_mismatch_count,
        "whole_video_drift_detected": whole_drift,
        "substitutions": substitutions,
        "final_decision": "blocked_need_user_material" if reasons else "passed",
    }
    return report, sorted(set(reasons))


def line_visual_tolerance_preflight(timeline: Any, path: Path | None) -> dict[str, Any]:
    if timeline is None:
        return blocked_report(
            "line_visual_tolerance_preflight",
            ["script_to_timeline_map_missing"],
            checked_input=rel(path) if path else "",
            line_visual_tolerance_rule=LINE_VISUAL_TOLERANCE_RULE,
        )
    report, reasons = build_near_equivalent_material_substitution_report(timeline)
    return blocked_report(
        "line_visual_tolerance_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        line_visual_tolerance_rule=LINE_VISUAL_TOLERANCE_RULE,
        near_equivalent_material_substitution_report=report,
        warnings=[
            "极其相近素材不等于主题相近；局部降级不等于全程偏差。",
            "达不到容差条件时必须 blocked，并等待用户补素材视频或图片，不允许硬剪。",
        ],
    )


def near_equivalent_material_substitution_preflight(timeline: Any, path: Path | None) -> dict[str, Any]:
    if timeline is None:
        return blocked_report(
            "near_equivalent_material_substitution_preflight",
            ["script_to_timeline_map_missing"],
            checked_input=rel(path) if path else "",
        )
    report, reasons = build_near_equivalent_material_substitution_report(timeline)
    return blocked_report(
        "near_equivalent_material_substitution_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        near_equivalent_material_substitution_report=report,
        check_depth="implemented",
    )


def tts_route_and_prosody_preflight(tts_map: Any, summary: Any, path: Path | None) -> dict[str, Any]:
    reasons: list[str] = []
    warnings = ["audio waveform / nonsilent validation is delegated to media probes when media is generated."]
    if tts_map is None:
        reasons.append("tts_requested_but_tts_prosody_anchor_map_missing")
        return blocked_report(
            "tts_route_and_prosody_preflight",
            reasons,
            checked_input=rel(path) if path else "",
            warnings=warnings,
        )
    if not isinstance(tts_map, dict):
        reasons.append("tts_prosody_anchor_map_invalid")
        return blocked_report("tts_route_and_prosody_preflight", reasons, warnings=warnings)

    target_provider = tts_map.get("target_tts_provider") or tts_map.get("target_provider") or tts_map.get("provider")
    target_model = tts_map.get("target_tts_model") or tts_map.get("target_model")
    expected_route = tts_map.get("expected_voice_route") or tts_map.get("target_voice_route")
    actual_provider = tts_map.get("actual_tts_provider") or tts_map.get("actual_provider") or tts_map.get("provider_used")
    actual_model = tts_map.get("actual_tts_model") or tts_map.get("actual_model") or tts_map.get("model_used")
    used_expected_voice = tts_map.get("used_expected_voice_route")
    used_expected_pacing = tts_map.get("used_expected_pacing")
    fallback_used = truthy(tts_map.get("fallback_used") or tts_map.get("local_tts_fallback_used"))
    fallback_authorized = truthy(tts_map.get("fallback_authorized"))

    for field, value in {
        "target_tts_provider": target_provider,
        "target_tts_model": target_model,
        "expected_voice_route": expected_route,
        "actual_tts_provider": actual_provider,
        "actual_tts_model": actual_model,
        "used_expected_voice_route": used_expected_voice,
        "used_expected_pacing": used_expected_pacing,
    }.items():
        if value in ("", None):
            reasons.append(f"{field}_missing")

    if target_provider and actual_provider and str(target_provider) != str(actual_provider):
        reasons.append("actual_voice_route_mismatch")
    if target_model and actual_model and str(target_model) != str(actual_model):
        reasons.append("actual_tts_model_mismatch")
    if used_expected_voice is not None and not truthy(used_expected_voice):
        reasons.append("actual_voice_route_mismatch")
    if used_expected_pacing is not None and not truthy(used_expected_pacing):
        reasons.append("expected_pacing_not_used")
    if fallback_used and not fallback_authorized:
        reasons.append("fallback_used_without_user_authorization")

    summary_text = flatten_text(summary).lower()
    if "audio_present" in summary_text and re.search(r"audio_present[^a-z0-9]+false", summary_text):
        reasons.append("no_audio_or_silent_audio")
    if not actual_provider or not actual_model:
        reasons.append("route_unknown_but_marked_passed")

    return blocked_report(
        "tts_route_and_prosody_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        route_summary={
            "target_tts_provider": target_provider,
            "target_tts_model": target_model,
            "expected_voice_route": expected_route,
            "actual_tts_provider": actual_provider,
            "actual_tts_model": actual_model,
            "used_expected_voice_route": used_expected_voice,
            "used_expected_pacing": used_expected_pacing,
            "fallback_used": fallback_used,
            "fallback_authorized": fallback_authorized,
        },
        warnings=warnings,
    )


def publish_candidate_voice_gate(tts_map: Any, summary: Any, path: Path | None) -> dict[str, Any]:
    validation = validate_publish_candidate_tts_route(tts_map, summary)
    reasons = validation.pop("blocked_reasons", [])
    warnings = [
        "B 方案仅保留为 voice_feel_reference；正片候选必须使用 MiniMax speech-2.8-hd 或 MiniMax/speech-2.8-hd。",
        "本 gate 只检查 TTS 路线与音频存在性字段；真实听感仍需要用户 / ChatGPT 人工复审。",
    ]
    if validation.get("voice_route_validation") == "internal_diagnostic_only":
        warnings.append("非 MiniMax TTS 仅允许 internal_diagnostic_only，不能写 publish_candidate_ready_for_human_review。")

    return blocked_report(
        "publish_candidate_voice_gate",
        reasons,
        checked_input=rel(path) if path else "",
        required_provider="minimax",
        required_model=sorted(REQUIRED_MINIMAX_MODELS),
        authorization_policy={
            "per_video_user_authorization_required": False,
            "meaning": "MiniMax route 在本地 runtime / 百炼代理 / 官方 API 中配置可用后，后续正片候选默认直接调用。",
            "not_meaning": "不代表可以打印、提交、绕过或伪造 API key / token / secret。",
        },
        **validation,
        warnings=warnings,
    )


def b_voice_feel_minimax_preflight(tts_map: Any, summary: Any, path: Path | None) -> dict[str, Any]:
    validation = validate_b_voice_feel_minimax_route(tts_map, summary)
    reasons = validation.pop("blocked_reasons", [])
    rule = validation.pop("b_voice_feel_minimax_formal_voice_rule", B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE)
    return blocked_report(
        "b_voice_feel_minimax_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        b_voice_feel_minimax_formal_voice_rule=rule,
        **validation,
        warnings=[
            "B 方案升级的是正式听感标准，不是旧 Qwen / 阿里 B 语音引擎。",
            "正式候选片生成路线必须是 MiniMax speech-2.8-hd 或 MiniMax/speech-2.8-hd；旧 B 语音脚本只能是历史 / reference / internal diagnostic。",
        ],
    )


def card_decision_preflight(content_route: Any, path: Path | None) -> dict[str, Any]:
    reasons: list[str] = []
    if content_route is None:
        reasons.append("card_placement_decision_missing")
        return blocked_report("card_decision_preflight", reasons, checked_input=rel(path) if path else "")
    if not isinstance(content_route, dict):
        return blocked_report("card_decision_preflight", ["content_route_card_invalid"])

    table = content_route.get("component_decision_table")
    if table is None and isinstance(content_route.get("card_decision_preflight"), dict):
        table = content_route.get("card_decision_preflight", {}).get("component_decision_table")
    if table is None and isinstance(content_route.get("card_placement_decision"), dict):
        table = content_route.get("card_placement_decision", {}).get("component_decision_table")
    if not isinstance(table, dict):
        reasons.append("component_decision_table_missing")
        table = {}

    component_results: dict[str, Any] = {}
    for card_type in CARD_TYPES:
        decision = table.get(card_type)
        if not isinstance(decision, dict):
            reasons.append(f"{card_type}_decision_missing")
            component_results[card_type] = {"status": "missing"}
            continue
        needed = decision.get("needed")
        has_reason = bool(decision.get("reason") or decision.get("not_needed_reason"))
        if needed is None:
            reasons.append(f"{card_type}_needed_missing")
        if not has_reason:
            reasons.append(f"{card_type}_reason_missing")
        if truthy(needed):
            if not decision.get("line_group_id"):
                reasons.append("selected_card_without_line_group")
            if not decision.get("evidence_dependency"):
                reasons.append("selected_card_without_evidence_dependency")
            if str(decision.get("interrupt_risk") or "").lower() in {"high", "blocked", "interrupts_key_evidence"}:
                reasons.append("selected_card_interrupts_key_evidence")
        component_results[card_type] = decision

    return blocked_report(
        "card_decision_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        component_decision_table=component_results,
    )


def forbidden_action_preflight(summary: Any, content_route: Any, locked_copy: Any, tts_map: Any) -> dict[str, Any]:
    text = "\n".join(flatten_text(item) for item in [summary, content_route, locked_copy, tts_map]).lower()
    detected: list[str] = []
    for action in FORBIDDEN_ACTIONS:
        if action.lower() in text:
            detected.append(action)
    if re.search(r"content_validation[^a-z0-9]+(passed|true|通过)", text):
        detected.append("advanced_content_validation")
    if re.search(r"send_ready[^a-z0-9]+(true|yes|1|是)", text):
        detected.append("advanced_send_ready")
    if re.search(r"voice_validation[^a-z0-9]+(passed|true|通过)", text):
        detected.append("advanced_voice_validation")
    if re.search(r"visual_master_locked[^a-z0-9]+(true|yes|1|是)", text):
        detected.append("advanced_visual_master_locked")
    if "fallback_used" in text and "fallback_authorized" not in text:
        detected.append("used_fallback_without_authorization")

    reasons = ["any_forbidden_action_detected"] if detected else []
    return blocked_report(
        "forbidden_action_preflight",
        reasons,
        detected_forbidden_actions=sorted(set(detected)),
        forbidden_actions=FORBIDDEN_ACTIONS,
        check_depth="implemented",
    )


def visual_evidence_readability_preflight(content_route: Any, summary: Any) -> dict[str, Any]:
    reasons: list[str] = []
    warnings = ["OCR/readability semantic validation requires future visual probe; this script enforces declared checks and known report status."]
    data_sources = [content_route, summary]
    text = "\n".join(flatten_text(item) for item in data_sources).lower()
    declared_check_found = any(
        key in text
        for key in [
            "visual_evidence_check",
            "readability_check",
            "visual_evidence_readability",
            "key_evidence_windows",
            "subtitles_not_covering_evidence",
            "cards_not_covering_evidence",
        ]
    )
    if not declared_check_found:
        reasons.append("visual_evidence_readability_check_missing")
    failure_signals = [
        "key_evidence_unreadable",
        "evidence_covered_by_subtitle",
        "evidence_covered_by_card",
        "whiteout_or_privacy_mask_without_authorization",
        "source_ratio_changed_without_authorization",
        "gray_or_black_edge_residue_affects_view",
        "readability_failed",
    ]
    detected = [signal for signal in failure_signals if signal in text]
    if detected:
        reasons.extend(detected)
    return blocked_report(
        "visual_evidence_readability_preflight",
        reasons,
        detected_readability_risks=detected,
        check_depth="structural_check_only",
        warnings=warnings,
    )


def locked_copy_diff_preflight(
    locked_copy: Any,
    summary: Any,
    content_route: Any,
    tts_map: Any,
    path: Path | None,
    *,
    timeline: Any = None,
    tts_route_report: Any = None,
    final_srt_text: str = "",
    final_ass_text: str = "",
    burned_subtitle_text: str = "",
    card_placement: Any = None,
) -> dict[str, Any]:
    reasons: list[str] = []
    if not isinstance(locked_copy, dict):
        return blocked_report("locked_copy_diff_preflight", ["locked_copy_contract_missing"], checked_input=rel(path) if path else "")

    locked_title = flatten_text(locked_copy.get("locked_title"))
    locked_opening = flatten_text(locked_copy.get("locked_opening_line"))
    locked_script = flatten_text(locked_copy.get("locked_final_script"))
    if not locked_title:
        reasons.append("locked_title_missing")
    if not locked_opening:
        reasons.append("locked_opening_line_missing")
    if not locked_script:
        reasons.append("locked_final_script_missing")

    payloads = [summary, content_route, tts_map]
    fallback_subtitle = ""
    fallback_tts = ""
    fallback_card = ""
    for payload in payloads:
        if isinstance(payload, dict):
            fallback_subtitle = fallback_subtitle or flatten_text(payload.get("actual_subtitle_text") or payload.get("subtitle_text"))
            fallback_tts = fallback_tts or flatten_text(payload.get("actual_tts_text") or payload.get("tts_text"))
            fallback_card = fallback_card or flatten_text(payload.get("actual_card_text") or payload.get("card_text"))

    timeline_text = extract_timeline_narration(timeline)
    tts_input_text = extract_tts_input_text(tts_map, tts_route_report) or fallback_tts
    srt_text = parse_srt_text(final_srt_text) or fallback_subtitle
    ass_text = parse_ass_text(final_ass_text)
    burned_text = burned_subtitle_text
    if card_placement is None and fallback_card:
        card_placement = {"card_groups": [{"card_role": "unknown", "card_text": fallback_card}]}

    subchecks = {
        "script_to_timeline_match": compare_locked_text(
            subcheck="script_to_timeline_match",
            locked_text=locked_script,
            actual_text=timeline_text,
            missing_reason="script_to_timeline_map_narration_text_missing",
            diff_type_when_equal="allowed_linebreak_diff",
        ),
        "tts_input_copy_match": compare_locked_text(
            subcheck="tts_input_copy_match",
            locked_text=locked_script,
            actual_text=tts_input_text,
            missing_reason="tts_input_text_missing",
            diff_type_when_equal="allowed_tts_pause_diff",
        ),
        "subtitle_copy_match": compare_locked_text(
            subcheck="subtitle_copy_match",
            locked_text=locked_script,
            actual_text=srt_text,
            missing_reason="final_srt_text_missing",
            diff_type_when_equal="allowed_subtitle_segmentation_diff",
        ),
        "ass_copy_match": compare_locked_text(
            subcheck="ass_copy_match",
            locked_text=locked_script,
            actual_text=ass_text,
            missing_reason="final_ass_text_missing",
            diff_type_when_equal="allowed_subtitle_segmentation_diff",
        ),
        "burned_subtitle_copy_match": compare_locked_text(
            subcheck="subtitle_copy_match",
            locked_text=locked_script,
            actual_text=burned_text,
            missing_reason="burned_subtitle_source_text_missing",
            diff_type_when_equal="allowed_subtitle_segmentation_diff",
        ),
        "opening_line_diff_check": compare_opening_prefix(
            locked_opening,
            "\n".join([timeline_text, tts_input_text, srt_text, ass_text]),
            "unauthorized_opening_line_change",
        ),
        "title_diff_check": compare_title_card(locked_title, card_placement),
        "card_text_semantic_match": validate_card_text_semantics(locked_script, locked_title, locked_opening, timeline, card_placement),
    }

    failed_subchecks = sorted(name for name, result in subchecks.items() if result.get("status") != "passed")
    reasons.extend(f"{name}:{subchecks[name].get('failure_type') or subchecks[name].get('diff_type')}" for name in failed_subchecks)

    return blocked_report(
        "locked_copy_diff_preflight",
        reasons,
        checked_input=rel(path) if path else "",
        compare={
            "locked_title_present": bool(locked_title),
            "locked_opening_line_present": bool(locked_opening),
            "locked_final_script_present": bool(locked_script),
            "script_to_timeline_narration_text_present": bool(timeline_text),
            "actual_tts_text_present": bool(tts_input_text),
            "final_srt_text_present": bool(srt_text),
            "final_ass_text_present": bool(ass_text),
            "burned_subtitle_source_text_present": bool(burned_text),
            "actual_card_text_present": bool(card_text_entries(card_placement)),
        },
        subchecks=subchecks,
        failed_subchecks=failed_subchecks,
        check_depth="implemented_locked_copy_diff",
        warnings=[
            "Allowed punctuation, line breaks, subtitle segmentation, and TTS pause marker changes are normalized before comparison.",
            "Missing/truncated locked script units in timeline, TTS input, SRT, ASS, burned subtitle source, or card text block publish candidate completion.",
        ],
    )


def publish_candidate_user_standard_preflight(summary: Any) -> dict[str, Any]:
    if summary is None:
        return blocked_report(
            "publish_candidate_user_standard_preflight",
            ["summary_json_missing"],
            publish_candidate_user_standard_rule={
                "status": "active",
                "user_definition": "publish_candidate_means_user_can_watch_and_directly_publish_after_human_review",
            },
        )
    if not isinstance(summary, dict):
        return blocked_report("publish_candidate_user_standard_preflight", ["summary_json_invalid"])

    raw_major_flaws = summary.get("forbidden_major_flaws", [])
    detected_major_flaws_set = {
        str(item)
        for item in raw_major_flaws
        if isinstance(raw_major_flaws, list) and str(item) in FORBIDDEN_MAJOR_FLAWS
    }
    detected_major_flaws_set.update(flaw for flaw in FORBIDDEN_MAJOR_FLAWS if truthy(summary.get(flaw)))
    status_text = str(summary.get("status") or "").lower()
    if status_text in FORBIDDEN_MAJOR_FLAWS:
        detected_major_flaws_set.add(status_text)
    detected_major_flaws = sorted(detected_major_flaws_set)
    declared_minor_flaws = {
        str(item)
        for item in summary.get("minor_flaws", [])
        if isinstance(summary.get("minor_flaws"), list)
    }
    unknown_minor_flaws = sorted(declared_minor_flaws - ALLOWED_MINOR_FLAWS)

    requirements = {
        "locked_copy_preserved": truthy(summary.get("locked_copy_preserved")),
        "minimax_voice_gate_passed": truthy(summary.get("minimax_voice_gate_passed")),
        "line_visual_tolerance_passed": truthy(summary.get("line_visual_tolerance_passed")),
        "core_evidence_mismatch_count_zero": int(summary.get("core_evidence_mismatch_count") or 0) == 0,
        "subtitle_card_overlap_check_passed": truthy(summary.get("subtitle_card_overlap_check_passed")),
        "visual_evidence_readability_passed": truthy(summary.get("visual_evidence_readability_passed")),
        "completion_truth_preflight_passed": truthy(summary.get("completion_truth_preflight_passed")),
        "review_pack_complete": truthy(summary.get("review_pack_complete")),
    }
    missing_requirements = sorted(key for key, value in requirements.items() if not value)
    reasons = []
    if detected_major_flaws:
        reasons.append("forbidden_major_flaws_detected")
    if unknown_minor_flaws:
        reasons.append("minor_flaw_not_in_allowed_list")
    if missing_requirements:
        reasons.append("candidate_required_fields_missing_or_failed")
    if truthy(summary.get("send_ready")):
        reasons.append("publish_candidate_does_not_equal_send_ready")

    publish_candidate_ready = not reasons
    return blocked_report(
        "publish_candidate_user_standard_preflight",
        reasons,
        publish_candidate_user_standard_rule={
            "status": "active",
            "user_definition": "publish_candidate_means_user_can_watch_and_directly_publish_after_human_review",
            "allowed_minor_flaws": sorted(ALLOWED_MINOR_FLAWS),
            "forbidden_major_flaws": sorted(FORBIDDEN_MAJOR_FLAWS),
            "candidate_allowed_only_if": sorted(requirements),
            "status_boundary": "publish_candidate_ready_for_human_review_does_not_equal_send_ready; send_ready_requires_user_or_chatgpt_final_confirmation",
        },
        detected_major_flaws=detected_major_flaws,
        allowed_minor_flaws_seen=sorted(declared_minor_flaws & ALLOWED_MINOR_FLAWS),
        unknown_minor_flaws=unknown_minor_flaws,
        requirements=requirements,
        missing_requirements=missing_requirements,
        publish_candidate_ready_for_human_review=publish_candidate_ready,
        send_ready_allowed=False,
        human_review_required=True,
        check_depth="implemented",
    )


def completion_truth_preflight(
    gate_reports: list[dict[str, Any]],
    review_pack: Path | None,
    summary: Any,
) -> dict[str, Any]:
    reasons: list[str] = []
    failed = [report["gate_name"] for report in gate_reports if report.get("status") != "passed"]
    if failed:
        reasons.append("any_required_gate_failed")
    if review_pack is None:
        reasons.append("review_pack_missing")
        missing_reports = REVIEW_PACK_REQUIRED_PREFLIGHT_REPORTS
    else:
        missing_reports = [name for name in REVIEW_PACK_REQUIRED_PREFLIGHT_REPORTS if not (review_pack / name).exists()]
        if missing_reports:
            reasons.append("review_pack_missing_preflight_reports")
    summary_text = flatten_text(summary).lower()
    if "full.mp4" in summary_text and "completed" in summary_text and failed:
        reasons.append("full_mp4_exists_but_preflight_missing_not_completed")
    if re.search(r"content_validation[^a-z0-9]+(passed|true|通过)", summary_text):
        reasons.append("no_forbidden_status_promotion")
    if re.search(r"send_ready[^a-z0-9]+(true|yes|1|是)", summary_text):
        reasons.append("no_forbidden_status_promotion")

    return blocked_report(
        "completion_truth_preflight",
        reasons,
        failed_gates=failed,
        review_pack=rel(review_pack) if review_pack else "",
        missing_review_pack_reports=missing_reports,
        required_review_pack_reports=REVIEW_PACK_REQUIRED_PREFLIGHT_REPORTS,
        check_depth="implemented",
    )


def validate_fixture_cases(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    data, errors = read_json(path, "fixture_cases")
    cases = data.get("cases") if isinstance(data, dict) else None
    case_errors: list[str] = errors[:]
    required = {"case_id", "input_signal", "expected_gate", "expected_status", "expected_reason", "must_not_write"}
    allowed_expected_status = {"blocked", "passed", "internal_diagnostic_only"}
    if not isinstance(cases, list):
        case_errors.append("fixture_cases_missing")
        cases = []
    for case in cases:
        if not isinstance(case, dict):
            case_errors.append("fixture_case_not_object")
            continue
        missing = sorted(required - set(case))
        if missing:
            case_errors.append(f"{case.get('case_id', 'unknown')}:missing:{','.join(missing)}")
        if case.get("expected_status") not in allowed_expected_status:
            case_errors.append(f"{case.get('case_id', 'unknown')}:unsupported_expected_status")
    return {
        "schema": "publish_candidate_preflight_suite.fixture_validation.v1",
        "fixture_path": rel(path),
        "case_count": len(cases),
        "status": "passed" if not case_errors else "blocked",
        "blocked_reasons": case_errors,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    timeline, _ = read_json(args.script_to_timeline_map, "script_to_timeline_map")
    tts_map, _ = read_json(args.tts_prosody_anchor_map, "tts_prosody_anchor_map")
    tts_route_report, _ = read_json(args.tts_route_report, "tts_route_report")
    locked_copy, _ = read_json(args.locked_copy_contract, "locked_copy_contract")
    content_route, _ = read_json(args.content_route_card, "content_route_card")
    card_placement, _ = read_json(args.card_placement_decision, "card_placement_decision")
    summary, _ = read_json(args.summary_json, "summary_json")
    final_srt_text, _ = read_text(args.final_srt, "final_srt")
    final_ass_text, _ = read_text(args.final_ass, "final_ass")
    burned_subtitle_text, _ = read_text(args.burned_subtitle_text, "burned_subtitle_text")

    reports = [
        run_material_parse_pack_reuse_gate(
            material_parse_pack=args.material_parse_pack,
            source_segment_inventory=args.source_segment_inventory,
            script_to_shot_execution_map=args.script_to_shot_execution_map,
            material_usage_ledger=args.material_usage_ledger,
        ),
        material_evidence_gate_preflight(
            material_report=args.material_detail_report,
            material_parse_pack=args.material_parse_pack,
            timeline=args.script_to_timeline_map,
            content_route_card=args.content_route_card,
            output_dir=output_dir,
        ),
        line_level_alignment_preflight(timeline, args.script_to_timeline_map),
        line_visual_tolerance_preflight(timeline, args.script_to_timeline_map),
        near_equivalent_material_substitution_preflight(timeline, args.script_to_timeline_map),
        tts_route_and_prosody_preflight(tts_map, summary, args.tts_prosody_anchor_map),
        publish_candidate_voice_gate(tts_map, summary, args.tts_prosody_anchor_map),
        b_voice_feel_minimax_preflight(tts_map, summary, args.tts_prosody_anchor_map),
        card_decision_preflight(content_route, args.content_route_card),
        forbidden_action_preflight(summary, content_route, locked_copy, tts_map),
        visual_evidence_readability_preflight(content_route, summary),
        locked_copy_diff_preflight(
            locked_copy,
            summary,
            content_route,
            tts_map,
            args.locked_copy_contract,
            timeline=timeline,
            tts_route_report=tts_route_report,
            final_srt_text=final_srt_text,
            final_ass_text=final_ass_text,
            burned_subtitle_text=burned_subtitle_text,
            card_placement=card_placement,
        ),
        publish_candidate_user_standard_preflight(summary),
    ]
    reports.append(completion_truth_preflight(reports, args.review_pack, summary))

    for report in reports:
        stem = REPORT_FILENAMES[report["gate_name"]]
        write_json(output_dir / f"{stem}.json", report)
        write_md(output_dir / f"{stem}.md", report)

    fixture_validation = validate_fixture_cases(args.fixture_cases)
    if fixture_validation:
        write_json(output_dir / "fixture_validation_report.json", fixture_validation)
        write_md(output_dir / "fixture_validation_report.md", fixture_validation)

    failed = [report["gate_name"] for report in reports if report["status"] != "passed"]
    if fixture_validation and fixture_validation["status"] != "passed":
        failed.append("fixture_validation")
    overall_status = "passed" if not failed else "blocked"
    aggregate = {
        "schema": "publish_candidate_preflight_suite.v2",
        "no_render": bool(args.no_render),
        "overall_status": overall_status,
        "status": overall_status,
        "failed_gates": failed,
        "required_gates": GATES,
        "gate_reports": {
            report["gate_name"]: {
                "status": report["status"],
                "json": f"{REPORT_FILENAMES[report['gate_name']]}.json",
                "md": f"{REPORT_FILENAMES[report['gate_name']]}.md",
            }
            for report in reports
        },
        "review_pack_required_preflight_reports": REVIEW_PACK_REQUIRED_PREFLIGHT_REPORTS,
        "fixture_validation": fixture_validation,
        "completion_rule": {
            "any_required_gate_failed": "blocked",
            "any_required_gate_missing": "continue_or_blocked",
            "only_docs_updated_but_no_script_or_report_wiring": "partial_completed",
            "full_mp4_exists_means_completed": False,
            "technical_validation_means_content_validation": False,
            "publish_candidate_ready_for_human_review_means_send_ready": False,
            "old_qwen_b_voice_route_means_publish_candidate": False,
        },
    }
    write_json(output_dir / "publish_candidate_preflight_report.json", aggregate)
    write_md(output_dir / "publish_candidate_preflight_report.md", aggregate)
    return aggregate


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run publish candidate preflight suite without rendering media.")
    parser.add_argument("--no-render", action="store_true", help="Assert that this run must not generate video, audio, TTS, or subtitles.")
    parser.add_argument("--review-pack", type=Path, help="Review pack directory to verify preflight report inclusion.")
    parser.add_argument("--summary-json", type=Path, help="Candidate summary.json.")
    parser.add_argument("--script-to-timeline-map", type=Path, help="script_to_timeline_map JSON.")
    parser.add_argument("--tts-prosody-anchor-map", type=Path, help="tts_prosody_anchor_map JSON.")
    parser.add_argument("--tts-route-report", type=Path, help="Actual TTS route report JSON containing segment input text.")
    parser.add_argument("--locked-copy-contract", type=Path, help="locked_copy_contract JSON.")
    parser.add_argument("--content-route-card", type=Path, help="content_route_card_v2 JSON.")
    parser.add_argument("--card-placement-decision", type=Path, help="card_placement_decision JSON containing actual card text.")
    parser.add_argument("--final-srt", type=Path, help="Final SRT subtitle file.")
    parser.add_argument("--final-ass", type=Path, help="Final ASS subtitle file.")
    parser.add_argument("--burned-subtitle-text", type=Path, help="Text file with exact burned subtitle overlay source / function output.")
    parser.add_argument("--material-detail-report", type=Path, help="material_detail_report Markdown.")
    parser.add_argument("--material-parse-pack", type=Path, help="material_parse_pack JSON.")
    parser.add_argument("--source-segment-inventory", type=Path, help="source_segment_inventory JSON.")
    parser.add_argument("--script-to-shot-execution-map", type=Path, help="script_to_shot_execution_map JSON.")
    parser.add_argument("--material-usage-ledger", type=Path, help="material_usage_ledger JSON.")
    parser.add_argument("--fixture-cases", type=Path, help="Fixture cases JSON for blocked-case validation.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for aggregate and child reports.")
    parser.add_argument("--allow-blocked-exit-zero", action="store_true", help="Write blocked reports but return 0 for no-render demonstrations.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    result = run(args)
    if result["overall_status"] == "passed" or args.allow_blocked_exit_zero:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
