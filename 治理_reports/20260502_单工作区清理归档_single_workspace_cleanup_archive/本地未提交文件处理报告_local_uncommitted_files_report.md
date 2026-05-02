# 本地未提交文件处理报告 local_uncommitted_files_report

## 1. 本轮目标

- `已确认` 本轮只处理 `codex/single-workspace-cleanup-from-user-readable-map-20260502` 本地工作区显示的大量未跟踪文件。
- `已确认` 不提交本地归档大文件、隔离区文件、视频、音频、图片、zip、HyperFrames 临时产物或旧口径文件。
- `已确认` 不永久删除任何未确认文件，不使用 `rm -rf`，不新建外部 worktree。

## 2. 必跑命令快照

- `pwd`：`/Users/fan/Documents/视频工厂`
- `git branch --show-current`：`codex/single-workspace-cleanup-from-user-readable-map-20260502`
- `git diff --name-status`：空
- `git diff --cached --name-status`：空
- `git ls-files --others --exclude-standard`：本轮处理前为 `5166` 个未忽略的未跟踪文件。
- `git ls-files --ignored --others --exclude-standard`：处理后为 `6287` 个 ignored local-only 文件。
- `git check-ignore -v 本地归档_local_archive/ 本地隔离区_local_quarantine/ || true`：确认两者命中 `.gitignore` 中的忽略规则。
- `git diff --name-only origin/codex/user-readable-map...HEAD`：仍只包含 PR #32 的规则文件、日志文件、治理报告和清单文件。

## 3. 分类结果

| classification | count | 说明 |
| --- | ---: | --- |
| `should_commit` | 1 | 本报告：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/本地未提交文件处理报告_local_uncommitted_files_report.md` |
| `should_ignore_local_only` | 5166 | 处理前所有未忽略的未跟踪文件；均为本地状态、历史备份、HyperFrames 测试产物、历史 `dist/` 生成物、复审包、素材目录、素材检查报告或旧日志 |
| `should_unstage` | 0 | 本地归档 / 隔离区没有被暂存；执行 `git restore --staged 本地归档_local_archive/ 本地隔离区_local_quarantine/ || true` 后只返回“pathspec 未被 Git 追踪” |
| `should_restore` | 0 | 没有 tracked diff；未发现误改 `dist/latest_review_pack/`、v3.1 正片、`content_validation` 或 `send_ready` |
| `blocked_need_user_review` | 0 | 当前 canonical workspace 内没有需要用户确认的未提交文件；两个 superpowers 历史 worktree 仍是上一轮记录的外部 blocked 项，不属于本轮 Git status |

## 4. should_ignore_local_only 分组

处理前未忽略的 `5166` 个未跟踪文件按顶层分组如下：

| top-level path | count | 处理方式 |
| --- | ---: | --- |
| `视频工厂_元素娃娃1080P复审包_20260428/` | 3013 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `dist/` | 1827 | 本机 `.git/info/exclude` 忽略，保留本地；不影响已追踪文件 |
| `复审包_review_packs/` | 121 | 本机 `.git/info/exclude` 忽略未跟踪部分，保留本地 |
| `临时产物_staging/` | 69 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `.omx/` | 43 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `素材检查_reports/` | 42 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `HyperFrames测试_hyperframes_result_card_component_20260502/` | 12 | 本机 `.git/info/exclude` 忽略，保留本地；本轮不处理 HyperFrames 边界 |
| `HyperFrames测试_hyperframes_screencast_annotation_20260502/` | 12 | 本机 `.git/info/exclude` 忽略，保留本地；本轮不处理 HyperFrames 边界 |
| `GPT 数据源/_backup_before_update_20260429_022552（更新前备份）/` | 10 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `codex_log/` 旧日志 | 6 | 本机 `.git/info/exclude` 精确忽略 6 个旧日志文件，保留本地 |
| `素材录制/` | 6 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `素材库_assets/` | 3 | 本机 `.git/info/exclude` 忽略，保留本地 |
| `文案库/` | 2 | 本机 `.git/info/exclude` 忽略，保留本地 |

## 5. 实际处理动作

- `已确认` 未执行永久删除。
- `已确认` 未移动这些本地文件。
- `已确认` 未执行 `git add .`。
- `已确认` 未提交本地归档区或隔离区。
- `已确认` `.gitignore` 已有：
  - `本地归档_local_archive/`
  - `本地隔离区_local_quarantine/`
- `已确认` 未向 `.gitignore` 增加全局 `*.mp4` / `*.png` / `*.jpg` / `*.wav` 等规则，因为本仓库确实存在需要被 Git 追踪的复审证据和小样本文件；一刀切忽略媒体扩展名会误伤后续合法产物回流。
- `已确认` 使用本机 `.git/info/exclude` 忽略当前已存在的 5166 个 local-only 未跟踪文件；该文件不进入 PR，只清理本机状态。

## 6. 最终状态

- `git status --short --branch --untracked-files=all` 在提交本报告前已显示 clean。
- 本报告提交后，PR #32 只新增一个小型治理报告文件。
- 防混乱边界保持：
  - staged / committed 文件不包含 `本地归档_local_archive/`
  - staged / committed 文件不包含 `本地隔离区_local_quarantine/`
  - staged / committed 文件不包含 `dist/latest_review_pack/`
  - staged / committed 文件不包含 `.mp4 / .mov / .wav / .mp3 / .aac / .zip`
  - 未把 `content_validation` 改成 `passed`
  - 未把 `send_ready` 改成 `true`

## 7. 剩余风险

- `部分成立` PR #32 工作区本身已清爽；但上一轮报告中仍有 2 个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree 因未跟踪文件未移除，仍需用户确认后另起清理轮次。
