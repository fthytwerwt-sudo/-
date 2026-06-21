#!/usr/bin/env python3
"""Route post-task RAG/vector maintenance to the safest next action.

The router is intentionally local and dry-run friendly. It reads existing
reports, decides whether to sync/resume/repair/fallback, and writes an audit
decision without calling embedding APIs or mutating DashVector.
"""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DECISION_JSON = common.OUT_DIR / "latest_rag_vector_maintenance_decision.json"
DECISION_MD = common.OUT_DIR / "latest_rag_vector_maintenance_decision.md"
TRACE_JSON = common.OUT_DIR / "trace_event_20260622_rag_vector_maintenance_router.json"
FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "maintenance_router"
GATE_REPORT_PATH = common.OUT_DIR / "latest_vector_sync_gate_report.json"
DELTA_MANIFEST_PATH = common.OUT_DIR / "latest_chunk_delta_manifest.json"
BATCH_MANIFEST_PATH = common.OUT_DIR / "latest_delta_batch_manifest.json"
CHECKPOINT_PATH = common.OUT_DIR / "latest_delta_sync_checkpoint.json"
PARTIAL_MANIFEST_PATH = common.OUT_DIR / "latest_delta_index_partial_manifest.json"
CLEANUP_PLAN_PATH = common.OUT_DIR / "latest_retrieval_stale_doc_cleanup_plan.json"


ACTION_DEFS: dict[str, dict[str, Any]] = {
    "no_vector_sync_needed": {
        "action_label": "no_indexable_change -> no_vector_sync_needed",
        "next_script_to_run": "",
        "repair_layer": "none",
        "safe_to_retry": True,
    },
    "run_delta_planner": {
        "action_label": "indexable_change_detected -> run_delta_planner",
        "next_script_to_run": "python3 scripts/rag_vector_delta_planner.py",
        "repair_layer": "RAG_sync_bus",
        "safe_to_retry": True,
    },
    "run_batch_delta_sync_or_resume": {
        "action_label": "delta_sync_needed -> run_batch_delta_sync_or_resume",
        "next_script_to_run": "python3 scripts/rag_dashvector_sync.py --resume --batch-size 8 --delta-manifest codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
        "repair_layer": "RAG_sync_bus",
        "safe_to_retry": True,
    },
    "resume_from_checkpoint": {
        "action_label": "batch_sync_interrupted -> resume_from_checkpoint",
        "next_script_to_run": "python3 scripts/rag_dashvector_sync.py --resume --batch-size 8 --delta-manifest codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
        "repair_layer": "RAG_sync_bus",
        "safe_to_retry": True,
    },
    "block_RAG_latest_and_continue_batch_sync": {
        "action_label": "final_manifest_missing -> block_RAG_latest_and_continue_batch_sync",
        "next_script_to_run": "python3 scripts/rag_dashvector_sync.py --resume --batch-size 8 --delta-manifest codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
        "repair_layer": "RAG_sync_bus",
        "safe_to_retry": True,
    },
    "run_retrieval_active_filter_and_stale_cleanup_plan": {
        "action_label": "final_manifest_written_but_probe_failed -> run_retrieval_active_filter_and_stale_cleanup_plan",
        "next_script_to_run": "python3 scripts/rag_retrieval_probe.py --dry-run-active-filter && python3 scripts/rag_dashvector_stale_doc_cleanup.py",
        "repair_layer": "retrieval_cleaning_layer",
        "safe_to_retry": True,
    },
    "reject_from_clean_top_k_and_write_cleanup_plan": {
        "action_label": "stale_or_inactive_doc_in_raw_top_k -> reject_from_clean_top_k_and_write_cleanup_plan",
        "next_script_to_run": "python3 scripts/rag_dashvector_stale_doc_cleanup.py",
        "repair_layer": "retrieval_cleaning_layer",
        "safe_to_retry": True,
    },
    "block_RAG_latest_and_route_to_retrieval_repair": {
        "action_label": "clean_top_k_failed -> block_RAG_latest_and_route_to_retrieval_repair",
        "next_script_to_run": "python3 scripts/rag_retrieval_probe.py --dry-run-active-filter",
        "repair_layer": "retrieval_repair",
        "safe_to_retry": True,
    },
    "repo_readback_fallback_or_block": {
        "action_label": "high_risk_task_with_stale_RAG -> repo_readback_fallback_or_block",
        "next_script_to_run": "",
        "repair_layer": "repo_readback_fallback",
        "safe_to_retry": False,
    },
    "require_explicit_user_authorization": {
        "action_label": "full_sync_required -> require_explicit_user_authorization",
        "next_script_to_run": "python3 scripts/post_commit_vector_sync_gate.py --mode sync --full-sync-explicit",
        "repair_layer": "human_decision_gate",
        "safe_to_retry": False,
    },
}


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return common.read_json(path) if path.exists() else {}


