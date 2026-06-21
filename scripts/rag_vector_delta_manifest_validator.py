#!/usr/bin/env python3
"""Validate true incremental vector sync delta fixtures."""

from __future__ import annotations

from typing import Any

from rag_decision_validator_common import COMMON_REQUIRED_FIELDS, run_fixture_validation


REQUIRED_FIELDS = COMMON_REQUIRED_FIELDS + ["chunk_delta_counts", "external_call_report"]


def validate(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    counts = data.get("chunk_delta_counts")
    if not isinstance(counts, dict):
        reasons.append("chunk_delta_counts_missing")
    else:
        for key in ("new_chunks", "changed_chunks", "unchanged_chunks", "deleted_chunks", "superseded_chunks"):
            if key not in counts:
                reasons.append(f"{key}_missing")
            elif int(counts.get(key, -1)) < 0:
                reasons.append(f"{key}_negative")
    external = data.get("external_call_report", {})
    if external.get("alibaba_embedding_api_called") is not False:
        reasons.append("alibaba_embedding_api_called_not_false")
    if external.get("dashvector_upsert_called") is not False:
        reasons.append("dashvector_upsert_called_not_false")
    return reasons


def main() -> int:
    return run_fixture_validation(
        validator_name="rag_vector_delta_manifest_validator",
        manifest_type="true_incremental_vector_sync",
        fixture_subdir="vector_delta",
        required_fields=REQUIRED_FIELDS,
        domain_validator=validate,
    )


if __name__ == "__main__":
    raise SystemExit(main())
