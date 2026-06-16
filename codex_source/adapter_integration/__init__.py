"""Branch-local no-render adapter integration candidate."""

from .task_packet import TaskPacket
from .workflow_registry import REQUIRED_WORKFLOWS, get_workflow, list_workflows
from .workflow_router import route_task

__all__ = [
    "REQUIRED_WORKFLOWS",
    "TaskPacket",
    "get_workflow",
    "list_workflows",
    "route_task",
]
