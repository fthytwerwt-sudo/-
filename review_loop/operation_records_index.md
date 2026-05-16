# 正式运营记录索引 operation_records_index

## 1. 文件定位

本文件是《视频工厂》正式运营阶段的内容数据记录索引。

从 2026-05-15 起，三期内容数据统一纳入：

- `operation_records（运营记录）`
- `operation_data_intake（运营数据录入）`
- `operation_review（运营复盘）`
- `operation_next_variable_decision（运营下一变量判断）`

旧 `gray_test（灰度测试）` 只作为历史术语、历史路径或 legacy alias 保留，不再作为当前默认项目阶段。

## 2. records_inventory

| video_id | title | record_path | current_status | data_completeness |
| --- | --- | --- | --- | --- |
| V001 | 我用 AI 做 PPT 踩过的坑 | `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md` | `historical_operation_record` | 24h / 72h / 7d 核心数据仍多为空；作为历史运营样本保留 |
| V002 | 自动流的最简单流程 | `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_发布后复盘记录_post_publish_review_record.md` | `policy_limited_abnormal_operation_sample` | 有播放 39、点赞 5、收藏 8 和平台减推通知；不是正常自然分发样本 |
| V003 | 以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件 | `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md` | `current_operation_target` | 已录入约 37 小时和约 65 小时中间数据；72h / 7d 未完成 |

## 3. per_record_boundary

### V001

- `operation_record_status`: `historical_operation_record`
- `what_can_be_concluded`: V001 是历史运营样本；旧灰度记录路径继续作为历史证据。
- `what_cannot_be_concluded`: 不能写内容通过、方向成立、商业成立；不能用空数据判断短板层。
- `next_required_data`: 如需复盘 V001，仍需补 24h / 72h / 7d 核心字段。

### V002

- `operation_record_status`: `policy_limited_abnormal_operation_sample`
- `what_can_be_concluded`: 已确认平台审核减推；点赞 / 收藏信号只能作为异常样本中的小样本兴趣信号。
- `what_cannot_be_concluded`: 不能作为正常自然流量样本；不能写成内容失败；不能把高收藏写成内容通过。
- `next_required_data`: 如需重测同类选题，应先规避平台风险表达，再观察正常分发样本。

### V003

- `operation_record_status`: `current_operation_target`
- `what_can_be_concluded`: 36h 与 65h 中间数据已录入，当前播放、留存、互动、观众画像均为低置信度运营观察；65h 仍未出现二次增长。
- `what_cannot_be_concluded`: 不能写成 72h / 7d final；不能决定方向失败；不能决定下一条正式文案。
- `next_required_data`: V003 72h / 7d 数据、3s 留存、主页访问、私信、有效私信、有效咨询、清晰需求客户。

## 4. status_boundary

- `formal_operation_active` 只说明项目进入真实发布与数据回流阶段。
- `formal_operation_active` 不等于 `content_validation = passed`。
- `formal_operation_active` 不等于 `send_ready = true`。
- `formal_operation_active` 不等于商业验证成立。
- `formal_operation_active` 不等于数据飞轮已跑通。
- `formal_operation_active` 不等于 multi-agent runtime 长期稳定。
- `current_data_goal_anchor` 仍是 `partial_data_recorded`，不是 `ready`。

## 5. next_target

V003 补齐 72h / 7d 数据后，进入 `operation_review`；复盘只用于判断下一轮唯一运营变量，不直接生成下一条正式视频执行 prompt。
