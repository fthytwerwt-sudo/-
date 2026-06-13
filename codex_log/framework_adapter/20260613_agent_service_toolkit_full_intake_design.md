# 20260613 Agent Service Toolkit Full Intake Adapter Design

## 1. route_decision

- `project_route`: `video_factory`
- `task_type`: `mechanism_repair_flow + external_framework_adapter_design + project_architecture_design + deepseek_positioning_repair`
- `workflow_route_decision`: `mechanism_repair_flow`
- `responsibility_layer`: `mechanism_fix_layer + project_judgment_layer + validation_layer + sync_layer`
- `large_task_gate.triggered`: `true`
- `lane_recommendation`: `audit_design_lane`
- `parallel_recommendation`: `read_parallel_for_audit / serial_only_for_design_writes`
- `execution_permission`: `design_files_only`
- `deepseek_triggered`: `false`
- `deepseek_status`: `not_triggered_by_policy`
- `not_deepseek_conclusion`: `true`
- `external_api_called`: `true_public_github_readonly`

This round does not install dependencies, does not copy external project code, does not modify `pyproject.toml`, `package.json`, `compose.yaml`, `docker-compose.yml`, `dist/`, `public/`, media assets, or formal video / voice / visual / publish status.

## 2. current_formal_state_check

### 2.1 Formal entry conflict

`AGENTS.md`, `codex_source/00_codex_readme.md`, `codex_source/17_deepseek_supply_controller_protocol.md`, and `codex_source/18_deepseek_supply_request_schema.md` still contain formal language that treats DeepSeek as a default / mandatory supply loop for every Codex task.

`docs/AI_ROLE_MAP.md`, `docs/RAG_EXECUTION_ARCHITECTURE.md`, `docs/DEEPSEEK_POSITIONING.md`, `docs/VECTOR_RETRIEVAL_PLAN.md`, and `docs/CODEX_EXECUTION_RULES.md` already contain the newer RAG-first / DeepSeek-as-reviewer direction, but they are explicitly marked:

- `document_status = draft_architecture_proposal`
- `authority_level = proposal_only`
- `active_runtime_rule = false`

Therefore, this round should not silently patch formal mechanism files. The correct action is to produce adapter design files and a formal patch proposal for a later controlled mechanism repair.

### 2.2 RAG / DashVector status

Current Vector RAG reports confirm:

- `selected_embedding_model = text-embedding-v4`
- `embedding_dimension = 1024`
- `dashvector_collection = video_factory_docs_test`
- `chunks_written = 261`
- `all_queries_success = true`
- `all_readback_success = true`

This proves a minimal retrieval readback chain, not a full runtime integration. DashVector remains `retrieval_index / cache_layer`; GitHub repo files remain `source_of_truth`.

### 2.3 Write boundary status

Older wording says `Codex-only write boundary`. The user has now confirmed this should become:

- `write_executor_boundary`
- `active_write_executor`
- `executor_type = codex / trae / future_ide_agent`

Current active executor remains `codex`, but the mechanism design must stop hardcoding Codex as the only possible future writer.

## 3. agent_service_toolkit_intake_analysis

### 3.1 External project role

`JoshuaC215/agent-service-toolkit` is a full agent service toolkit built around:

- `LangGraph`: agent state graph and control flow.
- `FastAPI`: service shell with invoke / stream endpoints.
- `Streamlit`: optional UI client.
- `agent registry`: `src/agents/agents.py` maps agent ids to graph instances.
- `RAG assistant`: Chroma-based sample retrieval agent.
- `GitHub MCP agent`: optional GitHub tooling agent gated by `GITHUB_PAT`.
- `Postgres checkpoint / Store`: runtime memory/checkpoint support.
- `tests`: unit and integration tests for service, client, agents, and streaming.

### 3.2 LangChain role

`LangChain` should be treated as the tool/model abstraction layer:

- acceptable use: wrap DashVector search as a LangChain-compatible tool or retriever;
- acceptable use: bind read-only tools into LangGraph nodes;
- not acceptable: let LangChain tools directly mutate repo files;
- not acceptable: treat LangChain tool output as completion proof.

### 3.3 LangGraph role

`LangGraph` should become the runtime decision graph, not the writer:

```text
task_intake
-> workflow_route_decision
-> retrieval_manifest
-> source_readback
-> deepseek_trigger_decision
-> blocked_if_check
-> human_review_interrupt
-> write_executor_handoff
-> execution_result_readback
-> completion_truth_check
```

