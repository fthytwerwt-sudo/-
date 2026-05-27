# 旧 B 到 MiniMax 迁移解阻报告

## 任务结果

```text
status: blocked
audio_generated: false
tts_api_called: false
video_generated: false
copy_changed: false
current_video_modified: false
```

## 路线裁决

- `old_qwen_role`: `reference_anchor_only`
- `minimax_role`: `final_generation_provider`
- `selected_route`: `route_b_migrate_old_b_to_minimax`
- `system_voice_candidates_allowed`: `false`

## 参考音频读取

- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`: exists=True, decode_ok=True, duration=16.32, sample_rate=24000
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`: exists=True, decode_ok=True, duration=13.6, sample_rate=24000

## 上传策略

- `selected`: `minimax_official_file_upload`
- `reason`: MiniMax 官方 voice clone 文档要求通过 /v1/files/upload 获取 file_id；当前没有可确认的 MiniMax audio_url 克隆接口，因此不把 OSS URL 当作已可用的克隆输入。
- `option_a_upload_to_user_controlled_oss.available`: `True`
- `option_a_upload_to_user_controlled_oss.selected`: `false`
- `option_b_minimax_official_file_upload.available`: `False`
- `upload_attempted`: `false`

本轮没有上传参考音频。原因是 MiniMax 官方克隆需要 `MINIMAX_API_KEY` 调用 `/v1/files/upload` 获取 `file_id`；当前本地未提供该官方认证。只上传到 OSS 不能生成 `generated_minimax_voice_id`，所以不做无效上传。

## 样本状态

| sample_id | status | blocked_reason |
| --- | --- | --- |
| V1_identity_match | not_generated | minimax_official_api_key_missing |
| V2_prosody_optimized | not_generated | minimax_official_api_key_missing |
| V3_emotion_rich | not_generated | minimax_official_api_key_missing |

## 阻断原因

- `primary_blocked_reason`: `minimax_official_api_key_missing`
- `blocked_reasons`: `minimax_official_api_key_missing`

## 声音锁边界

- `old_b_to_minimax_voice_lock.status`: `pending_minimax_official_auth`
- `generated_minimax_voice_id`: `null`
- `human_voice_review_status`: `pending_minimax_official_auth`
- `system_voice_substitution_allowed`: `false`
- `timbre_change_allowed`: `false`

## 后续动作

下一轮只需要在安全运行环境提供 `MINIMAX_API_KEY`，再复跑本入口生成 V1 / V2 / V3 三条短样本。不得回退到 MiniMax 系统音色候选，不得恢复旧 Qwen 为正式路线。
