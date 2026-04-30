# locked reference inheritance report

## 状态

- `locked_reference_registry_read`: `true`
- `locked_reference_inheritance_validation`: `passed_for_finished_quality_candidate_v3`
- `content_validation`: `pending_user_chatgpt_review`
- `send_ready`: `false`
- `voice_validation`: `pending_user_chatgpt_review`
- `final_voice_validated`: `false`

## locked references

| reference_id | 名称 | 本轮是否继承 | 本轮落点 / 证据 | reference deviation |
| --- | --- | --- | --- | --- |
| `middle_editing_round34_locked_20260425` | round34 中段剪辑语法锁定参考 | 已继承 | 真实录屏为主体，卡片只做辅助；本轮反面和正面段均使用真实录屏承担证据。 | 无未授权偏差 |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | 用户确认的中段放大剪辑锁定参考 | 已继承 | 按证据点切换 crop_x，关键文字窗口使用放大裁切，不沿用 PR #15 v2 失败放大位置。 | 无未授权偏差 |
| `sassy_card_three_type_rule_locked_20260428` | 三类骚萌卡放置规则锁定参考 | 已继承 | 三张卡分别落在问题钩子、反面反转、正面反转位置，只做情绪标点。 | 无未授权偏差 |
| `tts_15s_b_pacing_locked_20260427` | B 版 15 秒停顿梗感 TTS 节奏锁定参考 | 已继承 | TTS instructions 继承自然口语、轻吐槽、微反转、句间停顿方向；音色仍为 candidate。 | 不代表最终声音通过 |
| `opening_reference_element_doll_no_text_locked_20260428` | 元素娃娃无字开头锚点锁定参考 | 已继承 | 片头使用 005_1496_seg01_no_text_inpaint_opening_anchor.mp4，生成 2 秒 opening preview。 | 无未授权偏差 |

## candidate references used

- `sassy_card_pr7_a_candidate_20260428`: 仅作为三张骚萌卡视觉候选参考，未升级 locked。
- `card_visual_quality_clean_ui_texture_candidate_20260430`: 用于功能卡、结果差卡、尾卡的清晰质感参考，未升级 locked。
- `visual_master_voxel_element_doll_candidate_20260430`: 用于体素元素娃娃风格融合方向，仍为视觉母版候选。
- `voice_sample2_cute_guide_voice_candidate_20260426`: 使用最近 custom voice 脱敏标识 `qwen-t...ac19`，仍待听感复审。

## failed references avoided

- PR #15 v2 字幕失败参考：本轮 `subtitle_enabled=false`，没有烧录字幕。
- PR #15 v2 layout / 背景失败参考：本轮卡片重做为清晰质感候选方向，不继承其背景与 layout。
- PR #15 v2 TTS 缺失失败参考：本轮有 custom voice TTS 音轨。
- PR #15 v2 放大位置失败参考：本轮按正反证据点重新裁切，不沿用失败位置。

## source notes

- `已确认` 素材保真报告与文案样本节奏报告均已从远端分支只读读取。
- `已确认` 项目中心价值新口径来自本执行单装载；本轮不改 `GPT数据源/08_当前正式事实.md`。
