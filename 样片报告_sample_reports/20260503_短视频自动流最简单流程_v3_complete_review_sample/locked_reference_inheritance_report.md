# locked_reference_inheritance_report

## 1. registry

- `locked_reference_registry_read`：`true`
- `locked_reference_inheritance_validation`：`blocked_for_mainline_fallback_sample_produced`
- `sample_type`：`flow_proof_sample`

## 2. 命中 reference

| reference_id | status | 本轮落点 | 继承状态 |
| --- | --- | --- | --- |
| `middle_editing_round34_locked_20260425` | locked | 用户录制素材主体推进 | `inherited_at_structure_level` |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | locked | 录屏保全画面 + 局部遮挡 | `partially_inherited_no_zoom_contact_evidence` |
| `tts_15s_b_pacing_locked_20260427` | locked | TTS 节奏参考 | `not_inherited_project_tts_fallback` |
| `opening_reference_element_doll_no_text_locked_20260428` | locked | 开头主持壳位置 | `not_inherited_api_human_runtime_missing` |
| `cute_prompt_card_route_locked_20260501` | locked | 开头判断卡 | `inherited_at_route_level` |
| `cute_info_card_route_locked_20260501` | locked | API / 云剪 / 总结信息卡 | `inherited_at_route_level` |
| `sassy_card_pr7_b_visual_locked_20260501` | locked | 未使用骚萌卡 | `not_applicable_no_sassy_card_forced` |
| `visual_master_voxel_element_doll_candidate_20260430` | candidate | 主持壳方向 | `candidate_not_locked` |

## 3. 结论

`已确认` 本轮不能写成 `mainline_inheritance_candidate`，因为 API 主持壳、项目 TTS、V3 云剪未形成本轮真实 runtime 证据。
`已确认` 本轮可以写成 `flow_proof_sample`，用于复审豆包 -> Trae -> 项目骨架 -> Codex 检查流程。
