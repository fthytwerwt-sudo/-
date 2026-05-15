# Current Gray Test Target

## 当前对象

- `已确认` 本轮发生“最新一期视频切换”：当前灰度观察对象从 V001 切换到 V003。
- `已确认` 当前视频编号：`V003`
- `已确认` 当前视频标题：`以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件`
- `已确认` 当前视频记录：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md`
- `已确认` 当前截图证据目录：`review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/`
- `已确认` 截图清单：`review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md`
- `已确认` 发布时间截图可见：`2026-05-14 04:50`
- `已确认` 视频时长：`04:03`
- `已确认` 发布平台：`抖音`
- `已确认` 当前阶段：`post_publish_gray_test（发布后灰度测试阶段）`
- `已确认` 发布状态：`gray_test_published（已发片，进入灰度测试）`
- `已确认` 灰度状态：`active（灰度测试中）`
- `已确认` 发布后复盘要求：`post_publish_review_required = true`
- `待验证` 当前 V003 只有 `interim_36h_snapshot（约 37 小时早期截图）`，不是完整 72h / 7d 复盘。

## previous / historical

- `previous_current_target`: `V001 v3.1｜我用 AI 做 PPT 踩过的坑`
- `previous_record_path`: `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- `previous_status`: `historical_previous_gray_target`
- `note`: V001 保留为历史灰度目标，不被本轮截图覆盖。
- `existing_v002_status`: `V002 已存在，为《自动流的最简单流程》平台审核减推异常样本，不是本轮截图对应视频，不被本轮复用或覆盖。`

## 当前目标

当前 V003 灰度测试目标：

1. 记录 `between_24h_and_72h / interim_36h_snapshot` 早期数据。
2. 等待 72h / 7d 后补齐核心字段。
3. 不把 141 播放写成最终失败。
4. 不把收藏率 2.13% 写成方向成立。
5. 不直接决定下一条正式文案。
6. 用 72h / 7d 数据回答四个复盘问题后，再判断下一轮唯一变量。

这套指标体系不是运营数据大表，而是下一轮改动定位器。

当前复盘仍只回答 4 个问题，但本轮只能做早期草稿判断：

1. 这条有没有达到 6000 播放基础门槛？`待 7d 数据`
2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？`draft_low_confidence`
3. 下一轮只改哪一个变量？`draft_low_confidence，不进入正式执行`
4. 为什么先改它，改完看哪个指标？`待 72h / 7d 补足`

## 观察窗口

- `interim_36h_snapshot（约 37 小时早期截图）`：已录入。
- `72h 复检`：等待用户回填发布后 72h 数据。
- `7 天复盘`：等待用户回填发布后 7 天数据，用于判断 6000 播放基础门槛。

本轮截图来源文件名 / 文件修改时间约为 `2026-05-15 18:19-18:21`，距离 `2026-05-14 04:50` 发布约 37 小时；因此只能标注 `between_24h_and_72h / interim_36h_snapshot`，不得写成完整 72h 复检或 7d 封账。

## 数据统计频率

### 最低统计

每条视频最低统计两次：

1. 24h / early 初检
2. 72h 复检

### 标准统计

建议每条视频统计三次：

1. 24h / early 初检
2. 72h 复检
3. 7d 封账

### 分工

- 用户：提供截图。
- Codex：按视频 / 时间窗 / 数据类型归档截图，提取字段，更新记录。
- DeepSeek：只读供料与风险复核，不写文件，不拍板项目事实。
- ChatGPT：根据四个复盘问题做最终判断。

### 截图归档原则

- 不同视频分开。
- 24h / 72h / 7d 分开。
- 平台数据 / 评论 / 私信 / 咨询分开。
- 截图不清楚就标记 `uncertain_need_human_check`，不硬猜。
- 截图未出现字段写 `missing`。

## 当前早期可见数据摘要

```yaml
review_window: "between_24h_and_72h / interim_36h_snapshot"
data_confidence: "low"
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
share_count: 0
danmu_count: 0
new_follow_count: 1
fan_play_ratio: "4.3%"
traffic_sources:
  recommendation_page: "97.2%"
  profile_page: "1.4%"
  friend_page: "1.4%"
```

## 基础测试流量门槛

- `7d_play_count（7 天播放量）`
  - 达标：`>= 6000`
  - 部分达标：`3000-5999`
  - 未达标：`< 3000`
- `24h_play_count（24 小时播放量）`
  - 达标：`>= 1200`
  - 部分达标：`600-1199`
  - 未达标：`< 600`
