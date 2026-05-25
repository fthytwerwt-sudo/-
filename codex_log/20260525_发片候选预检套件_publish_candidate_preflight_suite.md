# 20260525｜发片候选预检套件 publish_candidate_preflight_suite

## 1. scope（范围）

- `task_type = mechanism_or_route_fix + project_file_change + code_debug + validation_dry_run`
- 本轮只做机制落库、脚本接入、fixture 和 no-render 验证。
- `video_generated = false`
- `audio_generated = false`
- `media_modified = false`
- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = not_advanced`

## 2. existing_rule_map（既有规则审计）

| rule_name | found_in | current_status_before_this_round | gap_before_this_round |
| --- | --- | --- | --- |
| `line_level_script_visual_alignment_gate` / `script_to_timeline_map` | `AGENTS.md`, `codex_source/00_codex_readme.md`, `codex_source/01_execution_rules.md`, `GPT数据源/05_文案路由规则.md`, `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `documented_only + partial_field_check` | 有 line_group 规则，但缺统一导出前 `actual_visual_observed / source_timecode / mismatch_reason / repair_action` 阻断报告。 |
| `tts_prosody_anchor_map` / `tts_route` | `GPT数据源/05_文案路由规则.md`, `codex_source/21_codex_judgment_permission_matrix.md`, 历史 review pack | `field_exists_check_only` | 有韵律锚点字段，但缺目标 route 与实际 provider/model/voice/fallback 授权一致性预检。 |
| `card_placement_decision` / `judgment_card` / `summary_card` / `result_diff_card` / `boundary_card` / `prompt_tail_card` | `GPT数据源/05_文案路由规则.md`, `codex_source/21_codex_judgment_permission_matrix.md`, `scripts/卡片判断闸门_card_decision_gate.py` | `script_exists + not_unified_before_export` | 有卡片判断脚本，但缺统一要求五类卡片“加与不加都写依据”，也缺 review_pack 必收报告约束。 |
| `forbidden_action` / `no_guess_execution_anchor_gate` | `AGENTS.md`, `codex_source/01_execution_rules.md`, `codex_source/00_codex_readme.md` | `documented_only` | 有禁止猜测和禁止降级完成规则，但缺导出前统一审计 `changed_locked_title / fallback_used_without_authorization / status_promotion` 等禁止事项。 |
| `source_native_no_mask_visual_execution_gate` / `visual_evidence_readability` | `codex_source/01_execution_rules.md`, `scripts/边缘防护_EdgeGuard_edge_residue_guard.py`, 历史 diagnostics | `script_exists + structural_visual_checks` | 已有边缘 / 遮挡相关检查，但缺与核心证据窗口、字幕卡片遮挡、OCR 可读性限制统一进入 publish candidate preflight。 |
| `locked_copy_contract` / `locked_copy_diff` | `AGENTS.md`, `codex_source/00_codex_readme.md`, `codex_source/01_execution_rules.md` | `documented_only + file_exists_check_only` | 有 locked copy 契约要求，但缺对 `actual_subtitle_text / actual_tts_text / actual_card_text` 的统一差异预检。 |
| `completion_truth_check` | `codex_source/01_execution_rules.md`, `codex_source/00_codex_readme.md`, `codex_log/latest.md` | `documented_only` | 有完成真实性规则，但缺检查所有 preflight report、review_pack 包含关系和 forbidden status promotion 的统一脚本出口。 |

## 3. implemented_suite（落库结果）

`publish_candidate_preflight_suite（发片候选预检套件）` 已收束 7 个 required gates：

1. `line_level_alignment_preflight`
2. `tts_route_and_prosody_preflight`
3. `card_decision_preflight`
4. `forbidden_action_preflight`
5. `visual_evidence_readability_preflight`
6. `locked_copy_diff_preflight`
7. `completion_truth_preflight`

后续命中 `publish_candidate / repair_candidate / video_execution / regenerate_video / pre_publish_fix / final_script_to_video / TTS generation / subtitle generation / card generation / timeline assembly / review_pack generation` 时，默认必须在导出前运行该 suite。

## 4. script_and_fixture（脚本与样例）

- `scripts/发片候选预检套件_publish_candidate_preflight_suite.py`
  - 支持 `--no-render`。
  - 支持 `--review-pack / --summary-json / --script-to-timeline-map / --tts-prosody-anchor-map / --locked-copy-contract / --content-route-card / --fixture-cases / --output-dir`。
  - 缺文件时输出 blocked 报告，不吞错。
  - 输出 aggregate report 与 7 个子报告。
  - 当前视觉语义 / OCR / 音频波形类检查标记为 `structural_check_only` 或 `requires_future_visual_probe`，不得写成真实视觉语义验证。
- `codex_source/fixtures/publish_candidate_preflight_suite_cases.json`
  - 已包含 7 个 blocked case。

## 5. review_pack_requirement（审片包要求）

后续 `review_pack` 必须包含：

- `publish_candidate_preflight_report.json`
- `publish_candidate_preflight_report.md`
- `line_level_alignment_report.json`
- `tts_route_and_prosody_report.json`
- `card_decision_preflight_report.json`
- `forbidden_action_audit.json`
- `visual_evidence_readability_report.json`
- `locked_copy_diff_report.json`
- `completion_truth_preflight_report.json`

缺任一 required gate 或 report，不得写 `completed`、不得把 `full.mp4` 存在当完成、不得把 `technical_validation` 当 `content_validation`。

## 6. validation（验证）

已运行：

- `python3 -m py_compile scripts/发片候选预检套件_publish_candidate_preflight_suite.py`
- `python3 scripts/发片候选预检套件_publish_candidate_preflight_suite.py --help`
- `python3 -m json.tool codex_source/fixtures/publish_candidate_preflight_suite_cases.json`
- 关键词 grep：`publish_candidate_preflight_suite` 与 7 个 gate 均可在机制文件 / 脚本 / fixture 中检索到。
- `--no-render` dry-run：输出到 `codex_log/diagnostics/publish_candidate_preflight_suite_20260525_no_render/`。

dry-run 结果：

- `overall_status = blocked`
- `fixture_validation.status = passed`
- blocked 原因来自真实候选片输入缺失与 required gate 未满足；这是预期行为，证明缺预检不能冒充完成。

## 7. DeepSeek participation（DeepSeek 参与）

- 已创建供料任务卡：`codex_log/supply_requests/20260525_publish_candidate_preflight_suite_pre_supply_request.json`
- 安全供料控制器返回：`invalid_context_pack`
- 本轮结论：`fallback_local_only`
- `not_deepseek_conclusion = true`
- 不写成 DeepSeek 深度参与，不写成 DeepSeek 结论。

## 8. remaining_risk（剩余风险）

- 当前脚本已覆盖结构级、字段级、显式信号级阻断；视觉 OCR、真实音频波形、真实画面语义仍需后续视觉探针 / 媒体探针补强。
- 下一轮真实发片 / 修片任务必须用真实 `review_pack` 和真实素材链跑 suite，验证它是否能在导出前阻断文案画面不对齐、TTS route 错误、卡片遗漏、证据被遮挡和 locked copy 被改。
