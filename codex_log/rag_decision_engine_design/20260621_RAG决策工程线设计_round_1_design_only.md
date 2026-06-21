# 20260621 RAG 决策工程线设计 Round 1

status: `design_completed_for_user_review`
project_route: `video_factory`
round_scope: `round_1_design_only`
engineering_depth: `L3_system_line`
external_api_called: `false`
dashvector_upsert_called: `false`
current_RAG_index_latest_claim: `false`

## 1. route_decision

```yaml
route_decision:
  project_route: video_factory
  task_type:
    - mechanism_or_route_fix
    - review_diagnosis_audit
    - project_file_change
  responsibility_layer:
    - project_judgment_layer
    - mechanism_fix_layer
    - validation_layer
    - sync_layer
  engineering_depth: L3_system_line
  round_scope: round_1_design_only
  workflow_route_decision: mechanism_repair_flow
  state_action_router:
    current_state: vector_sync_blocked_with_clear_reason
    selected_action: design_incremental_sync_plus_authority_overlay_before_round_2
    forbidden_status_promotion:
      - content_validation
      - send_ready
      - production_readiness
  large_task_gate:
    triggered: true
    lane_recommendation: audit_lane
    parallel_recommendation: serial_only
    write_owner: Codex integrator only
  supply_source_arbitration:
    retrieval_manifest: no_live_vector_retrieval_this_round
    source_readback_status: repo_files_readback_used
    deepseek_trigger_decision: not_triggered
    not_deepseek_conclusion: true
```

## 2. read_proof_report

```yaml
read_proof_report:
  files_read:
    - path: AGENTS.md
      status: read_ok
      key_findings:
        - video_factory route matched
        - route_decision_gate and large_task_gate required before write
        - mandatory_commit_push_gate active if files change
    - path: codex_log/latest.md
      status: read_ok
      key_findings:
        - latest RAG sync retry is vector_sync_blocked_with_clear_reason
        - changed_indexable_file_count is 23
        - latest_chunk_manifest_chunk_count is 5657
        - existing_index_manifest_indexed_chunk_count is 5597
        - current_RAG_index_latest_claim is false
    - path: codex_source/00_codex_readme.md
      status: read_ok
      key_findings:
        - Vector RAG / DashVector is retrieval cache, not formal fact
        - source readback and DeepSeek trigger decision are required before high-risk writes
    - path: codex_source/01_execution_rules.md
      status: read_ok
      key_findings:
        - RAG cleaning layer gate requires authority/stale/conflict/readback fields
        - completed requires Git sync and vector sync boundary
        - L3 tasks require node contracts, schema, evaluator, failure route, checkpoint, trace
    - path: GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md
      status: read_ok
      key_findings:
        - this task is L3_system_line
        - per-file plan, failure route, trace, schema, validator and fixture are required
    - path: GPT数据源/11_项目状态动作总控器_机制推理层.md
      status: read_ok
      key_findings:
        - RAG/source_readback tasks trigger supply_source_arbitration
        - stale index and source conflict route to RAG_sync_bus or fact_source_arbitration
    - path: codex_source/19_project_state_action_router.md
      status: read_ok
      key_findings:
        - rag_engineering_line_required forbids schema-only landing
        - post_commit_vector_sync_gate_required must block, not claim current, if sync fails
    - path: scripts/post_commit_vector_sync_gate.py
      status: read_ok
      key_findings:
        - check mode detects changed/deleted indexable files by git diff
        - sync/finish always runs inventory, chunking, rag_dashvector_sync, retrieval probe, validators
    - path: scripts/rag_dashvector_sync.py
      status: read_ok
      key_findings:
        - current execution embeds and upserts common.chunks_from_manifest(chunk_manifest)
        - no old index_manifest vs new chunk_manifest delta comparison
        - no checkpoint/resume cursor or partial manifest
    - path: scripts/rag_common.py
      status: read_ok
      key_findings:
        - chunk_id is source_path + line_start + line_end + chunk_hash based
        - DashVector docs store metadata, no content body
        - retrieval source readback can verify chunk_hash and file_hash
    - path: scripts/rag_build_source_inventory.py
      status: read_ok
      key_findings:
        - source inventory is full-corpus allowlist/denylist/secret scan
    - path: scripts/rag_chunk_project_sources.py
      status: read_ok
      key_findings:
        - chunk manifest is rebuilt from full source inventory
    - path: scripts/rag_supply_pack_builder.py
      status: read_ok
      key_findings:
        - has lightweight source classifier and cleaning fields
        - current candidate selection is simple lexical scoring, not weighted decision
    - path: scripts/rag_mid_task_supply_builder.py
      status: read_ok
      key_findings:
        - builds mid-task snippets and blocks if readback/can_feed/conflict fail
    - path: scripts/rag_supply_pack_validator.py
      status: read_ok
      key_findings:
        - blocks stale/low authority sources from feeding Codex
        - requires conflict_points for high-risk packs
    - path: scripts/rag_failure_route_resolver.py
      status: read_ok
      key_findings:
        - routes stale_index to RAG_sync_bus and source_conflict to fact_source_arbitration
    - path: codex_source/24_RAG清洗层执行契约_rag_cleaning_layer_execution_contract.md
      status: read_ok
      key_findings:
        - defines source_authority, stale_context, conflict, decision authority, supply cleaner, completion cleaner
    - path: codex_source/schema_contracts/schemas/rag_supply_pack.schema.yaml
      status: read_ok
      key_findings:
        - supply pack requires exact_snippet_pack and cleaning_layer_check
    - path: codex_source/schema_contracts/schemas/pre_supply_pack.schema.yaml
      status: read_ok
      key_findings:
        - pre-supply pack requires source_path, line_range, chunk_id, readback
    - path: codex_source/schema_contracts/schemas/mid_task_supply_pack.schema.yaml
      status: read_ok
      key_findings:
        - continue_allowed false blocks mid-task continuation
    - path: codex_source/schema_contracts/schemas/rag_cleaning_layer.schema.yaml
      status: read_ok
      key_findings:
        - current schema lacks conflict_group_registry and weighted decision fields
    - path: codex_log/rag_vector_sync/latest_vector_sync_gate_report.json
      status: read_ok
      key_findings:
        - gate status is blocked
        - changed_count is 23
        - failed stage is rag_dashvector_sync external sync timeout
    - path: codex_log/rag_vector_sync/latest_vector_sync_gate_report.md
      status: read_ok
      key_findings:
        - final index manifest was not written for source commit a5b8e668...
        - retrieval probe did not run for current source commit
    - path: codex_log/rag_vector_sync/latest_source_inventory.json
      status: read_ok
      key_findings:
        - current commit is a5b8e668...
        - allowed_file_count is 881
        - secret_scan_passed is true
    - path: codex_log/rag_vector_sync/latest_chunk_manifest.json
      status: read_ok
      key_findings:
        - current chunk_count is 5657
        - chunk_manifest_valid is true
    - path: codex_log/rag_vector_sync/latest_index_manifest.json
      status: read_ok
      key_findings:
        - indexed source commit is still 44b25ce9...
        - indexed_chunk_count is 5597
        - blocked is false for the old index, but stale for current worktree
    - path: codex_log/rag_cleaning_layer/vector_sync_blocked_20260621.json
      status: read_ok
      key_findings:
        - records vector_sync_blocked
        - source_commit_sha differs from latest gate report and must be reconciled in round 2 logs
  missing_files: []
  conflict_or_uncertain_files:
    - path: codex_log/rag_cleaning_layer/vector_sync_blocked_20260621.json
      issue: source_commit_sha is 8804852a..., while latest_vector_sync_gate_report uses a5b8e668...
    - path: codex_log/rag_vector_sync/latest_index_manifest.json
      issue: valid for old source commit 44b25ce9..., not current source commit a5b8e668...
```

