"""Task packet shape for branch-local workflow routing."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha1
from typing import Mapping


STOPLINE = "adapter_branch_integration_candidate_ready_for_runtime_probe"


NO_RENDER_CONSTRAINTS: dict[str, bool] = {
    "media_generated": False,
    "tts_called": False,
    "real_media_read": False,
    "external_api_called": False,
    "dashvector_real_call": False,
    "chroma_ingestion_run": False,
    "runtime_enabled": False,
    "service_started": False,
    "main_branch_modified": False,
}


@dataclass(frozen=True)
class TaskPacket:
    task_id: str
    raw_input: str
    normalized_input: str
    recognized_sample: str
    project_route: str
    task_type: tuple[str, ...]
    workflow: str
    native_workflow_route: str
    responsibility_layer: tuple[str, ...]
    must_read_files: tuple[str, ...]
    read_status: Mapping[str, str]
    blocked_if: tuple[str, ...]
    expected_outputs: tuple[str, ...]
    execution_permission: str
    stopline: str
    source_readback_status: str
    deepseek_trigger_decision: bool
    not_deepseek_conclusion: bool
    no_render_constraints: Mapping[str, bool]

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["task_type"] = list(self.task_type)
        data["responsibility_layer"] = list(self.responsibility_layer)
        data["must_read_files"] = list(self.must_read_files)
        data["blocked_if"] = list(self.blocked_if)
        data["expected_outputs"] = list(self.expected_outputs)
        data["read_status"] = dict(self.read_status)
        data["no_render_constraints"] = dict(self.no_render_constraints)
        return data


def make_task_id(raw_input: str, workflow: str) -> str:
    digest = sha1(f"{workflow}\n{raw_input}".encode("utf-8")).hexdigest()[:12]
    return f"adapter_round2_{digest}"
