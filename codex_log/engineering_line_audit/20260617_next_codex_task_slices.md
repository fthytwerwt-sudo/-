# 20260617 Next Codex Task Slices

## executive_summary（执行摘要）

本清单把后续修缺口拆成可下发给 Codex 的最小任务片。每个任务片只能处理一个工程线层级，默认不启动服务、不安装依赖、不调用外部 API、不生成媒体、不推进内容或生产状态。

## current_engineering_line_map（当前工程线地图）

当前可下发的安全起点是报告 / schema / fixture / probe 层。`main` 有 adapter candidate 和 probes，但 runtime、RAG default execution、Tool Registry、checkpoint、observability 都未闭环。

## target_engineering_line_map（目标工程线地图）

目标是让每个任务片都能明确接到：

```text
goal -> allowed_files -> must_read -> execution_steps -> validation -> done_when -> blocked_if
```

## module_status_matrix（模块状态矩阵）

| module | task_slice | priority |
|---|---|---|
| engineering state map | Task Slice 1 | P0 |
| State / Node / Edge | Task Slice 2 | P1 |
| RAG / Tool / Retriever | Task Slice 3 | P2 |
| Evaluator / Failure / Guardrails | Task Slice 4 | P3 |
| Checkpoint / Trace / Report | Task Slice 5 | P4 |
| Runtime hardening | Task Slice 6 | P5 |

## integration_gap_matrix（融合缺口矩阵）

| slice | gap | status before slice | expected status after slice |
|---|---|---|---|
| 1 | formal/candidate/probe/missing 混层 | conflict risk | mapped |
| 2 | no real State / Node / Edge | missing/probe_only | contract + probe |
| 3 | RAG / Tool / Retriever 未接线 | missing | fixture adapter ready |
| 4 | failure / human / guardrail 分散 | partial | routed |
| 5 | checkpoint / trace / report 不统一 | schema_only | local validation |
| 6 | runtime 未隔离加固 | missing | isolated no-write probe |

## future_repair_roadmap（未来修复路线图）

执行顺序固定为 Task Slice 1 -> 2 -> 3 -> 4 -> 5 -> 6。不得跳过 Task Slice 1 直接做 runtime。

## next_codex_task_slices（下一轮 Codex 任务切片）

### Task Slice 1：engineering_state_map_and_acceptance_contract

```yaml
task_name: engineering_state_map_and_acceptance_contract
goal: 建立 formal / candidate / probe_only / documented_only / missing / conflict 的工程状态地图和验收契约
allowed_files:
  - codex_log/engineering_line_audit/*
  - codex_source/schema_contracts/schemas/engineering_state_map.schema.yaml（如本轮授权）
  - codex_source/schema_contracts/fixtures/passing/engineering_state_map.passing.yaml（如本轮授权）
forbidden_files:
  - codex_source/adapter_integration/runtime_entry.py
  - codex_source/adapter_integration/service_boundary.py
  - .env*
  - dist/**
must_read:
  - AGENTS.md
  - codex_log/latest.md
  - codex_log/engineering_line_audit/20260617_engineering_line_audit_report.md
  - codex_log/framework_adapter/current_adapter_integration_handoff.md
  - codex_log/framework_adapter/20260617_main_merge_completed_report.md
  - codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md
  - codex_source/adapter_integration/workflow_registry.py
  - codex_source/adapter_integration/service_boundary.py
  - codex_source/schema_contracts/schemas/service_contract_no_write.schema.yaml
  - codex_source/schema_contracts/schemas/completion_truth_check_node.schema.yaml
execution_steps:
  - 列出所有工程模块
  - 给每个模块标状态与证据路径
  - 给每个状态写 done_when 和 blocked_if
  - 单列 branch-local / main merge、schema/code action vocabulary、completion truth 字段名、DeepSeek 供料口径冲突
validation:
  - grep 检查状态枚举
  - schema / fixture parse 如有新增
  - forbidden status scan
done_when:
  - 后续 Codex 可根据状态地图判断能否进入下一层
blocked_if:
  - 无法区分 candidate 和 formal
  - 需要启用 runtime
```

### Task Slice 2：state_node_edge_no_service_contract

```yaml
task_name: state_node_edge_no_service_contract
goal: 把 adapter workflow registry 映射为 State / Node / Edge 契约，仍保持 no-service
allowed_files:
  - codex_source/schema_contracts/schemas/*
  - codex_source/schema_contracts/fixtures/*
  - codex_source/schema_contracts/probes/*
forbidden_files:
  - pyproject.toml
  - package.json
  - compose.yaml
  - .env*
must_read:
  - codex_source/schema_contracts/00_schema_contracts_index.md
  - codex_source/schema_contracts/probes/no_service_graph_probe.py
  - codex_source/adapter_integration/workflow_registry.py
execution_steps:
  - 定义 State schema
  - 定义 Node / Edge contract
  - 增加 passing / blocked fixtures
  - 更新 no-service probe
validation:
  - python3 codex_source/schema_contracts/probes/no_service_graph_probe.py
  - git diff --check
done_when:
  - State / Node / Edge 可被本地 no-service probe 验证
blocked_if:
  - 需要安装 langgraph
  - 需要启动 FastAPI
```

