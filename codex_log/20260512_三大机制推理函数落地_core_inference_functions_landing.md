# 20260512｜三大机制推理函数落地 core inference functions landing

## 1. route_decision（本轮路由判断）

```text
project_route: video_factory
task_type:
  - mechanism_or_route_fix
  - project_file_change
responsibility_layer:
  - mechanism_fix_layer
  - project_judgment_layer
  - execution_layer
  - validation_layer
  - sync_layer
large_task_gate:
  triggered: true
  lane_recommendation: audit_lane -> standard_lane after impact check passed
  parallel_recommendation: serial_only
execution_permission: granted
```

`已确认` 本轮命中《视频工厂》，只做机制 / 路由 / 执行 / 验收口径补全，不做视频、声音、发布或媒体产物修改。

## 2. state_action_router（项目状态动作总控判断）

```text
current_project_state:
  - mechanism_repair_needed
  - editing_inference_needed
  - content_route_needed
  - quality_review_needed
trigger_mechanism:
  - editing_inference_function
  - content_route_inference_function
  - quality_issue_classifier
  - Completion Relay Gate
selected_action: 一次性补齐三个函数、入口调用、执行规则、fixture、latest 和 dated log。
forbidden_action:
  - 不生成媒体
  - 不调用 API
  - 不读取 secret
  - 不推进动态状态
```

## 3. completion_relay_gate（补全接力闸门）

```text
triggered: true
chatgpt_horizontal_context_loaded: true
codex_secondary_completion_required: true
required_output_inventory: created
child_task_graph: created
remaining_work_check: required before completed
sync_back_check: required before completed
```

## 4. impact_check（影响面检查）

```text
affected_layers:
  - entry_routing_layer
  - project_judgment_layer
  - mechanism_fix_layer
  - execution_layer
  - validation_layer
  - sync_layer
media_files_touched: false
api_or_secret_needed: false
gpt_project_upload_package_needed_now: false
branch_sync_needed: true
```

## 5. changed_files（实际修改文件）

1. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
   - 新增三大机制推理函数完整项目侧定义。
   - 三个函数均包含 `input_signal / observed_evidence / state_inference / action_policy / validation_rule / blocked_if / feedback_update`。
2. `codex_source/19_project_state_action_router.md`
   - 新增 Codex 执行侧三函数触发、输出、完成判断和 blocked 规则。
3. `codex_source/01_execution_rules.md`
   - 新增三大机制推理函数前置闸门。
   - 命中相关任务时，未输出对应函数不得写 `completed（已完成）`。
4. `GPT数据源/05_文案路由规则.md`
   - `content_route_card（内容路由卡）` 明确为 `content_route_inference_function（内容路由推理函数）` 输出。
   - `editing_decision_pack（剪辑决策包）` 明确由 `editing_inference_function（剪辑推理函数）` 推理后生成。
5. `GPT数据源/07_AI知识类视频价值规则.md`
   - `quality_lock_card（质量锁卡）` 明确必须调用 `quality_issue_classifier（质量短板分类器）`。
6. `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
   - 补充三函数在 OPC 闭环中的位置和禁止误写。
7. `GPT数据源/01_项目系统提示词.md`
   - 补充 GPT Project / ChatGPT 侧硬规则，命中内容承载、剪辑判断、质量复审时必须调用对应函数。
8. `GPT数据源/03_总索引与阅读顺序.md`
   - 明确三函数承载在 `11_项目状态动作总控器_机制推理层.md`。
9. `codex_source/00_codex_readme.md`
   - 补充 Codex 最小接手入口中的三函数执行入口。
10. `codex_source/fixtures/mechanism_inference_function_cases.json`
    - 新增三函数各 2 个最小测试样例。
11. `codex_log/latest.md`
    - 新增本轮摘要。
12. `codex_log/20260512_三大机制推理函数落地_core_inference_functions_landing.md`
    - 新增本 dated log。

## 6. fixture_or_test_cases（fixture / 最小测试样例）

路径：

```text
codex_source/fixtures/mechanism_inference_function_cases.json
```

覆盖：

- `editing_inference_function`
  - `editing_zoom_needed_button_too_small`
  - `editing_zoom_breaks_context_keep_full_frame`
- `content_route_inference_function`
  - `content_route_user_recording_middle_api_once`
  - `content_route_missing_validation_goal_blocked`
- `quality_issue_classifier`
  - `quality_demo_feeling_editing_issue_primary`
  - `quality_voice_weird_missing_audio_blocked`

## 7. validation_results（验证结果）

本日志对应验证要求：

- `manual_structure_check`: 三函数字段完整。
- `call_chain_check`: `GPT数据源/11`、`codex_source/19`、`codex_source/01`、`GPT数据源/05`、`GPT数据源/07` 已建立调用链。
- `keyword_check`: 三函数与 `state_inference / action_policy / validation_rule / blocked_if / feedback_update` 均可检索。
- `fixture_check`: fixture 文件可用 `json.tool` 解析，三函数各至少两个 case。
- `forbidden_status_check`: 不推进禁止状态。
- `media_check`: 不修改媒体文件，不修改 `dist/latest_review_pack/`。
- `api_secret_check`: 不读取 `.env`、`.env.swp`、secret，不调用外部 API。

本轮提交前必须以实际验证输出为准；若任一验证失败，必须继续修补，不得写 `completed（已完成）`。

## 8. sync_back_check（同步回写检查）

```text
latest_updated: true
dated_log_created: true
entry_files_updated_if_needed: true
gpt_project_upload_package_needed: false
current_facts_updated: false
reason_current_facts_updated_or_not: 本轮不改变视频动态事实；三函数机制事实已写入 GPT数据源/11、05、07、10、01、03 与 codex_source 执行入口。
```

## 9. remaining_work_check（剩余工作检查）

```text
must_fix_remaining: none
should_fix_later:
  - 用下一条真实内容执行或复审任务验证三函数长期稳定性
blocked_items: none
unnecessary_items:
  - 不生成 GPT Project 静态上传包
  - 不更新 current_local_artifact_paths
  - 不更新 current_publish_target / current_publish_target_light_evidence
  - 不修改 GPT 数据源/ 历史静态目录
```

## 10. completion_state（完成状态）

```text
completion_state: completed
```

本字段只表示本轮机制落地闭环完成；长期稳定性仍需下一条真实内容执行或质量复审任务验证。

## 11. 未推进状态声明

```text
content_validation: not_changed
send_ready: not_changed
publish_status: not_changed
voice_validation: not_changed
final_voice_validated: not_changed
visual_master_locked: not_changed
```

## 12. 下一个目标

用下一条真实内容执行或质量复审任务验证三大函数能否稳定做到：先判信号和证据，再输出卡片 / 决策包 / blocked，而不是只写动作名、卡片字段或技术通过结论。
