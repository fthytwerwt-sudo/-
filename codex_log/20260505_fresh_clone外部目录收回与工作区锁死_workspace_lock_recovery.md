# fresh clone 外部目录收回与工作区锁死 workspace_lock_recovery

## 1. 本轮范围

- `已确认` 本轮任务类型：项目文件修改任务 / 本地文件治理任务 / 机制修补 / 路由修补任务。
- `已确认` 本轮只处理 PR #50 fresh clone 审计目录收回与 `single_workspace_rule（单工作区硬规则）` 加固。
- `已确认` 本轮不是继续项目清理，不是迁移正式工作区，不是处理 `素材录制/`。

## 2. 目录收回结果

- 来源目录：`/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504`
- 目标目录：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260504/视频工厂_fresh_clone_audit_20260504`
- 是否移动成功：`已确认` 是。
- 是否仍有 Documents 顶层散目录：`已确认` 否，`/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 已不存在。
- 目标目录大小：`已确认` 约 `975M`。
- 目标目录文件数：`已确认` `633`。
- 目标目录目录数：`已确认` `100`。
- 是否发现嵌套 `.git/`：`已确认` 是，作为归档内容保留，不提交、不当子模块处理。

## 3. `.gitignore` 与误提交防护

- 是否已通过 `.gitignore` 防止误提交：`已确认` 是。
- 依据：`.gitignore` 既有规则已忽略 `本地归档_local_archive/` 与 `本地隔离区_local_quarantine/`。
- 本轮是否修改 `.gitignore`：`已确认` 否。
- 原因：移动后的归档目录未出现在 `git status --short` 中，不需要新增更宽规则。

## 4. 规则文件修改

本轮同步加固以下文件：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_source/01_execution_rules.md`
4. `codex_log/latest.md`

新增硬规则：

- Codex 只能在 `/Users/fan/Documents/视频工厂` 唯一正式工作区内执行。
- 不得默认新建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees`。
- 不得默认新建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区。
- 不得默认使用 `git worktree add` 创建外部工作区，除非用户本轮明确授权。
- 如果 Codex 判断确实需要外部目录，必须先停止，输出原因、目标路径、风险、唯一正式工作区内替代方案，等待用户明确确认。
- 已经产生的外部工作区，必须收回到唯一正式工作区内部的 `本地归档_local_archive/` 或 `本地隔离区_local_quarantine/`，不得继续散落在 `/Users/fan/Documents` 顶层。

## 5. 未执行高风险动作

- `已确认` 未处理 `素材录制/`。
- `已确认` 未修改当前视频产物。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前发布状态。
- `已确认` 未修改 `content_validation`。
- `已确认` 未修改 `send_ready`。
- `已确认` 未替换正式工作区。
- `已确认` 未删除正式工作区。
- `已确认` 未执行 `git gc` / `git prune` / `git repack`。
- `已确认` 未执行 Git LFS / history rewrite。
- `已确认` 未 force push。
- `已确认` 未把嵌套 fresh clone 目录作为子模块处理。

## 6. 当前剩余 blocker

- `已确认` 当前无阻断本轮收回与规则加固的 blocker。
- `待验证` 后续正式工作区迁移 / 原始素材归档仍需等用户买硬盘并另起任务确认；本轮不处理。

## 7. 下一个目标

新会话默认只在 `/Users/fan/Documents/视频工厂` 唯一正式工作区内执行；如未来确需 fresh clone / 外部对照 / 外部 worktree，Codex 先停止回报并等待用户明确确认。
