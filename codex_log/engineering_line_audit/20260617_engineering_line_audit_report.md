# 20260617 Engineering Line Audit Report

## route_decision（路由判断）

```yaml
project_route: video_factory
task_type:
  - engineering_line_audit
  - integration_gap_report
  - future_repair_roadmap
responsibility_layer:
  - project_judgment_layer
  - validation_layer
  - mechanism_fix_layer
  - sync_layer
large_task_gate:
  triggered: true
  lane_recommendation: audit_lane
  parallel_recommendation: read_parallel_then_serial_write
supply_source_arbitration:
  retrieval_manifest: repo_source_readback_only
  source_readback_status: read_ok
  deepseek_trigger_decision: false
  not_deepseek_conclusion: true
execution_permission: audit_report_write_only
```

本轮只做全工程线审计和后续修复路线图。未安装依赖，未启动服务，未打开端口，未调用外部 API，未调用 TTS，未调用 DashVector，未运行 Chroma 入库，未读取真实媒体，未生成视频 / 音频 / 字幕 / 卡片。

## executive_summary（执行摘要）

1. `已确认` adapter branch candidate 已合并进 `main`，合并范围包括 `codex_source/adapter_integration/`、`codex_source/schema_contracts/`、`codex_log/framework_adapter/` 和 `codex_log/latest.md`，证据见 `codex_log/framework_adapter/20260617_main_merge_completed_report.md`。
2. `已确认` 当前 adapter 线只证明了 workflow registry、TaskPacket、task cleaner、workflow router、contract validator、no-render runner、runtime entry 和 in-process service boundary 的候选链路。
3. `已确认` `service_boundary` 只允许 `route / validate / block / handoff`，并阻断 `write_repo / commit / push / modify_main / call_external_api / generate_media / claim_completion`。
4. `部分成立` RAG 线曾完成最小 DashVector smoke、最小 261 chunks 入库和 5 个查询 readback；但 `docs/RAG_EXECUTION_ARCHITECTURE.md` 与 `docs/VECTOR_RETRIEVAL_PLAN.md` 仍标为 `proposal_only`，adapter workflow 也未直接调用真实 Retriever。
5. `部分成立` LangGraph / LangChain 定位已经审计清楚：LangGraph 只应进入 workflow runtime layer，LangChain 只应进入 model / tool / retriever / loader adapter layer；当前 `main` 仍没有真实 LangGraph StateGraph 执行图。
6. `已确认` evaluator / failure route / guardrails 主要落在 schema、fixture、probe 和 completion truth guard 中，已能阻断多类 false completion；但它们仍是静态或 no-render 级别，不是生产运行时 evaluator。
7. `部分成立` checkpoint / trace / log 有 schema 字段、fake graph trace 和 dated report / latest 机制；但没有真实 runtime checkpoint store、node-level durable replay、统一 observability event model。
8. `缺失` Tool Registry、Vector Store abstraction、Retriever interface、RAG adapter、DashVector adapter、Chroma sandbox adapter 到 adapter workflow 的正式代码接线。
9. `缺失` Human-in-the-loop 目前以 schema / fixture / interrupt pattern 存在，尚未成为 runtime 中断恢复机制，也未接到具体服务或 UI。
10. `状态边界` 本轮报告只是后续修复和融合地图，不代表 runtime 已启用、RAG 已跑通、生产可用、内容验证通过或可以生成真实视频。
11. `冲突` 当前仍有少量口径待归一：`current_adapter_integration_handoff.md` 和部分 runtime probe 报告残留 branch-local / not_started 旧状态；`service_contract_no_write.schema.yaml` 与 `service_boundary.py` 允许动作集合不完全一致；`completion_truth_check_node.schema.yaml` 里 send_ready / ready_status 字段名不一致；旧 DeepSeek mandatory 文字与当前 RAG-first + conditional DeepSeek 规则冲突。

## current_engineering_line_map（当前工程线地图）

