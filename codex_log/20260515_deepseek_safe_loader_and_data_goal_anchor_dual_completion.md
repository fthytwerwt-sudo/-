# 20260515 DeepSeek 安全加载与 data_goal_anchor 执行链双修补日志

## 1. route_decision（路由判断）

- `project_route`: `video_factory（视频工厂）`
- `task_type`: `mechanism_or_route_fix（机制 / 路由修补）`、`project_file_change（项目文件修改）`、`code_debug（代码执行 / 调试）`、`field_and_function_landing（字段与函数落地）`、`gpt_project_static_package_sync（GPT Project 静态包同步）`
- `responsibility_layer`: `entry_routing_layer`、`execution_layer`、`validation_layer`、`sync_layer`、`mechanism_fix_layer`、`multi_agent_lane_layer`
- `large_task_gate`: `triggered`
- `lane`: `audit_lane -> standard_lane`
- `parallel`: `explore_plus_integrate`
- `execution_permission`: `allowed_for_read_audit_and_single_integrator_write`

## 2. state_action_router（项目状态动作总控器）

- `state_inference`: `deepseek_supply_gate_unstable` + `data_goal_anchor_wiring_needs_validation`
- `action_policy`: 先做两个只读探索，再由 Integrator 单点写入。
- `blocked_if`: 需要读取 `.env` 才能继续、需要把 `fallback_local_only` 写成 DeepSeek 结论、需要推进内容 / 发布 / 声音 / 视觉母版状态。

## 3. parallel_execution_report（并行执行报告）

- `Explorer A`: 只读审计 DeepSeek safe loader / process env / supply gate。
- `Explorer B`: 只读审计 `data_goal_anchor` / `13` / `14` / execution rules / editing / assembly / alignment check。
- `Integrator`: 唯一写入者，负责合并冲突、修改文件、跑验证、更新日志、生成 GPT Project 静态包、commit / push。
- `why_not_true_multi_task_parallel`: 两条问题都要改 `codex_source/17`、`18`、`19`、`01`、`GPT数据源/01`、`03`、`08`、`10`、`11`、fixture、日志和上传包，核心写入面重叠，必须单点整合。

## 4. required_output_inventory（必须交付清单）

- DeepSeek safe loader 策略：`process_env_only` 优先；授权 loader 只能作为单次子进程注入；无法安全获得 key 时 `blocked_missing_process_env_api_key`。
- DeepSeek controller / schema / fixture / protocol 同步。
- `data_goal_anchor` 到 ChatGPT prompt、DeepSeek supply request、Codex execution、editing / assembly、`data_goal_alignment_check` 的前置验收接线。
- `codex_log/latest.md`、本 dated log、`current_local_artifact_paths.md`。
- GPT Project 静态上传包：`GPT_Project_上传包_OPC_20260515_deepseek_safe_loader_data_goal_anchor/`。

## 5. child_task_graph（子任务树）

1. `Explorer A`: DeepSeek 安全 key / safe loader / controller / explorer / schema / fixture 只读审计。
2. `Explorer B`: `data_goal_anchor` / 13 / 14 / 执行规则 / editing / assembly / alignment check 只读审计。
3. `Integrator`: 汇总审计结果，统一写入脚本、规则、schema、fixture、日志和 GPT Project 包。
4. `Verifier`: JSON parse、Python syntax、fixture basic validation、safe runner blocked-path validation、keyword check、forbidden status check、no media / secret diff check、package manifest check、`git diff --check`。

## 6. deepseek_safe_loader_result（DeepSeek 安全加载结果）

- `root_cause`: DeepSeek API 曾经通过 live smoke test，但那是用户授权范围内由 safe loader 把 key 注入测试子进程；每轮 Codex 任务进程不一定天然带 `DEEPSEEK_API_KEY`。
- `policy_written`: 每轮真实 DeepSeek 供料默认走 `process_env_only`；controller / explorer 不直接读取 `.env`；需要 `.env` key 时必须有本轮明确授权的 wrapper / loader，只注入子进程。
- `blocked_policy`: `requires_real_deepseek_participation = true` 且 `process_env_key_present = false` 时，输出 `blocked_missing_process_env_api_key`，不得降级写成 DeepSeek 已参与。
- `fallback_boundary`: `fallback_local_only` 只能写成本地兜底，不得写成 DeepSeek 结论。
- `this_round_result`: 当前进程 `process_env_key_present = false`；本轮 pre-supply 真实 DeepSeek 参与为 `blocked_missing_process_env_api_key`。
- `secret_boundary`: `env_file_read = false`、`api_key_printed = false`、`api_key_written = false`。

## 7. data_goal_anchor_result（数据目标锚点结果）

- `anchor_fields`: `data_goal_anchor_used`、`main_bottleneck_supported`、`primary_variable_supported`、`forbidden_variables_avoided`、`post_publish_validation_metric`。
- `execution_wires`: ChatGPT prompt、DeepSeek supply request、Codex execution rules、`content_route_card V2`、`script_to_timeline_map`、`editing_decision_pack`、`assembly_decision_pack` 均接入数据目标字段。
- `editing / assembly wires`: 必须说明 `primary_variable_support`、`forbidden_visuals_by_goal` / `forbidden_variable_avoided`、`metric_supported`、`post_publish_validation_metric`。
- `alignment_check`: 完成前必须输出 `data_goal_alignment_check`，缺失则不得写完成。
- `alias_boundary`: `forbidden_variables_avoided`、`forbidden_visuals_by_goal`、`forbidden_variable_avoided` 可作为不同对象字段名，但必须回指同一组 `data_goal_anchor.forbidden_variables`。

## 8. validation_checks（验证检查）

- `json_parse`: `passed`
- `python_syntax_check`: `passed`
- `fixture_basic_validation`: `passed`
- `safe_runner_blocked_path_validation`: `passed_as_blocked_missing_process_env_api_key`
- `keyword_check`: `passed`
- `package_manifest_check`: `passed`
- `git_diff_check`: `passed`
- `jsonschema_full_validation`: `not_tested_full_jsonschema_validation_unavailable`

## 9. forbidden_status_check（禁止状态检查）

- `content_validation`: `not_advanced`
- `send_ready`: `not_advanced`
- `publish_status`: `not_advanced`
- `voice_validation`: `not_advanced`
- `final_voice_validated`: `not_advanced`
- `visual_master_locked`: `not_advanced`

## 10. state_boundary（状态边界）

- `mechanism_written`: `true`
- `real_task_stability`: `pending_next_real_video_execution`
- `deepseek_real_participation_this_round`: `blocked_missing_process_env_api_key`
- `multi_agent_runtime_stability`: `not_claimed`
- `content_validation`: `not_applicable_not_advanced`

## 11. 下一个目标

下一条真实视频执行前，先用 `data_goal_anchor` 锁定目标，再用 process-env-only DeepSeek supply gate 或明确 blocked 结果作为前置验收；Codex 完成前必须输出 `data_goal_alignment_check`。
