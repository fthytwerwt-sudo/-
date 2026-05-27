# 旧 B 到 MiniMax 声音迁移报告

## 结论

- `status = blocked_need_reference_audio_url`
- 本轮不恢复旧 Qwen / 阿里正式路线。
- 旧 Qwen / 阿里 B 只作为 `reference_anchor_only`。
- MiniMax 是 `final_generation_provider`。
- 本轮未调用 TTS API，未上传参考音频，未生成音频样本，未生成视频，未改文案，未修改当前视频。

## 路线裁决

```text
old_qwen_role: reference_anchor_only
minimax_role: final_generation_provider
selected_route: route_b_migrate_old_b_to_minimax
system_voice_candidates_allowed: false
old_qwen_formal_route_allowed: false
```

旧 B 历史锚点成立：

```text
provider: aliyun_bailian
model: qwen3-tts-vc-realtime-2026-01-15
custom_voice_masked_id: qwen-t...ac19
```

但 `qwen-t...ac19` 不是 MiniMax `voice_id`，不得写入 `expected_b_minimax_voice_id`。

## 参考音频

已读取并探测：

```text
dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav
duration: 16.32s
codec: pcm_s16le
sample_rate: 24000
channels: 1

dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav
duration: 13.60s
codec: pcm_s16le
sample_rate: 24000
channels: 1
```

## MiniMax 能力

`已确认` MiniMax 官方 voice clone 支持参考音频克隆：官方接口先上传音频获取 `file_id`，再创建 cloned `voice_id`，并可用 `speech-2.8-hd` 生成 preview audio。官方上传接口支持 `mp3 / m4a / wav`，用途为 `voice_clone`。

`已确认` 仓库当前阿里百炼代理到 MiniMax 的历史诊断记录为：voice clone/reference audio 需要公网 `audio_url`；上一轮本地 B 参考音频只读取，没有上传或用于克隆。

官方参考：

- https://platform.minimax.io/docs/api-reference/voice-cloning-clone
- https://platform.minimax.io/docs/api-reference/voice-cloning-uploadcloneaudio
- https://platform.minimax.io/docs/api-reference/api-overview

## 阻断原因

```text
blocked_reason: reference_audio_url_or_upload_authorization_missing
current_audio_url_available: false
reference_audio_upload_authorized: false
can_run_this_round: false
```

本轮没有旧 B 参考音频的公网 `audio_url`，也没有用户授权上传参考音频。因为参考声音属于用户声音资产，本轮不得擅自上传到 OSS 或 MiniMax files/upload。

## 禁止替代

以下声音不能替代旧 B：

```text
female-tianmei
female-shaonv
female-shaonv-jingpin
female-yujie
male-qn-qingse
male-qn-daxuesheng
Chinese (Mandarin)_Gentleman
Chinese (Mandarin)_Gentle_Youth
Chinese (Mandarin)_Sincere_Adult
```

男声方向只是筛选条件，不等于旧 B 声音身份。

## 声音锁

```text
old_b_to_minimax_voice_lock.status: pending_reference_audio_url
old_b_reference_voice_masked_id: qwen-t...ac19
target_provider: minimax
target_model: MiniMax/speech-2.8-hd
generated_minimax_voice_id: null
system_voice_substitution_allowed: false
old_qwen_formal_route_allowed: false
timbre_change_allowed: false
human_voice_review_required: true
human_voice_review_status: pending_reference_audio_url
```

后续正片候选必须检查：

```text
target_provider == minimax
generated_minimax_voice_id exists
system_voice_substitution_allowed == false
old_qwen_formal_route_allowed == false
human_voice_review_status == user_confirmed
```

## 下一步

用户需要二选一授权：

1. 授权把旧 B 参考音频上传到用户可控 OSS，生成 MiniMax 可访问的公网或签名 `audio_url`。
2. 授权使用 MiniMax 官方 `files/upload` 上传旧 B 参考音频，获取 `file_id` 后创建 cloned `voice_id`。

解除阻断后，只生成三条短试听：

```text
V1_identity_match
V2_prosody_optimized
V3_emotion_rich
```

不重生成全片旁白，不替换当前视频音轨，不改文案，不推进 `voice_validation`。

## DeepSeek

已创建供料任务卡并运行 safe runner。runtime provider 为 ready，key 未打印 / 未写入；controller 返回 `blocked_invalid_context_pack`，因此本报告结论不是 DeepSeek 结论：

```text
deepseek_actual_participation: not_attempted_policy_violation
not_deepseek_conclusion: true
```
