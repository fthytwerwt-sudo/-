# 剪辑动作分类表 Editing Action Taxonomy

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

| action_type | used_in_references | typical_timecode_examples | trigger_condition | visual_parameters | duration_range | frequency_observed | viewer_function | migrate_to_new_fourth_episode | forbidden_if | quality_failure_line |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hard_cut` | all | all timelines | every new claim/example | cut on speech beat or visual role change | instant | very_high | keeps pace | yes | cut changes topic without orientation | viewer feels dropped into random screen |
| `jump_cut` | host sections in all | ref01 00:00-00:20, ref03 05:40-06:04 | host sentence compression | same framing, new gesture | instant | high | remove dead air | yes | jump hides missing explanation | host feels fragmented |
| `zoom_in / crop_focus` | ref03, ref04, ref01 docs | ref03 02:45-04:20, ref04 01:10-03:35 | dense doc/chat needs active evidence | crop to paragraph/phone region | 5-20s | high | makes evidence readable | required for document proof | whole page remains tiny | viewer must scan whole page |
| `highlight_box` | ref03, ref04 | ref03 02:45-04:45, ref04 01:10-03:35 | one line/field proves claim | yellow/green/purple block or outline | 3-20s | high | directs eyes | yes | multiple unrelated highlights | no active evidence window |
| `overlay_card` | all | ref03 00:25-01:15, ref04 00:30-01:10 | abstract concept or section transition | black stage + white/yellow text | 2-8s | high | reset context | yes | replaces real evidence | becomes PPT-only |
| `bridge_card` | ref01/ref03/ref04 | ref01 chapter cards, ref04 practical method | after dense block or new section | low-density title / section card | 2-5s | medium | breathing point | yes | too frequent or decorative | rhythm stalls |
| `split_screen` | ref01/ref03 | ref01 01:45-02:20, ref03 boxes/docs | compare source/output or options | 2 panels or labeled boxes | 3-15s | medium | compare without long speech | conditional | no comparison claim | decorative collage |
| `picture_in_picture` | all | host/avatar or phone frame throughout | keep human/guide continuity during evidence | small circle/phone/side host | persistent or 5-30s | high | maintain human presence | yes, with original guide/PIP | covers evidence | guide steals attention |
| `icon_pop` | ref02/ref03/ref04 | green checks, chef/AI icons | step/result/emotion marker | small original icon | 1-4s | medium | mark category or emotion | conditional | decoration only | sticker slop |
| `keyword_pop` | all | Seedance/Agent Skills/AI memory | introduce term or conclusion | large high-contrast text | 2-6s | high | memory hook | yes | unverified claim or too many tags | keyword competes with evidence |
| `transition_flash / color_bar_reset` | ref02/ref04 | ref02 01:45, ref04 04:15 | comedic/reset beat | test-card or flash-like full-screen reset | 1-3s | low | break density | rare/optional | used as default transition | gimmick over clarity |
| `pan_or_slide / scroll_screen` | ref03/ref04 | docs and phone pages | page content exceeds frame | slow scroll/crop shift | 5-20s | medium | reveal sequence | yes | scroll too fast for reading | evidence unreadable |
| `freeze_frame` | implicit in highlighted docs | ref04 long phone text | viewer must read one passage | static frame with highlight | 5-15s | medium | give reading time | yes | no highlight or too long | dead screen |
| `dim_background` | ref03/ref04 | title cards over dim screens | isolate overlay text | dark matte / blurred backing | 2-8s | medium | hierarchy | yes | hides evidence needed now | fake clarity |
