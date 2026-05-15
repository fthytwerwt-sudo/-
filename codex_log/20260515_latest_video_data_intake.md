# 20260515 最新一期视频数据录入 latest_video_data_intake

## route_decision（路由判断）

- `project_route`: `video_factory（视频工厂）`
- `task_type`: `gray_test_data_intake + project_file_change + data_goal_anchor_update + deepseek_supply_required + gpt_project_static_package_sync`
- `responsibility_layer`: `project_judgment_layer + execution_layer + validation_layer + sync_layer`
- `large_task_gate`: `triggered`
- `lane_recommendation`: `serial_only`
- `parallel_recommendation`: `read_parallel_only_for_file_reads`
- `deepseek_supply_gate`: `required`
- `execution_permission`: `granted_after_deepseek_pre_supply_passed`

## state_action_router（项目状态动作总控器）

- `inferred_state`: `gray_test_data_intake`
- `current_video_target_switch_needed`: `true`
- `current_data_goal_anchor_update_needed`: `true`
- `deepseek_supply_required`: `true`
- `gpt_project_static_package_sync`: `required`
- `state_boundary`: 本轮只做截图归档、数据字段回填、早期摘要、DeepSeek 风险复核、日志和上传包同步；不做最终内容复盘，不生成正式下一条视频执行 prompt。

## 视频身份判断

- `current_gray_target_before_this_round`: `V001｜我用 AI 做 PPT 踩过的坑`
- `existing_video_ids_checked`: `V001, V002`
- `V001_title_match_result`: `not_matched`
- `V002_title_match_result`: `not_matched`
- `matched_existing_video`: `false`
- `new_video_id_created`: `V003`
- `title_match_result`: `截图标题与 V001 / V002 均不同，本轮按最新一期视频切换处理。`
- `old_records_policy`: `V001 保留为 previous / historical；V002 保留为平台审核减推异常样本，不覆盖。`

## screenshot_intake_result（截图录入结果）

- `screenshot_count`: `3`
- `screenshot_manifest`: `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md`
- `screenshot_paths`:
  - `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/platform_metrics/V003_interim_36h_总览_overview_20260515_182106.png`
  - `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/audience_retention/V003_interim_36h_流量分析_retention_traffic_20260515_181946.png`
  - `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/audience_profile/V003_interim_36h_观众分析_audience_profile_20260515_182041.png`
- `source_boundary`: 用户上传截图来自 `/Users/fan/Desktop/素材截图/`，已复制到仓库内部；Desktop 路径只作为只读来源。

## data_backfill_result（数据回填结果）

- `record_path`: `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md`
- `structured_snapshot`: `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_早期数据快照_early_interim_snapshot.json`
- `review_window`: `between_24h_and_72h / interim_36h_snapshot`
- `capture_time_if_known`: `2026-05-15 18:19-18:21`
- `publish_time_visible`: `2026-05-14 04:50`
- `inferred_hours_after_publish`: `约 37 小时`

### core_metrics

```yaml
play_count: 141
average_watch_time: "21秒"
cover_click_rate: "0.00%"
two_second_bounce_rate: "50.00%"
average_play_ratio: "8.51%"
completion_rate: "4.17%"
five_second_completion_rate: "28.13%"
like_count: 2
like_rate: "1.42%"
favorite_count: 3
favorite_rate: "2.13%"
comment_count: 0
comment_rate: "0.00%"
share_count: 0
share_rate: "0.00%"
danmu_count: 0
new_follow_count: 1
follow_rate_or_fan_rate_visible: "0.71%"
fan_play_ratio: "4.3%"
```

### traffic_sources

```yaml
recommendation_page: "97.2%"
profile_page: "1.4%"
friend_page: "1.4%"
```

### audience_metrics

