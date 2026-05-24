# 20260524 新第四期选品初筛发布候选片 TTS 解阻生成日志

## 1. 本轮任务目标

- 继续上一轮 `blocked_publish_candidate_unavailable_remote_tts_authorization_missing` 的新第四期发布候选片任务。
- 安全加载现有阿里 / 百炼 TTS 授权，不打印、不写入、不提交任何 key / token / secret。
- 使用 locked v0.2 / preflight line_group、`script_to_timeline_map`、`content_route_card_v2`、`tts_prosody_anchor_map`、`editing_decision_pack` 生成完整 `publish_candidate_ready_for_human_review`。

## 2. route_decision

- `project_route = video_factory`
- `task_type = video_sample_or_assembly + publish_candidate_delivery + locked_copy_execution + review_pack_generation`
- `responsibility_layer = execution_layer + validation_layer + sync_layer`
- `large_task_gate = triggered`
- `lane_recommendation = serial_only`
- `parallel_recommendation = read_parallel_for_inspection_only`
- `deepseek_supply_gate = fallback_local_only`
- `not_deepseek_conclusion = true`
- `execution_permission = granted_after_required_reads_and_tts_auth_presence_check`

## 3. state_action_router

- `input_signal = 用户确认阿里欠费已处理，要求继续走阿里 TTS 路线，片子不能有任何降级处理`
- `current_project_state = formal_operation_active；formal_operation_delivery_baseline = publish_candidate_or_blocked`
- `selected_action = locked_copy_publish_candidate_generation`
- `forbidden_action = rewrite_copy / local_tts_fallback / macos_say / silent_preview / content_validation_pass / send_ready_true`
- `done_when = full.mp4 + narration.wav + captions.srt + review pack + logs + path index + commit push`

## 4. 影响面检查

- `branch = main`
- `preflight_dir_exists = true`
- `blocked_review_pack_exists = true`
- `V001 / V003 / V004 = readable_and_decodable`
- `V002 = not_used`
- `unrelated_dirty_changes = present`
- `staging_policy = path_limited_only`
- `dist/latest_review_pack = not_modified`
- `locked_copy_semantics = not_modified`

## 5. TTS 授权安全加载

- `process_env_DASHSCOPE_API_KEY_present = false`
- `process_env_ALIYUN_API_KEY_present = false`
- `auth_source = authorized_runtime_config`
- `DASHSCOPE_API_KEY_present_after_safe_load = true`
- `ALIYUN_API_KEY_present_after_safe_load = false`
- `api_key_printed = false`
- `api_key_written = false`
- `api_key_committed = false`
- `secret_file_committed = false`

## 6. TTS 生成状态

- `provider = aliyun_bailian`
- `api_route_family = aliyun_qwen_realtime_websocket`
- `model = qwen3-tts-instruct-flash-realtime`
- `voice = Serena`
- `local_tts_fallback_used = false`
- `macos_say_used = false`
- `silent_audio_fallback_used = false`
- `narration_path = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/narration.wav`
- `captions_path = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/captions.srt`
- `notes = 个别远端 websocket 分段出现超时 / reset 后，均使用同一阿里正式路线缩小分段重试成功；没有降级到本地 TTS。`

## 7. 成片与审片包

- `review_pack_dir = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/`
- `full_video_path = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4`
- `review_manifest = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/review_manifest.md`
- `summary_json = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/summary.json`
- `media_probe = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/media_probe.json`
- `publish_candidate_checklist = /Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/publish_candidate_checklist.json`

## 8. 素材使用

- `V001 used = 商品卡浏览 / 商品字段 / 选品页`
- `V003 used = 候选表 / 明细表 / 云盘表格`
- `V004 used = 3 个更窄方向 / 4 个复查商品 / 优先级表`
- `V002 used = false`
- `subtitle_execution = burned_group_level_subtitle_layer + sidecar_captions_srt`
- `privacy_redaction = strengthened_after_visual_spot_check`
- `readability = local_zoom + card_translation + human_review_required`

## 9. 验证结果

- `ffprobe = passed`
- `ffmpeg_decode = passed`
- `audio_present = true`
- `non_silent = true`
- `mean_volume = -15.5 dB`
- `max_volume = -0.9 dB`
- `subtitles_present = true`
- `subtitle_card_overlap = passed_for_human_review`
- `privacy_redaction = passed_for_human_review_after_strengthened_redaction`
- `secret_scan = passed`
- `local_tts_fallback_used = false`
- `macos_say_used = false`

## 10. 状态边界

- `publish_candidate_ready_for_human_review = true`
- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`
- `media_committed = false`
- `raw_material_committed = false`
- `full_video_committed = false`
- `narration_committed = false`

## 11. commit / push 信息

- `commit_message = Generate new fourth episode publish candidate with authorized TTS`
- `commit_sha = recorded_in_final_response`
- `push_target = origin/main`
- `media_commit_policy = only JSON / Markdown review-pack files and logs are staged; full.mp4 / narration.wav / captions.srt / working clips / overlays / TTS segments are local-only`
