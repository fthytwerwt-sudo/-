# V003 缺失与待人工确认字段

## 缺失字段 missing

| field | status | reason |
| --- | --- | --- |
| 3s_retention | missing | 截图未直接显示 |
| profile_visit_count | missing | 截图未直接显示 |
| dm_count | missing | 截图未提供私信数据 |
| effective_dm_count | missing | 截图未提供有效私信数据 |
| effective_consult_count | missing | 截图未提供有效咨询数据 |
| clear_need_customer_count | missing | 截图未提供客户线索 |
| effective_comment_quality | missing | comment_count = 0，无评论质量样本 |
| exact_72h_final_at_exact_72h | not_applicable | 本轮截图晚于 72h，只能写 captured_late_after_72h |
| 7d_final_data | missing | 当前不是 7d 封账 |

## 待人工确认 uncertain_need_human_check

| field | status | reason |
| --- | --- | --- |
| exact_observation_window_from_platform | uncertain_need_human_check | 只能根据截图文件时间推断约 87 小时 42-44 分，平台页面未显示完整窗口标签 |
| exact_72h_capture_not_available | uncertain_need_human_check | 本轮不是精确 72h 截止点 |
| age_distribution_estimated_from_bar_chart | uncertain_need_human_check | 年龄分布来自柱状图估读，不是平台导出精确数 |
| gender_distribution_partial_visible_only | uncertain_need_human_check | 性别区域截图不完整 |
| trend_curve_point_values | uncertain_need_human_check | 曲线只能辅助判断，不录入精确点位 |
| partial_region_list_visible_only | uncertain_need_human_check | 本轮只记录地域表可见项，不补全未显示省份 |
| interest_distribution_estimated_from_chart | uncertain_need_human_check | 受众兴趣分布为图表估读 |
| whether_platform_will_update_again_before_7d_final | uncertain_need_human_check | 本轮不是 7d final |

## 最新补充窗口 latest post 72h window

- latest_snapshot_label：`post_72h_pre_7d_snapshot`
- review_window：`post_72h_pre_7d`
- capture_time_if_known：2026-05-17 20:32-20:34 左右
- inferred_hours_after_publish：约 87 小时 42-44 分
- source_status：archived_source_screenshot + user_chatgpt_visual_read_cross_check
- not_final：不是精确 72h final，不是 7d final

## 账号诊断边界 account diagnostic boundary

- account_diagnostic_record：`review_loop/account_diagnostics/20260517_account_diagnostic_snapshot/account_diagnostic_20260510_20260516.json`
- profile_visit_count_visible_in_account_diagnostic_yesterday：1
- boundary：账号诊断主页访问 1 是账号层昨日数据，不等于 V003 单条视频 `profile_visit_count`。

## 不可提前判断

- 不可判断内容最终失败。
- 不可判断方向成立。
- 不可判断市场成立。
- 不可判断需求成立。
- 不可决定下一条正式文案。
- 不可把 `current_data_goal_anchor` 写成 `ready`。
