# 20260517 V004 interim_17h 数据与文案补录

## route_decision（路由判断）

- `project_route`: `video_factory`
- `task_type`: `project_file_change + operation_data_intake + copy_record_backfill + operation_decision_rerun + copy_iteration_rerun`
- `current_project_state`: `formal_operation_active + operation_data_intake + latest_operation_sample_pre_24h`
- `large_task_gate`: triggered
- `lane`: `standard_lane`
- `parallel`: `serial_only`
- `previous_task_status`: V002 文案与 56 / 6 / 9 用户补充数据已完成本地录入和系统验证，但尚未 commit / push；本轮与 V004 统一收尾。

## state_action_router（状态动作总控器）

- `input_signal`: 用户提供 V004 约 17h 数据截图与完整 raw copy，并要求与未提交 V002 补录串行合并。
- `inferred_state`: `operation_data_intake + copy_version_record_missing + latest_sample_pre_24h_intake`
- `selected_action`: 归档截图、新增 V004 snapshot、运营记录、文案 raw record、结构图、文案迭代判断、简报，更新 index / registry / latest，重跑系统。
- `forbidden_action`: `next_formal_video_execution_prompt / content_validation / send_ready / current_data_goal_anchor ready / current_operation_target_switch_without_human_confirmation`
- `done_when`: V002 + V004 均完成记录、系统重跑、日志、commit 和 push。

## V004_identity_decision（V004 身份判断）

- `video_id`: `V004`
- `operation_record_status`: `latest_operation_sample_pre_24h`
- `current_operation_target_switched`: false
- `current_operation_target_kept`: `V003`
- `reason`: V004 仅有 `interim_17h_snapshot`，不是 24h / 72h / 7d final，且缺需求侧字段和人审确认。

## screenshot_archive_status（截图归档状态）

- `archive_status`: `archived_to_repo`
- `overview`: `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_总览_overview_20260517_212049.png`
- `retention_traffic`: `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_流量分析_retention_traffic_20260517_212140.png`
- `audience_profile`: `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_观众分析_audience_profile_20260517_212204.png`

## V004_data_snapshot（V004 数据快照）

- `snapshot_label`: `interim_17h_snapshot`
- `review_window`: `pre_24h`
- `play_count`: 55
- `like_count`: 1
- `favorite_count`: 0
- `completion_rate`: 4.76%
- `two_second_bounce_rate`: 41.18%
- `five_second_completion_rate`: 30.88%
- `average_watch_time`: 14秒
- `recommendation_page`: 95.2%
- `profile_page`: 4.8%
- `new_follow_count`: 0
- `not_72h_final`: true
- `not_7d_final`: true

## V004_copy_record_status（V004 文案记录状态）

- `raw_copy_path`: `review_loop/copy_iteration/V004/V004_copy_v1_raw.md`
- `copy_record`: `review_loop/copy_iteration/V004/V004_copy_v1_record.json`
- `structure_map`: `review_loop/copy_iteration/V004/V004_copy_structure_map.json`
- `copy_decision`: `review_loop/copy_iteration/V004/V004_copy_iteration_decision.json`
- `next_copy_brief`: `review_loop/copy_iteration/V004/V004_next_copy_revision_brief.md`
- `raw_copy_modified`: false
- `actual_metrics.favorite_count`: 0
- `raw_copy_mentions_previous_case_favorite_count`: 3

## system_rerun_result（系统重跑结果）

- `operation_decision_system`: passed；`records_processed = V001 / V002 / V003 / V004`
- `copy_iteration_decision_system`: passed；`copy_registry = V002 / V003 / V004`
- `DeepSeek_pre_supply`: passed；`deepseek_actual_participation = deepseek_passed`，`fallback_status = not_used`
- `current_decision`: 仍不能进入下一期正式执行。

## forbidden_status_check（禁止状态检查）

- `content_validation_advanced`: false
- `send_ready_advanced`: false
- `current_data_goal_anchor_ready`: false
- `next_formal_video_execution_prompt_generated`: false
- `voice_validation_advanced`: false
- `visual_master_locked_advanced`: false
- `V004_direction_failure_concluded`: false
- `V004_content_value_absent_concluded`: false

## remaining_blockers（剩余阻断）

- V004 缺 24h / 72h / 7d final。
- V004 缺 3s retention、profile visit、私信、有效私信、有效咨询、清晰需求客户。
- 是否把 V004 切换为 `current_operation_target` 需要用户 / ChatGPT 后续确认。

## next_target（下一个目标）

等待 V004 24h / 72h / 7d 数据；V003 仍按 current_operation_target 等待 7d 和需求侧字段。补齐前不生成正式下一条视频执行 prompt。
