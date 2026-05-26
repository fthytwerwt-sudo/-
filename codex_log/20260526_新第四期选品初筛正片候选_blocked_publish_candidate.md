# 20260526｜新第四期选品初筛锁稿正片候选阻断

- `task_result.status = blocked`
- `blocked_type = blocked_publish_candidate_unavailable`
- `target_delivery = publish_candidate_ready_for_human_review`
- `degradation_used = false`
- `no_degraded_output_created = true`
- `review_pack_path = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604`

## Route Decision

- `project_route = video_factory`
- `task_type = locked_copy_video_execution + publish_candidate_delivery + final_script_to_video + tts_route_execution + video_sample_or_assembly`
- `responsibility_layer = execution_layer + validation_layer + sync_layer`
- `large_task_gate = triggered`
- `lane_recommendation = serial_only`
- `parallel_recommendation = read_parallel_only`
- `target_delivery = publish_candidate_ready_for_human_review`
- `degradation_allowed = false`
- `blocked_instead_of_degraded = true`

## Locked Copy

- `locked_copy_created = true`
- `locked_copy_changed = false`
- `old_v02_reused = false`
- `locked_title = 新第四期选品初筛`
- `locked_opening_line = 朋友们，你有没有发现，现在做带货，最贵的已经不是拍一条视频了。`

## Material / Visual Gate

- `line_group_count = 245`
- `near_equivalent_count = 10`
- `near_equivalent_ratio = 0.0408`
- `consecutive_near_equivalent_max = 5`
- `core_evidence_mismatch_count = 10`
- `whole_video_drift_detected = false`
- `auto_edit_allowed = false`

阻断原因：

1. 锁稿中的“Codex 操作我的电脑 / 进入选品页面 / 输入品类词 / 一张一张翻商品卡”属于核心动作证据，现有素材只支持商品卡、表格和 AI 输出参考，不能无猜测证明该动作。
2. SKU 复杂度作为核心风险例子缺少清楚可读的 SKU/规格页或复查表近景。
3. 候选表、明细表、复查表虽有素材支持，但当前审计标注存在小字、隐私、路径或遮挡风险，未达到可发布候选的核心证据可读标准。
4. 旧 preflight 已提出 `copy_change_request`，但本轮锁稿禁止 Codex 改稿，因此只能 blocked。

## TTS Gate

- `actual_tts_provider = minimax`
- `actual_tts_model = MiniMax/speech-2.8-hd`
- `selected_route = route_b / aliyun_bailian_proxy_to_minimax`
- `candidate_narration_generated = false`
- `audio_present = false`
- `non_silent = false`
- `fallback_tts_used = false`
- `macos_say_used = false`
- `local_low_quality_tts_used = false`

MiniMax route smoke 结果：

- `audio_generated = true`
- `task_status = blocked`
- `blocked_reason = generated_audio_failed_technical_validation`
- smoke 音频仅为路线诊断，不是候选片旁白。

## Preflight Suite

- `publish_candidate_preflight_suite.status = blocked`
- `passed_gates = card_decision_preflight + forbidden_action_preflight + locked_copy_diff_preflight`
- `failed_gates = line_level_alignment_preflight + line_visual_tolerance_preflight + near_equivalent_material_substitution_preflight + tts_route_and_prosody_preflight + publish_candidate_voice_gate + b_voice_feel_minimax_preflight + visual_evidence_readability_preflight + publish_candidate_user_standard_preflight + completion_truth_preflight`
- `missing_review_pack_reports = []`

## Media Validation

- `full.mp4 = not_generated`
- `narration.wav = not_generated`
- `captions.srt = not_generated`
- `ffprobe/full_video = not_run_no_candidate_video`
- `ffmpeg_decode/full_video = not_run_no_candidate_video`
- `secret_scan = passed_no_raw_secret_detected`

## Status Boundary

- `publish_candidate_ready_for_human_review = false`
- `content_validation = pending_user_chatgpt_review_if_future_candidate_generated`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review_if_future_candidate_generated`
- `final_voice_validated = false`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = false`

## Recommended Next Material

1. `R001` Codex / computer-use 连续操作录屏：进入选品页面、输入品类词、逐张翻商品卡。
2. `R002` 商品卡字段高清近景：价格、佣金、销量、店铺分、商品分、退货风险。
3. `R003` 候选表 / 明细表高清近景或静态图。
4. `R004` 复查表高清近景或静态图，含四个复查对象和下一步核验项。
5. `R005` SKU / 规格复杂度证据，或由用户确认文案修改请求。
