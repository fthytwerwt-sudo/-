# Latest

## 20260616｜Agent Service Toolkit Full Integration Master Plan

```yaml
task_result.status（任务结果状态）: full_integration_master_plan_completed
project_route（项目路由）: video_factory
branch（分支）: adapter/agent-service-toolkit-sandbox
execution_permission（执行权限）: master_plan_report_only
goal_mode（Goal 模式）: active_for_plan_delivery_only
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
service_started（是否启动服务）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
upstream_code_copied（是否复制上游源码）: false
full_workflow_inventory_completed（workflow 全量盘点是否完成）: true
toolkit_capability_inventory_completed（toolkit 能力盘点是否完成）: true
integration_decision_matrix_created（接入分类矩阵是否创建）: true
direct_embed_list_created（可直接嵌入清单是否创建）: true
adapter_required_list_created（需要适配清单是否创建）: true
project_change_required_list_created（需要项目机制改动清单是否创建）: true
disable_or_quarantine_list_created（默认禁用 / 隔离清单是否创建）: true
data_architecture_master_plan_created（数据与架构保真总计划是否创建）: true
one_shot_integration_route_created（一次性接入路线是否创建）: true
user_decision_board_created（用户决策板是否创建）: true
candidate_new_workflow（候选新增 workflow）: adapter_infrastructure_flow（适配基础设施流，候选，未启用）
candidate_new_workflow_enabled（候选新增 workflow 是否启用）: false
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（是否不是 DeepSeek 结论）: true
generated_report（生成报告）: codex_log/framework_adapter/20260616_agent_service_toolkit_full_integration_master_plan.md
next_safe_step（下一步安全动作）: user_chatgpt_review_then_contract_schema_phase_after_confirmation
```

- `full_workflow_inventory（workflow 全量盘点）`: 已盘点 6 类正式 workflow 与 15 个原生 router / gate / bus / candidate 面；本轮承载线仍为 `mechanism_repair_flow（机制修补流）`，`adapter_infrastructure_flow（适配基础设施流）` 只作为 candidate，不启用。
- `integration_classification_matrix（接入分类矩阵）`: 已按 `direct_embed / adapter_required / project_change_required / disable_by_default / unmapped_quarantine / do_not_import / future_candidate` 七类归位上游能力。
- `direct_embed（可直接嵌入）`: human review interrupt pattern、completion truth check deterministic node、write executor handoff shape、pre-execution read contract gate、client/test contract shape、Pydantic/schema pattern。
- `adapter_required（需要适配）`: LangGraph runtime、LangChain model/tool、RAG assistant、Chroma sandbox output、DashVector formal route、source_readback、cleaning layer、FastAPI service、runtime memory、upstream schema mapping。
- `disable_or_quarantine（默认禁用 / 隔离）`: Streamlit、Docker Compose、Postgres / Mongo、GitHub MCP、LangSmith / Langfuse、supervisor / hierarchy agents、safeguard / Groq real call、raw Chroma ingestion、page_content-only RAG context、knowledge-base-agent。
- `data_architecture_master_plan（数据与架构保真总计划）`: DashVector 保留主线；Chroma 只做 sandbox；Git/repo/codex_log/review_loop 仍是事实源；`source_readback + human_review + completion_truth_check` 仍是完成真值链；runtime 不得直接写仓库。
- `one_shot_integration_route（一口气接入路线）`: 只作为后续 Goal Mode 分阶段路线；必须先经用户 / ChatGPT 复审，再进入 contract / schema / fixture / no-service graph / retrieval-cleaning probe / authorized service probe / main merge candidate review。
- `禁止推进`: 未启用 runtime，未修改 main，未安装依赖，未启动 FastAPI / Docker / Postgres / Streamlit，未运行 Chroma ingestion，未调用外部 API，未复制上游源码，未推进视频 / 声音 / 视觉 / 发布 / 发送状态。

## 20260615｜Formal Adapter Patch Plan

```yaml
task_result.status（任务结果状态）: formal_adapter_patch_plan_completed
project_route（项目路由）: video_factory
branch（分支）: adapter/agent-service-toolkit-sandbox
execution_permission（执行权限）: plan_report_only
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
workflow_mapping_completed（workflow 映射是否完成）: true
unmapped_workflow_register_created（未归位 workflow 登记是否创建）: true
data_architecture_preservation_plan_created（数据与架构保真计划是否创建）: true
candidate_new_workflow（候选新增 workflow）: adapter_infrastructure_flow（适配基础设施流，候选，未启用）
candidate_new_workflow_enabled（候选新增 workflow 是否启用）: false
upstream_code_copied（是否复制上游源码）: false
dependency_installed（是否安装依赖）: false
service_started（是否启动服务）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
generated_report（生成报告）: codex_log/framework_adapter/20260615_formal_adapter_patch_plan.md
next_safe_step（下一步安全动作）: contract_and_schema_patch_plan_after_user_confirmation
```

- `workflow_inventory（workflow 盘点）`: 已按 `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` 复核 6 类现有 workflow；本轮主承载线为 `mechanism_repair_flow（机制修补流）`。
- `workflow_adapter_mapping（workflow 适配映射）`: `copy_testing_flow / material_evidence_flow / aesthetic_editing_flow / quality_review_flow / data_review_flow` 均为 partial fit；`mechanism_repair_flow` 为本轮 direct fit；`adapter_infrastructure_flow（适配基础设施流）` 只登记为 candidate，不启用、不写入正式入口。
- `upstream_capability_map（上游能力地图）`: LangGraph 保留为 `workflow_runtime_layer（工作流运行层）`；LangChain 保留为 `adapter_layer（模型 / 工具 / 检索适配层）`；DashVector 保留为当前项目主检索路线；Chroma 只作为 sandbox 学习 / 并存评估对象。
- `data_architecture_preservation_plan（数据与架构保真计划）`: 必须保留 `current_data_goal_anchor / operation_records / review_loop / data_goal_execution_bus / retrieval_manifest / source_readback / completion_truth_check / write_executor_handoff / human_review_boundary`。
- `disabled_by_default（默认禁用）`: Streamlit frontend、Docker / Postgres / Mongo persistence、GitHub MCP agent、raw Chroma ingestion、LangSmith / Langfuse external telemetry、supervisor / hierarchy agents as formal workflow。
- `contracts_needed_before_code（写 adapter 代码前需补契约）`: `graph_runtime_adapter_contract`、`retrieval_manifest_schema`、`source_readback_map_schema`、`cleaning_adapter_contract`、`service_contract_no_write_probe`、`completion_truth_check_node_contract`。
- `禁止推进`: 未启用 runtime，未修改 main，未安装依赖，未启动 FastAPI / Docker / Postgres / Streamlit，未运行 Chroma ingestion，未调用外部 API，未复制上游源码，未推进视频 / 声音 / 视觉 / 发布状态。

## 20260614｜Agent Service Toolkit Sandbox Branch Context

```yaml
task_result.status（任务结果状态）: adapter_branch_context_created
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: create_and_push_adapter_branch_update_branch_latest_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
branch_name（分支名）: adapter/agent-service-toolkit-sandbox
branch_source（分支来源）: origin/main
branch_source_commit（分支来源提交）: 42954b677af5c8a21252d282f2a4846ce278a4dd
branch_purpose（分支用途）: agent-service-toolkit sandbox integration and adapter experiments
current_branch（当前分支）: adapter/agent-service-toolkit-sandbox
remote_branch_created（远端分支是否创建）: true
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
sandbox_upstream_commit（沙盒上游提交）: 5b3945f48e41a193816d7710b275eb89b90568ee
main_branch_modified_this_round（本轮是否修改 main 分支）: false
install_executed_in_main_repo（是否在主仓库安装）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
sandbox_files_committed（是否提交沙盒文件）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
fastapi_service_started（是否启动 FastAPI 服务）: false
chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
external_api_called（是否调用外部 API）: false
runtime_enabled（是否启用正式运行时）: false
generated_report（生成报告）: codex_log/framework_adapter/20260614_agent_service_toolkit_sandbox_branch_context.md
next_safe_step（下一步安全动作）: continue_agent_service_toolkit_adapter_work_on_adapter_branch
```

- `branch_context（分支上下文）`: 本分支只承载 `agent-service-toolkit` 沙盒接入、adapter、RAG、LangGraph、DashVector、清洗层和服务契约实验；不是 main 合并，也不是正式 runtime 启用。
- `sandbox_submission_policy（沙盒提交策略）`: 不提交 `.venv`、外部源码副本、`video_factory_probe` 临时脚本 / 输出、`.env` 或任何 secret。
- `main_policy（main 分支策略）`: main 只接收确认后的正式结果；本轮没有修改 main 分支指针，也没有把沙盒文件纳入主仓库。
- `forbidden_without_new_authorization（未经新授权禁止事项）`: 不合并 main，不启用 runtime，不启动 FastAPI / Docker / Postgres / Streamlit，不调用真实外部 API，不写 secret。

## 20260614｜Stability Proof Closed Loop Probe

```yaml
task_result.status（任务结果状态）: stability_proof_closed_loop_probe_completed
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: sandbox_fake_model_no_service_stability_probe_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
sandbox_graph_probe_result（沙盒图调用探测结果）: passed
positive_stability_test_result（正向稳定性测试结果）: passed
negative_block_test_result（负向阻断测试结果）: passed
determinism_check_result（确定性检查结果）: passed
source_readback_verified（原文回读是否验证）: true
completion_truth_check_verified（完成真实性检查是否验证）: true
executor_handoff_boundary_verified（执行器边界是否验证）: true
stability_gain_decision（稳定性提升判断）: proven_within_sandbox_fake_model_no_service_scope
stability_gain_proven（稳定性提升是否已证明）: true
proven_scope（已证明范围）: sandbox_fake_model_no_service_graph_probe_only
not_proven_scope（未证明范围）:
  - formal_video_factory_runtime
  - real_llm_provider
  - DashVector runtime adapter
  - FastAPI service contract
  - Chroma ingestion
  - production persistence
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
fastapi_service_started（是否启动 FastAPI 服务）: false
postgres_started（是否启动 Postgres）: false
chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
external_api_called（是否调用外部 API）: false
runtime_enabled（是否启用正式运行时）: false
sandbox_runtime_probe_only（仅沙盒运行探测）: true
generated_report（生成报告）: codex_log/framework_adapter/20260614_stability_proof_closed_loop_probe.md
next_safe_step（下一步安全动作）: formal_adapter_patch_plan_after_user_confirmation
```

- `stability_proof_scope（稳定性证明范围）`: 只证明 sandbox / fake fixture / no service / no external API 下，LangGraph 能把“能不能写完成”的检查链固定成确定性节点。
- `positive_stability_test（正向稳定性测试）`: 同一输入连续 3 次输出完全一致；3 个正向 JSON 的 SHA-256 均为 `dc9cc8aeaa858bb9c9bc5f3b48f8e5f0a4d0c3d6270a7a4b7fed573486f04090`。
- `negative_block_test（负向阻断测试）`: 缺失 `missing_source` 时稳定输出 `blocked_reason=source_readback_missing`，执行器 `can_write=false`，完成声明 `completion_claim_allowed=false`。
- `source_readback（原文回读）`: 正向回读到 `project_rule / latest_status / codex_report` 的 `source_id + chunk_id + exact_excerpt`；负向缺来源时明确阻断。
- `completion_truth_check（完成真实性检查）`: 技术验证只写 `passed_for_sandbox_graph_probe`，内容验证保持 `not_evaluated_not_promoted`，未推进正式状态。
- `修改范围`：主仓库只新增本轮稳定性证明报告并更新 `codex_log/latest.md`；sandbox 临时脚本和输出留在 `/Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614/video_factory_probe/`，未复制进主线。

## 20260614｜LangGraph / RAG / Cleaning Integration Probe

```yaml
task_result.status（任务结果状态）: langgraph_rag_cleaning_integration_probe_completed
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: sandbox_architecture_probe_report_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
sandbox_install_ready（沙盒安装就绪）: true
uv_path（uv 路径）: /Users/fan/.local/bin/uv
uv_pip_check（uv 依赖一致性检查）: passed_checked_241_packages
compile_probe_result（编译探测结果）: passed
minimal_import_probe_result（最小导入探测结果）: passed
pytest_collect_only_result（pytest 收集探测结果）: passed_128_tests_collected
langgraph_probe_done（LangGraph 探测完成）: true
langchain_position_audit_done（LangChain 定位审计完成）: true
rag_probe_done（RAG 探测完成）: true
cleaning_layer_slot_done（清洗层位置设计完成）: true
cleaning_layer_status（清洗层状态）: basic_ingestion_only
retrieval_policy（检索策略）: coexist_then_decide
current_project_retrieval（当前项目检索）: DashVector
upstream_retrieval（上游检索）: Chroma / RAG example
source_readback_required（是否必须原文回读）: true
retrieval_result_not_completion_proof（检索结果不是完成证明）: true
install_executed_in_main_repo（是否在主仓库安装）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
service_server_started（是否启动服务端）: false
chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
external_api_called（是否调用外部 API）: false
runtime_enabled（是否启用正式运行时）: false
sandbox_runtime_probe_only（仅沙盒运行探测）: true
generated_report（生成报告）: codex_log/framework_adapter/20260614_langgraph_rag_cleaning_integration_probe.md
next_safe_step（下一步安全动作）: sandbox_fake_model_no_service_graph_invoke_probe_after_user_confirmation
```

- `langgraph_structure_audit（LangGraph 结构审计）`: 已确认上游以 LangGraph 作为主编排层，注册 10 个 agent；`rag-assistant`、`research-assistant`、supervisor、interrupt、knowledge-base agent 均可静态取图，GitHub MCP agent 保持 deferred / unloaded。
- `langchain_position_fit_audit（LangChain 定位审计）`: 已确认 LangChain 更适合作为模型、工具、retriever、loader 适配层，不替代视频工厂状态路由和完成真实性检查。
- `rag_mechanism_probe（RAG 机制探测）`: 已确认上游 RAG 使用 Chroma + OpenAIEmbeddings + PDF/DOCX loader；当前工具输出只拼接 `page_content`，不保留 source/page/chunk metadata 到模型上下文。
- `cleaning_layer_gap_audit（清洗层缺口审计）`: 结论为 `basic_ingestion_only`；后续必须补 `video_factory_cleaning_adapter`，覆盖 secret scan、metadata 标准化、去重、chunk quality、source readback、retrieval manifest。
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled`。
- `修改范围`：只新增 LangGraph/RAG/cleaning integration probe 报告并更新 `codex_log/latest.md`；未修改 `AGENTS.md / GPT数据源 / codex_source / pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜Goal Mode Sandbox Install Completion

```yaml
task_result.status（任务结果状态）: goal_mode_sandbox_install_completed
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: goal_mode_sandbox_install_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
uv_available（uv 是否可用）: true
uv_path（uv 路径）: /Users/fan/.local/bin/uv
uv_version（uv 版本）: uv 0.11.21 (5aa65dd7a 2026-06-11 aarch64-apple-darwin)
path_persistence_fixed（PATH 是否已持久化修复）: false
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
partial_venv_cleanup_done（残缺 .venv 是否已清理）: true
sandbox_dependency_sync_result（沙盒依赖同步结果）: completed
sandbox_venv_usable（沙盒 .venv 是否可用）: true
sandbox_python_runtime（沙盒 Python 运行时）: CPython 3.13.14
sandbox_packages_installed（沙盒已安装包数量）: 241
uv_pip_check（uv 依赖一致性检查）: passed
compile_probe_result（编译探测结果）: passed
minimal_import_probe_result（最小导入探测结果）: passed_with_pythonpath_and_inline_fake_model
install_executed_in_main_repo（是否在主仓库安装）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
service_server_started（是否启动服务端）: false
runtime_enabled（是否启用正式运行时）: false
sandbox_runtime_probe_only（仅沙盒运行探测）: true
generated_report（生成报告）: codex_log/framework_adapter/20260614_goal_mode_sandbox_install_completion.md
next_safe_step（下一步安全动作）: sandbox_no_service_closed_loop_import_or_service_contract_probe_after_user_confirmation
```

- `uv_available（uv 可用）`: true
- `sandbox_dependency_sync_completed（沙盒依赖同步完成）`: true
- `sandbox_venv_usable（沙盒 .venv 可用）`: true
- `compile_probe_passed（编译探测通过）`: true
- `minimal_import_probe_done（最小导入探测已完成）`: true
- `blocked_if_any（如有阻断）`: null
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled`。
- `修改范围`：只新增 goal mode sandbox install completion 报告并更新 `codex_log/latest.md`；未修改 `AGENTS.md / GPT数据源 / codex_source / pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜UV Install And Sandbox Dependency Probe

```yaml
task_result.status（任务结果状态）: uv_install_and_sandbox_dependency_probe_blocked
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: install_uv_user_level_then_rerun_sandbox_dependency_probe
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
uv_found_before（安装前是否找到 uv）: false
uv_installed（是否安装 uv）: true
uv_install_method（uv 安装方式）: standalone_installer
uv_available_after（安装后 uv 是否可用）: true
uv_path_after_install（安装后 uv 路径）: /Users/fan/.local/bin/uv
uv_version_after_install（安装后 uv 版本）: uv 0.11.21 (5aa65dd7a 2026-06-11 aarch64-apple-darwin)
shell_profile_modified（是否修改 shell 配置）: false
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
sandbox_dependency_probe_result（沙盒依赖探测结果）: blocked_uv_sync_download_stalled_or_timed_out_in_sandbox
minimal_import_probe_result（最小导入探测结果）: blocked_not_run_because_uv_sync_interrupted_before_usable_dependency_environment
install_executed_in_main_repo（是否在主仓库安装）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
service_server_started（是否启动服务端）: false
runtime_enabled（是否启用正式运行时）: false
sandbox_runtime_probe_only（仅沙盒运行探测）: true
generated_report（生成报告）: codex_log/framework_adapter/20260614_uv_install_and_sandbox_dependency_probe.md
next_safe_step（下一步安全动作）: rerun_uv_sync_frozen_in_same_sandbox_with_longer_network_window_or_preseed_uv_cache
```

- `uv_checked（uv 已检查）`: true
- `uv_available_after_install_or_preexisting（uv 已存在或安装后可用）`: true
- `sandbox_dependency_probe_completed_or_blocked_with_reason（沙盒依赖探测完成或阻断原因清楚）`: true
- `minimal_import_probe_completed_or_blocked_with_reason（最小导入探测完成或阻断原因清楚）`: true
- `blocked_reason（阻断原因）`: `uv sync --frozen` 在 sandbox 依赖下载 / 同步阶段长时间无完成信号，最后 60 秒无输出；已中断并记录现场，未改 lock，未写 secret。
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled`。
- `修改范围`：只新增 uv install + sandbox dependency probe 报告并更新 `codex_log/latest.md`；未修改 `AGENTS.md / GPT数据源 / codex_source / pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜Agent Service Toolkit Sandbox Install Probe

```yaml
task_result.status（任务结果状态）: sandbox_install_probe_blocked
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: sandbox_install_probe_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
sandbox_workspace_created（沙盒工作区是否创建）: true
sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
upstream_project_downloaded（上游项目是否下载）: true
upstream_commit（上游提交）: 5b3945f48e41a193816d7710b275eb89b90568ee
dependency_probe_result（依赖探测结果）: blocked_uv_required_but_missing_and_install_not_authorized
minimal_import_probe_result（最小导入探测结果）: partial_static_compile_passed_runtime_imports_blocked_by_missing_dependencies
install_executed_in_main_repo（是否在主仓库安装）: false
dependency_installed_in_sandbox（是否在沙盒安装依赖）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
service_server_started（是否启动服务端）: false
runtime_enabled（是否启用正式运行时）: false
sandbox_runtime_probe_only（仅沙盒运行探测）: true
generated_report（生成报告）: codex_log/framework_adapter/20260614_sandbox_install_probe.md
next_safe_step（下一步安全动作）: authorize_uv_install_or_provide_existing_uv_then_rerun_sandbox_dependency_probe
```

- `sandbox_workspace_created_or_blocked_with_reason（沙盒工作区已创建或阻断原因清楚）`: true
- `upstream_project_downloaded_or_blocked_with_reason（上游项目已下载或阻断原因清楚）`: true
- `dependency_probe_completed_or_blocked_with_reason（依赖探测已完成或阻断原因清楚）`: true
- `minimal_import_probe_completed_or_blocked_with_reason（最小导入探测已完成或阻断原因清楚）`: true
- `blocked_reason（阻断原因）`: 当前 PATH 中没有 `uv`，且本轮不允许自动全局安装 `uv`；已用 Codex bundled Python 3.12.13 做只读依赖解析和 `compileall src`。
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled`。
- `修改范围`：只新增 sandbox install probe 报告并更新 `codex_log/latest.md`；未修改 `AGENTS.md / GPT数据源 / codex_source / pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜External Framework Full Intake Design

```yaml
task_result.status（任务结果状态）: external_framework_full_intake_design_completed
project_route（项目路由）: video_factory
external_framework（外部框架）: JoshuaC215/agent-service-toolkit
execution_permission（执行权限）: design_report_and_latest_only
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
large_task_gate.triggered（大任务闸门是否触发）: true
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
install_executed（是否已安装）: false
sandbox_created（是否创建沙盒）: false
runtime_enabled（是否启用运行时）: false
external_code_copied（是否复制外部代码）: false
frontend_policy（前端策略）: disabled_by_default
frontend_started（是否启动前端）: false
write_executor_policy（写入执行器策略）: executor_abstraction_required
active_write_executor（当前激活写入执行器）: codex
future_executor_candidates（未来候选执行器）:
  - trae
  - future_ide_agent
retrieval_policy（检索策略）: coexist_then_decide
current_project_retrieval（当前项目检索）: DashVector
upstream_retrieval（上游检索）: Chroma / RAG example
cleaning_layer_status（清洗层状态）: basic_ingestion_only
generated_report（生成报告）: codex_log/framework_adapter/20260614_external_framework_full_intake_design.md
next_safe_step（下一步安全动作）: sandbox_install_probe_prompt_after_user_confirmation
```

- `full_intake_plan_completed（完整接入计划已完成）`: true
- `sandbox_install_scope_completed（沙盒安装范围已完成）`: true
- `module_keep_disable_prune_matrix_completed（模块矩阵已完成）`: true
- `executor_abstraction_patch_plan_completed（执行器抽象修补方案已完成）`: true
- `retrieval_coexistence_plan_completed（检索并存方案已完成）`: true
- `cleaning_layer_gap_audit_completed（清洗层缺口审计已完成）`: true
- `closed_loop_probe_plan_completed（闭环探测计划已完成）`: true
- `upstream_read_status（上游读取状态）`: `read_ok_with_api_tree_fallback`；GitHub API tree endpoint 返回 403，但 raw URLs 与 codeload tarball stream 已完成指定文件 / 目录回读。
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled / sandbox_created / minimal_router_prototype_created`。
- `修改范围`：只新增 framework adapter 设计报告并更新 `codex_log/latest.md`；未修改 `AGENTS.md / GPT数据源 / codex_source / pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜Schema Contract Static Validation

- `task_result.status = schema_contract_static_validation_passed_install_preflight_ready`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = schema_contract_static_validation + schema_contract_fix_if_needed + install_preflight_gate_review + mechanism_repair_flow`
- `workflow_route_decision = mechanism_repair_flow`
- `large_task_gate.triggered = true`
- `execution_permission = validate_and_patch_schema_contract_files_only`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `static_validation = passed`
- `schemas_checked = 10`
- `passing_fixtures_checked = 9`
- `blocked_fixtures_checked = 9`
- `fixes_applied = workflow_route_decision_allowed_values_updated_for_static_validation`
- `install_preflight_ready = true`
- `sandbox_entry_allowed_this_round = false`
- `next_safe_step = sandbox_intake_no_write_prompt`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`
- `generated_report = codex_log/framework_adapter/20260614_schema_contract_static_validation.md`
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / publish_candidate_ready / runtime_enabled / sandbox_created / minimal_router_prototype_created`。
- `修改范围`：只修补 `codex_source/schema_contracts/` 内 schema/fixture/index，新增 static validation 报告并更新 latest；未修改 `pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260614｜Schema Contract Fix Plan

- `task_result.status = schema_contract_fix_plan_completed_static_draft`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = schema_contract_fix_plan + adapter_design_review_only + mechanism_repair_flow + project_file_change`
- `workflow_route_decision = mechanism_repair_flow`
- `large_task_gate.triggered = true`
- `execution_permission = write_schema_fixtures_index_report_latest_only`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `schemas_created = 10`
- `passing_fixtures_created = 9`
- `blocked_fixtures_created = 9`
- `cross_contract_trace_schema_created = true`
- `schema_contract_index_created = true`
- `schema_static_validation = passed`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`
- `sandbox_entry_allowed_now = false`
- `next_safe_step = schema_contract_static_validation`
- `generated_report = codex_log/framework_adapter/20260614_schema_contract_fix_plan.md`
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready / publish_candidate_ready / runtime_enabled / sandbox_created / minimal_router_prototype_created`。
- `修改范围`：只新增 schema contracts、fixtures、schema index、fix plan 报告并更新 latest；未修改 `pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260613｜Schema Contract Gap Review

- `task_result.status = schema_contract_gap_review_completed`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = schema_contract_gap_review + adapter_design_review_only + mechanism_repair_flow + review_diagnosis_audit`
- `workflow_route_decision = mechanism_repair_flow`
- `large_task_gate.triggered = true`
- `execution_permission = add_report_and_latest_only`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`
- `contracts_reviewed = 9`
- `all_required_fields_complete = false`
- `sandbox_entry_allowed_now = false`
- `sandbox_entry_blockers = no_canonical_schema_files / no_contract_fixtures / no_cross_contract_trace_id / no_completion_truth_contract / no_human_review_interrupt_contract`
- `next_safe_step = schema_contract_fix_plan`
- `generated_report = codex_log/framework_adapter/20260613_schema_contract_gap_review.md`
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready / publish_candidate_ready / runtime_enabled / sandbox_created / minimal_router_prototype_created`。
- `修改范围`：只新增 schema contract gap review 报告并更新 latest；未修改 `pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260613｜Adapter 设计硬冲突最小补丁

- `task_result.status = adapter_design_hard_conflict_patch_completed`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = adapter_design_review_only + hard_conflict_patch_only + mechanism_repair_flow`
- `workflow_route_decision = mechanism_repair_flow`
- `large_task_gate.triggered = true`
- `execution_permission = allowed_files_minimal_patch_only`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `install_or_migration = false`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `deepseek_position_after_patch`: DeepSeek 从每轮默认文件 / 上下文供应商降为条件触发的只读审查、风险复核和冲突二次意见；默认先走 Vector RAG / DashVector 检索与仓库原文件 readback。
- `write_executor_boundary_after_patch`: 当前 `active_write_executor = codex`；`executor_type = trae / future_ide_agent` 只作为未来候选，未启用、未授权、未验证；外部 runtime 不得直接写仓库、commit 或 push。
- `dashvector_boundary_after_patch`: DashVector / Vector RAG 是 retrieval_index / cache_layer，不替代 GitHub / 仓库原文件 source_of_truth；上游 Chroma / OpenAIEmbeddings 只作结构参考，不作为当前默认检索实现。
- `agent_service_toolkit_boundary_after_patch`: LangGraph / FastAPI / GitHub MCP / agent-service-toolkit runtime 只允许 route / retrieve / readback / validate / block / interrupt / handoff；实际文件写入由 `active_write_executor` 执行。
- `next_safe_step = option_a_design_review_only`
- `schema_contract_gap_review_required_before_next_stage = true`
- `禁止推进`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready / publish_candidate_ready`。
- `修改范围`：只改允许清单内入口、机制和 adapter 设计文件；未修改 `pyproject.toml / requirements.txt / package.json / compose.yaml / docker-compose.yml / dist / public / media / .env*`。

## 20260613｜Agent Service Toolkit 完整接入适配设计

- `task_result.status = agent_service_toolkit_full_intake_adapter_design_completed`
- `branch = main`
- `project_route = video_factory`
- `external_framework = JoshuaC215/agent-service-toolkit`
- `route_decision.task_type = mechanism_repair_flow + external_framework_adapter_design + project_architecture_design + deepseek_positioning_repair`
- `workflow_route_decision = mechanism_repair_flow`
- `large_task_gate.triggered = true`
- `execution_permission = design_files_only`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = true_public_github_readonly`
- `full_intake_plan_created = true`
- `module_keep_disable_prune_matrix_created = true`
- `dashvector_adapter_plan_created = true`
- `deepseek_positioning_plan_created = true`
- `write_executor_abstraction_plan_created = true`
- `workflow_runtime_mapping_created = true`
- `closed_loop_definition_created = true`
- `next_stage_execution_prompt_draft_created = true`
- `active_write_executor_current = codex`
- `write_executor_abstraction_target = executor_type: codex / trae / future_ide_agent`
- `agent_service_toolkit_phase_1_policy`: FastAPI and LangGraph can be design targets; Streamlit, GitHub MCP write tools, Postgres checkpoint, long-term Store, Chroma formal retrieval and Docker runtime remain disabled / draft-only until closed-loop proof.
- `dashvector_policy`: current Alibaba embedding + DashVector route remains the main retrieval path; upstream Chroma RAG is only structural reference.
- `deepseek_policy`: DeepSeek should move from default file/context supplier to conditional reasoning reviewer, risk auditor, conflict second opinion, fallback context synthesizer and optional external deep supply.
- `formal_patch_applied = false`
- `formal_patch_proposal_created = true`
- `本轮不是安装 / 迁移 / 视频执行`：未安装依赖，未复制外部代码，未修改 `pyproject.toml / package.json / compose.yaml / docker-compose.yml`，未修改 `dist/` 或 `public/`，未生成视频 / 音频 / 图片，未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。
- `新增设计文件`：`codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md`、`codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md`、`codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md`、`codex_source/23_agent_service_toolkit_full_intake_adapter_design.md`。
- `next_stage_recommendation = option_a_design_review_only`

## 20260613｜AI 架构换位越界补丁受控回滚

- `task_result.status = ai_architecture_role_shift_controlled_rollback_completed`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + review_diagnosis_audit`
- `rollback_base_commit = c61973caf71cdb1d0e59266d0c7ac422d79c79b2`
- `selected_option = B`
- `formal_mechanism_files_restored = true`
- `formal_mechanism_files_restored_list`：`AGENTS.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/08_当前正式事实.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`、`codex_source/13_execution_lane_and_parallel_rules.md`、`codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`。
- `reports_retained = true`
- `reports_retained_list`：`reports/ai_architecture_role_shift_audit.md`、`reports/ai_architecture_role_shift_change_review.md`。
- `docs_converted_to_draft = true`
- `docs_converted_to_draft_list`：`docs/AI_ROLE_MAP.md`、`docs/RAG_EXECUTION_ARCHITECTURE.md`、`docs/DEEPSEEK_POSITIONING.md`、`docs/VECTOR_RETRIEVAL_PLAN.md`、`docs/CODEX_EXECUTION_RULES.md`。
- `CURRENT_STATUS_top_level_removed_or_draft = true`
- `CURRENT_STATUS_moved_to = reports/drafts/20260613_current_status_ai_architecture_role_shift_draft.md`
- `rag_first_healthcheck_executed = false`
- `deepseek_called = false`
- `dashvector_written = false`
- `external_api_called = false`
- `secret_committed = false`
- `本轮不是视频执行`：不生成视频 / 音频 / 图片，不修改 `public/`、`dist/` 或媒体产物，不推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。
- `next_step = 用户确认后再另起 RAG-first 机制修补 / healthcheck 任务`

## 20260613｜AI 执行架构换位审计与 RAG-first 供料归位

- `task_result.status = ai_architecture_role_shift_audit_completed_with_minimal_document_patch`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = review_diagnosis_audit + mechanism_or_route_fix + project_file_change`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = read_parallel for audit / serial_only for writes`
- `deepseek_participation = fallback_local_only`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `secret_read_or_printed = false`
- `本轮不是视频执行`：不生成视频 / 音频 / 图片，不修改 `dist/latest_review_pack/`，不推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。
- `审计结论 = 部分成立`：项目已经有 20260611 / 20260613 的 RAG / DashVector 最小链路和边界设计，但正式入口仍残留 DeepSeek 每轮默认资料供料、深度文件供料和 mandatory loop 的旧口径。
- `DeepSeek 新定位`：推理、总结、改写、风险复核、冲突二次意见和外部深度供料；不作为资料库、向量库、默认文件读取器或长期记忆层。
- `RAG 新定位`：embedding + vector database + retrieval manifest 负责项目内资料召回，输出 chunk、metadata、source、版本、readback 和 retrieval gap；召回结果不得写成完成证明。
- `Codex 新定位`：唯一写入执行层，负责回读仓库原文件、改代码 / 文档、跑验证、写报告、更新状态和 Git 收尾；不得替用户 / GPT 拍板业务验收。
- `新增文档`：`docs/AI_ROLE_MAP.md`、`docs/RAG_EXECUTION_ARCHITECTURE.md`、`docs/DEEPSEEK_POSITIONING.md`、`docs/VECTOR_RETRIEVAL_PLAN.md`、`docs/CODEX_EXECUTION_RULES.md`。
- `新增报告`：`reports/ai_architecture_role_shift_audit.md`。
- `新增状态`：`CURRENT_STATUS.md`、`codex_log/supply_requests/20260613_ai_architecture_role_shift_audit_pre_supply_request.json`。
- `最小补丁`：`AGENTS.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/08_当前正式事实.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`、`codex_source/13_execution_lane_and_parallel_rules.md`、`codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`。
- `next_codex_goal_recommendation = RAG-first execution healthcheck`：输入任务 query，输出 retrieval manifest、source readback、retrieval gap、DeepSeek trigger decision 和 Codex execution permission。
- `git_sync_status`：待随本轮 path-limited commit / push / remote readback 完成后，以 Codex final report 为准。

## 20260613｜Vector RAG 最小链路验证与合并评审就绪

- `task_result.status = vector_rag_minimal_chain_ready_for_main_review`
- `branch = feature/vector-rag-router-design-20260611`
- `project_route = video_factory`
- `route_decision.task_type = code_debug + mechanism_or_route_fix + review_diagnosis_audit`
- `large_task_gate.triggered = true`
- `lane = standard_lane`
- `parallel = serial_only`
- `本轮不是视频执行`：不生成视频 / 音频 / 图片，不修改 `dist/latest_review_pack/`，不推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。
- `embedding_model = text-embedding-v4`
- `embedding_dimension = 1024`
- `dashvector_collection = video_factory_docs_test`
- `collection_config_verified = dimension 1024 / metric Cosine / dtype FLOAT`
- `phase_1_single_write_readback = passed`：固定测试 id `video_factory_rag_smoke_test_20260613_001` 写入 1 条并通过 top_k 查询回读。
- `phase_2_ingestion_policy_check = passed`：已复核 whitelist / blacklist / source priority / chunking / metadata / rebuild strategy。
- `phase_3_dry_run_manifest = passed`：扫描 13 个最小资料文件，允许 13 个，阻断 0 个，计划 chunk 261 个，预计 embedding 调用 261 次。
- `phase_4_minimal_real_ingestion = passed`：只入库最小正式资料包，写入 261 个 chunks；未全仓入库，未入库 `.env*`、本地配置、secret、媒体、`public/`、cache。
- `phase_5_retrieval_readback = passed`：5 个问题均能检索到 chunks，并通过 `source_file_path / section_title / content_hash` 回读原文件。
- `phase_6_pre_execution_read_chain = passed`：已验证 `query -> retrieve -> readback -> read_proof -> gate decision` 最小链路；`MISSING_REPORT` 仍只能诊断 / 阻断，不能放行真实执行。
- `phase_7_merge_recommendation = ready_for_main_review`
- `状态边界`：向量库只是 `retrieval_index / cache_layer`，仓库文件仍是 `source_of_truth`；不得把向量结果当最终事实，不得写成完整 RAG runtime 已自动接入，不得自动合并 main。
- `secret_safety`：`key_value_printed = false`，`vector_values_printed = false`，`secret_committed = false`。
- `reports`：`codex_log/vector_rag_router_design/20260613_vector_rag_merge_readiness_report.md`、`codex_log/vector_rag_router_design/20260613_vector_rag_smoke_test_report.md`、`codex_log/vector_rag_router_design/20260613_retrieval_readback_validation_report.md`。
- `git_sync_status`：本条记录待随本轮 path-limited commit / push / remote readback 完成后，以 Codex final report 为准。

## 20260609｜卡片最小真实链路用户通过与默认路线确认

- `task_result.status = card_minimal_chain_user_approved_default_route_recorded`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + user_review_result_sync`
- `本轮不是视频生成`：不生成新图片、不生成新视频、不修改 `dist/latest_review_pack/`、不修改 `public/`、不替换现有视频卡片。
- `user_feedback = 这轮我看了，我觉得是可以通过的，以后都这样。`
- `user_aesthetic_review = passed`
- `user_default_route_confirmation = true`
- `source_artifact_dir = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/`
- `confirmed_minimal_chain_outputs`：`01_image2_visual_base_raw.png`、`02_locked_copy_overlay_final.png`、`03_hyperframes_motion_wrapper_optional.mp4`、`card_chain_report.md`、`card_chain_summary.json`。
- `default_card_execution_route_after_user_approval`：`image2_visual_base_route_candidate -> codex_post_overlay_locked_copy -> optional HyperFrames_motion_wrapper`。
- `fallback_route`：`HTML/CSS/PIL_exact_text_layer` 只承担准确文字 fallback；不得冒充 HyperFrames 动效。
- `required_checks`：`locked_copy_diff_check / readability_check / social_editorial_card_v1_check / evidence_window_protection / subtitle_card_overlap_check / card_visual_quality_gate / publish_candidate_preflight_when_entering_real_video_chain`。
- `状态边界`：`image2_long_term_stable_passed = false`，`content_validation = not_advanced`，`send_ready = false`，`visual_master_locked = false`，`publish_candidate = not_advanced`，`current_data_goal_anchor_ready = not_advanced`。
- `dated_log = codex_log/20260609_card_minimal_chain_user_approved_default_route.md`
- `git_sync_status`：本轮用户通过回写随本次提交同步到 `main`；最终 SHA 以 Codex final report 为准。

## 20260609｜image2 卡片路线冲突修补

- `task_result.status = image2_card_route_conflict_repair_completed_git_synced`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + fixture_test_sync`
- `本轮不是视频生成`：不生成图片、不生成视频、不修改 `dist/latest_review_pack/`、不修改 `public/`、不替换现有视频卡片。
- `只读冲突审计结论已吸收`：旧机制把 `judgment_card / summary_card` 与 HyperFrames 无条件强绑定；本轮已改为条件触发。
- `image2 新定位`：`image2_visual_base_route_candidate（主视觉底图候选）`，负责主视觉 / 底图 / 构图 / 质感 / 社交编辑感；用户已人工反馈样张审美可过关，但不得写成长期稳定通过。
- `text_authority_route`：`codex_post_overlay_locked_copy` 为准确 locked copy 文字层；`HTML/CSS/PIL_exact_text_layer` 保留为 `exact_text_fallback（准确文字 fallback）`。
- `HyperFrames 新定位`：从主视觉默认路线降级为 optional `motion_wrapper / auxiliary_motion_route / card_motion_layer`；只有 `motion_wrapper_route = HyperFrames_motion_wrapper` 时才触发 runtime gate。
- `保留机制`：`social_editorial_card_v1`、横屏 `16:9 / 1920x1080`、`card_budget_gate`、`cluster_merge_rule`、`card_placement_decision`、`evidence_window_protection`、locked copy 语义保护。
- `新增阻断`：`image2_text_semantic_mismatch_unfixable`、`generated_fake_data_or_claim`、`evidence_window_covered`、`third_party_asset_detected`、`social_editorial_card_v1_deviation`、`post_overlay_readability_check_missing`、`hyperframes_motion_wrapper_selected_but_runtime_missing`。
- `fixtures/tests`：更新 Codex 判断权限 fixture 和机制推理 fixture；新增 card decision route tests，覆盖 image2 无 HyperFrames 不阻断、HyperFrames motion wrapper 缺 runtime 阻断、image2 文字错配需叠字或阻断、social_editorial_card_v1 偏离需阻断或 human review。
- `dated_log = codex_log/20260609_image2卡片路线冲突修补_image2_card_route_conflict_repair.md`
- `状态边界`：`image2_visual_probe_user_aesthetic_passed = true`，`image2_primary_visual_route_candidate = partial`，`hyperframes_primary_visual_route = downgraded`，`hyperframes_motion_wrapper = active`，`image2_long_term_stable_passed = false`。
- `未推进`：`content_validation = not_advanced`，`send_ready = false`，`visual_master_locked = false`，`current_data_goal_anchor_ready = not_advanced`。
- `git_sync_status`：本轮机制修补已 commit、push 到 `main`，并完成 remote HEAD verification；最终 SHA 以 Codex final report 为准。

## 20260607｜实现设计层机制升级与 GPT Project 同步包

- `task_result.status = implementation_design_layer_repair_completed_package_validation_passed_pending_git_sync`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + local_file_governance`
- `implementation_chain_upgraded_to`：`目标层 -> 机制层 -> 实现设计层 -> 流程层 -> 判断标准层 -> 反馈层`
- `new_gate = implementation_design_layer（实现设计层）`
- `new_state = implementation_design_needed（需要实现设计层）`
- `codex_blocker = blocked_need_implementation_design_layer`
- `implementation_design_layer_required_fields`：`target_effect / codex_capability_boundary / confirmed_capabilities / unverified_capabilities / preferred_execution_route / fallback_routes / capability_probe_tasks / done_when / blocked_if`
- `card_visual_route_example`：`HyperFrames` 可作为首选卡片路线但只代表待验证执行路线；`image2 / 图片生成能力` 只能写成待探测；静态 `HTML/CSS/PIL` fallback 必须说明损失，不能冒充原目标；能力边界不清时必须 blocked。
- `gpt_project_upload_package_canonical_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/上传说明_UPLOAD_MANIFEST.md`
- `updated_gpt_project_files`：`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `updated_codex_entry_files`：`codex_source/00_codex_readme.md`、`codex_source/19_project_state_action_router.md`、`codex_source/20_reference_to_execution_contract.md`、`codex_source/21_codex_judgment_permission_matrix.md`、`codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- `dated_log = codex_log/20260607_实现设计层机制升级_implementation_design_layer.md`
- `DeepSeek pre-supply`：已创建 `codex_log/supply_requests/20260607_implementation_design_layer_pre_supply_request.json` 并通过 safe runner 真实调用；`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`；但 `deepseek_depth_validation.status = failed_insufficient_depth`，不得写成长期深度参与已稳定。
- `DeepSeek post-risk-review`：已创建 `codex_log/supply_requests/20260607_implementation_design_layer_post_risk_review_request.json` 并尝试 safe runner；controller 返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；后置风险结论来自 Codex 本地验证。
- `local_validation`：`git diff --check` passed；package forbidden file path scan passed；`dist/latest_review_pack / public / GPT数据源/08_当前正式事实.md` diff check passed；secret value scan passed；status assignment scan passed；package file count = 23。
- `upload_boundary`：本地包生成不代表用户已上传 GPT Project UI；GitHub main 仍是主事实源。
- `未推进`：不生成视频、图片、音频或正式文案；不调用 TTS / 图片 / 视频生成 API；不修改 `dist/latest_review_pack/`；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 20260607｜V006 第六期新素材无 GPT 图标正片候选重做

- `task_result.status = publish_candidate_ready_for_human_review`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = video_sample_or_assembly + video_repair_execution + publish_candidate_regeneration + platform_risk_material_replacement + locked_copy_video_execution`
- `large_task_gate.triggered = true`
- `lane = standard_lane`
- `parallel = serial_only`
- `old_candidate_dir = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_20260607_034319`
- `new_output_dir = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300`
- `full_mp4 = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/full.mp4`
- `review_manifest = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/review_manifest.md`
- `summary = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/summary.json`
- `new_material_dir_requested = /Users/fan/Documents/视频工厂/素材录制-第六期`
- `new_material_dir_actual = /Users/fan/Documents/视频工厂/素材录制/第六期`
- `new_material_dir_fallback_used = true`
- `old_material_reused = false`
- `new_material_used = true`
- `final_used_materials = M04(2026-06-07 16:58:12) + M05(2026-06-07 17:00:57) + M06(2026-06-07 17:03:36) + generated_cards`
- `locked_copy_changed = false`
- `line_group_count = 38`
- `replaced_line_groups = 38`
- `line_group_replacement_failed = []`
- `tts_route = reused_previous_minimax_narration`
- `actual_tts_provider = minimax`
- `actual_tts_model = MiniMax/speech-2.8-hd`
- `actual_voice_id = oldBMinimax20260528010200`
- `gpt_icon_exposure_check = passed_final_sampled_frames_no_gpt_chatgpt_openai_icon_or_favicon_detected`
- `privacy_platform_risk_report = passed_no_secret_or_token_visible_project_paths_partial_human_review_required`
- `remaining_card_visual_deviation = true`
- `technical_validation`: `passed`，`ffprobe` 显示 `1920x1080 / 290.993s / h264 / AAC audio / decodable = true`
- `audio_validation`: `passed_non_silent`，`mean_volume = -16.2 dB`，`max_volume = -1.5 dB`
- `DeepSeek pre-supply`：已创建 `codex_log/supply_requests/20260607_V006_no_gpt_icon_material_replacement_pre_supply_request.json` 并通过 safe runner 真实调用；`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。
- `DeepSeek post-risk-review`：已创建 `codex_log/supply_requests/20260607_V006_no_gpt_icon_material_replacement_post_risk_review_request.json` 并尝试 safe runner；控制器返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；后置风险结论来自 Codex 本地验证。
- `post_risk_local_review = /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/post_risk_local_review.md`
- `visual_verdict`: `.omx/state/V006_no_gpt_icon/ralph-progress.json`，`score = 92`，`verdict = pass`
- `日志证据`: `codex_log/20260607_V006第六期新素材无GPT图标候选片重做.md`
- `同步边界`：本 V006 候选不替换 `dist/latest_review_pack/` legacy v3.1 当前复审对象，不覆盖当前运营数据目标；仅作为第六期新素材重做候选片入口。
- `未推进`：不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 20260606｜完整 GPT Project 同步包重新生成

- `task_result.status = full_gpt_project_sync_package_generated_git_synced`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = gpt_project_sync_package_update + project_file_change + local_file_governance`
- `previous_package_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`
- `previous_package_audit`：上一版同步包包含 `codex_log/latest.md` 和 `codex_log/current_local_artifact_paths.md`，但缺少 `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` 与 `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`。
- `new_package_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_完整GPTProject同步包_full_project_sync_package/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_完整GPTProject同步包_full_project_sync_package/上传说明_UPLOAD_MANIFEST.md`
- `package_source_commit = 6d9fd8a6f2838c56d74f770456d683a80a17698b`
- `package_generation_commit_sha = 4b535efbaf2143bca9d826a1411974e5c363a9fe`
- `git_sync_status`:
  - `current_branch = main`
  - `commit_sha = 4b535efbaf2143bca9d826a1411974e5c363a9fe`
  - `pushed = true`
  - `remote_head_verified = true`
  - `remote_head_sha = 4b535efbaf2143bca9d826a1411974e5c363a9fe`
  - `unrelated_dirty_files = public/reference_migration_20260601_010425/source_segment.mp4`
  - `secret_scan = passed`
  - `completed_allowed = true`
- `package_scope`：`GPT数据源/00-15` 全套主读入口、`codex_log/latest.md`、`codex_log/current_local_artifact_paths.md`、当前运营入口、当前数据目标锚点、运营记录索引、关键 Codex 入口镜像和上传说明。
- `ready_for_user_upload = true_after_manifest_and_path_verification`
- `upload_boundary`：本地完整包已生成，不代表用户已上传 GPT Project UI，也不代表 GPT Project UI 已同步成功；GitHub main 仍是主事实源。
- `user_uploaded_to_gpt_project_ui = false / not_claimed`
- `未推进`：不生成视频；不生成正式文案；不生成下一条视频执行 prompt；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 20260606｜需求确认机制 GPT Project 同步包生成

- `task_result.status = gpt_project_sync_package_generated_pending_git_sync`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = gpt_project_sync_package_update + project_file_change + local_file_governance`
- `package_based_on_commit = 8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`
- `gpt_project_upload_package_canonical_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/上传说明_UPLOAD_MANIFEST.md`
- `current_local_artifact_paths_updated = true`
- `ready_for_user_upload = true_after_manifest_and_path_verification`
- `package_contains`：本轮修改后的 GPT Project 主读文件、关键机制入口文件、`codex_log/latest.md`、`codex_log/current_local_artifact_paths.md`、当前运营入口、当前数据目标锚点、运营记录索引和本轮 dated log。
- `upload_boundary`：本地包已生成，不代表用户已上传 GPT Project UI；GitHub main 仍是主事实源。
- `未推进`：不生成视频；不生成正式文案；不生成下一条视频执行 prompt；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 20260606｜需求确认机制升级

- `task_result.status = requirement_alignment_gate_repair_completed_git_synced`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_repair_task + project_file_change + gpt_project_coordination_rule_update`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`
- `新增 / 补强机制`：`requirement_alignment_needed（需求对齐必需）`，用于问题、修改、修复、纠偏、需求不清楚、机制调整、执行方式变化、判断标准变化或失败反馈路由变化时，先做需求确认，再决定是否下发 Codex；`20260607_current_override`：当前最新机制已升级为六层确认，新增 `implementation_design_layer（实现设计层）`。
- `触发边界`：用户反馈“不对 / 不顺 / 怪 / 差点意思”，或提出需要改、修一下、优化、纠偏、调整机制、改执行方式、需求不清楚，或新需求可能和旧流程 / 旧机制 / 旧默认执行方式冲突。
- `不触发边界`：正常执行、正常做视频、已确认流程且无异常反馈时不触发；本机制用于减少错下发、减少旧机制冲突、减少 Codex 按旧流程乱跑，不是增加常规流程负担。
- `historical_five_layer_chain（历史五层确认链）`：`目标层 -> 机制层 -> 流程层 -> 判断标准层 -> 反馈层`；`20260607_current_override`：当前最新链路为 `目标层 -> 机制层 -> 实现设计层 -> 流程层 -> 判断标准层 -> 反馈层`。
- `冲突提醒`：新需求与旧执行方式冲突时，GPT Project / ChatGPT 必须提醒旧机制是降权、替换、保留为历史，还是只作为 fallback；不处理冲突时，Codex 可能继续按旧流程执行。
- `商品案例边界`：商品案例只作为用户解释问题 / 修改 / 新旧流程冲突的示例，不写成《视频工厂》当前正式主线。
- `DeepSeek pre-supply`：当前无可调用 DeepSeek 工具入口，本轮标记 `fallback_local_only`、`not_deepseek_conclusion = true`、`token_usage_expectation_check = not_observable`。
- `validation`：grep `requirement_alignment_needed` passed；grep `正常执行 / 正常做视频` passed；grep 历史五层字段 passed；商品案例误写检查 passed；forbidden status promotion scoped diff check passed；`git diff --check` passed；secret scan passed；`20260607_current_override`：后续按六层机制执行。
- `git_sync_status`:
  - `current_branch = main`
  - `requirement_alignment_gate_commit_sha = 8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`
  - `pushed = true`
  - `remote_head_verified = true`
  - `remote_head_sha = 8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`
  - `unrelated_dirty_files = public/`
  - `secret_scan = passed`
  - `completed_allowed = true`
- `未推进`：本轮不生成视频；不生成正式文案；不生成下一条视频执行 prompt；不修改 `dist/`、`public/`、`review_loop/records/`、`review_loop/screenshots/`；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。
- `日志证据`: `codex_log/20260606_需求确认机制升级_requirement_alignment_gate.md`

## 20260606｜文案前置判断机制升级

- `task_result.status = copy_prewrite_gate_repair_completed_git_synced`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + copy_mechanism_repair + validation_sync_repair`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`
- `本轮不是写稿`：不生成下一期正式文案，不生成下一条视频执行 prompt，不改 V005 raw_copy。
- `mechanism_gap_found`：现有文案规则已有风格偏好、文案流程、颗粒度配比、对标话语机制、说人话标准、素材证据和 locked copy 契约；缺口是这些规则没有强制压成写稿前判断顺序，导致后台词、机制词、复盘词可能直接进入口播。
- `新增 / 更新闸门`：`copy_type_router（文案类型判断器）`、`plain_language_translation_gate（后台词转人话闸门）`、`human_problem_first_gate（人的麻烦优先闸门）`、`copy_from_review_handoff_gate（复盘到文案交接闸门）`、`prewrite_copy_decision_card（写稿前文案判断卡）`。
- `GPT数据源/04`：新增写稿前判断器主入口、6 类文案类型、后台词转人话词表、复盘到文案交接和判断卡模板；明确缺卡不得进入 `locked_copy_contract`。
- `GPT数据源/15`：新增 `plain_language_translation_gate` 与 `human_problem_first_gate`；最终口播裸出后台词默认判为 `AI_tone_risk`；工具必须在人卡住之后出现。
- `GPT数据源/05`：新增 `prewrite_copy_decision_card required before locked_copy_contract`；缺判断卡不得建立 locked copy、不得输出正式口播稿、不得生成下一条正式视频执行 prompt。
- `learning_ledger_sync`：`current_copy_revision_handoff.md`、`next_episode_bet_card.md`、`operation_learning_memory.md` 已同步写稿前判断要求。
- `V005 followup default`：下一条默认不是教学视频，不是 Codex 剪辑教程，而是 `hybrid_experience_with_evidence（经验口播 + 少量证据展示）`。
- `plain_language_boundary`：`开头 / 中段 / 承接 / 变量 / 指标 / 机制 / 文案层 / 数据闭环 / 字幕断句 / 文案画面对齐` 不得裸进最终口播；复盘数据必须先翻译成“保留什么、只改什么、不改什么、用人话怎么说”。
- `DeepSeek pre-supply`：当前无可调用 DeepSeek 工具入口，本轮标记 `fallback_local_only`、`not_deepseek_conclusion = true`、`token_usage_expectation_check = not_observable`。
- `validation`：grep `copy_type_router` passed；grep `plain_language_translation_gate` passed；grep `human_problem_first_gate` passed；grep `prewrite_copy_decision_card` passed；`git diff --check` passed；forbidden path diff check passed。
- `git_sync_status`:
  - `current_branch = main`
  - `copy_prewrite_gate_repair_commit_sha = aee34b159e75cb448812b391b35096747bdaf788`
  - `git_sync_tail_cleanup_commit_sha = efd092e21752271a4f8e1fcf4e83fd22caa8c0dd`
  - `remote_contains_tail_cleanup_commit = true`
  - `pushed = true`
  - `remote_head_verified = true`
  - `remote_head_sha = aee34b159e75cb448812b391b35096747bdaf788`
  - `remote_readback_scope = copy_prewrite_gate_repair mechanism files + learning ledger + logs`
  - `unrelated_dirty_files = public/`
  - `secret_scan = passed`
  - `completed_allowed = true`
- `unrelated_dirty_files = public/`
- `未推进`：不生成下一期正式文案；不生成下一条正式视频执行 prompt；不修改 raw_copy；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；不修改 `dist/`、`public/`、`review_loop/records/`、`review_loop/screenshots/`。
- `日志证据`: `codex_log/20260606_文案前置判断机制升级_copy_prewrite_gate_repair.md`

## 20260606｜第一次运营复盘正反馈闭环修复

- `task_result.status = first_operation_feedback_loop_closure_completed_git_synced`
- `branch = main`
- `project_route = video_factory`
- `route_decision.task_type = mechanism_repair_task + review_loop_repair_task + copy_feedback_loop_repair_task + validation_sync_repair_task`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`
- `本轮不是旧数据回填`：不深度补旧截图，不重新 OCR 旧视频，不补齐旧视频缺失数据。
- `本轮核心修复`：把复盘系统从报告终点升级为 `数据回填 -> 指标好坏留痕 -> 单期变量登记 -> 跨期学习台账 -> 下一期创作下注卡 -> 文案层交接卡 -> ChatGPT 写下一期文案前强制读取 -> 下一期发布后验证下注`。
- `learning_ledger_dir = review_loop/learning_ledger/`
- `metric_event_log = review_loop/learning_ledger/metric_event_log.jsonl`
- `episode_variable_registry = review_loop/learning_ledger/episode_variable_registry.json`
- `episode_signal_summary = review_loop/learning_ledger/episode_signal_summary.md`
- `operation_learning_memory = review_loop/learning_ledger/operation_learning_memory.md`
- `next_episode_bet_card = review_loop/learning_ledger/next_episode_bet_card.md`
- `current_copy_revision_handoff = review_loop/learning_ledger/current_copy_revision_handoff.md`
- `latest_operation_learning_report = review_loop/learning_ledger/latest_operation_learning_report.json`
- `script = scripts/运营学习台账系统_operation_learning_ledger_system.py`
- `tests = tests/test_operation_learning_ledger_system.py`
- `V005 已进入第一次闭环`：V005 当前作为 `latest_sent_video_current_learning_sample`，使用 existing `between_24h_and_72h_snapshot` 与 raw_copy / structure map，不深补旧数据。
- `V005 good signals`：play_count 1514、like_count 50、like_rate 3.30%、cover_click_rate 7.14%、recommendation_page 96.1%。
- `V005 weak/bad signals`：average_watch_time 8秒、completion_rate 0.62%、two_second_bounce_rate 54.68%、five_second_completion_rate 22.45%、favorite_rate 0.79%。
- `V005 missing signals`：3s_retention、profile_visit_count、dm_count、effective_dm_count、effective_consult_count、clear_need_customer_count。
- `preliminary_learning`：V005 更像“用户选题 / 题眼 / 包装打开流量”，不是内容承接全面变好；下一期保留大题眼，只优先修 0-8 秒承接，并压到具体证明场景。
- `ChatGPT creative judgment responsibility`：已写入 learning ledger 和 GPT 数据源机制入口；下次写文案前必须输出创作下注，不能只给泛泛建议或纯数据解释。
- `copy_layer_handoff`：下次文案必须读取 `next_episode_bet_card.md`、`current_copy_revision_handoff.md`、`operation_learning_memory.md`、`review_loop/copy_iteration/V005/V005_copy_structure_map.json`。
- `report_sync`：`latest_copy_iteration_report.md`、`latest_operation_decision_report.md`、`final_user_operation_result.md` 已补 learning_loop_update。
- `mechanism_sync`：`GPT数据源/11` 新增 `operation_learning_ledger_required`；`GPT数据源/13` 增加 learning ledger gate；`GPT数据源/14` 增加 `bridge_to_copy_learning_memory`。
- `DeepSeek pre-supply`：已创建供料任务卡并运行 safe runner；runtime provider ready，key 未打印 / 未写入，但 controller 返回 `blocked_invalid_context_pack`，因此本轮标记 `fallback_local_only`、`not_deepseek_conclusion = true`。
- `validation`：py_compile passed；system_run passed，生成 29 条 metric event 与 11 个必需 ledger 输出；unittest passed（10 tests）；JSON validation passed；git diff check passed；staged forbidden path check passed；staged secret scan passed；staged forbidden status promotion check passed。
- `git_sync_status`:
  - `current_branch = main`
  - `operation_closure_commit_sha = ecd127d89e7d7f68fc5670d10c1c34c0eae14793`
  - `pushed = true`
  - `remote_head_verified = true`
  - `remote_head_sha = ecd127d89e7d7f68fc5670d10c1c34c0eae14793`
  - `remote_readback_scope = learning_ledger + operation_learning_ledger_script + operation_learning_ledger_tests`
  - `unrelated_dirty_files = public/`
  - `secret_scan = passed`
  - `completed_allowed = true`
- `未推进`：不生成下一条正式视频执行 prompt；不生成下一期完整正式文案；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`；不把 V005 写成内容通过、方向成立或商业验证成立。
- `日志证据`: `codex_log/20260606_第一次运营复盘正反馈闭环修复.md`

## 20260604｜最新发送视频 raw_copy 新增记录

- `task_result.status = latest_sent_video_raw_copy_recorded_pending_human_review`
- `task_mode = additional_task_after_latest_sent_video_data_intake`
- `branch = main`
- `previous_task = latest_sent_video_data_intake`
- `previous_task_commit_sha = 1a9f77f933b4a0bb8dd34378844d8fafc5b96311`
- `git_status_before = only unrelated untracked public/`
- `identified_video_id = V005`
- `video_id_status = confirmed`
- `identified_video_title = codex`
- `visible_thumbnail_text = 还是不赚钱`
- `linked_operation_record_path = review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/V005_发布后运营数据记录_post_publish_operation_record.md`
- `linked_snapshot_path = review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/V005_between_24h_and_72h_snapshot.json`
- `raw_copy_path = review_loop/copy_iteration/V005/V005_copy_v1_raw.md`
- `copy_record_path = review_loop/copy_iteration/V005/V005_copy_v1_record.json`
- `structure_map_path = review_loop/copy_iteration/V005/V005_copy_structure_map.json`
- `copy_notes_path = review_loop/copy_iteration/V005/V005_copy_notes.md`
- `copy_registry_path = review_loop/copy_iteration/copy_registry.json`
- `raw_copy_preserved = true`
- `raw_copy_modified = false`
- `raw_copy_sha256 = ddda203f37f86443723c76b63899ad2fdc5adfcc2b8b10e350bea607fff44fa4`
- `structure_observation_only = true`
- `DeepSeek pre-supply`: `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`
- `DeepSeek post-risk review`: `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`
- `validation`: JSON passed；`git_diff_check` passed；禁止状态检查仅命中边界文字，未发生状态推进。
- `未推进` 不生成下一版正式文案；不生成下一条正式视频执行 prompt；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；不覆盖上一轮数据回填任务。
- `日志证据`: `codex_log/20260604_最新发送视频raw_copy新增记录_copy_iteration_addon.md`

## 20260604｜最新发送视频数据截图回填

- `task_result.status = latest_sent_video_operation_data_intake_completed_pending_human_review`
- `target_video_policy = latest_sent_video_only`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = data_review_loop + review_diagnosis_audit + project_file_change`
- `large_task_gate.triggered = true`
- `write_lane = serial_only`
- `source_dir = /Users/fan/Desktop/数据`
- `source_file_count = 4`
- `image_file_count = 4`
- `matched_existing_record = false`
- `new_record_created = true`
- `identified_video_id = V005`
- `identified_video_title = codex`
- `visible_thumbnail_text = 还是不赚钱`
- `title_confidence = medium`
- `publish_time_visible = 2026-06-03 04:14`
- `publish_time_confidence = high`
- `video_duration_visible = 00:03:23`
- `snapshot_label = between_24h_and_72h_snapshot`
- `review_window = between_24h_and_72h`
- `inferred_hours_after_publish = 约 42 小时 13-15 分`
- `record_path = review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/V005_发布后运营数据记录_post_publish_operation_record.md`
- `structured_snapshot_path = review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/V005_between_24h_and_72h_snapshot.json`
- `screenshot_manifest_path = review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/V005_截图清单_screenshot_manifest.md`
- `已确认` 本轮未写入 V003；未写入 V004；V004 发布时间 / 时长与本轮截图不匹配。
- `已确认` 已归档 4 张原始 PNG，不裁切、不压缩、不覆盖。
- `已确认` 已提取播放量 1514、平均播放时长 8 秒、完播率 0.62%、2s 跳出率 54.68%、5s 完播率 22.45%、推荐页 96.1%、点赞 50、收藏 12、评论 1、分享 2、性别分布男 97% / 女 3% 等可见字段。
- `缺失字段`：24h final、72h final、7d final、3s 留存、主页访问、私信、有效私信、有效咨询、清晰需求客户、评论质量、商业信号等。
- `不确定字段`：页面标题 `codex` 与封面文字 `还是不赚钱` 的关系、年龄精确分布、完整地区分布、是否切换 current_operation_target。
- `current_data_goal_anchor`：仅新增 `latest_sent_video_data_intake` 保守段，不写 ready，不改主短板 / 主变量 / 禁止变量 / 成功失败指标。
- `DeepSeek pre-supply`：已创建并运行安全供料请求；runtime provider 就绪且未打印/写入 key，但 controller 返回 `blocked_invalid_context_pack`，因此 `pre_supply.deepseek_actual_participation = not_attempted_policy_violation`、`pre_supply.not_deepseek_conclusion = true`。
- `DeepSeek post-risk review`：已创建并运行执行后风险复核请求；结果为 `post_risk_review.deepseek_actual_participation = deepseek_passed`、`post_risk_review.not_deepseek_conclusion = false`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`；不生成下一条正式视频执行 prompt；不做最终复盘结论。
- `日志证据`：`codex_log/20260604_最新发送视频数据回填_operation_data_intake.md`、`codex_log/supply_requests/20260604_最新发送视频数据回填_pre_supply_request.json`、`codex_log/supply_requests/20260604_最新发送视频数据回填_post_risk_review_request.json`、`codex_log/deepseek_supply/20260604_latest_sent_video_data_intake_pre_supply/latest_supply_pack.md`、`codex_log/deepseek_supply/20260604_latest_sent_video_data_intake_post_risk_review/latest_supply_pack.md`。

## 20260604｜社交编辑感卡片参考图与 DeepSeek 后置复核补修

- `task_result.status = reference_and_post_risk_review_repair_completed_no_video_generation`
- `target_delivery = social_editorial_card_v1_reference_and_deepseek_post_review_repair`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = project_file_modification_task + mechanism_repair_task + validation_sync_repair_task`
- `large_task_gate.triggered = true`
- `write_lane = serial_only`
- `documented_old_reference_path = 素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png`
- `documented_old_reference_remote_status = missing_on_origin_main`
- `final_reference_path = references/card_style/social_editorial_card_v1_reference.png`
- `final_reference_sha256 = c5c675fee86989a63f1e9369d97b212d409adc1f91f250b921a61164883e531c`
- `visual_reference_status = repo_locked_reference`
- `historical_local_source_path = 素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png`
- `DeepSeek previous post-risk review`：旧请求 `20260604_social_editorial_card_post_risk_review` 返回 `blocked_invalid_context_pack`，保留为未通过记录，不改写成 passed。
- `DeepSeek repaired post-risk review`：已新增并运行更窄的补修复核请求 `codex_log/supply_requests/20260604_社交编辑感卡片参考图补修_post_risk_review_request.json`；请求校验通过，但 controller 仍返回 `blocked_invalid_context_pack`，因此 `deepseek_post_risk_review_status = blocked_invalid_context_pack_pending_fix`、`deepseek_actual_participation = not_attempted_policy_violation`、`not_deepseek_conclusion = true`，不写 passed。
- `DeepSeek repaired output`：`codex_log/deepseek_supply/20260604_social_editorial_card_reference_repair_post_risk_review/latest_supply_pack.md`。
- `Codex local validation`：JSON 解析通过；reference path grep 通过；禁止状态推进窄匹配无命中；secret scan 无命中；`git diff --check` 通过；除允许新增的 `references/card_style/social_editorial_card_v1_reference.png` 外，本轮不提交视频 / 音频媒体，不提交 `dist/latest_review_pack/` 或 `public/`。
- `未推进` 本轮不生成视频，不修改 `dist/latest_review_pack/`，不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `日志证据`：`codex_log/20260604_社交编辑感卡片参考图与DeepSeek后置复核补修.md`。

## 20260604｜16:9 社交编辑感卡片机制补丁

- `task_result.status = mechanism_repair_completed_no_video_generation`
- `target_delivery = social_editorial_card_v1_mechanism`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = project_file_modification_task + mechanism_repair_task + routing_repair_task`
- `large_task_gate.triggered = true`
- `write_lane = serial_only`
- `visual_reference_image_readable = true`
- `approved_visual_reference = references/card_style/social_editorial_card_v1_reference.png`
- `historical_local_source_path = 素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png`
- `reference_path_corrected_by = codex_log/20260604_社交编辑感卡片参考图与DeepSeek后置复核补修.md`
- `已确认` 已新增 `social_editorial_card_v1（社交编辑感卡片 V1）`：正式运营卡片默认横屏 `horizontal_16_9 / 1920x1080`，抖音风负责停留感，Ins 风负责干净质感，少量原创体素 / 像素 / 手绘点缀只做记忆点。
- `已确认` 已补 `judgment_card / summary_card / result_diff_card / prompt_tail_card` 的职责、视觉规则、文本密度、通过 / 失败标准、证据边界和 `copy_change_request` 边界。
- `已确认` `card_placement_decision` 不固定旧 shot、不固定模板位置；`card_budget_gate` 按信息簇插卡，不按句子机械插卡；卡片密度不得高于真实录屏证据密度。
- `已确认` 已补 `card_visual_quality_gate / card_content_boundary_gate / card_failure_route / card_feedback_update`，覆盖比例错配、PPT 感、机械 UI、卡片过密、证据遮挡、locked copy 语义错配、HyperFrames runtime 缺失和 reference 偏离。
- `已确认` 卡片视觉质量只是 `pre-publish human quality gate（发布前人工质量闸门）`，不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `已确认` 卡片只能辅助理解，不得替代中段真实录屏证据，不得新增素材里没有的数据、结论、平台指标或结果差；不得复用官方 Minecraft logo、字体、texture、model、sound 或可识别官方资产。
- `DeepSeek pre-supply`：已创建供料请求并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`；token 使用只能写 `token_decrement_expected / not_available_user_check_required`。
- `DeepSeek post-risk review`：已创建执行后风险复核任务卡并运行 safe runner；controller 返回 `blocked_invalid_context_pack`，因此 `deepseek_actual_participation = not_attempted_policy_violation`、`not_deepseek_conclusion = true`，后置风险复核由 Codex 本地验证继续完成；`api_key_printed = false`、`api_key_written = false`。
- `Codex local validation`：JSON 解析通过；机制关键词 grep 通过；禁止状态推进窄匹配无命中；`git diff --check` 通过；secret scan 通过；媒体 / `dist/latest_review_pack/` / `public/` 路径变更检查无命中；`package.json` 当前无 test script，未运行 npm test。
- `日志证据`：`codex_log/20260604_社交编辑感卡片机制_social_editorial_card_mechanism.md`、`codex_log/supply_requests/20260604_社交编辑感卡片机制_social_editorial_card_pre_supply_request.json`、`codex_log/supply_requests/20260604_社交编辑感卡片机制_social_editorial_card_post_risk_review_request.json`、`dist/deepseek_supply_controller/20260604_social_editorial_card_pre_supply/latest_supply_pack.md`、`dist/deepseek_supply_controller/20260604_social_editorial_card_post_risk_review/latest_supply_pack.md`。
- `待验证` 后续真实视频执行时，仍需按具体 locked copy、素材证据、line_group、subtitle overlap 和 HyperFrames runtime 状态逐片复核；本机制通过不代表后续任意卡片自动美观通过。

## 20260603｜locked_copy_diff_preflight 锁定文案差异预检修复

- `task_result.status = completed_preflight_gate_repaired`
- `target_delivery = locked_copy_diff_preflight_repair`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = code_execution_debug + mechanism_repair + project_file_change`
- `route_decision.selected_state = locked_copy_diff_preflight_required + self_repair_audit_required + mandatory_commit_push_required`
- `已确认` 已修复 `locked_copy_diff_preflight（锁定文案差异预检）`：不再只信任 summary / content_route / tts_map 摘要字段，改为读取并比较真实文本输出层。
- `已确认` 新增对 `script_to_timeline_map.line_groups[].narration_text`、`TTS route report segment_reports[].tts_text`、`final.srt`、`final.ass`、burned subtitle overlay source / function output text、`card_placement_decision.card_groups[].card_text` 和 title card text 的检查。
- `已确认` 任一 locked copy 子检查缺失或失败，都会让 `locked_copy_diff_preflight.status = blocked`，并通过总 suite 的 `failed_gates` 阻断 `publish_candidate_preflight_report`。
- `已确认` 已新增回归测试：`test_locked_copy_subtitle_truncation_blocks` 和 `test_locked_copy_split_subtitle_full_text_passes`。
- `验证通过` `python3 -m py_compile scripts/发片候选预检套件_publish_candidate_preflight_suite.py`。
- `验证通过` `python3 -m unittest tests.test_publish_candidate_preflight_tolerance`，共 6 个测试通过。
- `验证通过` `python3 -m unittest tests.test_publish_candidate_voice_gate tests.test_minimax_b_voice_identity_lock tests.test_publish_candidate_preflight_tolerance`，共 28 个测试通过。
- `只读复核` 使用新闸门读取第五期现有候选片产物，结果为 `status = blocked`，failed_subchecks 包含 `subtitle_copy_match / ass_copy_match / burned_subtitle_copy_match / card_text_semantic_match`，能抓到旧问题：`有人整理素材。有人做下一版测试。` 被字幕截断。
- `未推进` 本轮未修第五期视频、未重生成字幕、未重生成 TTS、未修改卡片、未修改最终文案、未推进 `content_validation / send_ready / publish_status_success / voice_validation / visual_master_locked`。
- `日志证据`：`codex_log/20260603_locked_copy_diff_preflight_repair.md`、`codex_log/copy_lock_audit/20260603_locked_copy_drift_audit.md`。

## 20260603｜第五期 Codex 赚钱主题完整正片候选片

- `task_result.status = publish_candidate_ready_for_human_review`
- `target_delivery = fifth_episode_codex_money_publish_candidate`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = video_sample_or_assembly + project_file_change + review_diagnosis_audit`
- `large_task_gate.triggered = true`
- `full_video = dist/fifth_episode_codex_money_publish_candidate_20260603/full.mp4`
- `full_video_absolute_path = /Users/fan/Documents/视频工厂/dist/fifth_episode_codex_money_publish_candidate_20260603/full.mp4`
- `review_pack = dist/fifth_episode_codex_money_publish_candidate_20260603/review_pack/`
- `review_manifest = dist/fifth_episode_codex_money_publish_candidate_20260603/review_manifest.md`
- `summary_json = dist/fifth_episode_codex_money_publish_candidate_20260603/summary.json`
- `publish_candidate_preflight_report = dist/fifth_episode_codex_money_publish_candidate_20260603/publish_candidate_preflight_report.json`
- `已确认` 已按 locked title / locked opening line / locked final script 生成完整横屏 16:9 / 1920x1080 正片候选片；不是技术预览、不是 silent preview、不是 route card、不是局部片段。
- `已确认` TTS 完整音轨已生成：`actual_tts_provider = minimax`、`actual_tts_model = MiniMax/speech-2.8-hd`、`actual_voice_id_or_voice_route = oldBMinimax20260528010200`、`tts_audio_path = dist/fifth_episode_codex_money_publish_candidate_20260603/audio/tts_full.wav`、`tts_duration = 203.646s`、`audio_present = true`、`non_silent = true`。
- `已确认` 已生成 `subtitles/final.srt` 与 `subtitles/final.ass`，并通过本地 overlay 方式烧录字幕；`subtitle_card_overlap_check = passed`，`high_severity_overlap_count = 0`。
- `已确认` 已生成本地标题卡 / 判断卡 / 三栏卡 / 过渡卡 / 金句卡 / CTA 卡 / 总结卡；`visual_api_generation_used = false`、`api_human_used = false`、`local_card_generation_used = true`。
- `已确认` M01-M05 均按 Shot Map 和素材证据契约使用：M01/M05 只做执行纪律 / QA 证据；M02 只做候选池和多项目可能性；M03/M04 只做问题入口与判断框架画面承载；不写商品已经赚钱、商业验证通过、账号跑通或 vlog 跑通。
- `已确认` `script_to_timeline_map` 覆盖 41 个 line_group；`line_level_alignment_preflight = passed`、`mismatch_count = 0`、`unresolved_mismatch_count = 0`。
- `已确认` `publish_candidate_preflight_report.status = passed`；`video_metadata_probe` 通过：`duration = 203.647s`、`resolution = 1920x1080`、`audio_codec = aac`、`decodable = true`、`validation_status = passed`。
- `DeepSeek pre-supply`：已创建供料请求并运行 safe runner；runtime provider 找到授权且 `api_key_printed = false / api_key_written = false`，但 controller 输出 `blocked_invalid_context_pack`，因此 `deepseek_actual_participation = not_attempted_policy_violation`、`fallback_status = not_used`、`not_deepseek_conclusion = true`；本轮风险结论来自 Codex 本地复核。
- `DeepSeek post-risk review`：已创建后置风险复核任务卡并运行 safe runner；runtime provider 找到授权且 `api_key_printed = false / api_key_written = false`，但 controller 同样输出 `blocked_invalid_context_pack`，因此 `deepseek_actual_participation = not_attempted_policy_violation`、`fallback_status = not_used`、`not_deepseek_conclusion = true`；不写 DeepSeek passed。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；不修改源素材；不修改 `dist/latest_review_pack/`。
- `Git policy`：`dist/` 当前被本地 exclude，媒体文件不提交 Git；已同步 `codex_log/current_local_artifact_paths.md` 记录本地绝对路径。
- `日志证据`：`codex_log/20260603_第五期Codex赚钱主题正片执行.md`、`codex_log/supply_requests/20260603_第五期Codex赚钱主题正片_pre_supply_request.json`、`dist/fifth_episode_codex_money_publish_candidate_20260603/`。

## 20260603｜第五期录制素材 5 个视频细节解析

- `task_result.status = completed_material_audit_pending_chatgpt_copy_judgement`
- `target_delivery = fifth_episode_material_evidence_flow`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = review_diagnosis_audit + local_file_governance + project_file_change`
- `route_decision.selected_state = material_audit_needed + deepseek_supply_required + mandatory_commit_push_required`
- `workflow_route_decision.workflow_type = material_evidence_flow`
- `source_dir = /Users/fan/Documents/视频工厂/素材录制/第五期`
- `analysis_dir = codex_log/material_audit/20260603_第五期素材细节解析/`
- `media_evidence_dir = dist/material_audit/20260603_第五期素材细节解析/`
- `已确认` 本轮从粘贴文本中的 Codex 执行 prompt 接手，只做第五期 5 个录制视频的素材细节解析、时间码证据、关键帧、contact sheet、短证据片段和 ChatGPT 交接摘要；不是写最终文案、不是剪辑成片、不是 TTS、不是发片候选。
- `已确认` 5/5 源视频均完成 `ffprobe`、`video-metadata-probe`、OpenCV 抽帧与 contact sheet；全部可解码，全部 `audio_present = false`。
- `已确认` 已生成 `material_inventory.json`、`timecode_evidence_map.json`、`sample_frame_index.json`、`material_detail_report.md`、`chatgpt_handoff_brief.md`、`missing_or_uncertain_points.md`、`reshoot_suggestions.md`、`material_evidence_contract.json` 和 `final_self_check.json`。
- `已确认` 已生成 270 张 keyframe JPEG、19 张 contact sheets、19 个 3 秒 evidence clips；源视频未修改、未移动、未删除、未上传。
- `核心判断`：M04 是候选商品 / 单独立项判断框架主轴；M03 是用户问题入口；M02 是候选媒体池例子；M01/M05 是执行流程、no fallback、contact sheet 和 frame review 闸门证据。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；不调用图片 / 视频 / TTS 生成 API；不修改 `dist/latest_review_pack/`。
- `DeepSeek pre-supply`：已创建供料请求并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`，token 使用只能写 `token_decrement_expected / not_available_user_check_required`。
- `DeepSeek post-risk review`：已创建执行后风险复核任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`；复核提醒本地绝对路径只适合内部交接，M01/M04 小字与阈值不得逐字过度引用。
- `日志证据`：`codex_log/supply_requests/20260603_第五期素材解析_pre_supply_request.json`、`codex_log/deepseek_supply/20260603_fifth_material_audit_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260603_第五期素材解析_post_risk_review_request.json`、`codex_log/deepseek_supply/20260603_fifth_material_audit_post_risk_review/latest_supply_pack.md`、`codex_log/material_audit/20260603_第五期素材细节解析/material_detail_report.md`。

## 20260602｜最新 4 条剪辑参考动态视觉母版重解析

- `task_result.status = dynamic_visual_master_parse_completed_pending_user_chatgpt_review`
- `target_delivery = latest_4_dynamic_visual_master_reparse_reference_analysis_only`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = review_diagnosis_audit + reference_analysis_only + local_file_governance + project_file_change`
- `route_decision.selected_state = dynamic_visual_master_parse`
- `已确认` 本轮只从源视频重解析 4 条最新剪辑参考的动态视觉母版、第一眼视觉、构图、字体 / 字幕 / 高亮、运动转场、密度层级和注意力路径；不是生成视频、不是验证片、不是完整候选片、不是回炉新第四期。
- `source_dir = /Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考`
- `analysis_dir = codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `media_evidence_dir = dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `已确认` 4/4 源视频完成 `ffprobe`、video-metadata-probe、ffmpeg 单帧抽取、OpenCV 打开与 5s 抽帧；每条均生成 scene candidate frames、1 秒动态证据 clips 和 contact sheets。
- `已确认` 上一轮 `codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/` 降级为 `failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only`；旧报告只作为失败样本，不作为本轮主视觉判断。
- `已确认` 本轮重新分类：`reference_03 = primary_teaching_dynamic_visual_master`，`reference_04 = primary_long_text_evidence_window_master`，`reference_01 = support_result_montage_and_comparison_master`，`reference_02 = support_phone_keyword_badge_packaging`。
- `已确认` 本轮核心发现：可迁移的是黑底 / 深灰舞台、主持人 reset、证据窗口、黄绿读线、关键词 badge、密度重置和注意力路径；不可复制竖屏平台壳、互动栏、真人脸、第三方 app / logo / UI / 字体 / 片段素材。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；不修改新第四期，不修改源视频，不修改 `GPT数据源/` 正式机制，不修改 `codex_source/` 正式规则，不修改 `dist/latest_review_pack/`。
- `DeepSeek pre-supply`：已创建供料请求并运行 safe runner；runtime provider 找到授权且 `api_key_printed = false / api_key_written = false`，但 controller 输出 `blocked_invalid_context_pack`，因此 `deepseek_actual_participation = not_attempted_policy_violation`，`fallback_status = fallback_local_only`，`not_deepseek_conclusion = true`。
- `日志证据`：`codex_log/supply_requests/20260602_最新剪辑参考4条动态视觉母版重解析_pre_supply_request.json`、`codex_log/deepseek_supply/20260602_latest_4_dynamic_visual_master_reparse_pre_supply/latest_supply_pack.md`。

## 20260602｜需求不确定澄清闸门与 GPT Project 资料同步包

- `task_result.status = mechanism_route_corrected_not_video_delivery`
- `target_delivery = ambiguous_goal_clarification_gate + ambiguous_reference_goal_gate + gpt_project_sync_package`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = mechanism_or_route_fix + project_file_change + gpt_project_static_package_sync`
- `route_decision.selected_state = mechanism_repair_needed + gpt_project_sync_needed + deepseek_supply_required`
- `已确认` 本轮只修《视频工厂》机制入口、reference 契约和 GPT Project 资料同步包；不是修视频、不是重新剪辑、不是生成新片、不是生成下一条正式视频执行 prompt。
- `已确认` 已新增 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）`，覆盖 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思 / 最高价值片子` 等高歧义目标；目标层级未锁定前不得直接下发 Codex。
- `已确认` 已新增 `ambiguous_reference_goal_gate（参考目标歧义闸门）`；reference 目标含糊时，必须先确认视觉观感、剪辑节奏、构图布局、字幕字体、动效、信息密度、证明方式、内容结构、情绪人感或整体观感，再进入 `Reference-to-Execution Contract`。
- `已确认` 已写入 ChatGPT / GPT Project 默认澄清模板：用户确认前不下发 Codex；若用户要求不追问直接做，也必须写清默认假设、风险、允许变化项和阻断条件。
- `gpt_project_sync_package = dist/gpt_project_sync_packages/20260602_需求不确定澄清闸门_ambiguous_goal_clarification_gate/`
- `gpt_project_sync_package_upload_manifest = dist/gpt_project_sync_packages/20260602_需求不确定澄清闸门_ambiguous_goal_clarification_gate/上传说明_UPLOAD_MANIFEST.md`
- `已确认` 同步包只包含上传说明、同步说明、变更清单、机制补丁、状态边界、项目入口机制文件副本和 Codex 执行层镜像；不包含视频、图片、音频、源素材、`dist/latest_review_pack/`、secret、API key、token、无关 `public/` 文件或大量历史日志。
- `未推进` 不推进内容验证、可发送状态、发布成功口径、声音验证、最终声音验证、视觉母版或当前数据目标锚点 ready；不把本机制写成长期稳定。
- `待验证` 本机制是否能在后续真实 reference / 视频任务中稳定阻断误下发，仍需后续真实任务验证。
- `DeepSeek pre-supply`：已创建执行前供料任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。
- `DeepSeek post-risk review`：已创建执行后风险复核任务卡并运行 safe runner；请求校验通过，但供料控制器返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮后置风险结论来自 Codex 本地验证，不写 DeepSeek 已深度参与。
- `日志证据`：`codex_log/supply_requests/20260602_需求不确定澄清闸门_pre_supply_request.json`、`codex_log/deepseek_supply/20260602_ambiguous_goal_clarification_gate_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260602_需求不确定澄清闸门_post_risk_review_request.json`、`codex_log/deepseek_supply/20260602_ambiguous_goal_clarification_gate_post_risk_review/latest_supply_pack.md`

## 20260602｜新第四期参考引导完整候选片生成

- `task_result.status = publish_candidate_ready_for_human_review`
- `target_delivery = new_fourth_reference_guided_full_publish_candidate`
- `branch = main`
- `已确认` 用户本轮明确允许直接使用新第四期原始素材做剪辑；本轮不再以“素材授权不足”作为阻断理由。
- `已确认` 已生成完整横屏 16:9 / 1920x1080 候选片，不是 30-45 秒验证片、silent preview、technical preview 或 Markdown route card。
- `full_video = dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/full.mp4`
- `review_pack = dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523`
- `review_manifest = dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/review_manifest.md`
- `reference_deviation_check = dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/reference_deviation_check.json`
- `publish_candidate_preflight_report = dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/publish_candidate_preflight_report.json`
- `已确认` 参考迁移口径：`primary_reference = reference_03`，`secondary_reference = reference_04`，`support_reference = reference_01`，`reference_02 = keyword_subtitle_phone_packaging_only_not_main_style`。
- `已确认` 本轮迁移了全片 `active_evidence_window`、字幕视线引导、功能关键词 badge 和低密度 bridge 提示；`guided_split_screen` 因多数句组不构成真实 A/B、source/output 或 before/after 对比，已按规则不强行迁移。
- `已确认` `publish_candidate_preflight_suite` 14 项 gate 全部 passed；`ffprobe / ffmpeg decode / audio_present / non_silent / subtitles_present / JSON parse / secret scan` 均 passed。
- `已确认` 抽帧复核发现 overlay 已覆盖全片，不再只停留在开头帧；仍需用户 / ChatGPT 做最终观感复审。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；本轮状态仍为候选片待人工复审。
- `DeepSeek`：已创建执行前供料任务卡并运行 safe runner；结果为 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核与预检结果，不写 DeepSeek 已深度参与。
- `日志`：`codex_log/20260602_新第四期参考引导完整候选片_new_fourth_reference_guided_publish_candidate.md`

## 20260601｜素材证据闸门选择性恢复并接回预检套件

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = material_evidence_gate_restored_and_connected_to_publish_candidate_preflight_suite`
- `branch = codex/restore-material-evidence-gate-20260601`
- `已确认` 本轮从 `stash@{0}^3` 只选择性恢复 3 个目标文件：`scripts/素材证据闸门_material_evidence_gate.py`、`tests/test_material_evidence_gate.py`、`codex_source/fixtures/素材证据闸门_material_evidence_gate_cases.json`。
- `已确认` 没有整包 `git stash apply`，没有恢复整个 `stash@{0}^3`，没有提交 `public/` 或 `dist/` 内容。
- `已确认` `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` 已新增 `material_evidence_gate_preflight`，并调用素材证据闸门输出 `material_evidence_contract.json`、`line_group_evidence_gate_report.json` 与 `auto_storyboard_preflight_report.json`。
- `已确认` 若素材证据闸门失败或 `auto_edit_allowed != true`，整体 `publish_candidate_preflight_suite` 必须 `blocked`，不得继续冒充发片候选预检通过。
- `已确认` 本轮未生成视频、未剪辑媒体、未调用 TTS / 视频 / 图片生成 API，未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。
- `DeepSeek`：已创建执行前供料任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`；token 使用只能写 `token_decrement_expected / not_available_user_check_required`，不写用户 token 面板已确认。
- `日志`：`codex_log/20260601_restore_material_evidence_gate.md`

## 20260601｜对标文案原文级 reference 改为 Google Drive 路线

- `task_result.status = mechanism_route_corrected_not_video_delivery`
- `target_delivery = google_drive_raw_reference_route + entry_sync`
- `已确认` 5 篇对标账号文案原文级 reference 默认保存在 Google Drive；GitHub 仓库不建立本地 raw 原文文件体系，不保存第三方原文全文，不建立复杂本地 reference manifest。
- `已确认` 已更新 `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`：新增 `原文级 reference 读取规则`，并将 `/Users/fan/Desktop/文案.rtf` 降级为 `historical_import_source_path（历史导入来源）`，不再作为后续默认读取路径。
- `已确认` 已更新 `GPT数据源/03_总索引与阅读顺序.md`：命中 `对标原文 / 原文级 reference / 强贴对标语气` 时，先读 15 号标准；如需全文参考，由 ChatGPT / GPT Project 从 Google Drive 读取原文后桥接进当轮任务，不从 GitHub 读取第三方全文。
- `已确认` 仓库只保存学习卡、判断标准、迁移边界和读取规则；Codex 默认不知道 Google Drive 原文，如需使用，必须由 ChatGPT 桥接进执行单或由用户当轮提供可读内容 / 链接。
- `未推进` 本轮未生成视频、未生成下一条正式视频执行 prompt，未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。
- `DeepSeek`：已创建前置供料任务卡与执行后风险复核任务卡并运行 safe runner，前置供料与 post-risk review 均为 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。
- `日志证据`：`codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_google_drive_raw_reference_route_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_post_risk_review_request.json`、`codex_log/deepseek_supply/20260601_google_drive_raw_reference_route_post_risk_review/latest_supply_pack.md`

## 20260601｜对标文案学习与说人话判断标准落库

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = copy_reference_learning_standard + entry_sync`
- `已确认` 本轮读取用户提供的 5 篇外部对标账号文案，并新增长期机制文件：`GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`。
- `已确认` 新文件只保存结构化学习卡和判断标准，不保存外部文案全文；5 篇文案被作为 `reference_pack（参考包）`、`copywriting_style_learning_reference（文案学习参考）`、`plain_language_and_visual_sense_standard_source（说人话与画面感标准来源）` 使用。
- `已确认` 新增标准覆盖：`plain_language_standard（说人话标准）`、`visual_sense_standard（画面感标准）`、`focus_allocation_rule（重点分配规则）`、`rhythm_standard（节奏标准）`、五篇逐篇学习卡、用户账号迁移边界和最终落稿前检查清单。
- `已确认` 已同步入口：`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`。
- `已确认` 本轮只修文案学习机制与入口引用；未生成新视频，未生成下一条正式视频执行 prompt，未改最终文案，未改视频 / 音频 / TTS / 剪辑脚本 / API 配置 / `dist/latest_review_pack/`。
- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。
- `待验证` 该标准是否适合用户账号，仍需后续发布后数据、人审反馈和真实文案回审校准；不得写成用户最终风格已确定或对标风格已被数据验证。
- `DeepSeek`：已创建前置供料任务卡与执行后风险复核任务卡并运行 safe runner，前置供料与 post-risk review 均为 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。
- `日志证据`：`codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260601_对标文案学习标准_post_risk_review_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_post_risk_review/latest_supply_pack.md`

## 20260529｜一次素材解析复用标准接入

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = material_parse_pack_reuse_standard + no-render gate`
- `已确认` 本轮制定“一次素材解析，后续剪辑复用解析包”标准，并接入执行链：`material_parse_pack -> source_segment_inventory -> script_to_shot_execution_map -> material_usage_ledger -> duplicate_material_check -> editing_decision_pack -> render / assembly`。
- `已确认` 原始素材只解析一次；剪辑阶段只能读取同一份 `material_parse_pack（素材解析包）`，不得重新解析原始素材作为主要判断来源。
- `已确认` `material_parse_pack（素材解析包）` 已定义必填字段、`reuse_policy` 和 `stale_if（过期条件）`；解析包缺失、过期或关键证据字段不足时必须 blocked。
- `已确认` 新增 no-render 脚本：`scripts/素材解析包复用闸门_material_parse_pack_reuse_gate.py`；并接入 `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` 的 `material_parse_pack_reuse_preflight`。
- `已确认` `duplicate_material_check（素材重复使用检查）` 阻断：缺解析包 / 缺片段清单 / 缺文案到镜头执行表 / 缺素材使用台账 / 无理由重复同一片段 / 连续重复片段 / 核心证据复用证明不同主张 / 主题相近硬配 / 选用 `cannot_support` 素材 / 句组未引用素材报告。
- `已确认` fixture 与测试新增：`codex_source/fixtures/素材解析包复用闸门_material_parse_pack_reuse_gate_cases.json`、`tests/test_material_parse_pack_reuse_gate.py`，覆盖 JSON parse、缺解析包、无理由重复片段、`cannot_support` 选中、主题相近硬配。
- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。
- `待验证` 后续真实剪辑任务仍需用真实 `material_parse_pack / source_segment_inventory / script_to_shot_execution_map / material_usage_ledger` 跑 gate，才能判断该标准是否稳定生效；本轮不写成“剪辑问题已解决”或“素材复用机制长期稳定”。
- `日志`：`codex_log/20260529_一次素材解析复用标准_material_parse_pack_reuse.md`

## 20260528｜锁定旧 B 迁移 MiniMax 声音并只替换当前候选片音轨

- `task_result.status = completed_with_locked_b_voice_audio_replacement`
- `target_delivery = b_voice_identity_lock + full_narration_regeneration_only + audio_track_replacement_only`
- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。
- `locked_voice.expected_b_minimax_voice_id = oldBMinimax20260528010200`；`selected_sample_version = V2_prosody_optimized`；`human_voice_review_status = user_confirmed`；`timbre_change_allowed = false`；`micro_tuning_allowed = true`。
- `generation_route`：`actual_tts_provider = minimax`；`actual_tts_model = MiniMax/speech-2.8-hd`；`selected_route = aliyun_bailian_proxy_to_minimax`；`fallback_used = false`；`system_voice_substitution_used = false`。
- `narration_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/narration.wav`；`actual_voice_id = oldBMinimax20260528010200`；`non_silent = true`；`mean_volume = -16.0 dB`；`duration = 636.254s`。
- `output_video_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/full.mp4`；源视频为 `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4`。
- `media_validation`：`video_stream_unchanged = true`；`audio_track_replaced_only = true`；`audio_present = true`；`ffmpeg_decode = passed`；`video probe = 1920x1080 / 636.254s / h264 / aac / decodable`。
- `copy_changed = false`；`visual_changed = false`；本轮未改锁稿、未重新剪辑、未重新抽系统音色、未恢复旧 Qwen 正式路线。
- `review_pack_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322`
- `reports`：`tts_route_report.json / b_voice_identity_lock_report.json / voice_gate_report.json / media_probe.json / ffmpeg_decode_check.log / audio_volumedetect.log / review_manifest.md`
- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。
- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 DeepSeek 已参与。
- `验证`：`py_compile` passed；`python3 -m unittest tests.test_publish_candidate_voice_gate tests.test_minimax_b_voice_identity_lock` 22/22 passed；voice gate rerun passed；JSON parse passed；`git diff --check` passed；secret scan passed。
- `日志`：`codex_log/20260528_lock_old_b_minimax_voice_audio_replace.md`

## 20260528｜旧 B 通过阿里百炼代理迁移到 MiniMax 试听样本

- `task_result.status = completed_with_old_b_minimax_samples_via_bailian`
- `target_delivery = old_b_to_minimax_via_aliyun_bailian`
- `auth_route_recheck`：上一轮 `minimax_official_api_key_missing` 阻断被用户纠正；本轮 `should_require_minimax_official_key = false`，实际使用 `aliyun_bailian_proxy_to_minimax`。
- `aliyun_bailian_auth_check`：项目既有本地正式运行配置 `[auth].api_key` 可用；`api_key_printed = false`；`api_key_written = false`。
- `bailian_minimax_clone_capability`：支持 `MiniMax/speech-2.8-hd`、`voice_clone`、`reference_audio`；百炼链路需要 `audio_url`，不接受直接本地文件；官方证据：`https://help.aliyun.com/zh/model-studio/mini-clone-api`。
- `reference_audio_inputs`：已仅上传用户授权的两条旧 B 参考音频到用户可控 OSS，并在报告中只保留脱敏签名 URL；未提交参考音频到 Git。
- `generated_minimax_voice_id = oldBMinimax20260528010200`
- `generated_samples`：
  - `V1_identity_match`: `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V1_identity_match.mp3`，`duration = 15.697s`，`non_silent = true`
  - `V2_prosody_optimized`: `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`，`duration = 16.236s`，`non_silent = true`
  - `V3_emotion_rich`: `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V3_emotion_rich.mp3`，`duration = 15.660s`，`non_silent = true`
- `diagnostics_path = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200`
- `migration_report = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/old_b_to_minimax_bailian_report.json`
- `review_table = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/voice_candidate_review_table_old_b_minimax.md`
- `old_b_to_minimax_voice_lock.status = pending_user_review`；`generated_minimax_voice_id = oldBMinimax20260528010200`；`human_voice_review_status = pending_user_review`；`system_voice_substitution_allowed = false`。
- `状态边界`：未生成全片旁白，未替换当前视频音轨，未生成视频，未改文案，未改画面，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。
- `DeepSeek`：前置供料与执行后风险复核均实际运行通过，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。
- `日志`：`codex_log/20260528_old_b_to_minimax_bailian.md`

## 20260527｜旧 B 到 MiniMax 迁移上传授权解阻检查

- `task_result.status = blocked`
- `target_delivery = old_b_to_minimax_migration_unblocked`
- `route_arbitration`：`old_qwen_role = reference_anchor_only`；`minimax_role = final_generation_provider`；`selected_route = route_b_migrate_old_b_to_minimax`；`system_voice_candidates_allowed = false`。
- `user_authorization = received`：用户授权仅上传两条旧 B 参考音频用于 MiniMax voice clone / reference 短样本；本轮未上传，因为当前官方 MiniMax clone 链路缺 `MINIMAX_API_KEY`。
- `reference_audio.loaded = true`：`B_15秒文案_停顿梗感.wav` 为 `16.32s / 24000 Hz / mono / wav`；`语音样本2_声音复刻试听_15秒.wav` 为 `13.60s / 24000 Hz / mono / wav`。
- `upload_strategy.selected = minimax_official_file_upload`；原因是 MiniMax 官方 voice clone 要先 `/v1/files/upload` 获取 `file_id`，再 `/v1/voice_clone` 创建 `voice_id`；仅上传到 OSS 不能在当前官方链路里直接生成 `generated_minimax_voice_id`。
- `blocked_reason = minimax_official_api_key_missing`；`audio_url_created = false`；`file_id_created = false`；`generated_samples = none`。
- `diagnostics_path = codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125`
- `migration_report = codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125/old_b_to_minimax_migration_unblocked_report.json`
- `review_table = codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125/voice_candidate_review_table_old_b_minimax.md`
- `old_b_to_minimax_voice_lock.status = pending_minimax_official_auth`；`generated_minimax_voice_id = null`；`human_voice_review_status = pending_minimax_official_auth`；`system_voice_substitution_allowed = false`。
- `状态边界`：未生成音频 / 视频，未上传参考音频，未调用 MiniMax TTS / clone API，未改文案，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。
- `DeepSeek`：已创建前置供料任务卡与后置风险复核任务卡并运行 safe runner；两次均返回 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。
- `日志`：`codex_log/20260527_old_b_to_minimax_migration_unblocked.md`

## 20260527｜旧 B 到 MiniMax 声音迁移审计

- `task_result.status = blocked_need_reference_audio_url`
- `target_delivery = old_b_to_minimax_voice_migration`
- `route_arbitration`：`old_qwen_role = reference_anchor_only`；`minimax_role = final_generation_provider`；`selected_route = route_b_migrate_old_b_to_minimax`；`system_voice_candidates_allowed = false`。
- `video_generated = false`；`audio_generated = false`；`tts_api_called = false`；`copy_changed = false`；`current_video_modified = false`。
- `diagnostics_path = codex_log/diagnostics/old_b_to_minimax_migration_20260527_224840`
- `migration_report = codex_log/diagnostics/old_b_to_minimax_migration_20260527_224840/old_b_to_minimax_migration_report.json`
- `old_b_reference_audio.loaded = true`：已读取 `B_15秒文案_停顿梗感.wav` 与 `语音样本2_声音复刻试听_15秒.wav` 的存在性和音频元信息。
- `minimax_reference_clone_capability`：MiniMax 官方 voice clone 支持先上传参考音频获取 `file_id` 再克隆 `voice_id`；仓库当前百炼代理链路记录为需要公网 `audio_url`。
- `blocked_reason = reference_audio_url_or_upload_authorization_missing`：当前没有旧 B 参考音频公网 `audio_url`，也没有本轮用户授权上传参考音频；因此未调用 MiniMax TTS / clone API，未生成迁移样本。
- `forbidden_replacement_rule.active = true`：禁止用 MiniMax 系统女声、男声或中性候选替代旧 B；旧 Qwen / 阿里 B 只作参考锚点，不恢复为正式默认路线。
- `old_b_to_minimax_voice_lock.status = pending_reference_audio_url`；`target_provider = minimax`；`target_model = MiniMax/speech-2.8-hd`；`generated_minimax_voice_id = null`；`system_voice_substitution_allowed = false`；`old_qwen_formal_route_allowed = false`；`human_voice_review_status = pending_reference_audio_url`。
- `DeepSeek`：已创建供料任务卡并运行 safe runner；runtime provider ready，key 未打印 / 未写入；controller 返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`。
- `状态边界`：未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。
- `日志`：`codex_log/20260527_old_b_to_minimax_migration.md`

## 20260527｜旧阿里 / Qwen B 方案声音恢复审计

- `task_result.status = completed_old_b_voice_audit`
- `target_delivery = old_aliyun_b_voice_restoration_audit`
- `video_generated = false`；`audio_generated = false`；`tts_api_called = false`；`copy_changed = false`；`current_video_modified = false`。
- `diagnostics_path = codex_log/diagnostics/old_aliyun_b_voice_restoration_audit_20260527_222316`
- `audit_report = codex_log/diagnostics/old_aliyun_b_voice_restoration_audit_20260527_222316/old_b_voice_restoration_audit_report.json`
- `old_b_voice_fact`：`provider = aliyun_bailian`；`api_route_family = aliyun_qwen_realtime_websocket_voice_clone`；`model / target_model = qwen3-tts-vc-realtime-2026-01-15`；`custom_voice_masked_id = qwen-t...ac19`。
- `old_b_reference_audio.loaded = true`：已读取 `B_15秒文案_停顿梗感.wav` 与 `语音样本2_声音复刻试听_15秒.wav`；本轮仅探测存在性与音频元信息，不生成新样本。
- `route_conflict.exists = true`：当前仓库近期默认 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`，但用户最新指令要求恢复旧阿里 / Qwen B 方案声音；不得通过继续抽 MiniMax 系统候选解决。
- `forbidden_replacement_rule.active = true`：`female-tianmei / female-shaonv / female-shaonv-jingpin / female-yujie` 不能替代旧 B；`male-qn-qingse / male-qn-daxuesheng / Chinese (Mandarin)_Gentleman / Chinese (Mandarin)_Gentle_Youth / Chinese (Mandarin)_Sincere_Adult` 等男声或中性系统候选也不能直接替代旧 B。
- `next_route.selected = route_a_restore_old_qwen_b`；原因是旧 B 证据链完整且用户当前明确要求恢复以前阿里大模型 B 声音；下一轮如授权调用 TTS API，先做最小 runtime smoke。
- `current_callable_status = pending_runtime_smoke`：旧脚本和历史授权运行证据存在，但本轮禁止调用 TTS API，且旧修复候选脚本当前有 `LEGACY_B_VOICE_ROUTE_BLOCKED_FOR_PUBLISH_CANDIDATE = True`，所以不写当前已通过。
- `DeepSeek`：已创建供料任务卡并运行 safe runner；runtime provider ready，key 未打印 / 未写入；controller 返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`。
- `状态边界`：未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。
- `日志`：`codex_log/20260527_old_aliyun_b_voice_restoration_audit.md`

## 20260527｜工作流入口归位索引

- `task_result.status = completed_with_entry_routing_index`
- `target_delivery = workflow_entry_routing_index`
- `repair_scope = Codex 执行入口层 / routing index layer`
- `audit_recheck`：`missing_standard = false`；`routing_index_gap = true（主缺口）`；`execution_discipline_gap = true（次缺口）`；`execution_entry_gap = partial`。
- `routing_index_path = codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- `codex_entry_updated = codex_source/00_codex_readme.md`
- `execution_rules_updated = codex_source/01_execution_rules.md`
- `state_action_router_updated = codex_source/19_project_state_action_router.md`
- `fixture_updated = codex_source/fixtures/mechanism_inference_function_cases.json`
- 新增要求：Codex 每轮在 `route_decision（路由判断）` 后、具体执行前，必须输出 `workflow_route_decision（工作流归位判断）`，并从 `copy_testing_flow / material_evidence_flow / aesthetic_editing_flow / quality_review_flow / data_review_flow / mechanism_repair_flow` 中选择工作流。
- `workflow_route_decision` 必须写明：`workflow_type / reason / must_read / required_handoff / forbidden_status / blocked_if`。
- `status_boundary`：未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。
- `video_generated = false`；`audio_generated = false`；`copy_changed = false`；`media_changed = false`。
- 本轮只修入口索引；未新增文案 / 素材 / 剪辑 / 复盘大机制；不代表机制长期稳定。
- 后续真实任务必须验证 Codex 是否稳定输出 `workflow_route_decision`。
- `日志`：`codex_log/20260527_工作流入口归位索引_workflow_entry_routing_index.md`

## 20260527｜B 声音本体重审与 MiniMax 男声/偏男候选试听包

- `task_result.status = completed_with_reaudited_voice_candidates`
- `target_delivery = b_voice_identity_reaudit_and_male_leaning_minimax_candidates`
- `video_generated = false`；`full_narration_regenerated = false`；`copy_changed = false`；`current_video_modified = false`。
- `diagnostics_path = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222`
- `audit_report = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/minimax_b_voice_identity_reaudit_report.json`
- `review_table_v2 = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/voice_candidate_review_table_v2.md`
- `previous_rejection_report = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/previous_candidate_rejection_report.json`
- `previous_wrong_candidates.rejected_by_user = [female-shaonv, female-shaonv-jingpin, female-yujie]`；`reason = wrong_gender_and_wrong_voice_identity`；`future_use_allowed = false`。
- `b_voice_reference_audio.loaded = true`：已读取 `B_15秒文案_停顿梗感.wav` 与 `语音样本2_声音复刻试听_15秒.wav`；音频可解码、非静音，停顿结构已记录到 `b_voice_reference_audit.json`。
- `b_voice_target_profile.gender_target = male_or_male_leaning`；旧 `可爱女生向导音` 口径只保留为历史冲突口径，不得覆盖当前 B 声音身份锁。
- `minimax_voice_list = read_ok`；`system_voice_count = 303`；本轮筛出男声/偏男候选后生成 5 个基础 voice_id、10 条短试听样本。
- `new_voice_candidates = [male-qn-qingse, male-qn-daxuesheng, Chinese (Mandarin)_Gentleman, Chinese (Mandarin)_Gentle_Youth, Chinese (Mandarin)_Sincere_Adult]`；每个候选均有 `v1_identity_stable` 与 `v2_emotional_rich`。
- `b_voice_identity_lock.status = pending_user_review`；`expected_b_minimax_voice_id = null`；`required_gender_direction = male_or_male_leaning`；`forbidden_voice_ids = [female-tianmei, female-shaonv, female-shaonv-jingpin, female-yujie]`；`human_voice_review_required = true`；`human_voice_review_status = pending_user_review`。
- `新增机制`：后续正片候选必须检查 `actual_voice_id == expected_b_minimax_voice_id`、`actual_voice_id not in forbidden_voice_ids`、`actual_gender_direction = male_or_male_leaning`、`timbre_change_allowed = false`、`human_voice_review_status = user_confirmed`；任一不满足必须 blocked。
- `状态边界`：未推进 `send_ready / content_validation / voice_validation / final_voice_validated / visual_master_locked`。
- `DeepSeek`：已创建供料任务卡并运行 safe runner；runtime provider ready，但 controller 返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + MiniMax 实测，不写 DeepSeek 已参与。
- `验证`：`py_compile` passed；`tests.test_publish_candidate_voice_gate` + `tests.test_minimax_b_voice_identity_lock` + `tests.test_publish_candidate_preflight_tolerance` 16/16 passed；`publish_candidate_preflight_suite --no-render` fixture validation passed（24 cases）。
- `日志`：`codex_log/20260527_b_voice_reference_reaudit_and_minimax_candidates.md`

## 20260527｜MiniMax B 方案声音身份锁定候选试听包

- `task_result.status = completed_with_voice_candidates`
- `target_delivery = minimax_b_voice_identity_lock_candidates`
- `video_generated = false`；`full_narration_regenerated = false`；`copy_changed = false`；`current_video_modified = false`。
- `diagnostics_path = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423`
- `review_table = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/voice_candidate_review_table.md`
- `lock_report = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/minimax_b_voice_identity_lock_report.json`
- `minimax_voice_capability`：`supports_voice_id = true`，`supports_voice_list = true`，`supports_voice_clone = true`，`supports_reference_audio = true`，`supports_style_prompt = false`，`supports_speed_pitch_emotion = true`。
- `actual_route = aliyun_bailian_proxy_to_minimax`；`actual_model = MiniMax/speech-2.8-hd`；`system_voice_count = 303`；`voice_cloning_count = 1`；`fallback_tts_used = false`；`api_key_printed = false`；`api_key_written = false`。
- `voice_candidates_generated = 6`：`female-shaonv / female-shaonv-jingpin / female-yujie` 各生成 `v1_stable` 与 `v2_more_emotional` 两个韵律版本；全部非静音，时长约 `13.248s / 14.22s / 13.824s / 14.868s / 16.92s / 19.152s`。
- `b_reference_audio.loaded = true`：已读取 `B_15秒文案_停顿梗感.wav` 与 `语音样本2_声音复刻试听_15秒.wav`；本轮未上传本地参考音频，原因是当前百炼 MiniMax voice clone 需要公网 `audio_url`，本轮 API scope 仅限短试听样本。
- `b_voice_identity_lock.status = pending_user_review`；`expected_b_minimax_voice_id = null`；`candidate_expected_b_minimax_voice_id_options = [female-shaonv, female-shaonv-jingpin, female-yujie]`；`human_voice_review_required = true`；`human_voice_review_status = pending_user_review`。
- `新增机制`：后续 B 方案正片候选不得只靠 `b_voice_feel_reflected = true` 通过；必须满足 `actual_voice_id == expected_b_minimax_voice_id`、`timbre_change_allowed = false`、`human_voice_review_status = user_confirmed`。
- `禁止继续默认`：`female-tianmei` 不得作为 B 方案默认声音，除非用户明确试听并确认。
- `状态边界`：未推进 `send_ready / content_validation / voice_validation / final_voice_validated / visual_master_locked`。
- `DeepSeek`：已创建前置供料请求与后置风险复核请求并运行 safe runner；两次均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`，因此本轮机制结论来自 Codex 本地复核 + 官方文档 + MiniMax 实测，不写 DeepSeek 已参与。
- `日志`：`codex_log/20260527_minimax_b_voice_identity_lock.md`

## 20260526｜新第四期选品初筛正片候选 rerun

- `task_result.status = completed`
- `target_delivery = publish_candidate_ready_for_human_review`
- `degradation_used = false`
- `review_pack_path = dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105`
- `output_video_path = dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4`
- `reused_v2_evidence_reports = true`：已读取并继承上一轮 `evidence_reclassification_report.json / line_visual_alignment_report_v2.json / near_equivalent_material_substitution_report_v2.json / candidate_rerun_readiness_report.md`。
- `can_continue_to_publish_candidate_generation = true`；`remaining_material_needed = []`；未重复阻断已解除的 `Codex / Atlas 操作电脑`、截图式商品卡处理、SKU 风险、候选表 / 明细表 / 复查表素材 blocker。
- `locked_copy_changed = false`；`old_v02_reused = false`；`copy_change_request_used = false`。
- `line_group_count = 245`；`exact_match_count = 245`；`near_equivalent_count = 0`；`near_equivalent_ratio = 0.0`；`core_evidence_mismatch_count = 0`；`whole_video_drift_detected = false`。
- `tts.actual_tts_provider = minimax`；`tts.actual_tts_model = MiniMax/speech-2.8-hd`；`selected_route = aliyun_bailian_proxy_to_minimax`；`fallback_tts_used = false`；`macos_say_used = false`；`local_low_quality_tts_used = false`。
- `narration.wav = generated`；`audio_present = true`；`non_silent = true`。
- `full.mp4 = generated`：`1920x1080`、约 `636.254s`、H.264 video、AAC audio、内嵌 `mov_text` 字幕轨。
- `V003 / V004` 表格画面已采用裁切 / 放大承接；核心字段可读；字幕 / 卡片未遮挡核心证据；敏感信息按执行包做遮挡与避让。
- `publish_candidate_preflight_suite.status = passed`；通过：`line_level_alignment_preflight / line_visual_tolerance_preflight / near_equivalent_material_substitution_preflight / tts_route_and_prosody_preflight / publish_candidate_voice_gate / b_voice_feel_minimax_preflight / card_decision_preflight / forbidden_action_preflight / visual_evidence_readability_preflight / locked_copy_diff_preflight / publish_candidate_user_standard_preflight / completion_truth_preflight`。
- `media_validation = passed`：`ffprobe / ffmpeg_decode / audio_present / non_silent / subtitles_present / edgeguard / visual_evidence_readability / secret_scan` 全部通过。
- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`visual_master_locked = false`。
- 大媒体 `full.mp4 / narration.wav` 保留本地 review pack，不纳入 Git 提交；提交范围仅限生成脚本、日志与可追踪小体积报告。
- `日志`：`codex_log/20260526_新第四期选品初筛正片候选_rerun.md`

## 20260526｜新第四期选品初筛素材证据复核

- `task_result.status = completed`
- `video_generated = false`；`tts_called = false`；`copy_changed = false`
- 本轮只做素材证据重新归类，不生成正片、不补素材、不继续 TTS、不降级文案。
- `review_pack_path = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604`
- `evidence_reclassification_report = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/evidence_reclassification_report.json`
- `codex_atlas_operation.status = direct_evidence_present`：V001 `00:00-00:12` 与 `01:27-01:33` 可见 ChatGPT Atlas、`已使用 Computer Use`、`已运行命令`、页面已进入选品广场、关键词/搜索框处理和可见样本获取。
- `product_card_processing.status = screenshot_based_product_card_processing_present`：V001 有商品卡页面，V003/V004 有商品字段进入候选表、明细表和复查表；`live_browser_page_turning_missing` 不是 blocker。
- `sku_evidence.status = table_evidence_passed`：V004 `00:27-00:39` 可见 `SKU 数量`、`买错/不适配差评`、`配列 / 轴体 / 兼容`。
- `candidate/detail/review_table_readability = high_res_source_present_edit_zoom_required_not_missing_material`：后续剪辑需裁切、放大、遮挡隐私和做字幕/卡片避让，但不再要求用户补素材。
- `previous_blockers.resolved = 28`；`previous_blockers.still_blocked = 0`
- `can_continue_to_publish_candidate_generation = true`
- `next_step = rerun publish candidate generation with existing locked script`
- `status_boundary`：未推进 `send_ready / content_validation / voice_validation / final_voice_validated / visual_master_locked`。
- `日志`：`codex_log/20260526_新第四期选品初筛素材证据复核_evidence_reclassification.md`

## 20260526｜新第四期选品初筛锁稿正片候选阻断

- `task_result.status = blocked`
- `blocked_type = blocked_publish_candidate_unavailable`
- `target_delivery = publish_candidate_ready_for_human_review`
- `degradation_used = false`
- `no_degraded_output_created = true`
- `review_pack_path = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604`
- `locked_copy_created = true`；`locked_copy_changed = false`；`old_v02_reused = false`；本轮未复用旧 v0.2 文案。
- `line_group_count = 245`；`near_equivalent_count = 10`；`near_equivalent_ratio = 0.0408`；`consecutive_near_equivalent_max = 5`；`core_evidence_mismatch_count = 10`；`whole_video_drift_detected = false`。
- `visual_blocker`：现有素材不能无猜测证明“Codex 操作我的电脑 / 进入选品页面 / 输入品类词 / 一张一张翻商品卡”；候选表、明细表、复查表存在小字/隐私/遮挡可读性风险；SKU 复杂度缺少清楚证据。
- `copy_blocker`：旧 preflight 已要求相关句子走 `copy_change_request`，但本轮锁稿禁止 Codex 改稿，因此 blocked。
- `tts`：MiniMax 百炼代理 route_b / `MiniMax/speech-2.8-hd` smoke 能生成音频，但 smoke 报告 `task_status = blocked`；本轮未生成全片 `narration.wav`，未使用 fallback / macOS say / 本地低质 TTS。
- `publish_candidate_preflight_suite.status = blocked`；通过：`card_decision_preflight / forbidden_action_preflight / locked_copy_diff_preflight`；失败：`line_level_alignment_preflight / line_visual_tolerance_preflight / near_equivalent_material_substitution_preflight / tts_route_and_prosody_preflight / publish_candidate_voice_gate / b_voice_feel_minimax_preflight / visual_evidence_readability_preflight / publish_candidate_user_standard_preflight / completion_truth_preflight`。
- `media_generated = false`；`full.mp4 = not_generated`；`narration.wav = not_generated`；`captions.srt = not_generated`。
- `content_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`final_voice_validated = false`；`visual_master_locked = false`；`current_data_goal_anchor_ready = false`。
- `日志`：`codex_log/20260526_新第四期选品初筛正片候选_blocked_publish_candidate.md`

## 20260526｜三项候选片判断机制落库

- `已确认` 本轮只做机制落库，不生成视频、不生成音频、不调用 MiniMax / 阿里 / 百炼 / TTS API、不修改 `dist/` 媒体产物、不修改素材目录、不修改用户文案。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + fixture_or_test_change`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260526_three_candidate_judgment_rules_pre_supply_request.json`；safe runner 返回 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`；`multi_agent_runtime_validation = not_started`。
- `DeepSeek 后置风险复核`：任务卡 `codex_log/supply_requests/20260526_three_candidate_judgment_rules_post_risk_review_request.json`；safe runner 返回 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`not_deepseek_conclusion = false`、`api_key_printed = false`、`api_key_written = false`；复核包读取结果为 `forbidden_status_promotion = 未发现`、`secret_risk = 未检测到`、`fallback_mislabel_risk = none_observed`。
- `机制 gap report`：`codex_log/mechanism_gap_report.md`。缺失项为 `line_visual_tolerance_rule / near_equivalent_material_substitution_report / publish_candidate_user_standard_rule`；`b_voice_feel_minimax_formal_voice_rule` 为部分成立，已补强。
- `已新增 / 补强` `line_visual_tolerance_rule（文案画面一致性容差规则）`：近似素材替代最多约 `5%`，连续近似替代最多 1 个句组；只允许非核心、局部、偶发、极其相近替代；核心证据错位为 0；全程漂移、需要猜测、素材不极近或用户素材缺失时必须 blocked。
- `已新增` `near_equivalent_material_substitution_report（近似素材替代报告）`：后续候选片必须输出 `total_line_group_count / exact_match_count / near_equivalent_count / near_equivalent_ratio / consecutive_near_equivalent_max / core_evidence_mismatch_count / whole_video_drift_detected / substitutions / final_decision`。
- `已补强` `b_voice_feel_minimax_formal_voice_rule（B 方案听感 + MiniMax 正式语音规则）`：B 方案升级为正式声音听感标准；正式生成路线必须是 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`；旧 Qwen / 阿里 B 语音路线、`Serena`、`macOS say`、本地低质 TTS、silent audio 或未授权 fallback 不能作为正片候选完成。
- `已新增` `publish_candidate_user_standard_rule（候选可发布用户标准）`：候选片必须达到用户打开后原则上可以直接发、再进入人工复审的标准；微小瑕疵可接受，整体漂移、文案被改、声音错、画面错、字幕卡片遮挡、技术预览或内部诊断冒充候选片不可接受。
- `已接入` `publish_candidate_preflight_suite`：新增 `line_visual_tolerance_preflight / near_equivalent_material_substitution_preflight / b_voice_feel_minimax_preflight / publish_candidate_user_standard_preflight`，并要求 review pack 增加对应报告。
- `已补 fixture / tests`：`codex_source/fixtures/publish_candidate_preflight_suite_cases.json` 覆盖用户指定 7 个 case；`tests/test_publish_candidate_voice_gate.py` 与 `tests/test_publish_candidate_preflight_tolerance.py` 覆盖 TTS 路线、B 听感、近似素材容差、核心证据阻断、全程漂移阻断、小瑕疵但仍需人审。
- `no-render dry run`：`codex_log/diagnostics/three_candidate_judgment_rules_preflight_20260526_no_render/` 已生成十二闸门报告；无输入 dry run 按预期 `overall_status = blocked`，fixture validation `passed`，case_count = 19。
- `未推进`：`content_validation = not_advanced`；`send_ready = false`；`voice_validation = not_advanced`；`final_voice_validated = false`；`visual_master_locked = false`。
- `日志`：`codex_log/20260526_三项候选片判断机制_three_candidate_judgment_rules.md`

## 20260526｜mandatory_commit_push_gate 强制提交推送闸门

- `已确认` 本轮只做 GPT / Codex 配合手册与执行规则修补，不生成媒体、不修改 `dist/` 媒体产物、不推进任何视频 / 声音 / 内容 / 发布状态。
- `已新增` `mandatory_commit_push_gate（强制提交推送闸门）`：以后任何最小任务只要创建或修改仓库文件，`completed` 必须等到本轮相关文件显式 stage、commit 创建、push 成功、远端 HEAD 校验通过、unrelated dirty files 未被提交、secret scan 通过后才允许写。
- `已补强` `completed` 定义：`relevant_files_committed = true`、`pushed_to_current_reading_branch = true`、`remote_head_verified = true`、`unrelated_dirty_files_not_committed = true`、`secret_scan_passed = true`。
- `已写入` non-push 状态边界：本地完成但未 push / 未远端校验时，只能写 `partial_completed: local_changes_done_but_not_pushed` 或 `blocked`，不得写 `completed`。
- `已更新` ChatGPT -> Codex prompt 默认完成标准：所有仓库写入类任务默认追加 `Git completion requirement`，包括 explicit staging、commit、push、remote HEAD verification 和 unrelated dirty exclusion。
- `已更新` Codex 最终回报格式：必须默认包含 `git_sync_status.current_branch / files_changed / files_staged / commit_sha / pushed / remote_head_verified / unrelated_dirty_files / secret_scan / completed_allowed`。
- `已更新` `sync_back_check`：必须检查 latest、dated log、commit、push、远端可查、是否有未提交本轮相关文件、unrelated dirty files 是否未混入、secret scan 是否通过。
- `DeepSeek`：已创建前置供料任务卡 `codex_log/supply_requests/20260526_mandatory_commit_push_gate_pre_supply_request.json` 与后置风险复核任务卡 `codex_log/supply_requests/20260526_mandatory_commit_push_gate_post_risk_review_request.json`；safe runner 均返回 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `状态边界`：`media_generated = false`；`dist_media_modified = false`；`content_validation = not_advanced`；`voice_validation = not_advanced`；`send_ready = false`；`final_voice_validated = false`；`visual_master_locked = false`。
- `日志`：`codex_log/20260526_mandatory_commit_push_gate.md`

## 20260525｜MiniMax speech-2.8-hd 默认正片候选 TTS 路线切换

- `已确认` 用户已将后续正片候选默认 TTS 路线切换为 MiniMax `speech-2.8-hd`；百炼代理模型名为 `MiniMax/speech-2.8-hd`。
- `已确认` B 方案只保留为 `voice_feel_reference（声音听感参考）`：轻陪伴、低压、停顿梗感、游戏向导感；阿里 / 百炼 `qwen-t...ac19` 与 `qwen3-tts-vc-realtime-2026-01-15` 不再是正片候选默认 TTS 生成路线。
- `已新增` provider / gate helper：`scripts/正片候选TTS路线_publish_candidate_tts_route.py`，统一判定 `passed_minimax / failed_non_minimax_voice / blocked_minimax_unavailable / internal_diagnostic_only`。
- `已升级` `publish_candidate_preflight_suite`：从七闸门升级为八闸门，新增 `publish_candidate_voice_gate`，并要求 review pack 包含 `tts_route_report.json/md`。
- `已更新` 当前第四期主生成脚本默认 TTS 路线为 MiniMax 百炼代理；旧 B 语音修复脚本、第二期横屏候选脚本、AI 赚钱正片候选装配脚本已加硬阻断，不能再用非 MiniMax TTS 生成正片候选完成态；旧脚本里不可达的 `publish_candidate_ready_for_human_review` 字面残留也已降为 blocked / reference-only 口径。
- `DeepSeek`：前置供料任务卡 `codex_log/supply_requests/20260525_minimax_default_tts_route_switch_pre_supply_request.json` 曾返回 `blocked_invalid_context_pack`；执行后风险复核任务卡 `codex_log/supply_requests/20260525_minimax_default_tts_route_switch_post_risk_review_request.json` 已通过 safe runner，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。
- `验证`：`py_compile` passed；fixture JSON parse passed；`tests/test_publish_candidate_voice_gate.py` 5/5 passed；no-render preflight 输出 `overall_status = blocked`，`publish_candidate_voice_gate` 因缺 `tts_route_report / MiniMax audio` 正常 blocked，fixture validation passed；旧 route grep 仅剩历史记录、负例 fixture、检测字段或已阻断 legacy script 残留。
- `未生成`：本轮未生成视频、未生成全片音频、未调用 TTS 生成正片、未修改 `dist/` 现有媒体产物。
- `状态边界`：`content_validation = not_advanced`；`send_ready = false`；`voice_validation = not_advanced`；`final_voice_validated = false`；`visual_master_locked = false`。
- `日志`：`codex_log/20260525_minimax_default_tts_route_switch.md`

## 20260525｜DeepSeek 供料链只读诊断

- `已确认` 本轮只做 DeepSeek 供料链诊断：不修代码、不改 DeepSeek runtime provider / safe runner / controller / schema、不改文案机制文件、不写文案、不生成视频、不推进内容状态。
- `上一轮复核`：commit `d8017bcc3c168b1d5a8658609fc1d2ed6d213704` 已在 `main / origin/main`；上一轮记录为 `supply_request_created = false`、`deepseek_call_attempted = false`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。
- `runtime provider`：`scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py status` 返回 `status = ready`；provider 只输出脱敏 public status，`api_key_printed = false`、`api_key_written = false`。
- `safe runner / smoke test`：`scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py` 可用；最小 workspace-local 临时 request 通过 safe runner/provider 返回 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`。
- `根因分类`：上一轮不是 runtime provider 不可用，也不是 safe runner 缺失；主因是 Codex 执行层绕过 mandatory DeepSeek supply gate，并把允许写入范围过窄当成未创建 supply_request 的理由。结果质量影响低，但 `affects_multi_agent_validation = true`。
- `修复建议`：下一轮应做 process gate compliance repair，明确没有 DeepSeek MCP tool 时仍必须使用仓库内 provider/safe runner；用户明确要求 DeepSeek 参与、视频执行、剪辑装配、数据复盘、reference audit、素材审计、runtime 诊断任务必须 `deepseek_passed` 或 blocked。
- `状态边界`：`content_validation = not_advanced`；`send_ready = false`；`voice_validation = not_advanced`；`visual_master_locked = false`；`current_data_goal_anchor_ready = not_advanced`；`multi_agent_runtime_validated = false`。
- `日志`：`codex_log/deepseek_diagnostics/20260525_deepseek_supply_line_diagnosis.md`

## 20260524｜对标文案话语机制反报告腔修正

- `已确认` 本轮是对上一轮 `reference_copy_voice_mechanism（对标文案话语机制）` 的修正；上一轮方向正确，但仍存在字段化、报告腔、标签化输出风险。
- `已新增` `前台口播转换规则`：后台检查字段只用于验收，不得出现在最终稿；最终文案必须把字段转成自然口播链条。
- `已新增` `anti_report_voice_gate（反报告腔话语闸门）`：最终稿不得出现“用户痛点句 / AI 救场句 / 能力定义句”等标签化段落，不得像在解释机制。
- `已新增` `反报告腔价值标准`：高价值文案必须像真人叙事 + 具体坑点 + 工具救场，不能像机制说明 + 字段罗列。
- 后续最终文案默认先讲普通人为什么卡住，再让 AI / Codex 作为救场工具自然出现；坑点细节要嵌在句子里，不做字段清单。
- 本轮不写新第四期最终文案、不生成视频、不修改素材、不提交第三方逐字稿全文、不推进任何内容状态。
- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `video_generated = false`
- `media_committed = false`
- `full_transcript_committed = false`
- `日志`：`codex_log/20260524_reference_copy_voice_anti_report_fix.md`

## 20260525｜publish_candidate_preflight_suite 发片候选预检套件机制落库

- `已确认` 本轮只做视频执行 / 修片 / 发片候选机制补强，不生成视频、不重渲染、不生成 TTS / 音频 / 字幕、不修改 `dist/` 媒体产物、不推进任何内容状态。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + validation_dry_run`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260525_publish_candidate_preflight_suite_pre_supply_request.json`；安全供料控制器返回 `invalid_context_pack`，本轮结论按 `fallback_local_only / not_deepseek_conclusion = true` 处理，不写成 DeepSeek 深度参与或 DeepSeek 结论。
- `已新增` `publish_candidate_preflight_suite（发片候选预检套件）` 最小可运行脚本：`scripts/发片候选预检套件_publish_candidate_preflight_suite.py`，支持 `--no-render`、结构级 / 字段级 gate 检查、缺文件 blocked 报告、7 个子报告输出和 `review_pack_required_preflight_reports`。
- `已新增` fixture：`codex_source/fixtures/publish_candidate_preflight_suite_cases.json`，覆盖 7 个 blocked case：逐句映射缺失、TTS route 不一致、判断卡决策缺失、禁止遮挡、视觉证据不可读、locked copy 语义差异、`full.mp4` 存在但预检缺失不得 completed。
- `已接入` 7 个闸门：`line_level_alignment_preflight`、`tts_route_and_prosody_preflight`、`card_decision_preflight`、`forbidden_action_preflight`、`visual_evidence_readability_preflight`、`locked_copy_diff_preflight`、`completion_truth_preflight`。
- `已更新` 机制入口 / 执行规则 / 状态动作路由 / 判断权限 / GPT Project 侧规则 / 文案路由 / 视频价值规则 / 项目状态动作总控器，后续命中视频执行、修片、发片候选、TTS、字幕、卡片、时间线、审片包任务时，必须在导出前跑预检套件。
- `review_pack` 新要求：后续审片包必须包含 `publish_candidate_preflight_report.json/md` 与 7 个 gate 子报告；缺任一 required gate 或 report，不得导出、不得 `completed`。
- `验证`：已运行脚本语法检查、`--help`、fixture JSON 解析、关键词 grep、fixture `--no-render` dry-run；dry-run 输出目录为 `codex_log/diagnostics/publish_candidate_preflight_suite_20260525_no_render/`，整体按预期为 `overall_status = blocked`，fixture validation 为 `passed`。
- `状态边界`：`video_generated = false`；`audio_generated = false`；`media_modified = false`；`content_validation = not_advanced`；`send_ready = false`；`voice_validation = not_advanced`；`visual_master_locked = false`；`current_data_goal_anchor_ready = not_advanced`。
- `待验证` 本轮机制写入只代表 preflight suite 可运行、可阻断、可产报告并已接入规则；下一轮真实发片 / 修片任务必须用真实 review pack 和真实素材链验证是否能在导出前阻断错误。
- `日志`：`codex_log/20260525_发片候选预检套件_publish_candidate_preflight_suite.md`

## 20260525｜流程启动闸门 + 发片清单 + 修片会话卡机制补强

- `已确认` 本轮只做视频执行 / 修片 / 发片候选机制补强，不生成视频、不重生成候选片、不修改 `dist/` 媒体产物、不改新第四期 locked 文案语义。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + validation_layer_sync`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260525_流程启动闸门修片会话机制_process_boot_gate_repair_session_pre_supply_request.json`，安全供料返回 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`；供料包只作为只读参考，项目事实仍以仓库原文件为准。
- `已写入` `process_boot_gate（流程启动闸门）`：后续命中视频执行、修片、发片候选、重新生成、发布前修复、最终文案进视频或 TTS / 字幕 / 卡片 / 时间线 / 审片包 / 视觉证据任务时，必须先读完整流程入口并输出 `process_boot_report（流程启动报告）`。
- `已写入` prompt 边界：GPT prompt 只代表本轮 `prompt_delta（增量目标）`，不是完整流程唯一依据；prompt 未写的默认流程义务不得静默省略。
- `已写入` `publish_candidate_required_inventory（发片候选必交付清单）`：`locked_copy_contract / content_route_card_v2 / card_placement_decision / script_to_timeline_map / tts_prosody_anchor_map / visual_evidence_check / subtitle_card_overlap_check / publish_candidate_checklist / data_goal_alignment_check / review_pack / remaining_blockers` 默认进入判断；不适用必须写 `not_applicable_reason`，缺必需项不得 `completed`。
- `已写入` `current_repair_session（当前修片会话卡）`：修片 / 既有候选片重生成必须先从 latest、review pack、summary、manifest 恢复或创建状态卡，锁本轮唯一主修问题，执行后更新 `remaining_blockers`，不得从 prompt 猜状态。
- `已接入` `state_action_router（项目状态动作总控器）`：新增 `process_boot_required / publish_candidate_inventory_required / repair_session_required` 三类状态、trigger、selected_action、blocked_if。
- `已补 fixture`：`codex_source/fixtures/mechanism_inference_function_cases.json` 新增 prompt 缺判断卡仍需组件判断、修片无 session 先恢复 / 创建、full.mp4 已生成但清单缺项不得 completed 三个最小 case。
- `状态边界`：`video_generated = false`；`content_validation = not_advanced`；`send_ready = false`；`voice_validation = not_advanced`；`visual_master_locked = false`；`current_data_goal_anchor_ready = not_advanced`。
- `待验证` 本轮机制写入只代表入口规则和 fixture 已落库，不代表长期稳定；下一轮真实视频 / 修片任务必须用 `process_boot_report` 和 `publish_candidate_required_inventory` 验证机制是否真实触发。
- `日志`：`codex_log/20260525_流程启动闸门修片会话机制_process_boot_gate_repair_session_mechanism.md`

## 20260524｜对标文案话语机制落库

- `已确认` 本轮只做文案机制补写，不写新第四期最终文案、不生成视频、不提交第三方逐字稿全文、不推进任何内容状态。
- `已新增` `reference_copy_voice_mechanism（对标文案话语机制）`：后续最终文案默认从普通人复杂问题起手，先讲旧方法痛点，再让 AI / Codex 作为救场工具出现。
- `已更新` `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`。
- 后续 ChatGPT 写稿默认继承对标稿的话语机制：普通人复杂问题起手、旧方法痛点、AI / Codex 救场、案例推进、坑点细节、能力定义、低压收尾。
- `已确认` 结构不写死：每条内容仍按真实素材、reference pack、证据强弱、平台风险、观众理解路径和本轮数据目标动态调整。
- `已确认` 本机制补在 `copy_granularity_mixture_rule（文案颗粒度配比规则）` 之上，用来回答“以后怎么说人话”；不是替换已有素材颗粒度规则。
- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `video_generated = false`
- `media_committed = false`
- `full_transcript_committed = false`
- `日志`：`codex_log/20260524_reference_copy_mechanism.md`

## 20260525｜新第四期无遮挡源比例 + B 语音修复候选片

- 已确认：本轮按用户指令先落库“源素材比例 + 无默认遮挡”视觉机制，再重生成新第四期修复候选片；未改 locked v0.2 文案语义。
- 已写入机制：`source_native_no_mask_visual_rule`、`visual_evidence_must_remain_visible_rule`、`no_default_masking_without_user_authorization = true`、`no_default_16_9_for_user_recording = true`、`source_material_ratio_preferred = true`、`blocked_if_visual_evidence_unreadable = true`。
- 已生成：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/full.mp4`。
- 已生成：`narration.wav`，走阿里 / 百炼 B 语音路线：`provider = aliyun_bailian`，`target_model = qwen3-tts-vc-realtime-2026-01-15`，`custom_voice_masked = qwen-t...ac19`，`used_b_voice = true`，`used_b_pacing = true`。
- 已生成：`captions.srt`，并作为 sidecar / embedded subtitle 使用；未烧录大黑条字幕，未用字幕遮挡中段核心素材。
- 视觉修复：`canvas = 3412x1846`，`canvas_strategy = source_native_or_primary_material_ratio`；未强制 16:9，未强制 1920x1080，未使用 gray padding / white padding / black padding / letterbox / pillarbox。
- 视觉修复：默认遮挡已禁用；未使用 final-stage whiteout、full-frame privacy mask、right account black block、edge privacy mask、gray dim overlay 或 large redaction rect。
- 验证：`ffprobe = passed`；`ffmpeg_decode = passed`；`audio_present = true`；`non_silent = true`；`subtitles_present = true`；`subtitle_card_overlap = passed`；`secret_scan = passed`。
- `publish_candidate_ready_for_human_review = true`
- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `media_committed = false`

## 20260525｜新第四期成片视觉 / TTS 路线只读诊断

- 已确认：本轮只做只读诊断；未修复、未重渲染、未重新生成 TTS，未修改 `full.mp4` / `narration.wav` / `captions.srt`。
- 已确认：诊断对象为 `dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4`。
- 已生成：诊断目录 `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732`。
- 视觉结论：大面积白屏 / 洗白主要来自最终装配阶段的 strengthened privacy redaction / whiteout layer；源素材和中间 `visual_with_captions.mp4` 没有同等程度主体洗白。
- 视觉结论：右上角黑块来自 right account/sidebar privacy mask；左侧 / 顶部灰边来自 edge privacy masks + canvas / padding safe bands 叠加。
- TTS 结论：实际为 `aliyun_bailian + qwen3-tts-instruct-flash-realtime + Serena`，没有走 B 语音路线。
- TTS 结论：预期 B 路线应检查 `qwen3-tts-vc-realtime-2026-01-15 + qwen-t...ac19 + tts_15s_b_pacing_locked_20260427`；本次 `used_b_voice = false`，`used_b_pacing = false`。
- 状态边界：`video_regenerated = false`，`tts_regenerated = false`，`content_validation = pending_user_chatgpt_review`，`send_ready = false`，`voice_validation = failed_user_feedback`，`visual_master_locked = false`。
- 下一步建议：先修视觉遮挡 / 白屏 / 灰边根因，再修 TTS B 语音 route；不得直接继续发布。

## 20260524｜新第四期选品初筛发布候选片生成（TTS 授权解阻）

- `已确认` 本轮继续上一轮 blocked 的新第四期 publish candidate 任务，不改 locked v0.2 文案语义，不采纳 copy_change_request 做改稿。
- `已确认` 安全加载现有阿里 / 百炼 TTS 授权：`auth_source = authorized_runtime_config`；只记录 presence / source，不打印、不写入、不提交 key。
- `已生成` 完整成片：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4`。
- `已生成` 正式 TTS 音轨：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/narration.wav`；`provider = aliyun_bailian`；`model = qwen3-tts-instruct-flash-realtime`；`local_tts_fallback_used = false`；`macos_say_used = false`。
- `已生成` 字幕：`captions.srt`，并已烧录 group-level 字幕层到 `full.mp4`。
- `已生成` review pack：`summary.json`、`media_probe.json`、`review_manifest.md`、`publish_candidate_checklist.json`、`script_to_timeline_map.json`、`tts_prosody_anchor_map.json`、`privacy_risk_check.json`、`readability_check.json`、`subtitle_card_overlap_check.json`、`platform_risk_precheck.json`、`secret_leak_scan_sanitized.json`。
- `隐私处理`：已对账号 / 路径 / 商品名 / 商品价格 / 佣金 / 月销 / 表格值执行遮挡或洗白，字段含义由卡片与字幕承载；仍需用户 / ChatGPT 人工抽查观感。
- `验证`：`ffprobe = passed`；`ffmpeg_decode = passed`；`audio_present = true`；`non_silent = true`；`subtitles_present = true`；`secret_scan = passed`。
- `publish_candidate_ready_for_human_review = true`
- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `media_committed = false`

## 20260524｜新第四期 locked v0.2 发布候选生成阻断

- `已确认` 本轮目标是按 locked v0.2 文案生成完整 `publish_candidate_ready_for_human_review`，不是技术预览、不是文案包、不是无声预览。
- `已确认` preflight 输出目录存在：`codex_log/script_preflight/新第四期_选品初筛_20260524_231118/`；`script_to_timeline_map` / `content_route_card_v2` / `tts_prosody_anchor_map` 均可解析。
- `素材检查`：`/Users/fan/Documents/视频工厂/素材录制/新第四期` 存在；V001 / V003 / V004 均可解码；素材本身无音轨，必须另行生成正式 TTS。
- `blocked_publish_candidate_unavailable_remote_tts_authorization_missing`：当前进程 `DASHSCOPE_API_KEY_present = false`、`ALIYUN_API_KEY_present = false`；本轮禁止读取 API key / token / secret，因此未读取本地 runtime 授权文件。
- `未生成` `full.mp4`、`narration.wav`、`captions.srt`；未生成无声视频，未使用 macOS say，未使用本地低质 TTS fallback。
- `已生成` 阻断审计包：`dist/new_fourth_episode_selection_publish_candidate_20260524_233231/`。
- `content_validation = not_advanced_due_blocked`
- `send_ready = false`
- `publish_candidate_ready_for_human_review = false`
- `voice_validation = not_advanced_due_blocked`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `media_committed = false`


## 20260524｜新第四期文案 line_group 与素材时间码对齐

- 已确认：本轮只做新第四期成片前置包，不生成视频、不生成音频、不替换素材、不推进内容状态。
- 已生成：`codex_log/script_preflight/新第四期_选品初筛_20260524_231118/`
- 已生成：`01_line_group_map.md`，共 21 个 line_group，已对齐 V001 / V003 / V004 时间码或边界卡承载方式。
- 已生成：`02_script_to_timeline_map.json` 与 `03_script_to_timeline_map.md`。
- 已生成：`04_content_route_card_v2.json` 与 `05_content_route_card_v2.md`，其中 `current_data_goal_anchor_status = partial_or_not_ready`，`formal_video_execution_ready = false`。
- 已生成：`06_tts_prosody_anchor_map.json`，只做韵律锚点，不生成 TTS。
- 已生成：`07_card_placement_decision.md`、`08_editing_decision_pack.md`、`09_privacy_and_readability_check.md`。
- 已生成：`10_copy_change_request_if_any.md`，正式成片前需先处理“直接操作电脑”“SKU 复杂”“最值得复查”“云盘遮挡”等风险表达。
- 已生成：`11_next_video_execution_prompt_draft.md`，标记 `not_executed_this_round = true`。
- content_validation = not_advanced
- send_ready = false
- video_generated = false
- audio_generated = false
- media_committed = false


## 20260524｜文案对标逐字稿与话语口味补充解析

- `已确认` 本轮只做对标视频逐字稿 / 话语口味补充解析，不写新第四期最终文案、不生成视频、不替换素材、不推进内容状态。
- `已确认` reference 视频：`/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`；上一轮 reference audit 目录：`codex_log/reference_audit/文案对标_20260524_215056/`。
- `音频提取`：已生成 local-only 音频 `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/reference_audio.wav`，不提交 Git。
- `逐字稿状态`：`transcript_status = blocked_local_asr_missing`；本机未检测到可用本地 ASR / OCR，且本轮禁止外部 API，因此未生成完整逐字稿。
- `full_transcript_local_only = not_generated`；`transcript_blocked_report` 位于 `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/transcript_blocked_report.md`。
- `FULL_TRANSCRIPT_COMMIT_ALLOWED = false`；未提交完整第三方逐字稿全文，只提交安全分析报告、短引用机制分析和改稿规则。
- `已生成` 仓库安全报告：`13_transcript_extraction_report.md`、`14_line_level_copy_taste_analysis.md`、`15_reference_vs_new_fourth_copy_gap.md`、`16_transcript_driven_chatgpt_handoff_pack.md`。
- `已生成` dated log：`codex_log/20260524_reference_transcript_copy_taste_audit.md`。
- `content_validation = not_advanced`
- `send_ready = false`
- `video_generated = false`
- `media_committed = false`
- `full_transcript_committed = false`

## 20260524｜项目内文案对标视频全方位解析

- `已确认` 本轮只做项目内对标视频解析和 reference pack，不写新第四期最终文案、不生成视频、不替换素材、不推进任何内容状态。
- `已确认` 对标路径：`/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`；原目录 `/Users/fan/Documents/视频工厂/文案库/文案对标` 不存在，本轮按 fallback 命中 `文案库/文案对标.MP4`。
- `已生成` 输出目录：`codex_log/reference_audit/文案对标_20260524_215056/`。
- `已生成` 12 个报告文件 + inventory JSON + manifest：`00_reference_inventory` 至 `12_chatgpt_handoff_pack`。
- `已生成` Reference-to-Execution Contract：`codex_log/reference_audit/文案对标_20260524_215056/09_reference_to_execution_contract.md`。
- `已生成` ChatGPT handoff pack：`codex_log/reference_audit/文案对标_20260524_215056/12_chatgpt_handoff_pack.md`。
- `已确认` 原始对标视频、音频、完整抽帧目录、contact sheet 大图均未提交；只提交 `.md / .json` 报告。
- `已确认` 未复用第三方人物、画面、平台 UI、BGM、音效、字体、logo 或原始素材资产；本轮只提取结构、节奏、卡片功能、动效功能和文案颗粒度机制。
- `content_validation = not_advanced`
- `send_ready = false`
- `video_generated = false`
- `media_committed = false`
- 本轮只支持 ChatGPT 后续参考，不代表当前视频已经过线。
- `日志`：`codex_log/20260524_reference_copy_visual_audio_audit.md`

## 20260524｜文案颗粒度配比机制补写

- `已确认` 本轮只做文案机制补写，不写最终文案、不生成视频、不生成音频、不推进任何内容状态。
- `已新增` `copy_granularity_mixture_rule（文案颗粒度配比规则）`：文案表层要顺口，但关键价值点必须落到素材颗粒度；精彩和重要的位置讲细节，普通过渡位置顺口推进。
- `已更新` `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`。
- 后续文案必须区分：`smooth_line（顺口推进句）`、`material_granularity_line（素材颗粒度句）`、`judgment_boundary_line（判断 / 边界句）`、`result_transition_line（结果变化句）`。
- 关键句必须绑定素材动作、真实页面、真实字段、真实表格 / 云盘表格、结果变化或回到聊天框结论；缺素材支撑时必须降级、退回改稿或 blocked。
- 普通过渡、轻吐槽、观众心理和收尾可以顺口，但不得承载事实证明；整篇机械堆步骤也必须退回改稿。
- `DeepSeek`：已创建供料任务卡并完成安全供料，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`；DeepSeek 只读供料，不拍板项目事实。
- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation / visual_master_locked / current_data_goal_anchor ready / publish_candidate_ready_for_human_review` 均未推进。
- `日志`：`codex_log/20260524_copy_granularity_mixture_mechanism.md`

## 20260523｜EdgeGuard 黑边 / 灰边 / 边缘残留机制修复

- `已确认` 本轮只修 `Layer 0 = EdgeGuard（边缘防护层）`；没有修复或重做第四期完整成片，没有覆盖任何 `full.mp4`，没有覆盖 `dist/latest_review_pack/`，没有新增 Remotion 效果层 / 高亮框 / 悬浮判断卡 / 3D 科技感 / 转场桥。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = edge_residue_bug_fix + visual_generation_pipeline_guard + validation_layer_sync`；`execution_mode = mechanism_fix_only`；`target_layer = Layer 0 EdgeGuard`；`DeepSeek = fallback_local_only`，`not_deepseek_conclusion = true`。
- `state_action_router（状态动作总控器）`：`selected_action = locate_edge_residue_sources + implement_or_fix_edgeguard + add_edge_scan_validation + update_logs_without_status_promotion`；禁止 `modify_fourth_episode_video / add_remotion_effects / add_highlight_box / add_floating_panel / promote_content_status`。
- `根因定位`：旧第四期输出只读扫描发现 left/right black edge，最大 `36px`；material_02 源录屏只读抽样 `source_has_edge_residue = false`；最可能根因为旧生成链路 `scale=1920:1080:force_original_aspect_ratio=decrease + pad=1920:1080` 默认黑底补边叠加源比例与 16:9 不完全一致。
- `已新增` EdgeGuard helper：`scripts/边缘防护_EdgeGuard_edge_residue_guard.py`，包含 `input_edge_preflight`、`safe_fit_policy`、`output_edge_scan`、synthetic diagnostic mode；阈值为 `max_unintended_edge_width_px = 3`、`suspicious = 4`、`fail = 8`。
- `已接入` 当前基础生成脚本：源录屏进入 1920x1080 时从默认黑底 `scale+pad` 改为 `cover_with_minimal_safe_crop`，记录 `edgeguard_safe_fit_policy`，并在导出后、候选声明前调用 `run_edgeguard_output_scan()`；`output_edge_scan.pass != true` 时阻断候选声明。
- `默认入口 no-render 验证`：`scripts/生成第四期数据成果卡发布候选片_generate_fourth_episode_data_result_card_publish_candidate.py --edgeguard-synthetic-only --output-dir dist/edgeguard_diagnostics/default_entrypoint_no_render_probe` passed，`full_mp4_generated = false`。
- `内部诊断产物`：`dist/edgeguard_diagnostics/input_edge_report.json`、`output_edge_report.json`、`edgeguard_probe_summary.json`、`before_after_edge_contact_sheet.png`、`fourth_episode_reference_read_only_output_scan/output_edge_report.json`、`fourth_episode_source_material_02_read_only_input_preflight/input_edge_report.json`。
- `测试`：`py_compile` passed；`tests/test_edgeguard.py` 4 cases passed；EdgeGuard synthetic probe passed；JSON parse passed；未触碰 `dist/latest_review_pack/`、第四期 `full.mp4` 或源录屏素材。
- `未推进`：`content_validation / send_ready / visual_master_locked / publish_status / voice_validation / current_data_goal_anchor_ready` 均未推进。
- `日志`：`codex_log/20260523_edgeguard_black_border_fix.md`

## 20260519｜素材证据闸门默认视频执行机制

- `已确认` 本轮只做机制修补，不修任何单条视频；未生成新视频、未重剪第四期、未修改任何 `full.mp4`、未重新生成 TTS、未改 HyperFrames 视觉形式 / 动效路线 / 皮肤。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + execution_gate_repair + validation_gate_repair + code_integration + validation_dry_run`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`。
- `DeepSeek`：本轮因用户禁止读取 API key / token / secret，供料闸门记录为 `fallback_local_only`，`not_deepseek_conclusion = true`；未打印、未写入、未读取 secret。
- `已新增` 可运行默认闸门：`scripts/素材证据闸门_material_evidence_gate.py`，支持 `--material-report`、`--timeline`、`--content-route-card`、`--output-dir`、`--dry-run`、`--require-pass`。
- `默认机制`：后续视频执行必须走 `material_detail_report -> material_evidence_contract -> line_group_evidence_gate -> auto_storyboard_preflight_report -> auto_edit_allowed check -> render only if passed`。
- `已接入` 当前默认第四期数据成果卡生成入口：`scripts/生成第四期数据成果卡发布候选片_generate_fourth_episode_data_result_card_publish_candidate.py` 已新增 `--preflight-only` / `--output-dir`，并在 TTS / `full.mp4` 生成前调用素材证据闸门。
- `第四期 dry-run`：`dist/fourth_episode_evidence_gate_default_mechanism_dry_run/` 已生成 `material_evidence_contract.json`、`line_group_evidence_gate_report.json`、`auto_storyboard_preflight_report.json`；当前数据成果卡候选片 timeline 为 `auto_edit_allowed = true`、`total_line_groups = 36`、`direct_match_count = 26`、`proxy_match_count = 6`、`card_required_resolved_count = 4`、全部阻断计数为 0。
- `legacy blocked 验证`：旧 `dist/fourth_episode_ai_review_system_publish_candidate/script_to_timeline_map.json` 另存 `dist/fourth_episode_evidence_gate_default_mechanism_dry_run_legacy_ai_review_blocked/`，结果为 `auto_edit_allowed = false`，命中 `data_sentence_without_source_count`，证明预检失败会阻断而不是继续产片。
- `测试`：`py_compile` passed；`tests/test_material_evidence_gate.py` 10 cases passed；default entrypoint `--preflight-only` passed 且 `full_mp4_generated = false`；dry-run JSON parse passed；`git diff --check` passed。
- `未推进`：`content_validation / send_ready / current_data_goal_anchor_ready / voice_validation / visual_master_locked` 均未推进；未覆盖 `dist/latest_review_pack/`。
- `日志`：`codex_log/20260519_material_evidence_gate_default_video_execution.md`

## 20260519｜第四期证据驱动自动剪辑修复候选片

- `已确认` 本轮按执行单直接修复第四期“文案和画面对不上号”问题：先从素材解析报告自动生成证据契约和句组证据闸门，通过后直接重做完整候选片，没有停在分析阶段，也没有要求用户多审一轮分镜。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = video_repair_execution + script_visual_alignment_repair + evidence_driven_auto_edit + hyperframes_result_card_repair + review_candidate_delivery`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`。
- `DeepSeek`：本轮因用户禁止读取 API key / token / secret，供料闸门记录为 `fallback_local_only`，`not_deepseek_conclusion = true`；结论来自 Codex 对 repo 文件、素材解析报告、运行产物和验证结果的本地复核。
- `已生成` 新修复候选片目录：`dist/fourth_episode_data_result_card_publish_candidate_repair_evidence_auto_edit/`，包含 `full.mp4`、`narration.wav`、`captions.srt`、`summary.json`、`review_manifest.md`、`publish_candidate_checklist.json`、`content_route_card_v2.json`、`script_to_timeline_map.json`、`material_evidence_contract.json`、`line_group_evidence_gate_report.json`、`auto_storyboard_preflight_report.json`、`hyperframes_card_validation_report.json`、`subtitle_card_overlap_check.json`、`platform_risk_precheck.json`、`privacy_risk_check.json`。
- `证据预检`：`auto_edit_allowed = true`；`total_line_groups = 36`；`direct_match_count = 6`；`proxy_match_count = 11`；`card_required_resolved_count = 19`；`blocked_no_evidence_count = 0`；`high_mismatch_risk_count = 0`；`privacy_high_selected_count = 0`；`material_03 00:30-00:55` 未入片。
- `文案画面对齐`：`lg_014-lg_016` 已全部改为 `card_required_resolved`，由 HyperFrames 下一轮变量 / 指标卡承接；判断句、动作句、边界句不再硬配普通录屏。
- `HyperFrames`：真实生成 19 个 HyperFrames 片段；`main_card_count = 4`、`sub_state_count = 15`、`actual_visible_main_cards = 4`、`whether_card_budget_gate_passed = true`；数据成果卡按原始数据、留存指标、AI 判断、下一步变量 / 验证指标逐层同步口播。
- `字幕 / 卡片`：卡片段不烧录大灰底字幕条，仅保留 sidecar SRT；`subtitle_card_overlap_check.status = passed`，`high_severity_overlap = false`。
- `验证`：`python3 -m py_compile scripts/*.py` passed；JSON parse passed；`ffprobe` passed；`ffmpeg decode` passed；video metadata probe passed；`npm run check` passed；`npx hyperframes lint / inspect` passed；`git diff --check` passed。
- `状态边界`：`review_candidate_ready_for_human_review = true`；`publish_candidate_ready = false`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`visual_master_locked = false`；未覆盖 `dist/latest_review_pack/`。
- `日志`：`codex_log/20260519_fourth_episode_evidence_auto_edit_alignment_repair.md`

## 20260519｜第四期修复候选片：逐句画面对齐 + HyperFrames 复盘卡

- `已确认` 本轮按用户人工审片反馈修复当前第四期候选片两个内容失败点：`script_visual_mismatch_issue（文案画面错位）` 与 `review_card_visual_quality_issue / hyperframes_not_used_issue（复盘卡未真实走 HyperFrames）`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = video_repair + quality_review + script_visual_alignment_repair + hyperframes_card_repair`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `影响面检查`：当前最新候选片来自 `codex_log/current_local_artifact_paths.md`，路径为 `dist/fourth_episode_data_result_card_publish_candidate/full.mp4`；`dist/latest_review_pack/` 仍是旧 v3.1 包，未作为本轮当前片、也未覆盖。
- `问题定位`：用户截图句“第六步，是下一轮变量。它最后不能给我十几个建议。”属于上一版 `dist/fourth_episode_ai_review_system_publish_candidate/lg_021`，不在最新数据成果卡候选片中；最新片对应语义为 `lg_014-lg_016`，已改用 HyperFrames 变量判断 / 指标卡承接。
- `根因分类`：`primary_issue = script_visual_mismatch_issue`；`secondary_issue = review_card_visual_quality_issue + hyperframes_not_used_issue`；当前旧候选片按 `content_validation = failed` 处理，不再写成内容通过。
- `已生成` 修复候选片目录：`dist/fourth_episode_data_result_card_publish_candidate_repair_script_visual_alignment_hyperframes_card/`，包含 `full.mp4`、`narration.wav`、`captions.srt`、`summary.json`、`media_probe.json`、`review_manifest.md`、`script_to_timeline_map.json`、`hyperframes_card_validation_report.json`、`subtitle_card_overlap_check.json`、`script_visual_alignment_report.json`、`quality_issue_classifier.json`、`repair_report.md`、`impact_check_report.md`。
- `HyperFrames`：真实调用 `npx --yes hyperframes@0.6.12 lint / inspect / render` 生成 10 个卡片片段；包含 `judgment_card`、`data_result_card`、`next_variable_judgment_card`、`metric_check_card`、`review_summary_card`、`boundary_card`、`review_result_card`、`summary_card`；每张均有 source HTML、render log、preview PNG 和 timeline MP4。
- `文案画面对齐`：`script_to_timeline_map.json` 已重写为 `line_group_repair_v1_hyperframes_cards`；`lg_014-lg_016` 不再硬配普通录屏；`lg_025 / lg_034 / lg_035` 这类抽象清单也改为结果卡承接；`script_visual_alignment_report.status = passed`。
- `字幕 / 卡片`：素材段字幕改为轻量底部胶囊；HyperFrames 卡片段不烧录大灰底字幕，仅保留 sidecar SRT；`subtitle_card_overlap_check.status = passed`，`high_severity_overlap = false`。
- `验证`：JSON parse passed；`python3 -m py_compile scripts/*.py` passed；`ffprobe` passed；`ffmpeg decode` passed；`npm run check` passed；`npx hyperframes lint && inspect` passed；`git diff --check` passed。
- `状态边界`：新片只是 `review_candidate_ready_for_human_review = true`；`publish_candidate_ready = false`；`publish_candidate_ready_for_human_review = false`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；未覆盖 `dist/latest_review_pack/`，未修改已发布视频，未推进 `visual_master_locked`。
- `日志`：`codex_log/20260519_repair_script_visual_alignment_and_hyperframes_review_card.md`

## 20260519｜第四期数据成果卡发布候选片生成

- `已确认` 本轮按用户锁定的新结构生成第四期完整 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`；不是 dry-run、不是文案包、不是 technical preview。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = video_sample_or_assembly + publish_candidate_delivery + locked_copy_video_execution + card_decision_gate_applied`；`current_project_state = formal_operation_active + data_driven_operation_iteration`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`。
- `DeepSeek`：执行前供料尝试被 `invalid_context_pack` 阻断，未写成 DeepSeek 真实结论；本轮结论来自 Codex 对 repo 文件、素材审计、运行产物和验证结果的本地复核。
- `已生成` 新候选片目录：`dist/fourth_episode_data_result_card_publish_candidate/`，包含 `full.mp4`、`narration.wav`、`captions.srt`、`summary.json`、`media_probe.json`、`review_manifest.md`、`publish_candidate_checklist.json`、`locked_copy_contract.json`、`content_route_card_v2.json`、`script_to_timeline_map.json`、`tts_prosody_anchor_map.json`、`card_decision_dry_run.json`、`subtitle_card_overlap_check.json`、`platform_risk_precheck.json`、`privacy_risk_check.json`、`narration_tts_debug_sanitized.json`。
- `locked_copy_contract`：锁定标题为 `我把一条低播放视频，变成了一页下一条能执行的复盘卡`；锁定开头句为 `我最近发了一条视频。`；未改核心语义；`content_validation = pending_user_chatgpt_review`。
- `卡片`：`card_decision_gate` 已运行；实际时长 `177.926s`；`max_main_cards = 4`；选中 `judgment_card / data_result_card / boundary_card / summary_card`；`data_result_card` 出现在 `00:00:22.109-00:00:27.503`；`evidence_window_protection = passed`；`hyperframes_unchanged_check = passed_no_visual_motion_skin_change`。
- `TTS`：使用远程 Aliyun/Bailian TTS，`target_model = qwen3-tts-vc-realtime-2026-01-15`，`voice_base_candidate = qwen-t...ac19`，继承 `20260427_B_pacing_reference`；只对远程 TTS 段做轻微 `speech_pacing` 调整；`local_tts_fallback_used = false`；`macos_say_used = false`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`。
- `素材使用`：`opening_evidence = material_04 00:55-01:30`；`middle_evidence = material_02 00:20-01:50`；`ending_support = material_01 01:04-01:28 + material_04 01:30-01:50`；未使用 `material_03 00:30-00:55`。
- `验证`：`py_compile` passed；`tests/test_card_decision_gate.py` passed；JSON parse passed；`ffprobe` passed；`ffmpeg decode` passed；video metadata probe passed；acceptance assertions passed；`git diff --check` passed；`secret_leak_scan_sanitized = passed`。
- `状态边界`：`publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`current_data_goal_anchor_ready = false`；`visual_master_locked = false`；`dist/latest_review_pack/` 未覆盖；未提交原始素材视频。
- `日志`：`codex_log/20260519_fourth_episode_data_result_card_publish_candidate.md`

## 20260519｜card_budget_gate 与 data_result_card 路由补强

- `已确认` 本轮只做《视频工厂》卡片判断机制补强；不重做第四期视频，不改变 HyperFrames 展示形式、视觉路线、动效路线、卡片皮肤或现有生成方式。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + validation_dry_run`；`large_task_gate = triggered`；`lane = serial_only`；`DeepSeek = fallback_local_only`；`not_deepseek_conclusion = true`。
- `state_action_router（状态动作总控器）`：`input_signal = data_result_card / card_budget_gate / cluster_merge_rule / evidence_window_protection`；`current_project_state = formal_operation_active + data_driven_operation_iteration`；`selected_action = 机制文件补强 + helper / fixture / test + 第四期 dry-run`；`forbidden_action = regenerate_video / change_HyperFrames_visual_motion_skin / advance_status`。
- `已更新` `GPT数据源/05_文案路由规则.md`：在 `content_route_card V2.card_placement_decision` 中补入 `card_budget_gate（卡片预算闸门）`、`cluster_merge_rule（信息簇合并规则）`、`evidence_window_protection（证据窗口保护规则）`、`data_result_card_priority（数据成果卡优先级）` 和 `card_type_selection_policy（卡片类型选择策略）`。
- `已更新` `GPT数据源/07_AI知识类视频价值规则.md`：明确 `data_result_card（数据成果卡）` 只能压缩真实数据、AI 判断、下一步变量和验证指标；卡片好看或位置正确不等于 `content_validation` 通过。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md`、`codex_source/19_project_state_action_router.md`、`codex_source/21_codex_judgment_permission_matrix.md`：接入卡片预算、信息簇、数据成果卡优先级和证据窗口保护；超预算时 `data_result_card > key_judgment_card > ending_summary_card > boundary_card > process_summary_card`。
- `已新增` 可运行判断层：`scripts/卡片判断闸门_card_decision_gate.py`、`codex_source/fixtures/卡片判断闸门_card_decision_gate_cases.json`、`tests/test_card_decision_gate.py`。
- `第四期 dry-run`：`dist/fourth_episode_ai_review_system_publish_candidate/card_decision_dry_run.json` 已生成；当前 4 张卡仍在预算内，`lg_010 -> lg_014` 间距为 `soft_spacing_warning`；识别 `lg_019-lg_023` 为 `data_result_card` 候选信息簇，但因缺真实数值，状态为 `candidate_blocked_missing_real_metric_values`。
- `建议`：若后续用户授权重做第四期并补齐真实数值，优先把 `lg_010 process_summary_card` 替换或合并为 `data_result_card`；当前不得新增素材里没有的数据结论。
- `未推进`：未生成或覆盖 `full.mp4 / narration.wav / captions.srt`；未覆盖 `dist/latest_review_pack/`；未推进 `content_validation / send_ready / current_data_goal_anchor_ready / voice_validation / visual_master_locked`。
- `验证`：JSON parse passed；Python `py_compile` passed；fixture unittest passed；第四期 dry-run passed；`git diff --check` passed。
- `日志`：`codex_log/20260519_card_budget_gate_and_data_result_card_route.md`

## 20260518｜第四期 AI 短视频复盘系统发布候选片生成

- `已确认` 本轮在用户明确授权阿里 / 百炼远程 TTS 后，使用 `authorized_runtime_config` 作为 TTS 授权来源；未打印、未写入、未提交 API key。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = video_sample_or_assembly + publish_candidate_delivery + TTS_authorization_unblock + project_file_change`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`execution_permission = conditional_execute_after_tts_auth_check -> executed`。
- `state_action_router（状态动作总控器）`：`inferred_state = remote_tts_authorization_check_required_before_video_assembly`；`selected_action = 先做 TTS 授权安全检查，再生成完整发布候选正片`；`forbidden_action = local_tts_fallback / macOS say / silent preview / technical_preview_as_delivery / key_print_or_write`。
- `skill_used`：本轮继续引用 `skills/视频素材解析_video_material_audit/SKILL.md`；第四期素材使用边界来自 `codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md`。
- `已生成` 完整发布候选片：`dist/fourth_episode_ai_review_system_publish_candidate/full.mp4`；规格 `1920x1080`、`16:9`、H.264、AAC 口播音轨、`mov_text` 字幕流、可解码。
- `已生成` 口播音轨：`dist/fourth_episode_ai_review_system_publish_candidate/narration.wav`；`provider = aliyun_bailian`；`model = qwen3-tts-vc-realtime-2026-01-15`；`local_tts_fallback_used = false`；`macos_say_used = false`。
- `已生成` 审片包与锚点文件：`summary.json`、`media_probe.json`、`review_manifest.md`、`publish_candidate_checklist.json`、`content_route_card_v2.json`、`script_to_timeline_map.json`、`tts_prosody_anchor_map.json`、`subtitle_card_overlap_check.json`、`platform_risk_precheck.json`、`privacy_risk_check.json`、`narration_tts_debug_sanitized.json`。
- `素材使用`：已使用 `material_04 00:55-01:50` 开头证据、`material_02 00:20-01:50` 中段主体、`material_01 01:04-01:28` 结尾辅助；未使用 `material_03 00:30-00:55` 高隐私片段。
- `验证`：JSON parse passed；`py_compile` passed；`ffprobe` passed；`ffmpeg decode` passed；音量检查非静音；抽帧 contact sheet 已人工目检；`secret_leak_scan_sanitized = passed`。
- `状态边界`：`publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`current_data_goal_anchor_ready = false`；`visual_master_locked = false`；`voice_validation = pending`。
- `未推进 / 未提交`：未覆盖 `dist/latest_review_pack/`；未提交原始素材视频；未生成正式下一条视频执行 prompt；未提交 runtime config 或任何 secret 文件。
- `日志`：`codex_log/20260518_fourth_episode_ai_review_system_publish_candidate.md`

## 20260518｜第四期 AI 短视频复盘系统发布候选片阻断

- `blocked_publish_candidate_unavailable`：本轮目标是直接生成 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`，但当前进程没有远程 TTS 授权环境变量，且用户本轮禁止读取 `.env / API key / token / secret`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = video_sample_or_assembly + project_file_change + review_diagnosis_audit`；`large_task_gate = triggered`；`lane = audit_lane -> blocked`；`parallel = serial_only`；`execution_permission = blocked_publish_candidate_unavailable_before_video_generation`。
- `state_action_router（状态动作总控器）`：`inferred_state = publish_candidate_requested_but_remote_tts_authorization_unavailable_under_secret_read_ban`；`selected_action = 记录阻断，不生成降级视频`；`forbidden_action = read_secret / local_tts_fallback / macos_say / silent_preview / technical_preview_as_delivery`。
- `skill_used`：已读取并使用 `skills/视频素材解析_video_material_audit/SKILL.md` 复核第四期素材证据边界；`material_02` 与 `material_04` 均仍可读，2 秒解码抽样通过。
- `TTS 状态`：`DASHSCOPE_API_KEY_present = false`、`ALIYUN_API_KEY_present = false`；既有脚本依赖本地 runtime config 的 `auth.api_key`，本轮按用户边界未读取该 secret，未调用远程 TTS。
- `未生成`：未创建 `dist/fourth_episode_ai_review_system_publish_candidate/`，未生成 `full.mp4 / narration.wav / captions.srt / review pack / publish_candidate_checklist`，未用 JSON / route card 冒充完成。
- `未推进`：`publish_candidate_ready_for_human_review = false`、`content_validation = pending_user_chatgpt_review_not_advanced`、`send_ready = false`、`current_data_goal_anchor_ready = false`、`voice_validation = pending_not_advanced`、`visual_master_locked = false`。
- `未修改`：未覆盖 `dist/latest_review_pack/`，未提交原始视频素材。
- `日志`：`codex_log/20260518_fourth_episode_ai_review_system_publish_candidate.md`

## 20260518｜第四期素材审计与项目内视频素材解析 skill

- `已确认` 本轮先新增项目内可复用 skill：`skills/视频素材解析_video_material_audit/SKILL.md`，并补充模板与 README；后续命中素材录制 / 解析视频 / 素材审计 / 给 ChatGPT 写素材报告类任务时，必须优先读取并使用该 skill。
- `已确认` 已最小同步入口：`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`；未读取或未实际使用该 skill，不得把素材审计写成 `completed（已完成）`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + review_diagnosis_audit + material_audit`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`execution_permission = audit_only`。
- `DeepSeek`：本轮用户明确禁止外部 API / secret 读取；已创建本地供料请求卡 `codex_log/supply_requests/20260518_fourth_episode_material_audit_pre_supply_request.json`，口径为 `fallback_local_only`、`not_deepseek_conclusion = true`，未写成 DeepSeek 真实参与。
- `已确认` 第四期素材目录命中 `/Users/fan/Documents/视频工厂/素材录制/第四期`，共 4 个 `.mp4` 素材；4 个素材均 `ffprobe` 可读、`ffmpeg` 可解码、H.264、30fps、无音轨。
- `已生成` 素材索引：`codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_index.json`。
- `已生成` ChatGPT 可读素材细节报告：`codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md`，报告中已标明 `skill_used = skills/视频素材解析_video_material_audit/SKILL.md`。
- `素材判断`：`material_02` 最适合作为主素材，证明从 prompt 拆成配置、字段、模板、报告和验收标准；`material_04 00:55-01:30` 最适合作为开头证据，直接支撑“一句糊话变执行单”；`material_03 00:30-00:55` 隐私风险最高，不建议未打码公开使用。
- `部分成立` 第四期素材能支撑下一条从“数据复盘能力”转向“真实 AI 工作流实验”；但 `待验证` 仍不能证明 AI 已经自动做完整条视频、商业闭环成立或正式执行 ready。
- `未推进`：未生成最终文案、未生成新视频、未生成正式下一条视频执行 prompt、未推进 `content_validation / send_ready / publish_candidate / current_data_goal_anchor ready`、未提交原始视频素材。
- `日志`：`codex_log/20260518_fourth_episode_material_audit.md`

## 20260517｜V004 interim_17h 数据与文案补录

- `已确认` 本轮在 V002 未提交补录基础上继续串行执行 V004 记录；最终计划 V002 + V004 统一 commit / push。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = project_file_change + operation_data_intake + copy_record_backfill + operation_decision_rerun + copy_iteration_rerun`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`。
- `state_action_router（状态动作总控器）`：`input_signal = 用户提供 V004 约 17h 数据截图和完整 raw copy`；`inferred_state = latest_operation_sample_pre_24h + copy_version_record_missing`；`selected_action = 归档截图、新增 V004 snapshot / operation record / copy_iteration 记录、重跑系统`。
- `V004 身份`：登记为 `latest_operation_sample_pre_24h`；`current_operation_target_switched = false`；V003 仍保持 `current_operation_target`。
- `截图归档`：三张截图已归档到 `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/`，`screenshot_archive_status = archived_to_repo`。
- `V004 数据`：播放 55、点赞 1、收藏 0、完播率 4.76%、2s 跳出 41.18%、5s 完播 30.88%、平均播放 14 秒、推荐页 95.2%、个人主页 4.8%、涨粉 0。
- `数据窗口`：`review_window = pre_24h`，`snapshot_label = interim_17h_snapshot`，不是 24h final、72h final 或 7d final。
- `raw copy`：V004 原始文案已保真写入 `review_loop/copy_iteration/V004/V004_copy_v1_raw.md`；`raw_copy_modified = false`。
- `文案数据边界`：V004 自身 `favorite_count = 0`；raw copy 中“3 个收藏”引用的是 V003 复盘案例，不是 V004 自身数据。
- `copy_registry`：已登记 `V002 / V003 / V004`，V004 为 `recorded_latest_sample_pre_24h_only`。
- `运营决策系统`：已重跑并验证通过；`records_processed = V001 / V002 / V003 / V004`，仍阻断正式下一期执行。
- `文案迭代系统`：已重跑并验证通过；V004 copy record / structure map / decision / brief 均已生成，未生成正式下一条视频执行 prompt。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`current_data_goal_anchor ready`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260517_V004_interim_17h_data_and_copy_intake.md`

## 20260517｜V002 原始文案与 56/6/9 用户补充数据补录

- `已确认` 本轮只做 V002《自动流的最简单流程》原始文案补录、用户补充数据补录、文案迭代记录补齐、系统重跑和日志更新；不生成新视频，不生成正式下一条视频执行 prompt，不推进 `content_validation / send_ready / current_data_goal_anchor ready`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = project_file_change + data_backfill + copy_iteration_record_backfill + operation_decision_rerun + copy_iteration_rerun`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `state_action_router（状态动作总控器）`：`input_signal = 用户指出 V002 原始文案未登记并补充 56/6/9 数据`；`inferred_state = copy_version_record_missing + V002_metric_backfill_needed + abnormal_sample_boundary_required`；`selected_action = 新增 V002 copy_iteration 记录、补录用户数据、重跑运营 / 文案迭代系统`；`forbidden_action = normal_distribution_attribution / content_validation passed / direction established / next formal prompt / ready promotion`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260517_V002_copy_and_metric_backfill_pre_supply_request.json`；真实供料通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `已新增` V002 文案记录目录：`review_loop/copy_iteration/V002/`，包含 `V002_copy_v1_raw.md`、`V002_copy_v1_record.json`、`V002_copy_structure_map.json`、`V002_copy_iteration_decision.json`、`V002_next_copy_revision_brief.md`。
- `raw copy`：用户本轮提供的第二期原始文案已保真写入；`raw_copy_modified = false`，疑似错字只在 record 中标记，不改 raw。
- `copy_registry`：`review_loop/copy_iteration/copy_registry.json` 已新增 `V002_copy_v1`；V002 标记为 `policy_limited_abnormal_operation_sample` 和 `recorded_abnormal_sample_reference_only`，不设为 current operation target。
- `V002 数据补录`：历史已记录 39 / 5 / 8 保留；新增用户补充 56 播放、6 点赞、9 收藏，`source_status = user_provided_in_chat / no_screenshot_yet`。
- `计算指标`：`like_rate = 6 / 56 = 10.71%`；`favorite_rate = 9 / 56 = 16.07%`；`like_plus_favorite_action_rate = 15 / 56 = 26.79%`。
- `样本解释`：V002 仍是 `policy_limited_abnormal_operation_sample（平台审核减推异常样本）`；`sample_interpretation_label = policy_limited_but_interest_signal_strong（平台减推污染样本，但兴趣信号强）`；不得写成正常自然流量样本、内容通过、方向成立或商业验证成立。
- `运营决策系统`：已重跑 `scripts/运营决策系统_operation_decision_system.py`；V002 仍被排除出正常自然流量归因，V003 仍是 `current_operation_target`，下一期正式执行仍 blocked。
- `文案迭代系统`：已重跑 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`；系统现在登记 V002 + V003 两条 copy records，V003 当前低置信度准备口径不变。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`current_data_goal_anchor ready`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`visual_master_locked（视觉母版锁定）`；未生成正式下一条视频执行 prompt。
- `日志`：`codex_log/20260517_V002_copy_and_metric_backfill.md`

## 20260517｜DeepSeek deep file supply mode 深度文件供料机制升级

- `已确认` 本轮只做 DeepSeek 供料机制、Codex 执行规则、schema / fixture / request / controller / 日志升级；不生成新视频，不修改已发布视频，不推进视频状态。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + validation_layer_sync`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `state_action_router（项目状态动作总控器）`：`input_signal = 用户要求 DeepSeek 深度参与并直接帮 Codex 读取任务相关文件内容`；`inferred_state = deepseek_deep_file_supply_required + codex_vertical_completion_missing`；`selected_action = 更新机制、执行规则、controller、schema、fixtures、supply requests、日志和验证链`。
- `impact_check_report（影响面检查）`：当前 DeepSeek 链路包含 `scripts/deepseek_supply_controller.py`、`scripts/deepseek_readonly_explorer.py`、`scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py`、`scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`、`codex_source/17`、`codex_source/18`、`codex_source/schemas/deepseek_supply_request.schema.json`、`codex_source/fixtures/*` 和 `codex_log/supply_requests/*`；旧机制已有 pre / post risk review，但缺内容级 `relevant_file_bundle / exact_snippet_pack` 和一等 `mid_task_incremental_supply` 字段。
- `已接入` `DeepSeek deep file supply mode（DeepSeek 深度文件供料模式）`：默认链路为 `route_decision -> create_supply_request -> deep_file_prefetch -> relevant_file_bundle -> exact_snippet_pack -> dependency_map -> risk_and_conflict_report -> codex_next_input -> mid_task_incremental_supply -> post_risk_review -> completion_truth_check`。
- `已接入` `Codex minimal review policy（Codex 最小必要复核策略）`：Codex 不再默认全仓深读，但必须复核 `will_modify_files`、`conflict_or_uncertain_files`、`validation_failed_files`、`safety_sensitive_files`、schema / tests 依赖文件和 runtime safety 文件。
- `已更新` controller：`scripts/deepseek_supply_controller.py` 支持 `deep_supply_mode`、嵌套 `file_scope`、`content_loading_policy`、`codex_minimal_review_policy`、`incremental_supply_request`，并把 `relevant_file_bundle`、`exact_snippet_pack`、`dependency_map`、`risk_delta_report`、`missing_or_uncertain_files` 写入 supply pack / manifest / markdown。
- `已更新` schema / docs：`codex_source/schemas/deepseek_supply_request.schema.json`、`codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`、`GPT数据源/01`、`08`、`10`、`11`。
- `已新增` fixtures：`codex_source/fixtures/DeepSeek深度文件供料_deep_file_supply_cases.json` 覆盖 `case_1_deep_file_prefetch_success`、`case_2_mid_task_incremental_supply_required`、`case_3_fallback_not_deep_participation`；`codex_source/fixtures/DeepSeek深度文件供料_deep_file_supply_request_example.json` 可用于 controller fallback truth 验证。
- `已新增 / 更新` supply requests：`codex_log/supply_requests/20260517_deepseek_deep_file_supply_mode_pre_supply_request.json`、`20260517_deepseek_deep_file_supply_mode_mid_task_incremental_supply_request.json`、`20260517_deepseek_deep_file_supply_mode_post_risk_review_request.json`。
- `DeepSeek real-call validation`：pre / mid / post 三次通过 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py`，均为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`；输出目录分别为 `dist/deepseek_supply_controller/deep_file_supply_mode_pre_supply/`、`deep_file_supply_mode_mid_task/`、`deep_file_supply_mode_post_risk_review/`。
- `field preservation validation`：pre pack 含 `relevant_file_bundle = 10`、`exact_snippet_pack = 11`、`dependency_map = 10`；mid pack 含 `relevant_file_bundle = 10`、`exact_snippet_pack = 11`、`dependency_map = 10`；post pack 含 `relevant_file_bundle = 9`、`exact_snippet_pack = 10`、`dependency_map = 9`，且 `post_risk_review = true`。
- `fallback truth validation`：fixture controller run 输出 `supply_source = fallback_local_only`、`not_deepseek_conclusion = true`，同时仍保留 `relevant_file_bundle / exact_snippet_pack / dependency_map`；fallback 未被误写成 DeepSeek 真实参与。
- `completion_truth_check`：`failed_insufficient_depth` 和 `failed_deepseek_not_deeply_participated` 两个负例断言通过；能识别 deep supply 不足和用户要求 DeepSeek 但只有 fallback 的情况。
- `验证`：`python3 -m py_compile scripts/*.py` passed；8 个 JSON parse passed；schema 新字段存在且 `mid_task_incremental_supply` 在 enum 中；fixture controller run passed；pre / mid / post safe runner real call passed；`git diff --check` passed。
- `GPT Project 上传包`：`not_generated（未生成）`；本轮只是机制文件、脚本、schema、fixture 和日志变更，没有伪装成 UI / GPT Project 上传已同步。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `待验证`：本轮证明机制接线和本地三次真实调用通过；DeepSeek 深度文件供料在后续独立 Codex 会话、更多任务类型、长期 token 递减和 post risk review 稳定性仍需继续验证，不能写成长期稳定已验证或 multi-agent runtime 已跑通。
- `日志`：`codex_log/20260517_DeepSeek深度文件供料闸门_deepseek_deep_file_supply_gate.md`
- `下一个目标`：后续所有大型 / 多文件 / DeepSeek 明确参与任务，默认使用 deep file supply request，并在执行中触发 `mid_task_incremental_supply`；Codex 只做最小必要复核、写入、验证和收尾。

## 20260517｜V003 post_72h_pre_7d 数据录入与账号诊断记录

- `已确认` 本轮只做 V003 运营数据录入、账号诊断记录、项目文件修改和复盘前置系统重跑；不生成新视频，不修改已发布视频，不生成正式下一条视频执行 prompt。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = operation_data_intake + account_diagnostic_intake + project_file_change + operation_decision_rerun + copy_iteration_rerun`；`current_project_state = formal_operation_active + operation_data_intake + account_diagnostic_intake + operation_review_pending`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `state_action_router（状态动作总控器）`：`input_signal = 用户提供 V003 72h 后 / 7d 前数据截图和账号诊断截图`；`inferred_state = operation_data_intake + account_diagnostic_intake`；`selected_action = 归档截图、新增 V003 post_72h_pre_7d 快照、单独记录账号诊断、重跑运营决策系统和文案迭代系统`；`forbidden_action = next_formal_video_execution_prompt / content_validation / send_ready / ready_status_promotion`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260517_V003_post_72h_pre_7d_data_intake_pre_supply_request.json`；真实供料通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `已归档` V003 三张截图到 `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/post_72h_pre_7d_snapshot/`，分别为总览、流量分析 / 留存、观众分析；`screenshot_archive_status = archived_to_repo`。
- `已归档` 账号诊断截图到 `review_loop/account_diagnostics/20260517_account_diagnostic_snapshot/`；账号诊断只作为账号层观察，不写入 V003 单条视频指标。
- `已新增` V003 结构化快照：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_post_72h_pre_7d_snapshot.json`。
- `数据窗口`：`review_window = post_72h_pre_7d`，`snapshot_label = post_72h_pre_7d_snapshot`，`captured_late_after_72h = true`，`exact_72h_capture = false`，`not_final_7d_review = true`；明确不是 `72h_final_at_exact_72h`，不是 `7d_final_data`。
- `核心数据`：播放 143、平均播放 20 秒、2s 跳出 48.81%、5s 完播 28.57%、完播率 4.05%、收藏 3 / 2.10%、涨粉 1、推荐页 94.6%、个人主页 4.1%、朋友页 1.4%。
- `对比 65h`：播放 141 -> 143，平均播放 21 秒 -> 20 秒，未出现明显二次分发；该结论只作为低置信度趋势，不写项目失败、方向失败、方向成立或账号增长稳定成立。
- `账号诊断`：已新增 `account_diagnostic_20260510_20260516.json` 与 `.md`；统计周期 `2026-05-10 至 2026-05-16`，投稿 2、播放 170、完播率 4.84%、互动指数 5.29%、粉丝净增 1；昨日主页访问 1 是账号层数据，不等于 V003 单条视频 `profile_visit_count`。
- `已更新` V003 记录、截图 manifest、缺失 / 不确定字段、ChatGPT 复盘输入、`current_operation_target`、`current_data_goal_anchor`、`operation_records_index`、当前正式事实、数据飞轮与数据目标总线。
- `运营决策系统`：已重跑 `scripts/运营决策系统_operation_decision_system.py`；最新报告读取 `post_72h_pre_7d_snapshot`，仍输出 `blocked_for_formal_next_episode_execution`。
- `文案迭代决策系统`：已重跑 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`；`current_data_window = post_72h_pre_7d_snapshot`，`formal_copy_revision_allowed = false`，仅允许低置信度准备 `opening_0_3s + bridge_3_8s`。
- `缺失字段`：`7d_final_data`、`3s_retention`、`profile_visit_count`、`dm_count`、`effective_dm_count`、`effective_consult_count`、`clear_need_customer_count` 仍为 missing。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`；`current_data_goal_anchor` 未写 ready；未生成正式下一条视频执行 prompt。
- `日志`：`codex_log/20260517_V003_post_72h_pre_7d_data_intake.md`

## 20260517｜第三期真实复盘现场低置信度审片包

- `已确认` 本轮基于第三期素材审计报告和 V003 文案迭代简报，生成 `low_confidence_review_candidate（低置信度审片候选）/ internal_review_pack（内部审片包）`；不是正式发布候选片，不生成正式下一条视频执行 prompt。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = low_confidence_review_candidate_video + material_execution + copy_iteration_candidate + project_file_change + code_debug`；`current_project_state = formal_operation_active + copy_iteration_prepare + material_audit_ready + formal_next_execution_blocked`；`execution_permission = low_confidence_internal_review_candidate_only`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`。
- `state_action_router（状态动作总控器）`：`input_signal = 用户要求按照真实复盘现场型结构执行`；`inferred_state = low_confidence_review_candidate_allowed`；`selected_action = 基于 locked copy、material_03 和判断卡生成内部审片候选包`；`forbidden_action = publish_candidate promotion / send_ready / content_validation passed / ready status promotion`。
- `DeepSeek`：已创建执行前供料任务卡 `codex_log/supply_requests/20260517_third_episode_real_review_scene_candidate_pre_supply_request.json` 和执行后风险复核任务卡 `codex_log/supply_requests/20260517_third_episode_real_review_scene_candidate_post_risk_review_request.json`；两次真实调用均通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `使用素材`：主素材 `material_03 / /Users/fan/Documents/视频工厂/素材录制/第三期/v004 2026-05-16 23-22-13.mp4`；辅助素材 `material_01 / /Users/fan/Documents/视频工厂/素材录制/第三期/第二期 2026-05-15 23-15-27.mp4`；`material_02_used = false`。
- `已生成` 审片包目录：`dist/third_episode_real_review_scene_candidate/`。
- `已生成` 主视频：`dist/third_episode_real_review_scene_candidate/full.mp4`；`1920x1080`、`30fps`、`16:9`、可解码、有 AAC 音轨、有 `mov_text` 字幕。
- `已生成` 审片与执行文件：`review_manifest.md`、`summary.json`、`content_route_card_v2.json`、`script_to_timeline_map.json`、`card_placement_decision.json`、`subtitle_card_overlap_check.json`、`media_probe.json`、`locked_copy_contract.json`、`captions.srt`、`narration.wav`、`narration_tts_debug_sanitized.json`、`tts_prosody_anchor_map.json`。
- `TTS 边界`：本轮按用户要求禁止本地 TTS，实际使用项目 Aliyun / Bailian 远程 TTS 链路；`local_tts_fallback_used = false`、`macos_say_used = false`、`silent_audio_fallback_used = false`；不推进 `voice_validation` 或 `final_voice_validated`。
- `HyperFrames`：使用 `clean_soft` 皮肤生成 1 张开头判断卡、2 张轻判断卡和 1 张结尾总结卡；卡片只做判断压缩，不替代 `material_03` 真实复盘录屏证据。
- `字幕 / 卡片重叠`：`subtitle_card_overlap_check.status = passed`，未发现 high severity overlap；卡片为独立短片段，不遮挡 `material_03` 关键证据窗口。
- `未推进`：`publish_candidate_ready_for_human_review`、`content_validation（内容验证）`、`send_ready（可发送状态）`、`current_data_goal_anchor ready`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260517_third_episode_real_review_scene_candidate.md`。
- `下一个安全用法`：只可供用户 / ChatGPT 内部审片判断真实复盘现场型结构是否值得继续；不能直接作为正式发布候选或下一条正式执行结果。

## 20260517｜第三期素材内容审计

- `已确认` 本轮只做第三期录制素材内容审计、复盘 / 诊断 / 审核和项目文件修改；不生成新视频，不修改已发布视频，不写下一期正式文案，不生成正式下一条视频执行 prompt。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = material_audit + review_diagnosis_audit + project_file_change`；`current_project_state = formal_operation_active + material_audit_needed + copy_iteration_prepare`；`execution_permission = audit_only`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`。
- `state_action_router（状态动作总控器）`：`input_signal = 用户录制第三期 3 个素材完成，要求解析并输出给 ChatGPT 的素材内容报告`；`inferred_state = material_audit_needed`；`trigger_mechanism = material_detail_report_for_copy_iteration`；`selected_action = 审计第三期素材并生成 ChatGPT 可用报告`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260517_third_episode_material_audit_pre_supply_request.json`；真实调用通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `素材目录`：`/Users/fan/Documents/视频工厂/素材录制/第三期`；已识别 3 个视频素材：`第二期 2026-05-15 23-15-27.mp4`、`内建视网膜显示器 2026-05-17 02-14-27.mp4`、`v004 2026-05-16 23-22-13.mp4`。
- `媒体检查`：3 个素材均为 h264、30fps、可解码、无音轨；`blackdetect` 未发现 2 秒以上明显黑屏；`freezedetect` 发现静态阅读停顿，结合画面判断主要是页面阅读停留，不等同于录屏中断。
- `内容审计结论`：`material_03` 是最强素材，支持“真实数据冲突开头”和“AI 真正有用的是判断下一条先改哪”；`material_01` 支持“一句糊话怎么变成可执行任务单”的候选方向但缺真实前后对比；`material_02` 支持 V003 65h 数据回填边界但含本地路径 / 桌面 / 侧栏暴露风险，需裁切或打码。
- `已新增` Markdown 报告：`codex_log/material_audit/third_episode/20260517_third_episode_material_detail_report.md`。
- `已新增` JSON 索引：`codex_log/material_audit/third_episode/20260517_third_episode_material_index.json`。
- `已新增` dated log：`codex_log/20260517_third_episode_material_audit.md`。
- `本地辅助抽帧`：`dist/material_audit/third_episode/`，仅作审计辅助，不纳入本轮 commit；源视频不提交 Git。
- `与 V003 文案迭代关系`：支持 `opening_packaging` 与 `bridge_3_8s` 的低置信度准备；`formal_copy_revision_allowed = false`；不支持全文重写、换方向、换人群或生成正式下一条视频执行 prompt。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`current_data_goal_anchor ready`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `下一个安全用法`：ChatGPT 读取本报告后，只做低置信度开头 / 3-8 秒承接备选；若要进入正式执行，先补录干净证据窗口或等待 V003 72h / 7d 与需求侧字段补齐。

## 20260516｜V003 interim_65h 数据录入与系统重跑

- `已确认` 本轮只做 V003 运营数据录入、项目文件修改和复盘前置数据更新；不生成新视频，不修改已发布视频，不生成正式下一条视频执行 prompt。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = operation_data_intake + project_file_change + operation_decision_rerun + copy_iteration_rerun`；`large_task_gate = triggered`；`lane = standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `state_action_router（状态动作总控器）`：`inferred_state = operation_data_intake + operation_decision_system_required + copy_iteration_system_required`；`selected_action = archive_screenshots + update_V003_interim_65h_snapshot + rerun_decision_systems`；`forbidden_action = next_formal_video_execution_prompt / content_validation / send_ready / ready_status_promotion`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260516_V003_interim_65h_data_intake_pre_supply_request.json`；真实供料通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。
- `已归档` 本轮 3 张截图到 `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/`，分别为总览、流量分析 / 留存、观众分析。
- `已新增` 结构化快照：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_interim_65h_snapshot.json`。
- `数据窗口`：`review_window = between_48h_and_72h`，`snapshot_label = interim_65h_snapshot`，`snapshot_alias = near_72h_pre_final_snapshot`；明确不是 `72h_final_data`，不是 `7d_final_data`。
- `核心数据`：播放 141、平均播放 21 秒、2s 跳出 49.69%、5s 完播 27.95%、完播率 4.14%、收藏 3 / 2.13%、涨粉 1、推荐页 96.6%、个人主页 2.1%、朋友页 1.4%。
- `对比 36h`：播放、平均观看、收藏、涨粉基本未增长；可记录为“未出现二次增长 / 分发未扩散”，但不得写项目失败、方向失败、方向成立或账号增长成立。
- `已更新` V003 记录、截图 manifest、缺失 / 不确定字段、ChatGPT 复盘输入、`current_operation_target`、`current_data_goal_anchor`、`operation_records_index`、legacy pointer 与当前正式事实。
- `运营决策系统`：已重跑 `scripts/运营决策系统_operation_decision_system.py`；最新报告读取 `interim_65h_snapshot`，仍输出 `blocked_for_formal_next_episode_execution`。
- `文案迭代决策系统`：已重跑 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`；`current_data_window = interim_65h_snapshot`，`problem_layer = opening_packaging`，`confidence = low`，`formal_copy_revision_allowed = false`，仅允许低置信度准备 `opening_0_3s + bridge_3_8s`。
- `缺失字段`：`72h_final_data`、`7d_final_data`、`3s_retention`、`profile_visit_count`、`dm_count`、`effective_dm_count`、`effective_consult_count`、`clear_need_customer_count` 仍为 missing。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`；`current_data_goal_anchor` 未写 ready；未生成正式下一条视频执行 prompt。
- `日志`：`codex_log/20260516_V003_interim_65h_data_intake.md`

## 20260516｜文案迭代决策系统

- `已确认` 本轮只做机制修补 / 路由修补、项目文件修改和代码执行 / 调试；不生成新视频，不修改已发布视频，不生成正式下一条视频执行 prompt，不直接重写 V003 文案。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_execution_or_debug + copy_iteration_system`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Codex Integrator only`。
- `state_action_router（项目状态动作总控器）`：`inferred_state = copy_iteration_system_missing`；`selected_action = build_copy_iteration_decision_system`；`done_when = V003 文案被记录，系统生成 next_copy_revision_brief，并接入运营决策报告`。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260516_copy_iteration_decision_system_pre_supply_request.json`；真实调用通过，`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`、`env_file_read = false`。
- `已新增` 可运行脚本：`scripts/文案迭代决策系统_copy_iteration_decision_system.py`。
- `已新增` 文案迭代目录：`review_loop/copy_iteration/`，包含 `copy_registry.json`、`latest_copy_iteration_report.json`、`latest_copy_iteration_report.md` 和 V003 文案记录目录。
- `已保真登记` V003 第一版原始文案：`review_loop/copy_iteration/V003/V003_copy_v1_raw.md`；raw 文案未改写，`克资 / 刻字定义 / 克兹` 只在 `suspected_typos` 中标记为疑似“客资”误写。
- `已生成` V003 文案版本记录、结构拆解和迭代决策：`V003_copy_v1_record.json`、`V003_copy_structure_map.json`、`V003_copy_iteration_decision.json`。
- `已生成` 给 ChatGPT 读取的 `V003_next_copy_revision_brief.md`：当前只允许低置信度准备开头 0-3 秒和 3-8 秒承接，不允许全文重写、换方向、换人群或改 offer。
- `V003_copy_iteration_result`：`problem_layer = opening_packaging`；`supporting_problem_layers = bridge_3_8s`；`confidence = low`；`formal_copy_revision_allowed = false`；`low_confidence_prepare_allowed = true`；`revision_scope = opening_0_3s + bridge_3_8s`；`validation_metric = 2s_bounce / 3s_retention / 5s_completion / average_watch_time`。
- `已接入` `scripts/运营决策系统_operation_decision_system.py`：最新运营决策报告已包含 `copy_iteration_linkage`，`final_user_operation_result.md` 增加“文案迭代入口”。
- `已同步` `GPT数据源/05`、`11`、`13`、`14` 与 `codex_source/19`：新增 `copy_iteration_system_required`、`copy_version_record_missing`、`next_copy_revision_brief_required` 与 `copy_iteration_decision gate`。
- `验证`：`py_compile` passed；`文案迭代决策系统 --validate-only` passed；`运营决策系统 --validate-only` passed；JSON parse passed；status boundary assertions passed；forbidden status scan passed。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`；`current_data_goal_anchor` 未写 ready；未生成正式下一条视频执行 prompt。
- `日志`：`codex_log/20260516_copy_iteration_decision_system.md`
- `下一个安全用法`：ChatGPT 读取 `review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md` 后向用户汇报并改稿；用户确认后再进入具体改稿或后续执行。

## 20260516｜HyperFrames 最小卡片用户通过与视觉皮肤锁定

- `已确认` 用户已人工复审 `dist/hyperframes_minimal_validation/combined_preview.mp4` 并反馈可以通过；本轮只做最小卡片用户通过与 HyperFrames 小升级锁定回写，不生成正式视频，不修改已发布视频，不修改 `dist/latest_review_pack/`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = user_visual_review_lock + hyperframes_visual_skin_baseline_upgrade + minimal_artifact_style_preset_generation + project_file_change`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`。
- `impact_check_report（影响面检查）`：当前 root manifest 已写 `actual_output_type = real_hyperframes_motion`，review manifest 已写 `fallback_static_card = false`；旧正式事实中 “runtime 未发现 / 待验证” 口径已修正为“最小 runtime 通过，正式视频链路接入待验证”。
- `已锁定` `hyperframes_minimal_style_baseline = locked_for_judgment_and_summary_cards`，`judgment_card_motion_minimal_baseline = locked`，`summary_card_motion_minimal_baseline = locked`。
- `已锁定` allowed visual skins：`clean_soft（干净柔和）`、`cute_ai_guide（可爱 AI 向导）`。
- `未纳入` `sharp_judgment（清晰判断）`：不写入默认锁定皮肤，不生成默认预览，不作为判断卡 / 总结卡默认基线。
- `已升级` 可复跑脚本：`scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py` 支持 `--skin clean_soft`、`--skin cute_ai_guide`、`--all-locked-skins`。
- `已生成` skin 1 / skin 3 预览包：`dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/`、`dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/`、`dist/hyperframes_minimal_validation/visual_skins_1_3/combined_skin_review.mp4`。
- `已同步` `GPT数据源/08_当前正式事实.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`codex_source/21_codex_judgment_permission_matrix.md`、`codex_source/01_execution_rules.md`、root manifest 与 review manifest。
- `验证`：`npm run check` passed；HyperFrames lint / inspect / render 均有 exit_code=0 证据；7 个新 MP4 均为 1920x1080、30fps、h264、可解码、无音轨；root / skin manifests JSON parse 通过。
- `状态边界`：本轮仍为 `internal_diagnostic_only（内部诊断产物）`；未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、发布候选、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_hyperframes_minimal_card_visual_lock.md`
- `下一个目标`：后续真实视频执行中，把判断卡 / 总结卡的皮肤选择写进 `content_route_card V2.card_placement_decision`，并继续检查 locked copy 语义一致、字幕卡片不重叠、证据窗口不被打断和 HyperFrames runtime gate。

## 20260516｜HyperFrames 最小判断卡 / 总结卡产物验证

- `已确认` 本轮只做 `hyperframes_minimal_runtime_validation（HyperFrames 最小运行验证）`，产物定位为 `internal_diagnostic_only（内部诊断产物）`；不生成正式视频，不修改已发布视频，不修改 `dist/latest_review_pack/`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = hyperframes_runtime_validation + minimal_artifact_generation + card_motion_baseline_test`；`large_task_gate = false`；`lane = standard_lane`；`parallel = serial_only`。
- `impact_check_report（影响面检查）`：仓库根 `package.json` 只有 `ffmpeg-static`，本轮前 `scripts/` 未发现项目级 HyperFrames 入口，本地 `skills/` 不存在；已读取全局 HyperFrames skill 与 HyperFrames CLI skill。
- `HyperFrames runtime`：`npx --yes hyperframes@0.6.12` 可调用；`doctor` 显示 CLI、Chrome、FFmpeg、FFprobe 可用。内存低是渲染风险提示，但本轮用 draft / single worker 完成最小渲染。
- `已新增` 可复跑脚本：`scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py`。该脚本不读取 secret，不调用项目外部 API，通过 `npx --yes hyperframes@0.6.12 lint / inspect / render` 生成最小卡片验证产物。
- `已生成` `judgment_card（判断卡）`：`dist/hyperframes_minimal_validation/01_judgment_card/judgment_card.mp4`；锁定文字为 `AI 的正确用法：先判断，再执行`；`actual_output_type = real_hyperframes_motion`。
- `已生成` `summary_card（总结卡）`：`dist/hyperframes_minimal_validation/02_summary_card/summary_card.mp4`；锁定文字为 `目标说清楚，下一步能验证，就可以冲`；`actual_output_type = real_hyperframes_motion`。
- `已生成` 合并预览：`dist/hyperframes_minimal_validation/combined_preview.mp4`。
- `已生成` 审片与验证文件：`dist/hyperframes_minimal_validation/manifest.json`、`dist/hyperframes_minimal_validation/review_manifest.md`、两张卡片各自的 manifest、预览 PNG、HyperFrames lint / inspect / render 日志。
- `技术验证`：HyperFrames lint 通过；HyperFrames validate 通过且 no console errors / 70 text elements pass WCAG AA；HyperFrames inspect 通过且 0 layout issues；HyperFrames render 三段均 exit_code=0；`ffprobe / ffmpeg decode` 验证三段视频均为 1920x1080、30fps、h264、可解码，无音轨（本轮不要求音轨）。
- `状态边界`：`technical_runtime_validation = passed`、`hyperframes_minimal_artifact = generated`、`internal_diagnostic_only = true`；未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、可发布候选片待复审状态、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_hyperframes_minimal_card_validation.md`
- `下一个目标`：若要进入真实视频执行，需要把本轮 runtime adapter 接入正式视频执行链，并继续通过 `card_placement_decision`、`hyperframes_visual_quality_gate`、`subtitle_card_overlap_check` 和 locked copy 语义检查。

## 20260516｜Codex 判断权限表与 HyperFrames 判断卡 / 总结卡基线

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、项目文件修改、Codex 执行层判断权限补全和 HyperFrames 卡片执行基线补强；不生成视频、不修改已发布视频、不修改 `dist/latest_review_pack/`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + route_repair + project_file_change + codex_execution_permission_matrix + hyperframes_card_baseline_repair`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = explore_plus_integrate`；`write_owner = Codex Integrator only`。
- `state_action_router（项目状态动作总控器）`：推断 `codex_judgment_permission_matrix_needed`、`hyperframes_judgment_summary_card_baseline_needed`、`route_permission_boundary_repair_needed`；外部 Perplexity 资料只作参考，和仓库规则冲突时以仓库当前规则为准。
- `parallel_execution_report（并行执行报告）`：Lane A 只读整理 Codex 判断权限表；Lane B 只读核 HyperFrames 卡片基线与 runtime 状态；Integrator 单点写入。没有多个写手写同一文件。
- `已新增` `codex_source/21_codex_judgment_permission_matrix.md（Codex 判断权限表）`：明确 `must_decide_and_execute`、`must_decide_but_request_change`、`must_decide_and_block`、`must_escalate_to_chatgpt_or_user` 四层权限。
- `已覆盖` 判断对象：`opening_route_decision`、`card_placement_decision`、`judgment_card`、`summary_card`、`result_diff_card`、`boundary_card`、`prompt_tail_card`、`script_to_timeline_map`、`subtitle_segmentation`、`tts_prosody`、`material_evidence`、`visual_mismatch`、`aspect_ratio_resolution`、`publish_candidate_readiness`、`data_goal_alignment`、`copy_change_request`、`human_review_required`。
- `已修正` Perplexity 外部资料中不适合本项目的结论：Codex 在本项目必须通过 `content_route_inference_function（内容路由推理函数）` 判断 `opening_route_decision（开头路由判断）`；Codex 必须判断是否需要 `judgment_card（判断卡）` / `summary_card（总结卡）`，加与不加都必须说明依据。
- `已补强` `GPT数据源/05_文案路由规则.md`：`content_route_card V2` 与 `card_placement_decision` 已接入 `hyperframes_required / hyperframes_motion_type / hyperframes_runtime_status / hyperframes_visual_quality_gate / blocked_if_hyperframes_unavailable`，并新增 `judgment_card_motion（判断卡动效）`、`summary_card_motion（总结卡动效）` 和 `hyperframes_card_motion_baseline（HyperFrames 卡片动效基线）`。
- `已补强` `codex_source/01_execution_rules.md` 与 `codex_source/19_project_state_action_router.md`：新增 `codex_judgment_permission_gate（Codex 判断权限闸门）`、`hyperframes_card_motion_gate（HyperFrames 卡片动效闸门）`、`completion_truth_check（完成真实性检查）` 的 HyperFrames 检查项。
- `已同步` `GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`codex_source/00_codex_readme.md`：写清 HyperFrames 只能强化卡片动效和观感，不替代真实录屏证据、不改文案、不新增素材里没有的数据结论、不推进内容验证。
- `HyperFrames runtime`：当前 Codex 会话可读取 HyperFrames skill，但已检查仓库 `package.json` 与 `scripts/`，未发现项目级 HyperFrames plugin / script / runtime entry。当前只能写 `runtime_execution = 待验证`、`hyperframes_runtime_status = missing / not_found / not_verified`；后续真实视频若要求 HyperFrames 且仓库 runtime 仍不可用，必须 `blocked` 或等待用户授权降级。
- `DeepSeek`：已创建供料请求任务卡 `codex_log/supply_requests/20260516_codex_judgment_permission_and_hyperframes_baseline_pre_supply_request.json`；本轮因机制任务且禁止真实外部 API 调用，供料口径为 `fallback_local_only`，`not_deepseek_conclusion = true`。
- `已新增` fixture：`codex_source/fixtures/codex_judgment_permission_matrix_cases.json`，覆盖 opening route 修正、判断卡 HyperFrames runtime 缺失、总结卡不强插、文案修改请求和发布候选阻断。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`；`current_data_goal_anchor` 未写 ready；未生成视频、音频、图片。
- `日志`：`codex_log/20260516_codex_judgment_permission_and_hyperframes_baseline.md`
- `下一个目标`：后续真实视频执行前，先验证 HyperFrames runtime / plugin / script 是否存在；若 judgment_card / summary_card 被选中且 runtime 不可用，必须 blocked 或等待用户授权降级，不能普通静态卡片冒充 HyperFrames。

## 20260516｜运营决策系统完整修补

- `已确认` 本轮把《视频工厂》的数据目标锚点 / 数据飞轮 / 运营复盘修成可运行 `operation_decision_system（运营决策系统）`，不是只写概念。
- `已新增` 可运行脚本：`scripts/运营决策系统_operation_decision_system.py`。
- `已新增` schema / config：`review_loop/decision_engine/operation_decision_schema.json`、`threshold_config_stage_hypothesis.json`、`sample_classification_rules.json`。
- `已生成` 三期归纳报告：`review_loop/decision_engine/V001_V002_V003_operation_synthesis_report.json` 与 `.md`。
- `已生成` 最新运营决策报告：`review_loop/decision_engine/latest_operation_decision_report.json` 与 `.md`。
- `已生成` 用户最终只读报告：`review_loop/decision_engine/final_user_operation_result.md`。
- `已生成` V003 单条判断：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_operation_decision_result.json` 与 `.md`。
- `records_processed`: V001 = `historical_operation_record`；V002 = `policy_limited_abnormal_operation_sample`；V003 = `current_operation_target`。
- `已回审修正`：V003 仍是当前目标样本，但在 `interim_36h_snapshot` 和关键字段缺失阶段，`normal_attribution_eligible = false`；必须等 72h / 7d 与需求侧字段补齐后才能进入正式归因。
- `current_decision`: V003 仍缺 72h / 7d、3s 留存、主页访问、私信、有效私信、有效咨询和清晰需求客户，下一期正式执行为 `blocked_for_formal_next_episode_execution`；只允许低置信度准备开头 / 前 5 秒方向草稿。
- `DeepSeek`: 已通过 `review_loop/decision_engine/operation_decision_system_supply_request.json` 执行只读供料；`deepseek_actual_participation = deepseek_passed`，`api_key_printed = false`，`api_key_written = false`。
- `已同步` `GPT数据源/13`、`14`、`11`、`08` 与 `codex_source/19`：运营判断层必须先有 `operation_decision_system` 最终报告。
- `提交前验证`：`py_compile`、脚本重跑、`--validate-only`、JSON parse、三期分类断言、forbidden status scan 均通过。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`；`current_data_goal_anchor` 未写 ready；未生成正式下一条视频执行 prompt。
- `日志`：`codex_log/20260516_operation_decision_system_full_repair.md`
- `下一个目标`：补齐 V003 72h / 7d 与需求侧字段后，重跑运营决策系统，再决定唯一主变量和下一期是否可进入正式执行。

## 20260516｜锁定文案契约与逐句画面对齐闸门修补

- `已确认` 本轮根据用户反馈修正视频执行机制，不修改已发布视频，不重新生成视频，不回炉当前片子。
- `已新增` `locked_copy_contract（锁定文案契约）`：视频执行前必须锁定 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。
- `已新增` `codex_copy_authority_boundary（Codex 文案权限边界）`：Codex 是执行层，不得擅自改标题、选题、开头句、核心判断、人味表达或视觉标题卡标题；如需改文案必须输出 `copy_change_request（文案修改请求）` 或 blocked。
- `已补强` `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）`：`script_to_timeline_map` 必须按 `line_group` 逐句绑定口播、素材时间码、预期画面、禁用画面、字幕、卡片和证据强度；只有段落级映射不得进入视频导出。
- `已新增` `subtitle_card_overlap_check（字幕卡片重叠检查）`：导出前必须检查口播字幕、标题卡、解释卡、总结卡、画面 OCR 和关键证据区域；high severity overlap 未修复必须 blocked。
- `已新增` `post_publish_no_rework_boundary（已发布视频不默认回炉边界）`：用户明确说视频已经发了 / 已发布时，当前视频只作为运营样本继续等待数据反馈；机制问题修机制和下一轮执行规则，不默认修已发布片。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_copy_lock_and_visual_alignment_gate_repair.md`
- `下一个目标`：已发布视频继续等待数据反馈；以后新视频执行前必须先锁定文案契约，并完成逐句文案画面对齐与字幕卡片重叠检查。

## 20260516｜正式运营用户反馈边界与禁止降级完成

- `已确认` 本轮根据用户反馈修正正式运营协作分工：用户只负责目标修正、页面 / 美观 / 观感对标和结果是否合格反馈。
- `已确认` GPT / Codex 负责内部执行问题自查与修复；当用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，必须触发 `self_repair_audit（自修审计）`，不得要求用户诊断内部原因。
- `已确认` Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能冒充 `completed`。
- `已确认` 降级方案只能作为 `blocked` 后待用户确认的修复建议；用户明确授权前，任务状态必须是 `blocked`，不是 `completed`。
- `已同步` `no_degrade_completion_gate（禁止降级完成闸门）`、`fallback_requires_user_authorization（降级需要用户授权）`、`self_repair_audit（自修审计）` 与 `completion_truth_check（完成真实性检查）` 到 AGENTS、Codex 执行规则、状态动作总控器、当前正式事实、OPC 协作机制和数据目标执行总线。
- `DeepSeek`：已创建供料任务卡 `codex_log/supply_requests/20260516_用户反馈边界与禁止降级完成_pre_supply_request.json`；本轮未调用外部 API，因本轮是机制修补且禁止额外 API 调用，供料口径为 `fallback_local_only`，`not_deepseek_conclusion = true`，不得写成 DeepSeek 结论。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_user_feedback_boundary_and_no_degrade_completion.md`
- `下一个目标`：后续用户只反馈目标、美观和结果是否合格；GPT / Codex 必须自行复盘内部执行问题，实打实完成仓库基线，做不到就 blocked，不得降级完成。

## 20260516｜第二期横屏 16:9 可发布候选片生成

- `已确认` 用户最新拍板后，本轮把正式运营默认出片比例修正为 `horizontal_16_9（横屏 16:9）` / `1920x1080`；旧 `vertical_9_16（竖屏 9:16）` 只保留为历史或用户明确指定的特殊策略，不再作为默认发布候选片比例。
- `已生成` 第二期横屏可发布候选片：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/第二期_KPI到判断系统_horizontal_publish_candidate_v1.mp4`。
- `publish_candidate_status`：`publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`。
- `媒体硬核验`：`1920x1080`、`display_aspect_ratio = 16:9`、`sample_aspect_ratio = 1:1`、`rotation = none`、`fps = 30/1`、`audio_codec = aac`、`audio_duration = 81.920000s`、`subtitle_stream = mov_text / chi`、`can_decode = true`。
- `TTS`：使用项目正式阿里 / 百炼链路，`provider = aliyun_bailian`、`api_route_family = aliyun_qwen_realtime_websocket_voice_clone`、`model = qwen3-tts-vc-realtime-2026-01-15`、`voice = qwen-t...ac19（脱敏）`；`local_say_fallback_used = false`、`api_key_printed = false`、`api_key_written = false`。
- `字幕`：已生成并嵌入 `mov_text` 字幕轨，同时保留 `subtitle.ass` 与 `subtitle.srt` sidecar。
- `卡片`：开头冲突卡与结尾判断卡已作为主视频片段写入；结尾判断卡保留“播放是入口 / 收藏是认可 / 私信要评分 / 每条只改一个变量”。
- `数据目标对齐`：服务当前候选主变量 `opening_route_or_first_5s_packaging`；协同变量仅限 `evidence_compression` 与 `result_diff_display`；`formal_data_driven_execution_ready = false`，未声称数据飞轮真实跑通。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_second_episode_horizontal_publish_candidate.md`
- `下一个目标`：ChatGPT / 用户复审 horizontal 16:9 publish candidate，判断是否能进入 `send_ready` 或需要局部回炉。

## 20260516｜正式运营交付基线修正：禁止技术预览冒充交付

- `已确认` 本轮根据用户反馈修正《视频工厂》正式运营交付口径：进入 `formal_operation_active（正式运营中）` 后，视频交付任务默认只接受 `publish_candidate（可发布候选片）` 或 `blocked（阻断）`。
- `已确认` `technical_preview（技术预览）`、`technical_preview_candidate（技术预览候选）`、`preflight package（执行前补全包）`、`silent preview（无声预览）`、无音轨视频、横屏技术包、只交 JSON / Markdown / route card，均只能作为 `internal_diagnostic_only（内部诊断产物）` 或 `historical_internal_diagnostic_only（历史内部诊断产物）`，不得写成用户交付物、阶段完成、内容推进或视频执行完成。
- `已确认` 已补强 `delivery_baseline_gate（交付基线闸门）`、`publish_candidate_required（可发布候选片必需）`、`technical_preview_not_delivery（技术预览不是交付）`、`blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）` 和 `formal_operation_delivery_blocked（正式运营交付阻断）`。
- `已确认` `content_route_card / script_to_timeline_map / tts_prosody_anchor_map / editing_decision_pack / assembly_decision_pack / data_goal_alignment_check` 只属于执行前必备条件，不是正式运营视频交付物。
- `historical_internal_diagnostic_only`：上一轮第二期 82 秒、1280x720、15fps、无音轨本地技术预览只保留为历史内部诊断证据；它不是当前交付物，不能作为以后视频交付样板。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260516_formal_operation_delivery_baseline_repair.md`
- `下一个目标`：重新判断第二期视频链路是否能生成真正 `publish_candidate（可发布候选片）`；若不能，必须返回 `blocked_publish_candidate_unavailable`，而不是再生成 `technical_preview（技术预览）`。

## 20260516｜第二期候选视频《从 KPI 到判断系统》执行前补全（historical_internal_diagnostic_only）

- `historical_internal_diagnostic_only` 本轮基于第二期素材审计报告和用户锁定选题，生成候选执行包与本地技术预览 / 审片包；该记录只保留历史内部诊断价值。
- `content_id`：`second_episode_kpi_to_judgment_system`。
- `选题`：别再让 AI 给你 KPI 了，它真正该帮你判断下一步改哪。
- `审片包目录`：`dist/第二期KPI到判断系统预览_second_episode_kpi_to_judgment_system_preview/`。
- `已生成但不作为交付`：`content_route_card V2`、候选口播稿 v1、`script_anchor_extraction_function` 输出、`script_to_timeline_map`、`tts_prosody_anchor_map`、`opening_visual_hook_spec`、`editing_decision_pack`、`assembly_decision_pack`、`data_goal_alignment_check`、`review_manifest.md` 和本地 `技术预览_preview.mp4`。这些只属于历史执行前补全 / 内部诊断证据，不是正式运营视频交付物。
- `技术预览_not_delivery`：82 秒，1280x720，15fps，H.264，无音轨，可解码；只用于历史内部诊断，不是发布成片，不是 `publish_candidate`。
- `素材复核`：两个源视频均存在、可解码、无音轨；素材不包含真实平台后台数据，不包含真实有效客资 / 成交；video_2 的 `video_goal_card` 只录到模板开头。
- `数据目标对齐`：服务当前候选主变量 `opening_route_or_first_5s_packaging`，协同变量仅限 `evidence_compression` 和 `result_diff_display`；`formal_data_driven_execution_ready = false`。
- `DeepSeek`：本轮未调用 DeepSeek；因未授权外部 API，供料口径为 `fallback_local_only`，不得写成 DeepSeek 结论。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：本轮不是正式下一条视频执行完成，不是数据飞轮已跑通，不是 V003 72h / 7d 复盘完成，不是可发送状态，不是当前正式运营交付物。
- `日志`：`codex_log/20260516_second_episode_kpi_to_judgment_system_preflight.md`
- `下一个目标`：本条历史诊断记录不再作为交付路线；后续必须先判断能否生成真正 `publish_candidate`，不能则 blocked。

## 20260515｜第二期素材审计报告回流

- `已确认` 本轮只补交上一轮已生成的第二期素材审计报告到 GitHub `main`，不重新审计素材，不重新分析视频。
- `报告路径`：`codex_log/material_audit/20260515_second_episode_material_detail_report.md`。
- `素材目录`：`/Users/fan/Documents/视频工厂/素材录制/第二期`。
- `视频数量`：2。
- `轻量副产物`：`dist/material_audit/second_episode/` 中的 OCR 原始表、contact sheet 与轻量副产物清单；原始视频和逐帧截图不纳入 Git。
- `报告用途`：给 ChatGPT 做选题方向、开头路线、是否补录、是否进入正式文案准备的判断依据。
- `DeepSeek`：本轮未调用 DeepSeek，报告不写 DeepSeek 结论。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：素材审计报告回流不等于内容通过，不等于数据飞轮已跑通，不等于下一条正式视频执行 prompt 已生成。
- `日志`：`codex_log/20260515_second_episode_material_audit.md`
- `下一个目标`：ChatGPT 读取 GitHub 上的第二期素材审计报告，判断素材是否足够支撑下一条候选内容、应走哪种开头路线、是否需要补录，以及是否可以进入正式文案准备。

## 20260515｜正式运营阶段迁移与三期运营记录统一

- `已确认` 本轮把《视频工厂》当前项目阶段从 `gray_test（灰度测试）` 当前口径迁移为 `formal_operation_active（正式运营中）`，运营方式写为 `data_driven_operation_iteration（数据驱动运营迭代）`。
- `已确认` 后续截图、评论、私信、咨询和平台数据默认走 `operation_data_intake（运营数据录入）`；复盘走 `operation_review（运营复盘）`；下一轮变量判断走 `operation_next_variable_decision（运营下一变量判断）`。
- `已新增` `codex_log/current_operation_target.md` 作为当前 canonical 运营入口。
- `已更新` `codex_log/current_gray_test_target.md`，降级为 `legacy_compatibility_pointer（历史兼容指针）`。
- `已新增` `review_loop/operation_records_index.md`，统一纳入 V001 / V002 / V003 三期运营记录。
- `records_inventory`：V001 = `historical_operation_record`；V002 = `policy_limited_abnormal_operation_sample`；V003 = `current_operation_target`。
- `已更新` `codex_log/current_data_goal_anchor.md`：当前阶段为 `formal_operation_active`，当前运营目标为 V003，`anchor_instance_status` 仍为 `partial_data_recorded`，不得写 `ready`。
- `DeepSeek`：执行前供料和后置风险复核均为 `deepseek_passed`，`fallback_count = 0`，`blocked_count = 0`，DeepSeek 只读参与，不写文件、不拍板项目事实。
- `已同步` GPT 数据源、Codex 执行规则、DeepSeek schema / fixture、review_loop 入口和三期记录身份。
- `已生成` GPT Project 静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_formal_operation_stage/`。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：正式运营不等于内容成功、商业验证成立、数据飞轮跑通、多 agent runtime 长期稳定或当前数据目标锚点 ready。
- `日志`：`codex_log/20260515_formal_operation_stage_migration.md`
- `下一个目标`：补齐 V003 72h / 7d 数据和需求侧字段后，进入 `operation_review`，只判断下一轮唯一运营变量。

## 20260515｜最新一期视频 V003 早期数据录入与当前数据锚点更新

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的最新一期视频数据截图录入、截图证据归档、当前灰度目标切换、当前数据目标锚点更新、DeepSeek 只读供料 / 风险复核、日志和 GPT Project 静态包同步；不做最终内容复盘，不生成正式下一条视频执行 prompt。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = gray_test_data_intake + project_file_change + data_goal_anchor_update + deepseek_supply_required + gpt_project_static_package_sync`；`large_task_gate = triggered`；`lane = serial_only`。
- `state_action_router（项目状态动作总控器）`：推断 `gray_test_data_intake`、`current_video_target_switch_needed`、`current_data_goal_anchor_update_needed`、`deepseek_supply_required`；动作是先判定视频身份，再新建 / 合并记录、归档截图、更新锚点与日志。
- `视频身份判断`：截图标题为 `以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件`；与 V001《我用 AI 做 PPT 踩过的坑》不一致；V002 已存在且为《自动流的最简单流程》平台审核减推异常样本；因此本轮创建 `V003`，不覆盖 V001 / V002。
- `已新增` V003 记录目录：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/`。
- `已新增` V003 截图证据目录：`review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/`；已归档总览、流量分析、观众分析 3 张截图并建立 `V003_截图清单_screenshot_manifest.md`。
- `观察窗口`：截图文件时间约 `2026-05-15 18:19-18:21`，可见发布时间 `2026-05-14 04:50`，推断约发布后 37 小时；记录为 `between_24h_and_72h / interim_36h_snapshot`，不得写成 72h final 或 7d 封账。
- `已回填核心字段`：播放量 141、平均观看 21 秒、封面点击率 0.00%、2s 跳出率 50.00%、平均播放占比 8.51%、完播率 4.17%、5s 完播率 28.13%、点赞 2、收藏 3、评论 0、分享 0、弹幕 0、涨粉 1、推荐页 97.2%。
- `早期诊断草稿`：`traffic_layer = draft_low_confidence / weak`；`opening_retention = draft_low_confidence / weak`；`content_value_signal = draft_low_confidence / small_positive_signal`；`interaction_signal = draft_low_confidence / weak`；`lead_signal = missing`。
- `当前数据锚点`：`codex_log/current_data_goal_anchor.md` 已从 `waiting_data` 更新为 `partial_data_recorded`；`data_confidence = low`；主短板草稿为 `opening_retention_and_initial_distribution_weak`；候选主变量草稿为 `opening_route_or_first_5s_packaging`；未写 `ready`。
- `DeepSeek 执行前供料`：`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`fallback_count = 0`、`blocked_count = 0`；DeepSeek 只读参与，不写文件、不拍板最终复盘。
- `缺失字段`：`3s_retention`、`profile_visit_count`、`dm_count`、`effective_dm_count`、`effective_consult_count`、`72h_final_data`、`7d_final_data` 仍为 `missing`。
- `待人工确认字段`：平台完整观察窗口、年龄分布柱状图估读、观看趋势曲线精确点位标为 `uncertain_need_human_check`。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260515_latest_video_data_intake.md`
- `下一个目标`：V003 继续收集 72h / 7d 数据；补齐 3s 留存、主页访问、私信、有效咨询后，再进入正式发布后复盘。

## 20260515｜DeepSeek runtime provider 项目级接入与多任务真实供料验证

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 DeepSeek 运行时供应商接入、脚本 / schema / fixture / 执行规则 / 日志 / GPT Project 静态包同步；未生成视频、音频、图片，未调用 TTS / 图片 / 视频 API，未修改 `dist/latest_review_pack/`。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = code_execution_or_debug + mechanism_or_route_fix + execution_architecture_rewire + field_and_function_landing + provider_runtime_integration + gpt_project_static_package_sync`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = explore_plus_integrate`。
- `state_action_router（项目状态动作总控器）`：推断 `deepseek_provider_runtime_required`、`deepseek_runtime_provider_ready`、`deepseek_multi_task_supply_required`、`deepseek_multi_task_supply_passed`；动作是接入 provider、doctor、自检、单任务 / 多任务真实供料、无 key 泄露检查和同步回写。
- `root_cause（根因）`：旧链路把真实参与绑定到当前 Codex 进程是否已有 `DEEPSEEK_API_KEY`；live smoke test 可通过，但普通任务会因 process env 缺 key 反复 `blocked_missing_process_env_api_key`。
- `已新增` `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`：加载顺序为 `process_env -> .env.local -> .env -> 本地运行配置_local_runtime/deepseek_runtime_authorization.local.json`；只允许 `DEEPSEEK_API_KEY`；只注入子进程 env；不打印、不写出 key。
- `已新增` `scripts/DeepSeek运行环境自检_deepseek_runtime_doctor.py`、`scripts/DeepSeek多任务供料运行器_deepseek_multi_task_supply_runner.py`、`scripts/DeepSeek环境安装器_deepseek_runtime_setup.py` 和 `本地运行配置_local_runtime/DeepSeek运行时授权说明_DEEPSEEK_RUNTIME_AUTH.md`。
- `已更新` safe runner / controller / explorer：safe runner 默认调用 runtime provider；controller 支持 provider 状态、真实参与必需和 fallback 不完成；explorer 不直接读取 `.env`，只接收子进程 env；真实 API 返回格式漂移时由 Codex 规整为四字段只读供料包。
- `runtime_doctor（运行环境自检）`：`status = ready`、`key_found = true`、`key_source = project_env`、`key_git_tracked = false`、`can_inject_child_process = true`、`can_call_deepseek = true`、`leak_found = false`。
- `single request DeepSeek validation`：`deepseek_runtime_validation_task_A_file_map` 已真实调用通过；`deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。
- `multi-task DeepSeek validation`：最终 combined report 为 `total_requests = 3`、`deepseek_passed_count = 3`、`fallback_count = 0`、`blocked_count = 0`、`all_outputs_exist = true`。
- `已生成` 验证产物：`dist/deepseek_runtime_validation/runtime_doctor_report.json`、`latest_combined_participation_report.json`、`latest_combined_participation_report.md`，以及 A/B/C 三个任务各自的 `latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json`、`participation_report.json`。
- `已同步` GPT / Codex 规则：`GPT数据源/08`、`09`、`10_OPC`、`11_项目状态动作总控器`、`codex_source/00`、`01`、`17`、`18`、schema 与 runtime provider fixture 均已更新。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_deepseek_runtime_provider/`。
- `已更新` `codex_log/current_local_artifact_paths.md`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向本轮 DeepSeek runtime provider 包；上一版 current data goal anchor 包降级为 previous / historical。
- `secret_policy（密钥策略）`：key 来源只记录为 `.env` 文件名；key 值未打印、未写入、未提交；`.env`、`.env.local`、`.env.*`、`.env.swp` 与本地 runtime 授权实际值文件已受 ignore 保护。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：`deepseek_api_capability = 已确认`；`deepseek_runtime_provider = 已确认`；`multi_task_supply_stability = 已确认本地三任务技术验证通过 / 待验证长期多轮真实项目任务`；`multi_agent_runtime_stability = 待验证`。
- `日志`：`codex_log/20260515_deepseek_runtime_provider_integration.md`
- `下一个目标`：后续每个需要 DeepSeek 的 Codex 任务默认走 runtime provider；若 provider not ready，进入一次性 runtime setup；若用户要求 DeepSeek 必须参与而真实调用未通过，则整体任务 blocked。

## 20260515｜当前数据目标锚点实例入口补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的当前实例锚点入口、机制接线、DeepSeek schema / fixture、日志和 GPT Project 静态包同步；未生成视频、音频、图片，未调用 TTS / 图片 / 视频 API，未修改 `dist/latest_review_pack/`，未读取 `.env` / `.env.*` / `.env.swp` / API key / token / secret。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + field_and_function_landing + gpt_project_static_package_sync`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`。
- `state_action_router（项目状态动作总控器）`：推断 `current_data_goal_anchor_required`、`current_data_goal_anchor_missing`、`current_data_goal_anchor_waiting_data_expected`；动作是新增当前实例锚点，并同步 13 / 14 / GPT 入口 / Codex 规则 / DeepSeek request / schema / fixture。
- `缺口审计`：`13_目标驱动数据飞轮与文案执行闭环` 已负责目标飞轮、阈值和文案闸门；`14_数据目标执行总线` 已负责抽象执行总线；缺的是当前这一条 / 下一条视频实际使用的稳定锚点实例入口。
- `已新增` `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`，作为当前实例卡；它不替代 `13`，不替代 `14`，只存当前这一条 / 下一条视频实际使用的 `data_goal_anchor` 实例。
- `当前锚点状态`：`anchor_instance_status = waiting_data`、`data_confidence = low`、`human_review_required = true`。由于当前 v3.1 灰度测试 24h / 72h / 7d 数据未回填，不得写成 `ready`。
- `已接入` 当前锚点实例路径：`GPT数据源/13`、`14`、`01`、`03`、`05`、`07`、`08`、`09`、`10`、`11`，以及 `codex_source/00`、`01`、`17`、`18`、`19`。
- `已补强` `content_route_card V2`、`script_to_timeline_map`、`editing_decision_pack`、`assembly_decision_pack` 和 `data_goal_alignment_check`：都必须回指 `codex_log/current_data_goal_anchor.md`，并读取 `current_data_goal_anchor_status`。
- `已更新` DeepSeek schema / fixture：`codex_source/schemas/deepseek_supply_request.schema.json`、`codex_source/18_deepseek_supply_request_schema.md`、`codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json` 已支持 `current_data_goal_anchor_path` 与 `current_data_goal_anchor_status`；`mechanism_inference_function_cases.json` 新增 missing / waiting_data / ready / alignment_check_missing 4 个 case。
- `本轮 DeepSeek 供料结果`：已创建并尝试执行 `codex_log/supply_requests/20260515_current_data_goal_anchor_pre_supply_request.json`；当前进程 `process_env_key_present = false`，safe runner 返回 `blocked_missing_process_env_api_key`；`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`；不得写成 DeepSeek 结论。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_current_data_goal_anchor/`。
- `已更新` `codex_log/current_local_artifact_paths.md`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向本轮 current data goal anchor 包；上一版 `deepseek_safe_loader_data_goal_anchor` 包降级为 previous / historical。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：当前锚点机制和实例入口已写入；当前实例不是 ready；真实视频任务是否稳定使用该锚点仍为 `待验证`；数据飞轮真实效果仍为 `待验证`；不声明 `multi-agent runtime（多 agent 运行时）` 已稳定跑通。
- `日志`：`codex_log/20260515_current_data_goal_anchor_instance.md`
- `下一个目标`：下一条真实视频执行前，先用发布后复盘数据把 `codex_log/current_data_goal_anchor.md` 补齐为 `ready` 或明确 `blocked`，再允许 Codex 进入正式数据驱动视频执行。

## 20260515｜DeepSeek 安全加载与 data_goal_anchor 执行链双修补

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、脚本 / schema / fixture / 执行规则 / 日志 / GPT Project 静态包同步；未生成视频、音频、图片，未调用 TTS / 图片 / 视频 API，未修改 `dist/latest_review_pack/`，未读取 `.env` / `.env.*` / `.env.swp` / API key / token / secret。
- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + field_and_function_landing + gpt_project_static_package_sync`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = explore_plus_integrate`。
- `parallel_execution_report（并行执行报告）`：Explorer A 只读审计 DeepSeek safe loader / process env / supply gate；Explorer B 只读审计 `data_goal_anchor` / 13 / 14 / execution rules / editing / assembly / alignment check；Integrator 单点写入。由于核心文件重叠，本轮不是 `true_multi_task_parallel`。
- `DeepSeek root_cause（根因）`：DeepSeek live smoke test 通过依赖用户授权范围内 safe loader 把 key 临时注入测试子进程；普通每轮 Codex 任务进程不一定带 `DEEPSEEK_API_KEY`。
- `已写入` 每轮安全加载策略：真实 DeepSeek 供料默认优先 `process_env_only`；controller / explorer 不直接读取 `.env`；若需要 `.env` key，必须有本轮明确授权的 wrapper / loader，只注入子进程；无法安全加载则 `blocked_missing_process_env_api_key`。
- `已新增` `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py`，作为 process-env-only 的安全供料入口；它只检查 `DEEPSEEK_API_KEY` 是否存在，不打印、不写出、不提交 key，并强制 `DEEPSEEK_DISABLE_ENV_FILE=1`。
- `已更新` `scripts/deepseek_supply_controller.py`：补齐 `requires_real_deepseek_participation`、`safe_loader_policy`、`process_env_key_present`、`blocked_missing_process_env_api_key`、`blocked_process_env_key_not_allowed`、`fallback_local_only` 边界，避免把本地兜底写成 DeepSeek 真实参与。
- `已更新` DeepSeek 协议 / schema / fixture：`codex_source/17_deepseek_supply_controller_protocol.md`、`18_deepseek_supply_request_schema.md`、`codex_source/schemas/deepseek_supply_request.schema.json`、`codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json`，并新增 `DeepSeek安全加载阻断_deepseek_safe_loader_blocked_missing_process_env_example.json`。
- `本轮 DeepSeek 供料结果`：当前进程 `process_env_key_present = false`；pre-supply request 经 safe runner 返回 `blocked_missing_process_env_api_key`；`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`；不得写成 DeepSeek 已参与。
- `data_goal_anchor 执行链`：已补强 `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`、`GPT数据源/05_文案路由规则.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`，要求 `content_route_card V2`、`script_to_timeline_map`、`editing_decision_pack`、`assembly_decision_pack` 和最终 `data_goal_alignment_check` 全部承接 `data_goal_anchor`。
- `已补齐` `forbidden_goal_field_alias_map`：`forbidden_variables_avoided`、`forbidden_visuals_by_goal`、`forbidden_variable_avoided`、`no_forbidden_variable_introduced` 可作为不同对象字段名，但必须回指同一组 `data_goal_anchor.forbidden_variables`。
- `已更新` `codex_source/fixtures/mechanism_inference_function_cases.json`：新增 / 校正 data_goal_anchor 相关 case，覆盖 content route 正常路径、script_to_timeline 缺主短板 blocked、forbidden alias 一致性、alignment check 缺失 blocked、editing 主变量支持失败 blocked、assembly 缺指标 blocked；全量 fixture basic validation 已通过。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_deepseek_safe_loader_data_goal_anchor/`。
- `已更新` `codex_log/current_local_artifact_paths.md`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向本轮 DeepSeek safe loader + data_goal_anchor 包；上一版 `data_goal_execution_bus` 包降级为 previous / historical。
- `验证摘要`：JSON parse passed；Python syntax check passed；fixture basic validation passed；safe runner blocked-path validation passed；keyword check passed；`jsonschema` 本地包不可用，完整 JSON schema 校验记录为 `not_tested_full_jsonschema_validation_unavailable`。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：机制已落库；真实任务稳定性仍为 `待验证`；本轮 DeepSeek 真实参与为 `blocked_missing_process_env_api_key`，不是 `deepseek_passed`；不声明 `multi-agent runtime（多 agent 运行时）` 已稳定跑通。
- `日志`：`codex_log/20260515_deepseek_safe_loader_and_data_goal_anchor_dual_completion.md`
- `下一个目标`：下一条真实视频执行前，使用 `data_goal_anchor` 锁定目标，并用 process-env-only DeepSeek supply gate 或明确 blocked 结果作为前置验收；Codex 完成前必须输出 `data_goal_alignment_check`。

## 20260515｜数据目标执行总线双重补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、执行架构重接线、DeepSeek 供料字段、schema、fixture、日志和 GPT Project 静态包同步，不生成视频、不生成音频、不生成图片，不调用 TTS / 阿里 / 豆包生成 API，不读取 `.env` / `.env.swp` / API key / token / secret，不修改 `dist/latest_review_pack/`。
- `审计结论`：`13_目标驱动数据飞轮与文案执行闭环` 已定义目标飞轮、阈值、文案闸门、内容结构反馈、单主变量和 `next_video_execution_prompt`，但未承担全执行链总线职责；本轮采用 `both`：补强 13，同时新增 14。
- `已新增` `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`，定义 `data_goal_anchor`、`data_goal_execution_bus`、`bridge_to_copy`、`bridge_to_deepseek`、`bridge_to_codex_execution`、`bridge_to_editing_and_assembly` 和 `data_goal_alignment_check`。
- `核心原则`：`目标锁死，结构可变`。Codex 可调整 segment 拆分、剪辑节奏、画面顺序、卡片位置、API 图是否需要、PPT 密度、TTS 分句和装配顺序；降级方案只能作为 blocked 后待用户授权的修复建议，不能作为完成结果。不得调整当前阶段目标、主短板、主变量、禁止变量、成功 / 失败 / 发布后验证指标。
- `已同步` GPT Project / ChatGPT 侧入口：`GPT数据源/01_项目系统提示词.md`、`03_总索引与阅读顺序.md`、`05_文案路由规则.md`、`07_AI知识类视频价值规则.md`、`08_当前正式事实.md`、`09_目标态计划.md`、`10_OPC一人公司闭环与多AI协作机制.md`、`11_项目状态动作总控器_机制推理层.md`、`13_目标驱动数据飞轮与文案执行闭环...md`。
- `已同步` Codex 执行侧入口：`codex_source/00_codex_readme.md`、`01_execution_rules.md`、`17_deepseek_supply_controller_protocol.md`、`18_deepseek_supply_request_schema.md`、`19_project_state_action_router.md`、`scripts/deepseek_supply_controller.py`。
- `已更新` schema / fixture：`codex_source/schemas/deepseek_supply_request.schema.json` 增加数据目标字段；`codex_source/fixtures/mechanism_inference_function_cases.json` 新增 5 个数据目标锚点 case；新增 `codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json`。
- `DeepSeek 供料闸门`：本轮已创建并尝试执行 `codex_log/supply_requests/20260515_数据目标执行总线_data_goal_execution_bus_pre_supply_request.json`；当前进程 `process_env_key_present = false`，controller 输出 `blocked_missing_process_env_api_key`，`env_file_read = false`，`api_key_printed = false`，`api_key_written = false`，不得写成 DeepSeek 结论。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_goal_execution_bus/`。
- `已更新` `codex_log/current_local_artifact_paths.md`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向本轮数据目标执行总线包；上一版 mandatory DeepSeek 包降级为 previous / historical。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：数据目标执行总线机制已写入；真实任务中是否稳定把剪辑 / 编排 / 供料锚定到数据目标仍为 `待验证`。本轮不代表数据飞轮真实跑通，也不代表 multi-agent runtime 稳定跑通。
- `日志`：`codex_log/20260515_data_goal_execution_bus.md`
- `下一个目标`：下一条真实视频执行前，ChatGPT / Codex / DeepSeek 都必须先读取 `data_goal_anchor`，并在 Codex 完成前输出 `data_goal_alignment_check`。

## 20260515｜DeepSeek 真实参与活体测试

- `测试结果`：`passed`。本轮已从上一轮 `blocked_missing_process_env_api_key` 升级验证为 `deepseek_passed`。
- `allowed_key_lookup_result（允许范围 key 查找结果）`：当前 Codex 进程初始 `PROCESS_ENV_KEY_PRESENT = false`；用户授权范围内发现 key 声明，`key_source = .env`。本轮没有全盘搜索，没有搜索 Desktop / Downloads / 浏览器缓存 / keychain / Git 历史 / 无关项目目录。
- `安全加载结果`：runner 只把 key 加载到当前测试子进程环境；`key_value_printed = false`、`key_value_written = false`、`.env_staged = false`、`.env.local_staged = false`、shell 配置未 staged。
- `controller / explorer 安全结果`：`env_file_read = false`、`process_env_key_present = true`、`safe_call_mode = process_env_only`、`api_key_printed = false`、`api_key_written = false`。
- `deepseek_actual_participation`：`deepseek_passed`。
- `supply_source`：`deepseek_passed`；`fallback_status = not_used`；`not_deepseek_conclusion = false`。
- `api_validation / context_pack_validation`：DeepSeek readonly explorer 输出 `api_validation = passed`、`context_pack_validation = passed`。
- `token_usage_expectation_check`：`token_usage_expected = true`、`token_usage_should_decrease = true`、`token_usage_observed_or_user_check_required = token_decrement_expected`。controller 输出未暴露 token delta，因此仍建议用户去 DeepSeek 控制台核对 token 是否减少。
- `供料输出`：`dist/deepseek_supply_controller/live_smoke_test_20260515/latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json` 已生成；`dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md` 记录 explorer 侧 `api_validation = passed`。
- `未生成`：未创建 GPT Project 上传包，未把本轮写成 multi-agent runtime 已跑通。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `日志`：`codex_log/20260515_deepseek_live_participation_smoke_test.md`
- `下一个目标`：用户到 DeepSeek 控制台核对本次调用后的 token / usage 是否减少；后续真实 Codex 任务继续默认进入 `deepseek_supply_gate（DeepSeek 供料闸门）`，并仍由 Codex 负责整合、验证和回写。

## 20260515｜强制 DeepSeek 供料循环与 Codex 二次补全机制落地

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、执行规则修改、脚本字段、schema、fixture、日志和 GPT Project 静态包同步，不生成视频、不生成音频、不生成图片，不读取 `.env` / `.env.swp` / API key / token / secret，不修改 `dist/latest_review_pack/`。
- `已写入` `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：每轮 Codex 任务默认先进入 `deepseek_supply_gate（DeepSeek 供料闸门）`，创建 `supply_request（供料请求任务卡）`，尝试执行前 DeepSeek 供料，Codex 执行后再做 DeepSeek 风险复核。
- `已写入` DeepSeek 从 `if_needed_trigger（按需触发）` 升级为 `mandatory_by_default（默认强制）`；Codex 不得凭主观判断跳过 DeepSeek。
- `已写入` `deepseek_participation_report（DeepSeek 参与报告）` 与 `token_usage_expectation_check（token 使用预期检查）` 为最终回报必需字段。
- `已写入` `fallback_local_only（本地兜底）` 不得写成 DeepSeek 结论；token 未观察到减少时，不得写 DeepSeek 已深度参与。
- `已写入` Codex 二次补全责任：必须自动补齐受影响文件、字段、脚本、schema、fixture、日志、路径索引和 GPT Project 静态上传包；只写协议或单文件不得写完成。
- `已更新` DeepSeek controller / explorer 脚本：`scripts/deepseek_supply_controller.py` 新增 `deepseek_supply_gate`、`deepseek_participation_report`、`token_usage_expectation_check`、`post_risk_review`；`scripts/deepseek_readonly_explorer.py` 补齐 `safe_call_mode` 和 `deepseek_actual_participation`。
- `已更新` schema：`codex_source/schemas/deepseek_supply_request.schema.json` 新增强制供料字段，并加入 `mandatory_pre_supply`、`mandatory_post_risk_review`。
- `已新增` fixture：`codex_source/fixtures/DeepSeek强制供料循环_mandatory_supply_loop_cases.json`，覆盖 8 个 case；既有 `deepseek_supply_request_*.json` fixture 已补齐强制字段。
- `已同步` 新聊天默认入口和 GPT Project 侧入口：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/13_execution_lane_and_parallel_rules.md`、`codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`codex_source/19_project_state_action_router.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/08_当前正式事实.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`。
- `本轮 DeepSeek 参与报告`：controller 供料验证为 `fallback_local_only`，`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`；本轮没有真实消耗 DeepSeek token，因此不能写 DeepSeek 已深度参与。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/`。
- `已生成` 上传说明：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/上传说明_UPLOAD_MANIFEST.md`。
- `已更新` `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向 20260515 mandatory DeepSeek 包，上一版 20260515 数据飞轮包降级为 `historical_previous_package_not_latest`。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：机制链、脚本字段、schema、fixture、日志和上传包已落库；DeepSeek 真实任务稳定供料、token 递减和 multi-agent runtime 稳定性仍 `待验证`。
- `日志`：`codex_log/20260515_mandatory_deepseek_supply_loop.md`
- `下一个目标`：下一轮真实 Codex 任务默认先进入 `deepseek_supply_gate（DeepSeek 供料闸门）`，并在最终回报中明确 DeepSeek 是否真实调用、token 是否应减少、是否 fallback，以及 Codex 是否完成二次补全。

## 20260515｜目标驱动数据飞轮、阈值、文案执行闭环与 GPT Project 静态包同步

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、项目文件修改、字段与函数落地和 GPT Project 静态包同步，不生成视频、不生成音频、不生成图片、不 mux、不重做 `full.mp4`、不修当前候选片、不推进发布状态。
- `已新增` `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`，作为目标、阈值、文案修改前置读取、内容结构反馈、单主变量和 Codex 动态执行 prompt 的正式机制入口。
- `已写入` `goal_driven_data_flywheel_spec_v1（目标驱动数据飞轮规格 V1）`：目标链路为 `目标 -> 单条视频实验 -> 发布数据 -> 复盘诊断 -> 下一条内容结构计划 -> Codex 动态执行 prompt -> 发布验证 -> 需求 / 客资 / 产品化沉淀 -> 目标更新`。
- `已写入` `threshold_config_v1（阈值配置 V1）`：包含播放、留存、收藏、点赞、有效评论、客资、阶段目标、指标裁决和状态边界。
- `已写入` 播放阈值：`< 1000` 触达不及格，`1000-3000` 基础观察，`3000-8000` 正向信号，`8000+` 小爆观察但需先排除泛流量。
- `已写入` 价值阈值：收藏率 `< 1% / 1%-2% / > 2%`，点赞率 `< 2% / 2%-5% / > 5%`，有效评论 `0-2 / 3-5 / > 5`。
- `已写入` 客资阈值：`lead_score >= 3` 为有效客资，`>= 4` 为高价值客资，`= 5` 为可转化客资；30 天客资信号分为 fail / baseline / strong / excellent。
- `已写入` 阶段阈值：`day_0_30`、`day_31_90`、`day_90_180` 的 stage_goal、pass_line、excellent_line、fail_line。
- `已写入` `lead_score_model（客资评分模型）`：0 分无效私信，1 分泛泛好奇，2 分弱需求，3 分明确问题，4 分明确场景 + 明确结果诉求，5 分明确场景 + 明确预算 / 时间 / 决策意愿。
- `已写入` `data_goal_copy_revision_gate（数据目标驱动文案修改闸门）`：正式文案修改前必须读取目标、阶段目标、阈值、`video_goal_card`、`post_publish_review_card`、`data_flywheel_memory`、`content_structure_feedback_card`、主短板、主变量、协同变量、禁止变量、成功指标和失败指标。
- `已写入` `content_structure_feedback_engine（内容结构反馈引擎）`：根据数据反推 `opening_0_3s`、`bridge_3_8s`、`problem_expand_8_15s`、`evidence_middle`、`judgment_turn`、`result_diff`、`ending_handoff` 每段下一条视频该放什么内容。
- `已写入` `single_primary_variable_rule（单主变量规则）`：默认 1 个主验证变量 + 最多 2 个协同变量；4 个变量必须标 `major_revision（大改版）`；超过 4 个变量不得写成单变量实验，只能写方向重做观察。
- `已写入` `next_video_execution_prompt（下一条视频执行 prompt）` 动态生成机制：Codex 不得只拿 `final_script（最终文案）` 自由发挥；缺动态执行 prompt 不得进入视频执行。
- `已新增 / 更新字段`：`video_goal_card`、`post_publish_review_card`、`data_flywheel_memory`、`content_structure_feedback_card`、`next_video_structure_plan`、`lead_score_model`、`threshold_config_v1`。
- `已新增阻断条件`：缺 `threshold_config_v1`、缺 `video_goal_card`、缺 `post_publish_review_card` 且声称数据驱动、缺 `main_bottleneck`、缺 `primary_variable`、变量数超限且未标 `major_revision`、缺 `next_video_execution_prompt`、缺 `content_structure_feedback_card` 却声称根据数据改结构。
- `已同步` GPT Project / ChatGPT 侧入口：`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`。
- `已同步` Codex 执行侧入口：`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`。
- `已同步` 当前事实 / 目标态：`GPT数据源/08_当前正式事实.md` 只写机制已落地、效果待验证；`GPT数据源/09_目标态计划.md` 写目标飞轮和阈值机制待验证方向。
- `已更新` fixture：`codex_source/fixtures/mechanism_inference_function_cases.json` 新增 9 个 case，覆盖阈值缺失 blocked、低播放 + 弱 3 秒留存、小流量高收藏、高播放低价值、缺数据改文案 blocked、bridge 下滑结构反馈、1 主 + 2 协同 allowed、4 变量 major_revision、5 变量 blocked；JSON parse 已通过，当前共 `27` 个 case。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/`。
- `已生成` 上传说明：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/上传说明_UPLOAD_MANIFEST.md`。
- `已更新` `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`：最新 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 指向 20260515 数据飞轮包，上一版 20260512 reference contract 包降级为 `historical_previous_package_not_latest`。
- `未修改`：`dist/latest_review_pack/`、视频 / 音频 / 图片 / 字幕 / 时间线产物、当前候选片媒体文件、`GPT 数据源/` 历史静态目录、`.env`、`.env.swp`、API key、token、secret。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：机制已写入、阈值已写入、字段已定义、阻断条件已写入、fixture 已补充、GPT Project 静态上传包已生成；目标飞轮真实效果仍 `待验证`，阈值仍是阶段工作假设，不是行业定论，也尚未被真实样本验证。
- `日志`：`codex_log/20260515_goal_driven_data_flywheel_copy_execution_loop_thresholds_and_gpt_project_package.md`
- `下一个目标`：下一条真实新片进入正式文案修改前，ChatGPT 先读取目标、阈值、上一条 / 同类视频数据、复盘结论、主短板和变量计划；改稿后生成 `next_video_execution_prompt（下一条视频执行 prompt）`，Codex 再进入执行。

## 20260514｜script anchor / TTS / opening / timeline 机制修补

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的执行前机制修补，不生成视频、不生成音频、不生成图片、不 mux、不重做 `full.mp4`、不修当前候选片。
- `已新增` `script_anchor_extraction_function（文案锚点提取函数）`：最终文案进入视频执行前，必须自动提取句子级 `script_function_map / evidence_anchor_map / visual_anchor_map / tts_prosody_anchor_map / card_anchor_map / forbidden_visual_map / script_to_timeline_map`。
- `已补强` `content_route_card V2（内容路由卡 V2）`：新增 `script_anchor_extraction_required / script_function_map_required / evidence_anchor_map_required / visual_anchor_map_required / tts_prosody_anchor_map_required / script_to_timeline_map_required / opening_visual_hook_spec_required / forbidden_visual_map_required`。
- `已补强` TTS 前置机制：`tts_prosody_anchor_map（TTS 韵律锚点表）` 成为 TTS 生成前置字段；用户反馈“某个字突然上扬”时，优先诊断 `prosody / pause_timing / sentence_segmentation / emphasis / pitch_contour`，不默认换音色。
- `已补强` 开头视觉机制：高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头必须先输出 `opening_visual_hook_spec（开头视觉钩子规格）`；静态两行标题页不能默认通过高情绪开头验收。
- `已补强` 文案到画面机制：`script_to_timeline_map（文案到时间线映射表）` 成为视频执行前置字段；只有 `material_01 / material_02 / material_03` 段落级分配时必须 blocked 为 `paragraph_level_mapping_insufficient`。
- `已补强` `editing_inference_function（剪辑推理函数）`：剪辑动作必须读取 `line_id / line_group_id` 和 `script_to_timeline_map`，不得只看段落级素材用途；文案句子与素材证据冲突时必须 blocked 或回到 ChatGPT 复审。
- `已补强` `quality_issue_classifier（质量短板分类器）`：新增 `voice_prosody_issue（声音韵律问题）`、`opening_visual_hook_issue（开头视觉钩子问题）`、`script_visual_mismatch_issue（文案画面错位问题）`。
- `已新增` 执行前阻断条件：`missing_script_anchor_extraction_function`、`missing_script_to_timeline_map`、`missing_tts_prosody_anchor_map`、`missing_opening_visual_hook_spec_when_high_emotion_hook`、`paragraph_level_mapping_only`。
- `已更新` fixture：`codex_source/fixtures/mechanism_inference_function_cases.json` 新增 5 个 case：`tts_pitch_rise_ai_feel_case`、`static_two_line_opening_failed_case`、`script_visual_mismatch_partial_case`、`paragraph_level_mapping_insufficient_case`、`ai_money_script_anchor_case`；JSON 可解析，当前共 `18` 个 case。
- `已同步` GPT Project 侧入口：`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`。
- `已同步` Codex 执行侧入口：`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`。
- `未修改`：`dist/latest_review_pack/`、任何视频 / 音频 / 图片 / 字幕 / 时间线成品、`GPT 数据源/` 历史静态目录、`.env` / `.env.swp` / API key / token / secret。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：字段、函数、fixture 和 blocked 条件写入为 `已确认`；真实新片效果、声音自然度、开头抓眼程度和句子级映射长期稳定性仍是 `待验证`。
- `日志`：`codex_log/20260514_script_anchor_tts_opening_timeline_mechanism_fix.md`
- `下一个目标`：下一条新片进入执行前，用 `script_anchor_extraction_function（文案锚点提取函数）` 自动生成句子级时间线、TTS 韵律和开头视觉 hook 规格，缺字段则自动 blocked。

## 20260514｜《AI 到底赚不赚钱》4:3 带 TTS 完整正片候选生成

- `已确认` 本轮生成《今天就说一个事：AI 到底能不能赚钱？》的 `4:3 带 TTS 完整正片候选`，不是字幕版技术样片，也不是纯技术预览。
- `输出目录`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/`
- `full.mp4`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/full.mp4`，`1440x1080`，时长 `243.85s`，`audio_present = true`，`decode_ok = true`，`technical_validation = passed`。
- `TTS / narration`：已生成 `dist/20260514_AI到底赚不赚钱_4_3_final_candidate/narration.wav`，共 `81` 个 TTS 分段，时长 `243.85s`，`pcm_s16le / 48000Hz / mono`，可被 `ffmpeg` 解码。
- `声音路线`：本轮使用项目既有安全 TTS 路线，目标模型 `qwen3-tts-vc-realtime-2026-01-15`，声音底子为脱敏 `qwen-t...ac19`；`voice_generation_validation = passed_for_generation_needs_human_review`。不得推进 `voice_validation` 或 `final_voice_validated`。
- `素材进入时间线`：三段用户真实录屏素材均已读取并进入时间线；`material_02` 承载粽子 / 婚纱样片，`material_01` 承载电商成本倒推，`material_03` 承载 Codex 本地项目执行系统。FocuSee 原始运镜按 `direct_cut_by_script` 保留，不做默认二次 zoom / crop / 重新运镜。
- `内容边界`：`10 分钟 / 22 元 / 半小时 / 20 多` 仍写为用户经验陈述，不写成素材画面直接证明；`material_03` 不写成 Codex 并发执行两个任务；不写 AI 自动赚钱，不写保证收益。
- `已生成` `content_route_card V2（内容路由卡 V2）`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/content_route_card_v2.json`，包含开头路线、三段素材证据计划、FocuSee 中段策略、总结卡、TTS 计划和平台风险说明。
- `字幕 / 卡片`：已生成 `captions.srt`、原创梗图感开头、结尾 `judgment_card（判断卡）`；抽帧与安全区检查未发现字幕 / 卡片遮挡核心证据的 must-fix。
- `平台风险初查`：`risk_level = caution`；未命中 `hard_block` 或 `rewrite_required`。本轮已把高风险表达 `自动赚钱` 改写为安全否定表达；发布前仍需人工复审标题、描述和平台 AI 标识。
- `未读取 / 未写出`：未读取 `.env` / `.env.swp`，未打印或写出 API key、token、secret。
- `未修改`：用户原始三段素材、`dist/latest_review_pack/`、当前复审包状态文件、当前发布目标。
- `未推进`：`content_validation = pending_user_chatgpt_review`，`send_ready = false`，`publish_status = not_advanced`，`visual_master_locked`、`voice_validation`、`final_voice_validated` 均不推进。
- `日志`：`codex_log/20260514_ai_money_4_3_final_candidate_assembly.md`
- `下一个目标`：用户 / ChatGPT 对 `full.mp4` 做内容、声音和发布文案复审，决定是否只改一个变量进入下一轮。

## 20260514｜4:3 画面比例技术装配修正

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 4:3 画面比例技术装配修正，不做内容验证，不推进发布状态，不改原始素材，不调用外部 API。
- `当前目标对象`：仍以 `codex_log/current_publish_target.md` 指向的《我用 AI 做 PPT 踩过的坑》v3.1 / `dist/latest_review_pack/` 为当前复审对象；本轮不覆盖 `dist/latest_review_pack/`，只生成 4:3 技术验证输出。
- `素材验证`：锁定正式工作区内最新可读 FocuSee 4:3 素材 `/Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4`；`ffprobe` 结果为 `2498x1874`，比例 `1.332978`，判定接近 `4:3`。
- `已新增` `scripts/四比三装配验证_4_3_assembly_validation.py（4:3 装配验证脚本）`：本地读取素材宽高、阻断非 4:3 素材、以 `scale + pad` 输出 `1440x1080`，不做默认二次 zoom / crop / 重新运镜。
- `已生成` 本地技术验证输出：`dist/20260514_4_3_aspect_ratio_assembly_fix/4_3_assembly_validation_preview.mp4`，`ffprobe` 结果为 `1440x1080`，比例 `1.333333`，`technical_validation = passed_for_4_3_assembly`。
- `已生成` `content_route_card V2（内容路由卡 V2）`：`dist/20260514_4_3_aspect_ratio_assembly_fix/content_route_card_v2.json`，包含 `target_aspect_ratio = 4:3`、素材宽高、`screen_first_opening`、FocuSee 中段直接剪辑策略、字幕安全区和卡片不插入策略。
- `字幕 / 卡片安全区`：本轮技术验证输出未烧字幕、未插总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡；V2 卡中记录后续 4:3 安全区建议，避免字幕或卡片压住中段真实证据。
- `未修改`：用户原始 FocuSee 素材、`dist/latest_review_pack/`、当前复审包状态文件、`.env`、`.env.swp`、API key、token、secret。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：本轮只可写成 `technical_validation = passed_for_4_3_assembly`；`content_validation = not_evaluated`，`send_ready = false`，不得写成内容过线或可发布。
- `日志`：`codex_log/20260514_4_3_aspect_ratio_assembly_fix.md`
- `下一个目标`：在下一轮真实内容执行中，用最终文案时间码把 4:3 FocuSee 素材切成正式段落，并按 4:3 安全区重新判断开头、字幕、卡片和证据窗口。

## 20260514｜content_route_card V2 与机制推理测试样例补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制推理测试样例与 `content_route_card V2（内容路由卡 V2）` 输出模板补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `codex_source/fixtures/mechanism_inference_function_cases.json（机制推理函数测试样例）`：在保留旧 6 个 case 的基础上新增 7 个 case，覆盖 FocuSee 直接剪辑、FocuSee 证据不清 blocked、梗图 GIF 开头、元素娃娃开头、反转卡位置、总结卡位置、卡片打断 FocuSee 证据窗口 blocked。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `content_route_card V2（内容路由卡 V2）` 标准输出模板，一次性判断 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / focusee_middle_editing_decision / card_placement_decision / api_human_usage / ppt_usage / prompt_tail_card_usage / flow_flex_reason / blocked_if`。
- `已轻量同步` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：明确 `content_route_card V2` 是 `content_route_inference_function（内容路由推理函数）` 的标准输出模板之一，fixture cases 是新增机制的最小验证样例。
- `已轻量同步` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：命中内容执行、视频执行、开头路由、中段剪辑或卡片位置时，Codex 必须输出 `content_route_card V2` 或等效完整字段；缺关键判断不得直接生成视频。
- `已轻量同步` `codex_source/01_execution_rules.md（Codex 执行规则）`：涉及内容执行 / 视频执行 / 文案进入执行时，必须先生成 `content_route_card V2`；缺 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / card_placement_decision / flow_flex_reason` 不得进入视频执行；素材来自 FocuSee 时必须额外填写 `focusee_middle_editing_decision`。
- `已轻量同步` `GPT数据源/03_总索引与阅读顺序.md（总索引与阅读顺序）`：补充 `content_route_card V2` 模板位置和覆盖范围，方便新会话从索引定位。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：fixture 样例写入和 V2 模板写入为 `已确认`；真实视频执行效果仍是 `待验证`，不得写成真实视频任务已验证通过。
- `日志`：`codex_log/20260514_content_route_card_v2_and_fixture_cases.md`
- `下一个目标`：下一条真实视频执行前，用 `content_route_card V2（内容路由卡 V2）` 验证 Codex / ChatGPT 能否一次性判断开头、中段、卡片、证据、API 人物、PPT、Prompt 尾卡和 blocked 条件。

## 20260514｜卡片位置路由机制补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的卡片位置路由机制补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `card_placement_decision（卡片位置判断）`，明确总结卡、反转卡、结果差卡和 Prompt 尾卡是文案功能卡，不是固定 shot 模板。
- `已更新` `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`：补充卡片只服务观众理解路径，不等于强证据；强证据仍来自用户录制素材、前后对比、步骤截图、结果截图或平台数据。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：`content_route_inference_function（内容路由推理函数）` 接入 `copy_function / reversal_point / conclusion_point / result_diff_point / evidence_window_active / prompt_handoff_needed`，`editing_inference_function（剪辑推理函数）` 接入卡片是否打断证据窗口的判断。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：命中总结卡、反转卡、结果差卡或 Prompt 尾卡位置判断时，必须先输出 `card_placement_decision（卡片位置判断）`，不得固定旧 shot。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：视频执行前若涉及卡片位置，缺 `card_placement_decision` 不得直接生成视频；文案没有明确反转点不得强插反转卡，文案没有明确结论 / 下一步不得强插总结卡。
- `已轻量同步` `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md（当前主线锚点）`：修正 `Prompt 引用尾卡` 和结尾总结壳的固定位置误读，改为由 `card_placement_decision` 判断。
- `新规则`：总结卡位置跟随文案收束点、判断结论和下一步动作；反转卡位置跟随认知反转、错误示范、新旧对比和结果差转折；卡片不得抢中段真实录屏证据。
- `保留边界`：v3.1 / round34 / PR #7 B / cute_info_card_route / sassy_reaction_card_route 等历史 reference 只作为参考白名单或历史基线保留，不误删、不废弃、不升级成所有内容固定位置。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：卡片位置路由机制写入为 `已确认`；真实视频卡片位置长期效果仍是 `待验证`，不得写成已在真实视频任务中长期验证通过。
- `日志`：`codex_log/20260514_card_placement_route_fix.md`
- `下一个目标`：下一条真实内容执行前，用 `card_placement_decision（卡片位置判断）` 验证 Codex / ChatGPT 能否按最终文案、证据窗口和观众理解路径选择卡片类型与位置。

## 20260514｜开头路由机制补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的开头路由机制补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：在 `content_route_card（内容路由卡）` 中新增 `opening_route_decision（开头路由判断）`，明确先判断开头路线，再执行开头。
- `已更新` `GPT数据源/04_选题与文案规则.md（选题与文案规则）`：选题进入主流程前必须判断开头路线；普通讲解 / 复盘 / 低压陪伴型选题可继续使用元素娃娃开头，争议 / 情绪 / 商业焦虑型且开头超过 `3s` 可优先考虑梗图 GIF 开场。
- `已更新` `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md（当前主线锚点）`：元素娃娃 / 可爱元素主持娃娃保留为合法 opening route，但不得理解成所有内容唯一默认开头。
- `已更新` `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`：补充梗图 GIF 开头只负责抓眼、起情绪、抛问题，不算强证据；强证据仍来自用户录制素材、前后对比、步骤截图、结果截图或平台数据。
- `已同步` `GPT数据源/00_项目总述.md（项目总述）` 与 `GPT数据源/08_当前正式事实.md（当前正式事实）`：修正旧“开头人物壳默认统一”事实入口，避免新会话继续误判元素娃娃为所有内容默认开头。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：`content_route_inference_function（内容路由推理函数）` 新增 `opening_duration`、`topic_emotion_level`、`controversy_level`、`evidence_start_strength`、`brand_consistency_need` 等输入信号，并新增四种 opening route 的状态与动作策略。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：Codex 执行侧命中开头路线、元素娃娃开头、梗图 GIF 开场或开头参考图时，必须先输出 `opening_route_decision`，不得绕过判断直接生成开头。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：涉及开头时，缺 `opening_route_decision` 不得直接生成视频；选择梗图 GIF 开头必须保留 reference contract / effect target / must_not_copy 边界；选择元素娃娃开头必须说明品牌一致性或轻陪伴理由。
- `已同步` `GPT数据源/01_项目系统提示词.md（项目系统提示词）`：修正系统提示入口中“开头人物壳默认统一”的旧句，避免新会话继续把元素娃娃误判为所有内容默认开头。
- `新规则`：元素娃娃开头保留为合法路线之一，不废弃；梗图 GIF 开场是条件优先路线，不是新唯一默认；开头 GIF 只负责 hook / ask，不负责 proof，不替代中段真实录屏证据。
- `reference 边界`：用户本轮上传抖音截图只继承“漫画冲击线 / 反应姿态 / 大字压屏 / GIF 感 / 快速抛问题”的开头机制，不复刻具体人物、头像、字体、构图或第三方可识别资产。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：开头路由机制写入为 `已确认`；真实视频开头效果长期稳定性仍是 `待验证`，不得写成已在真实视频任务中验证通过。
- `日志`：`codex_log/20260514_opening_route_mechanism_fix.md`
- `下一个目标`：下一条真实内容执行前，用 `opening_route_decision（开头路由判断）` 验证 Codex / ChatGPT 能否根据内容目标、时长、情绪、争议、证据强度和品牌一致性选择开头路线。

## 20260513｜FocuSee 中段剪辑职责机制修补

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 FocuSee 中段剪辑职责机制修补，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `3D-2. FocuSee 自带运镜录屏素材的中段剪辑边界`，明确 FocuSee 自带 `3D Motion（3D 运镜）` / 自动跟随 / 自动观看引导时，默认视为 `recording_layer_motion_baked_in（录制层运镜已内置）`。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（状态动作总控器与机制推理层）`：`editing_inference_function（剪辑推理函数）` 新增 `direct_cut_required`、`keep_original_motion`、`no_secondary_zoom_by_default`、`secondary_zoom_allowed_only_if_evidence_unclear` 等状态与动作策略。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：Codex 执行侧同步 FocuSee 自带运镜素材的 `state_inference / action_policy / not_allowed` 规则。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：当素材标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）` 时，Codex 不得默认二次放大、裁切重构视角或把自动放大当成中段剪辑完成标准。
- `新规则`：FocuSee 自带运镜素材默认不再由 Codex 二次 zoom / crop / 重新运镜；Codex 改为按最终文案识别时间码、切分段落、删冗余、保留原始运镜、衔接口播 / 字幕 / 卡片。
- `允许例外`：只有 FocuSee 运镜未覆盖关键证据点、关键文字仍不可读、结果差未展示清楚，或用户明确要求二次剪辑增强时，才允许判断辅助放大 / 定格 / 卡片；仍不得破坏 FocuSee 原有运镜节奏或抢走真实录屏证据。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：FocuSee 录制层运镜职责边界写入为 `已确认`；真实视频任务长期效果仍是 `待验证`，不得写成已在真实 FocuSee 成片中长期验证通过。
- `日志`：`codex_log/20260513_focusee_middle_editing_route_fix.md`
- `下一个目标`：下一条使用 FocuSee 录屏素材的真实执行任务中，验证 Codex 是否能按文案直接剪辑并保留原始 3D 运镜，而不是默认二次放大。

## 20260512｜三大机制推理函数落地

- `已确认` 本轮在《视频工厂｜OPC 一人公司 AI 闭环验证系统》中一次性落地三大机制推理函数：`editing_inference_function（剪辑推理函数）`、`content_route_inference_function（内容路由推理函数）`、`quality_issue_classifier（质量短板分类器）`。
- `已更新` GPT Project / ChatGPT 侧最高机制入口：`GPT数据源/11_项目状态动作总控器_机制推理层.md`，三大函数均补齐 `input_signal -> observed_evidence -> state_inference -> action_policy -> validation_rule -> blocked_if -> feedback_update` 结构。
- `已更新` Codex 执行侧入口：`codex_source/19_project_state_action_router.md`，明确命中剪辑、内容承载、质量复审时，必须先输出对应推理函数；缺函数结果不得生成卡片 / 决策包，不得进入视频执行，不得写 `completed（已完成）`。
- `已更新` Codex 执行规则：`codex_source/01_execution_rules.md`，新增三大机制推理函数前置闸门，要求命中相关任务时先输出函数结果，并把 fixture / 最小样例纳入机制修补完成条件。
- `已同步` `GPT数据源/05_文案路由规则.md`：`content_route_card（内容路由卡）` 明确为 `content_route_inference_function（内容路由推理函数）` 的输出卡；`editing_decision_pack（剪辑决策包）` 明确由 `editing_inference_function（剪辑推理函数）` 推理后生成。
- `已同步` `GPT数据源/07_AI知识类视频价值规则.md`：`quality_lock_card（质量锁卡）` 必须调用 `quality_issue_classifier（质量短板分类器）`，先定位唯一最高优先级短板，再决定下一轮只改一个变量。
- `已同步` `codex_source/00_codex_readme.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`，把三函数纳入默认接手、OPC 闭环、GPT Project 系统提示和总索引。
- `已新增` 最小测试样例：`codex_source/fixtures/mechanism_inference_function_cases.json`，覆盖三个函数各 2 个 case：正常判断 + blocked / human_review_required 判断。
- `已确认` 本轮是机制口径、路由口径、执行口径、验收口径补全；不是视频内容口径、发布状态口径、声音最终方案口径或商业化成立口径。
- `边界`：三大函数已写入并通过结构 / 关键词 / fixture 可解析检查后可作为后续任务前置机制；但长期真实任务稳定性仍是 `待验证`，不得写成机制长期稳定验证通过。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线 / 字幕 / TTS / 媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `日志`：`codex_log/20260512_三大机制推理函数落地_core_inference_functions_landing.md`
- `下一个目标`：用下一条真实内容执行或复审任务验证三大函数能否稳定阻断“只写动作名 / 只写卡片 / 技术通过当内容通过”的旧问题。

## 20260512｜参考到执行落地契约落地

- `已确认` 本轮在《视频工厂｜OPC 一人公司 AI 闭环验证系统》中正式落地 `Reference-to-Execution Contract（参考到执行落地契约）`。
- `已新增` GPT Project / ChatGPT 侧机制文件：`GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`，把用户目标、reference、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考转换成 Codex 可执行函数字段与可验收标准。
- `已新增` Codex 执行层机制文件：`codex_source/20_reference_to_execution_contract.md`，规定带 reference 的任务必须先输出 `reference_to_execution_contract`，没有契约不得执行，没有 `deviation_check（偏离检查）` 不得写 `completed（已完成）`。
- `已新增` 最小测试用例：`codex_source/fixtures/reference_to_execution_contract_cases.json`，覆盖 visual、editing、copywriting raw feeling、voice、quality sample、reference missing、state conflict、missing deviation check、Perplexity reference pack 共 9 个 case。
- `已同步` `GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`codex_source/19_project_state_action_router.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/18_deepseek_supply_request_schema.md`、`AGENTS.md`。
- `已确认` `DeepSeek / fallback` 供料包只可辅助携带 `reference_anchor`、`effect_targets`、`function_fields`、`deviation_check`、`done_when_contract`，不得替代正式 reference contract。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_reference_contract/`；上传包包含 `12_参考到执行落地契约_reference_to_execution_contract.md`、本轮 dated log、最新 `latest.md` 和当前本地产物路径索引。
- `边界`：本包只是 GPT Project 静态资料包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表内容验证通过，不代表 reference 机制长期执行效果已在真实视频任务中稳定验证。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_参考到执行落地契约落地.md`
- `下一个目标`：用下一次真实带 reference 的文案 / 视觉 / 剪辑任务验证 `Reference-to-Execution Contract（参考到执行落地契约）` 能否让 Codex 先拆效果目标和执行函数字段，再做偏离检查。

## 20260512｜项目状态动作总控器与机制推理层落地

- `已确认` 本轮把《视频工厂｜OPC 一人公司 AI 闭环验证系统》的最高机制层从审计蓝图落成可执行入口、可调用表、可验证字段、router fixtures 和 GPT Project 静态上传包。
- `已新增` GPT Project / ChatGPT 侧最高机制入口：`GPT数据源/11_项目状态动作总控器_机制推理层.md`，包含 `project_state_table`、`fact_source_arbitration_table`、`trigger_routing_table`、`mechanism_inference_template`、`completion_state_inference`、`feedback_update_rule` 和当前 `seed_state`。
- `已新增` Codex 执行层总控规则：`codex_source/19_project_state_action_router.md`，要求每轮在 `route_decision（路由判断）` 后、具体执行前输出 `state_action_router（项目状态动作总控器）`。
- `已新增` 最小路由测试用例：`codex_source/fixtures/project_state_action_router_cases.json`，覆盖截图 / 数据、最终文案、素材、Codex done、自觉不对、旧口径残留、灰度数据缺失、GPT Project 包落后、DeepSeek fallback 等 9 个场景。
- `已同步` `GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`AGENTS.md`，将最高机制入口从旧 `10 + 1` 口径升级为 `10 份基础执行包 + OPC 总纲 + 状态动作总控器`。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_state_router/`；上传包包含 `11_项目状态动作总控器_机制推理层.md` 与本轮 dated log。
- `边界`：本包只是静态资料包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表内容验证通过。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_项目状态动作总控器与机制推理层落地.md`
- `下一个目标`：把 `editing_inference_function（剪辑推理函数）` 落成同样的信号、状态、动作、验证和反馈链，让中段剪辑不再只停留在动作名。

## 20260512｜机制落地化审计与推理层蓝图

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》机制落地化审计，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已生成审计报告：`codex_log/20260512_机制落地化审计与推理层蓝图.md`。
- `已确认` 本轮 Must read 文件全部 `read_ok`，当前分支为 `main`；未跟踪 `.env.swp` 未读取、未触碰、未纳入本轮改动。
- `机制落地性结论`：当前项目已有 14 个核心机制；约 4 个具备较完整或局部可执行推理链，约 10 个仍缺统一 `机制推理函数`。
- `P0`：`editing_decision_pack（剪辑决策包）` 已有动作枚举和字段，但缺“什么点该放大 / 不该放大 / 放大会不会切断上下文 / 素材不清时是否 blocked”的推理函数。
- `P0`：`content_route_card（内容路由卡）` 缺从内容类型、素材证据、结果差、平台风险推断承载结构、API 人物次数、PPT / 尾卡使用方式的函数。
- `P0`：`quality_lock_card（质量锁卡）` 缺质量短板归因函数，尚不能稳定判断问题在声音、节奏、剪辑、证据、画面、卡片密度还是人感。
- `部分成立`：`review_loop（复盘闭环）` 是当前最接近推理函数的机制，已有“数据 -> 短板层 -> 单变量动作 -> 指标验证”链条；但 V001 真实数据和缺失字段仍待回填。
- `蓝图`：建议新增 `Mechanism Inference Layer（机制推理层）`，包含 `trigger_router`、`signal_taxonomy`、`state_inference`、`action_policy`、`validation_rule`、`feedback_update` 六个模块。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `下一个目标`：先把 `editing_decision_pack（剪辑决策包）` 补成可执行的 `editing_inference_function（剪辑推理函数）`，让 Codex 能按“信号 -> 状态推测 -> 动作选择 -> 验证 -> 反馈更新”判断中段该放大什么、该保留什么、什么时候必须 blocked。

## 20260512｜GPT Project 最新版上传包生成

- `已确认` 已生成最新版 GPT Project 静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512/`。
- `已确认` 上传包内包含 `上传说明_UPLOAD_MANIFEST.md（上传说明清单）`。
- `已确认` 本包包含 `GPT数据源/` 当前 10 + 1 基础执行包、最新 `codex_log/latest.md`、`Completion Relay Gate（补全接力闸门）` 机制修补日志、`项目残缺审计 project_gap_audit`、GPT Project 短路由说明和当前本地产物路径索引。
- `已确认` `codex_log/current_local_artifact_paths.md` 已将 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 更新为 20260512 新包；旧 20260509 包已降级为 `historical_previous_package_not_latest`。
- `状态边界`：本轮只生成静态上传包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表当前视频内容已通过，不代表 DeepSeek 长期稳定，不代表多 agent runtime 已跑通，不代表 v3.1 灰度测试完成。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_GPT_Project最新版上传包生成.md`
- `下一个目标`：用户将 20260512 新包上传到 GPT Project 后，GPT Project 静态资料与 GitHub `main` 当前机制、补全接力规则和项目残缺审计结果保持一致。

## 20260512｜项目残缺审计 project_gap_audit

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》项目残缺审计，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已生成审计报告：`codex_log/20260512_项目残缺审计_project_gap_audit.md`。
- `已确认` 本轮 Must read 文件全部 `read_ok`，未发现 missing / unreadable。
- `P0`：`codex_log/current_publish_target.md` 仍残留旧分支 / 旧同步口径，和当前 `main` 主读取分支规则不一致。
- `P0`：v3.1 灰度测试 24h / 72h / 7d 数据仍未回填，无法判断 6000 播放基础门槛、短板层和下一轮唯一变量。
- `P1`：`V001_missing_fields.md` 未真实列出缺失字段，容易把“没有数据”误读成“没有缺失”。
- `P1`：`Completion Relay Gate（补全接力闸门）` 已写入，但长期执行效果仍需真实修补任务验证。
- `P1`：DeepSeek / `execution_supply_pack family` 仍不能写成稳定真实供料链路。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `当前机制状态`：审计报告写入与缺口分级为 `已确认`；`Completion Relay Gate（补全接力闸门）` 长期防止 Codex 做一半提前收工的效果仍是 `待验证`。
- `下一个目标`：先把 `current_publish_target.md` 的旧分支残留和 v3.1 `review_loop` 缺失字段显示修到不会误导新会话，再用这一轮修补反向验证 `Completion Relay Gate（补全接力闸门）` 是否能真正执行到底。

## 20260512｜Completion Relay Gate 补全接力闸门机制修补

- `已确认` 本轮是机制修补，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已新增 / 补强 `Completion Relay Gate（补全接力闸门）`，用于连接 `ChatGPT 横向补全`、`Codex 纵向细化`、`执行后剩余工作反查` 与 `日志 / 当前事实 / 入口规则同步`。
- `已确认` `codex_source/01_execution_rules.md（Codex 执行规则）` 已新增 `2E-2. Completion Relay Gate（补全接力闸门）`，强制输出 `completion_relay_gate`、`required_output_inventory`、`child_task_graph`、`remaining_work_check`、`sync_back_check`。
- `已确认` `codex_source/00_codex_readme.md（Codex 执行层总入口）` 已补入口规则：Codex 收到 ChatGPT 完整执行单 / 横向补全包时，必须先转成任务树和交付清单，执行后反查剩余工作与同步回写。
- `已确认` `GPT数据源/01_项目系统提示词.md（项目系统提示词）` 已补 `GPT -> Codex 补全接力规则`，明确 ChatGPT 横向补全、Codex 纵向拆解与执行到底。
- `已确认` `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md（OPC 多 AI 协作机制）` 已补 `GPT -> Codex 补全接力机制`，明确 DeepSeek 只读供料，不替代 Codex 原文件复核与执行后反查。
- `已确认` `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（GPT Project 短路由说明）` 仍承担 GPT Project 侧短路由说明，本轮已补 Completion Relay Gate 触发提醒。
- `已确认` `AGENTS.md（仓库入口规则）` 已做轻量入口同步，只补机制入口引用，不改视频动态状态。
- `manual_structure_check`: `passed`
- `keyword_check`: `passed`
- `diff_scope_check`: `passed`
- `forbidden_status_check`: `passed_no_dynamic_status_promotion`
- `api_call_check`: `not_called`
- `secret_read_check`: `not_read`
- `media_generation_check`: `not_generated`
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：规则写入与结构检查为 `已确认`；长期执行效果仍是 `待验证`，不得写成机制长期稳定。
- `日志`：`codex_log/20260512_补全接力闸门机制修补.md`
- `下一个目标`：用下一次真实多文件执行单验证 `Completion Relay Gate（补全接力闸门）` 能否让 Codex 按任务树执行到底并在收尾前反查剩余工作。

## 20260510｜DeepSeek process env key 安全重跑通过

- `已确认` 已创建本地安全输入脚本：`scripts/run_safe_deepseek_stability_prompt.sh`。
- `已确认` 已通过 macOS Terminal 弹窗运行脚本，用户在 Terminal 内隐藏输入 `DEEPSEEK_API_KEY（DeepSeek API 密钥）`；Codex 对话框未接收 key。
- `已确认` 脚本只在当前进程临时 export key，测试结束后执行 `unset DEEPSEEK_API_KEY`。
- `request_file`: `codex_log/supply_requests/20260510_deepseek_stability_check_request.json`
- `supply_source`: `deepseek_passed`
- `fallback_status`: `not_used`
- `context_pack_validation`: `passed`
- `deepseek_generation_status`: `passed_with_retries`
- `deepseek_actual_participation`: `true`
- `blocked_reason`: `none`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `key_written_to_env_file`: `false`
- `key_found_in_git_diff`: `false`
- `结果边界`：本轮只证明 DeepSeek 对这个稳定化 request 样例真实供料通过；不代表 DeepSeek 长期稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，也不代表内容验证通过。
- `已确认` 本轮未调用阿里 API，未生成图片 / 视频 / 音频。
- `已确认` 本轮未修改发布状态、声音状态或内容验证状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `日志`：`codex_log/20260510_deepseek_process_env_rerun.md`
- `下一个目标`：进入一条真实文案的小范围素材计划执行，只做计划与供料验证，不调用阿里 API。

## 20260510｜DeepSeek 稳定化检查与 readiness 前置闸门

- `已确认` 本轮目标是稳定 DeepSeek 三态语义，不是强行证明 DeepSeek 每次成功。
- `已确认` 已新增稳定化 request：`codex_log/supply_requests/20260510_deepseek_stability_check_request.json`。
- `已确认` 已新增稳定化日志：`codex_log/20260510_deepseek_stability_check.md`。
- `已确认` 已补齐 `deepseek_readiness_check（DeepSeek 就绪检查）`：后续任何 DeepSeek 相关任务、`execution_supply_pack family（执行供料包族）`、reference / visual route / 多文件机制任务，都必须先输出该检查。
- `已确认` controller 现在稳定输出：
  - `deepseek_readiness_check`
  - `blocked_reason`
  - `env_file_read`
  - `process_env_key_allowed`
  - `process_env_key_present`
  - `not_deepseek_conclusion`
  - `deepseek_actual_participation`
- `已确认` explorer 已补齐 blocked 语义映射：
  - `blocked_missing_process_env_api_key`
  - `blocked_invalid_api_key`
  - `blocked_network_or_timeout`
  - `blocked_invalid_context_pack`
- `test_a_default_mode_supply_source`: `fallback_local_only`
- `test_a_default_mode_not_deepseek_conclusion`: `true`
- `test_b_process_env_key_present`: `false`
- `test_b_process_env_mode_supply_source`: `blocked`
- `test_b_context_pack_validation`: `blocked_missing_process_env_api_key`
- `test_b_deepseek_actual_participation`: `not_tested_missing_process_env_key`
- `blocked_reason`: `missing_process_env_api_key`
- `deepseek_real_supply_status`: `not_passed`
- `fallback_status`: `usable_with_fallback`
- `blocked_status`: `blocked_missing_process_env_key`
- `current_truth`: 当前进程环境没有 `DEEPSEEK_API_KEY`；本轮没有真实 DeepSeek passed，不能写成 DeepSeek 稳定供料。
- `py_compile`: `passed`
- `request_json_parse`: `passed`
- `schema_json_parse`: `passed`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `env_file_read`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `ali_api_called`: `false`
- `image_generated`: `false`
- `video_generated`: `false`
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：`technical_validation（技术验证）` 只代表脚本、request 和禁止项回归通过；`mechanism_validation（机制验证）` 代表 readiness 与三态语义补齐；`deepseek_supply_validation（DeepSeek 供料验证）` 当前仍是 `blocked_missing_process_env_key`；`content_validation（内容验证）` 未验证且未改变。
- `下一个目标`：用户先把 `DEEPSEEK_API_KEY` 安全注入 process environment，再重跑本稳定化测试；若 DeepSeek passed，再进入一条真实文案的小范围素材计划执行，不调用阿里 API。

## 20260510｜真实文案全执行供料链测试与 DeepSeek 安全参与路径

- `已确认` 本轮找到仓库内真实口播文本入口：`dist/latest_review_pack/timeline.json` 的 `voice_text` 字段；本轮只读文本，不读取媒体文件。
- `已确认` 真实文案选择状态为 `closest_available_repo_copy`：它是当前 v3.1 基线时间线中最接近当前真实口播脚本的仓库文本入口。
- `已确认` 已新增真实文案全执行供料链测试日志：`codex_log/20260510_real_copy_execution_supply_chain_test.md`。
- `已确认` 测试包包含：
  - `content_route_card（内容路由卡）`
  - `visual_asset_requirement_pack（视觉素材需求包）`
  - `api_asset_generation_pack（API 素材生成包）`
  - `image_prompt_pack（图片 prompt 包）`
  - `asset_validation_pack（素材验收包）`
  - `assembly_decision_pack（装配决策包）`
  - `editing_decision_pack（剪辑决策包）`
  - `review_pack_test_summary（测试审片回流摘要）`
- `已确认` 已新增 request：
  - `codex_log/supply_requests/20260510_real_copy_execution_supply_chain_request.json`
  - `codex_log/supply_requests/20260510_safe_deepseek_process_env_request.json`
- `已确认` 已建立 DeepSeek 安全真实参与路径：controller 可在显式 `--allow-process-env-api-key` / `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1` 下，让 explorer 使用 process environment 中已有的 `DEEPSEEK_API_KEY`；同时 `DEEPSEEK_DISABLE_ENV_FILE=1` / `--no-env-file` 禁止读取 `.env`。
- `已确认` 安全路径边界：不读取 `.env`，不打印 key，不写 key，不把 key 放进 prompt / supply pack / manifest / log，只把 key 用作 HTTP Authorization。
- `real_copy_request_validation`: `passed`
- `real_copy_supply_source`: `fallback_local_only`
- `real_copy_not_deepseek_conclusion`: `true`
- `safe_test_A_default_supply_source`: `fallback_local_only`
- `safe_test_B_allow_process_env_supply_source`: `blocked`
- `safe_test_B_context_pack_validation`: `blocked_missing_process_env_api_key`
- `deepseek_actual_participation`: `not_tested_missing_process_env_key`
- `原因`：当前 shell 进程环境没有 `DEEPSEEK_API_KEY`；按本轮安全规则不得读取 `.env` 补救。
- `env_file_read`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `request_json_parse`: `passed`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `已确认` 本轮未调用阿里 API，未读取 API key，未生成真实图片 / 视频 / 音频。
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：本轮只是机制与真实文案小范围供料链测试，不代表阿里 API 图片生成链路已跑通，不代表 DeepSeek 稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频内容通过。
- `安全参与测试日志`：`codex_log/20260510_safe_deepseek_participation_test.md`
- `下一个目标`：如果需要验证真实 DeepSeek API 参与，先把 `DEEPSEEK_API_KEY` 安全注入为 process environment 后，重跑 `safe_deepseek_participation_test`；如果已完成安全注入，再进入一条真实文案的小范围素材计划执行，不调用阿里 API。

## 20260510｜全执行供料包族与 DeepSeek 双重补全测试

- `已确认` 本轮把 DeepSeek + Codex 配合从 `editing_decision_pack（剪辑决策包）` 扩展为 `execution_supply_pack family（执行供料包族）`。
- `已确认` 新增并接入以下供料 action：
  - `visual_asset_requirement_pack（视觉素材需求包）`
  - `api_asset_generation_pack（API 素材生成包）`
  - `image_prompt_pack（图片 prompt 包）`
  - `asset_validation_pack（素材验收包）`
  - `assembly_decision_pack（装配决策包）`
  - 保留并接入 `editing_decision_pack（剪辑决策包）`
- `已确认` action 已同步进入 `codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`codex_source/schemas/deepseek_supply_request.schema.json` 和 `scripts/deepseek_supply_controller.py`。
- `已确认` `GPT数据源/05_文案路由规则.md` 已补全：`文案 -> 内容路由 -> 视觉素材需求 -> API 素材生成计划 -> 图片 prompt -> 素材验收 -> 装配决策 -> 剪辑决策 -> 审片回流`。
- `已确认` `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 已同步 DeepSeek 只读供料范围；最终执行判断仍在 Codex，内容质量判断仍在 ChatGPT / 用户。
- `已确认` `GPT数据源/07_AI知识类视频价值规则.md` 已补充 AI / API 生成图片与真实证据边界：API 图只能辅助表达，不能冒充真实录屏证据。
- `已确认` Codex 第二层自动补全发现用户点名 fixture 未覆盖 `asset_validation_pack（素材验收包）`，本轮已补增对应 fixture。
- `已确认` 新增 fixtures：
  - `codex_source/fixtures/deepseek_supply_request_visual_asset_requirement_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_api_asset_generation_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_image_prompt_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_asset_validation_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_assembly_decision_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_bad_forbidden_media_example.json`
  - `codex_source/fixtures/deepseek_supply_request_bad_forbidden_latest_review_pack_example.json`
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `fixture_json_parse`: `passed`
- `controller_runs`: `file_map / editing_decision_pack / visual_asset_requirement_pack / api_asset_generation_pack / image_prompt_pack / asset_validation_pack / assembly_decision_pack = passed_with_fallback_local_only`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `supply_source`: `fallback_local_only`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `deepseek_actual_participation`: `false`
- `原因`：本轮禁止读取 `.env / secret`；controller 因此跳过会读取 `.env` 的 DeepSeek explorer，使用本地兜底供料。
- `dist 输出口径`：`dist/deepseek_supply_controller/*` 是本地运行产物，不作为 GitHub 主事实提交；GitHub 可追溯证据以 `codex_log/20260510_execution_supply_pack_test_evidence.md` 为准。
- `已确认` 本轮未调用阿里 API，未读取 API key，未生成真实图片 / 视频 / 音频。
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：本轮只是机制与供料样例测试，不代表阿里 API 图片生成链路已跑通，不代表 DeepSeek 稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频内容通过。
- `执行日志`：`codex_log/20260510_全执行供料包族与DeepSeek双重补全测试.md`
- `供料证据日志`：`codex_log/20260510_execution_supply_pack_test_evidence.md`
- `下一个目标`：用一条真实最终文案做小范围执行测试：让 Codex 基于文案先生成视觉素材需求、API 素材生成计划、图片 prompt、素材验收、装配决策和剪辑决策，但仍不直接生成完整大视频，先验证全执行供料链是否能减少漏项和误用素材。

## 20260510｜DeepSeek 深度配合与自动补全闸门

- `已确认` 本轮落地 `Auto-completion gate（自动补全闸门）`，用于阻断 Codex 只完成用户点名任务、遗漏上游判断、供料、三卡、执行中补缺口、执行后风险复核、日志回流或事实同步。
- `已确认` 自动补全闸门已写入 `codex_source/01_execution_rules.md（Codex 执行规则）`，后续触发任务必须输出 `auto_completion_gate` 字段，并检查 `goal_layer / judgment_layer / route_layer / trigger_layer / supply_layer / execution_layer / feedback_layer / validation_layer / sync_layer`。
- `已确认` 本轮新增 DeepSeek action：`editing_decision_pack（剪辑决策包）`，已同步进入：
  - `codex_source/17_deepseek_supply_controller_protocol.md`
  - `codex_source/18_deepseek_supply_request_schema.md`
  - `codex_source/schemas/deepseek_supply_request.schema.json`
  - `scripts/deepseek_supply_controller.py`
- `已确认` 新增可运行样例任务卡：`codex_source/fixtures/deepseek_supply_request_editing_decision_pack_example.json`。
- `已确认` `editing_decision_pack（剪辑决策包）` 只允许基于 Codex 提供的文字化素材样料供料，不直接读取视频、音频、图片或媒体文件，不剪视频，不拍板最终画面质量。
- `已确认` DeepSeek 深度配合流程已写入 `codex_source/17_deepseek_supply_controller_protocol.md`：`route_decision -> Auto-completion gate -> supply_request -> controller -> supply_pack -> Codex 读包 -> Codex 复核原文件 -> 执行 -> after_read_gap / risk_report 复核 -> latest / dated log 回流`。
- `已确认` OPC 上位机制已轻量同步：DeepSeek 仍是只读供料层，供料扩展到执行前文件地图、执行中缺口补读、执行后风险复核和视频执行现场 `editing_decision_pack（剪辑决策包）`；最终执行判断仍在 Codex，方向 / 内容 / 人感 / 下一轮变量仍由 ChatGPT / 用户拍板。
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `fixture_json_parse`: `passed`
- `old_action_file_map_compatibility`: `passed`
- `editing_decision_pack_fixture_validation`: `passed`
- `editing_decision_pack_supply_source`: `deepseek_passed`
- `editing_decision_pack_context_pack_validation`: `passed`
- `editing_decision_pack_fallback_status`: `not_used`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `已确认` 供料输出三件套存在：`dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json`。
- `已确认` manifest 已包含 `action = editing_decision_pack`、`request_validation_status = passed`、`supply_source = deepseek_passed`、`not_deepseek_conclusion = false`、`codex_next_input`。
- `已确认` 本轮只代表机制落地与最小样例验证；不代表 DeepSeek 已稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频剪辑任务已经验证通过。
- `已确认` 本轮未修改视频 / 音频 / 图片等媒体文件，未修改 `dist/latest_review_pack/`，未修改 `codex_log/current_publish_target.md`，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）` 或声音状态。
- `执行日志`：`codex_log/20260510_DeepSeek深度配合与自动补全闸门.md`
- `下一个目标`：用一个真实小范围视频剪辑 / 录屏放大 / 卡片插入任务验证 `editing_decision_pack（剪辑决策包）` 是否真的能减少 Codex 漏读、误剪和硬套旧 SOP。

## 20260510｜DeepSeek 默认供料模型切换为 v4-flash

- `已确认` 本轮将 DeepSeek readonly explorer 默认供料模型从 `deepseek-v4-pro` 切换为 `deepseek-v4-flash`。
- `已确认` `deepseek-v4-pro` 保留为复杂任务升级模型 / 备用模型。
- `已确认` `.env.example` 已同步为 `DEEPSEEK_MODEL=deepseek-v4-flash`，并新增 `DEEPSEEK_ESCALATION_MODEL=deepseek-v4-pro`。
- `已确认` 本地 `.env` 存在且 `DEEPSEEK_API_KEY = present_nonempty`；本轮只把 `.env` 中 `DEEPSEEK_MODEL` 本地改为 `deepseek-v4-flash`，未打印 API key，未提交 `.env`。
- `smoke_test`: `passed`
- `smoke_test_model`: `deepseek-v4-flash`
- `已确认` 本轮只证明默认模型配置与最小 readonly explorer 链路通过，不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260510_DeepSeek默认模型切换为v4flash.md`
- `下一个目标`：用 `deepseek-v4-flash` 跑一次真实小步供料任务，观察是否比 Pro 更稳定或更快。

## 20260510｜视频质量与反馈总控机制 V1

- `已确认` 本轮落地 `视频质量与反馈总控机制 V1`，目标是把《视频工厂》从固定 SOP 倾向收束为“质量机制 + 文案路由 + 复盘反馈”的执行前判断机制。
- `已确认` 三张机制卡已进入执行前机制：
  - `content_route_card（内容路由卡）`
  - `quality_lock_card（质量锁卡）`
  - `review_variable_card（复盘变量卡）`
- `已确认` 已在 `codex_source/01_execution_rules.md（Codex 执行规则）` 写入 `DeepSeek + 三卡机制执行闸门`，后续视频 / 文案 / 复盘 / reference 相关任务必须在 `route_decision（路由判断）` 中判断供料与三卡需求。
- `已确认` DeepSeek / fallback 参与了执行前和执行后两次供料观察：
  - `preflight_request`: `codex_log/supply_requests/20260510_quality_feedback_mechanism_preflight_request.json`
  - `postcheck_request`: `codex_log/supply_requests/20260510_quality_feedback_mechanism_postcheck_request.json`
- `preflight_supply_source`: `fallback_local_only`
- `postcheck_supply_source`: `fallback_local_only`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `deepseek_generation_unstable`: `true`
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）` 或声音状态。
- `已确认` 本轮不代表完整 `multi-agent runtime（多 agent 运行时）` 已完成，不代表机制已经被真实发布数据验证，也不代表 DeepSeek 已能稳定完成真实供料。
- `执行日志`：`codex_log/20260510_视频质量与反馈总控机制V1.md`
- `下一个目标`：用三卡机制跑一次真实内容 / 视频任务，不生成大视频，先做内容路由和复盘变量测试。

## 20260509｜DeepSeek 任务卡参与真实机制修正

- `已确认` 本轮新增真实 `supply_request（供料请求任务卡）`：`codex_log/supply_requests/20260509_reference_entry_supply_request.json`。
- `已确认` 已通过 `--request-file` 运行 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`，并读取 `dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json` 和 `latest_supply_manifest.json`。
- `supply_source`: `fallback_local_only`
- `request_validation_status`: `passed`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `已确认` 已基于供料包和原文件复核，只在 `codex_source/00_codex_readme.md` 补强 `reference / locked reference / visual route / fixed_material_anchor / 旧 SOP 风险` 类任务优先走 `supply_request + controller` 的入口说明。
- `已确认` 本轮未修改 `GPT数据源/*`、DeepSeek 脚本、视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek任务卡参与真实机制修正.md`
- `下一个目标`：下一轮可以用任务卡机制参与一个更真实的 Codex 执行任务。

## 20260509｜DeepSeek 供料请求任务卡机制

- `已确认` 本轮新增 `codex_source/18_deepseek_supply_request_schema.md（DeepSeek 供料请求结构说明）`，定义 DeepSeek 每次供料前必须读取的 `supply_request（供料请求任务卡）`。
- `已确认` 已新增 JSON Schema：`codex_source/schemas/deepseek_supply_request.schema.json`。
- `已确认` 已新增样例任务卡：`codex_source/fixtures/deepseek_supply_request_file_map_example.json`、`codex_source/fixtures/deepseek_supply_request_risk_report_example.json`。
- `已确认` `scripts/deepseek_supply_controller.py` 已支持 `--request-file`，并保持旧 CLI 参数兼容。
- `已确认` request validation 可阻断缺字段 / 非法 action / 非法 trigger / forbidden path；负向 `.env` 请求已 blocked，未读取 `.env`。
- `test_legacy_cli`: `fallback_local_only`
- `test_request_file_map`: `fallback_local_only`
- `test_request_file_risk_report`: `fallback_local_only`
- `negative_test_forbidden_env`: `blocked`
- `已确认` 供料包与 manifest 已写入 `request_id`、`request_validation_status`、`current_goal`、`current_step`、`known_context`、`missing_context`、`decision_needed`。
- `已确认` 本轮未修改业务机制正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek供料请求任务卡机制.md`
- `下一个目标`：用标准 supply request 参与一次真实 Codex 机制修正任务。

## 20260509｜DeepSeek 供料中控最小机制

- `已确认` 本轮新增 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`，把 DeepSeek 从单次供料脚本升级为可触发、可回流、可兜底的最小中控入口。
- `已确认` 已新增 `codex_source/17_deepseek_supply_controller_protocol.md（DeepSeek 供料中控协议）`，写清触发机制、行动机制、范围机制和回流机制。
- `已确认` controller 支持 `file_map`、`risk_report`、`context_summary`、`missing_files`、`auto` 五类 action。
- `已确认` 输出回流路径为 `dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json`。
- `test_file_map`: `deepseek_passed`
- `test_risk_report`: `fallback_local_only`
- `pipeline_status`: `usable_with_fallback`
- `已确认` 本轮未修改业务机制正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek供料中控最小机制.md`
- `下一个目标`：用 supply controller 参与一次真实 Codex 机制修正任务。

## 20260509｜reference 质量机制锁最小测试

- `已确认` 本轮用 `DeepSeek readonly explorer` 先为 `reference` 质量机制锁修正生成资料包，再由 `Codex` 做最小范围机制修正。
- `已确认` 本轮供料来源是：`fallback_local_only`，不是 DeepSeek 真实任务稳定生成通过。
- `已确认` 已在 `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`、`GPT数据源/05_文案路由规则.md` 进一步写清：锁质量，不锁流程；文案驱动实时路由；`reference`、`locked reference`、`visual route` 不等于固定镜头 SOP。
- `已确认` 本轮未修改机制文件以外的项目正文，未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_reference质量机制锁最小测试.md`
- `下一个目标`：基于这次最小测试结果，继续推进 `reference` 质量机制锁修正的下一轮收口。

## 20260509｜DeepSeek 只读供料管线稳定性修复

- `已确认` 本轮把 `scripts/deepseek_readonly_explorer.py` 从单次最小调用扩展为稳定供料管线：加入输入压缩、三次受控重试、schema 校验和 local fallback。
- `已确认` smoke test 通过：`api_validation = passed`、`deepseek_generation_status = passed`、`context_pack_validation = passed`、`fallback_status = not_used`。
- `部分成立` 真实任务测试未拿到稳定 DeepSeek JSON，但 fallback 成功生成了 Codex 可读资料包。
- `real_task_pipeline_status`: `usable_with_fallback`
- `real_task_generation_status`: `failed`
- `real_task_context_pack_validation`: `fallback_local_only`
- `已确认` 当前可稳定给 Codex 提供资料，但这份真实任务资料包来自 local fallback，不是 DeepSeek passed。
- `已确认` 本轮未修改机制文件正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读供料管线稳定性修复.md`
- `下一个目标`：再让 DeepSeek 供料，Codex 执行 `reference` 质量机制锁修正。

## 20260509｜DeepSeek 只读探索器最小真实任务测试

- `已确认` 本轮只做 DeepSeek readonly explorer 最小真实任务测试，不修改机制文件正文。
- `已确认` 为承载真实任务测试，`scripts/deepseek_readonly_explorer.py` 仅做了最小可逆扩展：支持 `--task`、`--context-file`，并把请求超时提高到 `60s`。
- `部分成立` DeepSeek 已进入真实低风险任务调用阶段，但本轮未产出有效上下文包。
- `deepseek_test_result`: `blocked`
- `原因`：真实任务测试中先后出现 `timeout`、`truncated_json`、`empty_content`；最终输出未能稳定形成四字段上下文包。
- `已确认` 本轮没有出现写文件越权、拍板项目事实或把多 agent runtime 写成已跑通的内容。
- `已确认` 本轮未修改机制文件正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器最小真实任务测试.md`
- `下一个目标`：根据这次 blocked 结果，决定是否进入“reference 质量机制锁”规则修正，或先继续收紧 readonly explorer 的任务输入与输出约束。

## 20260509｜DeepSeek 正式事实口径同步

- `已确认` 本轮只同步 `GPT数据源/08_当前正式事实.md` 的 DeepSeek 正式事实口径。
- `已确认` 已把旧口径 `DeepSeek API 尚未接入` 改写为当前已验证口径：`api_validation = passed`、`context_pack_validation = passed`、`model = deepseek-v4-pro`。
- `已确认` 已同步写清：这只代表 readonly explorer 最小 API 调用链和四字段上下文包结构验证通过，不代表多 agent runtime 已跑通。
- `已确认` 本轮没有重新修改脚本，没有重新推进视频、声音、发布状态，也没有把 `context_pack_validation = passed` 写成生产执行通过。
- `执行日志`：`codex_log/20260509_DeepSeek正式事实口径同步.md`
- `下一个目标`：用 DeepSeek readonly explorer 为一次真实 Codex 任务生成上下文包。

## 20260509｜DeepSeek readonly explorer 输出结构修复

- `已确认` 本轮修复 `scripts/deepseek_readonly_explorer.py` 的输出结构约束。
- `已确认` DeepSeek API 仍使用 `deepseek-v4-pro`。
- `已确认` 已启用 JSON Output，并要求四个顶层字段：`prefetch_context_pack`、`must_read_file_map`、`risk_and_conflict_report`、`candidate_summary`。
- `已确认` 脚本已对四个顶层字段做本地校验，缺任一字段即写 `context_pack_validation = failed_unexpected_output` 并返回非 0。
- `api_validation`: `passed`
- `context_pack_validation`: `passed`
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器输出结构修复.md`
- `下一个目标`：用 DeepSeek readonly explorer 为一次真实 Codex 任务生成上下文包。

## 20260509｜DeepSeek readonly explorer API 复测

- `已确认` 本轮只重跑 DeepSeek readonly explorer 最小 API 验证。
- `已确认` `.env` 存在，且 `DEEPSEEK_API_KEY = present_nonempty`；本轮未打印 API key。
- `已确认` 当前模型配置为：`deepseek-v4-pro`。
- `api_validation`: `passed`
- `context_pack_validation`: `failed_unexpected_output`
- `说明`：DeepSeek API 调用链已真实返回成功，但本轮生成的 `latest_prefetch_context_pack.md` 缺少 `risk_and_conflict_report` 与 `candidate_summary` 两个要求字段，因此还不能写成“有效上下文包已通过”。
- `已确认` 这只证明 DeepSeek readonly explorer 最小 API 调用通过，不代表多 agent runtime 已跑通。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器API复测.md`
- `下一个目标`：修正 readonly explorer 输出结构约束后，再用 DeepSeek 为一次真实 Codex 任务生成完整上下文包。

## 20260509｜DeepSeek readonly explorer 模型锁定与最小验证

- `已确认` 已把 DeepSeek readonly explorer 默认模型锁定为：`deepseek-v4-pro`。
- `已确认` 已把 `.env.example` 示例变量更新为：`DEEPSEEK_BASE_URL=https://api.deepseek.com`、`DEEPSEEK_MODEL=deepseek-v4-pro`。
- `已确认` 已新增：
  - `codex_source/16_deepseek_readonly_explorer_rules.md`
  - `scripts/deepseek_readonly_explorer.py`
- `部分成立` 最小只读验证脚本已执行，并已生成本地验证输出：
  `dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md`
- `待验证` 当前真实 API 调用未通过，因为本地 `.env` 中未检测到 `DEEPSEEK_API_KEY`；因此本轮不能写成 `DeepSeek readonly explorer API validation passed`。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、代码逻辑、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器模型锁定与最小验证.md`
- `下一个目标`：用户先在 `.env` 中补齐 `DEEPSEEK_API_KEY`，再重跑 readonly explorer 最小 API 验证。

## 20260509｜GPT Project 上传包地址修复

- `已确认` 已审计 ChatGPT 之前给出的旧地址与 Codex 新上传包地址不一致问题。
- `已确认` 已生成唯一 GPT Project 上传包目录：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`
- `已确认` 以后 GPT Project 上传地址必须由 Codex 本地审计或 `current_local_artifact_paths.md` 给出，ChatGPT 不得凭记忆口头给地址。
- `已确认` 本轮未修改视频产物、代码、当前发布状态、`content_validation`、`send_ready`、声音产物。
- `执行日志`：`codex_log/20260509_GPT_Project上传包地址修复.md`
- `下一个目标`：用户使用 canonical upload package path 上传新版 GPT Project 资料包；上传后 ChatGPT 再按该包检查是否生效。

## 20260509｜OPC 入口读取口径收尾

- `已确认` 已把 `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 加入 `AGENTS.md` 的《视频工厂》最小读取顺序。
- `已确认` 已把《视频工厂》正式来源从“10 份执行包”更新为“10 份基础执行包 + 1 份 OPC 总纲机制文件”。
- `已确认` 已把 OPC 上位身份、多 AI 协作分工、DeepSeek 只读供料层、Codex 唯一写入 Integrator、reference 机制锁同步回仓库总入口。
- `已确认` 本轮只修改仓库入口读取口径，未修改视频产物、代码、当前发布状态、`content_validation`、`send_ready`、声音产物。
- `执行日志`：`codex_log/20260509_OPC入口读取口径收尾.md`
- `下一个目标`：基于 OPC 新口径，重新设计内容选题与展示层；如用户确认，再进入 DeepSeek 只读供料层 API 接入验证。

## 20260509｜OPC 一人公司闭环与多 AI 协作机制升级

- `已确认` 本轮只修改项目口径 / 机制 / 路由文件，未执行视频产物、代码、DeepSeek API 或多 agent runtime。
- `已确认` 已新增 OPC 总纲机制文件：`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`。
- `已确认` 已把项目身份升级为：`OPC 一人公司 AI 闭环验证系统`。
- `已确认` 已把多 AI 协作写成默认架构：`ChatGPT（总控脑 / 判断层）`、`Codex（唯一写入执行层 / Integrator）`、`DeepSeek（只读供料层 / Explorer）`、`Perplexity（外部研究层）`。
- `已确认` 已把 DeepSeek 定义为只读供料层，不写文件、不拍板项目事实、不替代 Codex 验证。
- `已确认` 已保持 Codex 为唯一写入 `Integrator（统一执行者）`。
- `已确认` 已把 `reference（参考）`、`reference_quality_sample（参考质量样片）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 从流程锁升级为机制判断锁：锁质量机制，不锁死固定流程。
- `已确认` 本轮未修改视频产物、声音 / TTS 产物、图片 / 卡片 / 素材产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、`voice_validation`、`final_voice_validated`。
- `执行日志`：`codex_log/20260509_OPC一人公司闭环与多AI协作机制升级.md`
- `下一个目标`：基于 OPC 新口径，重新设计内容选题与展示层，并决定是否进入 DeepSeek 只读供料层 API 接入验证。

## 20260509｜口径一致性修复

- `已确认` 已把 `latest.md` 中的新口径继续收口到当前动态事实执行包核心文件里。
- `已确认` 当前唯一远端主线 / 默认主读取分支仍统一为：`main`；`codex/user-readable-map` 只保留在历史日志正文或显式历史分支引用说明里。
- `已确认` 当前项目中心价值仍统一为：`真实 AI 使用经验 + 工作提效实录`。
- `已确认` `场景化专业输出工作包` 仍只作为：`可选沉淀单元 / 产品化承接单元`，不是每条视频默认主目标。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`current_publish_target`、`content_validation`、`send_ready`、归档区或任何媒体文件。
- `治理报告`：`治理_reports/20260509_口径一致性修复_branch_and_value_consistency_fix/口径一致性修复报告_branch_and_value_consistency_fix_report.md`
- `执行日志`：`codex_log/20260509_口径一致性修复_branch_and_value_consistency_fix.md`
- `下一个目标`：结束口径修补，回到当前视频工厂主线内容验证与发布后复盘执行。

## 20260509｜main主线与项目中心价值口径统一

- `已确认` 当前唯一远端主线 / 默认主读取分支已统一为：`main`。
- `已确认` 当前项目中心价值已统一为：`真实 AI 使用经验 + 工作提效实录`。
- `已确认` `场景化专业输出工作包` 已降级为：`可选沉淀单元 / 产品化承接单元`，不再要求每条视频默认生成工作包。
- `已确认` 当前内容优先验证：真实经验、工作提效证据、真实录屏、前后变化、小样本平台反馈与发布后复盘。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready` 或当前发布状态。
- `治理报告`：`治理_reports/20260509_main主线与项目中心价值口径统一_main_branch_and_value_alignment/main主线与项目中心价值口径统一报告_main_branch_and_value_alignment_report.md`
- `执行日志`：`codex_log/20260509_main主线与项目中心价值口径统一_main_branch_and_value_alignment.md`
- `下一个目标`：清理线结束后，回到当前视频工厂主线，继续围绕真实 AI 使用经验、工作提效实录与发布后复盘推进内容验证。

## 20260509｜最终收尾与 GitHub 分支清理

- `已确认` 本地收尾已完成：`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 已入库，工作树不再残留未跟踪规则文件。
- `已确认` 历史路径引用已收口：当前正式资料中涉及 `round28 voice clone trial` 的路径已改成 archive-only 外部目录口径；外部 archive 指针文件已存在。
- `已确认` 远端分支已按当前主线清理：当前保留 `main` 为唯一远端主线；`origin/HEAD -> origin/main` 仍作为符号引用存在。
- `说明`：脚本结果中的 `origin` 是远端伪引用，不是实际业务分支；删除返回 `remote ref does not exist`，已记入 blocked，但不影响主线清理完成。
- `治理报告`：`治理_reports/20260509_最终收尾_finalize_slimming_and_branch_cleanup/最终收尾报告_finalize_slimming_and_branch_cleanup.md`
- `下一个目标`：清理线结束，下一步可以回到视频工厂当前主线执行。

## 20260509｜一步瘦身

- `已确认` 已完成《视频工厂》主工作区一步瘦身。
- `已确认` 主工作区体积：`32G -> 1.1G`。
- `已确认` `.git` 体积：`21G -> 927M`。
- `已确认` `素材录制/`：`11G -> 55M`，仅保留当前语音样本锚点。
- `已确认` 已外移的大类：
  - `原始素材归档_raw_recordings_archive/`
  - `旧声音试配_voice_trials_archive/`
  - `旧参考包_reference_packs_archive/`
  - `旧媒体产物_old_media_outputs/`
  - `Git临时包归档_git_tmp_pack_archive/`
- `已确认` 当前仍保留在主工作区的核心对象：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与 reference 包
  - `素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
  - `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`
- `已确认` 外部 archive-only 目录：`/Users/fan/Documents/视频工厂归档+删除`
- `已确认` 本轮未删除任何业务文件，未做 history rewrite，未 force push。
- `治理报告`：`治理_reports/20260509_一步瘦身_one_pass_workspace_slimming/一步瘦身报告_one_pass_workspace_slimming_report.md`
- `执行日志`：`codex_log/20260509_一步瘦身_one_pass_workspace_slimming.md`
- `下一个目标`：清理并改写仍残留在正式资料中的历史路径引用，再决定是否继续外移最后 1 组历史 voice clone trial。

## 20260508｜主工作区与外部归档删除区分离

- `已确认` 已创建 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除`。
- `已确认` 已把以下旧媒体 / 旧产物 / 待确认大目录外移出主工作区：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`
  - `dist/voice_trials/20260425_round28_10s_voice_trial/`
  - `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`
  - `dist/完整成片_full_videos/`
  - `本地归档_local_archive/`
  - `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
  - `样片报告_sample_reports/`
  - `dist/prototypes/`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - 内部 archive zone 中已归档的旧媒体 payload
- `已确认` 当前主工作区继续保留：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与当前 reference 包
  - `素材录制/`
  - `素材库_assets/`
- `已确认` `/Users/fan/Documents/视频工厂归档+删除` 只作为 archive-only 外部目录，不是执行工作区，不是 fresh clone，不是 worktree。
- `下一个目标`：清理并重写内部 archive 指针清单，让后续会话只把外部目录当归档池，不再把内部旧路径当真实存放位置。

## 20260508｜历史产物归档审计与迁移

- `已确认` 已完成第二轮历史产物扫描：`dist/`、`复审包_review_packs/`、`验证_reports/`、`样片报告_sample_reports/`、`素材检查_reports/`、`本地归档_local_archive/`。
- `已确认` 已迁移 1 组明确旧产物候选：`验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/` -> `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/...`
- `已确认` 已迁移 3 组本地未跟踪旧媒体输出到：`归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/`
- `已确认` 当前继续保留不动：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与 reference 包
  - `素材录制/`
  - `素材库_assets/`
- `已确认` 本轮未删除任何文件。
- `治理报告`：`治理_reports/20260508_历史产物归档审计与迁移_old_artifacts_archive_audit/历史产物归档审计与迁移报告_old_artifacts_archive_audit_report.md`
- `执行日志`：`codex_log/20260508_历史产物归档审计与迁移_old_artifacts_archive_audit.md`
- `下一个目标`：先拆 `voice_trials/` 与 `reference_packs/` 的 current reference / pure history 边界，再做下一轮更细的历史产物迁移。

## 20260508｜主工作区与归档删除区分离

- `已确认` 已在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内创建 `归档删除区_archive_delete_zone/`。
- `已确认` 已隔离旧口径：`project_source/07_current_formal_facts.md`。
- `已确认` 已隔离旧入口：`codex_source/00_current_repo_audit.md`、`codex_source/02_codex_index.md`、`codex_source/07_formal_api_demo_target_plan.md`。
- `已确认` 已隔离 `dist/latest_review_pack/` 中明确旧副本：
  - 全部 `AI做PPT踩坑_成品候选_v3_*`
  - `AI做PPT踩坑_成品候选_v31_review_manifest.md`
  - `AI做PPT踩坑_成品候选_v31_summary.json`
- `已确认` 当前 P0 / P1 保留不动：`GPT数据源/`、`review_loop/`、`dist/latest_review_pack/` 当前正式入口、当前代码 / 工作台执行层、`素材库_assets/`、`素材录制/`。
- `已确认` 本轮未删除任何文件。
- `治理报告`：`治理_reports/20260508_主工作区与归档删除区分离_main_vs_archive_delete_split/主工作区与归档删除区分离报告_main_vs_archive_delete_split_report.md`
- `执行日志`：`codex_log/20260508_主工作区与归档删除区分离_main_vs_archive_delete_split.md`
- `下一个目标`：先处理 `执行日志_codex_log/` 与 root demo 入口降权，再决定下一轮待归档 / 待删除候选。

## 20260508｜新老文件分区与旧口径污染源审计

- `已确认` 已完成《视频工厂》唯一正式工作区 `/Users/fan/Documents/视频工厂` 的“新老文件分区与旧口径污染源审计”。
- `已确认` 本轮只做只读审计 + 报告落库；未删除、未移动、未重命名任何文件，未修改 `dist/latest_review_pack/`、`current_publish_target`、`content_validation`、`send_ready`、`GPT 数据源/` 或 `GPT数据源/` 当前 10 份执行包。
- `已确认` 当前正式核心区已收束到：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_log/latest.md`、`codex_log/current_*`、`GPT数据源/`、`review_loop/`、`dist/latest_review_pack/` 与当前代码 / 工作台执行层。
- `已确认` 已发现高风险污染源：
  - `执行日志_codex_log/最新摘要_latest.md` 仍是直播项目旧摘要，但 `AGENTS.md` 默认执行规则仍提到它。
  - `project_source/07_current_formal_facts.md` 仍保留历史“通过 / 可直接发送”样片口径，且仍被 `project_source` 多个入口文件引用。
  - `codex_source/02_codex_index.md`、`00_current_repo_audit.md`、`07_formal_api_demo_target_plan.md` 仍保留启动期 / demo 导航语义。
  - `dist/latest_review_pack/` 内同目录并存当前灰测口径文件与旧 v3 / 旧 v3.1 副本文件。
- `治理报告`：`治理_reports/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit/新老文件分区与旧口径污染源审计报告_file_partition_and_stale_context_audit_report.md`
- `执行日志`：`codex_log/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit.md`
- `下一个目标`：先做入口级旧口径降权与引用修正，再决定哪些历史产物进入归档候选、哪些纯缓存对象进入删除候选。

## 20260505｜复盘到文案调整桥接

- `已确认` 已新增复盘到文案调整桥接规则：`review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md`。
- `已确认` 已新增文案结构改版包模板：`review_loop/10_文案结构改版包模板_copy_revision_package_template.md`。
- `已确认` 已为 V002《自动流的最简单流程》生成复盘到文案调整桥接记录：`review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_复盘到文案调整桥接_review_to_copy_revision_bridge.md`。
- `已确认` 当前 V002b 仍是安全版文案结构草案，不是最终稿，不是已发布版本。
- `执行日志`：`codex_log/20260505_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `下一个目标`：由 ChatGPT / 用户确认 V002b 文案结构，再决定是否进入录制 / 剪辑 / 发布前风险检查。

## 20260505｜发布前平台风险检查规则

- `已确认` 已基于 V002《自动流的最简单流程》新增发布前平台风险检查规则：`review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`。
- `已确认` V002 不再只作为单条数据记录，也作为第一条发布前平台风险样本；其身份仍是 `policy_distribution_limited（平台审核减推 / 分发受限）` 与 `abnormal_distribution_sample（异常分发样本）`，不是内容失败样本。
- `已确认` 后续 AI 工作流 / AI 教程 / 自动化流程 / 工具操作演示 / 命令行或 IDE 画面展示类视频，发布前必须先检查标题、封面、字幕、画面文字、工具界面、命令行、结尾动作、简介和评论区引导中的平台风险表达。
- `已确认` 已在 `review_loop/00_review_loop_readme.md` 与 `codex_source/00_codex_readme.md` 增加最小入口引用；未修改当前 v3.1 视频状态、`content_validation`、`send_ready`、`dist/latest_review_pack/`、`GPT 数据源/` 或 `GPT数据源/`。
- `执行日志`：`codex_log/20260505_发布前平台风险检查规则_pre_publish_platform_risk_check.md`
- `下一个目标`：后续发布类似 AI 工作流 / 自动化流程类视频前，先输出平台风险检查结果，再决定是否允许发布、必须改写或阻断。

## 20260505｜《自动流的最简单流程》抖音审核减推记录

- `已确认` 已为《自动流的最简单流程》建立独立 `video_id = V002` 发布后复盘记录，未混入 V001 v3.1 灰度测试记录。
- `已确认` 已记录抖音审核通知：`review_result = 减少作品推荐`，`violation_reason = 引导至风险不可控渠道`，`reason_surface = 画面`。
- `已确认` 已记录用户确认数据：播放量 39、点赞 5、收藏 8；计算字段为点赞率 12.82%、收藏率 20.51%、点赞 + 收藏动作率 33.33%。
- `已确认` V002 已标记为 `policy_distribution_limited（平台审核减推 / 分发受限）` 与 `abnormal_distribution_sample（异常分发样本）`；不得作为正常自然流量样本或内容失败结论。
- `已确认` 本轮未修改当前 v3.1 视频状态、`content_validation`、`send_ready`、`dist/latest_review_pack/`、`GPT 数据源/` 或 `GPT数据源/`。
- `执行日志`：`codex_log/20260505_抖音减少推荐审核记录_douyin_reduce_recommendation_notice.md`
- `下一个目标`：ChatGPT / 用户基于 V002 复盘输入判断该样本最终归为排除样本还是可参考异常样本，并拍板下一轮唯一优先改点是否锁定为发布包装 / 风险表达 / 画面触发点。

## 20260505｜大任务闸门 large_task_gate

- `已确认` 本轮只补 `large_task_gate（大任务闸门）` 机制；未修改视频产物、未生成样片、未继续项目清理、未调整剪辑风格、未开发真正 multi-agent 系统。
- `已确认` `AGENTS.md` 已在 `route_decision_gate（执行前路由闸门）` 后补 `### 2.6A 大任务闸门 large_task_gate`。
- `已确认` `codex_source/01_execution_rules.md` 已补 `## 2C. large_task_gate 大任务闸门`，并把 `large_task_gate` 加入 `route_decision（路由判断）` 输出字段。
- `已确认` 规则已写入：任何视频 / 样片 / 成片 / 剪辑对象超过 `3 分钟 / 180 秒`，必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 规则已写入：多文件、多步骤、多验证、多模块，或“写文件 + 检查 + 日志 + push / 同步”等闭环任务，也必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 触发后必须读取 `codex_source/13_execution_lane_and_parallel_rules.md` 与 `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`，并输出 `lane_recommendation` 与 `parallel_recommendation`。
- `已确认` 规则已明确：触发大任务闸门不等于自动多 agent，不等于默认并发；写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定时，必须保持或降级为 `serial_only（串行执行）`。
- `已确认` 本轮未修改 `dist/latest_review_pack/`、当前发布状态、`content_validation`、`send_ready`，未处理 `素材录制/`，未新建外部工作区，未执行 Git GC / prune / repack / LFS / history rewrite / force push。
- `执行日志`：`codex_log/20260505_大任务闸门_large_task_gate.md`
- `下一个目标`：后续 Codex 看到超过 3 分钟视频、多文件、多步骤、多验证任务时，先自动触发 `large_task_gate（大任务闸门）` 并完成 lane / parallel 判断。

## 20260505｜Codex 执行前路由闸门

- `已确认` 本轮只把《视频工厂》的 Codex 执行机制升级为 `route_decision_gate（执行前路由闸门）`；未修改视频产物、未生成样片、未继续清理、未处理 `素材录制/`。
- `已确认` `AGENTS.md` 已新增 `## 2.6 Codex 执行前路由闸门 route_decision_gate`，要求每次执行前先输出项目路由、任务类型、责任层级、必读文件、读取状态、允许 / 禁止修改范围、阻断条件和执行许可。
- `已确认` `AGENTS.md` 的默认执行规则已补入：执行前必须先输出并通过 `route_decision（路由判断）`；未通过前不得修改任何文件。
- `已确认` `codex_source/01_execution_rules.md` 已新增 `## 2A. 执行前 route_decision 闸门` 与 `## 2B. 任务类型与必读文件映射`。
- `已确认` 任务类型映射已覆盖：项目文件修改 / 机制修补 / 路由修补、视频样片 / 成片 / 样片回炉、文案写作 / 改写、复盘 / 诊断 / 审核、数据记录 / 灰度复盘、本地文件治理 / 工作区治理、execution lane / multi-agent / parallel 机制。
- `已确认` `codex_source/00_codex_readme.md` 已做最小同步：每次 Codex 执行前必须先通过 `route_decision（路由判断）`。
- `已确认` 本轮未修改 `dist/latest_review_pack/`，未修改当前发布状态、`content_validation`、`send_ready`，未新建外部工作区，未执行 Git GC / prune / repack / LFS / history rewrite / force push。
- `执行日志`：`codex_log/20260505_Codex执行前路由闸门_codex_route_decision_gate.md`
- `下一个目标`：后续新会话在任何文件修改或执行前，先给出 `route_decision（路由判断）` 与 `read_status（读取状态）`，再判断是否允许执行。

## 20260505｜fresh clone 外部目录收回与工作区锁死

- `已确认` 本轮只做 PR #50 fresh clone 审计目录收回与 `single_workspace_rule（单工作区硬规则）` 加固；未继续项目清理，未处理 `素材录制/`，未修改当前视频产物或发布状态。
- `已确认` 外部散目录 `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 已收回到唯一正式工作区内部：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260504/视频工厂_fresh_clone_audit_20260504`。
- `已确认` `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 已不再作为 `/Users/fan/Documents` 顶层散目录存在。
- `已确认` 回收目录大小约 `975M`，文件数 `633`，目录数 `100`；内部包含嵌套 `.git/`，仅作为归档内容保留，不提交、不当子模块处理。
- `已确认` `.gitignore` 既有规则已忽略 `本地归档_local_archive/`；`git status --short` 未出现 fresh clone 大目录待提交项，因此本轮未改 `.gitignore`。
- `已确认` 已同步加固 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`：Codex 不得默认新建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区；确需外部目录必须先停止并等待用户明确确认。
- `已确认` 本轮未替换正式工作区，未删除正式工作区，未执行 `git gc` / `git prune` / `git repack`，未执行 Git LFS / history rewrite，未 force push，未修改 `content_validation` 或 `send_ready`。
- `执行日志`：`codex_log/20260505_fresh_clone外部目录收回与工作区锁死_workspace_lock_recovery.md`
- `下一个目标`：新会话默认只在 `/Users/fan/Documents/视频工厂` 唯一正式工作区内执行；如未来确需外部对照，先由 Codex 停止回报并等待用户明确确认。

## 20260504｜PR 合并与 fresh clone 体积对照验证

- `已确认` PR #48「Pre-upgrade delete old Video Factory assets」已合并到 `codex/user-readable-map`，merge commit：`d2df313920e1d7e4f720db279964d6a2324b06a1`。
- `已确认` PR #49「Audit Git history large files without cleanup」已合并到 `codex/user-readable-map`，merge commit：`a1981935e404a78377e121b0643601cad01e483a`。
- `已确认` PR #48 合并前已复核：`fixed_material_anchor（固定素材锚点）` 与 `reference_whitelist（参考白名单）` 已区分；TTS pacing / TTS voice 已区分；round34 中段最小参考、PR #7 B、cute card、TTS pacing、TTS voice candidate 均保留。
- `已确认` PR #49 合并前已复核：它是 Git 历史大文件只读审计，不包含 Git 清理、LFS 迁移、history rewrite 或发布状态修改。
- `已确认` fresh clone 已完成，目录为 `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504`，当前 checkout 分支为 `codex/user-readable-map`。
- `已确认` 正式工作区 `/Users/fan/Documents/视频工厂` 当前总大小约 `33G`，`.git` 约 `21G`，`.git/objects/pack` 约 `19G`，`素材录制/` 约 `11G`。
- `已确认` fresh clone 当前总大小约 `980M`，`.git` 约 `896M`，`.git/objects/pack` 约 `896M`。
- `已确认` 正式工作区 `.git/objects/pack/tmp_pack_*` 为 `28` 个，约 `15.49 GiB`；fresh clone `tmp_pack_*` 为 `0`，`git count-objects -vH` 显示 `garbage = 0`、`size-garbage = 0 bytes`。
- `结论`：正式工作区 `.git` 约 `21G` 主要来自当前本地 `tmp_pack_*` garbage；fresh clone 已显著变小，因此下一轮优先考虑 clean clone 迁移确认，不建议直接做 Git history rewrite。
- `已确认` 本轮未替换正式工作区，未删除正式工作区，未执行 `git gc` / `git prune` / `git repack` / `git lfs migrate` / `filter-repo` / `filter-branch` / BFG，未 force push，未修改当前发布状态。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 仍保持 `untracked / frozen / untouched`，本轮未纳入、未删除、未移动、未重命名、未修改。
- `治理报告`：`治理_reports/20260504_fresh_clone体积对照验证_fresh_clone_size_comparison/fresh_clone体积对照验证报告_fresh_clone_size_comparison_report.md`
- `下一个目标`：用户 / ChatGPT 复审 fresh clone 对照报告，再决定是否迁移到 fresh clone 工作区，或继续处理 `素材录制/` 原始素材。

## 20260504｜Git 历史大文件只读审计

- `已确认` 本轮从最新 `codex/user-readable-map` 创建只读审计分支：`codex/git-history-large-files-audit-20260504`。
- `已确认` 本轮只审计 `.git` 历史大文件来源；未删除、未移动、未重命名任何文件。
- `已确认` 未执行 `git gc`、`git prune`、`git repack`、`git lfs migrate`、`filter-repo`、`filter-branch`、BFG 或 force push。
- `已确认` `.git` 当前约 `21G`，`.git/objects` 约 `21G`，`.git/objects/pack` 约 `19G`，`.git/lfs` 不存在。
- `已确认` `git count-objects -vH` 报告 `size-garbage = 15.51 GiB`；`.git/objects/pack/tmp_pack_*` 临时包数量 `28`，合计约 `15.5 GiB`，是本地 `.git` 过大的最大直接来源。
- `已确认` 正式 pack 约 `3.99 GiB`，reachable 历史对象仍包含旧视频、旧音频、旧图片、旧复审包、旧 `dist/` 产物和历史 `node_modules/ffmpeg-static/ffmpeg`。
- `已确认` 当前工作树仍跟踪少量旧 `dist/` / `复审包_review_packs/` / `voice_trials` 媒体文件；本轮只记录，不做删除或迁移。
- `已确认` Git LFS 当前未安装 / 未配置，`.gitattributes` 不存在，本轮未做 LFS 迁移。
- `已确认` 已知冻结未追踪文件 `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 保持 `untracked / frozen / untouched`；本轮未纳入、未删除、未移动、未重命名、未修改。
- `推荐路线`：下一轮先做 fresh clone / clean clone 对照验证；如果远端历史仍大，再另起 Git LFS / history rewrite 方案。
- `治理报告`：`治理_reports/20260504_Git历史大文件只读审计_git_history_large_files_audit/Git历史大文件只读审计报告_git_history_large_files_audit_report.md`
- `下一个目标`：用户 / ChatGPT 复审 `.git` 历史大文件审计报告，再决定是否执行 Git LFS / 历史瘦身或重新 clone / 新建干净仓库。

## 20260504｜项目升级前旧资产清库

- `已确认` PR #48 追加清库口径修正：`v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）` 是当前唯一 `fixed_material_anchor（固定素材锚点）`，但元素娃娃不是唯一 reference。
- `已确认` reference whitelist 仍保留：`PR7_B_骚萌反应页.png`、cute card、round34 中段剪辑 / 证据窗口、`tts_15s_b_pacing_locked_20260427`、`visual_route_map.json`、`locked_reference_registry.md`；后续按路径索引和 registry 复核后使用。
- `已确认` PR #48 追加 TTS reference whitelist 修正：TTS reference 分为 `tts_pacing_reference（TTS 节奏参考）` 与 `tts_voice_reference（TTS 语音 / 音色参考）`；`voice_sample2_cute_guide_voice_candidate_20260426` 与脱敏 custom voice `qwen-t...ac19` 保留为语音 / 音色候选参考，`target_model = qwen3-tts-vc-realtime-2026-01-15`，但 `voice_validation` 仍为 `pending_user_chatgpt_review`，`final_voice_validated` 仍为 `false`。
- `已确认` round34 旧 817M 本地大包未恢复；但 `dist/latest_review_pack/middle_preview.mp4`、`cut_contact_sheet.jpg`、`problem_windows/30_32s.mp4`、`problem_windows/30_32s_frames.jpg` 均仍存在，并已在路径索引恢复为 `path_exists = true`。
- `已确认` PR #47 已先合并到 `codex/user-readable-map`，合并提交：`20d9419e0a9ad048075a2138c610472df93051be`。
- `已确认` 本轮从合并后的主读取分支创建清库分支：`codex/pre-upgrade-delete-old-assets-20260504`。
- `已确认` 本轮不生成视频，不修改当前发布 / 灰度状态，不把 `content_validation` 写成 `passed`，不把 `send_ready` 写成 `true`。
- `已确认` 当前唯一固定素材锚点收束为：`v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）`。
- `已确认` `v31_element_doll_opening_preview（v3.1 元素娃娃开头预览）` 只保留开头预览证据，不代表元素娃娃继续做全片主持。
- `已确认` PR #46 未合并、未关闭、未删除；当前只作为未来流程 / 教学 / 操作拆解类视频升级方向资料，不作为当前 reference。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 目录本轮冻结不动。
- `已确认` 清理前工作区体积约 `36G`；清理后约 `33G`；释放约 `3G`。其中 `.git/` 约 `21G` 和 `素材录制/` 约 `11G` 本轮按禁止 / 不确定规则未动。
- `已确认` 清理后仍为约 `33G` 的主要原因是 `.git/（Git 系统目录）约 21G` 与 `素材录制/（用户录制原始素材）约 11G` 本轮按安全规则未动；下一轮若继续瘦身，必须分成两条独立任务：`Git 历史 / LFS 瘦身` 和 `原始录屏素材外置 / 删除确认`。
- `已确认` 已从 Git 当前树移除旧 `dist` 噪音目录，包括 20260414 / 20260417 旧视频产物、旧 demo、旧 latest 指针和 v3 dist 产物。
- `已确认` 已删除本地旧大目录 / 缓存：旧元素娃娃 1080P 复审包、旧本地归档、旧本地隔离区、旧 v1/v2/v3 复审包、旧视频样片缓存、临时产物、HyperFrames 测试输出、`node_modules`。
- `已确认` 已更新 `codex_log/current_local_artifact_paths.md`；v3 已删除路径不再保留 `path_exists = true`，round34 中段最小参考证据改用 `dist/latest_review_pack/` 现存文件并恢复为 `path_exists = true`。
- `待验证` `素材录制/` 仍为 blocked_unknown；如需进一步瘦身，需要用户另轮确认哪些原始录制素材可外置 / 删除。
- `治理报告`：`治理_reports/20260504_项目升级前旧资产清库_pre_upgrade_delete_old_assets/项目升级前旧资产清库报告_pre_upgrade_delete_old_assets_report.md`
- `下一个目标`：用户 / ChatGPT 复审清库 PR，确认没有误删保留内核；通过后再进入项目升级机制收口。

## 20260504｜元素娃娃开头保留与旧资产清理

- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/keep-element-doll-clean-old-assets-20260504`。
- `已确认` 已将 v3.1 元素娃娃开头锚点补入 `codex_log/current_local_artifact_paths.md`：`v31_element_doll_opening_anchor`。
- `已确认` 已将 v3.1 开头预览补入 `codex_log/current_local_artifact_paths.md`：`v31_element_doll_opening_preview`。
- `已确认` 两个路径均在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内，本轮 `test -f` 验证存在。
- `边界`：元素娃娃只保留开头价值，不代表继续做全片主持，不替代录屏主体，不替代真人判断段。
- `已确认` PR #46 本轮降权为 `parallel_future_flow_teaching_asset（未来流程 / 教学 / 操作拆解类视频升级方向资料）`；本轮未合并、未关闭、未删除，不作为当前 reference，不写成主读取分支正式状态。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 本轮冻结不动，不纳入、不删除、不移动、不改名。
- `已确认` 已先输出 `cleanup_audit（清理审计）`，再删除 `.DS_Store` Finder 临时文件。
- `部分成立` 删除前原计划排除冻结 / 保护范围，但 `find -delete` 的执行行为导致部分受保护目录内 `.DS_Store` 也被删除；被额外影响的对象仅为 Finder 临时元数据，不是业务文件。
- `已确认` 本轮未生成视频、未修改 `dist/latest_review_pack/` 当前结构地图文件、未修改 `codex_log/current_publish_target.md` 状态字段、未删除任何核心 reference 或 blocked_unknown。
- `已确认` `content_validation` 未写成 `passed`，`send_ready` 未写成 `true`，`voice_validation` 未写成 `final`，当前 v3.1 发布 / 灰度状态未修改。
- `治理报告`：`治理_reports/20260504_元素娃娃开头保留与旧资产清理_keep_element_doll_cleanup_old_assets/元素娃娃开头保留与旧资产清理报告_keep_element_doll_cleanup_old_assets_report.md`
- `下一个目标`：用户 / ChatGPT 复审本轮 PR，确认元素娃娃开头路径索引补充无误、旧资产清理未误删；通过后再进入项目升级前的机制收口。

## 20260503｜阿里云剪辑复接验证 after audit

- `已确认` PR #34「接入 HyperFrames 三类卡片动效边界并审计阿里云剪辑」已合并到 `codex/user-readable-map`，合并提交：`edbe61e512c972d75c786a53f82c9e3db53ecfb2`。
- `已确认` PR #35 已关闭并标记 `Superseded`，未合并。
- `已确认` 本轮从合并 PR #34 后的最新 `codex/user-readable-map` 创建分支：`codex/aliyun-editing-reconnect-validation-after-audit-20260503`。
- `已确认` 已读取前置阿里云剪辑使用审计报告。
- `已确认` 阿里云 OSS + ICE / 云剪最小云端总装链路已真实跑通：OSS 上传、ICE 工程更新、云剪任务提交、轮询、MP4 导出均完成。
- `已确认` 导出样片本地下载后通过 `ffprobe`：12 秒，1080x1920，H.264，AAC。
- `候选判断`：阿里云剪辑可以作为 vNext 云端总装候选继续评估，但本轮不代表正式链路已稳定。
- `已确认` 本轮未修改 v3.1 正片，未修改 `dist/latest_review_pack/` 既有产物，未修改 `current_publish_target`。
- `已确认` 本轮未生成正式视频，未写新文案，未处理 HyperFrames 中段录屏。
- `已确认` 内容验证字段未提升为最终通过态；发送状态字段未提升；未将本地样片、签名链接、原始运行结果或敏感凭据提交进 Git。
- `验证报告`：`验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/阿里云剪辑复接验证报告_after_audit_aliyun_editing_reconnect_validation_report.md`
- `下一个目标`：决定是否将阿里云剪辑作为 vNext 云端总装候选推进；若推进，先做 vNext 专用 timeline / manifest 设计和多素材兼容验证。

## 20260503｜HyperFrames 卡片动效边界与阿里云剪辑审计

- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/hyperframes-card-routing-and-aliyun-edit-audit-20260503`。
- `已确认` 本轮只做 HyperFrames 卡片动效接入规则设计与阿里云剪辑只读审计；未生成视频 / 音频 / 图片，未写新文案，未处理 HyperFrames 中段录屏接入。
- `已确认` 已先读取并核对 `dist/latest_review_pack/visual_route_map.json` 与 `visual_route_validation_report.json`；三类 HyperFrames 卡片动效均可挂回现有 route，未发现 route map 冲突。
- `已确认` 数据卡 / 结果差卡动效归属 `cute_info_card_route`，当前主要对应 `shot15_result_diff_card`；未来灰度数据卡 / 指标卡也只能作为该 route 扩展。
- `已确认` Prompt 引用尾卡动效归属 `cute_info_card_route`，对应 `shot16_low_pressure_ending`，只承担引用、低压收束和承接，不承担主叙事。
- `已确认` 骚萌卡动效版归属 `sassy_reaction_card_route`，对应 `shot03_problem_hook_sassy_card`、`shot05_negative_reversal_sassy_card`、`shot14_positive_reversal_sassy_card`，必须继承 PR #7 B 独立 reaction page 路线。
- `已确认` HyperFrames 当前只是 `card_motion_layer（卡片动效层）`，不是新视觉路由，不是中段录屏叠层，不是整条视频生成层，也不是云端剪辑替代品。
- `部分成立` 阿里云剪辑审计发现仓库仍保留阿里云 ICE / OSS 云端 assembly 代码路径和配置字段，也有历史云剪 / ICE 验证记录。
- `未发现当前实际调用证据` 当前 v3.1 `dist/latest_review_pack/` 未发现阿里云剪辑 / ICE assembly 调用记录；命中的阿里百炼内容属于 TTS / voice clone，不等于剪辑服务。
- `已确认` 本轮未修改 v3.1 正片，未修改 `dist/latest_review_pack/` 既有产物，`content_validation` 保持当前灰度测试口径，`send_ready` 保持 `false`。
- `治理报告`：`治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`
- `审计报告`：`治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/阿里云剪辑使用审计报告_aliyun_edit_usage_audit.md`
- `下一个目标`：ChatGPT 复审本轮 PR 是否可合并；若后续要处理阿里云剪辑保留 / 替换 / 降级，另起单独执行链路决策任务。

## 20260503｜Superpowers 历史工作区清理

- `已确认` PR #32「Enforce Video Factory single workspace cleanup」已 squash merge 到 `codex/user-readable-map`，合并提交：`2d7883a`。
- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/superpowers-worktree-cleanup-20260503`。
- `已确认` 本轮只处理两个指定 Superpowers 历史 worktree，不处理 HyperFrames 任务，不生成视频 / 音频 / 图片，不写新文案。
- `已确认` 两个 worktree 的 tracked diff、staged diff、untracked 文件数量均为 clean / `0`。
- `已确认` 两个 worktree 的 commit 均已存在于远端分支，没有未推送提交。
- `已确认` 本轮新增回收文件数量为 `0`，checksum 失败数量为 `0`。
- `已确认` 已执行普通 `git worktree remove` 移除两个历史 worktree；未使用 `--force`，未使用 `rm -rf`。
- `已确认` `git worktree list` 最终只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` `/Users/fan/Documents` 顶层仍只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` `content_validation` 保持发布后灰度测试口径，没有写成内容最终通过；`send_ready` 保持否定状态。
- `治理报告`：`治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_cleanup_report.md`
- `下一个目标`：后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内执行。

## 20260502｜单工作区清理归档

- `已确认` 本轮从 `origin/codex/user-readable-map` 创建治理分支：`codex/single-workspace-cleanup-from-user-readable-map-20260502`。
- `已确认` `/Users/fan/Documents` 顶层《视频工厂》相关目录已清理到只剩：`/Users/fan/Documents/视频工厂`。
- `已确认` 已回收外部目录唯一文件 `442` 个，回收目标为 `/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260502/`。
- `已确认` 回收文件 size 与 checksum 全部一致；失败项 `0` 个。
- `已确认` 已安全 `git worktree remove` 干净外部 / 历史 worktree `18` 个；已将 `3` 个非 Git / 损坏临时残留目录移动到唯一工作区内部隔离区。
- `部分成立` `git worktree list` 仍保留 2 个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree，因为它们有未跟踪文件，按安全规则标记 `blocked_need_user_review`，本轮未移除。
- `已确认` 已写入 `single_workspace_rule`：以后唯一正式工作区是 `/Users/fan/Documents/视频工厂`；新分支只能在此目录内创建 / 切换；不得默认创建 `/Users/fan/Documents/视频工厂_*` 外部工作区或外部 `git worktree add`。
- `已确认` `codex_log/current_local_artifact_paths.md` 已改为内部路径优先；所有 `canonical_local_path` 均指向 `/Users/fan/Documents/视频工厂` 内部；旧外部路径只保留为 `historical_source_path` 说明。
- `已确认` 本轮未生成视频 / 音频 / 图片，未写新文案，未处理 HyperFrames 卡片边界任务，未修改 v3.1 正片内容，未修改 `dist/latest_review_pack` 既有产物内容。
- `已确认` `content_validation` 未改成 `passed`，`send_ready` 未改成 `true`，本轮未永久删除未回收文件。
- `审计报告`：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/单工作区清理归档报告_single_workspace_cleanup_archive_report.md`
- `下一个目标`：用户确认两个 blocked superpowers 历史 worktree 后，另起一轮处理剩余 worktree；后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内执行。

## 20260502｜截图数据录入与时间窗分桶机制

- `已确认` 本轮只修《视频工厂》v3.1 发布后灰度测试的数据记录机制；未写新文案、未生成视频、未生成音频、未重新装配全片、未修改 v3.1 视频产物。
- `已确认` 当前工作分支：`codex/v31-screenshot-data-buckets-20260502`。
- `已确认` 截图优先录入机制已接入既有 `review_loop/`，不新建重复复盘系统。
- `已确认` 新增截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`。
- `已确认` 当前 v3.1 视频已建立独立记录目录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`。
- `已确认` 当前 v3.1 主记录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`。
- `已确认` 当前截图证据目录：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`。
- `已确认` 旧记录 `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md` 保留为兼容入口，并指向新的 V001 主记录目录。
- `已确认` 已新增按视频分桶：不同视频必须使用不同 `video_id` 和独立记录目录。
- `已确认` 已新增 `24h / 72h / 7d` 时间窗分桶：不同时间窗不得互相覆盖。
- `已确认` 已新增平台数据 / 留存完播 / 互动 / 账号增长 / 评论 / 私信 / 咨询 / 其他证据分类。
- `已确认` 已新增三份截图提取报告模板、缺失字段记录、给 ChatGPT 的复盘输入文件和 screenshot manifest。
- `已确认` 截图看不清或字段不确定时必须标记 `uncertain_need_human_check`；截图未提供字段必须标记 `missing`；不得硬猜。
- `已确认` Codex 后续只负责截图归档、字段提取、缺失标记、初检和交接；最终判断仍交给 ChatGPT / 用户。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照。
- `待验证` 发布平台、发布时间、视频链接、24h / 72h / 7 天截图和数据仍待用户提交。
- `下一个目标`：等待用户提交 v3.1 的 24h 截图；Codex 根据截图提取数据并更新 V001 记录；ChatGPT 根据四个复盘问题判断下一轮只改一个变量。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/00_review_loop_readme.md`
- `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/README_video_context.md`
- `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 灰度测试指标体系 V1 落仓库

- `已确认` 本轮只做 v3.1 发布后灰度测试指标体系 V1 落仓库，并接入既有 `review_loop/`；未写新文案、未生成视频、未生成音频、未重新装配全片、未修改 v3.1 视频产物。
- `已确认` 当前工作分支：`codex/v31-gray-test-metrics-v1-20260502`。
- `已确认` 当前状态仍为：`publish_status = gray_test_published`、`gray_test_status = active`、`current_phase = post_publish_gray_test`、`content_validation = gray_testing_not_final_passed`。
- `已确认` 新增指标体系文件：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`。
- `已确认` 当前灰度测试目标文件：`codex_log/current_gray_test_target.md` 已更新为 24h / 72h / 7 天观察。
- `已确认` 当前 v3.1 单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md` 已补入 7 天播放目标、三类字段和四个复盘问题。
- `已确认` 7 天播放量 6000 是当前小样本阶段基础测试流量门槛，不是最终商业目标。
- `已确认` 指标体系不是运营数据大表，而是下一轮改动定位器。
- `已确认` 四层指标已写入：流量层、内容层、账号增长层、私域 / 客户转化层。
- `已确认` 字段已分为：核心必填字段、辅助观察字段、商业线索出现时才填字段。
- `已确认` 后续复盘默认收成四个问题：是否达到 6000 播放基础门槛、最短板在哪一层、下一轮只改哪一个变量、为什么先改它并看哪个指标。
- `已确认` Codex 在发布后复盘中只做记录、初检、归档和下一轮任务草稿；最终判断仍交给 ChatGPT / 用户。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照。
- `待验证` 发布平台、发布时间、视频链接、24h / 72h / 7 天数据均待用户回填。
- `下一个目标`：等待用户回填 24h / 72h / 7 天数据；回填后 Codex 做初检，ChatGPT 根据四个复盘问题判断下一轮只改一个变量。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- `review_loop/00_review_loop_readme.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 发片灰度测试与复盘机制接入

- `已确认` 本轮只做 v3.1 发片状态回写、灰度测试目标设定、既有 `review_loop/` 发布后复盘机制接入和仓库口径同步；不写新文案、不生成视频、不生成音频、不重新装配全片。
- `已确认` 当前工作分支：`codex/v31-gray-test-review-loop-20260502`。
- `已确认` 当前阶段已写入：`current_phase = post_publish_gray_test（发布后灰度测试阶段）`。
- `已确认` 当前发布状态已写入：`publish_status = gray_test_published（v3.1 已发片，进入灰度测试）`。
- `已确认` 当前灰度状态已写入：`gray_test_status = active（灰度测试中）`。
- `已确认` 当前发布后复盘要求已写入：`post_publish_review_required = true`。
- `已确认` 当前内容状态已写入：`content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`。
- `已确认` 仍保持：`send_ready = false`、`visual_master_locked = false`、`voice_validation = pending_user_chatgpt_review`、`final_voice_validated = false`、`technical_upgrade_next = true`。
- `已确认` 发布后复盘默认接入既有 `review_loop/`，不新建独立灰度系统。
- `已确认` 新增当前灰度测试目标文件：`codex_log/current_gray_test_target.md`。
- `已确认` 新增 v3.1 单条灰度测试记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`。
- `已确认` 24h / 72h、一次只改一个变量、小样本状态、异常样本处理、规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照，不能作为后续执行参考。
- `待验证` 发布平台、发布时间、视频链接、24h 数据、72h 数据均待用户回填。
- `下一个目标`：等待用户补充发布平台、发布时间、视频链接和 24h 数据；24h 数据回填后，Codex 做初检，ChatGPT 做质量判断。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- `review_loop/00_review_loop_readme.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 当前基线切换与旧 PR 降噪

- `已确认` 本轮只做当前基线切换、v3.1 有效产物回流、旧 PR 降噪和仓库口径同步；不重新生成视频、不重新生成音频、不重新生成图片、不重新装配全片。
- `已确认` 已从最新 `codex/user-readable-map` 创建工作分支：`codex/v31-current-baseline-sync-20260502`。
- `已确认` PR #24 不能原样合并：它基于 PR #22 head，会回退 PR #25 的旧口径归档与入口清理结果。
- `已确认` 已安全回流 PR #24 的 v3.1 有效产物：`dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`、`复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`、`dist/latest_review_pack/` 中的 v3.1 当前入口。
- `已确认` 当前最新视频基线切换为：`current_video_baseline = v3.1`。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于：`future_iteration_base = v3.1`。
- `已确认` v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` v3.1 仍不可发送：`send_ready = false`。
- `已确认` v3.1 内容没有写成通过：`content_validation = pending_user_chatgpt_review_or_not_passed_copywriting_side`。
- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 是后续骚萌卡唯一执行参考；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- `已确认` PR #7 A 只保留为历史 / candidate 对照，不能再作为任何后续骚萌卡执行参考。
- `已确认` PR #22 / PR #23 / PR #24 均已写入降噪口径：不得直接合并，不得覆盖当前 v3.1 基线。

## 20260502｜仓库清理与旧口径归档

- `已确认` 本轮只做仓库清理、旧口径归档、入口口径重写和执行噪音删除；不生成 v3.1，不生成新视频，不生成新音频，不重新装配全片。
- `已确认` 已从 `codex/user-readable-map` 创建清理分支：`codex/repo-cleanup-old-context-20260502`。
- `已确认` 当前入口继续写明 v3 技术层为 `v3_technical_milestone = reached_for_current_stage`，技术线未锁定，下一步仍需技术升级。
- `已确认` v3 内容未过线，主要在 GPT 文案侧；`content_validation = not_passed_user_review_gpt_copywriting_side`，`send_ready = false`，`visual_master_locked = false`。
- `已确认` PR #7 B 仍是后续骚萌卡执行参考；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- `已确认` PR #7 A 已降权为历史 / candidate 对照；v3 生成时的 PR #7 A 痕迹已在 metadata 中标为 `legacy_generation_candidate_references`，不再放在可继承候选参考字段里。
- `已确认` 新增归档目录：`归档_archive/旧口径_old_context_20260502/`，归档 PR #22 原始待复审口径、PR #23 原始 PR #7 A 优先判断、可爱卡片旧 route suggestion。
- `已确认` 更新 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`，明确归档目录只作复盘证据，不作为当前默认事实入口。
- `已确认` 本地原始脏工作区只删除 `dist/routeA_frame_*.png` 这 10 张未引用临时帧；素材、复审包、v3 证据、PR7_B、可爱卡片参考图均未删除。
- `已确认` 本轮必须 commit、push、创建 PR，并在验证通过后合并到 `codex/user-readable-map`，合并后清理口径才算新聊天默认正式已知。

## 20260501｜v3 技术里程碑与 v3.1 视觉参考锁定

- `已确认` 本轮只做仓库口径回写、reference registry 修补、v3.1 视觉路由前置规则同步和主读取分支回流；未生成 v3.1、未生成新视频、未生成新音频、未重新装配全片。
- `已确认` 用户已复审《我用 AI 做 PPT 踩过的坑》v3：技术层只能写为 `v3_technical_milestone = reached_for_current_stage（当前阶段技术里程碑达成）`，不得写成技术线最终锁定。
- `已确认` 下一步仍需要 `technical_upgrade_next = true（技术升级）`，`technical_baseline_locked = false（技术基线未锁定）`。
- `已确认` v3 内容未过线，主要问题在 GPT 文案侧；状态写为 `content_validation = not_passed_user_review_gpt_copywriting_side`，不得写 `passed` 或仅写 `pending_user_chatgpt_review`。
- `已确认` `send_ready = false`，`visual_master_locked = false`，`visual_master_candidate = true`。
- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 已写为后续骚萌卡执行参考；读不到 PR #7 B 必须 `blocked`，不得回退 PR #7 A。
- `已确认` PR #7 A 保留为历史 / candidate 对照，不删除、不升级 locked、不再作为下一轮 v3.1 后续骚萌卡执行参考。
- `已确认` 新增 route-level locked references：`sassy_card_pr7_b_visual_locked_20260501`、`cute_prompt_card_route_locked_20260501`、`cute_info_card_route_locked_20260501`。
- `已确认` 新增 v3.1 前置规则文件：`codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`。
- `已确认` 下一轮 v3.1 必须先输出并验证 `visual_route_map.json（视觉路由表）`；route map 通过前不得生成全片。
- `已确认` 三条视觉路由已写清：`cute_prompt_card_route（可爱段落提示卡路由）`、`cute_info_card_route（可爱信息卡路由）`、`sassy_reaction_card_route（骚萌反应卡路由）`。
- `已确认` 本轮同步了 PR #22 v3 latest review pack 的既有产物作为当前复审对象，但只改状态口径，不生成新产物。
- `已确认` 本轮新增 dated log：`codex_log/20260501_v3技术里程碑与v31视觉参考锁定.md`。
- `已确认` 只有 commit / push / 合并到 `codex/user-readable-map` 后，上述口径才算新聊天默认正式已知。

## 20260430｜v3 功能卡 / 结果差卡 / 尾卡清晰质感参考落仓库

- `已确认` 本轮只做 v3 前置参考口径落仓库，不生成 v3，不生成视频，不生成音频，不生成图片。
- `已确认` 新增 `card_visual_quality_clean_ui_texture_candidate_20260430（功能卡 / 结果差卡 / Prompt 引用尾卡清晰质感候选参考）`。
- `已确认` 该参考只作为 `candidate（候选参考）`，不是 `locked_reference（锁定参考）`，不是 `visual_master_reference（视觉母版参考）`。
- `已确认` 该参考用于 v3 的功能卡、结果差卡、Prompt 引用尾卡，以及少量 PPT / 卡片承载的信息整理段。
- `已确认` 该参考只继承清晰质感：干净、留白、圆角、轻阴影、轻高光、层级舒服、文字清楚、有一点高级 UI 感。
- `已确认` 该参考不继承底部黑色按钮、电商筛选页、`More Filters` 式 CTA、假 App 导航、一堆分类筛选项、英文乱码或真实 UI 照抄。
- `已确认` 当前没有 `visual_master_reference（视觉母版锁定参考）`；v3 若按该方向生成并通过用户 / ChatGPT 复审，后续才可能反向成为视觉母版候选。
- `已确认` 字幕本轮先不上；PR #15 v2 字幕仍是 `failed_reference（失败参考）`，不得继承为字幕标准。
- `已确认` PR #7 A 版骚萌卡视觉仍是 `candidate（候选参考）`；20260430 “v3 可先以它作为视觉参考”的旧口径已被 20260501 用户最新确认覆盖，后续骚萌卡执行参考改为 PR #7 B。
- `已确认` TTS 节奏 reference 仍是 `tts_15s_b_pacing_locked_20260427（B 版 15 秒停顿梗感 TTS 节奏锁定参考）`；最近 custom voice（脱敏标识 `qwen-t...ac19`）仍是声音底子候选，最终音色待验证。
- `已确认` 本轮新增 dated log：`codex_log/20260430_card_visual_quality_reference_for_v3.md`。
- `已确认` 本轮未修改 `dist/latest_review_pack/（最新审片包）`，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 只有本轮分支 / PR 合并或同步回 `codex/user-readable-map（主读取分支）` 后，该参考口径才算新聊天默认正式已知。

## 20260430｜video-metadata-probe skill 安装与配置

- `已确认` 本轮安装并验证 `Homebrew（Mac 包管理器）`：`/opt/homebrew/bin/brew`，版本 `Homebrew 5.1.8`。
- `已确认` 本轮安装并验证 `ffmpeg（音视频工具套件）`：`/opt/homebrew/bin/ffmpeg`，版本 `ffmpeg version 8.1`。
- `已确认` 本轮安装并验证 `ffprobe（视频信息读取工具）`：`/opt/homebrew/bin/ffprobe`，版本 `ffprobe version 8.1`。
- `已确认` 已创建全局 `video-metadata-probe（视频元数据检查）` skill：`/Users/fan/.codex/skills/video-metadata-probe/`。
- `已确认` skill 包含 `SKILL.md（skill 说明文件）`、`scripts/probe_video.sh（视频元数据检查脚本）`、`examples/README.md（使用示例）`。
- `已确认` 已用 `round34_middle_preview（round34 中段预览样片）` 做冒烟测试：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`。
- `已确认` 冒烟测试结果：`28.520000s / 720x1280 / 25.000fps / h264 / aac / 2ch / decodable = true / fallback_used = false / validation_status = passed`。
- `已确认` 冒烟测试只代表 `technical_validation（技术验证）`、`metadata_validation（元数据验证）`、`audio_validation（音频验证）`，不代表 `content_validation（内容验证）` 通过。
- `已确认` 本轮未生成视频，未修改视频 / 音频 / 图片，未修改 `dist/latest_review_pack（最新审片包）`，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 本轮日志分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，skill 安装记录才成为主读取分支正式已知。

## 20260430｜本地真实路径索引机制

- `已确认` 本轮新增 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`，记录 Codex 已在本机验证存在的本地审片 / 复审产物路径。
- `已确认` 后续 ChatGPT / Codex 给用户本地可打开路径时，必须优先读取该索引。
- `已确认` `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径只能作为线索，不能直接当真实可打开路径输出。
- `已确认` 只有索引中 `path_exists = true（路径存在）` 的记录，才能作为用户可打开路径输出；缺失或超过 24 小时未验证时，必须写成“路径待本地复核”。
- `已确认` 已验证 clean worktree 首选路径存在：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`、`problem_windows/30_32s.mp4`、`problem_windows/30_32s_frames.jpg`、`cut_contact_sheet.jpg`、`full.mp4`。
- `已确认` `no_zoom_completeness` 两张 1x PNG 与布局指标 JSON 在 clean worktree 指定路径未命中；本轮只在旧脏 worktree 中验证到备选打开路径，已标注不得作为默认执行路径。
- `部分成立` 视频文件已完成 `test -f` 与 `stat`；本机没有 `ffprobe`，本轮已尝试但命令不可用，时长 / 分辨率用 macOS `mdls` 只读补充。
- `已确认` 已在 `codex_source/00_codex_readme.md（Codex 执行层总入口）` 和 `codex_source/01_execution_rules.md（Codex 执行规则）` 接入本地路径索引读取规则。
- `已确认` 本轮未生成视频，未修改视频 / 音频 / 图片，未修改 `dist/latest_review_pack（最新审片包）` 内容本体，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 本轮 PR 合并 / 同步回 `codex/user-readable-map（主读取分支）` 后，该路径索引机制才成为新聊天默认正式已知。

## 20260430｜中段放大剪辑参考锁定

- `已确认` 本轮只更新 `codex_source/locked_reference_registry.md（锁定参考登记表）` 和日志，不生成视频、不修改视频产物。
- `已确认` 用户已看片确认：这一轮 `middle_preview（中段预览样片）` 的放大剪辑是对的，可以作为参考样本。
- `已确认` 用户确认样本路径：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`；repo relative（仓库相对路径）为 `dist/latest_review_pack/middle_preview.mp4`。
- `已确认` 新增 `middle_zoom_reference_confirmed_middle_preview_20260430（用户确认的中段放大剪辑锁定参考）`。
- `已确认` 该 reference 的 `status（状态） = locked（锁定参考）`，`confirmation_state（确认状态） = locked_reference_confirmed_by_user（用户确认锁定参考）`。
- `已确认` 锁定范围为同类中段录屏证据展示的放大剪辑方式、证据窗口选择方式和关键文字可读尺度；不锁所有视频的固定秒级时间码。
- `已确认` `zoom_pr15_v2_failed_20260430（PR #15 v2 放大位置失败参考）` 仍保持 `failed（失败参考）`；后续完整成片不得继承 PR #15 的失败放大位置。
- `已确认` `zoom_reference_missing_20260430（正确放大方式缺失历史记录）` 已标记为 `deprecated（已废弃缺口）`，并注明主要中段放大缺口已由新的 locked reference 补足。
- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`，不修改 `content_validation（内容验证）`，不修改 `send_ready（可发送状态）`。
- `待验证` 本轮分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，该 middle zoom locked reference 才成为新聊天默认正式已知。

## 20260430｜锁定参考登记表全量追回

- `已确认` 本轮只补全并升级 `codex_source/locked_reference_registry.md（锁定参考登记表）`，不生成视频、不做 v3、不修改现有视频产物。
- `已确认` 本轮新增日志：`codex_log/20260430_locked_reference_registry_full_recovery.md（锁定参考登记表全量追回日志）`。
- `已确认` 第一批升级为 `locked（锁定参考）`：
  - `middle_editing_round34_locked_20260425（round34 中段剪辑语法锁定参考）`
  - `sassy_card_three_type_rule_locked_20260428（三类骚萌卡放置规则锁定参考）`
  - `tts_15s_b_pacing_locked_20260427（20260427 B 版 15 秒停顿梗感 TTS 节奏锁定参考）`
  - `opening_reference_element_doll_no_text_locked_20260428（元素娃娃无字开头锚点锁定参考）`
- `已确认` `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）` 仍保持 `candidate（候选参考）`，不升级为视觉锁定参考。
- `已确认` 新增候选 / 缺口登记：体素元素娃娃视觉母版候选、round34 粉色樱花提示卡候选、功能卡 / 结果差卡候选、Prompt 引用尾卡规则候选、语音样本2声音底子候选、字幕标准缺口、正确放大方式缺口。
- `已确认` PR #15 v2 字幕、layout / 背景、TTS 缺失仍保持 `failed（失败参考）`；新增 PR #15 v2 放大位置失败参考。
- `已确认` 20260412 历史通过样片仍保持 `historical（历史参考）`，不升级为当前默认母版。
- `已确认` 本轮不修改 `dist/latest_review_pack/（最新审片包）`，不修改 `content_validation（内容验证）`，不修改 `send_ready（可发送状态）`。
- `待验证` 本轮分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，第一批 locked reference 才成为新聊天默认正式已知。

## 20260430｜锁定参考继承机制修补

- `已确认` 本轮不生成新视频，不修改现有视频，不创建成片候选。
- `已确认` 本轮只修机制：新增 locked_reference（锁定参考）定义、晋升条件、默认继承规则、完整成片前置读取、继承报告、summary 字段和 blocked 条件。
- `已确认` 当前仓库审计结论为 `locked_reference_inheritance_missing（缺少锁定参考继承机制）`：已有 reference pack / 声音参考锚点 / 当前审片包等相近机制，但没有统一 locked reference registry、强制继承报告和未继承 blocked 条件。
- `已确认` 新增规则文件：`codex_source/14_locked_reference_inheritance_rules.md`。
- `已确认` 新增登记表：`codex_source/locked_reference_registry.md`。
- `已确认` 初始 registry 没有任何 `locked` reference；只登记 `candidate`、`failed`、`historical`，避免把候选或失败样本误写成正式继承样板。
- `已确认` 初始 registry 已登记 round34 中段剪辑语法候选、PR #7 A 版骚萌卡视觉候选、PR #8 三类骚萌卡规则候选、PR #15 v2 字幕 / layout / TTS 失败参考、20260427 B 版 15 秒 TTS 节奏候选、20260412 历史通过样片。
- `已确认` 已接入读取链路：完整成片 / 成品候选片 / 技术预览升级 / 样片回炉 / 字幕 / TTS / 卡片 / 放大 / 剪辑 / 视觉母版修正任务，后续必须先读 locked reference 规则和 registry。
- `已确认` 若读不到 locked reference 规则或 registry，或未继承已锁定 reference，必须 `blocked`，不得写成候选片完成。
- `已确认` 后续完整成片 / 成品候选片 / 样片回炉必须输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`。
- `已确认` 本轮不修改 `dist/latest_review_pack/`，不修改 `content_validation`，不修改 `send_ready`。
- `待验证` 本机制当前只在工作分支 / PR 中成立；合并或同步回 `codex/user-readable-map` 后，才算主读取分支正式已知。

## 20260427｜中段吐槽插入风格视觉证据补齐

- `已确认` 本轮只是补齐上一轮 reference pack 的轻量视觉证据，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步视觉证据：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_关键帧联系表_keyframes_contact_sheet.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_吐槽三连帧_punchline_triptych.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第一次吐槽前后_context_01.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第二次吐槽前后_context_02.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第三次吐槽前后_context_03.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_GIF式吐槽动态预览_visual_punchline_preview.mp4`
- `已确认` 本轮新增报告：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/画面层保真补充_visual_punchline_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据补齐_run_summary.json`
- `待验证` GIF 式吐槽画面层仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不改视频，不生成新 round，不替换音轨，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation（内容验证）`，不改变 `send_ready（可发送状态）`。
- `已确认` 本轮不修改 `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`。
- `已确认` 原始 50MB MP4、完整 `frames/` 目录、音频副本与波形图未提交；本轮只提交筛选后的轻量视觉证据。

## 20260427｜中段吐槽插入风格参考包同步

- `已确认` 本轮只是把上一轮本地“中段吐槽插入风格高保真提取”文本 reference_pack 同步到 `codex/user-readable-map`，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步文本报告路径：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/素材清单_assets_inventory.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio_reference_note.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/scene_index.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/吐槽插入风格_reference_pack.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/给ChatGPT的素材汇报_material_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/run_summary.json`
- `已确认` 本轮同步源来自上一轮本地分析包：`/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`。
- `已确认` 上一轮本地分析包生成于 `fix/no-zoom-completeness-layout`，不是主读取分支；本轮已在 `codex/user-readable-map` 重新同步文本报告。
- `已确认` 上一轮存在路径漂移风险：上一轮分支中无空格 `GPT数据源/` 缺失，只读到 `GPT 数据源/`；本轮已在 `codex/user-readable-map` 读取无空格 `GPT数据源/` 当前执行包。
- `待验证` 吐槽插入风格仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不写入正式风格规则，不改视频，不生成新 round，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation`，不改变 `send_ready`。
- `已确认` 本轮未提交二进制证据文件：`keyframes_contact_sheet.jpg`、`audio/reference_audio.m4a`、`audio_waveform.png`、`frames/`；本轮只同步 Markdown / JSON 文本报告。

## 20260427｜文案生产流程与 B 版声音口径固化

- `已确认` 本轮只做《视频工厂》文案生产流程、最终风格锚点、声音 B 版暂定口径的规则落仓库；未生成新音频、新视频，未修改现有样片，未替换全片音轨。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入后续默认文案生产流程：`Perplexity（外部参考检索 / 研究工具）` 输出 `reference pack（参考包）` 与 `raw feeling draft（原感初稿）` -> 用户录制素材 -> `Codex（执行代理）` 做素材技术检查与细节证据报告 -> `ChatGPT（最终落稿与复审入口）` 写最终落稿 -> `Codex（执行代理）` 按最终稿执行。
- `已确认` 已明确 `Perplexity（外部参考检索 / 研究工具）` 只负责参考包 / 原感初稿，不是最终稿；不得直接进入执行。
- `已确认` 已在 `GPT数据源/05_文案路由规则.md（当前文案路由）` 写入 `Codex（执行代理）` 素材细节汇报标准：不能只报“素材存在 / 技术通过”，必须写清素材里有什么、在哪一秒、发生了什么、能证明什么，并给 `ChatGPT（最终落稿与复审入口）` 可写稿的细节。
- `已确认` 已在 `GPT数据源/07_AI知识类视频价值规则.md（当前价值规则）` 写入最终稿细节标准：最终稿必须尽量具体到真实工具 / 网站、页面、按钮、输入动作、生成结果、前后对比、失败点和下一步怎么做。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入最终文案风格锚点：用户确认的“用字更自然版长稿” + 20260427 B 版“停顿梗感”试听方向；风格为微反转、说话带梗、自然口语、生活观察起手、轻吐槽、避免 AI 感硬词，不写课程腔 / 广告腔 / 鸡血腔。
- `已确认` 已在 `GPT数据源/08_当前正式事实.md（当前正式事实）` 写入当前声音暂定口径：用户更喜欢 20260427 B 版“停顿梗感”方向；新样本2 `custom voice（自定义音色）` 脱敏标识 `qwen-t...ac19` 可继续作为当前声音底子。
- `已确认` 后续声音主要调 `speech_pacing（语速节奏）`、`pause_timing（停顿位置）`、`copy_fit（文案搭配）`；暂不优先重做 `voice cloning（声音复刻）`，暂不优先换音色。
- `待验证` B 版只是当前优先试听方向，不是最终成片音轨，不能写最终音色已定，不能写 `voice_validation_status（声音验证状态） = 通过`。
- `已确认` 未修改 `GPT 数据源/（GPT Project 协作规则包）`，未把 B 版暂定声音这种动态状态写入静态协作包。
- `已确认` 新增日志：`codex_log/20260427_文案生产流程与B版声音口径固化.md（本轮日期日志）`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260427｜十五秒文案语速停顿试配

- `已确认` 本轮只做《视频工厂》声音文案适配试听；未换音色、未重做 voice cloning、未重新裁剪 / 上传样本、未替换全片音轨。
- `已确认` 用户本轮确认方向已记录：新样本2音色底子可以继续用，后续主要调语速、停顿和文案搭配；偏好“微反转 + 说话带梗 + 自然口语”；需避免类似“下一步从哪打”的 AI 感硬词。
- `已确认` 使用新样本2 custom voice：`qwen-t...ac19`（脱敏）；`model / target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 本轮只通过 custom voice list 解析既有 voice，未重新 `create_custom_voice`；未使用 Serena；未使用上一轮 A / B custom voice。
- `已确认` 新增输出目录：`dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`。
- `已确认` A 版文案为自然节奏，去空白字数 `93`；B 版文案为停顿梗感，去空白字数 `97`；两版均未命中本轮禁用硬词。
- `已确认` 已生成 A / B 两条声音试听：
  - A：`A_15秒文案_自然节奏.wav`，`17.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.9 dB / loudnorm.input_i -23.92 LUFS`
  - B：`B_15秒文案_停顿梗感.wav`，`16.32s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.4 dB / loudnorm.input_i -23.67 LUFS`
- `已确认` A / B 均可被 `ffmpeg` 解码，且时长均在 13-18 秒范围内。
- `已确认` A / B API 原始输出已在目标范围内，本轮未使用 `atempo`。
- `已确认` 脱敏请求、音频验证与运行摘要已落盘：`A_voice_clone_tts_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`A_ffmpeg_decode_check.txt`、`B_ffmpeg_decode_check.txt`、`A_volumedetect.txt`、`B_volumedetect.txt`、`A_loudnorm_measure.txt`、`B_loudnorm_measure.txt`、`run_summary.json`。
- `已确认` 新增日志：`codex_log/20260427_十五秒文案语速停顿试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 的语速、停顿、轻吐槽和文案搭配是否合适，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜语音样本2复刻与文案风格解析

- `已确认` 本轮重开新语音样本链路，未沿用上一轮 A / B 声音试配结果；上一轮 A / B 只保留为失败参考。
- `已确认` 已定位用户新样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`，候选数量为 `1`，未回退使用旧样本。
- `已确认` 新样本只读解析：`23.16s / mov,mp4,m4a,3gp,3g2,mj2 / hevc / aac / 44100 Hz / stereo / mean_volume -13.3 dB / loudnorm.input_i -10.26 LUFS`。
- `已确认` 已生成分析副本与复刻输入：
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_分析副本.m4a`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- `已确认` 复刻输入样本为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`，从原 MP4 `2.0s` 起连续裁剪。
- `已确认` 已用新样本创建新的测试 custom voice，脱敏标识：`qwen-t...ac19`；`model = qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`，`preferred_name = vfsample20426`。
- `已确认` 已生成 1 条新样本声音复刻试听 trial：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`。
- `已确认` 试听 trial 可被 `ffmpeg` 解码：`13.60s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.8 dB / loudnorm.input_i -23.72 LUFS`。
- `已确认` 已尝试并完成完整 MP4 自动 ASR 转写，模型为 `paraformer-realtime-v2`；转写文件：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`。
- `待验证` 自动转写尚未人工校对，可能存在误识别；文案风格记录只能作为本轮 reference style，不能写成唯一标准风格。
- `已确认` 已新增高保真文案风格记录：`codex_log/20260426_语音样本2_文案风格高保真记录.md`。
- `已确认` 已新增音频参考报告：`codex_log/20260426_语音样本2_audio_reference_report.md`。
- `已确认` 已新增执行日志：`codex_log/20260426_语音样本2复刻与文案风格解析.md`。
- `已确认` 已新增本轮脚本：`scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py`。
- `待验证` 本轮只证明 `technical_generation` 通过；`voice_validation_status` 仍为待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜台湾口语开心降噪声音第二轮试配

- `已确认` 本轮只生成《视频工厂》声音第二轮最小对照 trial；未修改视频、未替换全片音轨、未生成新视频 round。
- `已确认` 用户本轮听感反馈已保真记录：
  1. 情绪上面还不够开心的那种。
  2. 需要把口语改成台湾的口音。
  3. 现在生成的环境音有点吵，需要降噪。
- `已确认` 新增本轮输出目录：`dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`。
- `已确认` A 版沿用当前 custom voice（脱敏：`qwen-t...de43`），使用台湾口语文本 + 开心轻快 instructions 生成，并保留：
  - `A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`
  - `A_沿用音色_台湾口语开心_原始.wav`
  - `A_沿用音色_台湾口语开心_轻降噪.wav`
- `已确认` B 版先对复刻输入样本做轻降噪，再重新创建测试 custom voice（脱敏：`qwen-t...bb3b`），使用同一文本 + 同一 instructions 生成，并保留：
  - `B_复刻输入样本_轻降噪.wav`
  - `B_重建音色_台湾口语开心_API原始_未节奏校准.wav`
  - `B_重建音色_台湾口语开心_原始.wav`
  - `B_重建音色_台湾口语开心_轻降噪.wav`
- `已确认` 因固定文案较长，API 直出分别为 `17.60s` / `16.56s`；本轮保留 API 直出审计文件，同时用 `atempo` 生成 10-15 秒未降噪节奏校准版。
- `已确认` 四个正式对照输出均可被 `ffmpeg` 解码：
  - A 原始：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.8 dB / loudnorm.input_i -22.13 LUFS`
  - A 轻降噪：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.3 dB / loudnorm.input_i -22.64 LUFS`
  - B 原始：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.4 dB / loudnorm.input_i -22.40 LUFS`
  - B 轻降噪：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.7 dB / loudnorm.input_i -22.65 LUFS`
- `已确认` 脱敏请求与验证记录已落盘：`custom_voice_list_debug_sanitized.json`、`A_voice_clone_tts_request_debug_sanitized.json`、`B_重建音色_create_custom_voice_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`run_summary.json`。
- `已确认` 新增脚本：`scripts/声音第二轮台湾口语开心降噪_trial_round2.py`。
- `已确认` 新增日志：`codex_log/20260426_台湾口语开心降噪声音试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 是否更开心、是否像台湾口语、降噪后是否仍自然，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜GPT Project 协作规则包更新

- `已确认` 本轮只更新 `GPT 数据源/`，将其定位改为 GPT Project 协作规则包；它只负责告诉 ChatGPT 如何协作、如何读 GitHub、如何处理冲突，不再承载动态当前事实。
- `已确认` 当前项目事实和执行状态的主事实源仍是 GitHub 当前文件；当前 round、`latest_review_pack`、`content_validation`、`send_ready`、声音试配状态都必须从 GitHub 当前文件读取。
- `已确认` 本轮在 `codex/user-readable-map` worktree 中新增并跟踪 `GPT 数据源/` 10 份文件；未修改 `GPT数据源/` 当前 10 份执行包。
- `已确认` `GPT 数据源/08_当前正式事实.md` 未纳入新包；新第 8 份文件为 `GPT 数据源/08_当前事实读取规则.md`，专门记录当前事实读取顺序和冲突裁决。
- `已确认` 本轮未修改视频、音频、图片、原始素材、生成脚本、测试脚本、`dist/latest_review_pack/*` 或 `dist/voice_trials/*`。
- `已确认` 本轮不改变当前视频与声音状态；声音试配和全片内容复审仍以 GitHub 当前文件为准。
- `下一个目标`：后续 ChatGPT 先按 `GPT 数据源/` 协作规则接手，再从 GitHub 当前文件读取项目事实。

## 20260426｜下一个目标与中文英文命名规则补丁

- `已确认` 本轮只做规则补丁，不做目录迁移，不执行 `git mv`，不重命名任何已有文件或文件夹。
- `已确认` 执行位置已校准到主读取分支 worktree：`/private/tmp/视频工厂_user_readable_map_sync`，当前分支为 `codex/user-readable-map`。
- `已确认` 已写入最终汇报和交接口径：最后一栏统一使用“下一个目标”，不再默认使用“下一步行动建议”。
- `已确认` 已写入新增业务文件 / 业务文件夹命名规则：默认使用“中文 + 英文”，推荐格式为 `中文名_english_name`。
- `已确认` 已有文件和已有文件夹本轮不追溯改名；工具链强制英文名保留为例外，且例外不得扩大到普通业务目录和业务文件。
- `已确认` 本轮不修改视频、音频、图片、原始素材、生成脚本或测试脚本。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 提交前本地验证已通过；远端同步状态以本轮收尾的 `git show origin/codex/user-readable-map:路径` 复读验证为准。

## 20260426｜round28 声音复刻试配继续执行

- `已确认` 本轮继续上轮被阿里百炼 `Arrearage` 阻塞的 voice cloning（声音复刻）路线；不重回 `Serena` 系统音色，不修改视频，不替换全片音轨，不生成新视频 round。
- `已确认` 复用上轮合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数仍为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 阿里账户本轮不再返回 `Arrearage`；用户 prompt 指定的 `vf_r28_clone_20260426` 因超过官方 `preferred_name` 16 字符限制返回 `InvalidParameter`，已按官方约束改用 `vfr28clone0426`。
- `已确认` 已创建测试 custom voice，脱敏标识：`qwen-t...de43`；创建模型为 `qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 已使用该 custom voice 生成 1 条 round28 声音复刻 trial：`dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`。
- `已确认` 输出音频验证：`12.96s / wav / pcm_s16le / 24000 Hz / mono / 622124 bytes`，可被 `ffmpeg` 解码；`mean_volume = -23.5 dB`，`loudnorm.input_i = -23.57 LUFS`。
- `已确认` 脱敏请求记录：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- `待验证` 本轮只证明 voice cloning trial 已生成；是否明显比上一轮 `Serena` 更接近用户样本，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音复刻最小试配

- `已确认` 用户授权已到位；本轮允许上传裁剪后的合规样本到阿里百炼声音复刻接口，仅用于《视频工厂》最小声音复刻试配。
- `已确认` 已生成合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 本轮实际走的是 `qwen-voice-enrollment -> qwen3-tts-vc-realtime-2026-01-15` 的声音复刻路线，没有回退到 `Serena` 系统音色。
- `已确认` 当前阻塞点发生在 `create_custom_voice` 阶段：阿里百炼返回 `400 / Arrearage`，未创建成功 custom voice，未生成新的声音复刻试配音频。
- `已确认` 脱敏请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`。
- `已确认` 复刻试配日志：`codex_log/20260425_round28_声音复刻最小试配.md`。
- `待验证` 账户恢复后，可直接复用本轮合规裁剪样本继续创建 custom voice；当前声音仍待验证。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音试配失败排查

- `已确认` 用户已听审 `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`，反馈为：和样本完全不一样，非常生硬，一听就是 AI。
- `已确认` 本轮只做声音路线诊断；未生成新音频，未修改视频 / 图片 / 原始素材 / 当前 trial 音频 / 脚本，未调用 TTS API，未上传用户样本。
- `已确认` 当前 trial 请求体为 `qwen3-tts-instruct-flash-realtime + Serena` 系统音色 + 指令控制；请求体里没有用户样本、custom voice、voice cloning 或 voice design 字段。
- `已确认` 失败主因：用户样本没有实际进入生成链路，当前路线只能做系统音色的风格指令控制，不能复刻用户样本声纹。
- `部分成立` 文案韵律和后处理可能放大生硬 / AI 感，但不是“完全不像样本”的主因。
- `待验证` 下一轮最值路线是：先取得用户明确授权，再走 `voice cloning（声音复刻）` 最小试配；若用户不授权上传样本，则退而走 `voice design（声音设计）`，不要继续盲调 `Serena`。
- `已确认` 诊断日志：`codex_log/20260425_round28_声音试配失败排查.md`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 最小声音试配

- `已确认` 本轮只生成 1 条 10-15 秒声音 trial（试配）音频；未修改任何视频、图片、原始素材、当前成片音轨或视频装配脚本。
- `已确认` 使用 round28 文案来源：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`。
- `已确认` 本轮试配文案取自 round28 字幕第 1 段 + 第 5 段首句：
  - `最费时间的，不是做汇报页。是第一行根本写不出来。后来我换上调好的提示词，直接砍掉空转。区别不是豆包，是那段提示词。`
- `已确认` 真实使用 TTS：`aliyun_bailian / aliyun_qwen_realtime_websocket / qwen3-tts-instruct-flash-realtime / Serena`。
- `已确认` 输出音频：`dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`。
- `已确认` 音频基础验证：`13.00s`、`aac (LC)`、`48000 Hz / mono`、`mean_volume = -16.4 dB`、`loudnorm.input_i = -16.25 LUFS`，可被 `ffmpeg` 解码。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 该 trial 只回答声音方向是否接近“低压、清楚、有一点可爱感的女生游戏向导音”；用户 / ChatGPT 听感复审前，不得写成最终音色、最终 TTS 或声音验证通过。

## 20260425｜语音样本只读排查与声音参考锚点

- `已确认` 本轮任务只做语音样本定位、音频基础参数分析、声音参考锚点落地与仓库口径更新；不改视频、不替换旁白、不生成新 round、不做 TTS 试配。
- `已确认` 当前 latest_review_pack 仍指向：`round34_中段双展示提示卡_正反分段提示修复`。
- `已确认` 用户语音样本已通过兜底搜索命中：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`。
- `已确认` 样本用于记录 `可爱女生向导音` 的 reference anchor（参考锚点）；它不等于最终 TTS 方案已确定，也不等于声音内容验证通过。
- `部分成立` `ffmpeg` 可用并已完成分析用音频副本提取、`volumedetect`、`astats`、`silencedetect` 与 `loudnorm` 初步测量；`ffprobe` 未在本机可执行路径中命中，本轮元数据读取降级使用 `ffmpeg` 输入信息。
- `已确认` 音频基础参数报告：`codex_log/20260425_语音样本_audio_reference_report.md`。
- `已确认` 分析文本输出目录：`codex_log/audio_reference/20260425_语音样本/`。
- `已确认` 当前视频状态未改变：
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 下一步声音动作是基于该样本做 10-15 秒最小声音试配，再和当前视频开头 / 结尾主持壳做听感匹配复审；不得直接全片替换。

## 20260425｜round34 中段双展示提示卡正反分段提示修复

- `已确认` 当前视频工作分支为 `codex/doubao-vnext-direct-fix-20260417`；该分支当前由 Git worktree `/private/tmp/视频工厂_round28_complete_readability` 持有。
- `已确认` 本轮新开 `round34_中段双展示提示卡_正反分段提示修复`，只做 `latest_review_pack` 中段局部修复；未重构整条视频。
- `已确认` 用户本轮同步的图二参考图可读取：`/Users/fan/Desktop/截屏2026-04-25 18.11.07.png`，尺寸 `908x492`。
- `已确认` 两张提示卡已按图二粉色樱花柔和展示牌风格重构为 720x1280、9:16 竖屏：
  - 《反面展示》：`先看旧做法：一句糊话，结果怎么变泛`
  - 《正面展示》：`再看工作包后：结果怎么一步步落成`
- `已确认` round34 中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- `已确认` 反面录屏与正面录屏仍由用户真实录屏承担，源时间码与 round33 一致，未裁短、未替换、未重录。
- `已确认` 开头主持壳、回场主持壳、`judgment_card`、Prompt 引用尾卡均未重做；未调用阿里 API，未重新生成元素娃娃，未修改原始录屏素材。
- `已确认` `latest_review_pack` 已更新指向：
  - `round34_中段双展示提示卡_正反分段提示修复`
- `已确认` 当前审片包口径：
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 用户已打开实际可用本地审片包路径：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`。
- `已确认` 用户最新反馈为“现在中段没什么问题了”，仓库口径记录为：round34 中段结构暂定接受，当前不继续修改中段。
- `已确认` 中段暂定接受只代表 `middle_segment_review` 暂定收束，不代表全片 `content_validation` 通过。
- `待验证` round34 内容最终是否过线仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 当前最新审片入口

- 当前可打开本地审片包：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/full.mp4`
- `dist/latest_review_pack/middle_preview.mp4`
- `dist/latest_review_pack/before_after.mp4`
- `dist/latest_review_pack/图二参考图.png`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/cut_contact_sheet.jpg`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/20260425_round34_中段暂定通过与本地审片路径修正.md`

## 20260524｜新第四期素材解析结果同步

- `已确认` 新第四期素材解析已完成，本轮只同步审计结果，不重跑素材解析、不生成成片、不提交原始素材和图片产物。
- `已确认` 素材目录：`/Users/fan/Documents/视频工厂/素材录制/新第四期`。
- `已确认` 结果目录：`codex_log/material_audit/新第四期_20260524_001649/`。
- `已确认` 本次同步到 main 的审计文件：
  - `00_material_inventory.md`
  - `01_media_probe_report.md`
  - `05_timeline_segment_map.md`
  - `06_evidence_anchor_report.md`
  - `07_missing_and_risk_report.md`
  - `08_chatgpt_handoff_pack.md`
  - `manifest.json`
- `sync_status = synced_to_main`
- `technical_material_audit = passed_with_limits`
- `content_validation = not_advanced`
- `send_ready = false`
- `blocked = false`
- `partial_completed = false`
- `未提交` 原始素材视频、keyframes 图片、contact_sheets 图片、音频副本、成片文件、dist 大媒体文件或任何凭据类文件 / 密钥值。
- `待验证` 本轮素材只支持 ChatGPT 进入最终文案判断，不代表内容验证通过，不代表可发送，不代表商品、佣金、流量或商业闭环已验证。
