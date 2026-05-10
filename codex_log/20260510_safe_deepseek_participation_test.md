# 20260510｜DeepSeek 安全真实参与测试

## 0. process_env_rerun_20260510（进程环境 key 安全重跑）

```yaml
safe_process_env_rerun:
  terminal_opened: true
  user_key_entered: true
  env_file_read: false
  process_env_key_allowed: true
  process_env_key_present: true
  api_key_printed: false
  api_key_written: false
  key_written_to_env_file: false
  request_file: codex_log/supply_requests/20260510_deepseek_stability_check_request.json
  supply_source: deepseek_passed
  fallback_status: not_used
  context_pack_validation: passed
  deepseek_generation_status: passed_with_retries
  deepseek_actual_participation: true
  blocked_reason: none
  result_boundary: 本轮 request 样例供料通过；不得写成 DeepSeek 长期稳定真实供料，也不得写成内容验证通过。
```

## 1. 测试口径

本文件记录 controller 在“不读取 `.env` 文件”的前提下，是否可以安全测试 DeepSeek 实际参与。

本轮没有把 `.env` 加入 context，没有读取 `.env` 文件内容，没有打印或写入 API key，没有调用阿里 API，没有生成真实图片 / 视频 / 音频。

## 2. safe_deepseek_participation_test

```yaml
safe_deepseek_participation_test:
  env_file_read: false
  process_env_key_allowed: true
  process_env_key_present: false
  api_key_printed: false
  api_key_written: false
  request_file: codex_log/supply_requests/20260510_safe_deepseek_process_env_request.json
  tested_action: file_map
  supply_source: blocked
  fallback_status: not_used
  context_pack_validation: blocked_missing_process_env_api_key
  deepseek_actual_participation: not_tested_missing_process_env_key
  reason: 显式安全模式已启用，但当前 shell 进程环境没有 DEEPSEEK_API_KEY；按规则不得读取 .env 补救，因此未发起真实 DeepSeek API 调用。
  remaining_unverified:
    - 进程环境注入 DEEPSEEK_API_KEY 后的真实 DeepSeek API 参与仍待重跑。
    - DeepSeek passed 只能在安全 process env key 存在且 API 返回有效上下文包后记录。
```

## 3. test_runs（测试运行）

```yaml
test_runs:
  - name: Test A 默认安全模式
    command_summary: controller request-file, no --allow-process-env-api-key
    request_validation_status: passed
    action: file_map
    supply_source: fallback_local_only
    fallback_status: used
    context_pack_validation: fallback_local_only
    deepseek_actual_participation: false
    env_file_read: false
    process_env_key_allowed: false
    process_env_key_present: false
    api_key_printed: false
    api_key_written: false
    not_deepseek_conclusion: true
    evidence_summary: 默认模式不允许 process env key；request 禁止 .env / secret，因此使用 fallback_local_only。
  - name: Test B 允许 process env key 的安全模式
    command_summary: DEEPSEEK_DISABLE_ENV_FILE=1 DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1 + --allow-process-env-api-key
    request_validation_status: passed
    action: file_map
    supply_source: blocked
    fallback_status: not_used
    context_pack_validation: blocked_missing_process_env_api_key
    deepseek_actual_participation: not_tested_missing_process_env_key
    env_file_read: false
    process_env_key_allowed: true
    process_env_key_present: false
    api_key_printed: false
    api_key_written: false
    not_deepseek_conclusion: true
    evidence_summary: 当前进程环境未提供 DEEPSEEK_API_KEY；controller / explorer 没有读取 .env 补救，结果如实 blocked。
```

## 4. forbidden_path_tests（禁止路径回归）

```yaml
forbidden_path_tests:
  - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_env_example.json
    result: blocked_before_read
    error: request_file_matches_forbidden_path:.env
  - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_media_example.json
    result: blocked_before_read
    error: request_file_matches_forbidden_path:素材样例/sample.mp4
  - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_latest_review_pack_example.json
    result: blocked_before_read
    error: request_file_matches_forbidden_path:dist/latest_review_pack/summary.json
```

## 5. 状态边界

- `technical_validation（技术验证）`: 安全调用开关、request validation 和禁止路径回归可运行。
- `mechanism_validation（机制验证）`: 已建立“不读 .env、只用 process env key”的安全参与路径。
- `deepseek_actual_participation（DeepSeek 实际参与）`: `not_tested_missing_process_env_key`，因为当前进程环境没有 key。
- `api_generation_validation（API 生成验证）`: 未调用阿里 API，未生成图片。
- `content_validation（内容验证）`: 未验证真实内容，不得写成 passed。
- `multi_agent_runtime_validation（多 agent 运行时验证）`: `not_started`。

## 6. 下一个目标

如果需要验证真实 DeepSeek API 参与，先把 `DEEPSEEK_API_KEY` 安全注入为 process environment，再重跑 `safe_deepseek_participation_test`；仍不得读取 `.env` 文件补救。
