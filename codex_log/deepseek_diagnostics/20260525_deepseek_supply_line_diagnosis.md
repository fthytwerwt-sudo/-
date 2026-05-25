# 20260525 DeepSeek 供料链只读诊断

## 1. 本轮目标

本轮只读诊断上一轮 `20260524｜对标文案话语机制反报告腔修正` 为什么没有触发 DeepSeek 供料链。

本轮不修代码、不修改 DeepSeek runtime provider / safe runner / controller / schema、不改 04 / 05 / 07 文案机制、不写新文案、不生成视频、不推进任何内容状态。

允许写入范围仅限：

- `codex_log/deepseek_diagnostics/20260525_deepseek_supply_line_diagnosis.md`
- `codex_log/latest.md`

## 2. route_decision

```text
project_route = video_factory
task_type = diagnosis_task + deepseek_supply_line_diagnosis + mechanism_route_check + no_code_change
responsibility_layer = validation_layer + mechanism_fix_layer + sync_layer
selected_action = readonly_deepseek_supply_line_diagnosis
forbidden_action = code_fix / mechanism_file_change / copywriting / generate_video / advance_status / read_or_print_secret
large_task_gate = triggered
lane_recommendation = serial_only
parallel_recommendation = serial_only
write_owner = Codex Integrator only
allowed_changes = codex_log/deepseek_diagnostics/20260525_deepseek_supply_line_diagnosis.md + codex_log/latest.md
execution_permission = readonly diagnosis + path-limited report write
```

## 3. state_action_router

```text
input_signal = 用户要求只读诊断上一轮 DeepSeek 供料链未触发
current_project_state = formal_operation_active + deepseek_supply_line_diagnosis
selected_action = write_readonly_diagnosis_report
done_when = 诊断报告 + latest 更新 + path-limited commit/push
blocked_if = 需要读取 secret / 无法安全运行 provider / 无法回答根因 / 无法 push
```

## 4. 影响面检查

```text
current_branch = main
current_head_before_report = 0b9b24bf7d0aa2fafbc6af603127936aad029575
unrelated_dirty_changes_present = true
path_limited_staging_required = true
previous_commit_exists = true
previous_commit_on_main = true
previous_commit_on_origin_main = true
deepseek_diagnostics_dir_exists_before_this_task = false
code_change_planned = false
deepseek_call_planned = yes, only through safe runner/provider if ready
secret_write_planned = false
status_promotion_planned = false
```

已确认当前工作区存在 unrelated dirty changes。本轮只允许 path-limited staging 诊断报告和 `latest.md` 的本轮新增段落，不纳入脚本、规则文件、`dist/`、素材、媒体或既有 unrelated 修改。

## 5. 上一轮 DeepSeek 状态复核

上一轮 commit：

```text
previous_commit = d8017bcc3c168b1d5a8658609fc1d2ed6d213704
commit_title = Prevent reference copy voice rules from becoming report-style scripts
changed_files = GPT数据源/04_选题与文案规则.md + GPT数据源/05_文案路由规则.md + GPT数据源/07_AI知识类视频价值规则.md + codex_log/latest.md + codex_log/20260524_reference_copy_voice_anti_report_fix.md
previous_commit_on_origin_main = true
```

上一轮 dated log 记录：

```text
supply_request_created = false
deepseek_call_attempted = false
fallback_status = fallback_local_only
not_deepseek_conclusion = true
stated_reason = 本轮无 DeepSeek 工具可调用，且用户把允许写入范围锁定为 5 个文件；不额外新增 supply_request 文件
```

判断：

```text
is_reason_valid = partial
valid_part = 未把 fallback_local_only 写成 deepseek_passed，且未声称 DeepSeek 真实参与
invalid_part = 项目已有 runtime provider / safe runner / controller；上一轮没有创建供料任务卡、没有运行 provider status、没有尝试 safe runner，也没有把 supply gate 缺失写成 blocked
previous_supply_request_file_found_for_that_task = false
```

## 6. 项目规则要求复核

项目规则复核结论：

```text
mandatory_by_project_rule = true
required_for_every_codex_task = true
allowed_fallback_cases = provider_not_ready / user_forbids_external_call_or_secret_access / task_too_narrow_and_fallback_recorded / safe_runner_blocked_with_reason
user_required_deepseek_cases = must_deepseek_passed_or_blocked
must_block_if_not_deepseek_cases = 用户明确要求 DeepSeek 真实参与 / 视频执行 / 剪辑装配 / 数据目标复盘 / reference audit / 素材审计 / runtime相关诊断 / 多任务供料验证
```

证据摘要：

