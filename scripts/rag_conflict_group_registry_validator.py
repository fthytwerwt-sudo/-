#!/usr/bin/env python3
"""Validate RAG conflict group registry fixtures."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["conflict_groups"]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    groups = data.get("conflict_groups")
    if not isinstance(groups, list) or not groups:
        return ["conflict_groups_missing"]
    for index, group in enumerate(groups):
        if not isinstance(group, dict):
            reasons.append(f"group_{index}_not_object")
            continue
        for field in ("conflict_group_id", "candidates", "current_winner", "status", "loser_policy"):
            if field not in group:
                reasons.append(f"group_{index}_{field}_missing")
        if group.get("status") == "pending" and not group.get("current_winner"):
            reasons.append("required_fact_without_current_winner")
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_conflict_group_registry_validator",
        manifest_type="conflict_group_registry",
        fixture_subdir="conflict_group",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
