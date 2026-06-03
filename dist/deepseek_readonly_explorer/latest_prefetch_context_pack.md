# DeepSeek readonly explorer latest_prefetch_context_pack

- `validation_status`: `blocked`
- `api_validation`: `passed`
- `deepseek_generation_status`: `blocked_invalid_context_pack`
- `context_pack_validation`: `blocked_invalid_context_pack`
- `fallback_status`: `not_used`
- `pipeline_status`: `blocked`
- `multi_agent_runtime_validation`: `not_started`
- `validated_at_utc`: `2026-06-03T19:17:57.101822+00:00`
- `base_url`: `https://api.deepseek.com`
- `model`: `deepseek-v4-flash`
- `scope`: `readonly_explorer_minimal_api_validation`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `safe_call_mode`: `process_env_only`
- `deepseek_actual_participation`: `not_attempted_policy_violation`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `error_category`: `finish_reason_length`

## attempt_log（尝试日志）

```json
[
  {
    "attempt_index": 1,
    "mode": "single_call_safe",
    "prompt_size_chars": 35857,
    "context_size_chars": 18130,
    "failure_reason": "finish_reason_length",
    "finish_reason": "length"
  },
  {
    "attempt_index": 2,
    "mode": "compressed_retry",
    "prompt_size_chars": 26725,
    "context_size_chars": 9137,
    "failure_reason": "finish_reason_length",
    "finish_reason": "length"
  },
  {
    "attempt_index": 3,
    "mode": "minimal_retry",
    "prompt_size_chars": 21257,
    "context_size_chars": 3736,
    "failure_reason": "finish_reason_length",
    "finish_reason": "length"
  }
]
```
