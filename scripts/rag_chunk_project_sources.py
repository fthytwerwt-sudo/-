#!/usr/bin/env python3
"""Chunk allowlisted Video Factory RAG source files with line metadata."""

from __future__ import annotations

import json

import rag_common as common


def write_markdown_report(manifest: dict) -> None:
    lines = [
        "# RAG Chunk Manifest",
        "",
        f"- project_route: `{manifest['project_route']}`",
        f"- branch: `{manifest['branch']}`",
        f"- commit_sha: `{manifest['commit_sha']}`",
        f"- file_count: `{manifest['file_count']}`",
        f"- chunk_count: `{manifest['chunk_count']}`",
        f"- chunk_manifest_valid: `{str(manifest['chunk_manifest_valid']).lower()}`",
        "",
        "## Sample Chunks",
        "",
    ]
    for item in manifest["chunks"][:30]:
        lines.append(
            f"- `{item['chunk_id']}` `{item['source_path']}:{item['line_range']}`"
        )
    common.write_markdown(common.OUT_DIR / "latest_chunk_manifest.md", lines)


def main() -> int:
    common.main_guard()
    if not common.SOURCE_INVENTORY_PATH.exists():
        raise SystemExit("blocked_source_inventory_missing")
    inventory = common.read_json(common.SOURCE_INVENTORY_PATH)
    manifest = common.build_chunks(inventory)
    common.write_json(common.CHUNK_MANIFEST_PATH, manifest)
    write_markdown_report(manifest)
    print(
        json.dumps(
            {
                "status": "passed" if not manifest["blocked"] else "blocked",
                "chunk_manifest_path": common.CHUNK_MANIFEST_PATH.as_posix(),
                "file_count": manifest["file_count"],
                "chunk_count": manifest["chunk_count"],
                "chunk_manifest_valid": manifest["chunk_manifest_valid"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if not manifest["blocked"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
