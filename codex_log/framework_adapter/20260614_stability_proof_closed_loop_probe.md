# 20260614 Stability Proof Closed Loop Probe

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - stability_proof_closed_loop（稳定性证明闭环）
  - sandbox_fake_model_graph_invoke_probe（沙盒假模型图调用探测）
  - no_service_langgraph_probe（不启动服务的 LangGraph 探测）
  - retrieval_manifest_source_readback_contract_probe（检索清单与原文回读契约探测）
  - executor_handoff_completion_truth_probe（执行器交接与完成真实性探测）
  - no_main_pollution_check（不污染主线检查）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
execution_permission（执行权限）: sandbox_fake_model_no_service_stability_probe_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
```

本轮只证明：在已安装成功的 sandbox 中，可以用 LangGraph 把视频工厂的完成真实性检查链路固定成确定性节点链。该证明不等于正式 runtime 启用。

## 2. files_read（已读取文件）

```yaml
files_read（已读取文件）:
  current_repo（当前仓库）:
    AGENTS.md: read_ok
    codex_log/latest.md: read_ok
    codex_source/00_codex_readme.md: read_ok
    codex_source/19_project_state_action_router.md: read_ok
    codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
    codex_log/framework_adapter/20260614_goal_mode_sandbox_install_completion.md: read_ok
    codex_log/framework_adapter/20260614_langgraph_rag_cleaning_integration_probe.md: read_ok
  sandbox（沙盒）:
    pyproject.toml: read_ok
    src/agents/rag_assistant.py: read_ok
    src/agents/tools.py: read_ok
    src/agents/agents.py: read_ok
    src/agents/interrupt_agent.py: read_ok
    src/schema/schema.py: read_ok
    src/service/service.py: read_ok
  skills_used（使用技能）:
    langchain-architecture: read_ok
    rag-implementation: read_ok
    data-quality-frameworks: read_ok
  memory_context（记忆上下文）: read_ok
  missing_files（缺失文件）: []
```

## 3. sandbox_ready_check（沙盒就绪检查）

```yaml
sandbox_ready_check（沙盒就绪检查）:
  sandbox_path（沙盒路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  sandbox_path_exists（沙盒路径存在）: true
  uv_available（uv 是否可用）: true
  uv_path（uv 路径）: /Users/fan/.local/bin/uv
  venv_usable（.venv 是否可用）: true
  compile_probe_passed（编译探测是否通过）: true
  minimal_import_probe_passed（最小导入是否通过）: true
```

本轮复核导入：

```yaml
minimal_import_recheck（最小导入复核）:
  langgraph: passed
  agents.rag_assistant: passed
  agents.tools: passed
  agents.agents: passed
  agents.interrupt_agent: passed
  schema.schema: passed
  service.service: passed
```

## 4. probe_graph_created（探测图创建结果）

```yaml
probe_graph_created（探测图创建结果）:
  script_path（脚本路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614/video_factory_probe/video_factory_stability_probe.py
  uses_langgraph（是否使用 LangGraph）: true
  graph_type（图类型）: StateGraph
  py_compile（脚本编译）: passed
  sandbox_only（是否只在沙盒）: true
```

创建的 sandbox fixture：

```yaml
fake_fixtures（假资料）:
  - video_factory_probe/fixtures/project_rule.md
  - video_factory_probe/fixtures/latest_status.md
  - video_factory_probe/fixtures/codex_report.md
fixture_secret_scan（假资料密钥扫描）: passed_by_probe_cleaning_adapter
```

图节点链：

```yaml
required_nodes（必需节点）:
  - route_decision_node
  - cleaning_adapter_node
  - retrieval_manifest_node
  - source_readback_node
  - retrieval_gap_report_node
  - executor_handoff_node
  - completion_truth_check_node
  - report_writer_node
```

## 5. positive_stability_test（正向稳定性测试）

```yaml
positive_stability_test（正向稳定性测试）:
  run_count（运行次数）: 3
  output_files（输出文件）:
    - video_factory_probe/probe_outputs/positive_run_1.json
    - video_factory_probe/probe_outputs/positive_run_2.json
    - video_factory_probe/probe_outputs/positive_run_3.json
  result（结果）: passed
  blocked（是否阻断）: false
  final_decision（最终判断）: sandbox_stability_probe_passed
  positive_sha256（正向输出 SHA-256）: dc9cc8aeaa858bb9c9bc5f3b48f8e5f0a4d0c3d6270a7a4b7fed573486f04090
