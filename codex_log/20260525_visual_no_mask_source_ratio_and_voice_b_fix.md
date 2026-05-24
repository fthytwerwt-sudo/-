# 20260525｜无遮挡源比例机制 + 新第四期 B 语音修复候选片

## 1. 本轮任务目标

本轮分两阶段串行执行：

1. 机制修补：写入 `source_native_no_mask_visual_rule（源素材比例 + 无遮挡视觉规则）`，取消用户录屏素材默认强制 `16:9 / 1920x1080`，禁止默认遮挡、洗白、灰色遮罩、黑块和整屏 privacy mask。
2. 成片修复：基于 locked v0.2 / preflight line_group 与上一轮诊断结果，重生成新第四期修复候选片，修复灰边 / 白屏 / 黑块和 TTS 未走 B 语音路线问题。

本轮未改 locked v0.2 文案语义，未覆盖旧失败成片，未提交媒体文件，未推进 `send_ready`。

## 2. route_decision

- project_route = video_factory
- task_type = mechanism_or_route_fix + video_sample_or_assembly + publish_candidate_delivery + tts_voice_route_fix + visual_artifact_fix
- responsibility_layer = mechanism_fix_layer + execution_layer + validation_layer + sync_layer
- selected_action = land_no_default_mask_source_ratio_rule_then_generate_visual_voice_fix_candidate
- forbidden_action = rewrite_locked_copy / overwrite_old_full_mp4 / default_masking / force_16_9 / use_Serena / local_tts_fallback / advance_send_ready
- large_task_gate = triggered
- lane_recommendation = standard_lane
- parallel_recommendation = serial_only
- deepseek_supply_gate = fallback_local_only
- not_deepseek_conclusion = true

## 3. state_action_router

- input_signal = 用户要求新增“无遮挡 + 源素材比例”视觉机制，并直接重生成新第四期语音 + 画面修复候选片。
- current_project_state = formal_operation_active；上一版 `full.mp4` 存在但用户反馈视觉失败、TTS 语音路线失败。
- selected_action = mechanism_landing + visual_artifact_fix + b_voice_route_fix + review_pack_generation
- done_when = 机制落库 + 新 `full.mp4` / `narration.wav` / `captions.srt` + B voice / B pacing 验证 + review pack + latest / paths 更新 + commit / push
- blocked_if = B voice route unavailable / provider only Serena / true secret visible and no user authorization / unable to generate no-mask source-ratio candidate

## 4. 影响面检查

- 当前分支：`main`
- 工作区状态：存在 unrelated dirty changes；本轮必须 path-limited staging，不得把无关改动一起提交。
- 上一轮失败成片目录存在：`dist/new_fourth_episode_selection_publish_candidate_20260525_001803/`
- 只读诊断目录存在：`codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/`
- locked v0.2 preflight 目录存在：`codex_log/script_preflight/新第四期_选品初筛_20260524_231118/`
- 新第四期素材目录存在：`/Users/fan/Documents/视频工厂/素材录制/新第四期`
- V001 / V003 / V004 均可读可解码。
- 旧问题确认：上一版视觉问题由最终装配 whiteout / privacy masks / padding bands 引入，源素材无同等灰边、白屏、黑块问题。
- 旧问题确认：上一版 TTS 实际为 `qwen3-tts-instruct-flash-realtime + Serena`，未走 B voice / B pacing。

## 5. 机制修补

已更新：

- `GPT数据源/05_文案路由规则.md`
  - 新增 `source_native_no_mask_visual_rule（源素材比例 + 无遮挡视觉规则）`
  - 明确用户录屏 / 桌面素材优先用源比例，不默认强制 `16:9 / 1920x1080`
  - 明确商品名、价格、佣金、月销、表格字段等默认不自动遮挡
- `GPT数据源/07_AI知识类视频价值规则.md`
  - 新增 `visual_evidence_must_remain_visible_rule（视觉证据必须可见规则）`
  - 明确商品卡、候选表、明细表、复查表、聊天框结论必须保持证据链可见
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
  - 将本轮用户素材交付口径改为 `source_native_ratio_or_user_provided_material_ratio`
