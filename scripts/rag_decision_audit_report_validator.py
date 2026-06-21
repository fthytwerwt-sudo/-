#!/usr/bin/env python3
"""Validate user-readable decision audit report fixtures and outputs."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["decision_audit_report"]
AUDIT_FIELDS = [
    "task_context",
    "retrieved_candidates",
    "readback_status",
    "cleaned_candidates",
    "conflict_groups_checked",
    "hard_gate_result",
    "weighted_score_breakdown",
    "candidate_actions",
    "selected_action",
    "why_selected",
    "why_not_others",
    "blocked_if",
    "user_review_required",
]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    report = data.get("decision_audit_report")
    if not isinstance(report, dict):
        return ["decision_audit_report_missing"]
    for field in AUDIT_FIELDS:
        if field not in report:
            reasons.append(f"{field}_missing")
    if not report.get("why_selected"):
        reasons.append("why_selected_missing")
    actions = report.get("candidate_actions")
    why_not = report.get("why_not_others")
    if isinstance(actions, list) and len(actions) > 1 and not why_not:
        reasons.append("why_not_others_missing")
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_decision_audit_report_validator",
        manifest_type="decision_audit_report",
        fixture_subdir="decision_audit",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
