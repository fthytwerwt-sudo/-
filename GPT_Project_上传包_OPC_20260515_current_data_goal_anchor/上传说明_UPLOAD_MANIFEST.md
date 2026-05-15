# GPT Project 上传说明｜OPC current_data_goal_anchor

## 1. 包信息

- `package_name`: `GPT_Project_上传包_OPC_20260515_current_data_goal_anchor`
- `package_path`: `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_current_data_goal_anchor/`
- `generated_at`: `2026-05-15 19:48 CST`
- `package_role`: `GPT Project / ChatGPT 静态同步包`
- `project_route`: `video_factory`

## 2. 本包用途

本包用于把《视频工厂｜OPC 一人公司 AI 闭环验证系统》的当前实例数据目标锚点入口同步给 GPT Project / ChatGPT。

核心新增入口：

- `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`

职责边界：

- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 继续负责目标飞轮、阈值、数据诊断、文案闸门和 `next_video_execution_prompt`。
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` 继续负责执行链如何使用 `data_goal_anchor`。
- `codex_log/current_data_goal_anchor.md` 只负责当前这一条 / 下一条视频实际使用的锚点实例。

## 3. 当前状态边界

- `mechanism_written`: `true`
- `current_anchor_instance_status`: `waiting_data`
- `current_anchor_instance_ready`: `false`
- `real_video_execution_stability`: `待验证`
- `data_flywheel_real_effect`: `待验证`
- `deepseek_real_participation_this_round`: `blocked_missing_process_env_api_key`
- `gpt_project_ui_uploaded`: `false`

本包生成不等于用户已经上传 GPT Project UI，也不等于 GPT Project UI 已同步成功。

## 4. 包内文件

### GPT数据源

- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/02_术语定义与状态边界.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/09_目标态计划.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`

### Codex 执行层

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`
- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json`

### 当前日志与指针

- `codex_log/current_data_goal_anchor.md`
- `codex_log/latest.md`
- `codex_log/20260515_current_data_goal_anchor_instance.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/supply_requests/20260515_current_data_goal_anchor_pre_supply_request.json`

## 5. 上传后读取规则

GPT Project / ChatGPT 命中文案修改、下一条视频、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态同步时，必须优先读取：

1. `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
2. `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
3. `codex_log/current_data_goal_anchor.md`

缺 `codex_log/current_data_goal_anchor.md` 时，不得进入正式视频执行。

当 `anchor_instance_status = waiting_data / draft` 时，只能做假设版锚点、机制接线、供料任务卡或 blocked 说明，不得写正式数据驱动执行 ready。

## 6. 禁止误读

- 不得把本包写成当前锚点已经 ready。
- 不得把本包写成数据飞轮已真实跑通。
- 不得把本包写成 DeepSeek 每轮稳定供料已长期验证。
- 不得把本包写成 Codex 后续一定不会偏。
- 不得推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- 不得生成或修改视频 / 音频 / 图片 / 字幕 / 时间线成品。
