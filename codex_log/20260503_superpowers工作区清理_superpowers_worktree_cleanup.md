# 20260503 Superpowers 工作区清理 superpowers_worktree_cleanup

## 1. 本轮结论

- `已确认` PR #32 已 squash merge 到 `codex/user-readable-map`，合并提交：`2d7883a`。
- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/superpowers-worktree-cleanup-20260503`。
- `已确认` 本轮只处理两个指定 Superpowers 历史 worktree。
- `已确认` 两个 worktree 的 tracked diff、staged diff、untracked 文件数量均为 clean / `0`。
- `已确认` 两个 worktree 的 commit 均已存在于远端分支，没有未推送提交。
- `已确认` 本轮新增回收文件数量为 `0`；没有 checksum 失败。
- `已确认` 已执行普通 `git worktree remove` 移除两个历史 worktree；未使用 `--force`。
- `已确认` `git worktree list` 最终只剩 `/Users/fan/Documents/视频工厂`。

## 2. 清理对象

- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-round1-visual-pass-report-style`

## 3. 报告与清单

- `治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_cleanup_report.md`
- `治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_recovery_manifest.tsv`
- `治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_recovery_manifest.json`
- `治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_removed_list.md`

## 4. 状态边界

- `已确认` 未生成视频 / 音频 / 图片。
- `已确认` 未写新文案。
- `已确认` 未修改 v3.1 正片。
- `已确认` 未修改 `dist/latest_review_pack` 既有产物。
- `已确认` `content_validation` 保持发布后灰度测试口径，没有写成内容最终通过。
- `已确认` `send_ready` 保持否定状态。
- `已确认` 未提交本地归档大文件或隔离区文件。

## 5. 下一个目标

- 后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内执行。
