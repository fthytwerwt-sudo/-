# 20260515 mandatory DeepSeek supply loop

## 本轮定位

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、执行规则修改、脚本字段、schema、fixture、日志和 GPT Project 静态包同步。
- `已确认` 本轮不生成视频、不生成音频、不生成图片、不读取 `.env` / `.env.swp` / API key / token / secret，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）`。

## 机制变更

- `已确认` `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）` 已写入 DeepSeek 协议、Codex 执行规则、OPC 总纲、状态动作总控器、Codex 状态动作路由和 GPT Project 短路由说明。
- `已确认` DeepSeek 已从 `if_needed_trigger（按需触发）` 升级为 `mandatory_by_default（默认强制）`：每轮 Codex 任务默认先进入 `deepseek_supply_gate（DeepSeek 供料闸门）`。
- `已确认` 每轮默认必须创建 `supply_request（供料请求任务卡）`，并尝试执行前供料与执行后风险复核。
- `已确认` `fallback_local_only（本地兜底）` 明确不得写成 DeepSeek 结论。
- `已确认` token 未观察到减少时，不得写 DeepSeek 已深度参与。

## Codex 二次补全责任

- `已确认` `codex_vertical_completion（Codex 二次补全）` 已写入规则：Codex 必须补齐受影响文件、字段、脚本、schema、fixture、日志、路径索引和 GPT Project 静态包。
- `已确认` 只写协议或单个入口文件，不得写机制修补完成。
- `已确认` Codex 最终回报必须包含 `deepseek_participation_report（DeepSeek 参与报告）` 和 `token_usage_expectation_check（token 使用预期检查）`。

## 脚本 / schema / fixture

- `已更新` `scripts/deepseek_supply_controller.py`：新增 `deepseek_supply_gate`、`deepseek_participation_report`、`token_usage_expectation_check`、`post_risk_review` 输出。
- `已更新` `scripts/deepseek_readonly_explorer.py`：补齐 `safe_call_mode` 与 `deepseek_actual_participation` 输出。
- `已更新` `codex_source/schemas/deepseek_supply_request.schema.json`：新增强制供料字段，并新增 `mandatory_pre_supply`、`mandatory_post_risk_review` trigger reason。
- `已新增` `codex_source/fixtures/DeepSeek强制供料循环_mandatory_supply_loop_cases.json`，覆盖 8 个强制供料与失败边界 case。
- `已更新` 既有 `deepseek_supply_request_*.json` fixture，补齐强制供料字段和 token / fallback 阻断语义。

## 本轮 DeepSeek 参与报告

- `已确认` 本轮 controller 供料验证走 `fallback_local_only（本地兜底）`。
- `已确认` 本轮没有读取 `.env`，没有打印或写入 API key，`env_file_read = false`、`api_key_printed = false`、`api_key_written = false`。
- `已确认` 本轮没有真实消耗 DeepSeek token；因此不得写 DeepSeek 已深度参与。
- `待验证` 下一轮真实任务仍需验证 process environment 中 `DEEPSEEK_API_KEY` 可用时的真实调用、token 递减和执行后风险复核稳定性。

## GPT Project 静态包

- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/`。
- `已生成` 上传说明：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/上传说明_UPLOAD_MANIFEST.md`。
- `已确认` 包生成不等于用户已上传 GPT Project UI；GitHub / 本地 `main` 仍是主事实源。

## 状态边界

- `已确认` 本轮机制修补链路已落库并通过本地语法 / JSON / schema / keyword / forbidden status / package manifest 检查。
- `待验证` DeepSeek 真实任务稳定供料、token 递减和 multi-agent runtime 稳定性仍需后续真实任务验证。

## 下一个目标

下一轮真实 Codex 任务默认先进入 `deepseek_supply_gate（DeepSeek 供料闸门）`，并在最终回报中明确 DeepSeek 是否真实调用、token 是否应减少、是否 fallback，以及 Codex 是否完成二次补全。
