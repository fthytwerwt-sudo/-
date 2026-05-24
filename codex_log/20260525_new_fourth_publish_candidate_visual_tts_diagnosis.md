# 20260525｜新第四期成片视觉 / TTS 路线只读诊断

## 本轮任务目标

只读诊断 `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4` 的视觉灰边 / 白屏 / 黑块和 TTS B 语音不符问题。不修复、不重渲染、不重新生成 TTS。

## route_decision

- project_route: video_factory
- task_type: review_diagnosis_audit + visual_artifact_diagnosis + tts_voice_route_diagnosis
- responsibility_layer: validation_layer + sync_layer
- selected_action: read_only_publish_candidate_visual_tts_diagnosis
- forbidden_action: repair / rerender / regenerate_tts / modify_locked_script / advance_status
- large_task_gate: triggered
- lane_recommendation: audit_lane / serial_only
- deepseek_supply_gate: fallback_local_only

## 影响面检查

- full.mp4 exists: true
- narration.wav exists: true
- captions.srt exists: true
- review pack exists: true
- source material check: V001 / V003 / V004 同类时间段没有 final 中的大面积主体白屏。
- unrelated dirty changes: present; 本轮采用 path-limited staging。

## 读取文件清单

- AGENTS.md
- codex_log/latest.md
- codex_source/00_codex_readme.md
- codex_source/01_execution_rules.md
- GPT数据源/04_选题与文案规则.md
- GPT数据源/05_文案路由规则.md
- GPT数据源/07_AI知识类视频价值规则.md
- codex_log/current_local_artifact_paths.md
- dist/new_fourth_episode_selection_publish_candidate_20260525_001803/review pack JSON/MD
- codex_log/script_preflight/新第四期_选品初筛_20260524_231118/TTS、卡片、剪辑、隐私前置文件
- codex_source/locked_reference_registry.md

## 视觉诊断结论

- gray_border_origin: privacy edge masks + canvas / edge padding bands
- whiteout_origin: final-stage strengthened redaction / whiteout privacy mask
- black_block_origin: right account/sidebar privacy mask
- source_material_has_issue: false for reported large whiteout pattern
- render_pipeline_added_issue: true

关键证据：`visual_no_audio.mp4` 和 `visual_with_captions.mp4` 在多个对应时间点仍能读到商品卡 / 表格结构；最终 `full.mp4` 额外出现大面积洗白、右上角黑块和边缘灰层。`privacy_risk_check.json` 记录字段已 masked or washed out，与抽帧结果一致。

## TTS 诊断结论

- provider: aliyun_bailian
- actual_model: qwen3-tts-instruct-flash-realtime
- actual_voice: Serena
- expected_b_voice_route: qwen3-tts-vc-realtime-2026-01-15 + qwen-t...ac19 + B 版停顿梗感节奏参考
- used_b_voice: false
- used_b_pacing: false
- mismatch_origin: wrong_model + missing_voice_reference + missing_pacing_reference + provider_route_bypassed_voice_clone

## 输出文件清单

- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/00_diagnostic_summary.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/01_visual_artifact_frame_index.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/02_visual_artifact_root_cause.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/03_redaction_overlay_audit.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/04_canvas_crop_padding_audit.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/05_subtitle_card_layer_audit.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/06_tts_actual_route_audit.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/07_tts_b_voice_mismatch_root_cause.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/08_minimal_fix_plan.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/09_do_not_fix_yet.md`
- `/Users/fan/Documents/视频工厂/codex_log/diagnostics/new_fourth_publish_candidate_visual_tts_audit_20260525_010732/manifest.json`

## 最小修复建议

先修视觉遮挡 / 灰边 / 白屏根因，再修 TTS B 语音路线。视觉层需要把大面积 whiteout 改为局部 blur / mask，并保留商品卡与表格结构可读性；TTS 层需要切到自定义 voice candidate + B pacing reference，而不是 `Serena` 普通 realtime voice。

## 状态边界

- video_regenerated: false
- tts_regenerated: false
- content_validation: pending_user_chatgpt_review
- send_ready: false
- voice_validation: failed_user_feedback
- visual_master_locked: false

## 验证结果

- artifact_exists_check: passed
- frame_extraction_check: passed
- source_vs_final_comparison: passed
- tts_route_check: passed
- report_exists_check: passed
- media_commit_check: passed_after_path_limited_staging_check
- secret_scan: passed
- git_diff_check: passed

## commit / push 信息

本轮采用 path-limited staging；最终 commit_sha / push 结果以最终回报为准。
