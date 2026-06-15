# 20260615 Formal Adapter Patch Plan

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - mechanism_repair_flow（机制修补流）
  - adapter_planning_task（适配计划任务）
  - workflow_routing_reconciliation（workflow 归位校准）
  - data_architecture_preservation_plan（数据与架构保真计划）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
execution_permission（执行权限）: plan_report_only（只允许计划报告）
branch（分支）: adapter/agent-service-toolkit-sandbox
active_write_executor（当前激活写入执行器）: codex
large_task_gate（大任务闸门）:
  triggered（是否触发）: true
  reason（原因）: 多文件读取、workflow 映射、adapter 分层、latest 与 Git 收尾
  lane_decision（车道判断）: read_parallel_then_serial_write（只读并行，写入串行）
supply_source_arbitration（供料来源裁决）:
  retrieval_manifest（检索清单）: source_readback_file_manifest_only（本轮只用仓库原文件回读清单）
  source_readback_status（事实源回读状态）: read_ok
  deepseek_trigger_decision（DeepSeek 触发判断）: false
  not_deepseek_conclusion（不是 DeepSeek 结论）: true
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
upstream_code_copied（是否复制上游源码）: false
```

本轮只把当前《视频工厂》已有 workflow、schema 契约、数据保真规则和 `agent-service-toolkit` 上游能力整理成正式适配补丁计划。它不是 runtime 启用，不是 adapter 代码实现，不是 main 合并，也不是视频、声音、视觉或发布状态推进。

## 2. impact_check（影响面检查）

```yaml
will_modify_files（本轮会修改文件）:
  - codex_log/framework_adapter/20260615_formal_adapter_patch_plan.md
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

## 3. files_read（已读取文件）

```yaml
core_entry（核心入口）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/01_execution_rules.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok

adapter_branch_context（adapter 分支上下文）:
  codex_log/framework_adapter/20260614_agent_service_toolkit_sandbox_branch_context.md: read_ok
  codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
  codex_log/framework_adapter/20260614_goal_mode_sandbox_install_completion.md: read_ok
  codex_log/framework_adapter/20260614_langgraph_rag_cleaning_integration_probe.md: read_ok
  codex_log/framework_adapter/20260614_stability_proof_closed_loop_probe.md: read_ok

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
  workflow-patterns: read_ok

missing_files（缺失文件）: []
```

## 4. branch_and_status_check（分支与状态确认）

```yaml
working_branch（工作分支）: adapter/agent-service-toolkit-sandbox
main_branch_policy（main 分支策略）: 不修改 main，不把本轮计划写入 main
unrelated_dirty_files（无关脏文件）:
  - public/（未跟踪，保留不碰）
runtime_enabled（是否启用正式运行时）: false
fastapi_service_started（是否启动 FastAPI）: false
docker_started（是否启动 Docker）: false
postgres_started（是否启动 Postgres）: false
streamlit_started（是否启动 Streamlit）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
external_api_called（是否调用外部 API）: false
```

## 5. required_layering（必须保留的架构分层）

```yaml
project_router_layer（项目状态路由层）: 视频工厂现有机制
workflow_runtime_layer（工作流运行层）: LangGraph
adapter_layer（模型 / 工具 / 检索适配层）: LangChain
retrieval_store_layer（向量库层）:
  current_project（当前项目）: DashVector
  upstream_sandbox（上游沙盒）: Chroma
truth_check_layer（真实性检查层）: source_readback + human_review + completion_truth_check
```

裁决原则：

- `LangGraph` 可进入工作流运行层，但不得替代 `Project State Action Router（项目状态动作总控器）`。
- `LangChain` 可进入模型 / 工具 / retriever / loader 适配层，但不得替代状态路由、事实裁决或完成真实性检查。
- `DashVector` 保持当前项目主检索路线；`Chroma` 只作为 sandbox 学习和并存评估对象。
- `source_readback（原文回读）`、`human_review（人工复审）`、`completion_truth_check（完成真实性检查）` 仍是完成声明前的真值链。

## 6. workflow_inventory（工作流盘点）

### 6.1 copy_testing_flow（文案测试流）

