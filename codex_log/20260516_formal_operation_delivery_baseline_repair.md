# 20260516｜正式运营交付基线修正 formal_operation_delivery_baseline_repair

## 1. 本轮定位

- `task_type`: `mechanism_or_route_fix + project_file_change + validation_gate_rewrite + delivery_boundary_rewrite + formal_operation_stop_line_repair`
- `current_stage`: `formal_operation_active`
- `operation_mode`: `data_driven_operation_iteration`
- `scope`: 只修正式运营交付口径、执行口径、验收口径和停止线；不生成视频，不修上一条视频，不生成新技术预览。

## 2. 核心修正

- `已确认` 正式运营阶段下，视频类交付任务默认必须收口到 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 或 `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`。
- `已确认` `technical_preview（技术预览）`、`technical_preview_candidate（技术预览候选）`、`preflight package（执行前补全包）`、`silent preview（无声预览）`、无音轨视频、横屏技术包、只交 JSON / Markdown / route card，只能作为 `internal_diagnostic_only（内部诊断产物）` 或 `historical_internal_diagnostic_only（历史内部诊断产物）`。
- `已确认` 技术预览不能写 `completed`、不能写内容推进、不能写视频执行完成、不能作为用户验收交付。
- `已确认` 做不到写进项目基线的能力，必须写 blocked / 不合格，而不是交一个技术预览。

## 3. 新增 / 补强状态

- `publish_candidate_required`
- `publish_candidate_blocked`
- `technical_preview_not_delivery`
- `formal_operation_delivery_blocked`
- `blocked_publish_candidate_unavailable`

## 4. 中间层边界

以下产物是进入视频执行前的必备条件，不是用户最终交付物：

- `content_route_card`
- `script_to_timeline_map`
- `tts_prosody_anchor_map`
- `editing_decision_pack`
- `assembly_decision_pack`
- `data_goal_alignment_check`

## 5. 上一轮 preview 记录处理

- `codex_log/20260516_second_episode_kpi_to_judgment_system_preflight.md` 已标记为 `historical_internal_diagnostic_only`。
- `dist/第二期KPI到判断系统预览_second_episode_kpi_to_judgment_system_preview/审片清单_review_manifest.md` 已标记为 `historical_internal_diagnostic_only`。
- 该 preview 暴露的问题不是“上一条视频失败”，而是仓库交付基线过低，曾允许技术预览错进正式运营内容链路。
- 本轮不删除 preview 包，不回写成失败视频，不把它作为以后视频交付样板。

## 6. 禁止状态检查

- `content_validation`: `not_advanced`
- `send_ready`: `not_advanced`
- `publish_status_success`: `not_advanced`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `not_advanced`
- `visual_master_locked`: `not_advanced`

## 7. 本轮未做

- 未生成视频。
- 未修改原始素材。
- 未修改 `dist/latest_review_pack/`。
- 未调用媒体生成、TTS、voice cloning 或外部 API。
- 未推进任何内容 / 发布 / 声音 / 视觉状态。

## 8. 下一个目标

重新判断第二期视频链路是否能生成真正 `publish_candidate（可发布候选片）`。若不能，必须返回 `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`，而不是再生成 `technical_preview（技术预览）`。