- `AGENTS.md` 要求每轮默认创建 `supply_request` 并尝试 DeepSeek 只读供料，必须输出参与报告、token 使用预期和 fallback 边界。
- `codex_source/01_execution_rules.md` 的 `mandatory_deepseek_supply_loop` 要求写入前有 `deepseek_supply_gate`，无真实调用时必须写 fallback / blocked，不能由 Codex 主观跳过。
- `GPT数据源/01_项目系统提示词.md` 写明 DeepSeek supply gate 不是 Codex 觉得需要才供料。
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 写明 safe runner/provider 是默认安全真实参与入口。
- `GPT数据源/11_项目状态动作总控器_机制推理层.md` 写明任一 Codex 任务进入执行前触发 `deepseek_supply_required`。
- `GPT数据源/08_当前正式事实.md` 写明 runtime provider 已接入，但长期稳定性仍待验证。

结论：上一轮机制修补任务可以在结果质量上用本地 diff 验证，但不应跳过 mandatory DeepSeek supply gate；至少应创建供料请求或运行 provider readiness，并在无法创建 request 时写明确 blocked/fallback 条件。

## 7. DeepSeek 文件清单

重点文件存在性：

```text
scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py:
  exists = true
  likely_role = runtime provider / redacted status / child env injection

scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py:
  exists = true
  likely_role = safe runner / provider + controller wrapper

scripts/deepseek_supply_controller.py:
  exists = true
  likely_role = supply request validation + supply pack generator

scripts/deepseek_readonly_explorer.py:
  exists = true
  likely_role = readonly DeepSeek explorer

codex_source/schemas/deepseek_supply_request.schema.json:
  exists = true
  likely_role = supply request schema

codex_source/18_deepseek_supply_request_schema.md:
  exists = true
  likely_role = request schema explanation and validation boundary

codex_log/supply_requests/:
  exists = true
  likely_role = historical supply request records
```

本轮诊断不修改上述任何文件。

## 8. runtime provider CLI 检查

provider help：

```text
help_supported = true
provider_commands = status / run
doctor_command = status
smoke_command = safe runner --request-file
cannot_determine_cli = false
```

safe runner help：

```text
help_supported = true
required_arg = --request-file
optional_arg = --output-dir
role = Run DeepSeek supply controller in process-env-only safe mode
```

controller help：

```text
help_supported = true
supports_request_file = true
supports_actions = file_map / risk_report / context_summary / missing_files / visual_asset_requirement_pack / api_asset_generation_pack / image_prompt_pack / asset_validation_pack / assembly_decision_pack / editing_decision_pack / auto
```

## 9. runtime doctor 结果

通过 provider `status` 做 readiness check，未读取 `.env` 原文，未打印 key。

```text
provider_exists = true
provider_cli_detected = true
doctor_ran = true
doctor_command = python3 scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py status
status = ready
can_call_deepseek = true
key_source_type = .env via provider public status only
api_key_printed = false
api_key_written = false
env_file_raw_read_by_codex = false
provider_policy = inject_to_child_process_only + never_print_key + never_write_key + redact_stdout_stderr
```

说明：provider public status 显示 key source 为 `.env`，但本轮没有 `cat .env`、没有读取 secret 原文，也没有把 key 写入日志或 Git。

## 10. smoke test 结果

本轮按要求只通过 safe runner/provider 做最小 smoke test，不手写 curl，不直接读取 key。

第一次尝试：

```text
attempted = true
runner_used = scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py
request_location = /private/var/.../tmp
result = blocked
blocked_reason = context_file_outside_workspace
interpretation = 安全边界正确生效，系统临时目录 request 被拒绝
```

第二次尝试：

```text
attempted = true
runner_used = scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py
request_location = 本地仅分析_local_only/deepseek_supply_line_diagnosis_smoke_tmp_20260525/deepseek_supply_line_diagnosis_smoke_request.json
request_created = temporary_workspace_request
request_cleaned_after_run = true
controller_returncode = 0
response_received = true
response_schema_valid = controller accepted and returned supply pack
deepseek_actual_participation = deepseek_passed
fallback_reason = none
fallback_status = not_used
env_file_read = false
api_key_printed = false
api_key_written = false
process_env_key_present = true
token_usage_expectation = token_should_decrease_if_real_call
user_should_verify_token_ui = true, if needing independent billing/token confirmation
```

边界：本轮 smoke test 只能证明当前 safe runner/provider 在本地最小任务中可真实返回 `deepseek_passed`；不代表 DeepSeek 长期稳定，不代表 multi-agent runtime 已验证。

## 11. 根因判断

