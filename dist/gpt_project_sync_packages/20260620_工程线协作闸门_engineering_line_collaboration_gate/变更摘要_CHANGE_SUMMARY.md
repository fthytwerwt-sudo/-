# 变更摘要｜20260620 工程线协作闸门

## 1. 机制更新

- 新增 `GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md`。
- 在 `GPT数据源/03_总索引与阅读顺序.md` 中加入新机制文件和复杂任务 / 机制修补 / 自动化 / 多节点 / Codex 下发前的读取规则。
- 在 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 中加入 `engineering_line_collaboration_gate_needed（需要工程线协作闸门）` 状态动作。

## 2. Codex 执行层更新

- `codex_source/19_project_state_action_router.md` 增加 `engineering_line_collaboration_gate_needed（需要工程线协作闸门）`、`per_file_detail_plan_required（需要单文件细节方案）`、`engineering_overdesign_risk（工程化过度风险）` 的动作策略。
- `codex_source/00_codex_readme.md` 增加工程深度判断入口。
- `codex_source/01_execution_rules.md` 增加缺节点契约、数据契约、评估器、失败路由、链路记录时不得写 completed 的完成标准。

## 3. 同步包更新

- 生成本轮 GPT Project 资料同步包。
- 更新 `codex_log/current_local_artifact_paths.md` 中的当前推荐同步包路径。
- 增加本轮报告 `codex_log/engineering_line_collaboration/20260620_工程线协作闸门_engineering_line_collaboration_gate_report.md`。

## 4. 状态未推进

- `content_validation（内容验证）`: not_promoted（未推进）
- `send_ready（可发送状态）`: false（未开启）
- `publish_status（发布状态）`: not_promoted（未推进）
- `voice_validation（声音验证）`: not_promoted（未推进）
- `final_voice_validated（最终声音验证）`: false（未通过）
- `visual_master_locked（视觉母版锁定）`: false（未锁定）
- `production_readiness（生产可用状态）`: not_claimed（未声称）
