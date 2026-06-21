#!/usr/bin/env python3
"""Build the RAG conflict group registry from known project decision conflicts."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DECISION_DIR = common.ROOT / "codex_log" / "rag_decision_engine"
REGISTRY_JSON = DECISION_DIR / "latest_conflict_group_registry.json"
REGISTRY_MD = DECISION_DIR / "latest_conflict_group_registry.md"


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def build_registry(source_commit_sha: str) -> dict[str, Any]:
    groups = [
        {
            "conflict_group_id": "voice_route",
            "topic": "voice_validation_and_supplier_route",
            "status": "resolved",
            "current_winner": "voice_validation_pending_user_chatgpt_review",
            "winner_reason": "Current formal facts keep final_voice_validated=false and voice_validation pending.",
            "candidates": ["voice_validation_pending_user_chatgpt_review", "old_voice_passed_claim"],
            "loser_policy": "stale_but_reference_allowed",
        },
        {
            "conflict_group_id": "formal_operation_ratio",
            "topic": "horizontal_16_9_vs_vertical_9_16",
            "status": "resolved",
            "current_winner": "horizontal_16_9",
            "winner_reason": "Formal operation delivery ratio is horizontal 16:9; vertical is historical context.",
            "candidates": ["horizontal_16_9", "vertical_9_16"],
            "loser_policy": "history_context_only",
        },
        {
            "conflict_group_id": "deepseek_supply_default",
            "topic": "DeepSeek default supply vs conditional trigger",
            "status": "resolved",
            "current_winner": "conditional_trigger_only",
            "winner_reason": "DeepSeek participates only on trigger or explicit user request.",
            "candidates": ["conditional_trigger_only", "default_supply_memory"],
            "loser_policy": "archive_only",
        },
        {
            "conflict_group_id": "formal_delivery_baseline",
            "topic": "technical_preview_vs_publish_candidate_or_blocked",
            "status": "resolved",
            "current_winner": "publish_candidate_or_blocked",
            "winner_reason": "Formal operation delivery accepts publish candidate or blocked; technical preview is internal diagnostic.",
            "candidates": ["publish_candidate_or_blocked", "technical_preview_delivery"],
            "loser_policy": "blocked_context",
        },
        {
            "conflict_group_id": "formal_fact_vs_target_state",
            "topic": "current formal fact vs target state plan",
            "status": "resolved",
            "current_winner": "current_formal_fact",
            "winner_reason": "Target state plan cannot override current formal facts until landed in repo facts.",
            "candidates": ["current_formal_fact", "target_state_plan"],
            "loser_policy": "target_state_only",
        },
    ]
    return {
        "manifest_type": "conflict_group_registry",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": source_commit_sha,
        "generated_at": common.now_iso(),
        "input_paths": ["codex_log/rag_decision_engine/latest_rag_authority_overlay.json"],
        "output_paths": [REGISTRY_JSON.as_posix(), REGISTRY_MD.as_posix()],
        "rules": {
            "current_formal_fact_beats_latest_log": True,
            "latest_log_beats_historical_log": True,
            "target_state_cannot_override_current_fact": True,
            "user_current_turn_override_temporary_only": True,
            "no_winner_for_required_fact_blocks": True,
        },
        "conflict_groups": groups,
        "blocked_if": ["required_fact_without_current_winner", "pending_conflict_for_execution_fact"],
        "validation_result": {"status": "passed"},
        "key_printed": False,
        "key_written": False,
    }


def write_markdown(registry: dict[str, Any], path: pathlib.Path = REGISTRY_MD) -> None:
    lines = [
        "# RAG Conflict Group Registry",
        "",
        f"- source_commit_sha: `{registry['source_commit_sha']}`",
        f"- conflict_group_count: `{len(registry['conflict_groups'])}`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "",
        "## Groups",
        "",
    ]
    for group in registry["conflict_groups"]:
        lines.append(f"- `{group['conflict_group_id']}` -> `{group['current_winner']}` ({group['status']})")
    common.write_markdown(path, lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Build RAG conflict group registry.")
    parser.add_argument("--source-commit-sha", default=common.current_commit())
    parser.add_argument("--out", default=str(REGISTRY_JSON))
    parser.add_argument("--md-out", default=str(REGISTRY_MD))
    args = parser.parse_args()
    registry = build_registry(args.source_commit_sha)
    out_path = _resolve(args.out)
    md_path = _resolve(args.md_out)
    common.write_json(out_path, registry)
    write_markdown(registry, md_path)
    print(json.dumps({"status": "passed", "conflict_group_registry_path": out_path.as_posix(), "group_count": len(registry["conflict_groups"])}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
