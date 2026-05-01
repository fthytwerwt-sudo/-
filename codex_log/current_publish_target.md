# Current Publish Target

## 当前口径

- `已确认` 本文件记录《视频工厂》当前复审 / publish target 入口。
- `已确认` 当前主题为《我用 AI 做 PPT 踩过的坑》v3。
- `已确认` 当前最新复审对象为：`dist/latest_review_pack/`。
- `已确认` 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3`。
- `已确认` 当前用户已完成 v3 复审；本文件写入用户最新确认后的仓库口径。
- `已确认` 用户最终人工确认前，`send_ready` 必须保持 `false` / `no`。

## 当前复审 target

- 当前完整片：`dist/latest_review_pack/full.mp4`
- 当前 contact sheet：`dist/latest_review_pack/cut_contact_sheet.jpg`
- 当前复审入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`
- 当前继承报告：`dist/latest_review_pack/locked_reference_inheritance_report.md`
- 当前 metadata probe：`dist/latest_review_pack/video_metadata_probe_report.json`

## 当前正式状态

- `v3_technical_milestone`：`reached_for_current_stage（当前阶段技术里程碑达成）`
- `technical_validation`：`reached_for_current_stage（当前阶段达成，不等于技术线最终锁定）`
- `technical_baseline_locked`：`false`
- `technical_upgrade_next`：`true`
- `metadata_validation`：`passed`
- `audio_validation`：`passed_non_silent_tts_track`
- `subtitle_enabled`：`false`
- `content_validation`：`not_passed_user_review_gpt_copywriting_side（用户复审未过线，主要在 GPT 文案侧）`
- `send_ready`：`false`
- `visual_master_candidate`：`true`
- `visual_master_locked`：`false`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 当前唯一最高优先级 blocker

- `已确认` v3 内容未过线，主要 blocker 在 GPT 文案侧。
- `已确认` v3 技术层只能作为当前阶段里程碑，下一步仍需技术升级。
- `已确认` 视觉路由必须在下一轮 v3.1 生成前拆开：段落提示卡、信息卡、骚萌卡不得继续共用同一套外壳。

## reference 口径

- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 是后续骚萌卡执行参考。
- `已确认` 如果读不到 PR #7 B 原始文件或证据路径，必须 `blocked`，不得回退 PR #7 A。
- `已确认` PR #7 A 保留为历史 / candidate 对照，不再作为下一轮 v3.1 后续骚萌卡执行参考。
- `已确认` 可爱段落提示卡路由和可爱信息卡路由已进入 route-level locked reference 流程。

## 下一轮 v3.1 前置规则

- `已确认` 下一轮 v3.1 生成前必须先输出并验证 `visual_route_map.json（视觉路由表）`。
- `已确认` route map 验证通过前，不得生成 v3.1 全片。
- `已确认` 三条 route 必须拆开：
  - `cute_prompt_card_route（可爱段落提示卡路由）`
  - `cute_info_card_route（可爱信息卡路由）`
  - `sassy_reaction_card_route（骚萌反应卡路由）`

## 现在最该看的入口

1. `dist/latest_review_pack/review_manifest.md`
2. `dist/latest_review_pack/summary.json`
3. `codex_source/locked_reference_registry.md`
4. `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
5. `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png`
6. `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/视觉判断_cute_card_visual_review.md`

## 当前同步状态

- 状态分类：`formal_sync_target_for_user_readable_map`
- 当前工作分支：`codex/v3-milestone-reference-locks-v31-routing-20260501`
- 当前主读取分支：`codex/user-readable-map`
- 本轮同步要求：commit、push 当前工作分支，并合并 / 快进到 `codex/user-readable-map`。

## 最后更新时间

- `2026-05-01 CST`

## 对应 dated log 路径

- `codex_log/20260501_v3技术里程碑与v31视觉参考锁定.md`
