#!/usr/bin/env python3
"""Build RAG supply packs from retrieval results and source readback."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any

import rag_common as common


ENGINEERING_OUT_DIR = common.ROOT / "codex_log" / "rag_engineering_line"


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [str(value)]


def _lower_words(value: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[\w\u4e00-\u9fff]+", value)}


def _load_index_manifest() -> dict[str, Any]:
    if not common.INDEX_MANIFEST_PATH.exists():
        raise SystemExit("blocked_index_manifest_missing")
    return common.read_json(common.INDEX_MANIFEST_PATH)


def _select_candidate_chunks(
    index_manifest: dict[str, Any],
    retrieval_goal: str,
    preferred_sources: list[str],
    limit: int = 3,
) -> list[dict[str, Any]]:
    chunks = index_manifest.get("chunks", [])
    if not chunks:
        raise RuntimeError("blocked_no_indexed_chunk_for_supply_pack")

    preferred_set = set(preferred_sources)
    goal_words = _lower_words(retrieval_goal)
    scored: list[tuple[int, int, dict[str, Any]]] = []
    for position, chunk in enumerate(chunks):
        source_path = str(chunk.get("source_path", ""))
        source_words = _lower_words(source_path)
        score = len(goal_words & source_words)
        if source_path in preferred_set:
            score += 100
        if any(source_path.startswith(prefix.rstrip("*")) for prefix in preferred_sources if prefix.endswith("*")):
            score += 50
        if score > 0:
            scored.append((score, -position, chunk))

    if not scored:
        scored = [(0, -position, chunk) for position, chunk in enumerate(chunks[:limit])]
    scored.sort(reverse=True)
    return [chunk for _score, _position, chunk in scored[:limit]]


def _exact_snippet_pack(chunks: list[dict[str, Any]], why_needed: str) -> list[dict[str, Any]]:
    snippets: list[dict[str, Any]] = []
    for chunk in chunks:
        readback = common.readback_for_chunk(chunk)
        snippets.append(
            {
                "source_path": readback["source_path"],
                "line_range": readback["line_range"],
                "chunk_id": readback["chunk_id"],
                "readback": readback["readback"],
                "snippet": readback["readback"],
                "readback_hash_match": readback["readback_hash_match"],
                "file_hash_match": readback["file_hash_match"],
                "why_needed": why_needed,
            }
        )
    return snippets


def build_pre_supply_pack(task_request: dict[str, Any], index_manifest: dict[str, Any]) -> dict[str, Any]:
    task_id = str(task_request.get("task_id") or "rag-engineering-line-task")
    task_type = task_request.get("task_type") or "engineering_line_landing"
    retrieval_goal = str(task_request.get("retrieval_goal") or "RAG engineering line supply pack")
    why_needed = str(
        task_request.get("why_needed")
        or "Codex 写入前必须拿到关键原文片段、任务约束和冲突点。"
    )
    preferred_sources = _as_list(task_request.get("preferred_source_paths"))
    chunks = _select_candidate_chunks(index_manifest, retrieval_goal, preferred_sources)
    snippets = _exact_snippet_pack(chunks, why_needed)
    first = snippets[0]
    conflict_points = _as_list(task_request.get("conflict_points"))
    if not conflict_points and bool(task_request.get("high_risk", False)):
        conflict_points = ["high_risk_task_requires_explicit_conflict_review"]
    return {
        "pack_type": "pre_supply_pack",
        "task_id": task_id,
        "task_type": task_type,
        "retrieval_goal": retrieval_goal,
        "exact_snippet_pack": snippets,
        "source_path": first["source_path"],
        "line_range": first["line_range"],
        "chunk_id": first["chunk_id"],
        "why_needed": why_needed,
        "execution_constraint": _as_list(task_request.get("execution_constraint"))
        or [
            "source_readback_required",
            "vector_result_is_not_formal_fact",
            "do_not_promote_content_validation_or_send_ready",
        ],
        "conflict_points": conflict_points,
        "blocked_if": _as_list(task_request.get("blocked_if"))
        or [
            "source_path_missing",
            "line_range_missing",
            "chunk_id_missing",
            "readback_missing",
            "stale_index_detected",
        ],
        "source_commit_sha": index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha"),
        "generated_at": common.now_iso(),
    }


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
    parser = argparse.ArgumentParser(description="Build RAG supply packs with source readback.")
    parser.add_argument("--task-request", help="JSON task request for a pre_supply_pack.")
    parser.add_argument("--out", help="Output path for --task-request mode.")
    args = parser.parse_args()

    index_manifest = _load_index_manifest()
    if args.task_request or args.out:
        if not args.task_request or not args.out:
            raise SystemExit("blocked_task_request_and_out_required_together")
        task_request_path = pathlib.Path(args.task_request)
        out_path = pathlib.Path(args.out)
        if not task_request_path.is_absolute():
            task_request_path = common.ROOT / task_request_path
        if not out_path.is_absolute():
            out_path = common.ROOT / out_path
        task_request = common.read_json(task_request_path)
        pack = build_pre_supply_pack(task_request, index_manifest)
        common.write_json(out_path, pack)
        print(json.dumps({"status": "passed", "pre_supply_pack_path": out_path.as_posix()}, ensure_ascii=False, sort_keys=True))
        return 0

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
