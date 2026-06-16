"""In-process service boundary probe for the adapter candidate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .runtime_entry import run_runtime_entry


ALLOWED_ACTIONS: tuple[str, ...] = ("route", "validate", "block", "handoff")
FORBIDDEN_ACTIONS: tuple[str, ...] = (
    "write_repo",
    "commit",
    "push",
    "modify_main",
    "call_external_api",
    "generate_media",
    "claim_completion",
)


@dataclass(frozen=True)
class ServiceBoundaryResult:
    action: str
    status: str
    payload: dict[str, Any]
    repo_write_attempted: bool = False
    external_api_called: bool = False
    media_generated: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "action": self.action,
            "status": self.status,
            "payload": self.payload,
            "repo_write_attempted": self.repo_write_attempted,
            "external_api_called": self.external_api_called,
            "media_generated": self.media_generated,
        }


def handle_service_action(
    action: str,
    *,
    raw_user_input: str | None = None,
    sample_key: str | None = None,
) -> dict[str, Any]:
    if action in FORBIDDEN_ACTIONS:
        return ServiceBoundaryResult(
            action=action,
            status="blocked",
            payload={
                "blocked_reason": f"forbidden_service_action:{action}",
                "allowed_actions": list(ALLOWED_ACTIONS),
            },
        ).to_dict()

    if action not in ALLOWED_ACTIONS:
        return ServiceBoundaryResult(
            action=action,
            status="blocked",
            payload={
                "blocked_reason": "unknown_service_action",
                "allowed_actions": list(ALLOWED_ACTIONS),
            },
        ).to_dict()

    runtime_result = run_runtime_entry(raw_user_input=raw_user_input, sample_key=sample_key)
    if action == "route":
        payload = {
            "task_packet": runtime_result["task_packet"],
            "route_decision": runtime_result["route_decision"],
        }
    elif action == "validate":
        payload = {
            "validation_result": runtime_result["validation_result"],
            "completion_truth_result": runtime_result["completion_truth_result"],
        }
    elif action == "block":
        payload = {
            "blocked_if": runtime_result["task_packet"]["blocked_if"],
            "no_render_boundaries": runtime_result["no_render_boundaries"],
        }
    else:
        payload = {
            "handoff": {
                "workflow": runtime_result["task_packet"]["workflow"],
                "native_workflow_route": runtime_result["task_packet"]["native_workflow_route"],
                "expected_outputs": runtime_result["task_packet"]["expected_outputs"],
                "stopline": runtime_result["route_decision"]["stopline"],
            }
        }

    return ServiceBoundaryResult(action=action, status="passed", payload=payload).to_dict()


def run_forbidden_action_check() -> dict[str, Any]:
    checks = [handle_service_action(action) for action in FORBIDDEN_ACTIONS]
    return {
        "status": "passed" if all(item["status"] == "blocked" for item in checks) else "failed",
        "allowed_actions": list(ALLOWED_ACTIONS),
        "forbidden_actions_checked": list(FORBIDDEN_ACTIONS),
        "results": checks,
        "repo_write_attempted": any(item["repo_write_attempted"] for item in checks),
        "external_api_called": any(item["external_api_called"] for item in checks),
        "media_generated": any(item["media_generated"] for item in checks),
    }
