# TTS Voice Identity Audit｜新第四期选品初筛

## Scope

- `task_type = readonly_tts_voice_audit`
- `will_call_tts_api = false`
- `will_generate_audio = false`
- `will_generate_video = false`
- `will_change_copy = false`
- `will_change_media = false`
- `will_change_rules = false`
- 本报告只解释为什么当前候选片听起来不像预定 B 方案声音，不修复、不重生成、不推进声音状态。

## 1. 当前 TTS 技术路线

`route_status = route_correct`。

- `actual_tts_provider = minimax`
- `actual_tts_model = MiniMax/speech-2.8-hd`
- `selected_route = aliyun_bailian_proxy_to_minimax`
- `audio_present = true`
- `non_silent = true`
- `fallback_tts_used = false`
- `macos_say_used = false`
- `local_low_quality_tts_used = false`

关键边界：路线正确不等于声音身份正确。

## 2. 实际声音身份

当前生成脚本里实际传给 MiniMax 的声音身份是：

- `voice_id = female-tianmei`
- `voice_setting.speed = 1.16`
- `voice_setting.vol = 1`
- `voice_setting.pitch = 0`
- `voice_setting.emotion = calm`
- `style_prompt = missing`
- `speaker / speaker_id / timbre = missing`

证据：

- `scripts/生成新第四期选品初筛MiniMax正片候选_rerun_generate_new_fourth_selection_minimax_publish_candidate.py`
- `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/tts_segments/chunk_001_debug_sanitized.json`

注意：本轮只找到了生成脚本中的请求 payload 结构，以及每个 chunk 的 `voice_id_masked = female-tianmei` 调试记录；完整运行时 request payload 没有单独持久化，所以标记为 `partial_script_payload_found_runtime_full_payload_not_persisted`。

## 3. B 方案当前如何表示

当前 B 方案不是一个 MiniMax 具体声音身份，而是：

- `type = feel_tags_only`
- `b_voice_scheme_role = formal_voice_feel_reference`
- `voice_feel_tags = light_companion / low_pressure / natural_spoken_chinese / b_pacing_feel / subtle_pause_joke_rhythm / game_guide_feeling / not_broadcast / not_sales / not_customer_service / not_childish_cute_voice`

没有发现：

- 具体的 `expected_b_minimax_voice_id`
- 具体的 MiniMax 音色名
- MiniMax 对参考音频的相似度检查
- 人耳复审通过记录

历史 B 方案的具体声音锚点是旧 Qwen custom voice：

- `voice_masked = qwen-t...ac19`
- `target_model = qwen3-tts-vc-realtime-2026-01-15`
- `reference_audio = dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`

该锚点从 2026-05-25 起被机制降级为 `voice_feel_reference`，不能作为正片候选默认 TTS 生成路线，也不能直接当作 MiniMax `voice_id` 使用。

## 4. `b_voice_feel_reflected = true` 的真实依据

当前依据是结构检查，不是听感实审。

- `tts_route_report.json`: `check_depth = structural_check_only`
- `b_voice_feel_minimax_report.json`: `check_depth = structural_check_only`
- `scripts/正片候选TTS路线_publish_candidate_tts_route.py` 会根据显式 `b_voice_feel_reflected` 或 required `voice_feel_tags` 判断通过。
- rerun 生成脚本直接写入了 `b_voice_feel_reflected = true` 和完整 `voice_feel_tags`。

所以：

- `b_voice_feel_reflected_is_structural_only = true`
- `human_voice_review_still_required = true`
- 不得把这项写成“预定 B 声音身份已锁定”或“声音已通过”。

## 5. 为什么听起来不像预定 B

最可能原因：

1. 当前实际使用的是 MiniMax system voice `female-tianmei`。
2. 预定 B 的历史具体声音是 Qwen custom voice `qwen-t...ac19`，没有传入 MiniMax。
3. 当前没有 MiniMax 内部的 B voice identity，也没有把参考音频做相似度 gate。
4. 当前没有 `style_prompt / instructions` 去约束“停顿梗感、轻吐槽、游戏向导感”的具体说话方式。
5. 长文被拆成 14 个 chunk，每个 chunk 是独立远端调用；虽然重复了同一个 `voice_setting`，但没有重复 style prompt，微停顿和梗感可能被拉平。
6. `speed = 1.16` 和 `emotion = calm` 可能进一步把声音推向普通平稳读稿，而不是用户预期的 B 停顿梗感。

## 6. Chunking 风险

- `chunk_count = 14`
- `chunking_strategy = max_chars=260`
- `chunk_pause_strategy = 每个 chunk 后插入约 0.12s silence`
- `whether_each_chunk_repeats_voice_prompt = voice_setting repeated, style_prompt missing`
- `whether_voice_style_may_reset_between_chunks = true`
- `whether_long_form_generation_may_flatten_style = true`
- `chunking_voice_risk = medium`

## 7. 试听片段

这些片段只是从既有 `narration.wav` 裁切，不是重新生成 TTS：

- `sample_01_opening.wav`
- `sample_02_field_listing.wav`
- `sample_03_boundary_close.wav`

## 8. 下一轮最小修复建议

应修最小点：先锁 `voice identity`，再调 `prosody`。

推荐最小修复范围：

- 增加 `expected_b_minimax_voice_id` 或先生成 MiniMax voice candidate 清单供人工选择。
- 增加 `expected_b_voice_reference_audio_path`，指向历史 B 试听样本。
- 在 TTS 报告里写入完整 `actual_voice_setting`，不只写 provider/model。
- 增加 `style_prompt_or_voice_instructions`，约束轻陪伴、低压、停顿梗感和非播音腔。
- 降低或复核 `speed`，优先试 `1.0-1.08` 区间。
- 增加人工试听 gate：`human_voice_review_status` 未通过前，不得写 `voice_validation = passed`。

结论：如果要修到用户预期声音，下一轮需要重新生成 `narration.wav`，但前提是先锁定 MiniMax 里的 B 声音身份或人工确认一个 MiniMax 替代音色。
