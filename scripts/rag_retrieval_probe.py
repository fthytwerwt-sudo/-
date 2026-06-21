#!/usr/bin/env python3
"""Run fixed DashVector retrieval probes and verify source readback."""

from __future__ import annotations

import argparse
import json
from typing import Any

import rag_common as common


QUERIES = [
    "RAG 默认判断链是什么",
    "Chroma 是否仍然使用",
    "DashVector 在当前项目中的角色是什么",
    "Codex 执行前如何获得资料包",
    "失败后应该回到哪一层",
    "本轮向量索引同步到了哪个 commit",
]


ACTIVE_FILTER_REPORT_JSON = common.OUT_DIR / "latest_retrieval_probe_active_filter_report.json"
ACTIVE_FILTER_REPORT_MD = common.OUT_DIR / "latest_retrieval_probe_active_filter_report.md"


def validate_doc(
    doc: dict[str, Any],
    manifest_by_chunk: dict[str, Any],
    active_manifest_by_chunk: dict[str, Any] | None = None,
) -> dict[str, Any]:
    fields = doc.get("fields", {})
    source_path = fields.get("source_path", "")
    chunk_id = fields.get("chunk_id", "")
    line_range = fields.get("line_range", "")
    result: dict[str, Any] = {
        "source_path": source_path,
        "line_range": line_range,
        "chunk_id": chunk_id,
        "score": doc.get("score"),
        "metadata_complete": bool(source_path and line_range and chunk_id),
        "readback_hash_match": False,
        "stale_index_check": False,
        "active_manifest_allowlist_passed": False,
    }
    if not result["metadata_complete"] or chunk_id not in manifest_by_chunk:
        result["blocked_reason"] = "source_path_line_range_or_chunk_id_missing"
        return result
    if active_manifest_by_chunk is not None and chunk_id not in active_manifest_by_chunk:
        result["blocked_reason"] = "chunk_not_in_active_manifest_allowlist"
        return result
    readback = common.readback_for_chunk(manifest_by_chunk[chunk_id])
    result.update(
        {
            "readback": readback["readback"],
            "readback_hash_match": readback["readback_hash_match"],
            "file_hash_match": readback["file_hash_match"],
            "stale_index_check": readback["readback_hash_match"] and readback["file_hash_match"],
            "active_manifest_allowlist_passed": active_manifest_by_chunk is None or chunk_id in active_manifest_by_chunk,
        }
    )
    return result