```yaml
workflow_type（工作流类型）: copy_testing_flow
current_scope（当前承载范围）: 最终文案、标题、开头、文案测试、Perplexity 初稿、ChatGPT 落稿、内容结构反馈
input_signal（输入信号）: 文案 / 标题 / 开头 / 下一条视频 / 内容结构反馈
must_read（必须读取）:
  - GPT数据源/04_选题与文案规则.md
  - GPT数据源/05_文案路由规则.md
  - GPT数据源/07_AI知识类视频价值规则.md
  - GPT数据源/08_当前正式事实.md
  - codex_log/current_data_goal_anchor.md
required_handoff（必须交接件）:
  - material_detail_report
  - final_script_source_check
  - content_route_card_v2
  - script_anchor_extraction_function_output
blockers（阻断条件）: 最终文案来源不明、素材细节缺失却要定稿、数据锚点未 ready 却要写正式数据驱动执行
what_it_can_absorb（能吸收什么新能力）: LangGraph 的 route / validate / interrupt 节点可用于文案测试前置检查；LangChain 可做模型与工具适配
what_it_cannot_absorb（不能吸收什么新能力）: 不能吸收 runtime/service/Chroma ingestion/schema fixture 等 adapter 基础设施；不能让 agent 自动重写最终文案
```

适配判断：`partial_fit（部分对应）`。不强制需要 LangGraph runtime；只有当文案测试需要可复用节点链、人工中断或完成真值检查时，才通过 adapter contract 接入。

### 6.2 material_evidence_flow（素材证据流）

```yaml
workflow_type（工作流类型）: material_evidence_flow
current_scope（当前承载范围）: 素材、录屏、截图、时间码、素材是否支撑文案、隐私 / 平台风险、素材报告
input_signal（输入信号）: 新素材、替换素材、录屏、截图、素材审计、素材能否支撑文案
must_read（必须读取）:
  - skills/视频素材解析_video_material_audit/SKILL.md
  - GPT数据源/05_文案路由规则.md
  - GPT数据源/07_AI知识类视频价值规则.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
required_handoff（必须交接件）:
  - material_delta_type_router_output
  - pre_execution_read_gate_output
  - material_parse_pack
  - source_segment_inventory
  - material_detail_report
  - material_evidence_contract
  - line_visual_alignment_report
  - missing_material_or_blocked_report
blockers（阻断条件）: 素材解析包缺失、时间码缺失、关键证据不可见、证据只能弱相关、需要补录却继续剪
what_it_can_absorb（能吸收什么新能力）: retrieval_manifest / source_readback / cleaning_adapter 输出可作为素材证据的检索与回读证明
what_it_cannot_absorb（不能吸收什么新能力）: 上游 RAG 的 page_content-only 输出不能直接当素材证据；Chroma ingestion 不能绕过素材解析 skill 和 source_readback
```

适配判断：`partial_fit + needs_adapter_contract（部分对应 + 需要适配契约）`。必须补 `retrieval_manifest_schema`、`source_readback_map_schema`、`cleaning_adapter_contract` 后才可接上游 RAG 能力。

### 6.3 aesthetic_editing_flow（审美剪辑流）

```yaml
workflow_type（工作流类型）: aesthetic_editing_flow
current_scope（当前承载范围）: 剪辑节奏、人感质量、卡片、字幕、画面可读性、可发布候选片装配
input_signal（输入信号）: 剪辑不顺、像 demo、不美观、卡片挡画面、重做中段、可发布候选片
must_read（必须读取）:
  - material_parse_pack
  - source_segment_inventory
  - GPT数据源/07_AI知识类视频价值规则.md
  - GPT数据源/08_当前正式事实.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
  - codex_source/19_project_state_action_router.md
  - codex_source/21_codex_judgment_permission_matrix.md
required_handoff（必须交接件）:
  - script_to_shot_execution_map
  - material_usage_ledger
  - duplicate_material_check
  - editing_decision_pack
  - visual_readability_report
  - review_pack
blockers（阻断条件）: 缺 line_group 级映射、核心证据不可读、字幕 / 卡片 high severity overlap、技术预览冒充完成
what_it_can_absorb（能吸收什么新能力）: LangGraph 可作为后续剪辑前检查图或 completion_truth_check 图节点
what_it_cannot_absorb（不能吸收什么新能力）: agent-service-toolkit 当前没有视频剪辑、媒体探针、审美验收或画面证据执行能力；不应把 aesthetic editing 迁入上游 service 主线
```

适配判断：`partial_fit（部分对应）`。审美剪辑继续由视频工厂现有执行链负责；上游框架最多提供 no-write 检查、阻断和 handoff，不进入媒体执行。

