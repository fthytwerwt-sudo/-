# V002 缺失与待人工确认字段

## 缺失字段

| field（字段） | status（状态） | notes（说明） |
| --- | --- | --- |
| screenshot_original_file（截图原图文件） | missing_user_not_provided | 用户本轮提供了截图字段文字，没有向 Codex 提供原图文件。 |
| screenshot_path（截图路径） | missing_user_not_provided | 不编造截图路径。 |
| video_link（视频链接） | missing_user_not_provided | 用户未提供。 |
| video_duration（视频时长） | missing_user_not_provided | 用户未提供。 |
| completion_rate（完播率） | missing_user_not_provided | 用户未提供。 |
| 3s_retention（3 秒留存） | missing_user_not_provided | 用户未提供。 |
| average_watch_time（平均观看时长） | missing_user_not_provided | 用户未提供。 |
| comment_count（评论数） | missing_user_not_provided | 用户未提供。 |
| share_count（转发数） | missing_user_not_provided | 用户未提供。 |
| profile_visit_count（主页访问数） | missing_user_not_provided | 用户未提供。 |
| new_follow_count（新增关注数） | missing_user_not_provided | 用户未提供。 |
| dm_count（私信数） | missing_user_not_provided | 用户未提供。 |
| effective_consult_count（有效咨询数） | missing_user_not_provided | 用户未提供。 |

## 待人工确认字段

| field（字段） | status（状态） | notes（说明） |
| --- | --- | --- |
| metric_time_window（数据时间窗） | uncertain_need_human_check | 用户提供播放 / 点赞 / 收藏数据，但未明确该数据对应 24h、72h 或其他时间窗；本轮不硬归入 24h / 72h。 |
| exact_trigger_frame（具体触发帧） | uncertain_need_human_check | 平台提示触发位置为“画面”，但具体帧未确认。 |
| sample_classification_final（最终样本分级） | uncertain_need_human_check | Codex 已标记异常分发样本；是否归为排除样本或可参考异常样本，交 ChatGPT / 用户最终判断。 |
| next_single_variable（下一轮唯一改动变量） | uncertain_need_human_check | Codex 初检建议优先看发布包装 / 风险表达 / 画面触发点，仍需 ChatGPT / 用户拍板。 |