LangGraph nodes may decide, retrieve, validate, interrupt, or package handoff. They must not directly write repo files in phase 1.

### 3.4 FastAPI role

`FastAPI service` should be retained as the adapter service boundary:

- `/info`: expose available video_factory adapter agents and schema versions.
- `/invoke`: accept one route decision / validator task and return structured output.
- `/stream`: optional for later diagnostics only.
- auth: keep disabled in local design unless sandbox explicitly needs it; no secrets in this phase.

### 3.5 Streamlit role

`Streamlit app` is not needed by the user in phase 1.

Decision:

- status: `keep_disabled`
- reason: UI is not part of current closed loop.
- future: may be pruned after closed-loop proof if no human review console is needed.

### 3.6 Agent registry role

The upstream registry pattern can map video_factory workflows:

| video_factory workflow | proposed agent id | role |
|---|---|---|
| `copy_testing_flow` | `vf-copy-testing-router` | copy route, source checks, handoff package |
| `material_evidence_flow` | `vf-material-evidence-router` | material evidence readback and blocker checks |
| `aesthetic_editing_flow` | `vf-aesthetic-editing-router` | preflight / handoff only, no media execution |
| `quality_review_flow` | `vf-quality-review-router` | technical/content boundary validator |
| `data_review_flow` | `vf-data-review-router` | operation data intake/review router |
| `mechanism_repair_flow` | `vf-mechanism-repair-router` | mechanism patch proposal and status boundary |

First implementation should not copy upstream agents. It should define local adapter schemas and only later map them into an agent registry.

### 3.7 Interrupt role

LangGraph `interrupt()` / `Command(resume=...)` maps well to:

- human review before status promotion;
- human review before sandbox install;
- human review when RAG readback conflicts with repo files;
- human review before enabling GitHub MCP tools;
- human review before any executor other than `codex`.

### 3.8 RAG assistant role

The upstream `rag_assistant` is useful as a shape reference but not as the retrieval implementation.

Reject as formal source:

- Chroma DB
- OpenAIEmbeddings as default
- local `./chroma_db`

Replace with:

- `dashvector_search_tool`
- `github_source_readback_tool`
- `retrieval_manifest_schema`
- `retrieval_gap_report_schema`

### 3.9 GitHub MCP agent role

The GitHub MCP agent must be `keep_disabled` in phase 1.

Reasons:

- It requires `GITHUB_PAT`.
- It exposes direct repository and file operations.
- It can bypass `active_write_executor` if enabled too early.

Allowed future use:

- read-only GitHub metadata query in sandbox;
- no write tools unless the write executor contract explicitly wraps and logs every change;
- no PAT/token requirement in design-only or no-write sandbox stage.

## 4. full_intake_plan

### Phase 0: Design only, current round

Outputs:

- `codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md`
- `codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md`
- `codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md`
- `codex_source/23_agent_service_toolkit_full_intake_adapter_design.md`
- `codex_log/latest.md` entry

No dependency installation. No external code copy. No runtime enablement.

### Phase 1: Adapter contract design review

Goal:

- Convert this design into a reviewed contract set.

Artifacts:

- `VideoFactoryTaskInput`
- `WorkflowRouteDecision`
- `RetrievalManifest`
- `SourceReadback`
- `RetrievalGapReport`
- `DeepSeekTriggerDecision`
- `BlockedIfCheck`
- `HumanReviewInterrupt`
- `WriteExecutorHandoff`
- `ExecutionResultReadback`
- `CompletionTruthCheck`

Exit criteria:

- every schema has required fields;
- every workflow has `input_signal / must_read / retrieval_query / handoff / blocked_if / human_review_point / write_executor_handoff / completion_truth_check`;
- no schema grants direct file write to runtime.

### Phase 2: Sandbox intake, no write

Goal:

- Create a sandbox adapter service outside the main runtime path, or in a clearly isolated repo subpath if later authorized.

Allowed:

- local mock DashVector adapter;
- static fixture retrieval manifest;
- no secrets;
- no GitHub write;
- no Streamlit.

Blocked if:

- requires dependency installation in current main environment;
- requires `.env`;
- requires `GITHUB_PAT`;
- tries to edit formal mechanism files.

### Phase 3: Minimal router prototype

Goal:

- Route one mechanism repair task through LangGraph and output a no-write handoff package.

