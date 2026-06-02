# Typography Subtitle Highlight Map

## typography

- 大标题：短词、粗体、高对比，常见白字 + 黄绿/紫粉关键词。它用于开头或章节，不承担长解释。
- 结构卡：黄底黑字或绿底黑字，单屏少词，位置靠近对应概念/步骤。
- 证据页：原 UI 小字不可靠，必须用外层高亮、裁切或重新排版让关键句可读。

## subtitle

- 源视频字幕属于平台壳低区，和画内证据天然分离。
- 横屏迁移必须建立 `subtitle_safe_zone`，字幕不得压住白页证据、黄线高亮、按钮、表格、手机框底部。
- 字幕是语义节奏，不是视觉主角；主视觉仍应由证据窗口 / 主持人 / 标题卡承担。

## highlight

| highlight type | source references | use | warning |
| --- | --- | --- | --- |
| `yellow_reading_line` | `reference_03`, `reference_04` | 长文本、文档、聊天页证据读线 | 只可贴真实证据，不可作装饰 |
| `green_keyword_badge` | `reference_02`, `reference_03` | 标功能词、结果词、步骤词 | 不要每个词都贴，必须绑定目标 |
| `large_title_emphasis` | all | 开头钩子、章节重置 | 不要让大标题代替证据 |
| `corner_label` | `reference_01` | 对比格、结果窗口标注 | 无比较关系时不要硬做 |