## 3. current_state_audit

```yaml
current_state_audit:
  true_incremental_sync_status: partial_only_detection_layer_incremental_execution_layer_full_corpus
  old_context_control_status: partial_cleaning_fields_exist_but_no_central_overlay_or_conflict_registry
  authority_overlay_status: missing_as_formal_overlay
  conflict_group_status: missing
  weighted_decision_status: missing
  checkpoint_resume_status: missing
  main_gaps:
    - file_delta_detection exists, chunk_delta_execution does not
    - full chunk_manifest rebuild is acceptable, but full embedding/upsert is not
    - current retrieval filter is commit-bound and conflicts with delta-only reuse
    - old vectors can remain in DashVector unless retrieval cleaning filters by active manifest
    - supply pack has cleaning fields but lacks group winner, hard gate, score breakdown and audit report
```

Evidence:

- `post_commit_vector_sync_gate.py` detects changed/deleted indexable files with `git diff previous_index_commit current_commit`.
- `rag_dashvector_sync.py` calls `common.chunks_from_manifest(chunk_manifest)` and then `upsert_chunks(chunks, batch_size)`, so it embeds/upserts the entire manifest.
- Current old/new manifest comparison by `chunk_id`:
  - old chunk count: `5597`
  - new chunk count: `5657`
  - unchanged by chunk_id: `5161`
  - new or changed by chunk_id: `496`
  - old missing from new by chunk_id: `436`
- Therefore only about `496` new/changed chunks appear to require embedding under a first-pass chunk-id delta design, not all `5657`.

## 4. proposed_engineering_line

```text
changed_file_detection
-> source_inventory_delta
-> chunk_delta_manifest
-> embedding_delta_upsert
-> tombstone_or_supersede_old_chunks
-> authority_overlay
-> conflict_group_registry
-> retrieval_cleaning_pipeline
-> hard_gate_check
-> weighted_decision_engine
-> decision_audit_report
-> codex_supply_pack
```

### node_contracts

