# 20260617 Engineering Line Gap Matrix

## executive_summary（执行摘要）

本矩阵把主线、adapter、RAG、Tool、Evaluator、Failure Route、Human-in-the-loop、Guardrails、Checkpoint、Report、Trace、Log 的融合状态拆成可修复缺口。结论：`main` 已有 adapter 候选代码和静态契约，但真实工程线仍处于 `candidate / probe_only / documented_only` 混合状态，最大缺口是“状态地图与验收契约没有统一入口”，其次是 RAG / Tool / Retriever 没有接入 adapter workflow。

## current_engineering_line_map（当前工程线地图）

| Line | Current status | Evidence | Boundary |
|---|---|---|---|
| 主项目路由 | `implemented` | `AGENTS.md`, `codex_source/19_project_state_action_router.md`, `codex_source/22_工作流入口归位索引...md` | 不等于 adapter runtime |
| Adapter workflow | `implemented / candidate` | `codex_source/adapter_integration/workflow_registry.py` | 候选映射，不替代正式 workflow |
| Schema / fixture / probe | `implemented / probe_only` | `codex_source/schema_contracts/00_schema_contracts_index.md` | 不等于 service 可用 |
| RAG | `partial / documented_only` | `20260613_vector_rag_merge_readiness_report.md`, `docs/RAG_EXECUTION_ARCHITECTURE.md` | 最小 smoke 不等于默认 runtime |
| Tool Registry | `missing` | 未找到本仓库 adapter tool registry | 不能靠 prompt 临场选工具 |
| Evaluator / failure | `partial` | `completion_truth.py`, blocked fixtures | 缺统一 evaluator registry |
| Human-in-the-loop | `documented_only` | `human_review_interrupt.schema.yaml` | 无真实 interrupt/resume |
| Checkpoint / trace | `schema_only / partial` | `cross_contract_trace.schema.yaml`, fake graph trace | 无 durable replay |
| Reports / latest | `implemented` | `codex_log/framework_adapter/*.md`, `codex_log/latest.md` | 缺统一报告字段校验 |

## target_engineering_line_map（目标工程线地图）

目标形态：

```text
goal_card
-> milestone_acceptance_contract
-> workflow_route_decision
-> state_schema
-> node_edge_contract
-> retrieval_manifest
-> source_readback
-> tool_registry
-> evaluator_result
-> failure_route
-> human_interrupt
-> checkpoint
-> report
-> trace
-> latest_log
```

## module_status_matrix（模块状态矩阵）

| module_name | current_status | evidence_files | what_exists_now | what_is_missing | risk_if_ignored | repair_priority | recommended_next_action | blocked_if |
|---|---|---|---|---|---|---|---|---|
| Formal workflow index | `implemented` | `codex_source/22_工作流入口归位索引...md` | 6 类 workflow 和 required handoff | 与 adapter candidate 的状态对齐表 | 新旧 workflow 混淆 | P0 | 建状态地图 | 试图替换正式 workflow |
| Adapter candidate registry | `implemented / candidate` | `workflow_registry.py` | 6 个 adapter workflow | candidate / formal 状态字段 | 候选被误读为 production | P0 | 加 acceptance contract | 缺 stopline |
| Runtime entry | `probe_only` | `runtime_entry.py` | sample route and validation | durable runtime lifecycle | probe 被当 runtime | P1 | no-service lifecycle contract | 需要启动服务 |
| Service boundary | `probe_only` | `service_boundary.py` | no-write action blocking | HTTP / network no-write proof | in-process 被当部署 | P6 | later isolated probe | 要开端口 |
| LangGraph graph | `probe_only` | `no_service_graph_probe.py` | fake graph nodes | real StateGraph | fake graph 冒充真实图 | P1 | real no-service graph probe | 依赖缺失 |
| RAG retriever | `missing in adapter` | RAG reports | smoke readback | retriever interface | RAG 无法接 workflow | P2 | fixture retriever adapter | 真实 API 必需 |
| Tool registry | `missing` | upstream audit only | 工具定位 | 本仓库 registry | 工具权限无边界 | P2 | schema only registry | 要调用工具 |
| Evaluator | `partial` | `completion_truth.py` | false completion guards | evaluator registry | 只能局部阻断 | P3 | evaluator matrix | 无 evidence |
| Failure route | `partial` | blocked fixtures | many blocked_if | owner / next_action route | blocked 无修复路径 | P3 | failure route table | blocked reason 泛化 |
| Human review | `documented_only` | `human_review_interrupt.schema.yaml` | schema | interrupt/resume artifact | 人审被跳过 | P3 | handoff fixture | 无人工决策 |
| Guardrails | `partial` | no-write, completion fixtures | 多个 guard | single guardrail runner | 扫描遗漏 | P3 | guardrail runner | 状态误推进 |
| Checkpoint | `missing` | runtime memory boundary | 禁止 memory 替代事实 | checkpoint contract | 无恢复能力 | P4 | checkpoint schema | 需 DB 服务 |
| Trace | `schema_only` | cross_contract_trace | trace fields | event log | 节点不可还原 | P4 | JSONL trace | 外部 telemetry |
| Report | `implemented / partial` | dated reports | 报告很多 | report required field check | 报告风格漂移 | P4 | report validator | 缺 status boundary |
| Status/schema conflict cleanup | `conflict` | handoff/report/schema/source policy readback | branch-local 状态、service action 集合、completion truth 字段名、DeepSeek 供料口径仍有残留冲突 | 冲突归一表和验收断言 | 旧口径继续污染后续判断 | P0 | 纳入状态地图 | 直接修改 runtime |
| Log sync | `implemented` | latest, AGENTS | commit/push/readback rule | automated final checker | 本地完成冒充完成 | P4 | completion checker | remote fail |

