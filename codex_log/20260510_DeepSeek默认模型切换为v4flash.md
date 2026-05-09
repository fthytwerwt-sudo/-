# DeepSeek 默认模型切换为 v4-flash

## 1. 本轮目标

- `项目`: 《视频工厂》
- `目标`: 将 DeepSeek 默认供料模型从 `deepseek-v4-pro` 切换为 `deepseek-v4-flash`
- `升级模型`: 保留 `deepseek-v4-pro` 作为复杂任务备用 / 升级模型
- `执行边界`: 不生成视频，不推进发布状态，不让 DeepSeek 写文件，不把模型切换写成稳定供料

## 2. 模型策略

- `default_supply_model`: `deepseek-v4-flash`
- `escalation_model`: `deepseek-v4-pro`

默认使用 `deepseek-v4-flash` 的任务：

- `file_map（文件地图）`
- `missing_files（缺失文件）`
- `context_summary（上下文摘要）`
- 普通 `risk_report（风险报告）`
- 复盘文件地图
- 标准提取

保留 `deepseek-v4-pro` 的升级场景：

- 多文件冲突
- 复杂机制判断
- 长任务审计
- 多轮供料包合并
- Flash 多次失败后升级
- Codex 明确标记 `after_read_gap（读完仍有缺口）` 且 fallback 不足

## 3. 修改文件

- `scripts/deepseek_readonly_explorer.py`
  - `DEFAULT_MODEL = "deepseek-v4-flash"`
  - `ESCALATION_MODEL = "deepseek-v4-pro"`
- `.env.example`
  - `DEEPSEEK_MODEL=deepseek-v4-flash`
  - `DEEPSEEK_ESCALATION_MODEL=deepseek-v4-pro`
- `codex_source/16_deepseek_readonly_explorer_rules.md`
  - 同步默认模型与升级模型策略
- `codex_source/17_deepseek_supply_controller_protocol.md`
  - 新增 `model routing（模型路由）`
- `codex_source/18_deepseek_supply_request_schema.md`
  - 补充后续 `preferred_model（优先模型）` 扩展边界
- `GPT数据源/08_当前正式事实.md`
  - 只同步 DeepSeek 默认模型状态，不改其他项目事实
- `codex_log/latest.md`
  - 记录本轮摘要

## 4. `.env` 本地状态

- `.env_exists`: `true`
- `DEEPSEEK_API_KEY`: `present_nonempty`
- `DEEPSEEK_MODEL`: `deepseek-v4-flash`
- `.env local updated`: `true`
- `.env committed`: `false`

说明：

- 本轮只本地修改 `.env` 的 `DEEPSEEK_MODEL` 变量。
- 本轮未打印 `.env` 全文。
- 本轮未打印 API key。
- 本轮不得 stage / commit `.env`。

## 5. 验证

- `py_compile`: `passed`
  - `scripts/deepseek_readonly_explorer.py`
  - `scripts/deepseek_supply_controller.py`
- `smoke_test`: `passed`
- `smoke_test_model`: `deepseek-v4-flash`
- `smoke_test_output`: `dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md`
- `multi_agent_runtime_validation`: `not_started`

## 6. 边界检查

- `已确认` 本轮没有修改视频产物。
- `已确认` 本轮没有修改音频 / TTS / voice trial 产物。
- `已确认` 本轮没有修改图片 / 卡片 / 素材产物。
- `已确认` 本轮没有修改 `dist/latest_review_pack/`。
- `已确认` 本轮没有修改 `content_validation`。
- `已确认` 本轮没有修改 `send_ready`。
- `已确认` 本轮没有修改 `publish_status`。
- `已确认` 本轮没有修改 `voice_validation`。
- `已确认` 本轮没有修改 `final_voice_validated`。
- `已确认` 本轮没有把 Flash 切换写成 DeepSeek 稳定供料。
- `已确认` 本轮没有把 smoke test 写成完整 `multi-agent runtime（多 agent 运行时）` 已跑通。

## 7. 一句话结论

本轮已把 DeepSeek 默认供料模型切换为 `deepseek-v4-flash`，并保留 `deepseek-v4-pro` 作为升级模型；smoke test 已用 `deepseek-v4-flash` 通过，但这只证明最小配置链路通过，不代表真实任务稳定性已验证。

## 8. 下一个目标

用 `deepseek-v4-flash` 跑一次真实小步供料任务，观察是否比 Pro 更稳定或更快。
