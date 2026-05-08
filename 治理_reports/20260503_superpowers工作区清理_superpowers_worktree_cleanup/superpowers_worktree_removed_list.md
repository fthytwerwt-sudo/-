# Superpowers 历史 worktree 移除清单

## 1. 移除结果

| worktree_path | branch | commit | remove_command | force_used | final_state |
| --- | --- | --- | --- | --- | --- |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1` | `codex/formal-api-demo-quality-liveportrait-round1` | `4beeeb1` | `git worktree remove <path>` | `false` | `removed` |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-round1-visual-pass-report-style` | `codex/round1-visual-pass-report-style` | `d8234e0` | `git worktree remove <path>` | `false` | `removed` |

## 2. 移除依据

- `已确认` 两个 worktree 的 tracked diff 均为空。
- `已确认` 两个 worktree 的 staged diff 均为空。
- `已确认` 两个 worktree 的 untracked 文件数量均为 `0`。
- `已确认` 两个 worktree 的 commit 均已存在于对应远端分支。
- `已确认` 没有使用 `--force`。
- `已确认` 没有使用 `rm -rf`。

## 3. 最终 worktree list

```text
/Users/fan/Documents/视频工厂      2d7883a [codex/superpowers-worktree-cleanup-20260503]
```
