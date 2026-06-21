#!/usr/bin/env python3
"""Validate RAG vector maintenance router fixtures and generated decision."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common
import rag_vector_maintenance_router as router


FIXTURE_DIR = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine" / "maintenance_router"
REPORT_PATH = common.ROOT / "codex_log" / "rag_decision_engine" / "latest_rag_vector_maintenance_router_validator_report.json"
REQUIRED_TOP_FIELDS = [
    "task_context",
    "vector_health",
    "sync_health",
    "retrieval_health",
    "expected_action_id",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate_fixture(data: dict[str, Any]) -> tuple[str, list[str], dict[str, Any]]:
    reasons: list[str] = []
    for field in REQUIRED_TOP_FIELDS:
        if field not in data:
            reasons.append(f"{field}_missing")
    expected = data.get("expected_action_id")
    decision = router.build_decision(data, dry_run=True)
    actual = decision["selected_action"]["action_id"]
    if actual != expected:
        reasons.append(f"action_mismatch:{actual}!={expected}")
    if decision.get("current_RAG_index_latest_claim") is not False:
        reasons.append("current_RAG_index_latest_claim_not_false")
    external = decision.get("external_call_report", {})
    for key in ("alibaba_embedding_api_called", "dashvector_query_called", "dashvector_upsert_called", "dashvector_delete_called"):
        if external.get(key) is not False:
            reasons.append(f"{key}_not_false")
    if not decision["selected_action"].get("action_label"):
        reasons.append("action_label_missing")
    if "next_script_to_run" not in decision["selected_action"]:
        reasons.append("next_script_to_run_missing")
    return actual, sorted(set(reasons)), decision


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate RAG vector maintenance router fixtures.")
    parser.add_argument("--fixture", help="Single fixture path.")
    parser.add_argument("--fixture-dir", default=str(FIXTURE_DIR))
    parser.add_argument("--report", default=str(REPORT_PATH))
    args = parser.parse_args()

    paths = [_resolve(args.fixture)] if args.fixture else sorted(_resolve(args.fixture_dir).glob("*.json"))
    results: list[dict[str, Any]] = []
    mismatches: list[str] = []
    for path in paths:
        data = common.read_json(path)
        actual, reasons, decision = validate_fixture(data)
        status = "blocked" if reasons else "passed"
        if reasons:
            mismatches.append(path.as_posix())
        results.append(
            {
                "fixture_path": path.as_posix(),
                "case_id": data.get("case_id"),
                "expected_action_id": data.get("expected_action_id"),
                "actual_action_id": actual,
                "actual_status": status,
                "blocked_reasons": reasons,
                "next_script_to_run": decision["selected_action"].get("next_script_to_run", ""),
            }
        )
    report = {
        "validator": "rag_vector_maintenance_router_validator",
        "generated_at": common.now_iso(),
        "fixture_count": len(paths),
        "expected_mismatches": mismatches,
        "results": results,
        "status": "passed" if paths and not mismatches else "blocked",
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(_resolve(args.report), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