Required proof:

- route decision;
- workflow route decision;
- retrieval manifest or retrieval gap;
- source readback proof;
- DeepSeek trigger decision;
- blocked_if result;
- human review interrupt when needed;
- write executor handoff package;
- no actual file write by runtime.

### Phase 4: Write executor handoff validation

Goal:

- Let `active_write_executor = codex` execute one generated handoff package.

Required proof:

- Codex reads handoff;
- Codex reads original files;
- Codex applies scoped changes;
- validation runs;
- report/log created;
- path-limited commit;
- push;
- remote readback.

This proves closed loop only for `executor_type = codex`.

### Phase 5: Optional executor expansion

Only after Codex executor loop is proven:

- evaluate `executor_type = trae`;
- define Trae handoff format;
- prove Trae cannot bypass source readback, status boundary, validation, git sync, and remote readback.

## 5. module_keep_disable_prune_matrix

| Module | Decision | First-stage policy | Reason |
|---|---|---|---|
| FastAPI service | `keep_enabled` | Use as adapter service shell in sandbox/no-write stage | Clean boundary for route/retrieval/validator endpoints |
| LangGraph agents | `keep_enabled` | Use for deterministic-ish graph flow and interrupt points | Best match for workflow runtime |
| LangChain tools | `keep_enabled` | Read-only tools only | Useful for tool abstraction; must not write |
| Streamlit app | `keep_disabled` | Do not run in phase 1 | User does not need frontend UI |
| Chroma RAG | `replace_adapter` | Do not use as formal retrieval source | Current project uses Alibaba embedding + DashVector |
| DashVector adapter | `keep_enabled` | Build as project-owned retrieval adapter | Main retrieval route |
| GitHub MCP agent | `keep_disabled` | Design reference only | Requires PAT and can bypass write boundary |
| Postgres checkpoint | `keep_disabled` | Keep disabled in first no-write prototype | Adds infra; current state remains repo/log based |
| long-term Store | `keep_disabled` | Disable until memory policy exists | Must not replace repo facts or RAG |
| tests | `keep_enabled` | Adapt test style for schemas/router/validator | Required for closed loop proof |
| Docker | `draft_only` | Do not modify current Docker files | Useful later for sandbox only |
| content moderation / Safeguard | `draft_only` | Optional later | Not core to video_factory routing loop |
| LangSmith / Langfuse feedback | `keep_disabled` | Disable unless user authorizes external observability | Avoid external telemetry/secrets |
| MCP adapters | `draft_only` | Keep as optional future adapter | Needs explicit tool boundary |
| privatecredentials pattern | `reject` | Do not adopt | Current project must not create a credential surface for this adapter |

Prune rule:

`prune_after_closed_loop` applies to Streamlit, Chroma sample code, demo agents, unused provider integrations, and sample credentials only after one full Codex write executor closed loop is proven and the adapter contract is stable.

## 6. dashvector_adapter_plan

### 6.1 Principle

Do not use upstream Chroma as the formal retrieval source. The upstream RAG assistant is a structural reference only.

Current formal retrieval path should be:

```text
task query
-> dashvector_search_tool
-> retrieval_manifest
-> github_source_readback_tool
-> source_readback
-> retrieval_gap_report
-> router / validator
```

### 6.2 Required adapters

#### dashvector_search_tool

Input:

- `query`
- `workflow_type`
- `authority_filter`
- `status_filter`
- `top_k`

Output:

- `chunk_id`
- `source_path`
- `heading_path`
- `content_hash`
- `commit_sha`
- `branch`
- `retrieval_score`
- `authority_level`
- `status_label`
- `do_not_use_for_completion_claim = true`

#### github_source_readback_tool

Input:

- `source_path`
- `content_hash`
- `commit_sha`
- `heading_path`

Output:

- `readback_status = passed / failed / conflict`
- `matched_excerpt`
- `current_file_hash`
- `conflict_reason`

#### retrieval_manifest_schema

Must include:

- `task_id`
- `workflow_type`
- `queries`
- `retrieved_chunks`
- `source_paths`
- `readback_required = true`
- `vector_result_not_completion_proof = true`

#### retrieval_gap_report_schema

Must include:

- `rag_empty`
- `rag_low_confidence`
- `source_conflict`
- `missing_source_path`
- `missing_content_hash`
- `legacy_source_hit`
- `blocked_if_unresolved`
- `deepseek_trigger_recommended`

