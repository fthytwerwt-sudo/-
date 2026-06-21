#!/usr/bin/env python3
"""Validate hard-gate-first weighted decision fixtures."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["hard_gate_result", "candidate_actions", "weighted_score_breakdown"]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    hard_gate = data.get("hard_gate_result")
    if not isinstance(hard_gate, dict):
        reasons.append("hard_gate_result_missing")
    else:
        if hard_gate.get("status") == "blocked" and hard_gate.get("proceeded_to_weighted_decision") is True:
            reasons.append("hard_gate_failed_but_weighted_decision_still_runs")
        if "failed_gates" not in hard_gate:
            reasons.append("failed_gates_missing")
    actions = data.get("candidate_actions")
    if not isinstance(actions, list) or not actions:
        reasons.append("candidate_actions_missing")
    score = data.get("weighted_score_breakdown")
    if not isinstance(score, dict):
        reasons.append("weighted_score_breakdown_missing")
    elif not score.get("selected_action"):
        reasons.append("selected_action_missing")
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_weighted_decision_validator",
        manifest_type="weighted_decision_engine",
        fixture_subdir="weighted_decision",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