### Task Slice 3：rag_tool_retriever_fixture_adapter

```yaml
task_name: rag_tool_retriever_fixture_adapter
goal: 建立 Tool Registry / Retriever / Vector Store 的 fixture-first adapter，不做真实调用
allowed_files:
  - codex_source/schema_contracts/schemas/*
  - codex_source/schema_contracts/fixtures/*
  - codex_source/adapter_integration/*
forbidden_files:
  - scripts/vector_sync/*（除非明确授权）
  - .env*
  - docs/RAG_EXECUTION_ARCHITECTURE.md（不把 proposal 改成 active runtime）
must_read:
  - docs/RAG_EXECUTION_ARCHITECTURE.md
  - docs/VECTOR_RETRIEVAL_PLAN.md
  - codex_log/vector_rag_router_design/20260613_vector_rag_merge_readiness_report.md
  - codex_source/schema_contracts/schemas/retrieval_manifest.schema.yaml
execution_steps:
  - 定义 tool registry schema
  - 定义 retriever adapter schema
  - 用 fixture 表示 DashVector / Chroma 输出
  - 强制 source_readback_required
validation:
  - YAML parse
  - blocked fixtures cover page_content_only / chroma_replace_dashvector / rag_as_fact
done_when:
  - adapter workflow 可消费 retrieval_manifest fixture
blocked_if:
  - 需要真实 DashVector / Chroma
  - 需要外部 embedding API
```

### Task Slice 4：evaluator_failure_guardrail_matrix

```yaml
task_name: evaluator_failure_guardrail_matrix
goal: 把 evaluator、failure route、human review、guardrails 汇总为一张可执行矩阵
allowed_files:
  - codex_source/schema_contracts/schemas/*
  - codex_source/schema_contracts/fixtures/*
  - codex_source/schema_contracts/probes/*
  - codex_log/framework_adapter/*
forbidden_files:
  - runtime service code that starts service
  - media generation scripts
must_read:
  - codex_source/adapter_integration/completion_truth.py
  - codex_source/schema_contracts/schemas/human_review_interrupt.schema.yaml
  - codex_source/schema_contracts/schemas/service_contract_no_write.schema.yaml
  - codex_source/schema_contracts/schemas/completion_truth_check_node.schema.yaml
execution_steps:
  - 定义 evaluator_result schema
  - 定义 failure_route schema
  - 绑定 human_review_interrupt
  - 增加 status promotion blocked fixtures
validation:
  - false completion blocked
  - no-write blocked
  - human review cannot auto-pass
done_when:
  - 每个 blocked reason 都有 next owner / next safe step
blocked_if:
  - failure route 没证据路径
  - 人审点被自动跳过
```

### Task Slice 5：trace_report_log_validator

```yaml
task_name: trace_report_log_validator
goal: 建立本地 trace / report / latest 字段检查，不接外部观测服务
allowed_files:
  - codex_source/schema_contracts/schemas/*
  - codex_source/schema_contracts/probes/*
  - codex_log/engineering_line_audit/*
forbidden_files:
  - LangSmith / Langfuse config
  - .env*
must_read:
  - codex_source/schema_contracts/schemas/cross_contract_trace.schema.yaml
  - codex_log/framework_adapter/20260617_main_merge_completed_report.md
  - codex_log/latest.md
execution_steps:
  - 定义 report_contract
  - 定义 trace_event JSONL 字段
  - 写本地 report presence / required section / forbidden status scan
validation:
  - report validator pass
  - status promotion scan pass
done_when:
  - 报告缺字段能被本地脚本阻断
blocked_if:
  - 需要外部 telemetry key
  - trace 试图替代 repo facts
```

### Task Slice 6：isolated_runtime_hardening_probe

```yaml
task_name: isolated_runtime_hardening_probe
goal: 在前 5 个任务片通过后，做隔离 no-write runtime hardening
allowed_files:
  - codex_source/adapter_integration/*
  - codex_log/framework_adapter/*
forbidden_files:
  - .env*
  - dist/**
  - media/**
  - GPT数据源/**
must_read:
  - Task Slice 1-5 outputs
  - codex_source/adapter_integration/runtime_entry.py
  - codex_source/adapter_integration/service_boundary.py
  - codex_source/adapter_integration/runtime_service_probe.py
execution_steps:
  - 只做 no-write runtime hardening
  - 证明 runtime 不能写 repo / commit / push / 外呼 / 生成媒体
  - 输出 dated report
validation:
  - py_compile
  - no-write probe
  - forbidden action scan
done_when:
  - isolated runtime hardening probe passed and boundaries preserved
blocked_if:
  - 需要安装依赖
  - 需要持久端口
  - 需要 secret / API / TTS / DashVector / Chroma / media
```

## status_boundary（状态边界）

这些任务片是后续执行单模板，不代表已经执行。默认只允许逐片推进，且每片完成后必须更新 dated report、latest、path-limited stage、commit、push 和 remote readback。
