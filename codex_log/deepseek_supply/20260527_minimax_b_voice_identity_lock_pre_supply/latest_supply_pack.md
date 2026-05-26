# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260526T162205Z`
- `request_id`: `20260527_minimax_b_voice_identity_lock_pre_supply_request`
- `request_validation_status`: `passed`
- `task_type`: `project_file_change + code_debug + tts_voice_identity_lock + mechanism_or_route_fix + short_audio_sample_generation`
- `trigger_reason`: `mandatory_pre_supply`
- `action`: `file_map`
- `supply_source`: `blocked`
- `context_pack_validation`: `blocked_invalid_context_pack`
- `deepseek_generation_status`: `blocked_invalid_context_pack`
- `fallback_status`: `not_used`
- `pipeline_status`: `blocked`
- `multi_agent_runtime_validation`: `not_started`
- `not_deepseek_conclusion`: `true`
- `deepseek_actual_participation`: `not_attempted_policy_violation`
- `blocked_reason`: `invalid_context_pack`
- `token_usage_observed_or_user_check_required`: `user_check_required`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `api_key_printed`: `false`
- `api_key_written`: `false`

## request_state（请求状态）

```json
{
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260527_minimax_b_voice_identity_lock_pre_supply_request.json",
  "current_goal": "本轮只完成 MiniMax B 方案声音身份锁定：确认 MiniMax 声音能力，生成 3-5 个短试听候选，每个候选至少 2 个韵律版本，补强 b_voice_identity_lock / human_voice_review_gate；不重生成完整视频，不替换 full.mp4 / narration.wav，不改文案，不推进 voice_validation 或 send_ready。",
  "requires_real_deepseek_participation": false,
  "safe_loader_policy": {},
  "runtime_provider": {
    "runtime_provider_status": "ready",
    "runtime_provider_auto_load_enabled": true,
    "runtime_provider_key_source": "project_env",
    "runtime_provider_key_source_path": ".env",
    "runtime_provider_version": "20260515"
  },
  "data_goal_anchor": {},
  "current_stage_goal": "",
  "main_bottleneck": "",
  "primary_variable": "",
  "forbidden_variables": [],
  "success_metric": "",
  "failure_metric": "",
  "post_publish_validation_metric": "",
  "current_step": "before_write_and_before_minimax_sample_generation",
  "known_context": [
    "当前候选片 TTS route 正确：actual_tts_provider=minimax, actual_tts_model=MiniMax/speech-2.8-hd, selected_route=aliyun_bailian_proxy_to_minimax。",
    "上一轮 TTS 声音身份审计确认实际 voice_id=female-tianmei，且 B 方案当前只是 voice_feel_tags_only，没有 expected_b_minimax_voice_id、similarity_check 或 human_review。",
    "用户明确要求音色身份优先于情绪韵律；female-tianmei 不得继续作为默认 B 方案，除非用户试听确认。",
    "历史 B 参考音频存在且本轮只作为只读 reference：B_15秒文案_停顿梗感.wav 与 语音样本2_声音复刻试听_15秒.wav。",
    "本轮允许调用 MiniMax/DashScope route_b 生成短试听样本；禁止 fallback 到 Qwen、Serena、macOS say、本地低质 TTS 或 silent audio。"
  ],
  "missing_context": [
    "Need verify current MiniMax/DashScope route can still call get_voice and synthesize short non-silent samples with selected voice_id values.",
    "Need determine whether current route can use reference_audio / voice_clone from local B reference audio, or whether it requires public audio_url / official MiniMax API file upload outside this task's safe scope.",
    "Need add executable voice identity gate so b_voice_feel_reflected=true cannot pass without actual voice_id match and human_voice_review_status=user_confirmed.",
    "Need ensure generated samples are pending_user_review only, not user_confirmed or voice_validation passed."
  ],
  "decision_needed": ""
}
```

## deepseek_supply_gate（DeepSeek 供料闸门）

```json
{
  "mandatory_for_every_task": true,
  "supply_request_created": true,
  "deepseek_call_required": true,
  "deepseek_call_attempted": false,
  "deepseek_actual_participation": "not_attempted_policy_violation",
  "supply_source": "blocked",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": true,
  "blocked_reason": "invalid_context_pack",
  "token_usage_expected": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
  "token_usage_observed_or_user_check_required": "user_check_required",
  "fallback_not_completion": true,
  "deepseek_must_not_be_skipped_by_codex_discretion": true
}
```

## deepseek_readiness_check（DeepSeek 就绪检查）

```json
{
  "required": true,
  "runtime_provider": {
    "runtime_provider_status": "ready",
    "runtime_provider_auto_load_enabled": true,
    "runtime_provider_key_source": "project_env",
    "runtime_provider_key_source_path": ".env",
    "runtime_provider_version": "20260515"
  },
  "env_file_read": "false",
  "process_env_key_allowed": "true",
  "process_env_key_present": "true",
  "safe_call_mode": "process_env_only",
  "request_validation_status": "passed",
  "supply_source": "blocked",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": true,
  "context_pack_validation": "blocked_invalid_context_pack",
  "deepseek_actual_participation": "not_attempted_policy_violation",
  "blocked_reason": "invalid_context_pack",
  "completion_rule": [
    "deepseek_passed 才能写 DeepSeek 真实参与。",
    "fallback_local_only 必须写 not_deepseek_conclusion = true。",
    "missing_process_env_key 必须写 blocked_missing_process_env_api_key。",
    "token 未观察到减少时，不得写 DeepSeek 已深度参与。",
    "不得把 fallback 写成 DeepSeek 稳定供料。"
  ]
}
```

## deepseek_participation_report（DeepSeek 参与报告）

```json
{
  "deepseek_call_real": false,
  "deepseek_actual_participation": "not_attempted_policy_violation",
  "supply_source": "blocked",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": true,
  "blocked_reason": "invalid_context_pack",
  "token_usage_expectation_check": {
    "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
    "expected_to_decrease": false,
    "observed_token_usage": "not_available_user_check_required",
    "token_usage_observed_or_user_check_required": "user_check_required",
    "cannot_claim_deepseek_deep_participation_if_token_not_decreased": true,
    "fallback_local_only_token_rule": "fallback_local_only 不应减少 DeepSeek token，也不能写 DeepSeek 已深度参与。"
  },
  "codex_original_file_review_required": true,
  "deepseek_may_write_files": false,
  "deepseek_may_decide_project_facts": false,
  "multi_agent_runtime_validation": "not_started"
}
```

