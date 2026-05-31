# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260531T194439Z`
- `request_id`: `20260601_copy_reference_learning_standard_post_risk_review_request`
- `request_validation_status`: `passed`
- `task_type`: `project_file_change + mechanism_or_route_fix + copywriting`
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
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260601_对标文案学习标准_post_risk_review_request.json",
  "current_goal": "复核本轮对标文案学习标准机制文件和入口引用是否存在重复机制、状态推进、外部文案全文复制、写入范围扩大或遗漏入口。",
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
    "新增 GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md。",
    "更新 GPT数据源/03_总索引与阅读顺序.md、GPT数据源/04_选题与文案规则.md、GPT数据源/05_文案路由规则.md、GPT数据源/07_AI知识类视频价值规则.md、codex_log/latest.md。",
    "本轮不生成新视频、不生成下一条正式视频执行 prompt、不推进任何视频状态。",
    "外部 5 篇对标文案只作为 reference pack 和结构化学习卡，不保存原文全文。"
  ],
  "missing_context": [
    "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review.",
    "Untracked public/ exists before staging and must remain unrelated."
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
  "request_id": "20260601_copy_reference_learning_standard_post_risk_review_request",
  "task_id": "copy_reference_learning_and_plain_language_standard",
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
  "current_goal": "复核本轮对标文案学习标准机制文件和入口引用是否存在重复机制、状态推进、外部文案全文复制、写入范围扩大或遗漏入口。",
  "current_step": "post_write_risk_review",
  "known_context": [
    "新增 GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md。",
    "更新 GPT数据源/03_总索引与阅读顺序.md、GPT数据源/04_选题与文案规则.md、GPT数据源/05_文案路由规则.md、GPT数据源/07_AI知识类视频价值规则.md、codex_log/latest.md。",
    "本轮不生成新视频、不生成下一条正式视频执行 prompt、不推进任何视频状态。",
    "外部 5 篇对标文案只作为 reference pack 和结构化学习卡，不保存原文全文。"
  ],
  "missing_context": [
    "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review.",
    "Untracked public/ exists before staging and must remain unrelated."
  ],
  "decision_needed": "",
  "expected_output": [
    "risk_and_conflict_report",
    "status_promotion_risk_check",
    "duplicate_mechanism_risk_check",
    "raw_copy_contamination_check",
    "codex_next_input"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "read_status_required": true,
    "impact_check_required": true,
    "write_scope": [
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/04_选题与文案规则.md",
      "GPT数据源/05_文案路由规则.md",
      "GPT数据源/07_AI知识类视频价值规则.md",
      "codex_log/latest.md",
      "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
      "codex_log/supply_requests/20260601_对标文案学习标准_post_risk_review_request.json",
      "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/",
      "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_post_risk_review/"
    ],
    "output_dir": "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_post_risk_review",
    "verification_required": [
      "keyword_check",
      "path_reference_check",
      "no_raw_full_copy_check",
      "no_forbidden_status_promotion_check",
      "git_diff_check",
      "secret_scan"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "new file is missing required sections",
    "entry references are missing or point to wrong path",
    "external reference scripts are copied at length into repo",
    "content_validation, send_ready, publish status, voice_validation, final_voice_validated, visual_master_locked, or current_data_goal_anchor ready status is promoted",
    "write scope expands beyond copy mechanism, entry references, latest log, and supply logs",
    "unrelated public/ or dist/deepseek_readonly_explorer changes are staged"
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime is stable or completed.",
    "Do not claim DeepSeek deep participation if token usage was not observed to decrease.",
    "Do not read or copy the raw external reference file.",
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
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/04_选题与文案规则.md",
      "GPT数据源/05_文案路由规则.md",
      "GPT数据源/07_AI知识类视频价值规则.md",
      "codex_log/latest.md"
    ],
    "must_prefetch_files": [
      "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/04_选题与文案规则.md",
      "GPT数据源/05_文案路由规则.md",
      "GPT数据源/07_AI知识类视频价值规则.md",
      "codex_log/latest.md"
    ],
    "optional_prefetch_files": [],
    "forbidden_files": [
      ".env",
      ".env.local",
      "dist/latest_review_pack",
      "素材录制/",
      "GPT 数据源/",
      "public/",
      "/Users/fan/Desktop/文案.rtf"
    ],
    "secret_files_forbidden": true
  },
  "content_loading_policy": {
    "read_only": true,
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 8,
    "max_chars_per_file": 1600,
    "max_total_chars": 16000,
    "truncate_policy": "head_and_relevant_snippets",
    "do_not_read_secret_files": true,
    "do_not_read_external_raw_reference_file": true,
    "do_not_modify_files": true
  },
  "codex_minimal_review_policy": {
    "will_modify_files": [
      "none_post_review_only"
    ],
    "conflict_or_uncertain_files": [
      "GPT数据源/04_选题与文案规则.md",
      "GPT数据源/05_文案路由规则.md"
    ],
    "safety_sensitive_files": [
      "GPT数据源/08_当前正式事实.md",
      "codex_log/current_data_goal_anchor.md",
      "dist/latest_review_pack",
      "public/"
    ]
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
  "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
  "GPT数据源/03_总索引与阅读顺序.md",
  "GPT数据源/04_选题与文案规则.md",
  "GPT数据源/05_文案路由规则.md",
  "GPT数据源/07_AI知识类视频价值规则.md",
  "codex_log/latest.md",
  "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
  "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
  "GPT数据源/03_总索引与阅读顺序.md",
  "GPT数据源/04_选题与文案规则.md",
  "GPT数据源/05_文案路由规则.md",
  "GPT数据源/07_AI知识类视频价值规则.md",
  "codex_log/latest.md",
  "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
  "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md"
]
```

## risks（风险）

```json
[
  "新文件与现有 copy_granularity_mixture_rule 或 reference_copy_voice_mechanism 可能存在机制重复或重叠，需确认无冲突",
  "外部五篇文案仅作为学习卡摘要，但截断内容未提供细节，需验证无大段原文复制",
  "04_选题与文案规则.md 中6D节已有对标文案话语机制，新增15文件可能造成规则冗余或路由矛盾",
  "05_文案路由规则.md 未提供内容，无法确认是否已同步新增入口",
  "新文件缺少 required sections（已确认结构完整，未发现缺失）",
  "entry references 缺失或指向错误路径（待验证04/05/07）",
  "external reference scripts 被全文复制（当前片段未发现，需全文检查）",
  "状态 promotion 涉及 forbidden 状态（无迹象）",
  "write scope 超出指定范围（无迹象）",
  "unrelated public/ 或 dist/ 被误改（无迹象）"
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
    "path": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "它负责把用户本轮提供的 5 篇外部对标账号文案，转成后续 ChatGPT / Codex 可读取、可判断、可回审的长期文案质量标准。\n- 替代 `content_validation（内容验证）`。\n- 推进 `send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n- 这次 AI / Codex 具体替人接了哪一步？\n现在：AI / Codex 接手一段流程，输出可检查、可修改、可复盘的结果\n- Codex 的价值不是“聪明”，而是把散乱素材、步骤和结果变成可复盘证据。\n- AI / Agent / Codex 出现时，是接手某段工作，不是被当成神秘名词。\n它输出了什么能被复核的东西？\n- 写清可编辑、可复核、可手动接管的结果。\n- 适合迁移到 Codex 自动整理素材、生成表格、跑检查、输出报告这类内容。\n- 很适合迁移到“Codex 不是给建议，而是先把一团材料整理成能决策的证据包”。\n- 写 Codex 时可以强调它不是聊天助手，而是执行层和 Integrator。\n- 适合《视频工厂》做工具链、模型链、Codex / ChatGPT / DeepSeek / Perplexity 分工讲解。\n- `Codex 执行层验证者`\n- 把 AI / Codex 写成接手一段工作，而不是万能答案机。\n### 10.4 Codex / AI 生产力选题的应用方式\n写 Codex / AI 生产力时，默认优先回答：\n3. Codex / AI 接手了哪段具体流程？\n5. 最后输出了什么可复核结果？\n13. 有没有把 AI / Codex 写成替用户拍板？\n- `Codex（执行代理）` 素材检查仍必须汇报真实细节、时间码、页面、按钮、动作、结果和证据强度。",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。\n`12_参考到执行落地契约_reference_to_execution_contract.md` 是 GPT Project / ChatGPT 侧 reference 保真入口。凡用户给 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料，必须先把它转换成 `reference_anchor -> effect_targets\n...[truncated]",
    "excerpt_range_or_marker": "lines:23-31",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/04_选题与文案规则.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "Codex 只能做标点、换行、字幕分句和 TTS 停顿等非语义执行调整，不得擅自改写标题、选题、核心判断、人味表达或视觉标题卡标题。若 Codex 判断文案太长、不适合剪辑、画面无法对应或 TTS 不适配，必须输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认；不得自行压缩、重写或替换文案。\n3. `Codex（执行代理）` 做素材技术检查与细节汇报。\n   - `Codex（执行代理）` 不负责最终文案定稿。\n   - `Codex（执行代理）` 必须把素材里可写进最终稿的细节报告给 `ChatGPT（最终落稿与复审入口）`。\n4. `ChatGPT（最终落稿与复审入口）` 基于 `Perplexity（外部参考检索 / 研究工具）` 参考包、用户素材和 `Codex（执行代理）` 细节报告写最终落稿。\n5. `Codex（执行代理）` 再按 `ChatGPT（最终落稿与复审入口）` 最终稿执行视频、字幕、音频、卡片和审片包。\n- `Codex（执行代理）` 素材检查不能被当成 `Codex（执行代理）` 写最终文案。\n- 出现“AI / Codex 帮我做了什么”。\nCodex 帮我自动筛选商品。\n你看这里，Codex 不是在聊天框里随便给建议，它是在我的电脑上直接操作。Codex 在屏幕上打字，先在搜索框里输入品类词，再翻商品卡，一个个看客单价、佣金、销量信号、店铺分、商品分和退货风险。\n- 本规则不授权 `Codex（执行代理）` 改写锁定最终文案；需要语义改动时仍必须输出 `copy_change_request（文案修改请求）`。\n以后最终文案默认继承对标稿的“普通人复杂问题救场”话语机制：先站在用户正在被复杂问题坑的位置说话，再用真实案例、坑点细节和结果变化引出 AI / Codex 的价值；文案要像真人讲给朋友听，不像功能说明，也不像项目报告。\n-> AI / Codex 不是来炫技，而是来接手一段具体工作\nCodex 记录了客单价、佣金、销量信号、店铺分、商品分。\n普通 AI 是给你建议；Codex 这类执行型 AI，是直接替你跑一段流程。但它最值钱的地方不是替你拍板，而是先把混乱商品整理成你能决策的证据表。\nAI 救场句：Codex 帮我初筛商品。\n能力定义句：Codex 是执行型 AI。\n你以为做带货最难的是拍视频，其实第一步就卡在：你根本不知道哪个商品值得测。你刷半天精选联盟，看到的全是商品卡。这个佣金高，那个销量好，但真要拍，你还是不知道先拍哪个。所以这次我没有继续手动翻，而是让 Codex 先替我跑一轮初筛。\n- 本入口不授权 `Codex（执行代理）` 改写锁定最终文案。",
    "excerpt_range_or_marker": "lines:23-41",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/05_文案路由规则.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "用户提供录屏 / 桌面素材进入正式视频执行时，必须优先应用 `source_native_no_mask_visual_rule（源素材比例 + 无遮挡视觉规则）`。该规则优先于旧固定横屏交付口径：除非用户本轮明确指定横屏 16:9 / 1920x1080，Codex 不得为了统一比例强行补灰边、白边、黑边、letterbox、pillarbox 或 padding bands。\n`已确认` 用户提供素材时，默认执行规则是“用户给什么素材，就优先使用什么素材本身”。除非用户本轮明确授权，Codex 不得为了隐私、美观、比例、字幕、卡片或平台风险主动遮挡、洗白、模糊或重塑用户素材。\nCodex 执行视频时不得重新定稿。允许做素材映射、字幕分句、TTS 停顿、剪辑节奏、卡片位置、证据窗口和导出参数；不允许改标题、选题、开头句、核心判断、人味表达、语义或视觉标题卡标题。若需要改文案，必须输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认。\n文案进入视频执行链路后，GPT prompt 只代表本轮 `prompt_delta（增量目标）`，不代表完整流程源。Codex 必须先跑 `process_boot_gate（流程启动闸门）`，输出 `process_boot_report（流程启动报告）`，再决定能否进入素材映射、TTS、字幕、卡片、时间线或审片包执行。\n- 若组件判断需要改 locked 文案语义，Codex 只能输出 `copy_change_request（文案修改请求）` 或 blocked。\n- `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 不等于 `send_ready = true`；`send_ready` 必须等待用户或 ChatGPT 最终确认。\n3. `Codex（执行代理）` 做素材技术检查与细节证据报告。\n4. `ChatGPT（最终落稿与复审入口）` 基于参考包、用户素材和 `Codex（执行代理）` 细节报告写最终落稿。\n5. `Codex（执行代理）` 按最终稿执行视频、字幕、声音、卡片和审片包。\n   - 执行完成后回到 `ChatGPT（最终落稿与复审入口）` 复审；`publish_candidate` 不等于 `send_ready`。\n- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。\n- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，Codex 不得进入视频执行。\n- ChatGPT 读取 `V003_next_copy_revision_brief.md` 后负责最终判断、汇报和改稿；Codex 只负责记录、结构化、生成报告和验证。\n## 3B. `Codex（执行代理）` 素材细节汇报标准\n`Codex（执行代理）` 检查素材时，必须按“给 `ChatGPT（最终落稿与复审入口）` 写最终稿”的标准汇报。\n- 示例包括：`Codex 在屏幕上打字`、点击确认、搜索商品、翻商品卡、记录商品名、价格、佣金、销量信号、店铺分、商品分、风险，写入云盘表格，最后回到聊天框给结论。\n- 不得写成商品一定能卖、商业闭环成立、内容已验证成功或 `send_ready = true`。\n- 如果文案说 Codex 自动操作电脑，但素材没有操作电脑画面，必须 blocked 或退回改写。\n- 如果文案说 Codex 生成表格，但没有表格、云盘、文件或结果画面，必须 blocked 或退回改写。\n本闸门与 `locked_copy_contract（锁定文案契约）` 不冲突：它只负责执行前密度标注\n...[truncated]",
    "excerpt_range_or_marker": "lines:13-33",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/07_AI知识类视频价值规则.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `ChatGPT（最终落稿与复审入口）` 写最终稿时，必须基于 `Codex（执行代理）` 的素材细节报告校准页面、按钮、动作和结果。\n- AI / Codex 在真实屏幕上打字。\n- AI / Codex 自动点击、搜索、筛选。\n- AI / Codex 翻商品卡。\n- AI / Codex 读取价格、佣金、销量、评分、风险。\n- AI / Codex 把乱商品整理成表。\n- AI / Codex 把结果传到云盘，形成云盘表格或文件。\n- AI / Codex 回到聊天框给清楚结论。\n- AI / Codex 说出哪个商品更适合用户、理由、风险和下一步。\n- 执行型 AI / 专家模式 / Codex 能接手一段具体工作。\nCodex 帮我筛选商品。\n你以为做带货最难的是拍视频，其实第一步就卡在：你根本不知道哪个商品值得测。佣金高的不一定适合你，销量好的可能太卷，内容好拍的也可能退货风险高。所以我让 Codex 先替我跑一轮初筛，把一堆商品卡整理成我能判断的复查表。\n本标准只提升话语价值，不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n- AI / Codex 出现时是不是救场，而不是产品介绍。\n- AI / Agent / Codex 具体接手了哪段工作。\n- 本价值补充不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n进入视频执行前，Codex 必须把 `material_detail_report（素材细节报告）` 转成 `material_evidence_contract（素材证据契约）`，并逐个 `line_group（句组）` 运行 `line_group_evidence_gate（句组证据闸门）`：\n1. 商品卡、候选表、明细表、复查表、聊天框结论是“Codex 选品初筛”类视频的价值主体，必须尽量保留结构可读。\nAI 知识类视频的 `publish_candidate（发片候选）` 必须同时看技术完整性、证据可读性、卡片 / 字幕不遮挡、TTS 韵律、人感顺滑、平台风险和审片包完整性。卡片好看、视频生成成功、TTS 文件存在、技术检查通过，都不等于 `content_validation（内容验证）` 通过。\n- `review_pack（审片包）` 能让 ChatGPT / 用户复核标题、文案、画面、声音、字幕、卡片、证据和剩余阻断。\n- `near_equivalent_material_substitution_report（近似素材替代报告）` 已输出并可复核；主题相近不能替代证据相近，素材无法支撑文案时必须 blocked 等待补素材。\n- `content_validation` 只能由 ChatGPT / 用户最终复审或明确规则链路推进；技术成功不得自动推进。\n- `send_ready`、`voice_validation`、`visual_master_locked`、`current_data_goal_anchor_ready` 不得由发片候选机制自动推进。\n- `publish_candidate_user_standard_pref\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。\n- `DeepSeek`：已创建前置供料任务卡并运行 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md`\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。\n- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 DeepSeek 已参与。\n- `状态边界`：未生成全片旁白，未替换当前视频音轨，未生成视频，未改文案，未改画面，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。\n- `DeepSeek`：前置供料与执行后风险复核均实际运行通过，`deepseek_actual_participation = deepseek_passed`，`fallback_status =\n...[truncated]",
    "excerpt_range_or_marker": "lines:12-21",
    "confidence": "high"
  },
  {
    "path": "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "\"request_id\": \"20260601_copy_reference_learning_standard_pre_supply_request\",\n  \"token_usage_expectation\": \"token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required\",\n  \"user_explicit_deepseek_required\": false,\n  \"deepseek_must_not_be_skipped_by_codex_discretion\": true,\n    \"AGENTS.md 要求 route_decision、large_task_gate、workflow_route_decision、state_action_router 和 DeepSeek supply gate 先于文件写入。\"\n    \"DeepSeek runtime provider key availability is unknown before safe runner attempt.\",\n    \"risk_and_conflict_report\",\n    \"missing_or_uncertain_files\",\n    \"codex_next_input\",\n    \"DeepSeek must not write files.\",\n    \"DeepSeek must not decide project facts.\",\n    \"Do not treat fallback_local_only as a DeepSeek conclusion.\",\n    \"Do not modify media outputs, TTS scripts, editing scripts, API config, dist/latest_review_pack, content_validation, send_ready, publish status, voice_validation, final_voice_validated, visual_master_locked, or current_data_goal_anchor ready status.\"\n      \"codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json\"\n    \"output_dir\": \"codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply\",\n    \"risk_and_conflict_report\",\n    \"missing_or_uncertain_files\",\n    \"codex_next_input\",\n    \"token_usage_expectation_check\"",
    "excerpt_range_or_marker": "lines:2-20",
    "confidence": "high"
  },
  {
    "path": "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# DeepSeek supply controller latest_supply_pack\n- `request_id`: `20260601_copy_reference_learning_standard_pre_supply_request`\n- `supply_source`: `deepseek_passed`\n- `deepseek_generation_status`: `passed_with_retries`\n- `not_deepseek_conclusion`: `false`\n- `deepseek_actual_participation`: `deepseek_passed`\n  \"request_file\": \"/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json\",\n  \"requires_real_deepseek_participation\": false,\n    \"AGENTS.md 要求 route_decision、large_task_gate、workflow_route_decision、state_action_router 和 DeepSeek supply gate 先于文件写入。\"\n    \"DeepSeek runtime provider key availability is unknown before safe runner attempt.\",\n## deepseek_supply_gate（DeepSeek 供料闸门）\n  \"supply_request_created\": true,\n  \"deepseek_call_required\": true,\n  \"deepseek_call_attempted\": true,\n  \"deepseek_actual_participation\": \"deepseek_passed\",\n  \"supply_source\": \"deepseek_passed\",\n  \"not_deepseek_conclusion\": false,\n  \"token_usage_expected\": \"token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required\",\n  \"deepseek_must_not_be_skipped_by_codex_discretion\": true\n## deepseek_readiness_check（DeepSeek 就绪检查）\n  \"supply_source\": \"deepseek_passed\",\n  \"not_deepseek_conclusion\": false,\n  \"deepseek_actual_participation\": \"deepseek_passed\",\n    \"deepseek_passed 才能写 DeepSeek 真实参与。\",\n    \"fallback_local_only 必须写 not_deepseek_conclusion = true。\",\n    \"token 未观察到减少时，不得写 DeepSeek 已深度参与。\",\n    \"不得把 fallback 写成 DeepSeek 稳定供料。\"\n## deepseek_participation_report（DeepSeek 参与报告）\n  \"deepseek_call_real\": true,\n  \"deepsee\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  }
]
```

## exact_snippet_pack（关键原文片段包）

```json
[
  {
    "path": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "snippet": "它负责把用户本轮提供的 5 篇外部对标账号文案，转成后续 ChatGPT / Codex 可读取、可判断、可回审的长期文案质量标准。\n- 替代 `content_validation（内容验证）`。\n- 推进 `send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n- 这次 AI / Codex 具体替人接了哪一步？\n现在：AI / Codex 接手一段流程，输出可检查、可修改、可复盘的结果\n- Codex 的价值不是“聪明”，而是把散乱素材、步骤和结果变成可复盘证据。\n- AI / Agent / Codex 出现时，是接手某段工作，不是被当成神秘名词。\n它输出了什么能被复核的东西？",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "snippet": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。\n`12_参考到执行落地契约_reference_to_execution_contract.md` 是 GPT Project / ChatGPT 侧 reference 保真入口。凡用户给 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料，必须先把它转换成 `reference_anchor -> effect_targets",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/04_选题与文案规则.md",
    "snippet": "Codex 只能做标点、换行、字幕分句和 TTS 停顿等非语义执行调整，不得擅自改写标题、选题、核心判断、人味表达或视觉标题卡标题。若 Codex 判断文案太长、不适合剪辑、画面无法对应或 TTS 不适配，必须输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认；不得自行压缩、重写或替换文案。\n3. `Codex（执行代理）` 做素材技术检查与细节汇报。\n   - `Codex（执行代理）` 不负责最终文案定稿。\n   - `Codex（执行代理）` 必须把素材里可写进最终稿的细节报告给 `ChatGPT（最终落稿与复审入口）`。\n4. `ChatGPT（最终落稿与复审入口）` 基于 `Perplexity（外部参考检索 / 研究工具）` 参考包、用户素材和 `Codex（执行代理）` 细节报告写最终落稿。\n5. `Codex（执行代理）` 再按 `ChatGPT（最终落稿与复审入口）` 最终稿执行视频、字幕、音频、卡片和审片包。\n- `Codex（执行代理）` 素材检查不能被当成 `Codex（执行代理）` 写最终文案。\n- 出现“AI / Codex 帮我做了什么”。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
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
    "path": "codex_log/latest.md",
    "snippet": "- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor_ready`。\n- `DeepSeek`：已创建前置供料任务卡并运行 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`。\n- `日志证据`：`codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json`、`codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md`\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_validated = false`；`send_ready = false`；`content_validation = pending_user_chatgpt_review`。\n- `DeepSeek`：已创建前置供料请求与执行后风险复核请求并运行 safe runner；runtime provider ready，但 controller 均返回 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核 + 百炼 MiniMax 实测，不写 DeepSeek 已参与。\n- `状态边界`：未生成全片旁白，未替换当前视频音轨，未生成视频，未改文案，未改画面，未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
    "snippet": "\"request_id\": \"20260601_copy_reference_learning_standard_pre_supply_request\",\n  \"token_usage_expectation\": \"token_usage_should_decrease_if_real_deepseek_called; otherwise mark fallback_local_only_or_runtime_setup_required\",\n  \"user_explicit_deepseek_required\": false,\n  \"deepseek_must_not_be_skipped_by_codex_discretion\": true,\n    \"AGENTS.md 要求 route_decision、large_task_gate、workflow_route_decision、state_action_router 和 DeepSeek supply gate 先于文件写入。\"\n    \"DeepSeek runtime provider key availability is unknown before safe runner attempt.\",\n    \"risk_and_conflict_report\",\n    \"missing_or_uncertain_files\",",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md",
    "snippet": "# DeepSeek supply controller latest_supply_pack\n- `request_id`: `20260601_copy_reference_learning_standard_pre_supply_request`\n- `supply_source`: `deepseek_passed`\n- `deepseek_generation_status`: `passed_with_retries`\n- `not_deepseek_conclusion`: `false`\n- `deepseek_actual_participation`: `deepseek_passed`\n  \"request_file\": \"/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json\",\n  \"requires_real_deepseek_participation\": false,",
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
    "source_file": "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/03_总索引与阅读顺序.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/04_选题与文案规则.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/05_文案路由规则.md",
    "depends_on": [],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/07_AI知识类视频价值规则.md",
    "depends_on": [],
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
    "source_file": "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md",
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
    "path_or_query": "DeepSeek must not read raw external /Users/fan/Desktop/文案.rtf during post review.",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "Untracked public/ exists before staging and must remain unrelated.",
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
    "GPT数据源/04_选题与文案规则.md",
    "GPT数据源/05_文案路由规则.md",
    "GPT数据源/07_AI知识类视频价值规则.md",
    "codex_log/latest.md",
    "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
    "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md"
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
    "GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md",
    "GPT数据源/03_总索引与阅读顺序.md",
    "GPT数据源/04_选题与文案规则.md",
    "GPT数据源/05_文案路由规则.md",
    "GPT数据源/07_AI知识类视频价值规则.md",
    "codex_log/latest.md",
    "codex_log/supply_requests/20260601_对标文案学习标准_pre_supply_request.json",
    "codex_log/deepseek_supply/20260601_copy_reference_learning_standard_pre_supply/latest_supply_pack.md"
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
