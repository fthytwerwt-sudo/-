# DeepSeek runtime doctor report

- `status`: `ready`
- `key_found`: `true`
- `key_source`: `project_env`
- `key_git_tracked`: `false`
- `can_inject_child_process`: `true`
- `can_call_deepseek`: `true`
- `api_key_printed`: `false`
- `api_key_written`: `false`

```json
{
  "generated_at_utc": "2026-05-15T12:38:12.539329+00:00",
  "status": "ready",
  "runtime_provider": {
    "status": "ready",
    "key_found": true,
    "key_source": "project_env",
    "key_source_path": ".env",
    "auto_load_enabled": true,
    "allowed_key_name": [
      "DEEPSEEK_API_KEY"
    ],
    "never_print_key": true,
    "never_write_key": true,
    "inject_to_child_process_only": true,
    "redact_stdout_stderr": true,
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-v4-flash",
    "escalation_model": "deepseek-v4-pro",
    "setup_required_reason": "",
    "load_order": [
      "process_env",
      "project_env_local",
      "project_env",
      "local_runtime_authorization"
    ],
    "load_attempts": [
      {
        "source": "process_env",
        "path": "process_env",
        "exists": "true",
        "key_field_present": "false",
        "key_nonempty": "false"
      },
      {
        "source": "project_env_local",
        "path": ".env.local",
        "exists": "false",
        "key_field_present": "false",
        "key_nonempty": "false"
      },
      {
        "source": "project_env",
        "path": ".env",
        "exists": "true",
        "key_field_present": "true",
        "key_nonempty": "true"
      }
    ]
  },
  "key_found": true,
  "key_source": "project_env",
  "key_source_path": ".env",
  "key_git_tracked": false,
  "can_inject_child_process": true,
  "inject_error": "",
  "can_call_deepseek": true,
  "explorer_status": {
    "validation_status": "passed",
    "api_validation": "passed",
    "deepseek_generation_status": "passed",
    "context_pack_validation": "passed",
    "fallback_status": "not_used",
    "pipeline_status": "passed",
    "multi_agent_runtime_validation": "not_started",
    "validated_at_utc": "2026-05-15T12:38:08.270600+00:00",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-v4-flash",
    "scope": "readonly_explorer_minimal_api_validation",
    "env_file_read": "false",
    "process_env_key_allowed": "true",
    "process_env_key_present": "true",
    "safe_call_mode": "process_env_only",
    "deepseek_actual_participation": "deepseek_passed",
    "api_key_printed": "false",
    "api_key_written": "false",
    "context_truncated": "false",
    "truncated_files": "[]"
  },
  "api_call_returncode": 0,
  "api_call_stdout_tail": "",
  "api_call_stderr_tail": "",
  "supply_pack_has_no_key": true,
  "manifest_has_no_key": true,
  "log_has_no_key": true,
  "api_key_printed": false,
  "api_key_written": false,
  "leak_scan": {
    "checked_files": [
      "dist/deepseek_runtime_validation/runtime_doctor_report.md",
      "dist/deepseek_runtime_validation/latest_combined_participation_report.json",
      "dist/deepseek_runtime_validation/latest_combined_participation_report.md",
      "dist/deepseek_runtime_validation/runtime_doctor_report.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/latest_supply_pack.md",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/latest_supply_manifest.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/latest_supply_pack.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/participation_report.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/latest_supply_pack.md",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/latest_supply_manifest.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/latest_supply_pack.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/participation_report.json",
      "dist/deepseek_runtime_validation/single_task_A_file_map/latest_supply_pack.md",
      "dist/deepseek_runtime_validation/single_task_A_file_map/latest_supply_manifest.json",
      "dist/deepseek_runtime_validation/single_task_A_file_map/latest_supply_pack.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/latest_supply_pack.md",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/latest_supply_manifest.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/latest_supply_pack.json",
      "dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/participation_report.json",
      "dist/deepseek_runtime_validation/single_task_C_risk_review_retry/latest_supply_pack.md",
      "dist/deepseek_runtime_validation/single_task_C_risk_review_retry/latest_supply_manifest.json",
      "dist/deepseek_runtime_validation/single_task_C_risk_review_retry/latest_supply_pack.json",
      "dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md"
    ],
    "leak_found": false,
    "leak_files": []
  },
  "setup_required_output": ""
}
```
