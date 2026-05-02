# 单工作区清理归档报告 single_workspace_cleanup_archive_report

## 1. 审计结论

- `已确认` 本轮发现多个《视频工厂》外部散工作区 / 旧 worktree / 临时导出。
- `已确认` 本轮从正确基线 `origin/codex/user-readable-map` 创建治理分支：`codex/single-workspace-cleanup-from-user-readable-map-20260502`。
- `已确认` `/Users/fan/Documents` 顶层最终只剩：`/Users/fan/Documents/视频工厂`。
- `已确认` 已复制回收唯一文件：`442` 个；复制失败：`0` 个。
- `已确认` 回收文件 size 与 checksum 全部一致。
- `已确认` 已安全执行 `git worktree remove`：`18` 个目录。
- `已确认` 已移动到内部隔离区：`3` 个目录。
- `部分成立` `git worktree list` 仍保留 2 个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree；它们有未跟踪文件，按安全规则未移除，列入 `blocked_need_user_review`。
- `已确认` 本轮未永久删除任何未回收文件，未运行 `rm -rf`，未清空目录。
- `已确认` 本轮未生成视频 / 音频 / 图片，未写新文案，未处理 HyperFrames 卡片边界任务。
- `已确认` 本轮未修改 `content_validation` 为 `passed`，未修改 `send_ready` 为 `true`。

## 2. 目录处理表

| path（路径） | type（类型） | git_status（Git 状态） | unique_files（唯一文件数） | action_taken（采取动作） | final_state（最终状态） | reason（原因） |
| --- | --- | --- | ---: | --- | --- | --- |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1` | `external_git_worktree` | untracked=42 | 90 | blocked and kept | still exists (blocked/kept) | untracked_files |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-round1-visual-pass-report-style` | `external_git_worktree` | untracked=84 | 146 | blocked and kept | still exists (blocked/kept) | untracked_files |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-v001-24h-screenshot-intake-20260502` | `external_git_worktree` | clean | 10 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/material-faithful-check-20260429` | `external_git_worktree` | clean | 53 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-gray-test-metrics-v1-20260502` | `external_git_worktree` | clean | 14 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-gray-test-review-loop-20260502` | `external_git_worktree` | clean | 13 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-screenshot-data-buckets-20260502` | `external_git_worktree` | clean | 0 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂` | `canonical_workspace` | tracked clean; existing untracked local artifacts present | 0 | kept as canonical workspace | kept | 唯一正式工作区 |
| `/Users/fan/Documents/视频工厂-worktrees` | `non_git_project_copy` | non-git | 1 | moved to internal quarantine | quarantined: `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂-worktrees` | 非 Git 散目录；可在回收唯一文件后整体移入唯一工作区隔离区 |
| `/Users/fan/Documents/视频工厂-worktrees/copy-sample-rhythm-extract-20260429` | `external_git_worktree` | clean | 1 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂/临时产物_staging/worktrees/ai_ppt_pitfall_preview_v1_20260429` | `external_git_worktree` | clean | 0 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂/临时产物_staging/worktrees/gpt_project_source_path_rule_20260428` | `external_git_worktree` | clean | 0 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430` | `external_git_worktree` | clean | 7 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_locked_reference_inheritance_20260430` | `external_git_worktree` | clean | 5 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502` | `external_git_worktree` | clean | 12 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_sassy-card-structure-budget-20260428` | `external_git_worktree` | clean | 9 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_v2_candidate_worktree` | `external_git_worktree` | clean | 2 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502` | `external_git_worktree` | clean | 7 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_v31_visual_route_fix` | `external_git_worktree` | clean | 9 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501` | `external_git_worktree` | clean | 19 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/private/tmp/视频工厂_opening_anchor_20260428` | `external_git_worktree` | clean | 5 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/private/tmp/视频工厂_real_ai_experience_mainline_20260428` | `external_git_worktree` | clean | 10 | git worktree remove | removed from git worktree list; path removed | Git 工作区干净且无未推送提交；唯一文件回收校验后可清理 |
| `/private/tmp/视频工厂_scheme_b_v3_diagnostics` | `external_git_worktree` | non-git | 0 | moved to internal quarantine | quarantined: `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂_scheme_b_v3_diagnostics__private_tmp` |  |
| `/private/tmp/视频工厂_user_readable_map_sync` | `external_git_worktree` | non-git | 0 | moved to internal quarantine | quarantined: `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂_user_readable_map_sync__private_tmp` |  |

