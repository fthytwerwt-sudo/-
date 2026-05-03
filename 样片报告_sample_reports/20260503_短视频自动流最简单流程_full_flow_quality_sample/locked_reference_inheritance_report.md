# locked_reference_inheritance_report

## 读取状态

- `locked_reference_registry_read`：`true`
- `locked_reference_rules_read`：`true`
- `visual_route_rules_read`：`true`

## 命中 reference

| reference_id | status | 本轮继承情况 | 落点 | 说明 |
|---|---|---|---|---|
| `middle_editing_round34_locked_20260425` | `locked` | `inherited_semantics` | 中段用户录制素材为主体，卡片辅助 | 继承“真实录屏主体，卡片不替代证据”的剪辑语法。 |
| `middle_zoom_reference_confirmed_middle_preview_20260430` | `locked` | `partially_inherited` | 豆包 / Trae / Codex 录屏裁切放大与遮挡 | 继承可读和证据点对齐原则；未逐秒复刻 round34。 |
| `tts_15s_b_pacing_locked_20260427` | `locked` | `partially_inherited` | 临时 TTS 节奏 | 使用系统临时 TTS，节奏方向参考低压停顿；未写 final voice passed。 |
| `sassy_card_pr7_b_visual_locked_20260501` | `locked` | `partially_inherited` | `sassy_reaction_process_card` | 仅用作独立 reaction card 路由与职责继承；未复刻 PR #7 B 图像资产。 |
| `cute_prompt_card_route_locked_20260501` | `locked` | `inherited` | 主持壳 fallback / 段落提示卡 | 少信息量、温柔提示、不开密集字段。 |
| `cute_info_card_route_locked_20260501` | `locked` | `inherited` | API、云剪、Trae 边界、即梦对比、总结卡 | 粉色柔和信息卡，清晰层级，一屏 2-3 模块以内。 |
| `visual_master_voxel_element_doll_candidate_20260430` | `candidate` | `used_as_candidate_only` | 主持壳 fallback 卡的体素娃娃 | 候选参考，不写成 locked。 |

## 未继承 / 未完全继承

- `API 生成真人 / 主持壳 runtime`：未找到本轮可安全真实调用的 API human runtime；使用“主持壳 fallback 卡”承载开头 / 判断 / 转折 / 收束，不冒充 API 真人。
- `云端剪辑 runtime`：本轮使用本地 assembly fallback 生成完整片，不写云剪正式稳定。
- `项目 API TTS / custom voice`：本轮使用 macOS `say` 临时旁白，不写 final voice passed。

## 结论

- `locked_reference_inheritance_validation`：`passed_with_runtime_fallback_gaps`
- `unapproved_reference_changes`：`[]`
- `reference_deviation_blockers`：`[]`
