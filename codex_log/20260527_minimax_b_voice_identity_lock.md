# 20260527 MiniMax B 方案声音身份锁定

## 结论

- `task_result.status = completed_with_voice_candidates`
- `video_generated = false`
- `full_narration_regenerated = false`
- `copy_changed = false`
- `current_video_modified = false`
- `send_ready = false`
- `voice_validation = not_advanced`
- `final_voice_validated = false`

## 本轮产物

- `diagnostics_path = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423`
- `minimax_b_voice_identity_lock_report.json = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/minimax_b_voice_identity_lock_report.json`
- `voice_candidate_review_table.md = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/voice_candidate_review_table.md`
- `voice_candidate_review_table.json = codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/voice_candidate_review_table.json`

## MiniMax 能力确认

- `supports_voice_id = true`
- `supports_voice_list = true`
- `supports_voice_clone = true`
- `supports_reference_audio = true`
- `supports_style_prompt = false`
- `supports_speed_pitch_emotion = true`
- `system_voice_count = 303`
- `voice_cloning_count = 1`
- `actual_route = aliyun_bailian_proxy_to_minimax`
- `actual_model = MiniMax/speech-2.8-hd`

## 候选试听样本

| candidate_id | voice_id | voice_name | version | emotion | speed | duration_seconds | sample_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B01_v1_stable | female-shaonv | 少女音色 | v1_stable | calm | 1.08 | 13.248 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B01_female-shaonv_v1_stable.mp3` |
| B01_v2_more_emotional | female-shaonv | 少女音色 | v2_more_emotional | happy | 1.04 | 14.22 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B01_female-shaonv_v2_more_emotional.mp3` |
| B02_v1_stable | female-shaonv-jingpin | 少女音色-beta | v1_stable | calm | 1.08 | 13.824 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B02_female-shaonv-jingpin_v1_stable.mp3` |
| B02_v2_more_emotional | female-shaonv-jingpin | 少女音色-beta | v2_more_emotional | happy | 1.04 | 14.868 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B02_female-shaonv-jingpin_v2_more_emotional.mp3` |
| B03_v1_stable | female-yujie | 御姐音色 | v1_stable | calm | 1.08 | 16.92 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B03_female-yujie_v1_stable.mp3` |
| B03_v2_more_emotional | female-yujie | 御姐音色 | v2_more_emotional | happy | 1.04 | 19.152 | `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/samples/B03_female-yujie_v2_more_emotional.mp3` |

## B 声音身份锁

```text
b_voice_identity_lock.status = pending_user_review
expected_b_minimax_voice_id = null
candidate_expected_b_minimax_voice_id_options = [female-shaonv, female-shaonv-jingpin, female-yujie]
timbre_change_allowed = false
emotion_optimization_allowed = true
prosody_optimization_allowed = true
human_voice_review_required = true
human_voice_review_status = pending_user_review
forbidden_default_voice_id_without_user_confirmation = female-tianmei
```

未经用户试听确认，不得写 `user_confirmed`、不得写 `voice_validation = passed`、不得把 `female-tianmei` 继续当 B 方案默认音色。

## DeepSeek 供料边界

- `supply_request = codex_log/supply_requests/20260527_minimax_b_voice_identity_lock_pre_supply_request.json`
- `supply_output = codex_log/deepseek_supply/20260527_minimax_b_voice_identity_lock_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = not_attempted_policy_violation`
- `blocked_reason = invalid_context_pack`
- `not_deepseek_conclusion = true`
- `post_risk_review_request = codex_log/supply_requests/20260527_minimax_b_voice_identity_lock_post_risk_review_request.json`
- `post_risk_review_output = codex_log/deepseek_supply/20260527_minimax_b_voice_identity_lock_post_risk_review/latest_supply_pack.md`
- `post_risk_review_deepseek_actual_participation = not_attempted_policy_violation`
- `post_risk_review_blocked_reason = invalid_context_pack`
- `post_risk_review_not_deepseek_conclusion = true`

本轮不能写 DeepSeek 已真实参与；机制落地依据为 Codex 本地复核、官方文档与 MiniMax 实测短样本。
