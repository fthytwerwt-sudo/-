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

## 20260616｜Editing Workflow Contract Patch

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: workflow_first_pre_integration_repair（工作流优先正式接入前修补）
  status（状态）: editing_workflow_contract_family_landed（剪辑 workflow 契约家族已落地）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段只补剪辑 workflow 契约家族和静态 fixture，用于阻断“技术预览、路由卡、报告生成、文件存在”冒充剪辑交付完成。它不执行剪辑、不生成视频、不启动 service、不启用 runtime、不合并 main。

### 2B.1 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `editing_execution_contract` | 约束剪辑执行必须有锁定文案、line_group 时间线、TTS、卡片、素材证据、审片包和完成真实性检查。 | `schemas/editing_execution_contract.schema.yaml` |
| `timeline_assembly_contract` | 约束时间线条目必须能回到 line_group、素材片段和时间码。 | `schemas/timeline_assembly_contract.schema.yaml` |
| `subtitle_card_overlap_contract` | 约束字幕、卡片和核心证据区不能 high severity 重叠。 | `schemas/subtitle_card_overlap_contract.schema.yaml` |
| `tts_route_contract` | 约束实际 TTS provider / model / voice_id / fallback 授权和非静音音频。 | `schemas/tts_route_contract.schema.yaml` |
| `review_pack_contract` | 约束候选片或阻断结果必须带审片包、预检报告、媒体探针和人工复审边界。 | `schemas/review_pack_contract.schema.yaml` |
| `media_probe_contract` | 约束媒体探针必须检查视频存在、音频、字幕、分辨率、时长和解码。 | `schemas/media_probe_contract.schema.yaml` |
| `publish_candidate_or_blocked_contract` | 约束剪辑 workflow 只能收口为人工复审候选片或可发布候选片不可交付阻断。 | `schemas/publish_candidate_or_blocked_contract.schema.yaml` |

### 2B.2 added_passing_fixtures（新增通过样例）

| fixture family | passing fixture |
|---|---|
| `editing_execution_contract` | `fixtures/passing/editing_execution_contract.passing.yaml` |
| `timeline_assembly_contract` | `fixtures/passing/timeline_assembly_contract.passing.yaml` |
| `subtitle_card_overlap_contract` | `fixtures/passing/subtitle_card_overlap_contract.passing.yaml` |
| `tts_route_contract` | `fixtures/passing/tts_route_contract.passing.yaml` |
| `review_pack_contract` | `fixtures/passing/review_pack_contract.passing.yaml` |
| `media_probe_contract` | `fixtures/passing/media_probe_contract.passing.yaml` |
| `publish_candidate_or_blocked_contract` | `fixtures/passing/publish_candidate_or_blocked_contract.passing.yaml` |

### 2B.3 added_blocked_fixtures（新增阻断样例）

| blocked case | blocked fixture |
|---|---|
| 缺文案到时间线映射 | `fixtures/blocked/editing_missing_script_to_timeline_map.blocked.yaml` |
| 技术预览冒充完成 | `fixtures/blocked/editing_technical_preview_as_completed.blocked.yaml` |
| 时间线画面错位 | `fixtures/blocked/timeline_visual_mismatch.blocked.yaml` |
| 字幕卡片高重叠 | `fixtures/blocked/subtitle_card_high_overlap.blocked.yaml` |
| TTS 未授权降级 | `fixtures/blocked/tts_fallback_unauthorized.blocked.yaml` |
| 审片包缺失 | `fixtures/blocked/review_pack_missing.blocked.yaml` |
| 媒体探针无效 | `fixtures/blocked/media_probe_invalid.blocked.yaml` |
| 候选片状态偷换 | `fixtures/blocked/publish_candidate_state_promotion.blocked.yaml` |

### 2B.4 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - 只补剪辑 workflow 契约，不等于正式接入整个项目
  - schema 落地不等于 runtime 接入
  - fixture 通过不等于真实剪辑可执行
  - review_pack contract 不等于真实审片包已生成
  - media_probe contract 不等于真实视频已探测
  - publish_candidate contract 不等于可发送状态开启
  - 本阶段不启动 service，不合并 main，不调用外部 API
```

## 20260616｜Editing Workflow No-Render Probe

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: editing_workflow_no_render_probe（剪辑工作流无渲染探测）
  status（状态）: no_render_probe_passed（无渲染探测通过）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  probe_script（探测脚本）: probes/editing_workflow_no_render_probe.py
  report（报告）: codex_log/framework_adapter/20260616_editing_workflow_no_render_probe_report.md
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  media_generated（是否生成媒体）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段新增剪辑 workflow 的本地无渲染 probe，用于验证 7 类剪辑契约家族和 15 个 passing / blocked fixture 能否形成可检查的静态链路。它不读取真实媒体、不调用 TTS、不调用 FFmpeg、不启动 service、不启用 runtime、不运行 Chroma 入库、不真实调用 DashVector。

### 2C.1 probe_inputs（探测输入）

| input family | files |
|---|---|
| `schemas` | `editing_execution_contract.schema.yaml`、`timeline_assembly_contract.schema.yaml`、`subtitle_card_overlap_contract.schema.yaml`、`tts_route_contract.schema.yaml`、`review_pack_contract.schema.yaml`、`media_probe_contract.schema.yaml`、`publish_candidate_or_blocked_contract.schema.yaml` |
| `passing fixtures` | `editing_execution_contract.passing.yaml`、`timeline_assembly_contract.passing.yaml`、`subtitle_card_overlap_contract.passing.yaml`、`tts_route_contract.passing.yaml`、`review_pack_contract.passing.yaml`、`media_probe_contract.passing.yaml`、`publish_candidate_or_blocked_contract.passing.yaml` |
| `blocked fixtures` | `editing_missing_script_to_timeline_map.blocked.yaml`、`editing_technical_preview_as_completed.blocked.yaml`、`timeline_visual_mismatch.blocked.yaml`、`subtitle_card_high_overlap.blocked.yaml`、`tts_fallback_unauthorized.blocked.yaml`、`review_pack_missing.blocked.yaml`、`media_probe_invalid.blocked.yaml`、`publish_candidate_state_promotion.blocked.yaml` |

### 2C.2 probe_result（探测结果）

```yaml
probe_result（探测结果）:
  schema_contracts_passed（schema 契约检查是否通过）: true
  passing_path_passed（通过路径是否通过）: true
  blocked_cases_passed（阻断样例是否通过）: true
  blocked_case_count（阻断样例数量）: 8
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
```

### 2C.3 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - no-render probe 通过不等于真实剪辑已执行
  - no-render probe 通过不等于视频已生成
  - no-render probe 通过不等于 TTS 已调用
  - no-render probe 通过不等于真实媒体探针已执行
  - no-render probe 通过不等于 runtime 接入
  - no-render probe 通过不等于 service 可启动
  - no-render probe 通过不等于 main 可合并
  - no-render probe 通过不等于整体代码接入已经就绪
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
