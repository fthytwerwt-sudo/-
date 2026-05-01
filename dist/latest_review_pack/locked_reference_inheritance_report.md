# locked reference inheritance report

## 状态

- `locked_reference_registry_read`: `true`
- `locked_reference_inheritance_validation`: `passed_for_finished_quality_candidate_v31_visual_route_fix`
- `content_validation`: `pending_user_chatgpt_review_or_not_passed_copywriting_side`
- `send_ready`: `false`
- `voice_validation`: `pending_user_chatgpt_review`
- `final_voice_validated`: `false`
- `sassy_card_execution_reference`: `PR7_B_骚萌反应页.png`
- `sassy_card_reference_status`: `locked_reference_formal_synced_for_future_execution`
- `sassy_card_reference_locked`: `true`

## locked references

| reference_id | 名称 | 本轮是否继承 | 本轮落点 / 证据 | reference deviation |
| --- | --- | --- | --- | --- |
| `middle_editing_round34_locked_20260425` | round34 中段剪辑语法锁定参考 | 已继承 | 真实录屏为主体，卡片只做辅助；本轮反面和正面段均使用真实录屏承担证据。 | 无未授权偏差 |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | 用户确认的中段放大剪辑锁定参考 | 已继承 | 按证据点切换 crop_x，关键文字窗口使用放大裁切，不沿用 PR #15 v2 失败放大位置。 | 无未授权偏差 |
| `sassy_card_three_type_rule_locked_20260428` | 三类骚萌卡放置规则锁定参考 | 已继承 | 三张卡分别落在问题钩子、反面反转、正面反转位置；视觉执行参考改为 PR #7 B locked execution reference。 | PR #7 B 已成为后续唯一执行参考；不代表视觉母版 locked |
| `tts_15s_b_pacing_locked_20260427` | B 版 15 秒停顿梗感 TTS 节奏锁定参考 | 已继承 | TTS instructions 继承自然口语、轻吐槽、微反转、句间停顿方向；音色仍为 candidate。 | 不代表最终声音通过 |
| `opening_reference_element_doll_no_text_locked_20260428` | 元素娃娃无字开头锚点锁定参考 | 已继承 | 片头使用 005_1496_seg01_no_text_inpaint_opening_anchor.mp4，生成 2 秒 opening preview。 | 无未授权偏差 |

## candidate references used

- `prompt_card_pink_sakura_round34_candidate_20260430`: 用于反面 / 正面段落提示卡，并作为信息卡主情绪 / 皮肤参考，未升级 locked。
- `card_visual_quality_clean_ui_texture_candidate_20260430`: 仅继承功能卡、结果差卡、尾卡的结构清晰度 / 留白 / 可读性规则，不继承冷静科技 UI 皮肤，未升级 locked。
- `sassy_card_pr7_b_visual_locked_20260501`: PR #7 B 是后续骚萌卡唯一执行参考；本轮基线切换已同步为主读取分支 locked reference，不代表视觉母版 locked。
- `voice_sample2_cute_guide_voice_candidate_20260426`: 使用最近 custom voice 脱敏标识 `qwen-t...ac19`，仍待听感复审。

## failed references avoided

- PR #15 v2 字幕失败参考：本轮 `subtitle_enabled=false`，没有烧录字幕。
- PR #15 v2 layout / 背景失败参考：本轮卡片重做为清晰质感候选方向，不继承其背景与 layout。
- PR #15 v2 TTS 缺失失败参考：本轮有 custom voice TTS 音轨。
- PR #15 v2 放大位置失败参考：本轮按正反证据点重新裁切，不沿用失败位置。
- v3 当前骚萌卡视觉混用信息卡外壳的问题：本轮拆出 `sassy_reaction_card_route`。
- ChatGPT 上一张深蓝科技 UI 信息卡方向：本轮信息卡改走粉色樱花柔和展示牌皮肤。

## source notes

- `已确认` PR #7 B 参考图与可爱卡片页参考包均已从远端分支只读读取。
- `已确认` 本轮不改 `GPT数据源/` 静态包。
