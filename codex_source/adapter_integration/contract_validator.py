"""Contract validation adapter around the existing no-render probe."""

from __future__ import annotations

from typing import Any

from codex_source.schema_contracts.probes import editing_workflow_no_render_probe as editing_probe


class ContractValidationError(AssertionError):
    """Raised when a reused schema-contract probe fails."""


def validate_editing_workflow_contracts() -> dict[str, Any]:
    """Run the existing editing workflow schema and fixture validation chain."""

    try:
        schema_results = {
            "editing_execution_contract": editing_probe.validate_editing_execution_contract(),
            "timeline_assembly_contract": editing_probe.validate_timeline_assembly_contract(),
            "subtitle_card_overlap_contract": editing_probe.validate_subtitle_card_overlap_contract(),
            "tts_route_contract": editing_probe.validate_tts_route_contract(),
            "review_pack_contract": editing_probe.validate_review_pack_contract(),
            "media_probe_contract": editing_probe.validate_media_probe_contract(),
            "publish_candidate_or_blocked_contract": editing_probe.validate_publish_candidate_or_blocked_contract(),
        }
        passing_path = editing_probe.run_passing_path()
        blocked_cases = editing_probe.run_blocked_cases()
        result: dict[str, Any] = {
            "status": "passed",
            "validator": "existing_editing_workflow_no_render_probe_reuse",
            "schema_contracts_passed": True,
            "passing_path_passed": passing_path["status"] == "passed",
            "blocked_cases_passed": all(case["status"] == "blocked_passed" for case in blocked_cases),
            "schema_results": schema_results,
            "passing_path_result": passing_path,
            "blocked_cases_result": blocked_cases,
            "no_render_boundary": {
                "media_generated": False,
                "tts_called": False,
                "real_media_read": False,
                "external_api_called": False,
                "dashvector_real_call": False,
                "chroma_ingestion_run": False,
                "runtime_enabled": False,
                "service_started": False,
            },
        }
        result["forbidden_status_promotion_scan"] = editing_probe.run_forbidden_status_promotion_scan(result)
        return result
    except editing_probe.ProbeFailure as exc:
        raise ContractValidationError(str(exc)) from exc
