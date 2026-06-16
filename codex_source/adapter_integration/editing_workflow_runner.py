"""No-render runner for the editing execution workflow."""

from __future__ import annotations

from typing import Any

from .contract_validator import validate_editing_workflow_contracts
from .task_packet import TaskPacket


def run_editing_workflow_no_render(packet: TaskPacket | None = None) -> dict[str, Any]:
    validation = validate_editing_workflow_contracts()
    return {
        "workflow": "editing_execution_workflow",
        "native_workflow_route": "aesthetic_editing_flow",
        "task_packet": packet.to_dict() if packet is not None else None,
        "runner_type": "no_render_contract_validation_only",
        "contract_validation": validation,
        "media_generated": False,
        "tts_called": False,
        "real_media_read": False,
        "external_api_called": False,
        "dashvector_real_call": False,
        "chroma_ingestion_run": False,
        "runtime_enabled": False,
        "service_started": False,
        "status": "passed" if validation["status"] == "passed" else "failed",
    }
