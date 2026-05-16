# 20260516 HyperFrames 最小卡片用户通过与视觉皮肤锁定

## route_decision

- `project_route`: video_factory
- `task_type`: user_visual_review_lock + hyperframes_visual_skin_baseline_upgrade + minimal_artifact_style_preset_generation + project_file_change
- `lane`: audit_lane -> standard_lane
- `parallel`: serial_only
- `execution_permission`: allowed_after_impact_check

## 用户人工复审

- `user_visual_review`: passed
- `reviewer`: user
- `review_basis`: user watched `dist/hyperframes_minimal_validation/combined_preview.mp4` and approved
- `locked_scope`: minimal judgment_card / summary_card visual baseline
- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards
- `judgment_card_motion_minimal_baseline`: locked
- `summary_card_motion_minimal_baseline`: locked

## 视觉皮肤锁定

- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide
- `clean_soft`: locked_as_allowed_minimal_skin
- `cute_ai_guide`: locked_as_allowed_minimal_skin
- `sharp_judgment`: not_selected_this_round
- `sharp_judgment` 未生成默认预览，未写入默认锁定皮肤，未作为判断卡 / 总结卡默认基线。

## 生成产物

- `clean_soft_judgment_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/judgment_card_clean_soft.mp4`
- `clean_soft_summary_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/summary_card_clean_soft.mp4`
- `clean_soft_combined`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/combined_clean_soft.mp4`
- `cute_ai_guide_judgment_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/judgment_card_cute_ai_guide.mp4`
- `cute_ai_guide_summary_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/summary_card_cute_ai_guide.mp4`
- `cute_ai_guide_combined`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/combined_cute_ai_guide.mp4`
- `combined_skin_review`: `dist/hyperframes_minimal_validation/visual_skins_1_3/combined_skin_review.mp4`
- `review_manifest`: `dist/hyperframes_minimal_validation/visual_skins_1_3/review_manifest.md`

## 验证结果

- `HyperFrames runtime`: found_and_callable
- `runtime_entry`: `npx --yes hyperframes@0.6.12 render`
- `actual_output_type`: real_hyperframes_motion
- `npm run check`: passed；HyperFrames lint exit 0，validate no console errors / text elements pass WCAG AA，inspect 0 layout issues。combined review 因文件较长有 composition-size / timeline-density warnings，但无 error。
- `ffprobe / ffmpeg decode`: 7 个新 MP4 均为 1920x1080、30fps、h264、可解码、无音轨。本轮不要求音轨。
- `JSON parse`: root manifest、clean_soft manifest、cute_ai_guide manifest 均通过。

## 已同步文件

- `GPT数据源/08_当前正式事实.md`：写入最小 runtime 已通过、用户人工复审通过、两套视觉皮肤锁定、正式视频链路仍待验证。
- `GPT数据源/05_文案路由规则.md`：写入 `hyperframes_visual_skin_presets`，并把 `content_route_card V2.card_placement_decision` 接入皮肤字段。
- `GPT数据源/07_AI知识类视频价值规则.md`：写入 clean_soft / cute_ai_guide 的价值边界与 sharp_judgment 未纳入。
- `codex_source/21_codex_judgment_permission_matrix.md`：新增 `hyperframes_visual_skin_permission`。
- `codex_source/01_execution_rules.md`：新增 HyperFrames 皮肤选择检查字段。
- `scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py`：新增 `--skin clean_soft`、`--skin cute_ai_guide`、`--all-locked-skins`。
- `dist/hyperframes_minimal_validation/manifest.json` 与 `review_manifest.md`：补写用户通过与最小皮肤锁定。
- `dist/hyperframes_minimal_validation/index.html` 与 `DESIGN.md`：保留当前 combined skin review 可检查 composition 与两套锁定皮肤的设计说明。

## 状态边界

- `internal_diagnostic_only`: true
- `content_validation`: not_advanced
- `send_ready`: false
- `publish_candidate`: false
- `voice_validation`: not_advanced
- `final_voice_validated`: false
- `visual_master_locked`: false
- `real_video_execution_chain_integration`: pending
- `long_term_runtime_stability`: pending

## 下一个目标

- 后续真实视频执行中，若 `card_placement_decision` 选择 `judgment_card` 或 `summary_card`，必须在 `clean_soft / cute_ai_guide` 中选择皮肤，并继续通过 locked copy 语义一致、字幕卡片不重叠、证据窗口不被打断和 HyperFrames runtime gate。