def _load_case(case: str | None, case_path: str | None) -> dict[str, Any] | None:
    if case_path:
        return common.read_json(_resolve(case_path))
    if case:
        path = FIXTURE_DIR / f"{case}.json"
        if path.exists():
            return common.read_json(path)
    return None


def _count_from_checkpoint(checkpoint: dict[str, Any], key: str) -> int:
    value = checkpoint.get(key)
    return len(value) if isinstance(value, list) else 0


def _probe_has_stale_docs(probe: dict[str, Any]) -> bool:
    if probe.get("stale_or_inactive_docs_detected") is True:
        return True
    for query_report in probe.get("query_reports", []):
        if query_report.get("stale_or_inactive_docs_detected") is True:
            return True
        for item in query_report.get("top_k_results", []) or []:
            if item.get("blocked_reason") or item.get("active_manifest_allowlist_passed") is False:
                return True
        for item in query_report.get("raw_top_k_results", []) or []:
            if item.get("blocked_reason") or item.get("stale_or_inactive"):
                return True
    return False


def _probe_clean_passed(probe: dict[str, Any]) -> bool:
    if "clean_top_k_passed" in probe:
        return probe.get("clean_top_k_passed") is True
    return probe.get("status") == "passed" and probe.get("source_readback_passed") is True


