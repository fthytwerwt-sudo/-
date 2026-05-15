# 20260515 当前数据目标锚点实例入口补全日志

## 1. route_decision（路由判断）

- `project_route`: `video_factory（视频工厂）`
- `task_type`: `mechanism_or_route_fix（机制 / 路由修补）`、`project_file_change（项目文件修改）`、`field_and_function_landing（字段与函数落地）`、`gpt_project_static_package_sync（GPT Project 静态包同步）`
- `responsibility_layer`: `project_judgment_layer`、`mechanism_fix_layer`、`execution_layer`、`validation_layer`、`sync_layer`
- `large_task_gate`: `triggered`
- `lane`: `audit_lane -> standard_lane`
- `parallel`: `serial_only`
- `execution_permission`: `allowed_for_current_anchor_instance_and_entry_sync`

## 2. state_action_router（项目状态动作总控器）

- `inferred_state`: `current_data_goal_anchor_required`、`current_data_goal_anchor_missing`、`current_data_goal_anchor_waiting_data_expected`、`current_instance_pointer_missing_from_execution_chain`
- `selected_action`: 新增 `codex_log/current_data_goal_anchor.md`，并把当前实例路径接入 `13`、`14`、GPT / ChatGPT 入口、Codex 执行规则、DeepSeek supply request / schema / fixture、`content_route_card V2`、`script_to_timeline_map`、`editing_decision_pack`、`assembly_decision_pack` 和 `data_goal_alignment_check`。
- `blocked_if`: 缺当前锚点仍进入正式视频执行、把 `waiting_data` 写成 `ready`、推进内容 / 发布 / 声音 / 视觉母版状态、读取 secret、生成媒体。

## 3. current_anchor_gap_audit（当前锚点缺口审计）

- `已有机制`: `GPT数据源/13` 已负责目标飞轮、阈值、文案闸门、内容结构反馈、单主变量和 `next_video_execution_prompt`；`GPT数据源/14` 已负责 `data_goal_anchor` 执行总线和完成前 `data_goal_alignment_check`。
- `缺口`: 仓库此前没有稳定的当前实例锚点入口；Codex 知道要读 `data_goal_anchor`，但没有一个规范路径承载“当前这一条 / 下一条视频实际使用的锚点卡”。
- `风险`: 若继续由 Codex 从 `video_goal_card`、`post_publish_review_card`、`data_flywheel_memory` 和 `content_structure_feedback_card` 现场拼，容易出现目标字段漂移、状态误判和供料口径不一致。
- `决策`: 新增 `codex_log/current_data_goal_anchor.md`，只作为当前实例指针；不替代 `13` 的目标飞轮职责，也不替代 `14` 的执行总线职责。

## 4. current_data_goal_anchor（当前数据目标锚点）

- `path`: `codex_log/current_data_goal_anchor.md`
- `file_role`: 当前这一条 / 下一条视频实际使用的数据目标锚点卡。
- `anchor_instance_status`: `waiting_data`
- `data_confidence`: `low`
- `human_review_required`: `true`
- `reason`: 当前 v3.1 灰度测试 24h / 72h / 7d 数据仍待用户回填，不能生成 `ready` 级数据驱动锚点。
- `filled_fields`: `current_north_star_goal`、`current_stage_goal`、`current_state`、`previous_data_summary.missing_fields`、`main_bottleneck`、`primary_variable`、`supporting_variables`、`forbidden_variables`、`success_metric`、`failure_metric`、`post_publish_validation_metric`、`codex_may_adapt`、`codex_must_not_adapt`、`blocked_if`、`done_when`。
- `missing_fields`: `24h_play_count`、`72h_play_count`、`7d_play_count`、`3s_retention`、`completion_rate`、`average_watch_time`、`favorite_count`、`favorite_rate`、`comment_quality`、`dm_count`、`effective_dm_count`、`valid_leads`、正式 `video_goal_card`、正式 `post_publish_review_card`、正式 `next_video_execution_prompt`。

## 5. entry_sync_check（入口同步检查）

- `13`: 已补充正式文案修改后必须生成或更新 `codex_log/current_data_goal_anchor.md`，再进入 Codex 执行。
- `14`: 已补充执行总线优先读取 `codex_log/current_data_goal_anchor.md`；缺当前实例锚点不得进入正式视频执行。
- `GPT / ChatGPT`: `GPT数据源/01`、`03`、`08`、`09`、`10`、`11` 已同步当前锚点读取、状态边界和目标态。
- `Codex`: `codex_source/00`、`01`、`19` 已同步当前锚点读取、阻断和 `waiting_data` 假设版边界。
- `content_route_card V2`: 已补 `current_data_goal_anchor_source.path` 与 `anchor_instance_status`。
- `script_to_timeline_map`: 已补 `current_data_goal_anchor_source` 与 `data_goal_anchor_used`。
- `editing_decision_pack / assembly_decision_pack`: 已补回指当前锚点实例的 source 字段。
- `data_goal_alignment_check`: 已要求检查当前实例锚点，而不是只检查抽象规则。

## 6. deepseek_schema_fixture_sync（DeepSeek schema / fixture 同步）

- `schema`: `codex_source/schemas/deepseek_supply_request.schema.json` 已新增 `current_data_goal_anchor_path` 与 `current_data_goal_anchor_status`。
- `request_schema_doc`: `codex_source/18_deepseek_supply_request_schema.md` 已写入当前锚点路径 / 状态字段。
- `protocol`: `codex_source/17_deepseek_supply_controller_protocol.md` 已要求 DeepSeek supply request 默认接收当前锚点路径与状态。
- `fixture`: `codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json` 已包含当前锚点路径。
- `mechanism_cases`: `codex_source/fixtures/mechanism_inference_function_cases.json` 已新增 missing / waiting_data / ready / alignment_check_missing 4 个 case。
- `this_round_supply_request`: `codex_log/supply_requests/20260515_current_data_goal_anchor_pre_supply_request.json`
- `this_round_deepseek_result`: `blocked_missing_process_env_api_key`
- `secret_boundary`: `env_file_read = false`、`api_key_printed = false`、`api_key_written = false`
- `not_deepseek_conclusion`: `true`

## 7. validation_checks（验证检查）

- `json_parse`: `passed`
- `python_syntax_check`: `passed_for_deepseek_supply_controller_and_safe_runner`
- `fixture_basic_validation`: `passed`
- `jsonschema_full_validation`: `not_tested_full_jsonschema_validation_unavailable`
- `keyword_check`: `passed`
- `forbidden_status_check`: `passed`
- `no_media_generation_check`: `passed`
- `no_secret_diff_check`: `passed`
- `package_manifest_check`: `passed`
- `git_diff_check`: `passed`

## 8. forbidden_status_check（禁止状态检查）

- `content_validation`: `not_advanced`
- `send_ready`: `not_advanced`
- `publish_status`: `not_advanced`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `not_advanced`
- `visual_master_locked`: `not_advanced`

## 9. state_boundary（状态边界）

- `mechanism_written`: `true`
- `current_anchor_instance_ready`: `false_waiting_data`
- `real_video_execution_stability`: `待验证`
- `data_flywheel_real_effect`: `待验证`
- `multi_agent_runtime_stability`: `not_claimed`
- `content_validation`: `not_applicable_not_advanced`

## 10. 下一个目标

下一条真实视频执行前，先由用户 / ChatGPT 或发布后复盘数据把 `codex_log/current_data_goal_anchor.md` 从 `waiting_data` 补齐为 `ready` 或明确 `blocked`；Codex 只有在当前锚点 ready 且完成 `data_goal_alignment_check` 后，才能进入正式数据驱动视频执行。
