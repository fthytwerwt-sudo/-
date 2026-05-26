# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260526T091743Z`
- `request_id`: `20260526_new_fourth_locked_script_publish_candidate_pre_supply`
- `request_validation_status`: `passed`
- `task_type`: `locked_copy_video_execution + publish_candidate_delivery + final_script_to_video + tts_route_execution`
- `trigger_reason`: `mandatory_pre_supply`
- `action`: `risk_report`
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
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260526_new_fourth_locked_script_publish_candidate_pre_supply_request.json",
  "current_goal": "Generate or block the locked-script new fourth episode selection-screening publish candidate without degradation.",
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
  "current_step": "preflight before any media completion claim",
  "known_context": [
    "Current project is 视频工厂 and formal_operation_active.",
    "Target delivery is publish_candidate_ready_for_human_review; degradation is forbidden.",
    "Locked final script in the user execution order cannot be semantically changed, compressed, reordered, or replaced with old v0.2 copy.",
    "Formal TTS route must be MiniMax speech-2.8-hd or MiniMax/speech-2.8-hd.",
    "Existing material audit says V001/V003/V004 support product-card to table to review-list workflow, but table readability and privacy risks remain.",
    "Existing old preflight had copy_change_request for direct computer operation phrasing; the current locked script forbids changing that phrase."
  ],
  "missing_context": [
    "Whether the locked phrase 'Codex 操作我的电脑' has direct enough visual evidence in current source videos.",
    "Whether the current data_goal_anchor partial_data_recorded state blocks this formal video execution.",
    "Whether MiniMax full-length TTS can generate non-silent narration for the complete locked script in this runtime.",
    "Whether the full locked script can be line-group mapped without unsupported core evidence claims."
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
  "request_id": "20260526_new_fourth_locked_script_publish_candidate_pre_supply",
  "task_id": "",
  "mandatory_for_every_task": true,
  "participation_level": "deep_file_prefetch",
  "pre_supply_required": true,
  "post_review_required": true,
  "codex_vertical_completion_required": true,
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
  "fallback_allowed": true,
  "fallback_not_completion": true,
  "user_explicit_deepseek_required": false,
  "deepseek_must_not_be_skipped_by_codex_discretion": true,
  "current_goal": "Generate or block the locked-script new fourth episode selection-screening publish candidate without degradation.",
  "current_step": "preflight before any media completion claim",
  "known_context": [
    "Current project is 视频工厂 and formal_operation_active.",
    "Target delivery is publish_candidate_ready_for_human_review; degradation is forbidden.",
    "Locked final script in the user execution order cannot be semantically changed, compressed, reordered, or replaced with old v0.2 copy.",
    "Formal TTS route must be MiniMax speech-2.8-hd or MiniMax/speech-2.8-hd.",
    "Existing material audit says V001/V003/V004 support product-card to table to review-list workflow, but table readability and privacy risks remain.",
    "Existing old preflight had copy_change_request for direct computer operation phrasing; the current locked script forbids changing that phrase."
  ],
  "missing_context": [
    "Whether the locked phrase 'Codex 操作我的电脑' has direct enough visual evidence in current source videos.",
    "Whether the current data_goal_anchor partial_data_recorded state blocks this formal video execution.",
    "Whether MiniMax full-length TTS can generate non-silent narration for the complete locked script in this runtime.",
    "Whether the full locked script can be line-group mapped without unsupported core evidence claims."
  ],
  "decision_needed": "",
  "expected_output": [
    "risk_and_conflict_report",
    "missing_or_uncertain_files",
    "codex_next_input",
    "not_deepseek_conclusion_if_fallback"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "output_dir": "dist/deepseek_supply_controller/20260526_new_fourth_locked_script_publish_candidate_pre_supply",
    "required_fields": [
      "deepseek_actual_participation",
      "fallback_status",
      "not_deepseek_conclusion",
      "token_usage_observed_or_user_check_required",
      "risk_and_conflict_report",
      "codex_next_input"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "DeepSeek writes files.",
    "Secret value appears in output.",
    "Fallback is reported as real DeepSeek participation.",
    "Risk report claims content validation passed."
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not read or expose API keys, tokens, secrets, .env, or local runtime config values.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime or 多 agent runtime is running just because a supply request exists.",
    "Do not approve publish_candidate_ready_for_human_review without Codex verification."
  ]
}

## files_considered（已考虑文件）

```json
[
  "AGENTS.md",
  "codex_source/00_codex_readme.md",
  "codex_source/01_execution_rules.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/21_codex_judgment_permission_matrix.md",
  "codex_log/current_data_goal_anchor.md",
  "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
  "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md"
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
  "codex_log/current_data_goal_anchor.md",
  "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
  "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md"
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
  "enabled": false,
  "modes": [],
  "missing_modes": [
    "mid_task_incremental_supply",
    "post_risk_review",
    "deep_file_prefetch"
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
    "content_excerpt": "- 需要 GPT Project 上传包地址时，必须先读取 `codex_log/current_local_artifact_paths.md` 或由 Codex 本地审计后给出。\n  - `Codex（唯一写入执行层 / Integrator）`\n  - `DeepSeek（每轮默认只读供料层 / Explorer）`\n- 当前最高机制入口已包含 `Project State Action Router（项目状态动作总控器）`：命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审时，先读 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md`，输出 `state_action_router（项目状态动作总控器）` 后再执行。\n- `DeepSeek（每轮默认只读供料层 / Explorer）` 每轮默认做执行前供料和执行后风险复核，输出上下文压缩、必读文件地图、风险冲突报告、遗漏同步检查和 Codex 下一步输入；不写文件、不拍板项目事实。\n- `Codex（唯一写入执行层 / Integrator）` 默认负责复核原文件、整合 DeepSeek 供料、补齐受影响文件 / 字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、日志和 Git 收尾。\n- Codex 收到 ChatGPT 完整执行单、横向补全包、多文件机制修补或“不要只做一半 / 执行到底”类任务时，必须触发 `Completion Relay Gate（补全接力闸门）`，先生成 `required_output_inventory（必须交付清单）` 与 `child_task_graph（子任务树）`，再执行并做 `remaining_work_check（剩余工作检查）`。\n- `content_validation = not_advanced_by_formal_operation（正式运营不等于内容最终通过；不得写成内容通过）`\n- `send_ready = false`\n- 上述 `content_validation` 是当前发布后阶段口径；不得把它写成 `passed`\n以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。\n- 不允许把 `technical_validati\n...[truncated]",
    "excerpt_range_or_marker": "lines:73-85",
    "confidence": "high"
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。\n- Codex 不得把本地生成当已 push。\n- Codex 不得把技术成功当内容成功。\n- Codex 不得把“没有明确失败”当完成。\nCodex 在视频执行中负责素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，不负责重新定稿。Codex 可以改标点、换行、字幕分句和 TTS 停顿，但不得改变语义、人味、标题语气、核心判断、前台表达角度，不能用视觉标题卡替换 `locked_title`。\n如果 Codex 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，等待 ChatGPT / 用户确认，不得自行改稿。\n以后凡是任务命中 `publish_candidate（发片候选）`、`video_execution（视频执行）`、`repair_candidate（修片候选）`、`regenerate_video（重新生成视频）`、`pre_publish_fix（发布前修复）`、`final_script_to_video（最终文案进入视频）`，或涉及 `TTS / subtitle / card / timeline / review_pack / privacy_mask / aspect_ratio / visual_evidence` 任一视频执行组件，Codex 必须先跑 `process_boot_gate（流程启动闸门）`。\n- `process_boot_gate` 只防止执行断层，不推进 `co\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/01_execution_rules.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# Codex 执行规则\n命中截图、平台数据、评论、私信、咨询、复盘或下一轮变量判断时，Codex 必须优先读取：\n本覆盖口径不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n当前进入 `formal_operation_active（正式运营中）` 后，Codex 在 `route_decision（路由判断）` 阶段必须判断本轮是否是视频交付任务。\nCodex 后续不得降级处理正式运营任务。凡任务目标指向做视频、产视频、发片候选、运营内容、下一条视频、发布候选、项目机制落库、GPT Project 同步、数据录入、复盘记录、素材审计、文案到执行映射、TTS、字幕、卡片、比例、导出、commit / push 等，必须实实在在完成仓库写明的目标。\n- DeepSeek 需要真实参与但只有 `fallback_local_only`。\n`mandatory_commit_push_gate（强制提交推送闸门）` 是 Codex 默认完成标准的一部分，不是临时收尾建议。以后任何最小任务只要对仓库文件产生有效改动，`completed（已完成）` 必须等到 Git 收尾完成后才允许写。\nCodex 最终回报必须默认包含：\n正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格；用户不负责替 GPT / Codex 诊断内部原因。\n当用户只反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，至少检查：\n- final_script 是否被 Codex 越权改写。\n发现任一内部问题，Codex 必须修复或 `blocked`，不得把诊断责任转给用户。\n正式运营视频执行前必须先有 `locked_copy_contract（锁定文案契约）`。该契约由 ChatGPT / 用户确认，Codex 只能按它执行，不得擅自改写。\n`codex_copy_authority_boundary（Codex 文案权限边界）`：\n11. `publish_candidate_user_standard_preflight（候选可发布用户标准预检）`：按用户标准区分可接受小瑕疵和重大缺陷；`publish_candidate_ready_for_human_review` 不等于 `send_ready`。\n  status_boundary: publish_candidate_rea\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:\n  action = create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let Codex continue with minimal necessary review\nif state = deepseek_mid_task_incremental_supply_required:\n  action = create incremental_supply_request with current_child_task, files_already_read, will_modify_files, conflict_points, and failed_validation_logs; run mid_task_incremental_supply before continuing\nif state = deepseek_not_deeply_participated:\n  action = mark blocked or deepseek_not_deeply_participated when user required deep participation but DeepSeek real call, relevant_file_bundle, exact_snippet_pack, or mid-task/post risk supply is missing\nif state = deepseek_pre_supply_missing:\n  action = run_deepseek_pre_supply or mark fallback_lo\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/21_codex_judgment_permission_matrix.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# Codex 判断权限表 codex_judgment_permission_matrix\n`已确认` 本文件是《视频工厂》Codex 执行层的判断权限表。\n1. 哪些判断 Codex 必须自己做，并可以直接执行。\n2. 哪些判断 Codex 必须自己做，但只能输出 `copy_change_request（文案修改请求）`。\n3. 哪些判断 Codex 必须自己做，并在命中风险时 `blocked（阻断）`。\n4. 哪些判断必须升级给 ChatGPT / 用户，Codex 不得擅自拍板。\n本文件不授权 Codex 改写 `locked_topic（锁定选题）`、`locked_title（锁定标题）`、`locked_opening_line（锁定开头句）`、`locked_final_script（锁定最终口播稿）` 的语义、核心判断、数据目标、发布状态或内容通过状态。\n    meaning: Codex 必须判断，并可在不改变锁定文案语义和项目状态的前提下执行。\n    meaning: Codex 必须判断问题是否存在，但一旦需要改文案语义、标题、核心观点或数据目标，只能输出 copy_change_request。\n    meaning: Codex 必须判断是否命中阻断线；命中后不得用技术预览、fallback、普通静态卡片或局部产物冒充完成。\n    meaning: 涉及内容方向、核心观点、标题语义、数据目标拍板、是否可发或主观审美最终判断时，Codex 必须升级。\n      - send_ready\n      - content_validation\n    external_pack_claim: Codex 不应自主判断 opening route\n    project_decision: 本项目中 Codex 必须通过 content_route_inference_function 判断 opening_route_decision\n    boundary: Codex 可判断开头路线，但不能改 locked_opening_line / locked_title / core_claim\n    external_pack_claim: Codex 只能根据判断句触发，不应决定不需要 judgment_card\n    project_decision: 本项目中 Codex 必须判断是否需要 judgment_card；加与不加都必须说明依据\n    project_decision: Codex 必须判断是否需要 summary_card；如果结尾一句话已自然收住，可不强行插卡，但必须说明理由\n    boundary: 总结卡不得写成 content_validation 通过证据\n`已确认` Codex 不能\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/current_data_goal_anchor.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- 给 ChatGPT / GPT Project / Codex / DeepSeek 提供稳定的当前锚点入口。\n- 防止 Codex 每次从 `video_goal_card`、`post_publish_review_card`、`data_flywheel_memory` 和 `content_structure_feedback_card` 里现场拼锚点。\n      note: \"本轮不得进入正式 Codex 视频执行。\"\n      - \"DeepSeek supply request\"\n      - \"content_validation\"\n      - \"send_ready\"\n1. 命中文案修改、下一条视频、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步时，必须先读取本文件。\n4. Codex 可归档截图和整理早期数据，但不得改写本文件里已锁定的数据目标字段。\n5. 缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。\n- `不适用` 本轮不做内容复审，不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。",
    "excerpt_range_or_marker": "lines:9-18",
    "confidence": "high"
  },
  {
    "path": "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- boundary: `technical_material_audit（技术素材审计）only; content_validation（内容验证）not advanced`\n| S-V001-01 | V001 `内建视网膜显示器 2026-05-23 20-57-41.mp4` | 00:00 | 00:12 | 12s | ChatGPT/Atlas 或浏览器窗口与选品页面并列，像是在整理当前任务和材料。 | 画面文字较小，部分可见 “Atlas / Computer Use / Codex” 类上下文。 | no_audio_track | 从对话/材料切回选品页面前的准备。 | weak_or_context_only | weak | 支撑“这是一次有 AI 辅助的选品过程录屏”。 | 不能支撑商品判断或电商动作。 | 开头背景/工作流铺垫，不宜做核心证据。 | 信息密度低，文字小。 |\n| S-V001-02 | V001 | 00:15 | 01:24 | 69s | 抖音/巨量百应选品广场页面；搜索框输入类似“键帽”，展示多张商品卡、筛选项、价格/佣金/月销等卡片字段。 | 可见“选品广场”、搜索词、商品卡、佣金/到手价/月销字段；具体数值 `uncertain`。 | no_audio_track | 搜索/浏览商品方向，先看商品卡字段。 | product_page_evidence + workflow_process_evidence | strong | 可支撑“选品前先看商品卡字段，不要凭大品类感觉拍板”。 | 不能证明这些商品能卖或佣金能覆盖成本。 | 中段第一证据：展示从大方向进入商品卡筛选。 | 公开展示需遮挡账号/平台侧栏；具体商品名/金额需复核。 |\n| S-V001-03 | V001 | 01:27 | 01:33 | 6s | ChatGPT/Atlas 对刚才画面做文字分析。 | 提到类似“高客单键帽”“25% 佣金”“单笔约 34.7”“需要核红”“找杯具”等，`uncertain`。 | no_audio_track | 用 AI 把商品卡信息转成风险提醒和下一步搜索方向。 | workflow_process_evidence | medium | 可支撑“AI 负责整理复核点，不直接替你判定成功”。 | 不能证明 AI 判断完全正确。 | 可用作转场：商品卡 -> 复核问题。 | AI 文本不是平台事实。 |\n| S-V001-05 | V001 | 02:12 | 03:24 | 72s | ChatGPT 输出和商品页来回切换；多次出现 AI 结论与页面商品卡。 | 文字提到高客单、佣金、样本、SKU/兼容风险、继续找更窄方向，`uncertain`。 | no_audio_track | 从商品\n...[truncated]",
    "excerpt_range_or_marker": "lines:4-9",
    "confidence": "high"
  },
  {
    "path": "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- boundary: `technical_material_audit only; content_validation not advanced`\n| A001 | 选品前先不要问“哪个品能赚”，先打开商品卡，看 `客单价 / 佣金 / 月销或销量信号 / 店铺分 / 商品分 / 退货风险`。 | V001 商品卡页面；V003 明细表字段 | V001 00:15-02:09；V003 00:51-01:30 | 画面明确展示选品页商品卡和明细表字段，能把“凭感觉选品”改成“先看字段”。 | 小字和数值需复核；不能把字段存在写成事实准确。 | high |\n| A005 | 复盘/下一步只补查 4 个商品卡，不要继续无限刷：按优先级逐个核验样品、店铺、佣金、SKU、合规。 | V004 “先确认 4 个商品卡”与优先级表 | V004 00:27-00:51 | 画面直接给出“先确认 4 个商品卡”和复查重点，是最清楚的行动锚点。 | 4 个商品名称/金额需复核；不等于确定上架。 | high |\n| A007 | 商品页拆解时，把 `卖点 / 人群 / 风险 / 内容角度` 分开写进 reason/evidence_note，而不是只抄标题。 | V003 明细表 reason/evidence_note | V003 00:51-01:30 | 表格列展示原因和证据备注，适合沉淀为动作模板。 | 字段内容小，需人工复核具体行。 | high |\n- 不能证明这批素材已经达到 `content_validation passed` 或 `send_ready`。\n| 1 | V004 | 00:39-00:51 | 优先级表：商品名、去巨量百应搜什么、复查重点。 | no_audio_track；视觉文字可见但非 OCR。 | A005：只补查 4 个商品卡。 | 数字/商品名需复核，需遮挡隐私。 | 结尾动作锚点 / ChatGPT 写稿核心。 |\n| 3 | V003 | 00:33-00:48 | 10 个候选方向汇总表。 | no_audio_track。 | A003：把方向做成候选表。 | 字段值需复核。 | 方法结构展示。 |\n| 5 | V004 | 00:09-00:24 | “3 个为什么留下”的判断与风险。 | no_audio_track；可见佣金/价格/判断句，uncertain。 | A002/A006：留下方向必须有收益信号和风险。 | AI 判断非平台事实。 | 反转：不是最赚钱，而是最值得复核。 |\n| 6 | V001 | 01:36-02:09 | 商品卡近景，键帽/键盘周边类商品。 | no_audio_track；商品卡文字可见但需复核。 | A001/A008：看商品卡字段。 | 商品详情不够清晰。 |\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
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
    "path": "codex_log/current_data_goal_anchor.md",
    "snippet": "- 给 ChatGPT / GPT Project / Codex / DeepSeek 提供稳定的当前锚点入口。\n- 防止 Codex 每次从 `video_goal_card`、`post_publish_review_card`、`data_flywheel_memory` 和 `content_structure_feedback_card` 里现场拼锚点。\n      note: \"本轮不得进入正式 Codex 视频执行。\"\n      - \"DeepSeek supply request\"\n      - \"content_validation\"\n      - \"send_ready\"\n1. 命中文案修改、下一条视频、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步时，必须先读取本文件。\n4. Codex 可归档截图和整理早期数据，但不得改写本文件里已锁定的数据目标字段。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
    "snippet": "- boundary: `technical_material_audit（技术素材审计）only; content_validation（内容验证）not advanced`\n| S-V001-01 | V001 `内建视网膜显示器 2026-05-23 20-57-41.mp4` | 00:00 | 00:12 | 12s | ChatGPT/Atlas 或浏览器窗口与选品页面并列，像是在整理当前任务和材料。 | 画面文字较小，部分可见 “Atlas / Computer Use / Codex” 类上下文。 | no_audio_track | 从对话/材料切回选品页面前的准备。 | weak_or_context_only | weak | 支撑“这是一次有 AI 辅助的选品过程录屏”。 | 不能支撑商品判断或电商动作。 | 开头背景/工作流铺垫，不宜做核心证据。 | 信息密度低，文字小。 |\n| S-V001-02 | V001 | 00:15 | 01:24 | 69s | 抖音/巨量百应选品广场页面；搜索框输入类似“键帽”，展示多张商品卡、筛选项、价格/佣金/月销等卡片字段。 | 可见“选品广场”、搜索词、商品卡、佣金/到手价/月销字段；具体数值 `uncertain`。 | no_audio_track | 搜索/浏览商品方向，先看商品卡字段。 | product_page_evidence + workflow_process_evidence | strong | 可支撑“选品前先看商品卡字段，不要凭大品类感觉拍板”。 | 不能证明这些商品能卖或佣金能覆盖成本。 | 中段第一证据：展示从大方向进入商品卡筛选。 | 公开展示需遮挡账号/平台侧栏；具体商品名/金额需复核。 |\n| S-V001-03 | V001 | 01:27 | 01:33 | 6s | ChatGPT/Atlas 对刚才画面做文字分析。 | 提到类似“高客单键帽”“25% 佣金”“单笔约 34.7”“需要核红”“找杯具”等，`uncertain`。 | no_audio_track | 用 AI 把商品卡信息转成风险提醒和下一步搜索方向。 | workflow_process_evidence | medium | 可支撑“AI 负责整理复核点，不直接替你判定成功”。 | 不能证明 AI 判断完全正确。 | 可用作转场：商品卡 -> 复核问题。 | AI 文本不是平台事实。 |\n| S-V001-05 | V001 | 02:12 | 03:24 | 72s | ChatGPT 输出和商品页来回切换；多次出现 AI 结论与页面商品卡。 | 文字提到高客单、佣金、样本、SKU/兼容风险、继续找更窄方向，`uncertain`。 | no_audio_track | 从商品\n...[truncated]",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md",
    "snippet": "- boundary: `technical_material_audit only; content_validation not advanced`\n| A001 | 选品前先不要问“哪个品能赚”，先打开商品卡，看 `客单价 / 佣金 / 月销或销量信号 / 店铺分 / 商品分 / 退货风险`。 | V001 商品卡页面；V003 明细表字段 | V001 00:15-02:09；V003 00:51-01:30 | 画面明确展示选品页商品卡和明细表字段，能把“凭感觉选品”改成“先看字段”。 | 小字和数值需复核；不能把字段存在写成事实准确。 | high |\n| A005 | 复盘/下一步只补查 4 个商品卡，不要继续无限刷：按优先级逐个核验样品、店铺、佣金、SKU、合规。 | V004 “先确认 4 个商品卡”与优先级表 | V004 00:27-00:51 | 画面直接给出“先确认 4 个商品卡”和复查重点，是最清楚的行动锚点。 | 4 个商品名称/金额需复核；不等于确定上架。 | high |\n| A007 | 商品页拆解时，把 `卖点 / 人群 / 风险 / 内容角度` 分开写进 reason/evidence_note，而不是只抄标题。 | V003 明细表 reason/evidence_note | V003 00:51-01:30 | 表格列展示原因和证据备注，适合沉淀为动作模板。 | 字段内容小，需人工复核具体行。 | high |\n- 不能证明这批素材已经达到 `content_validation passed` 或 `send_ready`。\n| 1 | V004 | 00:39-00:51 | 优先级表：商品名、去巨量百应搜什么、复查重点。 | no_audio_track；视觉文字可见但非 OCR。 | A005：只补查 4 个商品卡。 | 数字/商品名需复核，需遮挡隐私。 | 结尾动作锚点 / ChatGPT 写稿核心。 |\n| 3 | V003 | 00:33-00:48 | 10 个候选方向汇总表。 | no_audio_track。 | A003：把方向做成候选表。 | 字段值需复核。 | 方法结构展示。 |\n| 5 | V004 | 00:09-00:24 | “3 个为什么留下”的判断与风险。 | no_audio_track；可见佣金/价格/判断句，uncertain。 | A002/A006：留下方向必须有收益信号和风险。 | AI 判断非平台事实。 | 反转：不是最赚钱，而是最值得复核。 |",
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
    "source_file": "codex_log/current_data_goal_anchor.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md",
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
    "path_or_query": "Whether the locked phrase 'Codex 操作我的电脑' has direct enough visual evidence in current source videos.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Whether the current data_goal_anchor partial_data_recorded state blocks this formal video execution.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Whether MiniMax full-length TTS can generate non-silent narration for the complete locked script in this runtime.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Whether the full locked script can be line-group mapped without unsupported core evidence claims.",
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
    "codex_log/current_data_goal_anchor.md",
    "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
    "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md"
  ],
  "use_as": "readonly_supply_pack",
  "warning": "This pack is local fallback, not a DeepSeek conclusion.",
  "recommended_child_tasks": [
    "update_deep_file_supply_contract",
    "update_controller_schema_fixture",
    "run_validation_and_truth_check"
  ],
  "files_codex_must_review": [],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "AGENTS.md",
    "codex_source/00_codex_readme.md",
    "codex_source/01_execution_rules.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/21_codex_judgment_permission_matrix.md",
    "codex_log/current_data_goal_anchor.md",
    "codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md",
    "codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md"
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
