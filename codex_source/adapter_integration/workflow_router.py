"""Route cleaned tasks into registered adapter workflows."""

from __future__ import annotations

from pathlib import Path

from .task_cleaner import clean_task
from .task_packet import NO_RENDER_CONSTRAINTS, STOPLINE, TaskPacket, make_task_id
from .workflow_registry import get_workflow


REPO_ROOT = Path(__file__).resolve().parents[2]


def read_status_for(paths: tuple[str, ...]) -> dict[str, str]:
    status: dict[str, str] = {}
    for path in paths:
        if "*" in path:
            status[path] = "read_ok_glob_not_expanded_in_packet"
            continue
        status[path] = "read_ok" if (REPO_ROOT / path).exists() else "missing"
    return status


def route_task(user_input: str) -> TaskPacket:
    cleaned = clean_task(user_input)
    workflow = get_workflow(cleaned.workflow)
    read_status = read_status_for(workflow.must_read_files)
    blocked_if = workflow.blocked_if
    if cleaned.intent == "unknown":
        blocked_if = ("unrecognized_input_requires_manual_route_review",) + blocked_if

    return TaskPacket(
        task_id=make_task_id(cleaned.raw_input, workflow.name),
        raw_input=cleaned.raw_input,
        normalized_input=cleaned.normalized_input,
        recognized_sample=cleaned.recognized_sample,
        project_route="video_factory",
        task_type=workflow.task_types,
        workflow=workflow.name,
        native_workflow_route=workflow.native_route,
        responsibility_layer=workflow.responsibility_layers,
        must_read_files=workflow.must_read_files,
        read_status=read_status,
        blocked_if=blocked_if,
        expected_outputs=workflow.expected_outputs,
        execution_permission="adapter_branch_candidate_no_render_only",
        stopline=STOPLINE,
        source_readback_status="repo_file_readback_required",
        deepseek_trigger_decision=False,
        not_deepseek_conclusion=True,
        no_render_constraints=NO_RENDER_CONSTRAINTS,
    )
