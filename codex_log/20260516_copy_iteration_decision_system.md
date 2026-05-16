# 20260516｜文案迭代决策系统

## 1. 本轮定位

- `已确认` 本轮只做《视频工厂》的机制修补、路由修补、项目文件修改和代码执行 / 调试。
- `已确认` 本轮不是视频执行任务；未生成新视频，未修改已发布视频，未生成正式下一条视频执行 prompt，未直接重写 V003 文案。
- `current_project_state`: `formal_operation_active + operation_review_pending + copy_iteration_system_missing`。

## 2. route_decision

- `project_route`: `video_factory`
- `task_type`: `mechanism_or_route_fix + project_file_change + code_execution_or_debug + copy_iteration_system`
- `large_task_gate`: `triggered`
- `lane`: `audit_lane -> standard_lane`
- `parallel`: `serial_only`
- `write_owner`: `Codex Integrator only`

## 3. state_action_router

- `input_signal`: 用户要求记录 V003 原始文案，并建立数据反馈到文案的内容迭代决策机制。
- `inferred_state`: `copy_iteration_system_missing`
- `selected_action`: `build_copy_iteration_decision_system`
- `done_when`: V003 文案被记录，系统生成 `next_copy_revision_brief`，并接入运营决策报告。
- `blocked_if`: 只能写概念、无法记录文案版本、无法生成 ChatGPT 可读报告、误判换方向 / 换人群、生成正式下一条视频执行 prompt。

## 4. DeepSeek supply gate

- `supply_request`: `codex_log/supply_requests/20260516_copy_iteration_decision_system_pre_supply_request.json`
- `latest_supply_pack`: `dist/deepseek_runtime_validation/20260516_copy_iteration_decision_system_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation`: `deepseek_passed`
- `fallback_status`: `not_used`
- `not_deepseek_conclusion`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `env_file_read`: `false`
- `token_usage_expectation_check`: `token_decrement_expected`
- `multi_agent_runtime_validation`: `not_started`

## 5. 新增文案迭代系统

- `scripts/文案迭代决策系统_copy_iteration_decision_system.py`
- `review_loop/copy_iteration/copy_registry.json`
- `review_loop/copy_iteration/V003/V003_copy_v1_raw.md`
- `review_loop/copy_iteration/V003/V003_copy_v1_record.json`
- `review_loop/copy_iteration/V003/V003_copy_structure_map.json`
- `review_loop/copy_iteration/V003/V003_copy_iteration_decision.json`
- `review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md`
- `review_loop/copy_iteration/latest_copy_iteration_report.json`
- `review_loop/copy_iteration/latest_copy_iteration_report.md`

## 6. V003 文案迭代结果

- `problem_layer`: `opening_packaging`
- `supporting_problem_layers`: `bridge_3_8s`
- `confidence`: `low`
- `formal_copy_revision_allowed`: `false`
- `low_confidence_prepare_allowed`: `true`
- `revision_scope`: `opening_0_3s + bridge_3_8s`
- `forbidden_changes`: `target_user / topic_direction / offer / whole_script_rewrite / formal_next_video_execution_prompt`
- `validation_metric`: `2s_bounce / 3s_retention / 5s_completion / average_watch_time`
- `next_action`: `prepare_candidate_opening_revision_brief_only`

## 7. 接入运营决策系统

- `scripts/运营决策系统_operation_decision_system.py` 已新增 `copy_iteration_linkage`。
- `review_loop/decision_engine/latest_operation_decision_report.json` 已引用最新文案迭代报告路径。
- `review_loop/decision_engine/latest_operation_decision_report.md` 已增加 `copy_iteration_linkage`。
- `review_loop/decision_engine/final_user_operation_result.md` 已增加“文案迭代入口”，提示 ChatGPT 读取 `V003_next_copy_revision_brief.md`。

## 8. 机制文件最小接线

- `GPT数据源/05_文案路由规则.md`：新增文案问题层级判断和 copy iteration gate。
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`：新增 `copy_iteration_system_required`、`copy_version_record_missing`、`next_copy_revision_brief_required`。
- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`：新增 `copy_iteration_decision gate`。
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`：新增 `next_copy_revision_brief gate`。
- `codex_source/19_project_state_action_router.md`：新增 Codex 执行侧 copy iteration 路由动作。

## 9. 状态边界

- `content_validation_advanced`: `false`
- `send_ready_advanced`: `false`
- `current_data_goal_anchor_ready`: `false`
- `next_formal_video_execution_prompt_generated`: `false`
- `target_audience_changed`: `false`
- `topic_direction_changed`: `false`
- `new_video_generated`: `false`
- `published_video_modified`: `false`

## 10. 验证结果

`已验证` 以下 fresh validation 均通过：

```bash
python3 -m py_compile scripts/文案迭代决策系统_copy_iteration_decision_system.py scripts/运营决策系统_operation_decision_system.py
python3 scripts/文案迭代决策系统_copy_iteration_decision_system.py --validate-only
python3 scripts/运营决策系统_operation_decision_system.py --validate-only
python3 - <<'PY'
import json
from pathlib import Path
for path in [
    "review_loop/copy_iteration/copy_registry.json",
    "review_loop/copy_iteration/V003/V003_copy_v1_record.json",
    "review_loop/copy_iteration/V003/V003_copy_structure_map.json",
    "review_loop/copy_iteration/V003/V003_copy_iteration_decision.json",
    "review_loop/copy_iteration/latest_copy_iteration_report.json",
    "review_loop/decision_engine/latest_operation_decision_report.json",
]:
    json.loads(Path(path).read_text(encoding="utf-8"))
print("json_parse_passed")
PY
```

验证摘要：

- `script_compile`: passed
- `copy_iteration_script_validate`: passed
- `operation_decision_script_validate`: passed
- `json_parse`: passed
- `raw_copy_matches_locked_source`: true
- `forbidden_status_scan`: passed
- `next_formal_video_execution_prompt_generated`: false