- `codex_source/01_execution_rules.md`
  - 写入 `no_default_masking_without_user_authorization = true`
  - 写入 `no_default_16_9_for_user_recording = true`
  - 写入 `source_material_ratio_preferred = true`
  - 写入 `blocked_if_visual_evidence_unreadable = true`
- `codex_source/19_project_state_action_router.md`
  - 新增 `source_native_no_mask_visual_required`
  - 新增 `visual_evidence_unreadable_blocked`

## 6. 成片输出

- output_dir = `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/`
- full.mp4 = `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/full.mp4`
- narration.wav = `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/narration.wav`
- captions.srt = `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/captions.srt`

## 7. 画面修复摘要

- canvas_strategy = `source_native_or_primary_material_ratio`
- canvas = `3412x1846`
- source_material_ratio_used = true
- forced_16_9 = false
- forced_1920x1080 = false
- letterbox / pillarbox / padding_bands = false
- final_stage_whiteout = false
- full_frame_privacy_mask = false
- right_account_black_block = false
- edge_privacy_mask = false
- gray_dim_overlay = false
- subtitle_burn_in_used = false
- card_overlay_on_core_evidence_used = false

## 8. TTS 修复摘要

- provider = `aliyun_bailian`
- target_model = `qwen3-tts-vc-realtime-2026-01-15`
- custom_voice_masked = `qwen-t...ac19`
- voice_reference = `voice_sample2_cute_guide_voice_candidate_20260426`
- pacing_reference = `tts_15s_b_pacing_locked_20260427`
- used_b_voice = true
- used_b_pacing = true
- local_tts_fallback_used = false
- macos_say_used = false
- Serena used = false
- key_printed = false
- key_written = false
- key_committed = false

## 9. Review pack 文件清单

- `summary.json`
- `media_probe.json`
- `review_manifest.md`
- `publish_candidate_checklist.json`
- `visual_fix_report.json`
- `canvas_ratio_report.json`
- `mask_policy_report.json`
- `subtitle_card_overlap_check.json`
- `privacy_risk_check.json`
- `readability_check.json`
- `secret_leak_scan_sanitized.json`
- `narration_tts_debug_sanitized.json`
- `line_group_execution_map.json`
- `script_to_timeline_map.json`
- `content_route_card_v2.json`
- `tts_prosody_anchor_map.json`
- `card_placement_decision.json`
- `editing_decision_pack.json`
- `local_open_path_report.md`

## 10. 验证结果

- ffprobe = passed
- ffmpeg_decode = passed
- audio_present = true
- non_silent = true；`mean_volume = -15.8 dB`，`max_volume = -0.8 dB`
- subtitles_present = true；`mov_text` embedded subtitle + `captions.srt`
- subtitle_card_overlap = passed；未烧录字幕，不存在字幕 / 卡片遮挡核心素材
- gray_border_removed = true；未使用 padding / edge mask
- whiteout_removed = true；未使用 whiteout / full-frame mask；抽帧中高亮白色为源页面白底 UI，仍有文字 / 页面结构可读
- black_block_removed = true；未使用 right account black block
- secret_scan = passed；扫描范围为本轮生成文本 / JSON / Markdown / SRT / log，不包含视频 OCR
- media_committed = false

## 11. 状态边界

- publish_candidate_ready_for_human_review = true
- content_validation = pending_user_chatgpt_review
- send_ready = false
- voice_validation = pending_user_chatgpt_review
- visual_master_locked = false
- current_data_goal_anchor_ready = false
- video_generated = true
- audio_generated = true
- third_party_assets_copied = false
- locked_copy_semantics_changed = false

## 12. commit / push

- commit_message = `Fix visual masking policy and B voice route for new fourth episode candidate`
- commit_sha = final_response_reports_actual_sha
- pushed_to_main = final_response_reports_actual_result
