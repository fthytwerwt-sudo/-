# Schema Contracts Index

## 1. status

- `project_route = video_factory`
- `document_type = schema_contract_index`
- `status = draft`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`

This directory defines draft schema contracts and static fixtures for the future adapter contract layer. It does not install, enable, or run `agent-service-toolkit`.

## 2. contract order

```text
WorkflowRouteDecision
-> RetrievalManifest
-> SourceReadback
-> RetrievalGapReport
-> DeepSeekTriggerDecision
-> BlockedIfCheck
-> HumanReviewInterrupt
-> WriteExecutorHandoff
-> CompletionTruthCheck
```

`CrossContractTrace` is the shared trace schema across the chain. It standardizes `task_id / handoff_id / commit_sha / source_path / content_hash` style fields and keeps `runtime_enabled / sandbox_created / minimal_router_prototype_created` false in this design stage.

## 2A. 20260616 adapter contract phase update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: contracts_and_schemas（契约与 schema 阶段）
  status（状态）: contract_schema_phase_landed（契约 / schema / fixture 已落地）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段把 `agent-service-toolkit` 接入前必须遵守的规则落成静态 schema、passing fixture 和 blocked fixture。它仍然不是 adapter runtime 代码，不启动 FastAPI / Docker / Postgres / Streamlit，不运行 Chroma ingestion，不调用 DashVector 或外部 API。

### 2A.1 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `graph_runtime_adapter` | 规定 LangGraph 只能作为 no-write workflow runtime layer，不能替代 Project State Action Router。 | `schemas/graph_runtime_adapter.schema.yaml` |
| `retrieval_manifest` | 扩展检索清单字段，要求 provider / source_path / chunk_id / source_readback_required / gap_status。 | `schemas/retrieval_manifest.schema.yaml` |
| `source_readback_map` | 把检索命中映射回当前分支原文，判断能否作为事实。 | `schemas/source_readback_map.schema.yaml` |
| `cleaning_adapter` | 规定入库前安全加载、secret scan、metadata、dedup、chunking 和 source_readback index。 | `schemas/cleaning_adapter.schema.yaml` |
| `service_contract_no_write` | 规定 FastAPI / service 只能 route / retrieve / validate / block / interrupt / handoff，不能写仓库。 | `schemas/service_contract_no_write.schema.yaml` |
| `runtime_memory_boundary` | 规定 runtime memory 只能作临时状态和非权威缓存，不得替代仓库事实。 | `schemas/runtime_memory_boundary.schema.yaml` |
| `completion_truth_check_node` | 规定完成真实性检查节点必须拦截 false completion、false runtime、状态误推进、RAG 冒充事实和 service 冒充写入。 | `schemas/completion_truth_check_node.schema.yaml` |

### 2A.2 added_fixture_families（新增 fixture 家族）

| fixture family | passing fixtures | blocked fixtures |
|---|---|---|
| `graph_runtime_adapter` | `fixtures/passing/graph_runtime_adapter.passing.yaml` | `fixtures/blocked/graph_runtime_adapter.blocked_runtime_write.yaml`、`fixtures/blocked/graph_runtime_adapter.blocked_missing_source_readback.yaml`、`fixtures/blocked/graph_runtime_adapter.blocked_completed_without_truth_check.yaml` |
| `retrieval_manifest` | `fixtures/passing/retrieval_manifest_dashvector_fixture.passing.yaml`、`fixtures/passing/retrieval_manifest_chroma_sandbox_fixture.passing.yaml` | `fixtures/blocked/retrieval_manifest_chroma_metadata_missing.blocked.yaml`、`fixtures/blocked/retrieval_manifest_page_content_only.blocked.yaml`、`fixtures/blocked/retrieval_manifest_chroma_replace_dashvector.blocked.yaml`、`fixtures/blocked/retrieval_manifest_claimed_as_fact.blocked.yaml` |
| `source_readback_map` | `fixtures/passing/source_readback_map.passing.yaml` | `fixtures/blocked/source_readback_missing.blocked.yaml`、`fixtures/blocked/source_readback_conflict.blocked.yaml`、`fixtures/blocked/source_readback_stale_source.blocked.yaml` |
| `cleaning_adapter` | `fixtures/passing/cleaning_adapter.passing.yaml` | `fixtures/blocked/cleaning_secret_like_content.blocked.yaml`、`fixtures/blocked/cleaning_missing_metadata.blocked.yaml`、`fixtures/blocked/cleaning_chunk_missing_source_path.blocked.yaml`、`fixtures/blocked/cleaning_legacy_fact_override.blocked.yaml` |
| `service_contract_no_write` | `fixtures/passing/service_contract_no_write.passing.yaml` | `fixtures/blocked/service_contract_no_write_attempt_write.blocked.yaml`、`fixtures/blocked/service_contract_no_write_attempt_commit_push.blocked.yaml`、`fixtures/blocked/service_contract_no_write_runtime_enabled.blocked.yaml`、`fixtures/blocked/service_contract_no_write_external_api_without_auth.blocked.yaml` |
| `runtime_memory_boundary` | `fixtures/passing/runtime_memory_boundary.passing.yaml` | `fixtures/blocked/runtime_memory_boundary.blocked_repo_fact_replacement.yaml`、`fixtures/blocked/runtime_memory_boundary.blocked_operation_records_replacement.yaml`、`fixtures/blocked/runtime_memory_boundary.blocked_current_data_goal_anchor_replacement.yaml` |
| `completion_truth_check_node` | `fixtures/passing/completion_truth_check.passing.yaml` | `fixtures/blocked/completion_truth_check.false_completion_blocked.yaml`、`fixtures/blocked/completion_truth_check.sandbox_as_runtime_blocked.yaml`、`fixtures/blocked/completion_truth_check.rag_as_fact_blocked.yaml`、`fixtures/blocked/completion_truth_check.technical_as_content_blocked.yaml`、`fixtures/blocked/completion_truth_check.file_exists_as_done_blocked.yaml`、`fixtures/blocked/completion_truth_check.service_as_repo_write_blocked.yaml` |

### 2A.3 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - schema 落地不等于 runtime 接入
  - fixture 通过不等于正式服务可用
  - Chroma fixture 不等于 Chroma 替代 DashVector
  - service no-write fixture 不等于允许启动服务
  - runtime memory fixture 不等于 memory 可替代 Git / repo / codex_log / review_loop 事实
  - completion truth fixture 不等于视频 / 声音 / 视觉 / 发布状态推进
  - adapter_infrastructure_flow 仍为 candidate，未写入正式 workflow 索引
```

