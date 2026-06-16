"""Write Round 2 adapter handoff artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .task_packet import STOPLINE


REPO_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_DIR = REPO_ROOT / "codex_log" / "framework_adapter"
ROUND2_REPORT = FRAMEWORK_DIR / "20260617_round2_branch_local_adapter_integration_candidate_report.md"
HANDOFF = FRAMEWORK_DIR / "current_adapter_integration_handoff.md"
MANIFEST = FRAMEWORK_DIR / "20260617_adapter_integration_context_manifest.json"
LATEST = REPO_ROOT / "codex_log" / "latest.md"


def _rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def artifact_paths() -> dict[str, str]:
    return {
        "round2_report": _rel(ROUND2_REPORT),
        "handoff": _rel(HANDOFF),
        "manifest": _rel(MANIFEST),
        "latest": _rel(LATEST),
    }


def render_round2_report(result: dict[str, Any]) -> str:
    sample_summary = result["sample_summary"]
    editing = result["editing_workflow_probe"]
    completion = result["completion_truth"]
    return f"""# 20260617 Round 2 Branch-Local Adapter Integration Candidate

## 1. task_result

```yaml
status: {result["final_status"]}
meaning: branch-local adapter candidate code and no-render sample chain are ready for a later runtime probe request
project_route: video_factory
branch: {result["branch"]}
stopline: {STOPLINE}
runtime_boundary: not_enabled
service_boundary: not_started
media_boundary: no_media_generated
external_api_boundary: not_called
```

This report records a branch-local adapter integration candidate only. It does not claim formal project integration, production usability, main merge readiness, runtime enablement, or service startup.

## 2. generated_code

```yaml
generated_code:
  - codex_source/adapter_integration/__init__.py
  - codex_source/adapter_integration/workflow_registry.py
  - codex_source/adapter_integration/task_packet.py
  - codex_source/adapter_integration/task_cleaner.py
  - codex_source/adapter_integration/workflow_router.py
  - codex_source/adapter_integration/contract_validator.py
  - codex_source/adapter_integration/editing_workflow_runner.py
  - codex_source/adapter_integration/completion_truth.py
  - codex_source/adapter_integration/no_render_adapter_runner.py
  - codex_source/adapter_integration/context_handoff.py
  - codex_source/adapter_integration/README.md
```

## 3. sample_run_result

```yaml
samples_total: {sample_summary["samples_total"]}
samples_routed: {sample_summary["samples_routed"]}
registered_workflows: {sample_summary["registered_workflows"]}
editing_workflow_probe: {editing["status"]}
completion_truth_guards: {completion["false_completion_guards"]["status"]}
candidate_stopline_truth: {completion["candidate_stopline_truth"]["status"]}
```

The six sample inputs routed to:

```json
{json.dumps(result["sample_routes"], ensure_ascii=False, indent=2)}
```

## 4. validation_scope

```yaml
contract_validator: existing_editing_workflow_no_render_probe_reuse
schema_contracts_passed: {editing["contract_validation"]["schema_contracts_passed"]}
passing_path_passed: {editing["contract_validation"]["passing_path_passed"]}
blocked_cases_passed: {editing["contract_validation"]["blocked_cases_passed"]}
media_generated: false
tts_called: false
real_media_read: false
external_api_called: false
dashvector_real_call: false
chroma_ingestion_run: false
runtime_enabled: false
service_started: false
main_branch_modified: false
content_validation_status: not_promoted
send_ready: false
```

## 5. readback_and_missing_initialization

```yaml
preexisting_handoff: missing_initialized_this_round
preexisting_manifest: missing_initialized_this_round
fallback_sources:
  - codex_log/latest.md
  - codex_log/framework_adapter/20260616_agent_service_toolkit_full_integration_master_plan.md
  - codex_log/framework_adapter/20260616_editing_workflow_no_render_probe_report.md
  - codex_source/schema_contracts/00_schema_contracts_index.md
  - codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py
```

## 6. remaining_gaps

```yaml
real_runtime_probe: not_started
service_start: not_started
real_dashvector_call: not_started
chroma_ingestion: not_started
tts_call: not_started
media_render: not_started
human_review_for_next_phase: required_before_runtime_probe
```
"""


def render_handoff(result: dict[str, Any]) -> str:
    return f"""# Current Adapter Integration Handoff

```yaml
handoff_date: 2026-06-17
project_route: video_factory
branch: {result["branch"]}
current_stopline: {STOPLINE}
current_status: {result["final_status"]}
meaning: branch-local no-render adapter candidate is ready for a later runtime probe request
allowed_next_state: runtime_probe_design_or_runtime_probe_request_after_review
runtime_enabled: false
service_started: false
main_branch_modified: false
external_api_called: false
media_generated: false
tts_called: false
real_media_read: false
dashvector_real_call: false
chroma_ingestion_run: false
content_validation_status: not_promoted
send_ready: false
```

## handoff_summary

- Six adapter candidate workflows are registered.
- Six required sample inputs route to distinct workflows.
- `editing_execution_workflow` runs only the existing no-render schema / fixture validation chain.
- Completion truth guards block false completion claims and keep the stopline at branch-local candidate readiness.

## next_safe_step

