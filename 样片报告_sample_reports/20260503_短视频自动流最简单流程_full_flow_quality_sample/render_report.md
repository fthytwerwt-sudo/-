# render_report

## 任务结果

- `sample_type`：`full_flow_quality_sample`
- `technical_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `duration_seconds`：`948.12`
- `minimum_duration_gate`：`passed`
- `full_flow_chain_complete`：`true`
- `full_script_used`：`true`
- `compressed_runtime_used`：`false`
- `pr43_compressed_script_reused`：`false`
- `reference_script_used_for_tts`：`true`
- `reference_script_used_for_captions`：`true`

## 技术验证

- `resolution`：`720x1280`
- `video_codec`：`h264`
- `audio_codec`：`aac`
- `audio_channels`：`1`
- `decodable`：`true`

## 声音

- `audio_validation`：`temporary_preview`
- `voice_source`：macOS `say` `Tingting` 临时旁白
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 主线职责

- API 生成真人：未真实调用；使用主持壳 fallback 卡，不冒充 API 真人。
- 用户录制素材：豆包 / Trae / Codex 段为中段主体推进。
- 少量 PPT / 信息卡：只用于关键词、状态边界、工位解释、对比和总结。
- 云端剪辑：本轮未真实调用云剪；使用本地 assembly fallback，不写云剪稳定。

## 安全

- 火山引擎原画面使用：`false`
- API 段处理：`redaction_blocked_fallback_to_info_card`
- 敏感文本扫描：`passed`
