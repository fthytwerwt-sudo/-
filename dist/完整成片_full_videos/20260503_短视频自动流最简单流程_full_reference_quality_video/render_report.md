# render_report

- result_status：blocked_full_reference_quality_video_not_completed
- video_type：full_reference_quality_video
- generation_status：failed
- technical_validation：blocked
- content_precheck_for_reference_quality：blocked
- content_validation：pending_user_chatgpt_review
- send_ready：false
- full_video.mp4：未生成
- formal_chain_used：generate_formal_api_demo.py 已真实执行；assemble_formal_api_demo.py 未执行，因为 generation 未通过
- local_assembly_fallback_used：false
- macos_say_used：false

## 已确认

- 正式 case 已创建：/Users/fan/Documents/视频工厂/cases/短视频自动流最简单流程_full_reference_quality_video.md
- 完整 FINAL_SCRIPT_V2 已写入 case、文案库和 runtime_full_script.md。
- `compressed_runtime_used = false`，`pr43_compressed_script_reused = false`。
- 按用户最新要求重新提取项目 TTS 后，独立完整 TTS 音轨已生成并可解码：/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/tts_retry_20260503_attempt2/tts/formal_voiceover.mp3
- TTS 重提音轨时长：742.848 秒。
- 用户录制素材已按时间码进入 formal manifest 的 visual assets 准备阶段。
- PR #43 的 145 秒压缩稿、macOS say、本地 assembly fallback、host card fallback 均未继承。

## 阻断

- `部分成立` 项目 TTS 已可独立生成完整音轨；但重新执行正式 `generate_formal_api_demo.py` 时，主 generation 的 voiceover 步骤仍返回：`The read operation timed out`。
- visual / API 生成仍被远端额度状态阻断，错误族为：`AllocationQuota.FreeTierOnly`。
- 因正式 generation 未通过，API 真人不能完成真实入片，正式云剪 assembly 不允许启动。
