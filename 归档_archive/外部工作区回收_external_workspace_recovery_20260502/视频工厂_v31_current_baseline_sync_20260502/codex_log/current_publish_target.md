# Current Publish Target

## 当前口径

- `已确认` 本文件记录《视频工厂》当前复审 / publish target 入口。
- `已确认` 当前主题为《我用 AI 做 PPT 踩过的坑》v3.1。
- `已确认` 当前最新复审对象为：`dist/latest_review_pack/`。
- `已确认` 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`。
- `已确认` 当前视频基线：`current_video_baseline = v3.1`。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基础：`future_iteration_base = v3.1`。
- `已确认` v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` 用户最终人工确认前，`send_ready` 必须保持 `false` / `no`。

## 当前复审 target

- 当前完整片：`dist/latest_review_pack/full.mp4`
- 当前 contact sheet：`dist/latest_review_pack/cut_contact_sheet.jpg`
- 当前复审入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`
- 当前视觉路由表：`dist/latest_review_pack/visual_route_map.json`
- 当前视觉路由验证：`dist/latest_review_pack/visual_route_validation_report.json`
- 当前继承报告：`dist/latest_review_pack/locked_reference_inheritance_report.md`
- 当前 metadata probe：`dist/latest_review_pack/video_metadata_probe_report.json`

## 当前正式状态

- `current_round`：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- `current_video_baseline`：`v3.1`
- `future_iteration_base`：`v3.1`
- `base_for_next_upgrade`：`v3.1`
- `technical_validation`：`passed`
- `technical_line_locked`：`false`
- `technical_baseline_locked`：`false`
- `technical_upgrade_next`：`true`
- `metadata_validation`：`passed`
- `audio_validation`：`passed_non_silent_tts_track`
- `subtitle_enabled`：`false`
- `content_validation`：`pending_user_chatgpt_review_or_not_passed_copywriting_side（v3.1 仍待用户 / ChatGPT 内容复审；不得写成内容通过）`
- `send_ready`：`false`
- `visual_master_candidate`：`true`
- `visual_master_locked`：`false`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 当前唯一最高优先级 blocker

- `已确认` v3.1 是当前迭代基线，但不是可发送版本。
- `已确认` v3.1 内容仍需用户 / ChatGPT 复审；不得写成内容通过。
- `已确认` 下一步仍需要技术升级。
- `已确认` 后续修改必须保持三条视觉路由不混。

## reference 口径

- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 是后续骚萌卡唯一执行参考。
- `已确认` 如果读不到 PR #7 B 原始文件或证据路径，必须 `blocked`，不得回退 PR #7 A。
- `已确认` PR #7 A 只能作为历史 / candidate 对照，不得作为任何后续骚萌卡执行参考。
- `已确认` 可爱段落提示卡路由和可爱信息卡路由已进入 route-level locked reference 流程。

## 旧 PR 降噪口径

- PR #22：v3 历史候选，不再作为后续默认基础，不直接合并。
- PR #23：历史样本包，旧 PR #7 A 优先判断已被用户最新 PR #7 B 口径覆盖，不直接合并。
- PR #24：v3.1 有效产物已安全回流到最新主读取分支，PR #24 本身不再直接合并，避免回退 PR #25 清理结果。
- PR #25：已合并，保留为旧口径清理与归档基线。

## 现在最该看的入口

1. `dist/latest_review_pack/review_manifest.md`
2. `dist/latest_review_pack/summary.json`
3. `dist/latest_review_pack/visual_route_map.json`
4. `dist/latest_review_pack/visual_route_validation_report.json`
5. `codex_source/locked_reference_registry.md`
6. `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
7. `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
8. `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png`

## 当前同步状态

- 状态分类：`formal_sync_target_for_user_readable_map`
- 当前工作分支：`codex/v31-current-baseline-sync-20260502`
- 当前主读取分支：`codex/user-readable-map`
- 本轮同步要求：commit、push 当前分支，创建 PR，并在验证通过后合并到 `codex/user-readable-map`。
- 本轮边界：不重新生成视频、不重新生成音频、不重新生成图片、不重新装配全片。

## 最后更新时间

- `2026-05-02 CST`

## 对应 dated log 路径

- `codex_log/20260502_v31当前基线切换与旧PR降噪.md`