```yaml
recommendation: review this branch-local candidate, then authorize a separate runtime probe prompt if desired
blocked_before_next_phase_if:
  - branch is not adapter/agent-service-toolkit-sandbox
  - no-render runner does not pass
  - any runtime or service startup is requested without a new explicit task
  - any external API, TTS, Chroma ingestion, DashVector real call, or real media read is required
  - any middle state is claimed as final delivery
```
"""


def render_manifest(result: dict[str, Any]) -> str:
    manifest = {
        "manifest_date": "2026-06-17",
        "project_route": "video_factory",
        "branch": result["branch"],
        "stopline": STOPLINE,
        "final_status": result["final_status"],
        "samples_total": result["sample_summary"]["samples_total"],
        "samples_routed": result["sample_summary"]["samples_routed"],
        "registered_workflows": result["sample_summary"]["registered_workflows"],
        "artifacts": artifact_paths(),
        "boundaries": {
            "runtime_enabled": False,
            "service_started": False,
            "main_branch_modified": False,
            "external_api_called": False,
            "media_generated": False,
            "tts_called": False,
            "real_media_read": False,
            "dashvector_real_call": False,
            "chroma_ingestion_run": False,
            "content_validation_status": "not_promoted",
            "send_ready": False,
        },
        "must_run_validation": [
            "python3 -m py_compile codex_source/adapter_integration/*.py",
            "python3 codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py",
            "python3 -m codex_source.adapter_integration.no_render_adapter_runner --sample all",
            "git diff --check",
        ],
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def render_latest_section(result: dict[str, Any]) -> str:
    sample_summary = result["sample_summary"]
    return f"""## 20260617｜Round 2 Branch-Local Adapter Integration Candidate

```yaml
task_result.status（任务结果状态）: {result["final_status"]}
project_route（项目路由）: video_factory（视频工厂）
branch（分支）: {result["branch"]}
execution_permission（执行权限）: adapter_branch_candidate_no_render_only（只允许分支内无渲染候选接入）
stopline（停止线）: {STOPLINE}
workflow_registry（工作流注册表）: six_required_workflows_registered（6 个必需 workflow 已注册）
samples_total（样例总数）: {sample_summary["samples_total"]}
samples_routed（已路由样例数）: {sample_summary["samples_routed"]}
editing_workflow_probe（剪辑 workflow 探测）: {result["editing_workflow_probe"]["status"]}
completion_truth_guards（完成真实性检查）: {result["completion_truth"]["false_completion_guards"]["status"]}
runtime_enabled（是否启用正式运行时）: false（未启用）
service_started（是否启动服务）: false（未启动）
main_branch_modified（是否修改 main 主分支）: false（未修改）
external_api_called（是否调用外部 API）: false（未调用）
media_generated（是否生成媒体）: false（未生成）
tts_called（是否调用 TTS）: false（未调用）
real_media_read（是否读取真实媒体）: false（未读取）
Chroma_ingestion_run（是否运行 Chroma 入库）: false（未运行）
DashVector_real_call（是否真实调用 DashVector）: false（未调用）
content_validation_status（内容验证状态）: not_promoted（未推进）
send_ready（可发送状态）: false（未开启）
generated_report（生成报告）: codex_log/framework_adapter/20260617_round2_branch_local_adapter_integration_candidate_report.md
current_handoff（当前交接）: codex_log/framework_adapter/current_adapter_integration_handoff.md
context_manifest（上下文清单）: codex_log/framework_adapter/20260617_adapter_integration_context_manifest.json
next_safe_step（下一步安全动作）: review_branch_candidate_then_separate_runtime_probe_request（先回审分支候选，再另行授权运行时探测）
```

- `candidate_scope（候选范围）`: 本轮只新增 branch-local adapter candidate 代码链，覆盖 workflow registry、TaskPacket、task cleaner、workflow router、contract validator、editing no-render runner、completion truth 和 no-render CLI。
- `sample_route（样例路由）`: 6 个指定样例均已路由到对应候选 workflow；其中剪辑样例会复用既有剪辑 no-render probe。
- `status_boundary（状态边界）`: 本轮不代表正式接入完成、不代表生产可用、不代表 main 可合并、不代表 runtime 已启用、不代表 service 已启动。
- `禁止推进`: 未修改 main，未启用 runtime，未启动 FastAPI / Docker / Postgres / Streamlit，未运行 Chroma ingestion，未真实调用 DashVector，未调用外部 API，未调用 TTS，未读取真实媒体，未生成视频，未推进内容 / 发送 / 发布状态。

"""


def _replace_latest_section(latest_text: str, new_section: str) -> str:
    heading = "## 20260617｜Round 2 Branch-Local Adapter Integration Candidate"
    if heading not in latest_text:
        if latest_text.startswith("# Latest\n\n"):
            return latest_text.replace("# Latest\n\n", "# Latest\n\n" + new_section, 1)
        return new_section + latest_text
    start = latest_text.index(heading)
    next_start = latest_text.find("\n## ", start + 1)
    if next_start == -1:
        return latest_text[:start] + new_section.rstrip() + "\n"
    return latest_text[:start] + new_section + latest_text[next_start + 1 :]


def write_round2_artifacts(result: dict[str, Any]) -> dict[str, str]:
    FRAMEWORK_DIR.mkdir(parents=True, exist_ok=True)
    ROUND2_REPORT.write_text(render_round2_report(result), encoding="utf-8")
    HANDOFF.write_text(render_handoff(result), encoding="utf-8")
    MANIFEST.write_text(render_manifest(result), encoding="utf-8")
    latest_text = LATEST.read_text(encoding="utf-8")
    LATEST.write_text(_replace_latest_section(latest_text, render_latest_section(result)), encoding="utf-8")
    return artifact_paths()
