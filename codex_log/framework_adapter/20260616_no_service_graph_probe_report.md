# 20260616 no_service_graph_probe（无服务图探测报告）

```yaml
task_result.status（任务结果状态）: no_service_graph_probe_completed
project_route（项目路由）: video_factory
branch（分支）: adapter/agent-service-toolkit-sandbox
execution_permission（执行权限）: no_service_graph_probe_only
goal_mode（Goal 模式）: active_for_no_service_graph_probe
probe_scope（探测范围）: fixture_based_fake_graph_no_service_only
runtime_enabled（是否启用正式运行时）: false
service_started（是否启动服务）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
DashVector_real_call（是否真实调用 DashVector）: false
Chroma_ingestion_run（是否运行 Chroma 入库）: false
main_branch_modified（是否修改 main）: false
```

## 1. route_decision（路由判断）

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory（视频工厂）
  task_type（任务类型）:
    - adapter_probe_task（适配探测任务）
    - no_service_graph_probe_task（无服务图探测任务）
    - fixture_based_validation_task（基于样例的验证任务）
    - adapter_pre_code_guardrail_task（代码接入前护栏任务）
  workflow_route_decision（workflow 归位判断）: mechanism_repair_flow（机制修补流）
  responsibility_layer（责任层级）:
    - validation_layer（验收复审层）
    - mechanism_fix_layer（机制修补层）
    - sync_layer（同步回写层）
  execution_permission（执行权限）: no_service_graph_probe_only（只允许无服务图探测）
  main_branch_modification_allowed（是否允许修改 main）: false
```

本轮只证明：在不启动服务、不调用外部 API、不安装依赖、不运行 Chroma 入库、不真实调用 DashVector 的前提下，冻结 schema / fixture 可以被一个 fake graph runner 串成可检查的节点链。

## 2. probe_runner_result（探测运行器结果）

```yaml
probe_runner_result（探测运行器结果）:
  probe_script（探测脚本）: codex_source/schema_contracts/probes/no_service_graph_probe.py
  langgraph_available（LangGraph 是否可用）: false
  probe_runner_type（探测运行器类型）: fake_graph_runner_no_dependency
  dependency_install_required（是否需要安装依赖）: false
  service_required（是否需要服务）: false
  external_api_required（是否需要外部 API）: false
  reason（原因）: 本地未检测到 langgraph；本阶段只允许用无依赖 fake graph runner 验证契约链。
```

## 3. graph_probe_result（图探测结果）

```yaml
graph_probe_result（图探测结果）:
  passing_path_passed（通过路径是否通过）: true
  graph_nodes_tested（已测试图节点）:
    - route_decision_node（路由判断节点）
    - cleaning_adapter_node（清洗适配节点）
    - retrieval_manifest_node（检索清单节点）
    - source_readback_node（原文回读节点）
    - retrieval_gap_report_node（检索缺口报告节点）
    - executor_handoff_node（执行器交接节点）
    - completion_truth_check_node（完成真实性检查节点）
  passing_path_state_summary（通过路径状态摘要）:
    project_route（项目路由）: video_factory
    workflow_route_decision（workflow 归位判断）: mechanism_repair_flow
    retrieval_provider（检索来源）: DashVector
    source_readback_status（原文回读状态）: passed
    active_write_executor（当前激活写入执行器）: codex
    completion_claim_allowed（是否允许完成声明）: true_for_probe_only
