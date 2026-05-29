# 20260529｜剪辑参数包系统架子 Editing Profile System

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = editing_profile_system_scaffold`
- `已确认` 本轮新增 `codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md`，只定义 `editing_profile_schema（剪辑参数包结构）`、`default_editing_profile（默认剪辑参数包）`、`profile_registry（参数包注册表）`、`profile_selection_rule（参数包选择规则）` 与 `profile_override_rule（参数覆盖规则）`。
- `已确认` 默认参数包为 `default_general_content_v1`，用于尚未细分视频类型时的通用兜底；它不是所有片型最终标准。
- `已确认` `profile_registry` 仅预留 `ecommerce_profile_v1 / tutorial_profile_v1 / daily_vlog_profile_v1` 三个入口，状态均为 `placeholder_pending_detail`，并继承 `default_general_content_v1`；本轮未细化电商 / 教学 / 日常完整参数。
- `已接入` `aesthetic_editing_flow（审美剪辑流）`：`must_read` 增加剪辑参数包文件，`required_handoff` 增加 `editing_profile_selected` 与 `profile_id_in_script_to_shot_execution_map`，`blocked_if` 增加缺 profile、占位未继承默认包、单条镜头表缺 `profile_id`。
- `已接入` `editing_profile_gate（剪辑参数包闸门）`：剪辑进入 `editing_decision_pack / script_to_shot_execution_map / publish_candidate_preflight_suite` 前必须选择 `editing_profile`。
- `已接入` `editing_profile_preflight（剪辑参数包预检）`：`scripts/发片候选预检套件_publish_candidate_preflight_suite.py` 新增结构检查，覆盖 `profile_id_missing_in_script_to_shot_execution_map`、`profile_id_not_found_in_profile_registry`、`profile_placeholder_used_without_inheritance` 与 `profile_conflicts_with_user_instruction`。
- `已补 fixture / tests`：`codex_source/fixtures/publish_candidate_preflight_suite_cases.json` 新增 3 个剪辑参数包样例；`tests/test_publish_candidate_preflight_tolerance.py` 新增对应单元测试。
- `DeepSeek`：已创建前置供料任务卡 `codex_log/supply_requests/20260529_editing_profile_system_pre_supply_request.json` 与执行后风险复核任务卡 `codex_log/supply_requests/20260529_editing_profile_system_post_risk_review_request.json` 并运行 safe runner；两次均返回 `deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`，`not_deepseek_conclusion = false`，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`。`token_usage_observed_or_user_check_required = token_decrement_expected`，但未直接观测 token 用量，不能写 DeepSeek 长期稳定。
- `验证`：`py_compile` passed；`python3 -m unittest tests.test_publish_candidate_preflight_tolerance tests.test_material_parse_pack_reuse_gate` 12/12 passed；fixture / supply JSON parse passed；`git diff --check` passed。
- `状态边界`：本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。
- `待验证` 后续真实剪辑任务仍需用真实 `script_to_shot_execution_map（文案到镜头执行表）`、真实素材链和真实审片结果验证参数包是否足够；本轮不得写成“剪辑系统已经验证稳定”。
