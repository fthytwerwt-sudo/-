# 16 Transcript-driven ChatGPT Handoff Pack｜逐字稿驱动改稿包

## transcript_status_summary（逐字稿状态总结）

- `transcript_status = blocked_local_asr_missing`
- `audio_extract_status = passed`
- `full_transcript_generated = false`
- `full_transcript_committed = false`
- `FULL_TRANSCRIPT_COMMIT_ALLOWED = false`
- local_only_dir: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353`
- reason: 本机无可用本地 ASR / OCR，且任务禁止外部 API；因此不能编造完整逐字稿。

## reference_copy_voice（一句话说明对标视频怎么说话）

它像一个懂技术但会说人话的人：先拿具体痛点抓住你，再用短判断把复杂内容压扁，最后在表格/文档/卡片出现时才讲细节。

## sentence_patterns_to_imitate_mechanically_not_literally（可继承句式机制，不照搬原句）

1. `先给一个普通人能懂的问题，再给工具动作。`
2. `不是 A，而是 B：先纠正误解，再给正确动作。`
3. `同一个问题，拆成三层看：手动 / AI 初筛 / 人工复查。`
4. `结果句必须带可见载体：表格、字段、聊天框、风险列。`
5. `边界句要短：这只是初筛，不是最终验证。`
6. `转场句要轻：别用流程名硬转，用“这时就清楚了”这种人话转。`

## opening_voice_rules（开头话语规则）

- 先抛痛点，不先介绍 Codex。
- 8 秒内必须看到结果预览：候选表 / 云盘表格 / 聊天框结论三选一或组合。
- 开头语言要像：“我不是让 AI 替我选爆品，我是先让它把该核的商品挑出来。”
- 避免“本期我们将演示一个系统化流程”这种报告口吻。

## transition_voice_rules（转场话语规则）

- 每个转场只负责把观众带到下一步，不承担证明。
- 可以用短句：`这一步先别急着下判断。` / `真正有用的是后面这张表。` / `问题到这里才变清楚。`
- 转场后必须有画面证据承接，不能只靠口播推进。

## detail_entry_rules（什么时候进入细节）

- 字段出现时进入细节：商品名、佣金、评分、销量、风险、复查项。
- 表格出现时进入细节：不要说“整理好了”，要说“哪几列变成了可判断的信息”。
- 聊天框结论出现时进入细节：为什么留下、为什么排除、下一步核什么。
- 屏幕没有对应证据时，细节必须降级为顺口过渡或卡片说明。

## judgment_card_voice_rules（判断卡句式规则）

- `问题：这一堆商品先看什么？`
- `判断：AI 只做初筛，不替我拍板。`
- `结果：先留下少数复查对象。`
- `边界：这不是商业验证，只是下一步核验清单。`

## ending_voice_rules（结尾话语规则）

- 低压收尾，不强卖，不承诺爆品。
- 结尾要给下一步动作：复查样品、看价格、看风险词、看平台规则。
- 结尾可以回到聊天框，让 AI 的结论成为“下一步清单”，而不是最终答案。

## new_fourth_rewrite_rules（新第四期重写规则）

```text
new_fourth_copy_rewrite_rules:
  - opening must sound like: 我先把乱翻商品卡这件事，变成一张能复查的表。
  - first 8 seconds must show: 商品卡混乱感 + 候选表/聊天框结论预览。
  - when saying Codex operates computer, must include: 它点开/读取/整理了哪些真实字段，而不是一句“自动操作”。
  - when saying table, must include: 商品名、佣金、风险、下一步复查项至少三类可见字段。
  - when saying suitable product, must include: 适合只是“进入复查”，不是确认能卖。
  - boundary must say: AI 初筛不是最终选品，也不是商业验证；最后还要人工复核样品、价格、规则和风险。
  - avoid: 自动赚钱、爆品保证、一键上架、泛泛说 AI 提效、连续字段堆砌、没有画面证据的判断。
```

## forbidden_copying（禁止照搬）

- 禁止照搬 reference 原句、标题、人物、账号、平台 UI、BGM、音效、字体、卡片皮肤、文档内容和品牌包装。
- 禁止把完整第三方逐字稿提交到 GitHub。
- 禁止把 reference 的“AI 能力承诺”平移到新第四期，必须改成《视频工厂》自己的素材和边界。

## next_chatgpt_action（下一步 ChatGPT 动作）

ChatGPT 下一步应基于本逐字稿驱动接力包，重写新第四期素材锁定版长文案；重点不只是结构，而是话语方式、句子节奏、顺口和颗粒度的配比。输出时必须包含：口播、素材时间码、画面颗粒度、动态 / 音效 / 判断卡建议、边界检查。
