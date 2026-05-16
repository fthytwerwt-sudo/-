# 20260517 第三期真实复盘现场低置信度审片包日志

## 1. route_decision（路由判断）

- `project_route`: `video_factory`
- `task_type`: `low_confidence_review_candidate_video + material_execution + copy_iteration_candidate + project_file_change + code_debug`
- `current_project_state`: `formal_operation_active + copy_iteration_prepare + material_audit_ready + formal_next_execution_blocked`
- `execution_permission`: `low_confidence_internal_review_candidate_only`
- `large_task_gate`: `triggered`
- `lane_recommendation`: `standard_lane`
- `parallel_recommendation`: `serial_only`
- `DeepSeek`: execution pre-supply + post-risk-review, both `deepseek_passed`

## 2. state_action_router（状态动作总控器）

- `input_signal`: 用户要求按照“真实复盘现场型”结构执行。
- `inferred_state`: `low_confidence_review_candidate_allowed`
- `selected_action`: 基于 locked copy、`material_03` 和判断卡生成内部审片候选包。
- `forbidden_action`: `publish_candidate promotion`、`send_ready`、`content_validation passed`、`current_data_goal_anchor ready`、`voice_validation`、`final_voice_validated`、`visual_master_locked`。
- `done_when`: 低置信度审片包生成，技术验证通过，状态边界清楚。

## 3. 必读与 skills

本轮已读取用户指定的项目入口、运营目标、数据锚点、V003 文案迭代简报、第三期素材审计报告、GPT 数据源规则、Codex 执行规则、状态动作总控器和判断权限表。

本地仓库 `skills/` 未发现可用 skill。全局 skills 中已读取并使用 `video-metadata-probe`；已读取 HyperFrames plugin skills；未发现独立 TTS skill，TTS 按项目既有 Aliyun / Bailian 远程链路执行。

## 4. materials_used（使用素材）

- `main_material`: `material_03`，`/Users/fan/Documents/视频工厂/素材录制/第三期/v004 2026-05-16 23-22-13.mp4`
- `auxiliary_material`: `material_01`，`/Users/fan/Documents/视频工厂/素材录制/第三期/第二期 2026-05-15 23-15-27.mp4`
- `material_02_used`: `false`
- `material_02_policy`: 默认不使用；本轮未进入时间线，未使用未打码隐私画面。

## 5. media_probe（媒体检查）

### material_03

- `duration`: `205.933333s`
- `resolution`: `2912x1650`
- `fps`: `30`
- `codec`: `h264`
- `audio`: `false`
- `decode`: `passed`

### material_01

- `duration`: `96.333333s`
- `resolution`: `3148x1676`
- `fps`: `30`
- `codec`: `h264`
- `audio`: `false`
- `decode`: `passed`

## 6. locked_copy_contract（锁定文案契约）

- `locked_title`: `AI 时代，真正拉开差距的不是数据，是复盘能力`
- `locked_opening_line`: `AI 时代，真正拉开差距的不是数据，是复盘能力。`
- `allowed_copy_changes`: 标点微调、字幕分句、TTS 停顿、口播断句、为字幕可读性换行。
- `forbidden_copy_changes`: 不改标题、开头句、核心判断、“不是方向，而是开头”、“只改一个变量”、“播放是入口，收藏是认可，私信要评分”；不新增素材没有证明的数据、私信 / 咨询 / 客资 / 商业结果。
- `codex_semantic_rewrite_performed`: `false`

## 7. timeline_plan（时间线计划）

- `opening_card`: 0-3s，HyperFrames `clean_soft` 开头判断卡，文案为锁定标题，小字为 `141 播放｜2 秒跳出接近 50%｜收藏 3`。
- `material_03_segments`: 承担主干复盘现场，包括数据冲突、开头承接弱、下一条只改开头、数据不是答案、指标与变量关系、规则表和 next copy revision brief。
- `auxiliary_material_01`: 少量用于“素材准备 / 候选选题池”背景，不当作真实前后对比证明。
- `light_judgment_card_02`: `数据不是答案 / 数据是定位器`。
- `light_judgment_card_01`: `不是方向错 / 是开头没接住`。
- `closing_summary_card`: `哪一层出了问题？ / 下一条只改哪个变量？ / 改完看哪个指标？`

## 8. outputs_generated（生成产物）

输出目录：

`dist/third_episode_real_review_scene_candidate/`

核心产物：

- `full.mp4`
- `review_manifest.md`
- `summary.json`
- `content_route_card_v2.json`
- `script_to_timeline_map.json`
- `card_placement_decision.json`
- `subtitle_card_overlap_check.json`
- `media_probe.json`
- `locked_copy_contract.json`
- `captions.srt`
- `narration.wav`
- `narration_tts_debug_sanitized.json`
- `tts_prosody_anchor_map.json`
- `hyperframes_cards/`

## 9. TTS 与 HyperFrames 边界

- `TTS provider`: `aliyun_bailian`
- `TTS model`: `qwen3-tts-vc-realtime-2026-01-15`
- `local_tts_fallback_used`: `false`
- `macos_say_used`: `false`
- `silent_audio_fallback_used`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `voice_validation_advanced`: `false`

HyperFrames 真实渲染卡片已生成，`hyperframes_used = true`，视觉皮肤为 `clean_soft`。本轮不把 HyperFrames 卡片写成视觉母版锁定。

## 10. validation（验证）

- `JSON parse`: passed
- `script_to_timeline_map.line_group_count`: `20`
- `script_to_timeline_map.video_duration_nulls`: `0`
- `full_mp4`: exists
- `resolution`: `1920x1080`
- `fps`: `30/1`
- `aspect_ratio`: `16:9`
- `audio_present`: `true`
- `subtitles_present`: `true`
- `decode`: passed
- `subtitle_card_overlap_check`: passed
- `material_02_unblurred_used`: `false`
- `forbidden_status_scan`: passed
- `source_media_not_staged`: verified before commit

## 11. status_boundary（状态边界）

- `low_confidence_review_candidate`: `true`
- `publish_candidate_ready_for_human_review`: `false`
- `content_validation advanced`: `no`
- `send_ready advanced`: `no`
- `current_data_goal_anchor ready`: `no`
- `publish_status_success advanced`: `no`
- `voice_validation advanced`: `no`
- `final_voice_validated advanced`: `no`
- `visual_master_locked advanced`: `no`
- `next formal video prompt generated`: `no`

## 12. 下一步建议

本轮产物只适合内部审片：判断“真实复盘现场型”结构、`material_03` 作为主干、轻判断卡压缩结论是否顺。若要进入正式候选，仍需用户 / ChatGPT 复审内容观感、声音听感、节奏和素材证据窗口；不得把本轮直接升级成发布候选。
