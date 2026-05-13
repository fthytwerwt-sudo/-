# 20260514｜content_route_card V2 与机制推理测试样例补全

## 本轮目标

只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的双重补全：

1. 为最近三条机制补齐 `mechanism_inference_function_cases.json（机制推理函数测试样例）`。
2. 新增 `content_route_card V2（内容路由卡 V2）` 输出模板，让真实视频执行前统一判断开头、中段、卡片、证据、API 人物、PPT、Prompt 尾卡和 blocked 条件。

本轮不生成视频，不修改媒体，不推进任何内容状态。

## route_decision

```text
project_route: video_factory
task_type:
  - project_file_change
  - mechanism_or_route_fix
  - validation_template_fix
responsibility_layer:
  - mechanism_fix_layer
  - validation_layer
  - execution_layer
  - sync_layer
large_task_gate:
  triggered: true
  reason: 本轮涉及测试样例、内容路由卡模板、执行规则和日志同步，多文件机制补全
  lane_recommendation: audit_lane -> standard_lane after impact check passed
  parallel_recommendation: serial_only
completion_relay_gate:
  triggered: true
  reason: 本轮需要多文件影响面扫描、测试样例补全、模板写入、日志回流和剩余工作反查，不能只改单个文件
execution_permission: allowed_after_must_read_passed
```

## state_action_router

```text
input_signal: 用户要求双重补全，补 mechanism_inference_function_cases.json 与 content_route_card V2 输出模板
current_project_state:
  - mechanism_repair_needed
  - content_route_needed
  - editing_inference_needed
  - validation_template_fix_needed
fact_source_arbitration:
  primary_source: GitHub main 当前机制文件 + 用户本轮明确指令
  conflict_detected:
    - 新增机制已写入规则，但 fixture 样例未补齐
    - content_route_card 字段已扩展，但缺统一 V2 输出模板
  conflict_resolution:
    - 本轮补样例与模板，不推进媒体和动态状态
inferred_state:
  - fixture_cases_missing_for_new_mechanisms
  - content_route_card_v2_template_needed
confidence: high
trigger_mechanism:
  - content_route_inference_function
  - editing_inference_function
  - Completion Relay Gate
selected_action:
  - 补齐机制推理函数最小测试样例
  - 新增或补强 content_route_card V2 输出模板
  - 同步 Codex 执行侧完成标准
forbidden_action:
  - 不生成视频
  - 不修改媒体
  - 不推进 content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked
  - 不调用 API
done_when:
  - fixture cases 和 V2 模板写入、JSON 可解析、关键词检查通过、日志同步完成
blocked_if:
  - 关键文件缺失
  - JSON 无法安全修改或解析
  - 需要真实媒体或 API 才能继续
feedback_update_required: true
```

## actual_read_files

- `AGENTS.md`: read_ok
- `codex_source/00_codex_readme.md`: read_ok
- `codex_source/01_execution_rules.md`: read_ok
- `codex_log/latest.md`: read_ok
- `codex_source/fixtures/mechanism_inference_function_cases.json`: read_ok
- `GPT数据源/05_文案路由规则.md`: read_ok
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`: read_ok
- `codex_source/19_project_state_action_router.md`: read_ok
- `GPT数据源/08_当前正式事实.md`: read_ok
- `GPT数据源/03_总索引与阅读顺序.md`: read_ok
- `codex_source/13_execution_lane_and_parallel_rules.md`: read_ok
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`: read_ok

## changed_files

- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `codex_log/latest.md`
- `codex_log/20260514_content_route_card_v2_and_fixture_cases.md`

## fixture_cases_added

- `editing_focusee_direct_cut_keep_motion`
- `editing_focusee_evidence_unclear_blocked`
- `content_route_opening_meme_gif_ai_money`
- `content_route_opening_element_doll_low_pressure`
- `content_route_card_reversal_between_negative_positive`
- `content_route_card_summary_final_closure`
- `editing_card_interrupts_focusee_evidence_blocked`

## content_route_card_v2_summary

`content_route_card V2（内容路由卡 V2）` 已写入 `GPT数据源/05_文案路由规则.md`，作为真实视频执行前统一判断卡，覆盖：

- `validation_goal（本轮验证目标）`
- `opening_route_decision（开头路由判断）`
- `core_evidence（核心证据）`
- `middle_carrier_decision（中段承载判断）`
- `focusee_middle_editing_decision（FocuSee 中段剪辑判断）`
- `card_placement_decision（卡片位置判断）`
- `api_human_usage（API 生成人物使用方式）`
- `ppt_usage（少量 PPT 使用方式）`
- `prompt_tail_card_usage（Prompt 尾卡使用方式）`
- `flow_flex_reason（为什么本条不照搬固定流程）`
- `blocked_if（阻断条件）`

## JSON parse validation

- `before_change`: passed，旧 JSON 可解析，旧 case 数量为 6。
- `after_change`: passed，修改后 JSON 可解析，case 数量为 13。
- `required_cases_present`: true。
- `old_cases_retained`: true。

## forbidden_status_check

- 未修改 `dist/latest_review_pack/`。
- 未生成或修改视频、图片、音频、字幕、时间线、TTS 或任何媒体产物。
- 未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- 未读取 `.env / .env.swp / API key / token / secret`。
- 未调用 DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。

## remaining_work_check

- `mechanism_inference_function_cases.json` 新增 7 个目标 case：done。
- 旧 6 个 case 保留：done。
- JSON 可解析：done。
- `content_route_card V2` 模板写入：done。
- Codex 执行侧缺关键字段不得进入视频执行：done。
- latest 同步：done。
- dated log 创建：done。
- 真实视频执行效果：待验证，不在本轮推进。

## sync_back_check

- `GPT数据源/05_文案路由规则.md`: synced
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`: synced
- `codex_source/19_project_state_action_router.md`: synced
- `codex_source/01_execution_rules.md`: synced
- `GPT数据源/03_总索引与阅读顺序.md`: synced
- `codex_log/latest.md`: synced
- `codex_log/20260514_content_route_card_v2_and_fixture_cases.md`: created

## next_target

下一条真实视频执行前，用 `content_route_card V2（内容路由卡 V2）` 验证 Codex / ChatGPT 能否一次性判断开头、中段、卡片、证据、API 人物、PPT、Prompt 尾卡和 blocked 条件；真实视频效果仍为 `待验证`。
