#!/usr/bin/env python3
"""Validate RAG supply bus packs and fixtures."""

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
    result: dict[str, Any] = {"probe_name": "rag_supply_bus_probe"}
    try:
        for filename in (
            "rag_supply_pack.schema.yaml",
            "pre_supply_pack.schema.yaml",
            "mid_task_supply_pack.schema.yaml",
            "post_risk_review_pack.schema.yaml",
            "small_probe_run.schema.yaml",
        ):
            schema = load_yaml(SCHEMA_ROOT / filename)
            expect(schema["project_route"] == "video_factory（视频工厂）", f"{filename}: wrong route")

        pre = load_yaml(SCHEMA_ROOT / "pre_supply_pack.schema.yaml")
        for key in ("exact_snippet_pack（精确原文片段包）", "source_path（来源路径）", "line_range（行号范围）", "chunk_id（分块编号）"):
            expect(key in pre["required_fields（必填字段）"], f"pre supply schema missing {key}")
        mid = load_yaml(SCHEMA_ROOT / "mid_task_supply_pack.schema.yaml")
        expect("continue_allowed（是否允许继续）" in mid["required_fields（必填字段）"], "mid supply missing continue_allowed")

        passing = load_yaml(FIXTURE_ROOT / "passing" / "rag_supply_bus.passing.yaml")
        pack = passing["pre_supply_pack（执行前资料包）"]
        expect(passing["blocked"] is False, "passing fixture blocked")
        expect(bool(pack["exact_snippet_pack（精确原文片段包）"]), "passing fixture missing exact snippets")
        expect(bool(pack["source_path（来源路径）"]), "passing fixture missing source_path")
        expect(bool(pack["line_range（行号范围）"]), "passing fixture missing line_range")
        expect(passing["mid_task_supply_pack（执行中增量资料包）"]["continue_allowed（是否允许继续）"] is True, "mid supply should continue")
        expect(passing["small_probe_run（小跑探测）"]["can_execute（是否可执行）"] is True, "small probe should execute")

        blocked = load_yaml(FIXTURE_ROOT / "blocked" / "rag_supply_bus.blocked.yaml")
        reasons = set(blocked.get("blocked_reasons", []))
        required = {"retrieval_map_only", "missing_exact_snippet_pack", "missing_source_path", "missing_line_range", "page_content_only"}
        expect(blocked["blocked"] is True, "blocked fixture not blocked")
        expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
        expect(blocked["mid_task_supply_pack（执行中增量资料包）"]["continue_allowed（是否允许继续）"] is False, "blocked mid supply should stop")
        expect(blocked["post_risk_review_pack（完成前风险复核包）"]["completion_allowed（是否允许完成）"] is False, "blocked post review should stop completion")
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
