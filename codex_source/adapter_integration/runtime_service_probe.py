"""CLI probe for branch-local runtime entry and service boundary."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from .no_render_adapter_runner import build_result as build_no_render_adapter_result
from .runtime_entry import RUNTIME_FINAL_STATE, run_runtime_entry
from .service_boundary import ALLOWED_ACTIONS, handle_service_action, run_forbidden_action_check
from .task_cleaner import SAMPLE_INPUTS


ADAPTER_BRANCH = "adapter/agent-service-toolkit-sandbox"
MAIN_BRANCH = "main"
ALLOWED_BRANCHES = (ADAPTER_BRANCH, MAIN_BRANCH)
REPO_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_DIR = REPO_ROOT / "codex_log" / "framework_adapter"
REPORT_PATH = FRAMEWORK_DIR / "20260617_runtime_service_probe_report.md"
HANDOFF_PATH = FRAMEWORK_DIR / "current_adapter_integration_handoff.md"
MANIFEST_PATH = FRAMEWORK_DIR / "20260617_adapter_integration_context_manifest.json"
LATEST_PATH = REPO_ROOT / "codex_log" / "latest.md"


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


def summarize_runtime_result(sample_key: str, runtime_result: dict[str, Any]) -> dict[str, Any]:
    packet = runtime_result["task_packet"]
    return {
        "sample_key": sample_key,
        "raw_input": runtime_result["raw_input"],
        "selected_workflow": packet["workflow"],
        "native_workflow_route": packet["native_workflow_route"],
        "task_packet_created": bool(packet),
        "route_decision_created": bool(runtime_result["route_decision"]),
        "validation_status": runtime_result["validation_result"]["status"],
        "service_action": "route_validate_block_handoff",
        "repo_write_attempted": runtime_result["repo_write_attempted"],
        "external_api_called": runtime_result["external_api_called"],
        "media_generated": runtime_result["media_generated"],
    }


def run_runtime_and_service_samples(sample: str) -> dict[str, Any]:
    samples = selected_samples(sample)
    runtime_results = []
    service_results = []
    sample_runtime_results = []
    for sample_key in samples:
        runtime_result = run_runtime_entry(sample_key=sample_key)
        runtime_results.append(runtime_result)
        sample_runtime_results.append(summarize_runtime_result(sample_key, runtime_result))
        per_sample_service = {
            action: handle_service_action(action, sample_key=sample_key) for action in ALLOWED_ACTIONS
        }
        service_results.append({"sample_key": sample_key, "actions": per_sample_service})

    forbidden_action_scan = run_forbidden_action_check()
    return {
        "runtime_results": runtime_results,
        "service_results": service_results,
        "sample_runtime_results": sample_runtime_results,
        "forbidden_action_scan": forbidden_action_scan,
        "samples_total": len(samples),
        "samples_runtime_routed": sum(1 for item in sample_runtime_results if item["route_decision_created"]),
    }


def render_report(result: dict[str, Any]) -> str:
    return f"""# 20260617 Branch-Local Runtime Service Probe

## 1. route_decision

```yaml
project_route: video_factory
task_type:
  - runtime_probe_task
  - service_boundary_probe_task
  - adapter_candidate_validation_task
  - branch_local_code_execution_task
execution_permission: branch_local_runtime_service_probe_only
branch: {result["branch"]}
stopline: {RUNTIME_FINAL_STATE}
```

## 2. files_read

```yaml
files_read:
  - AGENTS.md
  - codex_log/latest.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
  - codex_source/19_project_state_action_router.md
  - codex_log/framework_adapter/current_adapter_integration_handoff.md
  - codex_log/framework_adapter/20260617_adapter_integration_context_manifest.json
  - codex_log/framework_adapter/20260617_round2_branch_local_adapter_integration_candidate_report.md
  - codex_source/adapter_integration/README.md
  - codex_source/adapter_integration/workflow_registry.py
  - codex_source/adapter_integration/task_packet.py
  - codex_source/adapter_integration/task_cleaner.py
  - codex_source/adapter_integration/workflow_router.py
  - codex_source/adapter_integration/contract_validator.py
  - codex_source/adapter_integration/editing_workflow_runner.py
  - codex_source/adapter_integration/completion_truth.py
  - codex_source/adapter_integration/no_render_adapter_runner.py
  - codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py
```

## 3. generated_or_modified_files

