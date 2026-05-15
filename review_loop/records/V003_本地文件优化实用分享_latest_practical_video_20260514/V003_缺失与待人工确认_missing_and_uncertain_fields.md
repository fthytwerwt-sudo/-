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
| 72h_final_data | missing | 当前不是完整 72h 复检 |
| 7d_final_data | missing | 当前不是 7d 封账 |

## 待人工确认 uncertain_need_human_check

| field | status | reason |
| --- | --- | --- |
| exact_observation_window_from_platform | uncertain_need_human_check | 只能根据截图文件时间推断约 37 小时，平台页面未显示完整窗口标签 |
| age_distribution_estimated_from_bar_chart | uncertain_need_human_check | 年龄分布来自柱状图估读，不是平台导出精确数 |
| trend_curve_point_values | uncertain_need_human_check | 曲线只能辅助判断，不录入精确点位 |

## 不可提前判断

- 不可判断内容最终失败。
- 不可判断方向成立。
- 不可判断市场成立。
- 不可判断需求成立。
- 不可决定下一条正式文案。
- 不可把 `current_data_goal_anchor` 写成 `ready`。
