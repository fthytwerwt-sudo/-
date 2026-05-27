# 20260527｜旧阿里 / Qwen B 方案声音恢复审计

## 任务边界

- `task_type = old_b_voice_restoration_audit`
- 不生成 MiniMax 系统候选。
- 不调用 TTS API。
- 不生成音频 / 视频。
- 不重生成全片旁白。
- 不替换当前视频音轨。
- 不改文案。
- 不推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。

## 审计结论

- `old_b_voice_exists = true`
- `old_b_voice_model = qwen3-tts-vc-realtime-2026-01-15`
- `old_b_voice_masked_id = qwen-t...ac19`
- `provider = aliyun_bailian`
- `api_route_family = aliyun_qwen_realtime_websocket_voice_clone`
- `request_method = WEBSOCKET`
- `create_model = qwen-voice-enrollment`
- `old_b_was_user_preferred = true`
- `confidence = high_for_historical_route_identity; medium_for_current_callable_status_until_next_runtime_smoke`

`qwen-t...ac19` 已确认是仓库中 20260427 B 版“停顿梗感”试配使用的旧阿里 / Qwen custom voice 脱敏标识；它不是 MiniMax `voice_id`。

## 参考音频

- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`
  - `exists = true`
  - `duration = 16.32s`
  - `sample_rate = 24000`
  - `channels = 1`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
  - `exists = true`
  - `duration = 13.6s`
  - `sample_rate = 24000`
  - `channels = 1`

## 证据路径

- `codex_log/20260427_十五秒文案语速停顿试配.md`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/run_summary.json`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_voice_clone_tts_request_debug_sanitized.json`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/custom_voice_list_debug_sanitized.json`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/run_summary.json`
- `scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py`
- `scripts/生成新第四期选品初筛源比例无遮挡B语音修复候选片_generate_new_fourth_selection_source_ratio_no_mask_b_voice_fix_candidate.py`
- `codex_log/20260525_visual_no_mask_source_ratio_and_voice_b_fix.md`
- `dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/summary.json`

## 路线冲突

- `conflict_exists = true`
- `current_minimax_default = MiniMax speech-2.8-hd / MiniMax/speech-2.8-hd`
- `user_requested_old_aliyun_b = true`
- `can_old_b_voice_run_on_minimax_directly = false`
- `can_minimax_clone_old_b_with_reference_audio = possible_but_not_selected_this_round`
- `can_qwen_old_b_route_be_restored_for_publish_candidate = yes_after_explicit_route_restore_and_runtime_smoke`
- `safest_next_path = route_a_restore_old_qwen_b`

## 禁止替代规则

系统音色候选不能替代旧 B，包括：

- `female-tianmei`
- `female-shaonv`
- `female-shaonv-jingpin`
- `female-yujie`
- `male-qn-qingse`
- `male-qn-daxuesheng`
- `Chinese (Mandarin)_Gentleman`
- `Chinese (Mandarin)_Gentle_Youth`
- `Chinese (Mandarin)_Sincere_Adult`

男声候选也不能自动等于旧 B。只有旧 Qwen / 阿里 B 路线恢复，或用旧 B 参考音频克隆并经用户确认，才能成为新 B。

## 下一轮路线

- `selected_route = route_a_restore_old_qwen_b`
- 下一轮如用户允许调用 TTS API，先做最小 runtime smoke。
- smoke 通过后，再决定是否只重生成全片旁白并替换音轨。
- 仍不得改文案、画面或推进声音通过状态，除非用户试听确认。

## DeepSeek

- `supply_request = codex_log/supply_requests/20260527_old_aliyun_b_voice_restoration_audit_pre_supply_request.json`
- `output_dir = codex_log/deepseek_supply/20260527_old_aliyun_b_voice_restoration_audit_pre_supply`
- `runtime_provider.status = ready`
- `api_key_printed = false`
- `api_key_written = false`
- `deepseek_actual_participation = not_attempted_policy_violation`
- `blocked_reason = invalid_context_pack`
- `not_deepseek_conclusion = true`

本轮结论来自 Codex 本地复核仓库证据，不写成 DeepSeek 结论。

## 产物

- `codex_log/diagnostics/old_aliyun_b_voice_restoration_audit_20260527_222316/old_b_voice_restoration_audit_report.json`
- `codex_log/diagnostics/old_aliyun_b_voice_restoration_audit_20260527_222316/old_b_voice_restoration_audit_report.md`
- `scripts/正片候选TTS路线_publish_candidate_tts_route.py`
- `tests/test_publish_candidate_voice_gate.py`
- `tests/test_minimax_b_voice_identity_lock.py`
- `GPT数据源/08_当前正式事实.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `codex_log/latest.md`

## 状态边界

- `video_generated = false`
- `audio_generated = false`
- `tts_api_called = false`
- `copy_changed = false`
- `current_video_modified = false`
- `voice_validation = not_advanced`
- `final_voice_validated = false`
- `content_validation = not_advanced`
- `send_ready = false`
- `visual_master_locked = false`
