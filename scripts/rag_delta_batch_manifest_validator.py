#!/usr/bin/env python3
"""Validate delta batch manifest fixtures and generated reports."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "batch_manifest"
REPORT_PATH = common.ROOT / "codex_log" / "rag_decision_engine" / "latest_rag_delta_batch_manifest_validator_report.json"
ALLOWED_BATCH_SIZES = {4, 8, 16, 32}
REQUIRED_FIELDS = [
    "manifest_type",
    "project_route",
    "repo_full_name",
    "source_commit_sha",
    "previous_index_commit_sha",
    "delta_manifest_hash",
    "batch_size",
    "batch_count",
    "total_delta_chunk_count",
    "batches",
    "key_printed",
    "key_written",
    "vector_values_written",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            reasons.append(f"{field}_missing")
    if data.get("manifest_type") != "delta_batch_manifest":
        reasons.append("manifest_type_mismatch")
    if data.get("project_route") != common.PROJECT_ROUTE:
        reasons.append("project_route_mismatch")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    if data.get("vector_values_written") is not False:
        reasons.append("vector_values_written_not_false")
    batch_size = data.get("batch_size")
    if batch_size not in ALLOWED_BATCH_SIZES:
        reasons.append("batch_size_not_allowed")
    batches = data.get("batches")
    if not isinstance(batches, list) or not batches:
        reasons.append("batches_missing")
        return reasons
    if data.get("batch_count") != len(batches):
        reasons.append("batch_count_mismatch")
    total = 0
    for index, batch in enumerate(batches):
        if batch.get("batch_index") != index:
            reasons.append("batch_index_sequence_mismatch")
        if not batch.get("batch_id"):
            reasons.append("batch_id_missing")
        chunk_ids = batch.get("chunk_ids")
        if not isinstance(chunk_ids, list) or not chunk_ids:
            reasons.append("chunk_ids_missing")
        if batch.get("chunk_count") != len(chunk_ids or []):
            reasons.append("chunk_count_mismatch")
        if batch.get("status") != "pending":
            reasons.append("initial_batch_status_not_pending")
        if not isinstance(batch.get("source_paths"), list) or not batch.get("source_paths"):
            reasons.append("source_paths_missing")
        total += int(batch.get("chunk_count") or 0)
    if data.get("total_delta_chunk_count") != total:
        reasons.append("total_delta_chunk_count_mismatch")
    external = data.get("external_call_report", {})
    if external.get("alibaba_embedding_api_called") is not False:
        reasons.append("alibaba_embedding_api_called_not_false")
    if external.get("dashvector_upsert_called") is not False:
        reasons.append("dashvector_upsert_called_not_false")
    return sorted(set(reasons))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate delta batch manifests.")
    parser.add_argument("--fixture", help="Single fixture or generated manifest path.")
    parser.add_argument("--fixture-dir", default=str(FIXTURE_DIR))
    parser.add_argument("--report", default=str(REPORT_PATH))
    args = parser.parse_args()

    paths = [_resolve(args.fixture)] if args.fixture else sorted(_resolve(args.fixture_dir).glob("*.json"))
    results: list[dict[str, Any]] = []
    mismatches: list[str] = []
    positive_passed = False
    blocked_blocked = False
    for path in paths:
        data = common.read_json(path)
        reasons = validate(data)
        status = "blocked" if reasons else "passed"
        expected = data.get("expected_status", status)
        if status != expected:
            mismatches.append(path.as_posix())
        positive_passed = positive_passed or status == "passed"
        blocked_blocked = blocked_blocked or status == "blocked"
        results.append({"fixture_path": path.as_posix(), "expected_status": expected, "actual_status": status, "blocked_reasons": reasons})
    single_fixture_mode = bool(args.fixture)
    report = {
        "validator": "rag_delta_batch_manifest_validator",
        "generated_at": common.now_iso(),
        "fixture_count": len(paths),
        "positive_fixture_passed": positive_passed,
        "blocked_fixture_blocked": blocked_blocked,
        "expected_mismatches": mismatches,
        "results": results,
        "status": "passed"
        if paths and positive_passed and not mismatches and (single_fixture_mode or blocked_blocked)
        else "blocked",
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(_resolve(args.report), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
