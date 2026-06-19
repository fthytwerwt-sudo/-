#!/usr/bin/env python3
"""Validate RAG index and chunk manifests without dumping vectors or secrets."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


REQUIRED_CHUNK_FIELDS = {
    "chunk_id",
    "source_path",
    "line_range",
    "chunk_hash",
    "file_hash",
    "commit_sha",
}


def _resolve(path_value: str | None, default: pathlib.Path) -> pathlib.Path:
    path = pathlib.Path(path_value) if path_value else default
    return path if path.is_absolute() else common.ROOT / path


def validate(index_manifest: dict[str, Any], chunk_manifest: dict[str, Any], check_current: bool) -> dict[str, Any]:
    blocked_reasons: list[str] = []
    missing_metadata: list[dict[str, Any]] = []
    stale_files: list[dict[str, str]] = []
    deleted_files: list[str] = []

    chunks = index_manifest.get("chunks") or chunk_manifest.get("chunks") or []
    if not chunks:
        blocked_reasons.append("indexed_chunks_missing")
    for chunk in chunks:
        missing = sorted(field for field in REQUIRED_CHUNK_FIELDS if not chunk.get(field))
        if missing:
            missing_metadata.append({"chunk_id": chunk.get("chunk_id"), "missing_fields": missing})

    if missing_metadata:
        blocked_reasons.append("chunk_missing_required_metadata")

    indexed_files = index_manifest.get("indexed_files") or []
    if check_current:
        for item in indexed_files:
            source_path = str(item.get("source_path", ""))
            path = common.ROOT / source_path
            if not path.exists():
                deleted_files.append(source_path)
                continue
            current_hash = common.sha256_file(path)
            if current_hash != item.get("file_hash"):
                stale_files.append(
                    {
                        "source_path": source_path,
                        "expected_file_hash": str(item.get("file_hash")),
                        "current_file_hash": current_hash,
                    }
                )
        if stale_files:
            blocked_reasons.append("stale_index_detected")
        if deleted_files:
            blocked_reasons.append("deleted_file_still_indexed")

    index_chunk_count = int(index_manifest.get("indexed_chunk_count") or len(index_manifest.get("chunks") or []))
    chunk_count = int(chunk_manifest.get("chunk_count") or len(chunk_manifest.get("chunks") or []))
    if index_chunk_count != chunk_count:
        blocked_reasons.append("index_chunk_count_mismatch")

    if index_manifest.get("blocked"):
        blocked_reasons.append("index_manifest_blocked")
    if chunk_manifest.get("blocked"):
        blocked_reasons.append("chunk_manifest_blocked")

    return {
        "validator": "rag_index_manifest_validator",
        "status": "blocked" if blocked_reasons else "passed",
        "index_commit_sha": index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha"),
        "check_current_worktree": check_current,
        "indexed_chunk_count": index_chunk_count,
        "chunk_manifest_count": chunk_count,
        "missing_metadata": missing_metadata[:50],
        "stale_files": stale_files[:50],
        "deleted_files": deleted_files[:50],
        "blocked_reasons": blocked_reasons,
    }


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Validate RAG index manifest metadata.")
    parser.add_argument("--index-manifest", default=str(common.INDEX_MANIFEST_PATH))
    parser.add_argument("--chunk-manifest", default=str(common.CHUNK_MANIFEST_PATH))
    parser.add_argument("--check-current-worktree", action="store_true")
    args = parser.parse_args()

    index_path = _resolve(args.index_manifest, common.INDEX_MANIFEST_PATH)
    chunk_path = _resolve(args.chunk_manifest, common.CHUNK_MANIFEST_PATH)
    if not index_path.exists():
        raise SystemExit("blocked_index_manifest_missing")
    if not chunk_path.exists():
        raise SystemExit("blocked_chunk_manifest_missing")
    report = validate(common.read_json(index_path), common.read_json(chunk_path), args.check_current_worktree)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
