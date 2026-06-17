#!/usr/bin/env python3
"""Validate report, trace, and latest-log completion evidence."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "schemas"
FIXTURE_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "fixtures"
LATEST = REPO_ROOT / "codex_log" / "latest.md"


class ProbeFailure(AssertionError):
    """Raised when report/trace/log evidence is incomplete or unsafe."""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ProbeFailure(f"missing file: {path.relative_to(REPO_ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ProbeFailure(f"not a mapping: {path.relative_to(REPO_ROOT)}")
    return data


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise ProbeFailure(message)


def validate_schemas() -> dict[str, Any]:
    report = load_yaml(SCHEMA_ROOT / "report_contract.schema.yaml")
    trace = load_yaml(SCHEMA_ROOT / "trace_event.schema.yaml")
    expect("validation_result（验证结果）" in report["required_fields（必填字段）"], "report requires validation_result")
    expect("source_path（来源路径）" in trace["required_fields（必填字段）"], "trace requires source_path")
    return {"status": "passed", "schema_count": 2}


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "passing" / "report_trace_log.passing.yaml")
    report = fixture["report_contract（报告契约）"]
    trace = fixture["trace_event（追踪事件）"]
    for key in (
        "files_read（已读取文件）",
        "files_modified（已修改文件）",
        "validation_result（验证结果）",
        "status_not_promoted（未推进状态）",
        "next_safe_step（下一步安全动作）",
    ):
        expect(bool(report.get(key)), f"report missing {key}")
    expect(bool(trace.get("source_path（来源路径）")), "trace source_path required")
    expect(bool(trace.get("report_path（报告路径）")), "trace report_path required")
    status = report["status_not_promoted（未推进状态）"]
    expect(status["runtime_enabled（运行时启用）"] is False, "runtime must remain false")
    return {"status": "passed"}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "blocked" / "report_trace_log.blocked.yaml")
    reasons = set(fixture.get("blocked_reasons", []))
    required = {
        "completed_without_validation_result",
        "report_missing_status_boundary",
        "trace_missing_source_path",
        "latest_runtime_enabled_miswritten",
        "local_only_claimed_as_pushed",
    }
    expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
    trace = fixture["trace_event（追踪事件）"]
    expect(not trace.get("source_path（来源路径）"), "blocked trace should miss source_path")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def validate_latest_top_section() -> dict[str, Any]:
    text = LATEST.read_text(encoding="utf-8")
    top = text.split("\n## 20260617", 1)[0]
    forbidden_patterns = [
        r"runtime_enabled[^\\n]*true",
        r"service_started[^\\n]*true",
        r"external_api_called[^\\n]*true",
        r"tts_called[^\\n]*true",
        r"dashvector_real_call[^\\n]*true",
        r"chroma_ingestion_run[^\\n]*true",
        r"media_generated[^\\n]*true",
        r"content_validation[^\\n]*passed",
        r"send_ready[^\\n]*true",
        r"production_readiness[^\\n]*ready",
    ]
    hits: list[str] = []
    for pattern in forbidden_patterns:
        hits.extend(match.group(0) for match in re.finditer(pattern, top, flags=re.IGNORECASE))
    expect(not hits, f"latest top section has forbidden status promotion: {hits}")
    return {"status": "passed", "scanned": "latest_top_section"}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "report_trace_log_validator",
        "runtime_enabled": False,
        "service_started": False,
        "external_api_called": False,
        "media_generated": False,
    }
    try:
        result["schema_result"] = validate_schemas()
        result["passing_fixture_result"] = validate_passing_fixture()
        result["blocked_fixture_result"] = validate_blocked_fixture()
        result["latest_top_section_result"] = validate_latest_top_section()
        result["final_probe_status"] = "passed"
    except ProbeFailure as exc:
        result["final_probe_status"] = "failed"
        result["failure"] = str(exc)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
