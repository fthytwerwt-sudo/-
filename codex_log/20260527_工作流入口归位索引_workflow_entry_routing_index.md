# 20260527 工作流入口归位索引 Workflow Entry Routing Index

## 1. 本轮任务

- `task_type = routing_index_repair（路由索引修补）`
- `selected_repair_scope = Codex 执行入口层 / routing index layer`
- `user_input_reference = 《视频工厂》现有工作流与 Codex 执行入口只读审计报告`
- `audit_recheck.current_gap = routing_index_gap 主缺口；execution_discipline_gap 次缺口；execution_entry_gap partial；missing_standard false`

## 2. 写入范围

- 新增短索引：`codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- 接入入口：`codex_source/00_codex_readme.md`
- 接入执行规则：`codex_source/01_execution_rules.md`
- 接入状态动作总控器：`codex_source/19_project_state_action_router.md`
- 补 fixture：`codex_source/fixtures/mechanism_inference_function_cases.json`
- 更新最新日志：`codex_log/latest.md`

## 3. 索引内容

本轮只补一张短索引，不新增大机制。

索引要求 Codex 在 `route_decision（路由判断）` 后、具体执行前输出：

```text
workflow_route_decision:
  workflow_type:
  reason:
  must_read:
  required_handoff:
  forbidden_status:
  blocked_if:
```

覆盖工作流：

- `copy_testing_flow（文案测试流）`
- `material_evidence_flow（素材证据流）`
- `aesthetic_editing_flow（审美剪辑流）`
- `quality_review_flow（质量复审流）`
- `data_review_flow（数据复盘流）`
- `mechanism_repair_flow（机制修补流）`

## 4. 状态边界

- `video_generated = false`
- `audio_generated = false`
- `copy_changed = false`
- `media_changed = false`
- `content_validation` 未推进
- `send_ready` 未推进
- `voice_validation` 未推进
- `final_voice_validated` 未推进
- `visual_master_locked` 未推进
- `current_data_goal_anchor_ready` 未推进

## 5. 诚实边界

- 本轮只修入口索引。
- 未生成视频。
- 未生成音频。
- 未改文案。
- 未推进状态。
- 不代表机制长期稳定。
- 后续真实任务必须验证 Codex 是否稳定输出 `workflow_route_decision（工作流归位判断）`。
