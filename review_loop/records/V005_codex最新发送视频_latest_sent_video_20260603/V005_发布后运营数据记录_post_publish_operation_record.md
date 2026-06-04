# V005《codex》发布后运营数据记录

## 正式运营记录口径 operation alias

- `video_id`: `V005`
- `operation_record_status`: `latest_operation_sample_between_24h_and_72h_recorded`
- `current_project_stage`: `formal_operation_active（正式运营中）`
- `publish_platform`: 抖音
- `publish_time_visible`: `2026-06-03 04:14`
- `publish_time_source_status`: `extracted_from_screenshot`
- `work_status`: 作品状态正常
- `video_duration_visible`: `00:03:23`
- `review_window`: `between_24h_and_72h`
- `snapshot_label`: `between_24h_and_72h_snapshot`
- `capture_time_from_uploaded_filenames`: `2026-06-04 22:27-22:29`
- `inferred_hours_after_publish`: `约 42 小时 13-15 分`
- `structured_snapshot_path`: `review_loop/records/V005_codex最新发送视频_latest_sent_video_20260603/V005_between_24h_and_72h_snapshot.json`
- `screenshot_manifest_path`: `review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/V005_截图清单_screenshot_manifest.md`
- `screenshot_archive_status`: `archived_to_repo`
- `source_status`: `screenshot_archived_to_repo_and_codex_visual_read`
- `human_review_required`: true

## 样本身份

`已确认` 用户本轮明确要求回填 `latest_sent_video（最新发送 / 最新发布的视频）`，且本轮截图显示发布时间为 `2026-06-03 04:14`、时长 `00:03:23`，不同于 V004 的 `2026-05-17 04:08` / `02:26`。

`已确认` 本轮未将数据写入 V003 或 V004；V003 / V004 只用于查询已有编号、避免重复建档和确认下一个可用编号。

`部分成立` 页面标题区可见 `codex`，封面文字可见 `还是不赚钱`；当前主标题按 `codex` 记录，但标题 / 封面文字关系需要用户或 ChatGPT 人审确认。

`待验证` 本轮截图为约 42 小时数据，不是 24h final、72h final 或 7d final；不得用于最终复盘结论。

## 截图归档

| screenshot_type | archive_path | source_status |
| --- | --- | --- |
| platform_metrics | `review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/between_24h_and_72h_snapshot/platform_metrics/V005_between_24h_and_72h_snapshot_platform_metrics_20260604_222701.png` | archived_to_repo |
| traffic_source | `review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/between_24h_and_72h_snapshot/traffic_source/V005_between_24h_and_72h_snapshot_traffic_source_20260604_222803.png` | archived_to_repo |
| audience_profile | `review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/between_24h_and_72h_snapshot/audience_profile/V005_between_24h_and_72h_snapshot_audience_profile_20260604_222911.png` | archived_to_repo |
| comments | `review_loop/screenshots/V005_codex最新发送视频_latest_sent_video_20260603/between_24h_and_72h_snapshot/comments/V005_between_24h_and_72h_snapshot_comment_hot_words_20260604_222931.png` | archived_to_repo |

## between_24h_and_72h_snapshot 核心数据

