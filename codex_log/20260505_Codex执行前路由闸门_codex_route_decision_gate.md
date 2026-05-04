# Codex 执行前路由闸门 codex_route_decision_gate

## 1. 本轮任务目标

- `已确认` 本轮只把《视频工厂》的 Codex 执行机制升级为 `route_decision_gate（执行前路由闸门）`。
- `已确认` 目标是让 Codex 每次执行前先判断项目路由、任务类型、责任层级、必读文件、读取状态、阻断条件、允许修改范围、禁止修改范围和执行许可。
- `已确认` 本轮不是修改视频，不是生成样片，不是继续项目清理，不是开发 multi-agent，不是调整剪辑风格。

## 2. 修改文件

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_log/latest.md（最新摘要）`
5. `codex_log/20260505_Codex执行前路由闸门_codex_route_decision_gate.md（本日志）`

## 3. route_decision 机制摘要

- `AGENTS.md` 新增 `## 2.6 Codex 执行前路由闸门 route_decision_gate`。
- `codex_source/01_execution_rules.md` 新增 `## 2A. 执行前 route_decision 闸门`。
- 每次任务必须先输出 `route_decision（路由判断）`。
- 没有 `route_decision（路由判断）`，或关键字段缺失时，Codex 必须停止，不得修改文件、生成产物、删除文件、提交 commit 或 push。
- `route_decision（路由判断）` 至少包含：`project_route（项目路由）`、`task_type（任务类型）`、`responsibility_layer（责任层级）`、`must_read_files（本轮必读文件）`、`read_status（读取状态）`、`allowed_changes（允许修改范围）`、`forbidden_changes（禁止修改范围）`、`blocked_if（阻断条件）`、`execution_permission（执行许可）`。

## 4. 任务类型映射摘要

`codex_source/01_execution_rules.md` 已补 `## 2B. 任务类型与必读文件映射`，覆盖：

1. 项目文件修改 / 机制修补 / 路由修补
2. 视频样片 / 成片 / 样片回炉
3. 文案写作 / 改写
4. 复盘 / 诊断 / 审核
5. 数据记录 / 灰度复盘
6. 本地文件治理 / 工作区治理
7. execution lane / multi-agent / parallel 机制

## 5. 哪些文件必须读

本轮实际必读并已读取：

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_log/latest.md（最新摘要）`
5. 全局 `~/.codex/skills/using-superpowers/SKILL.md`
6. 全局 `~/.codex/skills/context-driven-development/SKILL.md`
7. 全局 `~/.codex/skills/verification-before-completion/SKILL.md`

`已确认` 当前仓库本地 `skills/` 目录不存在；相关 skills 已回退读取全局 `~/.codex/skills`。

## 6. blocked 条件

新规则已写清以下情况必须 blocked：

- 项目未路由清楚。
- 任务类型未判断清楚。
- 责任层级未判断清楚。
- 关键必读文件 `missing（文件不存在）` 或 `unreadable（无法读取）`。
- 允许修改范围不清楚。
- 禁止修改范围不清楚。
- 需要新建外部工作区但用户未明确授权。
- 需要删除 / 移动 / 替换高风险文件但用户未明确授权。
- 需要把技术验证写成内容验证。
- 需要把中间态写成完成态。

## 7. 未执行高风险动作

- `已确认` 未修改视频产物。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前发布状态。
- `已确认` 未修改 `content_validation（内容验证）`。
- `已确认` 未修改 `send_ready（可发送状态）`。
- `已确认` 未处理 `素材录制/（用户录制原始素材目录）`。
- `已确认` 未新建外部工作区。
- `已确认` 未新建 fresh clone、audit clone、clean clone、临时 clone 或外部 worktree。
- `已确认` 未执行 Git GC / prune / repack。
- `已确认` 未执行 Git LFS / history rewrite。
- `已确认` 未 force push。

## 8. 验证结果

- `已确认` 已运行 `git diff --check`，无报错输出。
- `已确认` 已重新读取 `AGENTS.md`、`codex_source/01_execution_rules.md`、`codex_source/00_codex_readme.md` 和本日志。
- `已确认` `git diff --name-only` 只显示 `AGENTS.md`、`codex_log/latest.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`；未显示视频产物、当前发布状态文件或 `素材录制/`。

## 9. 下一个目标

后续新会话在任何文件修改或执行前，先给出 `route_decision（路由判断）` 与 `read_status（读取状态）`，再判断是否允许执行。
