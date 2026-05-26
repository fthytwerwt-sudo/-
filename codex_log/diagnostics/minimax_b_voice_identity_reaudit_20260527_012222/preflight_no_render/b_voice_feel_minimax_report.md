# b_voice_feel_minimax_preflight

- `status`: `blocked`
- `check_depth`: `structural_check_only`
- `blocked_reasons`:
  - `actual_gender_direction_missing`
  - `actual_voice_id_missing`
  - `audio_missing_or_silent`
  - `audio_not_generated_or_missing`
  - `b_voice_feel_not_reflected`
  - `b_voice_feel_required_tags_missing`
  - `expected_b_minimax_voice_id_missing`
  - `failed_non_minimax_voice`
  - `human_voice_review_status_not_user_confirmed`
  - `tts_route_report_missing`
  - `voice_identity_lock_status_not_user_confirmed`
- `warnings`:
  - `B 方案升级的是正式听感标准，不是旧 Qwen / 阿里 B 语音引擎。`
  - `正式候选片生成路线必须是 MiniMax speech-2.8-hd 或 MiniMax/speech-2.8-hd；旧 B 语音脚本只能是历史 / reference / internal diagnostic。`