```text
用户任务
  -> AGENTS route_decision                         [implemented]
  -> workflow_route_decision 六类正式 workflow       [implemented]
  -> Project State Action Router                  [implemented]
  -> adapter workflow registry 六个候选 workflow    [implemented, candidate]
  -> TaskPacket / task_cleaner / workflow_router   [implemented, no-render]
  -> schema_contracts / fixtures / probes          [implemented, probe_only]
  -> no_render_adapter_runner                      [probe_only]
  -> runtime_entry                                 [probe_only]
  -> in-process service_boundary                   [probe_only]
  -> real LangGraph StateGraph                     [missing in main]
  -> real RAG Retriever / Tool Registry            [missing in adapter]
  -> real DashVector / Chroma runtime call         [missing this line]
  -> evaluator / completion_truth                  [implemented as guard, not runtime evaluator]
  -> report + latest log                           [implemented]
  -> checkpoint / trace / observability            [documented_or_schema_only]
  -> production runtime / media generation          [missing, forbidden this round]
```

| Segment | Status | Evidence |
|---|---|---|
| Main merge of adapter candidate | `implemented` | `codex_log/framework_adapter/20260617_main_merge_completed_report.md` |
| Six formal project workflows | `implemented` | `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` |
| Six adapter candidate workflows | `implemented / candidate` | `codex_source/adapter_integration/workflow_registry.py` |
| No-render editing validation | `probe_only` | `codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py` |
| No-service fake graph | `probe_only` | `codex_source/schema_contracts/probes/no_service_graph_probe.py` |
| Runtime entry | `probe_only` | `codex_source/adapter_integration/runtime_entry.py` |
| Service boundary | `probe_only` | `codex_source/adapter_integration/service_boundary.py` |
| Real service deployment | `missing` | Merge report lists `real_service_deployment: not_started` |
| Real runtime deployment | `missing` | Merge report lists `real_runtime_deployment: not_started` |
| RAG default execution runtime | `documented_only / partial` | `docs/RAG_EXECUTION_ARCHITECTURE.md`, `20260613_vector_rag_merge_readiness_report.md` |
| Tool Registry | `missing` | No adapter `tool_registry` implementation found |
| Observability event stream | `missing` | Trace schema exists, but no runtime event emitter found |

## target_engineering_line_map（目标工程线地图）

```text
Goal / Milestone / Acceptance
  -> workflow_route_decision
  -> State object
  -> LangGraph node graph
  -> RAG retrieval_manifest
  -> source_readback
  -> Tool Registry / Retriever / Vector Store adapter
  -> Evaluator nodes
  -> Failure Route / blocked_if aggregator
  -> Human Review interrupt
  -> Guardrails
  -> Checkpoint
  -> active_write_executor handoff
  -> Codex write / no-write execution
  -> Report
  -> Trace / Observability events
  -> latest + dated log
  -> Git commit / push / remote readback
```

目标线必须保留三条硬边界：

1. LangGraph 是 workflow runtime layer，不替代 `Project State Action Router`。
2. RAG / Vector Store 是 retrieval index / cache layer，不替代仓库原文件事实。
3. runtime / service / memory 只能输出 handoff，不直接写 repo；实际写入仍由 `active_write_executor = codex` 完成。

## module_status_matrix（模块状态矩阵）

