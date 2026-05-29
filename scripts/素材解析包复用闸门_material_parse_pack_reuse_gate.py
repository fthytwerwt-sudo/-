#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PACK_FIELDS = [
    "parse_pack_id",
    "material_root",
    "source_files",
    "material_index_path",
    "material_detail_report_path",
    "contact_sheet_paths",
    "source_segment_inventory_path",
    "parse_timestamp",
    "parse_scope",
    "skill_used",
    "reuse_policy",
    "stale_if",
]

REQUIRED_STALE_IF = [
    "source_file_added_deleted_or_renamed",
    "source_file_size_or_mtime_changed",
    "script_target_changed_and_pack_cannot_support",
    "user_requested_reaudit",
    "missing_key_timecode_or_evidence_fields",
]


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def resolve_path(value: Any) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(str(value))
    if path.is_absolute():
        return path
    return ROOT / path


def read_json(path: Path | None, label: str) -> tuple[Any | None, list[str]]:
    if path is None:
        return None, [f"{label}_missing"]
    if not path.exists():
        return None, [f"{label}_missing:{rel(path)}"]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"{label}_json_parse_error:{exc}"]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# material_parse_pack_reuse_preflight",
        "",
        f"- `status`: `{report.get('status')}`",
        f"- `check_depth`: `{report.get('check_depth')}`",
        f"- `final_decision`: `{report.get('duplicate_material_check', {}).get('final_decision', '')}`",
    ]
    reasons = report.get("blocked_reasons") or []
    if reasons:
        lines.append("- `blocked_reasons`:")
        lines.extend(f"  - `{reason}`" for reason in reasons)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "passed", "pass", "1", "是", "已引用"}
    return bool(value)


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def get_nested(data: Any, *keys: str) -> Any:
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def first_path(cli_path: Path | None, pack: dict[str, Any] | None, key: str) -> Path | None:
    if cli_path:
        return cli_path
    if not isinstance(pack, dict):
        return None
    return resolve_path(pack.get(key))


def validate_parse_pack(pack: Any) -> tuple[dict[str, Any], list[str]]:
    reasons: list[str] = []
    if not isinstance(pack, dict):
        return {}, ["material_parse_pack_invalid"]
    missing = [field for field in REQUIRED_PACK_FIELDS if pack.get(field) in (None, "", [])]
    if missing:
        reasons.append("material_parse_pack_missing_required_fields")
    stale_if = set(str(item) for item in as_list(pack.get("stale_if")))
    missing_stale_if = [item for item in REQUIRED_STALE_IF if item not in stale_if]
    if missing_stale_if:
        reasons.append("material_parse_pack_stale_if_incomplete")
    if str(pack.get("skill_used")) != "skills/视频素材解析_video_material_audit/SKILL.md":
        reasons.append("material_parse_pack_skill_used_mismatch")
    if str(pack.get("reuse_policy") or "").lower() not in {
        "reuse_only",
        "read_only_reuse",
        "single_parse_reuse",
        "剪辑阶段只读复用",
    }:
        reasons.append("material_parse_pack_reuse_policy_not_strict")
    return {
        "missing_required_fields": missing,
        "missing_stale_if": missing_stale_if,
        "parse_pack_id": pack.get("parse_pack_id", ""),
    }, reasons


