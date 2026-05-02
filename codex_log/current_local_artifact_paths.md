# 当前本地产物路径索引 current_local_artifact_paths

## 1. 文件定位

本文件记录 Codex 已在本机验证真实存在的《视频工厂》本地产物路径。

`已确认` 本轮已执行 `single_workspace_rule（单工作区硬规则）`：

- 《视频工厂》唯一正式工作区是 `/Users/fan/Documents/视频工厂`。
- `canonical_local_path（首选本地路径）` 只能指向 `/Users/fan/Documents/视频工厂` 内部。
- `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees`、`/private/tmp`、`/Users/fan/Desktop`、`/Users/fan/Downloads` 不得作为最终交付路径。
- 旧外部路径只能作为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）` 记录，不得作为默认执行路径。
- 如果路径超过 24 小时未重新验证，必须标记为 `stale_pending_recheck（已过期，待重新检查）`。
- `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径，只能作为线索，不能直接当真实路径。

## 2. 当前路径优先级

路径优先级：

1. `project_internal_stable_path（唯一正式工作区内部稳定路径）`
2. `project_internal_latest_review_pack（唯一正式工作区内部 latest_review_pack）`
3. `historical_source_path（历史来源路径，仅说明来源，不作为默认执行路径）`
4. `fallback_path（备选路径，仅在本轮重新验证后可输出）`

## 3. 当前已验证路径表

字段：

| artifact_id（产物编号） | 中文名称 | purpose（用途） | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | fallback_paths（备选路径） | verified_at（验证时间） | source_record（来源记录） | notes（备注） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `round34_middle_preview` | round34 中段预览样片 | 用户复审中段放大剪辑尺度 / 中段结构 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1508_中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4` | `true` | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/middle_preview.mp4` | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `historical_source_path` 曾为 `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`，该外部 worktree 已安全移除，不再作为默认路径。 |
| `round34_problem_window_30_32` | round34 30-32 秒问题窗口 | 用户复审 30-32 秒问题窗口视频 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1511_30_32s.mp4` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `historical_source_path` 曾为外部 clean worktree 的 `dist/latest_review_pack/problem_windows/30_32s.mp4`，现已降级为历史来源。 |
| `round34_problem_window_30_32_frames` | round34 30-32 秒抽帧联系表 | 用户复审 30-32 秒问题窗口抽帧图 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1382_30_32s_frames.jpg` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 clean worktree 旧路径已降级为 `historical_source_path`。 |
| `round34_cut_contact_sheet` | round34 切点联系表 | 用户复审 cut points / 切点结构 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1675_cut_contact_sheet.jpg` | `true` | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/cut_contact_sheet.jpg` | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 clean worktree 旧路径已降级为 `historical_source_path`。 |
| `round34_full_video` | round34 完整正片 | 历史 round34 完整片复审入口 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1521_主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4` | `true` | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/full.mp4` | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `dist/latest_review_pack/full.mp4` 当前随 v3.1 指向变化，不再代表 round34 默认当前片；round34 内部稳定路径保留为历史复审入口。 |
| `v31_full_video_current_baseline` | AI 做 PPT 踩坑 v3.1 当前基线片 | 当前最新视频基线；后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基础 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | `true` | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/full.mp4` | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `historical_source_path` 曾为 `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502/...` 与 `/Users/fan/Documents/视频工厂_v31_visual_route_fix/...`，外部 worktree 已安全移除；`send_ready = false`、`content_validation = gray_testing_not_final_passed` 保持不变。 |
| `v3_full_video_review_candidate` | AI 做 PPT 踩坑 v3 完整候选片 | v3 历史候选 / 对照 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/AI做PPT踩坑_成品候选_v3_full.mp4` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `historical_source_path` 曾为 `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/...` 与 `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/...`，外部 worktree 已安全移除。 |
| `pr7_b_sassy_reference` | PR #7 B 骚萌卡视觉参考 | 后续骚萌卡执行参考 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 读不到该文件必须 `blocked`，不得回退 PR #7 A；外部 worktree 旧路径已降级为历史来源。 |
| `cute_prompt_card_negative_reference` | 可爱反面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 worktree 旧路径已降级为历史来源。 |
| `cute_prompt_card_positive_reference` | 可爱正面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 worktree 旧路径已降级为历史来源。 |
| `no_zoom_1x_review_frames` | 不放大完整可读 1x 默认视图复审图 | 历史 no_zoom_completeness 1x 默认视图复审图 | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png` | `false` | 无 | `2026-05-03 CST` | `test -f` 未命中；单工作区治理重新验证 | `stale_pending_recheck`：当前唯一正式工作区内未找到该 PNG；不得作为用户可打开路径输出。 |
| `no_zoom_layout_metrics` | 不放大完整可读布局指标 | 历史 no_zoom_completeness 布局指标 JSON | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` | `false` | 无 | `2026-05-03 CST` | `test -f` 未命中；单工作区治理重新验证 | `stale_pending_recheck`：当前唯一正式工作区内未找到该 JSON；不得作为用户可打开路径输出。 |

## 4. 本轮单工作区治理结果

- `已确认` `/Users/fan/Documents` 顶层执行 `find /Users/fan/Documents -maxdepth 1 -name '*视频工厂*' -print` 后，只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` 已回收外部目录唯一文件到：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260502/`。
- `已确认` 已将非 Git 散目录 / 损坏临时 worktree 残留移入：`/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/`。
- `已确认` 本轮未永久删除任何未回收文件；干净 Git worktree 只在无未提交、无未跟踪、无未推送且回收校验通过后执行 `git worktree remove`。
- `待验证` `git worktree list` 仍保留两个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree，因为它们有未跟踪文件，按安全规则保留并等待用户下一轮确认。

## 5. 历史外部来源降权清单

以下路径只作为 `historical_source_path（历史来源路径）` 说明，不再作为 `canonical_local_path` 或默认执行路径：

- `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`
- `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502`
- `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502`
- `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501`
- `/Users/fan/Documents/视频工厂_v31_visual_route_fix`
- `/Users/fan/Documents/视频工厂_v2_candidate_worktree`
- `/Users/fan/Documents/视频工厂_sassy-card-structure-budget-20260428`
- `/Users/fan/Documents/视频工厂_locked_reference_inheritance_20260430`
- `/Users/fan/Documents/视频工厂-worktrees`
- `/private/tmp/视频工厂_opening_anchor_20260428`
- `/private/tmp/视频工厂_real_ai_experience_mainline_20260428`
- `/private/tmp/视频工厂_scheme_b_v3_diagnostics`
- `/private/tmp/视频工厂_user_readable_map_sync`

## 6. 最后更新时间

- `2026-05-03 CST`
