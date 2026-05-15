# GPT Project 上传说明｜20260515 DeepSeek runtime provider

## 1. 本包用途

本包用于把《视频工厂》的 DeepSeek 项目级运行时供应商机制同步到 GPT Project。

本轮核心结果：

- `已确认` DeepSeek runtime provider 已能从授权项目 runtime key source 自动加载，并只注入 DeepSeek 子进程 env。
- `已确认` runtime doctor 通过：`status = ready`、`can_call_deepseek = true`。
- `已确认` 三任务真实供料通过：`deepseek_passed_count = 3`、`fallback_count = 0`、`blocked_count = 0`。
- `待验证` 后续多轮真实项目任务中的长期稳定性。
- `待验证` `multi-agent runtime（多 agent 运行时）` 长期稳定性。

## 2. 上传目录

```text
/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_deepseek_runtime_provider/
```

## 3. 包含内容

- `GPT数据源/`：当前正式事实、目标态计划、OPC 协作机制、状态动作总控器、数据飞轮和数据目标执行总线。
- `codex_source/`：Codex 入口、执行规则、DeepSeek controller 协议、supply request schema 说明和状态动作路由。
- `codex_source/schemas/deepseek_supply_request.schema.json`：DeepSeek 供料请求 schema。
- `codex_source/fixtures/DeepSeek运行时供应商_deepseek_runtime_provider_supply_request_example.json`：runtime provider 任务卡 fixture。
- `scripts/`：runtime provider、doctor、multi-task runner、setup、safe runner、controller、readonly explorer。
- `本地运行配置_local_runtime/`：授权说明和 example 文件；不包含真实 `.local.json`。
- `codex_log/`：latest、dated log、路径索引、三张 runtime validation request。
- `dist/deepseek_runtime_validation/`：脱敏后的 doctor report 与 combined participation report。

## 4. 不包含内容

- 不包含 `.env`。
- 不包含 `.env.local`。
- 不包含 `.env.*`。
- 不包含 `deepseek_runtime_authorization.local.json`。
- 不包含任何 API key / token / secret 实际值。
- 不包含视频、音频、图片、字幕、时间线成品。
- 不包含 `dist/latest_review_pack/`。

## 5. 状态边界

- `technical_validation`: `passed_runtime_provider_local_validation`
- `content_validation`: `not_applicable_not_advanced`
- `send_ready`: `not_changed`
- `publish_status`: `not_changed`
- `voice_validation`: `not_changed`
- `final_voice_validated`: `not_changed`
- `visual_master_locked`: `not_changed`

## 6. 下一个目标

后续每个需要 DeepSeek 的 Codex 任务默认走 runtime provider；若 provider not ready，进入一次性 runtime setup；若用户要求 DeepSeek 必须参与而真实调用未通过，则整体任务 blocked。
