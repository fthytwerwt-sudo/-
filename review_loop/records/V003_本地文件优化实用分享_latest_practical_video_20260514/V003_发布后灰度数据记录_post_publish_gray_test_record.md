# V003《本地文件优化实用分享》正式运营数据记录

## 正式运营记录口径 operation alias

- operation_record_status：current_operation_target（当前运营目标）
- current_project_stage：formal_operation_active（正式运营中）
- current_operation_mode：data_driven_operation_iteration（数据驱动运营迭代）
- legacy_previous_term：gray_test（历史兼容术语）
- canonical_operation_target：codex_log/current_operation_target.md
- canonical_operation_index：review_loop/operation_records_index.md
- legacy_record_filename_note：当前文件名仍含 `post_publish_gray_test_record`，为避免历史路径断裂，本轮不重命名；内容口径已迁移为正式运营数据记录。
- data_completeness：partial_interim_data_recorded（已新增 `interim_65h_snapshot`，仍非 72h final）
- what_can_be_concluded：V003 是当前运营样本，约 37 小时与约 65 小时两个中间数据窗口已录入。
- what_cannot_be_concluded：不得写成 72h / 7d final，不得判断内容成功、项目失败、商业成立或下一条正式文案。

## 基础信息

- video_id：V003
- video_slug：V003_本地文件优化实用分享_latest_practical_video_20260514
- video_title：以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件
- publish_platform：抖音
- publish_time_visible：2026-05-14 04:50
- video_duration：04:03
- work_status：作品状态正常
- current_phase：formal_operation_active（正式运营中）
- publish_status：published_in_formal_operation（已发布，进入正式运营数据回流；不是发布成功口径升级）
- operation_status：active（正式运营观察中）
- legacy_previous_phase：post_publish_gray_test（历史兼容字段）
- legacy_previous_publish_status：gray_test_published（历史兼容字段）
- legacy_previous_gray_test_status：active（历史兼容字段）
- content_validation：not_advanced（本轮不推进内容验证）
- send_ready：not_advanced（本轮不推进可发送状态）
- screenshot_root：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/
- screenshot_manifest：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md
- structured_snapshot：review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_interim_65h_snapshot.json
- previous_structured_snapshot：review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_早期数据快照_early_interim_snapshot.json
- deepseek_pre_supply：dist/deepseek_runtime_validation/20260515_latest_video_data_intake/pre_supply/latest_supply_pack.md

## 视频身份判断

- current_gray_test_target_before_this_round：V001《我用 AI 做 PPT 踩过的坑》
- existing_video_ids_checked：V001、V002
- V001_title_match_result：not_matched（标题不同）
- V002_title_match_result：not_matched（V002 已存在，为《自动流的最简单流程》平台审核减推异常样本）
- matched_existing_video：false
- new_video_id_created：V003
- identity_confidence：high
- identity_note：本轮是“最新一期视频切换”，不得默认写入旧 V001，也不得复用既有 V002。

## 观察窗口

- capture_time_if_known：latest = 2026-05-16 21:44-21:45 左右；previous = 2026-05-15 18:19-18:21 左右
- publish_time_visible：2026-05-14 04:50
- inferred_hours_after_publish：latest 约 65 小时；previous 约 37 小时
- review_window：between_48h_and_72h
- snapshot_label：interim_65h_snapshot
- previous_snapshot_label：interim_36h_snapshot
- review_window_status：near_72h_pre_final_snapshot_not_72h_final
- rule：不得把本轮截图写成完整 72h 复检或 7d 封账。

## interim_36h_snapshot 数据

### 截图证据

- platform_metrics：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/platform_metrics/V003_interim_36h_总览_overview_20260515_182106.png
- audience_retention：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/audience_retention/V003_interim_36h_流量分析_retention_traffic_20260515_181946.png
- interaction：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/audience_retention/V003_interim_36h_流量分析_retention_traffic_20260515_181946.png
- account_growth：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/platform_metrics/V003_interim_36h_总览_overview_20260515_182106.png
- audience_profile：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_36h_snapshot/audience_profile/V003_interim_36h_观众分析_audience_profile_20260515_182041.png

### 核心字段

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| play_count | 141 | extracted_from_screenshot | high |
| average_watch_time | 21秒 | extracted_from_screenshot | high |
| cover_click_rate | 0.00% | extracted_from_screenshot | high |
| completion_rate | 4.17% | extracted_from_screenshot | high |
| two_second_bounce_rate | 50.00% | extracted_from_screenshot | high |
| average_play_ratio | 8.51% | extracted_from_screenshot | high |
| five_second_completion_rate | 28.13% | extracted_from_screenshot | high |
| like_count | 2 | extracted_from_screenshot | high |
| like_rate | 1.42% | extracted_from_screenshot | high |
| favorite_count | 3 | extracted_from_screenshot | high |
| favorite_rate | 2.13% | extracted_from_screenshot | high |
| comment_count | 0 | extracted_from_screenshot | high |
| comment_rate | 0.00% | extracted_from_screenshot | high |
| share_count | 0 | extracted_from_screenshot | high |
| share_rate | 0.00% | extracted_from_screenshot | high |
| danmu_count | 0 | extracted_from_screenshot | high |
| new_follow_count | 1 | extracted_from_screenshot | high |
| follow_rate_or_fan_rate_visible | 0.71% | extracted_from_screenshot | high |
| fan_play_ratio | 4.3% | extracted_from_screenshot | high |

