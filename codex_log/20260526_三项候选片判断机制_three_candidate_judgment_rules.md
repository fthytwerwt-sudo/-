# 20260526｜三项候选片判断机制落库

## 本轮边界

- `已确认` 本轮只做机制落库，不生成视频、不生成音频、不生成 TTS、不调用 MiniMax / 阿里 / 百炼 / TTS API。
- `已确认` 本轮不修改 `dist/` 下任何媒体产物，不修改素材目录，不修改用户 locked copy。
- `已确认` 本轮不推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked`。

## DeepSeek 供料

- 前置任务卡：`codex_log/supply_requests/20260526_three_candidate_judgment_rules_pre_supply_request.json`
- safe runner 输出：`codex_log/deepseek_supply/20260526_three_candidate_judgment_rules_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `not_deepseek_conclusion = false`
- `api_key_printed = false`
- `api_key_written = false`
- `multi_agent_runtime_validation = not_started`

## DeepSeek 后置风险复核

- 后置风险复核任务卡：`codex_log/supply_requests/20260526_three_candidate_judgment_rules_post_risk_review_request.json`
- safe runner 输出：`codex_log/deepseek_supply/20260526_three_candidate_judgment_rules_post_risk_review/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `not_deepseek_conclusion = false`
- `api_key_printed = false`
- `api_key_written = false`
- 风险复核读取结果：`forbidden_status_promotion = 未发现`；`secret_risk = 未检测到`；`fallback_mislabel_risk = none_observed`。

## 机制 gap 审计

- 输出：`codex_log/mechanism_gap_report.md`
- 缺失项：`line_visual_tolerance_rule`、`near_equivalent_material_substitution_report`、`publish_candidate_user_standard_rule`
- 部分成立项：`b_voice_feel_minimax_formal_voice_rule`、`core_evidence_mismatch`
- 已存在项：`publish_candidate_voice_gate`、`locked_copy_diff_preflight`、`line_level_alignment_preflight`、`visual_evidence_readability_preflight`、`completion_truth_preflight`

## 已落库机制

### line_visual_tolerance_rule

```text
status: active
max_near_equivalent_ratio: 0.05
max_consecutive_near_equivalent_groups: 1
whole_video_drift_allowed: false
core_evidence_mismatch_allowed: false
blocked_if:
  - near_equivalent_ratio > 0.05
  - core_evidence_mismatch_count > 0
  - whole_video_drift_detected = true
  - visual_requires_guessing = true
  - replacement_material_not_extremely_close = true
  - user_material_needed_but_missing = true
```

`极其相近素材` 不等于主题相近；`局部降级` 不等于全程偏差。素材无法支撑文案时必须 blocked，等待用户补素材视频或图片，不允许为了完成出片硬剪。

### near_equivalent_material_substitution_report

后续候选片必须输出：

```text
total_line_group_count
exact_match_count
near_equivalent_count
near_equivalent_ratio
consecutive_near_equivalent_max
core_evidence_mismatch_count
whole_video_drift_detected
substitutions
final_decision
```

### b_voice_feel_minimax_formal_voice_rule

- `b_voice_scheme_role = formal_voice_feel_reference`
- B 方案升级为正式声音听感标准。
- 正式生成路线必须是 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`。
- 旧 Qwen / 阿里 B 语音路线、`qwen3-tts-vc-realtime-2026-01-15`、`qwen-t...ac19`、`Serena`、`macOS say`、本地低质 TTS、silent audio 或未授权 fallback 不能作为正片候选完成条件。

### publish_candidate_user_standard_rule

- 候选可发布的用户标准：用户打开片子后原则上可以直接发，再进入人工复审。
- 可接受：微小节奏瑕疵、非核心转场小问题、不影响理解的字幕节奏小问题、小审美瑕疵。
- 不可接受：locked copy 被改、标题被改、声音路线错、fallback / 无声、全程漂移、核心证据错位、字幕 / 卡片遮挡核心证据、明显黑灰边 / 白屏 / 黑块 / 未授权整屏遮挡、技术预览或内部诊断冒充候选片、缺 review pack / preflight suite、未验证就写完成。
- `publish_candidate_ready_for_human_review != send_ready`；`send_ready` 必须等待用户或 ChatGPT 最终确认。

## 执行入口

- `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` 已新增：
  - `line_visual_tolerance_preflight`
  - `near_equivalent_material_substitution_preflight`
  - `b_voice_feel_minimax_preflight`
  - `publish_candidate_user_standard_preflight`
- `scripts/正片候选TTS路线_publish_candidate_tts_route.py` 已新增：
  - `B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE`
  - `validate_b_voice_feel_minimax_route`
- `codex_source/fixtures/publish_candidate_preflight_suite_cases.json` 已补用户指定的 7 个 case。
- `tests/test_publish_candidate_voice_gate.py` 与 `tests/test_publish_candidate_preflight_tolerance.py` 已覆盖最小行为。

## 更新入口

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/latest.md`

`GPT数据源/11_项目状态动作总控器_机制推理层.md` 本轮已读取；因本地存在非本轮 dirty diff，本轮不写入，避免混入 unrelated changes。执行层对应路由已写入 `codex_source/19_project_state_action_router.md`。

## 验证记录

- `python3 -m unittest tests.test_publish_candidate_voice_gate tests.test_publish_candidate_preflight_tolerance`: passed
- `python3 scripts/发片候选预检套件_publish_candidate_preflight_suite.py --no-render --fixture-cases codex_source/fixtures/publish_candidate_preflight_suite_cases.json --output-dir codex_log/diagnostics/three_candidate_judgment_rules_preflight_20260526_no_render --allow-blocked-exit-zero`: passed；`overall_status = blocked` 符合 no-input dry run 预期；`fixture_validation.status = passed`，`case_count = 19`。
- 其余验证见最终回报与 Git diff。

## 状态边界

- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation = not_advanced`
- `final_voice_validated = false`
- `visual_master_locked = false`
- `media_generated = false`
- `audio_generated = false`
- `tts_api_called = false`
- `dist_modified = false`
