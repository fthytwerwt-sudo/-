# V002《自动流的最简单流程》发布后复盘记录

## 正式运营记录口径 operation alias

- operation_record_status：policy_limited_abnormal_operation_sample（平台审核减推异常运营样本）
- current_project_stage：formal_operation_active（正式运营中）
- legacy_previous_term：gray_test / post_publish_review（历史兼容术语）
- canonical_operation_index：review_loop/operation_records_index.md
- canonical_operation_target：codex_log/current_operation_target.md
- data_completeness：abnormal_sample_partial_data_recorded（异常样本部分数据已记录）
- what_can_be_concluded：V002 是正式运营记录中的异常样本，可用于平台风险与小样本兴趣信号参考。
- what_cannot_be_concluded：不得写成正常自然流量样本，不得与 V003 合并，不得写成内容失败或内容通过。

## 基础信息

- 视频编号：V002
- 视频版本：policy_notice_record_20260505（2026-05-05 平台审核通知记录）
- 当前基线：not_v31_baseline（不是 V001 / v3.1 主基线）
- 发布日期：2026-05-04
- 发布平台：抖音
- 发布时间：2026-05-04 17:00:08
- 视频标题：自动流的最简单流程
- 视频链接：missing_user_not_provided（用户未提供）
- 本期测试假设：待验证
- 本轮唯一测试假设：待验证
- 发布状态：published_then_policy_distribution_limited（已发布后被平台审核减推）
- 灰度测试状态：not_normal_gray_test_sample（不是正常灰度测试样本）
- 当前阶段：post_publish_policy_notice_record（发布后平台审核通知记录）

## 审核状态

- notice_type（通知类型）：作品审核通知
- review_result（审核结果）：减少作品推荐
- violation_reason（违规原因）：引导至风险不可控渠道
- reason_surface（触发位置）：画面
- distribution_status（分发状态）：policy_distribution_limited（平台审核减推 / 分发受限）
- abnormal_sample_status（异常样本状态）：abnormal_distribution_sample（异常分发样本）
- sample_interpretation_label（样本解释标签）：policy_limited_but_interest_signal_strong（平台减推污染样本，但兴趣信号强）
- policy_risk_bucket（政策风险桶）：external_channel_or_third_party_software_risk（外部渠道 / 第三方软件风险）
- ai_label_status（AI 标识状态）：extracted_from_screenshot（截图可见“作者声明：内容由 AI 生成”）
- appeal_entry（申诉入口）：截图可见“查看申诉”

## 执行前变量

- 主场景：AI 项目讲解 / AI 方法分享（待 ChatGPT 最终归类）
- 主结构：待验证
- 开头钩子类型：待验证
- 表现形式：屏幕录制 / 工具界面展示（基于截图可见画面字段记录）
- 时长区间：missing_user_not_provided（用户未提供）
- 结尾动作类型：missing_user_not_provided（用户未提供）
- 本条唯一改动变量：not_applicable（本轮只记录，不生成新视频）

## 用户确认数据

| metric（指标） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| play_count（播放量） | 39 | user_provided |
| like_count（点赞数） | 5 | user_provided |
| favorite_count（收藏数） | 8 | user_provided |

## 计算数据

| metric（指标） | formula（公式） | value（值） | source_status（来源状态） |
| --- | --- | --- | --- |
| like_rate（点赞率） | 5 / 39 | 12.82% | calculated_from_fields |
| favorite_rate（收藏率） | 8 / 39 | 20.51% | calculated_from_fields |
| like_plus_favorite_action_rate（点赞 + 收藏动作率，非去重） | 13 / 39 | 33.33% | calculated_from_fields |

## 结果字段

- 24h 数据状态：uncertain_need_human_check（时间窗未由截图原图确认）
- 72h 数据状态：uncertain_need_human_check（时间窗未由截图原图确认）
- 7 天数据状态：not_applicable_yet（尚未到 7d 封账）
- 播放量：39
- 24h 播放量：uncertain_need_human_check（不把用户补充数据硬归入 24h）
- 72h 播放量：uncertain_need_human_check（不把用户补充数据硬归入 72h）
- 7 天播放量：not_applicable_yet（尚未到 7d 封账）
- 是否达到 6000 播放基础门槛：not_applicable_policy_limited_sample（平台减推污染样本，不作为正常自然流量判断）
- 完播率：missing_user_not_provided
- 收藏率：20.51%
- 前 3 秒留存（可选）：missing_user_not_provided
- 平均观看时长（可选）：missing_user_not_provided
- 点赞率（可选）：12.82%
- 评论数（可选）：missing_user_not_provided
- 转粉数（可选）：missing_user_not_provided
- 私信 / 咨询数（可选）：missing_user_not_provided
- 中段主要流失点（可选）：missing_user_not_provided

## 样本与观察状态

- 样本状态：排除样本 / 可参考异常样本之间待 ChatGPT 最终归类；Codex 当前记录为 `abnormal_distribution_sample（异常分发样本）`。
- 是否异常样本：是
- 异常类型：平台异常限流 / 异常压制 / policy_distribution_limited
- 24h 初检结论：待验证；当前不作为正常自然流量样本。
- 72h 复检结论：待验证；当前不作为正常自然流量样本。

## 诊断字段

- 最主要现象描述：平台已发布后判定“减少作品推荐”，风险桶为“引导至风险不可控渠道”，触发位置为“画面”。
- 最可能问题层：发布包装 / 风险表达 / 画面表现层（待验证）
- 次可能问题层：平台规则理解 / 第三方工具呈现方式（待验证）
- 优先排查变量：画面中第三方工具界面、自动化生产流、命令行、项目结构、工具名称是否被平台理解为引导下载 / 使用第三方软件。
- 当前判断状态：部分成立

## 样本解释

- `已确认` 该视频处于 `policy_distribution_limited（平台审核减推 / 分发受限）` 状态，因此播放量不能作为正常自然流量样本判断。
- `已确认` 39 播放样本太小，不能沉淀为稳定规律。
- `部分成立` 点赞率 12.82%、收藏率 20.51%，属于 `high_intent_small_sample_signal（小样本高兴趣信号）`。
- `部分成立` 收藏数高于点赞数，初步说明该内容具有 `utility_value_signal（工具价值 / 可复用价值信号）`。
- `已确认` 本记录不得写成“内容失败”。
- `已确认` 本记录不得写成“自然流量差”。
- `已确认` 本记录标记为 `policy_limited_but_interest_signal_strong（平台减推污染样本，但兴趣信号强）`。

## 下一轮唯一最优先改点

- 下一条只改这一个变量：待 ChatGPT / 用户最终判断；Codex 初检建议优先看“发布包装 / 风险表达 / 画面触发点”。
- 下一轮只改一个变量：待验证
- 其余变量保持不变：待验证
- 下一条测试假设：降低平台误判为外部渠道 / 第三方软件引导的画面表达后，再观察同类内容是否能进入正常分发样本。

## 禁止误读

- 不把本条数据混入 V001 灰度测试记录。
- 不把 39 播放当作正常自然流量样本。
- 不把这条写成“内容失败”。
- 不把这条写成“AI 教程违规已确认”。
- 不把这条写成“未标注 AI 导致已确认”。
- 不把高点赞 / 高收藏直接写成内容已通过。
- 不修改 `content_validation（内容验证）`。
- 不修改 `send_ready（可发送状态）`。