### 6.4 quality_review_flow（质量复审流）

```yaml
workflow_type（工作流类型）: quality_review_flow
current_scope（当前承载范围）: 审片、质量问题、技术验证、内容验证边界、send_ready、remaining_blockers、声音 / TTS 冲突
input_signal（输入信号）: 复审、质量问题、不合格、不顺、不美观、technical_preview、full.mp4、route card
must_read（必须读取）:
  - codex_log/latest.md
  - GPT数据源/08_当前正式事实.md
  - GPT数据源/07_AI知识类视频价值规则.md
  - dist/latest_review_pack/summary.json
  - dist/latest_review_pack/review_manifest.md
  - codex_source/19_project_state_action_router.md
required_handoff（必须交接件）:
  - completion_truth_preflight_router_output
  - voice_route_conflict_gate_output
  - quality_issue_classifier_output
  - technical_validation
  - content_validation_boundary
  - remaining_blockers
blockers（阻断条件）: 技术验证写成内容验证、缺审片包或关键媒体证据、用户未确认却推进 send_ready
what_it_can_absorb（能吸收什么新能力）: LangGraph 的确定性节点链可承载 completion_truth_check、source_readback_missing_block、executor_handoff_boundary_check
what_it_cannot_absorb（不能吸收什么新能力）: agent output 不能替代 ChatGPT / 用户的人感复审；检索命中不能替代审片包和媒体证据
```

适配判断：`partial_fit + direct_node_fit（部分对应 + 节点可直接适配）`。上轮 sandbox 已证明 fake/no-service 图节点可稳定做 completion truth check，但只能作为节点链证明，不是正式 runtime。

### 6.5 data_review_flow（数据复盘流）

```yaml
workflow_type（工作流类型）: data_review_flow
current_scope（当前承载范围）: 24h / 72h / 7d 数据、平台数据、私信 / 咨询、运营复盘、下一轮唯一变量
input_signal（输入信号）: 发布后数据、播放、收藏、私信、咨询、下一轮只改一个变量
must_read（必须读取）:
  - review_loop/00_review_loop_readme.md
  - codex_log/current_operation_target.md
  - review_loop/operation_records_index.md
  - codex_log/current_data_goal_anchor.md
  - codex_log/current_gray_test_target.md
required_handoff（必须交接件）:
  - operation_data_record
  - missing_fields_report
  - threshold_check
  - next_variable_draft
blockers（阻断条件）: video_id 不明、时间窗不明、数据字段缺失、数据不足却判断成败、一次改多个主变量
what_it_can_absorb（能吸收什么新能力）: 图节点可检查 operation_records / current_data_goal_anchor / data_goal_execution_bus 是否齐全
what_it_cannot_absorb（不能吸收什么新能力）: 外部 memory store 不能替代 Git 仓库事实、operation_records 或 current_data_goal_anchor；Postgres / LangGraph store 不能改写数据目标
```

适配判断：`partial_fit（部分对应）`。runtime memory 只能保存临时线程状态，不能成为数据事实源。

### 6.6 mechanism_repair_flow（机制修补流）

```yaml
workflow_type（工作流类型）: mechanism_repair_flow
current_scope（当前承载范围）: 规则修补、入口补齐、路由修补、索引缺口、执行纪律、fallback、adapter 计划
input_signal（输入信号）: 修规则、补入口、外部 framework 接入计划、schema / fixture / probe 缺口、执行边界不清
must_read（必须读取）:
  - AGENTS.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
  - codex_source/19_project_state_action_router.md
  - codex_log/latest.md
  - 被影响的具体机制 / adapter 报告文件
required_handoff（必须交接件）:
  - impact_check
  - affected_entry_files
  - implementation_design_layer
  - fixture_or_keyword_check
  - status_boundary_report
blockers（阻断条件）: 已有等价索引会重复、需要生成视频 / 音频、需要推进内容 / 发布 / 声音 / 视觉状态、本地脏改无法隔离
what_it_can_absorb（能吸收什么新能力）: 本轮正式适配计划、schema / contract / fixture / probe 规划、adapter 基础设施候选登记
what_it_cannot_absorb（不能吸收什么新能力）: 不能把所有未归位上游能力硬塞进机制修补流；runtime/service/adapter infrastructure 应单列 candidate
```

