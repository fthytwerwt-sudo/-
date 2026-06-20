#!/usr/bin/env python3
"""Validate RAG supply packs and fail closed on missing source readback."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


REQUIRED_PRE_FIELDS = [
    "task_id",
    "task_type",
    "retrieval_goal",
    "exact_snippet_pack",
    "source_path",
    "line_range",
    "chunk_id",
    "why_needed",
    "execution_constraint",
    "conflict_points",
    "blocked_if",
]

HIGH_RISK_TERMS = (
    "rag",
    "vector",
    "sync",
    "route",
    "mechanism",
    "engineering",
    "failure",
    "trace",
    "供料",
    "向量",
    "机制",
    "路由",
)

CLEANING_SNIPPET_FIELDS = [
    "authority_level",
    "stale_status",
    "conflict_status",
    "readback_required",
    "can_feed_codex",
    "can_claim_completed",
]

ALLOWED_AUTHORITY_LEVELS = {
    "current_repo_source",
    "real_run_report",
    "latest_summary",
    "rag_retrieval_result",
    "chat_memory",
    "historical_archive",
}

ALLOWED_STALE_STATUSES = {"current", "legacy_demoted", "stale_index", "historical_reference"}
ALLOWED_CONFLICT_STATUSES = {"none", "resolved_by_source_priority", "requires_chatgpt_review", "requires_user_decision", "unresolved"}
BLOCKING_STALE_STATUSES = {"legacy_demoted", "stale_index", "historical_reference"}
LOW_AUTHORITY_LEVELS = {"chat_memory", "historical_archive"}


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _text(value: Any) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value or "")


def _is_high_risk(pack: dict[str, Any]) -> bool:
    text = f"{_text(pack.get('task_type'))} {_text(pack.get('retrieval_goal'))}".lower()
    return any(term in text for term in HIGH_RISK_TERMS)


def _validate_cleaning_fields(snippet: dict[str, Any], index: int) -> list[str]:
    reasons: list[str] = []
    for field in CLEANING_SNIPPET_FIELDS:
        if field not in snippet:
            reasons.append(f"snippet_{index}_{field}_missing")

    authority_level = snippet.get("authority_level")
    stale_status = snippet.get("stale_status")
    conflict_status = snippet.get("conflict_status")

    if authority_level is not None and authority_level not in ALLOWED_AUTHORITY_LEVELS:
        reasons.append(f"snippet_{index}_authority_level_invalid")
    if stale_status is not None and stale_status not in ALLOWED_STALE_STATUSES:
        reasons.append(f"snippet_{index}_stale_status_invalid")
    if conflict_status is not None and conflict_status not in ALLOWED_CONFLICT_STATUSES:
        reasons.append(f"snippet_{index}_conflict_status_invalid")

    if snippet.get("readback_required") is not True:
        reasons.append(f"snippet_{index}_readback_required_not_true")
    if stale_status in BLOCKING_STALE_STATUSES and snippet.get("can_feed_codex") is True:
        reasons.append(f"snippet_{index}_stale_source_can_feed_codex")
    if authority_level in LOW_AUTHORITY_LEVELS and snippet.get("can_feed_codex") is True:
        reasons.append(f"snippet_{index}_low_authority_can_feed_codex")
    if conflict_status in {"requires_chatgpt_review", "requires_user_decision", "unresolved"}:
        reasons.append(f"snippet_{index}_conflict_not_cleaned")
    if snippet.get("can_feed_codex") is not True:
        reasons.append(f"snippet_{index}_can_feed_codex_not_true")
    if snippet.get("can_claim_completed") is True:
        reasons.append(f"snippet_{index}_supply_pack_claims_completed")
    return reasons


def validate_pre_supply_pack(pack: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_PRE_FIELDS:
        value = pack.get(field)
        if value is None or value == "" or value == []:
            reasons.append(f"{field}_missing")

    snippets = pack.get("exact_snippet_pack")
    if not isinstance(snippets, list) or not snippets:
        reasons.append("exact_snippet_pack_missing")
        return reasons

    only_summary = True
    for index, snippet in enumerate(snippets):
        if not isinstance(snippet, dict):
            reasons.append(f"snippet_{index}_not_object")
            continue
        if not snippet.get("source_path"):
            reasons.append("source_path_missing")
        if not snippet.get("line_range"):
            reasons.append("line_range_missing")
        if not snippet.get("chunk_id"):
            reasons.append("chunk_id_missing")
        readback = snippet.get("readback") or snippet.get("snippet")
        if readback:
            only_summary = False
        else:
            reasons.append("readback_missing")
        reasons.extend(_validate_cleaning_fields(snippet, index))
    if only_summary:
        reasons.append("only_summary_without_snippet")

    cleaning_layer_check = pack.get("cleaning_layer_check")
    if not isinstance(cleaning_layer_check, dict):
        reasons.append("cleaning_layer_check_missing")
    else:
        if cleaning_layer_check.get("can_feed_codex") is not True:
            reasons.append("cleaning_layer_check_can_feed_codex_not_true")
        if cleaning_layer_check.get("can_claim_completed") is True:
            reasons.append("cleaning_layer_check_claims_completed")

    if _is_high_risk(pack) and not pack.get("conflict_points"):
        reasons.append("conflict_points_missing_for_high_risk_task")
    return sorted(set(reasons))


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Validate a RAG supply pack.")
    parser.add_argument("--pack", required=True)
    args = parser.parse_args()

    path = _resolve(args.pack)
    if not path.exists():
        report = {"status": "blocked", "blocked_reasons": ["pack_missing"], "pack_path": path.as_posix()}
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 2
    pack = common.read_json(path)
    reasons = validate_pre_supply_pack(pack)
    report = {
        "validator": "rag_supply_pack_validator",
        "status": "blocked" if reasons else "passed",
        "pack_path": path.as_posix(),
        "blocked_reasons": reasons,
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if not reasons else 2


if __name__ == "__main__":
    raise SystemExit(main())