```yaml
nodes:
  - node_name: changed_file_detection
    purpose: Detect changed/deleted indexable files since latest indexed source boundary.
    input: [latest_index_manifest, git HEAD, allowlist, denylist]
    output: changed_indexable_files, deleted_indexable_files, sync_required
    core_decisions: file-level sync necessity
    blocked_if: previous_index_commit_missing_or_git_diff_failed
    validation: unit fixture with changed/deleted/dynamic-audit-only cases
    failure_route: RAG_sync_bus

  - node_name: source_inventory_delta
    purpose: Build full current source inventory plus delta file classification.
    input: [latest_source_inventory, new_source_inventory, changed_indexable_files]
    output: full_source_inventory, source_inventory_delta
    core_decisions: new_files, changed_files, deleted_files, unchanged_files
    blocked_if: secret_scan_failed_or_allowlist_failed
    validation: source_inventory_delta fixture
    failure_route: validation_repair

  - node_name: chunk_delta_manifest
    purpose: Compare old index chunks and new chunk manifest to classify chunk state.
    input: [latest_index_manifest, latest_chunk_manifest]
    output: chunk_delta_manifest
    core_decisions: new_chunks, changed_chunks, unchanged_chunks, deleted_chunks, superseded_chunks
    blocked_if: required_chunk_metadata_missing
    validation: old/new manifest fixture with rename, edit, delete and unchanged cases
    failure_route: RAG_sync_bus

  - node_name: embedding_delta_upsert
    purpose: Call embedding/upsert only for delta chunks after preconditions pass.
    input: [chunk_delta_manifest.delta_chunks, source_readback]
    output: delta_upsert_report, partial_checkpoint
    core_decisions: batch slicing, retry, skip unchanged chunks
    blocked_if: auth_missing_or_preconditions_failed_or_external_timeout
    validation: dry-run and fake-client fixture before real API
    failure_route: RAG_sync_bus

  - node_name: tombstone_or_supersede_old_chunks
    purpose: Prevent deleted/superseded old chunks from feeding Codex.
    input: [deleted_chunks, superseded_chunks, DashVector capability probe]
    output: tombstone_plan, active_chunk_allowlist
    core_decisions: delete vs tombstone vs overlay supersede
    blocked_if: destructive_delete_unproven_or_unauthorized
    validation: retrieval post-filter excludes superseded old chunks
    failure_route: fact_source_arbitration

  - node_name: authority_overlay
    purpose: Attach authority/stale/conflict/feed/completion flags to chunks and snippets.
    input: [current fact rules, manifests, source paths, conflict registry]
    output: rag_authority_overlay
    core_decisions: authority_level, stale_status, can_feed_codex, hard_gate_flags
    blocked_if: source_path_unclassifiable_for_execution
    validation: schema and authority fixture
    failure_route: fact_source_arbitration

  - node_name: conflict_group_registry
    purpose: Group competing claims and select a current winner or block.
    input: [authority_overlay, current formal facts, latest logs, target plans, user instruction]
    output: conflict_group_registry
    core_decisions: current_winner, losers, pending_conflict
    blocked_if: no_winner_for_required_execution_fact
    validation: five conflict fixtures
    failure_route: human_decision_gate_or_fact_source_arbitration

  - node_name: retrieval_cleaning_pipeline
    purpose: Clean retrieved docs before they become supply.
    input: [DashVector query results, active_chunk_allowlist, authority_overlay, current manifest]
    output: cleaned_candidates
    core_decisions: reject stale/superseded/low-authority/conflicted candidates
    blocked_if: no_clean_candidate_for_execution
    validation: retrieval fixture with stale docs crowding top-k
    failure_route: RAG_supply_bus

  - node_name: hard_gate_check
    purpose: Apply one-vote veto before any score-based decision.
    input: [cleaned_candidates, task_context, conflict groups]
    output: hard_gate_result
    core_decisions: block or pass to weighted engine
    blocked_if: any hard gate fails
    validation: hard gate fixture matrix
    failure_route: selected by failed gate

  - node_name: weighted_decision_engine
    purpose: Rank candidates/actions only after hard gates pass.
    input: [task_type_weight_profile, cleaned_candidates, candidate_actions]
    output: weighted_score_breakdown, selected_action
    core_decisions: task-specific weights, penalties, boosts
    blocked_if: all_candidates_below_threshold_or_profile_missing
    validation: deterministic scoring fixture
    failure_route: chatgpt_review_or_human_decision_gate

  - node_name: decision_audit_report
    purpose: Explain why Codex selected one action and rejected alternatives.
    input: [task_context, retrieved, cleaned, hard_gate, weights, selected_action]
    output: decision_audit_report
    core_decisions: user-readable rationale and blocked conditions
    blocked_if: selected_action_missing_reason
    validation: report schema and golden fixture
    failure_route: completion_truth_check

  - node_name: codex_supply_pack
    purpose: Emit pre/mid/post supply packs with exact readback and decision audit reference.
    input: [decision_audit_report, cleaned_candidates, authority_overlay]
    output: pre_supply_pack, mid_task_supply_pack, post_risk_review_pack
    core_decisions: can_feed_codex, can_claim_completed
    blocked_if: readback_missing_or_supply_claims_completed
    validation: existing plus upgraded supply validators
    failure_route: RAG_supply_bus
```

## 5. true_incremental_sync_design