适配判断：`direct_fit（直接对应）`。本轮报告由此 workflow 承载。

## 7. upstream_capability_map（上游能力地图）

| layer（层） | keep（保留） | adapt（适配） | disable_by_default（默认禁用） | prune_later（以后再删） | do_not_import（不导入） | reason（原因） | evidence_source（证据来源） |
|---|---|---|---|---|---|---|---|
| service_layer（服务层） | FastAPI service shell | route / retrieve / validate / interrupt / handoff | 服务启动 | Streamlit service wrapper 可后评估 | direct_file_write | `/invoke` / `/stream` / `/history` 等有服务边界价值，但正式接入前只能 no-write | 20260614_external_framework_full_intake_design、20260614_langgraph_rag_cleaning_integration_probe |
| agent_layer（智能体层） | agent registry / selected graph references | `rag-assistant`、`interrupt-agent`、completion truth graph | GitHub MCP、knowledge-base agent、supervisor 直接主线化 | 长期无用 agent 示例 | agent 直接写仓库 | agent 能提供图节点形状，但权限必须收窄到 workflow router / validator / handoff | 20260614_langgraph_rag_cleaning_integration_probe |
| workflow_runtime_layer（LangGraph 工作流运行层） | StateGraph / Pregel / interrupt / Command | route -> clean -> retrieve -> readback -> handoff -> truth check | production runtime enable | 不适用 | 替代 Project State Action Router | LangGraph 是运行层，不是项目状态裁决层 | 20260614_stability_proof_closed_loop_probe |
| adapter_layer（LangChain 适配层） | model/tool/retriever/loader interfaces | 模型、工具、检索、loader 适配 | completion proof | 不适用 | 替代状态路由器 | LangChain 适合 adapter，不适合拍板项目事实 | 20260614_langgraph_rag_cleaning_integration_probe |
| retrieval_layer（检索层） | Chroma sandbox reference | 统一到 RetrievalManifest，后续加 DashVector adapter | Chroma formal path | DashVector adapter 证明后可裁剪 Chroma sample | page_content-only RAG 直接主线化 | 上游 RAG 丢 source/page/chunk_id，不能满足 source_readback | 20260614_langgraph_rag_cleaning_integration_probe |
| memory_layer（记忆层） | SQLite / InMemory for sandbox thread state | interrupt resume / short-lived runtime state | Postgres / Mongo formal persistence | 若无需 runtime persistence 可裁剪 | memory store 替代 repo facts | 项目事实仍在 Git/repo/log；memory 只保存运行态 | 20260614_external_framework_full_intake_design |
| client_layer（客户端层） | sync / async invoke / stream / feedback client | no-write closed loop probe client | external feedback to telemetry | 不适用 | client 直接写仓库 | 可作为 service contract test 形状 | 20260614_external_framework_full_intake_design |
| frontend_layer（前端层） | 文件结构保留 | 未来人工复审 console 候选 | Streamlit 默认禁用 | 闭环稳定且无 console 价值后 prune | 当前不导入主线 UI | 当前任务不需要前端，会扩大端口、voice、状态面 | 20260614_external_framework_full_intake_design |
| docker_layer（Docker 层） | compose / Dockerfile 作为上游参考 | 授权后 sandbox service contract probe | Docker / Postgres / Streamlit 默认禁用 | 不走容器时可裁剪本地适配 | 本轮不运行 | 会扩大服务、secret、端口面 | 20260614_external_framework_full_intake_design |
| test_layer（测试层） | service / client / schema / agent test shape | 视频工厂 schema / fixture / no-write contract tests | voice / docker e2e 首轮禁用 | 不适用 | 上游测试直接当视频工厂通过 | 测试形状有价值，但须补视频工厂契约字段 | 20260614_schema_contract_static_validation |
| cleaning_layer（清洗层） | basic ingestion reference | `video_factory_cleaning_adapter` | raw Chroma ingestion | DashVector path 成熟后可裁剪 sample | 未经清洗直接入库 | 缺 secret scan、dedup、metadata、source_readback、legacy blocker | 20260614_langgraph_rag_cleaning_integration_probe |

## 8. workflow_adapter_mapping（workflow 适配映射）

