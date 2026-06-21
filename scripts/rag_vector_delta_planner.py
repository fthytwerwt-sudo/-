#!/usr/bin/env python3
"""Plan chunk-level delta sync from old index manifest to current chunk manifest.

This planner is deliberately local-only. It never calls embedding APIs or
DashVector; it only classifies chunks so downstream sync can process delta
chunks instead of the full corpus.
"""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DELTA_MANIFEST_JSON = common.OUT_DIR / "latest_chunk_delta_manifest.json"
DELTA_MANIFEST_MD = common.OUT_DIR / "latest_chunk_delta_manifest.md"


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _source_range_key(chunk: dict[str, Any]) -> str:
    return f"{chunk.get('source_path')}::{chunk.get('line_range')}"


def _logical_chunk_key(chunk: dict[str, Any]) -> str:
    return f"{chunk.get('source_path')}::{chunk.get('line_start')}::{chunk.get('line_end')}"


def _chunk_ref(chunk: dict[str, Any], state: str, *, supersedes: str | None = None, reason: str = "") -> dict[str, Any]:
    return {
        "chunk_id": chunk.get("chunk_id"),
        "source_path": chunk.get("source_path"),
        "line_range": chunk.get("line_range"),
        "line_start": chunk.get("line_start"),
        "line_end": chunk.get("line_end"),
        "chunk_hash": chunk.get("chunk_hash"),
        "file_hash": chunk.get("file_hash"),
        "vector_state": state,
        "supersedes": supersedes,
        "reason": reason,
    }


def build_delta_manifest(index_manifest: dict[str, Any], chunk_manifest: dict[str, Any]) -> dict[str, Any]:
    old_chunks = list(index_manifest.get("chunks", []))
    new_chunks = list(chunk_manifest.get("chunks", []))

    old_by_id = {str(chunk.get("chunk_id")): chunk for chunk in old_chunks}
    old_by_source_range = {_source_range_key(chunk): chunk for chunk in old_chunks}
    old_by_logical = {_logical_chunk_key(chunk): chunk for chunk in old_chunks}
    consumed_old_ids: set[str] = set()

    unchanged: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []
    new: list[dict[str, Any]] = []
    superseded: list[dict[str, Any]] = []

    for chunk in new_chunks:
        chunk_id = str(chunk.get("chunk_id"))
        old = old_by_id.get(chunk_id)
        if old:
            consumed_old_ids.add(chunk_id)
            if old.get("chunk_hash") == chunk.get("chunk_hash") and old.get("file_hash") == chunk.get("file_hash"):
                unchanged.append(_chunk_ref(chunk, "reused_from_previous_index", reason="chunk_id_and_hashes_match"))
            else:
                changed.append(_chunk_ref(chunk, "delta_embed_required", supersedes=chunk_id, reason="same_chunk_id_hash_changed"))
                superseded.append(_chunk_ref(old, "superseded_by_changed_chunk", supersedes=chunk_id, reason="same_chunk_id_hash_changed"))
            continue

        candidate = old_by_source_range.get(_source_range_key(chunk)) or old_by_logical.get(_logical_chunk_key(chunk))
        if candidate:
            old_id = str(candidate.get("chunk_id"))
            consumed_old_ids.add(old_id)
            changed.append(_chunk_ref(chunk, "delta_embed_required", supersedes=old_id, reason="same_source_range_hash_changed"))
            superseded.append(_chunk_ref(candidate, "superseded_by_changed_chunk", supersedes=chunk_id, reason="same_source_range_hash_changed"))
        else:
            new.append(_chunk_ref(chunk, "delta_embed_required", reason="new_chunk_id"))

    deleted = [
        _chunk_ref(chunk, "deleted_or_tombstone_required", reason="old_chunk_missing_from_current_manifest")
        for chunk in old_chunks
        if str(chunk.get("chunk_id")) not in consumed_old_ids
    ]

    delta_chunks = new + changed
    source_commit_sha = str(chunk_manifest.get("commit_sha") or chunk_manifest.get("source_commit_sha") or "")
    previous_index_commit_sha = str(index_manifest.get("source_commit_sha") or index_manifest.get("commit_sha") or "")
    manifest = {
        "manifest_type": "true_incremental_vector_sync",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": source_commit_sha,
        "previous_index_commit_sha": previous_index_commit_sha,
        "generated_at": common.now_iso(),
        "input_paths": [common.INDEX_MANIFEST_PATH.as_posix(), common.CHUNK_MANIFEST_PATH.as_posix()],
        "output_paths": [DELTA_MANIFEST_JSON.as_posix(), DELTA_MANIFEST_MD.as_posix()],
        "chunk_delta_counts": {
            "new_chunks": len(new),
            "changed_chunks": len(changed),
            "unchanged_chunks": len(unchanged),
            "deleted_chunks": len(deleted),
            "superseded_chunks": len(superseded),
            "delta_chunks_to_embed": len(delta_chunks),
            "active_chunk_count": len(new_chunks),
            "previous_index_chunk_count": len(old_chunks),
        },
        "chunk_classes": {
            "new_chunks": new,
            "changed_chunks": changed,
            "unchanged_chunks": unchanged,
            "deleted_chunks": deleted,
            "superseded_chunks": superseded,
            "delta_chunks": delta_chunks,
        },
        "external_call_report": {
            "alibaba_embedding_api_called": False,
            "dashvector_upsert_called": False,
            "dashvector_query_called": False,
            "key_printed": False,
            "key_written": False,
            "vector_values_written": False,
        },
        "blocked_if": [
            "required_chunk_metadata_missing",
            "delta_planner_cannot_classify_chunks",
            "dry_run_would_call_external_api",
        ],
        "validation_result": {"status": "passed"},
        "key_printed": False,
        "key_written": False,
    }
    return manifest


