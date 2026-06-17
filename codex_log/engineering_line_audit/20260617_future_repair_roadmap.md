# 20260617 Future Repair Roadmap

## executive_summary（执行摘要）

本路线图只定义后续缺口修复顺序，不启用 runtime。修复原则是：先统一状态地图和验收口径，再接 workflow graph，再接 RAG / Tool / Retriever，再接 evaluator / failure / human / guardrails，最后才做 checkpoint / observability 和隔离 runtime hardening。任何阶段只要需要安装依赖、启动服务、调用外部 API、写真实媒体、真实 DashVector / Chroma / TTS，就必须停止并另开授权任务。

## current_engineering_line_map（当前工程线地图）

当前是：

```text
formal_project_router [implemented]
-> adapter_candidate_registry [implemented/candidate]
-> schema_fixture_probe [probe_only]
-> runtime_entry_in_process [probe_only]
-> service_boundary_in_process [probe_only]
-> real_runtime [missing]
-> real_rag_tool_retriever [missing]
-> production_media_line [missing/not_allowed]
```

## target_engineering_line_map（目标工程线地图）

目标是：

```text
Goal/Milestone/Acceptance
-> WorkflowRouteDecision
-> State
-> Node
-> Edge
-> RAG / Tool Registry / Retriever
-> Evaluator
-> Failure Route
-> Human-in-the-loop
-> Guardrails
-> Checkpoint
-> Report
-> Observability
-> Trace
-> Log
```

## module_status_matrix（模块状态矩阵）

| module_name | current_status | repair_lane | acceptance |
|---|---|---|---|
| Goal / Milestone / Acceptance | `documented_only / partial` | Milestone 1 | 每个阶段有 `done_when` 和 `blocked_if` |
| Workflow / State | `candidate / missing state` | Milestone 2 | State schema 可验证 |
| Node / Edge | `probe_only` | Milestone 2 | no-service node/edge probe 通过 |
| RAG / Tool / Retriever | `partial / missing adapter` | Milestone 3 | retrieval manifest + source readback fixture 通过 |
| Evaluator / Failure | `partial` | Milestone 4 | false completion 和 failure route 均有 owner |
| Human / Guardrails | `documented_only / partial` | Milestone 4 | 人审 interrupt artifact 和 guardrail runner 存在 |
| Checkpoint / Trace / Report / Log | `schema_only / partial` | Milestone 5 | trace JSONL + report validator + latest check |
| Runtime hardening | `missing` | Milestone 6 | isolated no-write service probe 通过 |

## integration_gap_matrix（融合缺口矩阵）

| Milestone | Gap covered | Output | Do not do |
|---|---|---|---|
| M1 | formal/candidate/probe/missing 混层 | `engineering_state_map` + `acceptance_contract` | 不改 runtime |
| M2 | workflow 没有真实 State / Node / Edge | `state_node_edge_contract` + no-service probe | 不启动 service |
| M3 | RAG / Tool / Retriever 没接 adapter | `tool_registry_contract` + `retriever_manifest_adapter` | 不调用真实 API |
| M4 | failure / human / guardrails 分散 | `failure_route_matrix` + `human_interrupt_handoff` | 不自动人审通过 |
| M5 | checkpoint / trace / report 不统一 | `trace_event_schema` + report validator | 不接外部 telemetry |
| M6 | runtime 未隔离加固 | isolated runtime hardening plan/probe | 不开公网、不写 repo |

## future_repair_roadmap（未来修复路线图）

### Milestone 1：工程线状态地图与入口统一

```yaml
goal: 让后续 Codex 一眼区分 formal / candidate / probe_only / documented_only / missing / conflict
allowed_files:
  - codex_log/engineering_line_audit/*
  - codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md（如另行授权）
  - codex_source/schema_contracts/schemas/engineering_state_map.schema.yaml（如另行授权）
validation:
  - 状态枚举完整
  - 每个状态有 evidence_files
  - 每个状态有 blocked_if
  - branch-local handoff 与 main merge truth 的冲突被单列
  - service action vocabulary 与 completion truth 字段名冲突被单列
  - RAG-first / conditional DeepSeek 供料优先级被单列
blocked_if:
  - 需要改 runtime
  - 需要启用服务
  - 无法裁决 candidate 与 formal 的边界
  - 为了归一冲突而放宽 no-write / no-external-api 边界
```

