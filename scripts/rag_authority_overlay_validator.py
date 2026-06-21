#!/usr/bin/env python3
"""Validate RAG authority overlay fixtures."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["authority_entries"]
ENTRY_FIELDS = [
    "chunk_id",
    "source_path",
    "line_range",
    "authority_level",
    "stale_status",
    "conflict_status",
    "retrieval_role",
    "can_feed_codex",
    "can_claim_completed",
    "readback_required",
    "hard_gate_flags",
]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    entries = data.get("authority_entries")
    if not isinstance(entries, list) or not entries:
        return ["authority_entries_missing"]
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            reasons.append(f"entry_{index}_not_object")
            continue
        for field in ENTRY_FIELDS:
            if field not in entry:
                reasons.append(f"entry_{index}_{field}_missing")
        if entry.get("authority_level") == "archive_only" and entry.get("can_feed_codex") is True:
            reasons.append("archive_only_can_feed_codex")
        if entry.get("stale_status") in {"conflict_pending", "superseded"} and entry.get("can_feed_codex") is True:
            reasons.append(f"{entry.get('stale_status')}_can_feed_codex")
        if entry.get("can_claim_completed") is True:
            reasons.append("authority_entry_claims_completed")
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_authority_overlay_validator",
        manifest_type="rag_authority_overlay",
        fixture_subdir="authority_overlay",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
