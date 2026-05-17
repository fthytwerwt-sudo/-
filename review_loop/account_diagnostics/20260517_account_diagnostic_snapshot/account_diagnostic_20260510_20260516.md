# 账号诊断快照 account diagnostic snapshot

## 1. 基础信息

- record_type：account_diagnostic_snapshot（账号诊断快照）
- record_scope：account_level_only（仅账号层）
- stats_period：2026-05-10 至 2026-05-16
- capture_time_if_known：2026-05-17 20:34:56
- source_screenshot：`review_loop/account_diagnostics/20260517_account_diagnostic_snapshot/account_diagnostic_20260510_20260516_short_video_20260517_203456.png`
- source_status：archived_source_screenshot

## 2. 账号诊断可见字段

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| post_count | 2 | extracted_from_screenshot | high |
| video_play_count | 170 | extracted_from_screenshot | high |
| completion_rate | 4.84% | extracted_from_screenshot | high |
| interaction_index | 5.29% | extracted_from_screenshot | high |
| net_follower_gain | 1 | extracted_from_screenshot | high |

## 3. 同类作者对比

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| active_percentile | 高于 81.00% 的同类创作者 | extracted_from_screenshot | high |
| play_percentile | 高于 83.62% 的同类创作者 | extracted_from_screenshot | high |
| completion_rate_relative | 低于 93.64% 的同类创作者 | extracted_from_screenshot | high |
| interaction_percentile | 高于 63.16% 的同类创作者 | extracted_from_screenshot | high |
| follower_gain_percentile | 高于 62.00% 的同类创作者 | extracted_from_screenshot | high |

## 4. 昨日数据 2026-05-16

| metric | value | source_status | confidence |
| --- | --- | --- | --- |
| play_count | 19 | extracted_from_screenshot | high |
| profile_visit_count | 1 | extracted_from_screenshot | high |
| work_like_count | 1 | extracted_from_screenshot | high |
| share_count | 0 | extracted_from_screenshot | high |
| comment_count | 0 | extracted_from_screenshot | high |
| cover_click_rate | - | extracted_from_screenshot | high |
| net_follower_gain | 0 | extracted_from_screenshot | high |
| unfollow_count | 0 | extracted_from_screenshot | high |
| total_followers | 4 | extracted_from_screenshot | high |

## 5. 边界

- 账号诊断只用于账号层观察。
- 账号诊断不等于 V003 单条视频主页访问。
- 昨日 `profile_visit_count = 1` 不得写入 V003 单条视频 `profile_visit_count`。
- 账号诊断不等于 V003 私信、有效私信、有效咨询或清晰需求客户字段。
- 账号诊断不直接推进商业验证、内容验证、`send_ready` 或下一条正式视频执行。
