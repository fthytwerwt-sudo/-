# mechanism_gap_report.md

## 本轮审计结论

- `line_visual_tolerance_rule`: 缺失。已有 `line_level_alignment_preflight` 能检查逐句字段与 mismatch 状态，但没有 5% 局部近似素材容差、核心证据 0 错位、全程漂移阻断和补素材阻断字段。
- `near_equivalent_material_substitution_report`: 缺失。已有素材证据闸门强调不能主题相关硬配，但发片候选预检套件没有逐条输出近似替代素材、时间码、风险和 allowed / blocked 结论。
- `core_evidence_mismatch`: 部分成立。已有 `line_level_alignment_preflight` 与素材证据闸门会阻断未修复 mismatch，但没有把商品卡、候选表、明细表、复查表、边界句、结果差、成本 / 佣金 / 风险 / 下一步列为不可近似替代的核心证据类型。
- `publish_candidate_user_standard`: 缺失。已有 `publish_candidate != send_ready` 和 `technical_preview_not_delivery`，但缺用户口径的“打开后原则上可以直接发、微小瑕疵可接受、重大缺陷阻断”的可判断字段。
- `b_voice_feel_minimax_formal_voice_rule`: 部分成立。已有 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd` 正片候选路线和旧 Qwen / Serena / macOS say 阻断；缺“B 方案是正式听感标准，而不是旧 Qwen / 阿里生成引擎”的独立 gate。
- `publish_candidate_voice_gate`: 已存在，但需与 `b_voice_feel_minimax_preflight` 配套。
- `locked_copy_diff_preflight`: 已存在。
- `line_level_alignment_preflight`: 已存在。
- `visual_evidence_readability_preflight`: 已存在。
- `completion_truth_preflight`: 已存在，但需增加 `publish_candidate_ready_for_human_review != send_ready` 和新报告要求。

## 本轮补强目标

- 新增 `line_visual_tolerance_preflight` 和 `near_equivalent_material_substitution_preflight`，把 5% 局部容差、核心证据 0 错位、全程漂移阻断和补素材阻断接入脚本。
- 新增 `b_voice_feel_minimax_preflight`，把 B 听感标准与 MiniMax 正式生成路线分开判断。
- 新增 `publish_candidate_user_standard_preflight`，把候选片用户标准、小瑕疵、重大缺陷、`send_ready` 边界接入脚本。
- 补 fixture / tests，覆盖用户指定的 7 个 case。
- 更新规则入口、当前正式事实、latest 和 dated log；本轮不生成媒体、不调用 TTS、不修改 `dist/`。
