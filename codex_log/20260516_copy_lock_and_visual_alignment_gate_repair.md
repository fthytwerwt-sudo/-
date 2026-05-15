# 20260516｜锁定文案契约与逐句画面对齐闸门修补

## route_decision

- `project_route`: `video_factory`
- `task_type`: `mechanism_or_route_fix + project_file_change + copy_lock_contract_repair + script_visual_alignment_gate_repair + codex_authority_boundary_repair + self_repair_audit_trigger_repair`
- `current_stage`: `formal_operation_active（正式运营中）`
- `execution_permission`: `mechanism_repair_only`

## change_summary

本轮根据用户反馈修正以后默认视频执行机制，不修改已发布视频，不重新生成视频，不回炉当前片子。

已写入：

1. `locked_copy_contract（锁定文案契约）`：视频执行前必须锁定 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。
2. `codex_copy_authority_boundary（Codex 文案权限边界）`：Codex 是执行层，不得擅自改标题、选题、开头句、核心判断、人味表达、文案语义或视觉标题卡标题。
3. `copy_change_request_required（文案修改请求必需）`：Codex 认为标题太长、文案不适合剪辑、画面无法对应或 TTS 不适配时，必须输出 `copy_change_request` 或 blocked，不能自行改稿。
4. `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）`：`script_to_timeline_map` 必须按 `line_group` 逐句绑定口播、素材时间码、预期画面、允许画面、禁用画面、字幕、卡片和证据强度。
5. `subtitle_card_overlap_check（字幕卡片重叠检查）`：导出前必须检查口播字幕、标题卡、解释卡、总结卡、画面 OCR 和关键证据区域；high severity overlap 未修复必须 blocked。
6. `post_publish_no_rework_boundary（已发布视频不默认回炉边界）`：用户明确说视频已经发了 / 已发布时，当前视频进入运营样本与数据回流，不默认回炉修改。
7. `user_feedback_self_repair_audit（用户反馈触发自修审计）`：用户反馈标题被改、文案画面对不上、字幕乱、卡片挡画面、视频不顺或不合格时，GPT / Codex 必须自行复盘，不让用户承担内部排障。

## status_boundary

- `content_validation`: `not_advanced`
- `send_ready`: `false`
- `publish_status_success`: `not_advanced`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `false`
- `visual_master_locked`: `false`
- `data_flywheel_passed`: `not_claimed`
- `commercial_validation_passed`: `not_claimed`

## no_media_change

- 未修改已发布视频。
- 未修改第二期横屏候选片目录下的视频、字幕或音轨。
- 未修改 `dist/latest_review_pack/`。
- 未修改 `素材录制/`。
- 未修改当前运营数据记录或当前数据目标锚点。

## next_target

已发布视频继续等待数据反馈；以后新视频执行前必须先锁定文案契约，并完成逐句文案画面对齐与字幕卡片重叠检查。