```

正向链路验证：

```yaml
positive_contract_check（正向契约检查）:
  route_decision_present（路由判断存在）: true
  retrieval_manifest_present（检索清单存在）: true
  source_readback_ok_count（原文回读成功数）: 3
  executor_handoff_can_write_report_only（执行器只允许写报告与 latest）: true
  locked_copy_edit_allowed（是否允许改锁定文案）: false
  content_validation（内容验证）: not_evaluated_not_promoted
  status_promotion_allowed（状态推进是否允许）: false
  retrieval_result_not_completion_proof（检索结果不是完成证明）: true
```

## 6. negative_block_test（负向阻断测试）

```yaml
negative_block_test（负向阻断测试）:
  test_name（测试名称）: missing_source_readback_should_block
  output_file（输出文件）: video_factory_probe/probe_outputs/negative_missing_source.json
  result（结果）: passed
  blocked（是否阻断）: true
  blocked_reason（阻断原因）: source_readback_missing
  missing_sources（缺失来源）:
    - missing_source
  final_decision（最终判断）: blocked
  negative_sha256（负向输出 SHA-256）: 2ac26755126e745f75e0b98624510c23305d394022e053a2c067c8fe64189f4f
```

负向链路验证：

```yaml
negative_contract_check（负向契约检查）:
  source_readback_node_marks_false（原文回读节点标记 false）: true
  retrieval_gap_report_outputs_missing_sources（检索缺口报告输出缺失来源）: true
  executor_handoff_can_write（执行器是否可写）: false
  completion_claim_allowed（是否允许完成声明）: false
  final_decision_is_blocked（最终判断是否阻断）: true
```

## 7. determinism_check（确定性检查）

```yaml
determinism_check（确定性检查）:
  same_required_keys（必填字段是否一致）: true
  same_route_decision（路由判断是否一致）: true
  same_blocked_status（阻断状态是否一致）: true
  same_completion_truth（完成真实性判断是否一致）: true
  same_output_report（输出报告是否一致）: true
  positive_run_1_2_equal（正向 1/2 是否字节一致）: true
  positive_run_1_3_equal（正向 1/3 是否字节一致）: true
  differences（差异）: []
  result（结果）: passed
```

## 8. source_readback_check（原文回读检查）

```yaml
source_readback_check（原文回读检查）:
  source_readback_verified（原文回读是否验证）: true
  positive_readbacks（正向回读）:
    project_rule: 技术验证通过不等于内容验证通过。
    latest_status: runtime_enabled=false。
    codex_report: 编译通过，但未启动服务。
  negative_missing_source_blocked（负向缺来源是否阻断）: true
```

## 9. completion_truth_check（完成真实性检查）

```yaml
completion_truth_check（完成真实性检查）:
  completion_truth_check_verified（完成真实性检查是否验证）: true
  technical_validation（技术验证）: passed_for_sandbox_graph_probe
  content_validation（内容验证）: not_evaluated_not_promoted
  status_promotion_allowed（是否允许状态推进）: false
  retrieval_result_not_completion_proof（检索结果不是完成证明）: true
  source_readback_required（是否必须原文回读）: true
  positive_completion_claim_allowed（正向是否允许沙盒完成声明）: true
  negative_completion_claim_allowed（负向是否允许完成声明）: false
