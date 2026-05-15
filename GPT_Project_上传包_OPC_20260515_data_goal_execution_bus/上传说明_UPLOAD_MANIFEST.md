# GPT Project 上传说明

## 1. package_identity（包身份）

- `package_name`：`GPT_Project_上传包_OPC_20260515_data_goal_execution_bus`
- `canonical_local_path`：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_goal_execution_bus/`
- `created_for`：`数据目标执行总线双重补全`
- `status`：`local_package_generated`

## 2. 使用边界

- 本包用于 GPT Project 静态上传 / 同步。
- 本包不等于 GPT Project UI 已经上传。
- GitHub / 本地 `main` 当前仓库文件仍高于本静态包。
- 本包只代表机制、入口、执行规则、schema、fixture、日志和路径索引同步，不代表真实数据飞轮已跑通。

## 3. included_files（包含文件）

### GPT 数据源

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

### Codex 执行规则同步件

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`
- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `codex_source/fixtures/数据目标锚点供料_data_goal_anchor_supply_request_example.json`

### 日志与路径索引

- `codex_log/latest.md`
- `codex_log/20260515_data_goal_execution_bus.md`
- `codex_log/current_local_artifact_paths.md`

## 4. new_default_rule（新默认规则）

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

## 5. not_included_or_not_claimed（未包含 / 不声明）

- 不包含视频、音频、图片或 `dist/latest_review_pack/` 媒体产物。
- 不包含 `.env`、`.env.swp`、API key、token、secret。
- 不声明 `content_validation（内容验证）` 已通过。
- 不声明 `send_ready（可发送状态）` 为 true。
- 不声明 `publish_status（发布状态）` 已推进。
- 不声明 DeepSeek / multi-agent runtime 已长期稳定跑通。
- 不声明数据目标执行总线已经在真实视频任务中稳定验证。

## 6. 下一个目标

上传到 GPT Project 后，下一条真实视频执行前必须先读取 `data_goal_anchor（数据目标锚点）`，并要求 Codex 在完成前输出 `data_goal_alignment_check（数据目标对齐检查）`。
