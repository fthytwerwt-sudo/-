# 20260528｜锁定旧 B 迁移 MiniMax 声音并替换当前候选片音轨

## 任务结果

- `task_result.status = completed_with_locked_b_voice_audio_replacement`
- `video_generated = true`，但本轮仅生成新输出目录里的音轨替换版 `full.mp4`，不是重新剪辑或重新生成画面。
- `full_narration_regenerated = true`
- `copy_changed = false`
- `current_video_modified = false`，源视频 `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4` 未被替换。
- `visual_changed = false`

## 用户确认

- `selected_voice_id = oldBMinimax20260528010200`
- `selected_sample_version = V2_prosody_optimized`
- `selected_sample_path = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3`
- `selected_sample_source = 刚刚 Codex 生成的 V2 试听样本`
- `user_confirmed = true`
- `future_changes_scope = micro_tuning_only_same_voice_id`

本轮锁定的不是泛指任意 `V2_prosody_optimized` 方向，而是上面这条具体样本对应的声音 ID 和韵律基准。

## 声音锁

- `b_voice_identity_lock.status = user_confirmed`
- `expected_b_minimax_voice_id = oldBMinimax20260528010200`
- `selected_prosody_version = V2_prosody_optimized`
- `target_provider = minimax`
- `target_model = MiniMax/speech-2.8-hd`
- `auth_route = aliyun_bailian_proxy_to_minimax`
- `old_b_reference_voice_masked_id = qwen-t...ac19`
- `old_qwen_role = reference_anchor_only`
- `timbre_change_allowed = false`
- `system_voice_substitution_allowed = false`
- `old_qwen_formal_route_allowed = false`
- `prosody_micro_tuning_allowed = true`
- `emotion_micro_tuning_allowed = true`
- `speed_micro_tuning_allowed = true`
- `human_voice_review_status = user_confirmed`

## 输出产物

- `review_pack_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322`
- `source_video_path = dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4`
- `output_video_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/full.mp4`
- `narration_path = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/narration.wav`
- `tts_route_report = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/tts_route_report.json`
- `b_voice_identity_lock_report = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/b_voice_identity_lock_report.json`
- `voice_gate_report = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/voice_gate_report.json`
- `media_probe = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/media_probe.json`
- `review_manifest = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/review_manifest.md`
- `ffmpeg_decode_check = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/ffmpeg_decode_check.log`
- `audio_volumedetect = dist/new_fourth_episode_selection_publish_candidate_voice_locked_20260528_031322/audio_volumedetect.log`

## 验证

- `actual_voice_id = oldBMinimax20260528010200`
- `actual_tts_provider = minimax`
- `actual_tts_model = MiniMax/speech-2.8-hd`
- `selected_route = aliyun_bailian_proxy_to_minimax`
- `fallback_used = false`
- `system_voice_substitution_used = false`
- `audio_present = true`
- `non_silent = true`
- `mean_volume = -16.0 dB`
- `max_volume = -0.9 dB`
- `video_stream_unchanged = true`
- `audio_track_replaced_only = true`
- `copy_changed = false`
- `visual_changed = false`
- `secret_scan = passed`
- `voice_gate_report.status = passed`
- `video_probe.validation_status = passed`
- `py_compile = passed`
- `unittest = tests.test_publish_candidate_voice_gate + tests.test_minimax_b_voice_identity_lock 22/22 passed`
- `json_parse = passed`
- `git_diff_check = passed`

全片旁白按 `V2_prosody_optimized` 基准生成，因整片音频需对齐源视频时长，执行了同一 `voice_id` 内的轻微速度微调：`tempo_factor = 1.010723`，在允许微调范围内。

## 状态边界

- `publish_candidate_ready_for_human_review = true`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `send_ready = false`
- `content_validation = pending_user_chatgpt_review`
- `visual_master_locked = false`

## DeepSeek

- `supply_request = codex_log/supply_requests/20260528_lock_old_b_minimax_voice_audio_replace_pre_supply_request.json`
- `supply_pack = codex_log/deepseek_supply/20260528_lock_old_b_minimax_voice_audio_replace_pre_supply/latest_supply_pack.md`
- `post_risk_review_request = codex_log/supply_requests/20260528_lock_old_b_minimax_voice_audio_replace_post_risk_review_request.json`
- `post_risk_review_pack = codex_log/deepseek_supply/20260528_lock_old_b_minimax_voice_audio_replace_post_risk_review/latest_supply_pack.md`
- `runtime_provider_status = ready`
- `controller_status = blocked_invalid_context_pack`
- `deepseek_actual_participation = not_attempted_policy_violation`
- `not_deepseek_conclusion = true`
- `api_key_printed = false`
- `api_key_written = false`
