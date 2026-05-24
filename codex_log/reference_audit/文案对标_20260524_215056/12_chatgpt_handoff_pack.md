# 12 ChatGPT Handoff Pack｜给 ChatGPT 的接力包

## reference_summary（一句话参考总结）

这条 reference 最值得学的是：用“具体问题卡 + 三层对比 + 真实页面/表格高亮 + 人话判断卡”把复杂 AI 能力讲成观众马上能理解的动作。

## most_valuable_reference_points（最有价值参考点）

- 开头先抓情绪，但很快落到具体问题。
- 中段不只说 AI 强，而是把资料页、表格、模式差异可视化。
- 高光句绑定字段和页面，不靠空泛口播。
- 判断卡负责把复杂材料翻译成一句人话。
- 结尾回到普通用户能做什么，而不是炫技术。

## copywriting_patterns_to_use（可用文案模式）

- “别先问 AI 最终答案，先让它把复查项列出来。”
- “同样是看商品卡，手动翻、AI 初筛、人工复查看到的是三层东西。”
- “我不是让它替我选爆品，我是让它先把不该漏的字段列齐。”

## opening_patterns_to_use（可用开头模式）

- 反差钩子：`你以为选品是在找能卖的品，其实第一步是先排除不能复查的卡。`
- 动作钩子：`我让 Codex 先替我翻一轮商品卡，最后只留下几个要人工核的。`
- 边界钩子：`这不是自动赚钱，这是把乱刷商品卡变成一张复查表。`

## motion_patterns_to_use（可用动态模式）

- 快速预览结果表，再回到操作过程。
- 商品卡字段局部放大，字段出现时配高亮。
- 三列对比卡：手动翻卡 / Codex 初筛 / 人工复查。
- 聊天框结论出现时，用结果卡压缩理由、风险和下一步。

## sfx_patterns_to_use（可用音效模式）

- 搜索输入：轻 typing/click。
- 商品卡被选中：soft pop。
- 表格生成 / 云盘文件出现：restrained ding。
- 聊天框结论出现：轻 settle sound。
- 全部必须自制或授权，不使用 reference 原音频。

## judgment_card_patterns_to_use（可用判断卡模式）

- `问题一：商品卡先看哪几个字段？`
- `判断：AI 只做初筛，不做最终上架决定。`
- `结果：留下 4 个复查对象，而不是 20 个泛泛方向。`
- `边界：表格不是商业验证，只是下一步核验清单。`

## visual_style_tokens（画面风格词）

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

## editing_rhythm_to_use（剪辑节奏）

开头 0-8 秒快，8-25 秒快速预览结果；中段每个关键字段放慢；表格出现至少留 2-3 秒阅读窗口；结尾用低压行动卡收束。

## how_to_apply_to_new_fourth_episode（如何用于新第四期）

| new_fourth_episode_part | reference_rule_to_apply | suggested_visual_motion | suggested_sfx | suggested_card_type | script_density | material_dependency | risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| opening | TR001 + TR002 | 大字问题卡 + 快速预览候选表/聊天框 | soft hit | opening problem card | smooth + sharp hook | 需要商品卡/候选表预览 | 避免爆品承诺 |
| Codex_operating_computer | TR003 | 屏幕录制中显示Codex整理字段 | typing/click | mode comparison card | material_granularity | Codex操作电脑真实画面 | 命令行/隐私遮挡 |
| product_card_browsing | TR004 | 商品卡字段局部放大 | soft click | field highlight overlay | material_granularity | 价格/佣金/销量/评分/风险字段 | 小字不可读 |
| candidate_table | TR005 | 候选表整屏 + 行列高亮 | restrained ding | result card | detail-heavy | 云盘/表格画面 | 不能新增素材里没有的数值 |
| cloud_drive_table | TR005 | 文件出现后切表格局部 | soft settle | info card | medium detail | 云盘文件和表格可读 | 路径/账号隐私 |
| chatbox_result | TR006 | 聊天框结论 + 判断卡 | low pop | judgment/result card | judgment boundary | 聊天框输出理由/风险/下一步 | AI结论需人工复核 |
| boundary_statement | TR008 | 黑底边界卡 | none or quiet hit | boundary card | clear boundary | 仓库状态边界 | 不能写内容通过 |
| ending_action | TR008 | 下一步核验清单 | light close | action card | low-pressure CTA | 四个商品卡复查项 | 不要强卖/引导私信 |

## do_not_copy（禁止照搬）

不要照搬原文案、人物、平台界面、BGM、音效、字体、卡片皮肤、第三方文档、互动数据或“专家模式”产品包装。只继承机制。

## next_chatgpt_action（下一步 ChatGPT 应该做什么）

ChatGPT 下一步应基于本 reference pack 和新第四期素材，重写“新第四期素材锁定版长文案”，并输出：口播、素材时间码、画面颗粒度、动态 / 音效 / 判断卡建议、边界检查。
