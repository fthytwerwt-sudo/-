# 旧 B 到 MiniMax 百炼代理迁移报告

## 任务结果

```text
status: completed_with_old_b_minimax_samples_via_bailian
audio_generated: true
tts_api_called: true
video_generated: false
copy_changed: false
current_video_modified: false
```

## 授权路线复核

- `previous_blocker`: `minimax_official_api_key_missing`
- `should_require_minimax_official_key`: `false`
- `selected_auth_route`: `aliyun_bailian_proxy_to_minimax`
- `aliyun_bailian_auth_available`: `True`
- `detected_env_name`: `authorized_runtime_config:[auth].api_key`
- `api_key_printed`: `false`
- `api_key_written`: `false`

## 百炼 MiniMax 克隆能力

- `supports_minimax_tts`: `true`
- `supports_reference_audio`: `true`
- `supports_voice_clone`: `true`
- `accepts_local_file`: `false`
- `requires_audio_url`: `true`
- `supports_file_upload`: `false`
- `returns_voice_id`: `false`
- `accepts_requested_voice_id`: `true`
- `evidence_path`: `https://help.aliyun.com/zh/model-studio/mini-clone-api`

## 参考音频读取

- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`: exists=True, decode_ok=True, duration=16.32, sample_rate=24000
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`: exists=True, decode_ok=True, duration=13.6, sample_rate=24000

## 上传输入

- `reference_audio_1`: uploaded=True, audio_url=https://zvip1-video-beijing.oss-cn-beijing.aliyuncs.com/video-factory/temp/old-b-to-minimax-bailian-20260528_010200/old_b_to_minimax_bailian/reference_audio/reference_audio_1_B_15%E7%A7%92%E6%96%87%E6%A1%88_%E5%81%9C%E9%A1%BF%E6%A2%97%E6%84%9F.wav?[REDACTED_SIGNED_QUERY], file_id=None
- `reference_audio_2`: uploaded=True, audio_url=https://zvip1-video-beijing.oss-cn-beijing.aliyuncs.com/video-factory/temp/old-b-to-minimax-bailian-20260528_010200/old_b_to_minimax_bailian/reference_audio/reference_audio_2_%E8%AF%AD%E9%9F%B3%E6%A0%B7%E6%9C%AC2_%E5%A3%B0%E9%9F%B3%E5%A4%8D%E5%88%BB%E8%AF%95%E5%90%AC_15%E7%A7%92.wav?[REDACTED_SIGNED_QUERY], file_id=None

## 样本状态

| sample_id | status | generated_minimax_voice_id | sample_path | non_silent | prosody_version |
| --- | --- | --- | --- | --- | --- |
| V1_identity_match | generated | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V1_identity_match.mp3` | True | V1_identity_match |
| V2_prosody_optimized | generated | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3` | True | V2_prosody_optimized |
| V3_emotion_rich | generated | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V3_emotion_rich.mp3` | True | V3_emotion_rich |

## 状态边界

- `full_narration_regenerated`: `false`
- `current_video_modified`: `false`
- `copy_changed`: `false`
- `voice_validation`: `not_advanced`
- `send_ready`: `false`
- `system_voice_candidates_allowed`: `false`
- `old_qwen_formal_route_allowed`: `false`

## 阻断 / 下一步

- `blocked_reason`: ``
- `next_required_user_action`: `试听 V1/V2/V3，选择一个或全部拒绝。`

用户下一步只需要试听已生成样本，选择一个候选或全部拒绝；未经试听确认，不能写 `user_confirmed`。
