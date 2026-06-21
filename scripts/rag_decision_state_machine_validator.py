#!/usr/bin/env python3
"""Validate Python-first RAG decision state machine fixtures."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["nodes", "task_request"]
REQUIRED_NODE_ORDER = [
    "task_classifier",
    "stale_index_checker",
    "vector_retriever_or_repo_readback",
    "source_readback_checker",
    "authority_overlay_filter",
    "conflict_group_resolver",
    "hard_gate_checker",
    "weighted_decision_engine",
    "decision_audit_reporter",
    "codex_supply_pack_emitter",
    "failure_router",
]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    nodes = data.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        reasons.append("nodes_missing")
    else:
        for node in nodes:
            if node not in REQUIRED_NODE_ORDER:
                reasons.append(f"unknown_node:{node}")
        if data.get("expected_status") == "passed" and nodes != REQUIRED_NODE_ORDER:
            reasons.append("passed_case_node_order_incomplete")
    if not isinstance(data.get("task_request"), dict):
        reasons.append("task_request_missing")
    if data.get("expected_status") == "blocked":
        reasons.extend(str(item) for item in data.get("blocked_if", []) if str(item).strip())
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_decision_state_machine_validator",
        manifest_type="rag_decision_state_machine",
        fixture_subdir="state_machine",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