### 6.3 Blockers

Block if:

- retrieval result lacks source path, chunk id, or content hash;
- readback fails;
- RAG hit is only legacy/demoted source and no current source confirms it;
- vector result is used as completion proof;
- adapter requires secret/API key in design or no-write sandbox stage.

## 7. deepseek_positioning_plan

DeepSeek moves from:

- `default_file_supplier`
- `default_context_reader`
- `default_project_memory`

To:

- `reasoning_reviewer`
- `risk_auditor`
- `conflict_second_opinion`
- `fallback_context_synthesizer`
- `external_deep_supply_optional`

Trigger only when:

- `rag_empty`
- `rag_low_confidence`
- `source_conflict`
- `mechanism_conflict`
- `high_risk_execution`
- `pre_execution_risk_review`
- `post_execution_discrepancy_review`
- `user_explicit_request`
- `external_deep_reasoning_needed`

Forbidden:

- write files;
- commit;
- push;
- replace GitHub repo source of truth;
- replace DashVector / Vector RAG retrieval;
- write unreconciled conclusions as project facts;
- decide final business/content validation alone;
- claim participation when token usage was not observed and execution was local fallback.

Input:

- `retrieval_manifest`
- `source_readback`
- `retrieval_gap_report`
- `user_goal`
- `risk_questions`

Output:

- `reasoning_review`
- `risk_report`
- `conflict_report`
- `missing_context_report`
- `executor_handoff_suggestions`

## 8. write_executor_abstraction_plan

Old:

- `codex_write_boundary`
- `Codex-only writer`

New:

- `write_executor_boundary`
- `active_write_executor`
- `executor_type`

Supported executor types:

- `executor_type = codex`
- `executor_type = trae`
- `executor_type = future_ide_agent`

Runtime responsibility:

- route;
- retrieve;
- readback;
- validate;
- block;
- interrupt for human review;
- generate handoff package.

Runtime must not:

- write repo files directly in phase 1;
- commit;
- push;
- update content/voice/visual/publish status;
- bypass human review.

Write executor responsibility:

- `file_change`
- `validation`
- `report`
- `git_sync` if supported
- `remote_readback` if supported

## 9. workflow_runtime_mapping

### 9.1 copy_testing_flow

- `input_signal`: final copy, title, opening, copy testing, next script.
- `must_read`: copy rules, copy router, AI video value rules, current formal facts, current data goal anchor.
- `retrieval_query`: current copy rule, final script source, data goal, forbidden copy changes.
- `required_handoff`: copy source check, content route card draft, material detail request if needed.
- `blocked_if`: final copy source unclear, data anchor missing, Codex asked to rewrite final copy directly.
- `human_review_point`: before final copy semantic change or content validation claim.
- `write_executor_handoff`: scoped doc/report update only.
- `completion_truth_check`: no content status promotion without human/GPT final review.

### 9.2 material_evidence_flow

- `input_signal`: new material, recording, screenshot, material audit, evidence sufficiency.
- `must_read`: material audit skill, copy router, AI video value rules, Codex readme/rules.
- `retrieval_query`: material evidence contract, source segment inventory, privacy/platform risk.
- `required_handoff`: material parse pack, timecode inventory, evidence contract, missing material report.
- `blocked_if`: missing timecodes, unreadable evidence, material cannot support copy.
- `human_review_point`: before deciding material is enough for final content.
- `write_executor_handoff`: generate reports only; no media execution by runtime.
- `completion_truth_check`: evidence report is not final script or video completion.

### 9.3 aesthetic_editing_flow

- `input_signal`: editing quality, not demo-like, subtitle/card overlap, publish candidate intent.
- `must_read`: material parse pack, source inventory, AI video value rules, current facts, router, judgment matrix.
- `retrieval_query`: editing decision rules, visual readability, script-to-timeline gate, overlap gate.
- `required_handoff`: editing decision pack, visual readability report, review pack requirements.
- `blocked_if`: no line-level script map, no material ledger, high severity overlap, technical preview only.
- `human_review_point`: before publish candidate quality claim.
- `write_executor_handoff`: video executor package only after all preflight reports.
- `completion_truth_check`: publish candidate requires media validation and human review boundary.

### 9.4 quality_review_flow