### 流量来源

| source | value | source_status | confidence |
| --- | --- | --- | --- |
| recommendation_page | 97.2% | extracted_from_screenshot | high |
| profile_page | 1.4% | extracted_from_screenshot | high |
| friend_page | 1.4% | extracted_from_screenshot | high |

### 观众画像

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| gender_male | 77% | extracted_from_screenshot | high |
| gender_female | 23% | extracted_from_screenshot | high |
| age_under_18 | 约2% | extracted_from_screenshot | medium |
| age_18_23 | 约20% | extracted_from_screenshot | medium |
| age_24_30 | 约32% | extracted_from_screenshot | medium |
| age_31_40 | 约34% | extracted_from_screenshot | medium |
| age_41_50 | 约9% | extracted_from_screenshot | medium |
| age_50_plus | 约2% | extracted_from_screenshot | medium |
| region_广东 | 17.27% | extracted_from_screenshot | high |
| region_北京 | 13.64% | extracted_from_screenshot | high |
| region_江苏 | 9.09% | extracted_from_screenshot | high |
| region_湖北 | 5.45% | extracted_from_screenshot | high |
| region_四川 | 5.45% | extracted_from_screenshot | high |
| region_河北 | 4.55% | extracted_from_screenshot | high |
| region_河南 | 4.55% | extracted_from_screenshot | high |
| region_上海 | 4.55% | extracted_from_screenshot | high |
| active_heavy | 72% | extracted_from_screenshot | high |
| active_medium | 18% | extracted_from_screenshot | high |
| active_light | 6% | extracted_from_screenshot | high |
| active_unknown | 4% | extracted_from_screenshot | high |

## interim_65h_snapshot 数据

### 截图证据

- platform_metrics：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/platform_metrics/V003_interim_65h_总览_overview_20260516_214439.png
- audience_retention：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/audience_retention/V003_interim_65h_流量分析_retention_traffic_20260516_214508.png
- interaction：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/audience_retention/V003_interim_65h_流量分析_retention_traffic_20260516_214508.png
- account_growth：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/platform_metrics/V003_interim_65h_总览_overview_20260516_214439.png
- audience_profile：review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/interim_65h_snapshot/audience_profile/V003_interim_65h_观众分析_audience_profile_20260516_214548.png

### 时间窗

- capture_time_if_known：2026-05-16 21:44-21:45 左右
- inferred_hours_after_publish：约 65 小时
- review_window：between_48h_and_72h
- snapshot_label：interim_65h_snapshot
- snapshot_alias：near_72h_pre_final_snapshot
- review_window_status：not_72h_final_data / not_7d_final_data

### 核心字段

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| play_count | 141 | extracted_from_screenshot | high |
| average_watch_time | 21秒 | extracted_from_screenshot | high |
| cover_click_rate | 0.00% | extracted_from_screenshot | high |
| completion_rate | 4.14% | extracted_from_screenshot | high |
| two_second_bounce_rate | 49.69% | extracted_from_screenshot | high |
| average_play_ratio | 8.46% | extracted_from_screenshot | high |
| five_second_completion_rate | 27.95% | extracted_from_screenshot | high |
| like_count | 2 | extracted_from_screenshot | high |
| like_rate | 1.42% | extracted_from_screenshot | high |
| favorite_count | 3 | extracted_from_screenshot | high |
| favorite_rate | 2.13% | extracted_from_screenshot | high |
| comment_count | 0 | extracted_from_screenshot | high |
| comment_rate | 0.00% | extracted_from_screenshot | high |
| share_count | 0 | extracted_from_screenshot | high |
| share_rate | 0.00% | extracted_from_screenshot | high |
| danmu_count | 0 | extracted_from_screenshot | high |
| not_interested_count | 0 | extracted_from_screenshot | high |
| not_interested_rate | 0.00% | extracted_from_screenshot | high |
| new_follow_count | 1 | extracted_from_screenshot | high |
| follow_rate_or_fan_rate_visible | 0.71% | extracted_from_screenshot | high |
| unfollow_count | 0 | extracted_from_screenshot | high |
| unfollow_rate | 0.00% | extracted_from_screenshot | high |
| fan_play_ratio | 4.3% | extracted_from_screenshot | high |

### 流量来源

