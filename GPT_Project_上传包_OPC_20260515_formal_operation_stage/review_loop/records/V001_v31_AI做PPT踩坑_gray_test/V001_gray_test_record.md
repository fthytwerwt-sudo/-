# V001 v3.1 历史运营样本记录

## 正式运营记录口径 operation alias

- operation_record_status：historical_operation_record（历史运营样本）
- current_project_stage：formal_operation_active（正式运营中）
- legacy_previous_term：gray_test（历史兼容术语）
- canonical_operation_index：review_loop/operation_records_index.md
- canonical_operation_target：codex_log/current_operation_target.md
- data_completeness：historical_record_data_incomplete（24h / 72h / 7d 核心数据仍待补）
- legacy_record_filename_note：当前目录和文件名仍含 `gray_test`，为避免历史路径断裂，本轮不重命名；内容口径已迁移为正式运营记录。
- what_can_be_concluded：V001 是历史运营样本，旧 gray_test 字段保留为 legacy_previous_term。
- what_cannot_be_concluded：不得写内容通过、方向成立、商业成立；不得用空数据判断短板层或下一轮唯一变量。

## 基础信息

- video_id：V001
- video_version：v3.1
- video_title：我用 AI 做 PPT 踩过的坑
- current_video_baseline：v3.1
- future_iteration_base：v3.1
- legacy_previous_publish_status：gray_test_published（历史兼容字段）
- legacy_previous_gray_test_status：active（历史兼容字段）
- legacy_previous_phase：post_publish_gray_test（历史兼容字段）
- legacy_previous_content_validation：gray_testing_not_final_passed（历史兼容字段，不等于内容最终通过）
- publish_date：2026-05-02
- publish_platform：待用户回填
- publish_time：待用户回填
- video_url：待用户回填
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

- platform_metrics：
- audience_retention：
- interaction：
- account_growth：
- comments：
- dm：
- consult：
- other：

### 核心字段

- 24h_play_count：
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

### 识别状态

- extracted_fields：
- missing_fields：
- uncertain_fields：

### 24h 初检备注

-

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
