# 20260528｜旧 B 通过阿里百炼代理迁移到 MiniMax 试听样本

## 任务结果

- `status = completed_with_old_b_minimax_samples_via_bailian`
- `video_generated = false`
- `full_narration_regenerated = false`
- `current_video_modified = false`
- `copy_changed = false`
- `voice_validation = not_advanced`
- `send_ready = false`

## 授权路线复核

- `previous_blocker = minimax_official_api_key_missing`
- `user_correction = use_aliyun_bailian_api_key`
- `should_require_minimax_official_key = false`
- `selected_auth_route = aliyun_bailian_proxy_to_minimax`
- `aliyun_bailian_auth_available = true`
- `detected_env_name = authorized_runtime_config:[auth].api_key`
- `api_key_printed = false`
- `api_key_written = false`

## 百炼 MiniMax 克隆能力

- `supports_minimax_tts = true`
- `supports_reference_audio = true`
- `supports_voice_clone = true`
- `accepts_local_file = false`
- `requires_audio_url = true`
- `supports_file_upload = false`
- `returns_voice_id = false`
- `accepts_requested_voice_id = true`
- `generated_voice_id_source = input.voice_id accepted; output.voice_id not echoed in the 20260528 call`
- `evidence_path = https://help.aliyun.com/zh/model-studio/mini-clone-api`

## 旧 B 参考音频

- `reference_audio_1 = dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`
  - `decode_ok = true`
  - `duration = 16.32s`
  - `sample_rate = 24000`
- `reference_audio_2 = dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
  - `decode_ok = true`
  - `duration = 13.60s`
  - `sample_rate = 24000`

## 上传与生成

- `upload_strategy.selected = upload_to_user_controlled_oss`
- `audio_url_created = true`
- `file_id_created = false`
- `reference_audio_committed_to_git = false`
- `generated_minimax_voice_id = oldBMinimax20260528010200`

本轮仅上传用户授权范围内两条旧 B 参考音频到用户可控 OSS；报告只记录脱敏签名 URL，不写入完整签名参数。

## 试听样本

| sample_id | sample_path | duration | non_silent | voice_id |
| --- | --- | --- | --- | --- |
| `V1_identity_match` | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V1_identity_match.mp3` | `15.697s` | `true` | `oldBMinimax20260528010200` |
| `V2_prosody_optimized` | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3` | `16.236s` | `true` | `oldBMinimax20260528010200` |
| `V3_emotion_rich` | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V3_emotion_rich.mp3` | `15.660s` | `true` | `oldBMinimax20260528010200` |

## 复审表与报告

- `migration_report = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/old_b_to_minimax_bailian_report.json`
- `migration_report_md = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/old_b_to_minimax_bailian_report.md`
- `review_table = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/voice_candidate_review_table_old_b_minimax.md`
- `review_table_json = codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/voice_candidate_review_table_old_b_minimax.json`

## 声音锁状态

- `old_b_to_minimax_voice_lock.status = pending_user_review`
- `generated_minimax_voice_id = oldBMinimax20260528010200`
- `human_voice_review_required = true`
- `human_voice_review_status = pending_user_review`
- `system_voice_substitution_allowed = false`
- `timbre_change_allowed = false`
- `old_qwen_formal_route_allowed = false`

未经用户人工试听确认，不得写 `user_confirmed`，不得推进 `voice_validation = passed` 或 `final_voice_validated = true`。

## DeepSeek 供料

- `supply_request = codex_log/supply_requests/20260528_old_b_to_minimax_bailian_pre_supply_request.json`
- `supply_pack = codex_log/deepseek_supply/20260528_old_b_to_minimax_bailian_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `api_key_printed = false`
- `api_key_written = false`

## DeepSeek 执行后风险复核

- `post_risk_review_request = codex_log/supply_requests/20260528_old_b_to_minimax_bailian_post_risk_review_request.json`
- `post_risk_review_pack = codex_log/deepseek_supply/20260528_old_b_to_minimax_bailian_post_risk_review/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `api_key_printed = false`
- `api_key_written = false`

## 禁止 fallback

- 不得用 `female-tianmei` 或上一轮女声候选替代旧 B。
- 不得用男声 / 中性系统候选替代旧 B。
- 不得恢复旧 Qwen 为后续正式默认路线。
- 不得使用 `macOS say`、`Serena`、本地 TTS 或 silent audio。

## 下一步

用户试听 `V1_identity_match / V2_prosody_optimized / V3_emotion_rich` 后，选择一个样本或全部拒绝。只有用户确认后，才能把该 `generated_minimax_voice_id` 写入正式 B 声音身份锁。