## 3. contract responsibilities

| order | contract | responsibility | schema |
|---:|---|---|---|
| 1 | `WorkflowRouteDecision` | Route user input into project, task type, workflow, responsibility layer, and execution permission. | `schemas/workflow_route_decision.schema.yaml` |
| 2 | `RetrievalManifest` | Record DashVector / Vector RAG retrieval and require repo source readback. | `schemas/retrieval_manifest.schema.yaml` |
| 3 | `SourceReadback` | Confirm repo source files remain `source_of_truth`. | `schemas/source_readback.schema.yaml` |
| 4 | `RetrievalGapReport` | Convert empty, low-confidence, legacy, or conflicting retrieval into blockers or DeepSeek trigger recommendation. | `schemas/retrieval_gap_report.schema.yaml` |
| 5 | `DeepSeekTriggerDecision` | Decide if DeepSeek enters as conditional read-only reviewer after retrieval/readback. | `schemas/deepseek_trigger_decision.schema.yaml` |
| 6 | `BlockedIfCheck` | Normalize blockers from all upstream contracts into one execution gate. | `schemas/blocked_if_check.schema.yaml` |
| 7 | `HumanReviewInterrupt` | Insert human review before sandbox, runtime enablement, status promotion, source conflict override, or executor switch. | `schemas/human_review_interrupt.schema.yaml` |
| 8 | `WriteExecutorHandoff` | Package scoped write instructions for `active_write_executor = codex`. | `schemas/write_executor_handoff.schema.yaml` |
| 9 | `CompletionTruthCheck` | Decide whether completion can be claimed without false status, fallback, retrieval-only, or local-only claims. | `schemas/completion_truth_check.schema.yaml` |

## 4. fixtures

Each of the 9 core contracts has:

- one passing fixture under `fixtures/passing/`
- one blocked fixture under `fixtures/blocked/`

Fixture task ids:

- passing: `vf_schema_contract_fixture_20260614_001`
- blocked: `vf_schema_contract_fixture_20260614_blocked_001`

The passing fixtures are static examples only. They do not prove a runtime exists. The blocked fixtures show how each contract must stop execution when a critical field is missing, a source conflict exists, a forbidden status appears, or human review is required.

## 5. sandbox preconditions

All 9 contracts are required before any sandbox or minimal router prototype.

Sandbox remains blocked unless all are true in a later task:

1. schemas are reviewed and accepted;
2. fixtures pass static validation;
3. cross-contract trace fields are consistent;
4. source readback remains mandatory after retrieval;
5. DeepSeek remains conditional read-only review;
6. human review interrupts cannot be auto-resumed;
7. write handoff keeps `active_write_executor = codex`;
8. completion truth check forbids status promotion and false completion claims.

## 6. install preflight status

2026-06-14 static validation outcome:

```text
schema_contract_static_validation = passed
install_preflight_ready = true
```

This means the schema contract layer is ready for a later no-write sandbox intake prompt. It does not mean sandbox has been created, runtime has been enabled, dependencies have been installed, or external code has been copied.

## 7. why sandbox is still not created in this stage

`sandbox_entry_allowed_this_round = false`

Reasons:

- this round is static validation only;
- no install task has been authorized;
- no adapter service has been installed or run;
- no sandbox path has been created;
- no minimal router prototype has been created;
- no external code has been copied;
- no dependency has been installed.

## 8. next stage

Next safe stage:

```text
sandbox_intake_no_write_prompt
```

The next prompt must remain no-write unless the user explicitly authorizes installation in a separate task.

Static validation checklist now passed:

1. 10 schema files exist.
2. 18 fixture files exist.
3. Every schema includes `contract_name / version / status / required_fields / trace_fields`.
4. Every passing fixture contains every minimum required field for its contract.
5. Every blocked fixture contains `blocked: true` and `blocked_reasons`.
6. Fixture files do not contain credential-like values.
7. Forbidden paths remain untouched.
8. Runtime, sandbox, prototype, video, publish, voice, and visual statuses remain unadvanced.
