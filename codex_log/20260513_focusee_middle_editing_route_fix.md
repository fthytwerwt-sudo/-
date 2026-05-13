# 20260513｜FocuSee 中段剪辑路由修补

## 1. 本轮目标

- `已确认` 本轮只做《视频工厂》的中段剪辑机制修补。
- `已确认` 新增 FocuSee 录制层自带运镜边界：当用户录制素材来自 `FocuSee`，且已经自带 `3D Motion（3D 运镜）`、自动跟随、自动 zoom 或观看引导时，Codex 默认不再做二次 zoom / crop / 重新运镜。
- `已确认` Codex 的中段职责改为按最终文案识别时间码、段落、动作和证据窗口，做直接剪辑、保留原始运镜、删冗余，并衔接口播 / 字幕 / 卡片。
- `已确认` 本轮不生成视频，不修改媒体，不推进任何内容状态。

## 2. route_decision

```text
project_route: video_factory
task_type:
  - project_file_change
  - mechanism_or_route_fix
responsibility_layer:
  - mechanism_fix_layer
  - project_judgment_layer
  - execution_layer
  - validation_layer
  - sync_layer
large_task_gate:
  triggered: true
  reason: 本轮涉及剪辑机制、文案路由、执行规则和日志同步，多文件机制修补
  lane_recommendation: audit_lane -> standard_lane after impact check passed
  parallel_recommendation: serial_only
completion_relay_gate:
  triggered: true
  reason: 本轮要求多文件同步、剩余工作反查和日志回流，不能只改一个文件就停
execution_permission: granted
```

## 3. state_action_router

```text
input_signal: 用户新增 FocuSee 录屏层 3D 运镜，要求 Codex 不再默认做中段放大，只根据文案直接剪辑
current_project_state:
  - mechanism_repair_needed
  - editing_inference_needed
fact_source_arbitration:
  primary_source: 当前用户明确指令 + 本地 main 当前机制文件
  conflict_detected: partial
  conflict_resolution: 用户本轮明确指令指导本轮，并写回机制文件成为后续默认边界
inferred_state:
  - recording_layer_motion_baked_in
  - codex_secondary_zoom_should_be_disabled_by_default
confidence: high
trigger_mechanism:
  - editing_inference_function
  - Completion Relay Gate
selected_action:
  - 修正文案路由和剪辑推理规则
  - 新增 FocuSee 自带运镜素材的剪辑职责边界
forbidden_action:
  - 不生成视频
  - 不修改媒体
  - 不推进 content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked
done_when: 机制文件和日志同步完成，关键词与禁止状态检查通过，无剩余 must-fix
feedback_update_required: true
```

## 4. actual_read_files

| file | status |
| --- | --- |
| `AGENTS.md` | `read_ok` |
| `codex_source/00_codex_readme.md` | `read_ok` |
| `codex_log/latest.md` | `read_ok` |
| `GPT数据源/05_文案路由规则.md` | `read_ok` |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `read_ok` |
| `codex_source/19_project_state_action_router.md` | `read_ok` |
| `codex_source/01_execution_rules.md` | `read_ok` |
| `GPT数据源/08_当前正式事实.md` | `read_ok` |
| `codex_source/13_execution_lane_and_parallel_rules.md` | `read_ok` |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | `read_ok` |
| `local skills/` | `missing` |
| `~/.codex/skills/using-superpowers/SKILL.md` | `read_ok` |
| `~/.codex/skills/context-driven-development/SKILL.md` | `read_ok` |
| `~/.codex/skills/verification-before-completion/SKILL.md` | `read_ok` |

## 5. changed_files

- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260513_focusee_middle_editing_route_fix.md`

## 6. forbidden_status_check

- `content_validation`: not_changed
- `send_ready`: not_changed
- `publish_status`: not_changed
- `voice_validation`: not_changed
- `final_voice_validated`: not_changed
- `visual_master_locked`: not_changed
- `dist/latest_review_pack/`: not_modified
- media_generation: not_called
- external_api_call: not_called
- secret_read: not_read

## 7. validation_result

- keyword_check: passed
- forbidden_status_diff_check: passed
- git_diff_check: passed
- target_file_readback: passed
- impact_check: passed_minimal_sync_only

## 8. remaining_work_check

- `GPT数据源/05_文案路由规则.md` FocuSee 中段剪辑边界：done
- `editing_inference_function` 新状态与动作策略：done
- `codex_source/19_project_state_action_router.md` 执行侧同步：done
- `codex_source/01_execution_rules.md` 执行硬规则：done
- `codex_log/latest.md` 回写：done
- dated log 写入：done
- 媒体与动态状态禁止项：passed

## 9. sync_back_check

- latest_updated: true
- dated_log_created: true
- current_facts_updated_if_needed: not_needed，本轮不改变视频动态事实
- entry_files_updated_if_needed: not_needed，本轮不改变项目入口 / 分支 / 默认读取顺序
- gpt_project_upload_package_created: false，本轮不需要生成 GPT Project 上传包

## 10. next_target

下一条使用 FocuSee 录屏素材的真实执行任务中，验证 Codex 是否能按文案直接剪辑、保留原始 `3D Motion（3D 运镜）`，并在关键证据不清时选择 `blocked_or_needs_rerecording（阻断或需补录）`，而不是默认二次放大。
