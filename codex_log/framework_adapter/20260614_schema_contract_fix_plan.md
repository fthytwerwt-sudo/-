# 20260614 Schema Contract Fix Plan

## 1. route_decision

- `project_route = video_factory`
- `task_type = schema_contract_fix_plan + adapter_design_review_only + mechanism_repair_flow + project_file_change`
- `workflow_route_decision = mechanism_repair_flow`
- `responsibility_layer = mechanism_fix_layer + validation_layer + sync_layer`
- `large_task_gate.triggered = true`
- `deepseek_triggered = false`
- `not_deepseek_conclusion = true`
- `external_api_called = false`
- `execution_permission = write_schema_fixtures_index_report_latest_only`

This round creates draft schema contracts and static fixtures only. It does not install dependencies, copy external code, create sandbox, create minimal router prototype, enable runtime, or advance video / voice / visual / publish status.

## 2. files_read

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_log/framework_adapter/20260613_schema_contract_gap_review.md`
- `codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md`
- `codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md`
- `codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md`
- `codex_source/23_agent_service_toolkit_full_intake_adapter_design.md`

## 3. schemas_created

10 schema draft files were created:

1. `codex_source/schema_contracts/schemas/workflow_route_decision.schema.yaml`
2. `codex_source/schema_contracts/schemas/retrieval_manifest.schema.yaml`
3. `codex_source/schema_contracts/schemas/source_readback.schema.yaml`
4. `codex_source/schema_contracts/schemas/retrieval_gap_report.schema.yaml`
5. `codex_source/schema_contracts/schemas/deepseek_trigger_decision.schema.yaml`
6. `codex_source/schema_contracts/schemas/blocked_if_check.schema.yaml`
7. `codex_source/schema_contracts/schemas/human_review_interrupt.schema.yaml`
8. `codex_source/schema_contracts/schemas/write_executor_handoff.schema.yaml`
9. `codex_source/schema_contracts/schemas/completion_truth_check.schema.yaml`
10. `codex_source/schema_contracts/schemas/cross_contract_trace.schema.yaml`

Each schema includes `contract_name / version / status / project_route / purpose / required_fields / optional_fields / input_from / output_to / blocked_if_missing / must_not_do / validation_notes / trace_fields`.

## 4. fixtures_created

18 static fixture files were created:

- 9 passing fixtures under `codex_source/schema_contracts/fixtures/passing/`
- 9 blocked fixtures under `codex_source/schema_contracts/fixtures/blocked/`

Passing fixture task id:

```text
vf_schema_contract_fixture_20260614_001
```

Blocked fixture task id:

```text
vf_schema_contract_fixture_20260614_blocked_001
```

Blocked fixtures include `blocked: true` and `blocked_reasons`. Passing fixtures include all minimum required fields for their contract.

## 5. cross_contract_trace_rule

`cross_contract_trace.schema.yaml` standardizes:

- `task_id`
- `handoff_id`
- `commit_sha`
- `source_paths`
- `content_hashes`
- `workflow_type`
- `executor_type`
- `runtime_enabled`
- `sandbox_created`
- `minimal_router_prototype_created`

Current trace policy:

```text
runtime_enabled = false
sandbox_created = false
minimal_router_prototype_created = false
active_write_executor = codex
```

## 6. remaining_gaps

- Schemas are still `status: draft`; they need later human / architecture review before sandbox.
- Fixtures are static examples, not runtime tests.
- No LangGraph / FastAPI adapter service exists yet.
- No no-write sandbox exists yet.
- No minimal router prototype exists yet.
- No external framework code has been copied or installed.

## 7. sandbox_entry_decision

```text
sandbox_entry_allowed_now = false
reason = schema_drafts_created_but_not_reviewed_or_runtime_validated
next_required_gate = schema_contract_static_validation
```

## 8. validation_result

- `schema_file_count = 10`
- `passing_fixture_count = 9`
- `blocked_fixture_count = 9`
- `fixture_total = 18`
- `schema_required_key_check = passed`
- `passing_fixture_required_field_check = passed`
- `blocked_fixture_reason_check = passed`
- `fixture_credential_pattern_check = passed`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `forbidden_status_advanced = false`

## 9. generated_or_modified_files

Generated:

- `codex_source/schema_contracts/00_schema_contracts_index.md`
- `codex_source/schema_contracts/schemas/*.schema.yaml`
- `codex_source/schema_contracts/fixtures/passing/*.passing.yaml`
- `codex_source/schema_contracts/fixtures/blocked/*.blocked.yaml`
- `codex_log/framework_adapter/20260614_schema_contract_fix_plan.md`

Modified:

- `codex_log/latest.md`

## 10. git_sync_status

`pending_before_path_limited_commit_push_remote_readback`

Final commit, push, and remote readback evidence must be reported in the Codex final response after this report is staged and synced.

## 11. next_safe_step

```text
schema_contract_static_validation
```

Do not enter sandbox, minimal router prototype, runtime enablement, dependency installation, or external framework migration before the schema contracts and fixtures are reviewed and accepted.
