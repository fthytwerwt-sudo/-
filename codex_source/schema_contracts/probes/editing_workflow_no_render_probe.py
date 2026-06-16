#!/usr/bin/env python3
"""No-render probe for the editing execution workflow contracts.

This probe intentionally avoids media generation, TTS calls, FFmpeg, external
APIs, runtime startup, service startup, vector-store access, and repository
writes. It reads the frozen editing workflow schemas and fixtures, then checks
that a static passing path reaches an allowed final state and that the blocked
fixtures are actually blocked.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_ROOT = REPO_ROOT / "codex_source" / "schema_contracts"
SCHEMA_ROOT = CONTRACT_ROOT / "schemas"
FIXTURE_ROOT = CONTRACT_ROOT / "fixtures"

SCHEMA_FILES = {
    "editing_execution_contract": "editing_execution_contract.schema.yaml",
    "timeline_assembly_contract": "timeline_assembly_contract.schema.yaml",
    "subtitle_card_overlap_contract": "subtitle_card_overlap_contract.schema.yaml",
    "tts_route_contract": "tts_route_contract.schema.yaml",
    "review_pack_contract": "review_pack_contract.schema.yaml",
    "media_probe_contract": "media_probe_contract.schema.yaml",
    "publish_candidate_or_blocked_contract": "publish_candidate_or_blocked_contract.schema.yaml",
}

PASSING_FIXTURES = {
    "editing_execution_contract": "passing/editing_execution_contract.passing.yaml",
    "timeline_assembly_contract": "passing/timeline_assembly_contract.passing.yaml",
    "subtitle_card_overlap_contract": "passing/subtitle_card_overlap_contract.passing.yaml",
    "tts_route_contract": "passing/tts_route_contract.passing.yaml",
    "review_pack_contract": "passing/review_pack_contract.passing.yaml",
    "media_probe_contract": "passing/media_probe_contract.passing.yaml",
    "publish_candidate_or_blocked_contract": "passing/publish_candidate_or_blocked_contract.passing.yaml",
}

BLOCKED_CASES = {
    "editing_missing_script_to_timeline_map": {
        "fixture": "blocked/editing_missing_script_to_timeline_map.blocked.yaml",
        "expected_reason": "missing_script_to_timeline_map",
    },
    "editing_technical_preview_as_completed": {
        "fixture": "blocked/editing_technical_preview_as_completed.blocked.yaml",
        "expected_reason": "technical_preview_only",
    },
    "timeline_visual_mismatch": {
        "fixture": "blocked/timeline_visual_mismatch.blocked.yaml",
        "expected_reason": "timeline_visual_mismatch",
    },
    "subtitle_card_high_overlap": {
        "fixture": "blocked/subtitle_card_high_overlap.blocked.yaml",
        "expected_reason": "subtitle_card_high_overlap",
    },
    "tts_fallback_unauthorized": {
        "fixture": "blocked/tts_fallback_unauthorized.blocked.yaml",
        "expected_reason": "tts_fallback_without_authorization",
    },
    "review_pack_missing": {
        "fixture": "blocked/review_pack_missing.blocked.yaml",
        "expected_reason": "review_pack_missing",
    },
    "media_probe_invalid": {
        "fixture": "blocked/media_probe_invalid.blocked.yaml",
        "expected_reason": "media_probe_invalid",
    },
    "publish_candidate_state_promotion": {
        "fixture": "blocked/publish_candidate_state_promotion.blocked.yaml",
        "expected_reason": "final_state_outside_allowed_states",
    },
}

ALLOWED_FINAL_STATES = {
    "publish_candidate_ready_for_human_review",
    "blocked_publish_candidate_unavailable",
}


try:
    import yaml as _yaml  # type: ignore
except Exception:  # pragma: no cover - exercised only when PyYAML is absent.
    _yaml = None


class ProbeFailure(AssertionError):
    """Raised when an editing workflow contract or fixture fails validation."""


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise ProbeFailure(message)


def coerce_scalar(raw_value: str) -> Any:
    value = raw_value.strip()
    if not value:
        return ""
    if value in {"true", "false"}:
        return value == "true"
    if value in {"[]", "[ ]"}:
        return []
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def fallback_yaml_parse(text: str) -> dict[str, Any]:
    """Parse the simple mapping/list subset used by these static fixtures."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    key_stack: list[tuple[int, str]] = []
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if line.startswith("- "):
            value = coerce_scalar(line[2:].strip())
            if not isinstance(parent, list):
                raise ProbeFailure("fallback YAML parser found list item under non-list parent")
            parent.append(value)
            continue
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        while key_stack and indent <= key_stack[-1][0]:
            key_stack.pop()
        if raw_value:
            parent[key] = coerce_scalar(raw_value)
            continue
        next_container: Any = {}
        parent[key] = next_container
        stack.append((indent, next_container))
        key_stack.append((indent, key))
        # Convert mapping to list lazily if the next meaningful child is a list.
        # The current fixtures parse with PyYAML in normal use; this fallback only
        # keeps the script runnable for the shallow fields used below.
    return root


