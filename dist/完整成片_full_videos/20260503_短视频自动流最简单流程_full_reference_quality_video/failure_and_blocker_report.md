# failure_and_blocker_report

## 20260504 本地参考修正版状态

- latest_user_requested_fix：`local_reference_quality_fix`
- local_fix_result_status：`local_reference_fix_completed`
- local_fix_blocked：`false`
- true_blocker：`none`
- blocked_stage：`none`
- custom_voice_reference：`qwen-t...ac19`
- re_enrolled_voice_used：`qwen-t...af51`
- target_model：`qwen3-tts-vc-realtime-2026-01-15`
- tts_15s_b_pacing_locked_20260427_read：`true`
- reference_voice_or_pacing_used_for_tts：`true`
- voice_validation：`pending_user_chatgpt_review`
- final_voice_validated：`false`
- cloud_assembly_used_this_round：`false`
- local_assembly_started_this_round：`true`
- macos_say_used：`false`
- old_tts_fallback_used：`false`
- full_video_local_fix_generated：`true`
- full_video_local_fix_path：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/full_video_local_fix.mp4`
- element_doll_after_opening_present：`false`
- sassy_cards_checked：`true`
- summary_card_hyperframes_used：`true`
- middle_dynamic_crop_x_removed：`true`
- subtitle_burn_in：`false`
- subtitle_burn_in_note：`本机 ffmpeg 缺少 subtitles filter，本轮生成并对齐 captions_local_fix.srt，未烧录进 MP4。`
- content_validation：`pending_user_chatgpt_review`
- send_ready：`false`

`已确认` 用户本轮要求“声音硬门优先”。早前 `qwen-t...ac19` 直接合成曾出现 WebSocket 异常；随后已按用户确认的 `qwen3-tts-vc-realtime-2026-01-15` 路径重新尝试，并从 `语音样本 2.MP4` 复刻出同一参考底子的可用声音 `qwen-t...af51`。完整 TTS 已生成并进入本地装配；本轮没有使用旧 TTS、macOS `say`、阿里云剪辑 / ICE / OSS，也没有交残片冒充完成。

## 20260503 云剪完整片历史状态

- result_status：full_reference_quality_video_completed_cloud_exported
- blocked：false
- true_blockers：[]
- previous_tts_timeout_resolved：true
- previous_visual_api_quota_not_carried_as_element_doll_blocker：true
- project_tts_audio_generated：true
- formal_generation_voiceover_ingestion：success_local_voiceover_path
- element_doll_host_reference_inheritance：success
- card_local_rendering_or_reference_inheritance：success
- new_pdf_or_image_api_generation_required：false
- generation_status：success
- cloud_assembly_status：success
- full_video_generated：true
- full_video_path：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/full_video.mp4`
- middle_zoom_reference_validation：passed_final_cloud_video_checked
- summary_card_validation：passed_cute_info_card_route
- sassy_reaction_card_validation：reference_read_not_used
- hyperframes_motion_validation：not_used_checked_no_boundary_violation
- content_validation：pending_user_chatgpt_review
- send_ready：false

没有把已解决的 TTS 超时或 liveportrait quota 继续写成 blocker；也没有把未使用的骚萌卡 / HyperFrames 误写成已入片。内容仍待用户 / ChatGPT 复审。

## 2026-05-04 local_reference_quality_fix_v2

- `status`：`completed`
- `cloud_assembly_used`：`false`
- `local_assembly_used`：`true`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- 用户反馈的中段左右晃和粉色背景不对称已进入 v2 本地修复证据包。
- `full_video_local_fix_v2`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality_v2/full_video_local_fix_v2.mp4`
