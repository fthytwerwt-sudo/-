# failure_and_blocker_report

- result_status：blocked_full_reference_quality_video_not_completed
- primary_blocker：formal_generation_voiceover_timeout_and_visual_api_quota_blocked
- standalone_tts_retry_status：success
- standalone_tts_retry_audio：/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/tts_retry_20260503_attempt2/tts/formal_voiceover.mp3
- standalone_tts_retry_duration_seconds：742.848
- provider_failure_reason：aliyun_bailian_tts_request_failed
- provider_error：The read operation timed out
- visual_generation_blocker：AllocationQuota.FreeTierOnly
- generation_status：failed
- assembly_status：not_started

## Blocked If 对照

- 项目 TTS 不能生成完整音轨：`部分成立`，独立重提 TTS 已成功；但正式 generation 的 voiceover 状态仍 failed，未进入可 assembly 状态，因此仍 blocked。
- API 真人不能真实生成：命中，blocked。
- 云剪不能真实导出：由于 generation 未通过，未启动，blocked。
- 只能输出短片、降级片或拼装片：未输出，保持 blocked。
- 需要 macOS say：未使用。
- 需要本地 assembly fallback：未使用。
- 需要 host card 冒充 API 真人：未使用。

## PR #43 错误继承检查

- PR #43 145 秒压缩稿：未继承。
- PR #43 local assembly fallback：未继承。
- PR #43 macOS say 临时音轨：未继承。
- PR #43 host / info card 替代 API 真人：未继承。