| existing_video_factory_workflow（现有视频工厂 workflow） | upstream_related_capability（上游相关能力） | mapping_type（映射类型） | required_adapter_contract（需要的适配契约） | required_schema（需要的 schema） | required_fixture（需要的 fixture） | required_probe（需要的探测） | blocked_if（阻断条件） |
|---|---|---|---|---|---|---|---|
| copy_testing_flow | LangGraph route / interrupt；LangChain model adapter | partial_fit | graph_runtime_adapter_contract；write_executor_handoff_contract | workflow_route_decision；completion_truth_check | copy_test_passing / copy_source_missing_blocked | fake no-service copy route probe | agent 改写 locked copy；缺 final_script_source_check |
| material_evidence_flow | RAG tool；cleaning script；retriever | needs_adapter_contract | retrieval_manifest_contract；source_readback_map_contract；cleaning_adapter_contract | retrieval_manifest；source_readback；retrieval_gap_report | material_source_readback_passing / missing_source_blocked | metadata propagation probe | page_content-only 被当事实；缺 source_path / chunk_id |
| aesthetic_editing_flow | LangGraph validation nodes only | partial_fit | completion_truth_check_node_contract；write_executor_handoff_contract | completion_truth_check；blocked_if_check | editing_review_pack_missing_blocked | no-media validation graph probe | graph/runtime 直接剪媒体；技术预览冒充完成 |
| quality_review_flow | completion truth graph；source_readback node；executor handoff node | partial_fit | completion_truth_check_node_contract | completion_truth_check；human_review_interrupt；write_executor_handoff | positive_truth_check / missing_readback_blocked | fake model deterministic graph probe | agent output 替代人工复审；推进 send_ready |
| data_review_flow | memory/store；graph validator | partial_fit | data_goal_preservation_contract；runtime_memory_boundary_contract | cross_contract_trace；blocked_if_check | data_goal_anchor_partial_blocked | operation_records source-readback probe | memory 替代 operation_records / current_data_goal_anchor |
| mechanism_repair_flow | service / graph / schema / test / cleaning planning | direct_fit | adapter_patch_plan_contract；service_no_write_contract | workflow_route_decision；cross_contract_trace | adapter_plan_passing / runtime_write_blocked | no-service plan-to-contract probe | 把 adapter 基础设施硬塞为正式 workflow；扩大写入范围 |
| adapter_infrastructure_flow（候选） | service/runtime/retrieval/schema/fixture/probe infrastructure | infrastructure_only + candidate_new_workflow | adapter_infrastructure_flow_contract（后续如获确认） | graph_runtime_adapter；retrieval_manifest；cleaning_adapter；service_contract | infra_candidate_passing / forbidden_runtime_blocked | contract-only probe | 本轮不得启用；缺高频证据、输入输出、阻断条件或用户确认 |

专项回答：

1. `copy_testing_flow` 不默认需要 LangGraph runtime；需要复用图节点链或人工中断时才接。
2. `material_evidence_flow` 必须需要 `retrieval_manifest / source_readback`；上游 RAG 不能直接满足。
3. `aesthetic_editing_flow` 继续由现有视频工厂执行链负责；上游框架只可做 no-write 验证和 handoff。
4. `quality_review_flow` 可以用 graph 节点做 `completion_truth_check`，但不能替代人工内容复审。
5. `data_review_flow` 必须保留 `current_data_goal_anchor / operation_records / review_loop`，不得被外部 memory/store 改写。
6. `mechanism_repair_flow` 是本轮主要承载线。
7. 需要新增 `adapter_infrastructure_flow` 的候选登记，但本轮只能标为 candidate，不能写入正式入口或默认 workflow。

## 9. unmapped_workflow_register（未归位 workflow 登记表）

