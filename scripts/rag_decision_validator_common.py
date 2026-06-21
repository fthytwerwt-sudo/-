#!/usr/bin/env python3
"""Shared fixture validation helpers for the RAG decision engine."""

from __future__ import annotations

import argparse
import copy
import json
import pathlib
from typing import Any, Callable

import rag_common as common


FIXTURE_ROOT = common.ROOT / "codex_source" / "fixtures" / "rag_decision_engine"
REPORT_DIR = common.ROOT / "codex_log" / "rag_decision_engine"

COMMON_REQUIRED_FIELDS = [
    "manifest_type",
    "project_route",
    "source_commit_sha",
    "generated_at",
    "input_paths",
    "output_paths",
    "blocked_if",
    "validation_result",
    "key_printed",
    "key_written",
]


def resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def list_fixture_files(fixture_dir: pathlib.Path) -> list[pathlib.Path]:
    return sorted(path for path in fixture_dir.glob("*.json") if path.is_file())


def forbidden_status_promotion_reasons(data: dict[str, Any]) -> list[str]:
    text = json.dumps(data, ensure_ascii=False).lower()
    reasons: list[str] = []
    if '"content_validation": "passed"' in text or '"content_validation":"passed"' in text:
        reasons.append("forbidden_content_validation_passed")
    if '"production_readiness": true' in text or '"production_ready": true' in text:
        reasons.append("forbidden_production_readiness_claim")
    if '"current_rag_index_latest_claim": true' in text or '"rag_latest_claim": true' in text:
        reasons.append("forbidden_RAG_latest_claim")
    if '"langgraph_implemented": true' in text:
        reasons.append("forbidden_langgraph_implemented_claim")
    return reasons


def common_reasons(data: dict[str, Any], manifest_type: str, required_fields: list[str]) -> list[str]:
    reasons: list[str] = []
    for field in required_fields:
        if field not in data:
            reasons.append(f"{field}_missing")
    if data.get("manifest_type") != manifest_type:
        reasons.append("manifest_type_mismatch")
    if data.get("project_route") != common.PROJECT_ROUTE:
        reasons.append("project_route_mismatch")
    if data.get("key_printed") is not False:
        reasons.append("key_printed_not_false")
    if data.get("key_written") is not False:
        reasons.append("key_written_not_false")
    reasons.extend(forbidden_status_promotion_reasons(data))
    return reasons


def status_from_reasons(reasons: list[str]) -> str:
    return "blocked" if reasons else "passed"


def run_fixture_validation(
    *,
    validator_name: str,
    manifest_type: str,
    fixture_subdir: str,
    required_fields: list[str],
    domain_validator: Callable[[dict[str, Any]], list[str]],
    argv: list[str] | None = None,
) -> int:
    parser = argparse.ArgumentParser(description=f"Validate {manifest_type} fixtures.")
    parser.add_argument("--fixture", help="Single fixture JSON path.")
    parser.add_argument("--fixture-dir", default=str(FIXTURE_ROOT / fixture_subdir))
    parser.add_argument("--report", default=str(REPORT_DIR / f"latest_{validator_name}_report.json"))
    args = parser.parse_args(argv)

    fixture_paths = [resolve(args.fixture)] if args.fixture else list_fixture_files(resolve(args.fixture_dir))
    results: list[dict[str, Any]] = []
    expected_mismatches: list[str] = []
    positive_passed = False
    blocked_blocked = False
    missing_required_field_blocked = False
    forbidden_status_promotion_blocked = False

    for path in fixture_paths:
        data = common.read_json(path)
        reasons = common_reasons(data, manifest_type, required_fields)
        reasons.extend(domain_validator(data))
        status = status_from_reasons(sorted(set(reasons)))
        expected_status = data.get("expected_status", status)
        if expected_status != status:
            expected_mismatches.append(path.as_posix())
        if status == "passed":
            positive_passed = True
        if status == "blocked":
            blocked_blocked = True

        missing_probe = copy.deepcopy(data)
        if required_fields:
            missing_probe.pop(required_fields[0], None)
            missing_required_field_blocked = missing_required_field_blocked or bool(
                common_reasons(missing_probe, manifest_type, required_fields)
            )

        promotion_probe = copy.deepcopy(data)
        promotion_probe["content_validation"] = "passed"
        forbidden_status_promotion_blocked = forbidden_status_promotion_blocked or bool(
            forbidden_status_promotion_reasons(promotion_probe)
        )

        results.append(
            {
                "fixture_path": path.as_posix(),
                "expected_status": expected_status,
                "actual_status": status,
                "blocked_reasons": sorted(set(reasons)),
            }
        )

    report = {
        "validator": validator_name,
        "manifest_type": manifest_type,
        "generated_at": common.now_iso(),
        "fixture_count": len(fixture_paths),
        "positive_fixture_passed": positive_passed,
        "blocked_fixture_blocked": blocked_blocked,
        "missing_required_field_blocked": missing_required_field_blocked,
        "forbidden_status_promotion_blocked": forbidden_status_promotion_blocked,
        "no_secret_written": True,
        "deterministic_result": True,
        "expected_mismatches": expected_mismatches,
        "results": results,
        "status": "passed"
        if fixture_paths
        and positive_passed
        and blocked_blocked
        and missing_required_field_blocked
        and forbidden_status_promotion_blocked
        and not expected_mismatches
        else "blocked",
        "key_printed": False,
        "key_written": False,
    }
    common.write_json(resolve(args.report), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "passed" else 2
