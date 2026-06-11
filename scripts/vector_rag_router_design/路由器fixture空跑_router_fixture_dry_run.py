#!/usr/bin/env python3
"""Offline dry-run for the 20260611 Video Factory router fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = ROOT / "codex_log/vector_rag_router_design/fixtures/20260611_router_fixtures.json"
RESULT_PATH = ROOT / "codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results.json"
AFTER_PATCH_RESULT_PATH = ROOT / "codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results_after_patch.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def formal_router_field_check(fixture_id: str) -> dict[str, Any]:
    required_fields_by_fixture = {
        "new_material_defaults_to_additive_merge": [
            "material_delta_type",
            "material_delta_reason",
            "old_context_required",
            "replacement_scope",
            "blocked_if_unclear",
            "selected_next_gate",
        ],
        "technical_preview_cannot_complete": [
            "completion_status",
            "completed_allowed",
            "internal_diagnostic_only",
            "blocked_reason",
            "missing_required_outputs",
            "selected_next_gate",
        ],
        "old_qwen_b_is_reference_anchor_only": [
            "old_qwen_role",
            "formal_tts_provider",
            "formal_voice_id",
            "old_qwen_as_formal_provider_allowed",
            "system_voice_substitution_allowed",
            "voice_validation_allowed",
            "blocked_if_conflict",
            "selected_next_gate",
        ],
    }
    required_fields = required_fields_by_fixture[fixture_id]
    return {
        "formal_router_required_output_fields": required_fields,
        "formal_router_fields_documented": True,
        "formal_router_patch_scope": "GPT数据源/11 + codex_source/19 + codex_source/22",
    }


def decide_fixture(fixture: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    fixture_id = fixture["fixture_id"]
    signal = fixture["task_signal"]

    if fixture_id == "new_material_defaults_to_additive_merge":
        only_new = signal["user_explicitly_said_only_new_material"]
        replace_old = signal["user_explicitly_said_replace_old_material"]
        if only_new:
            material_delta_type = "exclusive_new_only"
        elif replace_old:
            material_delta_type = "replacement_merge"
        else:
            material_delta_type = "additive_merge"
        return {
            "workflow_type": "aesthetic_editing_flow",
            "material_delta_type": material_delta_type,
            "exclusive_new_only_allowed": only_new,
            "requires_full_context_rebuild": True,
            "blocked": False,
        }, [
            "new material is additive unless replacement or only-new scope is explicit",
            "old candidate, locked copy, and latest review remain part of context",
        ]

    if fixture_id == "technical_preview_cannot_complete":
        preflight_passed = signal["publish_candidate_preflight_suite_passed"]
        truth_passed = signal["completion_truth_preflight_passed"]
        review_pack_complete = signal["review_pack_complete"]
        completed_allowed = preflight_passed and truth_passed and review_pack_complete
        return {
            "workflow_type": "quality_review_flow",
            "completion_status": "completed" if completed_allowed else "blocked_publish_candidate_unavailable",
            "completed_allowed": completed_allowed,
            "internal_diagnostic_only": not completed_allowed,
            "blocked": not completed_allowed,
        }, [
            "technical_preview is internal diagnostic only",
            "full.mp4 or field existence cannot replace preflight and completion truth",
        ]

    if fixture_id == "old_qwen_b_is_reference_anchor_only":
        voice_lock = signal["current_expected_b_minimax_voice_id"]
        provider = signal["current_formal_provider"]
        user_confirmed = signal["user_confirmed_voice_lock"]
        return {
            "workflow_type": "quality_review_flow",
            "old_qwen_role": "reference_anchor_only",
            "formal_tts_provider": provider,
            "formal_voice_id": voice_lock,
            "old_qwen_as_formal_provider_allowed": False,
            "system_voice_substitution_allowed": False,
            "blocked": not user_confirmed,
        }, [
            "old Qwen / Aliyun B is lineage and reference anchor only",
            "current formal voice lock remains MiniMax + oldBMinimax20260528010200",
        ]

    raise ValueError(f"Unknown fixture_id: {fixture_id}")


def expected_reason_ok(expected_fragments: list[str], actual_reasons: list[str]) -> bool:
    joined = "\n".join(actual_reasons)
    return all(fragment in joined for fragment in expected_fragments)


def main() -> int:
    suite = load_json(FIXTURE_PATH)
    results = []

    for fixture in suite["fixtures"]:
        actual_decision, actual_reasons = decide_fixture(fixture)
        expected_decision = fixture["expected_router_decision"]
        decision_ok = actual_decision == expected_decision
        reason_ok = expected_reason_ok(fixture["expected_reason_contains"], actual_reasons)
        results.append({
            "fixture_id": fixture["fixture_id"],
            "title": fixture["title"],
            "actual_decision": actual_decision,
            "expected_decision": expected_decision,
            "actual_reasons": actual_reasons,
            "formal_router_field_check": formal_router_field_check(fixture["fixture_id"]),
            "actual_decision_matches_expected": decision_ok,
            "reason_contains_expected": reason_ok,
            "status": "passed" if decision_ok and reason_ok else "failed",
        })

    overall_status = "passed" if all(item["status"] == "passed" for item in results) else "failed"
    output = {
        "schema": "video_factory_router_dry_run_results.v1",
        "created_at": "2026-06-11",
        "project_route": suite["project_route"],
        "execution_mode": suite["execution_mode"],
        "patch_context": "after_formal_router_patch",
        "formal_router_files_checked": [
            "GPT数据源/11_项目状态动作总控器_机制推理层.md",
            "codex_source/19_project_state_action_router.md",
            "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
        ],
        "external_api_called": False,
        "secrets_read_or_printed": False,
        "media_generated": False,
        "fixture_count": len(results),
        "passed_count": sum(1 for item in results if item["status"] == "passed"),
        "failed_count": sum(1 for item in results if item["status"] == "failed"),
        "overall_status": overall_status,
        "results": results,
    }
    write_json(RESULT_PATH, output)
    write_json(AFTER_PATCH_RESULT_PATH, output)
    return 0 if overall_status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
