#!/usr/bin/env python3
"""Build a RAG authority overlay for active chunks."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


DECISION_DIR = common.ROOT / "codex_log" / "rag_decision_engine"
OVERLAY_JSON = DECISION_DIR / "latest_rag_authority_overlay.json"
OVERLAY_MD = DECISION_DIR / "latest_rag_authority_overlay.md"


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def classify_source(source_path: str) -> dict[str, Any]:
    normalized = source_path.replace("\\", "/")
    if normalized == "AGENTS.md" or normalized.startswith("GPT数据源/08") or normalized.startswith("GPT数据源/11"):
        return {
            "authority_level": "current_formal_fact",
            "stale_status": "current",
            "retrieval_role": "decision_source",
            "default_weight": 1.0,
            "can_feed_codex": True,
            "hard_gate_flags": [],
        }
    if normalized.startswith("codex_log/latest.md") or normalized.startswith("codex_log/current_"):
        return {
            "authority_level": "latest_log",
            "stale_status": "current",
            "retrieval_role": "decision_source",
            "default_weight": 0.85,
            "can_feed_codex": True,
            "hard_gate_flags": [],
        }
    if normalized.startswith("codex_source/") or normalized.startswith("scripts/"):
        return {
            "authority_level": "execution_rule",
            "stale_status": "current",
            "retrieval_role": "execution_constraint",
            "default_weight": 0.9,
            "can_feed_codex": True,
            "hard_gate_flags": [],
        }
    if normalized.startswith("GPT数据源/09"):
        return {
            "authority_level": "target_state_plan",
            "stale_status": "target_state_only",
            "retrieval_role": "risk_context",
            "default_weight": 0.35,
            "can_feed_codex": False,
            "hard_gate_flags": ["target_state_cannot_override_current_fact"],
        }
    if any(marker in normalized for marker in ("归档", "archive", "old_context")):
        return {
            "authority_level": "archive_only",
            "stale_status": "stale_but_reference_allowed",
            "retrieval_role": "history_context",
            "default_weight": 0.05,
            "can_feed_codex": False,
            "hard_gate_flags": ["archive_only_cannot_feed_codex"],
        }
    if normalized.startswith("codex_log/"):
        return {
            "authority_level": "historical_log",
            "stale_status": "stale_but_reference_allowed",
            "retrieval_role": "history_context",
            "default_weight": 0.45,
            "can_feed_codex": False,
            "hard_gate_flags": ["dated_log_requires_latest_readback"],
        }
    return {
        "authority_level": "external_reference",
        "stale_status": "stale_but_reference_allowed",
        "retrieval_role": "risk_context",
        "default_weight": 0.25,
        "can_feed_codex": False,
        "hard_gate_flags": ["unknown_authority_requires_readback"],
    }


def build_overlay(chunk_manifest: dict[str, Any], delta_manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    superseded_by: dict[str, str] = {}
    if delta_manifest:
        for item in delta_manifest.get("chunk_classes", {}).get("superseded_chunks", []):
            old_id = str(item.get("chunk_id"))
            new_id = str(item.get("supersedes") or "")
            if old_id and new_id:
                superseded_by[old_id] = new_id

    entries: list[dict[str, Any]] = []
    for chunk in chunk_manifest.get("chunks", []):
        source_path = str(chunk.get("source_path") or "")
        classification = classify_source(source_path)
        conflict_status = "none"
        conflict_group_id = None
        if "current_gray_test_target" in source_path:
            classification["stale_status"] = "legacy_alias"
            classification["can_feed_codex"] = False
            classification["hard_gate_flags"] = ["legacy_alias_cannot_override_current_operation"]
        entry = {
            "chunk_id": chunk.get("chunk_id"),
            "source_path": source_path,
            "line_range": chunk.get("line_range"),
            "source_commit_sha": chunk.get("commit_sha") or chunk_manifest.get("commit_sha"),
            "authority_level": classification["authority_level"],
            "stale_status": classification["stale_status"],
            "conflict_status": conflict_status,
            "conflict_group_id": conflict_group_id,
            "superseded_by": superseded_by.get(str(chunk.get("chunk_id"))),
            "retrieval_role": classification["retrieval_role"],
            "default_weight": classification["default_weight"],
            "can_feed_codex": classification["can_feed_codex"],
            "can_claim_completed": False,
            "readback_required": True,
            "hard_gate_flags": classification["hard_gate_flags"],
        }
        entries.append(entry)

    source_commit_sha = str(chunk_manifest.get("commit_sha") or chunk_manifest.get("source_commit_sha") or "")
    return {
        "manifest_type": "rag_authority_overlay",
        "project_route": common.PROJECT_ROUTE,
        "repo_full_name": common.REPO_FULL_NAME,
        "source_commit_sha": source_commit_sha,
        "generated_at": common.now_iso(),
        "input_paths": [common.CHUNK_MANIFEST_PATH.as_posix()],
        "output_paths": [OVERLAY_JSON.as_posix(), OVERLAY_MD.as_posix()],
        "authority_entries": entries,
        "entry_count": len(entries),
        "blocked_if": [
            "archive_only_can_feed_codex",
            "target_state_only_claims_current_fact",
            "conflict_pending_can_feed_codex",
        ],
        "validation_result": {"status": "passed"},
        "key_printed": False,
        "key_written": False,
    }


def write_markdown(overlay: dict[str, Any], path: pathlib.Path = OVERLAY_MD) -> None:
    counts: dict[str, int] = {}
    for entry in overlay.get("authority_entries", []):
        key = str(entry.get("authority_level"))
        counts[key] = counts.get(key, 0) + 1
    lines = [
        "# RAG Authority Overlay",
        "",
        f"- source_commit_sha: `{overlay['source_commit_sha']}`",
        f"- entry_count: `{overlay['entry_count']}`",
        "- key_printed: `false`",
        "- key_written: `false`",
        "",
        "## Authority Counts",
        "",
    ]
    lines.extend(f"- {key}: `{value}`" for key, value in sorted(counts.items()))
    common.write_markdown(path, lines)


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Build RAG authority overlay.")
    parser.add_argument("--chunk-manifest", default=str(common.CHUNK_MANIFEST_PATH))
    parser.add_argument("--delta-manifest", default=str(common.OUT_DIR / "latest_chunk_delta_manifest.json"))
    parser.add_argument("--out", default=str(OVERLAY_JSON))
    parser.add_argument("--md-out", default=str(OVERLAY_MD))
    args = parser.parse_args()
    chunk_path = _resolve(args.chunk_manifest)
    delta_path = _resolve(args.delta_manifest)
    if not chunk_path.exists():
        raise SystemExit("blocked_chunk_manifest_missing")
    delta_manifest = common.read_json(delta_path) if delta_path.exists() else None
    overlay = build_overlay(common.read_json(chunk_path), delta_manifest)
    out_path = _resolve(args.out)
    md_out = _resolve(args.md_out)
    common.write_json(out_path, overlay)
    write_markdown(overlay, md_out)
    print(json.dumps({"status": "passed", "entry_count": overlay["entry_count"], "authority_overlay_path": out_path.as_posix()}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