| module_name（模块名） | current_status（当前状态） | evidence_files（证据文件） | what_exists_now（现在已有） | what_is_missing（缺什么） | risk_if_ignored（不修风险） | repair_priority（优先级） | recommended_next_action（建议下一步） | blocked_if（阻断条件） |
|---|---|---|---|---|---|---|---|---|
| Goal / Milestone / Acceptance | `documented_only / partial` | `20260616_agent_service_toolkit_full_integration_master_plan.md`, `20260617_main_merge_completed_report.md` | 分阶段报告、stopline、blocked_if | 机器可校验 milestone schema、acceptance runner、per-module done_when | 继续靠 prompt 判断完成 | P0 | 建 `engineering_state_map` 与 `acceptance_contract` | 缺 evidence path 或验收脚本 |
| Workflow Registry | `implemented / candidate` | `workflow_registry.py`, `codex_source/22...md` | 6 个 adapter workflow 映射到 6 类正式 workflow | 正式 workflow registry schema、candidate 与 formal 的状态隔离 | candidate 被误当正式入口 | P0 | 先统一入口状态地图 | 需要替换正式 workflow |
| LangGraph / State / Node / Edge | `probe_only` | `no_service_graph_probe.py`, `graph_runtime_adapter.schema.yaml` | fake graph nodes、trace、blocked fixtures | 真实 LangGraph StateGraph、State schema、node failure policy、edge branch contract | graph 被写成 runtime ready | P1 | 做 no-service real LangGraph probe | 需安装依赖或启动服务 |
| RAG / LangChain | `partial / documented_only` | `20260613_vector_rag_merge_readiness_report.md`, `docs/RAG_EXECUTION_ARCHITECTURE.md` | 最小 DashVector smoke、RAG proposal、metadata requirement | adapter 中 Retriever interface、Tool Registry、Vector Store abstraction | 向量结果被当事实或根本接不上 workflow | P2 | 建 RAG adapter contract 和 fixture | 需要真实外部 API |
| Tool Registry | `missing` | `20260614_langgraph_rag_cleaning_integration_probe.md` only upstream audit | 上游工具层定位审计 | 本仓库内工具注册表、权限、输入输出、禁用项 | 工具调用散落在 prompt | P2 | 先做 read-only tool registry schema | 需要真实工具执行 |
| Vector Store / Retriever | `partial / missing in adapter` | `VECTOR_RETRIEVAL_PLAN.md`, `retrieval_manifest.schema.yaml` | DashVector smoke、Chroma sandbox fixture | 统一 `Retriever -> RetrievalManifest -> SourceReadback` adapter | Chroma / DashVector 混层 | P2 | 只做 fixture-to-manifest adapter | 需要真实入库 |
| Evaluator | `probe_only` | `contract_validator.py`, `completion_truth.py`, schema probes | 静态 contract validator 和 false completion guards | 通用 evaluator registry、per-workflow evaluator outputs | 只能校验 editing 子集 | P3 | 建 evaluator/failure route matrix | 需要媒体质量真实判断 |
| Failure Route | `implemented / partial` | blocked fixtures, `completion_truth_check_node.schema.yaml` | blocked fixtures、blocked_if 字段 | 统一 failure route aggregator 和 next owner | blocked 分散，后续修复无路由 | P3 | 补 `failure_route_contract` | blocked reason 无 evidence |
| Human-in-the-loop | `documented_only / fixture` | `human_review_interrupt.schema.yaml`, `22...md` | schema 和人工复审边界 | runtime interrupt、resume、human decision artifact | 人审点被省略或自动通过 | P3 | 建 human review handoff fixture | 无人审却推进状态 |
| Guardrails | `implemented / partial` | `service_contract_no_write.schema.yaml`, blocked fixtures | 状态推进、no-write、fallback、RAG fact guard | guardrail registry 和扫描入口统一化 | 禁止状态扫描靠临时 rg | P3 | 汇总 guardrails 到 acceptance runner | 误写 status |
| Checkpoint | `documented_only` | `runtime_memory_boundary.schema.yaml`, upstream audit | runtime memory boundary | durable checkpoint store 和 replay policy | runtime 失败无法恢复且 memory 替代事实 | P4 | 先定义 checkpoint contract | 需要 Postgres/Mongo |
| Report | `implemented` | `codex_log/framework_adapter/*.md`, `codex_log/latest.md` | dated report + latest summary | report schema、required fields checker | 报告字段不一致 | P4 | 建 report validation script | 报告缺 status boundary |
| Observability / Trace | `schema_only / partial` | `cross_contract_trace.schema.yaml`, `no_service_graph_probe.py` | trace_fields、fake graph trace | runtime event stream、node duration、input/output hash、error class | 不能还原节点行为 | P4 | 先做 local JSONL trace contract | 需要外部 telemetry |
| Status / Schema Conflict Cleanup | `conflict` | `current_adapter_integration_handoff.md`, `runtime_service_probe_report.md`, `service_contract_no_write.schema.yaml`, `service_boundary.py`, `completion_truth_check_node.schema.yaml`, `GPT数据源/01...md`, `GPT数据源/03...md` | 冲突点已定位 | 统一 formal/candidate/probe 状态、schema/action 集合、字段名和 DeepSeek 触发口径 | 后续任务继续混用旧状态或旧供料规则 | P0 | 纳入 Milestone 1 状态地图与验收契约 | 直接改 runtime 或服务 |
| Log / Git Sync | `implemented` | `AGENTS.md`, latest, merge reports | latest、dated logs、commit/push/readback 规则 | 自动检查本轮 report paths / status scan | local-only 被写完成 | P4 | 加完成前验证 checklist | remote readback 失败 |
| Runtime / Service Hardening | `missing / next phase only` | `runtime_service_probe.py`, merge report | in-process probe | isolated runtime hardening、service contract probe、no-write service validation | 提前上线导致写仓库 / secret / API 风险 | P5 | 前 5 个 milestone 通过后再做 | 需要依赖安装 / 端口 / 外部 API |

