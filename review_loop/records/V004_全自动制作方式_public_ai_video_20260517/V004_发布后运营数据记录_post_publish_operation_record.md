# V004《不能做得说很好，但确实方便 如果这条没有人看，我直接公开我全自动的制作方式》发布后运营数据记录

## 正式运营记录口径 operation alias

- `video_id`: `V004`
- `operation_record_status`: `latest_operation_sample_pre_24h`
- `current_project_stage`: `formal_operation_active（正式运营中）`
- `publish_platform`: 抖音
- `publish_time_visible`: `2026-05-17 04:08`
- `work_status`: 作品状态正常
- `video_duration_visible`: `02:26`
- `review_window`: `pre_24h`
- `snapshot_label`: `interim_17h_snapshot`
- `structured_snapshot_path`: `review_loop/records/V004_全自动制作方式_public_ai_video_20260517/V004_interim_17h_snapshot.json`
- structured_snapshot_path: `review_loop/records/V004_全自动制作方式_public_ai_video_20260517/V004_interim_17h_snapshot.json`
- `screenshot_archive_status`: `archived_to_repo`
- `source_status`: `screenshot_archived_to_repo_and_user_provided_visual_read`
- `human_review_required`: true

## 样本身份

`已确认` V004 是最新一期已发布视频的早期运营样本，当前只记录约 17 小时数据。

`部分成立` V004 可作为 `latest_operation_sample_pre_24h（最新运营样本 / 24h 前早期快照）` 进入记录池，但当前不自动替换 V003 的 `current_operation_target（当前运营目标）`。

`待验证` 是否把 V004 切换为新的 `current_operation_target` 需要后续 24h / 72h / 7d 数据和用户 / ChatGPT 人审确认。

## 截图归档

| screenshot_type | archive_path | source_status |
| --- | --- | --- |
| overview | `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_总览_overview_20260517_212049.png` | archived_to_repo |
| retention_traffic | `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_流量分析_retention_traffic_20260517_212140.png` | archived_to_repo |
| audience_profile | `review_loop/screenshots/V004_全自动制作方式_public_ai_video_20260517/interim_17h_snapshot/V004_interim_17h_观众分析_audience_profile_20260517_212204.png` | archived_to_repo |

## interim_17h_snapshot 核心数据

| metric（指标） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| play_count（播放量） | 55 | screenshot_archived_to_repo |
| like_count（点赞量） | 1 | screenshot_archived_to_repo |
| comment_count（评论量） | 0 | screenshot_archived_to_repo |
| share_count（分享量） | 0 | screenshot_archived_to_repo |
| favorite_count（收藏量） | 0 | screenshot_archived_to_repo |
| danmu_count（弹幕量） | 0 | screenshot_archived_to_repo |
| completion_rate（完播率） | 4.76% | screenshot_archived_to_repo |
| two_second_bounce_rate（2s 跳出率） | 41.18% | screenshot_archived_to_repo |
| new_follow_count（涨粉量） | 0 | screenshot_archived_to_repo |
| unfollow_count（脱粉量） | 0 | screenshot_archived_to_repo |
| fan_play_ratio（粉丝播放占比） | 1.8% | screenshot_archived_to_repo |
| average_watch_time（平均播放时长） | 14秒 | screenshot_archived_to_repo |
| five_second_completion_rate（5s 完播率） | 30.88% | screenshot_archived_to_repo |
| average_play_ratio（平均播放占比） | 9.42% | screenshot_archived_to_repo |
| recommendation_page（推荐页来源占比） | 95.2% | screenshot_archived_to_repo |
| profile_page（个人主页来源占比） | 4.8% | screenshot_archived_to_repo |
| like_rate（点赞率） | 1.82% | screenshot_archived_to_repo |
| comment_rate（评论率） | 0.00% | screenshot_archived_to_repo |
| share_rate（分享率） | 0.00% | screenshot_archived_to_repo |
| favorite_rate（收藏率） | 0.00% | screenshot_archived_to_repo |
| not_interested_rate（不感兴趣率） | 0.00% | screenshot_archived_to_repo |

## 观众数据

- audience_growth：暂无有效观众趋势数据
- gender / age / region / interest：当前截图未提供有效可录入数据

## 文案与数据边界

- `V004 actual_metrics.favorite_count = 0`
- `V004 raw_copy_mentions_previous_case_favorite_count = 3`
- 说明：raw copy 中“这条视频虽然播放低，但它还有 3 个收藏”引用的是 V003 复盘案例，不是 V004 自身数据。

## 当前可判断

- `已确认` V004 已发布且作品状态正常。
- `已确认` V004 约 17 小时早期数据已记录，不能写成 24h final、72h final 或 7d final。
- `部分成立` 推荐页来源占比 95.2%，说明平台有早期推荐入口，但不能写成平台已充分验证。
- `部分成立` 2s 跳出 41.18%、5s 完播 30.88%、完播率 4.76% 只能作为早期留存观察，不能单独裁决方向。

## 当前不能判断

- 不能把 55 播放写成方向失败。
- 不能把 0 收藏写成内容无价值已确认。
- 不能把推荐页 95.2% 写成平台已经充分验证。
- 不能生成正式下一条视频执行 prompt。
- 不能推进 `content_validation / send_ready / current_data_goal_anchor ready`。

## 缺失字段

- `24h_final_data`
- `72h_final_data`
- `7d_final_data`
- `3s_retention`
- `profile_visit_count`
- `dm_count`
- `effective_dm_count`
- `effective_consult_count`
- `clear_need_customer_count`
- `gender_distribution`
- `age_distribution`
- `region_distribution`
- `interest_distribution`

## 下一步

等待 V004 24h / 72h / 7d 数据；在用户 / ChatGPT 明确确认前，本记录只作为 `latest_operation_sample_pre_24h`，不自动替换 V003 当前运营目标。
