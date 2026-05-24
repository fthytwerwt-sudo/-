# 20260524｜项目内文案对标视频全方位解析

## 1. 本轮任务目标

`已确认` 本轮继续上一次 `blocked_reference_path_missing` 后的 reference 审计任务，改读项目内 `文案库`，只做文案、视觉、动态、音效、卡片、节奏和迁移规则解析，不写新第四期最终文案，不生成视频，不推进内容状态。

## 2. route_decision（路由判断）

```text
project_route = video_factory
task_type = reference_audit + copywriting_reference_extraction + visual_motion_audio_audit + project_file_change
selected_action = parse_project_internal_reference_video_and_sync_reports
forbidden_action = write_final_script / generate_video / copy_reference_assets / advance_status
large_task_gate.triggered = true
large_task_gate.reason = reference video is 416.74s and task requires copy + visual + motion + audio + card + pacing + logs
lane_recommendation = serial_only
parallel_recommendation = serial_only
write_owner = Codex Integrator only
read_only_lanes = local media probe + local visual audit
execution_permission = allowed_after_project_internal_reference_found
```

## 3. state_action_router（项目状态动作总控器）

```text
input_signal = 用户已将文案对标视频放到项目内文案库，要求继续解析并 push
current_project_state = formal_operation_active + reference_contract_needed + material_audit_needed
fact_source_arbitration.primary_source = /Users/fan/Documents/视频工厂 当前仓库文件 + 项目内文案库 reference
selected_action = reference_pack + reference_to_execution_contract + chatgpt_handoff_pack + latest + dated_log
forbidden_action = write_final_script / generate_video / copy_reference_assets / advance_content_status
current_status_boundary = content_validation not advanced; send_ready false; voice_validation not advanced; visual_master_locked false
blocked_if = path missing / no video / media unreadable / critical tools missing without fallback / source media staged / secret detected / push failed
```

## 4. 影响面检查

- `已确认` 原指定目录 `/Users/fan/Documents/视频工厂/文案库/文案对标` 不存在。
- `已确认` fallback 在 `/Users/fan/Documents/视频工厂/文案库` 找到主视频：`/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`。
- `已确认` 同目录包含 `喜欢 txt.txt` 与 `不喜欢.txt`，只作为 secondary text context。
- `已确认` 本轮影响 reference pack、Reference-to-Execution Contract、ChatGPT 后续新第四期长文案、Codex 后续视频执行参考。
- `已确认` 本轮不影响当前成片状态、数据目标锚点 ready、内容验证状态、可发送状态。
- `已确认` 当前工作区已有 unrelated dirty changes，后续必须 path-limited staging。

## 5. 对标文件清单

| file_id | relative_path | file_type | size_bytes | duration_seconds | modified_time | primary_candidate | deep_audit | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R001 | 文案库/文案对标.MP4 | video/mp4 | 373998641 | 416.740114 | 2026-05-24T21:12:50 | True | True | 唯一名称包含“文案对标”的视频文件；位于文案库；体积最大且时长最长；进入深度解析。 |
| R002 | 文案库/喜欢 txt.txt | text/plain | 65688 |  | 2026-04-13T22:13:21 | False | False | 同目录文案喜好文本，作为 secondary reference context；不当作主视频 transcript。 |
| R003 | 文案库/不喜欢.txt | text/plain | 16272 |  | 2026-04-13T23:36:19 | False | False | 同目录文案喜好文本，作为 secondary reference context；不当作主视频 transcript。 |

## 6. 解析方法

- `ffprobe` 读取媒体信息。
- `ffmpeg` 生成只读 contact sheet、关键帧、响度和静音段检测。
- 本地隔离区辅助图只用于审计，不提交。
- local OCR / ASR 不可用，因此 transcript 是 `partial_transcript`，由可见字幕、问题卡、同目录文本和时间线共同支撑。

## 7. 工具使用情况

