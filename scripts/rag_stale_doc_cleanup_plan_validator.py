#!/usr/bin/env python3
"""Validate stale retrieval doc cleanup plan fixtures and generated reports."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "stale_doc_cleanup"
REPORT_PATH = common.ROOT / "codex_log" / "rag_decision_engine" / "latest_rag_stale_doc_cleanup_plan_validator_report.json"
REQUIRED_FIELDS = [
    "manifest_type",
    "project_route",
    "repo_full_name",
    "cleanup_mode",
    "stale_doc_count",
    "stale_docs",
    "delete_allowed",
    "physical_delete_executed",
    "tombstone_executed",
    "external_call_report",
    "key_printed",
    "key_written",
    "vector_values_written",
]
REQUIRED_DOC_FIELDS = [
    "stale_doc_id",
    "chunk_id",
    "source_path",
    "line_range",
    "first_seen_query",
    "raw_rank",
    "reason",
    "active_manifest_allowlist_passed",
    "readback_hash_match",
    "safe_to_delete_candidate",
    "delete_allowed",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            reasons.append(f"{field}_missing")
    if data.get("manifest_type") != "rag_retrieval_stale_doc_cleanup_plan":
        reasons.append("manifest_type_mismatch")
    if data.get("project_route") != common.PROJECT_ROUTE:
        reasons.append("project_route_mismatch")
    if data.get("cleanup_mode") != "dry_run_only":
        reasons.append("cleanup_mode_not_dry_run_only")
    stale_docs = data.get("stale_docs")
    if not isinstance(stale_docs, list):
        reasons.append("stale_docs_not_list")
        stale_docs = []
    if data.get("stale_doc_count") != len(stale_docs):
        reasons.append("stale_doc_count_mismatch")
    if data.get("physical_delete_executed") is not False:
        reasons.append("physical_delete_executed_not_false")
    if data.get("tombstone_executed") is not False:
        reasons.append("tombstone_executed_not_false")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    if data.get("vector_values_written") is not False:
        reasons.append("vector_values_written_not_false")
    external = data.get("external_call_report", {})
    for key in ("alibaba_embedding_api_called", "dashvector_query_called", "dashvector_upsert_called", "dashvector_delete_called"):
        if external.get(key) is not False:
            reasons.append(f"{key}_not_false")
    for index, item in enumerate(stale_docs):
        for field in REQUIRED_DOC_FIELDS:
            if field not in item:
                reasons.append(f"stale_doc_{index}_{field}_missing")
        if item.get("delete_executed") is not False:
            reasons.append(f"stale_doc_{index}_delete_executed_not_false")
        if item.get("tombstone_executed") is not False:
            reasons.append(f"stale_doc_{index}_tombstone_executed_not_false")
    return sorted(set(reasons))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate stale doc cleanup plans.")
    parser.add_argument("--fixture", help="Single fixture or generated cleanup plan path.")
    parser.add_argument("--fixture-dir", default=str(FIXTURE_DIR))
    parser.add_argument("--report", default=str(REPORT_PATH))
    args = parser.parse_args()

    paths = [_resolve(args.fixture)] if args.fixture else sorted(_resolve(args.fixture_dir).glob("*.json"))
    results: list[dict[str, Any]] = []
    mismatches: list[str] = []
    positive_passed = False
    for path in paths:
        data = common.read_json(path)
        reasons = validate(data)
        status = "blocked" if reasons else "passed"
        expected = data.get("expected_status", status)
        if status != expected:
            mismatches.append(path.as_posix())
        positive_passed = positive_passed or status == "passed"
        results.append({"fixture_path": path.as_posix(), "expected_status": expected, "actual_status": status, "blocked_reasons": reasons})
    report = {
        "validator": "rag_stale_doc_cleanup_plan_validator",
        "generated_at": common.now_iso(),
        "fixture_count": len(paths),
        "positive_fixture_passed": positive_passed,
        "expected_mismatches": mismatches,
        "results": results,
        "status": "passed" if paths and positive_passed and not mismatches else "blocked",
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(_resolve(args.report), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
