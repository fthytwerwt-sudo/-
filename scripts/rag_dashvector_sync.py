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
DEFAULT_DELTA_BATCH_SIZE = 8
ALLOWED_DELTA_BATCH_SIZES = {4, 8, 16, 32}
MAX_BATCH_SIZE_WITHOUT_EXPLICIT_FLAG = 16
DEFAULT_EMBEDDING_TIMEOUT_SECONDS = 120
DEFAULT_UPSERT_TIMEOUT_SECONDS = 120
DEFAULT_BATCH_TOTAL_TIMEOUT_SECONDS = 300
DELTA_MANIFEST_PATH = common.OUT_DIR / "latest_chunk_delta_manifest.json"
DELTA_BATCH_MANIFEST_PATH = common.OUT_DIR / "latest_delta_batch_manifest.json"
DELTA_BATCH_MANIFEST_MD_PATH = common.OUT_DIR / "latest_delta_batch_manifest.md"
DELTA_DRY_RUN_REPORT_PATH = common.OUT_DIR / "latest_delta_sync_dry_run_report.json"
DELTA_CHECKPOINT_PATH = common.OUT_DIR / "latest_delta_sync_checkpoint.json"
DELTA_PARTIAL_MANIFEST_PATH = common.OUT_DIR / "latest_delta_index_partial_manifest.json"
DELTA_PARTIAL_MANIFEST_MD_PATH = common.OUT_DIR / "latest_delta_index_partial_manifest.md"
DELTA_TIMEOUT_REPORT_PATH = common.OUT_DIR / "latest_delta_sync_timeout_report.json"


class BatchTimeoutError(RuntimeError):
    def __init__(self, report: dict[str, Any]):
        self.report = report
        super().__init__("blocked_batch_timeout")


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
    batch_manifest: dict[str, Any] | None = None,
    checkpoint: dict[str, Any] | None = None,
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
        "batch_sync_enabled": bool(batch_manifest),
        "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix() if batch_manifest else None,
        "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix() if checkpoint else None,
        "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix() if batch_manifest else None,
        "final_manifest_gate": upsert.get("final_manifest_gate") if isinstance(upsert, dict) else None,
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


def _stable_hash(value: dict[str, Any]) -> str:
    return common.sha256_text(json.dumps(value, ensure_ascii=False, sort_keys=True))


def _delta_manifest_hash(delta_manifest: dict[str, Any]) -> str:
    return _stable_hash(
        {
            "manifest_type": delta_manifest.get("manifest_type"),
            "source_commit_sha": delta_manifest.get("source_commit_sha"),
            "previous_index_commit_sha": delta_manifest.get("previous_index_commit_sha"),
            "chunk_delta_counts": delta_manifest.get("chunk_delta_counts", {}),
            "delta_chunk_ids": sorted(_delta_chunk_ids(delta_manifest)),
        }
    )


def _batch_manifest_hash(batch_manifest: dict[str, Any]) -> str:
    return _stable_hash(
        {
            "manifest_type": batch_manifest.get("manifest_type"),
            "source_commit_sha": batch_manifest.get("source_commit_sha"),
            "previous_index_commit_sha": batch_manifest.get("previous_index_commit_sha"),
            "delta_manifest_hash": batch_manifest.get("delta_manifest_hash"),
            "batch_size": batch_manifest.get("batch_size"),
            "batches": [
                {
                    "batch_index": batch.get("batch_index"),
                    "batch_id": batch.get("batch_id"),
                    "chunk_ids": batch.get("chunk_ids", []),
                }
                for batch in batch_manifest.get("batches", [])
            ],
        }
    )


def _normalize_batch_size(batch_size: int, *, allow_large_batch: bool = False) -> int:
    if batch_size not in ALLOWED_DELTA_BATCH_SIZES:
        raise SystemExit("blocked_delta_batch_size_not_allowed")
    if batch_size > MAX_BATCH_SIZE_WITHOUT_EXPLICIT_FLAG and not allow_large_batch:
        raise SystemExit("blocked_delta_batch_size_requires_explicit_flag")
    return batch_size