## token_usage_expectation_check（token 使用预期检查）

```json
{
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
  "expected_to_decrease": false,
  "observed_token_usage": "not_available_user_check_required",
  "token_usage_observed_or_user_check_required": "user_check_required",
  "cannot_claim_deepseek_deep_participation_if_token_not_decreased": true,
  "fallback_local_only_token_rule": "fallback_local_only 不应减少 DeepSeek token，也不能写 DeepSeek 已深度参与。"
}
```

## task（任务）

Use this supply_request task card as the only current task context. Do not infer missing project state from memory.
{
  "request_id": "20260527_minimax_b_voice_identity_lock_pre_supply_request",
  "task_id": "minimax_b_voice_identity_lock",
  "mandatory_for_every_task": true,
  "participation_level": "readonly_pre_supply",
  "pre_supply_required": true,
  "post_review_required": true,
  "codex_vertical_completion_required": true,
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
  "fallback_allowed": true,
  "fallback_not_completion": true,
  "user_explicit_deepseek_required": false,
  "deepseek_must_not_be_skipped_by_codex_discretion": true,
  "current_goal": "本轮只完成 MiniMax B 方案声音身份锁定：确认 MiniMax 声音能力，生成 3-5 个短试听候选，每个候选至少 2 个韵律版本，补强 b_voice_identity_lock / human_voice_review_gate；不重生成完整视频，不替换 full.mp4 / narration.wav，不改文案，不推进 voice_validation 或 send_ready。",
  "current_step": "before_write_and_before_minimax_sample_generation",
  "known_context": [
    "当前候选片 TTS route 正确：actual_tts_provider=minimax, actual_tts_model=MiniMax/speech-2.8-hd, selected_route=aliyun_bailian_proxy_to_minimax。",
    "上一轮 TTS 声音身份审计确认实际 voice_id=female-tianmei，且 B 方案当前只是 voice_feel_tags_only，没有 expected_b_minimax_voice_id、similarity_check 或 human_review。",
    "用户明确要求音色身份优先于情绪韵律；female-tianmei 不得继续作为默认 B 方案，除非用户试听确认。",
    "历史 B 参考音频存在且本轮只作为只读 reference：B_15秒文案_停顿梗感.wav 与 语音样本2_声音复刻试听_15秒.wav。",
    "本轮允许调用 MiniMax/DashScope route_b 生成短试听样本；禁止 fallback 到 Qwen、Serena、macOS say、本地低质 TTS 或 silent audio。"
  ],
  "missing_context": [
    "Need verify current MiniMax/DashScope route can still call get_voice and synthesize short non-silent samples with selected voice_id values.",
    "Need determine whether current route can use reference_audio / voice_clone from local B reference audio, or whether it requires public audio_url / official MiniMax API file upload outside this task's safe scope.",
    "Need add executable voice identity gate so b_voice_feel_reflected=true cannot pass without actual voice_id match and human_voice_review_status=user_confirmed.",
    "Need ensure generated samples are pending_user_review only, not user_confirmed or voice_validation passed."
  ],
  "decision_needed": "",
  "expected_output": [
    "file_map",
    "risk_and_conflict_report",
    "missing_or_uncertain_files",
    "codex_next_input",
    "status_promotion_risk_check",
    "voice_identity_lock_risk_check"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "read_status_required": true,
    "impact_check_required": true,
    "write_scope": [
      "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
      "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
      "codex_source/00_codex_readme.md",
      "codex_source/01_execution_rules.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/21_codex_judgment_permission_matrix.md",
      "GPT数据源/05_文案路由规则.md",
      "GPT数据源/07_AI知识类视频价值规则.md",
      "GPT数据源/08_当前正式事实.md",
      "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
      "tests/test_publish_candidate_voice_gate.py",
      "tests/test_minimax_b_voice_identity_lock.py",
      "codex_log/latest.md",
      "codex_log/20260527_minimax_b_voice_identity_lock.md",
      "codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_001951/"
    ],
    "output_dir": "codex_log/deepseek_supply/20260527_minimax_b_voice_identity_lock_pre_supply",
    "verification_required": [
      "MiniMax official capability evidence",
      "short sample audio ffprobe/decode/non_silent validation or blocked reason",
      "fixture_json_parse",
      "unit_tests",
      "py_compile",
      "no_full_video_or_full_narration_change_check",
      "no_status_promotion_check",
      "secret_scan",
      "git_diff_review"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "MiniMax authorization unavailable.",
    "MiniMax current route cannot specify voice_id.",
    "MiniMax current route cannot generate short non-silent samples.",
    "Historical B reference audio cannot be read by Codex.",
    "Only female-tianmei remains available and user has not confirmed it.",
    "Any implementation would require Qwen / Serena / macOS say / local fallback to approximate old B.",
    "Secret/API key/token risk is detected.",
    "Git sync cannot be completed."
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime is stable or completed.",
    "Do not generate or modify full video.",
    "Do not regenerate full narration.",
    "Do not modify locked copy.",
    "Do not promote content_validation, send_ready, voice_validation, final_voice_validated, or visual_master_locked.",
    "Do not approve female-tianmei as B voice unless user confirms after listening.",
    "Do not submit API key, token, or secret."
  ],
  "deep_supply_mode": {
    "enabled": true,
    "mode": [
      "deep_file_prefetch",
      "voice_identity_lock_risk_review"
    ]
  },
  "content_loading_policy": {
    "read_only": true,
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 12,
    "max_chars_per_file": 1400,
    "max_total_chars": 16000,
    "truncate_policy": "head_and_relevant_snippets",
    "do_not_read_secret_files": true,
    "do_not_modify_files": true
  },
  "codex_minimal_review_policy": {
    "will_modify_files": [
      "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
      "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
      "codex_source/00_codex_readme.md",
      "codex_source/01_execution_rules.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/21_codex_judgment_permission_matrix.md",
      "GPT数据源/05_文案路由规则.md",
      "GPT数据源/07_AI知识类视频价值规则.md",
      "GPT数据源/08_当前正式事实.md",
      "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
      "tests/test_publish_candidate_voice_gate.py",
      "tests/test_minimax_b_voice_identity_lock.py",
      "codex_log/latest.md",
      "codex_log/20260527_minimax_b_voice_identity_lock.md"
    ],
    "conflict_or_uncertain_files": [
      "codex_log/latest.md",
      "GPT数据源/08_当前正式事实.md",
      "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py"
    ],
    "safety_sensitive_files": [
      "GPT数据源/08_当前正式事实.md",
      "codex_log/latest.md",
      "dist/",
      "codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_001951/"
    ]
  }
}

## files_considered（已考虑文件）

```json
[
  "AGENTS.md",
  "codex_source/00_codex_readme.md",
  "codex_source/01_execution_rules.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/21_codex_judgment_permission_matrix.md",
  "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
  "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
  "GPT数据源/05_文案路由规则.md",
  "GPT数据源/07_AI知识类视频价值规则.md",
  "GPT数据源/08_当前正式事实.md",
  "codex_log/latest.md",
  "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "AGENTS.md",
  "codex_source/00_codex_readme.md",
  "codex_source/01_execution_rules.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/21_codex_judgment_permission_matrix.md",
  "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
  "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
  "GPT数据源/05_文案路由规则.md",
  "GPT数据源/07_AI知识类视频价值规则.md",
  "GPT数据源/08_当前正式事实.md",
  "codex_log/latest.md",
  "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md"
]
```

## risks（风险）

```json
[]
```

## missing_files（缺失文件）

```json
[]
```

## deepseek_depth_validation（DeepSeek 深度供料校验）

```json
{
  "enabled": true,
  "modes": [
    "deep_file_prefetch"
  ],
  "missing_modes": [
    "post_risk_review",
    "mid_task_incremental_supply"
  ],
  "relevant_file_bundle_exists": true,
  "exact_snippet_pack_exists": true,
  "deepseek_actual_required": false,
  "supply_source": "blocked",
  "status": "failed_insufficient_depth",
  "not_long_term_runtime_validation": true
}
```

## relevant_file_bundle（相关文件内容包）

```json
[
  {
    "path": "AGENTS.md",
    "file_role": "readonly_context",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- 需要 GPT Project 上传包地址时，必须先读取 `codex_log/current_local_artifact_paths.md` 或由 Codex 本地审计后给出。\n  - `Codex（唯一写入执行层 / Integrator）`\n  - `DeepSeek（每轮默认只读供料层 / Explorer）`\n- 当前最高机制入口已包含 `Project State Action Router（项目状态动作总控器）`：命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审时，先读 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md`，输出 `state_action_router（项目状态动作总控器）` 后再执行。\n- `DeepSeek（每轮默认只读供料层 / Explorer）` 每轮默认做执行前供料和执行后风险复核，输出上下文压缩、必读文件地图、风险冲突报告、遗漏同步检查和 Codex 下一步输入；不写文件、不拍板项目事实。\n- `Codex（唯一写入执行层 / Integrator）` 默认负责复核原文件、整合 DeepSeek 供料、补齐受影响文件 / 字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、日志和 Git 收尾。\n- Codex 收到 ChatGPT 完整执行单、横向补全包、多文件机制修补或“不要只做一半 / 执行到底”类任务时，必须触发 `Completion Relay Gate（补全接力闸门）`，先生成 `required_output_inventory（必须交付清单）` 与 `child_task_graph（子任务树）`，再执行并做 `remaining_work_check（剩余工作检查）`。\n- `content_validation = not_advanced_by_formal_operation（正式运营不等于内容最终通过；不得写成内容通过）`\n- `send_ready = false`\n- 上述 `content_validation` 是当前发布后阶段口径；不得把它写成 `passed`\n以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。\n- 不允许把 `technical_validation` 写成 `content_validation`\n- PR #7 B、cute card、round34 中段剪辑、TTS 节奏参考、TTS 语音 / 音色候选参考、`visual_route_map.json`、`locked_reference_registry.md` 仍属于 `reference_whitelist（参考白名单）`，后续按任务类型读取路径索引和 registry 复核\n...[truncated]",
    "excerpt_range_or_marker": "lines:73-86",
    "confidence": "high"
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。\n- Codex 不得把本地生成当已 push。\n- Codex 不得把技术成功当内容成功。\n- Codex 不得把“没有明确失败”当完成。\nCodex 在视频执行中负责素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，不负责重新定稿。Codex 可以改标点、换行、字幕分句和 TTS 停顿，但不得改变语义、人味、标题语气、核心判断、前台表达角度，不能用视觉标题卡替换 `locked_title`。\n如果 Codex 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，等待 ChatGPT / 用户确认，不得自行改稿。\n以后凡是任务命中 `publish_candidate（发片候选）`、`video_execution（视频执行）`、`repair_candidate（修片候选）`、`regenerate_video（重新生成视频）`、`pre_publish_fix（发布前修复）`、`final_script_to_video（最终文案进入视频）`，或涉及 `TTS / subtitle / card / timeline / review_pack / privacy_mask / aspect_ratio / visual_evidence` 任一视频执行组件，Codex 必须先跑 `process_boot_gate（流程启动闸门）`。\n- `process_boot_gate` 只防止执行断层，不推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n    content_validation_issue:\n- 没有人审前不得推进 `send_ready = true`。\n本套件只证明导出前预检链被调用和报告可复核；不自动推进 `c\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/01_execution_rules.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# Codex 执行规则\n命中截图、平台数据、评论、私信、咨询、复盘或下一轮变量判断时，Codex 必须优先读取：\n本覆盖口径不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n当前进入 `formal_operation_active（正式运营中）` 后，Codex 在 `route_decision（路由判断）` 阶段必须判断本轮是否是视频交付任务。\nCodex 后续不得降级处理正式运营任务。凡任务目标指向做视频、产视频、发片候选、运营内容、下一条视频、发布候选、项目机制落库、GPT Project 同步、数据录入、复盘记录、素材审计、文案到执行映射、TTS、字幕、卡片、比例、导出、commit / push 等，必须实实在在完成仓库写明的目标。\n- DeepSeek 需要真实参与但只有 `fallback_local_only`。\n`mandatory_commit_push_gate（强制提交推送闸门）` 是 Codex 默认完成标准的一部分，不是临时收尾建议。以后任何最小任务只要对仓库文件产生有效改动，`completed（已完成）` 必须等到 Git 收尾完成后才允许写。\nCodex 最终回报必须默认包含：\n正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格；用户不负责替 GPT / Codex 诊断内部原因。\n当用户只反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，至少检查：\n- final_script 是否被 Codex 越权改写。\n发现任一内部问题，Codex 必须修复或 `blocked`，不得把诊断责任转给用户。\n正式运营视频执行前必须先有 `locked_copy_contract（锁定文案契约）`。该契约由 ChatGPT / 用户确认，Codex 只能按它执行，不得擅自改写。\n`codex_copy_authority_boundary（Codex 文案权限边界）`：\n11. `publish_candidate_user_standard_preflight（候选可发布用户标准预检）`：按用户标准区分可接受小瑕疵和重大缺陷；`publish_candidate_ready_for_human_review` 不等于 `send_ready`。\n  status_boundary: publish_candidate_ready_for_human_review_does_not_equal_send_ready\nCodex 在《视频工厂》中可以做执行层推断，但不得凭自己的猜想改变用户 / ChatGPT 已锁定的目标、文案、结构、视觉路线、声音路线、素材证据链、状态结论或商业判断。\n以下属于 `safe_inference（安全推断）`，Codex 可以自行处理，但必须在最终报告写入 `safe_inference\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:\n  action = create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let Codex continue with minimal necessary review\nif state = deepseek_mid_task_incremental_supply_required:\n  action = create incremental_supply_request with current_child_task, files_already_read, will_modify_files, conflict_points, and failed_validation_logs; run mid_task_incremental_supply before continuing\nif state = deepseek_not_deeply_participated:\n  action = mark blocked or deepseek_not_deeply_participated when user required deep participation but DeepSeek real call, relevant_file_bundle, exact_snippet_pack, or mid-task/post risk supply is missing\nif state = deepseek_pre_supply_missing:\n  action = run_deepseek_pre_supply or mark fallback_local_only / blocked before write\nif state = deepseek_post_review_missing:\n  action = run_deepseek_post_risk_review before completion claim\nif state = deepseek_claim_without_token_usage:\n  action = run\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/21_codex_judgment_permission_matrix.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# Codex 判断权限表 codex_judgment_permission_matrix\n`已确认` 本文件是《视频工厂》Codex 执行层的判断权限表。\n1. 哪些判断 Codex 必须自己做，并可以直接执行。\n2. 哪些判断 Codex 必须自己做，但只能输出 `copy_change_request（文案修改请求）`。\n3. 哪些判断 Codex 必须自己做，并在命中风险时 `blocked（阻断）`。\n4. 哪些判断必须升级给 ChatGPT / 用户，Codex 不得擅自拍板。\n本文件不授权 Codex 改写 `locked_topic（锁定选题）`、`locked_title（锁定标题）`、`locked_opening_line（锁定开头句）`、`locked_final_script（锁定最终口播稿）` 的语义、核心判断、数据目标、发布状态或内容通过状态。\n    meaning: Codex 必须判断，并可在不改变锁定文案语义和项目状态的前提下执行。\n    meaning: Codex 必须判断问题是否存在，但一旦需要改文案语义、标题、核心观点或数据目标，只能输出 copy_change_request。\n    meaning: Codex 必须判断是否命中阻断线；命中后不得用技术预览、fallback、普通静态卡片或局部产物冒充完成。\n    meaning: 涉及内容方向、核心观点、标题语义、数据目标拍板、是否可发或主观审美最终判断时，Codex 必须升级。\n      - send_ready\n      - content_validation\n    external_pack_claim: Codex 不应自主判断 opening route\n    project_decision: 本项目中 Codex 必须通过 content_route_inference_function 判断 opening_route_decision\n    boundary: Codex 可判断开头路线，但不能改 locked_opening_line / locked_title / core_claim\n    external_pack_claim: Codex 只能根据判断句触发，不应决定不需要 judgment_card\n    project_decision: 本项目中 Codex 必须判断是否需要 judgment_card；加与不加都必须说明依据\n    project_decision: Codex 必须判断是否需要 summary_card；如果结尾一句话已自然收住，可不强行插卡，但必须说明理由\n    boundary: 总结卡不得写成 content_validation 通过证据\n`已确认` Codex 不能因为本轮 prompt 没点名某个组件，就跳过判断卡、总结卡、结果差卡、边界卡、Prompt 尾卡、TTS 路线、逐句画面对齐、禁止事项或视觉证据可读性判断。\n`已确认` Codex 后续判断正片候选声音路线时，不得把阿里 B 方案继续当默认生成 provider。B 方案升级为 `formal_voice_feel_reference（正式声音听感参考）`；正片候选实际 TTS 必须是 Mini\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
    "file_role": "runner_or_controller",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "#!/usr/bin/env python3\nfrom __future__ import annotations\n\nfrom typing import Any\n\n\nDEFAULT_TTS_PROVIDER_FOR_PUBLISH_CANDIDATE = \"minimax\"\nREQUIRED_MINIMAX_MODELS = {\"speech-2.8-hd\", \"MiniMax/speech-2.8-hd\"}\nMINIMAX_SELECTED_ROUTES = {\n    \"minimax_official_api\",\n    \"aliyun_bailian_proxy_to_minimax\",\n    \"route_a\",\n    \"route_b\",\n}\nB_VOICE_SCHEME_ROLE = {\n    \"status\": \"formal_voice_feel_reference\",\n    \"meaning\": \"B 方案升级为正式声音听感标准，保留停顿梗感、轻陪伴感和低压向导感\",\n    \"not_allowed\": \"不再把阿里 B 方案作为正片候选默认 TTS 生成路线\",\n}\nB_VOICE_FEEL_REQUIRED_TAGS = {\n    \"light_companion\",\n    \"low_pressure\",\n    \"natural_spoken_chinese\",\n    \"b_pacing_feel\",\n    \"subtle_pause_joke_rhythm\",\n    \"game_guide_feeling\",\n    \"not_broadcast\",\n    \"not_sales\",\n    \"not_customer_service\",\n    \"not_childish_cute_voice\",\n}\nB_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE = {\n    \"status\": \"active\",\n    \"b_voice_scheme_role\": \"formal_voice_feel_reference\",\n    \"required_generation_route\": {\n        \"provider_family\": [\"minimax\", \"aliyun_bailian_proxy_to_minimax\"],\n        \"model\": sorted(REQUIRED_MINIMAX_MODELS),\n    },\n    \"required_voice_feel\": sorted(B_VOICE_FEEL_REQUIRED_TAGS),\n    \"forbidden_generation_route\": [\n        \"aliyun_qwen_realtime_websocket_voice_clone_as_publish_candidate\",\n        \"qwen3-tts-vc-realtime-2026-01-15_as_publish_candidate\",\n        \"Serena\",\n        \"macOS_say\",\n        \"local_low_quality_tts\",",
    "excerpt_range_or_marker": "lines:1-45",
    "confidence": "high"
  },
  {
    "path": "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
    "file_role": "runner_or_controller",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "\"content_validation\": \"pending_user_chatgpt_review\",\n        \"send_ready\": False,\n                \"- `content_validation`: `pending_user_chatgpt_review`\",\n                \"- `send_ready`: `false`\",\n            \"send_ready\": False,\n            \"content_validation\": \"pending_user_chatgpt_review\",\n                \"8. 本轮会读取 v2 证据复核报告：是。\",\n                \"- `prompt_delta`: 基于 v2 证据复核继续生成正片候选，不重复阻断已解除素材 blocker。\",",
    "excerpt_range_or_marker": "lines:1265-1272",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/05_文案路由规则.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "用户提供录屏 / 桌面素材进入正式视频执行时，必须优先应用 `source_native_no_mask_visual_rule（源素材比例 + 无遮挡视觉规则）`。该规则优先于旧固定横屏交付口径：除非用户本轮明确指定横屏 16:9 / 1920x1080，Codex 不得为了统一比例强行补灰边、白边、黑边、letterbox、pillarbox 或 padding bands。\n`已确认` 用户提供素材时，默认执行规则是“用户给什么素材，就优先使用什么素材本身”。除非用户本轮明确授权，Codex 不得为了隐私、美观、比例、字幕、卡片或平台风险主动遮挡、洗白、模糊或重塑用户素材。\nCodex 执行视频时不得重新定稿。允许做素材映射、字幕分句、TTS 停顿、剪辑节奏、卡片位置、证据窗口和导出参数；不允许改标题、选题、开头句、核心判断、人味表达、语义或视觉标题卡标题。若需要改文案，必须输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认。\n文案进入视频执行链路后，GPT prompt 只代表本轮 `prompt_delta（增量目标）`，不代表完整流程源。Codex 必须先跑 `process_boot_gate（流程启动闸门）`，输出 `process_boot_report（流程启动报告）`，再决定能否进入素材映射、TTS、字幕、卡片、时间线或审片包执行。\n- 若组件判断需要改 locked 文案语义，Codex 只能输出 `copy_change_request（文案修改请求）` 或 blocked。\n- `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 不等于 `send_ready = true`；`send_ready` 必须等待用户或 ChatGPT 最终确认。\n3. `Codex（执行代理）` 做素材技术检查与细节证据报告。\n4. `ChatGPT（最终落稿与复审入口）` 基于参考包、用户素材和 `Codex（执行代理）` 细节报告写最终落稿。\n5. `Codex（执行代理）` 按最终稿执行视频、字幕、声音、卡片和审片包。\n   - 执行完成后回到 `ChatGPT（最终落稿与复审入口）` 复审；`publish_candidate` 不等于 `send_ready`。\n- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。\n- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，Codex 不得进入视频执行。\n- ChatGPT 读取 `V003_next_copy_revision_brief.md` 后负责最终判断、汇报和改稿；Codex 只负责记录、结构化、生成报告和验证。\n## 3B. `Codex（执行代理）` 素材细节汇报标准\n`Codex（执行代理）` 检查素材时，必须按“给 `ChatGPT（最终落稿与复审入口）` 写最终稿”的标准汇报。\n- 示例包括：`Codex 在屏幕上打字`、点击确认、搜索商品、翻商品卡、记录商品名、价格、佣金、销量信号、店铺分、商品分、风险，写入云盘表格，最后回到聊天框给结论。\n- 不得写成\n...[truncated]",
    "excerpt_range_or_marker": "lines:13-30",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/07_AI知识类视频价值规则.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `ChatGPT（最终落稿与复审入口）` 写最终稿时，必须基于 `Codex（执行代理）` 的素材细节报告校准页面、按钮、动作和结果。\n- AI / Codex 在真实屏幕上打字。\n- AI / Codex 自动点击、搜索、筛选。\n- AI / Codex 翻商品卡。\n- AI / Codex 读取价格、佣金、销量、评分、风险。\n- AI / Codex 把乱商品整理成表。\n- AI / Codex 把结果传到云盘，形成云盘表格或文件。\n- AI / Codex 回到聊天框给清楚结论。\n- AI / Codex 说出哪个商品更适合用户、理由、风险和下一步。\n- 执行型 AI / 专家模式 / Codex 能接手一段具体工作。\nCodex 帮我筛选商品。\n你以为做带货最难的是拍视频，其实第一步就卡在：你根本不知道哪个商品值得测。佣金高的不一定适合你，销量好的可能太卷，内容好拍的也可能退货风险高。所以我让 Codex 先替我跑一轮初筛，把一堆商品卡整理成我能判断的复查表。\n本标准只提升话语价值，不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n- AI / Codex 出现时是不是救场，而不是产品介绍。\n进入视频执行前，Codex 必须把 `material_detail_report（素材细节报告）` 转成 `material_evidence_contract（素材证据契约）`，并逐个 `line_group（句组）` 运行 `line_group_evidence_gate（句组证据闸门）`：\n1. 商品卡、候选表、明细表、复查表、聊天框结论是“Codex 选品初筛”类视频的价值主体，必须尽量保留结构可读。\nAI 知识类视频的 `publish_candidate（发片候选）` 必须同时看技术完整性、证据可读性、卡片 / 字幕不遮挡、TTS 韵律、人感顺滑、平台风险和审片包完整性。卡片好看、视频生成成功、TTS 文件存在、技术检查通过，都不等于 `content_validation（内容验证）` 通过。\n- `review_pack（审片包）` 能让 ChatGPT / 用户复核标题、文案、画面、声音、字幕、卡片、证据和剩余阻断。\n- `near_equivalent_material_substitution_report（近似素材替代报告）` 已输出并可复核；主题相近不能替代证据相近，素材无法支撑文案时必须 blocked 等待补素材。\n- `content_validation` 只能由 ChatGPT / 用户最终复审或明确规则链路推进；技术成功不得自动推进。\n- `send_ready`、`voice_validation`、`visual_master_locked`、`current_data_goal_anchor_ready` 不得由发片候选机制自动推进。\n- `publish_candidate_user_standard_preflight`\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/08_当前正式事实.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `已确认` 正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标和结果合格反馈；GPT / Codex 负责内部执行问题自查与修复，不得把内部排障责任转给用户。\n- `已确认` Codex 不得降级完成任何正式运营交付任务。凡仓库写明的目标、产物、验证、同步、回报未全部完成，必须 `blocked` 或继续修到满足基线，不得用 fallback、技术预览、局部结果、内部诊断或本地未同步产物冒充 `completed`。\n- `待验证` 本机制写入不代表当前所有执行问题已经解决，不代表当前视频已通过，不代表 Codex 后续永远不会再错，也不代表机制长期稳定；后续真实任务仍必须按闸门验证。\n- `已确认` ChatGPT / 用户是最终落稿和文案锁定入口；Codex 是执行层，不得擅自改标题、选题、开头句、核心判断、人味表达、文案语义或视觉标题卡标题。\n- `已确认` Codex 如判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能自行改稿。\n- `未推进` 本事实只修机制，不代表当前已发布视频内容通过，不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n- `未推进` 运营决策系统落地不代表内容成功、方向成立、商业验证成立或数据飞轮真实跑通；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`，也不把 `current_data_goal_anchor` 写成 `ready`。\n## 0E. 2026-05-16 Codex 判断权限表与 HyperFrames 卡片基线事实\n- `已确认` 本轮新增 `codex_source/21_codex_judgment_permission_matrix.md（Codex 判断权限表）`，用于区分 Codex 必须判断并执行、必须判断但只能请求改文案、必须判断并阻断、必须升级给 ChatGPT / 用户的边界。\n- `已确认` Codex 必须自行判断低风险、可逆、可验证的执行细节，包括 `opening_route_decision（开头路由判断）`、`card_placement_decision（卡片位置判断）`、`script_to_timeline_map（文案到时间线映射）`、`subtitle_segmentation（字幕分句）`、`tts_prosody（TTS 韵律）`、`aspect_ratio_resolution（比例与分辨率）` 和 `publish_candidate_readiness（可发布候选片准备状态）`。\n- `已确认` Codex 不得擅自改写 `locked_topic（锁定选题）`、`locked_title（锁定标题）`、`locked_opening_line（锁定开头句）`、\n...[truncated]",
    "excerpt_range_or_marker": "lines:23-34",
    "confidence": "high"
  },
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `can_continue_to_publish_candidate_generation = true`；`remaining_material_needed = []`；未重复阻断已解除的 `Codex / Atlas 操作电脑`、截图式商品卡处理、SKU 风险、候选表 / 明细表 / 复查表素材 blocker。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`visual_master_locked = false`。\n## 20260526｜新第四期选品初筛素材证据复核\n- `status_boundary`：未推进 `send_ready / content_validation / voice_validation / final_voice_validated / visual_master_locked`。\n- `日志`：`codex_log/20260526_新第四期选品初筛素材证据复核_evidence_reclassification.md`\n- `visual_blocker`：现有素材不能无猜测证明“Codex 操作我的电脑 / 进入选品页面 / 输入品类词 / 一张一张翻商品卡”；候选表、明细表、复查表存在小字/隐私/遮挡可读性风险；SKU 复杂度缺少清楚证据。\n- `copy_blocker`：旧 preflight 已要求相关句子走 `copy_change_request`，但本轮锁稿禁止 Codex 改稿，因此 blocked。\n- `content_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`final_voice_validated = false`；`visual_master_locked = false`；`current_data_goal_anchor_ready = false`。\n- `route_decision（路由判断）`：`project_route = video_factory`；`task_type = mechanism_or_route_fix + project_file_change + code_debug + fixture_or_test_change`；`large_task_gate = triggered`；`lane = audit_lane -> standard_lane`；`parallel = serial_only`；`write_owner = Code\n...[truncated]",
    "excerpt_range_or_marker": "lines:11-20",
    "confidence": "high"
  },
  {
    "path": "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- 降低或复核 `speed`，优先试 `1.0-1.08` 区间。",
    "excerpt_range_or_marker": "lines:125-125",
    "confidence": "high"
  }
]
```

## exact_snippet_pack（关键原文片段包）

```json
[
  {
    "path": "AGENTS.md",
    "snippet": "- 需要 GPT Project 上传包地址时，必须先读取 `codex_log/current_local_artifact_paths.md` 或由 Codex 本地审计后给出。\n  - `Codex（唯一写入执行层 / Integrator）`\n  - `DeepSeek（每轮默认只读供料层 / Explorer）`\n- 当前最高机制入口已包含 `Project State Action Router（项目状态动作总控器）`：命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审时，先读 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md`，输出 `state_action_router（项目状态动作总控器）` 后再执行。\n- `DeepSeek（每轮默认只读供料层 / Explorer）` 每轮默认做执行前供料和执行后风险复核，输出上下文压缩、必读文件地图、风险冲突报告、遗漏同步检查和 Codex 下一步输入；不写文件、不拍板项目事实。\n- `Codex（唯一写入执行层 / Integrator）` 默认负责复核原文件、整合 DeepSeek 供料、补齐受影响文件 / 字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、日志和 Git 收尾。\n- Codex 收到 ChatGPT 完整执行单、横向补全包、多文件机制修补或“不要只做一半 / 执行到底”类任务时，必须触发 `Completion Relay Gate（补全接力闸门）`，先生成 `required_output_inventory（必须交付清单）` 与 `child_task_graph（子任务树）`，再执行并做 `remaining_work_check（剩余工作检查）`。\n- `content_validation = not_advanced_by_formal_operation（正式运营不等于内容最终通过；不得写成内容通过）`",
    "why_it_matters": "readonly_context for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "snippet": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。\n- Codex 不得把本地生成当已 push。",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/01_execution_rules.md",
    "snippet": "# Codex 执行规则\n命中截图、平台数据、评论、私信、咨询、复盘或下一轮变量判断时，Codex 必须优先读取：\n本覆盖口径不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n当前进入 `formal_operation_active（正式运营中）` 后，Codex 在 `route_decision（路由判断）` 阶段必须判断本轮是否是视频交付任务。\nCodex 后续不得降级处理正式运营任务。凡任务目标指向做视频、产视频、发片候选、运营内容、下一条视频、发布候选、项目机制落库、GPT Project 同步、数据录入、复盘记录、素材审计、文案到执行映射、TTS、字幕、卡片、比例、导出、commit / push 等，必须实实在在完成仓库写明的目标。\n- DeepSeek 需要真实参与但只有 `fallback_local_only`。\n`mandatory_commit_push_gate（强制提交推送闸门）` 是 Codex 默认完成标准的一部分，不是临时收尾建议。以后任何最小任务只要对仓库文件产生有效改动，`completed（已完成）` 必须等到 Git 收尾完成后才允许写。\nCodex 最终回报必须默认包含：",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "snippet": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:\n  action = create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let Codex continue with minimal necessary review",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/21_codex_judgment_permission_matrix.md",
    "snippet": "# Codex 判断权限表 codex_judgment_permission_matrix\n`已确认` 本文件是《视频工厂》Codex 执行层的判断权限表。\n1. 哪些判断 Codex 必须自己做，并可以直接执行。\n2. 哪些判断 Codex 必须自己做，但只能输出 `copy_change_request（文案修改请求）`。\n3. 哪些判断 Codex 必须自己做，并在命中风险时 `blocked（阻断）`。\n4. 哪些判断必须升级给 ChatGPT / 用户，Codex 不得擅自拍板。\n本文件不授权 Codex 改写 `locked_topic（锁定选题）`、`locked_title（锁定标题）`、`locked_opening_line（锁定开头句）`、`locked_final_script（锁定最终口播稿）` 的语义、核心判断、数据目标、发布状态或内容通过状态。\n    meaning: Codex 必须判断，并可在不改变锁定文案语义和项目状态的前提下执行。",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
    "snippet": "#!/usr/bin/env python3\nfrom __future__ import annotations\n\nfrom typing import Any\n\n\nDEFAULT_TTS_PROVIDER_FOR_PUBLISH_CANDIDATE = \"minimax\"\nREQUIRED_MINIMAX_MODELS = {\"speech-2.8-hd\", \"MiniMax/speech-2.8-hd\"}",
    "why_it_matters": "runner_or_controller for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
    "snippet": "\"content_validation\": \"pending_user_chatgpt_review\",\n        \"send_ready\": False,\n                \"- `content_validation`: `pending_user_chatgpt_review`\",\n                \"- `send_ready`: `false`\",\n            \"send_ready\": False,\n            \"content_validation\": \"pending_user_chatgpt_review\",\n                \"8. 本轮会读取 v2 证据复核报告：是。\",\n                \"- `prompt_delta`: 基于 v2 证据复核继续生成正片候选，不重复阻断已解除素材 blocker。\",",
    "why_it_matters": "runner_or_controller for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/05_文案路由规则.md",
    "snippet": "用户提供录屏 / 桌面素材进入正式视频执行时，必须优先应用 `source_native_no_mask_visual_rule（源素材比例 + 无遮挡视觉规则）`。该规则优先于旧固定横屏交付口径：除非用户本轮明确指定横屏 16:9 / 1920x1080，Codex 不得为了统一比例强行补灰边、白边、黑边、letterbox、pillarbox 或 padding bands。\n`已确认` 用户提供素材时，默认执行规则是“用户给什么素材，就优先使用什么素材本身”。除非用户本轮明确授权，Codex 不得为了隐私、美观、比例、字幕、卡片或平台风险主动遮挡、洗白、模糊或重塑用户素材。\nCodex 执行视频时不得重新定稿。允许做素材映射、字幕分句、TTS 停顿、剪辑节奏、卡片位置、证据窗口和导出参数；不允许改标题、选题、开头句、核心判断、人味表达、语义或视觉标题卡标题。若需要改文案，必须输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认。\n文案进入视频执行链路后，GPT prompt 只代表本轮 `prompt_delta（增量目标）`，不代表完整流程源。Codex 必须先跑 `process_boot_gate（流程启动闸门）`，输出 `process_boot_report（流程启动报告）`，再决定能否进入素材映射、TTS、字幕、卡片、时间线或审片包执行。\n- 若组件判断需要改 locked 文案语义，Codex 只能输出 `copy_change_request（文案修改请求）` 或 blocked。\n- `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 不等于 `send_ready = true`；`send_ready` 必须等待用户或 ChatGPT 最终确认。\n3. `Codex（执行代理）` 做素材技术检查与细节证据报告。\n4. `ChatGPT（最终落稿与复审入口）` 基于参考包、用户素材和 `Codex（执行代理）` 细节报告写最终落稿。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/07_AI知识类视频价值规则.md",
    "snippet": "- `ChatGPT（最终落稿与复审入口）` 写最终稿时，必须基于 `Codex（执行代理）` 的素材细节报告校准页面、按钮、动作和结果。\n- AI / Codex 在真实屏幕上打字。\n- AI / Codex 自动点击、搜索、筛选。\n- AI / Codex 翻商品卡。\n- AI / Codex 读取价格、佣金、销量、评分、风险。\n- AI / Codex 把乱商品整理成表。\n- AI / Codex 把结果传到云盘，形成云盘表格或文件。\n- AI / Codex 回到聊天框给清楚结论。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/08_当前正式事实.md",
    "snippet": "- `已确认` 正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标和结果合格反馈；GPT / Codex 负责内部执行问题自查与修复，不得把内部排障责任转给用户。\n- `已确认` Codex 不得降级完成任何正式运营交付任务。凡仓库写明的目标、产物、验证、同步、回报未全部完成，必须 `blocked` 或继续修到满足基线，不得用 fallback、技术预览、局部结果、内部诊断或本地未同步产物冒充 `completed`。\n- `待验证` 本机制写入不代表当前所有执行问题已经解决，不代表当前视频已通过，不代表 Codex 后续永远不会再错，也不代表机制长期稳定；后续真实任务仍必须按闸门验证。\n- `已确认` ChatGPT / 用户是最终落稿和文案锁定入口；Codex 是执行层，不得擅自改标题、选题、开头句、核心判断、人味表达、文案语义或视觉标题卡标题。\n- `已确认` Codex 如判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能自行改稿。\n- `未推进` 本事实只修机制，不代表当前已发布视频内容通过，不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n- `未推进` 运营决策系统落地不代表内容成功、方向成立、商业验证成立或数据飞轮真实跑通；不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`，也不把 `current_data_goal_anchor` 写成 `ready`。\n## 0E. 2026-05-16 Codex 判断权限表与 HyperFrames 卡片基线事实",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/latest.md",
    "snippet": "- `can_continue_to_publish_candidate_generation = true`；`remaining_material_needed = []`；未重复阻断已解除的 `Codex / Atlas 操作电脑`、截图式商品卡处理、SKU 风险、候选表 / 明细表 / 复查表素材 blocker。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`visual_master_locked = false`。\n## 20260526｜新第四期选品初筛素材证据复核\n- `status_boundary`：未推进 `send_ready / content_validation / voice_validation / final_voice_validated / visual_master_locked`。\n- `日志`：`codex_log/20260526_新第四期选品初筛素材证据复核_evidence_reclassification.md`\n- `visual_blocker`：现有素材不能无猜测证明“Codex 操作我的电脑 / 进入选品页面 / 输入品类词 / 一张一张翻商品卡”；候选表、明细表、复查表存在小字/隐私/遮挡可读性风险；SKU 复杂度缺少清楚证据。\n- `copy_blocker`：旧 preflight 已要求相关句子走 `copy_change_request`，但本轮锁稿禁止 Codex 改稿，因此 blocked。\n- `content_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review_if_future_candidate_generated`；`final_voice_validated = false`；`visual_master_locked = false`；`current_data_goal_anchor_ready = false`。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md",
    "snippet": "- 降低或复核 `speed`，优先试 `1.0-1.08` 区间。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  }
]
```

## dependency_map（依赖映射）

```json
[
  {
    "source_file": "AGENTS.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/00_codex_readme.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/01_execution_rules.md",
    "depends_on": [],
    "dependency_type": "execution_rules_reference_controller_protocol",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/19_project_state_action_router.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/21_codex_judgment_permission_matrix.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/05_文案路由规则.md",
    "depends_on": [
      "codex_source/00_codex_readme.md",
      "codex_source/01_execution_rules.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/21_codex_judgment_permission_matrix.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/07_AI知识类视频价值规则.md",
    "depends_on": [
      "codex_source/00_codex_readme.md",
      "codex_source/01_execution_rules.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/21_codex_judgment_permission_matrix.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/08_当前正式事实.md",
    "depends_on": [
      "codex_source/00_codex_readme.md",
      "codex_source/01_execution_rules.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/21_codex_judgment_permission_matrix.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/latest.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  }
]
```

## risk_delta_report（增量风险报告）

```json
[
  {
    "risk_type": "fallback_mislabel_risk",
    "path": "deepseek_supply_pack",
    "evidence": "supply_source is not deepseek_passed",
    "severity": "high",
    "suggested_codex_action": "do_not_claim_completed_if_user_required_deepseek"
  }
]
```

## missing_or_uncertain_files（缺失或不确定文件）

```json
[
  {
    "path_or_query": "Need verify current MiniMax/DashScope route can still call get_voice and synthesize short non-silent samples with selected voice_id values.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Need determine whether current route can use reference_audio / voice_clone from local B reference audio, or whether it requires public audio_url / official MiniMax API file upload outside this task's safe scope.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Need add executable voice identity gate so b_voice_feel_reflected=true cannot pass without actual voice_id match and human_voice_review_status=user_confirmed.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Need ensure generated samples are pending_user_review only, not user_confirmed or voice_validation passed.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  }
]
```

## editing_decision_pack（剪辑决策包）

```json
null
```

## execution_supply_pack（执行供料包）

```json
null
```

## post_risk_review（执行后风险复核）

```json
null
```

## codex_next_input（给 Codex 的下一步输入）

```json
{
  "read_first": [
    "AGENTS.md",
    "codex_source/00_codex_readme.md",
    "codex_source/01_execution_rules.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/21_codex_judgment_permission_matrix.md",
    "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
    "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py",
    "GPT数据源/05_文案路由规则.md"
  ],
  "use_as": "readonly_supply_pack",
  "warning": "This pack is local fallback, not a DeepSeek conclusion.",
  "recommended_child_tasks": [
    "update_deep_file_supply_contract",
    "update_controller_schema_fixture",
    "run_validation_and_truth_check"
  ],
  "files_codex_must_review": [
    "scripts/正片候选TTS路线_publish_candidate_tts_route.py",
    "scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py"
  ],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "AGENTS.md",
    "codex_source/00_codex_readme.md",
    "codex_source/01_execution_rules.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/21_codex_judgment_permission_matrix.md",
    "GPT数据源/05_文案路由规则.md",
    "GPT数据源/07_AI知识类视频价值规则.md",
    "GPT数据源/08_当前正式事实.md",
    "codex_log/latest.md",
    "codex_log/diagnostics/tts_voice_audit_20260526_234902/tts_voice_identity_audit.md"
  ],
  "blocked_conditions": [
    "deepseek_actual_required_but_not_deepseek_passed",
    "relevant_file_bundle_missing",
    "exact_snippet_pack_missing",
    "validation_failed_files_not_reviewed_by_codex"
  ]
}
```

## not_allowed（禁止事项）

```json
[
  "Do not treat fallback_local_only as a DeepSeek conclusion.",
  "Do not claim DeepSeek is stable production supply.",
  "Do not claim multi-agent runtime is running.",
  "Do not let DeepSeek write files or decide project facts.",
  "Do not read .env, API keys, media files, or dist/latest_review_pack/.",
  "Do not call Aliyun or other real generation APIs in mechanism-only tests."
]
```
