# local_fix_report

- `result_status`：`local_reference_fix_completed`
- `technical_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `assembly_mode`：`local_reference_quality_fix`
- `cloud_assembly_used`：`false`
- `local_assembly_used`：`true`
- `macos_say_used`：`false`

## 已确认

- 已用阿里 `qwen3-tts-vc-realtime-2026-01-15` 重新生成完整 TTS。
- 开头元素娃娃只保留约 2 秒。
- 后续元素娃娃段已移除，按适配度改由骚萌卡、用户录制素材或信息卡承载；没有为了凑骚萌卡硬塞不贴文案的卡。
- 中段改为固定证据窗口，没有周期性 `crop_x` 左右晃。
- 总结卡使用 HyperFrames `card_motion_layer`。

- 新增素材 `/Users/fan/Documents/视频工厂/素材录制/最新素材/阿里云剪辑.mp4` 已用于 `seg12` 本地装配说明段。
- `captions_local_fix.srt` 已生成并对齐；本机 ffmpeg 缺少 `subtitles` filter，本轮未把字幕烧录进 MP4。

- `full_video_local_fix.mp4`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/full_video_local_fix.mp4`