```yaml
gender_distribution:
  male: "77%"
  female: "23%"
age_distribution_estimated:
  under_18: "约2%"
  age_18_23: "约20%"
  age_24_30: "约32%"
  age_31_40: "约34%"
  age_41_50: "约9%"
  age_50_plus: "约2%"
region_top_visible:
  广东: "17.27%"
  北京: "13.64%"
  江苏: "9.09%"
  湖北: "5.45%"
  四川: "5.45%"
  河北: "4.55%"
  河南: "4.55%"
  上海: "4.55%"
active_distribution:
  heavy: "72%"
  medium: "18%"
  light: "6%"
  unknown: "4%"
```

## missing_fields（缺失字段）

- `3s_retention`
- `profile_visit_count`
- `dm_count`
- `effective_dm_count`
- `effective_consult_count`
- `clear_need_customer_count`
- `effective_comment_quality`
- `72h_final_data`
- `7d_final_data`

## uncertain_fields（待人工确认字段）

- `exact_observation_window_from_platform`: `uncertain_need_human_check`
- `age_distribution_estimated_from_bar_chart`: `uncertain_need_human_check`
- `trend_curve_point_values`: `uncertain_need_human_check`

## early_diagnosis_summary（早期诊断摘要）

- `traffic_layer`: `draft_low_confidence / weak`。播放量 141，仍处于极小样本早期观察，不写最终失败。
- `opening_retention`: `draft_low_confidence / weak`。2s 跳出率 50.00%，5s 完播率 28.13%，完播率 4.17%，说明前 5 秒承接可能偏弱。
- `content_value_signal`: `draft_low_confidence / small_positive_signal`。收藏率 2.13%，在极小样本下有一点可复用价值信号，但不能放大成方向成立。
- `interaction_signal`: `draft_low_confidence / weak`。评论 0、分享 0，未形成公开需求反馈。
- `lead_signal`: `missing`。未看到私信、有效私信或有效咨询数据，不得写需求成立。
- `not_final_review`: 当前不是最终复盘，不决定方向失败，不决定下一条正式执行，等 72h / 7d 数据后再做正式复盘。

## current_data_goal_anchor_update（当前数据目标锚点更新）

- `anchor_path`: `codex_log/current_data_goal_anchor.md`
- `old_status`: `waiting_data`
- `new_status`: `partial_data_recorded`
- `data_confidence`: `low`
- `main_bottleneck_draft`: `opening_retention_and_initial_distribution_weak / draft_low_confidence`
- `primary_variable_draft`: `opening_route_or_first_5s_packaging / draft_low_confidence`
- `why_not_ready`: 72h / 7d、3s 留存、主页访问、私信、有效咨询和人审最终判断仍缺失。

## DeepSeek 参与

- `pre_supply_request`: `codex_log/supply_requests/20260515_最新视频数据录入_DeepSeek执行前供料_latest_video_data_intake_pre_supply_request.json`
- `pre_supply_output`: `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/pre_supply/latest_supply_pack.md`
- `pre_supply_status`: `deepseek_passed`
- `fallback_count`: `0`
- `blocked_count`: `0`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `post_risk_review_request`: `codex_log/supply_requests/20260515_最新视频数据录入_DeepSeek后置风险复核_latest_video_data_intake_post_risk_review_request.json`
- `post_risk_review_output`: `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/post_risk_review/latest_supply_pack.md`
- `post_risk_review_status`: `deepseek_passed`
- `post_risk_review_findings`: `未发现 V001 / V002 被覆盖或误用；仍需人工确认平台完整观察窗口和年龄分布估读。`

## forbidden_status_check（禁止状态检查）

- `content_validation`: `not_advanced`
- `send_ready`: `not_advanced`
- `publish_status`: `not_advanced_as_success`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `not_advanced`
- `visual_master_locked`: `not_advanced`

## 下一个目标

V003 进入 72h / 7d 继续观察；下一轮目标是补齐 72h / 7d、3s 留存、主页访问、私信和有效咨询字段，再做正式发布后复盘。
