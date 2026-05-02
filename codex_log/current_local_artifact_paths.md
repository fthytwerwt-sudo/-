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
- `single_workspace_rule（单工作区硬规则）`：`canonical_local_path（首选本地路径）` 只能指向 `/Users/fan/Documents/视频工厂` 内部路径。
- `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Desktop`、`/Users/fan/Downloads`、`/private/tmp` 只能记录为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）`，不得作为默认执行路径。

## 2. 当前路径优先级

路径优先级：

1. canonical workspace path（唯一正式工作区内部路径）
2. project internal stable archive path（项目内稳定归档路径）
3. historical source path（历史来源路径，仅作来源记录）
4. fallback path（备选路径，不作为默认执行路径）

## 3. 当前已验证路径表

字段：

| artifact_id（产物编号） | 中文名称 | purpose（用途） | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | fallback_paths（备选路径） | verified_at（验证时间） | source_record（来源记录） | notes（备注） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `round34_middle_preview` | round34 中段预览样片 | 用户复审中段放大剪辑尺度 / 中段结构 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1508_中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`<br>`fallback_path: /Users/fan/Documents/视频工厂/dist/latest_review_pack/middle_preview.mp4` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 clean path 一致 | `single_workspace_rule` 已生效；外部 clean worktree 路径已降级为 `historical_source_path`，不得作为默认执行路径 |
| `round34_problem_window_30_32` | round34 30-32 秒问题窗口 | 用户复审 30-32 秒问题窗口视频 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1511_30_32s.mp4` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s.mp4` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 clean path 一致 | 外部 clean worktree 路径已降级为历史来源 |
| `round34_problem_window_30_32_frames` | round34 30-32 秒抽帧联系表 | 用户复审 30-32 秒问题窗口抽帧图 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1382_30_32s_frames.jpg` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s_frames.jpg` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 clean path 一致 | 外部 clean worktree 路径已降级为历史来源 |
| `round34_cut_contact_sheet` | round34 切点联系表 | 用户复审 cut points / 切点结构 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1675_cut_contact_sheet.jpg` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/cut_contact_sheet.jpg` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 clean path 一致 | 外部 clean worktree 路径已降级为历史来源 |
| `round34_full_video` | round34 完整正片 | 用户 / ChatGPT 最终内容复审入口 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1521_主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/full.mp4` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 clean path 一致 | 外部 clean worktree 路径已降级为历史来源 |
| `no_zoom_1x_review_frames` | 不放大完整可读 1x 默认视图复审图 | 历史 no_zoom_completeness 1x 默认视图复审图 | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png` | `true` | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/02_1x默认视图_no_zoom.png` | `2026-05-02 CST` | `test -f` 已重新验证 canonical path 与 fallback path | `single_workspace_rule` 已生效；路径位于唯一正式工作区内部；01：`254717 bytes / Apr 24 05:13:43 2026 / 1080x1920`；02：`204019 bytes / Apr 24 05:13:43 2026 / 1080x1920` |
| `no_zoom_layout_metrics` | 不放大完整可读布局指标 | 历史 no_zoom_completeness 布局指标 JSON | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` | `true` | 无 | `2026-05-02 CST` | `test -f` 已重新验证 canonical path | `single_workspace_rule` 已生效；路径位于唯一正式工作区内部；`1976 bytes / Apr 24 05:13:41 2026` |
| `v31_full_video_current_baseline` | AI 做 PPT 踩坑 v3.1 当前基线片 | 当前最新视频基线；后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基础 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | `true` | `fallback_path: /Users/fan/Documents/视频工厂/dist/latest_review_pack/full.mp4`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502/dist/latest_review_pack/full.mp4`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v31_visual_route_fix/dist/latest_review_pack/full.mp4` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 v3.1 baseline path 一致 | 未重新生成视频；`send_ready = false`；内容仍待用户 / ChatGPT 复审 |
| `v3_full_video_review_candidate` | AI 做 PPT 踩坑 v3 完整候选片 | 用户 / ChatGPT 复审后的 v3 当前审片对象 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/AI做PPT踩坑_成品候选_v3_full.mp4` | `true` | `fallback_path: /Users/fan/Documents/视频工厂/dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_full.mp4`<br>`historical_source_path: /Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/dist/latest_review_pack/full.mp4`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/dist/latest_review_pack/full.mp4` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部 v3 path 一致 | v3 技术阶段里程碑达成，但内容未过线；`send_ready = false` |
| `pr7_b_sassy_reference` | PR #7 B 骚萌卡视觉参考 | 后续骚萌卡执行参考 | `/Users/fan/Documents/视频工厂/dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部参考图一致 | `720x1280`；读不到该文件必须 blocked，不得回退 PR #7 A |
| `cute_prompt_card_negative_reference` | 可爱反面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/round34_反面展示提示卡.png` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部参考图一致 | `720x1280` |
| `cute_prompt_card_positive_reference` | 可爱正面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/round34_正面展示提示卡.png` | `true` | `historical_source_path: /Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png`<br>`historical_source_path: /Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png` | `2026-05-02 CST` | `test -f` 已重新验证；SHA-256 与历史外部参考图一致 | `720x1280` |
| `hyperframes_result_diff_card_10s_sample` | HyperFrames 结果差提示卡 10 秒样片 | 云端剪辑可插入素材层验证；结果差提示卡 / 数据卡动态版本 | `/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_result_card_component_20260502/结果差提示卡_hyperframes_result_card_10s.mp4` | `true` | 无 | `2026-05-02 22:53:26 CST` | `test -f` 已通过；`ffprobe` 已确认 `h264 / 1080x1920 / 30fps / 10.000s / 720968 bytes`；`ffmpeg -v error ... -f null -` 解码通过 | 已在项目内部稳定目录；未使用 `/private/tmp`；仅为 HyperFrames 组件层样片，不改变 v3.1 正片、`content_validation` 或 `send_ready` |
| `hyperframes_shot07_screencast_annotation_overlay_alpha_mov` | HyperFrames shot07 录屏动态标注透明叠层 MOV | `shot07_deliverable_draft_keyword` 云端剪辑透明标注层；录屏主体不替换 | `/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_screencast_annotation_20260502/shot07_deliverable_draft_keyword_hyperframes_overlay_alpha.mov` | `true` | 无 | `2026-05-02 23:33:23 CST` | `test -f`、`ffprobe`、`ffmpeg -v error ... -f null -`、`video-metadata-probe` 均已通过 | HyperFrames `--format=mov` 产出；`prores (4444) / yuva444p12le / 1080x1920 / 30fps / 10.500s / 45951133 bytes`；alpha 通道存在；不改变 v3.1 正片、`content_validation` 或 `send_ready` |
| `hyperframes_shot07_screencast_annotation_precomp_mp4` | shot07 录屏 + HyperFrames 标注预合成 MP4 | 用户直接观看的技术样片；云端不支持透明 MOV 时的本地预合成备选 | `/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_screencast_annotation_20260502/shot07_deliverable_draft_keyword_screencast_plus_hyperframes_overlay_10_5s.mp4` | `true` | 无 | `2026-05-02 23:33:23 CST` | `test -f`、`ffprobe`、`ffmpeg -v error ... -f null -`、`video-metadata-probe` 均已通过 | `h264 / yuv420p / 1080x1920 / 30fps / 10.500s / 2890798 bytes`；基于源片 `source_start = 30.0` 截取；录屏为主体，顶部安全区标签 + 左侧节奏条 + 底部说明不替代录屏 |
