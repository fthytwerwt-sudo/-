# 20260515 数据目标执行总线日志

## 1. route_decision（路由判断）

- `project_route`：`video_factory（视频工厂）`
- `task_type`：`mechanism_or_route_fix / project_file_change / field_and_function_landing / execution_architecture_rewire / gpt_project_static_package_sync`
- `responsibility_layer`：`project_judgment_layer / mechanism_fix_layer / execution_layer / validation_layer / sync_layer`
- `large_task_gate`：`triggered`
- `lane`：`audit_lane -> standard_lane`
- `parallel`：`serial_only`

执行许可：

- `allowed_changes`：GPT 数据源入口、Codex 执行规则、DeepSeek 供料协议 / schema / fixture、日志、路径索引、GPT Project 静态上传包。
- `forbidden_changes`：不修改 `dist/latest_review_pack/`；不生成视频 / 音频 / 图片；不调用 TTS / 阿里 / 豆包 API；不读取 `.env`、`.env.swp`、API key、token、secret；不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。

## 2. audit_result（审计结果）

`13_目标驱动数据飞轮与文案执行闭环` 已定义目标飞轮、阈值、文案闸门、内容结构反馈、单主变量和 `next_video_execution_prompt（下一条视频执行 prompt）`。

缺口：

- `content_route_card V2（内容路由卡 V2）` 未默认承接 `data_goal_anchor（数据目标锚点）`。
- `script_to_timeline_map（文案到时间线映射表）` 未默认写明主短板、主变量和发布后验证指标。
- `editing_decision_pack（剪辑决策包）` 与 `assembly_decision_pack（装配决策包）` 原先更偏执行动作，没有把主变量、禁止变量和验证指标设为必填。
- DeepSeek 供料 request / schema 原先有 `current_goal`，但缺完整数据目标字段。
- Codex 执行规则原先要求 `next_video_execution_prompt`，但缺 `data_goal_alignment_check（数据目标对齐检查）` 作为完成前验收。

架构决策：

- `recommendation = both`
- 补强 13 文件，明确交接到执行总线。
- 新增 14 文件，作为全执行链总线，避免 13 变成臃肿的全能文件。

## 3. data_goal_execution_bus（数据目标执行总线）

已新增：

- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`

核心原则：

```text
数据目标定方向
素材证据定能做什么
人感质量定能不能发
Codex 负责编排和执行
DeepSeek 负责供料和风险提醒
ChatGPT / 用户负责最终判断
```

一句话：

```text
目标锁死，结构可变。
```

## 4. landing_scope（落地范围）

已补齐：

- GPT Project / ChatGPT 侧读取入口。
- Codex 执行前 `data_goal_anchor_gate（数据目标锚点闸门）`。
- DeepSeek supply request 数据目标字段。
- `content_route_card V2` 数据目标字段。
- `script_anchor_extraction_function` 数据目标字段。
- `editing_decision_pack` 数据目标字段。
- `assembly_decision_pack` 数据目标字段。
- `data_goal_alignment_check` 完成前验收字段。

Codex 可调整：

- segment 拆分
- 剪辑节奏
- 画面顺序
- 卡片位置
- API 图是否需要
- PPT 密度
- TTS 分句
- 装配顺序
- 降级方案

Codex 不得调整：

- current_stage_goal
- main_bottleneck
- primary_variable
- forbidden_variables
- success_metric
- failure_metric
- post_publish_validation_metric
- 用户 / ChatGPT 已锁定的数据目标判断

## 5. DeepSeek 供料状态

本轮供料请求：

- `codex_log/supply_requests/20260515_数据目标执行总线_data_goal_execution_bus_pre_supply_request.json`

controller 输出：

- `supply_source = blocked_missing_process_env_api_key`
- `deepseek_actual_participation = blocked_missing_process_env_api_key`
- `blocked_reason = missing_process_env_api_key`
- `env_file_read = false`
- `process_env_key_allowed = true`
- `process_env_key_present = false`
- `api_key_printed = false`
- `api_key_written = false`
- `not_deepseek_conclusion = true`

边界：

- 本轮没有读取 `.env` 补救。
- 本轮没有真实 DeepSeek token 消耗证据。
- 本轮供料结果不得写成 DeepSeek 结论。

## 6. status_boundary（状态边界）

- `已确认` 数据目标执行总线机制已写入。
- `已确认` 相关入口、执行规则、供料协议、schema、fixture、日志和上传包已同步。
- `待验证` 真实任务中是否稳定把剪辑 / 编排 / 供料锚定到数据目标。
- `待验证` 未来 DeepSeek 是否在真实数据目标供料中稳定通过。

未推进：

- `content_validation`
- `send_ready`
- `publish_status`
- `voice_validation`
- `final_voice_validated`
- `visual_master_locked`

## 7. 下一个目标

下一条真实视频执行前，ChatGPT / Codex / DeepSeek 都必须先读取 `data_goal_anchor（数据目标锚点）`；Codex 只能调整执行结构，不能改写目标锚点，并且必须在完成前输出 `data_goal_alignment_check（数据目标对齐检查）`。
