# 锁定参考继承计划 locked_reference_inheritance_plan

## 1. 已读取 registry

`已确认` 已读取：

- `codex_source/14_locked_reference_inheritance_rules.md`
- `codex_source/locked_reference_registry.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

## 2. 本轮命中 locked references

| reference_id | 状态 | 是否允许继承 | 本轮落点 | 不能继承的原因 | 是否 blocked |
| --- | --- | --- | --- | --- | --- |
| `middle_editing_round34_locked_20260425` | `locked` | 是 | 用户录制素材主体推进语法 | 不锁固定时间码，只锁真实录屏主体 + 卡片辅助语法 | 否 |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | `locked` | 是 | 豆包 / Trae / Codex 录屏关键文字可读尺度 | 需下一轮输出放大 / 裁切对照证据 | 否，render 前需验证 |
| `sassy_card_three_type_rule_locked_20260428` | `locked` | 可选继承 | 如设置骚萌卡，只能服务钩子 / 反转 / 正面反转 | 本题不强制三张骚萌卡，不能为了凑卡而插 | 否 |
| `tts_15s_b_pacing_locked_20260427` | `locked` | 是 | TTS 节奏参考 | 只锁 pacing，不锁最终音色 | 否 |
| `opening_reference_element_doll_no_text_locked_20260428` | `locked` | 是 | 开头主持壳 / 元素娃娃 opening 参考 | 读不到 artifact 或 API 主持壳 runtime 缺失时不能 mainline render | render 前待验证 |
| `sassy_card_pr7_b_visual_locked_20260501` | `locked` | 是，如使用骚萌卡 | `sassy_reaction_card_route` | 若读不到 PR #7 B，不得回退 PR #7 A | 可能 blocked |
| `cute_prompt_card_route_locked_20260501` | `locked` | 是 | 段落提示卡 | 不适用于信息卡 / 骚萌卡 | 否 |
| `cute_info_card_route_locked_20260501` | `locked` | 是 | 信息卡、结果差卡、Prompt 引用尾卡 | 不适用于骚萌卡 | 否 |

## 3. candidate references

| reference_id | 状态 | 是否允许继承 | 本轮用法 | 禁止误写 |
| --- | --- | --- | --- | --- |
| `visual_master_voxel_element_doll_candidate_20260430` | `candidate` | 只作方向候选 | vNext 主持壳方向：Minecraft-inspired 原创体素方块风、可爱元素主持娃娃 | 不得写成 visual master locked |
| `card_visual_quality_clean_ui_texture_candidate_20260430` | `candidate` | 只作质感参考 | 信息卡清晰、干净、有层级 | 不得写成 locked visual master |
| `sassy_card_pr7_a_candidate_20260428` | `candidate` / 历史对照 | 不允许作为执行参考 | 仅历史对照 | 不得回退 PR #7 A |

## 4. failed / historical references

- PR #41：`failed`，731 秒说明片，不能继承成片结构。
- PR #42：`failed`，105 秒 render-only 且不符合仓库样片口径，不能继承为合格样片。
- v3：`historical`，只作历史候选 / 对照，不作为后续默认基础。

## 5. blocked 条件

- 把 candidate 写成 locked。
- 把失败 PR 的局部元素写成 locked。
- 把 PR 自评 pass 写成用户确认。
- 读不到 PR #7 B 却回退 PR #7 A。
- 完整成片未输出 `locked_reference_inheritance_report.md`。
- 只写“类似”，没有对照证据。
