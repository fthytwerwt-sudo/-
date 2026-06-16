"""In-process runtime entry for the branch-local adapter candidate."""

from __future__ import annotations

from typing import Any

from .completion_truth import evaluate_completion_claim, run_false_completion_guards
from .contract_validator import validate_editing_workflow_contracts
from .editing_workflow_runner import run_editing_workflow_no_render
from .task_cleaner import SAMPLE_INPUTS, clean_task
from .workflow_router import route_task


RUNTIME_FINAL_STATE = "branch_local_runtime_service_probe_completed"

RUNTIME_NO_RENDER_BOUNDARIES: dict[str, bool] = {
    "writes_repo": False,
    "calls_external_api": False,
    "generates_media": False,
    "starts_service": False,
    "repo_write_attempted": False,
    "external_api_called": False,
    "media_generated": False,
    "tts_called": False,
    "real_media_read": False,
    "dashvector_real_call": False,
    "chroma_ingestion_run": False,
    "main_branch_modified": False,
}


def resolve_runtime_input(raw_user_input: str | None = None, sample_key: str | None = None) -> tuple[str, str | None]:
    if sample_key is not None:
        try:
            return SAMPLE_INPUTS[sample_key], sample_key
        except KeyError as exc:
            raise ValueError(f"unknown sample_key: {sample_key}") from exc
    if not raw_user_input:
        raise ValueError("raw_user_input or sample_key is required")
    return raw_user_input, None


def build_route_decision(packet: Any) -> dict[str, Any]:
    return {
        "project_route": packet.project_route,
        "task_type": list(packet.task_type),
        "workflow": packet.workflow,
        "native_workflow_route": packet.native_workflow_route,
        "responsibility_layer": list(packet.responsibility_layer),
        "execution_permission": "branch_local_runtime_service_probe_only",
        "stopline": RUNTIME_FINAL_STATE,
        "source_readback_status": packet.source_readback_status,
        "deepseek_trigger_decision": packet.deepseek_trigger_decision,
        "not_deepseek_conclusion": packet.not_deepseek_conclusion,
    }


def run_runtime_entry(raw_user_input: str | None = None, sample_key: str | None = None) -> dict[str, Any]:
    resolved_input, resolved_sample_key = resolve_runtime_input(raw_user_input, sample_key)
    cleaned = clean_task(resolved_input)
    packet = route_task(resolved_input)

    validation_result: dict[str, Any]
    if packet.workflow == "editing_execution_workflow":
        validation_result = run_editing_workflow_no_render(packet)
    else:
        validation_result = {
            "status": "passed",
            "validator": "route_only_no_render_runtime_entry",
            "workflow": packet.workflow,
            "contract_validation": "not_applicable_for_non_editing_sample",
            "repo_write_attempted": False,
            "external_api_called": False,
            "media_generated": False,
        }

    # The runtime entry still calls the contract validator explicitly, but only
    # for the editing workflow family where these static contracts apply.
    contract_validator_result: dict[str, Any] | None = None
    if packet.workflow == "editing_execution_workflow":
        contract_validator_result = validate_editing_workflow_contracts()

    false_completion_guards = run_false_completion_guards()
    completion_truth_result = {
        "status": "passed" if false_completion_guards["status"] == "passed" else "blocked",
        "final_state": RUNTIME_FINAL_STATE,
        "claim_check": evaluate_completion_claim(
            "branch_local_runtime_probe_claim",
            {"workflow": packet.workflow, "sample_key": resolved_sample_key or cleaned.intent},
        ),
        "false_completion_guards": false_completion_guards,
        "allowed_meaning": "branch-local runtime and service boundary probe only",
    }

    return {
        "runtime_entry": "codex_source/adapter_integration/runtime_entry.py",
        "sample_key": resolved_sample_key,
        "raw_input": resolved_input,
        "cleaned_task": cleaned.to_dict(),
        "task_packet": packet.to_dict(),
        "route_decision": build_route_decision(packet),
        "validation_result": validation_result,
        "contract_validator_result": contract_validator_result,
        "completion_truth_result": completion_truth_result,
        "no_render_boundaries": dict(RUNTIME_NO_RENDER_BOUNDARIES),
        "repo_write_attempted": False,
        "external_api_called": False,
        "media_generated": False,
        "status": "passed" if validation_result.get("status") == "passed" else "blocked",
    }
