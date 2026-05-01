# AI 做 PPT 踩坑成品候选 v3 审片入口

`已确认` 本包是 `finished_quality_candidate_v3（成品质量候选片 v3）` 与 `visual_master_candidate_v3（视觉母版候选 v3）`。

`已确认` 用户已完成 v3 复审：v3 技术层只能写为 `v3_technical_milestone = reached_for_current_stage（当前阶段技术里程碑达成）`，不能写成技术线最终锁定；下一步仍需 `technical_upgrade_next = true（技术升级）`。

`已确认` v3 内容层没有过线，主要问题在 GPT 文案侧；本包必须使用用户复审后的未过线口径，不能沿用旧待复审口径或写成内容通过。

## 先看文件

1. `AI做PPT踩坑_成品候选_v3_full.mp4`：v3 完整成品候选片。
2. `AI做PPT踩坑_成品候选_v3_contact_sheet.jpg`：全片关键帧联系表。
3. `locked_reference_inheritance_report.md`：锁定参考继承报告。
4. `video_metadata_probe_report.json`：video-metadata-probe 检查报告 JSON。
5. `AI做PPT踩坑_成品候选_v3_summary.json`：状态摘要。
6. `AI做PPT踩坑_成品候选_v3_timeline.json`：时间线。
7. `AI做PPT踩坑_成品候选_v3_cut_map.md`：镜头说明。

## 当前边界

- `v3_technical_milestone = reached_for_current_stage`
- `technical_baseline_locked = false`
- `technical_upgrade_next = true`
- `content_validation = not_passed_user_review_gpt_copywriting_side`
- `send_ready = false`
- `subtitle_enabled = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `visual_master_candidate = true`，但 `visual_master_locked = false`。
- `sassy_card_execution_reference_next = PR7_B_骚萌反应页.png`
- `v31_visual_route_map_required_before_generation = true`

## 本轮重点

- 保留“反面结果露馅 -> 方法词出现 -> 字段拆解 -> 正面操作 -> 结果预览 -> 边界收束”的节奏。
- 保留正反录屏素材事实，以真实录屏作为中段主体。
- 保留核心方法词：`可交付初稿`。
- 使用 custom voice TTS 入片，但声音仍待用户 / ChatGPT 听感复审。
- 下一轮 v3.1 生成前必须先输出并验证 `visual_route_map.json（视觉路由表）`，不得继续让段落提示卡、信息卡、骚萌卡共用同一套外壳。

## 本地路径

- 复审包：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3`
- full video：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/AI做PPT踩坑_成品候选_v3_full.mp4`
- duration_seconds：`150.002`
- resolution：`720x1280`
- audio_codec：`aac`
