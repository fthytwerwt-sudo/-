# 20260516｜正式运营用户反馈边界与禁止降级完成 user_feedback_boundary_and_no_degrade_completion

## 1. 本轮定位

- `task_type`: `mechanism_or_route_fix + project_file_change + user_feedback_boundary_repair + no_degrade_completion_gate + formal_operation_execution_accountability_repair`
- `current_stage`: `formal_operation_active`
- `operation_mode`: `data_driven_operation_iteration`
- `scope`: 只修正式运营协作分工、内部问题自修机制、完成状态口径和 blocked 停止线；不生成视频，不改素材，不调用媒体 / TTS / 生成 API。

## 2. 用户反馈分工修正

- `已确认` 正式运营阶段，用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格。
- `已确认` 用户不负责替 GPT / Codex 排查内部执行原因。
- `已确认` 当用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，GPT / Codex 必须自行触发 `self_repair_audit（自修审计）`。

## 3. GPT / Codex 自修责任

`self_repair_audit（自修审计）` 至少检查：

- locked_goal 是否被改变。
- locked_title 是否被改变。
- final_script 是否被 Codex 越权改写。
- script_to_timeline_map 是否逐句成立。
- subtitle / card 是否冲突。
- audio / TTS 是否达标。
- aspect_ratio 与 final_media_probe 是否达标。
- data_goal_alignment_check 是否真实检查。
- publish_candidate_checklist 是否真实通过。
- Git commit / push / sync 是否按任务完成。
- 是否存在降级冒充完成。

发现任一内部问题时，GPT / Codex 必须修复或 `blocked`，不得把诊断责任转给用户。

## 4. 禁止降级完成

- `已确认` Codex 后续不得降级处理正式运营任务。
- `已确认` 不能用技术预览、无声视频、比例错误视频、JSON / Markdown / route card、只读报告、局部文件、本地未同步产物、fallback 或临时替代冒充 `completed`。
- `已确认` 做不到仓库写明的目标、产物、验证、同步和回报时，必须 `blocked` 或继续修到满足基线。
- `已确认` 降级方案只能作为 `blocked` 后待用户确认的修复建议；未经用户明确授权，不得自行当作完成结果。

## 5. 状态边界

- `content_validation`: `not_advanced`
- `send_ready`: `not_advanced`
- `publish_status_success`: `not_advanced`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `not_advanced`
- `visual_master_locked`: `not_advanced`
- `data_flywheel_passed`: `not_advanced`
- `commercial_validation_passed`: `not_advanced`

## 6. 本轮未做

- 未生成视频。
- 未修改原始素材。
- 未修改 `dist/latest_review_pack/`。
- 未修改媒体文件。
- 未读取、打印、写入或提交 API key / token / secret。
- 未调用媒体生成、TTS、voice cloning 或外部 API。
- 未推进任何内容 / 发布 / 声音 / 视觉 / 商业验证状态。

## 7. DeepSeek 供料边界

- `deepseek_participation_report`: `fallback_local_only`
- `fallback_status`: `used_by_no_api_boundary`
- `not_deepseek_conclusion`: `true`
- `token_usage_expectation_check`: `token_usage_not_expected_this_round`
- `supply_request`: `codex_log/supply_requests/20260516_用户反馈边界与禁止降级完成_pre_supply_request.json`
- `reason`: 本轮是机制修补，且执行边界禁止额外 API 调用；因此不声称 DeepSeek 真实参与。

## 8. 下一个目标

后续用户只反馈目标、美观和结果是否合格；GPT / Codex 必须自行复盘内部执行问题，实打实完成仓库基线。做不到就 `blocked`，不得降级完成。
