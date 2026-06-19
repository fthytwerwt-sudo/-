#!/usr/bin/env python3
"""Validate RAG failure routing and trace log policy."""

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
    pass


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


def main() -> int:
    result: dict[str, Any] = {"probe_name": "rag_failure_trace_probe"}
    try:
        route = load_yaml(SCHEMA_ROOT / "rag_failure_route.schema.yaml")
        trace = load_yaml(SCHEMA_ROOT / "rag_trace_event.schema.yaml")
        for target in (
            "RAG_supply_bus（RAG 供料总线）",
            "RAG_sync_bus（RAG 同步总线）",
            "fact_source_arbitration（事实源裁决）",
            "human_decision_gate（人工决策闸门）",
            "validation_repair（验证修复）",
            "completion_truth_check（完成真实性检查）",
            "git_sync_gate（Git 同步闸门）",
        ):
            expect(target in route["failure_route_targets（失败路由目标）"], f"missing failure target {target}")
        expect(route["hard_rules（硬规则）"]["retry_without_route_forbidden（禁止只写重试）"] is True, "retry-only rule missing")
        expect(trace["hard_rules（硬规则）"]["no_secret_in_trace（追踪不得写入密钥）"] is True, "trace secret rule missing")

        passing = load_yaml(FIXTURE_ROOT / "passing" / "rag_failure_trace.passing.yaml")
        expect(passing["blocked"] is False, "passing fixture blocked")
        expect(passing["rag_failure_route（RAG 失败路由）"]["target_route（目标路由）"] == "RAG_sync_bus", "passing target route mismatch")
        expect(bool(passing["rag_trace_event（RAG 追踪事件）"]["source_path（来源路径）"]), "passing trace missing source")
        for key in ("trace_event（追踪事件）", "dated_log（日期日志）", "latest（最新日志）"):
            expect(key in passing["trace_log_policy（追踪日志策略）"], f"passing trace policy missing {key}")

        blocked = load_yaml(FIXTURE_ROOT / "blocked" / "rag_failure_trace.blocked.yaml")
        reasons = set(blocked.get("blocked_reasons", []))
        required = {"retry_without_route", "missing_owner", "missing_trace_source_path", "secret_in_trace_forbidden"}
        expect(blocked["blocked"] is True, "blocked fixture not blocked")
        expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
        expect(not blocked["rag_failure_route（RAG 失败路由）"]["owner（处理方）"], "blocked fixture should miss owner")
        expect(not blocked["rag_trace_event（RAG 追踪事件）"]["source_path（来源路径）"], "blocked fixture should miss source")
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
