"""Workflow registry for the branch-local adapter candidate."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable


REQUIRED_WORKFLOWS: tuple[str, ...] = (
    "copy_to_video_workflow",
    "material_audit_workflow",
    "editing_execution_workflow",
    "operation_data_review_workflow",
    "reference_to_execution_workflow",
    "adapter_infrastructure_workflow",
)


@dataclass(frozen=True)
class WorkflowDefinition:
    name: str
    native_route: str
    task_types: tuple[str, ...]
    responsibility_layers: tuple[str, ...]
    must_read_files: tuple[str, ...]
    expected_outputs: tuple[str, ...]
    blocked_if: tuple[str, ...]
    no_render_supported: bool = True

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


BASE_MUST_READ_FILES: tuple[str, ...] = (
    "AGENTS.md",
    "codex_log/latest.md",
    "codex_source/00_codex_readme.md",
    "codex_source/01_execution_rules.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
)


EDITING_CONTRACT_FILES: tuple[str, ...] = (
    "codex_source/schema_contracts/00_schema_contracts_index.md",
    "codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py",
    "codex_source/schema_contracts/schemas/editing_execution_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/timeline_assembly_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/subtitle_card_overlap_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/tts_route_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/review_pack_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/media_probe_contract.schema.yaml",
    "codex_source/schema_contracts/schemas/publish_candidate_or_blocked_contract.schema.yaml",
    "codex_source/schema_contracts/fixtures/passing/editing_execution_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/timeline_assembly_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/subtitle_card_overlap_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/tts_route_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/review_pack_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/media_probe_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/passing/publish_candidate_or_blocked_contract.passing.yaml",
    "codex_source/schema_contracts/fixtures/blocked/editing_missing_script_to_timeline_map.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/editing_technical_preview_as_completed.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/timeline_visual_mismatch.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/subtitle_card_high_overlap.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/tts_fallback_unauthorized.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/review_pack_missing.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/media_probe_invalid.blocked.yaml",
    "codex_source/schema_contracts/fixtures/blocked/publish_candidate_state_promotion.blocked.yaml",
)


_WORKFLOWS: dict[str, WorkflowDefinition] = {
    "copy_to_video_workflow": WorkflowDefinition(
        name="copy_to_video_workflow",
        native_route="copy_testing_flow",
        task_types=("copywriting", "video_sample_or_assembly"),
        responsibility_layers=("project_judgment_layer", "execution_layer"),
        must_read_files=BASE_MUST_READ_FILES
        + (
            "GPT数据源/04_选题与文案规则.md",
            "GPT数据源/05_文案路由规则.md",
            "GPT数据源/07_AI知识类视频价值规则.md",
        ),
        expected_outputs=("locked_copy_contract", "script_anchor_map", "copy_to_video_handoff"),
        blocked_if=("locked_copy_missing", "material_evidence_missing", "copy_semantic_change_requested"),
    ),
    "material_audit_workflow": WorkflowDefinition(
        name="material_audit_workflow",
        native_route="material_evidence_flow",
        task_types=("review_diagnosis_audit", "project_file_change"),
        responsibility_layers=("project_judgment_layer", "validation_layer"),
        must_read_files=BASE_MUST_READ_FILES
        + (
            "GPT数据源/05_文案路由规则.md",
            "GPT数据源/07_AI知识类视频价值规则.md",
        ),
        expected_outputs=("material_delta_type", "source_segment_inventory", "material_evidence_contract"),
        blocked_if=("source_segment_inventory_missing", "timecode_missing", "weak_evidence_only"),
    ),
    "editing_execution_workflow": WorkflowDefinition(
        name="editing_execution_workflow",
        native_route="aesthetic_editing_flow",
        task_types=("video_sample_or_assembly", "code_debug"),
        responsibility_layers=("execution_layer", "validation_layer"),
        must_read_files=BASE_MUST_READ_FILES + EDITING_CONTRACT_FILES,
        expected_outputs=("no_render_timeline_check", "editing_contract_validation", "completion_truth_check"),
        blocked_if=("line_group_mapping_missing", "high_overlap_detected", "review_pack_missing"),
    ),
    "operation_data_review_workflow": WorkflowDefinition(
        name="operation_data_review_workflow",
        native_route="data_review_flow",
        task_types=("data_review_loop", "review_diagnosis_audit"),
        responsibility_layers=("project_judgment_layer", "validation_layer"),
        must_read_files=BASE_MUST_READ_FILES
        + (
            "codex_log/current_operation_target.md",
            "review_loop/operation_records_index.md",
            "codex_log/current_data_goal_anchor.md",
        ),
        expected_outputs=("operation_data_record", "threshold_check", "next_variable_draft"),
        blocked_if=("video_id_missing", "time_window_missing", "insufficient_data_for_decision"),
    ),
    "reference_to_execution_workflow": WorkflowDefinition(
        name="reference_to_execution_workflow",
        native_route="mechanism_repair_flow",
        task_types=("review_diagnosis_audit", "video_sample_or_assembly"),
        responsibility_layers=("project_judgment_layer", "execution_layer"),
        must_read_files=BASE_MUST_READ_FILES
        + (
            "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
            "codex_source/20_reference_to_execution_contract.md",
        ),
        expected_outputs=("reference_intake_card", "execution_boundary", "blocked_reference_gap_report"),
        blocked_if=("reference_source_missing", "quality_rule_unclear", "reference_claim_overwrites_copy"),
    ),
    "adapter_infrastructure_workflow": WorkflowDefinition(
        name="adapter_infrastructure_workflow",
        native_route="mechanism_repair_flow",
        task_types=("mechanism_or_route_fix", "code_debug"),
        responsibility_layers=("mechanism_fix_layer", "execution_layer", "validation_layer"),
        must_read_files=BASE_MUST_READ_FILES
        + (
            "codex_source/schema_contracts/00_schema_contracts_index.md",
            "codex_log/framework_adapter/20260616_agent_service_toolkit_full_integration_master_plan.md",
            "codex_log/framework_adapter/20260616_editing_workflow_no_render_probe_report.md",
        ),
        expected_outputs=("workflow_registry", "task_packet", "no_render_adapter_runner", "round2_report"),
        blocked_if=("branch_mismatch", "runtime_or_service_requested", "external_api_required"),
    ),
}


def list_workflows() -> tuple[WorkflowDefinition, ...]:
    return tuple(_WORKFLOWS[name] for name in REQUIRED_WORKFLOWS)


def get_workflow(name: str) -> WorkflowDefinition:
    try:
        return _WORKFLOWS[name]
    except KeyError as exc:
        raise ValueError(f"unknown workflow: {name}") from exc


def validate_required_workflows(names: Iterable[str] | None = None) -> dict[str, object]:
    observed = tuple(names) if names is not None else tuple(_WORKFLOWS)
    missing = [name for name in REQUIRED_WORKFLOWS if name not in observed]
    extras = [name for name in observed if name not in REQUIRED_WORKFLOWS]
    return {
        "status": "passed" if not missing else "failed",
        "required_workflows": list(REQUIRED_WORKFLOWS),
        "registered_workflows": list(observed),
        "missing_workflows": missing,
        "extra_workflows": extras,
    }