def load_yaml_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ProbeFailure(f"missing YAML file: {path.relative_to(REPO_ROOT)}")
    text = path.read_text(encoding="utf-8")
    if _yaml is not None:
        data = _yaml.safe_load(text)
    else:
        data = fallback_yaml_parse(text)
    if not isinstance(data, dict):
        raise ProbeFailure(f"YAML did not parse to a mapping: {path.relative_to(REPO_ROOT)}")
    return data


def load_schema(name: str) -> dict[str, Any]:
    return load_yaml_file(SCHEMA_ROOT / SCHEMA_FILES[name])


def load_fixture(relative_path: str) -> dict[str, Any]:
    data = load_yaml_file(FIXTURE_ROOT / relative_path)
    data["_fixture_path"] = relative_path
    return data


def validate_required_keys(data: dict[str, Any], required_keys: list[str], label: str) -> None:
    missing = [key for key in required_keys if key not in data]
    expect(not missing, f"{label}: missing required keys: {missing}")


def validate_schema_basics(schema: dict[str, Any], contract_name: str, label: str) -> None:
    validate_required_keys(schema, ["contract_name", "version", "status", "project_route"], label)
    expect(schema["contract_name"] == contract_name, f"{label}: unexpected contract_name")
    expect(schema["project_route"] == "video_factory", f"{label}: unexpected project_route")
    hard_rules = schema.get("hard_rules", {})
    expect(isinstance(hard_rules, dict), f"{label}: hard_rules must be a mapping")
    if "runtime_write_allowed" in hard_rules:
        expect(hard_rules["runtime_write_allowed"] is False, f"{label}: runtime_write_allowed must remain false")


def validate_editing_execution_contract() -> dict[str, Any]:
    schema = load_schema("editing_execution_contract")
    validate_schema_basics(schema, "editing_execution_contract", "editing_execution_contract")
    validate_required_keys(schema, ["required_inputs", "required_outputs", "done_when", "blocked_if"], "editing_execution_contract")
    for key in ("runtime_enabled", "service_started", "locked_copy_semantic_change_allowed"):
        expect(schema["hard_rules"].get(key) is False, f"editing_execution_contract: {key} must be false")
    allowed = set(schema["done_when"].get("allowed_final_states", []))
    expect(ALLOWED_FINAL_STATES.issubset(allowed), "editing_execution_contract: allowed final states incomplete")
    return {"status": "passed", "required_inputs": schema["required_inputs"], "required_outputs": schema["required_outputs"]}


def validate_timeline_assembly_contract() -> dict[str, Any]:
    schema = load_schema("timeline_assembly_contract")
    validate_schema_basics(schema, "timeline_assembly_contract", "timeline_assembly_contract")
    expected = ["line_group_id", "source_segment_id", "source_timecode", "timeline_slot", "visual_role", "evidence_role", "allowed_visuals", "forbidden_visuals", "blocked_if_visual_mismatch"]
    expect(set(expected).issubset(set(schema.get("required_field_names", []))), "timeline_assembly_contract: required fields incomplete")
    expect(schema["hard_rules"].get("paragraph_only_mapping_allowed") is False, "timeline_assembly_contract: paragraph-only mapping must be disallowed")
    return {"status": "passed", "required_field_count": len(expected)}


