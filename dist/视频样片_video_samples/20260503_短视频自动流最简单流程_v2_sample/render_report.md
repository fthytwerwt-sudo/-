# 渲染报告 render_report

## 1. 任务结果

- `technical_validation`：`passed`
- `metadata_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `audio_validation`：`temporary_preview`
- `tts_validation`：`temporary_system_tts_preview`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 2. 输出文件

- full_video：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/full_video.mp4`
- captions：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/captions.srt`
- assembly_manifest：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/assembly_manifest.json`
- contact_sheet：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/contact_sheet.jpg`
- redaction_report：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/redaction_report.md`
- local_open_path_report：`/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/local_open_path_report.md`

## 3. ffprobe / decode

- exists：`True`
- file_size_bytes：`17201349`
- duration_seconds：`731.196`
- resolution：`720x1280`
- video_codec：`h264`
- audio_present：`true`
- audio_codec：`aac`
- audio_channels：`1`
- decodable：`true`

## 4. 脱敏与素材使用

- 火山引擎 API 特写：`not_used`
- fallback：`redaction_blocked_fallback_to_info_card`
- Codex 段遮挡：右侧分支详情 / 底部路径区域 / 顶部区域已加黑条遮挡。
- Trae 段遮挡：底部路径区域 / 顶部区域已加黑条遮挡。
- 豆包段遮挡：底部路径区域 / 顶部区域已加弱遮挡。

## 5. 敏感信息文本扫描

- scan_status：`passed`
- matched_files：`[]`
- notes：复扫范围为本轮可读交付文本和脚本，检查明文手机号、验证码、API Key 赋值、AccessKey 形态、token / secret 赋值和临时授权 URL 形态；未发现实际敏感值。文本中的敏感项名称仅作为脱敏规则说明出现。视觉层通过不使用火山原画面、遮挡敏感区域和 contact sheet 复审降低风险。

## 6. 时间线摘要

- segment_count：`16`
- 片段总时长以 mux 后 `full_video.mp4` 为准。

## 7. 状态边界

- 本轮生成 MP4 只代表技术样片存在。
- 技术验证通过不等于内容验证通过。
- 本轮不得把发送状态写成真值。
