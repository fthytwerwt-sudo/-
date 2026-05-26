# MiniMax B 声音身份锁定报告

- `status`: completed_with_voice_candidates
- `superseded_by_reaudit`: codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/minimax_b_voice_identity_reaudit_report.json
- `user_verdict_after_review`: rejected_all
- `rejection_reason`: wrong_gender_and_wrong_voice_identity
- `future_use_allowed`: false
- `run_id`: 20260527_003423
- `output_dir`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423
- `video_generated`: false
- `full_narration_regenerated`: false
- `copy_changed`: false
- `current_video_modified`: false

## MiniMax 声音能力

- `supports_voice_id`: True
- `supports_voice_list`: True
- `supports_voice_clone`: True
- `supports_reference_audio`: True
- `supports_style_prompt`: False
- `supports_speed_pitch_emotion`: True
- `system_voice_count`: 303

## 本轮策略

- 选择 `option_c_generate_candidate_samples_for_user_selection`。
- MiniMax 复刻/参考音频能力存在，但当前百炼 MiniMax 复刻需要公网 `audio_url`；本轮未上传本地 B 参考音频。
- 所有样本均为 MiniMax route_b 真实短样本，均不使用 Qwen / Serena / macOS say / local fallback。

## 候选样本

`注意`：以下女声候选已在 2026-05-27 被用户全部拒绝，不得继续进入 B 方案锁定候选列表。

### B01_v1_stable
- `voice_id`: female-shaonv
- `voice_name`: 少女音色
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B01_female-shaonv_v1_stable.mp3
- `speed`: 1.08
- `pitch`: 0
- `emotion`: calm
- `vol`: 1
- `pause_style`: moderate
- `duration_seconds`: 13.248
- `non_silent`: True
- `reference_audio_used`: False

### B01_v2_more_emotional
- `voice_id`: female-shaonv
- `voice_name`: 少女音色
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B01_female-shaonv_v2_more_emotional.mp3
- `speed`: 1.04
- `pitch`: 0
- `emotion`: happy
- `vol`: 1
- `pause_style`: stronger_boundary_pause
- `duration_seconds`: 14.22
- `non_silent`: True
- `reference_audio_used`: False

### B02_v1_stable
- `voice_id`: female-shaonv-jingpin
- `voice_name`: 少女音色-beta
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B02_female-shaonv-jingpin_v1_stable.mp3
- `speed`: 1.08
- `pitch`: 0
- `emotion`: calm
- `vol`: 1
- `pause_style`: moderate
- `duration_seconds`: 13.824
- `non_silent`: True
- `reference_audio_used`: False

### B02_v2_more_emotional
- `voice_id`: female-shaonv-jingpin
- `voice_name`: 少女音色-beta
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B02_female-shaonv-jingpin_v2_more_emotional.mp3
- `speed`: 1.04
- `pitch`: 0
- `emotion`: happy
- `vol`: 1
- `pause_style`: stronger_boundary_pause
- `duration_seconds`: 14.868
- `non_silent`: True
- `reference_audio_used`: False

### B03_v1_stable
- `voice_id`: female-yujie
- `voice_name`: 御姐音色
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B03_female-yujie_v1_stable.mp3
- `speed`: 1.08
- `pitch`: 0
- `emotion`: calm
- `vol`: 1
- `pause_style`: moderate
- `duration_seconds`: 16.92
- `non_silent`: True
- `reference_audio_used`: False

### B03_v2_more_emotional
- `voice_id`: female-yujie
- `voice_name`: 御姐音色
- `sample_path`: codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B03_female-yujie_v2_more_emotional.mp3
- `speed`: 1.04
- `pitch`: 0
- `emotion`: happy
- `vol`: 1
- `pause_style`: stronger_boundary_pause
- `duration_seconds`: 19.152
- `non_silent`: True
- `reference_audio_used`: False

## 锁定状态

- `b_voice_identity_lock.status`: pending_user_review
- `expected_b_minimax_voice_id`: null
- `human_voice_review_required`: true
- `human_voice_review_status`: pending_user_review
- `female-tianmei`: forbidden as default B unless user explicitly confirms it.

## 后续保证

- 后续正片候选必须检查 `actual_voice_id == expected_b_minimax_voice_id`。
- 后续正片候选必须检查 `human_voice_review_status == user_confirmed`。
- 只允许在同一 `voice_id` 内调 `speed / pitch / emotion / pause tags`，不得用情绪优化替换音色。
