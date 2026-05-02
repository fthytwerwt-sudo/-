# V001 v3.1 灰度测试记录

## 基础信息

- video_id：V001
- video_slug：v31_AI做PPT踩坑
- video_version：v3.1
- video_title：我用 AI 做 PPT 踩过的坑
- published_video_title：vibcoding 2 天做完视频工作流，我一个纯编程小白，真的都去学起来
- current_video_baseline：v3.1
- future_iteration_base：v3.1
- technical_validation：passed（技术验证通过；不等于内容通过）
- technical_upgrade_next：true
- publish_status：gray_test_published（已发片，灰度测试中）
- gray_test_status：active（灰度测试中）
- current_phase：post_publish_gray_test（发布后灰度测试阶段）
- content_validation：gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）
- send_ready：false
- visual_master_locked：false
- publish_platform：抖音
- publish_date：2026-05-01
- publish_time：23:24
- video_duration：00:02:30
- video_url：missing（截图未提供）
- screenshot_capture_time：uncertain_need_human_check（附件文件名显示 2026-05-02 22:24 左右，但不作为仓库确定截图时间）
- exact_24h_window：uncertain_need_human_check（用户标记为 24h，本轮按 24h 初检录入）
- current_review_pack：dist/latest_review_pack/
- current_round：20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix
- gray_test_metrics_v1：review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md
- screenshot_intake_rules：review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md
- screenshot_root：review_loop/screenshots/V001_v31_AI做PPT踩坑/

## 本期测试假设

真实 AI 使用经验 + 结果差 + 工作提效实录，能否让观众看懂“先定义交付，再让 AI 生成”的价值。

## 执行前变量

- 主场景：AI 案例拆解
- 主结构：旧方式 → 新方式
- 表现形式：用户录制素材 + 少量 PPT / 信息卡 + 可爱提示卡 + 骚萌反应卡
- 时长区间：约 150 秒
- 结尾动作类型：低压收束 / Prompt 引用尾卡
- 本轮唯一测试假设：v3.1 当前成片整体表现能否进入有效灰度观察
- 本条唯一改动变量：v3.1 当前成片整体表现

## 24h 初检数据

### 截图证据

- platform_metrics：`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png`
- audience_retention：`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png`
- interaction：`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png`；`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png`
- account_growth：`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png`；`review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png`
- comments：missing（截图未提供）
- dm：missing（截图未提供）
- consult：missing（截图未提供）
- other：无

### 核心字段

- 24h_play_count：19（extracted_from_screenshot）
- 3s_retention：missing（截图未提供）
- 5s_retention：missing（截图未提供；截图提供的是 5s_completion_rate，不等于 5s_retention）
- completion_rate：0.00%（extracted_from_screenshot）
- 5s_completion_rate：15.00%（extracted_from_screenshot）
- average_watch_time：5 秒（extracted_from_screenshot）
- average_watch_ratio：3.43%（extracted_from_screenshot）
- 2s_bounce_rate：70.00%（extracted_from_screenshot）
- like_count：0（extracted_from_screenshot）
- like_rate：0.00%（extracted_from_screenshot）
- comment_count：0（extracted_from_screenshot）
- comment_rate：0.00%（extracted_from_screenshot）
- share_count：0（extracted_from_screenshot）
- share_rate：0.00%（extracted_from_screenshot）
- favorite_count：0（extracted_from_screenshot）
- favorite_rate：0.00%（extracted_from_screenshot）
- danmaku_count：0（extracted_from_screenshot）
- not_interested_count：0（extracted_from_screenshot）
- not_interested_rate：0.00%（extracted_from_screenshot）
- recommendation_feed_source_rate：84.2%（extracted_from_screenshot）
- profile_page_source_rate：10.5%（extracted_from_screenshot）
- friend_page_source_rate：5.3%（extracted_from_screenshot）
- traffic_source_distribution：推荐页 84.2%；个人主页 10.5%；朋友页 5.3%（extracted_from_screenshot）
- profile_visit_count：missing（截图未提供）
- new_follow_count：0（extracted_from_screenshot）
- new_follow_rate：0.00%（extracted_from_screenshot）
- unfollow_count：0（extracted_from_screenshot）
- unfollow_rate：0.00%（extracted_from_screenshot）
- fan_play_ratio：5.3%（extracted_from_screenshot）
- dm_count：missing（截图未提供）
- effective_dm_count：missing（截图未提供）
- effective_consult_count：missing（截图未提供）
- real_question_comment_count：missing（截图未提供）
- main_drop_off_point：missing（播放量未超过 200，留存趋势图未展示有效数据）

