# V003 运营决策结果

## 1. 样本身份
- `current_operation_target（当前运营目标）`
- 当前最新数据窗口：`post_72h_pre_7d_snapshot（72h 后 / 7d 前补录，非 7d final）`。

## 2. 当前可用信号
- 播放量 143，仍是极小样本。
- 2s 跳出率 48.81%，5s 完播率 28.57%，完播率 4.05%。
- 收藏率 2.10%，只能记为小正信号，不能写方向成立。
- 评论、分享、私信、有效咨询侧仍没有可判断证据。

## 3. 当前短板草稿
- `opening_retention_and_initial_distribution_weak`
- 置信度：`low / draft_low_confidence`

## 4. 下一期正式执行判断
- can_enter_next_episode_execution: `false`
- blocked_reason: V003 仍是 post_72h_pre_7d_snapshot，缺 3s_retention、7d_final_data、clear_need_customer_count、dm_count、effective_consult_count、effective_dm_count、profile_visit_count，不能生成正式下一条视频执行 prompt。

## 5. 缺失数据
- `3s_retention`
- `7d_final_data`
- `clear_need_customer_count`
- `dm_count`
- `effective_consult_count`
- `effective_dm_count`
- `profile_visit_count`

## 6. 允许准备 / 不允许动作
- 允许：准备开头路线、前 5 秒包装、证据压缩的低置信度候选假设。
- 不允许：生成正式下一条视频执行 prompt，不允许进入新视频制作，不允许把 V003 写 ready。
