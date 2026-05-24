# 20260524｜文案对标逐字稿与话语口味补充解析

## 1. 本轮任务目标

继续 `codex_log/reference_audit/文案对标_20260524_215056/`，尝试提取 reference 视频逐字稿；在版权边界下不提交完整第三方逐字稿，输出话语口味、逐字表达机制、reference vs 新第四期差异和 ChatGPT 改稿接力包。

## 2. route_decision

```text
project_route = video_factory
task_type = reference_transcript_extraction + copy_taste_analysis + copy_granularity_alignment + project_file_change
selected_action = extract_local_transcript_if_possible_then_generate_copy_taste_reports
forbidden_action = write_final_script / generate_video / copy_reference_assets / commit_full_third_party_transcript / advance_status
large_task_gate.triggered = true
lane_recommendation = serial_only
write_owner = Codex Integrator only
execution_permission = allowed_with_transcript_commit_boundary
```

## 3. state_action_router

```text
input_signal = 用户要求继续文案对标，重点补逐字稿和话语口味差异
current_project_state = formal_operation_active + reference_pack_exists + copy_granularity_mixture_rule_active
selected_action = local_asr_probe + transcript_status_report + copy_taste_gap_analysis + chatgpt_handoff_pack
blocked_if = reference video missing / audio unreadable / external API required / full third-party transcript staged / push failed
```

## 4. 影响面检查

- `reference_video_exists = true`
- `previous_reference_audit_dir_exists = true`
- `audio_track_present = true`
- `unrelated_dirty_changes_present = true`
- `path_limited_staging_required = true`
- `FULL_TRANSCRIPT_COMMIT_ALLOWED = false`
- `content_validation = not_advanced`
- `send_ready = false`

## 5. ASR / OCR 工具检查

- `ffmpeg = available`
- `ffprobe = available`
- `whisper / whisper-cpp / faster_whisper / mlx_whisper / funasr / vosk = missing`
- `tesseract / pytesseract / cv2 = missing`
- `external_api_called = false`
- `deepseek_supply_gate = not_called_external_api_forbidden`
- `fallback_status = fallback_local_only`

## 6. 逐字稿生成状态

- `audio_extract_status = passed`
- `audio_local_only_path = /Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/reference_audio.wav`
- `transcript_status = blocked_local_asr_missing`
- `full_transcript_generated = false`
- `full_transcript_local_path = not_generated`
- `transcript_blocked_report = /Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/transcript_blocked_report.md`

## 7. 仓库安全报告清单

- `codex_log/reference_audit/文案对标_20260524_215056/13_transcript_extraction_report.md`
- `codex_log/reference_audit/文案对标_20260524_215056/14_line_level_copy_taste_analysis.md`
- `codex_log/reference_audit/文案对标_20260524_215056/15_reference_vs_new_fourth_copy_gap.md`
- `codex_log/reference_audit/文案对标_20260524_215056/16_transcript_driven_chatgpt_handoff_pack.md`

## 8. 话语口味关键发现

- reference 不是先讲系统，而是先讲具体问题。
- 过渡句顺口，高光句绑定画面字段。
- 判断句短，通常由问题卡、对比卡或主持人回脸承接。
- 细节集中出现在表格、文档、模式对比画面中。
- 结尾低压，不把 AI 写成万能或自动赚钱。

## 9. 新第四期改稿方向

- 开头先讲“乱翻商品卡 -> 复查表”，不要先讲 Codex 能力。
- 表格出现时讲字段，不要提前平铺字段。
- 聊天框结论要讲理由、风险、下一步。
- 判断卡必须明确 AI 初筛不是最终选品。
- 顺口句和颗粒度句要按功能分配。

## 10. 禁止照搬清单

- 不提交完整第三方逐字稿。
- 不照搬原文案、标题、人物、账号、BGM/SFX、字体、卡片皮肤、平台 UI 和第三方文档。
- 不把 reference 的能力承诺平移到新第四期。

## 11. 状态边界

- `content_validation = not_advanced`
- `send_ready = false`
- `publish_candidate_ready_for_human_review = not_advanced`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `video_generated = false`
- `media_committed = false`
- `full_transcript_committed = false`

## 12. 验证结果

- `local_audio_extract_check = passed`
- `asr_tool_check = passed_missing_detected`
- `report_exists_check = passed`
- `media_commit_check = passed_no_video_audio_image_staged`
- `transcript_commit_boundary_check = passed_full_transcript_not_generated_and_not_committed`
- `secret_scan = passed_sanitized_allowed_outputs_only`
- `status_promotion_check = passed_content_validation_not_advanced_send_ready_false`
- `git_diff_check = passed`

## 13. commit / push 信息

- commit_message: `Add transcript-driven copy taste analysis for reference video`
- commit_sha: `to_be_reported_in_final_response`
- push_target: `origin main`
