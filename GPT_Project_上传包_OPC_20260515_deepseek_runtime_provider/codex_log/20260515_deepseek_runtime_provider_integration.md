# 20260515 DeepSeek runtime provider 项目级接入

## route_decision（路由判断）

- `project_route`: `video_factory`
- `task_type`: `code_execution_or_debug + mechanism_or_route_fix + execution_architecture_rewire + field_and_function_landing + provider_runtime_integration + gpt_project_static_package_sync`
- `responsibility_layer`: `execution_layer + validation_layer + sync_layer + mechanism_fix_layer`
- `large_task_gate`: `triggered`
- `lane_recommendation`: `audit_lane -> standard_lane`
- `parallel_recommendation`: `explore_plus_integrate`
- `execution_permission`: `granted_after_required_reads`

## state_action_router（项目状态动作总控器）

- `input_signal`: 用户要求 DeepSeek 从 process-env-only 阻断态升级为项目级稳定 runtime provider。
- `current_project_state`: `deepseek_provider_runtime_required`
- `inferred_state`: `deepseek_runtime_provider_ready + deepseek_multi_task_supply_passed`
- `selected_action`: 接入 provider、doctor、多任务 runner，完成真实 DeepSeek 调用验证并同步规则 / 日志 / 上传包。
- `blocked_if`: key 缺失、provider not ready、真实调用失败、fallback_count > 0、blocked_count > 0、key 泄露、推进内容 / 发布 / 声音 / 视觉状态。

## root_cause（根因）

- `已确认` 旧 DeepSeek 链路把每轮真实参与绑定到当前 Codex 进程是否已有 `DEEPSEEK_API_KEY`。
- `已确认` live smoke test 能通过，说明 DeepSeek API 能力本身可用；普通任务 blocked 的主要原因是当前进程 env 不稳定。
- `已确认` process-env-only 策略不足以承担项目级 runtime provider，因为它需要每轮重新授权或手动注入。

## runtime_provider（运行时供应商）

- `path`: `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`
- `load_order`: `process_env -> .env.local -> .env -> 本地运行配置_local_runtime/deepseek_runtime_authorization.local.json`
- `allowed_key_name`: `DEEPSEEK_API_KEY`
- `key_source`: `project_env`
- `auto_load_enabled`: `true`
- `inject_to_child_process_only`: `true`
- `key_printed`: `false`
- `key_written`: `false`
- `key_committed`: `false`

## runtime_doctor（运行环境自检）

- `report_json`: `dist/deepseek_runtime_validation/runtime_doctor_report.json`
- `report_md`: `dist/deepseek_runtime_validation/runtime_doctor_report.md`
- `status`: `ready`
- `key_found`: `true`
- `key_source`: `project_env`
- `key_git_tracked`: `false`
- `can_inject_child_process`: `true`
- `can_call_deepseek`: `true`
- `leak_found`: `false`

## multi_task_supply_validation（多任务供料验证）

- `combined_report_json`: `dist/deepseek_runtime_validation/latest_combined_participation_report.json`
- `combined_report_md`: `dist/deepseek_runtime_validation/latest_combined_participation_report.md`
- `total_requests`: `3`
- `deepseek_passed_count`: `3`
- `fallback_count`: `0`
- `blocked_count`: `0`
- `all_outputs_exist`: `true`

## per_task_reports（逐任务报告）

- `task_A`: `dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/participation_report.json`
- `task_B`: `dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/participation_report.json`
- `task_C`: `dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/participation_report.json`

## changed_runtime_surfaces（运行时接线面）

- `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`
- `scripts/DeepSeek运行环境自检_deepseek_runtime_doctor.py`
- `scripts/DeepSeek多任务供料运行器_deepseek_multi_task_supply_runner.py`
- `scripts/DeepSeek环境安装器_deepseek_runtime_setup.py`
- `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py`
- `scripts/deepseek_supply_controller.py`
- `scripts/deepseek_readonly_explorer.py`

## sync_back（同步回写）

- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/09_目标态计划.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`
- `codex_source/fixtures/DeepSeek运行时供应商_deepseek_runtime_provider_supply_request_example.json`
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`

## gpt_project_package（GPT Project 上传包）

- `path`: `GPT_Project_上传包_OPC_20260515_deepseek_runtime_provider/`
- `status`: `generated`
- `manifest`: `GPT_Project_上传包_OPC_20260515_deepseek_runtime_provider/上传说明_UPLOAD_MANIFEST.md`

## validation_checks（验证检查）

- `python_syntax_check`: `passed`
- `json_parse`: `passed`
- `runtime_doctor`: `passed`
- `single_deepseek_call`: `passed`
- `two_request_deepseek_call`: `passed`
- `three_request_deepseek_call`: `passed`
- `no_key_leak`: `passed`
- `forbidden_status_check`: `passed`

## state_boundary（状态边界）

- `technical_validation`: `passed_runtime_provider_local_validation`
- `content_validation`: `not_applicable_not_advanced`
- `publish_status`: `not_changed`
- `send_ready`: `not_changed`
- `voice_validation`: `not_changed`
- `final_voice_validated`: `not_changed`
- `visual_master_locked`: `not_changed`
- `multi_agent_runtime_stability`: `待验证`

## next_target（下一个目标）

后续每个需要 DeepSeek 的 Codex 任务默认走 runtime provider；若 provider not ready，进入一次性 runtime setup；若用户要求 DeepSeek 必须参与而真实调用未通过，则整体任务 blocked。
