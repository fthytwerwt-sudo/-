#!/usr/bin/env python3
"""Validate delta sync checkpoint fixtures and generated checkpoints."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "checkpoint"
REPORT_PATH = common.ROOT / "codex_log" / "rag_decision_engine" / "latest_rag_delta_checkpoint_validator_report.json"
REQUIRED_FIELDS = [
    "run_id",
    "source_commit_sha",
    "previous_index_commit_sha",
    "delta_manifest_hash",
    "batch_manifest_hash",
    "completed_batch_indexes",
    "completed_chunk_ids",
    "failed_batch_indexes",
    "in_progress_batch_index",
    "resume_cursor",
    "last_success_at",
    "last_failure_at",
    "external_call_report",
    "key_printed",
    "key_written",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            reasons.append(f"{field}_missing")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    completed_batches = data.get("completed_batch_indexes")
    completed_chunks = data.get("completed_chunk_ids")
    failed_batches = data.get("failed_batch_indexes")
    if not isinstance(completed_batches, list):
        reasons.append("completed_batch_indexes_not_list")
    if not isinstance(completed_chunks, list):
        reasons.append("completed_chunk_ids_not_list")
    if not isinstance(failed_batches, list):
        reasons.append("failed_batch_indexes_not_list")
    if isinstance(completed_batches, list) and len(completed_batches) != len(set(completed_batches)):
        reasons.append("duplicate_completed_batch_indexes")
    if isinstance(completed_chunks, list) and len(completed_chunks) != len(set(completed_chunks)):
        reasons.append("duplicate_completed_chunk_ids")
    if data.get("expected_delta_manifest_hash") and data.get("delta_manifest_hash") != data.get("expected_delta_manifest_hash"):
        reasons.append("delta_manifest_hash_mismatch")
    if data.get("expected_batch_manifest_hash") and data.get("batch_manifest_hash") != data.get("expected_batch_manifest_hash"):
        reasons.append("batch_manifest_hash_mismatch")
    if data.get("resume_should_skip_completed_batches") and not data.get("skipped_completed_batch_indexes"):
        reasons.append("resume_skipped_completed_batches_missing")
    external = data.get("external_call_report", {})
    if external.get("key_printed") is not False:
        reasons.append("external_key_printed_not_false")
    if external.get("key_written") is not False:
        reasons.append("external_key_written_not_false")
    if external.get("vector_values_written") is not False:
        reasons.append("external_vector_values_written_not_false")
    return sorted(set(reasons))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate delta sync checkpoints.")
    parser.add_argument("--fixture", help="Single fixture or generated checkpoint path.")
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
        "validator": "rag_delta_checkpoint_validator",
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
