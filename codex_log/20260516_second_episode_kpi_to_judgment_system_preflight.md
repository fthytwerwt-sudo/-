# 20260516｜第二期候选视频《从 KPI 到判断系统》执行前补全

## 1. 本轮定位

- `content_id`: `second_episode_kpi_to_judgment_system`
- `selected_topic`: 别再让 AI 给你 KPI 了，它真正该帮你判断下一步改哪。
- `task_type`: `content_route_needed + material_based_copy_preparation + video_execution_preflight + technical_preview_candidate`
- `current_stage`: `formal_operation_active`
- `current_data_goal_anchor_status`: `partial_data_recorded`
- `formal_data_driven_execution_ready`: `false`

本轮只生成候选执行包和本地技术预览 / 审片包，用于 ChatGPT / 用户复审。它不是正式发布成片，不是 `send_ready`，不是 `content_validation passed`，也不是正式下一条视频执行完成。

## 2. 输入依据

- 素材审计报告：`codex_log/material_audit/20260515_second_episode_material_detail_report.md`
- 当前运营目标：`codex_log/current_operation_target.md`
- 当前数据目标锚点：`codex_log/current_data_goal_anchor.md`
- 素材目录：`/Users/fan/Documents/视频工厂/素材录制/第二期`
- video_1：`/Users/fan/Documents/视频工厂/素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4`
- video_2：`/Users/fan/Documents/视频工厂/素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4`

技术复核：

- video_1：存在，可解码，102.50 秒，3338x1644，30fps，H.264，无音轨。
- video_2：存在，可解码，119.03 秒，3248x1626，30fps，H.264，无音轨。
- 素材不包含真实平台后台数据。
- 素材不包含真实有效客资 / 成交数据。
- video_2 的 `video_goal_card` 只露出模板开头，不能写完整模板已录全。

## 3. 本轮生成文件

审片包目录：

`dist/第二期KPI到判断系统预览_second_episode_kpi_to_judgment_system_preview/`

核心文件：

- `候选口播稿_script_final_candidate.md`
- `内容路由卡_content_route_card_v2.json`
- `文案锚点提取_script_anchor_extraction_function.json`
- `文案到时间线映射_script_to_timeline_map.json`
- `TTS韵律锚点_tts_prosody_anchor_map.json`
- `开头视觉钩子_opening_visual_hook_spec.json`
- `剪辑决策包_editing_decision_pack.json`
- `装配决策包_assembly_decision_pack.json`
- `数据目标对齐检查_data_goal_alignment_check.json`
- `执行包总览_execution_package_summary.md`
- `审片清单_review_manifest.md`
- `技术预览字幕_preview_subtitles.ass`
- `技术预览_preview.mp4`

技术预览验证：

- `duration_seconds`: 82.00
- `resolution`: 1280x720
- `fps`: 15
- `video_codec`: h264
- `audio_present`: false
- `decodable`: true
- `validation_status`: passed

说明：本轮没有生成 TTS，`TTS韵律锚点_tts_prosody_anchor_map.json` 只用于后续声音执行前判断。

## 4. 执行判断

本轮内容路由：

- 开头路线：`screen_first_opening + direct_question_title_card overlay`
- 主体承载：用户录制素材先行，video_1 做过程证据，video_2 做结果证据。
- 总结卡：`judgment_card`，只保留四句短句。
- API 生成人物：不使用；缺 API 人物不阻断本轮。
- Prompt 尾卡：仅作为可选低压引用，不进入本轮技术预览主叙事。

数据目标对齐：

- 使用锚点：`codex_log/current_data_goal_anchor.md`
- 主变量：`opening_route_or_first_5s_packaging`
- 协同变量：`evidence_compression`、`result_diff_display`
- 发布后观察指标：`2s_bounce`、`5s_completion`、`3s_retention_if_available`、`average_watch_time`
- 当前状态：只允许作为候选技术预览，不得写正式数据驱动执行 ready。

## 5. 禁止状态检查

- `content_validation`: not_advanced
- `send_ready`: not_advanced
- `publish_status_success`: not_advanced
- `voice_validation`: not_advanced
- `final_voice_validated`: not_advanced
- `visual_master_locked`: not_advanced

## 6. 禁止误写

- 不得写数据飞轮已跑通。
- 不得写 V003 已完成 72h / 7d 复盘。
- 不得写当前已有有效客资或成交。
- 不得写素材里出现真实平台后台数据。
- 不得写完整 `video_goal_card` 已录全。
- 不得写本轮 DeepSeek 真实参与。
- 不得把技术预览写成可发布成片。

## 7. 下一个目标

ChatGPT / 用户复审候选脚本、开头路线、剪辑节奏和技术预览；通过后再决定是否进入正式视频执行或继续局部修正。
