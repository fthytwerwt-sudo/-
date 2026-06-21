#!/usr/bin/env python3
"""Embed allowlisted chunks and upsert them to DashVector.

The script writes manifests and sanitized API results only. It never writes
API keys or vector values.
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import time
import urllib.parse
from typing import Any

import rag_common as common


MAX_EMBED_BATCH_CHARS = 8000
MAX_EMBED_BATCH_ITEMS = 10
MAX_UPSERT_BATCH_CHARS = 12000
DELTA_MANIFEST_PATH = common.OUT_DIR / "latest_chunk_delta_manifest.json"
DELTA_DRY_RUN_REPORT_PATH = common.OUT_DIR / "latest_delta_sync_dry_run_report.json"
DELTA_CHECKPOINT_PATH = common.OUT_DIR / "latest_delta_sync_checkpoint.json"


def precondition_report(chunk_manifest: dict[str, Any]) -> dict[str, Any]:
    inventory = common.read_json(common.SOURCE_INVENTORY_PATH)
    report: dict[str, Any] = {
        "secret_scan_passed": bool(inventory.get("secret_scan_passed")),
        "allowlist_check_passed": bool(inventory.get("allowlist_check_passed")),
        "denylist_check_passed": bool(inventory.get("denylist_check_passed")),
        "chunk_manifest_valid": bool(chunk_manifest.get("chunk_manifest_valid")),
        "dirty_files_not_indexed_to_formal_store": common.has_only_allowed_dirty_paths(),
        "dashvector_collection_resolved": False,
        "alibaba_embedding_auth_available": False,
        "no_key_printed": True,
        "blocked_reasons": [],
    }
    try:
        _key, source_type, variable_name = common.load_dashscope_key()
        report["alibaba_embedding_auth_available"] = True
        report["embedding_key_source_type"] = source_type
        report["embedding_key_variable_name"] = variable_name
    except RuntimeError as exc:
        report["blocked_reasons"].append(str(exc))
    try:
        collection = common.dashvector_collection_check()
        report["dashvector_collection_resolved"] = True
        report["dashvector_collection"] = collection
        if not collection.get("dimension_ok"):
            report["blocked_reasons"].append("blocked_dashvector_dimension_mismatch")
    except RuntimeError as exc:
        report["blocked_reasons"].append(str(exc))
    for key in (
        "secret_scan_passed",
        "allowlist_check_passed",
        "denylist_check_passed",
        "chunk_manifest_valid",
        "dirty_files_not_indexed_to_formal_store",
    ):
        if not report[key]:
            report["blocked_reasons"].append(f"blocked_{key}_false")
    report["preconditions_passed"] = not report["blocked_reasons"]
    return report


def embed_batch_with_retry(batch: list[common.Chunk], *, max_attempts: int = 3) -> list[list[float]]:
    last_error: RuntimeError | None = None
    texts = [chunk.text for chunk in batch]
    if len(batch) > 1 and sum(len(text) for text in texts) > MAX_EMBED_BATCH_CHARS:
        mid = len(batch) // 2
        return embed_batch_with_retry(batch[:mid], max_attempts=max_attempts) + embed_batch_with_retry(
            batch[mid:], max_attempts=max_attempts
        )
    for attempt in range(max_attempts):
        try:
            return common.embed_texts(texts)
        except RuntimeError as exc:
            last_error = exc
            time.sleep(2 + attempt * 3)
    if len(batch) > 1:
        mid = len(batch) // 2
        return embed_batch_with_retry(batch[:mid], max_attempts=max_attempts) + embed_batch_with_retry(
            batch[mid:], max_attempts=max_attempts
        )
    chunk = batch[0]
    raise RuntimeError(f"{last_error}:chunk_id={chunk.chunk_id}:source_path={chunk.source_path}:{chunk.line_range}")


def upsert_docs_with_retry(docs: list[dict[str, Any]], *, max_attempts: int = 3) -> dict[str, Any]:
    last_result: dict[str, Any] | None = None
    for attempt in range(max_attempts):
        result = common.upsert_docs(docs)
        last_result = result
        if result["success"]:
            return result
        time.sleep(2 + attempt * 3)
    if len(docs) > 1:
        mid = len(docs) // 2
        left = upsert_docs_with_retry(docs[:mid], max_attempts=max_attempts)
        right = upsert_docs_with_retry(docs[mid:], max_attempts=max_attempts)
        return {
            "http_status": "split",
            "success": bool(left.get("success")) and bool(right.get("success")),
            "code": 0 if bool(left.get("success")) and bool(right.get("success")) else "split_failed",
            "message_preview": "split_upsert",
            "request_id_present": bool(left.get("request_id_present")) or bool(right.get("request_id_present")),
        }
    return last_result or {"success": False, "http_status": None, "code": "missing_result", "request_id_present": False}


def iter_sync_batches(chunks: list[common.Chunk], batch_size: int) -> list[list[common.Chunk]]:
    batches: list[list[common.Chunk]] = []
    current: list[common.Chunk] = []
    current_chars = 0
    for chunk in chunks:
        chunk_chars = len(chunk.text)
        max_items = min(batch_size, MAX_EMBED_BATCH_ITEMS)
        if current and (len(current) >= max_items or current_chars + chunk_chars > MAX_UPSERT_BATCH_CHARS):
            batches.append(current)
            current = []
            current_chars = 0
        current.append(chunk)
        current_chars += chunk_chars
    if current:
        batches.append(current)
    return batches


def upsert_chunks(chunks: list[common.Chunk], batch_size: int) -> dict[str, Any]:
    started_at = common.now_iso()
    upserted = 0
    batches: list[dict[str, Any]] = []
    offset = 0
    for batch in iter_sync_batches(chunks, batch_size):
        vectors = embed_batch_with_retry(batch)
        if len(vectors) != len(batch):
            raise RuntimeError("blocked_embedding_vector_count_mismatch")
        docs = [
            common.dashvector_doc_from_chunk(chunk, vector)
            for chunk, vector in zip(batch, vectors)
        ]
        result = upsert_docs_with_retry(docs)
        batches.append(
            {
                "batch_index": len(batches),
                "chunk_offset": offset,
                "chunk_count": len(batch),
                "success": result["success"],
                "http_status": result["http_status"],
                "code": result["code"],
                "request_id_present": result["request_id_present"],
            }
        )
        if not result["success"]:
            raise RuntimeError("blocked_dashvector_upsert_failed")
        upserted += len(batch)
        offset += len(batch)
        if len(batches) % 25 == 0:
            print(json.dumps({"sync_progress": {"batches": len(batches), "chunks": upserted}}, ensure_ascii=False), flush=True)
        time.sleep(0.2)
    return {
        "started_at": started_at,
        "finished_at": common.now_iso(),
        "upserted_chunk_count": upserted,
        "batch_count": len(batches),
        "batches": batches,
    }


def write_index_manifest(
    chunk_manifest: dict[str, Any],
    preconditions: dict[str, Any],
    upsert: dict[str, Any] | None,
    *,
    delta_manifest: dict[str, Any] | None = None,
) -> dict[str, Any]:
    collection = (
        preconditions.get("dashvector_collection", {}).get("collection")
        if isinstance(preconditions.get("dashvector_collection"), dict)
        else ""
    )
    indexed_files: dict[str, dict[str, Any]] = {}
    for chunk in chunk_manifest.get("chunks", []):
        entry = indexed_files.setdefault(
            chunk["source_path"],
            {
                "source_path": chunk["source_path"],
                "file_hash": chunk["file_hash"],
                "chunk_count": 0,
                "line_ranges": [],
            },
        )
        entry["chunk_count"] += 1
        entry["line_ranges"].append(chunk["line_range"])

    manifest = {
        "manifest_type": "vector_index_manifest",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "branch": chunk_manifest["branch"],
        "commit_sha": chunk_manifest["commit_sha"],
        "source_commit_sha": chunk_manifest["commit_sha"],
        "generated_at": common.now_iso(),
        "source_inventory_path": common.SOURCE_INVENTORY_PATH.as_posix(),
        "chunk_manifest_path": common.CHUNK_MANIFEST_PATH.as_posix(),
        "embedding_model": common.EMBEDDING_MODEL,
        "embedding_dimension": common.EMBEDDING_DIMENSION,
        "vector_store_provider": common.VECTOR_STORE_PROVIDER,
        "dashvector_collection": collection,
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
        "external_call_report": {
            "provider": "Alibaba / DashVector",
            "call_type": "embedding / upsert",
            "alibaba_embedding_api_called": bool(upsert),
            "dashvector_upsert_called": bool(upsert),
            "key_printed": False,
            "key_written": False,
        },
        "preconditions": preconditions,
        "sync_mode": "delta" if delta_manifest else "full_sync_explicit",
        "delta_manifest_path": DELTA_MANIFEST_PATH.as_posix() if delta_manifest else None,
        "indexed_file_count": len(indexed_files) if upsert else 0,
        "indexed_chunk_count": len(chunk_manifest.get("chunks", [])) if upsert and delta_manifest else int(upsert["upserted_chunk_count"]) if upsert else 0,
        "indexed_files": list(indexed_files.values()) if upsert else [],
        "chunks": chunk_manifest.get("chunks", []) if upsert else [],
        "blocked": upsert is None,
        "blocked_reasons": preconditions.get("blocked_reasons", []) if upsert is None else [],
        "stale_files": [],
        "deleted_files": [],
    }
    common.write_json(common.INDEX_MANIFEST_PATH, manifest)
    return manifest


def _load_delta_manifest(path_value: str) -> dict[str, Any]:
    path = common.ROOT / path_value if not pathlib.Path(path_value).is_absolute() else pathlib.Path(path_value)
    if not path.exists():
        raise SystemExit("blocked_delta_manifest_missing")
    return common.read_json(path)


def _delta_chunk_ids(delta_manifest: dict[str, Any]) -> set[str]:
    return {str(item.get("chunk_id")) for item in delta_manifest.get("chunk_classes", {}).get("delta_chunks", []) if item.get("chunk_id")}


def _chunks_from_delta_manifest(chunk_manifest: dict[str, Any], delta_manifest: dict[str, Any]) -> list[common.Chunk]:
    delta_ids = _delta_chunk_ids(delta_manifest)
    chunks = common.chunks_from_manifest(chunk_manifest)
    return [chunk for chunk in chunks if chunk.chunk_id in delta_ids]


def _write_checkpoint(delta_manifest: dict[str, Any], *, completed_chunks: list[str] | None = None, failed_batches: list[int] | None = None) -> dict[str, Any]:
    delta_hash = common.sha256_text(json.dumps(delta_manifest.get("chunk_delta_counts", {}), ensure_ascii=False, sort_keys=True))
    checkpoint = {
        "run_id": f"delta_sync_{delta_manifest.get('source_commit_sha')}",
        "source_commit_sha": delta_manifest.get("source_commit_sha"),
        "previous_index_commit_sha": delta_manifest.get("previous_index_commit_sha"),
        "delta_manifest_hash": delta_hash,
        "completed_batch_indexes": [],
        "completed_chunk_ids": completed_chunks or [],
        "failed_batch_indexes": failed_batches or [],
        "resume_cursor": len(completed_chunks or []),
        "generated_at": common.now_iso(),
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(DELTA_CHECKPOINT_PATH, checkpoint)
    return checkpoint


def write_delta_dry_run_report(chunk_manifest: dict[str, Any], delta_manifest: dict[str, Any]) -> dict[str, Any]:
    delta_ids = sorted(_delta_chunk_ids(delta_manifest))
    counts = delta_manifest.get("chunk_delta_counts", {})
    checkpoint = _write_checkpoint(delta_manifest, completed_chunks=[])
    report = {
        "manifest_type": "delta_sync_dry_run_report",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": chunk_manifest.get("commit_sha"),
        "generated_at": common.now_iso(),
        "delta_manifest_path": DELTA_MANIFEST_PATH.as_posix(),
        "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
        "would_embed_chunk_ids": delta_ids,
        "would_embed_chunk_count": len(delta_ids),
        "would_upsert_chunk_count": len(delta_ids),
        "chunk_delta_counts": counts,
        "unchanged_chunk_count": counts.get("unchanged_chunks", 0),
        "deleted_chunk_count": counts.get("deleted_chunks", 0),
        "deleted_policy": "overlay_supersede_or_tombstone_first",
        "checkpoint": checkpoint,
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_upsert_called": False,
            "dashvector_query_called": False,
            "key_printed": False,
            "key_written": False,
            "vector_values_written": False,
        },
        "validation_result": {"status": "passed"},
        "blocked_if": ["delta_manifest_missing", "dry_run_would_call_external_api"],
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(DELTA_DRY_RUN_REPORT_PATH, report)
    common.write_markdown(
        common.OUT_DIR / "latest_delta_sync_dry_run_report.md",
        [
            "# RAG Delta Sync Dry Run Report",
            "",
            "- status: `passed`",
            f"- source_commit_sha: `{report['source_commit_sha']}`",
            f"- would_embed_chunk_count: `{report['would_embed_chunk_count']}`",
            f"- unchanged_chunk_count: `{report['unchanged_chunk_count']}`",
            f"- deleted_policy: `{report['deleted_policy']}`",
            "- alibaba_embedding_api_called: `false`",
            "- dashvector_upsert_called: `false`",
            "- key_printed: `false`",
            "- key_written: `false`",
        ],
    )
    return report


def write_markdown(manifest: dict[str, Any]) -> None:
    lines = [
        "# RAG DashVector Index Manifest",
        "",
        f"- status: `{'blocked' if manifest['blocked'] else 'indexed'}`",
        f"- source_commit_sha: `{manifest['source_commit_sha']}`",
        f"- embedding_model: `{manifest['embedding_model']}`",
        f"- embedding_dimension: `{manifest['embedding_dimension']}`",
        f"- vector_store_provider: `{manifest['vector_store_provider']}`",
        f"- dashvector_collection: `{manifest.get('dashvector_collection') or ''}`",
        f"- indexed_file_count: `{manifest['indexed_file_count']}`",
        f"- indexed_chunk_count: `{manifest['indexed_chunk_count']}`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "- vector_values_written: `false`",
    ]
    if manifest["blocked"]:
        lines.extend(["", "## Blocked Reasons", ""])
        lines.extend(f"- `{reason}`" for reason in manifest.get("blocked_reasons", []))
    common.write_markdown(common.OUT_DIR / "latest_index_manifest.md", lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Sync RAG chunks to DashVector.")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--dry-run", action="store_true", help="Write blocked precondition manifest without external calls.")
    parser.add_argument("--delta-manifest", default=str(DELTA_MANIFEST_PATH), help="Chunk delta manifest for delta-only sync.")
    parser.add_argument("--dry-run-delta", action="store_true", help="Plan delta sync without external API or DashVector calls.")
    parser.add_argument("--resume", action="store_true", help="Resume from latest delta checkpoint when running real delta sync.")
    parser.add_argument("--full-sync-explicit", action="store_true", help="Explicitly allow legacy full-manifest sync.")
    args = parser.parse_args()
    if not common.CHUNK_MANIFEST_PATH.exists():
        raise SystemExit("blocked_chunk_manifest_missing")
    chunk_manifest = common.read_json(common.CHUNK_MANIFEST_PATH)

    if args.dry_run_delta:
        delta_manifest = _load_delta_manifest(args.delta_manifest)
        report = write_delta_dry_run_report(chunk_manifest, delta_manifest)
        print(
            json.dumps(
                {
                    "status": report["validation_result"]["status"],
                    "delta_sync_dry_run_report_path": DELTA_DRY_RUN_REPORT_PATH.as_posix(),
                    "would_embed_chunk_count": report["would_embed_chunk_count"],
                    "alibaba_embedding_api_called": False,
                    "dashvector_upsert_called": False,
                    "key_printed": False,
                    "key_written": False,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0

    if not args.full_sync_explicit:
        delta_manifest = _load_delta_manifest(args.delta_manifest)
        preconditions = precondition_report(chunk_manifest)
        upsert: dict[str, Any] | None = None
        if not args.dry_run and preconditions["preconditions_passed"]:
            chunks = _chunks_from_delta_manifest(chunk_manifest, delta_manifest)
            upsert = upsert_chunks(chunks, max(1, args.batch_size))
            _write_checkpoint(delta_manifest, completed_chunks=[chunk.chunk_id for chunk in chunks])
        manifest = write_index_manifest(chunk_manifest, preconditions, upsert, delta_manifest=delta_manifest)
        write_markdown(manifest)
        print(
            json.dumps(
                {
                    "status": "indexed" if not manifest["blocked"] else "blocked",
                    "sync_mode": "delta",
                    "index_manifest_path": common.INDEX_MANIFEST_PATH.as_posix(),
                    "indexed_chunk_count": manifest["indexed_chunk_count"],
                    "blocked_reasons": manifest["blocked_reasons"],
                    "key_printed": False,
                    "key_written": False,
                    "vector_values_written": False,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0 if not manifest["blocked"] else 2

    preconditions = precondition_report(chunk_manifest)
    upsert: dict[str, Any] | None = None
    if not args.dry_run and preconditions["preconditions_passed"]:
        chunks = common.chunks_from_manifest(chunk_manifest)
        upsert = upsert_chunks(chunks, max(1, args.batch_size))
    manifest = write_index_manifest(chunk_manifest, preconditions, upsert)
    write_markdown(manifest)
    print(
        json.dumps(
            {
                "status": "indexed" if not manifest["blocked"] else "blocked",
                "index_manifest_path": common.INDEX_MANIFEST_PATH.as_posix(),
                "indexed_file_count": manifest["indexed_file_count"],
                "indexed_chunk_count": manifest["indexed_chunk_count"],
                "blocked_reasons": manifest["blocked_reasons"],
                "key_printed": False,
                "key_written": False,
                "vector_values_written": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if not manifest["blocked"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
