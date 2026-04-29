# 三张骚萌卡生成 prompt

`已确认` 本轮以 PR #7 A 版为唯一视觉 reference，不做 A/B 融合。
`已确认` 本轮未使用普通信息卡兜底；三张图均为独立 9:16 reaction card 资产。

> 实现说明：为保证三张卡与 PR #7 A 版同角色体系，本轮采用“PR #7 A 版 reference style extension（参考风格扩展）”：保留 A 版角色、橙黄爆炸背景和 3D/GIF 感，替换三张卡的 punchline 文案并统一排版。

## problem_hook_sassy_card

- 输出：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/problem_hook_sassy_card.png`
- 文案：`你以为在做 PPT， / 它以为在写读后感。`

```text
Use PR #7 candidate A as the single visual reference: cheeky blue 3D mascot, orange-yellow burst full-page 9:16 reaction card, wink, raised eyebrow, hand-covering-mouth giggle, smug tiny pointing gesture. Replace punchline with: 你以为在做 PPT，/ 它以为在写读后感。 Keep large bold readable Chinese text, same character system, no platform UI, no sticker overlay, not an info card.
```

## negative_reversal_sassy_card

- 输出：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/negative_reversal_sassy_card.png`
- 文案：`它给了我一份 / 更好的 Word， / 但我要的是 PPT。`

```text
Use PR #7 candidate A as the single visual reference: cheeky blue 3D mascot, orange-yellow comic burst, full-page standalone 9:16 reaction card, mischievous wink and held-back laugh. Punchline: 它给了我一份更好的 Word，/ 但我要的是 PPT。 Make the mood sassy, teasing, funny, not explanatory, not serious, not a course title page.
```

## positive_reversal_sassy_card

- 输出：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/positive_reversal_sassy_card.png`
- 文案：`这回终于不像 / 空气方案了。 / 虽然还不能直接发。`

```text
Use PR #7 candidate A as the single visual reference: same blue 3D mascot and orange-yellow comic burst full-page reaction card. Punchline: 这回终于不像空气方案了。/ 虽然还不能直接发。 Mood is lightly smug relief, funny but bounded, keeps final-product boundary, no extra method explanation.
```