```yaml
true_incremental_sync_design:
  delta_detection_rule:
    compare:
      old: latest_index_manifest.chunks
      new: latest_chunk_manifest.chunks
    primary_identity: chunk_id
    secondary_identity:
      - source_path
      - line_range
      - chunk_hash
      - file_hash
    round_2_addition:
      - logical_chunk_key: source_path + stable_section_anchor + chunk_ordinal
      - vector_doc_commit_sha: commit that originally wrote this DashVector doc
      - active_source_commit_sha: current full source commit represented by final manifest

  chunk_classes:
    new_chunks: new chunk_id not in old and no overlapping old chunk
    changed_chunks: new chunk_id not in old but overlaps old source_path/line_range or logical_chunk_key
    unchanged_chunks: new chunk_id in old with same chunk_hash/file_hash
    deleted_chunks: old source_path deleted or old chunk has no new successor
    superseded_chunks: old chunk replaced by changed chunk in same source/logical range

  changed_chunk_policy:
    - embed and upsert only new_chunks + changed_chunks
    - write supersedes old chunk ids in delta manifest
    - require source readback before embedding

  deleted_chunk_policy:
    default: overlay_superseded
    reason: DashVector delete/metadata update behavior has not been validated in this round
    round_2_probe:
      - validate DashVector delete docs API or metadata update API in isolated fake/client dry-run first
      - only enable physical delete after explicit fixture and live probe pass

  unchanged_chunk_policy:
    - do not call embedding API
    - do not call DashVector upsert for vectors
    - carry old vector_doc_commit_sha and chunk_id into final full manifest
    - mark vector_state: reused_from_previous_index

  manifest_write_policy:
    final_index_manifest:
      source_commit_sha: current full source commit
      indexed_chunk_count: current full active chunk count
      chunks: all current active chunks
      per_chunk_fields:
        - chunk_id
        - source_path
        - line_range
        - chunk_hash
        - file_hash
        - active_source_commit_sha
        - vector_doc_commit_sha
        - vector_state
        - supersedes
      sync_operation_summary:
        - unchanged_chunk_count
        - embedded_delta_chunk_count
        - upserted_delta_chunk_count
        - deleted_or_superseded_chunk_count
        - api_call_boundary

  retrieval_filter_policy:
    current_problem: existing retrieval_probe filters DashVector docs by commit_sha == source_commit_sha
    issue: delta sync reuses old docs whose DashVector metadata still has old commit_sha
    round_2_change:
      - query by project_route/repo_full_name and maybe topk expansion
      - post-filter using final_index_manifest active chunk_id + chunk_hash + authority overlay
      - reject any doc not in active_chunk_allowlist
      - do not treat DashVector commit filter as the only freshness guarantee

  checkpoint_resume_policy:
    checkpoint_file: codex_log/rag_vector_sync/latest_delta_sync_checkpoint.json
    partial_manifest_file: codex_log/rag_vector_sync/latest_delta_index_partial_manifest.json
    checkpoint_fields:
      - run_id
      - source_commit_sha
      - previous_index_commit_sha
      - delta_manifest_hash
      - batch_size
      - completed_batch_indexes
      - completed_chunk_ids
      - failed_batch_indexes
      - resume_cursor
      - external_call_report
    resume_rule:
      - refuse resume if source_commit_sha or delta_manifest_hash changed
      - skip completed chunk_ids
      - retry failed batches with smaller batch size
      - write final full manifest only after all delta batches succeed

  external_api_call_boundary:
    no_api_in_round_1: true
    round_2_api_calls:
      - embedding only for delta chunks
      - DashVector upsert only for delta docs
      - DashVector query only for retrieval probe after final manifest
```

Validation cases:

1. One unchanged file: `unchanged_chunks = all`, `embedding_called = false`.
2. One line edit inside one file: only affected chunks embed/upsert.
3. New file added: only that file's chunks embed/upsert.
4. File deleted: old chunks are superseded/tombstoned, no embedding.
5. Interrupted after batch N: resume starts at N+1 and final manifest is not written early.
6. Existing stale old docs appear in retrieval: post-filter rejects them if not in active manifest.

## 6. rag_authority_overlay_design

```yaml
rag_authority_overlay_fields:
  chunk_id: string
  source_path: string
  line_range: string
  source_commit_sha: string
  vector_doc_commit_sha: string
  authority_level: enum
  stale_status: enum
  conflict_status: enum
  conflict_group_id: string|null
  superseded_by: string|null
  retrieval_role: enum
  default_weight: number
  can_feed_codex: boolean
  can_claim_completed: boolean
  readback_required: boolean
  hard_gate_flags: list[string]

authority_level:
  current_formal_fact: highest project fact source, e.g. GPT数据源/08, AGENTS.md route facts
  latest_log: codex_log/latest.md and current dated logs
  execution_rule: codex_source execution/router/rule files and scripts
  mechanism_contract: RAG cleaning and decision contracts
  target_state_plan: GPT数据源/09 or future plan documents
  historical_log: old dated logs and previous reports
  external_reference: external/non-repo source
  archive_only: archive/quarantine/historical-only source

stale_status:
  current: active current source
  superseded: replaced by newer source/chunk
  stale_but_reference_allowed: old but allowed for context only
  legacy_alias: historical compatibility pointer
  target_state_only: desired future state, not current fact
  conflict_pending: not safe until conflict group resolved

retrieval_role:
  decision_source: can shape current decision after readback
  execution_constraint: hard constraint for Codex execution
  risk_context: risk/background signal
  history_context: history only
  blocked_context: retrieved but blocked from feeding execution
```

Default mapping:

- `GPT数据源/`, `AGENTS.md`, current `codex_source/` rules -> `current_formal_fact`, `execution_constraint`, high weight.
- `codex_log/latest.md` -> `latest_log`, useful for status but cannot override formal fact rules.
- `codex_log/rag_vector_sync/**` -> dynamic sync evidence, not indexed formal corpus.
- `review_loop/**` -> `latest_log` or `historical_log` depending record date and current target.
- `归档*`, `old_context`, `GPT 数据源/` with space -> `archive_only` or `historical_log`, default `can_feed_codex=false` for execution.