```

通过路径说明：

- `route_decision_node（路由判断节点）`: 验证 `runtime_write_allowed=false`、`source_readback_required=true`、`completion_truth_check_required=true`。
- `cleaning_adapter_node（清洗适配节点）`: 验证 `secret_scan_before_ingestion=passed`，并保留 `source_path / chunk_id`。
- `retrieval_manifest_node（检索清单节点）`: 验证 DashVector fixture 带有 `source_path / chunk_id / source_readback_required`，且 `gap_status=none`。
- `source_readback_node（原文回读节点）`: 回读当前分支 `codex_source/schema_contracts/00_schema_contracts_index.md`，确认原文件存在且可读。
- `executor_handoff_node（执行器交接节点）`: 验证 `active_write_executor=codex`，service 与 runtime memory 均不得成为写入者或事实源。
- `completion_truth_check_node（完成真实性检查节点）`: 只允许在本 probe 范围内声明检查链通过，不推进内容、声音、视觉、发布或正式 runtime 状态。

## 4. blocked_path_results（阻断路径结果）

```yaml
blocked_path_results（阻断路径结果）:
  blocked_paths_passed（阻断路径是否全部通过）: true
  covered_cases（已覆盖阻断场景）:
    - case（场景）: graph_direct_write_blocked
      fixture（样例）: graph_runtime_adapter.blocked_runtime_write.yaml
      expected_reason（预期阻断理由）: graph_attempted_direct_repo_write
      result（结果）: blocked_passed
    - case（场景）: graph_missing_source_readback_blocked
      fixture（样例）: graph_runtime_adapter.blocked_missing_source_readback.yaml
      expected_reason（预期阻断理由）: missing_source_readback_required
      result（结果）: blocked_passed
    - case（场景）: retrieval_page_content_only_blocked
      fixture（样例）: retrieval_manifest_page_content_only.blocked.yaml
      expected_reason（预期阻断理由）: page_content_only
      result（结果）: blocked_passed
    - case（场景）: chroma_replace_dashvector_blocked
      fixture（样例）: retrieval_manifest_chroma_replace_dashvector.blocked.yaml
      expected_reason（预期阻断理由）: chroma_sandbox_attempted_to_replace_dashvector
      result（结果）: blocked_passed
    - case（场景）: service_write_repo_blocked
      fixture（样例）: service_contract_no_write_attempt_write.blocked.yaml
      expected_reason（预期阻断理由）: service_attempted_write_repo
      result（结果）: blocked_passed
    - case（场景）: memory_replace_repo_fact_blocked
      fixture（样例）: runtime_memory_boundary.blocked_repo_fact_replacement.yaml
      expected_reason（预期阻断理由）: memory_attempted_repo_fact_replacement
      result（结果）: blocked_passed
    - case（场景）: sandbox_as_runtime_blocked
      fixture（样例）: completion_truth_check.sandbox_as_runtime_blocked.yaml
      expected_reason（预期阻断理由）: sandbox_success_claimed_as_formal_runtime
      result（结果）: blocked_passed
    - case（场景）: technical_as_content_blocked
      fixture（样例）: completion_truth_check.technical_as_content_blocked.yaml
      expected_reason（预期阻断理由）: technical_success_claimed_as_content_success
      result（结果）: blocked_passed
    - case（场景）: rag_as_fact_blocked
      fixture（样例）: completion_truth_check.rag_as_fact_blocked.yaml
      expected_reason（预期阻断理由）: rag_result_claimed_as_fact_without_source_readback
      result（结果）: blocked_passed
```

## 5. boundary_validation_result（边界验证结果）

```yaml
boundary_validation_result（边界验证结果）:
  source_readback_preserved（是否保留原文回读）: true
  retrieval_manifest_preserved（是否保留检索清单）: true
  active_write_executor_preserved（是否保留当前激活写入执行器）: true
  completion_truth_check_preserved（是否保留完成真实性检查）: true
  Project_State_Action_Router_preserved（是否保留项目状态动作总控器）: true
  LangGraph_replaces_router（LangGraph 是否替代路由器）: false
  LangChain_replaces_router（LangChain 是否替代路由器）: false
  Chroma_replaces_DashVector（Chroma 是否替代 DashVector）: false
  memory_replaces_repo_facts（memory 是否替代仓库事实）: false
  service_can_write_repo（service 是否能写仓库）: false
  runtime_direct_repo_write_allowed（runtime 是否允许直接写仓库）: false
```

## 6. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  probe_command（探测命令）: python3 codex_source/schema_contracts/probes/no_service_graph_probe.py
  probe_exit_code（探测退出码）: 0
  passing_fixture_check（通过样例检查）: passed
  blocked_fixture_check（阻断样例检查）: passed
  fake_graph_trace_check（fake graph trace 检查）: passed
  source_readback_check（原文回读检查）: passed
  no_service_check（未启动服务检查）: passed
  no_external_api_check（未调用外部 API 检查）: passed
  no_dependency_install_check（未安装依赖检查）: passed
  no_runtime_enablement_check（未启用 runtime 检查）: passed
```

本报告不声称：

- 不声称正式 adapter runtime 已接入。
- 不声称 FastAPI / Docker / Streamlit / Postgres 已启动。
- 不声称 Chroma 可以替代 DashVector。
- 不声称 DashVector 已被真实调用。
- 不声称 RAG 摘要可以替代原文回读。
- 不声称技术验证可以替代内容验证。
- 不声称 service / runtime 可以直接写仓库。

## 7. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）:
  recommendation（建议）: retrieval_cleaning_adapter_probe_after_user_chatgpt_review
  blocked_before_next_phase_if（进入下一阶段前的阻断条件）:
    - 用户 / ChatGPT 未复审本 no-service graph probe 报告
    - retrieval_manifest / source_readback_map 无法保留 source_path / chunk_id / line_range
    - cleaning adapter 无法在入库前完成 secret scan
    - 任何服务或 runtime 试图绕过 Codex 写仓库
    - 任何 sandbox 成功被写成正式 runtime 成功
```