| workflow_or_capability（workflow 或能力） | source（来源） | why_unmapped（为什么未归位） | risk_if_forced_into_existing_workflow（硬塞风险） | proposed_category（建议分类） | next_decision_needed（下一步判断） | current_status（当前状态） |
|---|---|---|---|---|---|---|
| adapter_infrastructure_flow（适配基础设施流） | 本轮归位分析 | runtime / service / adapter / schema / fixture / probe 不属于内容生产 6 流 | 全塞进 mechanism_repair_flow 会让机制修补流变成 runtime 运维流 | adapter_infrastructure_candidate + candidate_new_workflow | ChatGPT + user | candidate |
| FastAPI service contract probe | upstream service_layer | 属于服务契约，不属于文案 / 素材 / 剪辑 / 复审 / 数据 / 机制正文 | 误写成 runtime 已接入或允许 service 写仓库 | adapter_infrastructure_candidate | user authorization + Codex probe | parked |
| raw Chroma ingestion | upstream retrieval_layer | 只有基础入库，缺 source metadata 与 source_readback | 污染 DashVector 主线，绕过清洗和 secret scan | upstream_only_disabled | Codex probe | disabled |
| Streamlit frontend | upstream frontend_layer | 当前视频工厂没有前端控制台需求 | 启动 UI 被误当正式 runtime 或人工复审 console | upstream_only_disabled | user | disabled |
| Docker / Postgres / Mongo persistence | upstream docker / memory layer | 属于 runtime persistence，不属于项目事实层 | 用数据库 memory 替代 Git/repo/log 事实 | upstream_only_disabled | user authorization | disabled |
| GitHub MCP agent | upstream agent_layer | 外部连接与写权限风险高，本轮不需要 | agent 绕过 active_write_executor 和 path-limited Git 收尾 | upstream_only_disabled | user + security review | disabled |
| LangSmith / Langfuse feedback | upstream service/test layer | 外部遥测需 key，当前不需要 | 任务内容外泄或 false observability claim | upstream_only_disabled | user | disabled |
| supervisor / hierarchy multi-agent examples | upstream agent_layer | 有学习价值，但当前没有正式多 agent runtime 准入 | 新增 workflow 只因上游有 agent，导致过度架构 | orphan_uncertain | ChatGPT + Codex probe | parked |
| page_content-only RAG context | upstream RAG tool | 丢弃 source/page/chunk_id，不满足检索清单 | RAG 命中直接变成事实，破坏 completion_truth_check | duplicate_or_overlap | Codex probe | blocked |

硬规则执行结果：

```yaml
forced_mapping_detected（是否发现硬塞映射）: false
candidate_new_workflows（候选新增 workflow）:
  - adapter_infrastructure_flow（适配基础设施流，候选，未启用）
disabled_upstream_capabilities（默认禁用的上游能力）:
  - Streamlit frontend
  - Docker / Postgres / Mongo runtime persistence
  - GitHub MCP agent
  - raw Chroma ingestion
  - LangSmith / Langfuse external telemetry
  - supervisor / hierarchy agents as formal workflow
```

## 10. new_workflow_admission_criteria（新增 workflow 准入条件）

新增 workflow 不能因为上游存在 agent 或 service 就成立。后续只有同时满足以下条件，才允许把 `adapter_infrastructure_flow` 从 candidate 升级为正式 workflow：

1. `high_frequency_trigger（高频触发）`: 至少连续多轮出现 runtime / service / adapter / schema / fixture / probe 任务，且用现有 6 类承载会持续失真。
2. `existing_workflow_insufficient（现有 workflow 无法承载）`: 不是 mechanism_repair_flow 的字段扩展，也不是 quality_review_flow 的检查节点。
3. `clear_input（输入清楚）`: 输入必须是 adapter/runtime/service/schema/retrieval/fixture/probe 任务卡，不是普通视频执行或文案任务。
4. `clear_output（输出清楚）`: 输出必须是 contract、schema、fixture、probe report、service no-write report、handoff，不是 runtime enabled。
5. `blocked_if_defined（阻断条件清楚）`: 需要安装、服务启动、API、secret、main merge、写仓库、状态推进时必须阻断或另行授权。
6. `boundary_with_old_workflows（与旧 workflow 边界清楚）`: 不接管 copy/material/editing/review/data 的业务判断。
7. `human_confirmation（人工确认）`: 需要 ChatGPT / 用户确认后才能写入正式 workflow 索引。
8. `fixtures_exist（fixture 存在）`: 至少有 passing / blocked fixture 证明不会越权。
9. `completion_truth_connected（完成真实性检查已接入）`: 不能让 runtime 输出绕过 `source_readback + human_review + completion_truth_check`。

