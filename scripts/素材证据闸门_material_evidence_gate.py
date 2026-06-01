#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA_SIGNALS = [
    "播放",
    "点赞",
    "收藏",
    "完播",
    "留存",
    "跳出",
    "平均观看",
    "主页访问",
    "私信",
    "咨询",
    "%",
]
JUDGMENT_SIGNALS = ["判断", "不是", "不能", "不等于", "说明", "更像", "方向", "失败", "价值", "有用"]
ACTION_SIGNALS = ["点击", "打开", "进入", "输入", "复制", "运行", "生成", "执行", "配置", "记录", "拆", "改完看"]
BOUNDARY_SIGNALS = ["不能说", "不能直接", "不保证", "不得", "还不能", "不代表", "待确认", "缺失"]
PROCESS_SIGNALS = ["第一步", "第二步", "第三步", "第四步", "第五步", "第六步", "流程", "字段", "模板", "报告"]
EVIDENCE_SIGNALS = ["截图", "素材", "画面", "显示", "页面", "按钮", "结果", "数据"]

CARD_ROLES = {
    "judgment_card",
    "summary_card",
    "ending_summary_card",
    "boundary_card",
    "data_result_card",
    "result_diff_card",
    "generated_card",
    "hyperframes_card",
    "process_summary_card",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def split_md_table_row(line: str) -> list[str]:
    return [cell.strip().replace("`", "") for cell in line.strip().strip("|").split("|")]


def parse_time_range(value: str) -> tuple[float | None, float | None]:
    value = value.strip()
    if value in {"", "card"}:
        return None, None
    match = re.search(r"(\d{2}):(\d{2})\s*[-–]\s*(\d{2}):(\d{2})", value)
    if match:
        sm, ss, em, es = [int(part) for part in match.groups()]
        return sm * 60 + ss, em * 60 + es
    match = re.search(r"(\d{2}):(\d{2}):(\d{2})\s*[-–]\s*(\d{2}):(\d{2}):(\d{2})", value)
    if match:
        sh, sm, ss, eh, em, es = [int(part) for part in match.groups()]
        return sh * 3600 + sm * 60 + ss, eh * 3600 + em * 60 + es
    return None, None


def overlap_seconds(a: tuple[float | None, float | None], b: tuple[float | None, float | None]) -> float:
    if None in a or None in b:
        return 0.0
    start = max(float(a[0]), float(b[0]))
    end = min(float(a[1]), float(b[1]))
    return max(0.0, end - start)


def evidence_strength(value: str) -> str:
    lowered = value.lower()
    if "high" in lowered:
        return "direct"
    if "medium" in lowered:
        return "partial"
    if "low" in lowered:
        return "weak"
    if "not_evidence" in lowered:
        return "not_evidence"
    return "partial"


def classify_claim_type(text: str, strength: str) -> list[str]:
    types: list[str] = []
    if any(signal in text for signal in DATA_SIGNALS):
        types.append("data_visible")
    if any(signal in text for signal in ACTION_SIGNALS):
        types.append("workflow_step")
    if any(signal in text for signal in ["点击", "输入", "滚动", "停留", "复制", "切换", "选择"]):
        types.append("ui_action")
    if any(signal in text for signal in JUDGMENT_SIGNALS):
        types.append("ai_judgment_visible")
    if any(signal in text for signal in ["配置", "字段", "模板", "报告", "Definition of Done", "DoD"]):
        types.append("report_structure_visible")
    if any(signal in text for signal in ["结果", "截图", "播放", "收藏", "完播", "留存"]):
        types.append("result_page_visible")
    if not types or strength in {"weak", "not_evidence"}:
        types.append("background_context_only")
    return sorted(set(types))


def extract_bullets(block: str, key: str) -> list[str]:
    pattern = rf"`{re.escape(key)}`\s*:\s*([^\n]+)"
    match = re.search(pattern, block)
    if not match:
        return []
    raw = match.group(1).strip()
    return [part.strip(" ，。；;") for part in re.split(r"[；;]", raw) if part.strip()]


def parse_material_report(report_path: Path) -> dict[str, Any]:
    text = report_path.read_text(encoding="utf-8")
    blocks = re.split(r"\n###\s+(material_\d+)\n", text)
    materials: list[dict[str, Any]] = []
    for index in range(1, len(blocks), 2):
        material_id = blocks[index].strip()
        block = blocks[index + 1]
        file_match = re.search(r"file_name:\s*(.+)", block)
        source_file = file_match.group(1).strip() if file_match else material_id
        can_support = extract_bullets(block, "can_support")
        cannot_support = extract_bullets(block, "cannot_support")
        best_use = extract_bullets(block, "best_use")
        not_allowed_use = extract_bullets(block, "not_allowed_use")
        segments: list[dict[str, Any]] = []
        for line in block.splitlines():
            if not line.startswith("|") or "timecode" in line or "---" in line:
                continue
            cells = split_md_table_row(line)
            if len(cells) < 9:
                continue
            timecode, visible_content, user_action, readable_text, possible_copy_value, raw_strength, platform_risk, privacy_risk, uncertainty = cells[:9]
            start, end = parse_time_range(timecode)
            strength = evidence_strength(raw_strength)
            claim_text = " / ".join(part for part in [possible_copy_value, visible_content, readable_text] if part)
            claim_type = classify_claim_type(claim_text + user_action, strength)
            segments.append(
                {
                    "material_id": material_id,
                    "source_file": source_file,
                    "timecode_start": timecode.split("-")[0].strip(),
                    "timecode_end": timecode.split("-")[-1].strip() if "-" in timecode else timecode,
                    "timecode_range_seconds": [start, end],
                    "visible_content": visible_content,
                    "readable_text": readable_text,
                    "user_action": user_action,
                    "evidence_claims": [
                        {
                            "claim_id": f"{material_id}_{len(segments) + 1:03d}_claim",
                            "claim_text": claim_text,
                            "claim_type": claim_type,
                            "evidence_strength": strength,
                            "can_support": can_support,
                            "cannot_support": cannot_support,
                            "best_use": best_use,
                            "not_allowed_use": not_allowed_use,
                        }
                    ],
                    "platform_risk": platform_risk.lower(),
                    "privacy_risk": privacy_risk.lower(),
                    "public_safe": "high" not in privacy_risk.lower() and "blocked" not in platform_risk.lower(),
                    "uncertainty": uncertainty,
                }
            )
        materials.append(
            {
                "material_id": material_id,
                "source_file": source_file,
                "can_support": can_support,
                "cannot_support": cannot_support,
                "best_use": best_use,
                "not_allowed_use": not_allowed_use,
                "segments": segments,
            }
        )
    return {
        "schema": "material_evidence_contract.v1",
        "source_report": rel(report_path),
        "hard_rules": [
            "background_context_only cannot be direct evidence",
            "privacy_risk = high cannot be selected by default",
            "cannot_support blocks matching narration claims",
        ],
        "materials": materials,
        "material_evidence_contract": [
            segment for material in materials for segment in material["segments"]
        ],
    }


def line_groups_from_timeline(timeline: dict[str, Any]) -> list[dict[str, Any]]:
    groups = timeline.get("line_groups")
    if isinstance(groups, list):
        return groups
    groups = timeline.get("script_to_timeline_map", {}).get("line_groups")
    if isinstance(groups, list):
        return groups
    return []


def group_id(group: dict[str, Any]) -> str:
    return str(group.get("line_group_id") or group.get("id") or "")


def narration_text(group: dict[str, Any]) -> str:
    return str(group.get("narration_text") or group.get("text") or "")


def selected_visual_type(group: dict[str, Any]) -> str:
    required = str(group.get("required_material") or "")
    card_role = str(group.get("card_role") or group.get("visual_role") or "")
    if required.startswith("material_"):
        return "material_clip"
    if required == "generated_card":
        return "hyperframes_card" if card_role in CARD_ROLES else "generated_card"
    if required in {"card", "hyperframes_card"} or card_role in CARD_ROLES:
        return "hyperframes_card"
    return "no_visual"


def classify_line_group(text: str) -> str:
    if any(signal in text for signal in BOUNDARY_SIGNALS):
        return "boundary_sentence"
    if any(signal in text for signal in DATA_SIGNALS) and re.search(r"\d|%", text):
        return "data_sentence"
    if any(signal in text for signal in JUDGMENT_SIGNALS):
        return "judgment_sentence"
    if any(signal in text for signal in ACTION_SIGNALS):
        return "action_sentence"
    if any(signal in text for signal in PROCESS_SIGNALS):
        return "process_sentence"
    if any(signal in text for signal in EVIDENCE_SIGNALS):
        return "evidence_sentence"
    return "transition_sentence"


def required_evidence_type(claim_type: str) -> str:
    if claim_type in {"judgment_sentence", "boundary_sentence"}:
        return "hyperframes_card"
    if claim_type in {"data_sentence", "action_sentence", "evidence_sentence", "process_sentence"}:
        return "direct_material_evidence"
    return "no_visual_proof_needed"


def find_segment(contract: dict[str, Any], material_id: str, source_timecode: str) -> dict[str, Any] | None:
    requested = parse_time_range(source_timecode)
    candidates = [
        segment
        for segment in contract["material_evidence_contract"]
        if segment.get("material_id") == material_id
    ]
    if not candidates:
        return None
    overlapping = [(overlap_seconds(requested, tuple(segment["timecode_range_seconds"])), segment) for segment in candidates]
    overlapping.sort(key=lambda item: item[0], reverse=True)
    if overlapping[0][0] > 0:
        return overlapping[0][1]
    return candidates[0]


def phrase_hit(text: str, phrases: list[str]) -> str | None:
    text = text.lower()
    for phrase in phrases:
        clean = phrase.strip().lower()
        if len(clean) >= 3 and clean in text:
            return phrase
    return None


def build_line_group_gate(contract: dict[str, Any], timeline: dict[str, Any], content_route_card: dict[str, Any] | None) -> dict[str, Any]:
    line_groups = line_groups_from_timeline(timeline)
    entries: list[dict[str, Any]] = []
    for group in line_groups:
        text = narration_text(group)
        claim_type = classify_line_group(text)
        visual_type = selected_visual_type(group)
        material_id = str(group.get("required_material") or "")
        source_timecode = str(group.get("source_timecode") or "")
        segment = find_segment(contract, material_id, source_timecode) if material_id.startswith("material_") else None
        claim = segment["evidence_claims"][0] if segment else None
        cannot_hit = phrase_hit(text, claim.get("cannot_support", []) if claim else [])
        privacy_high = bool(segment and "high" in str(segment.get("privacy_risk", "")).lower())
        evidence_strength_value = claim.get("evidence_strength") if claim else "not_evidence"
        direct_material = bool(segment and evidence_strength_value in {"direct", "partial"} and not cannot_hit and not privacy_high)
        card_resolved = visual_type in {"hyperframes_card", "generated_card"} and str(group.get("card_role") or group.get("visual_role") or "") not in {"", "none", "no_card"}

        status = "proxy_match"
        mismatch_risk = "low"
        blocked_if: list[str] = []
        if claim_type == "transition_sentence":
            status = "proxy_match" if visual_type == "material_clip" else "direct_match"
        elif claim_type in {"judgment_sentence", "boundary_sentence"}:
            if card_resolved:
                status = "card_required_resolved"
            elif direct_material:
                status = "direct_match"
            else:
                status = "card_required"
                blocked_if.append("card_required_unresolved")
        elif claim_type == "data_sentence":
            has_data_source = direct_material or bool(group.get("real_metric_values")) or str(group.get("data_source_status")) in {"verified", "provided", "not_data_group"}
            if card_resolved and has_data_source:
                status = "card_required_resolved"
            elif direct_material:
                status = "direct_match"
            else:
                status = "blocked_no_evidence"
                blocked_if.append("data_sentence_without_source")
        elif claim_type == "action_sentence":
            if direct_material and any(t in (claim.get("claim_type", []) if claim else []) for t in ["workflow_step", "ui_action", "report_structure_visible"]):
                status = "direct_match"
            elif card_resolved:
                status = "card_required_resolved"
            else:
                status = "blocked_no_evidence"
                blocked_if.append("action_sentence_without_card_or_direct_visual")
        else:
            status = "direct_match" if direct_material else ("card_required_resolved" if card_resolved else "proxy_match")

        if privacy_high:
            blocked_if.append("privacy_high_selected")
        if cannot_hit:
            blocked_if.append("selected_material_in_cannot_support")
        if status == "blocked_no_evidence":
            mismatch_risk = "high"
        elif status in {"card_required", "proxy_match"} and claim_type not in {"transition_sentence"}:
            mismatch_risk = "medium"
        elif privacy_high or cannot_hit:
            mismatch_risk = "high"
        else:
            mismatch_risk = "none" if status in {"direct_match", "card_required_resolved"} else "low"

        entries.append(
            {
                "line_group_id": group_id(group),
                "narration_text": text,
                "claim_summary": str(group.get("line_group_goal") or text[:80]),
                "claim_type": claim_type,
                "required_evidence_type": required_evidence_type(claim_type),
                "selected_visual_type": visual_type,
                "material_evidence_refs": [
                    {
                        "material_id": material_id,
                        "source_timecode": source_timecode,
                        "evidence_claim_id": claim.get("claim_id") if claim else None,
                        "evidence_strength": evidence_strength_value,
                        "can_support_quote": (claim.get("can_support") or [""])[0] if claim else "",
                        "cannot_support_check": cannot_hit or "passed",
                    }
                ]
                if material_id.startswith("material_")
                else [],
                "evidence_match_status": status,
                "mismatch_risk": mismatch_risk,
                "validation_rule": "material clip must map to a contract claim; card claims require resolved HyperFrames/generated card",
                "blocked_if": blocked_if,
            }
        )
    return {
        "schema": "line_group_evidence_gate.v1",
        "content_route_card_used": bool(content_route_card),
        "total_line_groups": len(entries),
        "line_group_evidence_gate": entries,
    }


def build_preflight(gate_report: dict[str, Any]) -> dict[str, Any]:
    entries = gate_report["line_group_evidence_gate"]
    counts = {
        "total_line_groups": len(entries),
        "total_line_groups_checked": len(entries),
        "direct_match_count": sum(1 for item in entries if item["evidence_match_status"] == "direct_match"),
        "proxy_match_count": sum(1 for item in entries if item["evidence_match_status"] == "proxy_match"),
        "card_required_count": sum(1 for item in entries if item["evidence_match_status"] == "card_required"),
        "card_required_resolved_count": sum(1 for item in entries if item["evidence_match_status"] == "card_required_resolved"),
        "blocked_no_evidence_count": sum(1 for item in entries if item["evidence_match_status"] == "blocked_no_evidence"),
        "high_mismatch_risk_count": sum(1 for item in entries if item["mismatch_risk"] == "high"),
        "privacy_high_selected_count": sum(1 for item in entries if "privacy_high_selected" in item["blocked_if"]),
        "data_sentence_without_source_count": sum(1 for item in entries if "data_sentence_without_source" in item["blocked_if"]),
        "judgment_sentence_hard_mapped_to_recording_count": sum(
            1
            for item in entries
            if item["claim_type"] == "judgment_sentence"
            and item["selected_visual_type"] == "material_clip"
            and item["evidence_match_status"] not in {"direct_match"}
        ),
        "action_sentence_without_card_or_direct_visual_count": sum(
            1 for item in entries if "action_sentence_without_card_or_direct_visual" in item["blocked_if"]
        ),
        "selected_material_in_cannot_support_count": sum(1 for item in entries if "selected_material_in_cannot_support" in item["blocked_if"]),
        "card_required_unresolved_count": sum(1 for item in entries if "card_required_unresolved" in item["blocked_if"]),
    }
    blocked_reasons = [
        key
        for key in [
            "blocked_no_evidence_count",
            "high_mismatch_risk_count",
            "privacy_high_selected_count",
            "data_sentence_without_source_count",
            "judgment_sentence_hard_mapped_to_recording_count",
            "action_sentence_without_card_or_direct_visual_count",
            "selected_material_in_cannot_support_count",
            "card_required_unresolved_count",
        ]
        if counts[key] > 0
    ]
    return {
        "schema": "auto_storyboard_preflight_report.v1",
        "auto_storyboard_preflight_report": {
            "auto_edit_allowed": not blocked_reasons and counts["total_line_groups_checked"] == counts["total_line_groups"],
            "video_execution_blocked": bool(blocked_reasons),
            **counts,
            "blocked_reasons": blocked_reasons,
            "high_risk_line_groups": [
                item["line_group_id"] for item in entries if item["mismatch_risk"] == "high" or item["blocked_if"]
            ],
            "card_required_resolved_groups": [
                item["line_group_id"] for item in entries if item["evidence_match_status"] == "card_required_resolved"
            ],
        },
    }


def assert_render_allowed(preflight: dict[str, Any]) -> None:
    report = preflight.get("auto_storyboard_preflight_report", preflight)
    if report.get("auto_edit_allowed") is not True:
        raise RuntimeError(
            json.dumps(
                {
                    "status": "blocked_evidence_preflight_failed",
                    "blocked_reasons": report.get("blocked_reasons", []),
                    "high_risk_line_groups": report.get("high_risk_line_groups", []),
                },
                ensure_ascii=False,
            )
        )


def run_material_evidence_gate(
    *,
    material_report: Path,
    timeline: Path,
    output_dir: Path,
    content_route_card: Path | None = None,
) -> dict[str, Any]:
    contract = parse_material_report(material_report)
    timeline_payload = read_json(timeline)
    content_payload = read_json(content_route_card) if content_route_card and content_route_card.exists() else None
    gate_report = build_line_group_gate(contract, timeline_payload, content_payload)
    preflight = build_preflight(gate_report)
    write_json(output_dir / "material_evidence_contract.json", contract)
    write_json(output_dir / "line_group_evidence_gate_report.json", gate_report)
    write_json(output_dir / "auto_storyboard_preflight_report.json", preflight)
    return {
        "material_evidence_contract": contract,
        "line_group_evidence_gate_report": gate_report,
        "auto_storyboard_preflight_report": preflight,
        "output_dir": str(output_dir),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the default material evidence gate before video rendering.")
    parser.add_argument("--material-report", required=True, type=Path)
    parser.add_argument("--timeline", required=True, type=Path)
    parser.add_argument("--content-route-card", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Generate gate reports without rendering or modifying media.")
    parser.add_argument("--require-pass", action="store_true", help="Exit non-zero when auto_edit_allowed is false.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_material_evidence_gate(
        material_report=args.material_report,
        timeline=args.timeline,
        content_route_card=args.content_route_card,
        output_dir=args.output_dir,
    )
    preflight = result["auto_storyboard_preflight_report"]
    if args.require_pass:
        assert_render_allowed(preflight)
    report = preflight["auto_storyboard_preflight_report"]
    print(
        json.dumps(
            {
                "status": "passed" if report["auto_edit_allowed"] else "blocked",
                "dry_run": bool(args.dry_run),
                "output_dir": str(args.output_dir),
                "auto_edit_allowed": report["auto_edit_allowed"],
                "total_line_groups": report["total_line_groups"],
                "blocked_reasons": report["blocked_reasons"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
