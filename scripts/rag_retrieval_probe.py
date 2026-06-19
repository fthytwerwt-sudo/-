#!/usr/bin/env python3
"""Run fixed DashVector retrieval probes and verify source readback."""

from __future__ import annotations

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


def validate_doc(doc: dict[str, Any], manifest_by_chunk: dict[str, Any]) -> dict[str, Any]:
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
    }
    if not result["metadata_complete"] or chunk_id not in manifest_by_chunk:
        result["blocked_reason"] = "source_path_line_range_or_chunk_id_missing"
        return result
    readback = common.readback_for_chunk(manifest_by_chunk[chunk_id])
    result.update(
        {
            "readback": readback["readback"],
            "readback_hash_match": readback["readback_hash_match"],
            "file_hash_match": readback["file_hash_match"],
            "stale_index_check": readback["readback_hash_match"] and readback["file_hash_match"],
        }
    )
    return result


def main() -> int:
    common.main_guard()
    if not common.INDEX_MANIFEST_PATH.exists():
        raise SystemExit("blocked_index_manifest_missing")
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    if index_manifest.get("blocked"):
        raise SystemExit("blocked_index_manifest_not_ready")
    manifest_by_chunk = common.load_chunk_by_id(index_manifest)
    query_vectors = common.embed_texts(QUERIES)
    if len(query_vectors) != len(QUERIES):
        raise RuntimeError("blocked_query_embedding_vector_count_mismatch")
    source_commit_sha = index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha")
    filter_expression = f'project_route = "video_factory" and commit_sha = "{source_commit_sha}"'
    query_reports: list[dict[str, Any]] = []
    all_passed = True
    for query, vector in zip(QUERIES, query_vectors):
        raw = common.query_dashvector(vector, topk=8, filter_expression=filter_expression)
        docs = [validate_doc(doc, manifest_by_chunk) for doc in raw.get("docs", [])]
        top_docs = docs[:3]
        query_passed = bool(top_docs) and all(
            item["metadata_complete"] and item["readback_hash_match"] and item["stale_index_check"]
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
