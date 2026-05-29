# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260529T142421Z`
- `request_id`: `20260529_editing_profile_system_post_risk_review_request`
- `request_validation_status`: `passed`
- `task_type`: `project_file_change`
- `trigger_reason`: `mandatory_post_risk_review`
- `action`: `risk_report`
- `supply_source`: `deepseek_passed`
- `context_pack_validation`: `passed`
- `deepseek_generation_status`: `passed_with_retries`
- `fallback_status`: `not_used`
- `pipeline_status`: `usable`
- `multi_agent_runtime_validation`: `not_started`
- `not_deepseek_conclusion`: `false`
- `deepseek_actual_participation`: `deepseek_passed`
- `blocked_reason`: `none`
- `token_usage_observed_or_user_check_required`: `token_decrement_expected`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `api_key_printed`: `false`
- `api_key_written`: `false`

## request_state（请求状态）

```json
{
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260529_editing_profile_system_post_risk_review_request.json",
  "current_goal": "执行后复核 editing_profile_system 架子接入是否遗漏入口、脚本、fixture、测试或日志，是否误推进 content_validation/send_ready/voice_validation/visual_master_locked/current_data_goal_anchor_ready，是否混入 unrelated dirty changes。",
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
  "current_step": "post_write_risk_review_before_commit",
  "known_context": [
    "已新增 editing_profile_system 文档。",
    "已更新 aesthetic_editing_flow、execution_rules、codex readme 短引用。",
    "已接入 editing_profile_preflight 到 publish_candidate_preflight_suite。",
    "已新增 3 个 fixture case 和 3 个 unit tests。",
    "已更新 latest 和 dated log。",
    "验证已通过：py_compile、unittest、JSON parse、git diff --check。"
  ],
  "missing_context": [
    "尚未完成 stage / secret scan / commit / push / remote verification。",
    "后续真实剪辑任务尚未验证真实审美效果。"
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
  "deepseek_call_attempted": true,
  "deepseek_actual_participation": "deepseek_passed",
  "supply_source": "deepseek_passed",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": false,
  "blocked_reason": "none",
  "token_usage_expected": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_blocked_not_deepseek_conclusion",
  "token_usage_observed_or_user_check_required": "token_decrement_expected",
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
  "supply_source": "deepseek_passed",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": false,
  "context_pack_validation": "passed",
  "deepseek_actual_participation": "deepseek_passed",
  "blocked_reason": "none",
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
  "deepseek_call_real": true,
  "deepseek_actual_participation": "deepseek_passed",
  "supply_source": "deepseek_passed",
  "fallback_status": "not_used",
  "not_deepseek_conclusion": false,
  "blocked_reason": "none",
  "token_usage_expectation_check": {
    "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_blocked_not_deepseek_conclusion",
    "expected_to_decrease": true,
    "observed_token_usage": "not_available_user_check_required",
    "token_usage_observed_or_user_check_required": "token_decrement_expected",
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
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_blocked_not_deepseek_conclusion",
  "expected_to_decrease": true,
  "observed_token_usage": "not_available_user_check_required",
  "token_usage_observed_or_user_check_required": "token_decrement_expected",
  "cannot_claim_deepseek_deep_participation_if_token_not_decreased": true,
  "fallback_local_only_token_rule": "fallback_local_only 不应减少 DeepSeek token，也不能写 DeepSeek 已深度参与。"
}
```

## task（任务）

