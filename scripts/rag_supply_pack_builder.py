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
DECISION_DIR = common.ROOT / "codex_log" / "rag_decision_engine"
DECISION_AUDIT_REPORT_PATH = DECISION_DIR / "latest_decision_audit_report.json"


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


def load_decision_context() -> dict[str, Any]:
    if not DECISION_AUDIT_REPORT_PATH.exists():
        return {
            "decision_audit_report_id": None,
            "hard_gate_result": {"status": "not_available", "failed_gates": []},
            "selected_action": None,
            "can_feed_codex": True,
            "can_claim_completed": False,
            "conflict_group_id": None,
        }
    report = common.read_json(DECISION_AUDIT_REPORT_PATH)
    audit = report.get("decision_audit_report", {})
    hard_gate = audit.get("hard_gate_result", {"status": "missing", "failed_gates": ["hard_gate_result_missing"]})
    return {
        "decision_audit_report_id": report.get("decision_audit_report_id"),
        "hard_gate_result": hard_gate,
        "selected_action": audit.get("selected_action"),
        "can_feed_codex": hard_gate.get("status") == "passed",
        "can_claim_completed": False,
        "conflict_group_id": "rag_decision_engine_round_2",
    }


def apply_decision_context(pack: dict[str, Any]) -> dict[str, Any]:
    context = load_decision_context()
    pack.update(context)
    blocked_if = _as_list(pack.get("blocked_if"))
    for reason in ("hard_gate_failed", "conflict_pending_required_fact", "high_risk_stale_source_without_readback"):
        if reason not in blocked_if:
            blocked_if.append(reason)
    pack["blocked_if"] = blocked_if
    return pack


def _classify_source_for_cleaning(source_path: str) -> dict[str, Any]:
    """Attach conservative cleaning metadata to a readback source."""
    normalized = source_path.replace("\\", "/")
    lower = normalized.lower()

    authority_level = "rag_retrieval_result"
    source_priority_rank = 4
    status_label = "readback_supported"
    stale_status = "current"
    can_feed_codex = True

    if any(marker in normalized for marker in ("归档", "归档删除区", "archive", "old_context")):
        authority_level = "historical_archive"
        source_priority_rank = 6
        status_label = "historical_reference_only"
        stale_status = "historical_reference"
        can_feed_codex = False
    elif normalized.startswith(("GPT数据源/", "codex_source/")) or normalized == "AGENTS.md" or normalized.startswith("scripts/"):
        authority_level = "current_repo_source"
        source_priority_rank = 1
        status_label = "current_repo_readback"
    elif normalized.startswith("review_loop/"):
        authority_level = "real_run_report"
        source_priority_rank = 2
        status_label = "real_run_report"
    elif normalized == "codex_log/latest.md":
        authority_level = "latest_summary"
        source_priority_rank = 3
        status_label = "latest_repo_summary"
    elif normalized.startswith("codex_log/"):
        authority_level = "real_run_report"
        source_priority_rank = 2
        status_label = "repo_run_report"

    if "current_gray_test_target" in lower:
        status_label = "legacy_compatibility_pointer"
        stale_status = "legacy_demoted"
        can_feed_codex = False

    return {
        "authority_level": authority_level,
        "source_priority_rank": source_priority_rank,
        "status_label": status_label,
        "stale_status": stale_status,
        "conflict_status": "none",
        "readback_required": True,
        "can_feed_codex": can_feed_codex,
        "can_claim_completed": False,
    }


def _snippet_from_readback(readback: dict[str, Any], why_needed: str | None = None) -> dict[str, Any]:
    snippet = {
        "source_path": readback["source_path"],
        "line_range": readback["line_range"],
        "chunk_id": readback["chunk_id"],
        "readback": readback["readback"],
        "snippet": readback["readback"],
        "readback_hash_match": readback["readback_hash_match"],
        "file_hash_match": readback.get("file_hash_match", True),
    }
    if why_needed:
        snippet["why_needed"] = why_needed
    snippet.update(_classify_source_for_cleaning(readback["source_path"]))
    return snippet


def _aggregate_cleaning_layer_check(snippets: list[dict[str, Any]]) -> dict[str, Any]:
    if not snippets:
        return {
            "authority_level": "unknown",
            "stale_status": "unknown",
            "conflict_status": "unknown",
            "readback_required": True,
            "can_feed_codex": False,
            "can_claim_completed": False,
            "status": "blocked",
        }
    return {
        "authority_level": snippets[0].get("authority_level"),
        "stale_status": "current" if all(item.get("stale_status") == "current" for item in snippets) else "mixed_or_stale",
        "conflict_status": "none" if all(item.get("conflict_status") == "none" for item in snippets) else "requires_cleaning",
        "readback_required": True,
        "can_feed_codex": all(bool(item.get("can_feed_codex")) for item in snippets),
        "can_claim_completed": False,
        "status": "passed" if all(bool(item.get("can_feed_codex")) for item in snippets) else "blocked",
    }


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
        snippets.append(_snippet_from_readback(readback, why_needed))
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
    pack = {
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
        "cleaning_layer_check": _aggregate_cleaning_layer_check(snippets),
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
    return apply_decision_context(pack)


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
    exact_snippet_pack = [_snippet_from_readback(readback)]
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
        "cleaning_layer_check": _aggregate_cleaning_layer_check(exact_snippet_pack),
        "blocked_if": ["source_path_missing", "line_range_missing", "readback_failed", "stale_index_detected"],
    }
    pre = apply_decision_context(pre)
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
    mid = apply_decision_context(mid)
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
    post = apply_decision_context(post)
    small_probe = {
        "task_id": "rag-vector-sync-20260620",
        "can_execute": bool(readback["readback_hash_match"]) and not index_manifest.get("blocked", True),
        "missing_context": [],
        "conflict_points": [],
        "blocked_if": ["readback_failed", "index_manifest_blocked"],
    }
    small_probe = apply_decision_context(small_probe)
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
