# Agent Service Toolkit Full Intake Adapter Design

## 1. file_role

This file is the Codex-side index for the future `JoshuaC215/agent-service-toolkit` adapter design.

It is not an install guide. It is not a migration guide. It is not a runtime enablement record.

## 2. current_status

- `project_route`: `video_factory`
- `external_framework`: `JoshuaC215/agent-service-toolkit`
- `design_status`: `adapter_design_only`
- `runtime_enabled`: `false`
- `dependency_installed`: `false`
- `external_code_copied`: `false`
- `main_flow_replaced`: `false`
- `active_write_executor`: `codex`
- `future_write_executor_types`: `trae / future_ide_agent`

## 3. canonical_design_files

Read these files before any future sandbox/prototype task:

1. `codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md`
2. `codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md`
3. `codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md`

## 4. first_principles

- External framework adapts to video_factory, not the reverse.
- GitHub repo files remain `source_of_truth`.
- DashVector / Vector RAG remains `retrieval_index / cache_layer`.
- DeepSeek is conditional reviewer / risk auditor / conflict second opinion, not default file reader.
- Runtime routes, retrieves, validates, blocks, interrupts, and creates handoff packages.
- `active_write_executor` performs actual writes.
- Current `active_write_executor = codex`.

## 5. agent_service_toolkit_module_policy

| Module | Policy |
|---|---|
| FastAPI service | keep enabled for sandbox/no-write adapter service |
| LangGraph agents | keep enabled for route and state graph |
| LangChain tools | keep enabled for read-only tools |
| Streamlit app | keep disabled first |
| Chroma RAG | replace with DashVector adapter |
| GitHub MCP agent | keep disabled until explicit authorization |
| Postgres checkpoint | keep disabled first |
| long-term Store | keep disabled first |
| tests | keep enabled/adapted |
| Docker | draft only for future sandbox |

## 6. minimum_closed_loop

```text
user_task_input
-> workflow_route_decision
-> retrieval_manifest
-> source_readback
-> deepseek_trigger_decision
-> blocked_if_check
-> human_review_interrupt
-> write_executor_handoff
-> execution_result_readback
-> technical_validation
-> content_validation_boundary_check
-> log_sync
-> next_action_decision
```

Do not enter sandbox install or minimal router prototype until this loop is reviewable as a schema-level contract.

## 7. next_allowed_stage

Recommended next stage:

`option_a_design_review_only`

Do not choose:

- `full_migration`
- `main_runtime_replace`
- `dependency_install_in_main`
