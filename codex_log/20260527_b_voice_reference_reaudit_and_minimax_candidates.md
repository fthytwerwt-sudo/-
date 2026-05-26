# 20260527 B 声音本体重审与 MiniMax 男声/偏男候选

## 结果

- `task_result.status = completed_with_reaudited_voice_candidates`
- `video_generated = false`
- `full_narration_regenerated = false`
- `copy_changed = false`
- `current_video_modified = false`

## 产物

- `diagnostics_path = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222`
- `minimax_b_voice_identity_reaudit_report = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/minimax_b_voice_identity_reaudit_report.json`
- `b_voice_reference_audit = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/b_voice_reference_audit.json`
- `voice_candidate_review_table_v2 = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/voice_candidate_review_table_v2.md`
- `samples_dir = codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples`

## 上一轮女声候选拒绝

- `female-shaonv = rejected_by_user`
- `female-shaonv-jingpin = rejected_by_user`
- `female-yujie = rejected_by_user`
- `user_reason = wrong_gender_and_wrong_voice_identity`
- `future_use_allowed = false`

已更新上一轮复审表：

- `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/voice_candidate_review_table.md`
- `codex_log/diagnostics/minimax_b_voice_identity_lock_20260527_003423/voice_candidate_review_table.json`

## B 声音目标画像

- `gender_target = male_or_male_leaning`
- `timbre_target = low_pressure_natural_male_leaning_companion_tone`
- `pause_target = moderate_to_clear_boundary_pause_with_joke_timing`
- `emotion_target = warm_light_roast_sincere_explanatory`
- `must_not_be = female_system_voice / childish_cute_voice / broadcast_voice / sales_voice / flat_reader_voice`
- `human_audio_reference_review_needed = true`

## 新候选

| base_candidate_id | voice_id | voice_name | versions |
| --- | --- | --- | --- |
| BMALE_01 | male-qn-qingse | 青涩青年音色 | v1_identity_stable / v2_emotional_rich |
| BMALE_02 | male-qn-daxuesheng | 青年大学生音色 | v1_identity_stable / v2_emotional_rich |
| BMALE_03 | Chinese (Mandarin)_Gentleman | 温润男声 | v1_identity_stable / v2_emotional_rich |
| BMALE_04 | Chinese (Mandarin)_Gentle_Youth | 温润青年 | v1_identity_stable / v2_emotional_rich |
| BMALE_05 | Chinese (Mandarin)_Sincere_Adult | 真诚青年 | v1_identity_stable / v2_emotional_rich |

## 声音身份锁

```text
b_voice_identity_lock:
  status: pending_user_review
  expected_b_minimax_voice_id: null
  required_gender_direction: male_or_male_leaning
  forbidden_voice_ids:
    - female-tianmei
    - female-shaonv
    - female-shaonv-jingpin
    - female-yujie
  human_voice_review_required: true
  human_voice_review_status: pending_user_review
  timbre_change_allowed: false
  emotion_optimization_allowed: true
  prosody_optimization_allowed: true
```

## 状态边界

- 未生成全片旁白。
- 未修改完整视频。
- 未改锁稿文案。
- 未推进 `voice_validation = passed`。
- 未推进 `final_voice_validated = true`。
- 未推进 `send_ready = true`。

## 验证

- `py_compile`: passed
- `tests.test_publish_candidate_voice_gate`: passed
- `tests.test_minimax_b_voice_identity_lock`: passed
- `tests.test_publish_candidate_preflight_tolerance`: passed
- `publish_candidate_preflight_suite --no-render`: `fixture_validation.status = passed`，`case_count = 24`；无输入 no-render 按预期 `overall_status = blocked`。

## DeepSeek

- `supply_request = codex_log/supply_requests/20260527_B声音身份重审_DeepSeek执行前供料_b_voice_identity_reaudit_pre_supply_request.json`
- `supply_pack = codex_log/deepseek_supply/20260527_B声音身份重审_b_voice_identity_reaudit_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = not_attempted_policy_violation`
- `blocked_reason = invalid_context_pack`
- `not_deepseek_conclusion = true`

## Git

- 使用 path-limited stage。
- 不使用 `git add .`。
- 大媒体未触碰。
- 不提交 API key / token / secret。
