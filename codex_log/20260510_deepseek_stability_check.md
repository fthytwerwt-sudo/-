# 20260510｜DeepSeek 稳定化检查

## 1. deepseek_stability_check

```yaml
deepseek_stability_check:
  goal: stabilize DeepSeek participation state, not force success
  env_file_read: false
  process_env_key_allowed:
    test_a_default_mode: false
    test_b_process_env_mode: true
  process_env_key_present:
    test_a_default_mode: false
    test_b_process_env_mode: false
  api_key_printed: false
  api_key_written: false
  request_file: codex_log/supply_requests/20260510_deepseek_stability_check_request.json
  test_a_default_mode:
    supply_source: fallback_local_only
    fallback_status: used
    not_deepseek_conclusion: true
    context_pack_validation: fallback_local_only
    deepseek_actual_participation: "false"
    blocked_reason: none
  test_b_process_env_mode:
    supply_source: blocked
    fallback_status: not_used
    not_deepseek_conclusion: true
    context_pack_validation: blocked_missing_process_env_api_key
    deepseek_actual_participation: not_tested_missing_process_env_key
    blocked_reason: missing_process_env_api_key
  final_stability_status:
    - usable_with_fallback
    - blocked_missing_process_env_key
  execution_layer_completion:
    deepseek_readiness_check_added: true
    future_tasks_required_to_check_readiness: true
  remaining_unverified:
    - 进程环境注入 DEEPSEEK_API_KEY 后的真实 DeepSeek API 供料仍未通过本轮验证。
    - 本轮没有调用阿里 API，没有生成图片 / 视频 / 音频。
```

## 2. previous_safe_test_audit

```yaml
previous_safe_test_audit:
  env_file_read: false
  process_env_key_allowed: true
  process_env_key_present: false
  api_key_printed: false
  api_key_written: false
  supply_source: blocked
  deepseek_actual_participation: not_tested_missing_process_env_key
  reason: 当前 shell 进程环境没有 DEEPSEEK_API_KEY；安全规则禁止读取 .env 补救。
  remaining_gap: DeepSeek passed 仍待用户把 DEEPSEEK_API_KEY 安全注入 process environment 后重跑。
```

## 3. deepseek_readiness_check（DeepSeek 就绪检查）

已补齐或确认：

- `scripts/deepseek_supply_controller.py` 输出 `deepseek_readiness_check` 和 `blocked_reason`。
- `scripts/deepseek_readonly_explorer.py` 将 key 无效、网络 / timeout、输出不合格映射为稳定 blocked 状态。
- `codex_source/01_execution_rules.md` 要求后续 DeepSeek 相关任务先输出 `deepseek_readiness_check`。
- `codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md` 和 JSON Schema 已同步 readiness 字段。

完成规则：

- `deepseek_passed` 才能写 DeepSeek 真实参与。
- `fallback_local_only` 必须写 `not_deepseek_conclusion = true`。
- 缺 process env key 必须写 `blocked_missing_process_env_api_key` 或 `not_tested_missing_process_env_key`。
- fallback 不能写成 DeepSeek 稳定供料。

## 4. validation（验证）

```yaml
validation:
  py_compile: passed
  request_json_parse: passed
  schema_json_parse: passed
  forbidden_env_check: blocked_before_read
  forbidden_media_check: blocked_before_read
  forbidden_latest_review_pack_check: blocked_before_read
  test_a_default_mode: passed_with_fallback_local_only
  test_b_process_env_mode: blocked_missing_process_env_key
```

禁止路径回归：

- `.env` request: `request_file_matches_forbidden_path:.env`
- media request: `request_file_matches_forbidden_path:素材样例/sample.mp4`
- `dist/latest_review_pack/` request: `request_file_matches_forbidden_path:dist/latest_review_pack/summary.json`

## 5. status_boundaries（状态边界）

```yaml
status_boundaries:
  technical_validation: passed_for_scripts_request_and_guardrails
  mechanism_validation: readiness_check_added_and_three_state_semantics_stabilized
  deepseek_supply_validation: blocked_missing_process_env_key
  execution_layer_completion: deepseek_readiness_check_added
  content_validation: unchanged_not_validated
  env_file_read: false
  api_key_printed: false
  api_key_written: false
  ali_api_called: false
  image_generated: false
  video_generated: false
  content_validation_changed: false
  send_ready_changed: false
  publish_status_changed: false
  voice_validation_changed: false
  final_voice_validated_changed: false
```

## 6. 下一个目标

如果要验证 `deepseek_passed（DeepSeek 真实供料通过）`，用户先把 `DEEPSEEK_API_KEY` 安全注入当前进程环境，再重跑本稳定化测试；仍不得读取 `.env` 补救。若已注入并通过，则进入一条真实文案的小范围素材计划执行，不调用阿里 API。