| source | value | source_status | confidence |
| --- | --- | --- | --- |
| recommendation_page | 96.6% | extracted_from_screenshot | high |
| profile_page | 2.1% | extracted_from_screenshot | high |
| friend_page | 1.4% | extracted_from_screenshot | high |

### 观众画像

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| gender_male | 约78% | extracted_from_screenshot | high |
| gender_female | 约22% | extracted_from_screenshot | high |
| age_under_18 | 约2% | extracted_from_screenshot | medium |
| age_18_23 | 约19%-20% | extracted_from_screenshot | medium |
| age_24_30 | 约32% | extracted_from_screenshot | medium |
| age_31_40 | 约34%-35% | extracted_from_screenshot | medium |
| age_41_50 | 约9%-10% | extracted_from_screenshot | medium |
| age_50_plus | 约2% | extracted_from_screenshot | medium |
| region_广东 | 15.83% | extracted_from_screenshot | high |
| region_北京 | 15.83% | extracted_from_screenshot | high |
| region_江苏 | 8.33% | extracted_from_screenshot | high |
| region_四川 | 6.67% | extracted_from_screenshot | high |
| region_湖北 | 5.00% | extracted_from_screenshot | high |
| region_上海 | 5.00% | extracted_from_screenshot | high |
| region_河北 | 4.17% | extracted_from_screenshot | high |

### 与 36h 快照的低置信度对比

- play_count：141 -> 141，约 65 小时仍基本未增长。
- average_watch_time：21秒 -> 21秒。
- favorite_count：3 -> 3；收藏率仍为 2.13%，只能保留为小样本价值信号，不能写方向成立。
- new_follow_count：1 -> 1；不得写账号增长成立。
- recommendation_page：97.2% -> 96.6%；profile_page：1.4% -> 2.1%；friend_page：1.4% -> 1.4%。
- preliminary_note：65h 数据仍未出现二次增长，说明前端承接弱 / 分发未扩散的判断更清楚；但本轮仍不是 72h final 或 7d final，不写最终失败。

## 缺失字段

- 3s_retention：missing（截图未提供）
- profile_visit_count：missing（截图未提供）
- dm_count：missing（截图未提供）
- effective_dm_count：missing（截图未提供）
- effective_consult_count：missing（截图未提供）
- clear_need_customer_count：missing（截图未提供）
- effective_comment_quality：missing（comment_count = 0，无评论质量样本）
- 72h_final_data：missing（当前不是完整 72h 复检）
- 7d_final_data：missing（当前不是 7d 封账）

## 待人工确认字段

- exact_observation_window_from_platform：uncertain_need_human_check（平台页面未显示完整窗口标签）
- age_distribution_estimated_from_bar_chart：uncertain_need_human_check（年龄分布来自柱状图估读）
- trend_curve_point_values：uncertain_need_human_check（观看趋势曲线不录入精确点位）

## data_intake_summary

- traffic_layer：draft_low_confidence / weak。播放量 141，仍处于极小样本早期观察，不写最终失败。
- opening_retention：draft_low_confidence / weak。2s 跳出率 50.00%，5s 完播率 28.13%，完播率 4.17%，说明前 5 秒承接可能偏弱。
- content_value_signal：draft_low_confidence / small_positive_signal。收藏率 2.13%，在极小样本下有一点可复用价值信号，但不能放大成方向成立。
- interaction_signal：draft_low_confidence / weak。评论 0、分享 0，未形成公开需求反馈。
- lead_signal：missing。未看到私信、有效私信或有效咨询数据，不得写需求成立。
- traffic_source_note：推荐页 97.2%，说明平台给过初始推荐；但当前数据更像初始承接不足，不是最终方向失败。
- interim_65h_update：约 65 小时播放仍为 141，推荐页来源 96.6%，2s 跳出 49.69%，5s 完播 27.95%；可以更明确记录“未出现二次增长 / 分发未扩散”，但仍不得写项目失败或方向失败。

## not_final_review

- 当前不是最终复盘。
- 当前不是 72h final data。
- 当前不是 7d final data。
- 不决定方向失败。
- 不决定下一条正式执行。
- 不生成正式 Codex 视频执行 prompt。
- 等 72h / 7d 数据后再做正式复盘。

## candidate_next_variable_draft

- value：opening_route_or_first_5s_packaging
- status：draft_low_confidence
- validation_metric：2s bounce, 5s completion, 3s retention if later available, average_watch_time
- forbidden_variables：
  - 不改目标用户
  - 不改核心选题方向
  - 不改承接 / 变现口径
  - 不同时改多个变量

## 禁止误读

- 不得覆盖 V001 数据。
- 不得覆盖或复用 V002 异常样本记录。
- 不得把 141 播放写成最终失败。
- 不得把低播放写成项目失败。
- 不得把收藏率 2.13% 写成方向成立。
- 不得把当前截图写成完整 72h / 7d 复盘。
- 不得直接决定下一条正式文案。
- 不得推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
