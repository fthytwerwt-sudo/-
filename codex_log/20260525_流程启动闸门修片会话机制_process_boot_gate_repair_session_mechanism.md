# 20260525｜流程启动闸门 + 发片清单 + 修片会话卡机制补强

## route_decision

- `project_route = video_factory`
- `task_type = mechanism_or_route_fix + project_file_change + validation_layer_sync`
- `responsibility_layer = entry_routing_layer + execution_layer + validation_layer + reporting_layer + mechanism_fix_layer`
- `large_task_gate = triggered`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`
- `write_owner = Codex Integrator only`

## impact_check

- `must_update_files`：`codex_source/00_codex_readme.md`、`codex_source/19_project_state_action_router.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`codex_source/fixtures/mechanism_inference_function_cases.json`、`codex_log/latest.md`
- `should_update_files`：本 dated log、DeepSeek supply request
- `must_not_update_files`：`dist/` 媒体产物、原始素材、locked 文案语义、已发布视频事实字段、API key / token / secret、`content_validation / send_ready / voice_validation / visual_master_locked / current_data_goal_anchor_ready`
- `existing_overlap_rules`：已有 `route_decision`、`state_action_router`、`Completion Relay Gate`、`material_evidence_gate`、`script_to_timeline_map`、`tts_prosody_anchor_map`、`data_goal_alignment_check`
- `conflict_resolution`：本轮不另起平行系统，只把三层机制接到 `route_decision -> state_action_router -> Completion Relay Gate`

## mechanism_added

### process_boot_gate

后续命中视频执行、修片、发片候选、重新生成、发布前修复、最终文案进入视频，或命中 TTS / 字幕 / 卡片 / 时间线 / 审片包 / 视觉证据任务时，Codex 必须先读取完整流程入口并输出 `process_boot_report（流程启动报告）`。

`GPT prompt` 只代表 `prompt_delta（本轮增量目标）`，不得作为完整流程唯一依据。prompt 没写到的默认组件必须按仓库流程继续判断。

### publish_candidate_required_inventory

发片候选、修片、视频执行、重新生成、发布前修复默认必查：

- `locked_copy_contract`
- `content_route_card_v2`
- `card_placement_decision`
- `script_to_timeline_map`
- `tts_prosody_anchor_map`
- `visual_evidence_check`
- `subtitle_card_overlap_check`
- `publish_candidate_checklist`
- `data_goal_alignment_check`
- `review_pack`
- `remaining_blockers`

不适用必须写 `not_applicable_reason`；需要但缺失时必须 `blocked` 或 `continue`，不得 `completed`。

### current_repair_session

修片 / 既有候选片重生成前必须读或创建状态卡，字段至少包含目标候选片、锁定目标、已知问题、本轮唯一主修问题、允许 / 禁止改动、验证项、完成态和剩余阻断。若上一轮状态不可恢复，必须 blocked，不得从 prompt 猜。

## validation_scope

- 本轮不生成视频。
- 本轮不推进内容状态。
- 本轮不推进发送、声音、视觉母版或当前数据目标锚点 ready。
- 本轮机制写入不等于长期稳定验证。

## next_target

下一轮真实视频 / 修片任务必须先输出 `process_boot_report`，再生成 `publish_candidate_required_inventory`；若是修片任务，还必须先读或创建 `current_repair_session`。验证重点是 prompt 缺组件时是否仍触发组件判断、清单缺项时是否阻断完成态、修片状态是否能跨轮延续。
