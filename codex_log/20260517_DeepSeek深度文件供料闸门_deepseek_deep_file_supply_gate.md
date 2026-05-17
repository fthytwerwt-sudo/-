# 20260517｜DeepSeek深度文件供料闸门 deepseek_deep_file_supply_gate

## 本轮目标

把当前 DeepSeek 供料机制从轻量 `must_read_file_map（必读文件地图）` / 风险摘要，升级为 `DeepSeek deep file supply mode（DeepSeek 深度文件供料模式）`。

本轮不是视频生成任务，不修改已发布视频，不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。

## route_decision 摘要

```text
project_route: video_factory
task_type: mechanism_or_route_fix + project_file_change + code_debug + validation_layer_sync
responsibility_layer: entry_routing_layer + execution_layer + validation_layer + sync_layer + mechanism_fix_layer
large_task_gate.triggered: true
lane_recommendation: audit_lane -> standard_lane
parallel_recommendation: serial_only
write_owner: Codex Integrator only
deepseek_supply_gate.required: true
deepseek_supply_gate.mode: deep_file_supply_design_and_validation
execution_permission: allowed_after_must_read_and_impact_check
```

## state_action_router 摘要

```text
input_signal: 用户要求 DeepSeek 深度参与，直接帮 Codex 读取 / 接收任务相关文件内容并持续供料。
current_project_state:
  - mechanism_repair_needed
  - deepseek_deep_file_supply_required
  - codex_vertical_completion_missing
fact_source_arbitration.primary_source: repo current files
inferred_state: 当前 DeepSeek 供料深度不足，需要从轻量文件地图升级为深度文件内容供料。
trigger_mechanism:
  - mandatory_deepseek_supply_loop
  - deepseek_deep_file_supply_gate
  - Completion Relay Gate
selected_action: 更新机制、脚本、schema、fixtures、日志和验证链
forbidden_action:
  - 不生成视频
  - 不推进内容状态
  - 不把 fallback 写成 DeepSeek 真实参与
```

## impact_check_report

1. 当前 DeepSeek 供料链路：`scripts/deepseek_supply_controller.py`、`scripts/deepseek_readonly_explorer.py`、`scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py`、`scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`、`scripts/DeepSeek多任务供料运行器_deepseek_multi_task_supply_runner.py`、`codex_source/17`、`codex_source/18`、`codex_source/schemas/deepseek_supply_request.schema.json`、`codex_source/fixtures/*`、`codex_log/supply_requests/*`。
2. 旧 schema 已支持 request-file 与基础供料字段，但不完整支持内容级 `deep_supply_mode / relevant_file_bundle / exact_snippet_pack / incremental_supply_request`。
3. 旧 controller 已支持 request-file、context files、fallback provenance、post risk review，但输出仍偏轻量；本轮已补内容级 bundle / snippet / dependency 输出。
4. safe runner 已支持通过 runtime provider 做真实调用；本轮补了 pre / mid / post 三次 request 来验证多轮供料。
5. 当前已有 `post_risk_review（执行后风险复核）`，本轮增强为 deep supply 输出链的一部分。
6. 旧规则中“Codex 必须复核原文件”容易被理解为默认全仓深读；本轮改为 `Codex minimal review policy（Codex 最小必要复核策略）`。
7. 需要同步 `GPT数据源/01`、`08`、`10`、`11`。
8. 需要同步 `codex_source/00`、`01`、`17`、`18`、`19`。
9. 需要更新 schema、request example、fixture cases、controller 输出和验证。
10. dated log 为本文件。
11. GPT Project 上传包本轮 `not_generated（未生成）`。

## 实际修改文件

- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`
- `scripts/deepseek_supply_controller.py`
- `codex_source/fixtures/DeepSeek深度文件供料_deep_file_supply_cases.json`
- `codex_source/fixtures/DeepSeek深度文件供料_deep_file_supply_request_example.json`
- `codex_log/supply_requests/20260517_deepseek_deep_file_supply_mode_pre_supply_request.json`
- `codex_log/supply_requests/20260517_deepseek_deep_file_supply_mode_mid_task_incremental_supply_request.json`
- `codex_log/supply_requests/20260517_deepseek_deep_file_supply_mode_post_risk_review_request.json`
- `codex_log/latest.md`
- `codex_log/20260517_DeepSeek深度文件供料闸门_deepseek_deep_file_supply_gate.md`

## DeepSeek 深度供料机制新增点

新增默认链路：

```text
route_decision
-> create_supply_request
-> deep_file_prefetch
-> relevant_file_bundle
-> exact_snippet_pack
-> dependency_map
-> risk_and_conflict_report
-> codex_next_input
-> Codex child_task_graph
-> mid_task_incremental_supply
-> Codex write / validate
-> post_risk_review
-> completion_truth_check
```

供料请求新增 / 强化字段：

- `deep_supply_mode`
- `file_scope`
- `content_loading_policy`
- `codex_minimal_review_policy`
- `will_modify_files`
- `conflict_or_uncertain_files`
- `validation_failed_files`
- `safety_sensitive_files`
- `incremental_supply_request`
- `mid_task_incremental_supply_trigger`
- `mid_task_incremental_supply_action`

供料包新增 / 强化字段：

- `relevant_file_bundle`
- `exact_snippet_pack`
- `dependency_map`
- `risk_and_conflict_report`
- `risk_delta_report`
- `missing_or_uncertain_files`
- `codex_next_input.files_codex_must_review`
- `deepseek_depth_validation`

## Codex 最小必要复核边界

Codex 不再默认全仓深读，但不能完全不读。Codex 必须复核：

- `will_modify_files（本轮要修改的文件）`
- `conflict_or_uncertain_files（DeepSeek 标记冲突 / 不确定的文件）`
- `validation_failed_files（验证失败后关联文件）`
- `safety_sensitive_files（安全敏感文件）`
- schema / tests 依赖文件
- secret、API key、runtime provider 安全边界相关文件

若 DeepSeek 供料与仓库原文件冲突，以 Codex 对目标文件的复核为准，并记录冲突。

## 脚本 / schema / fixture 接入情况

- `scripts/deepseek_supply_controller.py` 已接收嵌套 `file_scope.must_prefetch_files / candidate_files / optional_prefetch_files`。
- controller 已根据 `content_loading_policy` 裁剪文本并输出 `relevant_file_bundle` 与 `exact_snippet_pack`。
- controller 已输出 `dependency_map`、`missing_or_uncertain_files`、`risk_delta_report`、`deepseek_depth_validation`。
- controller 已支持 `trigger_reason = mid_task_incremental_supply`，并在 `codex_next_input` 输出 `files_codex_must_review`。
- schema 已加入 `deep_supply_mode / file_scope / content_loading_policy / codex_minimal_review_policy / incremental_supply_request`。
- fixture 已覆盖 deep prefetch success、mid-task required、fallback not deep participation 三种 case。

## 验证命令与结果

```text
python3 -m py_compile scripts/*.py
result: passed

JSON parse: schema + fixture + request cards
result: passed, 8 files

schema field check:
schema_required_props_missing = []
mid_task_incremental_supply_in_enum = true

fixture controller run:
supply_source = fallback_local_only
not_deepseek_conclusion = true
relevant_file_bundle = 4
exact_snippet_pack = 5
dependency_map = 4
deepseek_depth_validation.status = passed_contract_level

pre safe runner:
deepseek_actual_participation = deepseek_passed
relevant_file_bundle = 10
exact_snippet_pack = 11
dependency_map = 10
deepseek_depth_validation.status = passed_contract_level

mid safe runner:
deepseek_actual_participation = deepseek_passed
relevant_file_bundle = 10
exact_snippet_pack = 11
dependency_map = 10
deepseek_depth_validation.status = passed_contract_level

post safe runner:
deepseek_actual_participation = deepseek_passed
relevant_file_bundle = 9
exact_snippet_pack = 10
dependency_map = 9
post_risk_review = true

completion truth negative checks:
empty_required = failed_insufficient_depth
fallback_required = failed_deepseek_not_deeply_participated

git diff --check:
result: passed
```

安全字段：

```text
env_file_read = false
api_key_printed = false
api_key_written = false
fallback_local_only_not_mislabeled = true
token_usage_observed_by_codex = not_available
token_usage_expected = token_decrement_expected
token_usage_user_check_required = true
```

## 未完成 / 待验证项

- `待验证` 本轮证明机制接线与三次本地真实 DeepSeek API 调用通过，不等于 DeepSeek 深度文件供料在长期独立 Codex 会话中稳定。
- `待验证` token 实际扣减仍需用户侧控制台确认；Codex 只记录 `token_decrement_expected`，不能替用户观察 token 变化。
- `待验证` GPT Project 上传包本轮未生成，状态为 `not_generated（未生成）`。
- `待验证` 本机制后续在视频执行、数据复盘、文案改稿等不同任务类型中仍需继续跑真实任务验证。

## 状态边界

本轮未推进：

- `content_validation（内容验证）`
- `send_ready（可发送状态）`
- `publish_status_success（发布成功口径）`
- `voice_validation（声音验证）`
- `final_voice_validated（最终声音验证）`
- `visual_master_locked（视觉母版锁定）`

本轮不证明：

- `multi-agent_runtime（多 agent 运行时）` 已跑通
- DeepSeek 深度文件供料长期稳定
- fallback 可以算 DeepSeek 真实参与
- Codex 可以完全不读文件

## completion_truth_check

```text
mechanism_files_updated: true
execution_rules_updated: true
deepseek_schema_updated: true
fixtures_updated: true
runner_or_controller_updated: true
validation_run: true
latest_updated: true
dated_log_created: true
forbidden_status_promotion_absent: true
fallback_not_mislabeled_as_deepseek: true
codex_minimal_review_policy_preserved: true
remaining_work:
  - 后续真实任务继续验证长期稳定性
  - 用户侧确认 token 扣减
  - 如需 GPT Project 上传包，另起同步任务生成，不得假装本轮已同步 UI
```

## 下一个目标

后续任何大型 / 多文件 / 用户明确要求 DeepSeek 深度参与任务，默认使用 `deep_supply_mode.enabled = true` 的 supply request，并在执行中按缺口触发 `mid_task_incremental_supply（任务中增量供料）`；Codex 只做最小必要复核、写入、验证、日志和收尾。
