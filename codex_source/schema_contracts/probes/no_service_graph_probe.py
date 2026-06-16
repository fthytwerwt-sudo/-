#!/usr/bin/env python3
"""No-service graph probe for adapter contract fixtures.

This probe intentionally avoids service startup, external API calls, package
installs, vector-store ingestion, and repository writes. It reads frozen schema
contract fixtures and runs a small fake graph to prove adapter guardrails before
runtime code is allowed.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "fixtures"

PASSING_FIXTURES = {
    "graph_runtime_adapter": "passing/graph_runtime_adapter.passing.yaml",
    "cleaning_adapter": "passing/cleaning_adapter.passing.yaml",
    "retrieval_manifest": "passing/retrieval_manifest_dashvector_fixture.passing.yaml",
    "source_readback_map": "passing/source_readback_map.passing.yaml",
    "service_contract_no_write": "passing/service_contract_no_write.passing.yaml",
    "runtime_memory_boundary": "passing/runtime_memory_boundary.passing.yaml",
    "completion_truth_check": "passing/completion_truth_check.passing.yaml",
}

BLOCKED_CASES = {
    "graph_direct_write_blocked": {
        "fixture": "blocked/graph_runtime_adapter.blocked_runtime_write.yaml",
        "reason": "graph_attempted_direct_repo_write",
    },
    "graph_missing_source_readback_blocked": {
        "fixture": "blocked/graph_runtime_adapter.blocked_missing_source_readback.yaml",
        "reason": "missing_source_readback_required",
    },
    "retrieval_page_content_only_blocked": {
        "fixture": "blocked/retrieval_manifest_page_content_only.blocked.yaml",
        "reason": "page_content_only",
    },
    "chroma_replace_dashvector_blocked": {
        "fixture": "blocked/retrieval_manifest_chroma_replace_dashvector.blocked.yaml",
        "reason": "chroma_sandbox_attempted_to_replace_dashvector",
    },
    "service_write_repo_blocked": {
        "fixture": "blocked/service_contract_no_write_attempt_write.blocked.yaml",
        "reason": "service_attempted_write_repo",
    },
    "memory_replace_repo_fact_blocked": {
        "fixture": "blocked/runtime_memory_boundary.blocked_repo_fact_replacement.yaml",
        "reason": "memory_attempted_repo_fact_replacement",
    },
    "sandbox_as_runtime_blocked": {
        "fixture": "blocked/completion_truth_check.sandbox_as_runtime_blocked.yaml",
        "reason": "sandbox_success_claimed_as_formal_runtime",
    },
    "technical_as_content_blocked": {
        "fixture": "blocked/completion_truth_check.technical_as_content_blocked.yaml",
        "reason": "technical_success_claimed_as_content_success",
    },
    "rag_as_fact_blocked": {
        "fixture": "blocked/completion_truth_check.rag_as_fact_blocked.yaml",
        "reason": "rag_result_claimed_as_fact_without_source_readback",
    },
}


try:
    import yaml as _yaml  # type: ignore
except Exception:  # pragma: no cover - exercised only where PyYAML is absent.
    _yaml = None


class ProbeFailure(AssertionError):
    """Raised when a frozen contract fixture violates the no-service probe."""


def coerce_scalar(raw_value: str) -> Any:
    value = raw_value.strip()
    if not value:
        return ""
    if value in {"true", "false"}:
        return value == "true"
    if value in {"[]", "[ ]"}:
        return []
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        items = value[1:-1].strip()
        if not items:
            return []
        return [coerce_scalar(item.strip()) for item in items.split(",")]
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def fallback_yaml_parse(text: str) -> dict[str, Any]:
    """Parse the small fixture subset used by this probe when PyYAML is absent."""
    parsed: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith("  - ") and current_key:
            if not isinstance(parsed.get(current_key), list):
                parsed[current_key] = []
            parsed[current_key].append(coerce_scalar(raw_line.strip()[2:].strip()))
            continue
        if raw_line.startswith("  ") and current_key and ":" in raw_line:
            if not isinstance(parsed.get(current_key), dict):
                parsed[current_key] = {}
            subkey, subvalue = raw_line.strip().split(":", 1)
            parsed[current_key][subkey.strip()] = coerce_scalar(subvalue.strip())
            continue
        if ":" in raw_line and not raw_line.startswith(" "):
            key, value = raw_line.split(":", 1)
            current_key = key.strip()
            parsed[current_key] = coerce_scalar(value.strip())
    return parsed


def load_fixture(relative_path: str) -> dict[str, Any]:
    path = FIXTURE_ROOT / relative_path
    if not path.exists():
        raise ProbeFailure(f"missing fixture: {relative_path}")
    text = path.read_text(encoding="utf-8")
    if _yaml is not None:
        data = _yaml.safe_load(text)
    else:
        data = fallback_yaml_parse(text)
    if not isinstance(data, dict):
        raise ProbeFailure(f"fixture did not parse to mapping: {relative_path}")
    return {"relative_path": relative_path, "path": str(path), "text": text, "data": data}


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise ProbeFailure(message)


def require_value(data: dict[str, Any], key: str, expected: Any, label: str) -> None:
    expect(data.get(key) == expected, f"{label}: expected {key}={expected!r}, got {data.get(key)!r}")


def require_truthy(data: dict[str, Any], key: str, label: str) -> None:
    expect(bool(data.get(key)) is True, f"{label}: expected truthy {key}")


def require_false(data: dict[str, Any], key: str, label: str) -> None:
    expect(data.get(key) is False, f"{label}: expected {key}=false, got {data.get(key)!r}")


def require_not_blocked(fixture: dict[str, Any], label: str) -> dict[str, Any]:
    data = fixture["data"]
    require_value(data, "case_type（样例类型）", "passing", label)
    require_value(data, "expected_result（预期结果）", "passed", label)
    require_false(data, "blocked", label)
    return data


def require_blocked_case(case_name: str, relative_path: str, reason: str) -> dict[str, Any]:
    fixture = load_fixture(relative_path)
    data = fixture["data"]
    require_value(data, "case_type（样例类型）", "blocked", case_name)
    require_value(data, "expected_result（预期结果）", "blocked", case_name)
    require_truthy(data, "blocked", case_name)
    reasons = data.get("blocked_reasons", [])
    expect(isinstance(reasons, list), f"{case_name}: blocked_reasons must be a list")
    expect(reason in reasons, f"{case_name}: missing blocked reason {reason!r}")
    return {
        "case_name": case_name,
        "fixture": relative_path,
        "expected_reason": reason,
        "observed_reasons": reasons,
        "status": "blocked_passed",
    }


def route_decision_node(state: dict[str, Any]) -> dict[str, Any]:
    graph = require_not_blocked(load_fixture(PASSING_FIXTURES["graph_runtime_adapter"]), "route_decision_node")
    require_value(graph, "workflow_route_decision", "mechanism_repair_flow", "route_decision_node")
    require_false(graph, "runtime_write_allowed", "route_decision_node")
    require_truthy(graph, "source_readback_required", "route_decision_node")
    require_truthy(graph, "completion_truth_check_required", "route_decision_node")
    state.update(
        {
            "project_route": "video_factory",
            "workflow_route_decision": graph["workflow_route_decision"],
            "runtime_write_allowed": graph["runtime_write_allowed"],
            "source_readback_required": graph["source_readback_required"],
            "completion_truth_check_required": graph["completion_truth_check_required"],
        }
    )
    state["trace"].append("route_decision_node")
    return state


def cleaning_adapter_node(state: dict[str, Any]) -> dict[str, Any]:
    cleaning = require_not_blocked(load_fixture(PASSING_FIXTURES["cleaning_adapter"]), "cleaning_adapter_node")
    require_value(cleaning, "secret_scan_before_ingestion", "passed", "cleaning_adapter_node")
    require_value(cleaning, "chunk_quality_check", "passed", "cleaning_adapter_node")
    metadata = cleaning.get("metadata_standardization", {})
    expect(isinstance(metadata, dict), "cleaning_adapter_node: metadata_standardization missing")
    expect(bool(metadata.get("source_path")), "cleaning_adapter_node: metadata source_path missing")
    expect(bool(metadata.get("chunk_id")), "cleaning_adapter_node: metadata chunk_id missing")
    state["cleaning_adapter_status"] = "passed"
    state["cleaning_source_path"] = metadata["source_path"]
    state["trace"].append("cleaning_adapter_node")
    return state


def retrieval_manifest_node(state: dict[str, Any]) -> dict[str, Any]:
    manifest = require_not_blocked(load_fixture(PASSING_FIXTURES["retrieval_manifest"]), "retrieval_manifest_node")
    require_value(manifest, "provider", "DashVector", "retrieval_manifest_node")
    require_truthy(manifest, "source_readback_required", "retrieval_manifest_node")
    require_value(manifest, "gap_status", "none", "retrieval_manifest_node")
    expect(bool(manifest.get("source_path")), "retrieval_manifest_node: source_path missing")
    expect(bool(manifest.get("chunk_id")), "retrieval_manifest_node: chunk_id missing")
    state["retrieval_manifest"] = {
        "provider": manifest["provider"],
        "source_path": manifest["source_path"],
        "chunk_id": manifest["chunk_id"],
        "source_readback_required": manifest["source_readback_required"],
        "gap_status": manifest["gap_status"],
    }
    state["trace"].append("retrieval_manifest_node")
    return state


def source_readback_node(state: dict[str, Any]) -> dict[str, Any]:
    readback = require_not_blocked(load_fixture(PASSING_FIXTURES["source_readback_map"]), "source_readback_node")
    require_value(readback, "readback_status", "passed", "source_readback_node")
    require_false(readback, "conflict_found", "source_readback_node")
    require_truthy(readback, "can_use_as_fact", "source_readback_node")
    source_path = REPO_ROOT / str(readback["source_path"])
    expect(source_path.exists(), f"source_readback_node: source path missing: {source_path}")
    source_text = source_path.read_text(encoding="utf-8")
    expect(bool(source_text.strip()), "source_readback_node: source path empty")
    state["source_readback"] = {
        "source_path": readback["source_path"],
        "readback_status": readback["readback_status"],
        "can_use_as_fact": readback["can_use_as_fact"],
    }
    state["trace"].append("source_readback_node")
    return state


def retrieval_gap_report_node(state: dict[str, Any]) -> dict[str, Any]:
    manifest = state["retrieval_manifest"]
    expect(manifest["gap_status"] == "none", "retrieval_gap_report_node: unexpected retrieval gap")
    state["retrieval_gap_report"] = {"gap_status": "none", "blocked": False}
    state["trace"].append("retrieval_gap_report_node")
    return state


def executor_handoff_node(state: dict[str, Any]) -> dict[str, Any]:
    service = require_not_blocked(load_fixture(PASSING_FIXTURES["service_contract_no_write"]), "executor_handoff_node")
    memory = require_not_blocked(load_fixture(PASSING_FIXTURES["runtime_memory_boundary"]), "executor_handoff_node")
    require_value(service, "active_write_executor", "codex", "executor_handoff_node")
    require_false(service, "service_can_write_repo", "executor_handoff_node")
    require_false(service, "external_api_authorized", "executor_handoff_node")
    require_truthy(memory, "repo_facts_win", "executor_handoff_node")
    require_false(memory, "memory_can_replace_repo_facts", "executor_handoff_node")
    state["executor_handoff"] = {
        "active_write_executor": service["active_write_executor"],
        "service_can_write_repo": service["service_can_write_repo"],
        "runtime_memory_authoritative": False,
    }
    state["trace"].append("executor_handoff_node")
    return state


def completion_truth_check_node(state: dict[str, Any]) -> dict[str, Any]:
    truth = require_not_blocked(
        load_fixture(PASSING_FIXTURES["completion_truth_check"]), "completion_truth_check_node"
    )
    require_truthy(truth, "user_goal_met", "completion_truth_check_node")
    require_truthy(truth, "required_outputs_exist", "completion_truth_check_node")
    require_truthy(truth, "source_readback_passed", "completion_truth_check_node")
    require_value(
        truth,
        "forbidden_status_promotion_scan",
        "passed",
        "completion_truth_check_node",
    )
    require_truthy(truth, "runtime_not_falsely_enabled", "completion_truth_check_node")
    require_truthy(truth, "completion_claim_allowed", "completion_truth_check_node")
    state["completion_truth_check"] = {
        "source_readback_passed": truth["source_readback_passed"],
        "forbidden_status_promotion_scan": truth["forbidden_status_promotion_scan"],
        "completion_claim_allowed": "true_for_probe_only",
    }
    state["trace"].append("completion_truth_check_node")
    return state


def run_passing_path() -> dict[str, Any]:
    state: dict[str, Any] = {"trace": []}
    for node in (
        route_decision_node,
        cleaning_adapter_node,
        retrieval_manifest_node,
        source_readback_node,
        retrieval_gap_report_node,
        executor_handoff_node,
        completion_truth_check_node,
    ):
        state = node(state)
    return {
        "status": "passed",
        "trace": state["trace"],
        "node_count": len(state["trace"]),
        "state_summary": {
            "project_route": state["project_route"],
            "workflow_route_decision": state["workflow_route_decision"],
            "retrieval_provider": state["retrieval_manifest"]["provider"],
            "source_readback_status": state["source_readback"]["readback_status"],
            "active_write_executor": state["executor_handoff"]["active_write_executor"],
            "completion_claim_allowed": state["completion_truth_check"]["completion_claim_allowed"],
        },
    }


def run_blocked_paths() -> list[dict[str, Any]]:
    results = []
    for case_name, case_spec in BLOCKED_CASES.items():
        results.append(require_blocked_case(case_name, case_spec["fixture"], case_spec["reason"]))
    return results


def main() -> int:
    langgraph_available = importlib.util.find_spec("langgraph") is not None
    result: dict[str, Any] = {
        "probe_name": "no_service_graph_probe",
        "probe_date": "2026-06-16",
        "langgraph_available": langgraph_available,
        "probe_runner_type": "fake_graph_runner_no_dependency",
        "service_started": False,
        "external_api_called": False,
        "dependency_installed": False,
        "DashVector_real_call": False,
        "Chroma_ingestion_run": False,
        "runtime_enabled": False,
        "runtime_write_allowed": False,
    }
    try:
        passing = run_passing_path()
        blocked = run_blocked_paths()
        result.update(
            {
                "final_probe_status": "passed",
                "passing_path_passed": passing["status"] == "passed",
                "blocked_paths_passed": all(item["status"] == "blocked_passed" for item in blocked),
                "graph_nodes_tested": True,
                "graph_trace": passing["trace"],
                "passing_path_result": passing,
                "blocked_paths_result": blocked,
                "source_readback_preserved": True,
                "retrieval_manifest_preserved": True,
                "active_write_executor_preserved": True,
                "completion_truth_check_preserved": True,
            }
        )
    except ProbeFailure as exc:
        result.update(
            {
                "final_probe_status": "failed",
                "passing_path_passed": False,
                "blocked_paths_passed": False,
                "failure": str(exc),
            }
        )
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
