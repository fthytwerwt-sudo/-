#!/usr/bin/env python3
"""Validate delta index partial manifests and timeout fixtures."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "partial_manifest"
TIMEOUT_FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "timeout"
REPORT_PATH = common.ROOT / "codex_log" / "rag_decision_engine" / "latest_rag_delta_partial_manifest_validator_report.json"
REQUIRED_FIELDS = [
    "manifest_type",
    "project_route",
    "repo_full_name",
    "source_commit_sha",
    "status",
    "completed_batch_count",
    "completed_chunk_count",
    "failed_batch_count",
    "pending_batch_count",
    "final_index_manifest_written",
    "current_RAG_index_latest_claim",
    "key_printed",
    "key_written",
    "vector_values_written",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate_partial(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            reasons.append(f"{field}_missing")
    if data.get("manifest_type") != "delta_index_partial_manifest":
        reasons.append("manifest_type_mismatch")
    if data.get("status") not in {"partial", "blocked", "interrupted"}:
        reasons.append("status_not_partial_blocked_or_interrupted")
    if data.get("final_index_manifest_written") is not False:
        reasons.append("partial_manifest_wrote_final_index")
    if data.get("current_RAG_index_latest_claim") is not False:
        reasons.append("partial_manifest_claimed_RAG_latest")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    if data.get("vector_values_written") is not False:
        reasons.append("vector_values_written_not_false")
    for field in ("completed_batch_count", "completed_chunk_count", "failed_batch_count", "pending_batch_count"):
        if int(data.get(field, -1)) < 0:
            reasons.append(f"{field}_negative")
    return sorted(set(reasons))


def validate_timeout(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if data.get("manifest_type") != "delta_sync_timeout_report":
        reasons.append("manifest_type_mismatch")
    if data.get("stage") not in {"embedding", "upsert"}:
        reasons.append("stage_not_embedding_or_upsert")
    if data.get("blocked_reason") != "blocked_batch_timeout":
        reasons.append("blocked_reason_not_timeout")
    if int(data.get("batch_index", -1)) < 0:
        reasons.append("batch_index_negative")
    if float(data.get("elapsed_seconds", -1)) < 0:
        reasons.append("elapsed_seconds_negative")
    if not data.get("batch_id"):
        reasons.append("batch_id_missing")
    if not data.get("chunk_ids"):
        reasons.append("chunk_ids_missing")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    if data.get("vector_values_written") is not False:
        reasons.append("vector_values_written_not_false")
    return sorted(set(reasons))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate delta partial manifests and timeout reports.")
    parser.add_argument("--fixture", help="Single partial fixture or generated manifest path.")
    parser.add_argument("--fixture-dir", default=str(FIXTURE_DIR))
    parser.add_argument("--timeout-fixture-dir", default=str(TIMEOUT_FIXTURE_DIR))
    parser.add_argument("--report", default=str(REPORT_PATH))
    args = parser.parse_args()

    paths = [_resolve(args.fixture)] if args.fixture else sorted(_resolve(args.fixture_dir).glob("*.json"))
    timeout_paths = [] if args.fixture else sorted(_resolve(args.timeout_fixture_dir).glob("*.json"))
    results: list[dict[str, Any]] = []
    mismatches: list[str] = []
    positive_passed = False
    blocked_blocked = False
    timeout_cases_passed = True
    for path in paths:
        data = common.read_json(path)
        reasons = validate_partial(data)
        status = "blocked" if reasons else "passed"
        expected = data.get("expected_status", status)
        if status != expected:
            mismatches.append(path.as_posix())
        positive_passed = positive_passed or status == "passed"
        blocked_blocked = blocked_blocked or data.get("status") in {"blocked", "interrupted"}
        results.append({"fixture_path": path.as_posix(), "expected_status": expected, "actual_status": status, "blocked_reasons": reasons})
    for path in timeout_paths:
        data = common.read_json(path)
        reasons = validate_timeout(data)
        status = "blocked" if reasons else "passed"
        expected = data.get("expected_status", status)
        if status != expected:
            mismatches.append(path.as_posix())
        timeout_cases_passed = timeout_cases_passed and status == "passed"
        results.append({"fixture_path": path.as_posix(), "expected_status": expected, "actual_status": status, "blocked_reasons": reasons})
    single_fixture_mode = bool(args.fixture)
    report = {
        "validator": "rag_delta_partial_manifest_validator",
        "generated_at": common.now_iso(),
        "fixture_count": len(paths) + len(timeout_paths),
        "positive_fixture_passed": positive_passed,
        "blocked_or_interrupted_fixture_present": blocked_blocked,
        "timeout_cases_passed": timeout_cases_passed,
        "expected_mismatches": mismatches,
        "results": results,
        "status": "passed"
        if paths and positive_passed and not mismatches and (single_fixture_mode or (blocked_blocked and timeout_cases_passed))
        else "blocked",
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(_resolve(args.report), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