## 7. conflict_group_registry_design

```yaml
conflict_group_registry_design:
  group_id_rule: "cfg_" + normalized_topic + "_" + sha256(sorted(candidate_claim_keys))[0:12]
  candidate_fields:
    - claim_id
    - claim_text
    - source_path
    - line_range
    - authority_level
    - stale_status
    - source_commit_sha
    - user_instruction_scope
    - evidence_strength
    - can_be_current_winner
  winner_selection_rule:
    - hard gate first
    - current_formal_fact beats latest_log
    - latest_log beats historical_log
    - explicit current-turn user instruction can override for this task only
    - target_state_plan cannot beat current_formal_fact unless accepted and written back
  loser_policy:
    - keep for audit
    - mark stale_status as superseded or stale_but_reference_allowed
    - can_feed_codex false unless retrieval_role is history_context/risk_context
  pending_conflict_policy:
    - if required for execution, block with conflict_pending
    - if only explanatory, allow with notice and readback
  user_instruction_override_policy:
    - current turn user instruction can set temporary winner
    - permanent winner requires repo writeback to formal fact/log layer
```

Examples:

```yaml
examples:
  voice_provider_conflict:
    group_id: cfg_voice_route_formal_provider
    candidates: [old_qwen_reference_anchor, minimax_formal_voice]
    current_winner: minimax_formal_voice
    loser_policy: old_qwen_reference_anchor_only

  aspect_ratio_conflict:
    group_id: cfg_video_delivery_aspect_ratio
    candidates: [vertical_9_16_historical, horizontal_16_9_formal_operation]
    current_winner: horizontal_16_9_formal_operation
    loser_policy: vertical_9_16_historical_context

  deepseek_supply_conflict:
    group_id: cfg_deepseek_supply_default
    candidates: [deepseek_default_supplier_old, deepseek_conditionally_triggered_current]
    current_winner: deepseek_conditionally_triggered_current
    loser_policy: old_default_supplier_superseded

  technical_preview_vs_publish_candidate:
    group_id: cfg_delivery_baseline
    candidates: [technical_preview_internal, publish_candidate_or_blocked]
    current_winner: publish_candidate_or_blocked
    loser_policy: technical_preview_internal_diagnostic_only

  formal_fact_vs_target_plan:
    group_id: cfg_current_fact_vs_target_state
    candidates: [current_formal_fact, target_state_plan]
    current_winner: current_formal_fact
    loser_policy: target_state_only_until_written_back
```

## 8. hard_gate_and_weighted_decision_design

Hard gates run before scoring.

```yaml
hard_gate:
  secret_or_token_detected:
    blocked_if: source_inventory.secret_scan_passed != true
    failure_route: validation_repair
  source_readback_missing:
    blocked_if: execution task has candidate without source_path/line_range/chunk_id/readback
    failure_route: RAG_supply_bus
  current_formal_fact_conflict:
    blocked_if: conflict group has no current_winner for required fact
    failure_route: fact_source_arbitration
  user_must_decide_required:
    blocked_if: decision_owner = user_must_decide and no decision
    failure_route: human_decision_gate
  technical_validation_misused_as_content_validation:
    blocked_if: any candidate promotes technical_validation to content_validation
    failure_route: completion_truth_check
  fallback_without_authorization:
    blocked_if: fallback/degradation selected without explicit authorization
    failure_route: human_decision_gate
  stale_index_for_high_risk_task:
    blocked_if: task_risk = high and vector_sync_status in [stale, blocked] and no repo readback alternative
    failure_route: RAG_sync_bus
```

Weight profiles:

```yaml
task_type_weight_profile:
  mechanism_repair:
    - source_type: current_formal_fact
      base_weight: 1.00
      boost_if: source is AGENTS/GPT数据源/codex_source current contract
      penalty_if: source is latest summary only
      forbidden_if: source is archive_only claiming current
      reason: mechanism edits must follow formal contracts
    - source_type: latest_log
      base_weight: 0.82
      boost_if: dated current blocker evidence
      penalty_if: counts conflict with manifest
      forbidden_if: promotes status
      reason: latest explains state, but manifest proves sync

  code_execution:
    - source_type: execution_rule
      base_weight: 1.00
      boost_if: script and validator agree
      penalty_if: no fixture
      forbidden_if: secret/API needed but forbidden
      reason: code changes need executable contract and tests

  rag_supply:
    - source_type: decision_source
      base_weight: 0.90
      boost_if: readback_hash_match and active manifest allowlisted
      penalty_if: stale_index notice
      forbidden_if: missing readback
      reason: retrieval is useful only after source verification

  codex_prompt_generation:
    - source_type: current_formal_fact
      base_weight: 0.95
      boost_if: includes route_decision and blocked_if
      penalty_if: lacks file-level plan
      forbidden_if: asks Codex to promote forbidden status
      reason: prompt should encode current contracts

  video_execution:
    - source_type: execution_constraint
      base_weight: 1.00
      boost_if: locked copy and line-level mapping present
      penalty_if: only technical preview
      forbidden_if: publish baseline missing
      reason: video execution is high-risk user-visible delivery

  operation_review:
    - source_type: latest_log
      base_weight: 0.90
      boost_if: record has time window and screenshot evidence
      penalty_if: missing video_id/time window
      forbidden_if: mixes 24h/72h/7d windows
      reason: operation review depends on actual records

  historical_audit:
    - source_type: historical_log
      base_weight: 0.75
      boost_if: used only to explain why changed
      penalty_if: tries to decide current action
      forbidden_if: overrides current formal fact
      reason: history is context, not current default
```