def validate_subtitle_card_overlap_contract() -> dict[str, Any]:
    schema = load_schema("subtitle_card_overlap_contract")
    validate_schema_basics(schema, "subtitle_card_overlap_contract", "subtitle_card_overlap_contract")
    expected = ["subtitle_region", "card_region", "evidence_region", "overlap_severity", "repair_action", "blocked_if_high_severity_overlap"]
    expect(set(expected).issubset(set(schema.get("required_field_names", []))), "subtitle_card_overlap_contract: required fields incomplete")
    expect(schema["hard_rules"].get("high_severity_overlap_allowed") is False, "subtitle_card_overlap_contract: high overlap must be disallowed")
    return {"status": "passed", "required_field_count": len(expected)}


def validate_tts_route_contract() -> dict[str, Any]:
    schema = load_schema("tts_route_contract")
    validate_schema_basics(schema, "tts_route_contract", "tts_route_contract")
    expected = ["actual_tts_provider", "actual_tts_model", "actual_voice_id", "expected_voice_id", "fallback_used", "fallback_authorized", "audio_present", "non_silent", "blocked_if_route_mismatch"]
    expect(set(expected).issubset(set(schema.get("required_field_names", []))), "tts_route_contract: required fields incomplete")
    expect(schema["hard_rules"].get("unauthorized_fallback_allowed") is False, "tts_route_contract: unauthorized fallback must be disallowed")
    expect(schema["hard_rules"].get("silent_audio_allowed") is False, "tts_route_contract: silent audio must be disallowed")
    return {"status": "passed", "required_field_count": len(expected)}


def validate_review_pack_contract() -> dict[str, Any]:
    schema = load_schema("review_pack_contract")
    validate_schema_basics(schema, "review_pack_contract", "review_pack_contract")
    expected = ["full_video_path", "summary_report", "preflight_reports", "media_probe", "remaining_blockers", "human_review_required", "blocked_if_missing_review_pack"]
    expect(set(expected).issubset(set(schema.get("required_field_names", []))), "review_pack_contract: required fields incomplete")
    expect(schema["hard_rules"].get("human_review_required_for_candidate") is True, "review_pack_contract: human review boundary required")
    return {"status": "passed", "required_field_count": len(expected)}


def validate_media_probe_contract() -> dict[str, Any]:
    schema = load_schema("media_probe_contract")
    validate_schema_basics(schema, "media_probe_contract", "media_probe_contract")
    expected = ["video_exists", "audio_present", "non_silent", "subtitle_present", "resolution", "duration", "decode_passed", "blocked_if_media_invalid"]
    expect(set(expected).issubset(set(schema.get("required_field_names", []))), "media_probe_contract: required fields incomplete")
    expect(schema["hard_rules"].get("silent_video_as_candidate_allowed") is False, "media_probe_contract: silent video must be disallowed")
    return {"status": "passed", "required_field_count": len(expected)}


def validate_publish_candidate_or_blocked_contract() -> dict[str, Any]:
    schema = load_schema("publish_candidate_or_blocked_contract")
    validate_schema_basics(schema, "publish_candidate_or_blocked_contract", "publish_candidate_or_blocked_contract")
    allowed = set(schema.get("allowed_final_states", []))
    expect(ALLOWED_FINAL_STATES == allowed, "publish_candidate_or_blocked_contract: final state set must be exact")
    expect(schema["hard_rules"].get("review_pack_required") is True, "publish_candidate_or_blocked_contract: review pack required")
    expect(schema["hard_rules"].get("completion_truth_check_required") is True, "publish_candidate_or_blocked_contract: completion truth check required")
    return {"status": "passed", "allowed_final_states": sorted(allowed)}


def sample_from_fixture(data: dict[str, Any], label: str) -> dict[str, Any]:
    sample = data.get("sample")
    expect(isinstance(sample, dict), f"{label}: sample must be a mapping")
    return sample


def require_passing_fixture(name: str) -> dict[str, Any]:
    fixture = load_fixture(PASSING_FIXTURES[name])
    expect(fixture.get("case_type（样例类型）") == "passing", f"{name}: expected passing case")
    expect(fixture.get("expected_result（预期结果）") == "pass", f"{name}: expected_result must be pass")
    sample = sample_from_fixture(fixture, name)
    expect(sample.get("blocked") is False, f"{name}: passing sample must not be blocked")
    return sample


