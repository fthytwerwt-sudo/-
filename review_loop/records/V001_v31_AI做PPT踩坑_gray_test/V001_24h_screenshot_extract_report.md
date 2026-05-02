# 截图提取报告

适用对象：V001 24h。

## 基础信息

- video_id：V001
- time_window：24h
- screenshot_batch_id：V001_24h_20260502_2224_user_marked_24h
- processed_at：2026-05-02 22:33:49 CST
- processed_by：Codex
- source_note：3 张原始截图均已从用户提供的本地路径归档；字段按 `extracted_from_screenshot` 记录。
- boundary_note：本轮只做 24h 初检数据录入，不做最终内容判断。

## 收到截图

| screenshot_path | data_type | readable | notes |
| --- | --- | --- | --- |
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | platform_metrics | true | 总览 / 播放 / 互动 / 粉丝数据截图；同时提供部分 `interaction` 与 `account_growth` 字段。 |
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | audience_retention | true | 留存 / 完播 / 平均播放 / 来源占比截图；播放量未超过 200，留存趋势图未展示有效数据。 |
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | account_growth | true | 观众数据 / 涨粉 / 脱粉 / 不感兴趣截图。 |

## 已提取字段

| field | value | source_screenshot | extraction_status | notes |
| --- | --- | --- | --- | --- |
| publish_platform | 抖音 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 页面为抖音创作者数据。 |
| publish_date | 2026-05-01 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 截图显示发布时间 `2026年05月01日 23:24`。 |
| publish_time | 23:24 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 同上。 |
| published_video_title | vibcoding 2 天做完视频工作流，我一个纯编程小白，真的都去学起来 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 平台展示标题；V001 内部标题仍为《我用 AI 做 PPT 踩过的坑》。 |
| video_duration | 00:02:30 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 截图封面角标。 |
| 24h_play_count | 19 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 24h 初检播放量。 |
| like_count | 0 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 互动数据。 |
| comment_count | 0 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 互动数据。 |
| share_count | 0 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 互动数据。 |
| favorite_count | 0 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 互动数据。 |
| danmaku_count | 0 | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 互动数据。 |
| completion_rate | 0.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 总览与留存图均显示 0.00%。 |
| 5s_completion_rate | 15.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 不等于 `5s_retention`。 |
| average_watch_time | 5 秒 | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 留存 / 完播数据。 |
| average_watch_ratio | 3.43% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 留存 / 完播数据。 |
| 2s_bounce_rate | 70.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 总览与留存图均显示 70.00%。 |
| like_rate | 0.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 互动数据。 |
| comment_rate | 0.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 互动数据。 |
| share_rate | 0.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 互动数据。 |
| favorite_rate | 0.00% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | 互动数据。 |
| not_interested_count | 0 | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 观众数据。 |
| not_interested_rate | 0.00% | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 观众数据。 |
| recommendation_feed_source_rate | 84.2% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | traffic_source_distribution。 |
| profile_page_source_rate | 10.5% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | traffic_source_distribution。 |
| friend_page_source_rate | 5.3% | `audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | extracted_from_screenshot | traffic_source_distribution。 |
| new_follow_count | 0 | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 账号增长。 |
| new_follow_rate | 0.00% | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 账号增长。 |
| unfollow_count | 0 | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 账号增长。 |
| unfollow_rate | 0.00% | `account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | extracted_from_screenshot | 账号增长。 |
| fan_play_ratio | 5.3% | `platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | extracted_from_screenshot | 粉丝播放占比。 |

## 缺失字段

- `video_url`：missing（截图未提供）
- `3s_retention`：missing（截图未提供）
- `5s_retention`：missing（截图未提供；截图提供的是 5s 完播率，不等于 5 秒留存）
- `profile_visit_count`：missing（截图未提供）
- `dm_count`：missing（截图未提供）
- `effective_dm_count`：missing（截图未提供）
- `effective_consult_count`：missing（截图未提供）
- `real_question_comment_count`：missing（评论截图未提供，评论量为 0）
- `main_drop_off_point`：missing（播放量未超过 200，留存趋势图未展示有效数据）

## 不确定字段

- `screenshot_capture_time`：uncertain_need_human_check（本地附件文件名显示 2026-05-02 22:24 左右，但不能仅凭附件名写死）
- `exact_24h_window`：uncertain_need_human_check（用户标记为 24h，本轮按 24h 初检录入；是否严格满 24 小时待人工确认）

## 给 ChatGPT 的复盘输入

- 24h 初检可用数据已写入 `V001_chatgpt_review_input.md`。
- 本轮只提供数据输入和缺失项，不提前下 7d 结论。
- 需要 ChatGPT / 用户基于后续 72h / 7d 数据继续判断四个复盘问题。

## 本次不做的事

- 不做最终内容判断
- 不写下一条文案
- 不把灰度测试写成内容通过
