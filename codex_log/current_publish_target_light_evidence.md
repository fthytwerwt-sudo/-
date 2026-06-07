# Current Publish Target Light Evidence

## 0A. formal_operation override

`已确认` 当前 canonical 运营入口已迁移到 `codex_log/current_operation_target.md`。

本文件保留 V001 / v3.1 旧发布目标轻量证据；其中 `gray_test` 字段均按 `legacy_previous_term` 读取，不再作为当前默认项目阶段。

## 对应对象

- 20260607 V006 第六期新素材无 GPT 图标重做候选片：`dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/full.mp4`
- 20260607 V006 review pack：`dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300`
- 20260607 V006 review manifest：`dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/review_manifest.md`
- 20260607 V006 summary：`dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/summary.json`
- 20260607 V006 图标专项检查：`dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/gpt_icon_exposure_check.md`
- 20260607 V006 状态：`publish_candidate_ready_for_human_review`
- 20260607 V006 边界：`old_material_reused = false`，`locked_copy_changed = false`，`content_validation = pending_user_chatgpt_review`，`send_ready = false`，`voice_validation = pending_user_chatgpt_review / not_advanced`，`visual_master_locked = false`
- 20260607 V006 不替换 legacy v3.1 / `dist/latest_review_pack/` 当前复审对象，不覆盖当前运营数据目标。

- 20260602 新第四期新增完整参考引导候选片：`dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523/full.mp4`
- 20260602 新第四期 review pack：`dist/new_fourth_episode_reference_guided_publish_candidate_20260602_034523`
- 20260602 新第四期状态：`publish_candidate_ready_for_human_review`
- 20260602 新第四期边界：`content_validation = pending_user_chatgpt_review`，`send_ready = false`，`voice_validation = pending_user_chatgpt_review`，`visual_master_locked = false`
- 20260602 新第四期不替换 legacy v3.1 / `dist/latest_review_pack/` 当前复审对象，不覆盖当前运营数据目标。

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- 当前视频基线：`v3.1`
- 后续默认迭代基础：`v3.1`
- 当前完整片：`dist/latest_review_pack/full.mp4`
- 当前审片入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`
- legacy_previous_phase：`post_publish_gray_test`
- legacy_previous_publish_status：`gray_test_published`
- legacy_previous_gray_test_status：`active`
- legacy_previous_gray_test_target：`codex_log/current_gray_test_target.md`
- 当前截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 当前单条主记录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- 当前记录目录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- 当前截图证据目录：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- 当前指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`

## Git 可追踪轻量证据包

1. `dist/latest_review_pack/summary.json`
   - `current_video_baseline = v3.1`
   - `future_iteration_base = v3.1`
   - `legacy_previous_phase = post_publish_gray_test`
   - `legacy_previous_publish_status = gray_test_published`
   - `legacy_previous_gray_test_status = active`
   - `post_publish_review_required = true`
   - `legacy_previous_content_validation = gray_testing_not_final_passed`
   - `send_ready = false`
   - `visual_master_locked = false`
   - `voice_validation = pending_user_chatgpt_review`
   - `sassy_card_execution_reference = PR7_B_骚萌反应页.png`
   - `sassy_card_execution_reference_id = sassy_card_pr7_b_visual_locked_20260501`
2. `dist/latest_review_pack/review_manifest.md`
   - 明确 v3.1 是当前基线。
   - 明确 v3.1 不是可发送状态。
   - 明确 v3.1 旧阶段曾发片进入灰度测试。
   - 明确旧灰度测试不等于内容通过。
3. `dist/latest_review_pack/visual_route_map.json`
   - 三张骚萌卡走 `sassy_reaction_card_route`。
   - 信息卡走 `cute_info_card_route`。
   - 反面 / 正面展示提示卡走 `cute_prompt_card_route`。
4. `dist/latest_review_pack/visual_route_validation_report.json`
   - `passed = true`
   - `route_map_exists = true`
   - `sassy_cards_use_pr7_b_reference = true`
   - `send_ready_unchanged = true`
5. `dist/latest_review_pack/video_metadata_probe_report.json`
   - `duration_seconds = 149.993000`
   - `width = 720`
   - `height = 1280`
   - `audio_present = true`
   - `decodable = true`
   - `validation_status = passed`
