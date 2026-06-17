#!/usr/bin/env python3
"""Validate State / Node / Edge no-service contract fixtures."""

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
    """Raised when State / Node / Edge fixtures violate no-service rules."""


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


def validate_schema() -> dict[str, Any]:
    schema = load_yaml(SCHEMA_ROOT / "state_node_edge_contract.schema.yaml")
    hard = schema["hard_rules（硬规则）"]
    for key in (
        "no_langgraph_install_required（不需要安装 LangGraph）",
        "service_start_forbidden（禁止启动服务）",
        "graph_cannot_replace_project_router（图不能替代项目状态动作总控器）",
        "node_failure_cannot_promote_status（节点失败不能推进状态）",
        "human_required_edge_must_interrupt（需要用户确认的边必须中断）",
    ):
        expect(hard.get(key) is True, f"missing hard rule: {key}")
    return {"status": "passed"}


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "passing" / "state_node_edge.passing.yaml")
    expect(fixture["case_type（样例类型）"] == "passing", "passing fixture type mismatch")
    for node in fixture["nodes（节点）"]:
        for key in (
            "input（输入）",
            "output（输出）",
            "validation（验证）",
            "blocked_if（阻断条件）",
            "fallback_layer（失败回退层）",
            "trace_fields（追踪字段）",
        ):
            expect(bool(node.get(key)), f"{node.get('node_id（节点编号）')}: missing {key}")
    for edge in fixture["edges（边）"]:
        expect(edge.get("transition_condition（流转条件）"), "edge transition condition required")
        expect(edge.get("blocked_transition_if（禁止流转条件）"), "edge blocked transition required")
        if edge.get("human_review_required_if（需要人工复审的条件）"):
            expect(edge["to_node（目标节点）"] == "human_gate_node", "human-required edge must interrupt")
    expect(fixture["hard_boundaries（硬边界）"]["service_started（服务启动）"] is False, "service must remain false")
    return {"status": "passed", "node_count": len(fixture["nodes（节点）"])}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "blocked" / "state_node_edge.blocked.yaml")
    reasons = set(fixture.get("blocked_reasons", []))
    required = {
        "node_missing_input_output_validation",
        "node_failure_promoted_status",
        "human_required_edge_without_interrupt",
    }
    expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
    edge = fixture["edges（边）"][0]
    expect(edge.get("human_interrupt_created（是否创建人工中断）") is False, "blocked fixture must show missing interrupt")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "state_node_edge_no_service_probe",
        "service_started": False,
        "external_api_called": False,
        "dependency_installed": False,
        "runtime_enabled": False,
    }
    try:
        result["schema_result"] = validate_schema()
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
