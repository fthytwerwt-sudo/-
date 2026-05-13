# 20260514｜卡片位置路由机制修补日志

## 1. 本轮目标

`已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的卡片位置路由机制补全。

目标是把“总结卡 / 反转卡固定出现在某个 shot、某个段落、某个旧 reference 位置”的旧理解修正为：

- 总结卡、反转卡、结果差卡和 Prompt 尾卡是文案功能卡。
- 卡片职责可以稳定，卡片位置必须由最终文案、素材证据、结果差、转折点和观众理解路径判断。
- Codex 不得先固定卡片位置，再把文案塞进去。
- 卡片不得抢中段真实录屏证据。

## 2. route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - project_file_change
    - mechanism_or_route_fix
    - copywriting_route_fix
  responsibility_layer:
    - project_judgment_layer
    - mechanism_fix_layer
    - execution_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: true
    reason: 本轮涉及文案路由、卡片位置路由、剪辑决策、执行规则和日志同步，多文件机制修补
    lane_recommendation: audit_lane -> standard_lane after impact check passed
    parallel_recommendation: serial_only
  completion_relay_gate:
    triggered: true
    reason: 本轮需要多文件影响面扫描、规则写入、日志回流和剩余工作反查，不能只改单个文件
  execution_permission: allowed_after_must_read_passed
```

## 3. state_action_router

```text
state_action_router:
  input_signal: 用户明确要求总结卡和反转卡位置也由 Codex 根据文案判断
  current_project_state:
    - mechanism_repair_needed
    - content_route_needed
    - editing_inference_needed
  fact_source_arbitration:
    primary_source: 当前用户明确指令 + GitHub main 当前机制文件
    conflict_detected:
      - 旧口径可能固定总结卡 / 反转卡位置
    conflict_resolution:
      - 卡片职责可固定，卡片位置必须由文案功能判断
  inferred_state:
    - card_placement_route_needed
    - summary_card_position_should_follow_copy_closure
    - reversal_card_position_should_follow_copy_turning_point
  confidence: high
  trigger_mechanism:
    - content_route_inference_function
    - editing_inference_function
    - Completion Relay Gate
  selected_action:
    - 新增卡片位置判断字段
    - 修正总结卡 / 反转卡固定位置旧口径
    - 同步 Codex 执行侧判断
```

## 4. actual_read_files

- `AGENTS.md（仓库入口规则）`
- `codex_source/00_codex_readme.md（Codex 执行层总入口）`
- `codex_source/01_execution_rules.md（Codex 执行规则）`
- `codex_log/latest.md（最新日志）`
- `GPT数据源/05_文案路由规则.md（文案路由规则）`
- `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`
- `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`
- `GPT数据源/08_当前正式事实.md（当前正式事实）`
- `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（多执行器路由说明）`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md（当前主线锚点，impact check 命中后读取）`

## 5. impact_check

`已确认` 影响面分三类：

1. 需要修改：
   - `GPT数据源/05_文案路由规则.md`
   - `GPT数据源/07_AI知识类视频价值规则.md`
   - `GPT数据源/11_项目状态动作总控器_机制推理层.md`
   - `codex_source/19_project_state_action_router.md`
   - `codex_source/01_execution_rules.md`
   - `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
   - `codex_log/latest.md`
2. 只保留历史 / reference，不修改：
   - `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
   - `codex_source/locked_reference_registry.md`
   - 历史 `codex_log/20260430*`、`codex_log/20260503*`、`codex_log/supply_requests/*`
3. 不扩大同步：
   - `project_source/*` 多为历史 / 辅助镜像，本轮不作为主事实写入面。

## 6. changed_files

- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260514_card_placement_route_fix.md`

## 7. key_rule_changes

- 新增 `card_placement_decision（卡片位置判断）`。
- 明确 `summary_card（总结卡）`、`reversal_card（反转卡）`、`result_diff_card（结果差卡）`、`prompt_tail_card（Prompt 引用尾卡）` 的职责、适合位置和禁止项。
- `content_route_inference_function（内容路由推理函数）` 新增 `copy_function / reversal_point / conclusion_point / result_diff_point / evidence_window_active / prompt_handoff_needed` 等输入信号。
- `editing_inference_function（剪辑推理函数）` 新增 `card_insertion_safe / card_insertion_interrupts_evidence / keep_evidence_window_uninterrupted` 等状态判断。
- Codex 执行侧新增硬规则：涉及卡片位置时，缺 `card_placement_decision` 不得直接生成视频。

## 8. forbidden_status_check

- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改视频、图片、音频、字幕、时间线、TTS 或任何媒体产物。
- `已确认` 未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `已确认` 未读取 `.env`、`.env.swp`、API key、token、secret。
- `已确认` 未调用 DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。

## 9. validation_result

- `git diff --check`: passed。
- 关键词检查覆盖：`card_placement_decision`、`summary_card`、`reversal_card`、`result_diff_card`、`prompt_tail_card`、`copy_function`、`reversal_point`、`conclusion_point`、`evidence_window_active`、`card_interrupts_evidence_window`。
- 禁止状态推进检查：未发现新增 `content_validation =`、`send_ready =`、`publish_status =`、`voice_validation =`、`final_voice_validated =`、`visual_master_locked =` 写入。

## 10. remaining_work_check

```text
remaining_work_check:
  must_fix_remaining: none
  media_generation_remaining: not_applicable
  dynamic_status_update_remaining: not_applicable
  real_video_effect_validation: pending_future_real_task
```

## 11. sync_back_check

```text
sync_back_check:
  mechanism_files_synced: true
  codex_execution_rules_synced: true
  latest_synced: true
  dated_log_created: true
  gpt_project_upload_package_generated: false
  note: 本轮未要求生成 GPT Project 上传包；不生成静态包。
```

## 12. next_target

下一条真实内容执行前，用 `card_placement_decision（卡片位置判断）` 验证 Codex / ChatGPT 能否按最终文案、证据窗口和观众理解路径选择卡片类型与位置，而不是沿用固定 shot。