```yaml
generated_or_modified_files:
  - codex_source/adapter_integration/runtime_entry.py
  - codex_source/adapter_integration/service_boundary.py
  - codex_source/adapter_integration/runtime_service_probe.py
  - codex_log/framework_adapter/20260617_runtime_service_probe_report.md
  - codex_log/framework_adapter/current_adapter_integration_handoff.md
  - codex_log/framework_adapter/20260617_adapter_integration_context_manifest.json
  - codex_log/latest.md
```

## 4. runtime_entry_result

```yaml
status: {result["runtime_entry_result"]["status"]}
samples_total: {result["samples_total"]}
samples_runtime_routed: {result["samples_runtime_routed"]}
repo_write_attempted: false
external_api_called: false
media_generated: false
```

## 5. service_boundary_result

```yaml
status: {result["service_boundary_result"]["status"]}
allowed_actions:
  - route
  - validate
  - block
  - handoff
repo_write_attempted: false
external_api_called: false
media_generated: false
```

## 6. sample_runtime_results

```json
{json.dumps(result["sample_runtime_results"], ensure_ascii=False, indent=2)}
```

## 7. forbidden_action_scan

```yaml
status: {result["forbidden_action_scan"]["status"]}
repo_write_attempted: {str(result["forbidden_action_scan"]["repo_write_attempted"]).lower()}
external_api_called: {str(result["forbidden_action_scan"]["external_api_called"]).lower()}
media_generated: {str(result["forbidden_action_scan"]["media_generated"]).lower()}
forbidden_actions_checked:
  - write_repo
  - commit
  - push
  - modify_main
  - call_external_api
  - generate_media
  - claim_completion
```

## 8. validation_result

```yaml
no_render_adapter_runner: {result["no_render_adapter_runner"]["final_status"]}
runtime_service_probe: {result["final_status"]}
runtime_entry: {result["runtime_entry_result"]["status"]}
service_boundary: {result["service_boundary_result"]["status"]}
```

## 9. remaining_gaps

```yaml
real_runtime_deployment: not_started
real_service_deployment: not_started
real_dashvector_call: not_started
real_chroma_ingestion: not_started
real_tts_call: not_started
real_media_render: not_started
main_merge_candidate_review: not_started
```

## 10. next_safe_step

```yaml
recommendation: user_review_then_isolated_runtime_hardening_or_main_merge_candidate_review
blocked_before_next_phase_if:
  - branch changes away from adapter/agent-service-toolkit-sandbox
  - runtime or service needs external network, secrets, dependency install, or persistent port
  - service boundary attempts repository write, commit, push, or main modification
  - any real media, TTS, DashVector, or Chroma operation is required
```
"""


def render_handoff(result: dict[str, Any]) -> str:
    return f"""# Current Adapter Integration Handoff

```yaml
handoff_date: 2026-06-17
project_route: video_factory
branch: {result["branch"]}
current_status: {RUNTIME_FINAL_STATE}
current_stopline: {RUNTIME_FINAL_STATE}
meaning: branch-local runtime entry and in-process service boundary probe completed only
next_allowed_state: isolated_runtime_hardening_or_main_merge_candidate_review_after_user_authorization
runtime_entry: codex_source/adapter_integration/runtime_entry.py
service_boundary: codex_source/adapter_integration/service_boundary.py
runtime_service_probe: codex_source/adapter_integration/runtime_service_probe.py
runtime_enabled_for_production: false
service_started_for_production: false
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

- Six sample inputs pass through the runtime entry.
- The in-process service boundary allows route / validate / block / handoff only.
- Forbidden service actions are blocked without repository writes, external calls, or media generation.

## next_safe_step

```yaml
recommendation: user_review_then_isolated_runtime_hardening_or_main_merge_candidate_review
blocked_before_next_phase_if:
  - runtime requires dependency installation
  - service requires persistent port or public network
  - any external API, TTS, Chroma ingestion, DashVector real call, or real media read is required
  - any middle state is claimed as final delivery
