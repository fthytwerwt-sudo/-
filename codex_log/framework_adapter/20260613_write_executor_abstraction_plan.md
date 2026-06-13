# 20260613 Write Executor Abstraction Plan

## 1. status

- `project_route`: `video_factory`
- `document_type`: `adapter_design`
- `formal_runtime_rule`: `false`
- `active_write_executor_current`: `codex`

This file designs the future write boundary. It does not enable Trae, install IDE tooling, or change current execution behavior.

## 2. reason_for_change

The old wording `Codex-only write boundary` is too narrow for the future architecture. The user confirmed future write execution may use:

- `Codex`
- `Trae`
- another IDE-based agent

The architecture should therefore use:

- `write_executor_boundary`
- `active_write_executor`
- `executor_type`

## 3. executor_types

| executor_type | Status now | Meaning |
|---|---|---|
| `codex` | `active` | Current write executor in this repository |
| `trae` | `future_candidate` | Future IDE write executor, not enabled |
| `future_ide_agent` | `future_candidate` | Placeholder for other verified IDE agents |

## 4. runtime_vs_executor_boundary

### Runtime may do

- route decision;
- workflow route decision;
- retrieval query construction;
- DashVector retrieval;
- source readback request;
- DeepSeek trigger decision;
- blocked_if validation;
- human review interrupt;
- execution handoff package generation.

### Runtime must not do in phase 1

- write repo files;
- edit formal mechanism files;
- commit;
- push;
- modify video / audio / image outputs;
- update `content_validation`, `send_ready`, `voice_validation`, `final_voice_validated`, `visual_master_locked`, or `current_data_goal_anchor_ready`.

### Write executor must do

- read handoff;
- read original files;
- apply scoped file changes;
- validate;
- report;
- run secret/status checks;
- path-limited stage;
- commit;
- push if supported and required;
- remote readback if supported and required.

## 5. handoff_schema

```yaml
write_executor_handoff:
  handoff_id:
  created_at:
  project_route: video_factory
  executor_type: codex | trae | future_ide_agent
  active_write_executor:
  task_type:
  workflow_type:
  allowed_files:
  forbidden_files:
  forbidden_status_fields:
  source_readback:
  retrieval_manifest:
  retrieval_gap_report:
  deepseek_trigger_decision:
  human_review_required:
  exact_changes_requested:
  validation_required:
  completion_truth_check:
  git_sync_required:
  remote_readback_required:
  blocked_if:
```

## 6. executor_result_schema

```yaml
write_executor_result:
  handoff_id:
  executor_type:
  files_changed:
  validation_result:
  generated_reports:
  forbidden_status_check:
  secret_check:
  git_status_before:
  git_status_after:
  commit_sha:
  push_status:
  remote_readback_status:
  completion_truth_check:
  remaining_blockers:
```

## 7. acceptance_conditions

A new executor can be enabled only if it proves:

1. It respects `allowed_files`.
2. It refuses `forbidden_files`.
3. It preserves forbidden status fields.
4. It reads original files before edits.
5. It validates after edits.
6. It records a report.
7. It can separate unrelated dirty changes.
8. It supports or explicitly reports lack of git sync.
9. It supports or explicitly reports lack of remote readback.
10. It does not bypass human review interrupts.

## 8. current_default

Until further proof:

```yaml
active_write_executor:
  executor_type: codex
  write_allowed: true
  git_sync_supported: true
  remote_readback_supported: true
```

All other executors remain `future_candidate`.