### 识别状态

- extracted_fields：publish_platform、publish_date、publish_time、published_video_title、video_duration、24h_play_count、like_count、comment_count、share_count、favorite_count、danmaku_count、completion_rate、5s_completion_rate、average_watch_time、average_watch_ratio、2s_bounce_rate、like_rate、comment_rate、share_rate、favorite_rate、not_interested_count、not_interested_rate、recommendation_feed_source_rate、profile_page_source_rate、friend_page_source_rate、new_follow_count、new_follow_rate、unfollow_count、unfollow_rate、fan_play_ratio
- missing_fields：video_url、3s_retention、5s_retention、profile_visit_count、dm_count、effective_dm_count、effective_consult_count、real_question_comment_count、main_drop_off_point
- uncertain_fields：screenshot_capture_time、exact_24h_window

### 24h 初检备注

- 本轮只做 24h 截图数据录入和初检输入；不写新文案、不生成视频、不生成音频、不重新装配全片、不修改 v3.1 视频产物。
- 播放量未超过 200，留存趋势图提示“播放量超过 200 后，展示数据”，因此 `main_drop_off_point` 记录为 missing。
- `content_validation` 保持 `gray_testing_not_final_passed`；`send_ready` 保持 `false`；灰度测试不等于内容最终通过。

## 72h 复检数据

### 截图证据

- platform_metrics：
- audience_retention：
- interaction：
- account_growth：
- comments：
- dm：
- consult：
- other：

### 核心字段

- 72h_play_count：
- play_growth_continues：
- 3s_retention：
- completion_rate：
- average_watch_time：
- favorite_count：
- favorite_rate：
- profile_visit_count：
- new_follow_count：
- dm_count：
- effective_dm_count：
- effective_consult_count：
- real_question_comment_count：
- main_drop_off_point：

### 识别状态

- extracted_fields：
- missing_fields：
- uncertain_fields：

### 72h 复检备注

-

## 7d 封账数据

### 截图证据

- platform_metrics：
- audience_retention：
- interaction：
- account_growth：
- comments：
- dm：
- consult：
- other：

### 核心字段

- 7d_play_count：
- reached_6000_play_threshold：
- completion_rate：
- average_watch_time：
- favorite_rate：
- like_rate：
- comment_rate：
- profile_visit_count：
- new_follow_count：
- dm_count：
- effective_dm_count：
- effective_consult_count：
- followable_customer_count：
- appointment_count：
- deal_count：
- top_3_feedback：

### 识别状态

- extracted_fields：
- missing_fields：
- uncertain_fields：

### 7d 封账备注

-

## 样本与观察状态

- 样本状态：待判断
- 是否异常样本：待判断
- 异常类型：待回填
- 当前判断状态：待验证

## 四个复盘问题

1. 这条有没有达到 6000 播放基础门槛？
2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
3. 下一轮只改哪一个变量？
4. 为什么先改它，改完看哪个指标？

## 下一轮只改一个变量

- next_single_variable：
- why_this_variable：
- keep_unchanged：
- done_when：
- validation_metrics：

## 当前边界

- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `technical_upgrade_next = true`
- `PR7_B_骚萌反应页.png` 是后续骚萌卡唯一执行参考
- PR #7 A 只作为历史 / candidate 对照

## 当前禁止判断

- 不得写成内容通过。
- 不得写成已验证成功。
- 不得写成账号方向已验证。
- 不得写成市场成立。
- 不得写成规律成立。
- 不得跳过截图 / 数据直接设定下一条文案。
