# 20260526｜mandatory_commit_push_gate 强制提交推送闸门

## 任务定位

- `已确认` 本轮只做机制修补 / 路由修补 / Codex 执行规则修补。
- `已确认` 不生成媒体，不修改 `dist/` 媒体产物，不推进视频、声音、内容或发布状态。
- `已确认` 核心机制名为 `mandatory_commit_push_gate（强制提交推送闸门）`。

## route_decision

```text
project_route = video_factory
task_type = mechanism_repair + project_file_change + codex_execution_rule_fix
responsibility_layer = entry_routing_layer + execution_layer + validation_layer + sync_layer + mechanism_fix_layer
media_generation = false
dist_media_write = false
large_task_gate = triggered
lane_recommendation = serial_only
write_owner = Codex Integrator
```

## DeepSeek supply gate

- `pre_supply_request`: `codex_log/supply_requests/20260526_mandatory_commit_push_gate_pre_supply_request.json`
- `post_risk_review_request`: `codex_log/supply_requests/20260526_mandatory_commit_push_gate_post_risk_review_request.json`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `not_deepseek_conclusion = false`
- `api_key_printed = false`
- `api_key_written = false`
- `env_file_read = false`
- `token_usage_observed_or_user_check_required = token_decrement_expected`
- `multi_agent_runtime_validation = not_started`

## 规则写入

`mandatory_commit_push_gate` 已写入以下长期入口：

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/10_codex_multi_agent_prompt_library.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`

## 完成标准更新

```text
completed:
  required_if_repo_files_changed:
    - relevant_files_committed = true
    - pushed_to_current_reading_branch = true
    - remote_head_verified = true
    - unrelated_dirty_files_not_committed = true
    - secret_scan_passed = true
```

本地文件已改但未 push / 未远端校验时，不得写 `completed`；只能写：

```text
partial_completed:
  reason: local_changes_done_but_not_pushed

blocked:
  reason:
    - push_failed
    - current_branch_unclear
    - unrelated_dirty_files_cannot_be_isolated
    - secret_scan_failed
    - remote_head_not_verified
```

## ChatGPT -> Codex prompt 模板更新

后续 Codex prompt 的 `Done when` 默认追加：

```text
Git completion requirement:
- If any repository file is created or modified, this task is not completed until:
  1. relevant files are explicitly staged
  2. commit is created
  3. commit is pushed to the current reading branch
  4. remote HEAD is verified
  5. unrelated dirty / untracked files are not included
- If push cannot be completed, report blocked or partial_completed. Do not write completed.
```

## Codex final report 更新

所有最终回报必须默认包含：

```text
git_sync_status:
  current_branch:
  files_changed:
  files_staged:
  commit_sha:
  pushed:
  remote_head_verified:
  unrelated_dirty_files:
  secret_scan:
  completed_allowed:
```

## sync_back_check 更新

`sync_back_check` 必须检查：

- `latest_updated`
- `dated_log_created`
- `commit_created`
- `push_succeeded`
- `remote_head_verified`
- `remote_commit_readable`
- `uncommitted_related_files`
- `unrelated_dirty_files_not_committed`
- `secret_scan_passed`

## status_boundaries

- `media_generated = false`
- `dist_media_modified = false`
- `content_validation = not_advanced`
- `voice_validation = not_advanced`
- `send_ready = false`
- `final_voice_validated = false`
- `visual_master_locked = false`
