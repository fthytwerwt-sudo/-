#!/usr/bin/env python3
"""Validate fixture-first RAG default decision boundaries."""

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
    """Raised when RAG fixture-first rules are violated."""


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
        "rag_default_decision.schema.yaml",
        "tool_registry.schema.yaml",
        "retriever_adapter.schema.yaml",
        "vector_store_adapter.schema.yaml",
    ):
        schema = load_yaml(SCHEMA_ROOT / filename)
        expect(schema.get("project_route") == "video_factory（视频工厂）", f"{filename}: wrong project route")
    rag = load_yaml(SCHEMA_ROOT / "rag_default_decision.schema.yaml")
    hard = rag["hard_rules（硬规则）"]
    expect(hard["rag_is_default_judgment_route（RAG 是默认判断路线）"] is True, "RAG must be default judgment route")
    expect(hard["rag_default_is_not_real_call（RAG 默认不等于真实外部调用）"] is True, "RAG default must not be real call")
    expect(hard["source_readback_required（必须原文回读）"] is True, "source readback required")
    return {"status": "passed", "schema_count": 4}


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "passing" / "rag_default_decision.passing.yaml")
    rag = fixture["rag_default_decision（RAG 默认判断）"]
    tool = fixture["tool_registry（工具注册表）"]
    retriever = fixture["retriever_adapter（检索器适配）"]
    vector = fixture["vector_store_adapter（向量库适配）"]
    expect(rag["rag_default_route_enabled（RAG 默认判断链是否启用）"] is True, "RAG default route must be enabled")
    expect(rag["real_external_call_allowed（是否允许真实外部调用）"] is False, "real external call must remain false")
    for key in ("source_path（来源路径）", "chunk_id（分块编号）", "line_range（行号范围）", "readback（原文回读）"):
        expect(bool(rag.get(key)), f"RAG passing fixture missing {key}")
    expect(tool["can_call_external_api（能否调用外部 API）"] is False, "tool cannot call external API")
    expect(tool["can_write_repo（能否写仓库）"] is False, "tool cannot write repo")
    expect(retriever["readback_required（是否必须回读）"] is True, "retriever readback required")
    expect(vector["store_provider（向量库来源）"] == "DashVector_fixture", "DashVector fixture remains main route")
    expect(vector["real_call_allowed（是否允许真实调用）"] is False, "vector real call forbidden")
    expect(vector["ingestion_allowed（是否允许入库）"] is False, "ingestion forbidden")
    return {"status": "passed"}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(FIXTURE_ROOT / "blocked" / "rag_default_decision.blocked.yaml")
    reasons = set(fixture.get("blocked_reasons", []))
    required = {
        "missing_source_path",
        "summary_without_readback",
        "rag_conflict_claimed_as_fact",
        "chroma_replaces_dashvector",
        "unclear_tool_permission",
        "rag_claimed_as_formal_fact",
    }
    expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
    rag = fixture["rag_default_decision（RAG 默认判断）"]
    expect(not rag.get("source_path（来源路径）"), "blocked fixture should miss source_path")
    expect(rag.get("readback（原文回读）") == "missing", "blocked fixture should miss readback")
    vector = fixture["vector_store_adapter（向量库适配）"]
    expect(vector["store_provider（向量库来源）"] == "Chroma_sandbox_fixture", "blocked fixture should use Chroma sandbox")
    expect(vector["route_role（路线角色）"] == "main_route", "blocked fixture should attempt Chroma replacement")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "rag_default_decision_probe",
        "rag_default_route_enabled": True,
        "real_external_call_allowed": False,
        "external_api_called": False,
        "dashvector_real_call": False,
        "chroma_ingestion_run": False,
        "runtime_enabled": False,
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