def _build_batch_manifest(delta_manifest: dict[str, Any], chunks: list[common.Chunk], *, batch_size: int) -> dict[str, Any]:
    batches: list[dict[str, Any]] = []
    for batch_index, batch in enumerate(iter_sync_batches(chunks, batch_size)):
        chunk_ids = [chunk.chunk_id for chunk in batch]
        batch_id = f"delta_batch_{batch_index:04d}_{common.sha256_text('|'.join(chunk_ids))[:12]}"
        batches.append(
            {
                "batch_index": batch_index,
                "batch_id": batch_id,
                "chunk_ids": chunk_ids,
                "source_paths": sorted({chunk.source_path for chunk in batch}),
                "chunk_count": len(batch),
                "status": "pending",
            }
        )
    manifest = {
        "manifest_type": "delta_batch_manifest",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": delta_manifest.get("source_commit_sha"),
        "previous_index_commit_sha": delta_manifest.get("previous_index_commit_sha"),
        "delta_manifest_hash": _delta_manifest_hash(delta_manifest),
        "generated_at": common.now_iso(),
        "batch_size": batch_size,
        "batch_size_policy": {
            "default_batch_size": DEFAULT_DELTA_BATCH_SIZE,
            "allowed_batch_sizes": sorted(ALLOWED_DELTA_BATCH_SIZES),
            "fallback_on_failure": "split_failed_batch_in_half",
            "max_batch_size_without_explicit_flag": MAX_BATCH_SIZE_WITHOUT_EXPLICIT_FLAG,
        },
        "batch_count": len(batches),
        "total_delta_chunk_count": sum(batch["chunk_count"] for batch in batches),
        "batches": batches,
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_upsert_called": False,
            "dashvector_query_called": False,
            "key_printed": False,
            "key_written": False,
            "vector_values_written": False,
        },
        "validation_result": {"status": "passed"},
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    manifest["batch_manifest_hash"] = _batch_manifest_hash(manifest)
    return manifest


def _write_batch_manifest(batch_manifest: dict[str, Any]) -> None:
    common.write_json(DELTA_BATCH_MANIFEST_PATH, batch_manifest)
    lines = [
        "# RAG Delta Batch Manifest",
        "",
        f"- source_commit_sha: `{batch_manifest['source_commit_sha']}`",
        f"- previous_index_commit_sha: `{batch_manifest['previous_index_commit_sha']}`",
        f"- delta_manifest_hash: `{batch_manifest['delta_manifest_hash']}`",
        f"- batch_manifest_hash: `{batch_manifest['batch_manifest_hash']}`",
        f"- batch_size: `{batch_manifest['batch_size']}`",
        f"- batch_count: `{batch_manifest['batch_count']}`",
        f"- total_delta_chunk_count: `{batch_manifest['total_delta_chunk_count']}`",
        "- all_batches_initial_status: `pending`",
        "- alibaba_embedding_api_called: `false`",
        "- dashvector_upsert_called: `false`",
        "- vector_values_written: `false`",
    ]
    common.write_markdown(DELTA_BATCH_MANIFEST_MD_PATH, lines)


