# Current Publish Target Light Evidence

## 对应对象

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- 当前视频基线：`v3.1`
- 后续默认迭代基础：`v3.1`
- 当前完整片：`dist/latest_review_pack/full.mp4`
- 当前审片入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`
- 当前阶段：`post_publish_gray_test`
- 当前发布状态：`gray_test_published`
- 当前灰度状态：`active`
- 当前灰度目标：`codex_log/current_gray_test_target.md`
- 当前单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- 当前指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`

## Git 可追踪轻量证据包

1. `dist/latest_review_pack/summary.json`
   - `current_video_baseline = v3.1`
   - `future_iteration_base = v3.1`
   - `current_phase = post_publish_gray_test`
   - `publish_status = gray_test_published`
   - `gray_test_status = active`
   - `post_publish_review_required = true`
   - `content_validation = gray_testing_not_final_passed`
   - `send_ready = false`
   - `visual_master_locked = false`
   - `voice_validation = pending_user_chatgpt_review`
   - `sassy_card_execution_reference = PR7_B_骚萌反应页.png`
   - `sassy_card_execution_reference_id = sassy_card_pr7_b_visual_locked_20260501`
2. `dist/latest_review_pack/review_manifest.md`
   - 明确 v3.1 是当前基线。
   - 明确 v3.1 不是可发送状态。
   - 明确 v3.1 已发片进入灰度测试。
   - 明确灰度测试不等于内容通过。
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
11. `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
   - 已建立 v3.1 单条发布后灰度测试记录；发布平台、发布时间、链接、24h / 72h / 7 天数据均待用户回填。
12. `review_loop/00_review_loop_readme.md`
   - 明确当前 v3.1 灰度测试接入既有 `review_loop/`，不另起独立灰度系统。
13. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
   - 明确指标体系不是运营数据大表，而是下一轮改动定位器。
   - 明确四层指标：流量层、内容层、账号增长层、私域 / 客户转化层。
   - 明确字段分级：核心必填、辅助观察、商业线索出现时才填。
   - 明确四个复盘问题和下一轮只改一个变量规则。

## 这些轻量证据共同证明什么

- `已确认` 当前最新视频基线已经切换到 v3.1。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1。
- `已确认` v3.1 已发片，当前进入发布后灰度测试。
- `已确认` 发布后复盘机制已接入既有 `review_loop/`。
- `已确认` v3.1 灰度测试指标体系 V1 已接入既有 `review_loop/`。
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