def source_file_staleness(pack: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    stale_files: list[dict[str, Any]] = []
    for index, item in enumerate(as_list(pack.get("source_files")), start=1):
        if isinstance(item, str):
            source = {"path": item}
        elif isinstance(item, dict):
            source = item
        else:
            stale_files.append({"index": index, "reason": "source_file_entry_invalid"})
            continue
        path = resolve_path(source.get("path") or source.get("source_path") or source.get("file_path"))
        if path is None:
            stale_files.append({"index": index, "reason": "source_file_path_missing"})
            continue
        if not path.exists():
            stale_files.append({"path": rel(path), "reason": "source_file_missing_or_renamed"})
            continue
        stat = path.stat()
        expected_size = source.get("size") or source.get("size_bytes")
        if expected_size not in (None, "") and int(expected_size) != stat.st_size:
            stale_files.append({"path": rel(path), "reason": "source_file_size_changed"})
        expected_mtime = source.get("mtime") or source.get("mtime_ns")
        if expected_mtime not in (None, ""):
            actual_mtime = stat.st_mtime_ns if "mtime_ns" in source else int(stat.st_mtime)
            if int(float(expected_mtime)) != actual_mtime:
                stale_files.append({"path": rel(path), "reason": "source_file_mtime_changed"})
    reasons = ["material_parse_pack_stale"] if stale_files else []
    return stale_files, reasons


def inventory_segments(inventory: Any) -> list[dict[str, Any]]:
    if not isinstance(inventory, dict):
        return []
    candidates = [
        inventory.get("segments"),
        inventory.get("source_segments"),
        inventory.get("source_segment_inventory"),
        get_nested(inventory, "source_segment_inventory", "segments"),
    ]
    for candidate in candidates:
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return []


def execution_line_groups(execution_map: Any) -> list[dict[str, Any]]:
    if not isinstance(execution_map, dict):
        return []
    candidates = [
        execution_map.get("line_groups"),
        execution_map.get("shots"),
        execution_map.get("script_to_shot_execution_map"),
        get_nested(execution_map, "script_to_shot_execution_map", "line_groups"),
        get_nested(execution_map, "script_to_timeline_map", "line_groups"),
    ]
    for candidate in candidates:
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return []


def ledger_usages(ledger: Any) -> list[dict[str, Any]]:
    if not isinstance(ledger, dict):
        return []
    candidates = [
        ledger.get("usages"),
        ledger.get("usage_entries"),
        ledger.get("material_usage_ledger"),
        get_nested(ledger, "material_usage_ledger", "usages"),
    ]
    for candidate in candidates:
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return []


def line_group_id(item: dict[str, Any], index: int) -> str:
    return str(item.get("line_group_id") or item.get("shot_id") or item.get("id") or f"line_group_{index:03d}")


def segment_id(item: dict[str, Any]) -> str:
    return str(
        item.get("segment_id")
        or item.get("source_segment_id")
        or item.get("material_segment_id")
        or item.get("selected_segment_id")
        or item.get("material_id")
        or ""
    )


def line_group_segment_id(group: dict[str, Any]) -> str:
    direct = segment_id(group)
    if direct:
        return direct
    refs = group.get("material_evidence_refs")
    if isinstance(refs, list) and refs and isinstance(refs[0], dict):
        return segment_id(refs[0])
    return ""


def has_report_citation(group: dict[str, Any], usage: dict[str, Any] | None) -> bool:
    citation_fields = [
        "material_report_ref",
        "material_detail_report_ref",
        "material_detail_report_path",
        "material_parse_pack_id",
        "claim_id",
        "evidence_claim_id",
        "source_report",
    ]
    if truthy(group.get("material_report_cited")):
        return True
    if any(group.get(field) not in (None, "", []) for field in citation_fields):
        return True
    if group.get("material_evidence_refs"):
        return True
    if usage and any(usage.get(field) not in (None, "", []) for field in citation_fields):
        return True
    return False


def is_theme_only(group: dict[str, Any], usage: dict[str, Any] | None) -> bool:
    joined = " ".join(
        str(value)
        for value in [
            group.get("match_type"),
            group.get("evidence_match_status"),
            group.get("visual_match_type"),
            group.get("selected_reason"),
            usage.get("match_type") if usage else "",
            usage.get("selected_reason") if usage else "",
        ]
    ).lower()
    return (
        truthy(group.get("theme_only_match"))
        or truthy(group.get("material_only_thematically_related"))
        or (usage is not None and truthy(usage.get("theme_only_match")))
        or "theme_only" in joined
        or "material_only_thematically_related" in joined
        or "主题相近" in joined
    )


def cannot_support_selected(group: dict[str, Any], usage: dict[str, Any] | None) -> bool:
    values = [
        group.get("support_status"),
        group.get("selected_material_support_status"),
        usage.get("support_status") if usage else "",
    ]
    joined = " ".join(str(value).lower() for value in values)
    return (
        truthy(group.get("cannot_support_selected"))
        or truthy(group.get("selected_material_in_cannot_support"))
        or (usage is not None and truthy(usage.get("cannot_support_selected")))
        or "cannot_support" in joined
        or "not_allowed" in joined
    )


def build_usage_from_execution_map(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    usages: list[dict[str, Any]] = []
    for index, group in enumerate(groups, start=1):
        sid = line_group_segment_id(group)
        if sid:
            usages.append(
                {
                    "line_group_id": line_group_id(group, index),
                    "segment_id": sid,
                    "reuse_reason": group.get("reuse_reason", ""),
                    "is_core_evidence": group.get("is_core_evidence"),
                    "claim_id": group.get("claim_id") or group.get("evidence_claim_id") or group.get("line_group_goal"),
                }
            )
    return usages


def duplicate_material_check(
    *,
    segments: list[dict[str, Any]],
    groups: list[dict[str, Any]],
    usages: list[dict[str, Any]],
) -> tuple[dict[str, Any], list[str]]:
    reasons: list[str] = []
    if not usages and groups:
        usages = build_usage_from_execution_map(groups)
    usage_by_line_group = {str(item.get("line_group_id") or ""): item for item in usages}
    segment_counts = Counter(segment_id(item) for item in usages if segment_id(item))
    repeated_segment_ids = sorted(sid for sid, count in segment_counts.items() if sid and count > 1)
    segment_index = {segment_id(item): item for item in segments if segment_id(item)}

    repeated_without_reason = []
    repeated_core_evidence_ids = []
    core_claims: dict[str, set[str]] = defaultdict(set)
    for usage in usages:
        sid = segment_id(usage)
        if not sid or segment_counts[sid] <= 1:
            continue
        if not str(usage.get("reuse_reason") or "").strip():
            repeated_without_reason.append(sid)
        is_core = truthy(usage.get("is_core_evidence")) or truthy(segment_index.get(sid, {}).get("is_core_evidence"))
        if is_core:
            repeated_core_evidence_ids.append(sid)
            claim = str(usage.get("claim_id") or usage.get("claim_text") or usage.get("line_group_goal") or "")
            if claim:
                core_claims[sid].add(claim)

    consecutive_duplicate_count = 0
    previous_sid = ""
    for usage in usages:
        sid = segment_id(usage)
        if sid and sid == previous_sid:
            consecutive_duplicate_count += 1
        previous_sid = sid

    theme_only_count = 0
    cannot_support_count = 0
    report_not_cited_count = 0
    for index, group in enumerate(groups, start=1):
        gid = line_group_id(group, index)
        usage = usage_by_line_group.get(gid)
        if is_theme_only(group, usage):
            theme_only_count += 1
        if cannot_support_selected(group, usage):
            cannot_support_count += 1
        if line_group_segment_id(group) and not has_report_citation(group, usage):
            report_not_cited_count += 1

    if repeated_without_reason:
        reasons.append("same_segment_reused_without_reuse_reason")
    if consecutive_duplicate_count > 0:
        reasons.append("consecutive_duplicate_segment_used")
    if any(len(claims) > 1 for claims in core_claims.values()):
        reasons.append("core_evidence_reused_for_different_claim")
    if theme_only_count > 0:
        reasons.append("theme_only_match_used_as_direct_evidence")
    if cannot_support_count > 0:
        reasons.append("cannot_support_material_selected")
    if report_not_cited_count > 0:
        reasons.append("material_report_not_cited_by_line_group")

    report = {
        "total_segments": len(segments),
        "total_line_groups": len(groups),
        "repeated_segment_count": len(repeated_segment_ids),
        "repeated_core_evidence_count": len(set(repeated_core_evidence_ids)),
        "consecutive_duplicate_count": consecutive_duplicate_count,
        "theme_only_match_count": theme_only_count,
        "cannot_support_selected_count": cannot_support_count,
        "report_not_cited_count": report_not_cited_count,
        "repeated_segment_ids": repeated_segment_ids,
        "final_decision": "blocked" if reasons else "passed",
    }
    return report, sorted(set(reasons))


def run_material_parse_pack_reuse_gate(
    *,
    material_parse_pack: Path | None,
    source_segment_inventory: Path | None = None,
    script_to_shot_execution_map: Path | None = None,
    material_usage_ledger: Path | None = None,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    pack, read_errors = read_json(material_parse_pack, "material_parse_pack")
    reasons = ["material_parse_pack_missing"] if read_errors else []
    reasons.extend(read_errors)
    pack_info: dict[str, Any] = {}
    stale_files: list[dict[str, Any]] = []
    if isinstance(pack, dict):
        pack_info, pack_reasons = validate_parse_pack(pack)
        reasons.extend(pack_reasons)
        stale_files, stale_reasons = source_file_staleness(pack)
        reasons.extend(stale_reasons)
    else:
        pack = {}

    inventory_path = first_path(source_segment_inventory, pack, "source_segment_inventory_path")
    execution_path = first_path(script_to_shot_execution_map, pack, "script_to_shot_execution_map_path")
    ledger_path = first_path(material_usage_ledger, pack, "material_usage_ledger_path")

    inventory, inventory_errors = read_json(inventory_path, "source_segment_inventory")
    execution_map, execution_errors = read_json(execution_path, "script_to_shot_execution_map")
    ledger, ledger_errors = read_json(ledger_path, "material_usage_ledger")
    reasons.extend("source_segment_inventory_missing" if item.startswith("source_segment_inventory_missing") else item for item in inventory_errors)
    reasons.extend("script_to_shot_execution_map_missing" if item.startswith("script_to_shot_execution_map_missing") else item for item in execution_errors)
    reasons.extend("material_usage_ledger_missing" if item.startswith("material_usage_ledger_missing") else item for item in ledger_errors)

    segments = inventory_segments(inventory)
    groups = execution_line_groups(execution_map)
    usages = ledger_usages(ledger)
    if inventory is not None and not segments:
        reasons.append("source_segment_inventory_missing")
    if execution_map is not None and not groups:
        reasons.append("script_to_shot_execution_map_missing")
    if ledger is not None and not usages:
        reasons.append("material_usage_ledger_missing")

    duplicate_report, duplicate_reasons = duplicate_material_check(
        segments=segments,
        groups=groups,
        usages=usages,
    )
    if inventory_errors or execution_errors or ledger_errors:
        reasons.append("duplicate_material_check_missing")
    reasons.extend(duplicate_reasons)

    blocked_reasons = sorted(set(reason for reason in reasons if reason))
    report = {
        "schema": "material_parse_pack_reuse_gate.v1",
        "gate_name": "material_parse_pack_reuse_preflight",
        "status": "blocked" if blocked_reasons else "passed",
        "check_depth": "implemented_no_render_no_media_parse",
        "blocked_reasons": blocked_reasons,
        "checked_inputs": {
            "material_parse_pack": rel(material_parse_pack) if material_parse_pack else "",
            "source_segment_inventory": rel(inventory_path) if inventory_path else "",
            "script_to_shot_execution_map": rel(execution_path) if execution_path else "",
            "material_usage_ledger": rel(ledger_path) if ledger_path else "",
        },
        "material_parse_pack": {
            **pack_info,
            "stale_files": stale_files,
            "reuse_policy": pack.get("reuse_policy", "") if isinstance(pack, dict) else "",
        },
        "editing_parse_reuse_rule": {
            "raw_media_reparse_allowed": False,
            "allowed_light_checks": [
                "file_exists",
                "ffprobe_basic_info_readable",
                "contact_sheet_path_exists",
                "report_reference_path_exists",
            ],
            "not_allowed": [
                "reparse_raw_media_as_primary_judgment_source",
                "override_material_detail_report_with_new_interpretation",
                "theme_only_match_as_direct_evidence",
                "same_segment_reuse_without_reuse_reason",
            ],
        },
        "duplicate_material_check": duplicate_report,
    }
    if output_dir:
        write_json(output_dir / "material_parse_pack_reuse_report.json", report)
        write_md(output_dir / "material_parse_pack_reuse_report.md", report)
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check that editing reuses one material_parse_pack without raw media reparsing.")
    parser.add_argument("--material-parse-pack", type=Path, required=True)
    parser.add_argument("--source-segment-inventory", type=Path)
    parser.add_argument("--script-to-shot-execution-map", type=Path)
    parser.add_argument("--material-usage-ledger", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-blocked-exit-zero", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = run_material_parse_pack_reuse_gate(
        material_parse_pack=args.material_parse_pack,
        source_segment_inventory=args.source_segment_inventory,
        script_to_shot_execution_map=args.script_to_shot_execution_map,
        material_usage_ledger=args.material_usage_ledger,
        output_dir=args.output_dir,
    )
    print(json.dumps({"status": report["status"], "blocked_reasons": report["blocked_reasons"]}, ensure_ascii=False, indent=2))
    if report["status"] == "passed" or args.allow_blocked_exit_zero:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
