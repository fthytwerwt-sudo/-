# Current Publish Target Light Evidence

## 对应对象

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- 当前视频基线：`v3.1`
- 后续默认迭代基础：`v3.1`
- 当前完整片：`dist/latest_review_pack/full.mp4`
- 当前审片入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`

## Git 可追踪轻量证据包

1. `dist/latest_review_pack/summary.json`
   - `current_video_baseline = v3.1`
   - `future_iteration_base = v3.1`
   - `content_validation = pending_user_chatgpt_review_or_not_passed_copywriting_side`
   - `send_ready = false`
   - `visual_master_locked = false`
   - `voice_validation = pending_user_chatgpt_review`
   - `sassy_card_execution_reference = PR7_B_骚萌反应页.png`
   - `sassy_card_execution_reference_id = sassy_card_pr7_b_visual_locked_20260501`
2. `dist/latest_review_pack/review_manifest.md`
   - 明确 v3.1 是当前基线。
   - 明确 v3.1 不是可发送状态。
   - 明确内容仍待用户 / ChatGPT 复审，未写成内容通过。
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

## 这些轻量证据共同证明什么

- `已确认` 当前最新视频基线已经切换到 v3.1。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1。
- `已确认` v3 只保留为历史候选 / 对照。
- `已确认` v3.1 技术验证与视觉路由验证有可追踪证据。
- `已确认` v3.1 仍不可发送。
- `已确认` v3.1 内容没有写成通过。
- `已确认` PR #7 B 是后续骚萌卡唯一执行参考。
- `已确认` PR #7 A 只保留为历史 / candidate 对照。

## 当前不能证明什么

- 不能证明 v3.1 内容通过。
- 不能证明 v3.1 可发送。
- 不能证明技术线最终锁定。
- 不能证明视觉母版已锁定。
- 不能证明声音最终通过。

## 最后更新时间

- `2026-05-02 CST`
