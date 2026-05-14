# 上传说明 UPLOAD_MANIFEST

## 包身份

- `package_name`: `GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop`
- `package_type`: `GPT Project 静态上传包`
- `created_for`: `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`
- `canonical_local_path`: `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/`

## 本包包含

- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`
- `codex_source/fixtures/DeepSeek强制供料循环_mandatory_supply_loop_cases.json`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `scripts/deepseek_supply_controller.py`
- `scripts/deepseek_readonly_explorer.py`
- `Codex执行规则摘要_codex_execution_summary.md`
- `codex_log/latest.md`
- `codex_log/20260515_mandatory_deepseek_supply_loop.md`
- `codex_log/current_local_artifact_paths.md`

## 上传边界

- `已确认` 本包只做 GPT Project 静态同步，不是实时事实库。
- `已确认` GitHub / 本地 `main` 仓库文件仍是主事实源。
- `已确认` 本包生成不代表用户已上传到 GPT Project UI。
- `已确认` 本包生成不代表 DeepSeek token 已减少。
- `待验证` 下一轮真实任务仍需验证 DeepSeek 真实调用、token 递减和执行后风险复核稳定性。

## 禁止误读

- 不代表 `content_validation（内容验证）` 通过。
- 不代表 `send_ready（可发送状态）` 变成 true。
- 不代表 `publish_status（发布状态）` 推进。
- 不代表 `voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）` 推进。
- 不代表 `multi-agent runtime（多 agent 运行时）` 已稳定跑通。
