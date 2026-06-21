#!/usr/bin/env python3
"""Build a dry-run cleanup plan for stale DashVector retrieval docs.

This script never deletes or tombstones DashVector documents. It only turns
retrieval evidence into an auditable plan so a later authorized run can decide
whether cleanup is safe.
"""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


CLEANUP_PLAN_JSON = common.OUT_DIR / "latest_retrieval_stale_doc_cleanup_plan.json"
CLEANUP_PLAN_MD = common.OUT_DIR / "latest_retrieval_stale_doc_cleanup_plan.md"


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _candidate_value(candidate: dict[str, Any], key: str, default: Any = "") -> Any:
    if key in candidate:
        return candidate.get(key, default)
    fields = candidate.get("fields")
    if isinstance(fields, dict):
        return fields.get(key, default)
    return default


def normalize_stale_doc(candidate: dict[str, Any], *, allow_delete: bool = False) -> dict[str, Any]:
    active_passed = bool(candidate.get("active_manifest_allowlist_passed"))
    readback_match = bool(candidate.get("readback_hash_match"))
    file_hash_match = bool(candidate.get("file_hash_match"))
    reason = (
        candidate.get("blocked_reason")
        or candidate.get("reason")
        or ("chunk_not_in_active_manifest_allowlist" if not active_passed else "readback_or_file_hash_mismatch")
    )
    safe_to_delete_candidate = (not active_passed) or (not readback_match) or (not file_hash_match)
    return {
        "stale_doc_id": candidate.get("id") or _candidate_value(candidate, "chunk_id") or candidate.get("chunk_id", ""),
        "chunk_id": _candidate_value(candidate, "chunk_id"),
        "source_path": _candidate_value(candidate, "source_path"),
        "line_range": _candidate_value(candidate, "line_range"),
        "first_seen_query": candidate.get("first_seen_query") or candidate.get("query") or "",
        "raw_rank": candidate.get("raw_rank"),
        "score": candidate.get("score"),
        "reason": reason,
        "active_manifest_allowlist_passed": active_passed,
        "readback_hash_match": readback_match,
        "file_hash_match": file_hash_match,
        "safe_to_delete_candidate": safe_to_delete_candidate,
        "delete_allowed": bool(allow_delete),
        "delete_executed": False,
        "tombstone_executed": False,
    }


def extract_stale_docs_from_retrieval_report(report: dict[str, Any]) -> list[dict[str, Any]]:
    stale_docs: list[dict[str, Any]] = []
    for candidate in report.get("stale_or_inactive_docs", []):
        if isinstance(candidate, dict):
            stale_docs.append(candidate)
    for query_report in report.get("query_reports", []):
        query = query_report.get("query", "")
        for list_key in ("stale_or_inactive_docs", "raw_top_k_results", "top_k_results"):
            for rank, candidate in enumerate(query_report.get(list_key, []) or [], start=1):
                if not isinstance(candidate, dict):
                    continue
                is_stale = (
                    candidate.get("blocked_reason")
                    or candidate.get("active_manifest_allowlist_passed") is False
                    or candidate.get("readback_hash_match") is False
                    or candidate.get("file_hash_match") is False
                )
                if not is_stale:
                    continue
                enriched = dict(candidate)
                enriched.setdefault("first_seen_query", query)
                enriched.setdefault("raw_rank", candidate.get("raw_rank") or rank)
                stale_docs.append(enriched)
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, Any]] = []
    for candidate in stale_docs:
        key = (
            str(_candidate_value(candidate, "chunk_id")),
            str(candidate.get("first_seen_query") or candidate.get("query") or ""),
            str(candidate.get("raw_rank") or ""),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate)
    return unique


def build_cleanup_plan(
    stale_docs: list[dict[str, Any]],
    *,
    source_commit_sha: str = "",
    retrieval_report_path: str = "",
    allow_delete: bool = False,
    allow_tombstone: bool = False,
) -> dict[str, Any]:
    entries = [normalize_stale_doc(candidate, allow_delete=allow_delete) for candidate in stale_docs]
    return {
        "manifest_type": "rag_retrieval_stale_doc_cleanup_plan",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "generated_at": common.now_iso(),
        "source_commit_sha": source_commit_sha,
        "retrieval_report_path": retrieval_report_path,
        "cleanup_mode": "dry_run_only",
        "stale_doc_count": len(entries),
        "stale_docs": entries,
        "delete_allowed": bool(allow_delete),
        "tombstone_allowed": bool(allow_tombstone),
        "dashvector_delete_called": False,
        "dashvector_tombstone_called": False,
        "physical_delete_executed": False,
        "tombstone_executed": False,
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_query_called": False,
            "dashvector_upsert_called": False,
            "dashvector_delete_called": False,
        },
        "status": "passed_dry_run" if entries else "passed_no_stale_docs_detected",
        "blocked_if": ["delete_requested_without_explicit_authorization", "stale_doc_missing_chunk_id"],
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }


def write_cleanup_plan(plan: dict[str, Any], json_path: pathlib.Path = CLEANUP_PLAN_JSON, md_path: pathlib.Path = CLEANUP_PLAN_MD) -> None:
    common.write_json(json_path, plan)
    lines = [
        "# Retrieval Stale Doc Cleanup Plan",
        "",
        f"- status: `{plan['status']}`",
        f"- cleanup_mode: `{plan['cleanup_mode']}`",
        f"- stale_doc_count: `{plan['stale_doc_count']}`",
        f"- delete_allowed: `{str(plan['delete_allowed']).lower()}`",
        f"- tombstone_allowed: `{str(plan['tombstone_allowed']).lower()}`",
        "- dashvector_delete_called: `false`",
        "- dashvector_tombstone_called: `false`",
        "- physical_delete_executed: `false`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "",
        "## Candidates",
        "",
    ]
    for item in plan["stale_docs"][:80]:
        lines.append(
            f"- `{item['chunk_id']}` `{item['source_path']}:{item['line_range']}` "
            f"rank=`{item.get('raw_rank')}` reason=`{item['reason']}` safe_to_delete_candidate=`{str(item['safe_to_delete_candidate']).lower()}`"
        )
    common.write_markdown(md_path, lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Build a dry-run stale DashVector doc cleanup plan.")
    parser.add_argument("--from-retrieval-report", default=str(common.RETRIEVAL_REPORT_JSON_PATH))
    parser.add_argument("--out", default=str(CLEANUP_PLAN_JSON))
    parser.add_argument("--md-out", default=str(CLEANUP_PLAN_MD))
    parser.add_argument("--allow-delete", action="store_true")
    parser.add_argument("--allow-tombstone", action="store_true")
    args = parser.parse_args()

    report_path = _resolve(args.from_retrieval_report)
    report = common.read_json(report_path) if report_path.exists() else {}
    stale_docs = extract_stale_docs_from_retrieval_report(report)
    plan = build_cleanup_plan(
        stale_docs,
        source_commit_sha=str(report.get("source_commit_sha") or ""),
        retrieval_report_path=report_path.as_posix(),
        allow_delete=args.allow_delete,
        allow_tombstone=args.allow_tombstone,
    )
    write_cleanup_plan(plan, _resolve(args.out), _resolve(args.md_out))
    print(
        json.dumps(
            {
                "status": plan["status"],
                "cleanup_plan_path": _resolve(args.out).as_posix(),
                "stale_doc_count": plan["stale_doc_count"],
                "dashvector_delete_called": False,
                "dashvector_tombstone_called": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
