# 量化质量判断标准草案 Quantitative Quality Standards Draft

status_boundary:
- `task_result.status = reference_analysis_completed_pending_user_review`
- `mechanism_status = draft_pending_chatgpt_user_review`
- `content_validation = not_applicable（本轮不做内容验证）`
- `send_ready = false（不可发送）`
- `video_rendered = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`
- `code_or_function_landed = false`
- `ocr_status = unavailable_local_tesseract_not_found`
- `deepseek_actual_participation = not_attempted_policy_violation / blocked_invalid_context_pack`

`status = draft_pending_chatgpt_user_review`

## standards

```yaml
split_screen:
  layout_ratio_range: "50:50 to 70:30; phone/PIP may be 65:35"
  min_duration: "3s"
  max_duration: "15s normal; 30s only for readable phone/text evidence with progressive highlight"
  max_frequency_per_30s: "3 comparison boards"
  observed_range: "reference_01 high; reference_03 medium; reference_02/04 low-medium phone PIP"
  confidence: medium
  fail_if:
    - no comparison claim
    - any panel unreadable
    - panel role unlabeled

keyword:
  max_keywords_per_5s: 2
  duration_range: "2-6s for hook/result; 5-20s for side label"
  position_rules: "outside active evidence window; side/top safe area preferred"
  motion_rules: "pop / cut-in / highlight only; no constant shaking"
  observed_range: "1 major keyword + 0-2 small tags per beat"
  confidence: medium_high
  fail_if:
    - keyword not in voice/evidence
    - more than one main attention target

subtitle:
  max_lines: 2
  max_chars_per_line: "12-18 Chinese chars preferred; longer only in low-density host shot"
  display_duration_range: "1.5-4s normal; follows speech beat"
  readability_rule: "must not overlap prompt/table/chat/button/key highlight"
  confidence: medium
  fail_if:
    - high severity overlap
    - subtitle rewrites locked copy
    - subtitle competes with title card

icon_or_sticker:
  max_icons_per_10s: "1 functional motif, persistent PIP excluded"
  allowed_roles:
    - attention_marker
    - emotion_marker
    - step_marker
    - warning_marker
    - result_marker
  forbidden_roles:
    - decoration_only
    - third_party_asset_copy
    - platform_template_copy
  confidence: medium
  fail_if:
    - icon has no information role
    - icon covers evidence

bridge_card:
  duration_range: "2-5s"
  max_text_density: "1 title + 1 subtitle or 3 bullets max"
  allowed_position: "between dense evidence clusters or at section boundary"
  fail_if:
    - bridge interrupts proof before claim is proven
    - bridge card becomes main content instead of evidence

evidence_window:
  min_readability: "active evidence line/field readable at target output size"
  allowed_occlusion: "none over active evidence; PIP must stay outside active window"
  highlight_rule: "one main highlight cluster per claim"
  fail_if:
    - whole page shown tiny
    - multiple unrelated highlights
    - active evidence cannot be named

rhythm:
  visual_change_frequency_per_10s:
    hook_or_example_cluster: "2-4"
    evidence_cluster: "1-2"
  average_shot_length_range:
    host_or_hook: "3-8s"
    evidence: "8-20s"
  breathing_point_rule: "after 2-3 dense screens or 15-30s dense evidence, insert host/guide/bridge reset"
  fail_if:
    - dense proof runs without reset
    - evidence is flashed too fast
    - transitions have no semantic role

reference_similarity_check:
  must_compare:
    - split_screen_timing
    - keyword_motion
    - subtitle_guidance
    - icon_density
    - evidence_window
    - rhythm_transition
    - bridge_card_density
  fail_if:
    - looks similar in color but does not guide attention
    - uses more decoration but less evidence clarity
    - copies source assets instead of mechanism
```