## 11. data_architecture_preservation_plan（数据与架构保真计划）

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
  - 不得用 memory store 替代 GitHub / repo 仓库事实
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
```

保真执行说明：

- `current_data_goal_anchor` 与 `operation_records` 仍由仓库文件和 review_loop 维护；runtime memory 只可保存临时 thread state。
- `retrieval_manifest` 必须记录 provider、query、source_path、chunk_id、content_hash、commit_sha、authority_level、status_label、score 和 `source_readback_required = true`。
- `source_readback` 必须回读当前分支仓库原文件；DashVector / Chroma / agent 摘要都不是完成证明。
- `completion_truth_check` 必须检查 false completion claims，包括 runtime enabled、sandbox created、content passed、send_ready、voice passed、visual locked、publish success、DeepSeek false participation。
- `write_executor_handoff` 必须保持 `active_write_executor = codex`，runtime 只能 route / retrieve / validate / block / interrupt / handoff。

## 12. contracts_schemas_fixtures_probes_needed（正式写 adapter 前缺口）

```yaml
contracts_needed（需要的契约）:
  - graph_runtime_adapter_contract（图运行适配契约）
  - retrieval_adapter_contract（检索适配契约）
  - cleaning_adapter_contract（清洗适配契约）
  - service_no_write_contract（服务不写仓库契约）
  - runtime_memory_boundary_contract（运行时记忆边界契约）
  - adapter_infrastructure_flow_candidate_contract（适配基础设施候选契约）

schemas_needed（需要的 schema）:
  - graph_runtime_adapter.schema.yaml
  - retrieval_manifest.schema.yaml（如需扩展 provider metadata 字段）
  - source_readback_map.schema.yaml
  - cleaning_adapter.schema.yaml
  - service_contract_no_write.schema.yaml
  - adapter_infrastructure_flow.schema.yaml（候选，未启用）

fixtures_needed（需要的 fixture）:
  - graph_runtime_adapter.passing.yaml
  - graph_runtime_adapter.blocked_runtime_write.yaml
  - retrieval_manifest_chroma_metadata_missing.blocked.yaml
  - retrieval_manifest_dashvector_fixture.passing.yaml
  - source_readback_missing.blocked.yaml
  - cleaning_secret_like_content.blocked.yaml
  - service_contract_no_write.passing.yaml
  - adapter_infrastructure_flow_candidate.blocked_without_authorization.yaml

probes_needed（需要的探测）:
  - no_service_graph_contract_probe（无服务图契约探测）
  - metadata_propagation_probe（source/page/chunk_id 元数据传播探测）
  - cleaning_adapter_fixture_probe（清洗适配 fixture 探测）
  - DashVector_adapter_fixture_probe（DashVector 适配 fixture 探测）
  - service_contract_no_write_probe（授权后服务契约不写仓库探测）
  - runtime_memory_boundary_probe（运行时 memory 不替代仓库事实探测）
```

## 13. adapter_phase_plan（分阶段适配计划）

```yaml
phase_0_current_report_only（当前计划阶段）:
  goal（目标）: 完成正式适配补丁计划，建立 workflow 归位、上游能力地图、未归位登记、数据保真和阶段路线。
  allowed（允许）:
    - 写 codex_log/framework_adapter/20260615_formal_adapter_patch_plan.md
    - 更新 codex_log/latest.md
    - 做 Markdown / Git / secret / forbidden status 验证
  forbidden（禁止）:
    - runtime_enablement
    - adapter_code_implementation
    - main_merge
    - dependency_installation
    - service_start
    - external_api_call
  output（输出）: formal_adapter_patch_plan + latest update + commit/push/readback