def _new_checkpoint(delta_manifest: dict[str, Any], batch_manifest: dict[str, Any]) -> dict[str, Any]:
    checkpoint = {
        "run_id": f"delta_sync_{delta_manifest.get('source_commit_sha')}",
        "source_commit_sha": delta_manifest.get("source_commit_sha"),
        "previous_index_commit_sha": delta_manifest.get("previous_index_commit_sha"),
        "delta_manifest_hash": batch_manifest.get("delta_manifest_hash"),
        "batch_manifest_hash": batch_manifest.get("batch_manifest_hash"),
        "completed_batch_indexes": [],
        "completed_chunk_ids": [],
        "failed_batch_indexes": [],
        "in_progress_batch_index": None,
        "resume_cursor": 0,
        "last_success_at": None,
        "last_failure_at": None,
        "stage_progress": [],
        "skipped_completed_batch_indexes": [],
        "external_call_report": {
            "embedding_batch_calls": 0,
            "upsert_batch_calls": 0,
            "alibaba_embedding_api_called": False,
            "dashvector_upsert_called": False,
            "dashvector_query_called": False,
            "key_printed": False,
            "key_written": False,
            "vector_values_written": False,
        },
        "generated_at": common.now_iso(),
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    return checkpoint


def _write_checkpoint(checkpoint: dict[str, Any]) -> dict[str, Any]:
    checkpoint["generated_at"] = common.now_iso()
    common.write_json(DELTA_CHECKPOINT_PATH, checkpoint)
    return checkpoint


def _load_checkpoint_for_resume(delta_manifest: dict[str, Any], batch_manifest: dict[str, Any]) -> dict[str, Any]:
    if not DELTA_CHECKPOINT_PATH.exists():
        raise SystemExit("blocked_checkpoint_missing")
    checkpoint = common.read_json(DELTA_CHECKPOINT_PATH)
    if checkpoint.get("source_commit_sha") != delta_manifest.get("source_commit_sha"):
        raise SystemExit("blocked_source_commit_sha_mismatch")
    if checkpoint.get("delta_manifest_hash") != batch_manifest.get("delta_manifest_hash"):
        raise SystemExit("blocked_delta_manifest_hash_mismatch")
    if checkpoint.get("batch_manifest_hash") != batch_manifest.get("batch_manifest_hash"):
        raise SystemExit("blocked_batch_manifest_hash_mismatch")
    return checkpoint


def _dedupe(values: list[Any]) -> list[Any]:
    seen: set[Any] = set()
    output: list[Any] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def _write_timeout_report(
    *,
    batch: dict[str, Any],
    stage: str,
    elapsed_seconds: float,
    blocked_reason: str = "blocked_batch_timeout",
) -> dict[str, Any]:
    report = {
        "manifest_type": "delta_sync_timeout_report",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "generated_at": common.now_iso(),
        "batch_index": batch["batch_index"],
        "batch_id": batch["batch_id"],
        "stage": stage,
        "elapsed_seconds": round(elapsed_seconds, 3),
        "chunk_ids": batch.get("chunk_ids", []),
        "source_paths": batch.get("source_paths", []),
        "blocked_reason": blocked_reason,
        "validation_result": {"status": "blocked"},
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    common.write_json(DELTA_TIMEOUT_REPORT_PATH, report)
    return report


def _run_stage_with_timeout(
    *,
    batch: dict[str, Any],
    stage: str,
    timeout_seconds: int,
    batch_started_monotonic: float,
    batch_total_timeout_seconds: int,
    action: Any,
) -> tuple[Any, float]:
    stage_started = time.monotonic()
    try:
        result = action()
    except Exception as exc:
        elapsed = time.monotonic() - stage_started
        if elapsed > timeout_seconds or time.monotonic() - batch_started_monotonic > batch_total_timeout_seconds:
            raise BatchTimeoutError(_write_timeout_report(batch=batch, stage=stage, elapsed_seconds=elapsed)) from exc
        raise
    elapsed = time.monotonic() - stage_started
    if elapsed > timeout_seconds or time.monotonic() - batch_started_monotonic > batch_total_timeout_seconds:
        raise BatchTimeoutError(_write_timeout_report(batch=batch, stage=stage, elapsed_seconds=elapsed))
    return result, elapsed


def _batch_progress(batch_manifest: dict[str, Any], checkpoint: dict[str, Any]) -> dict[str, int | bool | None]:
    completed = set(int(item) for item in checkpoint.get("completed_batch_indexes", []))
    failed = set(int(item) for item in checkpoint.get("failed_batch_indexes", []))
    batch_count = int(batch_manifest.get("batch_count") or 0)
    pending = [idx for idx in range(batch_count) if idx not in completed and idx not in failed]
    return {
        "batch_sync_enabled": True,
        "batch_count": batch_count,
        "completed_batch_count": len(completed),
        "failed_batch_count": len(failed),
        "pending_batch_count": len(pending),
        "completed_chunk_count": len(set(checkpoint.get("completed_chunk_ids", []))),
        "delta_chunk_count": int(batch_manifest.get("total_delta_chunk_count") or 0),
        "resume_available": bool(completed or failed),
        "last_completed_batch_index": max(completed) if completed else None,
    }


def _write_partial_manifest(
    *,
    status: str,
    delta_manifest: dict[str, Any],
    batch_manifest: dict[str, Any],
    checkpoint: dict[str, Any],
    blocked_reasons: list[str] | None = None,
    timeout_report: dict[str, Any] | None = None,
) -> dict[str, Any]:
    progress = _batch_progress(batch_manifest, checkpoint)
    manifest = {
        "manifest_type": "delta_index_partial_manifest",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "generated_at": common.now_iso(),
        "status": status,
        "source_commit_sha": delta_manifest.get("source_commit_sha"),
        "previous_index_commit_sha": delta_manifest.get("previous_index_commit_sha"),
        "delta_manifest_hash": batch_manifest.get("delta_manifest_hash"),
        "batch_manifest_hash": batch_manifest.get("batch_manifest_hash"),
        "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
        "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
        "completed_batch_count": progress["completed_batch_count"],
        "completed_chunk_count": progress["completed_chunk_count"],
        "failed_batch_count": progress["failed_batch_count"],
        "pending_batch_count": progress["pending_batch_count"],
        "final_index_manifest_written": False,
        "current_RAG_index_latest_claim": False,
        "blocked_reasons": blocked_reasons or [],
        "timeout_report": timeout_report,
        "external_call_report": checkpoint.get("external_call_report", {}),
        "validation_result": {"status": "blocked" if status in {"blocked", "interrupted"} else "passed"},
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    common.write_json(DELTA_PARTIAL_MANIFEST_PATH, manifest)
    lines = [
        "# RAG Delta Index Partial Manifest",
        "",
        f"- status: `{manifest['status']}`",
        f"- source_commit_sha: `{manifest['source_commit_sha']}`",
        f"- completed_batch_count: `{manifest['completed_batch_count']}`",
        f"- completed_chunk_count: `{manifest['completed_chunk_count']}`",
        f"- failed_batch_count: `{manifest['failed_batch_count']}`",
        f"- pending_batch_count: `{manifest['pending_batch_count']}`",
        "- final_index_manifest_written: `false`",
        "- current_RAG_index_latest_claim: `false`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "- vector_values_written: `false`",
    ]
    if blocked_reasons:
        lines.extend(["", "## Blocked Reasons", ""])
        lines.extend(f"- `{reason}`" for reason in blocked_reasons)
    common.write_markdown(DELTA_PARTIAL_MANIFEST_MD_PATH, lines)
    return manifest


def _evaluate_final_manifest_gate(
    *,
    delta_manifest: dict[str, Any],
    batch_manifest: dict[str, Any],
    checkpoint: dict[str, Any],
) -> dict[str, Any]:
    reasons: list[str] = []
    completed_batches = set(int(item) for item in checkpoint.get("completed_batch_indexes", []))
    all_batch_indexes = {int(batch["batch_index"]) for batch in batch_manifest.get("batches", [])}
    completed_chunk_ids = set(checkpoint.get("completed_chunk_ids", []))
    delta_chunk_count = int(batch_manifest.get("total_delta_chunk_count") or 0)
    if completed_batches != all_batch_indexes:
        reasons.append("partial_batches_only")
    if checkpoint.get("failed_batch_indexes"):
        reasons.append("failed_batches_exist")
    if len(completed_chunk_ids) != delta_chunk_count:
        reasons.append("completed_chunk_count_not_equal_delta_chunk_count")
    if checkpoint.get("delta_manifest_hash") != batch_manifest.get("delta_manifest_hash"):
        reasons.append("delta_manifest_hash_mismatch")
    if checkpoint.get("batch_manifest_hash") != batch_manifest.get("batch_manifest_hash"):
        reasons.append("batch_manifest_hash_mismatch")
    counts = delta_manifest.get("chunk_delta_counts", {})
    if counts.get("unchanged_chunks") is None:
        reasons.append("unchanged_chunks_reuse_status_missing")
    if counts.get("deleted_chunks") is None or counts.get("superseded_chunks") is None:
        reasons.append("deleted_or_superseded_chunk_policy_missing")
    return {
        "status": "passed" if not reasons else "blocked",
        "write_final_index_manifest_allowed": not reasons,
        "blocked_reasons": reasons,
        "all_batches_passed": completed_batches == all_batch_indexes,
        "no_failed_batches": not checkpoint.get("failed_batch_indexes"),
        "completed_chunk_count_equals_delta_chunk_count": len(completed_chunk_ids) == delta_chunk_count,
        "unchanged_chunks_reused": counts.get("unchanged_chunks") is not None,
        "deleted_or_superseded_chunks_marked": counts.get("deleted_chunks") is not None and counts.get("superseded_chunks") is not None,
    }


def _simulate_delta_batches(
    *,
    delta_manifest: dict[str, Any],
    batch_manifest: dict[str, Any],
    checkpoint: dict[str, Any],
    resume: bool = False,
    simulate_batch_execution: bool = False,
    simulate_interruption_after_batch_index: int | None = None,
    simulate_timeout_stage: str | None = None,
    simulate_timeout_batch_index: int = 0,
) -> tuple[dict[str, Any], dict[str, Any] | None, list[int]]:
    skipped: list[int] = []
    completed = set(int(item) for item in checkpoint.get("completed_batch_indexes", []))
    timeout_report: dict[str, Any] | None = None
    if resume:
        checkpoint["skipped_completed_batch_indexes"] = sorted(completed)
        skipped = sorted(completed)
    if not simulate_batch_execution and simulate_timeout_stage is None and simulate_interruption_after_batch_index is None:
        _write_checkpoint(checkpoint)
        _write_partial_manifest(
            status="partial",
            delta_manifest=delta_manifest,
            batch_manifest=batch_manifest,
            checkpoint=checkpoint,
        )
        return checkpoint, None, skipped

    for batch in batch_manifest.get("batches", []):
        batch_index = int(batch["batch_index"])
        if batch_index in completed:
            continue
        checkpoint["in_progress_batch_index"] = batch_index
        checkpoint["resume_cursor"] = batch_index
        _write_checkpoint(checkpoint)

        if simulate_timeout_stage and batch_index == simulate_timeout_batch_index:
            timeout_report = _write_timeout_report(
                batch=batch,
                stage=simulate_timeout_stage,
                elapsed_seconds=(
                    DEFAULT_EMBEDDING_TIMEOUT_SECONDS + 1
                    if simulate_timeout_stage == "embedding"
                    else DEFAULT_UPSERT_TIMEOUT_SECONDS + 1
                ),
            )
            checkpoint["failed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("failed_batch_indexes", []), batch_index]))
            checkpoint["last_failure_at"] = common.now_iso()
            checkpoint["in_progress_batch_index"] = None
            _write_checkpoint(checkpoint)
            _write_partial_manifest(
                status="blocked",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=["blocked_batch_timeout"],
                timeout_report=timeout_report,
            )
            return checkpoint, timeout_report, skipped

        if not simulate_batch_execution:
            continue
        checkpoint.setdefault("stage_progress", []).append(
            {
                "batch_index": batch_index,
                "batch_id": batch["batch_id"],
                "stage": "embedding",
                "status": "passed",
                "elapsed_seconds": 0.0,
                "dry_run": True,
            }
        )
        checkpoint.setdefault("stage_progress", []).append(
            {
                "batch_index": batch_index,
                "batch_id": batch["batch_id"],
                "stage": "upsert",
                "status": "passed",
                "elapsed_seconds": 0.0,
                "dry_run": True,
            }
        )
        checkpoint["completed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("completed_batch_indexes", []), batch_index]))
        checkpoint["completed_chunk_ids"] = sorted(_dedupe([*checkpoint.get("completed_chunk_ids", []), *batch.get("chunk_ids", [])]))
        checkpoint["failed_batch_indexes"] = [idx for idx in checkpoint.get("failed_batch_indexes", []) if idx != batch_index]
        checkpoint["last_success_at"] = common.now_iso()
        checkpoint["resume_cursor"] = batch_index + 1
        checkpoint["in_progress_batch_index"] = None
        _write_checkpoint(checkpoint)
        _write_partial_manifest(
            status="partial",
            delta_manifest=delta_manifest,
            batch_manifest=batch_manifest,
            checkpoint=checkpoint,
        )
        if simulate_interruption_after_batch_index is not None and batch_index >= simulate_interruption_after_batch_index:
            _write_partial_manifest(
                status="interrupted",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=["simulated_interruption_after_batch"],
            )
            return checkpoint, timeout_report, skipped
    return checkpoint, timeout_report, skipped


def _sync_delta_batches(
    *,
    delta_manifest: dict[str, Any],
    batch_manifest: dict[str, Any],
    chunks_by_id: dict[str, common.Chunk],
    checkpoint: dict[str, Any],
    embedding_timeout_seconds: int,
    upsert_timeout_seconds: int,
    batch_total_timeout_seconds: int,
) -> dict[str, Any]:
    started_at = common.now_iso()
    batches: list[dict[str, Any]] = []
    completed = set(int(item) for item in checkpoint.get("completed_batch_indexes", []))
    skipped = sorted(completed)
    checkpoint["skipped_completed_batch_indexes"] = skipped
    _write_checkpoint(checkpoint)
    for batch in batch_manifest.get("batches", []):
        batch_index = int(batch["batch_index"])
        if batch_index in completed:
            continue
        batch_chunks = [chunks_by_id[chunk_id] for chunk_id in batch["chunk_ids"] if chunk_id in chunks_by_id]
        if len(batch_chunks) != len(batch["chunk_ids"]):
            checkpoint["failed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("failed_batch_indexes", []), batch_index]))
            checkpoint["last_failure_at"] = common.now_iso()
            _write_checkpoint(checkpoint)
            _write_partial_manifest(
                status="blocked",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=["batch_chunk_id_missing_from_current_manifest"],
            )
            raise RuntimeError("batch_chunk_id_missing_from_current_manifest")
        batch_started = time.monotonic()
        checkpoint["in_progress_batch_index"] = batch_index
        checkpoint["resume_cursor"] = batch_index
        _write_checkpoint(checkpoint)
        try:
            vectors, embedding_elapsed = _run_stage_with_timeout(
                batch=batch,
                stage="embedding",
                timeout_seconds=embedding_timeout_seconds,
                batch_started_monotonic=batch_started,
                batch_total_timeout_seconds=batch_total_timeout_seconds,
                action=lambda: embed_batch_with_retry(batch_chunks),
            )
            checkpoint["external_call_report"]["alibaba_embedding_api_called"] = True
            checkpoint["external_call_report"]["embedding_batch_calls"] += 1
            checkpoint.setdefault("stage_progress", []).append(
                {
                    "batch_index": batch_index,
                    "batch_id": batch["batch_id"],
                    "stage": "embedding",
                    "status": "passed",
                    "elapsed_seconds": round(embedding_elapsed, 3),
                }
            )
            _write_checkpoint(checkpoint)
            if len(vectors) != len(batch_chunks):
                raise RuntimeError("blocked_embedding_vector_count_mismatch")
            docs = [
                common.dashvector_doc_from_chunk(chunk, vector)
                for chunk, vector in zip(batch_chunks, vectors)
            ]
            result, upsert_elapsed = _run_stage_with_timeout(
                batch=batch,
                stage="upsert",
                timeout_seconds=upsert_timeout_seconds,
                batch_started_monotonic=batch_started,
                batch_total_timeout_seconds=batch_total_timeout_seconds,
                action=lambda: upsert_docs_with_retry(docs),
            )
            checkpoint["external_call_report"]["dashvector_upsert_called"] = True
            checkpoint["external_call_report"]["upsert_batch_calls"] += 1
            checkpoint.setdefault("stage_progress", []).append(
                {
                    "batch_index": batch_index,
                    "batch_id": batch["batch_id"],
                    "stage": "upsert",
                    "status": "passed" if result.get("success") else "blocked",
                    "elapsed_seconds": round(upsert_elapsed, 3),
                }
            )
            if not result.get("success"):
                raise RuntimeError("blocked_dashvector_upsert_failed")
        except BatchTimeoutError as exc:
            checkpoint["failed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("failed_batch_indexes", []), batch_index]))
            checkpoint["last_failure_at"] = common.now_iso()
            checkpoint["in_progress_batch_index"] = None
            _write_checkpoint(checkpoint)
            _write_partial_manifest(
                status="blocked",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=["blocked_batch_timeout"],
                timeout_report=exc.report,
            )
            raise
        except Exception:
            checkpoint["failed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("failed_batch_indexes", []), batch_index]))
            checkpoint["last_failure_at"] = common.now_iso()
            checkpoint["in_progress_batch_index"] = None
            _write_checkpoint(checkpoint)
            _write_partial_manifest(
                status="blocked",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=["batch_execution_failed"],
            )
            raise
        checkpoint["completed_batch_indexes"] = sorted(_dedupe([*checkpoint.get("completed_batch_indexes", []), batch_index]))
        checkpoint["completed_chunk_ids"] = sorted(_dedupe([*checkpoint.get("completed_chunk_ids", []), *batch["chunk_ids"]]))
        checkpoint["failed_batch_indexes"] = [idx for idx in checkpoint.get("failed_batch_indexes", []) if idx != batch_index]
        checkpoint["resume_cursor"] = batch_index + 1
        checkpoint["last_success_at"] = common.now_iso()
        checkpoint["in_progress_batch_index"] = None
        _write_checkpoint(checkpoint)
        batches.append(
            {
                "batch_index": batch_index,
                "batch_id": batch["batch_id"],
                "chunk_count": batch["chunk_count"],
                "success": True,
            }
        )
        _write_partial_manifest(
            status="partial",
            delta_manifest=delta_manifest,
            batch_manifest=batch_manifest,
            checkpoint=checkpoint,
        )
        if len(checkpoint["completed_batch_indexes"]) % 5 == 0:
            print(json.dumps({"sync_progress": _batch_progress(batch_manifest, checkpoint)}, ensure_ascii=False), flush=True)
    final_gate = _evaluate_final_manifest_gate(
        delta_manifest=delta_manifest,
        batch_manifest=batch_manifest,
        checkpoint=checkpoint,
    )
    if final_gate["status"] != "passed":
        _write_partial_manifest(
            status="blocked",
            delta_manifest=delta_manifest,
            batch_manifest=batch_manifest,
            checkpoint=checkpoint,
            blocked_reasons=final_gate["blocked_reasons"],
        )
        raise RuntimeError("blocked_final_index_manifest_gate")
    return {
        "started_at": started_at,
        "finished_at": common.now_iso(),
        "upserted_chunk_count": len(set(checkpoint.get("completed_chunk_ids", []))),
        "batch_count": len(batch_manifest.get("batches", [])),
        "skipped_completed_batch_indexes": skipped,
        "batches": batches,
        "checkpoint": checkpoint,
        "final_manifest_gate": final_gate,
    }


def write_delta_dry_run_report(
    chunk_manifest: dict[str, Any],
    delta_manifest: dict[str, Any],
    *,
    batch_size: int,
    resume: bool = False,
    simulate_batch_execution: bool = False,
    simulate_interruption_after_batch_index: int | None = None,
    simulate_timeout_stage: str | None = None,
    simulate_timeout_batch_index: int = 0,
) -> dict[str, Any]:
    delta_ids = sorted(_delta_chunk_ids(delta_manifest))
    counts = delta_manifest.get("chunk_delta_counts", {})
    chunks = _chunks_from_delta_manifest(chunk_manifest, delta_manifest)
    batch_manifest = _build_batch_manifest(delta_manifest, chunks, batch_size=batch_size)
    _write_batch_manifest(batch_manifest)
    checkpoint = _load_checkpoint_for_resume(delta_manifest, batch_manifest) if resume else _new_checkpoint(delta_manifest, batch_manifest)
    checkpoint, timeout_report, skipped_batches = _simulate_delta_batches(
        delta_manifest=delta_manifest,
        batch_manifest=batch_manifest,
        checkpoint=checkpoint,
        resume=resume,
        simulate_batch_execution=simulate_batch_execution,
        simulate_interruption_after_batch_index=simulate_interruption_after_batch_index,
        simulate_timeout_stage=simulate_timeout_stage,
        simulate_timeout_batch_index=simulate_timeout_batch_index,
    )
    progress = _batch_progress(batch_manifest, checkpoint)
    final_gate = _evaluate_final_manifest_gate(delta_manifest=delta_manifest, batch_manifest=batch_manifest, checkpoint=checkpoint)
    report_status = "blocked" if timeout_report else "passed"
    if simulate_interruption_after_batch_index is not None and progress["pending_batch_count"]:
        report_status = "interrupted"
    report = {
        "manifest_type": "delta_sync_dry_run_report",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": chunk_manifest.get("commit_sha"),
        "generated_at": common.now_iso(),
        "delta_manifest_path": DELTA_MANIFEST_PATH.as_posix(),
        "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
        "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
        "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
        "would_embed_chunk_ids": delta_ids,
        "would_embed_chunk_count": len(delta_ids),
        "would_upsert_chunk_count": len(delta_ids),
        "batch_sync_enabled": True,
        "batch_size": batch_manifest["batch_size"],
        "batch_count": batch_manifest["batch_count"],
        "batch_manifest_hash": batch_manifest["batch_manifest_hash"],
        "delta_manifest_hash": batch_manifest["delta_manifest_hash"],
        "completed_batch_count_in_dry_run": progress["completed_batch_count"],
        "failed_batch_count_in_dry_run": progress["failed_batch_count"],
        "pending_batch_count_in_dry_run": progress["pending_batch_count"],
        "resume_skips_completed_batches": bool(resume and skipped_batches),
        "skipped_completed_batch_indexes": skipped_batches,
        "no_duplicate_completed_chunk_ids": len(checkpoint.get("completed_chunk_ids", [])) == len(set(checkpoint.get("completed_chunk_ids", []))),
        "timeout_report": timeout_report,
        "final_manifest_gate": final_gate,
        "final_index_manifest_written": False,
        "current_RAG_index_latest_claim": False,
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
        "validation_result": {"status": report_status},
        "blocked_if": ["delta_manifest_missing", "dry_run_would_call_external_api"],
        "key_printed": False,
        "key_written": False,
        "vector_values_written": False,
    }
    common.write_json(DELTA_DRY_RUN_REPORT_PATH, report)
    common.write_markdown(
        common.OUT_DIR / "latest_delta_sync_dry_run_report.md",
        [
            "# RAG Delta Sync Dry Run Report",
            "",
            f"- status: `{report_status}`",
            f"- source_commit_sha: `{report['source_commit_sha']}`",
            f"- would_embed_chunk_count: `{report['would_embed_chunk_count']}`",
            f"- batch_count: `{report['batch_count']}`",
            f"- batch_size: `{report['batch_size']}`",
            f"- completed_batch_count_in_dry_run: `{report['completed_batch_count_in_dry_run']}`",
            f"- failed_batch_count_in_dry_run: `{report['failed_batch_count_in_dry_run']}`",
            f"- pending_batch_count_in_dry_run: `{report['pending_batch_count_in_dry_run']}`",
            f"- unchanged_chunk_count: `{report['unchanged_chunk_count']}`",
            f"- deleted_policy: `{report['deleted_policy']}`",
            "- final_index_manifest_written: `false`",
            "- current_RAG_index_latest_claim: `false`",
            "- alibaba_embedding_api_called: `false`",
            "- dashvector_upsert_called: `false`",
            "- key_printed: `false`",
            "- key_written: `false`",
            "- vector_values_written: `false`",
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
    parser.add_argument("--batch-size", type=int, default=DEFAULT_DELTA_BATCH_SIZE)
    parser.add_argument("--allow-large-batch", action="store_true", help="Explicitly allow delta batch size > 16.")
    parser.add_argument("--dry-run", action="store_true", help="Write blocked precondition manifest without external calls.")
    parser.add_argument("--delta-manifest", default=str(DELTA_MANIFEST_PATH), help="Chunk delta manifest for delta-only sync.")
    parser.add_argument("--dry-run-delta", action="store_true", help="Plan delta sync without external API or DashVector calls.")
    parser.add_argument("--resume", action="store_true", help="Resume from latest delta checkpoint when running real delta sync.")
    parser.add_argument("--full-sync-explicit", action="store_true", help="Explicitly allow legacy full-manifest sync.")
    parser.add_argument("--embedding-timeout-seconds", type=int, default=DEFAULT_EMBEDDING_TIMEOUT_SECONDS)
    parser.add_argument("--upsert-timeout-seconds", type=int, default=DEFAULT_UPSERT_TIMEOUT_SECONDS)
    parser.add_argument("--batch-total-timeout-seconds", type=int, default=DEFAULT_BATCH_TOTAL_TIMEOUT_SECONDS)
    parser.add_argument("--simulate-batch-execution", action="store_true", help="Dry-run only: simulate per-batch completion without external calls.")
    parser.add_argument("--simulate-interruption-after-batch-index", type=int, help="Dry-run only: stop after completing this batch index.")
    parser.add_argument("--simulate-timeout-stage", choices=("embedding", "upsert"), help="Dry-run only: simulate a stage timeout.")
    parser.add_argument("--simulate-timeout-batch-index", type=int, default=0)
    args = parser.parse_args()
    if not common.CHUNK_MANIFEST_PATH.exists():
        raise SystemExit("blocked_chunk_manifest_missing")
    chunk_manifest = common.read_json(common.CHUNK_MANIFEST_PATH)
    batch_size = _normalize_batch_size(args.batch_size, allow_large_batch=args.allow_large_batch)

    if args.dry_run_delta:
        delta_manifest = _load_delta_manifest(args.delta_manifest)
        report = write_delta_dry_run_report(
            chunk_manifest,
            delta_manifest,
            batch_size=batch_size,
            resume=args.resume,
            simulate_batch_execution=args.simulate_batch_execution,
            simulate_interruption_after_batch_index=args.simulate_interruption_after_batch_index,
            simulate_timeout_stage=args.simulate_timeout_stage,
            simulate_timeout_batch_index=args.simulate_timeout_batch_index,
        )
        print(
            json.dumps(
                {
                    "status": report["validation_result"]["status"],
                    "delta_sync_dry_run_report_path": DELTA_DRY_RUN_REPORT_PATH.as_posix(),
                    "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
                    "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
                    "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
                    "would_embed_chunk_count": report["would_embed_chunk_count"],
                    "batch_count": report["batch_count"],
                    "batch_size": report["batch_size"],
                    "completed_batch_count_in_dry_run": report["completed_batch_count_in_dry_run"],
                    "failed_batch_count_in_dry_run": report["failed_batch_count_in_dry_run"],
                    "resume_skips_completed_batches": report["resume_skips_completed_batches"],
                    "no_duplicate_completed_chunk_ids": report["no_duplicate_completed_chunk_ids"],
                    "alibaba_embedding_api_called": False,
                    "dashvector_upsert_called": False,
                    "current_RAG_index_latest_claim": False,
                    "key_printed": False,
                    "key_written": False,
                    "vector_values_written": False,
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
        chunks = _chunks_from_delta_manifest(chunk_manifest, delta_manifest)
        batch_manifest = _build_batch_manifest(delta_manifest, chunks, batch_size=batch_size)
        _write_batch_manifest(batch_manifest)
        checkpoint = _load_checkpoint_for_resume(delta_manifest, batch_manifest) if args.resume else _new_checkpoint(delta_manifest, batch_manifest)
        if args.dry_run:
            _write_checkpoint(checkpoint)
            _write_partial_manifest(
                status="partial",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
            )
            blocked_reasons = ["dry_run_delta_real_sync_not_executed"]
        elif not preconditions["preconditions_passed"]:
            _write_checkpoint(checkpoint)
            blocked_reasons = list(preconditions.get("blocked_reasons", []))
            _write_partial_manifest(
                status="blocked",
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
                blocked_reasons=blocked_reasons,
            )
        else:
            try:
                chunks_by_id = {chunk.chunk_id: chunk for chunk in chunks}
                upsert = _sync_delta_batches(
                    delta_manifest=delta_manifest,
                    batch_manifest=batch_manifest,
                    chunks_by_id=chunks_by_id,
                    checkpoint=checkpoint,
                    embedding_timeout_seconds=args.embedding_timeout_seconds,
                    upsert_timeout_seconds=args.upsert_timeout_seconds,
                    batch_total_timeout_seconds=args.batch_total_timeout_seconds,
                )
                checkpoint = upsert["checkpoint"]
                blocked_reasons = []
            except Exception as exc:
                print(json.dumps({"status": "blocked", "blocked_reason": str(exc), "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix()}, ensure_ascii=False, sort_keys=True))
                return 2
        if upsert:
            manifest = write_index_manifest(
                chunk_manifest,
                preconditions,
                upsert,
                delta_manifest=delta_manifest,
                batch_manifest=batch_manifest,
                checkpoint=checkpoint,
            )
            write_markdown(manifest)
        else:
            manifest = {
                "blocked": True,
                "blocked_reasons": blocked_reasons,
                "indexed_chunk_count": 0,
                "final_index_manifest_written": False,
                "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
            }
        print(
            json.dumps(
                {
                    "status": "indexed" if not manifest["blocked"] else "blocked",
                    "sync_mode": "delta",
                    "index_manifest_path": common.INDEX_MANIFEST_PATH.as_posix() if upsert else None,
                    "batch_manifest_path": DELTA_BATCH_MANIFEST_PATH.as_posix(),
                    "checkpoint_path": DELTA_CHECKPOINT_PATH.as_posix(),
                    "partial_manifest_path": DELTA_PARTIAL_MANIFEST_PATH.as_posix(),
                    "indexed_chunk_count": manifest["indexed_chunk_count"],
                    "blocked_reasons": manifest["blocked_reasons"],
                    "final_index_manifest_written": bool(upsert),
                    "current_RAG_index_latest_claim": False,
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
