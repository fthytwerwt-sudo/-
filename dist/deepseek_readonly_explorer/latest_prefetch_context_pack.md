# DeepSeek readonly explorer latest_prefetch_context_pack

- `validation_status`: `passed`
- `api_validation`: `passed`
- `deepseek_generation_status`: `passed_with_retries`
- `context_pack_validation`: `passed`
- `fallback_status`: `not_used`
- `pipeline_status`: `passed`
- `multi_agent_runtime_validation`: `not_started`
- `validated_at_utc`: `2026-05-17T13:44:03.411861+00:00`
- `base_url`: `https://api.deepseek.com`
- `model`: `deepseek-v4-flash`
- `scope`: `readonly_explorer_minimal_api_validation`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `safe_call_mode`: `process_env_only`
- `deepseek_actual_participation`: `deepseek_passed`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `context_truncated`: `true`
- `truncated_files`: `["AGENTS.md", "codex_log/latest.md", "codex_source/00_codex_readme.md", "codex_source/01_execution_rules.md"]`

## prefetch_context_pack（预读取上下文包）

```json
{
  "confirmed": [
    "V004 pre_24h interim_17h_snapshot",
    "V003 remains current_operation_target"
  ],
  "pending_verification": [
    "V004 24h final",
    "human confirmation for switching target"
  ],
  "source_summary": [
    "AGENTS.md: project routing rules",
    "latest.md: V002 staged unfixed"
  ]
}
```

## must_read_file_map（必读文件地图）

```json
{
  "required_files": [
    "review_loop/operation_records_index.md",
    "review_loop/copy_iteration/copy_registry.json"
  ],
  "optional_files": [
    "codex_log/current_operation_target.md",
    "codex_log/current_data_goal_anchor.md"
  ],
  "reason": "Verify V003 target and V004 registry boundaries before intake"
}
```

## risk_and_conflict_report（风险与冲突报告）

```json
{
  "risks": [
    "V004 raw copy 3 favorites misattributed as actual",
    "V002 staged overwrite by V004 registry"
  ],
  "conflicts": [
    "V004 must be pre_24h not final",
    "Only V003 is current_operation_target"
  ],
  "blocked_if": [
    "V004_record_missing",
    "V004_written_as_24h_72h_or_7d_final"
  ]
}
```

## candidate_summary（候选摘要）

```json
{
  "summary": "V004 intake pre-supply: read-only review complete",
  "recommended_next_step": "Codex: archive V004, keep V003 target, rerun systems",
  "not_allowed": [
    "write files",
    "decide project facts"
  ]
}
```

## attempt_log（尝试日志）

```json
[
  {
    "attempt_index": 1,
    "mode": "single_call_safe",
    "prompt_size_chars": 33700,
    "context_size_chars": 18143,
    "failure_reason": "empty_content",
    "finish_reason": "length"
  },
  {
    "attempt_index": 2,
    "mode": "compressed_retry",
    "prompt_size_chars": 24561,
    "context_size_chars": 9138,
    "failure_reason": "finish_reason_length",
    "finish_reason": "length"
  },
  {
    "attempt_index": 3,
    "mode": "minimal_retry",
    "prompt_size_chars": 19149,
    "context_size_chars": 3742,
    "failure_reason": "none",
    "finish_reason": "stop"
  }
]
```