### Milestone 2：workflow / State / Node / Edge 接线

```yaml
goal: 把 adapter workflow registry 映射成可验证 State / Node / Edge，但仍停在 no-service
allowed_files:
  - codex_source/schema_contracts/schemas/*
  - codex_source/schema_contracts/fixtures/*
  - codex_source/schema_contracts/probes/*
  - codex_source/adapter_integration/*
validation:
  - State schema parse pass
  - no-service graph probe pass
  - node failure route pass
blocked_if:
  - 需要安装 langgraph
  - 需要启动 FastAPI
  - graph 尝试写 repo
```

### Milestone 3：RAG / Tool Registry / Retriever 抽象接线

```yaml
goal: 先用 fixture 接通 Tool Registry、Retriever、Vector Store 和 RetrievalManifest，不跑真实外部服务
allowed_files:
  - codex_source/schema_contracts/schemas/tool_registry.schema.yaml
  - codex_source/schema_contracts/schemas/retriever_adapter.schema.yaml
  - codex_source/schema_contracts/fixtures/*
  - codex_source/adapter_integration/*
validation:
  - Chroma sandbox fixture 不替代 DashVector
  - DashVector fixture 输出 retrieval_manifest
  - source_readback_required=true
blocked_if:
  - 需要真实 DashVector 调用
  - 需要 Chroma 入库
  - 工具可能写仓库或外呼
```

### Milestone 4：Evaluator / Failure Route / Guardrails 接线

```yaml
goal: 把分散 blocked_if、completion_truth、service no-write、人审边界统一为可执行 failure route
allowed_files:
  - codex_source/schema_contracts/schemas/failure_route.schema.yaml
  - codex_source/schema_contracts/schemas/evaluator_result.schema.yaml
  - codex_source/schema_contracts/probes/*
validation:
  - false completion blocked
  - technical_as_content blocked
  - rag_as_fact blocked
  - human_review_required cannot auto-pass
blocked_if:
  - 缺 failure owner
  - 缺 human review artifact
  - guardrail 只写文档未进入 fixture/probe
```

### Milestone 5：Checkpoint / Observability / Trace / Report / Log 接线

```yaml
goal: 每个节点可追踪、可报告、可写回 latest，但不接外部 telemetry
allowed_files:
  - codex_source/schema_contracts/schemas/cross_contract_trace.schema.yaml
  - codex_source/schema_contracts/schemas/report_contract.schema.yaml
  - codex_source/schema_contracts/probes/report_contract_probe.py
validation:
  - 每个节点有 trace_id / source_path / status / blocked_if / report_path
  - report required section check pass
  - forbidden status promotion scan pass
blocked_if:
  - 需要 LangSmith / Langfuse key
  - checkpoint store 替代 repo facts
```

### Milestone 6：隔离 runtime hardening（隔离运行时加固）

```yaml
goal: 在前 5 个 milestone 通过后，才允许隔离 no-write runtime hardening
allowed_files:
  - codex_source/adapter_integration/*
  - codex_log/framework_adapter/*
validation:
  - no-write service probe pass
  - no external API by default
  - no repo write from runtime
  - active_write_executor handoff required
blocked_if:
  - 需要安装依赖但未授权
  - 需要持久端口或公网
  - 需要 secret / API / TTS / DashVector / Chroma / media
```

## next_codex_task_slices（下一轮 Codex 任务切片）

下一轮优先顺序：

1. `engineering_state_map_and_acceptance_contract`
2. `state_node_edge_no_service_contract`
3. `rag_tool_retriever_fixture_adapter`
4. `evaluator_failure_guardrail_matrix`
5. `trace_report_log_validator`
6. `isolated_runtime_hardening_probe`

## status_boundary（状态边界）

本路线图不代表任何 milestone 已完成。它只规定后续修复顺序、允许文件范围、验证方式和阻断条件。未经后续单独授权，不得把 Milestone 6 提前执行。
