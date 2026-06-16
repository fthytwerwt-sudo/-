"""Completion truth checks for the adapter branch candidate."""

from __future__ import annotations

from typing import Mapping

from .task_packet import STOPLINE


BLOCKED_CLAIM_TYPES: dict[str, str] = {
    "technical_preview_as_completed": "technical preview cannot satisfy the requested completion boundary",
    "route_card_as_completed": "route card alone is not executable completion evidence",
    "report_only_as_completed": "report-only output cannot replace runnable no-render validation",
    "no_review_pack_as_completed": "review pack absence must remain a blocker for editing delivery",
    "full_code_integration_ready_claim": "branch-local candidate cannot claim whole-codebase readiness",
}


def evaluate_completion_claim(claim_type: str, evidence: Mapping[str, object] | None = None) -> dict[str, object]:
    evidence = evidence or {}
    if claim_type in BLOCKED_CLAIM_TYPES:
        return {
            "claim_type": claim_type,
            "claim_allowed": False,
            "status": "blocked",
            "blocked_reasons": [BLOCKED_CLAIM_TYPES[claim_type]],
            "evidence_summary": dict(evidence),
        }
    return {
        "claim_type": claim_type,
        "claim_allowed": True,
        "status": "allowed",
        "blocked_reasons": [],
        "evidence_summary": dict(evidence),
    }


def run_false_completion_guards() -> dict[str, object]:
    results = [evaluate_completion_claim(claim_type) for claim_type in BLOCKED_CLAIM_TYPES]
    return {
        "status": "passed" if all(item["status"] == "blocked" for item in results) else "failed",
        "blocked_claim_count": len(results),
        "blocked_claims": results,
    }


def evaluate_adapter_candidate_stopline(
    *,
    samples_total: int,
    samples_routed: int,
    editing_validation_status: str,
) -> dict[str, object]:
    blockers: list[str] = []
    if samples_total != 6:
        blockers.append("sample_count_mismatch")
    if samples_routed != 6:
        blockers.append("workflow_route_incomplete")
    if editing_validation_status != "passed":
        blockers.append("editing_contract_validation_not_passed")

    return {
        "status": "allowed_for_branch_candidate" if not blockers else "blocked",
        "stopline": STOPLINE,
        "candidate_claim_allowed": not blockers,
        "blocked_reasons": blockers,
        "allowed_meaning": "branch-local no-render candidate may enter a later runtime probe request",
    }
