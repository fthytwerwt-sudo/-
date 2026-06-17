#!/usr/bin/env python3
"""Validate engineering state map and acceptance contract fixtures.

本探测只读取本地 schema（结构契约）和 fixture（测试样例），不启用
runtime（运行时）、service（服务）、RAG（检索增强生成）真实调用或媒体链路。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"PyYAML required by existing probe environment: {exc}")


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "schemas"
FIXTURE_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "fixtures"


class ProbeFailure(AssertionError):
    """Raised when the local fixture-first engineering state map is unsafe."""


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
    state_schema = load_yaml(SCHEMA_ROOT / "engineering_state_map.schema.yaml")
    acceptance_schema = load_yaml(SCHEMA_ROOT / "acceptance_contract.schema.yaml")
    statuses = set(state_schema["allowed_statuses（允许状态）"])
    required_statuses = {
        "formal（正式）",
        "candidate（候选）",
        "probe_only（仅探测）",
        "documented_only（仅文档）",
        "missing（缺失）",
        "conflict（冲突）",
        "blocked（阻断）",
    }
    expect(required_statuses.issubset(statuses), "engineering state statuses incomplete")
    for key in (
        "probe_only_cannot_jump_to_formal（仅探测不能直接跳正式）",
        "documented_only_cannot_claim_implemented（仅文档不能声称已实现）",
        "evidence_files_required（必须有证据文件）",
        "runtime_status_promotion_forbidden（禁止推进运行时状态）",
    ):
        expect(state_schema["hard_rules（硬规则）"].get(key) is True, f"missing hard rule: {key}")
    expect(
        acceptance_schema["hard_rules（硬规则）"].get(
            "probe_result_is_not_runtime（探测结果不等于运行时）"
        )
        is True,
        "acceptance contract must keep probe result separate from runtime",
    )
    return {"status": "passed", "status_count": len(statuses)}


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "passing" / "engineering_state_map.passing.yaml")
    expect(fixture["case_type（样例类型）"] == "passing", "passing fixture type mismatch")
    modules = fixture.get("modules（模块）", [])
    expect(isinstance(modules, list) and modules, "passing fixture modules missing")
    seen_conflict = False
    for module in modules:
        name = module["module_name（模块名）"]
        status = module["current_status（当前状态）"]
        evidence = module.get("evidence_files（证据文件）", [])
        expect(evidence, f"{name}: evidence_files required")
        expect(module.get("fallback_layer（失败回退层）"), f"{name}: fallback_layer required")
        if status == "probe_only":
            expect("formal" not in module.get("allowed_next_states（允许进入的下一状态）", []), f"{name}: probe_only cannot jump formal")
        if status == "conflict":
            seen_conflict = True
            expect(module.get("conflict_reason（冲突原因）"), f"{name}: conflict_reason required")
            expect(module.get("fact_source_arbitration（事实源裁决）"), f"{name}: fact_source_arbitration required")
    status_flags = fixture["status_not_promoted（未推进状态）"]
    expect(status_flags["runtime_enabled（运行时启用）"] is False, "runtime must remain false")
    expect(status_flags["service_started（服务启动）"] is False, "service must remain false")
    expect(status_flags["rag_runtime_enabled（RAG 运行时启用）"] is False, "RAG runtime must remain false")
    expect(status_flags["media_generated（媒体生成）"] is False, "media must remain false")
    expect(seen_conflict, "passing fixture must include one conflict with arbitration")
    return {"status": "passed", "module_count": len(modules)}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "blocked" / "engineering_state_map.blocked.yaml")
    expect(fixture["case_type（样例类型）"] == "blocked", "blocked fixture type mismatch")
    reasons = set(fixture.get("blocked_reasons", []))
    required = {
        "missing_evidence_files",
        "probe_only_direct_to_formal",
        "documented_only_claimed_implemented",
        "conflict_missing_fact_source_arbitration",
        "forbidden_status_promotion_attempt",
    }
    expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "engineering_state_map_probe",
        "runtime_enabled": False,
        "service_started": False,
        "external_api_called": False,
        "dashvector_real_call": False,
        "chroma_ingestion_run": False,
        "media_generated": False,
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
