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
