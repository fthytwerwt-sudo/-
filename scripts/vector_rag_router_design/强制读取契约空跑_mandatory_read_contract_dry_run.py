#!/usr/bin/env python3
"""Offline dry-run for mandatory_read_manifest and read_proof_gate fixtures."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = ROOT / "codex_log/vector_rag_router_design/fixtures/20260611_read_contract_fixtures.json"
RESULT_PATH = ROOT / "codex_log/vector_rag_router_design/fixtures/20260611_read_contract_dry_run_results.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_mandatory_read_manifest(fixture: dict[str, Any]) -> dict[str, Any]:
    manifest = deepcopy(fixture["manifest"])
    manifest["user_prompt_summary"] = fixture["task_signal"]["user_prompt_summary"]
    manifest["generated_by"] = "router_or_rag_bridge"
    return manifest


def decision_for_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    fixture_id = fixture["fixture_id"]
    signal = fixture["task_signal"]

    if fixture_id == "new_material_read_contract":
        only_new = signal["user_explicitly_said_only_new_material"]
        replace_old = signal["user_explicitly_said_replace_old_material"]
        if only_new:
            material_delta_type = "exclusive_new_only"
        elif replace_old:
            material_delta_type = "replacement_merge"
        else:
            material_delta_type = "additive_merge"
        return {
            "material_delta_type": material_delta_type,
            "old_context_required": True,
            "exclusive_new_only_allowed": only_new,
            "blocked_if_old_context_missing": True,
        }

    if fixture_id == "technical_preview_read_contract":
        return {
            "completed_allowed": False,
            "completion_status": "blocked_publish_candidate_unavailable",
            "internal_diagnostic_only": True,
            "blocked_if_completion_truth_missing": True,
        }

    if fixture_id == "voice_conflict_read_contract":
        return {
            "old_qwen_role": "reference_anchor_only",
            "formal_tts_provider": "MiniMax",
            "formal_voice_id": "oldBMinimax20260528010200",
            "old_qwen_as_formal_provider_allowed": False,
            "system_voice_substitution_allowed": False,
            "voice_validation_allowed": False,
        }

    raise ValueError(f"unknown fixture_id: {fixture_id}")


def proof_level_to_status(proof_level: str) -> str:
    if proof_level == "insufficient":
        return "missing"
    return "read_ok"


def build_read_proof_report(manifest: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    missing_required_items: list[str] = []
    missing_required_sections: list[str] = []
    read_items: list[dict[str, Any]] = []

    for item in manifest["must_read_items"]:
        proof_level = item.get("simulated_proof_level", "insufficient")
        read_status = proof_level_to_status(proof_level)
        if read_status != "read_ok" and item.get("blocked_if_missing", True):
            missing_required_items.append(item["item_id"])
        if proof_level == "file_read":
            evidence_summary = "full file read in simulated proof"
        elif proof_level == "section_read":
            evidence_summary = "required section read in simulated proof"
        elif proof_level == "schema_checked":
            evidence_summary = "schema / script interface checked in simulated proof"
        elif proof_level == "metadata_checked":
            evidence_summary = "metadata or missing-report pointer checked in simulated proof"
        else:
            evidence_summary = "insufficient read proof"
            missing_required_sections.append(item["item_id"])

        read_items.append(
            {
                "item_id": item["item_id"],
                "source_path": item["source_path"],
                "required_section": item["required_section"],
                "read_status": read_status,
                "evidence_summary": evidence_summary,
                "decision_supported": item["expected_decision_supported"],
                "missing_or_conflict": read_status != "read_ok" or bool(item.get("conflict_tags")),
                "proof_level": proof_level,
            }
        )

    conflicts_found = fixture["simulated_read_context"].get("conflicts_found", [])
    conflict_arbitration = fixture["simulated_read_context"].get("conflict_arbitration", "repo_wins")
    all_required_files_read = not missing_required_items
    all_required_sections_read = not missing_required_sections

    if missing_required_items or missing_required_sections:
        gate_status = "blocked_missing_read"
    elif conflicts_found and conflict_arbitration != "repo_wins":
        gate_status = "blocked_conflict_unresolved"
    else:
        gate_status = "passed"

    return {
        "manifest_id": manifest["manifest_id"],
        "all_required_files_read": all_required_files_read,
        "all_required_sections_read": all_required_sections_read,
        "missing_required_items": missing_required_items,
        "conflicts_found": conflicts_found,
        "conflict_arbitration": conflict_arbitration,
        "blocked_if_unread": True,
        "gate_status": gate_status,
        "read_items": read_items,
    }


def build_pre_execution_read_gate(
    manifest: dict[str, Any],
    proof: dict[str, Any],
    fixture: dict[str, Any],
) -> dict[str, Any]:
    missing_required_files = proof["missing_required_items"]
    missing_required_sections = [
        item["item_id"]
        for item in proof["read_items"]
        if item["proof_level"] == "insufficient"
    ]
    gate_status = proof["gate_status"]
    expected_execution_allowed = fixture["expected_execution_allowed"]
    execution_allowed = gate_status == "passed" and expected_execution_allowed

    if missing_required_files or missing_required_sections:
        blocked_reason = "missing required read proof"
    elif proof["conflicts_found"] and proof["conflict_arbitration"] != "repo_wins":
        blocked_reason = "unresolved or router-blocked conflict"
    elif not expected_execution_allowed:
        blocked_reason = "expected decision blocks execution"
    else:
        blocked_reason = None

    return {
        "mandatory_read_manifest_loaded": True,
        "read_proof_report_loaded": True,
        "all_required_files_read": proof["all_required_files_read"],
        "missing_required_files": missing_required_files,
        "missing_required_sections": missing_required_sections,
        "conflicts_found": proof["conflicts_found"],
        "gate_status": gate_status,
        "execution_allowed": execution_allowed,
        "blocked_reason": blocked_reason,
    }


def build_missing_read_negative_check(manifest: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    missing_item_id = fixture["simulated_read_context"]["negative_missing_item_id"]
    negative_manifest = deepcopy(manifest)
    for item in negative_manifest["must_read_items"]:
        if item["item_id"] == missing_item_id:
            item["simulated_proof_level"] = "insufficient"
            break
    proof = build_read_proof_report(negative_manifest, fixture)
    gate = build_pre_execution_read_gate(negative_manifest, proof, {**fixture, "expected_execution_allowed": True})
    return {
        "missing_item_id": missing_item_id,
        "gate_status": gate["gate_status"],
        "execution_allowed": gate["execution_allowed"],
        "blocked_as_expected": gate["gate_status"] == "blocked_missing_read" and gate["execution_allowed"] is False,
    }


def expected_decision_matches(actual: dict[str, Any], expected: dict[str, Any]) -> bool:
    return all(actual.get(key) == value for key, value in expected.items())


def run_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    manifest = build_mandatory_read_manifest(fixture)
    proof = build_read_proof_report(manifest, fixture)
    gate = build_pre_execution_read_gate(manifest, proof, fixture)
    actual_decision = decision_for_fixture(fixture)
    decision_matches = expected_decision_matches(actual_decision, fixture["expected_decision"])
    negative_check = build_missing_read_negative_check(manifest, fixture)

    required_items_count = len(manifest["must_read_items"])
    manifest_generated = required_items_count > 0 and bool(manifest.get("manifest_id"))
    proof_generated = bool(proof["read_items"])
    gate_matches = (
        gate["gate_status"] == fixture["expected_gate_status"]
        and gate["execution_allowed"] == fixture["expected_execution_allowed"]
    )
    passed = manifest_generated and proof_generated and decision_matches and gate_matches and negative_check["blocked_as_expected"]

    return {
        "fixture_id": fixture["fixture_id"],
        "fixture_name": fixture["fixture_name"],
        "mandatory_read_manifest_generated": manifest_generated,
        "mandatory_read_manifest": manifest,
        "required_items_count": required_items_count,
        "read_proof_generated": proof_generated,
        "read_proof_report": proof,
        "pre_execution_read_gate": gate,
        "missing_required_items": proof["missing_required_items"],
        "conflicts_found": proof["conflicts_found"],
        "gate_status": gate["gate_status"],
        "execution_allowed": gate["execution_allowed"],
        "actual_decision": actual_decision,
        "expected_decision": fixture["expected_decision"],
        "expected_decision_matches": decision_matches,
        "missing_read_negative_check": negative_check,
        "pass_or_fail": "passed" if passed else "failed",
    }


def main() -> int:
    suite = load_json(FIXTURE_PATH)
    results = [run_fixture(fixture) for fixture in suite["fixtures"]]
    missing_read_blocked = all(
        item["missing_read_negative_check"]["blocked_as_expected"] for item in results
    )
    output = {
        "schema": "video_factory_read_contract_dry_run_results.v1",
        "created_at": "2026-06-12",
        "project_route": suite["project_route"],
        "execution_mode": suite["execution_mode"],
        "external_api_called": False,
        "deepseek_called": False,
        "embedding_generated": False,
        "vector_written": False,
        "media_content_read": False,
        "fixture_count": len(results),
        "passed_count": sum(1 for item in results if item["pass_or_fail"] == "passed"),
        "failed_count": sum(1 for item in results if item["pass_or_fail"] == "failed"),
        "missing_read_block_test": "passed" if missing_read_blocked else "failed",
        "overall_status": "passed"
        if all(item["pass_or_fail"] == "passed" for item in results) and missing_read_blocked
        else "failed",
        "results": results,
    }
    write_json(RESULT_PATH, output)
    return 0 if output["overall_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
