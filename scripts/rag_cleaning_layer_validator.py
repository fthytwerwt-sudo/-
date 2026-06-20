#!/usr/bin/env python3
"""Validate RAG cleaning-layer cases and fail closed on unsafe authority claims."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DEFAULT_FIXTURE_DIR = common.ROOT / "codex_log" / "rag_cleaning_layer" / "fixtures"

REQUIRED_TOP_LEVEL_FIELDS = [
    "case_id",
    "expected_status",
    "task_mode",
    "source_authority_classifier",
    "stale_context_detector",
    "conflict_cleaner",
    "decision_authority_router",
    "supply_pack_cleaner",
    "completion_claim_cleaner",
    "user_minimal_review_panel",
]

ALLOWED_EXPECTED_STATUSES = {"passed", "blocked"}
ALLOWED_TASK_MODES = {"execution", "explanation", "review_panel"}
ALLOWED_AUTHORITY_LEVELS = {
    "current_repo_source",
    "real_run_report",
    "latest_summary",
    "rag_retrieval_result",
    "chat_memory",
    "historical_archive",
}
LOW_AUTHORITY_LEVELS = {"chat_memory", "historical_archive"}
ALLOWED_STALE_STATUSES = {"current", "legacy_demoted", "stale_index", "historical_reference"}
BLOCKING_STALE_STATUSES = {"legacy_demoted", "stale_index", "historical_reference"}
ALLOWED_CONFLICT_STATUSES = {
    "none",
    "resolved_by_source_priority",
    "requires_chatgpt_review",
    "requires_user_decision",
    "unresolved",
}
ALLOWED_DECISION_OWNERS = {"system_default", "codex_auto_decide", "chatgpt_review", "user_must_decide"}
COMPLETION_REQUIRED_TRUE_FIELDS = [
    "files_landed",
    "schema_landed",
    "validator_landed",
    "fixtures_landed",
    "latest_updated",
    "commit_created",
    "pushed",
    "remote_verified",
    "secret_scan_passed",
]
COMPLETION_ALLOWED_VECTOR_STATUSES = {"completed", "not_required"}


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _is_present(value: Any) -> bool:
    return value not in (None, "", [])


def _has_readback(snippet: dict[str, Any]) -> bool:
    return bool(snippet.get("readback") or snippet.get("snippet"))


def _validate_source_authority(case: dict[str, Any], reasons: list[str]) -> None:
    source = case.get("source_authority_classifier") or {}
    if not isinstance(source, dict):
        reasons.append("source_authority_classifier_not_object")
        return

    authority_level = source.get("authority_level")
    if authority_level not in ALLOWED_AUTHORITY_LEVELS:
        reasons.append("authority_level_invalid")
    if not _is_present(source.get("source_path")):
        reasons.append("source_path_missing")
    if not _is_present(source.get("status_label")):
        reasons.append("status_label_missing")
    if not isinstance(source.get("source_priority_rank"), int):
        reasons.append("source_priority_rank_missing_or_invalid")

    if authority_level in LOW_AUTHORITY_LEVELS and source.get("can_use_as_current_fact") is True:
        reasons.append("low_authority_claims_current_fact")
    if authority_level == "rag_retrieval_result" and source.get("can_use_as_current_fact") is True and not source.get("repo_readback_verified"):
        reasons.append("rag_result_claims_current_without_repo_readback")


def _validate_stale_context(case: dict[str, Any], reasons: list[str]) -> None:
    stale = case.get("stale_context_detector") or {}
    source = case.get("source_authority_classifier") or {}
    if not isinstance(stale, dict):
        reasons.append("stale_context_detector_not_object")
        return

    stale_status = stale.get("stale_status")
    if stale_status not in ALLOWED_STALE_STATUSES:
        reasons.append("stale_status_invalid")
    if stale.get("tries_to_override_current") is True and stale_status != "current":
        reasons.append("stale_context_attempts_to_override_current")
    if stale_status in BLOCKING_STALE_STATUSES and source.get("can_use_as_current_fact") is True:
        reasons.append("stale_context_claims_current_fact")
    if stale_status == "stale_index" and stale.get("requires_vector_sync") is not True:
        reasons.append("stale_index_missing_vector_sync_route")


def _validate_conflict(case: dict[str, Any], reasons: list[str]) -> None:
    conflict = case.get("conflict_cleaner") or {}
    decision = case.get("decision_authority_router") or {}
    if not isinstance(conflict, dict):
        reasons.append("conflict_cleaner_not_object")
        return

    conflict_status = conflict.get("conflict_status")
    if conflict_status not in ALLOWED_CONFLICT_STATUSES:
        reasons.append("conflict_status_invalid")
    if conflict_status == "unresolved":
        reasons.append("source_conflict_unresolved")
    if conflict_status == "requires_user_decision" and decision.get("decision_owner") != "user_must_decide":
        reasons.append("user_conflict_not_routed_to_user")
    if conflict_status == "requires_chatgpt_review" and decision.get("decision_owner") not in {"chatgpt_review", "user_must_decide"}:
        reasons.append("chatgpt_conflict_not_routed_to_review")


def _validate_decision_authority(case: dict[str, Any], reasons: list[str]) -> None:
    decision = case.get("decision_authority_router") or {}
    panel = case.get("user_minimal_review_panel") or {}
    if not isinstance(decision, dict):
        reasons.append("decision_authority_router_not_object")
        return

    owner = decision.get("decision_owner")
    if owner not in ALLOWED_DECISION_OWNERS:
        reasons.append("decision_owner_invalid")
    if owner == "user_must_decide":
        if not _as_list(panel.get("decision_items")):
            reasons.append("user_must_decide_without_panel_items")
        if panel.get("blocked_if_not_decided") is not True:
            reasons.append("user_panel_missing_blocked_if_not_decided")


def _validate_supply_pack(case: dict[str, Any], reasons: list[str], warnings: list[str]) -> None:
    supply = case.get("supply_pack_cleaner") or {}
    if not isinstance(supply, dict):
        reasons.append("supply_pack_cleaner_not_object")
        return

    task_mode = supply.get("task_mode") or case.get("task_mode")
    if task_mode not in ALLOWED_TASK_MODES:
        reasons.append("task_mode_invalid")

    snippets = _as_list(supply.get("exact_snippet_pack"))
    if task_mode == "execution" and not snippets:
        reasons.append("exact_snippet_pack_missing_for_execution")

    for index, snippet in enumerate(snippets):
        if not isinstance(snippet, dict):
            reasons.append(f"snippet_{index}_not_object")
            continue
        summary_only = bool(snippet.get("summary_only"))
        required_fields = ["source_path", "line_range", "chunk_id"]
        missing_required = [field for field in required_fields if not _is_present(snippet.get(field))]
        missing_readback = not _has_readback(snippet)
        if task_mode == "execution":
            for field in missing_required:
                reasons.append(f"snippet_{index}_{field}_missing")
            if missing_readback:
                reasons.append(f"snippet_{index}_readback_missing")
            if summary_only:
                reasons.append(f"snippet_{index}_summary_only")
            if snippet.get("readback_required") is not True:
                reasons.append(f"snippet_{index}_readback_required_not_true")
            if snippet.get("can_feed_codex") is not True:
                reasons.append(f"snippet_{index}_can_feed_codex_not_true")
            if snippet.get("can_claim_completed") is True:
                reasons.append(f"snippet_{index}_supply_pack_claims_completed")
        elif missing_required or missing_readback or summary_only:
            warnings.append(f"snippet_{index}_evidence_weak")

    if supply.get("summary_only") is True and task_mode == "execution":
        reasons.append("summary_only_execution_supply_pack")


def _validate_completion_claim(case: dict[str, Any], reasons: list[str]) -> None:
    completion = case.get("completion_claim_cleaner") or {}
    if not isinstance(completion, dict):
        reasons.append("completion_claim_cleaner_not_object")
        return

    claim_requested = completion.get("claim_requested", "not_requested")
    if claim_requested == "completed":
        for field in COMPLETION_REQUIRED_TRUE_FIELDS:
            if completion.get(field) is not True:
                reasons.append(f"completion_{field}_not_true")
        if completion.get("vector_sync_status") not in COMPLETION_ALLOWED_VECTOR_STATUSES:
            reasons.append("completion_vector_sync_status_not_final")
        if completion.get("can_claim_completed") is not True:
            reasons.append("completion_can_claim_completed_not_true")

    if completion.get("technical_preview_only") is True:
        reasons.append("technical_preview_claimed_as_completion")
    if completion.get("forbidden_status_promoted") is True:
        reasons.append("forbidden_status_promoted")
    if completion.get("technical_as_content") is True:
        reasons.append("technical_validation_swapped_to_content_validation")
    if completion.get("can_claim_completed") is True and claim_requested != "completed":
        reasons.append("completion_claim_allowed_without_completed_request")


def validate_case(case: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    warnings: list[str] = []

    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in case:
            reasons.append(f"{field}_missing")

    expected_status = case.get("expected_status")
    if expected_status not in ALLOWED_EXPECTED_STATUSES:
        reasons.append("expected_status_invalid")
    if case.get("task_mode") not in ALLOWED_TASK_MODES:
        reasons.append("task_mode_invalid")

    if not reasons:
        _validate_source_authority(case, reasons)
        _validate_stale_context(case, reasons)
        _validate_conflict(case, reasons)
        _validate_decision_authority(case, reasons)
        _validate_supply_pack(case, reasons, warnings)
        _validate_completion_claim(case, reasons)

    actual_status = "blocked" if reasons else "passed"
    expected_matched = actual_status == expected_status
    return {
        "case_id": case.get("case_id", "unknown_case"),
        "expected_status": expected_status,
        "actual_status": actual_status,
        "expected_matched": expected_matched,
        "blocked_reasons": sorted(set(reasons)),
        "warnings": sorted(set(warnings)),
    }


def _fixture_paths(args: argparse.Namespace) -> list[pathlib.Path]:
    if args.fixture:
        return [_resolve(item) for item in args.fixture]
    fixture_dir = _resolve(args.fixtures)
    return sorted(fixture_dir.glob("*.json"))


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Validate RAG cleaning-layer fixtures.")
    parser.add_argument("--fixtures", default=DEFAULT_FIXTURE_DIR.as_posix(), help="Directory containing fixture JSON files.")
    parser.add_argument("--fixture", action="append", help="Validate one fixture path. Can be repeated.")
    parser.add_argument("--summary-out", help="Optional path for the JSON summary.")
    args = parser.parse_args()

    fixture_paths = _fixture_paths(args)
    if not fixture_paths:
        summary = {
            "validator": "rag_cleaning_layer_validator",
            "status": "blocked",
            "blocked_reasons": ["fixtures_missing"],
        }
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
        return 2

    case_results = []
    for path in fixture_paths:
        if not path.exists():
            case_results.append(
                {
                    "case_id": path.name,
                    "expected_status": "unknown",
                    "actual_status": "blocked",
                    "expected_matched": False,
                    "blocked_reasons": ["fixture_missing"],
                    "warnings": [],
                }
            )
            continue
        case = common.read_json(path)
        result = validate_case(case)
        result["fixture_path"] = path.as_posix()
        case_results.append(result)

    failed = [result for result in case_results if not result["expected_matched"]]
    summary = {
        "validator": "rag_cleaning_layer_validator",
        "status": "passed" if not failed else "blocked",
        "fixture_count": len(case_results),
        "passed_fixture_tests": len(case_results) - len(failed),
        "expected_blocked_fixture_count": sum(1 for result in case_results if result["expected_status"] == "blocked"),
        "failed_fixtures": failed,
        "warnings": [warning for result in case_results for warning in result["warnings"]],
    }
    if args.summary_out:
        common.write_json(_resolve(args.summary_out), summary)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