def run_active_filter_dry_run() -> dict[str, Any]:
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    chunk_manifest = common.read_json(common.CHUNK_MANIFEST_PATH)
    index_ids = set(common.load_chunk_by_id(index_manifest))
    active_ids = set(common.load_chunk_by_id(chunk_manifest))
    reused_or_active = len(index_ids & active_ids)
    rejected_stale = len(index_ids - active_ids)
    report = {
        "project_route": common.PROJECT_ROUTE,
        "generated_at": common.now_iso(),
        "source_commit_sha": chunk_manifest.get("commit_sha"),
        "old_problem": "commit_only_filter_not_enough_for_delta_reuse",
        "new_policy": [
            "query_by_project_route_and_repo",
            "post_filter_by_active_manifest_allowlist",
            "verify_chunk_hash_and_file_hash_by_readback",
            "reject_stale_or_superseded_docs",
        ],
        "active_manifest_chunk_count": len(active_ids),
        "indexed_manifest_chunk_count": len(index_ids),
        "indexed_chunks_still_active": reused_or_active,
        "indexed_chunks_rejected_by_active_manifest": rejected_stale,
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_query_called": False,
            "dashvector_upsert_called": False,
        },
        "status": "passed",
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    common.write_json(ACTIVE_FILTER_REPORT_JSON, report)
    common.write_markdown(
        ACTIVE_FILTER_REPORT_MD,
        [
            "# RAG Retrieval Probe Active Manifest Filter Dry Run",
            "",
            "- status: `passed`",
            f"- active_manifest_chunk_count: `{report['active_manifest_chunk_count']}`",
            f"- indexed_manifest_chunk_count: `{report['indexed_manifest_chunk_count']}`",
            f"- indexed_chunks_still_active: `{report['indexed_chunks_still_active']}`",
            f"- indexed_chunks_rejected_by_active_manifest: `{report['indexed_chunks_rejected_by_active_manifest']}`",
            "- alibaba_embedding_api_called: `false`",
            "- dashvector_query_called: `false`",
            "- dashvector_upsert_called: `false`",
        ],
    )
    return report


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Run fixed DashVector retrieval probes and verify source readback.")
    parser.add_argument("--dry-run-active-filter", action="store_true", help="Validate active manifest post-filter without external API.")
    args = parser.parse_args()
    if args.dry_run_active_filter:
        report = run_active_filter_dry_run()
        print(json.dumps({"status": report["status"], "active_filter_report_path": ACTIVE_FILTER_REPORT_JSON.as_posix(), "dashvector_query_called": False}, ensure_ascii=False, sort_keys=True))
        return 0

    if not common.INDEX_MANIFEST_PATH.exists():
        raise SystemExit("blocked_index_manifest_missing")
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    if index_manifest.get("blocked"):
        raise SystemExit("blocked_index_manifest_not_ready")
    manifest_by_chunk = common.load_chunk_by_id(index_manifest)
    active_manifest = common.read_json(common.CHUNK_MANIFEST_PATH)
    active_manifest_by_chunk = common.load_chunk_by_id(active_manifest)
    query_vectors = common.embed_texts(QUERIES)
    if len(query_vectors) != len(QUERIES):
        raise RuntimeError("blocked_query_embedding_vector_count_mismatch")
    source_commit_sha = index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha")
    filter_expression = 'project_route = "video_factory"'
    query_reports: list[dict[str, Any]] = []
    all_passed = True
    for query, vector in zip(QUERIES, query_vectors):
        raw = common.query_dashvector(vector, topk=8, filter_expression=filter_expression)
        docs = [validate_doc(doc, manifest_by_chunk, active_manifest_by_chunk) for doc in raw.get("docs", [])]
        top_docs = docs[:3]
        query_passed = bool(top_docs) and all(
            item["metadata_complete"] and item["readback_hash_match"] and item["stale_index_check"]
            and item["active_manifest_allowlist_passed"]
            for item in top_docs
        )
        all_passed = all_passed and query_passed
        query_reports.append(
            {
                "query": query,
                "query_success": raw.get("success") is True,
                "top_k_results": top_docs,
                "source_readback_passed": query_passed,
            }
        )
    report = {
        "project_route": common.PROJECT_ROUTE,
        "generated_at": common.now_iso(),
        "source_commit_sha": source_commit_sha,
        "filter_expression": filter_expression,
        "active_manifest_post_filter": True,
        "queries_tested": QUERIES,
        "query_reports": query_reports,
        "source_readback_passed": all_passed,
        "stale_index_check": all_passed,
        "page_content_only": False,
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
        "status": "passed" if all_passed else "blocked",
    }
    common.write_json(common.RETRIEVAL_REPORT_JSON_PATH, report)
    lines = [
        "# RAG Retrieval Probe Report",
        "",
        f"- status: `{report['status']}`",
        f"- source_commit_sha: `{report['source_commit_sha']}`",
        f"- source_readback_passed: `{str(report['source_readback_passed']).lower()}`",
        f"- stale_index_check: `{str(report['stale_index_check']).lower()}`",
        "- page_content_only: `false`",
        "",
        "## Queries",
        "",
    ]
    for item in query_reports:
        lines.append(f"- `{item['query']}`: `{'passed' if item['source_readback_passed'] else 'blocked'}`")
    common.write_markdown(common.RETRIEVAL_REPORT_MD_PATH, lines)
    print(json.dumps({"status": report["status"], "queries_tested": len(QUERIES)}, ensure_ascii=False, sort_keys=True))
    return 0 if all_passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