## 9. stale_index_policy_design

```yaml
stale_index_policy:
  low_risk_task:
    allowed: true
    required_notice: true
    readback_required: false for explanation, true for any factual claim
    examples:
      - explaining historical mechanism
      - listing likely files to inspect

  medium_risk_task:
    allowed: conditional
    readback_required: true
    authority_overlay_required: true
    examples:
      - drafting a Codex task prompt
      - preparing design-only plan
    blocked_if:
      - no source readback for selected facts
      - conflict group unresolved for selected action

  high_risk_task:
    allowed: false_for_execution_facts
    blocked_if:
      - vector_sync_status in [stale, blocked]
      - no repo readback can replace stale retrieval
      - task would write code/status/video based on stale retrieval only
    required_fix:
      - run true incremental sync if authorized
      - or bypass RAG and read repo source files directly
      - or block for user/human decision if facts conflict
```

This policy prevents two bad extremes:

- RAG stale does not freeze simple explanation or design work.
- RAG stale cannot feed high-risk execution, completion claims, status promotion or media delivery.

## 10. checkpoint_resume_design

```yaml
checkpoint_resume_design:
  run_id: timestamp + source_commit_sha_short + delta_manifest_hash_short
  checkpoint_path: codex_log/rag_vector_sync/latest_delta_sync_checkpoint.json
  partial_manifest_path: codex_log/rag_vector_sync/latest_delta_index_partial_manifest.json
  batch_checkpoint_fields:
    - batch_index
    - chunk_ids
    - source_paths
    - started_at
    - finished_at
    - status
    - attempts
    - embedding_called
    - upsert_called
    - request_id_present
  resume_cursor:
    - next_batch_index
    - completed_chunk_ids
    - failed_chunk_ids
  retry_policy:
    - retry batch up to 3 times
    - split failed batch in half
    - if single chunk fails, mark blocked_single_chunk with source_path and line_range
  finalization_rule:
    - final index_manifest is written only after all delta batches pass
    - failed/interrupted runs write partial manifest and blocked report only
```

## 11. decision_audit_report_design

```yaml
decision_audit_report_fields:
  task_context:
    - task_id
    - project_route
    - task_type
    - risk_level
    - source_commit_sha
    - vector_sync_status
  retrieved_candidates:
    - candidate_id
    - source_path
    - line_range
    - chunk_id
    - raw_score
  readback_status:
    - readback_hash_match
    - file_hash_match
    - source_readback_required
  cleaned_candidates:
    - authority_level
    - stale_status
    - conflict_status
    - conflict_group_id
    - can_feed_codex
  conflict_groups_checked:
    - group_id
    - current_winner
    - pending
  hard_gate_result:
    - passed
    - failed_gates
    - failure_route
  weighted_score_breakdown:
    - candidate_id
    - base_weight
    - boosts
    - penalties
    - final_score
  candidate_actions:
    - action_id
    - required_files
    - risks
  selected_action: string
  why_selected: string
  why_not_others: list
  blocked_if: list
  user_review_required: boolean
```

Example:

```yaml
example_case:
  question: 当前应继续全量同步、只修增量同步，还是修增量同步 + 权威覆盖层？
  selected_action: fix_incremental_sync_plus_authority_overlay
  reason:
    - 只修增量同步能解决速度，但不能解决旧口径污染
    - 只修权威覆盖层能解决污染，但不能解决 5657 chunk 全量 embedding/upsert 超时
    - 当前阻断同时来自同步慢和索引/供料判断边界不足
  why_not_others:
    continue_full_sync_now: repeats the 30-40 minute timeout risk
    fix_incremental_only: stale old docs can still be retrieved without overlay
    fix_overlay_only: current sync remains slow and interrupted
  user_review_required: true
```

## 12. file_level_landing_blueprint

