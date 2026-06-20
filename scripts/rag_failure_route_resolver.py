#!/usr/bin/env python3
"""Resolve RAG engineering failures to a concrete repair layer."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


ROUTES = {
    "RAG_supply_bus": {
        "keywords": (
            "missing_context",
            "source_path_missing",
            "line_range_missing",
            "readback_missing",
            "missing_readback",
            "only_summary",
            "summary_only",
            "snippet",
        ),
        "next_action": "rebuild_supply_pack_with_source_readback",
    },
    "RAG_sync_bus": {
        "keywords": (
            "stale_index",
            "vector_sync_stale",
            "commit_mismatch",
            "index_manifest",
            "deleted_file",
            "upsert_missing",
            "sync_guard",
        ),
        "next_action": "rerun_sync_guard_or_vector_sync_when_authorized",
    },
    "fact_source_arbitration": {
        "keywords": (
            "fact_conflict",
            "source_conflict",
            "authority_uncertain",
            "legacy_override",
            "legacy_demoted",
            "stale_context",
            "deepseek_conflict",
            "dashvector_conflict",
            "github_conflict",
        ),
        "next_action": "compare_repo_github_dashvector_and_readback_sources",
    },
    "validation_repair": {
        "keywords": ("validation", "py_compile", "schema_probe", "fixture", "probe_failed", "test_failed"),
        "next_action": "repair_script_schema_fixture_or_probe_then_rerun_validation",
    },
    "human_decision_gate": {
        "keywords": (
            "auth_missing",
            "api_permission",
            "cost",
            "external_api",
            "aesthetic",
            "semantic",
            "status_promotion",
            "user_decision_required",
            "delete_authorization",
            "degradation_authorization",
            "publish_decision",
            "delivery_decision",
            "human",
        ),
        "next_action": "request_human_decision_or_authorization",
    },
    "completion_truth_check": {
        "keywords": (
            "completion",
            "completion_claim_risk",
            "preview_as_completed",
            "partial_as_completed",
            "status_swap",
            "local_only",
            "missing_log",
            "not_pushed",
        ),
        "next_action": "run_completion_truth_check_before_claiming_done",
    },
    "git_sync_gate": {
        "keywords": ("git", "commit", "push", "remote", "readback", "branch"),
        "next_action": "repair_commit_push_remote_readback",
    },
}


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def resolve_route(event: dict[str, Any]) -> dict[str, Any]:
    text = json.dumps(event, ensure_ascii=False).lower()
    selected = "human_decision_gate"
    matched_cleaning_keyword = False
    for route, config in ROUTES.items():
        matched_keywords = [keyword for keyword in config["keywords"] if keyword in text]
        if matched_keywords:
            selected = route
            matched_cleaning_keyword = any(
                keyword
                in {
                    "summary_only",
                    "missing_readback",
                    "readback_missing",
                    "only_summary",
                    "stale_index",
                    "vector_sync_stale",
                    "authority_uncertain",
                    "legacy_override",
                    "legacy_demoted",
                    "stale_context",
                    "source_conflict",
                    "user_decision_required",
                    "completion_claim_risk",
                    "preview_as_completed",
                    "not_pushed",
                }
                for keyword in matched_keywords
            )
            break
    config = ROUTES[selected]
    return {
        "failure_id": event.get("failure_id") or event.get("event_id") or "failure_event",
        "failure_type": event.get("failure_type") or event.get("event_type") or "unknown_failure",
        "route_target": selected,
        "next_action": config["next_action"],
        "blocked_until": "repair_layer_completed",
        "reason": event.get("reason") or event.get("message") or "resolved_by_keyword_route",
        "cleaning_layer_failure_route": matched_cleaning_keyword,
        "available_route_targets": list(ROUTES),
        "generated_at": common.now_iso(),
    }


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Resolve a RAG failure event.")
    parser.add_argument("--failure-event", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    event_path = _resolve(args.failure_event)
    out_path = _resolve(args.out)
    if not event_path.exists():
        raise SystemExit("blocked_failure_event_missing")
    route = resolve_route(common.read_json(event_path))
    common.write_json(out_path, route)
    print(json.dumps({"status": "passed", "route_target": route["route_target"], "failure_route_path": out_path.as_posix()}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