phase_1_contracts_and_schemas（契约与 schema 阶段）:
  goal（目标）: 把本计划里的 adapter bridge 转为 schema / contract / fixture。
  files_to_create_or_update_later（后续可能创建或更新文件）:
    - codex_source/schema_contracts/schemas/graph_runtime_adapter.schema.yaml
    - codex_source/schema_contracts/schemas/source_readback_map.schema.yaml
    - codex_source/schema_contracts/schemas/cleaning_adapter.schema.yaml
    - codex_source/schema_contracts/schemas/service_contract_no_write.schema.yaml
    - codex_source/schema_contracts/fixtures/**
  validation（验证）: YAML parse、required fields、passing / blocked fixture、forbidden status scan、secret scan
  blocked_if（阻断条件）: 需要启用 runtime、需要改 main、schema 允许 runtime 直接写仓库、fixture 缺 blocked case

phase_2_no_service_graph_probe（无服务图探测阶段）:
  goal（目标）: 不启动 FastAPI，不调用外部 API，用 fake input 验证 graph_runtime_adapter_contract。
  graph_nodes（图节点）:
    - route_decision_node
    - cleaning_adapter_node
    - retrieval_manifest_node
    - source_readback_node
    - retrieval_gap_report_node
    - executor_handoff_node
    - completion_truth_check_node
  fake_inputs（假输入）:
    - repo rule fixture
    - latest status fixture
    - missing source fixture
  output（输出）: no_service_graph_probe_report
  blocked_if（阻断条件）: 需要真实 API、需要启动服务、输出缺 source_readback 或 completion_truth_check

phase_3_retrieval_and_cleaning_adapter_probe（检索与清洗适配探测阶段）:
  goal（目标）: 用 fixture 验证 Chroma sandbox 输出和 DashVector 目标输出都能转为统一 retrieval_manifest。
  DashVector_boundary（DashVector 边界）: 当前项目主检索路线；先 fixture，不调用真实 DashVector。
  Chroma_boundary（Chroma 边界）: sandbox 学习 / 对照对象；不得替代 DashVector。
  cleaning_adapter_boundary（清洗适配边界）: 入库前必须 secret scan、dedup、metadata、source_readback、legacy blocker。
  output（输出）:
    - retrieval_manifest_fixture.yaml
    - source_readback_map_fixture.yaml
    - cleaning_adapter_probe_report.md
  blocked_if（阻断条件）: page_content-only 进入模型上下文、缺 source_path/chunk_id、secret scan 未跑、Chroma ingestion 需真实写库

phase_4_service_contract_probe_after_authorization（授权后服务契约探测阶段）:
  goal（目标）: 仅在用户明确授权后，验证 service contract；优先 no-write / fake model。
  allowed_only_after_user_authorization（授权后才允许）:
    - FastAPI service start
    - local service health check
    - invoke / stream contract probe
  forbidden（禁止）:
    - Streamlit 默认启动
    - GitHub MCP write tools
    - Postgres / Docker 默认启动
    - external API without explicit key authorization
    - runtime 直接写仓库
  output（输出）: service_contract_no_write_probe_report

phase_5_main_merge_candidate_review（main 合并候选复审阶段）:
  goal（目标）: 只有 contract / schema / fixture / probe 通过后，才评估是否回 main。
  merge_required_evidence（合并所需证据）:
    - path-limited diff review
    - secret scan passed
    - forbidden status promotion scan passed
    - no runtime direct write
    - source_readback and completion_truth_check preserved
    - user confirmation
  user_confirmation_required（是否需要用户确认）: true
  blocked_if（阻断条件）: main 会被直接修改、runtime 状态被写成启用、证据缺失、unrelated dirty files 无法隔离
```

## 14. validation_plan_for_this_round（本轮验证计划）

```yaml
markdown_report_created（报告是否创建）: expected_true
latest_updated（latest 是否更新）: expected_true
git_diff_check（Git diff 格式检查）: required
forbidden_path_scan（禁止路径扫描）: required
secret_like_pattern_scan（密钥模式扫描）: required
forbidden_status_promotion_scan（禁止状态推进检查）: required
runtime_not_enabled（runtime 未启用）: required
external_api_not_called（外部 API 未调用）: required
main_branch_untouched（main 未修改）: required
path_limited_stage_commit_push_remote_readback（限定路径提交推送远端回读）: required
```

## 15. final_decision（本轮结论）

```yaml
task_result.status（任务结果状态）: formal_adapter_patch_plan_completed_after_git_sync
workflow_mapping_completed（workflow 映射是否完成）: true
unmapped_workflow_register_created（未归位 workflow 登记是否创建）: true
data_architecture_preservation_plan_created（数据与架构保真计划是否创建）: true
candidate_new_workflow_count（候选新增 workflow 数量）: 1
candidate_new_workflow（候选新增 workflow）: adapter_infrastructure_flow（适配基础设施流）
candidate_new_workflow_enabled（候选新增 workflow 是否启用）: false
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
next_safe_step（下一步安全动作）: contract_and_schema_patch_plan_after_user_confirmation
```

一句话结论：`agent-service-toolkit` 可以作为 LangGraph 工作流运行层、LangChain adapter 层和 service/client/test 参考层进入后续适配，但必须先补齐 `retrieval_manifest + source_readback + cleaning_adapter + write_executor_handoff + completion_truth_check` 契约；现有 6 类视频工厂 workflow 不应被上游框架冲掉，`adapter_infrastructure_flow` 只能先登记为候选，等待用户 / ChatGPT 确认后再决定是否写入正式 workflow 索引。