- `input_signal`: review, not good, technical/content validation, send_ready, voice conflict.
- `must_read`: latest, current facts, AI value rules, review pack summary/manifest, project router.
- `retrieval_query`: technical validation boundary, content validation boundary, remaining blockers.
- `required_handoff`: quality issue classifier, technical validation report, remaining blockers.
- `blocked_if`: technical validation written as content validation, missing review pack, voice route unclear.
- `human_review_point`: before content validation, send_ready, voice validation, final visual status.
- `write_executor_handoff`: report/log update only.
- `completion_truth_check`: forbidden status fields remain unchanged unless explicitly authorized.

### 9.5 data_review_flow

- `input_signal`: 24h / 72h / 7d data, platform metrics, post-publish review, next variable.
- `must_read`: review loop readme, current operation target, operation records index, current data goal anchor.
- `retrieval_query`: current operation target, threshold config, current video record, next variable rule.
- `required_handoff`: operation data record, missing fields report, threshold check, next variable draft.
- `blocked_if`: video id unclear, time window unclear, missing data, multiple variables at once.
- `human_review_point`: before deciding success/failure or next content variable.
- `write_executor_handoff`: data record/report update only.
- `completion_truth_check`: data intake is not business validation success.

### 9.6 mechanism_repair_flow

- `input_signal`: mechanism/routing repair, external framework adapter, old context conflict.
- `must_read`: AGENTS, Codex readme, workflow index, state router, latest, affected mechanism files.
- `retrieval_query`: current mechanism boundary, RAG-first drafts, DeepSeek old/new position, write executor boundary.
- `required_handoff`: impact check, affected entry files, design layer, status boundary report.
- `blocked_if`: direct formal fact/status modification without explicit scope, dependency install, external code copy.
- `human_review_point`: before formal mechanism patch, sandbox install, or runtime enablement.
- `write_executor_handoff`: design files or explicit formal patch proposal.
- `completion_truth_check`: no runtime enabled unless closed-loop proof exists.

## 10. closed_loop_definition

Minimum closed loop:

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

Completion requires:

- source readback passed;
- blocked_if check passed or blocked honestly;
- human review interrupt is present where needed;
- write executor handoff is explicit;
- execution result is read back from changed files;
- technical validation is separate from content validation;
- log sync records the true state;
- no forbidden status field is advanced.

Only after this loop is proven should the project enter sandbox install or minimal router prototype.

## 11. formal_patch_proposal_if_needed

Later formal mechanism patch should update, in one controlled task:

- `AGENTS.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`

Patch goals:

1. Replace `Codex-only write boundary` with `write_executor_boundary`.
2. Keep `active_write_executor = codex` until another executor is proven.
3. Replace DeepSeek mandatory default supply with RAG-first arbitration plus conditional DeepSeek review.
4. Keep DashVector as retrieval/cache layer, not fact source.
5. Add human review and completion truth checks before runtime enablement.

This round does not apply that patch.

## 12. next_stage_execution_prompt_draft

```text
【任务目标】
本轮只做《视频工厂》agent-service-toolkit adapter design review，不安装、不迁移、不改主流程。

【必须读取】
- AGENTS.md
- codex_log/latest.md
- codex_source/23_agent_service_toolkit_full_intake_adapter_design.md
- codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md
- codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md
- codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md
- docs/RAG_EXECUTION_ARCHITECTURE.md
- docs/VECTOR_RETRIEVAL_PLAN.md

【执行步骤】
1. 输出 route_decision。
2. 复审 adapter contract 是否完整。
3. 输出 schema list：WorkflowRouteDecision / RetrievalManifest / SourceReadback / RetrievalGapReport / DeepSeekTriggerDecision / BlockedIfCheck / HumanReviewInterrupt / WriteExecutorHandoff / CompletionTruthCheck。
4. 判断是否可以进入 option_b_sandbox_intake_no_write。

【禁止】
- 不安装依赖。
- 不复制外部项目代码。
- 不修改 pyproject.toml/package.json/compose.yaml。
- 不启用 GitHub MCP write tools。
- 不推进内容、声音、视觉、发布状态。

【输出】
- adapter_design_review_report
- schema_contract_gap_list
- sandbox_no_write_entry_conditions
- next_safe_step
```

## 13. next_stage_recommendation

`option_a_design_review_only`

Reason:

- Formal mechanism still contains old DeepSeek mandatory-loop language.
- RAG-first docs are still draft/proposal, not active runtime rule.
- No adapter schemas exist yet.
- No no-write sandbox has been created.
- Full closed loop has not been proven.