- `72h_play_count（72 小时播放量）`
  - 达标：`>= 3500`
  - 部分达标：`1800-3499`
  - 未达标：`< 1800`

以上阈值是小样本阶段初始建议值，不是行业标准，后续会随样本校准。V003 当前不是 72h / 7d 封账，不能按最终失败裁决。

## 优先观察指标

### 核心必填字段

- `24h_play_count（24 小时播放量）`：已用 `interim_36h_snapshot` 早期播放量临时记录为 `141`，需 72h / 7d 补足。
- `72h_play_count（72 小时播放量）`：`missing`
- `7d_play_count（7 天播放量）`：`missing`
- `3s_retention（3 秒留存）`：`missing`
- `completion_rate（完播率）`：`4.17%`
- `average_watch_time（平均观看时长）`：`21秒`
- `favorite_count（收藏数）`：`3`
- `favorite_rate（收藏率）`：`2.13%`
- `profile_visit_count（主页访问数）`：`missing`
- `new_follow_count（新增关注数）`：`1`
- `dm_count（私信数）`：`missing`
- `effective_dm_count（有效私信数）`：`missing`
- `effective_consult_count（有效咨询数）`：`missing`

### 辅助观察字段

- `5s_completion_rate（5 秒完播率）`：`28.13%`
- `two_second_bounce_rate（2 秒跳出率）`：`50.00%`
- `main_drop_off_point（中段主要流失点）`：`uncertain_need_human_check`
- `like_count（点赞数）`：`2`
- `like_rate（点赞率）`：`1.42%`
- `comment_count（评论数）`：`0`
- `comment_rate（评论率）`：`0.00%`
- `share_count（转发数）`：`0`
- `share_rate（转发率）`：`0.00%`
- `profile_visit_rate（主页访问率）`：`missing`
- `play_to_follow_rate（播放转粉率）`：`0.71%`（截图可见口径，待平台字段名人工确认）
- `profile_to_follow_rate（主页访问转粉率）`：`missing`
- `real_question_comment_count（评论中的真实问题数）`：`missing`
- `next_topic_clues（后续选题线索）`：`missing`

### 商业线索出现时才填

- `clear_need_customer_count（有明确需求的客户数）`：`missing`
- `followable_customer_count（可跟进客户数）`：`missing`
- `appointment_count（预约数）`：`missing`
- `deal_count（成交数）`：`missing`
- `customer_problem_types（客户问题类型）`：`missing`
- `budget_or_payment_intent（预算 / 付费意愿）`：`missing`
- `valid_lead_notes（有效线索摘录）`：`missing`
- `invalid_lead_notes（无效线索摘录）`：`missing`

## 诊断层

- `traffic_layer`: `draft_low_confidence / weak`
- `opening_retention`: `draft_low_confidence / weak`
- `content_value_signal`: `draft_low_confidence / small_positive_signal`
- `interaction_signal`: `draft_low_confidence / weak`
- `lead_signal`: `missing`
- `preliminary_main_bottleneck`: `opening_retention_and_initial_distribution_weak / draft_low_confidence`
- `candidate_primary_variable`: `opening_route_or_first_5s_packaging / draft_low_confidence`

上述仅为早期数据摘要，不是最终内容复盘。

## 当前执行机制

- 截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 当前视频记录目录：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/`
- 当前单条主记录：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md`
- 当前结构化快照：`review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_早期数据快照_early_interim_snapshot.json`
- 截图证据目录：`review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/`
- 截图清单：`review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md`
- 灰度测试指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`

## 当前禁止判断

- 不得写成内容通过。
- 不得写成账号方向已验证。
- 不得写成市场成立。
- 不得写成规律成立。
- 不得跳过数据直接设定下一条文案。
- 不得把已发片写成最终成功。
- 不得把灰度测试写成验证成功。
- 不得把 V003 的 141 播放写成最终失败。
- 不得把收藏率 2.13% 写成方向成立。

## 当前保持状态

- `content_validation = gray_testing_not_final_passed / not_advanced_this_round`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `technical_upgrade_next = true`

## 下一步

1. 等待用户提交 V003 的 72h 数据截图。
2. 等待用户提交 V003 的 7d 数据截图。
3. Codex 继续按视频 / 时间窗 / 数据类型归档并提取字段。
4. 72h / 7d 数据补齐后，再由 ChatGPT / 用户按四个复盘问题做正式判断。
