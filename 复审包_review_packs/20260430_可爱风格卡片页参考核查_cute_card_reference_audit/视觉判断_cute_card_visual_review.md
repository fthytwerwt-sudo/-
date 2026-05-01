# 可爱风格卡片页视觉判断

## main_judgment

`已确认` GitHub / 仓库内存在可爱风格卡片页参考，真实对象是 `prompt_card_pink_sakura_round34_candidate_20260430（round34 粉色樱花提示卡候选）`；它是段落提示卡视觉候选，不是清晰 UI 信息卡候选，也不是骚萌 reaction card。

## reference_check

### prompt_card_pink_sakura_round34_candidate_20260430

`已确认` registry 记录：

- `type = prompt_card_visual（提示卡视觉）`
- `status = candidate（候选参考）`
- `artifact_path = dist/latest_review_pack/反面展示提示卡_单帧.png; dist/latest_review_pack/正面展示提示卡_单帧.png`
- `evidence_path = dist/latest_review_pack/图二参考图.png; dist/latest_review_pack/正反提示卡_并排对比.png; dist/latest_review_pack/review_manifest.md; dist/latest_review_pack/cut_map.md`
- `applies_to = round34 同类反面 / 正面展示提示卡、段落提示卡`
- `does_not_apply_to = 全片背景风格、骚萌卡视觉、字幕标准、完整 visual master`

### card_visual_quality_clean_ui_texture_candidate_20260430

`已确认` 这条是功能卡 / 结果差卡 / Prompt 引用尾卡的清晰质感候选参考，继承重点是干净、留白、圆角、轻阴影、轻高光、层级舒服、文字清楚、有一点高级 UI 感。

`已确认` 它明确不适用于骚萌卡，也不继承底部黑色按钮、电商筛选页、`More Filters` CTA、假 App 导航。

## visual_evidence

`已确认` 找到并查看以下图片：

- `图二参考图.png`：横版粉色樱花展示牌，带桌面 / 樱花 / 杯子 / 柔光背景，是 round34 参考图来源。
- `round34_反面展示提示卡.png`：720x1280 竖屏重构，中心白粉圆角展示牌，主标题《反面展示》，一句短副标题。
- `round34_正面展示提示卡.png`：720x1280 竖屏重构，和反面卡统一风格，主标题《正面展示》。
- `round34_正反提示卡并排对比.png`：证明两张提示卡视觉统一。

## visual_features

| 维度 | 判断 |
| --- | --- |
| 可爱感 | `已确认` 强，来自粉色主色、樱花枝、蝴蝶结、花边和柔光 |
| 清晰度 | `已确认` 标题清楚，副标题可读 |
| 信息层级 | `部分成立` 适合 1 个大标题 + 1 句副标题，不适合直接承载复杂字段拆解 |
| 字体可读性 | `已确认` 大标题可读，副标题需要控制字数 |
| 留白 | `已确认` 大面积留白，短信息舒适 |
| 是否像普通 PPT 模板 | `已确认` 不像普通 PPT，更像柔和展示牌 |
| 是否适合 9:16 | `已确认` round34 已有 720x1280 竖屏重构 |
| 是否兼容体素 / 元素娃娃 | `部分成立` 同属可爱表达壳，但需要避免和体素场景背景割裂 |
| 是否能和骚萌卡区分 | `已确认` 它是展示牌，不是角色表情 reaction card |
| 是否能和录屏共存 | `已确认` round34 中只做短段落提示，不替代录屏证据 |

## difference_from_clean_ui_reference

`prompt_card_pink_sakura_round34_candidate_20260430` 更像“可爱展示牌 / 段落提示牌”：粉色、樱花、花边、蝴蝶结、软光、情绪亲和，信息量低，适合开段、转场、短提示。

`card_visual_quality_clean_ui_texture_candidate_20260430` 更像“清晰 UI 信息卡”：干净、结构化、留白、圆角、轻阴影、层级明确，适合功能卡、结果差卡、Prompt 尾卡承载更多信息。

## recommendation

`部分成立` 如果下一轮目标是摆脱“冷静科技 UI”，建议把 `prompt_card_pink_sakura_round34_candidate_20260430` 作为信息卡确认图的主情绪 / 皮肤参考，同时保留 `card_visual_quality_clean_ui_texture_candidate_20260430` 的可读性、留白和层级规则。

不建议直接把 round34 提示卡原样套到结果差卡 / Prompt 尾卡上，因为结果差卡需要两列对比和底部判断，Prompt 尾卡需要可读字段，信息量明显高于 round34 段落提示卡。

## chatgpt_prompt_boundary

下一张确认图可以要求：

- 走粉色樱花柔和展示牌方向。
- 保留白粉圆角主卡、细线边框、轻花边、樱花枝、少量花瓣、蝴蝶结、柔和光感。
- 字体要中文大字清楚，不堆小字。
- 信息卡仍需有清晰分组、足够留白和可读层级。
- 不要冷静科技 SaaS UI，不要底部黑按钮，不要电商筛选页，不要 More Filters CTA。
- 不要做成骚萌卡，不要角色表情，不要 wink / 捂嘴偷笑。

## route_suggestion

`待验证` 下一轮若要落入生成脚本，建议把视觉路由拆成三条：

1. `cute_prompt_card_route`：继承 round34 粉色樱花展示牌，用于段落提示卡、温柔提示卡。
2. `cute_info_card_route`：以粉色樱花为皮肤，以清晰 UI 质感为层级，用于功能卡 / 结果差卡 / Prompt 尾卡确认图。
3. `sassy_reaction_card_route`：按用户 2026-05-01 最新确认独立继承 PR #7 B 版骚萌 reaction card，不和前两者混用；若读不到 PR #7 B，必须 blocked，不得回退 PR #7 A。

## boundaries

- `已确认` 未生成新视频。
- `已确认` 未生成新卡片。
- `已确认` 未修改 v3。
- `已确认` 未修改 `dist/latest_review_pack`。
- `已确认` 未修改 `content_validation`。
- `已确认` 未修改 `send_ready`。
- `已确认` 未修改 registry 状态。
- `已确认` 未把 candidate 写成 locked。
