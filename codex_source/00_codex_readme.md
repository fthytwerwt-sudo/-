# codex_source 总入口

## 1. 这份文件是什么

本文件是《视频工厂》当前 Codex 执行层入口。

它负责回答：

- `codex_source/` 是干什么的
- 新会话最小先读什么
- 当前正式默认主线是什么
- 当前主读取分支是什么
- GPT 数据源与仓库不同步时，谁算源事实

## 2. `codex_source/` 负责什么

`codex_source/` 负责：

- 读取顺序
- 执行边界
- 仓库同步规则
- 已知状态分层
- 验证与汇报口径

它不负责：

- 项目脑正文
- 单条脚本内容
- 代码实现细节

这些分别属于 `project_source/` 与代码层。

## 3. 新会话最小接手入口

新 Codex 会话默认最少先读：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`

若任务偏执行规则，再补读：

4. `codex_source/01_execution_rules.md`
5. `codex_source/02_current_execution_context.md`
6. `codex_source/03_research_findings_bridge.md`

若任务命中展示路由，再补读：

7. `project_source/16_presentation_routing_rules.md`
8. `project_source/24_human_self_footage_light_ppt_routing_rules.md`

若任务命中选题 / 文案 / 价值判断，再补读：

9. `project_source/21_topic_selection_and_copywriting_rules.md`
10. `project_source/22_copy_mode_routing_rules.md`
11. `project_source/25_ai_knowledge_video_value_rules.md`
12. `codex_source/11_ai_knowledge_video_value_bridge.md`

若任务命中“当前正式事实 / 目标态计划 / 术语边界”，再补读：

13. `project_source/02_term_definitions_and_state_boundaries.md`
14. `project_source/07_current_formal_facts.md`
15. `project_source/09_target_state_plan.md`

若任务命中“什么算已知”，再补读：

16. `codex_source/12_codex_known_state_three_layer_rules.md`

## 4. 当前正式默认主线

当前正式默认主线 `已确认` 为：

- API 生成真人
- 用户录制素材
- 少量 PPT / 图片辅助
- 云端剪辑

必须同时默认理解：

- 结构跟着文案走
- `API生成真人段` 出现 1 次还是 2 次，是 block 路由结果
- pure PPT / 信息卡，不再是默认主线
- AI talking avatar / 数字人口播，不再是默认主线
- `云端剪辑 / cloud-only` 是当前正式方向，不等于 runtime 已稳定跑通
- `local preview` / `local mp4` 只能算辅助
- demo 只是链路锚点，不是质量样片

## 5. 当前主读取分支

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

只有同步回这个分支，才算：

- 新聊天默认正式已知
- 仓库正式状态已更新

## 6. GPT 数据源与仓库不同步时的硬规则

当前必须写死：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 当前仓库 `project_source/` 是 GPT 数据源中文文件集的同步镜像，不是独立源事实
- 只有写进仓库文件，并同步到 `codex/user-readable-map`，才算新聊天默认正式已知

执行层里对“什么算已知”的正式分层，统一看：

- `codex_source/12_codex_known_state_three_layer_rules.md`

## 7. 入口一句话

新会话默认先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`；当前正式默认主线按“API 生成真人 + 用户录制素材 + 少量 PPT / 图片 + 云端剪辑”理解，结构跟着文案走，`API生成真人段` 次数由 block 路由决定；若 GPT 数据源与仓库不同步，以已同步进 `project_source/`、`codex_source/` 并已回流 `codex/user-readable-map` 的事实为准。
