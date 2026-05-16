# 最新文案迭代报告

## 当前结论
- 当前文案版本：`V003_copy_v1 / v1_raw`
- 当前数据窗口：`interim_65h_snapshot`
- 当前问题层级：`opening_packaging`
- 置信度：`low`
- 本轮只允许改：`opening_0_3s + bridge_3_8s`
- 当前不允许：全文重写、换选题方向、换目标人群、生成正式下一条视频执行 prompt。

## 保留项
- 核心观点：目标不是 KPI 表，而是下一步动作判断系统。
- 播放是入口，收藏是认可，私信要评分。
- 每条只改一个主变量。

## 禁止项
- `target_user`
- `topic_direction`
- `offer`
- `whole_script_rewrite`
- `formal_next_video_execution_prompt`

## 什么时候继续调文案
补齐 72h / 7d 或下一轮同类样本后，若 2s/3s/5s 仍弱，继续调 opening_packaging 和 bridge_3_8s。

## 什么时候调选题方向
只有多个正常分发样本在开头、结构、语气测试后仍收藏/评论/需求信号持续弱，才进入 topic_angle 判断。

## 什么时候允许打新人群
必须 7-10 个正常样本经过开头、结构、语气测试仍失败后，才允许讨论 target_audience 变化。

## ChatGPT 下一步读取
- `review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md`

## 状态边界
- content_validation_advanced: `false`
- send_ready_advanced: `false`
- current_data_goal_anchor_ready: `false`
- next_formal_video_execution_prompt_generated: `false`
- target_audience_changed: `false`
- topic_direction_changed: `false`