def run_passing_path() -> dict[str, Any]:
    editing = require_passing_fixture("editing_execution_contract")
    outputs = editing.get("outputs", {})
    expect(isinstance(outputs, dict), "editing passing fixture: outputs must be a mapping")
    timeline = require_passing_fixture("timeline_assembly_contract")
    overlap = require_passing_fixture("subtitle_card_overlap_contract")
    tts = require_passing_fixture("tts_route_contract")
    review_pack = require_passing_fixture("review_pack_contract")
    media_probe = require_passing_fixture("media_probe_contract")
    publish = require_passing_fixture("publish_candidate_or_blocked_contract")

    requirements = {
        "locked_copy_contract_present": editing.get("locked_copy_contract") == "present",
        "script_to_timeline_map_present": editing.get("script_to_timeline_map") == "line_group_level",
        "tts_prosody_anchor_map_present": editing.get("tts_prosody_anchor_map") == "present",
        "card_placement_decision_present": editing.get("card_placement_decision") == "present",
        "material_evidence_contract_present": editing.get("material_evidence_contract") == "present",
        "material_usage_ledger_present": editing.get("material_usage_ledger") == "present",
        "data_goal_anchor_present": editing.get("data_goal_anchor") == "present",
        "timeline_present": outputs.get("timeline") == "present" and bool(timeline.get("line_group_id")),
        "subtitle_present": outputs.get("subtitle") == "present",
        "audio_present": outputs.get("audio") == "present" and tts.get("audio_present") is True,
        "cards_decision_present": outputs.get("cards") == "present",
        "review_pack_present": outputs.get("review_pack") == "present" and bool(review_pack.get("summary_report")),
        "media_probe_valid": all(media_probe.get(key) is True for key in ("video_exists", "audio_present", "non_silent", "subtitle_present", "decode_passed")),
        "completion_truth_check_present": outputs.get("completion_truth_check") == "present" and publish.get("completion_truth_check") == "present",
        "final_state_allowed": editing.get("final_state") in ALLOWED_FINAL_STATES and publish.get("final_state") in ALLOWED_FINAL_STATES,
    }
    failed = [key for key, passed in requirements.items() if not passed]
    expect(not failed, f"passing path failed requirements: {failed}")
    expect(overlap.get("overlap_severity") != "high", "passing path: overlap severity cannot be high")
    expect(tts.get("fallback_used") is False, "passing path: fallback must not be used")
    expect(tts.get("actual_voice_id") == tts.get("expected_voice_id"), "passing path: actual and expected voice ids must match")
    expect(review_pack.get("human_review_required") is True, "passing path: candidate must keep human review boundary")
    return {
        "status": "passed",
        "final_state": publish["final_state"],
        "requirements": requirements,
        "fixtures_checked": sorted(PASSING_FIXTURES.values()),
    }


def require_blocked_fixture(case_name: str, spec: dict[str, str]) -> dict[str, Any]:
    fixture = load_fixture(spec["fixture"])
    expect(fixture.get("case_type（样例类型）") == "blocked", f"{case_name}: expected blocked case")
    expect(fixture.get("expected_result（预期结果）") == "blocked", f"{case_name}: expected_result must be blocked")
    sample = sample_from_fixture(fixture, case_name)
    expect(sample.get("blocked") is True, f"{case_name}: sample.blocked must be true")
    reasons = sample.get("blocked_reasons", [])
    expect(isinstance(reasons, list), f"{case_name}: blocked_reasons must be a list")
    expect(spec["expected_reason"] in reasons, f"{case_name}: missing expected reason {spec['expected_reason']!r}")
    return sample


