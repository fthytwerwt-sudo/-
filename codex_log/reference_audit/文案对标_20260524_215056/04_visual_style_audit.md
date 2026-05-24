# 04 Visual Style Audit｜画面风格解析

## visual_style_tokens

```json
{
  "style_name": "竖屏平台录屏 + 主播讲解 + 黑底问题卡 + 文档/表格高亮的 AI 教程风",
  "color_palette": [
    "black/dark platform chrome",
    "white document panels",
    "yellow highlight",
    "green mode tag",
    "purple-pink studio light",
    "white bold title text"
  ],
  "font_behavior": "大标题用超粗白字/黄色重点；正文字幕为底部小黑底白字；表格/文档文字依赖局部放大和高亮。",
  "layout_pattern": "主播脸用于情绪和判断；屏幕录制/文档卡用于证明；问题卡分段；三模式卡作比较。",
  "card_pattern": "黑底问题卡、三列模式卡、左侧模式标签、结果/表格卡。",
  "highlight_pattern": "黄色荧光标注、红/橙小标题、绿色模式标签、局部放大。",
  "motion_pattern": "快速切入 -> 资料页持屏 -> 高亮/滚动 -> 主播回脸总结。",
  "forbidden_to_copy": [
    "creator face/avatar/account",
    "Douyin UI chrome",
    "third-party documents/screens",
    "original card skin",
    "BGM/SFX/fonts/logos"
  ],
  "safe_to_inherit": [
    "problem-card function",
    "three-layer comparison",
    "field highlight",
    "table-result proof",
    "host-to-screen rhythm",
    "boundary card role"
  ]
}
```

## detailed audit

- 画幅比例：竖屏手机录屏，`1180x2556`，内含平台 UI。新第四期正式运营默认是横屏 16:9，因此只能迁移机制，不能迁移画幅。
- 构图：上方手机状态栏/搜索框，中央为 reference 视频，右侧平台互动按钮，底部为作者/标题/评论入口。
- 主体比例：主持人镜头约占内容主体的 40-60%；屏幕/文档/表格证明镜头约占 40-60%。
- 背景色：平台黑/深灰；主持人背景紫粉灯效；文档区白底。
- 字体层级：巨大标题字负责开头停留；问题卡大字负责分段；文档高亮负责证明；底部字幕负责口播跟随。
- 字幕位置：主视频字幕在内容区底部，平台评论输入区另有 UI；新第四期需避免字幕压住表格/商品卡字段。
- 判断卡：黑底大字 + 黄色/白色关键词，通常先出问题再给证据。
- 信息卡：三模式卡、表格卡、文档高亮卡；信息密度较高，需要局部放大。
- 结果卡：表格/资料输出承担结果，不靠口播空说。
- 边界卡：通过“不是所有资料都看”“不只是程序员专属”等句子把能力边界讲清。
- 高光方式：大字、黄色标注、绿色标签、局部框选、表格行高亮、主持人回脸总结。

## transfer to video factory

- 可迁移：黑底问题卡的分段功能、三层对比、字段高亮、表格作为结果证明、主持人/聊天框结论承担判断。
- 不可迁移：竖屏平台 UI、第三方人物、账号、原始 BGM/SFX、原始字体/卡片皮肤、第三方文档/表格内容。
