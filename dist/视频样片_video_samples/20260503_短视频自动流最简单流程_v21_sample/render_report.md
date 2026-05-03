# render_report｜短视频自动流 V2.1 样片

## 1. 状态

- `created_at`：`2026-05-03T20:11:40+08:00`
- `technical_validation`：`passed`
- `metadata_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`temporary_preview`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 执行边界

- `已确认` 本轮为 render-only 执行任务。
- `已确认` 使用已落地 V2.1 计划包，不重写 `runtime_script.md`，不重写 `timeline_plan.md`，不重写 `timeline_manifest.json`。
- `已确认` TTS 与字幕来源均为 `runtime_script.md`。
- `已确认` `reference_script.md` 仅复制留档，未用于 TTS、字幕或直接渲染。
- `已确认` Segment 08 使用 API 信息卡 fallback，未使用火山引擎原画面。
- `部分成立` 计划包原始 `guardrail_check.md` 中 render gate 为等待审核；本轮用户已明确下发 render-only 执行单，因此记录为 `current_user_render_only_instruction_authorized_render_after_plan_review`。

## 3. 视频验证

- `full_video.mp4`：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v21_sample/full_video.mp4`
- `duration_seconds`：`105.0`
- `resolution`：`720x1280`
- `video_codec`：`h264`
- `audio_codec`：`aac`
- `audio_present`：`true`
- `decodable`：`true`

## 4. 来源验证

- `runtime_script_sha256`：`a084e094d32c11a7bac298bc380fe315fde7ab9176b5868a88f42d9e9e48e254`
- `reference_script_sha256`：`540a497d147423bb327b92b7edd32a027234eee55523fa92318fef7c2f9af391`
- `runtime_reference_length_ratio`：`0.301`
- `captions_source`：`runtime_script.md`
- `audio_source`：`runtime_script.md`
- `reference_script_used_for_tts`：`false`
- `reference_script_used_for_captions`：`false`

## 5. 素材验证

- `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4`：`hevc`，`3420x2214`，`duration=296.165s`
- `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4`：`hevc`，`3420x2214`，`duration=160.567s`
- `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4`：`hevc`，`3420x2214`，`duration=244.317s`

## 6. 脱敏与敏感信息

- `volcengine_original_used`：`false`
- `api_segment`：`api_info_card_fallback`
- `redaction_decision`：`redaction_blocked_fallback_to_info_card`
- `codex_masks`：右侧分支详情、底部路径、顶部区域、局部任务信息遮挡。
- `trae_masks`：底部路径、顶部本地路径区域遮挡。
- `sensitive_text_scan_passed`：`true`
- `sensitive_text_hits`：`[]`

## 7. 内容边界

- `已确认` Trae 项目骨架不等于 app 跑通。
- `已确认` API 信息卡不等于 API 已接通。
- `已确认` 云剪工位不等于阿里云剪辑正式稳定。
- `已确认` Codex 检查不等于内容过线。
- `已确认` 即梦对比不写成即梦不可用。