## integration_gap_matrix（融合缺口矩阵）

| integration_edge（融合边） | current_status | evidence | gap | repair_owner_line |
|---|---|---|---|---|
| 主线判断层 -> adapter workflow | `partial` | `workflow_registry.py` 映射 6 类 workflow；`22` 正式只允许 6 类 | candidate registry 未写成正式入口状态地图 | Milestone 1 |
| adapter workflow -> LangGraph State/Node/Edge | `probe_only` | `no_service_graph_probe.py` fake graph | 没有真实 StateGraph / node failure / edge branch | Milestone 2 |
| adapter workflow -> RAG / Tool / Retriever | `missing` | `runtime_entry.py` 未调用 retriever；RAG 仅 proposal/smoke | 没有 Tool Registry、Retriever interface、Vector Store adapter | Milestone 3 |
| RAG -> source_readback | `partial` | retrieval readback report passed 5 queries | adapter 未把每次 retrieval 转成 source_readback map | Milestone 3 |
| Evaluator -> Failure Route | `partial` | `completion_truth.py`, blocked fixtures | 没有跨 workflow failure route aggregator | Milestone 4 |
| Failure Route -> Human-in-the-loop | `documented_only` | `human_review_interrupt.schema.yaml` | 没有 interrupt/resume artifact | Milestone 4 |
| Guardrails -> code/probe | `partial` | no-write service boundary、completion truth fixtures | guardrail 扫描分散，非统一 runner | Milestone 4 |
| Checkpoint -> Report | `missing` | runtime memory boundary only | 没有 checkpoint id / replay / resume report | Milestone 5 |
| Trace -> Log / latest | `partial` | fake graph trace、latest | trace 未形成 dated JSONL / report field | Milestone 5 |
| Runtime -> active_write_executor | `documented_only / probe_only` | service boundary blocks write | 缺正式 write_executor_handoff runtime contract test | Milestone 6 |

## future_repair_roadmap（未来修复路线图）

| milestone | goal | allowed_files | validation | blocked_if |
|---|---|---|---|---|
| Milestone 1 | 工程线状态地图与入口统一 | `codex_log/engineering_line_audit/*`, optional `codex_source/22...md` after separate auth | 状态地图能区分 formal / candidate / probe / missing | 要改 runtime 或真实服务 |
| Milestone 2 | workflow / State / Node / Edge 接线 | schema contracts, adapter no-service probe | 真 LangGraph no-service probe 或 fallback fake graph 明确标边界 | 需要安装依赖 / 服务 |
| Milestone 3 | RAG / Tool Registry / Retriever 抽象接线 | schema + adapter contracts + fixtures | fixture-to-manifest adapter 通过，source_readback 必须通过 | 需要真实 DashVector / Chroma |
| Milestone 4 | Evaluator / Failure Route / Guardrails 接线 | evaluator/failure route schema + probes | false completion、status promotion、no-write、human interrupt fixtures 全过 | 人审缺失却自动通过 |
| Milestone 5 | Checkpoint / Observability / Trace / Report / Log 接线 | trace schema, report validator, latest checker | 每个节点有 trace_id、source_path、status、blocked_if、report_path | 需要外部 telemetry |
| Milestone 6 | 隔离 runtime hardening | adapter runtime package only | no-write service probe、no external API by default、manual auth gates | 依赖安装、端口、secret、外部 API 未授权 |

## next_codex_task_slices（下一轮 Codex 任务切片）

详见 `codex_log/engineering_line_audit/20260617_next_codex_task_slices.md`。本报告建议下一轮只选一个切片执行，默认从 `Task Slice 1: engineering_state_map_and_acceptance_contract` 开始，不要直接跳到 runtime hardening。

## status_boundary（状态边界）

- 本轮审计不代表 `runtime_enabled = true`。
- 本轮审计不代表 service 已启动。
- 本轮审计不代表 RAG 已成为每轮默认运行时。
- 本轮审计不代表 DashVector / Chroma 已真实接入 adapter workflow。
- 本轮审计不代表 TTS、媒体生成、字幕、卡片或真实剪辑链路可用。
- 本轮审计不代表生产可用或可上线状态。
- 本轮审计不代表 content_validation 通过。
- 本轮审计不代表 send_ready。
- 本轮报告只是未来修复和融合的工程地图。
