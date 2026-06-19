#!/usr/bin/env python3
"""Guard whether the DashVector index manifest is current enough to supply RAG."""

from __future__ import annotations

import json

import rag_common as common


def main() -> int:
    common.main_guard()
    if not common.INDEX_MANIFEST_PATH.exists():
        raise SystemExit("blocked_index_manifest_missing")
    manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    indexed_by_path = {item["source_path"]: item for item in manifest.get("indexed_files", [])}
    stale_files: list[dict[str, str]] = []
    deleted_files: list[str] = []
    for source_path, item in indexed_by_path.items():
        path = common.ROOT / source_path
        if not path.exists():
            deleted_files.append(source_path)
            continue
        current_hash = common.sha256_file(path)
        if current_hash != item["file_hash"]:
            stale_files.append(
                {"source_path": source_path, "expected_file_hash": item["file_hash"], "current_file_hash": current_hash}
            )
    dirty_safe = common.has_only_allowed_dirty_paths()
    status = {
        "guard_name": "rag_sync_guard",
        "project_route": common.PROJECT_ROUTE,
        "index_manifest_path": common.INDEX_MANIFEST_PATH.as_posix(),
        "index_commit_sha": manifest.get("source_commit_sha") or manifest.get("commit_sha"),
        "current_head_sha": common.current_commit(),
        "dynamic_audit_artifacts_excluded_from_stale_check": list(common.DYNAMIC_AUDIT_PREFIXES),
        "stale_files": stale_files,
        "deleted_files": deleted_files,
        "dirty_files_not_indexed_to_formal_store": True,
        "only_dynamic_or_public_dirty_paths": dirty_safe,
        "stale_index_check": not stale_files and not deleted_files and dirty_safe and not manifest.get("blocked", True),
        "blocked_reasons": [],
    }
    if stale_files:
        status["blocked_reasons"].append("stale_index_detected")
    if deleted_files:
        status["blocked_reasons"].append("deleted_file_still_indexed")
    if not dirty_safe:
        status["blocked_reasons"].append("dirty_files_may_affect_indexed_sources")
    if manifest.get("blocked", True):
        status["blocked_reasons"].append("index_manifest_blocked")
    common.write_json(common.OUT_DIR / "latest_sync_guard_report.json", status)
    print(json.dumps(status, ensure_ascii=False, sort_keys=True))
    return 0 if status["stale_index_check"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
