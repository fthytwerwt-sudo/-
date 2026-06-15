# 20260616 Agent Service Toolkit Full Integration Master Plan

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - mechanism_repair_flow（机制修补流）
  - adapter_master_planning_task（适配总计划任务）
  - workflow_total_inventory_task（workflow 全量盘点任务）
  - integration_classification_task（接入分类任务）
  - one_shot_integration_route_design（一次性接入路线设计）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）承载本轮总计划；adapter_infrastructure_flow（适配基础设施流）只作为候选，不启用
execution_permission（执行权限）: master_plan_report_only（只允许总计划报告）
goal_mode（Goal 模式）: active_for_plan_delivery（仅用于本轮计划交付闭环，不代表 runtime 启用）
branch（分支）: adapter/agent-service-toolkit-sandbox
active_write_executor（当前激活写入执行器）: codex
large_task_gate（大任务闸门）:
  triggered（是否触发）: true
  reason（原因）: 本轮涉及 workflow 全量盘点、上游能力分类、数据架构保真、后续一次性接入路线和 Git 同步
  lane_decision（车道判断）: read_parallel_then_serial_write（只读并行，写入串行）
supply_source_arbitration（供料来源裁决）:
  retrieval_manifest（检索清单）: source_readback_file_manifest_only（本轮只使用仓库文件回读清单，不调用向量库）
  source_readback_status（事实源回读状态）: read_ok
  deepseek_trigger_decision（DeepSeek 触发判断）: false
  not_deepseek_conclusion（是否不是 DeepSeek 结论）: true
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
service_started（是否启动服务）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
upstream_code_copied（是否复制上游源码）: false
```

本轮目标是生成一份 `agent-service-toolkit_full_integration_master_plan（全量接入总计划）`。这份文件只回答接入路线、分类、边界和准入条件，不写 adapter 代码，不启用运行时，不合并 main，不运行服务，不调用外部 API，也不推进视频、声音、视觉、发布或发送状态。

## 2. impact_check（影响面检查）

```yaml
will_modify_files（本轮会修改文件）:
  - codex_log/framework_adapter/20260616_agent_service_toolkit_full_integration_master_plan.md
  - codex_log/latest.md

