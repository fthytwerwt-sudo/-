# Side By Side Deviation Check Template

status_boundary:
- `template_only = true`
- `new_fourth_episode_modified = false`
- `content_validation = not_applicable`

## usage

未来只有在用户要求修改/重做新第四期或下一条视频时，才能用本模板对照候选片。当前本轮不对新第四期做修改，也不声称它已符合参考。

| check_id | reference_anchor | expected_dynamic_visual | candidate_frame_path | candidate_observation | deviation_level | repair_if_needed | pass_condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `first_impression` | ref03/ref04 opening | 3 秒内出现主持人/标题/核心对象，第一眼清楚主题 |  |  | `none/minor/major/blocking` | 重做 opening hierarchy | 观众第一眼不先看平台壳或装饰 |
| `evidence_window` | ref03/ref04 middle | 主证据窗口占 55%-70% 横屏宽，有裁切/高亮 |  |  |  | 调整窗口尺寸、位置、裁切 | 关键证据可读 |
| `highlight_binding` | ref03/ref04 yellow/green highlighter | 高亮贴真实证据，不漂浮 |  |  |  | 重新绑定高亮位置 | 高亮能回答“看哪里” |
| `host_reset` | all | 高密证据后有主持人/标题/低密度卡 reset |  |  |  | 插入 reset bridge | 高密段不连续疲劳 |
| `split_relation` | ref01 comparison board | 分屏只用于真实比较关系 |  |  |  | 去掉装饰分屏或补足比较关系 | 分屏左右有语义关系 |
| `subtitle_safe_zone` | all | 字幕不压证据窗口/OCR/高亮 |  |  |  | 重排字幕或证据窗口 | 无 high severity overlap |
| `asset_copy_risk` | all | 无平台 UI/真人/logo/第三方素材复制 |  |  |  | 替换为项目原创资产 | 无侵权/误导性复制 |

## blocking_deviation

- 只有大标题页，没有证据窗口。
- 证据窗口小到不可读。
- 黄/绿标签离目标太远，变成装饰。
- 分屏没有比较关系。
- 字幕、卡片、OCR 三层文字互相遮挡。
- 复制平台 UI、真人、logo 或第三方素材。
