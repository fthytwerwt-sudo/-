# tts_generation_report

- status：partial_success_standalone_tts_extracted_generation_voiceover_blocked
- provider：aliyun_bailian
- api_route_family：aliyun_bailian_cosyvoice
- model：cosyvoice-v2
- voice_desensitized_hash：2954ab7e83
- full_script_used：true
- compressed_runtime_used：false
- reference_script_used_for_tts：true
- reference_script_used_for_captions：true
- standalone_tts_retry_status：success
- standalone_tts_retry_audio：/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/tts_retry_20260503_attempt2/tts/formal_voiceover.mp3
- duration_seconds：742.848
- audio_validation：passed_ffprobe_audio_only_mp3_24000hz_mono
- main_generation_tts_probe_status：success
- main_generation_voiceover_status：failed
- main_generation_voiceover_error：The read operation timed out
- entered_assembly：false
- macos_say_used：false
- pr43_temporary_audio_reused：false

## 结论

`已确认` 本轮已重新提取项目正式 TTS，完整音轨生成成功并可解码，时长 742.848 秒。

`部分成立` 该成功音轨来自正式 TTS 配置和 `formal_api_demo_core.py` 的 TTS 执行逻辑；但随后重新跑 `scripts/generate_formal_api_demo.py` 时，主 generation 的 voiceover 步骤仍因远端读取超时失败，manifest 未形成可进入 assembly 的完整 voiceover 状态。

因此本轮仍必须 blocked，不能用 macOS say、静音、旧 PR #43 临时音轨或部分音频替代，也不能进入云剪总装。