```

说明：正向的 `completion_claim_allowed=true` 只允许声明本轮 sandbox stability probe 完成，不允许声明视频工厂正式 runtime 或内容验证完成。

## 10. executor_handoff_check（执行器交接检查）

```yaml
executor_handoff_check（执行器交接检查）:
  executor_handoff_boundary_verified（执行器边界是否验证）: true
  executor_type（执行器类型）: codex
  active_write_executor（当前激活写入执行器）: codex
  positive_can_write（正向是否允许写）: true
  positive_allowed_write_paths（正向允许写路径）:
    - codex_log/framework_adapter/20260614_stability_proof_closed_loop_probe.md
    - codex_log/latest.md
  negative_can_write（负向是否允许写）: false
  locked_copy_edit_allowed（是否允许改锁定文案）: false
  forbidden_write_paths（禁止写路径）:
    - AGENTS.md
    - GPT数据源/*
    - codex_source/*
    - pyproject.toml
    - requirements.txt
    - package.json
    - compose.yaml
    - docker-compose.yml
    - dist/*
    - public/*
    - media/*
    - .env*
```

## 11. stability_gain_decision（稳定性提升判断）

```yaml
stability_gain_decision（稳定性提升判断）:
  stability_gain_proven（稳定性提升是否已证明）: true
  proven_scope（已证明范围）: sandbox_fake_model_no_service_graph_probe_only
  not_proven_scope（未证明范围）:
    - formal_video_factory_runtime
    - real_llm_provider
    - DashVector runtime adapter
    - FastAPI service contract
    - Chroma ingestion
    - production persistence
  actual_value（实际价值）: LangGraph 可以把视频工厂“能不能写完成”的关键检查固定成确定性节点链，并在缺 source readback 时稳定阻断。
  limitation（限制）: 本轮是 sandbox / fake fixture / no service / no external API 探测，不能证明生产运行稳定性。
```

## 12. disabled_services_check（禁用服务检查）

```yaml
disabled_services_check（禁用服务检查）:
  streamlit_started（Streamlit 是否启动）: false
  fastapi_service_started（FastAPI 服务是否启动）: false
  docker_started（Docker 是否启动）: false
  postgres_started（Postgres 是否启动）: false
  chroma_ingestion_script_run（Chroma 入库是否运行）: false
  external_api_called（外部 API 是否调用）: false
```

## 13. main_repo_pollution_check（主仓库污染检查）

```yaml
main_repo_pollution_check（主仓库污染检查）:
  main_repo_dependency_modified（主仓库依赖是否被修改）: false
  external_code_copied_to_main（是否复制外部代码到主线）: false
  env_or_secret_written（是否写入 env 或 secret）: false
  forbidden_paths_modified（是否修改禁止路径）: false
  unrelated_untracked_public（无关未跟踪 public）: present_but_not_staged
```

## 14. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  sandbox_install_ready（沙盒安装是否可用）: true
  langgraph_probe_script_created（LangGraph 探测脚本是否创建）: true
  positive_stability_test_done（正向稳定性测试是否完成）: true
  positive_stability_test_passed（正向稳定性测试是否通过）: true
  negative_block_test_done（负向阻断测试是否完成）: true
  negative_block_test_passed（负向阻断测试是否通过）: true
  determinism_check_done（确定性检查是否完成）: true
  determinism_check_passed（确定性检查是否通过）: true
  source_readback_verified（原文回读是否验证）: true
  completion_truth_check_verified（完成真实性检查是否验证）: true
  executor_handoff_boundary_verified（执行器边界是否验证）: true
  no_main_repo_dependency_modified（主仓库依赖未修改）: true
  no_external_code_tracked_in_main（外部代码未被主仓库跟踪）: true
  no_env_or_secret_written（未写入 env 或 secret）: true
  no_frontend_started（未启动前端）: true
  no_docker_started（未启动 Docker）: true
  no_fastapi_service_started（未启动 FastAPI 服务）: true
  no_formal_runtime_enabled（未启用正式运行时）: true
  report_created（报告已生成）: true
  latest_updated（latest 已更新）: true
  git_diff_check（Git diff 格式检查）: passed
  forbidden_path_scan（禁止路径扫描）: passed_except_unrelated_untracked_public_not_staged
  secret_like_pattern_scan（密钥模式扫描）: passed_on_main_added_lines_and_sandbox_probe_files
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed_on_added_lines
  disabled_service_process_scan（禁用服务进程扫描）: passed
```

提交前还需复核 staged diff 只包含本轮允许文件，并完成 commit / push / remote readback。

## 15. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - 没有启动 FastAPI service，因此未证明 HTTP service contract。
  - 没有调用真实 LLM，因此未证明 provider 稳定性。
  - 没有调用 DashVector，因此未证明正式检索适配层。
  - 没有运行 Chroma 入库，因此未证明真实向量库写入。
  - sandbox 临时脚本没有进入主仓库代码，只作为本轮探测证据。
```

## 16. blocked_if_any（如有阻断）

```yaml
blocked_if_any（如有阻断）: null
```

## 17. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: formal_adapter_patch_plan_after_user_confirmation
```

如果继续推进，建议先做正式 adapter patch plan，而不是直接启用 runtime：把本轮 LangGraph 节点链转换成主仓库内的契约 / schema / fixture，再决定是否接 DashVector 或服务层。
