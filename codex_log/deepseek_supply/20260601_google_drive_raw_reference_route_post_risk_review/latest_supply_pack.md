# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260601T134737Z`
- `request_id`: `20260601_google_drive_raw_reference_route_post_risk_review_request`
- `request_validation_status`: `passed`
- `task_type`: `project_file_change + mechanism_or_route_fix + copywriting_reference_governance`
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
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_post_risk_review_request.json",
  "current_goal": "复核本轮 Google Drive 原文级 reference 路线修正是否仍存在本地 raw / manifest 残留、第三方全文入库、状态晋级、入口遗漏或写入范围扩大。",
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
  "current_step": "post_write_risk_review",
  "known_context": [
    "15 号文件已新增原文级 reference 读取规则。",
    "15 号文件已将 /Users/fan/Desktop/文案.rtf 降级为 historical_import_source_path。",
    "03 总索引已补充原文级 reference 路线：先读 15 号标准，再由 ChatGPT / GPT Project 读取 Google Drive 原文。",
    "latest 已记录本轮路线修正。",
    "本轮未创建本地 raw reference 文件或 reference manifest。"
  ],
  "missing_context": [
    "Google Drive concrete URL or file id is not provided in this task.",
    "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review."
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
  "token_usage_expected": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
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
    "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
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
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
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
  "request_id": "20260601_google_drive_raw_reference_route_post_risk_review_request",
  "task_id": "google_drive_raw_reference_route_for_copy_reference_standard",
  "mandatory_for_every_task": true,
  "participation_level": "readonly_post_risk_review",
  "pre_supply_required": false,
  "post_review_required": true,
  "codex_vertical_completion_required": true,
  "token_usage_expectation": "token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required",
  "fallback_allowed": true,
  "fallback_not_completion": true,
  "user_explicit_deepseek_required": false,
  "deepseek_must_not_be_skipped_by_codex_discretion": true,
  "current_goal": "复核本轮 Google Drive 原文级 reference 路线修正是否仍存在本地 raw / manifest 残留、第三方全文入库、状态晋级、入口遗漏或写入范围扩大。",
  "current_step": "post_write_risk_review",
  "known_context": [
    "15 号文件已新增原文级 reference 读取规则。",
    "15 号文件已将 /Users/fan/Desktop/文案.rtf 降级为 historical_import_source_path。",
    "03 总索引已补充原文级 reference 路线：先读 15 号标准，再由 ChatGPT / GPT Project 读取 Google Drive 原文。",
    "latest 已记录本轮路线修正。",
    "本轮未创建本地 raw reference 文件或 reference manifest。"
  ],
  "missing_context": [
    "Google Drive concrete URL or file id is not provided in this task.",
    "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review."
  ],
  "decision_needed": "",
  "expected_output": [
    "risk_and_conflict_report",
    "raw_reference_route_check",
    "missing_or_uncertain_files",
    "codex_next_input",
    "status_promotion_risk_check"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "read_status_required": true,
    "impact_check_required": true,
    "write_scope": [
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "codex_log/latest.md",
      "codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_pre_supply_request.json",
      "codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_post_risk_review_request.json"
    ],
    "output_dir": "codex_log/deepseek_supply/20260601_google_drive_raw_reference_route_post_risk_review",
    "verification_required": [
      "keyword_check",
      "path_reference_check",
      "no_raw_full_copy_check",
      "no_local_raw_reference_files_check",
      "no_forbidden_status_promotion_check",
      "git_diff_check",
      "secret_scan"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "third-party full text is detected in changed files",
    "local raw reference or reference manifest is created",
    "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md no longer preserves existing learning cards",
    "status fields are promoted",
    "write scope expands beyond allowed files"
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime is stable or completed.",
    "Do not copy the 5 external reference scripts into repo as raw full text.",
    "Do not create local raw reference files.",
    "Do not create a local reference manifest system.",
    "Do not generate a new formal video execution prompt.",
    "Do not modify media outputs, TTS scripts, editing scripts, API config, dist/latest_review_pack, content_validation, send_ready, publish status, voice_validation, final_voice_validated, visual_master_locked, or current_data_goal_anchor ready status."
  ],
  "deep_supply_mode": {
    "enabled": true,
    "mode": [
      "deep_file_prefetch",
      "mid_task_incremental_supply",
      "post_risk_review"
    ]
  },
  "file_scope": {
    "candidate_files": [
      "codex_log/latest.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md"
    ],
    "must_prefetch_files": [
      "codex_log/latest.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md"
    ],
    "forbidden_files": [
      ".env",
      ".env.local",
      "dist/latest_review_pack",
      "public/",
      "GPT数据源/reference_manifests/",
      "GPT数据源/raw_reference/",
      "GPT数据源/本地参考原文_local_reference/",
      "/Users/fan/Desktop/文案.rtf"
    ],
    "secret_files_forbidden": true
  },
  "content_loading_policy": {
    "read_only": true,
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 3,
    "max_chars_per_file": 2200,
    "max_total_chars": 10000,
    "truncate_policy": "head_and_relevant_snippets",
    "do_not_read_secret_files": true,
    "do_not_read_external_raw_reference_file": true,
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
  "codex_log/latest.md",
  "GPT数据源/03_总索引与阅读顺序.md",
  "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
  "GPT数据源/03_总索引与阅读顺序.md",
  "codex_log/latest.md"
]
```

## risks（风险）

```json
[
  {
    "risk": "03总索引原文级reference路线可能未与实际修改对齐",
    "severity": "medium",
    "detail": "截断内容未显示补充语句，需验证"
  },
  {
    "risk": "15号文件规则可能包含对本地raw文件的残余引用",
    "severity": "medium",
    "detail": "截断未看到规则全文，需检查是否保留/Users/fan/Desktop/文案.rtf以外的本地路径"
  },
  {
    "conflict": "latest.md记录状态为mechanism_route_corrected，但03总索引和15号文件状态字段可能未对齐",
    "detail": "需确认所有相关文件的状态字段是否同步更新"
  },
  "第三方全文入库",
  "本地raw reference或reference manifest被创建",
  "15号文件丢失现有学习卡片",
  "状态字段被晋级"
]
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
    "deep_file_prefetch",
    "mid_task_incremental_supply",
    "post_risk_review"
  ],
  "missing_modes": [],
  "relevant_file_bundle_exists": true,
  "exact_snippet_pack_exists": true,
  "deepseek_actual_required": false,
  "supply_source": "deepseek_passed",
  "status": "passed_contract_level",
  "not_long_term_runtime_validation": true
}
```

## relevant_file_bundle（相关文件内容包）

```json
[
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `已确认` 仓库只保存学习卡、判断标准、迁移边界和读取规则；Codex 默认不知道 Google Drive 原文，如需使用，必须由 ChatGPT 桥接进执行单或由用户当轮提供可读内容 / 链接。\n- `未推进` 本轮未生成视频、未生成下一条正式视频执行 prompt，未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek`：已创建前置供料任务卡并运行 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_google_drive_raw_reference_route_pre_supply/latest_supply_pack.md`\n- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。\n- `DeepSeek`：已创建前置供料任务卡与执行后风险复核任务卡并运行 safe runner，前置供料与 post-risk review 均为 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260601_对标文案学习标准_post_risk_review_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_post_risk_review/latest_supply_pack.md`\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。\n- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 De\n...[truncated]",
    "excerpt_range_or_marker": "lines:10-21",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。\n`12_参考到执行落地契约_reference_to_execution_contract.md` 是 GPT Project / ChatGPT 侧 reference 保真入口。凡用户给 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料，必须先把它转换成 `reference_anchor -> effect_targets -> function_fields -> deviation_check -> done_when`，再下发 Codex 执行。\n`13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 是 GPT Project / ChatGPT 侧目标、阈值、文案修改前置读取、内容结构反馈、单主变量和 Codex 动态执行 prompt 的正式机制入口。\n`14_数据目标执行总线_data_goal_execution_bus.md` 是把 `data_goal_anchor（数据目标锚点）` 接入 ChatGPT 文案、DeepSeek 供料、Codex 剪辑 / 编排 / 装配、发布后复盘和执行完成验收的正式机制入口。\n- `bridge_to_deepseek（桥接到 DeepSeek）`\n- `bridge_to_codex_execution（桥接到 Codex 执行）`\n- DeepSeek 供料\n缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。\n### 命中多 AI / DeepSeek / Codex 提速\n22. `codex_source/17_deepseek_supply_controller_protoc\n...[truncated]",
    "excerpt_range_or_marker": "lines:23-39",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "它负责把用户本轮提供的 5 篇外部对标账号文案，转成后续 ChatGPT / Codex 可读取、可判断、可回审的长期文案质量标准。\n- 替代 `content_validation（内容验证）`。\n- 推进 `send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n-> Codex 只按执行单和仓库规则落地，不凭本地摘要硬猜原文\n- Codex 默认不知道 Google Drive 原文；如 Codex 需要使用原文级 reference，必须由 ChatGPT 桥接到执行单，或由用户当轮提供可读内容 / 链接。\n- 这次 AI / Codex 具体替人接了哪一步？\n现在：AI / Codex 接手一段流程，输出可检查、可修改、可复盘的结果\n- Codex 的价值不是“聪明”，而是把散乱素材、步骤和结果变成可复盘证据。\n- AI / Agent / Codex 出现时，是接手某段工作，不是被当成神秘名词。\n它输出了什么能被复核的东西？\n- 写清可编辑、可复核、可手动接管的结果。\n- 适合迁移到 Codex 自动整理素材、生成表格、跑检查、输出报告这类内容。\n- 很适合迁移到“Codex 不是给建议，而是先把一团材料整理成能决策的证据包”。\n- 写 Codex 时可以强调它不是聊天助手，而是执行层和 Integrator。\n- 适合《视频工厂》做工具链、模型链、Codex / ChatGPT / DeepSeek / Perplexity 分工讲解。\n- `Codex 执行层验证者`\n- 把 AI / Codex 写成接手一段工作，而不是万能答案机。\n### 10.4 Codex / AI 生产力选题的应用方式\n写 Codex / AI 生产力时，默认优先回答：\n3. Codex / AI 接手了哪段具体流程？\n5. 最后输出了什么可复核结果？\n13. 有没有把 AI / Codex 写成替用户拍板？\n- `Codex（执行代理）` 素材检查仍必须汇报真实细节、时间码、页面、按钮、动作、结果和证据强度。",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  }
]
```

## exact_snippet_pack（关键原文片段包）

```json
[
  {
    "path": "codex_log/latest.md",
    "snippet": "- `已确认` 仓库只保存学习卡、判断标准、迁移边界和读取规则；Codex 默认不知道 Google Drive 原文，如需使用，必须由 ChatGPT 桥接进执行单或由用户当轮提供可读内容 / 链接。\n- `未推进` 本轮未生成视频、未生成下一条正式视频执行 prompt，未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek`：已创建前置供料任务卡并运行 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_Google_Drive_原文级reference路线_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_google_drive_raw_reference_route_pre_supply/latest_supply_pack.md`\n- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。\n- `DeepSeek`：已创建前置供料任务卡与执行后风险复核任务卡并运行 safe runner，前置供料与 post-risk review 均为 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md`、`codex_log/supply_requests/20260601_对标文案学习标准_post_risk_review_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_post_risk_review/latest_supply_pack.md`\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "snippet": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。\n`12_参考到执行落地契约_reference_to_execution_contract.md` 是 GPT Project / ChatGPT 侧 reference 保真入口。凡用户给 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料，必须先把它转换成 `reference_anchor -> effect_targets -> function_fields -> deviation_check -> done_when`，再下发 Codex 执行。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "snippet": "它负责把用户本轮提供的 5 篇外部对标账号文案，转成后续 ChatGPT / Codex 可读取、可判断、可回审的长期文案质量标准。\n- 替代 `content_validation（内容验证）`。\n- 推进 `send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n-> Codex 只按执行单和仓库规则落地，不凭本地摘要硬猜原文\n- Codex 默认不知道 Google Drive 原文；如 Codex 需要使用原文级 reference，必须由 ChatGPT 桥接到执行单，或由用户当轮提供可读内容 / 链接。\n- 这次 AI / Codex 具体替人接了哪一步？\n现在：AI / Codex 接手一段流程，输出可检查、可修改、可复盘的结果\n- Codex 的价值不是“聪明”，而是把散乱素材、步骤和结果变成可复盘证据。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  }
]
```

## dependency_map（依赖映射）

```json
[
  {
    "source_file": "codex_log/latest.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/03_总索引与阅读顺序.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
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
    "path_or_query": "Google Drive concrete URL or file id is not provided in this task.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review.",
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
    "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "GPT数据源/03_总索引与阅读顺序.md",
    "codex_log/latest.md"
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
  "files_codex_must_review": [],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "codex_log/latest.md",
    "GPT数据源/03_总索引与阅读顺序.md",
    "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md"
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
