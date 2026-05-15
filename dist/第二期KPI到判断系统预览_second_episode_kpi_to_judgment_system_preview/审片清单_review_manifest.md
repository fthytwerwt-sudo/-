# 第二期候选技术预览审片清单 review_manifest

## 0A. historical_internal_diagnostic_only

本审片清单按 20260516 正式运营交付基线修正后，仅作为 `historical_internal_diagnostic_only（历史内部诊断产物）` 保留。它不是 `publish_candidate（可发布候选片）`，不是正式运营视频交付物，不得作为以后视频交付样板。

## 定位

- `content_id`: `second_episode_kpi_to_judgment_system`
- `selected_topic`: 别再让 AI 给你 KPI 了，它真正该帮你判断下一步改哪。
- `status`: `historical_internal_diagnostic_only`
- `previous_status`: `technical_preview_candidate`
- `not_delivery`: `true`
- `not_publish_candidate`: `true`
- `content_validation`: `not_advanced`
- `send_ready`: `false`
- `formal_data_driven_execution_ready`: `false`

## 本地文件

- 候选口播稿：`候选口播稿_script_final_candidate.md`
- 内容路由卡：`内容路由卡_content_route_card_v2.json`
- 文案锚点提取：`文案锚点提取_script_anchor_extraction_function.json`
- 时间线映射：`文案到时间线映射_script_to_timeline_map.json`
- TTS 韵律锚点：`TTS韵律锚点_tts_prosody_anchor_map.json`
- 开头视觉钩子：`开头视觉钩子_opening_visual_hook_spec.json`
- 剪辑决策包：`剪辑决策包_editing_decision_pack.json`
- 装配决策包：`装配决策包_assembly_decision_pack.json`
- 数据目标对齐：`数据目标对齐检查_data_goal_alignment_check.json`
- 技术预览字幕：`技术预览字幕_preview_subtitles.ass`
- 技术预览：`技术预览_preview.mp4`（生成后本地查看）

## 素材证据

- video_1：`/Users/fan/Documents/视频工厂/素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4`
- video_2：`/Users/fan/Documents/视频工厂/素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4`
- 素材审计报告：`codex_log/material_audit/20260515_second_episode_material_detail_report.md`

## 审片重点

1. 前 0-5 秒是否能直接听懂/看懂“AI 给 KPI 没用”。
2. video_1 的“第一版不够 -> 第二版追问”是否清楚。
3. video_2 的指标分层和客资评分是否够支撑“判断系统”。
4. 总结卡是否只保留 4 个短句，没有变 dashboard。
5. 是否误写数据飞轮已跑通、V003 已完成复盘、已有有效客资或成交。

## 禁止状态

- 不推进 `content_validation`。
- 不推进 `send_ready`。
- 不推进 `publish_status_success`。
- 不推进 `voice_validation` / `final_voice_validated`。
- 不推进 `visual_master_locked`。
- 不覆盖 `dist/latest_review_pack/`。
