# DeepSeek supply controller latest_supply_pack

- `supply_id`: `supply_20260602T090419Z`
- `request_id`: `20260602_ambiguous_goal_clarification_gate_post_risk_review`
- `request_validation_status`: `passed`
- `task_type`: `project_file_change + mechanism_or_route_fix + gpt_project_static_package_sync`
- `trigger_reason`: `mandatory_post_risk_review`
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
  "request_file": "/Users/fan/Documents/视频工厂/codex_log/supply_requests/20260602_需求不确定澄清闸门_post_risk_review_request.json",
  "current_goal": "复核本轮需求不确定澄清闸门、参考目标歧义闸门和 GPT Project 资料同步包是否有入口遗漏、状态越权、媒体/secret 混入或同步包路径问题。",
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
    "本轮应已更新 03、11、12、codex_source 19/20、latest、current_local_artifact_paths。",
    "本轮应已生成 dist/gpt_project_sync_packages/20260602_需求不确定澄清闸门_ambiguous_goal_clarification_gate/。",
    "本轮不应生成视频、音频、图片或修改 dist/latest_review_pack。",
    "本轮不应推进任何内容、发送、发布、声音或视觉母版状态。"
  ],
  "missing_context": [
    "用户是否已经上传 GPT Project UI 不在本轮可验证范围，必须保持未上传边界。",
    "新机制的长期有效性必须等待未来真实任务验证。"
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
  "request_id": "20260602_ambiguous_goal_clarification_gate_post_risk_review",
  "task_id": "ambiguous_goal_clarification_gate_mechanism_patch",
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
  "current_goal": "复核本轮需求不确定澄清闸门、参考目标歧义闸门和 GPT Project 资料同步包是否有入口遗漏、状态越权、媒体/secret 混入或同步包路径问题。",
  "current_step": "post_write_risk_review",
  "known_context": [
    "本轮应已更新 03、11、12、codex_source 19/20、latest、current_local_artifact_paths。",
    "本轮应已生成 dist/gpt_project_sync_packages/20260602_需求不确定澄清闸门_ambiguous_goal_clarification_gate/。",
    "本轮不应生成视频、音频、图片或修改 dist/latest_review_pack。",
    "本轮不应推进任何内容、发送、发布、声音或视觉母版状态。"
  ],
  "missing_context": [
    "用户是否已经上传 GPT Project UI 不在本轮可验证范围，必须保持未上传边界。",
    "新机制的长期有效性必须等待未来真实任务验证。"
  ],
  "decision_needed": "",
  "expected_output": [
    "risk_and_conflict_report",
    "missed_sync_files",
    "status_promotion_risk",
    "sync_package_safety_check",
    "codex_next_input"
  ],
  "codex_next_input": "",
  "return_to_codex": {
    "read_status_required": true,
    "impact_check_required": true,
    "write_scope": [
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/11_项目状态动作总控器_机制推理层.md",
      "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md",
      "codex_log/latest.md",
      "codex_log/current_local_artifact_paths.md",
      "codex_log/supply_requests/20260602_需求不确定澄清闸门_pre_supply_request.json",
      "codex_log/supply_requests/20260602_需求不确定澄清闸门_post_risk_review_request.json",
      "dist/gpt_project_sync_packages/20260602_需求不确定澄清闸门_ambiguous_goal_clarification_gate/"
    ],
    "output_dir": "codex_log/deepseek_supply/20260602_ambiguous_goal_clarification_gate_post_risk_review",
    "verification_required": [
      "keyword_check",
      "no_forbidden_status_promotion_check",
      "sync_package_manifest_check",
      "media_absence_check",
      "secret_scan",
      "git_diff_check"
    ]
  },
  "stop_condition": "",
  "blocked_if": [
    "ambiguous_goal_clarification_needed is missing from 11 and codex_source/19",
    "ambiguous_reference_goal_gate is missing from 12 and codex_source/20",
    "default clarification template is missing",
    "GPT Project sync package has no upload manifest",
    "sync package includes media or secret-like files",
    "current_local_artifact_paths does not record the new package",
    "latest does not record the new package and status boundary",
    "forbidden status fields are promoted"
  ],
  "not_allowed": [
    "DeepSeek must not write files.",
    "DeepSeek must not decide project facts.",
    "Do not treat fallback_local_only as a DeepSeek conclusion.",
    "Do not claim multi-agent runtime is stable or completed.",
    "Do not claim the user uploaded the GPT Project package.",
    "Do not claim the new mechanism is long-term stable.",
    "Do not promote content validation, send readiness, publish success status, voice validation, final voice validation, visual master lock, or current data goal anchor readiness.",
    "Do not include media, public/, secret files, API key, token, or unrelated historical logs in sync package."
  ],
  "deep_supply_mode": {
    "enabled": true,
    "mode": [
      "post_risk_review"
    ]
  },
  "file_scope": {
    "candidate_files": [
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/11_项目状态动作总控器_机制推理层.md",
      "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md",
      "codex_log/latest.md",
      "codex_log/current_local_artifact_paths.md"
    ],
    "must_prefetch_files": [
      "GPT数据源/03_总索引与阅读顺序.md",
      "GPT数据源/11_项目状态动作总控器_机制推理层.md",
      "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md",
      "codex_log/latest.md",
      "codex_log/current_local_artifact_paths.md"
    ],
    "forbidden_files": [
      ".env",
      ".env.local",
      ".env.*",
      "dist/latest_review_pack",
      "public/",
      "素材录制/",
      "dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/"
    ],
    "secret_files_forbidden": true
  },
  "content_loading_policy": {
    "read_only": true,
    "include_file_content": true,
    "include_exact_snippets": true,
    "max_file_count": 7,
    "max_chars_per_file": 2200,
    "max_total_chars": 18000,
    "truncate_policy": "head_and_relevant_snippets",
    "do_not_read_secret_files": true,
    "do_not_read_media_files": true,
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
  "GPT数据源/03_总索引与阅读顺序.md",
  "GPT数据源/11_项目状态动作总控器_机制推理层.md",
  "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/20_reference_to_execution_contract.md",
  "codex_log/latest.md",
  "codex_log/current_local_artifact_paths.md"
]
```

## files_recommended（建议读取文件）

```json
[
  "GPT数据源/03_总索引与阅读顺序.md",
  "GPT数据源/11_项目状态动作总控器_机制推理层.md",
  "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
  "codex_source/19_project_state_action_router.md",
  "codex_source/20_reference_to_execution_contract.md",
  "codex_log/latest.md",
  "codex_log/current_local_artifact_paths.md"
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
    "post_risk_review"
  ],
  "missing_modes": [
    "mid_task_incremental_supply",
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
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n命中 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思`，且用户没有说明要像哪一层时，必须先进入 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）`。ChatGPT / GPT Project 必须先锁视觉观感、剪辑节奏、构图布局、字幕字体、动效、信息密度、证明方式、内容结构、情绪人感或整体观感中的主目标；目标未锁定前不得下发 Codex 执行单。\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。\n`12_参考到执行落地契约_reference_to_execution_contract.md` 是 GPT Project / ChatGPT 侧 reference 保真入口。凡用户给 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料，必须先把它转换成 `reference_anchor -> effect_targets -> function_fields -> deviation_check -> done_when`，再下发 Codex 执行。\n若 reference 目标本身含糊，必须先走 `ambiguous_reference_goal_gate（参考目标歧义闸门）`：确认用户到底要继承第一眼视觉观感、剪辑节奏、构图布局、字幕 / 字体、高亮 / 动效、信息密度、证明方式、内容结构、情绪 / 人感还是整体观感。视觉还原任务缺 `primary_reference_video / keyframe_set / composition_map / typography_map / motion_map / density_map / hierarchy_map / pacing_map / side_by_side_deviation_c\n...[truncated]",
    "excerpt_range_or_marker": "lines:23-33",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "| `formal_operation_delivery_blocked（正式运营交付阻断）` | 当前链路无法按正式运营基线生成可发布候选片 | 停止当前视频执行线，回写交付边界和停止线 | `AGENTS.md`、Codex 执行规则、当前正式事实、latest、dated log | 不得写阶段完成、内容推进、send_ready 或内容通过 | 当前线 blocked，禁止状态未推进 | 把不合格写成部分完成 |\n| `copy_iteration_system_required（需要文案迭代系统）` | 用户要求记录文案版本、根据数据判断文案改哪一层、或让 ChatGPT 汇报文案好坏 | 运行 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`，生成 registry、V003 raw、结构拆解、决策、brief 和 latest report | `latest_operation_decision_report.json`、`final_user_operation_result.md`、`copy_registry.json`、V003 copy record、V003 structure map | 不得改 raw 原文，不得由 Codex 最终定稿，不得生成正式下一条视频执行 prompt | `latest_copy_iteration_report` 和 `V003_next_copy_revision_brief` 均存在且验证通过 | 只写概念、缺脚本、缺 ChatGPT 可读报告 |\n| `ambiguous_goal_clarification_needed（需求不确定，需要澄清）` | 用户说 `1:1`、像对标、最高价值片子、高级感、不是一回事、按这个效果做、完全不像、差点意思、感觉不像 / 不对但未说明层级，或给 reference 但未说明要继承视觉、节奏、结构、语气、证明方式还是整体观感 | 停止直接下发 Codex；先拆出 2-5 个可能含义，锁定唯一主目标或默认优先级；如用户要求不追问直接做，必须写清默认假设、风险、允许变化项和阻断条件 | 本文件、`12_参考到执行落地契约_reference_to_execution_contract.md`、当前正式事实、必要 reference 描述 | 不得用 ChatGPT 自己的解释替用户拍板；不得把机制分析草案当视觉还原标准；不得把“有分屏 / 有高亮 / 有字幕”写成“像参考”；不得在未澄清时下发完整 Codex 成片执行单 | 用户确认目标层级，或已显式写清默认假设、风险、允许变化项和阻断条件；若进入执行，执行单能回指到澄清结果 | 未澄清就下发执行单；用机制名替代用户要的观感；用户反馈“不是一回事”后仍继续局部修补 |\n| `repair_session_required（修片会话卡必需）` | 修片、发布前修复或重生成既有候选片 | 读取或创建 `current_repair_session`，从 latest / review pack / summary / manifest 恢复上一轮状态，锁本轮唯一主修问题，执行后更新 remaining_blockers | `codex_log/latest.md`、当前 review pack、`summary.json`、`review_manifest.md`、本轮执行单 | 不得从 prompt 猜上一轮状态，不得无人审推进 send_ready，不得一次混修多个最高优先级问题 | 状态卡存在，目标对象、锁定目标、已知问题、主修问题、验证项和剩余阻断清楚 | target_candidate 不明、上一轮状态不可恢复、locked_goal 冲突 |\n| `deepseek_supply_required（DeepSeek 供料必需）` | 任一 Codex 任务进入执行前 | 创建 `supply_request`，优先通过 `DeepSeek runtime provider` 运行执行前供料，输出 `deepseek_supply_gate` | DeepSeek 协议、request schema、controller、Codex 执行规则、runtime provider、safe runner | 不得由 Codex 主观跳过，不得让 controller / explorer 直接读取 `.env`，不得把缺 key 或 fallback 写成 passed | 供料来源、provider 状态、参与状态、token 检查、Codex 下一步输入清楚；provider 缺 key 时写 `runtime_setup_required` | 未建任务卡却继续写文件，或用 fallback 冒充 DeepSeek |\n| `deepseek_runtime_provider_ready（DeepSeek 运行时供应商就绪）` | runtime doctor 通过，且真实 DeepSeek 调用 passed | 允许需要 DeepSeek 的任务通过 safe runner 注入子进程 env |\n...[truncated]",
    "excerpt_range_or_marker": "lines:41-47",
    "confidence": "high"
  },
  {
    "path": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "file_role": "project_mechanism_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段和可验证标准。\n- Codex 需要根据 reference 生成或修改产物。\n如果触发条件成立，ChatGPT 不得把 reference 原样平移给 Codex，必须先生成本契约字段。\n缺这些字段，不得进入 Codex 成片执行。\n- `reference_id`：能复核的参考编号、文件名、路径、用户描述或外部资料标题。\n`function_fields（执行函数字段）` 用来让 Codex 在执行前知道：输入信号是什么、该做什么、为什么做、怎么验收、失败时怎么回退。\n- `function_fields_filled`：Codex 已知道执行动作、理由、验证规则和阻断条件。\n- `no_forbidden_status_promotion`：没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek（只读供料层）`：可帮助压缩文字化资料、列风险和文件地图，但不替代 contract。\n- `Codex（唯一写入执行层 / Integrator）`：按 contract 执行、偏离检查、验证、日志和 Git 收尾。\n**凡是用户给 reference / 样片 / 原感稿 / 外部资料并要求 Codex 落地，必须先判断 reference 目标是否清楚；目标含糊时先过 `ambiguous_reference_goal_gate（参考目标歧义闸门）`，目标清楚后再生成 `Reference-to-Execution Contract（参考到执行落地契约）`；没有契约，不进入执行。**",
    "excerpt_range_or_marker": "lines:5-15",
    "confidence": "high"
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\n  action = repair the Codex entry routing index only, keep it short, update affected entry files and minimal fixtures/logs, do not add a new big mechanism or promote project status\n  action = stop concrete execution, list 2-5 possible user-goal layers, require ChatGPT/user confirmation of the primary target or write explicit default assumptions / risks / allowed changes / blocked_if before creating any Codex execution prompt\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification\nif state = deepseek_deep_file_supply_required:\n  action = create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let Codex continue with minimal necessary review\nif state = deepseek_mid_task_incremental_supply_required:\n  action = create incremental_supply_request with current_child_task, files_already_read, will_modify_files, conflict_points, and failed_validation_logs; run mid_task_incremental_supply before continuing\nif state = deepseek_not_deeply_participated:\n  action = mark blocked or deepseek_not_deeply_participated when user required deep participation but DeepSeek real call, relevant_file_bundle, exact_snippet_pack, or mid-task/post risk supply is missing\nif state = deepseek_pre_supply_missing:\n  action = run_deepseek_pre_supply or mark fallback_local_only / blocked before write\nif state = deepseek_post_review_missing:\n  action = run_deepseek_post_risk_review before completion claim\nif state = deepseek_claim_without_token_usage:\n  action = run token_usage_expectation_check; do not write DeepSeek deep participation\n  action = verify publish_candidate_user_standard_rule; allow only minor flaws that do not affect publishing; block locked copy/title changes, wrong voice route, fallback/silent audio, whole-video drift, core evidence mismatch, subtitle/card blocking evidence, obvious borders/blocks/masks, internal\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_source/20_reference_to_execution_contract.md",
    "file_role": "codex_execution_rule_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件是 Codex 执行层的 `Reference-to-Execution Contract（参考到执行落地契约）` 规则。\n它负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段、偏离检查和完成验收。\n- 推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\nCodex 每次执行带 reference 的任务前，必须先输出：\n## 3. Codex 执行前判断\n当 reference 任务出现 `像 / 1:1 / 高级感 / 还原 / 不是一回事 / 按这个效果做 / 完全不像 / 差点意思 / 对标观感 / 参考视频观感`，且没有说明要继承哪一层时，Codex 不得进入具体执行。\n-> selected_action = clarify target layer before reference contract or Codex execution\nCodex 执行侧状态新增：\n## 7. 与 DeepSeek / Perplexity 的边界\nDeepSeek / fallback 供料包可选携带以下 reference contract 字段，辅助 Codex 判断：\n- DeepSeek 只读供料，不写文件，不拍板项目事实。\n- DeepSeek / fallback 只能辅助整理文字化 reference 资料、风险冲突和候选字段。\n- DeepSeek / Perplexity 摘要不得替代 `Reference-to-Execution Contract`。\n- Codex 必须复核原文件和用户本轮输入，再执行和验证。\n不得让 DeepSeek / Perplexity 摘要替代原 reference contract\n- 不得因为技术生成成功就写 `content_validation = passed`。\nCodex 收尾前必须检查：\n  deepseek_not_substitute_contract:\n- Codex 必须继续补齐；若无法补齐，则写 `blocked（阻断）`。\n**凡任务带 reference，Codex 必须先判断 reference 目标是否清楚；目标含糊时先过 `ambiguous_reference_goal_gate（参考目标歧义闸门）`，目标清楚后再拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when`；没有契约，不进入执行，不能写 completed。**",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  },
  {
    "path": "codex_log/latest.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "- `route_decision.selected_state = mechanism_repair_needed + gpt_project_sync_needed + deepseek_supply_required`\n- `已确认` 已新增 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）`，覆盖 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思 / 最高价值片子` 等高歧义目标；目标层级未锁定前不得直接下发 Codex。\n- `已确认` 已写入 ChatGPT / GPT Project 默认澄清模板：用户确认前不下发 Codex；若用户要求不追问直接做，也必须写清默认假设、风险、允许变化项和阻断条件。\n- `已确认` 同步包只包含上传说明、同步说明、变更清单、机制补丁、状态边界、项目入口机制文件副本和 Codex 执行层镜像；不包含视频、图片、音频、源素材、`dist/latest_review_pack/`、secret、API key、token、无关 `public/` 文件或大量历史日志。\n- `DeepSeek pre-supply`：已创建执行前供料任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。\n- `DeepSeek post-risk review`：待执行后置风险复核并回填结果。\n- `日志证据`：`codex_log/supply_requests/20260602_需求不确定澄清闸门_pre_supply_request.json`、`codex_log/deepseek_supply/20260602_ambiguous_goal_clarification_gate_pre_supply/latest_supply_pack.md`\n- `已确认` 抽帧复核发现 overlay 已覆盖全片，不再只停留在开头帧；仍需用户 / ChatGPT 做最终观感复审。\n- `未推进` 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`；本轮状态仍为候选片待人工复审。\n- `DeepSeek`：已创建执行前供料任务卡并运行 safe runner；结果为 `blocked_invalid_context_pack`，`deepseek_actual_participation = not_attempted_policy_violation`，`not_deepseek_conclusion = true`；本轮结论来自 Codex 本地复核与预检结果，不写 DeepSeek 已深度参与。\n- `已确认` 本轮未生成视频、未剪辑媒体、未调用 TTS / 视频 / 图片生成 API，未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek`：已创建执行前供料任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`；token 使用只能写 `token_decrement_expected / not_available_user_check_required`，不写用户 token 面板已确认。\n- `已确认` 仓库只保存学习卡、判断标准、迁移边界和读取规则；Codex 默认不知道 Google Drive 原文，如需使用，必须由 ChatGPT 桥接进执行单或由用户当轮提供可读内容 / 链接。\n- `未推进` 本轮未生成视频、未生成下一条正式视频执行 prompt，未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。\n- `DeepSeek`：已创建前置供料任务卡与执行后风险复核任务卡并运行 safe runner，前置供料与 post-risk review 均为 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_\n...[truncated]",
    "excerpt_range_or_marker": "lines:10-25",
    "confidence": "high"
  },
  {
    "path": "codex_log/current_local_artifact_paths.md",
    "file_role": "current_log_or_request_source",
    "why_relevant": "included_by_supply_request_file_scope_or_context_files",
    "content_excerpt": "本文件记录 Codex 已在本机验证真实存在的《视频工厂》本地产物路径。\n| `new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938` | 新第四期选品初筛无遮挡源比例 + B 语音修复候选片 | 修复上一版灰边 / 白屏 / 黑块 / Serena 声音路线问题，按源素材比例和 B voice route 生成的完整发布候选片，待用户 / ChatGPT 人工复审 | `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/full.mp4` | `true` | 审片包目录：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/`；音轨：`narration.wav`；字幕：`captions.srt` | `2026-05-25 CST` | `codex_log/20260525_visual_no_mask_source_ratio_and_voice_b_fix.md`；`dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/review_manifest.md`；`ffprobe` / `ffmpeg decode` / audio volumedetect 已通过 | `publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`visual_master_locked = false`；`current_data_goal_anchor_ready = false`；`canvas = 3412x1846 source_native_ratio`；`used_b_voice = true`；`used_b_pacing = true`；无默认遮挡 / 无 whiteout / 无黑块 / 无强制 16:9；媒体不提交 Git。 |\n| `new_fourth_episode_selection_publish_candidate_20260525_001803` | 新第四期选品初筛发布候选片 | 基于 locked v0.2 / preflight line_group 生成的完整横屏发布候选片，待用户 / ChatGPT 人工复审 | `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4` | `true` | 审片包目录：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/`；音轨：`narration.wav`；字幕：`captions.srt` | `2026-05-25 CST` | `codex_log/20260524_new_fourth_selection_publish_candidate_tts_unblocked.md`；`dist/new_fourth_episode_selection_publish_candidate_20260525_001803/review_manifest.md`；`ffprobe` / `ffmpeg decode` / audio volumedetect 已通过 | `publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`visual_master_locked = false`；使用阿里 / 百炼正式 TTS，未使用 macOS say / 本地 fallback / 无声预览；媒体不提交 Git。 |\n| `new_fourth_episode_selection_publish_candidate_blocked_20260524_233231` | 新第四期选品初筛发布候选阻断审计包 | 本轮按 locked v0.2 尝试进入发布候选\n...[truncated]",
    "excerpt_range_or_marker": "selected_relevant_lines",
    "confidence": "high"
  }
]
```

## exact_snippet_pack（关键原文片段包）

```json
[
  {
    "path": "GPT数据源/03_总索引与阅读顺序.md",
    "snippet": "1. 用户只负责 `goal_correction（目标修正）`、`page_aesthetic_reference（页面 / 美观 / 观感对标）` 和 `result_quality_feedback（结果是否合格反馈）`；用户不负责替 GPT / Codex 诊断内部执行原因。\n2. Codex 不得降级完成正式运营任务。fallback、技术预览、局部结果、内部诊断、本地未同步产物、无声视频、比例错误视频、只读报告或 route card 不能写 `completed`；做不到仓库写明的目标必须 `blocked`，降级方案只能在 blocked 后等待用户明确授权。\n命中用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，先读 `11_项目状态动作总控器_机制推理层.md` 的 `self_repair_audit_required（自修审计必需）` 与 Codex 执行规则里的 `no_degrade_completion_gate（禁止降级完成闸门）`。\n视频执行前必须有 `locked_copy_contract（锁定文案契约）`：`locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。ChatGPT / 用户是最终落稿和文案锁定入口；Codex 只能执行锁定文案，不能自行改标题、选题、开头句、核心判断或人味表达。\n如 Codex 判断文案无法执行，必须输出 `copy_change_request（文案修改请求）` 或 blocked，不能为了剪辑方便自行改稿。视频执行必须生成 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 级别的 `script_to_timeline_map`，通常每 1-2 句一个 `line_group`；只有段落级映射不得进入成片生成。\n- 让 GPT 与 Codex 在 `10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线 + 对标文案学习标准` 内完成 80% 路由判断、reference 执行保真、数据驱动文案前置判断、数据目标锚定执行和文案说人话回审\n命中 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思`，且用户没有说明要像哪一层时，必须先进入 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）`。ChatGPT / GPT Project 必须先锁视觉观感、剪辑节奏、构图布局、字幕字体、动效、信息密度、证明方式、内容结构、情绪人感或整体观感中的主目标；目标未锁定前不得下发 Codex 执行单。\n当前每轮 Codex 执行还必须进入 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`：`route_decision（路由判断）` 后先建 `supply_request（供料请求任务卡）`，再尝试 DeepSeek 执行前供料；Codex 修改后必须做 DeepSeek 执行后风险复核和 `codex_vertical_completion（Codex 二次补全）`。若 DeepSeek 未真实调用或 token 未观察到减少，必须写 fallback / blocked 状态，不得写 DeepSeek 已深度参与。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "snippet": "| `formal_operation_delivery_blocked（正式运营交付阻断）` | 当前链路无法按正式运营基线生成可发布候选片 | 停止当前视频执行线，回写交付边界和停止线 | `AGENTS.md`、Codex 执行规则、当前正式事实、latest、dated log | 不得写阶段完成、内容推进、send_ready 或内容通过 | 当前线 blocked，禁止状态未推进 | 把不合格写成部分完成 |\n| `copy_iteration_system_required（需要文案迭代系统）` | 用户要求记录文案版本、根据数据判断文案改哪一层、或让 ChatGPT 汇报文案好坏 | 运行 `scripts/文案迭代决策系统_copy_iteration_decision_system.py`，生成 registry、V003 raw、结构拆解、决策、brief 和 latest report | `latest_operation_decision_report.json`、`final_user_operation_result.md`、`copy_registry.json`、V003 copy record、V003 structure map | 不得改 raw 原文，不得由 Codex 最终定稿，不得生成正式下一条视频执行 prompt | `latest_copy_iteration_report` 和 `V003_next_copy_revision_brief` 均存在且验证通过 | 只写概念、缺脚本、缺 ChatGPT 可读报告 |\n| `ambiguous_goal_clarification_needed（需求不确定，需要澄清）` | 用户说 `1:1`、像对标、最高价值片子、高级感、不是一回事、按这个效果做、完全不像、差点意思、感觉不像 / 不对但未说明层级，或给 reference 但未说明要继承视觉、节奏、结构、语气、证明方式还是整体观感 | 停止直接下发 Codex；先拆出 2-5 个可能含义，锁定唯一主目标或默认优先级；如用户要求不追问直接做，必须写清默认假设、风险、允许变化项和阻断条件 | 本文件、`12_参考到执行落地契约_reference_to_execution_contract.md`、当前正式事实、必要 reference 描述 | 不得用 ChatGPT 自己的解释替用户拍板；不得把机制分析草案当视觉还原标准；不得把“有分屏 / 有高亮 / 有字幕”写成“像参考”；不得在未澄清时下发完整 Codex 成片执行单 | 用户确认目标层级，或已显式写清默认假设、风险、允许变化项和阻断条件；若进入执行，执行单能回指到澄清结果 | 未澄清就下发执行单；用机制名替代用户要的观感；用户反馈“不是一回事”后仍继续局部修补 |\n| `repair_session_required（修片会话卡必需）` | 修片、发布前修复或重生成既有候选片 | 读取或创建 `current_repair_session`，从 latest / review pack / summary / manifest 恢复上一轮状态，锁本轮唯一主修问题，执行后更新 remaining_blockers | `codex_log/latest.md`、当前 review pack、`summary.json`、`review_manifest.md`、本轮执行单 | 不得从 prompt 猜上一轮状态，不得无人审推进 send_ready，不得一次混修多个最高优先级问题 | 状态卡存在，目标对象、锁定目标、已知问题、主修问题、验证项和剩余阻断清楚 | target_candidate 不明、上一轮状态不可恢复、locked_goal 冲突 |\n| `deepseek_supply_required（DeepSeek 供料必需）` | 任一 Codex 任务进入执行前 | 创建 `supply_request`，优先通过 `DeepSeek runtime provider` 运行执行前供料，输出 `deepseek_supply_gate` | DeepSeek 协议、request schema、controller、Codex 执行规则、runtime provider、safe runner | 不得由 Codex 主观跳过，不得让 controller / explorer 直接读取 `.env`，不得把缺 key 或 fallback 写成 passed | 供料来源、provider 状态、参与状态、token 检查、Codex 下一步输入清楚；provider 缺 key 时写 `runtime_setup_required` | 未建任务卡却继续写文件，或用 fallback 冒充 DeepSeek |\n| `deepseek_runtime_provider_ready（DeepSeek 运行时供应商就绪）` | runtime doctor 通过，且真实 DeepSeek 调用 passed | 允许需要 DeepSeek 的任务通过 safe runner 注入子进程 env |\n...[truncated]",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "snippet": "本文件负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段和可验证标准。\n- Codex 需要根据 reference 生成或修改产物。\n如果触发条件成立，ChatGPT 不得把 reference 原样平移给 Codex，必须先生成本契约字段。\n缺这些字段，不得进入 Codex 成片执行。\n- `reference_id`：能复核的参考编号、文件名、路径、用户描述或外部资料标题。\n`function_fields（执行函数字段）` 用来让 Codex 在执行前知道：输入信号是什么、该做什么、为什么做、怎么验收、失败时怎么回退。\n- `function_fields_filled`：Codex 已知道执行动作、理由、验证规则和阻断条件。\n- `no_forbidden_status_promotion`：没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。",
    "why_it_matters": "project_mechanism_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/19_project_state_action_router.md",
    "snippet": "本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。\n每次 Codex 任务必须先输出 `route_decision（路由判断）`。\n  - Codex partial completion risk\n## 4. Codex 动作策略\n  action = repair the Codex entry routing index only, keep it short, update affected entry files and minimal fixtures/logs, do not add a new big mechanism or promote project status\n  action = stop concrete execution, list 2-5 possible user-goal layers, require ChatGPT/user confirmation of the primary target or write explicit default assumptions / risks / allowed changes / blocked_if before creating any Codex execution prompt\nif state = deepseek_supply_required:\n  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_source/20_reference_to_execution_contract.md",
    "snippet": "本文件是 Codex 执行层的 `Reference-to-Execution Contract（参考到执行落地契约）` 规则。\n它负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段、偏离检查和完成验收。\n- 推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。\nCodex 每次执行带 reference 的任务前，必须先输出：\n## 3. Codex 执行前判断\n当 reference 任务出现 `像 / 1:1 / 高级感 / 还原 / 不是一回事 / 按这个效果做 / 完全不像 / 差点意思 / 对标观感 / 参考视频观感`，且没有说明要继承哪一层时，Codex 不得进入具体执行。\n-> selected_action = clarify target layer before reference contract or Codex execution\nCodex 执行侧状态新增：",
    "why_it_matters": "codex_execution_rule_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/latest.md",
    "snippet": "- `route_decision.selected_state = mechanism_repair_needed + gpt_project_sync_needed + deepseek_supply_required`\n- `已确认` 已新增 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）`，覆盖 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思 / 最高价值片子` 等高歧义目标；目标层级未锁定前不得直接下发 Codex。\n- `已确认` 已写入 ChatGPT / GPT Project 默认澄清模板：用户确认前不下发 Codex；若用户要求不追问直接做，也必须写清默认假设、风险、允许变化项和阻断条件。\n- `已确认` 同步包只包含上传说明、同步说明、变更清单、机制补丁、状态边界、项目入口机制文件副本和 Codex 执行层镜像；不包含视频、图片、音频、源素材、`dist/latest_review_pack/`、secret、API key、token、无关 `public/` 文件或大量历史日志。\n- `DeepSeek pre-supply`：已创建执行前供料任务卡并运行 safe runner；结果为 `deepseek_actual_participation = deepseek_passed`、`fallback_status = not_used`、`api_key_printed = false`、`api_key_written = false`。\n- `DeepSeek post-risk review`：待执行后置风险复核并回填结果。\n- `日志证据`：`codex_log/supply_requests/20260602_需求不确定澄清闸门_pre_supply_request.json`、`codex_log/deepseek_supply/20260602_ambiguous_goal_clarification_gate_pre_supply/latest_supply_pack.md`\n- `已确认` 抽帧复核发现 overlay 已覆盖全片，不再只停留在开头帧；仍需用户 / ChatGPT 做最终观感复审。",
    "why_it_matters": "current_log_or_request_source for DeepSeek deep file supply mode",
    "codex_should_use_for": "minimal_review_before_write_or_conflict_check",
    "risk_if_ignored": "Codex may keep defaulting to broad self-read or miss fallback / status boundary."
  },
  {
    "path": "codex_log/current_local_artifact_paths.md",
    "snippet": "本文件记录 Codex 已在本机验证真实存在的《视频工厂》本地产物路径。\n| `new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938` | 新第四期选品初筛无遮挡源比例 + B 语音修复候选片 | 修复上一版灰边 / 白屏 / 黑块 / Serena 声音路线问题，按源素材比例和 B voice route 生成的完整发布候选片，待用户 / ChatGPT 人工复审 | `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/full.mp4` | `true` | 审片包目录：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/`；音轨：`narration.wav`；字幕：`captions.srt` | `2026-05-25 CST` | `codex_log/20260525_visual_no_mask_source_ratio_and_voice_b_fix.md`；`dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/review_manifest.md`；`ffprobe` / `ffmpeg decode` / audio volumedetect 已通过 | `publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`visual_master_locked = false`；`current_data_goal_anchor_ready = false`；`canvas = 3412x1846 source_native_ratio`；`used_b_voice = true`；`used_b_pacing = true`；无默认遮挡 / 无 whiteout / 无黑块 / 无强制 16:9；媒体不提交 Git。 |\n| `new_fourth_episode_selection_publish_candidate_20260525_001803` | 新第四期选品初筛发布候选片 | 基于 locked v0.2 / preflight line_group 生成的完整横屏发布候选片，待用户 / ChatGPT 人工复审 | `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4` | `true` | 审片包目录：`/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/`；音轨：`narration.wav`；字幕：`captions.srt` | `2026-05-25 CST` | `codex_log/20260524_new_fourth_selection_publish_candidate_tts_unblocked.md`；`dist/new_fourth_episode_selection_publish_candidate_20260525_001803/review_manifest.md`；`ffprobe` / `ffmpeg decode` / audio volumedetect 已通过 | `publish_candidate_ready_for_human_review = true`；`content_validation = pending_user_chatgpt_review`；`send_ready = false`；`voice_validation = pending_user_chatgpt_review`；`visual_master_locked = false`；使用阿里 / 百炼正式 TTS，未使用 macOS say / 本地 fallback / 无声预览；媒体不提交 Git。 |\n| `new_fourth_episode_selection_publish_candidate_blocked_20260524_233231` | 新第四期选品初筛发布候选阻断审计包 | 本轮按 locked v0.2 尝试进入发布候选\n...[truncated]",
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
    "source_file": "GPT数据源/03_总索引与阅读顺序.md",
    "depends_on": [
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "depends_on": [
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "depends_on": [
      "codex_source/19_project_state_action_router.md",
      "codex_source/20_reference_to_execution_contract.md"
    ],
    "dependency_type": "project_mechanism_mirrors_codex_execution_surface",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/19_project_state_action_router.md",
    "depends_on": [],
    "dependency_type": "readonly_context",
    "impact": "update_together_if_deep_file_supply_contract_changes"
  },
  {
    "source_file": "codex_source/20_reference_to_execution_contract.md",
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
    "source_file": "codex_log/current_local_artifact_paths.md",
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
    "path_or_query": "用户是否已经上传 GPT Project UI 不在本轮可验证范围，必须保持未上传边界。",
    "reason": "request_missing_context",
    "blocked_if_missing": false
  },
  {
    "path_or_query": "新机制的长期有效性必须等待未来真实任务验证。",
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
  "fallback_mislabel_risk": "present",
  "remaining_work": "Codex must run validation, sync logs/package/path index, and report token check boundary."
}
```

## codex_next_input（给 Codex 的下一步输入）

```json
{
  "read_first": [
    "GPT数据源/03_总索引与阅读顺序.md",
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/20_reference_to_execution_contract.md",
    "codex_log/latest.md",
    "codex_log/current_local_artifact_paths.md"
  ],
  "use_as": "readonly_supply_pack",
  "warning": "This pack is local fallback, not a DeepSeek conclusion.",
  "post_risk_review_required": true,
  "status_promotion_risk": "check_required_no_forbidden_status_promotion",
  "forbidden_change_risk": "check_required_no_env_media_or_latest_review_pack_change",
  "missed_sync_files": "check_required_docs_scripts_schema_fixture_logs_package_paths",
  "fallback_mislabel_risk": "present",
  "remaining_work": "Codex must run validation, sync logs/package/path index, and report token check boundary.",
  "recommended_child_tasks": [
    "update_deep_file_supply_contract",
    "update_controller_schema_fixture",
    "run_validation_and_truth_check"
  ],
  "files_codex_must_review": [],
  "files_codex_can_trust_from_deepseek_unless_conflict": [
    "GPT数据源/03_总索引与阅读顺序.md",
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/20_reference_to_execution_contract.md",
    "codex_log/latest.md",
    "codex_log/current_local_artifact_paths.md"
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
