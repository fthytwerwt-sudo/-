# 20260430 本地路径索引机制日志 local_artifact_path_index

## 1. 本轮结论

- `已确认` 本轮建立 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`。
- `已确认` 本轮目标是让 ChatGPT 后续给用户本地路径前，优先读取 Codex 已在本机验证过的 local path index（本地路径索引）。
- `已确认` 本轮只写轻量文本索引，不提交视频、音频、图片本体。

## 2. 为什么不能只相信 manifest / summary 路径

- `已确认` `summary.json（状态摘要）` 和 `review_manifest.md（审片入口）` 中的路径只能作为线索。
- `已确认` 这些路径可能来自旧 worktree（旧工作区）、临时目录或已经不存在的目录。
- `已确认` 后续 ChatGPT 给用户本地路径时，必须先看 `current_local_artifact_paths.md（当前本地产物路径索引）`。
- `已确认` 只有 `path_exists = true（路径存在）` 的记录，才能作为用户可打开路径输出。

## 3. 已验证存在的路径

- `已确认` `round34_middle_preview` clean worktree 首选路径存在：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`
- `已确认` `round34_middle_preview` 另有两个已验证存在的 fallback：
  - `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1508_中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4`
  - `/Users/fan/Documents/视频工厂/dist/latest_review_pack/middle_preview.mp4`
- `已确认` `round34_problem_window_30_32` 存在：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s.mp4`
- `已确认` `round34_problem_window_30_32_frames` 存在：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/problem_windows/30_32s_frames.jpg`
- `已确认` `round34_cut_contact_sheet` 存在：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/cut_contact_sheet.jpg`
- `已确认` `round34_full_video` 存在：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/full.mp4`
- `已确认` `no_zoom_1x_review_frames` 在 clean worktree 未命中，但在旧脏 worktree 中找到并验证两个 PNG：
  - `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png`
  - `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/02_1x默认视图_no_zoom.png`
- `已确认` `no_zoom_layout_metrics` 在 clean worktree 未命中，但在旧脏 worktree 中找到并验证：
  - `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json`

## 4. 不存在或不作为首选的路径

- `已确认` `/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/middle_preview.mp4` 本轮 `test -f` 结果为不存在，未写入 fallback。
- `已确认` clean worktree 中 `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/` 未找到 PNG。
- `已确认` clean worktree 中 `dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` 不存在。
- `已确认` 旧脏 worktree 路径只作为历史 / 备选打开路径记录，不得作为默认执行路径。

## 5. 验证限制

- `部分成立` 视频文件已执行 `test -f` 与 `stat -f "%z %Sm"`。
- `部分成立` 本机当前 shell 中没有 `ffprobe` 命令；本轮已尝试执行但命令不可用。
- `已确认` 视频时长与分辨率用 macOS `mdls` 只读补充记录。
- `已确认` 图片文件已执行 `test -f`、`stat -f "%z %Sm"`、`sips -g pixelWidth -g pixelHeight`。
- `已确认` JSON 文件已执行 `test -f` 与 `stat -f "%z %Sm"`。

## 6. 边界

- `已确认` 本轮未生成视频。
- `已确认` 本轮未修改视频 / 音频 / 图片。
- `已确认` 本轮未修改 `dist/latest_review_pack（最新审片包）` 内容本体。
- `已确认` 本轮未修改 `content_validation（内容验证）`。
- `已确认` 本轮未修改 `send_ready（可发送状态）`。

## 7. 下一个目标

后续 ChatGPT 给用户本地路径时，优先读取 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`；没有 `path_exists = true（路径存在）` 的记录时，只能说“路径待本地复核”，不能直接把 manifest / summary 里的路径当作可打开路径输出。
