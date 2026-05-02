# V001 缺失字段记录

## 24h 缺失字段

| field | status | reason | next_required_input |
| --- | --- | --- | --- |
| video_url | missing | 24h 截图未提供视频链接。 | 用户补充抖音视频链接或后续截图含链接入口。 |
| 3s_retention | missing | 截图未提供 3 秒留存。 | 后续平台若展示留存数据，补对应截图。 |
| 5s_retention | missing | 截图提供的是 `5s_completion_rate = 15.00%`，不等于 5 秒留存。 | 后续平台若展示 5 秒留存，补对应截图。 |
| profile_visit_count | missing | 截图未提供主页访问数。 | 后续补主页访问 / 账号增长相关截图。 |
| dm_count | missing | 截图未提供私信数。 | 后续补私信数据截图。 |
| effective_dm_count | missing | 截图未提供有效私信，且不能由私信数硬推。 | 用户 / ChatGPT 后续按私信内容人工标记。 |
| effective_consult_count | missing | 截图未提供有效咨询，且不能由私信数硬推。 | 用户 / ChatGPT 后续按咨询内容人工标记。 |
| real_question_comment_count | missing | 截图未提供评论内容，评论量为 0。 | 后续如有评论截图再人工判断。 |
| main_drop_off_point | missing | 播放量未超过 200，留存趋势图未展示有效数据。 | 播放量超过平台阈值后补留存趋势截图。 |

## 72h 缺失字段

- 待 72h 复检截图回填，本轮不写入 72h 数据。

## 7d 缺失字段

- 待 7d 封账截图回填，本轮不写入 7d 数据。

## 待人工确认字段

| field | status | reason |
| --- | --- | --- |
| screenshot_capture_time | uncertain_need_human_check | 本地附件文件名显示 2026-05-02 22:24 左右，但仓库不能仅凭附件名写死截图时间。 |
| exact_24h_window | uncertain_need_human_check | 用户标记为 24h，本轮按 24h 初检录入；是否严格满 24 小时待人工确认。 |

## 备注

截图未提供或识别不清时，必须记录在这里，不得硬猜。