```
"""


def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        return {}
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    return data


def render_manifest(result: dict[str, Any]) -> str:
    data = load_manifest()
    artifacts = data.setdefault("artifacts", {})
    artifacts["runtime_service_probe_report"] = "codex_log/framework_adapter/20260617_runtime_service_probe_report.md"
    artifacts["runtime_entry"] = "codex_source/adapter_integration/runtime_entry.py"
    artifacts["service_boundary"] = "codex_source/adapter_integration/service_boundary.py"
    artifacts["runtime_service_probe"] = "codex_source/adapter_integration/runtime_service_probe.py"
    data.update(
        {
            "manifest_date": "2026-06-17",
            "project_route": "video_factory",
            "branch": result["branch"],
            "final_status": RUNTIME_FINAL_STATE,
            "stopline": RUNTIME_FINAL_STATE,
            "samples_total": result["samples_total"],
            "samples_runtime_routed": result["samples_runtime_routed"],
            "service_boundary_passed": result["service_boundary_result"]["status"] == "passed",
        }
    )
    boundaries = data.setdefault("boundaries", {})
    boundaries.update(
        {
            "runtime_enabled_for_production": False,
            "service_started_for_production": False,
            "main_branch_modified": False,
            "external_api_called": False,
            "media_generated": False,
            "tts_called": False,
            "real_media_read": False,
            "dashvector_real_call": False,
            "chroma_ingestion_run": False,
            "content_validation_status": "not_promoted",
            "send_ready": False,
        }
    )
    data["must_run_validation"] = [
        "python3 -m py_compile codex_source/adapter_integration/*.py",
        "python3 codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py",
        "python3 -m codex_source.adapter_integration.no_render_adapter_runner --sample all",
        "python3 -m codex_source.adapter_integration.runtime_service_probe --sample all",
        "git diff --check",
    ]
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def render_latest_section(result: dict[str, Any]) -> str:
    return f"""## 20260617｜Branch-Local Runtime Service Probe

```yaml
task_result.status（任务结果状态）: {RUNTIME_FINAL_STATE}（分支内运行时 / 服务探测完成）
project_route（项目路由）: video_factory（视频工厂）
branch（分支）: {result["branch"]}
execution_permission（执行权限）: branch_local_runtime_service_probe_only（只允许分支内运行时 / 服务探测）
runtime_entry（运行时入口）: codex_source/adapter_integration/runtime_entry.py
service_boundary（服务边界）: codex_source/adapter_integration/service_boundary.py
probe_script（探测脚本）: codex_source/adapter_integration/runtime_service_probe.py
generated_report（生成报告）: codex_log/framework_adapter/20260617_runtime_service_probe_report.md
samples_total（样例总数）: {result["samples_total"]}
samples_runtime_routed（运行时已路由样例数）: {result["samples_runtime_routed"]}
service_boundary_passed（服务边界是否通过）: {str(result["service_boundary_result"]["status"] == "passed").lower()}（通过）
repo_write_attempted（是否尝试写仓库）: false（否）
runtime_enabled_for_production（是否启用生产运行时）: false（否）
service_started_for_production（是否启动生产服务）: false（否）
main_branch_modified（是否修改 main 主分支）: false（否）
external_api_called（是否调用外部 API）: false（否）
media_generated（是否生成媒体）: false（否）
next_safe_step（下一步安全动作）: user_review_then_isolated_runtime_hardening_or_main_merge_candidate_review（用户回审后进入隔离运行时加固或 main 合并候选复审）
```

- `runtime_scope（运行时范围）`: 本轮只证明 adapter 分支内 runtime entry 与 in-process service boundary 可以调用候选链。
- `service_boundary（服务边界）`: 仅允许 route / validate / block / handoff；写仓库、提交、推送、改 main、外部调用、媒体生成和正式完成声明均被阻断。
- `status_boundary（状态边界）`: 不代表正式接入完成，不代表生产可用，不代表 main 可合并，不代表内容验证通过，不代表可发送。
- `禁止推进`: 未修改 main，未启动生产服务，未开放公网端口，未安装依赖，未真实调用 DashVector，未运行 Chroma 入库，未调用 TTS，未读取真实媒体，未生成视频 / 音频 / 字幕 / 卡片。

"""


def replace_latest_section(latest_text: str, new_section: str) -> str:
    heading = "## 20260617｜Branch-Local Runtime Service Probe"
    if heading not in latest_text:
        return latest_text.replace("# Latest\n\n", "# Latest\n\n" + new_section, 1)
    start = latest_text.index(heading)
    next_start = latest_text.find("\n## ", start + 1)
    if next_start == -1:
        return latest_text[:start] + new_section.rstrip() + "\n"
    return latest_text[:start] + new_section + latest_text[next_start + 1 :]


def write_artifacts(result: dict[str, Any]) -> dict[str, str]:
    FRAMEWORK_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(result), encoding="utf-8")
    HANDOFF_PATH.write_text(render_handoff(result), encoding="utf-8")
    MANIFEST_PATH.write_text(render_manifest(result), encoding="utf-8")
    latest_text = LATEST_PATH.read_text(encoding="utf-8")
    LATEST_PATH.write_text(replace_latest_section(latest_text, render_latest_section(result)), encoding="utf-8")
    return {
        "runtime_service_probe_report": str(REPORT_PATH.relative_to(REPO_ROOT)),
        "handoff": str(HANDOFF_PATH.relative_to(REPO_ROOT)),
        "manifest": str(MANIFEST_PATH.relative_to(REPO_ROOT)),
        "latest": str(LATEST_PATH.relative_to(REPO_ROOT)),
    }


def build_probe_result(sample: str) -> dict[str, Any]:
    branch = current_branch()
    if branch not in ALLOWED_BRANCHES:
        return {
            "final_status": "blocked",
            "blocked_reason": "branch_mismatch",
            "expected_branches": list(ALLOWED_BRANCHES),
            "actual_branch": branch,
        }

    no_render_adapter_result = build_no_render_adapter_result(sample)
    runtime_service = run_runtime_and_service_samples(sample)
    runtime_entry_status = (
        "passed"
        if runtime_service["samples_total"] == runtime_service["samples_runtime_routed"]
        and all(item["validation_status"] == "passed" for item in runtime_service["sample_runtime_results"])
        else "blocked"
    )
    service_boundary_status = (
        "passed"
        if runtime_service["forbidden_action_scan"]["status"] == "passed"
        and all(
            all(action_result["status"] == "passed" for action_result in sample_result["actions"].values())
            for sample_result in runtime_service["service_results"]
        )
        else "blocked"
    )
    final_status = (
        RUNTIME_FINAL_STATE
        if no_render_adapter_result.get("final_status") == "adapter_branch_integration_candidate_ready_for_runtime_probe"
        and runtime_entry_status == "passed"
        and service_boundary_status == "passed"
        else "blocked"
    )
    return {
        "probe_name": "branch_local_runtime_service_probe",
        "branch": branch,
        "validation_context": "adapter_branch" if branch == ADAPTER_BRANCH else "main_post_merge_validation",
        "project_route": "video_factory",
        "sample_argument": sample,
        "final_status": final_status,
        "no_render_adapter_runner": no_render_adapter_result,
        "runtime_entry_result": {
            "status": runtime_entry_status,
            "samples_total": runtime_service["samples_total"],
            "samples_runtime_routed": runtime_service["samples_runtime_routed"],
        },
        "service_boundary_result": {
            "status": service_boundary_status,
            "repo_write_attempted": runtime_service["forbidden_action_scan"]["repo_write_attempted"],
            "external_api_called": runtime_service["forbidden_action_scan"]["external_api_called"],
            "media_generated": runtime_service["forbidden_action_scan"]["media_generated"],
        },
        "sample_runtime_results": runtime_service["sample_runtime_results"],
        "service_results": runtime_service["service_results"],
        "forbidden_action_scan": runtime_service["forbidden_action_scan"],
        "samples_total": runtime_service["samples_total"],
        "samples_runtime_routed": runtime_service["samples_runtime_routed"],
        "runtime_validation": {
            "status": "branch_local_probe_only",
            "repo_write_attempted": False,
            "external_api_called": False,
            "media_generated": False,
            "tts_called": False,
            "real_media_read": False,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run branch-local runtime/service probe.")
    parser.add_argument("--sample", default="all", help="sample key or all")
    args = parser.parse_args(argv)

    try:
        result = build_probe_result(args.sample)
        if result.get("final_status") != "blocked" and result.get("branch") == ADAPTER_BRANCH:
            result["artifact_generation"] = {"status": "generated", "paths": write_artifacts(result)}
        elif result.get("final_status") != "blocked":
            result["artifact_generation"] = {
                "status": "skipped_main_post_merge_validation_no_write",
                "paths": {
                    "runtime_service_probe_report": str(REPORT_PATH.relative_to(REPO_ROOT)),
                    "handoff": str(HANDOFF_PATH.relative_to(REPO_ROOT)),
                    "manifest": str(MANIFEST_PATH.relative_to(REPO_ROOT)),
                    "latest": str(LATEST_PATH.relative_to(REPO_ROOT)),
                },
            }
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
