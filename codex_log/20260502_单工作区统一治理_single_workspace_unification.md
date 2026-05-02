# 20260502 单工作区统一治理 single workspace unification

## 本轮目标

- `已确认` 全面审计 `/Users/fan/Documents` 下《视频工厂》相关散工作区，安全回收唯一产物到唯一正式工作区。
- `已确认` 建立后续只能在 `/Users/fan/Documents/视频工厂` 内工作的仓库规则。

## 执行前已确认事实

- `已确认` 唯一正式工作区是 `/Users/fan/Documents/视频工厂`。
- `已确认` 当前仓库是 Git 仓库，本轮分支是 `codex/single-workspace-unification-20260502`。
- `已确认` 本轮开始前正式工作区已有未提交 / 未跟踪内容，包括 `codex_log/latest.md`、`codex_log/current_local_artifact_paths.md`、若干历史产物目录和 `.omx/`；本轮未覆盖、未清空这些既有内容。
- `已确认` 当前仓库内没有本地 `skills/` 目录；已读取全局 `using-git-worktrees`、`finishing-a-development-branch`、`verification-before-completion`、`context-driven-development` skill。
- `已确认` `GPT数据源/08_当前正式事实.md` 在当前仓库未命中；`GPT 数据源/01_项目系统提示词.md` 存在并已读取。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `project_source/06_project_index.md`
- `GPT 数据源/01_项目系统提示词.md`
- `git worktree list --porcelain`
- `/Users/fan/Documents/视频工厂*`
- `/private/tmp/视频工厂_*`
- `/Users/fan/Desktop` 与 `/Users/fan/Downloads` 下匹配 `*视频工厂*` 的目录查找结果

## 实际改动

- 修改 `AGENTS.md`：新增 `单工作区硬规则 single_workspace_rule`。
- 修改 `codex_source/00_codex_readme.md`：补充执行层单工作区规则。
- 修改 `codex_source/01_execution_rules.md`：新增 `EXEC-006B 单工作区硬规则 single_workspace_rule`。
- 修改 `codex_log/current_local_artifact_paths.md`：将外部散工作区首选路径降级为 `historical_source_path` / `fallback_path`，首选路径改为 `/Users/fan/Documents/视频工厂` 内部路径。
- 修改 `codex_log/latest.md`：写入本轮简版交接摘要。
- 新增 `治理_reports/20260502_单工作区审计_single_workspace_audit/` 审计报告与 JSON 清单。
- 新增 `归档_archive/外部工作区回收_external_workspace_recovery_20260502/` 回收目录、checksum 清单、待删候选清单。

## 实际执行

- `已确认` 执行了正式工作区确认、Git 状态检查、分支创建、外部目录发现、Git worktree 清单读取。
- `已确认` 扫描 13 个外部 / 历史目录，合计 7661 个项目产物 / 报告类文件。
- `已确认` 7464 个文件已在正式工作区存在等价 SHA-256；84 个为外部重复文件；113 个为唯一需回收文件。
- `已确认` 113 个唯一文件已复制到 `/Users/fan/Documents/视频工厂/归档_archive/外部工作区回收_external_workspace_recovery_20260502/`，并通过源 / 目标大小一致与 SHA-256 一致校验。
- `已确认` 复制失败项为 0。

## 当前结果

- `已确认` 已生成完整审计报告：`治理_reports/20260502_单工作区审计_single_workspace_audit/单工作区审计报告_single_workspace_audit_report.md`。
- `已确认` 已生成待删候选清单：`归档_archive/外部工作区回收_external_workspace_recovery_20260502/待删候选_delete_candidates.md`。
- `已确认` 本轮未永久删除任何文件，未运行 `rm -rf`，未执行 `git worktree remove`。
- `已确认` 本轮未生成视频 / 音频 / 图片，未写新文案，未修改 v3.1 正片内容，未修改 `content_validation`，未修改 `send_ready`。

## 下一步建议

- `下一个目标`：用户确认 `delete_candidate` / `migrate_then_delete_candidate` 后，进入第二轮安全删除候选目录与 `git worktree` 清理。
- `待验证` 第二轮清理前仍需重新执行 `git status`、`git worktree list`、候选目录 checksum / 路径存在性复核。