def run_blocked_cases() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for case_name, spec in BLOCKED_CASES.items():
        sample = require_blocked_fixture(case_name, spec)
        if case_name == "editing_missing_script_to_timeline_map":
            expect(sample.get("script_to_timeline_map") == "missing", f"{case_name}: script map must be missing")
        elif case_name == "editing_technical_preview_as_completed":
            expect(sample.get("technical_preview_only") is True, f"{case_name}: technical preview flag must be true")
        elif case_name == "timeline_visual_mismatch":
            expect(sample.get("actual_visual") in sample.get("forbidden_visuals", []), f"{case_name}: actual visual must be forbidden")
        elif case_name == "subtitle_card_high_overlap":
            expect(sample.get("overlap_severity") == "high", f"{case_name}: overlap severity must be high")
        elif case_name == "tts_fallback_unauthorized":
            expect(sample.get("fallback_used") is True and sample.get("fallback_authorized") is False, f"{case_name}: unauthorized fallback expected")
        elif case_name == "review_pack_missing":
            expect(sample.get("summary_report") == "missing" and sample.get("media_probe") == "missing", f"{case_name}: review pack fields must be missing")
        elif case_name == "media_probe_invalid":
            expect(sample.get("decode_passed") is False and sample.get("audio_present") is False, f"{case_name}: invalid media probe expected")
        elif case_name == "publish_candidate_state_promotion":
            expect(sample.get("final_state") not in ALLOWED_FINAL_STATES, f"{case_name}: final state must be disallowed")
        results.append(
            {
                "case_name": case_name,
                "fixture": spec["fixture"],
                "expected": "blocked",
                "actual": "blocked",
                "expected_reason": spec["expected_reason"],
                "status": "blocked_passed",
            }
        )
    return results


def run_forbidden_status_promotion_scan(payload: dict[str, Any]) -> dict[str, Any]:
    forbidden_names = [
        ("runtime", "_enabled"),
        ("service", "_started"),
        ("main_branch", "_modified"),
        ("formal", "_integration", "_completed"),
        ("production", "_ready"),
        ("content", "_validation", "_passed"),
        ("send", "_ready", "_true"),
        ("full", "_code", "_integration", "_ready"),
    ]
    names = ["".join(parts) for parts in forbidden_names]
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    hits = []
    for name in names:
        if f'"{name}": true' in serialized.lower():
            hits.append(name)
        if name in serialized and name not in {"runtime_enabled", "service_started", "main_branch_modified"}:
            hits.append(name)
    expect(not hits, f"forbidden status promotion detected: {sorted(set(hits))}")
    return {
        "status": "passed",
        "forbidden_status_values_detected": [],
    }


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "editing_workflow_no_render_probe",
        "probe_date": "2026-06-16",
        "project_route": "video_factory",
        "branch": "adapter/agent-service-toolkit-sandbox",
        "probe_scope": "static_fixture_no_render_only",
        "media_generated": False,
        "tts_called": False,
        "real_media_read": False,
        "runtime_enabled": False,
        "service_started": False,
        "external_api_called": False,
        "DashVector_real_call": False,
        "Chroma_ingestion_run": False,
        "main_branch_modified": False,
    }
    try:
        schema_results = {
            "editing_execution_contract": validate_editing_execution_contract(),
            "timeline_assembly_contract": validate_timeline_assembly_contract(),
            "subtitle_card_overlap_contract": validate_subtitle_card_overlap_contract(),
            "tts_route_contract": validate_tts_route_contract(),
            "review_pack_contract": validate_review_pack_contract(),
            "media_probe_contract": validate_media_probe_contract(),
            "publish_candidate_or_blocked_contract": validate_publish_candidate_or_blocked_contract(),
        }
        passing_path = run_passing_path()
        blocked_cases = run_blocked_cases()
        result.update(
            {
                "final_probe_status": "passed",
                "schema_contracts_passed": True,
                "passing_path_passed": passing_path["status"] == "passed",
                "blocked_cases_passed": all(case["status"] == "blocked_passed" for case in blocked_cases),
                "schema_results": schema_results,
                "passing_path_result": passing_path,
                "blocked_cases_result": blocked_cases,
            }
        )
        result["forbidden_status_promotion_scan"] = run_forbidden_status_promotion_scan(result)
    except ProbeFailure as exc:
        result.update(
            {
                "final_probe_status": "failed",
                "schema_contracts_passed": False,
                "passing_path_passed": False,
                "blocked_cases_passed": False,
                "failure": str(exc),
            }
        )
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
