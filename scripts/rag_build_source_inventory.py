#!/usr/bin/env python3
"""Build the Video Factory RAG source inventory and secret scan report."""

from __future__ import annotations

import json
import pathlib

import rag_common as common


def write_markdown_report(inventory: dict) -> None:
    lines = [
        "# RAG Source Inventory",
        "",
        f"- project_route: `{inventory['project_route']}`",
        f"- branch: `{inventory['branch']}`",
        f"- commit_sha: `{inventory['commit_sha']}`",
        f"- secret_scan_passed: `{str(inventory['secret_scan_passed']).lower()}`",
        f"- allowlist_check_passed: `{str(inventory['allowlist_check_passed']).lower()}`",
        f"- denylist_check_passed: `{str(inventory['denylist_check_passed']).lower()}`",
        f"- allowed_file_count: `{inventory['allowed_file_count']}`",
        f"- excluded_file_count: `{inventory['excluded_file_count']}`",
        f"- excluded_by_secret_or_privacy_scan_count: `{inventory['excluded_by_secret_or_privacy_scan_count']}`",
        f"- indexed_secret_hit_count: `{inventory['indexed_secret_hit_count']}`",
        "",
        "## Excluded Files",
        "",
    ]
    if inventory["excluded_files"]:
        lines.extend(
            f"- `{item['source_path']}`: `{item['reason']}`"
            for item in inventory["excluded_files"][:120]
        )
        if len(inventory["excluded_files"]) > 120:
            lines.append(f"- ... {len(inventory['excluded_files']) - 120} more")
    else:
        lines.append("- none")
    common.write_markdown(common.OUT_DIR / "latest_source_inventory.md", lines)


def main() -> int:
    common.main_guard()
    inventory = common.build_source_inventory()
    common.write_json(common.SOURCE_INVENTORY_PATH, inventory)
    common.write_json(
        common.SECRET_SCAN_PATH,
        {
            "generated_at": inventory["generated_at"],
            "secret_scan_passed": inventory["secret_scan_passed"],
            "secret_hit_count": inventory["secret_hit_count"],
            "secret_hits": inventory["secret_hits"],
            "key_printed": False,
            "key_written": False,
        },
    )
    write_markdown_report(inventory)
    print(
        json.dumps(
            {
                "status": "passed" if not inventory["blocked"] else "blocked",
                "source_inventory_path": common.SOURCE_INVENTORY_PATH.as_posix(),
            "secret_scan_report_path": common.SECRET_SCAN_PATH.as_posix(),
            "allowed_file_count": inventory["allowed_file_count"],
            "excluded_file_count": inventory["excluded_file_count"],
            "excluded_by_secret_or_privacy_scan_count": inventory["excluded_by_secret_or_privacy_scan_count"],
            "indexed_secret_hit_count": inventory["indexed_secret_hit_count"],
            "secret_scan_passed": inventory["secret_scan_passed"],
            "key_printed": False,
        },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if not inventory["blocked"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