```yaml
file_level_landing_blueprint:
  - path: codex_source/25_RAG决策工程线执行契约_rag_decision_engine_execution_contract.md
    change_type: create
    purpose: Contract for true incremental sync, authority overlay, conflict groups, hard gates and weighted decisions.
    layer: mechanism_contract
    inputs: [latest_index_manifest, latest_chunk_manifest, rag_cleaning_layer_contract]
    outputs: [node_contracts, blocked_if, completion boundary]
    core_decisions: what is current, stale, blocked, winner, selected action
    schemas_needed: all schemas below
    validators_needed: contract completeness validator
    fixtures_needed: five conflict examples plus delta examples
    reports_generated: decision audit report
    blocked_if: missing node/schema/validator/fixture/failure route
    validation: markdown contract lint + fixture references
    user_review_points: conflict winner policy and stale index policy

  - path: codex_source/schema_contracts/schemas/true_incremental_vector_sync.schema.yaml
    change_type: create
    purpose: Delta manifest, checkpoint and final manifest contract.
    layer: schema
    inputs: [old index manifest, new chunk manifest]
    outputs: [chunk_delta_manifest, checkpoint]
    validators_needed: rag_vector_delta_manifest_validator.py
    fixtures_needed: unchanged/edit/add/delete/interrupted cases
    validation: schema fixture validation

  - path: codex_source/schema_contracts/schemas/rag_authority_overlay.schema.yaml
    change_type: create
    purpose: Authority/stale/conflict/feed/completion fields.
    layer: schema
    inputs: [source_path rules, current facts, conflict registry]
    outputs: [authority overlay records]
    validators_needed: rag_authority_overlay_validator.py
    fixtures_needed: current, archive, target-only, conflict-pending cases

  - path: codex_source/schema_contracts/schemas/conflict_group_registry.schema.yaml
    change_type: create
    purpose: Conflict group candidates, winners, losers, pending rules.
    layer: schema
    inputs: [authority overlay, formal facts, latest logs]
    outputs: [current_winner, loser_policy]
    validators_needed: rag_conflict_group_registry_validator.py
    fixtures_needed: five required conflict examples

  - path: codex_source/schema_contracts/schemas/weighted_decision_engine.schema.yaml
    change_type: create
    purpose: Task type weight profiles and scoring breakdown.
    layer: schema
    inputs: [cleaned candidates, hard gate result]
    outputs: [weighted_score_breakdown, selected_action]
    validators_needed: rag_weighted_decision_validator.py
    fixtures_needed: task profile golden fixtures

  - path: codex_source/schema_contracts/schemas/decision_audit_report.schema.yaml
    change_type: create
    purpose: User-readable decision explanation contract.
    layer: schema
    inputs: [retrieval, readback, hard gates, weights]
    outputs: [decision_audit_report]
    validators_needed: rag_decision_audit_report_validator.py
    fixtures_needed: current blocked sync scenario

  - path: scripts/rag_vector_delta_planner.py
    change_type: create
    purpose: Compare old index and new chunk manifest; no external API.
    layer: runner/helper
    inputs: [latest_index_manifest.json, latest_chunk_manifest.json]
    outputs: [latest_chunk_delta_manifest.json]
    core_decisions: chunk class assignment
    validation: py_compile + fixtures

  - path: scripts/rag_dashvector_sync.py
    change_type: update
    purpose: Add --delta-manifest, --resume and --dry-run-delta while preserving current full sync behind explicit flag.
    layer: runner
    inputs: [chunk_delta_manifest, checkpoint]
    outputs: [final index manifest, checkpoint, delta upsert report]
    core_decisions: only embed/upsert delta chunks
    blocked_if: source_commit changed during resume
    validation: fake client dry-run before live API

  - path: scripts/post_commit_vector_sync_gate.py
    change_type: update
    purpose: Insert delta planner before sync and write blocked reports with unified source_commit.
    layer: integration_hook
    inputs: [change detection, delta planner]
    outputs: [gate report with delta counts]
    validation: check mode remains no-network

  - path: scripts/rag_authority_overlay_builder.py
    change_type: create
    purpose: Build overlay from active manifest and source rules.
    layer: cleaning_layer
    outputs: [latest_rag_authority_overlay.json]
    validation: overlay validator fixtures

  - path: scripts/rag_conflict_group_registry_builder.py
    change_type: create
    purpose: Build conflict registry and pick winners or pending blocks.
    layer: decision_layer
    outputs: [latest_conflict_group_registry.json]
    validation: five conflict fixtures

  - path: scripts/rag_weighted_decision_engine.py
    change_type: create
    purpose: Apply hard gates, then score actions/candidates.
    layer: decision_layer
    outputs: [latest_decision_audit_report.json]
    validation: deterministic scoring tests

  - path: scripts/rag_supply_pack_builder.py
    change_type: update
    purpose: Consume authority overlay/conflict registry/decision audit.
    layer: supply_bus
    outputs: [pre/mid/post packs with conflict_group_id and audit_report_id]
    validation: existing validator plus upgraded fields

  - path: scripts/rag_supply_pack_validator.py
    change_type: update
    purpose: Block missing conflict groups, hard-gate failures and stale high-risk supply.
    layer: validator
    validation: passing and blocked fixtures

  - path: scripts/rag_retrieval_probe.py
    change_type: update
    purpose: Replace commit-only freshness filter with active manifest allowlist post-filter.
    layer: integration_hook
    blocked_if: active manifest missing
    validation: fake retrieval fixture with stale docs

  - path: scripts/rag_failure_route_resolver.py
    change_type: update
    purpose: Add routes for hard_gate_failed, conflict_group_pending, weighted_score_below_threshold, checkpoint_resume_failed.
    layer: failure_route

  - path: codex_source/fixtures/rag_decision_engine/
    change_type: create
    purpose: Store delta, overlay, conflict, hard gate, weighted decision and audit fixtures.
    layer: fixture

  - path: codex_log/rag_decision_engine/
    change_type: create
    purpose: Store latest and dated decision reports, trace and validation outputs.
    layer: report_trace

  - path: codex_log/latest.md
    change_type: update
    purpose: Record round_2 pending status without claiming implementation or latest RAG.
    layer: latest_log
```

## 13. round_2_goal_mode_execution_map

