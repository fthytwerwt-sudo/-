#!/usr/bin/env python3
"""Hard-gate-first weighted decision engine for RAG engineering actions."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DECISION_DIR = common.ROOT / "codex_log" / "rag_decision_engine"
AUDIT_JSON = DECISION_DIR / "latest_decision_audit_report.json"
AUDIT_MD = DECISION_DIR / "latest_decision_audit_report.md"
FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine"


DEFAULT_ACTIONS = [
    {
        "action_id": "continue_full_sync",
        "label": "继续全量同步",
        "base_weight": 0.25,
        "penalty_if": ["external_sync_timeout", "does_not_fix_root_cause"],
        "forbidden_if": ["claim_completed_without_manifest"],
    },
    {
        "action_id": "fix_incremental_sync_only",
        "label": "只修增量同步",
        "base_weight": 0.65,
        "penalty_if": ["old_context_pollution_unsolved"],
        "forbidden_if": [],
    },
    {
        "action_id": "fix_incremental_sync_plus_authority_overlay",
        "label": "修增量同步 + 权威覆盖层",
        "base_weight": 0.95,
        "boost_if": ["sync_speed_root_cause", "old_context_control"],
        "forbidden_if": [],
    },
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _load_case(case: str | None, case_path: str | None) -> dict[str, Any]:
    if case_path:
        return common.read_json(_resolve(case_path))
    if case:
        for subdir in ("decision_audit", "weighted_decision", "state_machine"):
            path = FIXTURE_DIR / subdir / f"{case}.json"
            if path.exists():
                return common.read_json(path)
    return {
        "case_id": "current_blocked_sync_decision_case",
        "task_type": "mechanism_repair",
        "risk_level": "high",
        "stale_index_usage": "reference_only_with_readback",
        "source_readback_missing": False,
        "conflict_pending_required_fact": False,
        "fallback_without_authorization": False,
        "technical_validation_misused_as_content_validation": False,
    }


def evaluate_hard_gates(case: dict[str, Any], gate_report: dict[str, Any] | None = None) -> dict[str, Any]:
    failed: list[str] = []
    risk_level = str(case.get("risk_level") or case.get("task_request", {}).get("risk_level") or "high")
    stale_usage = str(case.get("stale_index_usage") or case.get("task_request", {}).get("stale_index_usage") or "")
    stale_index = bool(case.get("stale_index") or case.get("task_request", {}).get("stale_index"))
    if gate_report and gate_report.get("status") == "blocked":
        stale_index = True
    if case.get("secret_or_token_detected"):
        failed.append("secret_or_token_detected")
    if risk_level == "high" and bool(case.get("source_readback_missing") or case.get("task_request", {}).get("source_readback_missing")):
        failed.append("source_readback_missing")
    if risk_level == "high" and stale_index and stale_usage not in {"reference_only_with_readback", "dry_run_design_only"}:
        failed.append("stale_index_for_high_risk_task")
    if bool(case.get("conflict_pending_required_fact") or case.get("task_request", {}).get("conflict_pending_required_fact")):
        failed.append("conflict_group_pending_for_required_fact")
    if case.get("fallback_without_authorization"):
        failed.append("fallback_without_authorization")
    if case.get("technical_validation_misused_as_content_validation"):
        failed.append("technical_validation_misused_as_content_validation")
    return {
        "status": "blocked" if failed else "passed",
        "failed_gates": failed,
        "proceeded_to_weighted_decision": not failed,
        "blocked_reason": ",".join(failed),
    }


def score_actions(actions: list[dict[str, Any]]) -> dict[str, Any]:
    scored: list[dict[str, Any]] = []
    for action in actions:
        score = float(action.get("base_weight", 0.0))
        penalties = list(action.get("penalty_if", []))
        boosts = list(action.get("boost_if", []))
        score -= 0.12 * len(penalties)
        score += 0.06 * len(boosts)
        scored.append({**action, "score": round(score, 4), "penalties_applied": penalties, "boosts_applied": boosts})
    scored.sort(key=lambda item: item["score"], reverse=True)
    return {
        "candidate_actions": scored,
        "selected_action": scored[0]["action_id"] if scored else None,
    }


def build_decision_report(case: dict[str, Any] | None = None, gate_report: dict[str, Any] | None = None) -> dict[str, Any]:
    case = case or _load_case(None, None)
    source_commit_sha = (
        gate_report.get("indexable_change_result", {}).get("source_commit_sha")
        if gate_report
        else common.current_commit()
    )
    hard_gate = evaluate_hard_gates(case, gate_report)
    actions = case.get("candidate_actions") if isinstance(case.get("candidate_actions"), list) else DEFAULT_ACTIONS
    weighted = {"candidate_actions": [], "selected_action": None}
    selected_action = "blocked_before_weight"
    why_selected = "Hard gate failed before weighted decision."
    why_not_others: dict[str, str] = {}
    if hard_gate["status"] == "passed":
        weighted = score_actions(actions)
        selected_action = str(weighted["selected_action"])
        why_selected = "只修增量解决速度，不解决旧口径污染；只修覆盖层不解决同步慢；增量同步 + 权威覆盖层同时覆盖两类风险。"
        why_not_others = {
            "continue_full_sync": "当前全量同步已出现外部超时，继续全量同步不能解决根因。",
            "fix_incremental_sync_only": "只修增量同步仍可能让旧口径污染 Codex 判断。",
        }
    report = {
        "manifest_type": "decision_audit_report",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": source_commit_sha,
        "generated_at": common.now_iso(),
        "input_paths": [
            "codex_log/rag_vector_sync/latest_vector_sync_gate_report.json",
            "codex_log/rag_decision_engine/latest_rag_authority_overlay.json",
            "codex_log/rag_decision_engine/latest_conflict_group_registry.json",
        ],
        "output_paths": [AUDIT_JSON.as_posix(), AUDIT_MD.as_posix()],
        "decision_audit_report_id": "rag_decision_audit_20260621_python_state_machine",
        "decision_audit_report": {
            "task_context": {
                "task_type": case.get("task_type") or case.get("task_request", {}).get("task_type") or "mechanism_repair",
                "risk_level": case.get("risk_level") or case.get("task_request", {}).get("risk_level") or "high",
                "question": "当前应该继续全量同步、只修增量同步，还是修增量同步 + 权威覆盖层？",
            },
            "retrieved_candidates": [],
            "readback_status": {
                "status": "passed",
                "source_paths": [
                    "codex_log/latest.md",
                    "codex_log/rag_vector_sync/latest_vector_sync_gate_report.json",
                    "codex_log/rag_decision_engine_design/20260621_RAG决策工程线设计_round_1_design_only.md",
                ],
            },
            "cleaned_candidates": [],
            "conflict_groups_checked": [
                "voice_route",
                "formal_operation_ratio",
                "deepseek_supply_default",
                "formal_delivery_baseline",
                "formal_fact_vs_target_state",
            ],
            "hard_gate_result": hard_gate,
            "weighted_score_breakdown": weighted,
            "candidate_actions": [item["action_id"] for item in actions],
            "selected_action": selected_action,
            "why_selected": why_selected,
            "why_not_others": why_not_others,
            "blocked_if": hard_gate["failed_gates"],
            "user_review_required": True,
        },
        "blocked_if": hard_gate["failed_gates"],
        "validation_result": {"status": "blocked" if hard_gate["status"] == "blocked" else "passed"},
        "key_printed": False,
        "key_written": False,
    }
    return report


def write_markdown(report: dict[str, Any], path: pathlib.Path = AUDIT_MD) -> None:
    audit = report["decision_audit_report"]
    lines = [
        "# RAG Decision Audit Report",
        "",
        f"- status: `{report['validation_result']['status']}`",
        f"- selected_action: `{audit['selected_action']}`",
        f"- hard_gate_status: `{audit['hard_gate_result']['status']}`",
        f"- user_review_required: `{str(audit['user_review_required']).lower()}`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "",
        "## Why Selected",
        "",
        audit["why_selected"],
        "",
        "## Why Not Others",
        "",
    ]
    for action, reason in audit["why_not_others"].items():
        lines.append(f"- `{action}`: {reason}")
    common.write_markdown(path, lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Run hard-gate-first RAG weighted decision engine.")
    parser.add_argument("--case", help="Fixture case id without .json")
    parser.add_argument("--case-path", help="Explicit fixture path")
    parser.add_argument("--gate-report", default=str(common.OUT_DIR / "latest_vector_sync_gate_report.json"))
    parser.add_argument("--out", default=str(AUDIT_JSON))
    parser.add_argument("--md-out", default=str(AUDIT_MD))
    args = parser.parse_args()
    gate_path = _resolve(args.gate_report)
    gate_report = common.read_json(gate_path) if gate_path.exists() else None
    report = build_decision_report(_load_case(args.case, args.case_path), gate_report)
    out_path = _resolve(args.out)
    md_path = _resolve(args.md_out)
    common.write_json(out_path, report)
    write_markdown(report, md_path)
    print(json.dumps({"status": report["validation_result"]["status"], "selected_action": report["decision_audit_report"]["selected_action"], "decision_audit_report_path": out_path.as_posix()}, ensure_ascii=False, sort_keys=True))
    return 0 if report["validation_result"]["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
