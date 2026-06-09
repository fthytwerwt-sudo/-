# 20260609｜卡片最小真实链路用户通过与默认路线确认

## 1. 本轮状态

- `task_result.status = card_minimal_chain_user_approved_default_route_recorded`
- `project_route = video_factory`
- `task_type = mechanism_or_route_fix + project_file_change + user_review_result_sync`
- `artifact_scope = local_quarantine_minimal_chain_test`
- `source_artifact_dir = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/`
- `no_new_image_generation = true`
- `no_new_video_generation = true`
- `no_existing_card_replacement = true`

## 2. 用户人工反馈

- `user_feedback = 这轮我看了，我觉得是可以通过的，以后都这样。`
- `user_aesthetic_review = passed`
- `user_default_route_confirmation = true`
- `approved_default_card_route = image2_visual_base_route_candidate -> codex_post_overlay_locked_copy -> optional HyperFrames_motion_wrapper`

## 3. 本地最小链路产物事实

- `chain_report = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/card_chain_report.md`
- `chain_summary = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/card_chain_summary.json`
- `image2_raw = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/01_image2_visual_base_raw.png`
- `overlay_final_png = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/02_locked_copy_overlay_final.png`
- `motion_wrapper_mp4 = 本地隔离区_local_quarantine/20260609_card_minimal_real_chain_test/03_hyperframes_motion_wrapper_optional.mp4`
- `locked_copy_diff_result = passed`
- `readability_result = passed`
- `social_editorial_card_v1_result = passed_minimal_sample`
- `image2_overreach_check = passed`
- `third_party_asset_check = passed_by_manual_visual_review`
- `evidence_window_safety = passed_for_standalone_card`
- `motion_wrapper_safety = passed`

## 4. 后续默认卡片执行路线

```text
default_card_execution_route_after_user_approval:
  visual_base_route: image2_visual_base_route_candidate
  text_authority_route: codex_post_overlay_locked_copy
  exact_text_fallback: HTML/CSS/PIL_exact_text_layer
  motion_wrapper_route: none_by_default
  optional_motion_wrapper_route: HyperFrames_motion_wrapper
  runtime_gate_required_when: motion_wrapper_route = HyperFrames_motion_wrapper
  required_checks:
    - locked_copy_diff_check
    - readability_check
    - social_editorial_card_v1_check
    - evidence_window_protection
    - subtitle_card_overlap_check
    - card_visual_quality_gate
    - publish_candidate_preflight_when_entering_real_video_chain
```

## 5. 状态边界

- `image2_long_term_stable_passed = false`
- `content_validation = not_advanced`
- `send_ready = false`
- `visual_master_locked = false`
- `publish_candidate = not_advanced`
- `current_data_goal_anchor_ready = not_advanced`

## 6. 不变规则

- image2 只负责主视觉、底图、构图、质感和社交编辑感，不负责最终中文文字准确性。
- 最终 locked copy 文字必须由 Codex 后期叠字或 `HTML/CSS/PIL_exact_text_layer` 承担。
- HyperFrames 只作为可选轻动效包装层；未选择动效时不得强制 runtime gate。
- HyperFrames 不可用时，只阻断该动效包装路线，不直接阻断已满足文字、审美和证据安全的静态 image2 卡片路线。
- 卡片仍必须遵守 `social_editorial_card_v1`、`card_budget_gate`、`cluster_merge_rule`、`card_placement_decision` 和 `evidence_window_protection`。
- 卡片好看、用户通过最小链路样张，不等于 `content_validation` 通过，不等于 `send_ready`，不等于 `visual_master_locked`，不等于 image2 长期批量稳定通过。
