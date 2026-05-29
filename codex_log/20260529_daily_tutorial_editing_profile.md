# 20260529｜日常化教学剪辑参数包 Daily Tutorial Editing Profile

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = daily_tutorial_editing_profile_scaffold`
- `已确认` 本轮参考 `GPT数据源/05_文案路由规则.md（文案路由规则）` 的组织方式整理剪辑参数包文件，只复用“文件定位 / 类型分类 / 默认交付包 / 参数包 / 闸门 / 一句话规则”的组织方式，不复制文案规则内容。
- `已新增` `daily_tutorial_profile_v1（日常化教学剪辑参数包）`，状态为 `draft_profile_ready_for_first_real_video_test（草案参数包，等待第一条真实视频验证）`，继承 `default_general_content_v1（默认通用内容参数包）`。
- `定义`：`daily_tutorial（日常化教学）` = 用日常真实场景降低压力，用教学结构交付一个可模仿的小动作。
- `已区分` `daily_tutorial_profile_v1（日常化教学剪辑参数包）` 与 `daily_vlog_profile_v1（日常 / Vlog 剪辑参数包）`；后者仍为 `placeholder_pending_detail` 占位，本轮未被覆盖。
- `已保留` `ecommerce_profile_v1 / tutorial_profile_v1 / daily_vlog_profile_v1` 为占位，本轮未填满电商 / 教学 / 日常 Vlog 完整参数。
- `已接入` `aesthetic_editing_flow（审美剪辑流）`：日常化教学剪辑命中时优先选择 `daily_tutorial_profile_v1`。
- `已接入` `editing_profile_preflight（剪辑参数包预检）`：`daily_tutorial_profile_v1` 可被 registry 识别，不会被误判为 unknown profile。
- `DeepSeek`：已创建前置供料任务卡 `codex_log/supply_requests/20260529_daily_tutorial_editing_profile_pre_supply_request.json` 并运行 safe runner；runtime provider ready，`api_key_printed = false`，`api_key_written = false`，`env_file_read = false`，controller 返回 `blocked_invalid_context_pack`，因此前置供料不写 DeepSeek 真实参与。执行后风险复核任务卡 `codex_log/supply_requests/20260529_daily_tutorial_editing_profile_post_risk_review_request.json` 通过 safe runner，`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`；不写 DeepSeek 长期稳定。
- `验证`：`py_compile` passed；`python3 -m unittest tests.test_publish_candidate_preflight_tolerance tests.test_material_parse_pack_reuse_gate` 13/13 passed；fixture / supply JSON parse passed；`git diff --check` passed。
- `状态边界`：本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未改当前候选片、未推进 `content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`。
- `待验证` 后续必须用第一条真实日常化教学视频、真实素材链、真实 `script_to_shot_execution_map（文案到镜头执行表）` 和审片结果验证该参数包是否足够；本轮不得写成“日常化教学剪辑效果已经真实验证”。
