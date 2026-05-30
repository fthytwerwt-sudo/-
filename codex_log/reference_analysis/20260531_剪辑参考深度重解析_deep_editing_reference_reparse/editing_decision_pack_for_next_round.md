# 下一轮剪辑决策包 Editing Decision Pack For Next Round

## 1. decision_boundary（决策边界）

- `source_reference = /Users/fan/Documents/视频工厂/素材录制/剪辑参考/ScreenRecording_05-24-2026 21-12-50_1.MP4`
- `derived_from_report = codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/deep_reference_reparse_report.md`
- `status = draft_for_chatgpt_user_review`
- `is_this_a_minor_element_upgrade = false`
- `is_this_a_full_editing_method_change = true`
- `video_generated = false`
- `core_rules_modified = false`

## 2. target_style_statement（目标风格一句话）

把真实录屏 / 文档证据包装成一套 `guided proof video（被引导的证据视频）`：每个画面先说明看哪里，再展示证据，再用字幕、标签、高亮、分屏和非真人桥接保持顺滑。

## 3. required_inputs（下一轮必需输入）

- `locked_copy_contract`
- `material_parse_pack`
- `script_to_timeline_map`
- `current_data_goal_anchor`
- `visual_style_decision`
- `active_evidence_window_map`

缺任一项，不进入真实剪辑验证。

## 4. core_rules（核心执行规则）

| rule_id | rule | blocked_if |
| --- | --- | --- |
| `edp_01_active_evidence_window` | 每个 line_group 必须先确定 `active_evidence_window` | 只给整页截图或主题相关画面 |
| `edp_02_subtitle_as_attention_guide` | 字幕服务节奏和注意力，不做长篇转写 | 字幕遮挡证据或改变锁稿语义 |
| `edp_03_split_screen_comparison_only` | 分屏只用于 before/after、prompt/result、source/output、option A/B | 分屏只是装饰或 panel 不可读 |
| `edp_04_one_claim_one_highlight` | 一句/一组只允许一个主高亮簇 | 多高亮导致不知道看哪里 |
| `edp_05_non_human_bridge_default` | 默认用低密度桥接卡 + 声音/字幕桥替代真人桥 | 默认真人实拍或复制创作者身份 |
| `edp_06_bridge_after_dense_blocks` | 连续 2-3 个 dense proof screen 后插入低密度桥 | 桥接卡拖慢未完成的证据链 |
| `edp_07_no_decoration_overload` | 一屏最多一节标签、一高亮、一 guide/PiP、一字幕块 | 装饰层覆盖 prompt/table/button/chat evidence |

## 5. minimum_validation_scope（最小验证范围）

```yaml
recommended_validation_scope:
  duration: 30_to_45s
  source_material: one dense evidence segment
  output:
    - before_after_comparison
    - 30_to_45s_clip
    - review_pack
  must_validate:
    - subtitle_readability
    - split_screen_readability
    - evidence_window_safety
    - no_real_person_default
    - no_decoration_overload
    - smoother_than_current_baseline
```

## 6. non_human_bridge_policy（非真人人感桥策略）

默认优先级：

1. `low_density_bridge_card + voice_and_subtitle_bridge`
2. `element_doll_or_guide` only as small edge guide
3. `api_generated_human` only for opening / transition / closing after route decision

禁止：

- `default_real_person_shooting`
- `copied_creator_face_or_identity`
- `stock_person_as_fake_evidence`

## 7. split_screen_policy（分屏策略）

- `use_when`: before/after, prompt/result, source/output, option A/B, two evidence states that must be compared.
- `do_not_use_when`: one evidence stream is enough, text becomes unreadable, panel role is unclear, or split is decorative.
- `max_panel_count`: 2 dense panels by default; 3 only for low-text labels; 4 only for very short preview board.
- `required_fields`: `split_screen_use_reason / panel_role / panel_source_timecode / panel_active_evidence_window / comparison_claim / exit_condition`.

## 8. subtitle_policy（字幕策略）

- `subtitle_text`: 1-2 short lines.
- `keyword_badge_text`: separate from subtitle, only for hook/punchline/section terms.
- `subtitle_safe_zone`: must be chosen before render.
- `subtitle_change_sync_point`: align with cut, hold or claim transition.
- `blocked_if`: subtitle covers evidence, adds unverified claim, or changes locked copy meaning.

## 9. screen_design_policy（屏幕设计策略）

Allowed elements:

- dark/neutral matte background
- clean evidence container
- section label
- active highlight
- small keyword badge
- optional guide layer outside proof
- subtitle safe area

Forbidden elements:

- rough PPT mockup as final design
- exact Douyin/TikTok wrapper
- copied creator face / stickers / fonts
- decorative collage without evidence role
- labels covering evidence
- dense cute card for every screen

## 10. blocked_if（阻断条件）

- no `locked_copy_contract`
- no `material_parse_pack`
- no `script_to_timeline_map`
- no `active_evidence_window`
- split screen has no comparison reason
- subtitle/card overlap high severity
- guide layer covers evidence
- default real-person shooting is selected without explicit route decision
- current media output cannot be verified
