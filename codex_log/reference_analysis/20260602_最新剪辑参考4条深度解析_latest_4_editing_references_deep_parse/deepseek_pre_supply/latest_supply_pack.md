# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260601T165246Z`
- `request_id`: `20260602_latest_4_editing_references_pre_supply`
- `request_validation_status`: `passed`
- `task_type`: `reference_analysis_only`
- `trigger_reason`: `mandatory_pre_supply`
- `action`: `editing_decision_pack`
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
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/deepseek_pre_supply_request.json",
  "current_goal": "Deep read-only analysis of 4 latest editing reference videos without rendering or modifying formal mechanism files.",
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
  "current_step": "before writing analysis reports",
  "known_context": [
    "Reference videos are under /Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考",
    "Exactly 4 video files were found before execution",
    "This round may write only codex_log/reference_analysis and dist/reference_analysis artifacts",
    "content_validation and send_ready must not be promoted"
  ],
  "missing_context": [
    "OCR may be unavailable locally; do not invent exact subtitle or keyword text if unreadable",
    "DeepSeek token usage cannot be observed directly by Codex",
    "editing_decision_pack_missing:source_segments",
    "editing_decision_pack_missing:narration_lines",
    "editing_decision_pack_missing:frame_descriptions",
    "editing_decision_pack_missing:editing_question"
  ],
  "decision_needed": "Flag risks in treating reference mechanics as project rules, and list files Codex must keep read-only."
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
  "token_usage_expected": "token_decrement_expected_if_deepseek_real_call_succeeds",
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
    "token_usage_expectation": "token_decrement_expected_if_deepseek_real_call_succeeds",
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
  "token_usage_expectation": "token_decrement_expected_if_deepseek_real_call_succeeds",
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
  "request_id": "20260602_latest_4_editing_references_pre_supply",
  "task_id": "latest_4_editing_references_deep_parse",
  "mandatory_for_every_task": true,
  "participation_level": "mandatory_by_default",
  "pre_supply_required": true,
  "post_review_required": true,
  "codex_vertical_completion_required": true,
  "token_usage_expectation": "token_decrement_expected_if_deepseek_real_call_succeeds",
  "fallback_allowed": true,
  "fallback_not_completion": true,
  "user_explicit_deepseek_required": false,
  "deepseek_must_not_be_skipped_by_codex_discretion": true,
  "current_goal": "Deep read-only analysis of 4 latest editing reference videos without rendering or modifying formal mechanism files.",
  "current_step": "before writing analysis reports",
  "known_context": [
    "Reference videos are under /Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考",
    "Exactly 4 video files were found before execution",
    "This round may write only codex_log/reference_analysis and dist/reference_analysis artifacts",
    "content_validation and send_ready must not be promoted"
  ],
  "missing_context": [
    "OCR may be unavailable locally; do not invent exact subtitle or keyword text if unreadable",
    "DeepSeek token usage cannot be observed directly by Codex"
  ],
  "decision_needed": "Flag risks in treating reference mechanics as project rules, and list files Codex must keep read-only.",
  "expected_output": [
    "file_map",
    "risk_report",
    "context_summary",
    "missing_files",
    "codex_next_input",
    "token_usage_expectation_check"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "output_dir": "codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/deepseek_pre_supply",
    "status_field": "deepseek_participation_report"
  },
  "stop_condition": "",
  "blocked_if": [
    "reference video directory is missing",
    "reference count is not 4",
    "ffprobe or ffmpeg cannot inspect videos",
    "OCR unavailable but exact text is invented",
    "analysis requires external paid API or secret",
    "analysis would modify formal mechanism files or current media"
  ],
  "not_allowed": [
    "DeepSeek must not write files or edit repository files",
    "DeepSeek must not decide project facts or promote project status",
    "fallback_local_only is not a DeepSeek conclusion",
    "Do not claim multi-agent runtime is stable or passed"
  ],
  "deep_supply_mode": {
    "enabled": true,
    "mode": [
      "deep_file_prefetch",
      "post_risk_review"
    ]
  },
  "file_scope": {
    "candidate_files": [
      "AGENTS.md",
      "codex_source/00_codex_readme.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md",
      "codex_source/13_execution_lane_and_parallel_rules.md",
      "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
      "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
      "GPT数据源/11_项目状态动作总控器_机制推理层.md",
      "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
      "codex_log/latest.md"
    ],
    "must_prefetch_files": [
      "AGENTS.md",
      "GPT数据源/11_项目状态动作总控器_机制推理层.md",
      "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
      "codex_source/20_reference_to_execution_contract.md"
    ],
    "optional_prefetch_files": [
      "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/deep_reference_reparse_report.md",
      "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/editing_decision_pack_for_next_round.md"
    ],
    "forbidden_files": [
      ".env",
      ".env.local",
      ".git/",
      "dist/latest_review_pack/",
      "/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考"
    ],
    "secret_files_forbidden": true
  },
  "content_loading_policy": {
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 12,
    "max_chars_per_file": 5000,
    "max_total_chars": 30000,
    "truncate_policy": "front_and_relevant_snippets",
    "redaction_policy": "no_secret_files_no_env_values"
  },
  "output_required": [
    "relevant_file_bundle",
    "exact_snippet_pack",
    "dependency_map",
    "risk_and_conflict_report",
    "missing_or_uncertain_files",
    "codex_next_input",
    "token_usage_expectation_check"
  ]
}

## files_considered（已考虑文件）