| metric（指标） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| play_count（播放量） | 1514 | extracted_from_screenshot |
| average_watch_time（平均播放时长） | 8秒 | extracted_from_screenshot |
| average_play_ratio（平均播放占比） | 4.01% | extracted_from_screenshot |
| completion_rate（完播率） | 0.62% | extracted_from_screenshot |
| two_second_bounce_rate（2s 跳出率） | 54.68% | extracted_from_screenshot |
| five_second_completion_rate（5s 完播率） | 22.45% | extracted_from_screenshot |
| cover_click_rate（封面点击率） | 7.14% | extracted_from_screenshot |
| like_count（点赞量） | 50 | extracted_from_screenshot |
| like_rate（点赞率） | 3.30% | extracted_from_screenshot |
| favorite_count（收藏量） | 12 | extracted_from_screenshot |
| favorite_rate（收藏率） | 0.79% | extracted_from_screenshot |
| comment_count（评论量） | 1 | extracted_from_screenshot |
| comment_rate（评论率） | 0.07% | extracted_from_screenshot |
| share_count（分享量） | 2 | extracted_from_screenshot |
| share_rate（分享率） | 0.13% | extracted_from_screenshot |
| danmu_count（弹幕量） | 0 | extracted_from_screenshot |
| not_interested_rate（不感兴趣率） | 0.00% | extracted_from_screenshot |
| new_follow_count（涨粉量） | 0 | extracted_from_screenshot |
| unfollow_count（脱粉量） | 0 | extracted_from_screenshot |
| fan_play_ratio（粉丝播放占比） | 0.1% | extracted_from_screenshot |
| recommendation_page（推荐页来源占比） | 96.1% | extracted_from_screenshot |
| profile_page（个人主页来源占比） | 2.2% | extracted_from_screenshot |
| search_page（搜索来源占比） | 1.2% | extracted_from_screenshot |
| message_page（消息页来源占比） | 0.1% | extracted_from_screenshot |
| other_page（其他来源占比） | 0.4% | extracted_from_screenshot |

## 观众数据

- `gender_distribution`: 男性 97%，女性 3%（extracted_from_screenshot）
- `age_distribution`: 柱状图可见，但无精确数值标签，标记 `uncertain_need_human_check`
- `region_distribution`: 可见部分行包括广东 14.12%、贵州 0.69%、甘肃 0.54%、海南 0.23%、香港 0.23%、台湾 0.15%、青海 0.15%；完整地区分布标记 `uncertain_need_human_check`
- `interest_distribution`: 汽车 / 随拍 / 时尚 / 电影 / 二次元均为 20.00%（extracted_from_screenshot）
- `active_distribution`: 低活 0%、轻度 2%、中度 9%、重度 83%、未知 6%（extracted_from_screenshot）
- `comment_hot_words`: 你说 / 赚钱 / 运气（extracted_from_screenshot）

## 当前可判断

- `已确认` V005 已建立为最新发送视频的独立运营记录。
- `已确认` 本轮截图显示作品状态正常。
- `已确认` 本轮截图为 `between_24h_and_72h_snapshot`，只能作为约 42 小时运营数据记录。
- `部分成立` 推荐页来源占比 96.1%，说明该截图窗口内主要流量来自推荐页；不能写成平台已充分验证。

## 当前不能判断

- 不能判断内容通过。
- 不能判断商业验证成立。
- 不能判断方向成立或方向失败。
- 不能把 1514 播放写成项目成功。
- 不能把 12 收藏写成内容通过。
- 不能把当前约 42 小时截图写成 24h final、72h final 或 7d final。
- 不能生成下一条正式视频执行 prompt。
- 不能推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 缺失字段

- `24h_final_data`
- `72h_final_data`
- `7d_final_data`
- `three_second_retention`
- `friend_page`
- `profile_visit_count`
- `dm_count`
- `effective_dm_count`
- `effective_consult_count`
- `clear_need_customer_count`
- `comment_body_or_comment_quality`
- `paid_or_commercial_signal`
- `full_region_distribution`
- `exact_age_distribution_values`
- `platform_capture_time_explicit_on_page`

## 不确定字段

- `video_title_codex_vs_thumbnail_text_still_not_making_money`
- `exact_review_window_from_platform_page`
- `age_distribution_exact_values`
- `region_distribution_complete_rows`
- `whether_platform_will_continue_distribution_before_72h`
- `whether_V005_should_replace_V003_or_V004_as_current_operation_target_requires_human_confirmation`

## 下一步

等待用户 / ChatGPT 确认标题与封面文字关系，并补后续 72h / 7d 数据、3s 留存、主页访问、私信、有效私信、有效咨询和清晰需求客户字段；本轮不进入最终复盘结论。
