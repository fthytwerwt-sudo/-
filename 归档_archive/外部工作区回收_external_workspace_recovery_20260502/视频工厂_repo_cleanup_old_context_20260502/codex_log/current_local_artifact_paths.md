# 当前本地产物路径索引 current_local_artifact_paths

## 1. 文件定位

本文件记录 Codex 已在本机验证真实存在的本地产物路径。

硬规则：

- ChatGPT 给用户本地路径时，必须优先读取本文件。
- `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径，只能作为线索，不能直接当真实路径。
- 只有本文件中 `path_exists = true（路径存在）` 的路径，才能作为用户可打开路径输出。
- 如果路径超过 24 小时未验证，必须标记为 `stale_pending_recheck（已过期，待重新检查）`。
- `/private/tmp（系统临时目录）` 路径默认不稳定，除非当前重新验证存在，否则不得作为首选路径。
- 旧脏 worktree（旧脏工作区）路径不得作为默认执行路径，但可作为历史 / 备选打开路径记录。

## 2. 当前路径优先级

路径优先级：

1. clean worktree path（干净工作区路径）
2. project internal stable path（项目内稳定路径）
3. old dirty worktree path（旧脏工作区路径，仅备选）
4. private tmp path（系统临时路径，仅当下验证存在时可用）

## 3. 当前已验证路径表

字段：

| artifact_id（产物编号） | 中文名称 | purpose（用途） | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | fallback_paths（备选路径） | verified_at（验证时间） | source_record（来源记录） | notes（备注） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `round34_middle_preview` | round34 中段预览样片 | 用户复审中段放大剪辑尺度 / 中段结构 | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4` | `true` | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1508_中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4`<br>`/Users/fan/Documents/视频工厂/dist/latest_review_pack/middle_preview.mp4` | `2026-04-30 18:02:32 CST` | `test -f`、`stat -f "%z %Sm"` 已通过；`ffprobe` 已尝试但本机命令不可用；视频时长 / 分辨率用 `mdls` 只读补充 | clean path：`1548882 bytes / Apr 30 04:13:53 2026 / 28.52s / 720x1280`；fallback1：`1548882 bytes / Apr 28 22:09:10 2026 / 28.52s / 720x1280`；fallback2：`1429937 bytes / Apr 25 00:51:40 2026 / 26.92s / 720x1280`；`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/middle_preview.mp4` 本轮不存在，未写入 fallback |
| `round34_problem_window_30_32` | round34 30-32 秒问题窗口 | 用户复审 30-32 秒问题窗口视频 | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s.mp4` | `true` | 无 | `2026-04-30 18:02:32 CST` | `test -f`、`stat -f "%z %Sm"` 已通过；`ffprobe` 已尝试但本机命令不可用；视频时长 / 分辨率用 `mdls` 只读补充 | `82935 bytes / Apr 30 04:13:53 2026 / 2.00s / 720x1280` |
| `round34_problem_window_30_32_frames` | round34 30-32 秒抽帧联系表 | 用户复审 30-32 秒问题窗口抽帧图 | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s_frames.jpg` | `true` | 无 | `2026-04-30 18:02:32 CST` | `test -f`、`stat -f "%z %Sm"`、`sips -g pixelWidth -g pixelHeight` 已通过 | `200155 bytes / Apr 30 04:13:53 2026 / 900x1162` |
| `round34_cut_contact_sheet` | round34 切点联系表 | 用户复审 cut points / 切点结构 | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/cut_contact_sheet.jpg` | `true` | 无 | `2026-04-30 18:02:32 CST` | `test -f`、`stat -f "%z %Sm"`、`sips -g pixelWidth -g pixelHeight` 已通过 | `615951 bytes / Apr 30 04:13:53 2026 / 720x2972` |
| `round34_full_video` | round34 完整正片 | 用户 / ChatGPT 最终内容复审入口 | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/full.mp4` | `true` | 无 | `2026-04-30 18:02:32 CST` | `test -f`、`stat -f "%z %Sm"` 已通过；`ffprobe` 已尝试但本机命令不可用；视频时长 / 分辨率用 `mdls` 只读补充 | `7727831 bytes / Apr 30 04:13:53 2026 / 55.89533333333333s / 720x1280` |
| `no_zoom_1x_review_frames` | 不放大完整可读 1x 默认视图复审图 | 历史 no_zoom_completeness 1x 默认视图复审图 | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png` | `true` | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/02_1x默认视图_no_zoom.png` | `2026-04-30 18:02:32 CST` | clean worktree 指定目录未命中；从 `/Users/fan/Documents` 只读查找命中旧脏 worktree；`test -f`、`stat -f "%z %Sm"`、`sips -g pixelWidth -g pixelHeight` 已通过 | clean worktree 中 `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/` 未找到 PNG；当前记录为旧脏 worktree 备选打开路径，不得作为默认执行路径；01：`254717 bytes / Apr 24 05:13:43 2026 / 1080x1920`；02：`204019 bytes / Apr 24 05:13:43 2026 / 1080x1920` |
| `no_zoom_layout_metrics` | 不放大完整可读布局指标 | 历史 no_zoom_completeness 布局指标 JSON | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` | `true` | 无 | `2026-04-30 18:02:32 CST` | clean worktree 指定路径未命中；从 `/Users/fan/Documents` 只读查找命中旧脏 worktree；`test -f`、`stat -f "%z %Sm"` 已通过 | clean worktree 中 `dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` 不存在；当前记录为旧脏 worktree 备选打开路径，不得作为默认执行路径；`1976 bytes / Apr 24 05:13:41 2026` |
| `v3_full_video_review_candidate` | AI 做 PPT 踩坑 v3 完整候选片 | 用户 / ChatGPT 复审后的 v3 当前审片对象 | `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/dist/latest_review_pack/full.mp4` | `true` | `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/dist/latest_review_pack/full.mp4`<br>`dist/latest_review_pack/full.mp4` | `2026-05-02 CST` | 本轮清理分支重新验证；未生成新视频；仅复核已同步的 v3 latest review pack | v3 技术阶段里程碑达成，但内容未过线，主要在 GPT 文案侧；`send_ready = false` |
| `pr7_b_sassy_reference` | PR #7 B 骚萌卡视觉参考 | 后续骚萌卡执行参考 | `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | `true` | `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png`<br>`复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | `2026-05-02 CST` | `test -f`、`sips -g pixelWidth -g pixelHeight` 已通过 | `720x1280`；读不到该文件必须 blocked，不得回退 PR #7 A |
| `cute_prompt_card_negative_reference` | 可爱反面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png` | `true` | `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png`<br>`复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png` | `2026-05-02 CST` | `test -f`、`sips -g pixelWidth -g pixelHeight` 已通过 | `720x1280` |
| `cute_prompt_card_positive_reference` | 可爱正面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png` | `true` | `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png`<br>`复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png` | `2026-05-02 CST` | `test -f`、`sips -g pixelWidth -g pixelHeight` 已通过 | `720x1280` |
