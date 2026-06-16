# 20260613 Schema Contract Gap Review

## route_decision

- `project_route`: `video_factory`
- `task_type`: `schema_contract_gap_review + adapter_design_review_only + mechanism_repair_flow + review_diagnosis_audit`
- `workflow_route_decision`: `mechanism_repair_flow`
- `execution_permission`: `add_report_and_latest_only`
- `large_task_gate.triggered`: `true`
- `deepseek_triggered`: `false`
- `external_api_called`: `false`
- `active_write_executor`: `codex`

本轮只做 9 个结构契约的缺口复审，不写 runtime 代码，不安装依赖，不复制外部项目代码，不创建 sandbox，不创建 minimal router prototype，不推进视频 / 声音 / 视觉 / 发布状态。

## current_adapter_status

- `design_status = adapter_design_only`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`
- `next_safe_step = schema_contract_fix_plan`

判断：进入 sandbox / prototype 前必须先补齐 9 个契约的 schema 草案、样例 fixture 和字段级阻断规则；当前不允许进入 `option_b_sandbox_intake_no_write`。

## schema_contract_gap_review_report

### 1. WorkflowRouteDecision

- `contract_role`: 把任务归位到 6 条 workflow，并给下游 runtime 一个确定的路线、职责层和下一步边界。
- `required_fields`: `task_id`, `project_route`, `task_type`, `workflow_route_decision`, `responsibility_layer`, `large_task_gate`, `execution_permission`, `allowed_next_steps`, `forbidden_next_steps`, `reasoning_summary`.
- `optional_fields`: `confidence`, `parallel_mode`, `must_read_files`, `required_handoff`, `forbidden_status`, `blocked_if`.
- `input_from`: `AGENTS.md`, user task, `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`.
- `output_to`: `state_action_router`, `retrieval_manifest`, `blocked_if_check`.
- `blocked_if_missing`: true.
- `must_not_do`: 不得直接进入写入、媒体生成、runtime enablement 或状态推进。
- `gap_status`: `partial`.
- `gap_detail`: 现有 workflow index 只定义 `workflow_type / reason / must_read / required_handoff / forbidden_status / blocked_if`；缺 `task_id / project_route / task_type / responsibility_layer / large_task_gate / execution_permission / allowed_next_steps / forbidden_next_steps / reasoning_summary` 的统一契约。
- `before_sandbox_required`: true.

### 2. RetrievalManifest

- `contract_role`: 记录 DashVector / Vector RAG 检索输入、召回结果、权威等级和必须回读的来源证据。
- `required_fields`: `task_id`, `workflow_type`, `retrieval_queries`, `retrieval_provider`, `embedding_model`, `vector_collection`, `retrieved_chunks`, `source_paths`, `content_hashes`, `commit_sha`, `authority_level`, `readback_required`, `vector_result_not_completion_proof`.
- `optional_fields`: `top_k`, `score_threshold`, `heading_path`, `status_filter`, `authority_filter`, `legacy_hit_reason`.
- `input_from`: `WorkflowRouteDecision`, DashVector adapter, repo allowlist / metadata.
- `output_to`: `SourceReadback`, `RetrievalGapReport`, `DeepSeekTriggerDecision`.
- `blocked_if_missing`: true when execution depends on retrieved context.
- `must_not_do`: 不得把向量召回写成事实源或完成证明；不得使用 Chroma / OpenAIEmbeddings 替代当前 DashVector 路线。
- `gap_status`: `partial`.
- `gap_detail`: 设计文件已有 `dashvector_search_tool` 输入输出字段，但缺顶层 `RetrievalManifest` schema，且没有把 `embedding_model = text-embedding-v4`、`vector_collection = video_factory_docs_test`、`readback_required`、`vector_result_not_completion_proof` 固定成契约字段。
- `before_sandbox_required`: true.

### 3. SourceReadback

- `contract_role`: 从仓库原文件回读召回来源，确认 vector chunk 未替代 source_of_truth。
- `required_fields`: `task_id`, `source_path`, `expected_content_hash`, `current_content_hash`, `commit_sha`, `readback_status`, `matched_excerpt`, `conflict_reason`, `source_of_truth_confirmed`.
- `optional_fields`: `heading_path`, `line_range`, `read_timestamp`, `branch`, `reader`.
- `input_from`: `RetrievalManifest`, Git repo source files.
- `output_to`: `RetrievalGapReport`, `BlockedIfCheck`, `CompletionTruthCheck`.
- `blocked_if_missing`: true.
- `must_not_do`: 不得只用 RAG 摘要、DeepSeek 摘要或旧日志替代原文件回读。
- `gap_status`: `partial`.
- `gap_detail`: 设计文件已有 `github_source_readback_tool` 输入输出，但缺 `task_id / expected_content_hash / current_content_hash / source_of_truth_confirmed` 的标准命名和通过条件。
- `before_sandbox_required`: true.

### 4. RetrievalGapReport

- `contract_role`: 判断检索是否为空、低置信、命中旧源或与仓库回读冲突，并决定是否阻断或触发 DeepSeek。
- `required_fields`: `task_id`, `rag_empty`, `rag_low_confidence`, `source_conflict`, `missing_source_path`, `missing_content_hash`, `legacy_source_hit`, `retrieval_gap_summary`, `blocked_if_unresolved`, `deepseek_trigger_recommended`.
- `optional_fields`: `confidence_score`, `missing_paths`, `conflict_sources`, `recommended_retrieval_queries`.
- `input_from`: `RetrievalManifest`, `SourceReadback`.
- `output_to`: `DeepSeekTriggerDecision`, `BlockedIfCheck`.
- `blocked_if_missing`: true before sandbox.
- `must_not_do`: 不得把 `MISSING_REPORT` 或低置信召回当作执行放行。
- `gap_status`: `missing_schema`.
- `gap_detail`: 当前设计只把 `retrieval_gap_report` 放进流程名，没有字段级 schema。
- `before_sandbox_required`: true.

### 5. DeepSeekTriggerDecision

- `contract_role`: 在 RAG/readback 之后判断是否触发 DeepSeek 只读审查。
- `required_fields`: `task_id`, `deepseek_triggered`, `trigger_reasons`, `not_deepseek_conclusion`, `fallback_status`, `token_usage_observed_or_user_check_required`, `input_package_required`, `allowed_deepseek_roles`, `forbidden_deepseek_actions`.
- `optional_fields`: `input_package_path`, `model_policy`, `expected_output_fields`, `blocked_reason`.
- `input_from`: `RetrievalGapReport`, user explicit request, risk level, source conflict.
- `output_to`: `DeepSeek review node`, `BlockedIfCheck`, `WriteExecutorHandoff`.
- `blocked_if_missing`: true.
- `must_not_do`: 不得把 DeepSeek 当默认文件供应商；不得让 fallback 写成 DeepSeek 结论；不得允许写文件、commit、push、状态推进。
- `gap_status`: `partial`.
- `gap_detail`: DeepSeek trigger policy、input/output contract 已有设计，但缺统一 `DeepSeekTriggerDecision` schema，尤其缺 `deepseek_triggered / fallback_status / token_usage_observed_or_user_check_required / allowed_deepseek_roles / forbidden_deepseek_actions` 的一体化记录。
- `before_sandbox_required`: true.

### 6. BlockedIfCheck

- `contract_role`: 把每个契约和 workflow 的阻断条件转成统一 runtime 可判定结果。
- `required_fields`: `task_id`, `workflow_type`, `blocked`, `blocked_reasons`, `severity`, `blocking_files`, `required_fix_before_continue`, `allowed_fallback`, `human_review_required`.
- `optional_fields`: `blocked_source_contract`, `fallback_loss`, `retry_allowed`, `owner`.
- `input_from`: 8 个上游契约、workflow index、state_action_router.
- `output_to`: `HumanReviewInterrupt`, `WriteExecutorHandoff`, sandbox decision.
- `blocked_if_missing`: true.
- `must_not_do`: 不得用自然语言 blocker 替代结构化阻断；不得允许 fallback 自动当完成。
- `gap_status`: `missing_schema`.
- `gap_detail`: 仓库有大量 `blocked_if` 规则，但没有统一 `BlockedIfCheck` 结果契约。
- `before_sandbox_required`: true.

### 7. HumanReviewInterrupt

- `contract_role`: 在状态推进、sandbox、runtime enablement、来源冲突、写入执行器切换等位置插入人工复审中断。
- `required_fields`: `task_id`, `interrupt_required`, `interrupt_reason`, `reviewer`, `review_question`, `allowed_user_responses`, `resume_condition`, `forbidden_auto_resume`.
- `optional_fields`: `timeout_policy`, `review_artifacts`, `escalation_target`.
- `input_from`: `BlockedIfCheck`, `DeepSeekTriggerDecision`, workflow human review points.
- `output_to`: `WriteExecutorHandoff`, sandbox decision.
- `blocked_if_missing`: true where human review is required.
- `must_not_do`: 不得自动恢复状态推进、sandbox install、GitHub MCP write tool enablement 或非 Codex executor enablement。
- `gap_status`: `missing_schema`.
- `gap_detail`: 设计文件已有 `human_review_point` 和 LangGraph interrupt 概念，但缺标准中断契约字段。
- `before_sandbox_required`: true.

### 8. WriteExecutorHandoff

- `contract_role`: 把 runtime 的只读判断转交给当前激活写入执行器。
- `required_fields`: `handoff_id`, `task_id`, `executor_type`, `active_write_executor`, `allowed_files`, `forbidden_files`, `forbidden_status_fields`, `source_readback`, `retrieval_manifest`, `deepseek_trigger_decision`, `human_review_required`, `exact_changes_requested`, `validation_required`, `git_sync_required`, `remote_readback_required`.
- `optional_fields`: `created_at`, `project_route`, `task_type`, `workflow_type`, `retrieval_gap_report`, `completion_truth_check`, `blocked_if`.
- `input_from`: `WorkflowRouteDecision`, `RetrievalManifest`, `SourceReadback`, `DeepSeekTriggerDecision`, `BlockedIfCheck`, `HumanReviewInterrupt`.
- `output_to`: `active_write_executor`.
- `blocked_if_missing`: true before any write.
- `must_not_do`: 不得让 LangGraph / FastAPI / GitHub MCP / agent-service-toolkit runtime 直接写文件、commit 或 push。
- `gap_status`: `partial`.
- `gap_detail`: `write_executor_abstraction_plan` 已有较完整 handoff schema，但缺用户要求的 `task_id`，且 `forbidden_status_fields / exact_changes_requested / validation_required / git_sync_required / remote_readback_required` 还没有示例 fixture。
- `before_sandbox_required`: true.

### 9. CompletionTruthCheck

- `contract_role`: 判断是否允许声称完成，并防止技术预览、RAG 召回、fallback、local-only 输出冒充完成。
- `required_fields`: `task_id`, `technical_validation`, `content_boundary_check`, `forbidden_status_promotion_check`, `source_readback_ok`, `validation_artifacts`, `remaining_blockers`, `completion_claim_allowed`, `not_allowed_completion_claims`.
- `optional_fields`: `git_sync_status`, `remote_readback_status`, `human_review_status`, `runtime_enabled_check`.
- `input_from`: `WriteExecutorHandoff` result, validation artifacts, repo readback, status scan.
- `output_to`: `latest.md`, final report, sandbox decision.
- `blocked_if_missing`: true.
- `must_not_do`: 不得把技术验证写成内容验证；不得推进 send_ready / voice / visual / publish 状态；不得把本地未 push 当完成。
- `gap_status`: `missing_schema`.
- `gap_detail`: 仓库有 completion_state 表和 completion_truth_check 规则，但没有独立可序列化契约字段。
- `before_sandbox_required`: true.

## contract_required_fields_matrix

| contract | required_fields_complete | critical_gaps | before_sandbox_required | recommendation |
|---|---|---|---|---|
| WorkflowRouteDecision | false | 缺 task_id、职责层、权限和 next step 字段 | true | `schema_draft_needed` |
| RetrievalManifest | false | 缺顶层 manifest schema、provider/model/collection 固定字段 | true | `schema_draft_needed` |
| SourceReadback | false | 缺标准 hash 命名和 source_of_truth_confirmed | true | `schema_draft_needed` |
| RetrievalGapReport | false | 只有流程名，缺字段级 schema | true | `schema_draft_needed` |
| DeepSeekTriggerDecision | false | trigger policy 有，decision record schema 缺 | true | `schema_draft_needed` |
| BlockedIfCheck | false | blocker 散落，缺统一结果契约 | true | `schema_draft_needed` |
| HumanReviewInterrupt | false | human_review_point 有，interrupt schema 缺 | true | `schema_draft_needed` |
| WriteExecutorHandoff | false | handoff schema 接近完整，但缺 task_id 与 fixture | true | `schema_draft_needed` |
| CompletionTruthCheck | false | 规则存在，缺可序列化完成检查契约 | true | `schema_draft_needed` |

## contract_gap_list

| gap_id | contract_name | missing_or_unclear_field | risk_if_unfixed | must_fix_before_sandbox | suggested_fix_level |
|---|---|---|---|---|---|
| GAP-001 | WorkflowRouteDecision | `task_id / project_route / task_type / responsibility_layer / execution_permission / next_steps` 未统一 | runtime 无法稳定路由或阻断 | true | `schema_draft_needed` |
| GAP-002 | RetrievalManifest | `retrieval_provider / embedding_model / vector_collection / vector_result_not_completion_proof` 未成 schema | Chroma/OpenAI 或向量结果被误当正式事实 | true | `schema_draft_needed` |
| GAP-003 | SourceReadback | `source_of_truth_confirmed` 与 hash 字段未标准化 | RAG chunk 可能绕过原文件回读 | true | `schema_draft_needed` |
| GAP-004 | RetrievalGapReport | 缺完整契约 | 无法判断是否触发 DeepSeek 或阻断 | true | `schema_draft_needed` |
| GAP-005 | DeepSeekTriggerDecision | 缺一体化 decision record | DeepSeek 可能被误触发、误跳过或误写成结论 | true | `schema_draft_needed` |
| GAP-006 | BlockedIfCheck | 缺统一 blocker 输出 | runtime 只能读自然语言，无法可靠中止 | true | `schema_draft_needed` |
| GAP-007 | HumanReviewInterrupt | 缺 reviewer / review_question / resume_condition | 人审点可能被自动越过 | true | `schema_draft_needed` |
| GAP-008 | WriteExecutorHandoff | 缺 `task_id` 和 fixture 示例 | handoff 难以追踪任务和验证边界 | true | `schema_draft_needed` |
| GAP-009 | CompletionTruthCheck | 缺独立完成真实性 schema | sandbox 后可能把技术通过、local-only 或 fallback 当完成 | true | `schema_draft_needed` |
| GAP-010 | Cross-contract | 9 个契约缺共同 id / trace 字段规范 | 难以串起一次 runtime 决策链 | true | `schema_draft_needed` |

## blocked_before_sandbox

- `blocked_no_canonical_schema_files`: 9 个契约没有统一 schema 草案。
- `blocked_no_contract_fixtures`: 缺每个契约的 passing / blocked fixture。
- `blocked_no_cross_contract_trace_id`: 缺 `task_id / handoff_id / commit_sha` 的跨契约关联规范。
- `blocked_no_completion_truth_contract`: 完成真实性仍是规则文本，不是 runtime 可消费结构。
- `blocked_no_human_review_interrupt_contract`: 人审中断无法被 LangGraph 安全恢复。

## sandbox_entry_decision

```text
sandbox_entry_allowed_now = false
sandbox_entry_blockers = [
  no_canonical_schema_files,
  no_contract_fixtures,
  no_cross_contract_trace_id,
  no_completion_truth_contract,
  no_human_review_interrupt_contract
]
required_before_sandbox = schema_contract_fix_plan
recommended_next_step = schema_contract_fix_plan
```

## validation_result

- `read_required_files = passed`
- `contracts_checked = 9`
- `code_written = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `runtime_enabled = false`
- `forbidden_status_advanced = false`
