"""CLI runner for the branch-local no-render adapter candidate."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Any

from .completion_truth import evaluate_adapter_candidate_stopline, run_false_completion_guards
from .context_handoff import artifact_paths, write_round2_artifacts
from .editing_workflow_runner import run_editing_workflow_no_render
from .task_cleaner import SAMPLE_INPUTS
from .workflow_registry import REQUIRED_WORKFLOWS, validate_required_workflows
from .workflow_router import route_task


EXPECTED_BRANCH = "adapter/agent-service-toolkit-sandbox"


def current_branch() -> str:
    completed = subprocess.run(
        ["git", "branch", "--show-current"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def selected_samples(sample: str) -> dict[str, str]:
    if sample == "all":
        return dict(SAMPLE_INPUTS)
    if sample in SAMPLE_INPUTS:
        return {sample: SAMPLE_INPUTS[sample]}
    raise ValueError(f"unknown sample: {sample}")


def build_result(sample: str) -> dict[str, Any]:
    branch = current_branch()
    if branch != EXPECTED_BRANCH:
        return {
            "final_status": "blocked",
            "blocked_reason": "branch_mismatch",
            "expected_branch": EXPECTED_BRANCH,
            "actual_branch": branch,
        }

    routed_packets = []
    sample_routes = []
    editing_probe: dict[str, Any] | None = None
    samples = selected_samples(sample)
    for sample_key, text in samples.items():
        packet = route_task(text)
        packet_dict = packet.to_dict()
        routed_packets.append(packet_dict)
        sample_routes.append(
            {
                "sample_key": sample_key,
                "input": text,
                "workflow": packet.workflow,
                "native_workflow_route": packet.native_workflow_route,
                "task_id": packet.task_id,
            }
        )
        if packet.workflow == "editing_execution_workflow":
            editing_probe = run_editing_workflow_no_render(packet)

    if editing_probe is None:
        editing_probe = {"status": "not_applicable", "contract_validation": {"status": "not_applicable"}}

    samples_routed = sum(1 for packet in routed_packets if packet["workflow"] in REQUIRED_WORKFLOWS)
    registry_validation = validate_required_workflows()
    false_completion_guards = run_false_completion_guards()
    candidate_stopline_truth = evaluate_adapter_candidate_stopline(
        samples_total=len(samples),
        samples_routed=samples_routed,
        editing_validation_status=editing_probe["status"],
    )
    final_status = (
        "adapter_branch_integration_candidate_ready_for_runtime_probe"
        if len(samples) == 6
        and samples_routed == 6
        and registry_validation["status"] == "passed"
        and editing_probe["status"] == "passed"
        and false_completion_guards["status"] == "passed"
        and candidate_stopline_truth["status"] == "allowed_for_branch_candidate"
        else "blocked"
    )

    result: dict[str, Any] = {
        "runner_name": "no_render_adapter_runner",
        "branch": branch,
        "project_route": "video_factory",
        "sample_argument": sample,
        "final_status": final_status,
        "sample_summary": {
            "samples_total": len(samples),
            "samples_routed": samples_routed,
            "registered_workflows": len(REQUIRED_WORKFLOWS),
        },
        "workflow_registry_validation": registry_validation,
        "sample_routes": sample_routes,
        "task_packets": routed_packets,
        "editing_workflow_probe": editing_probe,
        "completion_truth": {
            "false_completion_guards": false_completion_guards,
            "candidate_stopline_truth": candidate_stopline_truth,
        },
        "no_render_boundaries": {
            "media_generated": False,
            "tts_called": False,
            "real_media_read": False,
            "external_api_called": False,
            "dashvector_real_call": False,
            "chroma_ingestion_run": False,
            "runtime_enabled": False,
            "service_started": False,
            "main_branch_modified": False,
        },
        "artifact_generation": {
            "status": "pending",
            "paths": artifact_paths(),
        },
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run branch-local no-render adapter samples.")
    parser.add_argument("--sample", default="all", help="sample key or all")
    args = parser.parse_args(argv)

    try:
        result = build_result(args.sample)
        if result.get("final_status") != "blocked":
            paths = write_round2_artifacts(result)
            result["artifact_generation"] = {"status": "generated", "paths": paths}
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if result.get("final_status") != "blocked" else 2
    except Exception as exc:  # pragma: no cover - CLI boundary.
        print(
            json.dumps(
                {
                    "final_status": "blocked",
                    "blocked_reason": type(exc).__name__,
                    "message": str(exc),
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
