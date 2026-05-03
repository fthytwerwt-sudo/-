# sassy_card_replacement_report

## 执行口径

- `sassy_route_reference_read`：`true`
- `reference_image`：`/Users/fan/Documents/视频工厂/dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png`
- `legacy_pr7_a_used`：`false`
- `route`：`sassy_reaction_card_route`
- `forced_where_not_fit`：`false`
- `same_card_reused_for_all`：`false`

`已确认` 本轮按用户更新后的口径执行：骚萌卡只放在适合“吐槽 / 反转 / 判断”的短情绪点；不适合的位置改用用户录制素材、稳定录屏或 `cute_info_card_route` 信息卡承载，不为了凑骚萌卡硬塞尴尬 punchline。

| 替换原段落 | 新承载 | 卡片类型 | 表情 / 动作 | punchline | 是否继承 PR #7 B | 是否与其他卡不同 | 适配判断 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `seg01` 后段 | 骚萌卡 + 信息卡 | 问题钩子骚萌卡 | 吐槽表情 / 举牌提示 | `一键生成？先别急` | `true` | `true` | 适合承接“一键生成跑偏”的轻吐槽 |
| `seg05` | 骚萌卡 + 信息卡 | 正面反转骚萌卡 | 进入状态 / 指向待办 | `从聊天 变成待办` | `true` | `true` | 适合承接 prompt 变任务列表的转折 |
| `seg14` | 用户录制素材固定窗口 | 不使用骚萌卡 | `not_applicable` | 未硬塞骚萌卡 | `not_used_for_fit` | `not_applicable` | Codex 检查段需要真实证据，骚萌卡会抢主叙事 |

## 差异复核

- `cards_generated`：`3`
- `pairwise_visual_difference_checked`：`true`
- `pairwise_visual_difference_report`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/sassy_card_visual_diff_report.json`
- `visual_verdict`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/sassy_card_visual_verdict.json`
- `contact_sheet`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/sassy_card_contact_sheet.jpg`

`已确认` 三张骚萌卡属于同一角色体系，但不是同一张图复制粘贴。差异报告显示三组 pairwise mean pixel difference 均为 `different = true`；其中 `seg14` 的卡片仅作为复核生成证据，最终段落承载仍按适配度使用用户录制素材固定窗口。
