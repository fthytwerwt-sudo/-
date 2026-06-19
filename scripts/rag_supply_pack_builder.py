#!/usr/bin/env python3
"""Build RAG pre/mid/post supply packs from retrieval results and readback."""

from __future__ import annotations

import argparse
import json
from typing import Any

import rag_common as common


def first_valid_probe_result(retrieval_report: dict[str, Any], index_manifest: dict[str, Any]) -> dict[str, Any]:
    manifest_by_chunk = common.load_chunk_by_id(index_manifest)
    for query_report in retrieval_report.get("query_reports", []):
        for result in query_report.get("top_k_results", []):
            chunk_id = result.get("chunk_id")
            if chunk_id in manifest_by_chunk:
                readback = common.readback_for_chunk(manifest_by_chunk[chunk_id])
                return {
                    "query": query_report["query"],
                    "chunk": manifest_by_chunk[chunk_id],
                    "readback": readback,
                }
    if index_manifest.get("chunks"):
        chunk = index_manifest["chunks"][0]
        readback = common.readback_for_chunk(chunk)
        return {"query": "fallback_first_indexed_chunk", "chunk": chunk, "readback": readback}
    raise RuntimeError("blocked_no_indexed_chunk_for_supply_pack")


def build_packs(seed: dict[str, Any], index_manifest: dict[str, Any]) -> dict[str, Any]:
    chunk = seed["chunk"]
    readback = seed["readback"]
    exact_snippet_pack = [
        {
            "source_path": readback["source_path"],
            "line_range": readback["line_range"],
            "chunk_id": readback["chunk_id"],
            "snippet": readback["readback"],
            "readback_hash_match": readback["readback_hash_match"],
        }
    ]
    pre = {
        "task_id": "rag-vector-sync-20260620",
        "task_type": "mechanism_repair_and_vector_ingestion",
        "retrieval_goal": seed["query"],
        "exact_snippet_pack": exact_snippet_pack,
        "source_path": readback["source_path"],
        "line_range": readback["line_range"],
        "chunk_id": readback["chunk_id"],
        "why_needed": "Codex 开工前必须拿到关键原文片段、任务约束和冲突点。",
        "execution_constraint": [
            "vector_result_is_not_formal_fact",
            "source_readback_required",
            "do_not_promote_content_validation_or_send_ready",
        ],
        "conflict_points": [],
        "blocked_if": ["source_path_missing", "line_range_missing", "readback_failed", "stale_index_detected"],
    }
    mid = {
        "child_task_id": "rag-sync-guard-check",
        "files_already_read": [readback["source_path"]],
        "will_modify_files": [],
        "missing_context": [],
        "validation_failure_logs": [],
        "conflict_points": [],
        "incremental_snippets": exact_snippet_pack,
        "action_constraint": ["continue_only_if_readback_hash_match"],
        "continue_allowed": bool(readback["readback_hash_match"]),
    }
    post = {
        "task_id": "rag-vector-sync-20260620",
        "completion_truth_check": {
            "source_commit_sha": index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha"),
            "indexed_chunk_count": index_manifest.get("indexed_chunk_count"),
            "content_validation": "not_promoted",
            "send_ready": False,
            "production_readiness": "not_promoted",
        },
        "exact_snippet_pack": exact_snippet_pack,
        "risk_points": [],
        "completion_allowed": bool(readback["readback_hash_match"]) and not index_manifest.get("blocked", True),
        "blocked_if": ["missing_log", "missing_probe", "stale_index_detected", "status_promotion_attempted"],
    }
    small_probe = {
        "task_id": "rag-vector-sync-20260620",
        "can_execute": bool(readback["readback_hash_match"]) and not index_manifest.get("blocked", True),
        "missing_context": [],
        "conflict_points": [],
        "blocked_if": ["readback_failed", "index_manifest_blocked"],
    }
    return {
        "pre_supply_pack": pre,
        "mid_task_supply_pack": mid,
        "post_risk_review_pack": post,
        "small_probe_run": small_probe,
    }


def write_reports(packs: dict[str, Any]) -> None:
    report = {
        "project_route": common.PROJECT_ROUTE,
        "generated_at": common.now_iso(),
        "status": "passed" if packs["post_risk_review_pack"]["completion_allowed"] else "blocked",
        **packs,
        "retrieval_map_is_not_supply_complete": True,
        "exact_snippet_required": True,
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(common.SUPPLY_REPORT_JSON_PATH, report)
    common.write_json(common.OUT_DIR / "latest_pre_supply_pack.json", packs["pre_supply_pack"])
    common.write_json(common.OUT_DIR / "latest_mid_task_supply_pack.json", packs["mid_task_supply_pack"])
    common.write_json(common.OUT_DIR / "latest_post_risk_review_pack.json", packs["post_risk_review_pack"])
    common.write_json(common.OUT_DIR / "latest_small_probe_run.json", packs["small_probe_run"])
    lines = [
        "# RAG Supply Bus Report",
        "",
        f"- status: `{report['status']}`",
        "- retrieval_map_is_not_supply_complete: `true`",
        "- exact_snippet_required: `true`",
        f"- pre_supply_pack: `{packs['pre_supply_pack']['source_path']}:{packs['pre_supply_pack']['line_range']}`",
        f"- mid_task_continue_allowed: `{str(packs['mid_task_supply_pack']['continue_allowed']).lower()}`",
        f"- post_completion_allowed: `{str(packs['post_risk_review_pack']['completion_allowed']).lower()}`",
        f"- small_probe_can_execute: `{str(packs['small_probe_run']['can_execute']).lower()}`",
    ]
    common.write_markdown(common.SUPPLY_REPORT_MD_PATH, lines)


def main() -> int:
    common.main_guard()
    if not common.INDEX_MANIFEST_PATH.exists():
        raise SystemExit("blocked_index_manifest_missing")
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    retrieval_report = (
        common.read_json(common.RETRIEVAL_REPORT_JSON_PATH)
        if common.RETRIEVAL_REPORT_JSON_PATH.exists()
        else {"query_reports": []}
    )
    seed = first_valid_probe_result(retrieval_report, index_manifest)
    packs = build_packs(seed, index_manifest)
    write_reports(packs)
    status = "passed" if packs["post_risk_review_pack"]["completion_allowed"] else "blocked"
    print(json.dumps({"status": status, "supply_report_path": common.SUPPLY_REPORT_JSON_PATH.as_posix()}, ensure_ascii=False, sort_keys=True))
    return 0 if status == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
