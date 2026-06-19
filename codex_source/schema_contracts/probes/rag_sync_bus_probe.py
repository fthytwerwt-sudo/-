#!/usr/bin/env python3
"""Validate RAG sync bus schema and fixtures."""

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
    result: dict[str, Any] = {"probe_name": "rag_sync_bus_probe"}
    try:
        sync_schema = load_yaml(SCHEMA_ROOT / "rag_sync_bus.schema.yaml")
        manifest_schema = load_yaml(SCHEMA_ROOT / "vector_index_manifest.schema.yaml")
        for key in (
            "repo_full_name（仓库全名）",
            "commit_sha（提交编号）",
            "source_inventory_path（源文件清单路径）",
            "chunk_manifest_path（分块清单路径）",
            "index_manifest_path（索引清单路径）",
            "dashvector_collection（DashVector 集合）",
            "stale_files（过期文件）",
        ):
            expect(key in sync_schema["required_fields（必填字段）"], f"rag_sync_bus missing {key}")
        hard = sync_schema["hard_rules（硬规则）"]
        expect(hard["local_first_execution（本地优先执行）"] is True, "local-first rule missing")
        expect(hard["github_audit_after_push（GitHub 推送后审核）"] is True, "github audit rule missing")
        expect(hard["dashvector_only_formal_store（DashVector 是唯一正式向量库）"] is True, "DashVector-only rule missing")
        expect(hard["chroma_disabled（Chroma 停用）"] is True, "Chroma disabled rule missing")
        expect("chunk_hash（分块哈希）" in manifest_schema["required_fields（必填字段）"], "index manifest missing chunk_hash")
        expect(manifest_schema["hard_rules（硬规则）"]["vector_values_not_written_to_git（向量值不得写入 Git）"] is True, "vector dump rule missing")

        passing = load_yaml(FIXTURE_ROOT / "passing" / "rag_sync_bus.passing.yaml")
        bus = passing["rag_sync_bus（RAG 同步总线）"]
        expect(passing["blocked"] is False, "passing fixture blocked")
        expect(bus["vector_store_provider（向量库供应商）"] == "DashVector", "passing fixture must use DashVector")
        expect(bus["stale_files（过期文件）"] == [], "passing fixture must not have stale files")
        expect(bus["hard_rules（硬规则）"]["dirty_files_not_indexed_to_formal_store（本地脏文件不进正式向量库）"] is True, "dirty rule missing")

        blocked = load_yaml(FIXTURE_ROOT / "blocked" / "rag_sync_bus.blocked.yaml")
        reasons = set(blocked.get("blocked_reasons", []))
        required = {"missing_commit_sha", "dirty_file_selected_for_index", "stale_index_detected", "chroma_selected_as_formal_store"}
        expect(blocked["blocked"] is True, "blocked fixture not blocked")
        expect(required.issubset(reasons), f"blocked reasons incomplete: {required - reasons}")
        expect(blocked["rag_sync_bus（RAG 同步总线）"]["vector_store_provider（向量库供应商）"] == "Chroma", "blocked fixture must attempt Chroma")
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
