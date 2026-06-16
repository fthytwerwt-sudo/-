# 20260616 User Decision Record And Contract Scope

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - user_decision_record_task（用户决策记录任务）
  - contract_schema_patch_task（契约与 schema 补丁任务）
  - fixture_validation_task（样例验证任务）
  - adapter_pre_code_guardrail_task（代码接入前护栏任务）
workflow_route_decision（workflow 归位判断）: mechanism_repair_flow（机制修补流）
execution_permission（执行权限）: contracts_schemas_fixtures_only（仅契约 / schema / fixture）
branch（分支）: adapter/agent-service-toolkit-sandbox
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
service_started（是否启动服务）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
```

本记录把 20260616 全量接入总计划里的用户 / ChatGPT 决策冻结为仓库事实，作为后续代码接入前的契约范围。它不是 adapter runtime 代码，不启用服务，不代表 Chroma、FastAPI、GitHub MCP 或 memory store 已正式进入视频工厂主线。

## 2. user_decision_record（用户决策记录）

```yaml
adapter_infrastructure_flow（适配基础设施流）:
  decision（决策）: keep_candidate（继续只做候选）
  enabled（是否启用）: false
  reason（原因）: 缺正式 workflow 准入 fixture 与 blocked case，暂不写入正式 workflow 索引

Chroma（上游本地向量库）:
  decision（决策）: sandbox_only（只做 sandbox / 对照）
  replace_DashVector（是否替代 DashVector）: false
  reason（原因）: DashVector 仍是当前项目主检索路线；Chroma 只可作为上游学习、对照和 fixture 来源

FastAPI_service（FastAPI 服务）:
  decision（决策）: no_write_probe_only（只做不写仓库探测）
  can_write_repo（是否能写仓库）: false
  reason（原因）: service 只能 route / retrieve / validate / block / interrupt / handoff，不得绕过 active_write_executor

Streamlit_frontend（Streamlit 前端）:
  decision（决策）: disabled_by_default（默认禁用）
  reason（原因）: 当前没有 human-review console 授权，启动 UI 会扩大端口、状态和误报面

GitHub_MCP_agent（GitHub MCP 智能体）:
  decision（决策）: disabled_by_default（默认禁用）
  reason（原因）: 外部连接和写权限风险高，不得绕过 active_write_executor = codex

runtime_memory（运行时记忆）:
  decision（决策）: cannot_replace_repo_facts（不得替代仓库事实）
  reason（原因）: Git / repo / codex_log / review_loop 仍是项目事实源，memory 只可作为临时运行态缓存

Codex_Goal_Mode（Codex 目标模式）:
  decision（决策）: allowed_for_phased_execution（允许分阶段执行）
  current_allowed_phase（当前允许阶段）: contracts_and_schemas（契约与 schema 阶段）
  reason（原因）: 契约冻结后可进入 schema / fixture / validation 阶段，但仍不得写正式 runtime 代码
```

## 3. approved_contract_scope（已确认契约范围）

```yaml
approved_contract_scope（已确认契约范围）:
  - graph_runtime_adapter_contract（图运行适配契约）
  - retrieval_manifest_schema（检索清单结构）
  - source_readback_map_schema（原文回读映射结构）
  - cleaning_adapter_contract（清洗适配契约）
  - service_contract_no_write_schema（服务不写仓库结构）
  - runtime_memory_boundary_schema（运行时记忆边界结构）
  - completion_truth_check_node_schema（完成真实性检查节点结构）
```

## 4. status_boundary（状态边界）

```yaml
schema_landing_is_runtime（schema 落地是否等于 runtime 接入）: false
fixture_passing_is_service_available（fixture 通过是否等于正式服务可用）: false
Chroma_fixture_replaces_DashVector（Chroma fixture 是否替代 DashVector）: false
service_no_write_fixture_allows_service_start（service no-write fixture 是否允许启动服务）: false
runtime_memory_can_be_fact_source（runtime memory 是否能成为事实源）: false
agent_output_can_replace_truth_check（agent 输出是否能替代完成真实性检查）: false
runtime_can_write_repo（runtime 是否能写仓库）: false
```

## 5. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: contracts_and_schemas_static_validation_then_no_service_graph_probe_after_user_chatgpt_review
blocked_before_next_phase_if（进入下一阶段前阻断条件）:
  - schema 允许 runtime 直接写仓库
  - retrieval_manifest 缺 source_path / chunk_id / source_readback_required
  - source_readback_map 无法回指当前分支原文
  - cleaning_adapter 缺 secret scan
  - service_contract_no_write 允许 service 写仓库
  - runtime_memory_boundary 允许 memory 替代仓库事实
  - completion_truth_check_node 允许技术成功冒充内容成功
```
