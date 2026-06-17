#!/usr/bin/env python3
"""Validate evaluator, failure route, human gate, and guardrail fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "schemas"
FIXTURE_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "fixtures"


class ProbeFailure(AssertionError):
    """Raised when evaluator/failure/guardrail rules are unsafe."""


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
    for filename in (
        "evaluator_result.schema.yaml",
        "failure_route.schema.yaml",
        "human_decision_gate.schema.yaml",
        "guardrail_result.schema.yaml",
    ):
        schema = load_yaml(SCHEMA_ROOT / filename)
        expect(schema.get("project_route") == "video_factory（视频工厂）", f"{filename}: wrong project route")
    guard = load_yaml(SCHEMA_ROOT / "guardrail_result.schema.yaml")
    expect(guard["hard_rules（硬规则）"]["git_add_dot_forbidden（禁止 git add . 全量暂存）"] is True, "git add dot must be forbidden")
    return {"status": "passed", "schema_count": 4}


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "passing" / "evaluator_failure_guardrail.passing.yaml")
    evaluator = fixture["evaluator_result（评估结果）"]
    human = fixture["human_decision_gate（人工决策闸门）"]
    guard = fixture["guardrail_result（护栏结果）"]
    expect(evaluator["content_validation（内容验证）"] == "not_promoted", "content validation must not be promoted")
    expect(evaluator["send_ready（可发送状态）"] is False, "send_ready must remain false")
    expect(evaluator["production_readiness（生产可用状态）"] == "not_claimed", "production readiness not claimed")
    expect(human["required_user_confirmation（是否必须用户确认）"] is False, "passing fixture should not require user")
    expect(guard["triggered（是否触发）"] is False, "guardrail should not be triggered")
    return {"status": "passed"}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "blocked" / "evaluator_failure_guardrail.blocked.yaml")
    reasons = set(fixture.get("blocked_reasons", []))
    required = {
        "technical_validation_claimed_as_content",
        "content_validation_auto_promotes_send_ready",
        "human_required_but_auto_passed",
        "degraded_plan_without_user_confirmation",
        "guardrail_triggered_but_completed",
        "secret_scan_bypassed",
        "git_add_dot_attempted",
    }
    expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
    human = fixture["human_decision_gate（人工决策闸门）"]
    guard = fixture["guardrail_result（护栏结果）"]
    expect(human["required_user_confirmation（是否必须用户确认）"] is True, "human confirmation required")
    expect(human["auto_pass_allowed（是否允许自动通过）"] is True, "blocked fixture should expose unsafe auto-pass")
    expect(guard["triggered（是否触发）"] is True, "blocked guardrail should trigger")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "evaluator_failure_guardrail_probe",
        "runtime_enabled": False,
        "service_started": False,
        "external_api_called": False,
        "content_validation": "not_promoted",
        "send_ready": False,
    }
    try:
        result["schema_result"] = validate_schemas()
        result["passing_fixture_result"] = validate_passing_fixture()
        result["blocked_fixture_result"] = validate_blocked_fixture()
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