def load_current_health(task_context: dict[str, Any] | None = None) -> dict[str, Any]:
    task_context = task_context or {}
    git_head = common.current_commit()
    index_manifest = _read_json(common.INDEX_MANIFEST_PATH)
    chunk_manifest = _read_json(common.CHUNK_MANIFEST_PATH)
    gate_report = _read_json(GATE_REPORT_PATH)
    delta_manifest = _read_json(DELTA_MANIFEST_PATH)
    batch_manifest = _read_json(BATCH_MANIFEST_PATH)
    checkpoint = _read_json(CHECKPOINT_PATH)
    partial = _read_json(PARTIAL_MANIFEST_PATH)
    probe = _read_json(common.RETRIEVAL_REPORT_JSON_PATH)
    cleanup = _read_json(CLEANUP_PLAN_PATH)

    index_source_commit = str(index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha") or "")
    gate_change = gate_report.get("indexable_change_result", {}) if isinstance(gate_report.get("indexable_change_result"), dict) else {}
    batch_count = int(batch_manifest.get("batch_count") or len(batch_manifest.get("batches", [])) or 0)
    completed_batch_count = int(partial.get("completed_batch_count") or _count_from_checkpoint(checkpoint, "completed_batch_indexes"))
    failed_batch_count = int(partial.get("failed_batch_count") or _count_from_checkpoint(checkpoint, "failed_batch_indexes"))
    pending_batch_count = int(partial.get("pending_batch_count") or max(0, batch_count - completed_batch_count - failed_batch_count))
    delta_chunk_count = int(batch_manifest.get("total_delta_chunk_count") or gate_report.get("delta_chunk_count") or 0)
    completed_chunk_count = int(partial.get("completed_chunk_count") or _count_from_checkpoint(checkpoint, "completed_chunk_ids"))
    retrieval_probe_passed = probe.get("status") == "passed" and probe.get("source_readback_passed") is True
    clean_top_k_passed = _probe_clean_passed(probe)
    source_readback_passed = probe.get("source_readback_passed") is True
    final_index_manifest_written = bool(index_manifest) and not bool(index_manifest.get("blocked"))
    vector_latest_allowed = (
        final_index_manifest_written
        and index_source_commit == git_head
        and retrieval_probe_passed
        and clean_top_k_passed
        and source_readback_passed
    )
    return {
        "task_context": {
            "task_type": task_context.get("task_type") or "RAG_vector_maintenance",
            "risk_level": task_context.get("risk_level") or "medium",
            "current_git_head": git_head,
            "source_commit_sha": index_source_commit,
            "full_sync_required": bool(task_context.get("full_sync_required")),
        },
        "vector_health": {
            "index_manifest_exists": common.INDEX_MANIFEST_PATH.exists(),
            "index_manifest_valid": final_index_manifest_written and bool(index_manifest.get("chunks")),
            "source_commit_matches_head": bool(index_source_commit) and index_source_commit == git_head,
            "current_RAG_index_latest_claim_allowed": vector_latest_allowed,
            "index_manifest_path": common.INDEX_MANIFEST_PATH.as_posix(),
            "index_source_commit_sha": index_source_commit,
            "chunk_manifest_commit_sha": chunk_manifest.get("commit_sha"),
            "final_index_manifest_written": final_index_manifest_written,
        },
        "sync_health": {
            "sync_required": bool(gate_change.get("sync_required")) if gate_change else (index_source_commit != git_head),
            "delta_manifest_exists": DELTA_MANIFEST_PATH.exists(),
            "batch_manifest_exists": BATCH_MANIFEST_PATH.exists(),
            "checkpoint_exists": CHECKPOINT_PATH.exists(),
            "completed_batch_count": completed_batch_count,
            "failed_batch_count": failed_batch_count,
            "pending_batch_count": pending_batch_count,
            "completed_chunk_count": completed_chunk_count,
            "delta_chunk_count": delta_chunk_count,
            "batch_count": batch_count,
            "resume_available": bool(checkpoint and (completed_batch_count or failed_batch_count or pending_batch_count)),
            "gate_status": gate_report.get("status") or "",
            "partial_manifest_status": partial.get("status") or "",
        },
        "retrieval_health": {
            "retrieval_probe_passed": retrieval_probe_passed,
            "source_readback_passed": source_readback_passed,
            "stale_or_inactive_docs_detected": _probe_has_stale_docs(probe) or int(cleanup.get("stale_doc_count") or 0) > 0,
            "clean_top_k_passed": clean_top_k_passed,
            "retrieval_probe_path": common.RETRIEVAL_REPORT_JSON_PATH.as_posix(),
            "cleanup_plan_exists": CLEANUP_PLAN_PATH.exists(),
            "cleanup_plan_path": CLEANUP_PLAN_PATH.as_posix(),
        },
        "raw_reports": {
            "gate_report_status": gate_report.get("status"),
            "retrieval_report_status": probe.get("status"),
        },
    }


def _merge_case_health(base: dict[str, Any], case: dict[str, Any] | None) -> dict[str, Any]:
    if not case:
        return base
    merged = json.loads(json.dumps(base, ensure_ascii=False))
    for key in ("task_context", "vector_health", "sync_health", "retrieval_health"):
        merged.setdefault(key, {})
        merged[key].update(case.get(key, {}))
    merged["case_id"] = case.get("case_id")
    merged["expected_action_id"] = case.get("expected_action_id")
    return merged


def select_action(health: dict[str, Any]) -> tuple[str, str, list[str]]:
    task = health["task_context"]
    vector = health["vector_health"]
    sync = health["sync_health"]
    retrieval = health["retrieval_health"]
    blocked_if = [
        "external_api_required_for_dry_run",
        "physical_delete_or_tombstone_requested_without_authorization",
        "RAG_latest_claim_without_final_manifest_and_probe",
    ]
    if task.get("full_sync_required"):
        return "require_explicit_user_authorization", "Full sync is outside the daily default and requires explicit user authorization.", blocked_if
    if task.get("risk_level") == "high" and not vector.get("current_RAG_index_latest_claim_allowed"):
        return "repo_readback_fallback_or_block", "High-risk tasks cannot rely on stale or unprobed RAG; use repo readback or block.", blocked_if
    if sync.get("failed_batch_count", 0) > 0 or (sync.get("pending_batch_count", 0) > 0 and sync.get("resume_available")):
        return "resume_from_checkpoint", "Batch sync is incomplete and a checkpoint is available, so resume before any latest claim.", blocked_if
    if sync.get("sync_required") and not sync.get("delta_manifest_exists"):
        return "run_delta_planner", "Indexable changes are detected but no delta manifest exists yet.", blocked_if
    if sync.get("delta_manifest_exists") and not sync.get("batch_manifest_exists"):
        return "run_batch_delta_sync_or_resume", "Delta manifest exists but batch execution has not been planned or completed.", blocked_if
    if sync.get("sync_required") and not vector.get("final_index_manifest_written"):
        return "block_RAG_latest_and_continue_batch_sync", "Sync is required and the final index manifest is not safely written.", blocked_if
    if vector.get("final_index_manifest_written") and not retrieval.get("retrieval_probe_passed"):
        if retrieval.get("stale_or_inactive_docs_detected"):
            return "run_retrieval_active_filter_and_stale_cleanup_plan", "Final manifest exists but retrieval found stale or inactive raw candidates.", blocked_if
        if not retrieval.get("clean_top_k_passed"):
            return "block_RAG_latest_and_route_to_retrieval_repair", "Clean top-k did not pass, so RAG latest stays blocked.", blocked_if
        return "block_RAG_latest_and_route_to_retrieval_repair", "Retrieval probe failed after final manifest, so repair retrieval before latest claim.", blocked_if
    if retrieval.get("stale_or_inactive_docs_detected") and retrieval.get("clean_top_k_passed"):
        return "reject_from_clean_top_k_and_write_cleanup_plan", "Raw top-k contains stale docs but clean top-k still passes after filtering.", blocked_if
    if not sync.get("sync_required"):
        return "no_vector_sync_needed", "No indexable change requires vector sync for this maintenance pass.", blocked_if
    return "run_batch_delta_sync_or_resume", "Delta sync is required by default daily policy.", blocked_if


def build_decision(case: dict[str, Any] | None = None, *, dry_run: bool = True) -> dict[str, Any]:
    base = load_current_health((case or {}).get("task_context") if case else None)
    health = _merge_case_health(base, case)
    action_id, reason, blocked_if = select_action(health)
    action = ACTION_DEFS[action_id]
    selected_action = {
        "action_id": action_id,
        "action_label": action["action_label"],
        "reason": reason,
        "blocked_if": blocked_if,
        "next_script_to_run": action["next_script_to_run"],
    }
    decision = {
        "manifest_type": "rag_vector_maintenance_decision",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "generated_at": common.now_iso(),
        "case_id": health.get("case_id") or "current_reports",
        "dry_run": dry_run,
        "task_context": health["task_context"],
        "vector_health": health["vector_health"],
        "sync_health": health["sync_health"],
        "retrieval_health": health["retrieval_health"],
        "selected_action": selected_action,
        "downgrade_policy": {
            "allow_repo_readback_fallback": action_id == "repo_readback_fallback_or_block",
            "allow_stale_RAG_as_reference_only": not health["vector_health"].get("current_RAG_index_latest_claim_allowed"),
            "user_review_required": action_id in {"repo_readback_fallback_or_block", "require_explicit_user_authorization"},
        },
        "repair_policy": {
            "repair_layer": action["repair_layer"],
            "repair_script": action["next_script_to_run"],
            "safe_to_retry": action["safe_to_retry"],
        },
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_query_called": False,
            "dashvector_upsert_called": False,
            "dashvector_delete_called": False,
        },
        "status": "passed",
        "current_RAG_index_latest_claim": False,
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    return decision


def write_decision_markdown(decision: dict[str, Any], path: pathlib.Path = DECISION_MD) -> None:
    lines = [
        "# RAG Vector Maintenance Decision",
        "",
        f"- status: `{decision['status']}`",
        f"- case_id: `{decision['case_id']}`",
        f"- action_id: `{decision['selected_action']['action_id']}`",
        f"- action_label: `{decision['selected_action']['action_label']}`",
        f"- reason: {decision['selected_action']['reason']}",
        f"- current_git_head: `{decision['task_context']['current_git_head']}`",
        f"- source_commit_sha: `{decision['task_context']['source_commit_sha']}`",
        f"- current_RAG_index_latest_claim_allowed: `{str(decision['vector_health']['current_RAG_index_latest_claim_allowed']).lower()}`",
        f"- retrieval_probe_passed: `{str(decision['retrieval_health']['retrieval_probe_passed']).lower()}`",
        f"- clean_top_k_passed: `{str(decision['retrieval_health']['clean_top_k_passed']).lower()}`",
        f"- stale_or_inactive_docs_detected: `{str(decision['retrieval_health']['stale_or_inactive_docs_detected']).lower()}`",
        "- alibaba_embedding_api_called: `false`",
        "- dashvector_upsert_called: `false`",
        "- dashvector_delete_called: `false`",
        "",
        "## Next Script",
        "",
        f"`{decision['selected_action']['next_script_to_run']}`",
    ]
    common.write_markdown(path, lines)


def write_trace(decision: dict[str, Any], path: pathlib.Path = TRACE_JSON) -> dict[str, Any]:
    trace = {
        "created_at": common.now_iso(),
        "event_id": "20260622_rag_vector_maintenance_router",
        "event_type": "rag_vector_maintenance_router.decision_written",
        "task_goal": "route_vector_sync_degradation_cleanup_and_repair",
        "selected_action": decision["selected_action"],
        "current_RAG_index_latest_claim": False,
        "external_call_report": decision["external_call_report"],
        "files_written": [
            DECISION_JSON.as_posix(),
            DECISION_MD.as_posix(),
            TRACE_JSON.as_posix(),
        ],
        "status": "passed",
    }
    common.write_json(path, trace)
    return trace


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Route RAG/vector maintenance after a Codex task.")
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--case")
    parser.add_argument("--case-path")
    parser.add_argument("--risk-level", choices=("low", "medium", "high"), default=None)
    parser.add_argument("--task-type", default=None)
    parser.add_argument("--full-sync-required", action="store_true")
    parser.add_argument("--out", default=str(DECISION_JSON))
    parser.add_argument("--md-out", default=str(DECISION_MD))
    args = parser.parse_args()

    case = _load_case(args.case, args.case_path) or {}
    task_context = case.setdefault("task_context", {})
    if args.risk_level:
        task_context["risk_level"] = args.risk_level
    if args.task_type:
        task_context["task_type"] = args.task_type
    if args.full_sync_required:
        task_context["full_sync_required"] = True
    decision = build_decision(case or None, dry_run=True)
    out_path = _resolve(args.out)
    md_path = _resolve(args.md_out)
    common.write_json(out_path, decision)
    write_decision_markdown(decision, md_path)
    write_trace(decision)
    print(
        json.dumps(
            {
                "status": decision["status"],
                "action_id": decision["selected_action"]["action_id"],
                "decision_path": out_path.as_posix(),
                "current_RAG_index_latest_claim": False,
                "alibaba_embedding_api_called": False,
                "dashvector_upsert_called": False,
                "dashvector_delete_called": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
