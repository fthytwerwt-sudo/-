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


def run_sync_pipeline(mode: str, batch_size: int) -> dict[str, Any]:
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
        report["status"] = "sync_required" if change_result["sync_required"] else "passed_no_sync_required"
        _write_gate_report(report)
        return report

    if not change_result["sync_required"]:
        report["status"] = "skipped_no_sync_required"
        _write_gate_report(report)
        return report

    pipeline = [
        ["python3", "scripts/rag_build_source_inventory.py"],
        ["python3", "scripts/rag_chunk_project_sources.py"],
        ["python3", "scripts/rag_dashvector_sync.py", "--batch-size", str(batch_size)],
        ["python3", "scripts/rag_retrieval_probe.py"],
        ["python3", "scripts/rag_index_manifest_validator.py"],
        ["python3", "scripts/rag_index_manifest_validator.py", "--check-current-worktree"],
    ]
    for command in pipeline:
        result = _run_command(command)
        report["commands"].append(result)
        if not result["passed"]:
            report["status"] = "blocked"
            report["blocked_reasons"].append(f"command_failed:{result['command']}")
            _write_gate_report(report)
            return report

    counts = _read_manifest_counts()
    report.update(counts)
    report["status"] = "passed"
    report["external_call_report"].update(
        {
            "alibaba_embedding_api_called": True,
            "dashvector_upsert_called": True,
            "dashvector_query_called": True,
        }
    )
    _write_gate_report(report)
    return report


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Post-commit DashVector sync gate.")
    parser.add_argument("--mode", choices=("check", "sync", "finish"), required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    args = parser.parse_args()
    mode = "sync" if args.mode == "finish" else args.mode
    report = run_sync_pipeline(mode, max(1, args.batch_size))
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
    return 0 if report["status"] in {"passed", "sync_required", "passed_no_sync_required", "skipped_no_sync_required"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
