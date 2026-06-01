# Current Publish Target

## 0A. formal_operation override

`已确认` 2026-05-15 起，当前项目阶段已迁移为 `formal_operation_active（正式运营中）`。

本文件中关于 V001 / v3.1 `gray_test` 的旧字段只作为 `legacy_previous_term（历史兼容术语）` 保留。当前运营目标以 `codex_log/current_operation_target.md` 为准；三期运营记录以 `review_loop/operation_records_index.md` 为准。

正式运营不等于内容通过、商业验证成立、数据飞轮跑通或 `send_ready = true`。

## 0B. 20260602 新第四期参考引导候选片补充入口

- `已确认` 本轮新增新第四期完整参考引导候选片：`dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/full.mp4`。
- `review_pack`: `dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523`
- `review_manifest`: `dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/review_manifest.md`
- `summary`: `dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/summary.json`
- `reference_deviation_check`: `dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/reference_deviation_check.json`
- `publish_candidate_preflight_report`: `dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/publish_candidate_preflight_report.json`
- `status`: `publish_candidate_ready_for_human_review`
- `content_validation`: `pending_user_chatgpt_review`
- `send_ready`: `false`
- `voice_validation`: `pending_user_chatgpt_review`
- `visual_master_locked`: `false`
- `边界` 本补充入口不替换下方 legacy v3.1 / `dist/latest_review_pack/` 当前复审对象，不覆盖当前运营数据目标。

## legacy_previous_publish_target 旧发布目标口径

- `已确认` 本文件记录《视频工厂》当前复审 / publish target 入口。
- `已确认` 当前主题为《我用 AI 做 PPT 踩过的坑》v3.1。
- `已确认` 当前最新复审对象为：`dist/latest_review_pack/`。
- `已确认` 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`。
- `已确认` 当前视频基线：`current_video_baseline = v3.1`。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基础：`future_iteration_base = v3.1`。
- `已确认` v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` 用户最终人工确认前，`send_ready` 必须保持 `false` / `no`。
- `legacy` 用户曾确认：v3.1 已发片，旧阶段进入灰度测试。
- `legacy_previous_phase`：`post_publish_gray_test（发布后灰度测试阶段）`。
- `legacy_previous_publish_status`：`gray_test_published（已发片，进入灰度测试）`。
- `legacy_previous_gray_test_status`：`active（灰度测试中）`。
- `已确认` 发布后复盘：`post_publish_review_required = true（需要发布后复盘）`。
- `legacy_previous_content_validation`：`gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`。

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
- `legacy_previous_phase`：`post_publish_gray_test`
- `legacy_previous_publish_status`：`gray_test_published`
- `legacy_previous_gray_test_status`：`active`
- `post_publish_review_required`：`true`
- `gray_test_metrics_v1`：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- `current_gray_test_target`：`codex_log/current_gray_test_target.md`
- `screenshot_data_intake_rules`：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- `current_video_record_dir`：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- `current_video_record`：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- `legacy_video_record`：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- `current_screenshot_root`：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- `technical_validation`：`passed`
- `technical_line_locked`：`false`
- `technical_baseline_locked`：`false`
- `technical_upgrade_next`：`true`
- `metadata_validation`：`passed`
- `audio_validation`：`passed_non_silent_tts_track`
- `subtitle_enabled`：`false`
- `legacy_previous_content_validation`：`gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`
- `send_ready`：`false`
- `visual_master_candidate`：`true`
- `visual_master_locked`：`false`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 当前唯一最高优先级 blocker

- `已确认` v3.1 是当前迭代基线，但不是可发送版本。
- `legacy` v3.1 已发片进入灰度测试，但该旧阶段不等于内容通过。
- `已确认` v3.1 需要跑完 24h / 72h 灰度观察，再进入 Codex 初检与 ChatGPT / 用户判断。
- `已确认` 下一步仍需要技术升级。
- `已确认` 后续修改必须保持三条视觉路由不混。

## legacy_previous_gray_test_target

- legacy 目标文件：`codex_log/current_gray_test_target.md`
- 截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 当前视频记录目录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- 当前单条主记录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- 兼容旧记录入口：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- 当前截图证据目录：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- 当前复盘机制：沿用既有 `review_loop/`，不新建独立灰度系统。
- 当前指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- 当前目标：用 v3.1 这条已发布视频跑完 24h / 72h / 7 天灰度观察，判断它的主要问题层，并产出下一轮“只改一个变量”的执行方向。
- 7 天播放量基础测试流量门槛：`6000`
- 指标体系定位：不是运营数据大表，而是下一轮改动定位器。
- 当前录入方式：用户可直接提交截图；Codex 按视频 / 时间窗 / 数据类型归档，提取可识别字段，标记缺失与不确定项，再交给 ChatGPT 复盘。
- 当前分桶规则：不同视频分开，`24h / 72h / 7d` 分开，平台数据 / 评论 / 私信 / 咨询等类型分开。
- 当前 24h 数据状态：`待用户回填`
- 当前 72h 数据状态：`待用户回填`
- 当前 7 天数据状态：`待用户回填`
- 当前四个复盘问题：
  1. 这条有没有达到 6000 播放基础门槛？
  2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
  3. 下一轮只改哪一个变量？
  4. 为什么先改它，改完看哪个指标？
- 当前禁止：不得写成内容通过、不得写成最终成功、不得跳过数据直接设定新文案。

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
9. `codex_log/current_gray_test_target.md`
10. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
11. `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
12. `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
13. `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
14. `review_loop/00_review_loop_readme.md`
15. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`

## 当前同步状态

- 状态分类：`formal_sync_target_for_user_readable_map`
- 当前工作分支：`codex/v31-screenshot-data-buckets-20260502`
- 当前主读取分支：`codex/user-readable-map`
- 本轮同步要求：commit、push 当前分支，创建 PR，并在验证通过后合并到 `codex/user-readable-map`。
- 本轮边界：不重新生成视频、不重新生成音频、不重新生成图片、不重新装配全片、不写新文案。

## 最后更新时间

- `2026-05-02 CST`

## 对应 dated log 路径

- `codex_log/20260502_截图数据录入与时间窗分桶机制.md`