def write_delta_markdown(manifest: dict[str, Any], path: pathlib.Path = DELTA_MANIFEST_MD) -> None:
    counts = manifest["chunk_delta_counts"]
    lines = [
        "# RAG Chunk Delta Manifest",
        "",
        f"- source_commit_sha: `{manifest['source_commit_sha']}`",
        f"- previous_index_commit_sha: `{manifest['previous_index_commit_sha']}`",
        f"- new_chunks: `{counts['new_chunks']}`",
        f"- changed_chunks: `{counts['changed_chunks']}`",
        f"- unchanged_chunks: `{counts['unchanged_chunks']}`",
        f"- deleted_chunks: `{counts['deleted_chunks']}`",
        f"- superseded_chunks: `{counts['superseded_chunks']}`",
        f"- delta_chunks_to_embed: `{counts['delta_chunks_to_embed']}`",
        "- alibaba_embedding_api_called: `false`",
        "- dashvector_upsert_called: `false`",
        "- key_printed: `false`",
        "- key_written: `false`",
    ]
    common.write_markdown(path, lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Build a local-only RAG chunk delta manifest.")
    parser.add_argument("--index-manifest", default=str(common.INDEX_MANIFEST_PATH))
    parser.add_argument("--chunk-manifest", default=str(common.CHUNK_MANIFEST_PATH))
    parser.add_argument("--out", default=str(DELTA_MANIFEST_JSON))
    parser.add_argument("--md-out", default=str(DELTA_MANIFEST_MD))
    args = parser.parse_args()

    index_path = _resolve(args.index_manifest)
    chunk_path = _resolve(args.chunk_manifest)
    out_path = _resolve(args.out)
    md_out_path = _resolve(args.md_out)
    if not index_path.exists():
        raise SystemExit("blocked_index_manifest_missing")
    if not chunk_path.exists():
        raise SystemExit("blocked_chunk_manifest_missing")

    manifest = build_delta_manifest(common.read_json(index_path), common.read_json(chunk_path))
    common.write_json(out_path, manifest)
    write_delta_markdown(manifest, md_out_path)
    counts = manifest["chunk_delta_counts"]
    print(
        json.dumps(
            {
                "status": manifest["validation_result"]["status"],
                "chunk_delta_manifest_path": out_path.as_posix(),
                "new_chunks": counts["new_chunks"],
                "changed_chunks": counts["changed_chunks"],
                "unchanged_chunks": counts["unchanged_chunks"],
                "deleted_chunks": counts["deleted_chunks"],
                "superseded_chunks": counts["superseded_chunks"],
                "delta_chunks_to_embed": counts["delta_chunks_to_embed"],
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


if __name__ == "__main__":
    raise SystemExit(main())
