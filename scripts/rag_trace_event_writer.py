#!/usr/bin/env python3
"""Append validated RAG trace events as JSONL."""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import rag_common as common


REQUIRED_FIELDS = [
    "event_id",
    "task_id",
    "event_type",
    "input_signal",
    "supply_used",
    "files_read",
    "files_modified",
    "validation_result",
    "failure_route_if_any",
    "next_safe_step",
]


def _resolve(path_value: str) -> pathlib.Path:
    path = pathlib.Path(path_value)
    return path if path.is_absolute() else common.ROOT / path


def validate_event(event: dict[str, Any]) -> list[str]:
    return [field for field in REQUIRED_FIELDS if field not in event]


def main() -> int:
    common.main_guard()
    parser = argparse.ArgumentParser(description="Append a RAG trace event.")
    parser.add_argument("--event", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    event_path = _resolve(args.event)
    out_path = _resolve(args.out)
    if not event_path.exists():
        raise SystemExit("blocked_trace_event_missing")
    event = common.read_json(event_path)
    missing = validate_event(event)
    if missing:
        print(json.dumps({"status": "blocked", "blocked_reasons": [f"{field}_missing" for field in missing]}, ensure_ascii=False, sort_keys=True))
        return 2
    event.setdefault("created_at", common.now_iso())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps({"status": "passed", "trace_event_path": out_path.as_posix(), "event_id": event["event_id"]}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
