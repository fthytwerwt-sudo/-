# 20260502 单工作区清理归档 single_workspace_cleanup_archive

## 1. 本轮结论

- `已确认` 本轮从 `origin/codex/user-readable-map` 创建分支：`codex/single-workspace-cleanup-from-user-readable-map-20260502`。
- `已确认` `/Users/fan/Documents` 顶层《视频工厂》相关目录已清理到只剩：`/Users/fan/Documents/视频工厂`。
- `已确认` 已回收外部目录唯一文件 `442` 个到唯一正式工作区内部本地归档区。
- `已确认` 回收文件 size 与 checksum 全部一致；失败项 `0` 个。
- `已确认` 已安全移除干净 Git worktree `18` 个。
- `已确认` 已移动非 Git / 损坏临时残留目录 `3` 个到唯一正式工作区内部隔离区。
- `部分成立` 仍有 2 个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree 因未跟踪文件被标记 `blocked_need_user_review`，本轮未移除。

## 2. 单工作区规则

`single_workspace_rule` 已写入：

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/current_local_artifact_paths.md`

规则核心：

- 唯一正式工作区是 `/Users/fan/Documents/视频工厂`。
- 不允许默认创建 `/Users/fan/Documents/视频工厂_*` 或外部 Git worktree。
- 新分支只能在唯一正式工作区内创建 / 切换。
- 所有最终产物、复审包、报告、日志、路径索引都必须落在唯一正式工作区内部。
- 外部路径最多作为历史来源或备选路径，不得作为默认执行路径。

## 3. 路径索引

- `codex_log/current_local_artifact_paths.md` 已改为内部路径优先。
- 所有 `canonical_local_path` 均指向 `/Users/fan/Documents/视频工厂` 内部。
- 旧 `/Users/fan/Documents/视频工厂_*` 路径已降级为 `historical_source_path` 说明。
- 未重新验证存在的 no_zoom 路径已标记 `path_exists = false` / `stale_pending_recheck`。

## 4. 状态边界

- `已确认` 本轮未生成视频、音频、图片。
- `已确认` 本轮未写新文案。
- `已确认` 本轮未修改 v3.1 正片内容。
- `已确认` 本轮未修改 `dist/latest_review_pack` 既有产物内容。
- `已确认` 本轮未修改 `content_validation` 为 `passed`。
- `已确认` 本轮未修改 `send_ready` 为 `true`。
- `已确认` 本轮未处理 HyperFrames 卡片边界任务。
- `已确认` 本轮未永久删除未回收文件。

## 5. 报告与清单

- 审计报告：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/单工作区清理归档报告_single_workspace_cleanup_archive_report.md`
- 初始审计表：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/audit_directory_table_initial.tsv`
- 回收 manifest：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/recovery_manifest.json`
- 清理 manifest：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/cleanup_actions_manifest.json`
- 最终验证快照：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/final_state_verification_snapshot.json`

## 6. 下一个目标

- 用户确认两个 blocked superpowers 历史 worktree 的未跟踪文件是否可忽略或需要继续回收。
- 后续所有《视频工厂》任务均从 `/Users/fan/Documents/视频工厂` 内发起。
