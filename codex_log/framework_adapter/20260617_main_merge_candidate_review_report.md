# 20260617 Main Merge Candidate Review

## 1. task_result

```yaml
status: main_merge_candidate_review_in_progress
meaning: adapter branch candidate has entered merge safety review; main merge is allowed only after all validation gates pass
project_route: video_factory
source_branch: adapter/agent-service-toolkit-sandbox
target_branch: main
runtime_enabled: false
service_started: false
external_api_called: false
media_generated: false
content_validation_status: not_promoted
send_ready: false
```

## 2. route_decision

```yaml
project_route: video_factory
task_type:
  - project_file_change
  - code_debug
  - mechanism_or_route_fix
  - review_diagnosis_audit
responsibility_layer:
  - validation_layer
  - execution_layer
  - sync_layer
  - mechanism_fix_layer
large_task_gate:
  triggered: true
  reason: adapter code, schema fixtures, framework reports, latest log, merge validation, commit, push, and remote readback are all in scope
  lane_recommendation: audit_lane_then_standard_lane
  parallel_recommendation: serial_only_for_writes_read_parallel_for_reads
supply_source_arbitration:
  retrieval_manifest: repo_source_readback_only
  source_readback_status: read_ok
  deepseek_trigger_decision: false
  not_deepseek_conclusion: true
execution_permission: adapter_branch_review_fix_then_main_merge_only_if_all_gates_pass
```

## 3. files_read

```yaml
required_files_read:
  - AGENTS.md
  - codex_log/latest.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
  - codex_source/13_execution_lane_and_parallel_rules.md
  - codex_source/19_project_state_action_router.md
  - codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md
  - project_source/20_codex_multi_agent_routing_note_for_gpt_project.md
  - codex_log/framework_adapter/current_adapter_integration_handoff.md
  - codex_log/framework_adapter/20260617_adapter_integration_context_manifest.json
  - codex_log/framework_adapter/20260617_round2_branch_local_adapter_integration_candidate_report.md
  - codex_log/framework_adapter/20260617_runtime_service_probe_report.md
  - codex_source/adapter_integration/README.md
  - codex_source/adapter_integration/*.py
  - codex_source/schema_contracts/00_schema_contracts_index.md
  - codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py
  - codex_source/schema_contracts/schemas/*.schema.yaml
  - codex_source/schema_contracts/fixtures/passing/*.yaml
  - codex_source/schema_contracts/fixtures/blocked/*.yaml
read_status: read_ok
schema_fixture_readback: sha256_readback_completed
```

## 4. merge_scope

```yaml
source_branch: adapter/agent-service-toolkit-sandbox
target_branch: main
included_scope:
  - adapter_integration_candidate_code
  - editing_workflow_contract_schema_fixture_probe
  - branch_local_runtime_service_probe_code
  - framework_adapter_reports
  - latest_adapter_status_log
excluded_scope:
  - env_or_secret_files
  - real_media_assets
  - public_untracked_noise
  - dist_review_pack
  - GPT数据源
  - production runtime enablement
  - persistent service startup
```

## 5. alignment_checks

```yaml
project_router_alignment:
  status: aligned
  evidence: video_factory route confirmed through AGENTS and workflow routing index
codex_write_boundary_alignment:
  status: aligned
  evidence: active write executor remains codex; service boundary blocks repo write, commit, push, main modification, external calls, and media generation
delivery_baseline_alignment:
  status: aligned
  evidence: this is not a video delivery task and does not advance publish candidate, content, send, voice, or visual states
status_alignment:
  status: aligned_after_fix
  evidence:
    - post-merge runner context fixed so main validation can run without branch mismatch
    - historical negative guard field names adjusted to avoid forbidden scan false positives
```

## 6. validation_commands

```yaml
pre_merge_validation_required:
  - python3 -m py_compile codex_source/adapter_integration/*.py
  - python3 codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py
  - python3 -m codex_source.adapter_integration.no_render_adapter_runner --sample all
  - python3 -m codex_source.adapter_integration.runtime_service_probe --sample all
  - manifest_json_required_key_check
  - git diff --check
  - forbidden_status_promotion_scan
  - secret_scan
post_merge_validation_required:
  - python3 -m py_compile codex_source/adapter_integration/*.py
  - python3 codex_source/schema_contracts/probes/editing_workflow_no_render_probe.py
  - python3 -m codex_source.adapter_integration.no_render_adapter_runner --sample all
  - python3 -m codex_source.adapter_integration.runtime_service_probe --sample all
  - git diff --check
  - forbidden_status_promotion_scan
  - secret_scan
```

## 7. risk_register

```yaml
risks:
  - risk: runner_branch_guard_blocks_main_validation
    disposition: fixed_on_adapter_branch
  - risk: historical_negative_guard_names_trigger_regex_scan
    disposition: fixed_in_framework_adapter_reports_without_status_promotion
  - risk: merge_conflict_in_forbidden_paths
    disposition: block_and_abort_merge_if_detected
  - risk: public_untracked_noise_accidentally_staged
    disposition: path_limited_stage_only
  - risk: middle_state_claimed_as_final_delivery
    disposition: blocked_by_completion_truth_and_report_language
```

## 8. merge_decision

```yaml
decision: conditionally_allowed_after_validation
meaning: proceed to adapter validation; merge main only if all pre-merge and post-merge gates pass
runtime_enabled: false
service_started: false
external_api_called: false
media_generated: false
content_validation_status: not_promoted
send_ready: false
production_readiness_claim: not_claimed
```

## 9. blocked_if

```yaml
blocked_if:
  - adapter validation fails
  - manifest required keys are missing
  - forbidden status promotion scan fails
  - secret scan fails
  - merge conflict touches env, GPT数据源, dist, media, public, AGENTS, or uncertain paths
  - post-merge validation fails
  - main push fails
  - remote head readback does not match local head
```
