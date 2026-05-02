# Superpowers 工作区清理报告 superpowers_worktree_cleanup_report

## 1. 本轮范围

- `已确认` PR #32 已合并到 `codex/user-readable-map`。
- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/superpowers-worktree-cleanup-20260503`。
- `已确认` 本轮只处理 2 个指定 Superpowers 历史 worktree。
- `已确认` 未扫描无关私人目录。
- `已确认` 未创建外部 worktree，未使用 `git worktree add`。
- `已确认` 未生成视频、音频、图片，未写新文案，未处理 HyperFrames 任务。

## 2. 审计结果

| worktree_path | branch | commit | tracked_diff | staged_diff | untracked_files | unpushed_commits | file_count | size_summary | action |
| --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1` | `codex/formal-api-demo-quality-liveportrait-round1` | `4beeeb1` | `empty` | `empty` | 0 | `false` | 102 | `71M` | `git worktree remove` |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-round1-visual-pass-report-style` | `codex/round1-visual-pass-report-style` | `d8234e0` | `empty` | `empty` | 0 | `false` | 162 | `156M` | `git worktree remove` |

说明：

- `codex/formal-api-demo-quality-liveportrait-round1` 没有本地 upstream 配置，但 `origin/codex/formal-api-demo-quality-liveportrait-round1` 存在，且 `origin/...HEAD` 对比为 `0 0`，因此没有未推送提交。
- `codex/round1-visual-pass-report-style` 的 upstream 为 `origin/codex/round1-visual-pass-report-style`，`@{u}...HEAD` 对比为 `0 0`，因此没有未推送提交。
- `已确认` 两个 worktree 在本轮 Phase B 审计时已经没有 untracked 文件；PR #32 报告中曾记录的风险项在本轮最终审计时不再出现。

## 3. 回收结果

- 回收目标：`/Users/fan/Documents/视频工厂/本地归档_local_archive/superpowers_worktree_recovery_20260503/`
- `codex-formal-api-demo-quality-liveportrait-round1` 本轮新增回收文件数量：`0`
- `codex-round1-visual-pass-report-style` 本轮新增回收文件数量：`0`
- checksum 失败数量：`0`
- manifest：`治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_recovery_manifest.tsv`
- manifest JSON：`治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_recovery_manifest.json`

`已确认` 本轮未发现需要复制的新唯一 untracked 文件，因此 manifest 为合法空清单。

## 4. 清理结果

- `已确认` 已对两个路径执行普通 `git worktree remove <path>`。
- `已确认` 未使用 `git worktree remove --force`。
- `已确认` 未使用 `rm -rf`。
- `已确认` `git worktree list` 最终只剩唯一正式工作区：

```text
/Users/fan/Documents/视频工厂      2d7883a [codex/superpowers-worktree-cleanup-20260503]
```

## 5. 安全理由

- tracked diff 为空。
- staged diff 为空。
- untracked 文件数量为 `0`。
- 相关 commit 均已存在于远端分支。
- 没有需要回收但未校验的唯一文件。
- 本轮只移除 Git 管理的 worktree，不清空目录，不永久删除未回收文件。

## 6. 状态边界

- `已确认` 未生成视频 / 音频 / 图片。
- `已确认` 未写新文案。
- `已确认` 未修改 v3.1 正片。
- `已确认` 未修改 `dist/latest_review_pack` 既有产物。
- `已确认` `content_validation` 保持发布后灰度测试口径，没有写成内容最终通过。
- `已确认` `send_ready` 保持否定状态。
- `已确认` 未提交 `本地归档_local_archive/` 或 `本地隔离区_local_quarantine/`。

## 7. 结论

`已确认` 两个 Superpowers 历史 worktree 已安全移除。后续《视频工厂》任务只能在 `/Users/fan/Documents/视频工厂` 内创建 / 切换分支和落治理记录。
