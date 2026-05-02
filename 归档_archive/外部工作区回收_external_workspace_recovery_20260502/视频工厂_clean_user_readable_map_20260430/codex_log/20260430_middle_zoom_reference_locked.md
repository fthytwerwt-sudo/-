# 20260430｜中段放大剪辑参考锁定

## 本轮定位

- `已确认` 本轮只更新 `codex_source/locked_reference_registry.md（锁定参考登记表）` 和日志。
- `已确认` 本轮不生成视频，不修改视频产物，不清理旧 worktree（旧工作区）。
- `已确认` 本轮使用干净 worktree（干净工作区）：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`。

## 用户确认样本

- `已确认` 用户确认的 `middle_preview（中段预览样片）` 路径为：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`。
- `已确认` repo relative（仓库相对路径）为：`dist/latest_review_pack/middle_preview.mp4`。
- `已确认` 该样片是 round34（第 34 轮）中段预览，时长 `28.52s`，分辨率 `720x1280`。
- `已确认` 用户确认依据：用户已看片确认“这一轮 middle_preview（中段预览样片）的放大剪辑是对的，可以作为参考样本”。

## 证据路径

- `dist/latest_review_pack/middle_preview.mp4（中段预览样片）`
- `dist/latest_review_pack/cut_contact_sheet.jpg（切点联系表）`
- `dist/latest_review_pack/problem_windows/30_32s.mp4（30-32 秒问题窗口）`
- `dist/latest_review_pack/problem_windows/30_32s_frames.jpg（30-32 秒问题窗口抽帧联系表）`
- `dist/latest_review_pack/timeline.json（时间线）`
- `dist/latest_review_pack/cut_map.md（镜头说明）`
- `dist/latest_review_pack/summary.json（审片包摘要）`
- `dist/latest_review_pack/review_manifest.md（审片入口）`
- `codex_log/current_publish_target.md（当前复审 / 发布目标）`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md（round34 中段修复日志）`

## registry 更新

- `已确认` 新增 `middle_zoom_reference_confirmed_middle_preview_20260430（用户确认的中段放大剪辑锁定参考）`。
- `已确认` `status（状态） = locked（锁定参考）`。
- `已确认` `confirmation_state（确认状态） = locked_reference_confirmed_by_user（用户确认锁定参考）`。
- `已确认` `type（类型） = zoom_reference（录屏放大方式参考） / middle_zoom_reference（中段放大剪辑参考）`。

## 锁定范围

- 同类中段录屏证据展示。
- 中段放大 / 裁切 / 证据窗口选择方式。
- 关键文字可读尺度。
- 放大位置必须和讲述证据点对得上。
- 后续完整成片必须输出对照证据，不能只写“类似”。

## 不锁定范围

- 不锁所有视频的固定秒级时间码。
- 不锁具体文案。
- 不锁完全不同素材结构。
- 不代表 `content_validation（内容验证）= 通过`。
- 不代表 `send_ready（可发送状态）= yes`。

## failed / gap 处理

- `已确认` `zoom_pr15_v2_failed_20260430（PR #15 v2 放大位置失败参考）` 仍保持 `failed（失败参考）`，不得继承。
- `已确认` `zoom_reference_missing_20260430（正确放大方式缺失历史记录）` 已标为 `deprecated（已废弃缺口）`，并注明主要中段放大缺口已由新的 middle zoom locked reference 补足。

## 边界

- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`。
- `已确认` 本轮不修改 `content_validation（内容验证）`。
- `已确认` 本轮不修改 `send_ready（可发送状态）`。
- `已确认` 本轮不修改视频、音频、图片产物。

## 下一个目标

下一轮进入 v3 或完整成片规划时，必须先读取 registry（登记表），继承 `middle_zoom_reference_confirmed_middle_preview_20260430（用户确认的中段放大剪辑锁定参考）` 并输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`。