must_not_modify_files（本轮禁止修改文件）:
  - AGENTS.md
  - GPT数据源/**
  - codex_source/**
  - pyproject.toml
  - requirements.txt
  - package.json
  - compose.yaml
  - docker-compose.yml
  - .env*
  - dist/**
  - public/**
  - media/**

main_branch_modification_allowed（是否允许修改 main）: false
dependency_change_allowed（是否允许改依赖）: false
runtime_start_allowed（是否允许启动运行时）: false
external_api_allowed（是否允许外部 API）: false
upstream_code_copy_allowed（是否允许复制上游源码）: false
```

如果后续任何步骤需要超出上述两个文件的写入范围，必须停止并返回 `blocked（阻断）`，不得自行扩大范围。

## 3. files_read（已读取文件）

```yaml
request_source（任务来源）:
  /Users/fan/.codex/attachments/8119a199-97e6-48c7-8064-144cdaa87c18/pasted-text.txt: read_ok

core_entry（核心入口）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/01_execution_rules.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok

adapter_reports（适配报告）:
  codex_log/framework_adapter/20260614_agent_service_toolkit_sandbox_branch_context.md: read_ok
  codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
  codex_log/framework_adapter/20260614_goal_mode_sandbox_install_completion.md: read_ok
  codex_log/framework_adapter/20260614_langgraph_rag_cleaning_integration_probe.md: read_ok
  codex_log/framework_adapter/20260614_stability_proof_closed_loop_probe.md: read_ok
  codex_log/framework_adapter/20260615_formal_adapter_patch_plan.md: read_ok

schema_and_contract_sources（schema 与契约来源）:
  codex_source/schema_contracts/00_schema_contracts_index.md: read_ok
  codex_log/framework_adapter/20260614_schema_contract_static_validation.md: read_ok

current_architecture_sources（当前架构来源）:
  GPT数据源/10_OPC一人公司闭环与多AI协作机制.md: read_ok
  GPT数据源/11_项目状态动作总控器_机制推理层.md: read_ok
  GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md: read_ok
  GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md: read_ok
  GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md: read_ok

skills_used（使用的技能）:
  plan: read_ok（用于计划型任务的输出纪律；本轮仍按用户指定路径写报告）

missing_files（缺失文件）: []
```

## 4. branch_and_status_check（分支与状态确认）

```yaml
working_branch（工作分支）: adapter/agent-service-toolkit-sandbox
remote_tracking（远端跟踪）: origin/adapter/agent-service-toolkit-sandbox
main_branch_policy（main 分支策略）: 本轮不修改 main，不把本轮计划写入 main
unrelated_dirty_files（无关脏文件）:
  - public/（未跟踪目录，保留不碰）
runtime_enabled（是否启用正式运行时）: false
fastapi_service_started（是否启动 FastAPI）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
streamlit_started（是否启动 Streamlit）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
external_api_called（是否调用外部 API）: false
```

## 5. current_required_layering（当前必须保留的架构分层）

```yaml
project_router_layer（项目状态路由层）: 视频工厂现有机制，核心为 Project State Action Router
workflow_runtime_layer（工作流运行层）: LangGraph，可作为运行图层进入 adapter，但不能替代项目路由
adapter_layer（模型 / 工具 / 检索适配层）: LangChain，可承接模型、工具、retriever、loader 适配
retrieval_store_layer（向量库层）:
  current_project（当前项目）: DashVector
  upstream_sandbox（上游沙盒）: Chroma
truth_check_layer（真实性检查层）: source_readback + human_review + completion_truth_check
write_boundary（写入边界）: active_write_executor = codex；runtime 不得直接写仓库
```

总裁决：

- `LangGraph` 进入的是 `workflow_runtime_layer（工作流运行层）`，不是 `project_router_layer（项目状态路由层）`。
- `LangChain` 进入的是 `adapter_layer（模型 / 工具 / 检索适配层）`，不是事实裁决层。
- `DashVector` 仍是当前项目主检索路线；`Chroma` 只作为上游 sandbox 学习、对照和 fixture 评估对象。
- `source_readback（原文回读）`、`retrieval_manifest（检索清单）`、`completion_truth_check（完成真实性检查）` 不能被上游 RAG、agent output 或 memory store 替代。

## 6. full_workflow_inventory（workflow 全量盘点）

### 6.1 formal_video_factory_workflows（现有 6 类正式 workflow）

| workflow（工作流） | current_home（当前归位） | current_scope（当前承载范围） | toolkit_carry_decision（是否承载 toolkit） | boundary（边界） |
|---|---|---|---|---|
| copy_testing_flow（文案测试流） | 正式 workflow | 标题、开头、最终文案、文案测试、内容结构反馈 | partial_support（部分支持） | 不默认需要 LangGraph runtime；只在需要 route / validate / interrupt / truth check 节点时接入 |
| material_evidence_flow（素材证据流） | 正式 workflow | 素材、录屏、截图、时间码、素材是否支撑文案、隐私和平台风险 | adapter_required（需要适配） | 必须补 `retrieval_manifest + source_readback_map + cleaning_adapter`；上游 page_content-only RAG 不可直接进入 |
| aesthetic_editing_flow（审美剪辑流） | 正式 workflow | 剪辑节奏、人感质量、卡片、字幕、画面可读性、候选片装配 | validate_only（只适合验证 / 阻断 / handoff） | agent-service-toolkit 当前不承接真实媒体剪辑和审美执行链 |
| quality_review_flow（质量复审流） | 正式 workflow | 审片、质量复审、技术验证与内容边界、remaining_blockers | direct_node_support（节点可直接支持） | 可用 graph 节点做 completion truth check，但不能替代人工复审 |
| data_review_flow（数据复盘流） | 正式 workflow | 24h / 72h / 7d 数据、运营复盘、下一轮唯一变量 | validator_support（验证器支持） | external memory/store 不能改写 current_data_goal_anchor、operation_records 或 review_loop |
| mechanism_repair_flow（机制修补流） | 正式 workflow | 规则修补、入口补齐、路由修补、adapter 计划、schema / fixture / probe 缺口 | direct_fit（直接承载本轮计划） | 只能承载机制计划和候选登记，不能把所有 runtime / service 基础设施硬塞为正式 workflow |

专项结论：

1. `copy_testing_flow（文案测试流）` 不默认需要 LangGraph runtime；只有当文案测试链要复用 graph 节点、人工中断或完成真值检查时才通过 adapter contract 接入。
2. `material_evidence_flow（素材证据流）` 必须需要 `retrieval_manifest（检索清单）` 和 `source_readback（原文回读）`；上游 RAG 当前只拼 `page_content`，不能直接满足。
3. `aesthetic_editing_flow（审美剪辑流）` 继续由视频工厂现有执行链负责；agent-service-toolkit 最多提供 no-write validation、blocked reason 和 handoff。
4. `quality_review_flow（质量复审流）` 可以用 LangGraph 节点做 `completion_truth_check（完成真实性检查）`，但不能用 agent output 代替人工内容复审。
5. `data_review_flow（数据复盘流）` 必须保留原数据目标锚点，不得被外部 memory/store 改写。
6. `mechanism_repair_flow（机制修补流）` 是本轮总计划主承载线。
7. `adapter_infrastructure_flow（适配基础设施流）` 有新增候选价值，但本轮只能是 candidate，不得启用为正式入口。

### 6.2 native_router_and_gate_surfaces（原生路由 / 闸门 / 总线面）

| surface（机制面） | type（类型） | relation_to_toolkit（与 toolkit 关系） | classification（接入分类） | decision（裁决） |
|---|---|---|---|---|
| Project State Action Router（项目状态动作总控器） | native_router（原生路由） | 上游不可替代，只能读取其输出后运行 | do_not_import | 不导入替代路由；LangGraph 只能执行 router 之后的图 |
| Reference-to-Execution Contract（参考到执行落地契约） | native_contract（原生契约） | 可被 graph 节点检查，但不能被 agent 重写 | direct_embed | 作为 adapter 输入检查项保留 |
| Completion Relay Gate / completion_truth_preflight_router（补全接力 / 完成真值预检） | native_gate（原生闸门） | 可映射为 completion_truth_check_node | direct_embed | 节点化保留，不允许 agent 自证完成 |
| material_delta_type_router（素材增量类型路由） | native_router（原生路由） | cleaning / retrieval adapter 可读取其分类 | adapter_required | 后续补 material_delta -> cleaning_adapter 的字段映射 |
| pre_execution_read_contract_gate（执行前读取契约闸门） | native_gate（原生闸门） | 可直接作为 graph 前置节点 | direct_embed | 保留 readback 必须性 |
| data_goal_execution_bus（数据目标执行总线） | native_bus（原生总线） | graph 可校验，不可替代 | do_not_import | 不让 external memory 改写数据目标 |
| operation_data_intake（运营数据录入） | native_flow（原生流程） | 可用 graph 检查字段完整度 | adapter_required | 只做 validation，事实仍写入 review_loop |
| operation_review / next_variable_decision（运营复盘 / 下一变量判断） | native_flow（原生流程） | 可用 source_readback + truth check 辅助 | adapter_required | 不允许 runtime 直接判断商业成立 |
| operation_decision_system（运营决策系统） | native_system（原生系统） | 可被 adapter 报告引用 | do_not_import | 不导入上游 agent 替代 |
| operation_learning_ledger（运营学习账本） | native_record（原生记录） | 可被 readback 与 manifest 引用 | adapter_required | 不用 memory store 替代 |
| copy_iteration_system（文案迭代系统） | native_flow（原生流程） | 可用 LangChain model adapter 辅助草案 / 检查 | adapter_required | locked copy 仍由项目规则约束 |
| conditional_deepseek_review_loop（DeepSeek 条件复核环） | native_review_loop（原生复核环） | 不被 toolkit 替代 | do_not_import | DeepSeek 仍按条件触发，不是默认供应商 |
| publish_candidate / delivery_baseline_gate（可发布候选 / 交付基线闸门） | native_gate（原生闸门） | graph 可检查缺项 | direct_embed | 不能把中间态写成交付态 |
| legacy gray_test aliases（旧灰度别名） | legacy_compatibility（历史兼容） | 上游无须接入 | do_not_import | 保留历史降权，不导入 |
| adapter_infrastructure_flow（适配基础设施流） | candidate_workflow（候选 workflow） | 用于 runtime / service / adapter / retrieval / schema / fixture / probe | future_candidate | 不启用；等待用户 / ChatGPT 确认 |

```yaml
formal_workflow_count（正式 workflow 数量）: 6
native_router_gate_surface_count（原生路由 / 闸门 / 总线面数量）: 15
total_workflow_surface_count（总盘点面数量）: 21
formal_direct_fit_count（正式 workflow 直接承载数量）: 1
formal_partial_or_adapter_fit_count（正式 workflow 部分 / 适配承载数量）: 5
candidate_new_workflow_count（候选新增 workflow 数量）: 1
candidate_new_workflow_enabled（候选新增 workflow 是否启用）: false
```

## 7. upstream_toolkit_capability_inventory（上游 toolkit 能力盘点）

| upstream_layer（上游层） | capability（能力） | can_connect（能否接入） | primary_classification（主分类） | connect_method（接入方式） | disabled_or_blocked_if（默认禁用 / 阻断条件） |
|---|---|---|---|---|---|
| service_layer（服务层） | FastAPI service shell、`/info`、`/invoke`、`/stream`、`/feedback`、`/history`、`/health` | can_connect_after_contract（契约后可接） | adapter_required | `service_contract_no_write_probe` 后作为 no-write service boundary | 未授权服务启动、写仓库、外部 API、secret |
| client_layer（客户端层） | sync / async client、stream client、feedback client | can_connect_as_test_shape（可作为测试形状接入） | direct_embed | 作为 service/client contract fixture 和 no-write probe 客户端形状 | 不能写仓库，不能作为状态事实 |
| workflow_runtime_layer（工作流运行层） | LangGraph StateGraph / interrupt / Command | can_connect（可接） | adapter_required | `graph_runtime_adapter_contract` | 不能替代 Project State Action Router |
| agent_layer（智能体层） | `rag-assistant` | can_connect_after_metadata_adapter（元数据适配后可接） | adapter_required | RAG 输出转 `RetrievalManifest` 后再进模型上下文 | page_content-only、缺 source/page/chunk_id |
| agent_layer（智能体层） | `interrupt-agent` | can_connect_as_pattern（可作为模式接入） | direct_embed | 作为 human_review_interrupt pattern | 不能绕过人工复审边界 |
| agent_layer（智能体层） | chatbot / research-assistant / command-agent / bg-task-agent | limited_connect（有限接入） | adapter_required | 仅作为 graph pattern 或 tool adapter 参考 | 不得直接成为视频工厂正式 workflow |
| agent_layer（智能体层） | supervisor / hierarchy agents | not_now（当前不接） | disable_by_default | 只保留学习参考 | 多 agent runtime 未准入，易扩大执行面 |
| agent_layer（智能体层） | GitHub MCP agent | not_now（当前不接） | disable_by_default | 禁用，不进入主线 | 写权限、外部连接和 active_write_executor 边界风险 |
| agent_layer（智能体层） | knowledge-base-agent | quarantine（隔离） | unmapped_quarantine | 待确认是否与 DashVector / RAG 重叠 | 缺运行时证明和项目边界 |
| adapter_layer（适配层） | LangChain model / tool / retriever / loader | can_connect（可接） | adapter_required | 模型 / 工具 / 检索 / loader adapter | 不能替代状态路由或完成真实性检查 |
| retrieval_layer（检索层） | Chroma RAG | sandbox_only（仅沙盒） | adapter_required | Chroma -> RetrievalManifest 对照适配 | 不得替代 DashVector，不运行 ingestion |
| retrieval_layer（检索层） | raw Chroma ingestion path | disabled（禁用） | unmapped_quarantine | 暂存隔离，等待 cleaning_adapter | 缺 secret scan、dedup、metadata、source_readback |
| retrieval_layer（检索层） | page_content-only context format | not_importable（不能导入） | unmapped_quarantine | 必须先改为 metadata-rich context | 缺 source、page、chunk_id，破坏 source_readback |
| retrieval_store_layer（向量库层） | DashVector adapter（项目自有方向） | must_build_later（后续必须自建适配） | adapter_required | DashVector -> RetrievalManifest | 不调用真实 DashVector，先 fixture |
| memory_layer（记忆层） | InMemory / SQLite thread state | can_connect_limited（可有限接入） | adapter_required | runtime_memory_boundary_contract | 不能替代 Git/repo/log 事实 |
| memory_layer（记忆层） | Postgres / Mongo persistence | disabled（禁用） | disable_by_default | 只保留上游参考 | 会扩大持久化和 secret 面 |
| schema_layer（schema 层） | Pydantic / typed request-response shape | can_connect（可接） | direct_embed | 映射到 schema_contracts 与 fixtures | 不直接代表 runtime 已接入 |
| test_layer（测试层） | service / client / agent tests | can_connect（可接） | direct_embed | 转为 no-write、blocked-if、fixture 验证形状 | 上游测试不能直接等于视频工厂通过 |
| cleaning_layer（清洗层） | basic ingestion / load / split pattern | can_connect_after_adapter（适配后可接） | adapter_required | `cleaning_adapter_contract` | 缺 secret scan、dedup、metadata、legacy blocker |
| frontend_layer（前端层） | Streamlit frontend | not_now（当前不接） | disable_by_default | 默认禁用 | 会扩大 UI、端口和状态面 |
| docker_layer（Docker 层） | Docker Compose / service stack | not_now（当前不接） | disable_by_default | 默认禁用 | 本轮不启动容器和服务 |
| observability_layer（观测层） | LangSmith / Langfuse / feedback telemetry | not_now（当前不接） | disable_by_default | 默认禁用 | 外部遥测、key、隐私与误报风险 |
| safeguard_layer（安全层） | safeguard / Groq sample | not_now（当前不接） | disable_by_default | 只保留概念参考 | 需要外部 API 和授权 |

## 8. integration_classification_matrix（接入分类矩阵）

分类只使用以下七类：`direct_embed`、`adapter_required`、`project_change_required`、`disable_by_default`、`unmapped_quarantine`、`do_not_import`、`future_candidate`。

### 8.1 direct_embed（可直接嵌入）

| item（项目） | target（目标位置） | why_direct（为什么可直接嵌入） | guardrail（护栏） |
|---|---|---|---|
| HumanReviewInterrupt pattern（人工复审中断模式） | quality_review_flow / completion truth graph | 与人工复审边界一致 | 不能绕过用户 / ChatGPT 复审 |
| CompletionTruthCheck deterministic node（完成真实性检查确定性节点） | quality_review_flow / mechanism_repair_flow | 已有 no-service fake model 探测证明节点形状稳定 | 只证明节点形状，不证明正式 runtime |
| WriteExecutorHandoff shape（写入执行器交接形状） | active_write_executor = codex 边界 | 与现有写入执行器交接一致 | runtime 不得直接写仓库 |
| PreExecutionReadContract gate（执行前读取契约闸门） | source_readback 前置节点 | 与仓库原文件回读机制一致 | 缺 readback 必须 blocked |
| Client/test contract shape（客户端 / 测试契约形状） | no-write probe 与 fixture | 可用于验证 service contract，不必启正式服务 | 不能把测试通过写成正式接入完成 |
| Pydantic/schema pattern（类型化 schema 模式） | schema_contracts 后续扩展 | 与现有 schema / fixture 静态验证方向一致 | schema 不是 runtime |

```yaml
direct_embed_count（可直接嵌入数量）: 6
```

### 8.2 adapter_required（需要适配层）

| item（项目） | adapter_needed（需要的适配） | first_safe_artifact（第一安全产物） | blocked_if（阻断条件） |
|---|---|---|---|
| LangGraph runtime | graph_runtime_adapter_contract | no_service_graph_contract_probe | 替代项目路由、启正式 runtime、写仓库 |
| LangChain model / tool layer | langchain_model_tool_adapter_contract | fake model / fake tool fixture | agent 直接拍板事实 |
| RAG assistant | retrieval_manifest_adapter | metadata propagation fixture | page_content-only 进入事实链 |
| Chroma sandbox output | chroma_to_retrieval_manifest_adapter | Chroma fixture -> manifest | 替代 DashVector 或运行入库 |
| DashVector formal route | dashvector_retrieval_adapter | DashVector fixture -> manifest | 未授权真实调用、维度 / collection 不明 |
| Source readback | source_readback_map_adapter | source_readback_map fixture | vector hit 替代原文回读 |
| Cleaning layer | cleaning_adapter_contract | secret / dedup / metadata blocked fixtures | 未清洗直接入库 |
| FastAPI service | service_contract_no_write_adapter | no-write service contract report | 启服务、写仓库、外部 API |
| Runtime memory | runtime_memory_boundary_contract | memory boundary probe | memory store 替代 repo facts |
| Upstream schemas | upstream_to_video_factory_schema_map | schema mapping report | 上游字段覆盖视频工厂契约 |

```yaml
adapter_required_count（需要适配数量）: 10
```

### 8.3 project_change_required（需要项目机制改动）

| item（项目） | change_needed_later（后续可能改动） | condition（触发条件） | current_status（当前状态） |
|---|---|---|---|
| workflow index extension（workflow 索引扩展） | 可能新增 `adapter_infrastructure_flow` 正式入口 | 用户 / ChatGPT 确认、fixture 与 blocked 条件齐全 | not_this_round（本轮不做） |
| schema_contracts index expansion（schema 契约索引扩展） | 增加 graph / retrieval / cleaning / service / memory schema | phase_1 获授权 | not_this_round |
| fixture / probe registry（fixture / probe 登记） | 建立 passing / blocked fixture 目录和 probe report 索引 | phase_1 获授权 | not_this_round |
| latest phase protocol（latest 阶段协议） | 后续记录 contract / probe / service 状态 | 每阶段完成后 path-limited 更新 | not_this_round |
| write_executor handoff docs（写入执行器交接文档） | 后续补 runtime -> codex handoff 契约 | no-service graph probe 通过后 | not_this_round |

```yaml
project_change_required_count（需要项目机制改动数量）: 5
```

### 8.4 disable_by_default（默认禁用）

| item（项目） | why_disabled（为什么默认禁用） | re_enable_condition（重新评估条件） |
|---|---|---|
| Streamlit frontend | 当前没有前端控制台需求，会扩大 UI 和端口面 | 用户明确需要 human-review console 并授权 |
| Docker Compose service stack | 本轮不启服务、不启容器、不扩依赖 | service contract probe 阶段另行授权 |
| Postgres / Mongo persistence | 会扩大持久化与 secret 面 | runtime memory boundary 通过后再评估 |
| GitHub MCP agent | 写权限和外部连接风险高 | 安全审查和 no-write 权限证明后 |
| LangSmith / Langfuse telemetry | 需要外部 key，存在内容外流和误报风险 | 用户明确授权外部观测 |
| supervisor / hierarchy agents as formal workflow | 容易因上游样例新增项目 workflow | 多 agent 准入标准和 fixtures 齐全后 |
| safeguard / Groq real call | 需要真实外部 API | 用户明确授权 API、key、费用和数据边界 |

```yaml
disable_by_default_count（默认禁用数量）: 7
```

### 8.5 unmapped_quarantine（未归位隔离）

| item（项目） | why_quarantined（为什么隔离） | next_judge（下一判断者） | exit_condition（解除隔离条件） |
|---|---|---|---|
| knowledge-base-agent | 与 DashVector / RAG / memory 边界重叠，缺项目侧证明 | ChatGPT + Codex probe | 明确只读用途、metadata、readback 和 no-write 边界 |
| raw Chroma ingestion path | 缺 cleaning_adapter、secret scan、dedup、metadata 和 source_readback | Codex probe | cleaning_adapter fixture 通过后再评估 |
| page_content-only RAG prompt context | 丢 source / page / chunk_id，不能满足原文回读 | Codex probe | 改为 metadata-rich context 并生成 retrieval_manifest |

```yaml
unmapped_quarantine_count（未归位隔离数量）: 3
```

### 8.6 do_not_import（不导入）

| item（项目） | covered_by（被哪个现有机制覆盖） | reason（原因） |
|---|---|---|
| runtime direct repo writer（runtime 直接写仓库） | active_write_executor = codex | 写入边界已明确，不允许 service / graph 直接写文件 |
| memory store as project facts（memory store 作为项目事实源） | Git repo + codex_log + review_loop | 项目事实必须由仓库文件回读确认 |
| Chroma as DashVector replacement（Chroma 替代 DashVector） | DashVector formal retrieval route | Chroma 只作为 sandbox / 对照 |
| agent as final decision maker（agent 作为最终决策者） | source_readback + human_review + completion_truth_check | agent 输出不能替代完成真实性检查 |

```yaml
do_not_import_count（不导入数量）: 4
```

### 8.7 future_candidate（未来候选）

| item（项目） | why_candidate（为什么是候选） | enable_condition（启用条件） | current_status（当前状态） |
|---|---|---|---|
| adapter_infrastructure_flow（适配基础设施流） | runtime / service / adapter / retrieval / schema / fixture / probe 任务会高频出现，且不属于内容生产 6 流 | 满足新增 workflow 准入条件并获用户 / ChatGPT 确认 | candidate_only（仅候选） |
| human_review_console_or_service_client（人工复审 console 或 service client） | 后续可能需要把 interrupt / feedback 变成可视化复审入口 | service no-write probe、隐私边界、用户授权齐全 | candidate_only |

```yaml
future_candidate_count（未来候选数量）: 2
```

## 9. workflow_adapter_mapping（workflow 适配映射）

| existing_video_factory_workflow（现有视频工厂 workflow） | upstream_related_capability（上游相关能力） | mapping_type（映射类型） | required_adapter_contract（需要的适配契约） | required_schema（需要的 schema） | required_fixture（需要的 fixture） | required_probe（需要的探测） | blocked_if（阻断条件） |
|---|---|---|---|---|---|---|---|
| copy_testing_flow | LangGraph route / interrupt；LangChain model adapter | partial_fit | graph_runtime_adapter_contract；write_executor_handoff_contract | workflow_route_decision；completion_truth_check | copy_source_ok / copy_source_missing_blocked | fake no-service copy route probe | agent 改写 locked copy；缺 final_script_source_check |
| material_evidence_flow | RAG assistant；cleaning layer；retriever | needs_adapter_contract | retrieval_manifest_contract；source_readback_map_contract；cleaning_adapter_contract | retrieval_manifest；source_readback；retrieval_gap_report | material_source_readback_ok / missing_source_blocked | metadata propagation probe | page_content-only 被当事实；缺 source_path / chunk_id |
| aesthetic_editing_flow | graph validation nodes only | partial_fit | completion_truth_check_node_contract；write_executor_handoff_contract | completion_truth_check；blocked_if_check | editing_review_pack_missing_blocked | no-media validation graph probe | graph/runtime 直接剪媒体；中间态冒充交付 |
| quality_review_flow | completion truth graph；source_readback node；handoff node | partial_fit + direct_node_support | completion_truth_check_node_contract | completion_truth_check；human_review_interrupt；write_executor_handoff | positive_truth_check / missing_readback_blocked | fake model deterministic graph probe | agent output 替代人工复审；状态越级推进 |
| data_review_flow | memory boundary；graph validator | partial_fit | data_goal_preservation_contract；runtime_memory_boundary_contract | cross_contract_trace；blocked_if_check | data_goal_anchor_partial_blocked | operation_records source-readback probe | memory 替代 operation_records / current_data_goal_anchor |
| mechanism_repair_flow | service / graph / schema / test / cleaning planning | direct_fit | adapter_patch_plan_contract；service_no_write_contract | workflow_route_decision；cross_contract_trace | adapter_plan_ok / runtime_write_blocked | no-service plan-to-contract probe | 把 adapter 基础设施硬塞成正式 workflow；扩大写入范围 |

## 10. unmapped_workflow_register（未归位 workflow 登记表）

| workflow_or_capability（workflow 或能力） | source（来源） | why_unmapped（为什么未归位） | risk_if_forced_into_existing_workflow（硬塞风险） | proposed_category（建议分类） | next_decision_needed（下一步需要谁判断） | current_status（当前状态） |
|---|---|---|---|---|---|---|
| adapter_infrastructure_flow（适配基础设施流） | 本轮全量接入分析 | runtime / service / adapter / retrieval / schema / fixture / probe 不属于内容生产 6 流 | 全塞进 mechanism_repair_flow 会让机制修补流变成运行时运维流 | future_candidate | ChatGPT + user | candidate |
| service_contract_probe（服务契约探测） | upstream service_layer | 属于服务边界验证，不属于文案 / 素材 / 剪辑 / 复审 / 数据生产 | 误写成正式 runtime 已接入，或允许 service 写仓库 | project_change_required | user + Codex probe | parked |
| raw Chroma ingestion | upstream retrieval_layer | 缺清洗、secret scan、metadata 和 source_readback | 污染 DashVector 主线，绕过检索清单 | unmapped_quarantine | Codex probe | blocked |
| page_content-only RAG context | upstream RAG format | 缺 source / page / chunk_id，不满足原文回读 | RAG 命中直接变成事实，破坏 truth check | unmapped_quarantine | Codex probe | blocked |
| Streamlit frontend | upstream frontend_layer | 当前不需要 UI 控制台 | UI 启动被误当正式接入 | disable_by_default | user | disabled |
| Docker / Postgres / Mongo persistence | upstream runtime layer | 属于持久化服务，不属于项目事实层 | 用数据库记忆替代 Git/repo/log | disable_by_default | user | disabled |
| GitHub MCP agent | upstream agent_layer | 外部连接和写权限风险高 | 绕过 active_write_executor 和 path-limited Git 收尾 | disable_by_default | user + security review | disabled |
| knowledge-base-agent | upstream agent_layer | 与现有 RAG / DashVector / memory 边界不清 | 产生第二套知识库事实源 | unmapped_quarantine | ChatGPT + Codex probe | parked |
| supervisor / hierarchy agents | upstream agent_layer | 样例价值大于当前主线价值 | 因上游有 agent 就新增 workflow | disable_by_default | ChatGPT + user | parked |

```yaml
quarantine_created（是否创建隔离登记）: true
forced_mapping_detected（是否发现硬塞映射）: false
candidate_new_workflows（候选新增 workflow）:
  - adapter_infrastructure_flow（适配基础设施流）
disabled_upstream_capabilities（默认禁用的上游能力）:
  - Streamlit frontend
  - Docker / Postgres / Mongo persistence
  - GitHub MCP agent
  - LangSmith / Langfuse telemetry
  - supervisor / hierarchy agents as formal workflow
  - safeguard / Groq real call
```

## 11. new_workflow_admission_criteria（新增 workflow 准入条件）

`adapter_infrastructure_flow（适配基础设施流）` 只有同时满足以下条件，才能从 candidate 升级为正式 workflow：

1. `high_frequency_trigger（高频触发）`: 多轮连续出现 runtime / service / adapter / retrieval / schema / fixture / probe 任务。
2. `existing_workflow_insufficient（现有 workflow 无法承载）`: 不是 mechanism_repair_flow 的字段扩展，也不是 quality_review_flow 的检查节点。
3. `clear_input（输入清楚）`: 输入必须是 adapter/runtime/service/schema/retrieval/fixture/probe 任务卡。
4. `clear_output（输出清楚）`: 输出必须是 contract、schema、fixture、probe report、service no-write report 或 handoff。
5. `blocked_if_defined（阻断条件清楚）`: 安装依赖、服务启动、外部 API、secret、main merge、runtime 直接写仓库、状态推进时必须阻断或另行授权。
6. `boundary_with_old_workflows（与旧 workflow 边界清楚）`: 不接管 copy/material/editing/review/data 的业务判断。
7. `fixtures_exist（fixture 存在）`: 至少有 passing / blocked fixture 证明不会越权。
8. `completion_truth_connected（完成真实性检查已接入）`: 不允许 runtime 输出绕过 source_readback、human_review 和 completion_truth_check。
9. `human_confirmation（人工确认）`: 需要用户 / ChatGPT 确认后才能写入正式 workflow 索引。

本轮结论：`adapter_infrastructure_flow` 值得保留为候选，但不得启用。

## 12. data_architecture_preservation_master_plan（数据与架构保真总计划）

```yaml
must_preserve（必须保留）:
  - current_data_goal_anchor（当前数据目标锚点）
  - operation_records（运营记录）
  - review_loop（复盘闭环）
  - data_goal_execution_bus（数据目标执行总线）
  - retrieval_manifest（检索清单）
  - source_readback（原文回读）
  - completion_truth_check（完成真实性检查）
  - write_executor_handoff（写入执行器交接）
  - human_review_boundary（人工复审边界）

must_not_replace（不得替代）:
  - 不得用 LangGraph 替代 Project State Action Router
  - 不得用 LangChain 替代状态路由器
  - 不得用 Chroma 替代 DashVector
  - 不得用 memory store 替代 Git / repo / codex_log / review_loop 事实
  - 不得用 RAG 结果替代 source_readback
  - 不得用 agent output 替代 completion_truth_check
  - 不得让 runtime 直接写仓库

adapter_bridge_needed（需要补的适配桥）:
  - retrieval_manifest_schema
  - source_readback_map_schema
  - cleaning_adapter_contract
  - graph_runtime_adapter_contract
  - write_executor_handoff_contract
  - service_contract_no_write_probe
  - completion_truth_check_node_contract
  - runtime_memory_boundary_contract
```

保真路线：

- `retrieval_manifest（检索清单）`: 每次检索必须记录 provider、query、source_path、source_id、chunk_id、page、content_hash、commit_sha、score、authority_level、readback_required 和 gap status。
- `source_readback（原文回读）`: 检索命中后必须回读当前分支仓库文件；DashVector / Chroma / agent 摘要不能直接成为事实。
- `source_readback_map（原文回读映射）`: 将 retrieval result 映射回真实文件路径、行号 / 页码 / chunk、hash 和证据强度。
- `retrieval_gap_report（检索缺口报告）`: source 缺失、metadata 缺失、低置信度、冲突命中、legacy 降权、secret 风险必须进入 gap report。
- `completion_truth_check（完成真实性检查）`: 检查报告是否把计划写成实现、把 sandbox 写成正式 runtime、把服务未启动写成已接、把状态越级推进、把 agent 输出写成事实。
- `human_review_boundary（人工复审边界）`: 质量、内容、声音、视觉、发布、商业判断仍由用户 / ChatGPT 复审；graph 只能给出证据和阻断。
- `write_executor_handoff（写入执行器交接）`: runtime 只能 route / retrieve / validate / block / interrupt / handoff，实际仓库写入仍由 `active_write_executor = codex` 执行。

## 13. contracts_schemas_fixtures_probes_before_code（写 adapter 代码前缺口）

```yaml
contracts_needed（需要的契约）:
  - graph_runtime_adapter_contract（图运行适配契约）
  - langchain_model_tool_adapter_contract（LangChain 模型 / 工具适配契约）
  - retrieval_adapter_contract（检索适配契约）
  - cleaning_adapter_contract（清洗适配契约）
  - service_no_write_contract（服务不写仓库契约）
  - runtime_memory_boundary_contract（运行时记忆边界契约）
  - write_executor_handoff_contract（写入执行器交接契约）
  - completion_truth_check_node_contract（完成真实性检查节点契约）

schemas_needed（需要的 schema）:
  - graph_runtime_adapter.schema.yaml
  - retrieval_manifest.schema.yaml（如需扩展 provider metadata 字段）
  - source_readback_map.schema.yaml
  - cleaning_adapter.schema.yaml
  - service_contract_no_write.schema.yaml
  - runtime_memory_boundary.schema.yaml
  - adapter_infrastructure_flow_candidate.schema.yaml（候选，未启用）

fixtures_needed（需要的 fixture）:
  - graph_runtime_adapter.passing.yaml
  - graph_runtime_adapter.blocked_runtime_write.yaml
  - retrieval_manifest_chroma_metadata_missing.blocked.yaml
  - retrieval_manifest_dashvector_fixture.passing.yaml
  - source_readback_missing.blocked.yaml
  - cleaning_secret_like_content.blocked.yaml
  - service_contract_no_write.passing.yaml
  - runtime_memory_boundary.blocked_repo_fact_replacement.yaml
  - completion_truth_check.false_completion_blocked.yaml
  - adapter_infrastructure_flow_candidate.blocked_without_authorization.yaml

probes_needed（需要的探测）:
  - no_service_graph_contract_probe（无服务图契约探测）
  - metadata_propagation_probe（source/page/chunk_id 元数据传播探测）
  - cleaning_adapter_fixture_probe（清洗适配 fixture 探测）
  - DashVector_adapter_fixture_probe（DashVector 适配 fixture 探测）
  - service_contract_no_write_probe（授权后服务契约不写仓库探测）
  - runtime_memory_boundary_probe（运行时 memory 不替代仓库事实探测）
  - completion_truth_check_false_claim_probe（完成真实性检查误报阻断探测）
```

## 14. one_shot_integration_route_result（一次性接入路线结果）

这里的 `one_shot（一口气接入）` 不是盲目一次性写代码，而是后续可由 Codex Goal Mode 承接的分阶段闭环：每阶段有输入、输出、验证和 hard stop。任何 hard stop 命中时必须停止，不能继续把局部结果写成完成。

```yaml
one_shot_route_name（一次性路线名称）: agent_service_toolkit_goal_mode_phased_integration
current_round_status（当前轮状态）: master_plan_only_completed_after_validation
code_implementation_allowed_now（当前是否允许写代码）: false
runtime_enablement_allowed_now（当前是否允许启 runtime）: false
main_merge_allowed_now（当前是否允许合并 main）: false
requires_user_review_before_code（写代码前是否需要用户复审）: true
```

### Phase 0｜current_master_plan_only（当前总计划阶段）

```yaml
goal（目标）: 输出全量接入总计划、workflow 盘点、能力分类、未归位登记、数据保真和后续路线。
allowed（允许）:
  - 写本报告
  - 更新 codex_log/latest.md
  - 做 Git / secret / forbidden status / remote HEAD 验证
forbidden（禁止）:
  - adapter_code_implementation
  - runtime_enablement
  - service_start
  - dependency_installation
  - external_api_call
  - main_merge
output（输出）: master plan report + latest update + git sync evidence
```

### Phase 1｜user_decision_and_contract_freeze（用户复审与契约冻结）

```yaml
goal（目标）: 用户 / ChatGPT 确认哪些分类进入后续代码阶段，哪些继续禁用或隔离。
required_decisions（必须决策）:
  - 是否保持 adapter_infrastructure_flow 为 candidate
  - 是否确认 Chroma 只作 sandbox
  - 是否确认 FastAPI 只做 no-write service probe
  - 是否确认 GitHub MCP / Streamlit / Docker 默认禁用
  - 是否确认 memory store 不替代 repo facts
output（输出）: user_decision_record + approved_contract_scope
blocked_if（阻断条件）: 用户未确认却进入代码阶段；需要启服务或 API
```

### Phase 2｜contracts_and_schemas（契约与 schema 阶段）

```yaml
goal（目标）: 创建或更新 adapter 所需 contract / schema / fixture，不写 runtime。
expected_files_later（后续可能文件）:
  - codex_source/schema_contracts/schemas/graph_runtime_adapter.schema.yaml
  - codex_source/schema_contracts/schemas/source_readback_map.schema.yaml
  - codex_source/schema_contracts/schemas/cleaning_adapter.schema.yaml
  - codex_source/schema_contracts/schemas/service_contract_no_write.schema.yaml
  - codex_source/schema_contracts/fixtures/**
validation（验证）:
  - YAML parse
  - required fields
  - passing / blocked fixture
  - forbidden status promotion scan
  - secret scan
blocked_if（阻断条件）: schema 允许 runtime 直接写仓库、fixture 缺 blocked case、需要改 main
```

### Phase 3｜no_service_graph_probe（无服务图探测）

```yaml
goal（目标）: 不启动 FastAPI，不调用外部 API，用 fake inputs 验证 graph_runtime_adapter_contract。
graph_nodes（图节点）:
  - route_decision_node
  - cleaning_adapter_node
  - retrieval_manifest_node
  - source_readback_node
  - retrieval_gap_report_node
  - executor_handoff_node
  - completion_truth_check_node
fake_inputs（假输入）:
  - repo_rule_fixture
  - latest_status_fixture
  - missing_source_fixture
output（输出）: no_service_graph_contract_probe_report
blocked_if（阻断条件）: 需要真实 API、需要启动服务、输出缺 source_readback 或 completion_truth_check
```

### Phase 4｜retrieval_and_cleaning_adapter_probe（检索与清洗适配探测）

```yaml
goal（目标）: 用 fixture 证明 Chroma sandbox 输出与 DashVector 目标输出都能转为统一 retrieval_manifest。
DashVector_boundary（DashVector 边界）: 当前项目主检索路线；先 fixture，不调用真实 DashVector。
Chroma_boundary（Chroma 边界）: sandbox 学习 / 对照对象；不得替代 DashVector。
cleaning_adapter_boundary（清洗适配边界）: 入库前必须 secret scan、dedup、metadata、source_readback、legacy blocker。
output（输出）:
  - retrieval_manifest_fixture.yaml
  - source_readback_map_fixture.yaml
  - cleaning_adapter_probe_report.md
blocked_if（阻断条件）: page_content-only 进入模型上下文、缺 source_path/chunk_id、secret scan 未跑、Chroma ingestion 需真实写库
```

### Phase 5｜authorized_service_contract_probe（授权后服务契约探测）

```yaml
goal（目标）: 仅在用户明确授权后，验证 FastAPI service contract 和 client contract。
allowed_only_after_user_authorization（用户授权后才允许）:
  - local FastAPI service start
  - local health check
  - invoke / stream contract probe
forbidden（禁止）:
  - Streamlit 默认启动
  - GitHub MCP write tools
  - Postgres / Docker 默认启动
  - external API without explicit authorization
  - runtime direct repo write
output（输出）: service_contract_no_write_probe_report
blocked_if（阻断条件）: service 要写仓库、需要 secret、需要真实外部 API、端口 / 依赖不可控
```

### Phase 6｜main_merge_candidate_review（main 合并候选复审）

```yaml
goal（目标）: contract / schema / fixture / probe 全部通过后，才评估是否回 main。
merge_required_evidence（合并所需证据）:
  - path_limited_diff_review
  - secret_scan_passed
  - forbidden_status_promotion_scan_passed
  - no_runtime_direct_write
  - source_readback_preserved
  - completion_truth_check_preserved
  - user_confirmation
blocked_if（阻断条件）: main 会被直接修改、runtime 状态被误写、证据缺失、unrelated dirty files 无法隔离
```

## 15. user_decision_board（用户 / ChatGPT 复审决策板）

| decision（待决策项） | recommended_decision（建议） | reason（原因） | required_before_code（写代码前是否必须确认） |
|---|---|---|---|
| 是否把 `adapter_infrastructure_flow` 写成正式 workflow | keep_candidate（先保留候选） | 缺正式输入 / 输出 / fixture / blocker 批准 | yes |
| Chroma 是否只作为 sandbox / 对照 | confirm_sandbox_only（确认只作沙盒） | DashVector 是当前主检索路线 | yes |
| FastAPI 是否只做 no-write service probe | confirm_no_write_probe（确认不写仓库探测） | 保护 active_write_executor 边界 | yes |
| Streamlit 是否继续默认禁用 | keep_disabled（继续禁用） | 当前没有 UI 控制台需求 | yes |
| GitHub MCP 是否继续默认禁用 | keep_disabled（继续禁用） | 写权限和外部连接风险高 | yes |
| runtime memory 是否不得替代 repo facts | confirm_boundary（确认边界） | 项目事实必须来自仓库回读 | yes |
| 是否允许后续 Codex Goal Mode 分阶段一口气接入 | allow_after_decision（复审后允许） | 可以提速，但必须按 Phase 1-6 hard stop 执行 | yes |

## 16. final_master_decision（总裁决）

```yaml
task_result.status（任务结果状态）: full_integration_master_plan_completed_after_validation
workflow_inventory_completed（workflow 盘点是否完成）: true
toolkit_capability_inventory_completed（toolkit 能力盘点是否完成）: true
integration_decision_matrix_created（接入分类矩阵是否创建）: true
direct_embed_list_created（可直接嵌入清单是否创建）: true
adapter_required_list_created（需要适配清单是否创建）: true
project_change_required_list_created（需要项目机制改动清单是否创建）: true
disable_or_quarantine_list_created（默认禁用 / 隔离清单是否创建）: true
data_architecture_master_plan_created（数据与架构保真总计划是否创建）: true
one_shot_integration_route_created（一次性接入路线是否创建）: true
user_decision_board_created（用户决策板是否创建）: true
candidate_new_workflow（候选新增 workflow）: adapter_infrastructure_flow（适配基础设施流）
candidate_new_workflow_enabled（候选新增 workflow 是否启用）: false
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
next_safe_step（下一步安全动作）: user_chatgpt_review_then_contract_schema_phase_after_confirmation
```

一句话结论：`agent-service-toolkit` 可以进入《视频工厂》的 LangGraph 工作流运行层、LangChain adapter 层、service/client/test 参考层和后续 RAG / cleaning 适配层；但它不能替代 Project State Action Router、DashVector 主检索路线、Git 仓库事实、source_readback、human_review、completion_truth_check 或 active_write_executor。下一步安全动作是让用户 / ChatGPT 复审本决策板，再决定是否进入契约与 schema 阶段。