```json
[
  "AGENTS.md",
  "GPT数据源/11_项目状态动作总控器_机制推理层.md",
  "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
  "codex_source/20_reference_to_execution_contract.md",
  "codex_source/00_codex_readme.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/13_execution_lane_and_parallel_rules.md",
  "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
  "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
  "codex_log/latest.md",
  "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/deep_reference_reparse_report.md",
  "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/editing_decision_pack_for_next_round.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "AGENTS.md",
  "GPT数据源/11_项目状态动作总控器_机制推理层.md",
  "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
  "codex_source/20_reference_to_execution_contract.md",
  "codex_source/00_codex_readme.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/13_execution_lane_and_parallel_rules.md",
  "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
  "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
  "codex_log/latest.md",
  "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/deep_reference_reparse_report.md",
  "codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/editing_decision_pack_for_next_round.md"
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
    "deep_file_prefetch",
    "post_risk_review"
  ],
  "missing_modes": [
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
    "content_excerpt": "- 需要 GPT Project 上传包地址时，必须先读取 `codex_log/current_local_artifact_paths.md` 或由 Codex 本地审计后给出。\n  - `Codex（唯一写入执行层 / Integrator）`\n  - `DeepSeek（每轮默认只读供料层 / Explorer）`\n- 当前最高机制入口已包含 `Project State Action Router（项目状态动作总控器）`：命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审时，先读 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md`，输出 `state_action_router（项目状态动作总控器）` 后再执行。\n- `DeepSeek（每轮默认只读供料层 / Explorer）` 每轮默认做执行前供料和执行后风险复核，输出上下文压缩、必读文件地图、风险冲突报告、遗漏同步检查和 Codex 下一步输入；不写文件、不拍板项目事实。\n- `Codex（唯一写入执行层 / Integrator）` 默认负责复核原文件、整合 DeepSeek 供料、补齐受影响文件 / 字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、日志和 Git 收尾。\n- Codex 收到 ChatGPT 完整执行单、横向补全包、多文件机制修补或“不要只做一半 / 执行到底”类任务时，必须触发 `Completion Relay Gate（补全接力闸门）`，先生成 `required_output_inventory（必须交付清单）` 与 `child_task_graph（子任务树）`，再执行并做 `remaining_work_check（剩余工作检查）`。\n- `content_validation = not_advanced_by_formal_operation（正式运营不等于内容最终通过；不得写成内容通过）`\n- `send_ready = false`\n- 上述 `content_validation` 是当前发布后阶段口径；不得把它写成 `passed`\n以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。\n- 不允许把 `technical_validation` 写成 `content_validation`\n- PR #7 B、cute card、round34 中段剪辑、TTS 节奏参考、TTS 语音 / 音色候选参考、`visual_route_map.json`、`locked_reference_registry.md` 仍属于 `reference_whitelist（参考白名单）`，后续按任务类型读取路径索引和 registry 复核后可继续使用。\n- 后续所有 v3.1 基线升级必须保留并复核 `visual_route_map.json（视觉路由表）`，不得让段落提示卡、信息卡、骚萌卡共用同一套外壳。\n- Codex 后续不得默认新建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees` 作为外部散工作区。\n- 如果 Codex 判断确实需要 fresh clone / 外部对照 / 外部 worktree / 任何外部目录，必须先停止，回报 `reason（原因）`、`target_path（目标路径）`、`risk（风险）`、`internal_alternative（唯一正式工作区内替代方案）`，等待用户本轮明确确认后才能继续。\n- Codex 只做截图归档、字段提取、缺失标记、初检和交接，不做最终内容判断。\n- `已确认` 正式运营阶段用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格；用户不负责替 GPT / Codex 排查内部执行原因。\n- 当用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，GPT / Codex 必须触发 `self_repair_audit（自修审计）`，自行回查 locked goal、locked title、final script、文案到画面映射、字幕 / 卡片、音轨 / TTS、比例、时间线、导出参数、数据目标锚点、交付基线、Git 同步和是否存在降级冒充完成；不得要求用户诊断内部原因。\n- `Codex` 后续不得降级完成任何正式运营交付任务。凡仓库写明的目标、产物、验证、同步、回报未全部完成，必须 `blocked` 或继续修到满足基线，不得用 fallback、技术预览、局部结果、内部诊断、无声视频、比例错误视频、本地未同步产物或只读报告冒充 `completed`。\n- `Codex` 是视频执行层，不是重新定稿层；可以调整标点、换行、字幕分句、TTS 停顿、素材映射、剪辑节奏、卡片位置、比例和导出，但不得擅自改 `locked_topic`、`locked_title`、`locked_opening_line`、核心判断、人味表达、文案语义或视觉标题卡标题。\n- 如果 `Codex` 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，不得自行改稿。\n- `send_ready` 仍保持 `false`\n## 2.6 Codex 执行前路由闸门 route_decision_gate\n每次执行任何任务前，Codex 必须先完成并输出 `route_decision（路由判断）`。\n5. `deepseek_supply_gate（DeepSeek 供料闸门）`\n   - 每轮任务默认必须创建 `supply_request（供料请求任务卡）` 并尝试 DeepSeek 只读供料；不得由 Codex 凭主观判断跳过。\n   - 必须输出 `deepseek_participation_report（DeepSeek 参与报告）`、`token_usage_expectation_check（token 使用预期检查）`、`fallback_status（fallback 状态）` 和 `not_deepseek_conclusion（是否不是 DeepSeek 结论）`。\n   - 若未真实调用 DeepSeek，必须写 `fallback_local_only` 或 blocked 原因；token 未观察到减少时，不得写 DeepSeek 已深度参与。\n   - 必须列出本轮禁止修改的文件、目录、状态字段或高风险动作；任务涉及《视频工厂》时，默认禁止误改 `content_validation（内容验证）`、`send_ready（可发送状态）`、当前发布状态和 `dist/latest_review_pack/（最新复审包）`，除非用户本轮明确授权。\nCodex 每次执行前，除了判断项目路由、任务类型和责任层级，还必须判断本轮是否触发 `large_task_gate（大任务闸门）`。\n6. Codex 判断单执行器可能遗漏段落、漏读文件、混淆内容层与执行层。\n  原因：Codex 固定入口文件名，不能改。\nCodex 最终回报必须默认包含：",
    "excerpt_range_or_marker": "lines:73-106",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "| `formal_operation_delivery_blocked（正式运营交付阻断）` | 当前链路无法按正式运营基线生成可发布候选片 | 停止当前视频执行线，回写交付边界和停止线 | `AGENTS.md`、Codex 执行规则、当前正式事实、latest、dated log | 不得写阶段完成、内容推进、send_ready 或内容通过 | 当前线 blocked，禁止状态未推进 | 把不合格写成部分完成 |\n| `copy_iteration_system_required（需要文案迭代系统）` | 用户要求记录文案版本、根据数据判断文案改哪一层、或让 ChatGPT 汇报文案好坏 | 运行 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`，生成 registry、V003 raw、结构拆解、决策、brief 和 latest report | `latest_operation_decision_report.json`、`final_user_operation_result.md`、`copy_registry.json`、V003 copy record、V003 structure map | 不得改 raw 原文，不得由 Codex 最终定稿，不得生成正式下一条视频执行 prompt | `latest_copy_iteration_report` 和 `V003_next_copy_revision_brief` 均存在且验证通过 | 只写概念、缺脚本、缺 ChatGPT 可读报告 |\n| `repair_session_required（修片会话卡必需）` | 修片、发布前修复或重生成既有候选片 | 读取或创建 `current_repair_session`，从 latest / review pack / summary / manifest 恢复上一轮状态，锁本轮唯一主修问题，执行后更新 remaining_blockers | `codex_log/latest.md`、当前 review pack、`summary.json`、`review_manifest.md`、本轮执行单 | 不得从 prompt 猜上一轮状态，不得无人审推进 send_ready，不得一次混修多个最高优先级问题 | 状态卡存在，目标对象、锁定目标、已知问题、主修问题、验证项和剩余阻断清楚 | target_candidate 不明、上一轮状态不可恢复、locked_goal 冲突 |\n| `deepseek_supply_required（DeepSeek 供料必需）` | 任一 Codex 任务进入执行前 | 创建 `supply_request`，优先通过 `DeepSeek runtime provider` 运行执行前供料，输出 `deepseek_supply_gate` | DeepSeek 协议、request schema、controller、Codex 执行规则、runtime provider、safe runner | 不得由 Codex 主观跳过，不得让 controller / explorer 直接读取 `.env`，不得把缺 key 或 fallback 写成 passed | 供料来源、provider 状态、参与状态、token 检查、Codex 下一步输入清楚；provider 缺 key 时写 `runtime_setup_required` | 未建任务卡却继续写文件，或用 fallback 冒充 DeepSeek |\n| `deepseek_runtime_provider_ready（DeepSeek 运行时供应商就绪）` | runtime doctor 通过，且真实 DeepSeek 调用 passed | 允许需要 DeepSeek 的任务通过 safe runner 注入子进程 env | provider、doctor、safe runner、controller、explorer、participation report | 不得打印 / 写入 / 提交 key，不得让 DeepSeek 写文件 | `runtime_provider.status = ready`、`can_call_deepseek = true`、`api_key_printed = false`、`api_key_written = false` | key 泄露、provider 状态缺失或真实调用未通过 |\n| `deepseek_runtime_provider_setup_required（DeepSeek 运行时供应商需要安装）` | provider 找不到 key source，或 key source 被 Git 跟踪风险命中 | 进入一次性 setup 流程，指向 `.env.local`、`.env` 或本地未跟踪授权文件 | setup 脚本、本地授权说明、`.gitignore` | 不得重复每轮只报 process env 缺 key，不得写真实参与 | 输出 `runtime_setup_required` 和补一次即可的配置说明 | 继续 fallback 并写 completed |\n| `deepseek_multi_task_supply_required（DeepSeek 多任务供料必需）` | 大任务、多个供料 request，或用户要求 2-3 个任务分别报告 | 使用 multi-task runner 逐个 request 运行，并生成 per-task report + combined report | multi-task runner、request files、combined report | 不得只给一个总报告，不得用 fallback 冒充任一任务 passed | 每个 request 有 `participation_report.json`，combined report 统计清楚 | 少任一任务报告或统计不完整 |\n| `deepseek_multi_task_supply_passed（DeepSeek 多任务供料通过）` | combined report 显示 `deepseek_passed_count >= 2`、`fallback_count = 0`、`blocked_count = 0` | Codex 可继续整合供料并同步 runtime provider 口径 | combined report、per-task reports、doctor report | 不得写 multi-agent runtime 已跑通，不得推进内容 / 发布 / 声音 / 视觉状态 | 多任务真实供料本地技术验证通过 | 把技术验证写成长期稳定或内容通过 |\n| `deepseek_multi_task_supply_blocked（DeepSeek 多任务供料阻断）` | 任一 required request fallback 或 blocked，且用户要求 DeepSeek 必须参与 | 停止写 completed，修 provider / request / network / schema 后重跑 | combined report、blocked task report、controller manifest | 不得把未通过任务吞掉，不得继续写 completed | blocked 原因清楚并有修复路径 | `fallback_count > 0` 或 `blocked_count > 0` 仍写完成 |\n| `deepseek_pre_supply_missing（DeepSeek 执行前供料缺失）` | 进入写入前没有供料包 / 任务卡 | `create_supply_request` + `run_deepseek_pre_supply`，无法真实调用则写 fallback / blocked | DeepSeek 协议、controller 输出、latest supply pack | 不得写 DeepSeek 真实参与 | `file_map / risk_report / context_summary / missing_files / codex_next_input` 已存在或 blocked 原因清楚 | 用本地判断冒充 DeepSeek |\n| `deepseek_post_review_missing（DeepSeek 执行后复核缺失）` | Codex 已修改但未做 DeepSeek 风险复核 | `run_deepseek_post_risk_review` | diff、修改文件、DeepSeek 协议、latest supply pack | 不得推进状态或写 completed | `status_promotion_risk / forbidden_change_risk / missed_sync_files / fallback_mislabel_risk / remaining_work` 已检查 | 缺执行后复核却写完成 |\n| `deepseek_claim_without_token_usage（无 token 证据声称 DeepSeek 参与）` | token 未观察到减少或未真实调用却写 DeepSeek 深度参与 | 标记 `fallback_local_only` 或 blocked，要求用户检查 token 用量 | controller 输出、用户 token 面板 / 运行日志 | 不得写 `deepseek_passed` 或 DeepSeek 深度参与完成 | `token_usage_expectation_check` 清楚 | token 没减少仍写参与完成 |\n| `codex_vertical_completion_missing（Codex 二次补全缺失）` | 只改协议或单文件，未同步脚本 / schema / fixture / 日志 / 上传包 | `run_codex_vertical_completion` | route_decision、影响面检查、schema、fixtures、日志、路径索引 | 不得把点状修改写完成 | 必交付清单、影响面、验证、同步回写完成 | 只写规则、不接脚本和验收链 |\n| `data_goal_anchor_needed（需要数据目标锚点）` | 文案修改、视频执行、剪辑、编排、DeepSeek 供料或复盘任务缺 `data_goal_anchor` | `create_data_goal_anchor` 或回读 13 / 14 / review_loop 后补齐锚点 | 13 数据飞轮、14 数据目标执行总线、当前 video_goal / post_publish_review / data_flywheel_memory | 不得进入视频执行，不得改写目标 | 锚点字段齐全，主短板、主变量、禁止变量和验证指标明确 | 缺锚点仍执行 |\n| `current_data_goal_anchor_required（需要当前数据目标锚点）` | 命中文案修改、下一条视频、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 同步 | 读取或创建 `codex_log/current_data_goal_anchor.md` | 13、14、`codex_log/current_data_goal_anchor.md`、current_gray_test_target、current_publish_target | 不得从多张卡现场拼锚点后直接执行 | 当前实例路径、状态、缺失字\n...[truncated]",
    "excerpt_range_or_marker": "lines:41-56",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段和可验证标准。\n- Codex 需要根据 reference 生成或修改产物。\n如果触发条件成立，ChatGPT 不得把 reference 原样平移给 Codex，必须先生成本契约字段。\n- `reference_id`：能复核的参考编号、文件名、路径、用户描述或外部资料标题。\n`function_fields（执行函数字段）` 用来让 Codex 在执行前知道：输入信号是什么、该做什么、为什么做、怎么验收、失败时怎么回退。\n- `function_fields_filled`：Codex 已知道执行动作、理由、验证规则和阻断条件。\n- `no_forbidden_status_promotion`：没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek（只读供料层）`：可帮助压缩文字化资料、列风险和文件地图，但不替代 contract。\n- `Codex（唯一写入执行层 / Integrator）`：按 contract 执行、偏离检查、验证、日志和 Git 收尾。\n**凡是用户给 reference / 样片 / 原感稿 / 外部资料并要求 Codex 落地，必须先生成 `Reference-to-Execution Contract（参考到执行落地契约）`；没有契约，不进入执行。**",
    "excerpt_range_or_marker": "lines:5-14",
    "confidence": "high"
  },
  {
    "path": "codex_source/20_reference_to_execution_contract.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Reference-to-Execution Contract（参考到执行落地契约）` 规则。\n它负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段、偏离检查和完成验收。\n- 推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\nCodex 每次执行带 reference 的任务前，必须先输出：\n## 3. Codex 执行前判断\nCodex 执行侧状态新增：\n## 6. 与 DeepSeek / Perplexity 的边界\nDeepSeek / fallback 供料包可选携带以下 reference contract 字段，辅助 Codex 判断：\n- DeepSeek 只读供料，不写文件，不拍板项目事实。\n- DeepSeek / fallback 只能辅助整理文字化 reference 资料、风险冲突和候选字段。\n- DeepSeek / Perplexity 摘要不得替代 `Reference-to-Execution Contract`。\n- Codex 必须复核原文件和用户本轮输入，再执行和验证。\n不得让 DeepSeek / Perplexity 摘要替代原 reference contract\n- 不得因为技术生成成功就写 `content_validation = passed`。\nCodex 收尾前必须检查：\n  deepseek_not_substitute_contract:\n- Codex 必须继续补齐；若无法补齐，则写 `blocked（阻断）`。\n**凡任务带 reference，Codex 必须先把 reference 拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when`；没有契约，不进入执行，不能写 completed。**",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n后续唯一推荐修复路线改为 `route_b_migrate_old_b_to_minimax（旧 B 迁移到 MiniMax）`。MiniMax 必须通过旧 B 参考音频生成或克隆出新的 MiniMax 声音身份；当前百炼代理复刻需要公网 `audio_url`，MiniMax 官方 voice clone 需要上传参考音频拿 `file_id`。缺公网 URL、缺用户授权上传、缺 `generated_minimax_voice_id` 或缺用户试听确认时，必须写 `blocked_need_reference_audio_url` / `pending_reference_audio_url`，不得回退为系统音色候选，也不得推进 `voice_validation = passed`、`final_voice_validated = true` 或 `send_ready = true`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。\n- Codex 不得把本地生成当已 push。\n- Codex 不得把技术成功当内容成功。\n- Codex 不得把“没有明确失败”当完成。\nCodex 在视频执行中负责素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，不负责重新定稿。Codex 可以改标点、换行、字幕分句和 TTS 停顿，但不得改变语义、人味、标题语气、核心判断、前台表达角度，不能用视觉标题卡替换 `locked_title`。\n如果 Codex 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，等待 ChatGPT / 用户确认，不得自行改稿。\n以后凡是任务命中 `publish_candidate（发片候选）`、`video_execution（视频执行）`、`repair_candidate（修片候选）`、`regenerate_video（重新生成视频）`、`pre_publish_fix（发布前修复）`、`final_script_to_video（最终文案进入视频）`，或涉及 `TTS / subtitle / card / timeline / review_pack / privacy_mask / aspect_ratio / visual_evidence` 任一视频执行组件，Codex 必须先跑 `process_boot_gate（流程启动闸门）`。\n- `process_boot_gate` 只防止执行断层，不推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n`workflow_route_decision（工作流归位判断）` 来自 `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`。它不替代 `route_decision`、`state_action_router` 或 `process_boot_gate`；它只负责让 Codex 先归位到文案测试、素材证据、审美剪辑、质量复审、数据复盘或机制修补中的一条工作流。\n    content_validation_issue:\n- 没有人审前不得推进 `send_ready = true`。\n本套件只证明导出前预检链被调用和报告可复核；不自动推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n本文件是《视频工厂》当前 Codex 执行层入口。\n新 Codex 会话默认最少先读：\n每次 Codex 执行前必须先通过 `route_decision（路由判断）`；未输出项目路由、任务类型、责任层级、必读文件与读取状态前，不得执行。\n若任务命中“素材录制 / 录制素材 / 解析视频 / 素材审计 / 第几期素材 / 给 ChatGPT 写素材报告 / 素材证据链 / 平台风险 / 隐私风险”，Codex 必须优先读取项目内 skill：\n没有读取并实际使用该 skill，不得把素材审计任务写成 `completed（已完成）`。该 skill 只允许输出素材索引、素材细节报告、时间码解析、证据强度和风险判断；不得生成视频、写最终文案或推进 `content_validation / send_ready / publish_candidate / current_data_goal_anchor ready`。\n若任务命中长视频、大信息量、多文件、多步骤、多验证，或用户明确提到多 agent / 并发 / 提速，Codex 必须在 `route_decision（路由判断）` 阶段触发 `large_task_gate（大任务闸门）`，并读取 `codex_source/13_execution_lane_and_parallel_rules.md` 与 `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`。\n若任务命中判断权限、卡片判断、判断卡、总结卡、文案到画面映射、HyperFrames 卡片动效或发布候选片检查，Codex 必须读取 `codex_source/21_codex_judgment_permission_matrix.md（Codex 判断权限表）`，并输出 `codex_judgment_permission_gate（Codex 判断权限闸门）` 与 `hyperframes_card_motion_gate（HyperFrames 卡片动效闸门）`。Codex 必须自行判断低风险、可逆、可验证的执行细节；涉及标题、核心观点、文案语义、数据目标、内容是否通过或是否可发送时，只能请求变更、blocked 或升级给 ChatGPT / 用户。\n若任务命中文案修改、下一条视频、根据数据改、播放低 / 收藏低 / 客资弱、复盘后重写、数据飞轮、目标驱动、数据目标、单主变量、内容结构反馈、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步，Codex 必须补读：\n缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。\n命中任何复杂任务、机制修补、文案执行、视频执行、发布复盘、数据回填、GPT Project 静态包同步、Codex 执行结果回审时，Codex 都必须先读：\n命中 `reference（参考）`、样片、参考图、参考视频、参考声音、参考效果、“按这个做”、“像这个效果”、原感稿或外部资料并要求落地时，Codex 必须先读：\n- DeepSeek / Perplexity 摘要只能辅助供料，不得替代 reference contract。\n命中以下任一信号时，Codex 必须先读取 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`、`GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` 与 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`：\n- DeepSeek 供料\n-> Codex video execution preflight\n- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。\n- 本机制写入不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\nCodex 可以调整 segment 拆分、画面顺序、卡片位置、剪辑节奏、TTS 分句和装配顺序；降级方案只能作为 `blocked` 后待用户授权的修复建议，不能作为完成结果。Codex 不得调整 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）` 或发布后验证指标。\n- `Codex` = 唯一写入执行层 / `Integrator`\n- `DeepSeek` = 每轮默认只读供料层 / `Explorer`\n- DeepSeek 是每轮 Codex 任务默认进入的只读 `Explorer（探索器）` / 供料层，默认进入 `DeepSeek deep file supply mode（DeepSeek 深度文件供料模式）`，输出相关文件内容包、关键原文片段包、依赖图、风险冲突报告、执行中增量供料、执行后风险复核和 Codex 下一步输入。\n- DeepSeek 不得写文件，不得拍板项目事实，不得替代 Codex 验证。\n- Codex 仍是唯一写入 `Integrator（统一执行者）`，负责把 DeepSeek 供料整合为可执行改动，执行最小必要复核，并补齐字段、脚本、schema、fixture、日志、上传包、验证和 Git 收尾。\n- Codex 不再默认全仓深读，但必须复核 `will_modify_files（本轮要修改的文件）`、`conflict_or_uncertain_files（冲突 / 不确定文件）`、`validation_failed_files（验证失败关联文件）` 和 `safety_sensitive_files（安全敏感文件）`。\nDeepSeek 供料中控最小入口：\n- 每轮任务在 `route_decision（路由判断）` 后必须输出 `deepseek_supply_gate（DeepSeek 供料闸门）`，并默认运行或准备运行 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py（DeepSeek 安全供料运行器）` 或 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`。\n- Codex 必须先生成或使用 `s\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\n  action = repair the Codex entry routing index only, keep it short, update affected entry files and minimal fixtures/logs, do not add a new big mechanism or promote project status\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:\n  action = create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let Codex continue with minimal necessary review\nif state = deepseek_mid_task_incremental_supply_required:\n  action = create incremental_supply_request with current_child_task, files_already_read, will_modify_files, conflict_points, and failed_validation_logs; run mid_task_incremental_supply before continuing\nif state = deepseek_not_deeply_participated:\n  action = mark blocked or deepseek_not_deeply_participated when user required deep participation but DeepSeek real call, relevant_file_bundle, exact_snippet_pack, or mid-task/post risk supply is missing\nif state = deepseek_pre_supply_missing:\n  action = run_deepseek_pre_supply or mark fallback_local_only / blocked before write\nif state = deepseek_post_review_missing:\n  action = run_deepseek_post_risk_review before completion claim\nif state = deepseek_claim_without_token_usage:\n  action = run token_usage_expectation_check; do not write DeepSeek deep participation\n  action = verify publish_candidate_user_standard_rule; allow only minor flaws that do not affect publishing; block locked copy/title changes, wrong voice route, fallback/silent audio, whole-video drift, core evidence mismatch, subtitle/card blocking evidence, obvious borders/blocks/masks, internal diagnostic only, technical preview only, missing review_pack/preflight, or completion claim without validation; keep send_ready false until user or ChatGPT final confirmation\n  action = verify required_output_inventory, all preflight reports, all gates passed, review_pack contains reports, media probes if media generated, latest updated if mechanism changed, no forbidden status promotion, and publish_candidate_ready_for_human_review does not imply send_ready\n  action = read codex_log/current_data_goal_anchor.md before copy, video execution, editing, assembly, or DeepSeek supply\n  action = allow Codex preflight only after locked fields and data_goal_alignment_check requirement are present\n  action = wire data_goal_anchor into copy, DeepSeek supply, Codex execution, editing, assembly, validation, logs, and GPT Project package\nif input_signal includes judgment_card / 判断卡 / summary_card / 总结卡 / Codex 判断权限 / 判断权限表:\nif input_signal includes Codex 执行下一条视频 / 根据数据执行 / 动态 prompt:\n  action = check locked_topic, locked_title, locked_final_script, locked_opening_line, allowed_copy_changes, forbidden_copy_changes, and copy_change_request_required_if_needed; block if missing or if Codex changed locked copy without approval\n  action = create or read Codex judgment permission matrix and wire it into route_decision, content_route_card V2, card_placement_decision, and completion_truth_check\n- `deepseek_supply_required`：每轮默认成立；不得由 Codex 主观跳过 DeepSeek 供料闸门。\n- `deepseek_pre_supply_missing`：写入前必须先补 `supply_request` 和执行前供料；无法真实调用时写 fallback / blocked。\n- `deepseek_post_review_missing`：修改后必须复核状态偷换、禁止修改、遗漏同步、fallback 误标和剩余工作。\n- `deepseek_claim_without_token_usage`：token 未观察到减少时不得写 DeepSeek 已深度参与。\n- `publish_candidate_user_standard_preflight_required`：按用户打开后原则上可直接发的标准判断候选；小瑕疵可进人工复审，重大缺陷只能 blocked / internal_diagnostic_only，且 `publish_candidate_ready_for_human_review != send_ready`。\n- `codex_execution_structure_drift_risk`：Codex 可以改结构，不能改目标、主短板、主变量、禁止变量和验证指标。\n- `self_repair_audit_required`：用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时触发；Codex 必须自行审计内部执行问题，修复或 blocked，不得要求用户诊断内部原因。\n- `locked_copy_contract_required`：视频执行、发布候选片生成或最终文案转视频时触发；缺 `locked_topic / locked_title / locked_final_script / locked_opening_line` 或 Codex 未授权改写时 blocked。\n- `fallback_requires_user_authorization`：原目标做不到且 Codex 想使用 fallback / 降级方案时触发；降级只能作为 blocked 后的修复建议，用户明确授权前不能作为完成结果。\n- `codex_judgment_permission_matrix_needed`：任务涉及 Codex 什么时候判断 / 什么时候不判断时触发；必须读取 `codex_source/21_codex_judgment_permission_matrix.md` 并输出 execute / change_request / blocked / escalation 边界。\n命中以下任一信号时，Codex 必须先读 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 与 `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`：\n- DeepSeek 供料\n    - data_goal 已定义，但 content_route_card / DeepSeek supply_request / editing_decision_pack / assembly_decision_pack 未接入\n    - Codex 执行可能只按素材、画面或旧流程自由发挥\n    - Codex 需要改写目标而不是调整结构\n- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。\n- 本机制不推进 `content_validation / send_ready / publish_status / voice_va\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/13_execution_lane_and_parallel_rules.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件已有完整 lane / parallel 判断规则；当 `route_decision（路由判断）` 命中 `large_task_gate（大任务闸门）` 时，Codex 必须读取本文件。\n## 3B. DeepSeek 每轮默认只读供料层边界\n`已确认` DeepSeek 在《视频工厂》中的默认定位是：\n- `serial_only（串行执行）` 下也必须先过 `deepseek_supply_gate（DeepSeek 供料闸门）`\nDeepSeek 默认供料不是“是否并发”的判断项。每轮 Codex 任务都要先创建 `supply_request（供料请求任务卡）`，并尝试执行前供料和执行后风险复核；是否开启 Codex native subagent 或多写手并发另行按 lane / parallel 判断。\nDeepSeek 可以输出：\n- `risk_and_conflict_report（风险与冲突报告）`\n- `deepseek_participation_report（DeepSeek 参与报告）`\n- `token_usage_expectation_check（token 使用预期检查）`\n- `post_risk_review（执行后风险复核）`\nDeepSeek 不得：\n- 把 `fallback_local_only（本地兜底）` 写成 DeepSeek 结论\n- 在 token 未观察到减少时写 DeepSeek 已深度参与\n- 替代 Codex 的原文件复核、验证、日志和 Git 收尾\n任何写入仍由 Codex `integrator（统一执行者）` 执行。\n若 DeepSeek 输出与仓库原文件冲突，Codex 必须以仓库原文件为准，并在最终回报中标记冲突。\n- 当前慢点主要不在读取，而在真实执行 / 组装 / 复核\n- DeepSeek 默认作为每轮只读供料层，预先整理上下文包、必读文件地图、风险冲突报告和执行后风险复核；这不等于自动开启并发\n- DeepSeek 默认承担只读供料线；若本轮另开多探索线，DeepSeek 仍不写文件，最终写入仍必须由 Codex integrator 完成",
    "excerpt_range_or_marker": "lines:68-86",
    "confidence": "high"
  },
  {
    "path": "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
    "file_role": "readonly_context",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "# 20｜Codex 执行车道与并发路由说明（给 GPT Project 用）\n5. DeepSeek 默认供料和多 agent 并发的边界怎么分\n- Codex 执行层细则全文\n**本文件只负责让 GPT Project 知道“这轮该走哪条执行车道、能不能并发、该把 Codex 路由成什么结构”，不负责替代 Codex 执行层正文。**\nChatGPT / GPT Project 发现以下任一情况时，应提醒 Codex 在 `route_decision（路由判断）` 阶段进入 `large_task_gate（大任务闸门）`：\nChatGPT 不必每次替 Codex 指定是否多 agent，但必须在 prompt 中提醒大任务触发 lane / parallel 判断。\n最终 lane / parallel 判断由 Codex 按 `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）` 执行。\n触发 `large_task_gate（大任务闸门）` 不等于默认并发；如果写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定，Codex 仍应保持或降级为 `serial_only（串行执行）`。\nChatGPT / GPT Project 发现以下任一情况时，应提醒 Codex 触发 `Completion Relay Gate（补全接力闸门）`：\n2. 任务明确包含 `GPT 横向补全`、`Codex 纵向细化`、`剩余工作检查` 或 `日志同步`。\n4. 本轮涉及机制修补、路由修补、多文件同步、DeepSeek / 多 AI 协作或会影响新聊天默认接手事实。\nGPT Project 下发给 Codex 时，必须提醒 Codex 输出：\n## 2C. DeepSeek 默认供料不是并发可选项\nDeepSeek 当前不是“需要时才叫一下”的并发可选项，而是每轮 Codex 任务默认进入的只读供料层：\n1. Codex 先输出 `route_decision（路由判断）`。\n2. Codex 再输出 `deepseek_supply_gate（DeepSeek 供料闸门）`。\n3. Codex 必须创建或选择 `supply_request（供料请求任务卡）`。\n4. 执行前默认尝试 `run_deepseek_pre_supply（执行前 DeepSeek 供料）`。\n5. Codex 修改后默认执行 `run_deepseek_post_risk_review（执行后 DeepSeek 风险复核）`。\n6. Codex 负责最终整合、补全、验证和写入。\n- DeepSeek 只读供料，不写文件、不 commit、不 push、不拍板项目事实。\n- DeepSeek 默认供料不等于自动开启多写手并发。\n- `fallback_local_only（本地兜底）` 不得写成 DeepSeek 结论。\n- token 未观察到减少时，不得写 DeepSeek 已深度参与。\n8. 一份可直接给 Codex 的 prompt",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "DeepSeek 仍只读供料，Codex 仍是唯一写入执行层；正式运营不代表内容、商业、数据飞轮或 multi-agent runtime 已验证成功。\nGPT 是判断和复盘入口，负责把用户的“不合格 / 不对 / 不顺 / 不美观 / 不是我要的”转成目标、结构、证据、声音、比例、时间线、导出、状态口径和仓库规则的自查任务。Codex 是执行和自查入口，负责复核原文件、修复执行链、补齐规则 / prompt / 日志 / 验证 / Git 同步，或在做不到时写 `blocked（阻断）`。\n不得把用户的“不合格”拆成让用户继续解释大量内部细节；内部错误必须由 GPT / Codex 形成 `self_repair_audit（自修审计）` 和规则修复，不得把文案画面映射、标题改写、字幕 / 卡片 / 音轨 / 比例 / 时间线 / 导出参数、prompt 漏洞或仓库规则漏洞转嫁给用户排查。\nChatGPT / 用户是最终落稿和文案锁定入口；Codex 是执行落地层，不是重新定稿层。凡进入视频执行，必须先建立 `locked_copy_contract（锁定文案契约）`，包含 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。\nCodex 可执行素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，但不得擅自改标题、选题、开头句、核心判断、人味表达或视觉标题卡标题。若认为文案不适合剪辑、画面无法支撑或 TTS 不适配，必须输出 `copy_change_request（文案修改请求）` 或 blocked。\n- `content_validation（内容验证）` 通过判断\n- `send_ready（可发送状态）` 修改\n- DeepSeek API 接入证明\n- 它不替代 Codex 执行规则。\n- 它不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n- `content_validation（内容验证）` 已通过的自动证据\n-> Codex 动态执行 prompt\n- Codex 执行前必须读取 `next_video_execution_prompt（下一条视频执行 prompt）`，并按目标、数据短板、主变量、协同变量、内容结构计划和执行约束落地。\nCodex 负责编排和执行\nDeepSeek 负责供料和风险提醒\n- 视频、DeepSeek、Codex、Perplexity 都围绕 `data_goal_anchor（数据目标锚点）` 工作。\n- DeepSeek 供料必须输出和数据目标相关的文件地图、风险、缺口和执行建议。\n- Codex 是执行结构调度者，但不是目标改写者。\n- Codex 可变的是执行结构，不可变的是 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）` 和验证指标。\n| `Codex` | 唯一写入执行层 / `Integrator` | 负责读仓库、整合 DeepSeek 供料、改文件、补齐字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、Git 收尾 |\n| `DeepSeek` | 每轮默认只读供料层 / `Explorer` | 默认通过 `DeepSeek runtime provider（DeepSeek 运行时供应商）` 加载；负责每轮执行前供料、压缩上下文、输出文件地图和风险冲突报告，并在执行后做风险复核；不写文件 |\n## 5A. GPT -> Codex 补全接力机制\n`Codex` 的职责不是只按第一眼任务改文件，而是把任务地图纵向拆成 `child_task_graph（子任务树）`，建立 `required_output_inventory（必须交付清单）`，逐项执行到底，并在结束前完成 `remaining_work_check（剩余工作检查）` 与 `sync_back_check（同步回写检查）`。\n`DeepSeek` 每轮默认只读供料，不替代 Codex 的原文件复核和执行后反查。`Perplexity` 只做外部研究线索，不直接成为项目正式事实。\n### 5A-1. DeepSeek runtime provider（DeepSeek 运行时供应商）\n`DeepSeek runtime provider（DeepSeek 运行时供应商）` 是 DeepSeek 只读供料层的项目级运行时入口。\n1. Codex 每轮需要 DeepSeek 供料时，默认先调用 `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`。\n2. provider 的授权加载顺序为：`process_env -> .env.local -> .env -> 本地运行配置_local_runtime/deepseek_runtime_authorization.local.json`。\n3. provider 只允许读取 `DEEPSEEK_API_KEY`，且只把 key 注入 DeepSeek 子进程 env；不得把 key 放进 prompt、stdout、stderr、supply pack、manifest、日志或 Git。\n5. 用户明确要求 DeepSeek 必须真实参与时，`fallback_local_only（本地兜底）` 不得视为完成。\n7. DeepSeek 仍只供料和提醒风险，不写文件、不 commit、不 push、不拍板项目事实。\nCodex 二次补全责任：\n1. 必须把 DeepSeek 供料转成可执行改动，不得只复制摘要。\n4. 必须在最终回报写 `deepseek_participation_report（DeepSeek 参与报告）` 与 `token_usage_expectation_check（token 使用预期检查）`。\nCodex 不得把“写入某个机制文件”当成“多 AI 协作机制已经长期稳定”。接力完成必须同时满足：\n| `ChatGPT` | 负责 reference 保真提取与契约化，把用户目标拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when` | 不得只把 reference 原样平移给 Codex，不得只写“风格类似” |\n| `Codex` | 负责按契约执行、验证、偏离检查、日志和 Git 收尾 | 不得在没有契约时直接执行带 reference 的任务，不得把偏离结果写成 completed |\n| `DeepSeek` | 只读辅助供料，可整理文字化 reference 样料、文件地图、风险冲突和候选字段 | 不得替代 reference contract，不得写文件，不得拍板项目事实 |\n| `Perplexity` | 形成外部 reference pack / raw feeling draft，供 ChatGPT 契约化 | 不得直接升级成仓库已确认事实，不得绕过 ChatGPT / Codex 验证 |\n-> Codex executable function fields\n- 本机制不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\n## 6. DeepSeek 每轮默认只读供料层规则\n`DeepSeek` 在本项目中的默认身份是：\n-> deepseek_supply_gate\n-> create_supply_request\n-> relevant_file_bundle\n-> exact_snippet_pack\n-> dependency_map\n-> risk_and_conflict_report\n-> codex_next_input\n-> Codex child_task_graph\n-> Codex write / validate\n-> Codex vertical_completion\n`DeepSeek deep file supply mode（DeepSeek 深度文件供料模式）` 是每轮供料的默认目标形态。DeepSeek 不只输出 `must_read_file_map（必读文件地图）`，而是由 controller / safe runner 在允许范围内读取或接收任务相关文本文件内容，再输出 Codex 可直接执行的上下文包、关键原文片段、依赖关系、冲突提醒和下一步输入。\n如果安全架构不允许模型直接访问本地文件系统，则由 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）` 或 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py（DeepSeek 安全供料运行器）` 读取允许范围内的文本内容，形成 `relevant_file_bundle（相关文件内容包）` 与 `exact_snippet_pack（关键原文片段包）` 后再供给 DeepSeek。DeepSeek 仍不得读取 secret、媒体文件、`.git/`、`dist/latest_review_pack/`，不得写文件、commit、push 或拍板项目事实。\n- `risk_and_conflict_report（风险与冲突报告）`\n- `relevant_file_bundle（相关文件内容包）`\n- `exact_snippet_pack（关键原文片段包）`\n- `dependency_map（依赖关系图）`\n- `missing_or_uncertain_files（缺失或不确定文件）`\nDeepSeek 供料范围从“文件地图 / 风险冲突”扩展为每轮默认深度供料：\n2. `relevant_file_bundle（相关文件内容包）` 与 `exact_snippet_pack（关键原文片段包）`。\n4. 执行后 `post_risk_review（风险复核）`。\n`editing_decision_pack（剪辑决策包）` 只能基于 Codex 提供的文字化素材样料工作，例如 `source_segments（素材片段）`、`narration_lines（口播句子）`、`frame_descriptions（抽帧描述）`、`ocr_text（OCR 文字）` 和 `editing_question（剪辑问题）`。它不直接读取视频、音频、图片或媒体文件。\n`execution_supply_pack family（执行供料包族）` 也只能基于 Codex 提供的文字化任务样料工作，例如 `script_blocks（脚本块）`、`segments（段落）`、`content_route_card（内容路由卡）`、`visual_asset_requirements（视觉素材需求）`、`api_generation_targets（API 生成目标）`、`image\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未改音频、未改素材、未改当前 review pack。\n- `DeepSeek`：本轮执行单禁止外部 API / secret，因此只创建供料任务卡并标记 `deepseek_actual_participation = not_attempted_policy_constraint`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、音频，未改 source video、current review pack 或核心规则。\n- `DeepSeek`：本轮执行单禁止外部 API，因此只创建供料任务卡并标记 `deepseek_actual_participation = not_attempted_policy_constraint`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未生成音频、未改素材、未改当前 review pack。\n- `DeepSeek`：前置供料任务卡 safe runner 返回 `blocked_invalid_context_pack`，因此前置供料不写 DeepSeek 真实参与；执行后风险复核任务卡通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`。本轮不写 DeepSeek 长期稳定。\n- `验证`：`py_compile` passed；`python3 -m unittest tests.test_publish_candidate_preflight_tolerance tests.test_material_parse_pack_reuse_gate` 13/13 passed；fixture / supply JSON parse passed；`git diff --check` passed。当前未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `DeepSeek`：本轮前置供料与执行后风险复核均通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`；token 用量只记录为 `token_decrement_expected`，不写长期稳定。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `已确认` 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。\n- `user_confirmation`：用户确认的不是泛指任意 `V2_prosody_optimized` 方向，而是刚刚 Codex 生成的具体试听样本 `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`。\n- `candidate_status`：`publish_candidate_ready_for_human_review = true`；`voice_validation = pending_user_chatgpt_review`；`final_voice_valida\n...[truncated]",
    "excerpt_range_or_marker": "lines:18-31",
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
    "path": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "snippet": "| `formal_operation_delivery_blocked（正式运营交付阻断）` | 当前链路无法按正式运营基线生成可发布候选片 | 停止当前视频执行线，回写交付边界和停止线 | `AGENTS.md`、Codex 执行规则、当前正式事实、latest、dated log | 不得写阶段完成、内容推进、send_ready 或内容通过 | 当前线 blocked，禁止状态未推进 | 把不合格写成部分完成 |\n| `copy_iteration_system_required（需要文案迭代系统）` | 用户要求记录文案版本、根据数据判断文案改哪一层、或让 ChatGPT 汇报文案好坏 | 运行 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`，生成 registry、V003 raw、结构拆解、决策、brief 和 latest report | `latest_operation_decision_report.json`、`final_user_operation_result.md`、`copy_registry.json`、V003 copy record、V003 structure map | 不得改 raw 原文，不得由 Codex 最终定稿，不得生成正式下一条视频执行 prompt | `latest_copy_iteration_report` 和 `V003_next_copy_revision_brief` 均存在且验证通过 | 只写概念、缺脚本、缺 ChatGPT 可读报告 |\n| `repair_session_required（修片会话卡必需）` | 修片、发布前修复或重生成既有候选片 | 读取或创建 `current_repair_session`，从 latest / review pack / summary / manifest 恢复上一轮状态，锁本轮唯一主修问题，执行后更新 remaining_blockers | `codex_log/latest.md`、当前 review pack、`summary.json`、`review_manifest.md`、本轮执行单 | 不得从 prompt 猜上一轮状态，不得无人审推进 send_ready，不得一次混修多个最高优先级问题 | 状态卡存在，目标对象、锁定目标、已知问题、主修问题、验证项和剩余阻断清楚 | target_candidate 不明、上一轮状态不可恢复、locked_goal 冲突 |\n| `deepseek_supply_required（DeepSeek 供料必需）` | 任一 Codex 任务进入执行前 | 创建 `supply_request`，优先通过 `DeepSeek runtime provider` 运行执行前供料，输出 `deepseek_supply_gate` | DeepSeek 协议、request schema、controller、Codex 执行规则、runtime provider、safe runner | 不得由 Codex 主观跳过，不得让 controller / explorer 直接读取 `.env`，不得把缺 key 或 fallback 写成 passed | 供料来源、provider 状态、参与状态、token 检查、Codex 下一步输入清楚；provider 缺 key 时写 `runtime_setup_required` | 未建任务卡却继续写文件，或用 fallback 冒充 DeepSeek |\n| `deepseek_runtime_provider_ready（DeepSeek 运行时供应商就绪）` | runtime doctor 通过，且真实 DeepSeek 调用 passed | 允许需要 DeepSeek 的任务通过 safe runner 注入子进程 env | provider、doctor、safe runner、controller、explorer、participation report | 不得打印 / 写入 / 提交 key，不得让 DeepSeek 写文件 | `runtime_provider.status = ready`、`can_call_deepseek = true`、`api_key_printed = false`、`api_key_written = false` | key 泄露、provider 状态缺失或真实调用未通过 |\n| `deepseek_runtime_provider_setup_required（DeepSeek 运行时供应商需要安装）` | provider 找不到 key source，或 key source 被 Git 跟踪风险命中 | 进入一次性 setup 流程，指向 `.env.local`、`.env` 或本地未跟踪授权文件 | setup 脚本、本地授权说明、`.gitignore` | 不得重复每轮只报 process env 缺 key，不得写真实参与 | 输出 `runtime_setup_required` 和补一次即可的配置说明 | 继续 fallback 并写 completed |\n| `deepseek_multi_task_supply_required（DeepSeek 多任务供料必需）` | 大任务、多个供料 request，或用户要求 2-3 个任务分别报告 | 使用 multi-task runner 逐个 request 运行，并生成 per-task report + combined report | multi-task runner、request files、combined report | 不得只给一个总报告，不得用 fallback 冒充任一任务 passed | 每个 request 有 `participation_report.json`，combined report 统计清楚 | 少任一任务报告或统计不完整 |\n| `deepseek_multi_task_supply_passed（DeepSeek 多任务供料通过）` | combined report 显示 `deepseek_passed_count >= 2`、`fallback_count = 0`、`blocked_count = 0` | Codex 可继续整合供料并同步 runtime provider 口径 | combined report、per-task reports、doctor report | 不得写 multi-agent runtime 已跑通，不得推进内容 / 发布 / 声音 / 视觉状态 | 多任务真实供料本地技术验证通过 | 把技术验证写成长期稳定或内容通过 |",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "snippet": "本文件负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段和可验证标准。\n- Codex 需要根据 reference 生成或修改产物。\n如果触发条件成立，ChatGPT 不得把 reference 原样平移给 Codex，必须先生成本契约字段。\n- `reference_id`：能复核的参考编号、文件名、路径、用户描述或外部资料标题。\n`function_fields（执行函数字段）` 用来让 Codex 在执行前知道：输入信号是什么、该做什么、为什么做、怎么验收、失败时怎么回退。\n- `function_fields_filled`：Codex 已知道执行动作、理由、验证规则和阻断条件。\n- `no_forbidden_status_promotion`：没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek（只读供料层）`：可帮助压缩文字化资料、列风险和文件地图，但不替代 contract。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/20_reference_to_execution_contract.md",
    "snippet": "本文件是 Codex 执行层的 `Reference-to-Execution Contract（参考到执行落地契约）` 规则。\n它负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段、偏离检查和完成验收。\n- 推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\nCodex 每次执行带 reference 的任务前，必须先输出：\n## 3. Codex 执行前判断\nCodex 执行侧状态新增：\n## 6. 与 DeepSeek / Perplexity 的边界\nDeepSeek / fallback 供料包可选携带以下 reference contract 字段，辅助 Codex 判断：",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/00_codex_readme.md",
    "snippet": "Codex 后续默认先读：\n若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。\n后续唯一推荐修复路线改为 `route_b_migrate_old_b_to_minimax（旧 B 迁移到 MiniMax）`。MiniMax 必须通过旧 B 参考音频生成或克隆出新的 MiniMax 声音身份；当前百炼代理复刻需要公网 `audio_url`，MiniMax 官方 voice clone 需要上传参考音频拿 `file_id`。缺公网 URL、缺用户授权上传、缺 `generated_minimax_voice_id` 或缺用户试听确认时，必须写 `blocked_need_reference_audio_url` / `pending_reference_audio_url`，不得回退为系统音色候选，也不得推进 `voice_validation = passed`、`final_voice_validated = true` 或 `send_ready = true`。\n用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：\n- final script 是否被 Codex 越权改写\n- Codex 不得把 fallback 当完成。\n- Codex 不得把 `internal_diagnostic_only` 当完成。\n- Codex 不得把 `partial result（局部结果）` 当完整交付。",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "snippet": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\n  action = repair the Codex entry routing index only, keep it short, update affected entry files and minimal fixtures/logs, do not add a new big mechanism or promote project status\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/13_execution_lane_and_parallel_rules.md",
    "snippet": "本文件已有完整 lane / parallel 判断规则；当 `route_decision（路由判断）` 命中 `large_task_gate（大任务闸门）` 时，Codex 必须读取本文件。\n## 3B. DeepSeek 每轮默认只读供料层边界\n`已确认` DeepSeek 在《视频工厂》中的默认定位是：\n- `serial_only（串行执行）` 下也必须先过 `deepseek_supply_gate（DeepSeek 供料闸门）`\nDeepSeek 默认供料不是“是否并发”的判断项。每轮 Codex 任务都要先创建 `supply_request（供料请求任务卡）`，并尝试执行前供料和执行后风险复核；是否开启 Codex native subagent 或多写手并发另行按 lane / parallel 判断。\nDeepSeek 可以输出：\n- `risk_and_conflict_report（风险与冲突报告）`\n- `deepseek_participation_report（DeepSeek 参与报告）`",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
    "snippet": "# 20｜Codex 执行车道与并发路由说明（给 GPT Project 用）\n5. DeepSeek 默认供料和多 agent 并发的边界怎么分\n- Codex 执行层细则全文\n**本文件只负责让 GPT Project 知道“这轮该走哪条执行车道、能不能并发、该把 Codex 路由成什么结构”，不负责替代 Codex 执行层正文。**\nChatGPT / GPT Project 发现以下任一情况时，应提醒 Codex 在 `route_decision（路由判断）` 阶段进入 `large_task_gate（大任务闸门）`：\nChatGPT 不必每次替 Codex 指定是否多 agent，但必须在 prompt 中提醒大任务触发 lane / parallel 判断。\n最终 lane / parallel 判断由 Codex 按 `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）` 执行。\n触发 `large_task_gate（大任务闸门）` 不等于默认并发；如果写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定，Codex 仍应保持或降级为 `serial_only（串行执行）`。",
    "why_it_matters": "readonly_context for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
    "snippet": "DeepSeek 仍只读供料，Codex 仍是唯一写入执行层；正式运营不代表内容、商业、数据飞轮或 multi-agent runtime 已验证成功。\nGPT 是判断和复盘入口，负责把用户的“不合格 / 不对 / 不顺 / 不美观 / 不是我要的”转成目标、结构、证据、声音、比例、时间线、导出、状态口径和仓库规则的自查任务。Codex 是执行和自查入口，负责复核原文件、修复执行链、补齐规则 / prompt / 日志 / 验证 / Git 同步，或在做不到时写 `blocked（阻断）`。\n不得把用户的“不合格”拆成让用户继续解释大量内部细节；内部错误必须由 GPT / Codex 形成 `self_repair_audit（自修审计）` 和规则修复，不得把文案画面映射、标题改写、字幕 / 卡片 / 音轨 / 比例 / 时间线 / 导出参数、prompt 漏洞或仓库规则漏洞转嫁给用户排查。\nChatGPT / 用户是最终落稿和文案锁定入口；Codex 是执行落地层，不是重新定稿层。凡进入视频执行，必须先建立 `locked_copy_contract（锁定文案契约）`，包含 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。\nCodex 可执行素材映射、剪辑节奏、字幕断句、卡片布局、音轨生成、比例与导出、证据窗口处理和数据目标对齐检查，但不得擅自改标题、选题、开头句、核心判断、人味表达或视觉标题卡标题。若认为文案不适合剪辑、画面无法支撑或 TTS 不适配，必须输出 `copy_change_request（文案修改请求）` 或 blocked。\n- `content_validation（内容验证）` 通过判断\n- `send_ready（可发送状态）` 修改\n- DeepSeek API 接入证明",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/latest.md",
    "snippet": "- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未改音频、未改素材、未改当前 review pack。\n- `DeepSeek`：本轮执行单禁止外部 API / secret，因此只创建供料任务卡并标记 `deepseek_actual_participation = not_attempted_policy_constraint`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、音频，未改 source video、current review pack 或核心规则。\n- `DeepSeek`：本轮执行单禁止外部 API，因此只创建供料任务卡并标记 `deepseek_actual_participation = not_attempted_policy_constraint`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。\n- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未生成音频、未改素材、未改当前 review pack。\n- `DeepSeek`：前置供料任务卡 safe runner 返回 `blocked_invalid_context_pack`，因此前置供料不写 DeepSeek 真实参与；执行后风险复核任务卡通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`。本轮不写 DeepSeek 长期稳定。\n- `验证`：`py_compile` passed；`python3 -m unittest tests.test_publish_candidate_preflight_tolerance tests.test_material_parse_pack_reuse_gate` 13/13 passed；fixture / supply JSON parse passed；`git diff --check` passed。当前未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。",
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
    "source_file": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "depends_on": [
      "codex_source/20_reference_to_execution_contract.md",
      "codex_source/00_codex_readme.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/13_execution_lane_and_parallel_rules.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "depends_on": [
      "codex_source/20_reference_to_execution_contract.md",
      "codex_source/00_codex_readme.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/13_execution_lane_and_parallel_rules.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/20_reference_to_execution_contract.md",
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
    "source_file": "codex_source/19_project_state_action_router.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/13_execution_lane_and_parallel_rules.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
    "depends_on": [
      "codex_source/20_reference_to_execution_contract.md",
      "codex_source/00_codex_readme.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/13_execution_lane_and_parallel_rules.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_log/latest.md",
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
    "path_or_query": "OCR may be unavailable locally; do not invent exact subtitle or keyword text if unreadable",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "DeepSeek token usage cannot be observed directly by Codex",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  }
]
```

## editing_decision_pack（剪辑决策包）

```json
{
  "sample_source": "supply_request_text_fields_only",
  "data_goal_anchor_used": {},
  "line_group_goal": "待 Codex 基于 script_to_timeline_map 复核",
  "primary_variable_support": "",
  "evidence_role_for_metric": "",
  "forbidden_visuals_by_goal": [],
  "edit_action_reason_against_data_goal": "剪辑建议必须服务主变量，并避免引入 forbidden_variables；具体动作需 Codex 复核原素材。",
  "post_publish_validation_metric": "",
  "missing_context": [
    "source_segments",
    "narration_lines",
    "frame_descriptions",
    "editing_question"
  ],
  "blocked_if_insufficient_editing_sample": true,
  "source_segment": {
    "file_reference": "",
    "time_range": "",
    "visible_content": "",
    "evidence_role": ""
  },
  "narration_intent": {
    "line": "",
    "function": "待 DeepSeek / fallback 基于文字样料补充",
    "viewer_should_understand": "待 Codex 复核原文件后确认"
  },
  "visual_action": {
    "action_type": "do_not_touch",
    "target_area": "待 Codex 复核原素材后确认",
    "timing": ""
  },
  "reason": "供料只能基于文字样料生成剪辑建议，不能替代 Codex 原文件复核。",
  "reference_quality_point": "",
  "risk": [
    "DeepSeek 不直接读取或判断媒体文件。",
    "fallback_local_only 不是 DeepSeek 结论。",
    "文字化样料不足时不得进入真实剪辑执行。"
  ],
  "blocked_if": [
    "缺少 source_segments / narration_lines / frame_descriptions / editing_question 中的关键样料。",
    "需要 DeepSeek 直接读取视频、音频、图片或 dist/latest_review_pack/。",
    "需要把剪辑建议写成最终内容判断。"
  ],
  "codex_execution_note": "Codex 必须先复核素材证据、原文件和当前规则，再决定是否执行剪辑动作。"
}
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
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "codex_source/20_reference_to_execution_contract.md",
    "codex_source/00_codex_readme.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/13_execution_lane_and_parallel_rules.md",
    "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md"
  ],
  "use_as": "readonly_supply_pack",
  "warning": "This pack is local fallback, not a DeepSeek conclusion.",
  "editing_decision_pack_review_required": true,
  "blocked_if_insufficient_editing_sample": true,
  "codex_original_file_review_required": true,
  "recommended_child_tasks": [
    "update_deep_file_supply_contract",
    "update_controller_schema_fixture",
    "run_validation_and_truth_check"
  ],
  "files_codex_must_review": [],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "AGENTS.md",
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "codex_source/20_reference_to_execution_contract.md",
    "codex_source/00_codex_readme.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/13_execution_lane_and_parallel_rules.md",
    "project_source/20_codex_multi_agent_routing_note_for_gpt_project.md",
    "GPT数据源/10_OPC一人公司闭环与多AI协作机制.md",
    "codex_log/latest.md"
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