## integration_gap_matrix（融合缺口矩阵）

| gap_id | Edge | Status | Evidence | Missing connector | Repair priority | Blocked if |
|---|---|---|---|---|---|---|
| G01 | formal workflow -> adapter workflow | `partial` | `22...md`, `workflow_registry.py` | formal/candidate state map | P0 | adapter workflow 被启用为正式入口 |
| G02 | adapter workflow -> State | `missing` | TaskPacket has fields but no global State | State schema | P1 | 状态只存在于 packet 局部 |
| G03 | State -> Node / Edge | `probe_only` | `no_service_graph_probe.py` | real node/edge definitions | P1 | 需安装或服务 |
| G04 | adapter -> RAG | `missing` | RAG docs/smoke separate | Retriever interface | P2 | 需要真实 DashVector |
| G05 | RAG -> source_readback | `partial` | readback report exists | automatic source_readback adapter | P2 | page_content-only |
| G06 | RAG -> Tool Registry | `missing` | upstream tool audit only | tool registry schema | P2 | 工具会写仓库或外呼 |
| G07 | Evaluator -> Failure Route | `partial` | blocked fixtures | failure route aggregator | P3 | blocked 无 owner |
| G08 | Failure Route -> Human | `documented_only` | human schema | interrupt handoff artifact | P3 | 人审缺失 |
| G09 | Guardrails -> Report | `partial` | scans in reports | guardrail summary schema | P3 | forbidden status scan 缺失 |
| G10 | Checkpoint -> Trace | `missing` | runtime memory boundary | checkpoint id + replay trace | P4 | memory 替代事实 |
| G11 | Trace -> latest | `partial` | fake trace, latest logs | trace-to-report fields | P4 | report 无 trace |
| G12 | Report -> Git sync | `implemented / manual` | AGENTS mandatory gate | automated staged-diff checker | P4 | unrelated dirty 混入 |
| G13 | Runtime -> Service | `probe_only` | in-process service boundary | isolated service no-write probe | P6 | 开端口或外部 API 未授权 |
| G14 | main merge truth -> branch-local handoff | `conflict` | main merge completed, handoff still branch-local | status normalization assertion | P0 | 直接把 branch-local 当 current main truth |
| G15 | service schema -> service boundary code | `conflict` | schema includes retrieve/interrupt, code allows route/validate/block/handoff | action vocabulary reconciliation | P0 | 为了对齐而放宽 no-write boundary |
| G16 | completion truth schema -> required field names | `conflict` | send_ready vs ready_status naming mismatch | field-name compatibility rule | P0 | 状态晋级扫描漏检 |
| G17 | RAG-first source arbitration -> old DeepSeek mandatory wording | `conflict` | current AGENTS uses conditional DeepSeek, older files contain mandatory wording | source arbitration precedence note | P0 | DeepSeek 被误当默认供料层 |

## future_repair_roadmap（未来修复路线图）

1. Milestone 1：先补工程线状态地图与入口统一，解决 G01。
2. Milestone 2：再补 State / Node / Edge，解决 G02-G03。
3. Milestone 3：再补 RAG / Tool Registry / Retriever 抽象，解决 G04-G06。
4. Milestone 4：再补 Evaluator / Failure Route / Guardrails / Human handoff，解决 G07-G09。
5. Milestone 5：再补 Checkpoint / Trace / Report / Log，解决 G10-G12。
6. Milestone 6：最后进入隔离 runtime hardening，解决 G13。

## next_codex_task_slices（下一轮 Codex 任务切片）

建议下一轮先执行 `Task Slice 1: engineering_state_map_and_acceptance_contract`。如果直接做 RAG 或 runtime，状态地图缺失会继续导致 probe-only 被误读成 completed。

## status_boundary（状态边界）

本矩阵不推进 `runtime_enabled`、`service_started`、`external_api_called`、`tts_called`、`dashvector_real_call`、`chroma_ingestion_run`、`media_generated`、`production_readiness`、`content_validation` 或 `send_ready`。