Use this supply_request task card as the only current task context. Do not infer missing project state from memory.
{
  "request_id": "20260529_editing_profile_system_post_risk_review_request",
  "task_id": "editing_profile_system_scaffold_20260529_post_risk_review",
  "mandatory_for_every_task": true,
  "participation_level": "readonly_post_risk_review",
  "pre_supply_required": false,
  "post_review_required": true,
  "codex_vertical_completion_required": true,
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_blocked_not_deepseek_conclusion",
  "fallback_allowed": true,
  "fallback_not_completion": true,
  "user_explicit_deepseek_required": false,
  "deepseek_must_not_be_skipped_by_codex_discretion": true,
  "current_goal": "执行后复核 editing_profile_system 架子接入是否遗漏入口、脚本、fixture、测试或日志，是否误推进 content_validation/send_ready/voice_validation/visual_master_locked/current_data_goal_anchor_ready，是否混入 unrelated dirty changes。",
  "current_step": "post_write_risk_review_before_commit",
  "known_context": [
    "已新增 editing_profile_system 文档。",
    "已更新 aesthetic_editing_flow、execution_rules、codex readme 短引用。",
    "已接入 editing_profile_preflight 到 publish_candidate_preflight_suite。",
    "已新增 3 个 fixture case 和 3 个 unit tests。",
    "已更新 latest 和 dated log。",
    "验证已通过：py_compile、unittest、JSON parse、git diff --check。"
  ],
  "missing_context": [
    "尚未完成 stage / secret scan / commit / push / remote verification。",
    "后续真实剪辑任务尚未验证真实审美效果。"
  ],
  "decision_needed": "",
  "expected_output": [
    "risk_and_conflict_report",
    "status_promotion_risk_check",
    "unrelated_dirty_risk_check",
    "missing_sync_check",
    "codex_next_input",
    "token_usage_expectation_check"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "read_status_required": true,
    "impact_check_required": true,
    "output_dir": "codex_log/deepseek_supply/20260529_editing_profile_system_post_risk_review",
    "verification_required": [
      "secret_scan",
      "path_limited_stage",
      "commit",
      "push",
      "remote_head_verification"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "Forbidden status promotion appears in modified files.",
    "Profile placeholders are expanded into full ecommerce/tutorial/daily parameter sets.",
    "aesthetic_editing_flow does not require editing_profile_selected.",
    "script_to_shot_execution_map does not require profile_id.",
    "preflight gate cannot block missing profile_id.",
    "latest or dated log missing status boundary.",
    "secret scan fails.",
    "unrelated dirty files cannot be isolated."
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime is stable or completed.",
    "Do not claim editing profile system is fully validated by real videos.",
    "Do not promote content_validation/send_ready/voice_validation/visual_master_locked/current_data_goal_anchor_ready.",
    "Do not read or print secrets.",
    "Do not include unrelated dirty changes."
  ],
  "requires_real_deepseek_participation": false,
  "file_scope": {
    "candidate_files": [
      "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
      "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
      "codex_source/01_execution_rules.md",
      "codex_source/00_codex_readme.md",
      "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
      "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
      "tests/test_publish_candidate_preflight_tolerance.py",
      "codex_log/latest.md",
      "codex_log/20260529_剪辑参数包系统_editing_profile_system.md"
    ],
    "must_prefetch_files": [
      "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
      "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
      "codex_source/01_execution_rules.md",
      "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
      "codex_log/latest.md"
    ],
    "optional_prefetch_files": [
      "codex_source/00_codex_readme.md",
      "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
      "tests/test_publish_candidate_preflight_tolerance.py",
      "codex_log/20260529_剪辑参数包系统_editing_profile_system.md"
    ],
    "forbidden_files": [
      ".env",
      ".env.local",
      "本地运行配置_local_runtime/",
      "dist/latest_review_pack/",
      "dist/",
      "素材录制/"
    ],
    "secret_files_forbidden": true
  },
  "content_loading_policy": {
    "read_only": true,
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 9,
    "max_chars_per_file": 1600,
    "max_total_chars": 14000,
    "truncate_policy": "head_and_relevant_snippets",
    "do_not_read_secret_files": true,
    "do_not_modify_files": true
  },
  "output_required": [
    "risk_and_conflict_report",
    "missing_or_uncertain_files",
    "codex_next_input",
    "token_usage_expectation_check"
  ]
}

## files_considered（已考虑文件）

```json
[
  "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
  "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
  "codex_source/01_execution_rules.md",
  "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
  "codex_log/latest.md",
  "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
  "tests/test_publish_candidate_preflight_tolerance.py",
  "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
  "codex_source/00_codex_readme.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
  "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
  "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
  "codex_log/latest.md",
  "codex_source/01_execution_rules.md",
  "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
  "tests/test_publish_candidate_preflight_tolerance.py",
  "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
  "codex_source/00_codex_readme.md"
]
```

## risks（风险）

```json
[
  "22.md未显式要求aesthetic_editing_flow必须输出editing_profile_selected，可能导致profile_id遗漏",
  "preflight脚本片段未显示editing_profile_preflight检查缺失profile_id，gate可能不生效",
  "01_execution_rules.md内容不完整，无法确认是否已更新profile_id相关规则",
  "23.md声明不推进状态，但22.md中aesthetic_editing_flow的forbidden_status引用第2节统一禁止状态（未在片段中提供），需确认无冲突",
  "aesthetic_editing_flow未要求editing_profile_selected（需进一步读取22.md完整内容）",
  "preflight gate不能阻塞缺失profile_id（需查看preflight脚本中editing_profile_preflight实现）",
  "latest或dated log缺少status边界（latest.md显示mechanism_connected，暂安全）"
]
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
    "post_risk_review",
    "deep_file_prefetch",
    "mid_task_incremental_supply"
  ],
  "relevant_file_bundle_exists": true,
  "exact_snippet_pack_exists": true,
  "deepseek_actual_required": false,
  "supply_source": "deepseek_passed",
  "status": "failed_insufficient_depth",
  "not_long_term_runtime_validation": true
}
```

## relevant_file_bundle（相关文件内容包）

```json
[
  {
    "path": "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# 剪辑参数包与镜头选择标准 Editing Profile And Shot Selection Rules\n\n## 1. 文件定位\n\n本文件只定义 `editing_profile_system（剪辑参数包系统）` 的基础结构。\n\n它不生成视频、不改文案、不细化所有片型参数、不推进任何内容 / 发布 / 声音 / 视觉状态。\n\n关系固定如下：\n\n```text\nshot_selection_quantitative_rules（镜头选择量化规则）\n= 通用评分尺\n\nediting_profile（剪辑参数包）\n= 当前片型的剪辑偏好\n\nscript_to_shot_execution_map（文案到镜头执行表）\n= 当前这条片子的具体镜头安排\n```\n\n原则固定为：\n\n```text\n通用底线少动\n类型参数可调\n单条镜头表负责落地\n```\n\n## 2. editing_profile_schema（剪辑参数包结构）\n\n```text\nediting_profile_schema:\n  profile_id（参数包编号）: 唯一编号，必须写入 script_to_shot_execution_map。\n  profile_name（参数包名称）: 人类可读名称。\n  video_type（视频类型）: 当前参数包服务的内容形式。\n  target_viewer_action（观众目标动作）: 观众看完后应做的动作或判断。\n  rhythm_density（节奏密度）: low / medium / high；控制镜头切换与信息推进速度。\n  evidence_requirement（证据强度要求）: low / medium / medium_high / high；控制画面证据硬度。\n  readability_priority（可读性优先级）: low / medium / high；控制表格、页面、字幕、卡片是否优先可读。\n  emotion_priority（情绪优先级）: low / medium / high；控制人感、吐槽、陪伴感权重。\n  card_density_limit（卡片密度限制）: low / medium / high；限制解释卡、判断卡、总结卡密度。\n  material_reuse_limit（素材复用限制）: 限制同一素材片段和核心证据复用。\n  music_beat_weight（音乐卡点权重）: low / low_to_medium / medium / high；控制音乐节拍对剪辑的影响。\n  motion_intensity（运动强度）: low / medium / high；控制放大、裁切、转场、动效强度。\n  text_density_limit（文字密度限制）: low / medium / high；限制同屏文字数量和叠层。\n  shot_selection_threshold（镜头选择阈值）: 最低可选镜头分数；低于阈值必须替换或 blocked。\n  fallback_policy（兜底策略）: 缺素材、参数冲突或 profile 占位时如何处理。\n  blocked_if（阻断条件）: 触发后不得进入剪辑、装配或完成态。\n```\n\n## 3. default_editing_profile（默认剪辑参数包）\n\n`default_general_content_v1（默认通用内容参数包）` 只作为 v1 通用默认，不代表所有片型最终标准。后续具体片型可以覆盖这些参数。\n\n```yaml\ndefault_editing_profile:\n  profile_id: default_general_content_v1\n  profile_name: 默认通用内容参数包\n  video",
    "excerpt_range_or_marker": "lines:1-60",
    "confidence": "high"
  },
  {
    "path": "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件只是 Codex 执行入口层的短索引，不新增文案、素材、剪辑、复审或复盘大机制。\n用途：让 Codex 每轮在 `route_decision（路由判断）` 之后、具体执行之前，先判断任务属于哪条工作流，再读取对应文件、产出对应交接件、触发对应 blocker。\n- `content_validation = passed（内容验证通过）`\n- `send_ready = true（可发送）`\n除非用户 / ChatGPT 明确最终复审确认，Codex 不得推进以上状态。\n- `blocked_if（阻断条件）`：最终文案来源不明、Perplexity 初稿被当成最终稿、素材细节缺失却要定稿、Codex 被要求直接重写最终文案、数据锚点为 `draft / waiting_data` 却要写正式数据驱动执行。\n- `input_signal（输入信号）`：复审、审片、质量问题、像 demo、不舒服、不合格、不顺、不美观、技术验证、内容验证、send_ready、remaining_blockers。\n- `required_handoff（必须交接件）`：`quality_issue_classifier_output（质量短板分类结果）`、`technical_validation（技术验证）`、`content_validation_boundary（内容验证边界）`、`remaining_blockers（剩余阻断）`。\n- `blocked_if（阻断条件）`：把技术验证写成内容验证、用户未确认却推进 send_ready、声音 / 视觉 / 内容状态边界不清、缺审片包或关键媒体证据却要裁决可发。",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/01_execution_rules.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# Codex 执行规则\n命中截图、平台数据、评论、私信、咨询、复盘或下一轮变量判断时，Codex 必须优先读取：\n本覆盖口径不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n当前进入 `formal_operation_active（正式运营中）` 后，Codex 在 `route_decision（路由判断）` 阶段必须判断本轮是否是视频交付任务。\nCodex 后续不得降级处理正式运营任务。凡任务目标指向做视频、产视频、发片候选、运营内容、下一条视频、发布候选、项目机制落库、GPT Project 同步、数据录入、复盘记录、素材审计、文案到执行映射、TTS、字幕、卡片、比例、导出、commit / push 等，必须实实在在完成仓库写明的目标。\n- DeepSeek 需要真实参与但只有 `fallback_local_only`。\n`mandatory_commit_push_gate（强制提交推送闸门）` 是 Codex 默认完成标准的一部分，不是临时收尾建议。以后任何最小任务只要对仓库文件产生有效改动，`completed（已完成）` 必须等到 Git 收尾完成后才允许写。\nCodex 最终回报必须默认包含：\n正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格；用户不负责替 GPT / Codex 诊断内部原因。\n当用户只反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，至少检查：\n- final_script 是否被 Codex 越权改写。\n发现任一内部问题，Codex 必须修复或 `blocked`，不得把诊断责任转给用户。\n正式运营视频执行前必须先有 `locked_copy_contract（锁定文案契约）`。该契约由 ChatGPT / 用户确认，Codex 只能按它执行，不得擅自改写。\n`codex_copy_authority_boundary（Codex 文案权限边界）`：\n11. `publish_candidate_user_standard_preflight（候选可发布用户标准预检）`：按用户标准区分可接受小瑕疵和重大缺陷；`publish_candidate_ready_for_human_review` 不等于 `send_ready`。\nMiniMax B 声音身份锁硬规则：后续 B 方案正片候选不得再只靠 `voice_feel_tags`、`b_voice_feel_reflected = true` 或“听起来像 B”放行。2026-05-28 起，正式 B 方案声音已由用户确认并锁定为 `expected_b_minimax_voice_id = oldBMinimax20260528010200`。用户确认对象不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本：`codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。后续实际生成报告必须写明 `actual_voice_id`，且必须等于 `oldBMinimax20260528010200`；`b_voice_identity_lock.statu\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
    "file_role": "runner_or_controller",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "\"advanced_content_validation\",\n    \"advanced_send_ready\",\n    if re.search(r\"content_validation[^a-z0-9]+(passed|true|通过)\", text):\n        detected.append(\"advanced_content_validation\")\n    if re.search(r\"send_ready[^a-z0-9]+(true|yes|1|是)\", text):\n        detected.append(\"advanced_send_ready\")\n    if truthy(summary.get(\"send_ready\")):\n        reasons.append(\"publish_candidate_does_not_equal_send_ready\")\n            \"status_boundary\": \"publish_candidate_ready_for_human_review_does_not_equal_send_ready; send_ready_requires_user_or_chatgpt_final_confirmation\",\n        send_ready_allowed=False,\n    if re.search(r\"content_validation[^a-z0-9]+(passed|true|通过)\", summary_text):\n    if re.search(r\"send_ready[^a-z0-9]+(true|yes|1|是)\", summary_text):\n            \"technical_validation_means_content_validation\": False,\n            \"publish_candidate_ready_for_human_review_means_send_ready\": False,",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `DeepSeek`：本轮前置供料通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`；token 用量只记录为 `token_decrement_expected`，不写长期稳定。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。\n- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 DeepSeek 已参与。\n- `状态边界`：未生成全片旁白，未替换当前视频音轨，未生成视频，未改文案，未改画面，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。\n- `DeepSeek`：前置供料与执行后风险复核均实际运行通过，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `状态边界`：未生成音频 / 视频，未上传参考音频，未调用 MiniMax TTS / clone A\n...[truncated]",
    "excerpt_range_or_marker": "lines:12-21",
    "confidence": "high"
  },
  {
    "path": "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
    "file_role": "fixture_or_request_example",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "\"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"voice_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"whole_video_drift_allowed\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"voice_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"voice_validation_passed\", \"final_voice_validated_true\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\", \"voice_validation_passed\", \"final_voice_validated_true\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"voice_validation_passed\", \"final_voice_validated_true\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"voice_validation_passed\", \"final_voice_validated_true\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"sen\n...[truncated]",
    "excerpt_range_or_marker": "lines:11-25",
    "confidence": "high"
  },
  {
    "path": "tests/test_publish_candidate_preflight_tolerance.py",
    "file_role": "runner_or_controller",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "\"send_ready\": False,\n        self.assertFalse(result[\"send_ready_allowed\"])",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `DeepSeek`：已创建前置供料任务卡 `codex_log/supply_requests/20260529_editing_profile_system_pre_supply_request.json` 并运行 safe runner；`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`。`token_usage_observed_or_user_check_required = token_decrement_expected`，但未直接观测 token 用量，不能写 DeepSeek 长期稳定。\n- `状态边界`：本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。",
    "excerpt_range_or_marker": "lines:12-13",
    "confidence": "high"
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n后续唯一推荐修复路线改为 `route_b_migrate_old_b_to_minimax（旧 B 迁移到 MiniMax）`。MiniMax 必须通过旧 B 参考音频生成或克隆出新的 MiniMax 声音身份；当前百炼代理复刻需要公网 `audio_url`，MiniMax 官方 voice clone 需要上传参考音频拿 `file_id`。缺公网 URL、缺用户授权上传、缺 `generated_minimax_voice_id` 或缺用户试听确认时，必须写 `blocked_need_reference_audio_url` / `pending_reference_audio_url`，不得回退为系统音色候选，也不得推进 `voice_validation = passed`、`final_voice_validated = true` 或 `send_ready = true`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。\n- Codex 不得把本地生成当已 push。\n- Codex 不得把技术成功当内容成功。\n- Codex 不得把“没有明确失败”当完成。\nCodex 在视频执行中负责素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，不负责重新定稿。Codex 可以改标点、换行、字幕分句和 TTS 停顿，但不得改变语义、人味、标题语气、核心判断、前台表达角度，不能用视觉标题卡替换 `locked_title`。\n如果 Codex 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，等待 ChatGPT / 用户确认，不得自行改稿。\n以后凡是任务命中 `publish_candidate（发片候选）`、`video_execution（视频执行）`、`repair_candidate（修片候选）`、`regenerate_video（重新生成视频）`、`pre_publish_fix（发布前修复）`、`final_script_to_video（最终文案进入视频）`，或涉及 `TTS / subtitle / card / timeline / review_pack / privacy_mask / aspect_ratio / visual_evidence` 任一视频执行组件，Codex 必须先跑 `process_boot_gate（流程启动闸门）`。\n- `process_boot_gate` 只防止执行断层，不推进\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  }
]
```

## exact_snippet_pack（关键原文片段包）

```json
[
  {
    "path": "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
    "snippet": "# 剪辑参数包与镜头选择标准 Editing Profile And Shot Selection Rules\n\n## 1. 文件定位\n\n本文件只定义 `editing_profile_system（剪辑参数包系统）` 的基础结构。\n\n它不生成视频、不改文案、不细化所有片型参数、不推进任何内容 / 发布 / 声音 / 视觉状态。\n",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
    "snippet": "本文件只是 Codex 执行入口层的短索引，不新增文案、素材、剪辑、复审或复盘大机制。\n用途：让 Codex 每轮在 `route_decision（路由判断）` 之后、具体执行之前，先判断任务属于哪条工作流，再读取对应文件、产出对应交接件、触发对应 blocker。\n- `content_validation = passed（内容验证通过）`\n- `send_ready = true（可发送）`\n除非用户 / ChatGPT 明确最终复审确认，Codex 不得推进以上状态。\n- `blocked_if（阻断条件）`：最终文案来源不明、Perplexity 初稿被当成最终稿、素材细节缺失却要定稿、Codex 被要求直接重写最终文案、数据锚点为 `draft / waiting_data` 却要写正式数据驱动执行。\n- `input_signal（输入信号）`：复审、审片、质量问题、像 demo、不舒服、不合格、不顺、不美观、技术验证、内容验证、send_ready、remaining_blockers。\n- `required_handoff（必须交接件）`：`quality_issue_classifier_output（质量短板分类结果）`、`technical_validation（技术验证）`、`content_validation_boundary（内容验证边界）`、`remaining_blockers（剩余阻断）`。",
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
    "path": "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
    "snippet": "\"advanced_content_validation\",\n    \"advanced_send_ready\",\n    if re.search(r\"content_validation[^a-z0-9]+(passed|true|通过)\", text):\n        detected.append(\"advanced_content_validation\")\n    if re.search(r\"send_ready[^a-z0-9]+(true|yes|1|是)\", text):\n        detected.append(\"advanced_send_ready\")\n    if truthy(summary.get(\"send_ready\")):\n        reasons.append(\"publish_candidate_does_not_equal_send_ready\")",
    "why_it_matters": "runner_or_controller for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/latest.md",
    "snippet": "- `DeepSeek`：本轮前置供料通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`；token 用量只记录为 `token_decrement_expected`，不写长期稳定。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。\n- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 DeepSeek 已参与。\n- `状态边界`：未生成全片旁白，未替换当前视频音轨，未生成视频，未改文案，未改画面，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。\n- `DeepSeek`：前置供料与执行后风险复核均实际运行通过，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
    "snippet": "\"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"voice_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"send_ready_true\", \"content_validation_passed\", \"whole_video_drift_allowed\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"publish_candidate_ready_for_human_review_true\", \"send_ready_true\", \"content_validation_passed\"]\n      \"must_not_write\": [\"completed\", \"send_ready_true\", \"content_validation_passed\"]",
    "why_it_matters": "fixture_or_request_example for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "tests/test_publish_candidate_preflight_tolerance.py",
    "snippet": "\"send_ready\": False,\n        self.assertFalse(result[\"send_ready_allowed\"])",
    "why_it_matters": "runner_or_controller for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
    "snippet": "- `DeepSeek`：已创建前置供料任务卡 `codex_log/supply_requests/20260529_editing_profile_system_pre_supply_request.json` 并运行 safe runner；`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`。`token_usage_observed_or_user_check_required = token_decrement_expected`，但未直接观测 token 用量，不能写 DeepSeek 长期稳定。\n- `状态边界`：本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "snippet": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n后续唯一推荐修复路线改为 `route_b_migrate_old_b_to_minimax（旧 B 迁移到 MiniMax）`。MiniMax 必须通过旧 B 参考音频生成或克隆出新的 MiniMax 声音身份；当前百炼代理复刻需要公网 `audio_url`，MiniMax 官方 voice clone 需要上传参考音频拿 `file_id`。缺公网 URL、缺用户授权上传、缺 `generated_minimax_voice_id` 或缺用户试听确认时，必须写 `blocked_need_reference_audio_url` / `pending_reference_audio_url`，不得回退为系统音色候选，也不得推进 `voice_validation = passed`、`final_voice_validated = true` 或 `send_ready = true`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  }
]
```

## dependency_map（依赖映射）

```json
[
  {
    "source_file": "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
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
    "source_file": "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/latest.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "tests/test_publish_candidate_preflight_tolerance.py",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/00_codex_readme.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  }
]
```

## risk_delta_report（增量风险报告）

```json
[]
```

## missing_or_uncertain_files（缺失或不确定文件）

```json
[
  {
    "path_or_query": "尚未完成 stage / secret scan / commit / push / remote verification。",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "后续真实剪辑任务尚未验证真实审美效果。",
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
{
  "status_promotion_risk": "check_required_no_forbidden_status_promotion",
  "forbidden_change_risk": "check_required_no_env_media_or_latest_review_pack_change",
  "missed_sync_files": "check_required_docs_scripts_schema_fixture_logs_package_paths",
  "fallback_mislabel_risk": "none_observed",
  "remaining_work": "Codex must run validation, sync logs/package/path index, and report token check boundary."
}
```

## codex_next_input（给 Codex 的下一步输入）

```json
{
  "read_first": [
    "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
    "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
    "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
    "codex_log/latest.md",
    "codex_source/01_execution_rules.md",
    "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
    "tests/test_publish_candidate_preflight_tolerance.py",
    "codex_log/20260529_剪辑参数包系统_editing_profile_system.md"
  ],
  "use_as": "readonly_supply_pack",
  "warning": "DeepSeek generated the pack, but Codex must still verify original files.",
  "post_risk_review_required": true,
  "status_promotion_risk": "check_required_no_forbidden_status_promotion",
  "forbidden_change_risk": "check_required_no_env_media_or_latest_review_pack_change",
  "missed_sync_files": "check_required_docs_scripts_schema_fixture_logs_package_paths",
  "fallback_mislabel_risk": "none_observed",
  "remaining_work": "Codex must run validation, sync logs/package/path index, and report token check boundary.",
  "recommended_child_tasks": [
    "update_deep_file_supply_contract",
    "update_controller_schema_fixture",
    "run_validation_and_truth_check"
  ],
  "files_codex_must_review": [
    "scripts/发片候选预检套件_publish_candidate_preflight_suite.py",
    "tests/test_publish_candidate_preflight_tolerance.py"
  ],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md",
    "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
    "codex_source/01_execution_rules.md",
    "codex_log/latest.md",
    "codex_source/fixtures/publish_candidate_preflight_suite_cases.json",
    "codex_log/20260529_剪辑参数包系统_editing_profile_system.md",
    "codex_source/00_codex_readme.md"
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
