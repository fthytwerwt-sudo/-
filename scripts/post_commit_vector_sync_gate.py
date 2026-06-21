#!/usr/bin/env python3
"""Post-commit gate for keeping DashVector aligned with indexable source commits.

Modes:
- check: detect whether the current commit has indexable changes since the
  latest source_commit_sha. No external API calls.
- sync: run source inventory, chunking, DashVector upsert, retrieval probe, and
  write evidence when sync is required.
- finish: Codex completion gate alias for sync-or-skip.

The gate writes only sanitized evidence. It never prints API keys or vectors.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
from typing import Any

import rag_common as common


GATE_REPORT_JSON = common.OUT_DIR / "latest_vector_sync_gate_report.json"
GATE_REPORT_MD = common.OUT_DIR / "latest_vector_sync_gate_report.md"
DELTA_BATCH_MANIFEST_PATH = common.OUT_DIR / "latest_delta_batch_manifest.json"
DELTA_CHECKPOINT_PATH = common.OUT_DIR / "latest_delta_sync_checkpoint.json"
DELTA_PARTIAL_MANIFEST_PATH = common.OUT_DIR / "latest_delta_index_partial_manifest.json"
DELTA_TIMEOUT_REPORT_PATH = common.OUT_DIR / "latest_delta_sync_timeout_report.json"
MAINTENANCE_DECISION_PATH = common.OUT_DIR / "latest_rag_vector_maintenance_decision.json"


def _run_git(args: list[str], *, check: bool = True) -> str:
    return common.run_git(args, check=check)


def _path_is_dynamic_audit(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in common.DYNAMIC_AUDIT_PREFIXES)


def _path_is_indexable(path: str) -> bool:
    if _path_is_dynamic_audit(path):
        return False
    if common.deny_reason(path) is not None:
        return False
    return common.allowed_by_pattern(path)


def _changed_files(previous_commit: str, current_commit: str) -> tuple[list[str], list[str], list[dict[str, str]]]:
    output = _run_git(["diff", "--name-status", previous_commit, current_commit], check=False)
    changed: list[str] = []
    deleted: list[str] = []
    raw: list[dict[str, str]] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        path = parts[-1]
        raw.append({"status": status, "path": path})
        if status.startswith("D"):
            deleted.append(path)
        else:
            changed.append(path)
    return changed, deleted, raw


def detect_indexable_changes(index_manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    manifest = index_manifest if index_manifest is not None else common.read_json(common.INDEX_MANIFEST_PATH)
    previous_commit = str(manifest.get("source_commit_sha") or manifest.get("commit_sha") or "")
    current_commit = common.current_commit()
    if not previous_commit:
        return {
            "source_commit_sha": current_commit,
            "previous_index_commit_sha": "",
            "indexable_changed": True,
            "changed_indexable_files": [],
            "deleted_indexable_files": [],
            "dynamic_audit_only": False,
            "sync_required": True,
            "skip_reason": "",
            "blocked_reasons": ["previous_index_commit_missing"],
        }

    changed, deleted, raw = _changed_files(previous_commit, current_commit)
    changed_indexable = [path for path in changed if _path_is_indexable(path)]
    deleted_indexable = [path for path in deleted if _path_is_indexable(path)]
    all_changed_paths = changed + deleted
    dynamic_audit_only = bool(all_changed_paths) and all(_path_is_dynamic_audit(path) for path in all_changed_paths)
    indexable_changed = bool(changed_indexable or deleted_indexable)
    sync_required = indexable_changed
    if previous_commit == current_commit:
        skip_reason = "already_indexed_current_commit"
        sync_required = False
    elif dynamic_audit_only:
        skip_reason = "dynamic_audit_only"
        sync_required = False
    elif not indexable_changed:
        skip_reason = "no_indexable_file_changes"
    else:
        skip_reason = ""
    return {
        "source_commit_sha": current_commit,
        "previous_index_commit_sha": previous_commit,
        "indexable_changed": indexable_changed,
        "changed_indexable_files": sorted(changed_indexable),
        "deleted_indexable_files": sorted(deleted_indexable),
        "dynamic_audit_only": dynamic_audit_only,
        "sync_required": sync_required,
        "skip_reason": skip_reason,
        "raw_changed_files": raw[:200],
        "blocked_reasons": [],
    }


def _run_command(args: list[str]) -> dict[str, Any]:
    completed = subprocess.run(
        args,
        cwd=common.ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "command": " ".join(args),
        "returncode": completed.returncode,
        "stdout_tail": completed.stdout[-3000:],
        "stderr_tail": completed.stderr[-2000:],
        "passed": completed.returncode == 0,
    }


def _write_gate_report(report: dict[str, Any]) -> None:
    common.write_json(GATE_REPORT_JSON, report)
    refresh = _refresh_maintenance_decision()
    report.update(refresh)
    report.update(_read_maintenance_decision_fields())
    common.write_json(GATE_REPORT_JSON, report)
    lines = [
        "# Post-Commit Vector Sync Gate Report",
        "",
        f"- status: `{report['status']}`",
        f"- mode: `{report['mode']}`",
        f"- source_commit_sha: `{report['indexable_change_result']['source_commit_sha']}`",
        f"- previous_index_commit_sha: `{report['indexable_change_result']['previous_index_commit_sha']}`",
        f"- sync_required: `{str(report['indexable_change_result']['sync_required']).lower()}`",
        f"- skip_reason: `{report['indexable_change_result'].get('skip_reason') or ''}`",
        f"- changed_indexable_file_count: `{len(report['indexable_change_result'].get('changed_indexable_files', []))}`",
        f"- deleted_indexable_file_count: `{len(report['indexable_change_result'].get('deleted_indexable_files', []))}`",
        f"- delta_chunks_to_embed: `{report.get('delta_counts', {}).get('delta_chunks_to_embed', '')}`",
        f"- unchanged_chunk_count: `{report.get('delta_counts', {}).get('unchanged_chunks', '')}`",
        f"- batch_sync_enabled: `{str(report.get('batch_sync_enabled', False)).lower()}`",
        f"- batch_manifest_path: `{report.get('batch_manifest_path') or ''}`",
        f"- checkpoint_path: `{report.get('checkpoint_path') or ''}`",
        f"- partial_manifest_path: `{report.get('partial_manifest_path') or ''}`",
        f"- batch_count: `{report.get('batch_count', '')}`",
        f"- completed_batch_count: `{report.get('completed_batch_count', '')}`",
        f"- failed_batch_count: `{report.get('failed_batch_count', '')}`",
        f"- pending_batch_count: `{report.get('pending_batch_count', '')}`",
        f"- completed_chunk_count: `{report.get('completed_chunk_count', '')}`",
        f"- delta_chunk_count: `{report.get('delta_chunk_count', '')}`",
        f"- resume_available: `{str(report.get('resume_available', False)).lower()}`",
        f"- last_completed_batch_index: `{report.get('last_completed_batch_index', '')}`",
        f"- timeout_stage: `{report.get('timeout_stage') or ''}`",
        f"- maintenance_router_refresh_status: `{report.get('maintenance_router_refresh_status') or ''}`",
        f"- maintenance_router_refresh_error: `{report.get('maintenance_router_refresh_error') or ''}`",
        f"- maintenance_decision_path: `{report.get('maintenance_decision_path') or ''}`",
        f"- maintenance_action_id: `{report.get('maintenance_action_id') or ''}`",
        f"- maintenance_repair_layer: `{report.get('maintenance_repair_layer') or ''}`",
        f"- maintenance_next_script_to_run: `{report.get('maintenance_next_script_to_run') or ''}`",
        f"- maintenance_RAG_latest_claim_allowed: `{str(report.get('maintenance_RAG_latest_claim_allowed', False)).lower()}`",
        f"- maintenance_decision_generated_at: `{report.get('maintenance_decision_generated_at') or ''}`",
        f"- indexed_file_count: `{report.get('indexed_file_count', '')}`",
        f"- indexed_chunk_count: `{report.get('indexed_chunk_count', '')}`",
        f"- alibaba_embedding_api_called: `{str(report['external_call_report']['alibaba_embedding_api_called']).lower()}`",
        f"- dashvector_upsert_called: `{str(report['external_call_report']['dashvector_upsert_called']).lower()}`",
        f"- dashvector_query_called: `{str(report['external_call_report']['dashvector_query_called']).lower()}`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "- vector_values_written: `false`",
    ]
    if report.get("blocked_reasons"):
        lines.extend(["", "## Blocked Reasons", ""])
        lines.extend(f"- `{reason}`" for reason in report["blocked_reasons"])
    if report["indexable_change_result"].get("changed_indexable_files"):
        lines.extend(["", "## Changed Indexable Files", ""])
        lines.extend(f"- `{path}`" for path in report["indexable_change_result"]["changed_indexable_files"][:80])
    common.write_markdown(GATE_REPORT_MD, lines)


def _refresh_maintenance_decision() -> dict[str, Any]:
    result = _run_command(["python3", "scripts/rag_vector_maintenance_router.py", "--dry-run"])
    fields: dict[str, Any] = {
        "maintenance_router_refresh_command": result["command"],
        "maintenance_router_refresh_status": "passed" if result["passed"] else "blocked",
        "maintenance_router_refresh_returncode": result["returncode"],
        "maintenance_router_refresh_error": "",
    }
    if not result["passed"]:
        fields["maintenance_router_refresh_error"] = result.get("stderr_tail") or result.get("stdout_tail") or "maintenance_router_refresh_failed"
    return fields


def _read_maintenance_decision_fields() -> dict[str, Any]:
    fields: dict[str, Any] = {
        "maintenance_decision_path": MAINTENANCE_DECISION_PATH.as_posix(),
        "maintenance_action_id": None,
        "maintenance_repair_layer": None,
        "maintenance_next_script_to_run": None,
        "maintenance_RAG_latest_claim_allowed": False,
        "maintenance_decision_generated_at": None,
    }
    if not MAINTENANCE_DECISION_PATH.exists():
        return fields
    decision = common.read_json(MAINTENANCE_DECISION_PATH)
    fields.update(
        {
            "maintenance_action_id": decision.get("selected_action", {}).get("action_id"),
            "maintenance_repair_layer": decision.get("repair_policy", {}).get("repair_layer"),
            "maintenance_next_script_to_run": decision.get("selected_action", {}).get("next_script_to_run"),
            "maintenance_RAG_latest_claim_allowed": bool(decision.get("vector_health", {}).get("current_RAG_index_latest_claim_allowed")),
            "maintenance_decision_generated_at": decision.get("generated_at"),
        }
    )
    return fields


def _read_batch_progress_fields() -> dict[str, Any]:
    fields: dict[str, Any] = {
        "batch_sync_enabled": False,
        "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
        "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
        "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
        "batch_count": 0,
        "completed_batch_count": 0,
        "failed_batch_count": 0,
        "pending_batch_count": 0,
        "completed_chunk_count": 0,
        "delta_chunk_count": 0,
        "resume_available": False,
        "last_completed_batch_index": None,
        "timeout_stage": None,
    }
    if not DELTA_BATCH_MANIFEST_PATH.exists():
        return fields
    batch_manifest = common.read_json(DELTA_BATCH_MANIFEST_PATH)
    checkpoint = common.read_json(DELTA_CHECKPOINT_PATH) if DELTA_CHECKPOINT_PATH.exists() else {}
    partial = common.read_json(DELTA_PARTIAL_MANIFEST_PATH) if DELTA_PARTIAL_MANIFEST_PATH.exists() else {}
    timeout = partial.get("timeout_report") if isinstance(partial.get("timeout_report"), dict) else {}
    completed = set(int(item) for item in checkpoint.get("completed_batch_indexes", []))
    failed = set(int(item) for item in checkpoint.get("failed_batch_indexes", []))
    batch_count = int(batch_manifest.get("batch_count") or len(batch_manifest.get("batches", [])))
    pending_count = int(partial.get("pending_batch_count") or max(0, batch_count - len(completed) - len(failed)))
    fields.update(
        {
            "batch_sync_enabled": True,
            "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
            "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
            "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
            "batch_count": batch_count,
            "completed_batch_count": int(partial.get("completed_batch_count") or len(completed)),
            "failed_batch_count": int(partial.get("failed_batch_count") or len(failed)),
            "pending_batch_count": pending_count,
            "completed_chunk_count": int(partial.get("completed_chunk_count") or len(set(checkpoint.get("completed_chunk_ids", [])))),
            "delta_chunk_count": int(batch_manifest.get("total_delta_chunk_count") or 0),
            "resume_available": bool(completed or failed),
            "last_completed_batch_index": max(completed) if completed else None,
            "timeout_stage": timeout.get("stage"),
            "partial_manifest_status": partial.get("status"),
        }
    )
    return fields


def _read_manifest_counts() -> dict[str, Any]:
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    chunk_manifest = common.read_json(common.CHUNK_MANIFEST_PATH)
    return {
        "indexed_file_count": index_manifest.get("indexed_file_count"),
        "indexed_chunk_count": index_manifest.get("indexed_chunk_count"),
        "chunk_manifest_count": chunk_manifest.get("chunk_count"),
        "source_commit_sha": index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha"),
        "dashvector_collection": index_manifest.get("dashvector_collection"),
    }


def _run_delta_planner(report: dict[str, Any]) -> dict[str, Any] | None:
    result = _run_command(["python3", "scripts/rag_vector_delta_planner.py"])
    report["commands"].append(result)
    if not result["passed"]:
        report["status"] = "blocked"
        report["blocked_reasons"].append("command_failed:python3 scripts/rag_vector_delta_planner.py")
        return None
    delta_manifest = common.read_json(common.OUT_DIR / "latest_chunk_delta_manifest.json")
    report["delta_counts"] = delta_manifest.get("chunk_delta_counts", {})
    return delta_manifest


def _run_delta_dry_run(report: dict[str, Any], batch_size: int) -> bool:
    result = _run_command(
        [
            "python3",
            "scripts/rag_dashvector_sync.py",
            "--dry-run-delta",
            "--batch-size",
            str(batch_size),
            "--delta-manifest",
            "codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
        ]
    )
    report["commands"].append(result)
    if not result["passed"]:
        report["status"] = "blocked"
        report["blocked_reasons"].append("command_failed:python3 scripts/rag_dashvector_sync.py --dry-run-delta")
        report.update(_read_batch_progress_fields())
        return False
    report.update(_read_batch_progress_fields())
    return True


def run_sync_pipeline(
    mode: str,
    batch_size: int,
    *,
    real_delta_sync: bool = False,
    full_sync_explicit: bool = False,
) -> dict[str, Any]:
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    change_result = detect_indexable_changes(index_manifest)
    report: dict[str, Any] = {
        "gate_name": "post_commit_vector_sync_gate",
        "mode": mode,
        "generated_at": common.now_iso(),
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "indexable_change_result": change_result,
        "commands": [],
        "status": "skipped",
        "blocked_reasons": [],
        "current_RAG_index_latest_claim": False,
        "final_index_manifest_written": False,
        "retrieval_probe_passed": False,
        "external_call_report": {
            "provider": "Alibaba / DashVector",
            "alibaba_embedding_api_called": False,
            "dashvector_upsert_called": False,
            "dashvector_query_called": False,
            "key_printed": False,
            "key_written": False,
            "vector_values_written": False,
        },
    }

    if mode == "check":
        if _run_delta_planner(report) is None:
            _write_gate_report(report)
            return report
        if not _run_delta_dry_run(report, batch_size):
            _write_gate_report(report)
            return report
        report["status"] = "sync_required" if change_result["sync_required"] else "passed_no_sync_required"
        report.update(_read_batch_progress_fields())
        _write_gate_report(report)
        return report

    if not change_result["sync_required"]:
        report["status"] = "skipped_no_sync_required"
        _write_gate_report(report)
        return report

    pipeline = [
        ["python3", "scripts/rag_build_source_inventory.py"],
        ["python3", "scripts/rag_chunk_project_sources.py"],
        ["python3", "scripts/rag_vector_delta_planner.py"],
    ]
    if full_sync_explicit:
        pipeline.append(["python3", "scripts/rag_dashvector_sync.py", "--batch-size", str(batch_size), "--full-sync-explicit"])
        pipeline.extend(
            [
                ["python3", "scripts/rag_retrieval_probe.py"],
                ["python3", "scripts/rag_index_manifest_validator.py"],
                ["python3", "scripts/rag_index_manifest_validator.py", "--check-current-worktree"],
            ]
        )
    elif real_delta_sync:
        pipeline.append(
            [
                "python3",
                "scripts/rag_dashvector_sync.py",
                "--batch-size",
                str(batch_size),
                "--delta-manifest",
                "codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
            ]
        )
        pipeline.extend(
            [
                ["python3", "scripts/rag_retrieval_probe.py", "--dry-run-active-filter"],
                ["python3", "scripts/rag_index_manifest_validator.py"],
                ["python3", "scripts/rag_index_manifest_validator.py", "--check-current-worktree"],
            ]
        )
    else:
        pipeline.append(
            [
                "python3",
                "scripts/rag_dashvector_sync.py",
                "--dry-run-delta",
                "--delta-manifest",
                "codex_log/rag_vector_sync/latest_chunk_delta_manifest.json",
            ]
        )
    for command in pipeline:
        result = _run_command(command)
        report["commands"].append(result)
        if not result["passed"]:
            report["status"] = "blocked"
            report["blocked_reasons"].append(f"command_failed:{result['command']}")
            report.update(_read_batch_progress_fields())
            _write_gate_report(report)
            return report

    delta_path = common.OUT_DIR / "latest_chunk_delta_manifest.json"
    if delta_path.exists():
        report["delta_counts"] = common.read_json(delta_path).get("chunk_delta_counts", {})
    report.update(_read_batch_progress_fields())
    if not real_delta_sync and not full_sync_explicit:
        counts = _read_manifest_counts()
        report.update(counts)
        report["status"] = "ready_for_controlled_real_delta_sync_pending_user_or_existing_gate_authorization"
        report.update(_read_batch_progress_fields())
        _write_gate_report(report)
        return report

    counts = _read_manifest_counts()
    report.update(counts)
    report.update(_read_batch_progress_fields())
    report["status"] = "passed"
    report["external_call_report"].update(
        {
            "alibaba_embedding_api_called": True,
            "dashvector_upsert_called": True,
            "dashvector_query_called": bool(full_sync_explicit or real_delta_sync),
        }
    )
    _write_gate_report(report)
    return report


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Post-commit DashVector sync gate.")
    parser.add_argument("--mode", choices=("check", "sync", "finish"), required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--real-delta-sync", action="store_true", help="Allow controlled real delta embedding/upsert after dry-run validation.")
    parser.add_argument("--full-sync-explicit", action="store_true", help="Explicitly allow legacy full sync.")
    args = parser.parse_args()
    mode = "sync" if args.mode == "finish" else args.mode
    report = run_sync_pipeline(
        mode,
        max(1, args.batch_size),
        real_delta_sync=args.real_delta_sync,
        full_sync_explicit=args.full_sync_explicit,
    )
    print(
        json.dumps(
            {
                "status": report["status"],
                "mode": args.mode,
                "sync_required": report["indexable_change_result"]["sync_required"],
                "source_commit_sha": report["indexable_change_result"]["source_commit_sha"],
                "previous_index_commit_sha": report["indexable_change_result"]["previous_index_commit_sha"],
                "indexed_file_count": report.get("indexed_file_count"),
                "indexed_chunk_count": report.get("indexed_chunk_count"),
                "delta_counts": report.get("delta_counts", {}),
                "batch_sync_enabled": report.get("batch_sync_enabled", False),
                "batch_count": report.get("batch_count", 0),
                "completed_batch_count": report.get("completed_batch_count", 0),
                "failed_batch_count": report.get("failed_batch_count", 0),
                "pending_batch_count": report.get("pending_batch_count", 0),
                "completed_chunk_count": report.get("completed_chunk_count", 0),
                "resume_available": report.get("resume_available", False),
                "timeout_stage": report.get("timeout_stage"),
                "maintenance_action_id": report.get("maintenance_action_id"),
                "maintenance_decision_path": report.get("maintenance_decision_path"),
                "maintenance_router_refresh_status": report.get("maintenance_router_refresh_status"),
                "maintenance_repair_layer": report.get("maintenance_repair_layer"),
                "maintenance_next_script_to_run": report.get("maintenance_next_script_to_run"),
                "blocked_reasons": report.get("blocked_reasons", []),
                "gate_report_path": GATE_REPORT_JSON.as_posix(),
                "key_printed": False,
                "key_written": False,
                "vector_values_written": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if report["status"] in {"passed", "sync_required", "passed_no_sync_required", "skipped_no_sync_required", "ready_for_controlled_real_delta_sync_pending_user_or_existing_gate_authorization"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
