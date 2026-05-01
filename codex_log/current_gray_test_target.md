# Current Gray Test Target

## 当前对象

- `已确认` 当前主题：`我用 AI 做 PPT 踩过的坑`
- `已确认` 当前视频版本：`v3.1`
- `已确认` 当前视频基线：`v3.1`
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于：`v3.1`
- `已确认` 当前阶段：`post_publish_gray_test（发布后灰度测试阶段）`
- `已确认` 发布状态：`gray_test_published（已发片，进入灰度测试）`
- `已确认` 灰度状态：`active（灰度测试中）`
- `已确认` 发布后复盘要求：`post_publish_review_required = true`

## 当前目标

当前 v3.1 灰度测试目标：

7 天播放量达到 6000 左右；
同时用留存、完播、收藏、涨粉、私信、有效咨询判断下一轮只改一个变量。

这套指标体系不是运营数据大表，而是下一轮改动定位器。

当前复盘只回答 4 个问题：

1. 这条有没有达到 6000 播放基础门槛？
2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
3. 下一轮只改哪一个变量？
4. 为什么先改它，改完看哪个指标？

原 24h / 72h 观察仍保留；7 天数据用于判断是否达到 6000 基础测试流量门槛。

## 观察窗口

- `24h 初检`：等待用户回填发布后 24h 数据。
- `72h 复检`：等待用户回填发布后 72h 数据。
- `7 天复盘`：等待用户回填发布后 7 天数据，用于判断 6000 播放基础门槛。

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

以上阈值是小样本阶段初始建议值，不是行业标准，后续会随样本校准。

## 优先观察指标

### 核心必填字段

- `24h_play_count（24 小时播放量）`
- `72h_play_count（72 小时播放量）`
- `7d_play_count（7 天播放量）`
- `3s_retention（3 秒留存）`
- `completion_rate（完播率）`
- `average_watch_time（平均观看时长）`
- `favorite_count（收藏数）`
- `favorite_rate（收藏率）`
- `profile_visit_count（主页访问数）`
- `new_follow_count（新增关注数）`
- `dm_count（私信数）`
- `effective_dm_count（有效私信数）`
- `effective_consult_count（有效咨询数）`

### 辅助观察字段

- `5s_retention（5 秒留存）`
- `main_drop_off_point（中段主要流失点）`
- `like_count（点赞数）`
- `like_rate（点赞率）`
- `comment_count（评论数）`
- `comment_rate（评论率）`
- `share_count（转发数）`
- `share_rate（转发率）`
- `profile_visit_rate（主页访问率）`
- `play_to_follow_rate（播放转粉率）`
- `profile_to_follow_rate（主页访问转粉率）`
- `real_question_comment_count（评论中的真实问题数）`
- `next_topic_clues（后续选题线索）`

### 商业线索出现时才填

- `clear_need_customer_count（有明确需求的客户数）`
- `followable_customer_count（可跟进客户数）`
- `appointment_count（预约数）`
- `deal_count（成交数）`
- `customer_problem_types（客户问题类型）`
- `budget_or_payment_intent（预算 / 付费意愿）`
- `valid_lead_notes（有效线索摘录）`
- `invalid_lead_notes（无效线索摘录）`

## 诊断层

- 流量层
- 内容层
- 账号增长层
- 私域 / 客户转化层
- 必要时再回看：场景层、结构层、心理机制层、画面表现层、字幕与配音节奏层

## 当前执行机制

- 单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- 单条模板：`review_loop/02_video_record_template.md`
- 灰度测试指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- 结果看板模板：`review_loop/03_result_dashboard_template.md`
- 诊断模板：`review_loop/04_diagnosis_template.md`
- Codex 初检 / ChatGPT 判断交接：`review_loop/05_dual_review_handoff_template.md`
- 下一轮只改一个变量：`review_loop/06_next_round_task_template.md`

## 当前禁止判断

- 不得写成内容通过。
- 不得写成账号方向已验证。
- 不得写成市场成立。
- 不得写成规律成立。
- 不得跳过数据直接设定下一条文案。
- 不得把已发片写成最终成功。
- 不得把灰度测试写成验证成功。

## 当前保持状态

- `content_validation = gray_testing_not_final_passed`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `technical_upgrade_next = true`

## reference 边界

- `已确认` PR #7 B 是后续骚萌卡唯一执行参考。
- `已确认` PR #7 A 只能作为历史 / candidate 对照。
- `已确认` 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。

## 下一步

1. 等待用户补充发布平台、发布时间、视频链接。
2. 等待用户回填 24h / 72h / 7 天数据。
3. 24h 数据回填后，Codex 按 `review_loop/04_diagnosis_template.md` 做初检。
4. 72h 数据回填后，Codex 复检播放增长、留存、完播、收藏、涨粉和私信 / 咨询变化。
5. 7 天数据回填后，按四个复盘问题收口；ChatGPT / 用户基于初检判断主要问题层和下一轮唯一改点，不提前写成规律成立。
