#!/usr/bin/env python3
"""Build mid-task RAG supply packs from child task state."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common
import rag_supply_pack_builder as pre_builder


REQUIRED_STATE_FIELDS = [
    "child_task_id",
    "files_already_read",
    "will_modify_files",
    "missing_context",
    "validation_failure_logs",
    "conflict_points",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)] if str(value).strip() else []


def validate_state(state: dict[str, Any]) -> list[str]:
    return [field for field in REQUIRED_STATE_FIELDS if field not in state]


def build_mid_pack(state: dict[str, Any]) -> dict[str, Any]:
    missing = validate_state(state)
    if missing:
        raise RuntimeError("blocked_child_task_state_missing_fields:" + ",".join(missing))
    index_manifest = common.read_json(common.INDEX_MANIFEST_PATH)
    retrieval_goal = " ".join(
        _as_list(state.get("missing_context"))
        + _as_list(state.get("validation_failure_logs"))
        + _as_list(state.get("conflict_points"))
        + _as_list(state.get("will_modify_files"))
    ).strip() or "mid task incremental RAG supply"
    chunks = pre_builder._select_candidate_chunks(
        index_manifest,
        retrieval_goal,
        _as_list(state.get("will_modify_files")),
        limit=3,
    )
    snippets = pre_builder._exact_snippet_pack(chunks, "执行中缺上下文、验证失败或高风险写入前补料。")
    continue_allowed = bool(snippets) and all(
        item.get("readback_hash_match") and item.get("can_feed_codex") and item.get("conflict_status") == "none"
        for item in snippets
    )
    return {
        "pack_type": "mid_task_supply_pack",
        "child_task_id": state["child_task_id"],
        "files_already_read": _as_list(state.get("files_already_read")),
        "will_modify_files": _as_list(state.get("will_modify_files")),
        "missing_context": _as_list(state.get("missing_context")),
        "validation_failure_logs": _as_list(state.get("validation_failure_logs")),
        "conflict_points": _as_list(state.get("conflict_points")),
        "incremental_snippets": snippets,
        "action_constraint": [
            "source_readback_required_before_continue",
            "rag_cleaning_layer_fields_required_before_continue",
            "do_not_continue_if_validation_failure_unexplained",
        ],
        "continue_allowed": continue_allowed,
        "blocked_if": [
            "child_task_state_missing",
            "incremental_snippets_missing",
            "readback_failed",
            "cleaning_layer_blocked",
            "conflict_points_unresolved",
        ],
        "generated_at": common.now_iso(),
    }


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Build mid-task RAG supply pack.")
    parser.add_argument("--child-task-state", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    state_path = _resolve(args.child_task_state)
    out_path = _resolve(args.out)
    if not state_path.exists():
        raise SystemExit("blocked_child_task_state_missing")
    pack = build_mid_pack(common.read_json(state_path))
    common.write_json(out_path, pack)
    print(json.dumps({"status": "passed" if pack["continue_allowed"] else "blocked", "mid_task_supply_pack_path": out_path.as_posix()}, ensure_ascii=False, sort_keys=True))
    return 0 if pack["continue_allowed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