```text
root_cause_category = codex_bypassed_mandatory_gate + permission_boundary_too_narrow + local_only_allowed_but_should_have_logged_gate
primary_cause = 上一轮 Codex 执行层没有按项目 mandatory DeepSeek supply gate 创建 supply_request 或运行 provider/safe runner
secondary_cause = 上一轮把“无 DeepSeek 工具可调用”和“允许写入范围锁定 5 个文件”作为跳过依据，但仓库内实际已有 safe runner/provider；即使不提交 supply_request，也应运行 readiness/safe runner 或明确 blocked
not_primary_cause = runtime_provider_not_ready / safe_runner_missing_or_broken / supply_request_schema_missing / key_missing
severity = medium
affects_result_quality = low
affects_multi_agent_validation = true
```

说明：上一轮修改是窄范围文案机制修补，最终 diff 可由本地 grep、diff、状态边界验证，所以内容结果质量影响较低；但因为没有真实 DeepSeek 参与，不能写成多 AI 供料链已执行，也不能把它作为 multi-agent runtime 通过样本。

## 12. DeepSeek 必需 / 可 fallback 任务矩阵

| task_type | deepseek_required | fallback_allowed | completed_allowed_without_deepseek | required_log_fields | blocked_if |
| --- | --- | --- | --- | --- | --- |
| 项目机制修补 | true | yes, if narrow and fully logged | yes, only with `fallback_local_only` + `not_deepseek_conclusion=true` | supply_request or blocked reason, provider status, fallback reason | user explicitly requires DeepSeek passed |
| 文案机制修补 | true | yes, if narrow and no final script/video state change | yes, only with explicit fallback boundary | same as above | no supply gate record at all |
| 视频执行 | true | normally no | no | pre supply + post risk review + token expectation | no deepseek_passed unless user forbids external call and task is blocked |
| 剪辑 / 装配 | true | normally no | no | file map, risk report, alignment risks | fallback used but task writes completed |
| 数据目标 / 复盘 | true | limited | generally no for formal decisions | data goal map, risk conflict report | no supply pack for formal data-driven claim |
| reference audit | true | limited | generally no | reference file map, gap/risk report | DeepSeek skipped without blocked reason |
| 素材审计 | true | limited | generally no | material file map, evidence/risk report | media/secret path required or no supply gate |
| 小范围纯文本 typo / 格式修复 | true by default policy | yes | yes | fallback reason + not DeepSeek conclusion | user required DeepSeek or change scope expands |
| secret / API / runtime 相关任务 | true | no if diagnosis requires runtime truth | no, unless blocked/setup_required | provider status, safe runner result, key printed/written flags | needs reading secret or cannot run safe path |
| 用户明确要求 DeepSeek 参与 | true | no | no | `deepseek_actual_participation=deepseek_passed` or blocked | fallback_local_only / blocked hidden as completed |

## 13. 是否需要下一轮修复

```text
repair_needed = true
repair_type = process_gate_compliance_repair, not runtime_code_repair
runtime_code_repair_needed = false
safe_runner_repair_needed = false
schema_repair_needed = false
```

建议下一轮修复 prompt 摘要：

```text
修正 Codex 执行层 DeepSeek supply gate 执行纪律：
1. 即使没有 DeepSeek MCP tool，也必须优先使用仓库内 scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py 与 scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py。
2. 每轮写入前必须创建 supply_request；若用户允许写入范围不包含 supply_request，则必须使用工作区内临时 request 运行 safe runner，或明确 blocked/fallback 及原因。
3. 用户明确要求 DeepSeek 参与、视频执行、剪辑装配、数据复盘、reference audit、素材审计、runtime 诊断任务，必须 deepseek_passed 或 blocked，不得 completed。
4. fallback_local_only 只能作为窄范围低风险任务的记录边界，必须写 not_deepseek_conclusion=true，不能写 multi_agent_runtime_validated。
5. latest / dated log 必须保留 provider status、runner result、api_key_printed/api_key_written/env_file_read、token_usage_expectation_check。
```

## 14. 状态边界

```text
content_validation = not_advanced
send_ready = false
voice_validation = not_advanced
visual_master_locked = false
current_data_goal_anchor_ready = not_advanced
multi_agent_runtime_validated = false
code_modified = false
video_generated = false
media_committed = false
secret_committed = false
full_transcript_committed = false
deepseek_long_term_stability_claimed = false
```

## 15. 验证结果

```text
previous_commit_check = passed
policy_read_check = passed
runtime_provider_exists_check = passed
safe_runner_exists_check = passed
provider_cli_check = passed
runtime_doctor_check = passed_ready
smoke_test_check = passed_deepseek_passed_via_safe_runner
secret_scan = passed_for_new_report_and_new_latest_entry; staged diff scan required before commit
media_file_check = passed_no_media_file_added
status_promotion_check = passed_no_status_promotion_in_new_report_or_new_latest_entry
git_diff_check = passed
path_limited_staging_check = passed_only_report_and_latest_new_entry
```

提交前 staged diff 检查确认只提交本诊断报告和 `latest.md` 的本轮新增段落。
