# 20260524｜新第四期选品初筛发布候选生成阻断

## 1. 本轮目标
基于 `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/` 和用户锁定的 v0.2 长文案，生成完整 `publish_candidate_ready_for_human_review`。

## 2. route_decision
- project_route = video_factory
- task_type = video_sample_or_assembly + publish_candidate_delivery + locked_copy_execution + review_pack_generation
- large_task_gate = triggered
- lane_recommendation = serial_only
- deepseek_supply_gate = fallback_local_only；not_deepseek_conclusion = true

## 3. state_action_router
- input_signal = 用户要求按 locked v0.2 文案直接生成发布候选成片
- selected_action = publish_candidate_delivery_if_all_hard_gates_pass
- blocked_action = technical_preview / silent_preview / macos_say_preview / local_tts_fallback_preview
- final_state = blocked_publish_candidate_unavailable_remote_tts_authorization_missing

## 4. 影响面检查
- branch = main
- unrelated_dirty_changes = present；后续只允许 path-limited staging
- preflight_output_dir_exists = true
- locked_copy_contract_candidate_exists = true
- script_to_timeline_map_json_parse = passed
- content_route_card_v2_json_parse = passed
- tts_prosody_anchor_map_json_parse = passed
- material_dir_exists = true
- V001 / V003 / V004 decodable = true
- TTS authorization = unavailable under current constraints
- privacy_risk = high_if_rendered，需要遮挡 Drive、路径、商品、价格、佣金、月销、店铺信息
- readability_risk = high_if_rendered，需要局部放大 / 卡片转译

## 5. 素材检查
- V001: `/Users/fan/Documents/视频工厂/素材录制/新第四期/内建视网膜显示器 2026-05-23 20-57-41.mp4`；duration = 481.667s；audio_present = false；decodable = true
- V003: `/Users/fan/Documents/视频工厂/素材录制/新第四期/内建视网膜显示器 2026-05-23 22-44-33.mp4`；duration = 96.333s；audio_present = false；decodable = true
- V004: `/Users/fan/Documents/视频工厂/素材录制/新第四期/内建视网膜显示器 2026-05-23 22-51-40.mp4`；duration = 50.2s；audio_present = false；decodable = true
- V002: `/Users/fan/Documents/视频工厂/素材录制/新第四期/内建视网膜显示器 2026-05-23 21-28-53.mp4`；duration = 12.5s；audio_present = false；decodable = true；默认不入正片

## 6. TTS 授权检查
- required_provider = aliyun_bailian / qwen3-tts-vc-realtime-2026-01-15
- DASHSCOPE_API_KEY_present = false
- ALIYUN_API_KEY_present = false
- authorized_runtime_config_exists = true
- authorized_runtime_config_read = false
- reason = 本轮禁止读取 / 打印 / 写入 API key / token / secret；不能读取本地 runtime 授权文件
- macos_say_used = false
- local_tts_fallback_used = false
- silent_audio_fallback_used = false

## 7. 输出文件清单
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/summary.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/media_probe.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/review_manifest.md`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/publish_candidate_checklist.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/locked_copy_contract.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/line_group_execution_map.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/script_to_timeline_map.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/tts_prosody_anchor_map.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/content_route_card_v2.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/card_placement_decision.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/editing_decision_pack.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/privacy_risk_check.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/readability_check.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/subtitle_card_overlap_check.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/platform_risk_precheck.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/narration_tts_debug_sanitized.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/secret_leak_scan_sanitized.json`
- `dist/new_fourth_episode_selection_publish_candidate_20260524_233231/local_open_path_report.md`

## 8. 状态边界
- publish_candidate_ready_for_human_review = false
- content_validation = not_advanced_due_blocked
- send_ready = false
- voice_validation = not_advanced_due_blocked
- visual_master_locked = false
- current_data_goal_anchor_ready = false
- video_generated = false
- audio_generated = false
- media_committed = false

## 9. 验证结果
- file_exists_check = passed；阻断审计包 18 个文本 / JSON / Markdown 文件均存在
- json_parse_check = passed；输出目录内所有 JSON 均可解析
- media_probe_check = passed_for_source_materials
- tts_authorization_check = blocked；`DASHSCOPE_API_KEY_present = false`、`ALIYUN_API_KEY_present = false`，且本轮未读取本地 runtime secret
- no_degrade_check = passed；未生成无声预览、未使用 macOS say、未使用本地低质 TTS fallback
- generated_media_check = passed；本轮输出目录没有生成 `full.mp4`、`narration.wav`、`captions.srt` 或图片
- secret_scan = passed_for_new_outputs；未写入真实 API key / token / secret
- latest_top_check = passed
- current_local_artifact_paths_check = passed；已登记阻断审计包路径，不登记不存在的 full.mp4 为可打开成片
- media_commit_check = pending_final_git_verification
- git_diff_check = passed

## 10. commit / push
- commit_message = Generate new fourth episode selection publish candidate review pack
- commit_sha = pending
- pushed_to_main = pending
