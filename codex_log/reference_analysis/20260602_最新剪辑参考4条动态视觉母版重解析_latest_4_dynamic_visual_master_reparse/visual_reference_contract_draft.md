# Visual Reference Contract Draft

## reference_anchor

- `reference_id = latest_4_dynamic_visual_master_reparse_20260602`
- `reference_type = dynamic_visual_master + editing_reference + evidence_window_reference + typography_highlight_reference`
- `source_layer = user_provided_local_source_videos`
- `exact_reference_available = true`
- `source_dir = /Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考`
- `primary_reference_video = reference_03 + reference_04`
- `support_reference_video = reference_01 + reference_02`

## effect_targets

- `viewer_first_impression`: 第一眼知道有人在带着看一个 AI 工具/机制/证据，不是随手拼屏。
- `information_hierarchy`: 主持人或标题先定题，证据窗口承载证明，高亮/badge 指读哪里，字幕解释语义。
- `visual_weight`: 证据窗口 > 主持人 reset > 高亮/badge > 字幕 > 装饰。
- `pacing`: 高密证据段必须与低密 reset 交替。
- `evidence_clarity`: 文档、手机、聊天、网页等证据必须有可读裁切或高亮读线。

## function_fields

| field | value |
| --- | --- |
| `input_signal` | 用户要求重解析最新四条剪辑参考的视频源 |
| `evidence_role` | 动态视觉母版，不是正式项目机制 |
| `importance_type` | `must_preserve_visual_language / must_not_copy_assets` |
| `target_area` | composition, typography, subtitle, highlight, motion, transition, density, attention path |
| `selected_action` | 生成动态视觉时间线、视觉地图、偏离检查模板和迁移说明 |
| `validation_rule` | 每条 reference 必须回指源视频、frame/contact sheet/dynamic clip 证据 |
| `blocked_if` | 只写机制名、无关键帧、无第一眼描述、复制平台 UI 或第三方资产、推进状态 |

## must_preserve

- 黑底/深灰舞台承载证据窗口。
- 主持人/标题 reset 与证据窗口交替。
- 证据窗口必须有位置、大小、持续时间、出现/消失方式和遮挡关系。
- 黄/绿高亮必须绑定真实证据位置。
- 分屏只在关系成立时使用。

## can_vary

- 颜色皮肤、字体、角色、项目品牌、横屏布局、证据素材、卡片形态。

## must_not_copy

- 真人脸、平台 UI、互动栏、头像、logo、第三方视频/图片、原 app UI、原字幕/标题文案、平台水印或商业标识。

## done_when

- 4 条源视频技术探针通过。
- 每条有动态视觉时间线。
- 组合地图、角色分类、偏离检查模板、迁移说明完成。
- 不修改新第四期、不推进正式状态。