```yaml
round_2_goal_mode_execution_map:
  goal: Implement true incremental vector sync plus RAG authority overlay/conflict group/hard gate/weighted decision/audit report pipeline.
  required_files_to_modify:
    - scripts/rag_dashvector_sync.py
    - scripts/post_commit_vector_sync_gate.py
    - scripts/rag_supply_pack_builder.py
    - scripts/rag_supply_pack_validator.py
    - scripts/rag_mid_task_supply_builder.py
    - scripts/rag_failure_route_resolver.py
    - scripts/rag_retrieval_probe.py
    - codex_source/00_codex_readme.md
    - codex_source/01_execution_rules.md
    - codex_source/19_project_state_action_router.md
    - codex_log/latest.md
  required_files_to_create:
    - codex_source/25_RAG决策工程线执行契约_rag_decision_engine_execution_contract.md
    - codex_source/schema_contracts/schemas/true_incremental_vector_sync.schema.yaml
    - codex_source/schema_contracts/schemas/rag_authority_overlay.schema.yaml
    - codex_source/schema_contracts/schemas/conflict_group_registry.schema.yaml
    - codex_source/schema_contracts/schemas/weighted_decision_engine.schema.yaml
    - codex_source/schema_contracts/schemas/decision_audit_report.schema.yaml
    - scripts/rag_vector_delta_planner.py
    - scripts/rag_authority_overlay_builder.py
    - scripts/rag_conflict_group_registry_builder.py
    - scripts/rag_weighted_decision_engine.py
    - scripts/rag_decision_audit_report_validator.py
    - codex_source/fixtures/rag_decision_engine/*.json
    - codex_log/rag_decision_engine/*.json
    - codex_log/rag_decision_engine/*.md
  forbidden_files:
    - .env
    - .env.*
    - secret/token/key files
    - dist/latest_review_pack/**
    - media/audio/video/image binaries
  execution_order:
    - lock current behavior with fixtures for current full-sync blocked scenario
    - implement delta planner and validator without external API
    - implement checkpoint/resume dry-run
    - implement authority overlay and conflict registry
    - implement hard gates and weighted decision engine
    - integrate supply pack builder/validator
    - update retrieval probe active-manifest post-filter
    - only after dry-run validation, run controlled delta sync if authorized by existing gate
    - update latest, stage path-limited, secret scan, commit, push, remote readback
  validation_order:
    - py_compile changed scripts
    - schema fixture validators
    - delta planner fixtures
    - dry-run delta sync with fake client
    - supply pack validator
    - failure route resolver fixtures
    - no external API validation for dry-run path
    - optional real post_commit_vector_sync_gate finish only after all preconditions pass
  blocked_if:
    - required fixture missing
    - delta planner cannot classify chunks
    - checkpoint resume cannot prove no duplicate upsert
    - active manifest post-filter cannot prevent stale docs
    - any high-risk stale source can feed Codex
    - external API would be required before dry-run validation
  final_report_format:
    - route_decision
    - read_proof_report
    - implemented_files
    - validation_evidence
    - vector_sync_status
    - current_RAG_index_latest_claim
    - git_sync_status
    - remaining_risks
```

## 14. validation_plan

```yaml
validation_plan:
  schema_validation:
    - validate every new schema with positive and blocked fixtures
  fixture_validation:
    - include old/new manifest delta cases
    - include five conflict group examples
    - include hard gate failures
    - include weighted score golden cases
  dry_run_validation:
    - delta planner produces counts without external API
    - delta sync dry-run shows which chunks would embed/upsert
    - resume dry-run skips completed batches
  no_external_api_validation:
    - check/dry-run path asserts alibaba_embedding_api_called=false
    - check/dry-run path asserts dashvector_upsert_called=false
  integration_validation:
    - supply pack builder consumes overlay and decision report
    - retrieval probe post-filter rejects stale docs
    - failure resolver maps new failure types
```

## 15. status_boundary

```yaml
status_boundary:
  technical_validation: design_only_static_readback_and_local_non_network_validators_ran
  content_validation: not_promoted
  runtime_validation: not_performed
  production_readiness: not_claimed
  vector_sync_status: blocked_existing_state_not_fixed_this_round
  current_RAG_index_latest_claim: false
  weighted_decision_engine_real_task_validation: not_performed
```

## 16. git_sync_status_placeholder

This report requires normal repository sync before it can be treated as repository fact.

```yaml
git_sync_status:
  files_changed:
    - codex_log/rag_decision_engine_design/20260621_RAG决策工程线设计_round_1_design_only.md
    - codex_log/latest.md
  commit_sha: pending_until_commit
  pushed: pending_until_push
  remote_head_verified: pending_until_remote_readback
  secret_scan: pending_until_staged_scan
```

## 17. next_safe_step

```yaml
next_safe_step:
  recommendation: user_review_round_1_design_then_open_round_2_full_horizontal_implementation
  user_review_points:
    - 是否接受 active manifest allowlist + authority overlay post-filter 作为默认旧 docs 防污染策略
    - 是否接受 round 2 先做 dry-run/fake-client，再跑真实 DashVector delta sync
    - 是否允许未来在 DashVector delete/metadata update probe 通过后启用物理 delete
  ready_for_round_2_if:
    - user accepts this design
    - round_2 prompt preserves no secret/no external API until dry-run validators pass
    - implementation keeps path-limited stage/commit/push/readback
```