6. `codex_source/locked_reference_registry.md`
   - `sassy_card_pr7_b_visual_locked_20260501（PR #7 B 骚萌卡视觉锁定参考）`
   - `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）` 保留为历史 / candidate 对照，不再作为后续执行参考。
7. `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
   - 明确 v3.1 是当前基线。
   - 明确后续修改必须先复核 `visual_route_map.json`。
   - 明确 PR #7 B 缺失必须 blocked，不得回退 PR #7 A。
8. `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
   - 独立 v3.1 复审包已进入仓库。
9. `归档_archive/旧口径_old_context_20260502/README_归档说明_archive_readme.md`
   - 说明 PR #22 原始待复审状态、PR #23 原始 PR #7 A 优先判断、可爱卡片旧 route suggestion 已归档降权，后续默认不按旧口径执行。
10. `codex_log/current_gray_test_target.md`
   - 明确当前目标是跑完 24h / 72h / 7 天灰度观察，判断主要问题层，并产出下一轮只改一个变量。
   - 明确 7 天播放量 6000 是当前小样本阶段基础测试流量门槛。
11. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
   - 明确用户可以直接给截图，Codex 负责按视频 / 时间窗 / 数据类型归档、提取字段、标记缺失与不确定项。
   - 明确不同视频、`24h / 72h / 7d`、平台数据 / 评论 / 私信 / 咨询不得混写。
12. `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
   - 已建立 V001 独立主记录，支持 `24h / 72h / 7d` 分开写入；发布平台、发布时间、链接、24h / 72h / 7 天数据均待用户截图或回填。
13. `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
   - 已建立 README、三份截图提取报告模板、缺失字段记录和给 ChatGPT 的复盘输入文件。
14. `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
   - 已建立当前视频截图证据目录索引，截图按时间窗和数据类型分桶。
15. `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
   - 保留为兼容入口，并指向新的 V001 主记录目录。
16. `review_loop/00_review_loop_readme.md`
   - 明确当前 v3.1 灰度测试接入既有 `review_loop/`，不另起独立灰度系统。
17. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
   - 明确指标体系不是运营数据大表，而是下一轮改动定位器。
   - 明确四层指标：流量层、内容层、账号增长层、私域 / 客户转化层。
   - 明确字段分级：核心必填、辅助观察、商业线索出现时才填。
   - 明确四个复盘问题和下一轮只改一个变量规则。
   - 明确最低统计 `24h / 72h`，标准统计 `24h / 72h / 7d`，并按视频、时间窗、数据类型分桶。

## 这些轻量证据共同证明什么

- `已确认` 当前最新视频基线已经切换到 v3.1。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1。
- `已确认` v3.1 已发片，当前进入发布后灰度测试。
- `已确认` 发布后复盘机制已接入既有 `review_loop/`。
- `已确认` v3.1 灰度测试指标体系 V1 已接入既有 `review_loop/`。
- `已确认` 截图优先录入机制已接入既有 `review_loop/`。
- `已确认` 后续截图必须按视频、`24h / 72h / 7d` 时间窗和数据类型分开归档。
- `已确认` 7 天播放量 6000 是当前小样本阶段基础测试流量门槛。
- `已确认` 指标体系不是运营数据大表，而是下一轮改动定位器。
- `已确认` v3 只保留为历史候选 / 对照。
- `已确认` v3.1 技术验证与视觉路由验证有可追踪证据。
- `已确认` v3.1 仍不可发送。
- `已确认` v3.1 内容没有写成通过。
- `已确认` PR #7 B 是后续骚萌卡唯一执行参考。
- `已确认` PR #7 A 只保留为历史 / candidate 对照。

## 当前不能证明什么

- 不能证明 v3.1 内容通过。
- 不能证明 v3.1 可发送。
- 不能证明灰度测试已经成功。
- 不能证明账号方向、市场或规律已经成立。
- 不能证明 7 天播放已经达到 6000。
- 不能证明下一轮唯一变量已经可以拍板。
- 不能证明技术线最终锁定。
- 不能证明视觉母版已锁定。
- 不能证明声音最终通过。

## 最后更新时间

- `2026-05-02 CST`
