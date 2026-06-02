# Migration Notes For New Fourth Episode Dynamic Visual Only

status_boundary:
- `not_video_task = true`
- `new_fourth_episode_modified = false`
- `candidate_generated = false`
- `content_validation = not_applicable`
- `send_ready = false`

## current_round_scope

本轮只完成动态视觉母版重解析，不回炉新第四期，不改任何新第四期素材、剪辑、声音、字幕、review_pack 或 `dist/latest_review_pack/`。

## future_migration_priority

1. `primary`: 用 `reference_03` 处理“教学/流程/工具机制怎么讲清楚”。
2. `primary`: 用 `reference_04` 处理“长文本/聊天/文档证据怎么被高亮带读”。
3. `support`: 用 `reference_01` 处理“结果差/能力样例/比较板/章节 reset”。
4. `support`: 用 `reference_02` 处理“手机框和绿色关键词包装”，不要把它当整片主视觉。

## future_execution_notes

- 新第四期若继续使用用户录屏/文档/表格证据，应优先迁移 ref03/ref04 的证据窗口和高亮读线，而不是复制竖屏平台壳。
- 若句组没有 before/after、source/output、reference/result 关系，不应强行使用 ref01 多窗口分屏。
- 若需要手机框，只作为局部证据容器，不能让手机框小到看不清。
- 字幕必须与证据窗口分离；动态高亮不能被字幕覆盖。
- 所有角色、图标、标签、品牌和背景必须重做为《视频工厂》原创视觉语言。

## blocked_if_future_video_task

- 缺 locked copy contract。
- 缺 line_group 级 script_to_timeline_map。
- 缺 evidence window plan。
- 缺 subtitle_card_overlap_check。
- 缺 side-by-side deviation check。
- 试图复制平台 UI / 真人 / logo / 第三方样例。