- `ffprobe = available / used`
- `ffmpeg = available / used_with_non_monotonic_dts_warnings`
- `video-metadata-probe = used; default validation_status failed due DTS warning`
- `fallback_decode_check = passed_sample_video_and_audio_with_genpts`
- `local_asr = unavailable`
- `local_ocr = unavailable`
- `DeepSeek_supply_gate = not_called_external_api_forbidden`
- `fallback_status = fallback_local_only`
- `not_deepseek_conclusion = true`

## 8. 输出文件清单

- `codex_log/reference_audit/文案对标_20260524_215056/00_reference_inventory.md`
- `codex_log/reference_audit/文案对标_20260524_215056/00_reference_inventory.json`
- `codex_log/reference_audit/文案对标_20260524_215056/01_media_probe_report.md`
- `codex_log/reference_audit/文案对标_20260524_215056/02_scene_timeline_map.md`
- `codex_log/reference_audit/文案对标_20260524_215056/03_copy_transcript_and_structure.md`
- `codex_log/reference_audit/文案对标_20260524_215056/04_visual_style_audit.md`
- `codex_log/reference_audit/文案对标_20260524_215056/05_motion_efficiency_audit.md`
- `codex_log/reference_audit/文案对标_20260524_215056/06_audio_sfx_rhythm_audit.md`
- `codex_log/reference_audit/文案对标_20260524_215056/07_card_and_overlay_audit.md`
- `codex_log/reference_audit/文案对标_20260524_215056/08_editing_pacing_audit.md`
- `codex_log/reference_audit/文案对标_20260524_215056/09_reference_to_execution_contract.md`
- `codex_log/reference_audit/文案对标_20260524_215056/10_transferable_rules_for_video_factory.md`
- `codex_log/reference_audit/文案对标_20260524_215056/11_risk_and_non_transferable_parts.md`
- `codex_log/reference_audit/文案对标_20260524_215056/12_chatgpt_handoff_pack.md`
- `codex_log/reference_audit/文案对标_20260524_215056/manifest.json`

## 9. reference contract 摘要

- reference_anchor: `/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`
- effect_targets: 文案抓人、问题卡、三层对比、表格/文档高亮、判断卡、人话边界、低压行动。
- must_not_copy: 原始文案、人物、账号、平台 UI、BGM/SFX、字体、卡片皮肤、第三方文档和画面资产。

## 10. 可迁移规则摘要

- 开头：大字抓停留 + 具体问题。
- 中段：问题卡分段 + 字段高亮 + 三层对比。
- 结果：候选表 / 云盘表格 / 聊天框结论必须成为证明。
- 边界：AI 初筛不是最终选品，不代表商品一定能卖。

## 11. 不可迁移风险摘要

- 原视频是抖音界面录屏，平台 UI、账号、互动数据、人物肖像均不可复用。
- 原音轨/BGM/SFX 不可复用。
- 竖屏风格不能直接套到正式运营横屏 16:9。
- 表格/文档信息过密，照搬会造成字幕/字段不可读。

## 12. 状态边界

- `content_validation = not_advanced`
- `send_ready = false`
- `publish_candidate_ready_for_human_review = not_advanced`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor ready = not_advanced`
- `video_generated = false`
- `media_committed = false`
- `third_party_assets_copied = false`

## 13. 验证结果

- `file_exists_check = passed`
- `report_file_exists_check = passed`
- `manifest_coverage_check = passed`
- `media_commit_check = passed_no_media_files_in_report_dir_and_source_media_not_staged`
- `secret_scan = passed_sanitized_allowed_outputs_only`
- `status_promotion_check = passed_content_validation_not_advanced_send_ready_false`
- `git_diff_check = passed`

## 14. commit / push 信息

- commit_message: `Audit project reference video for copy, motion, audio, and visual rules`
- commit_sha: `to_be_reported_in_final_response`
- push_target: `origin main`