## 3. 回收结果

- 回收目录：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260502`
- 回收文件数量：`442`
- 新复制文件数量：`442`
- checksum 失败项：`0`
- 回收 manifest：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/recovery_manifest.json`
- 回收 TSV：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/recovery_manifest.tsv`

## 4. 清理结果

### 已 git worktree remove

- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-v001-24h-screenshot-intake-20260502`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/material-faithful-check-20260429`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-gray-test-metrics-v1-20260502`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-gray-test-review-loop-20260502`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/v31-screenshot-data-buckets-20260502`
- `/Users/fan/Documents/视频工厂-worktrees/copy-sample-rhythm-extract-20260429`
- `/Users/fan/Documents/视频工厂/临时产物_staging/worktrees/ai_ppt_pitfall_preview_v1_20260429`
- `/Users/fan/Documents/视频工厂/临时产物_staging/worktrees/gpt_project_source_path_rule_20260428`
- `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`
- `/Users/fan/Documents/视频工厂_locked_reference_inheritance_20260430`
- `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502`
- `/Users/fan/Documents/视频工厂_sassy-card-structure-budget-20260428`
- `/Users/fan/Documents/视频工厂_v2_candidate_worktree`
- `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502`
- `/Users/fan/Documents/视频工厂_v31_visual_route_fix`
- `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501`
- `/private/tmp/视频工厂_opening_anchor_20260428`
- `/private/tmp/视频工厂_real_ai_experience_mainline_20260428`

### 已移动到隔离区

- `/Users/fan/Documents/视频工厂-worktrees` -> `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂-worktrees`
- `/private/tmp/视频工厂_scheme_b_v3_diagnostics` -> `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂_scheme_b_v3_diagnostics__private_tmp`
- `/private/tmp/视频工厂_user_readable_map_sync` -> `/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/视频工厂_user_readable_map_sync__private_tmp`

### blocked 未处理目录及原因

- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`：untracked_files；unique_files=90，已复制回收但因风险未移除。
- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-round1-visual-pass-report-style`：untracked_files；unique_files=146，已复制回收但因风险未移除。

## 5. 规则修补结果

- `AGENTS.md`：新增《视频工厂》`single_workspace_rule`，并保留多项目仓库入口规则。
- `codex_source/00_codex_readme.md`：新增单工作区入口规则。
- `codex_source/01_execution_rules.md`：新增 `6B. 单工作区硬规则 single_workspace_rule`。
- `.gitignore`：忽略 `本地归档_local_archive/` 与 `本地隔离区_local_quarantine/`，防止大视频 / 图片 / 音频和隔离目录被误提交。

## 6. 路径索引修正

- `codex_log/current_local_artifact_paths.md` 已重写为唯一正式工作区内部路径优先。
- `canonical_local_path` 已全部指向 `/Users/fan/Documents/视频工厂` 内部。
- 旧外部路径只保留为 `historical_source_path` 说明，不再作为默认执行路径。
- `no_zoom_1x_review_frames` 与 `no_zoom_layout_metrics` 在本轮 `test -f` 未命中，已标记 `path_exists = false` 与 `stale_pending_recheck`。

## 7. 状态边界

- `已确认` 未生成视频 / 音频 / 图片。
- `已确认` 未写新文案。
- `已确认` 未修改 v3.1 正片内容。
- `已确认` 未修改 `dist/latest_review_pack` 既有产物内容。
- `已确认` `content_validation` 保持 `gray_testing_not_final_passed` 口径，没有改成 `passed`。
- `已确认` `send_ready` 保持 `false` 口径，没有改成 `true`。
- `已确认` 未处理 HyperFrames 卡片边界任务。

## 8. 验证快照

- `pwd`：`/Users/fan/Documents/视频工厂`
- `git branch --show-current`：`codex/single-workspace-cleanup-from-user-readable-map-20260502`
- `find /Users/fan/Documents -maxdepth 1 -name '*视频工厂*' -print`：`/Users/fan/Documents/视频工厂`
- `git worktree list`：仍保留 canonical workspace 与 2 个 blocked superpowers 历史 worktree。
- 验证快照：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/final_state_verification_snapshot.json`

## 9. 下一个目标

- 若用户确认两个 blocked superpowers 历史 worktree 中的未跟踪文件可忽略或已回收，下一轮再执行安全清理。
- 后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内创建 / 切换分支和落产物。
