# reference_03 Timeline Full Parse

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

analysis_basis:
- `frame_sampling`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_03/frames_5s/`
- `contact_sheets`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_03/contact_sheet_5s_page_*.jpg`
- `ocr_note`: 本机 OCR 不可用；能读出的少量大字为人工视觉观察，小字统一低置信度。

| timecode | duration | visual_layout | screen_content | split_screen_state | keyword_state | subtitle_state | icon_or_sticker_state | editing_action | camera_or_motion | transition_type | rhythm_density | information_density | viewer_attention_target | function_in_story | possible_migration_rule | not_allowed_to_copy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:25 | 25s | host + large Agent Skills title and PPT-like black stage | concept hook: what Agent Skills are | host and title card, no heavy split | Agent Skills readable, yellow highlight | lower subtitles | round avatar/platform controls | title_pop, host_bridge, keyword_highlight | host gestures | hard_cut | medium_high | medium | big highlighted term | define abstract concept fast | start with one large term and simple host explanation | copying external article/site title as own |
| 00:25-01:15 | 50s | black stage with boxes, chef/cooking analogy, AI circle | maps skills to cooking steps: cook/prepare/plate | box grid and simple diagrams | large Chinese labels visible; exact small labels partly readable | subtitles under cards | cartoon chef, AI circle icon, small emoji-like marks | diagram_build, icon_pop, keyword_pop | elements appear progressively | hard_cut + build | medium | medium_high | one box/step at a time | teach concept by analogy | use simple analogy diagram before dense screen evidence | copying chef character / decorative cartoons |
| 01:15-02:00 | 45s | host bridges with chef/food examples | transition from analogy to practical uses | mostly host + example inserts | green/yellow phrases visible | subtitles present | chef icon and food cards | bridge_card, insert_card, keyword_pop | moderate | hard_cut | medium | medium | example card | make abstract workflow relatable | use examples only after definition is clear | making cute icon the main evidence |
| 02:00-02:45 | 45s | skill/task list cards and host explanations | segments: lesson prep / after-class / interactions | list card with yellow highlighted terms | large list labels readable | subtitles present | PIP/avatar | overlay_card, list_card, crop_focus | low motion, text appears/cuts | hard_cut | medium | high | yellow highlighted list item | organize use cases into categories | limit list to 3-5 items and highlight current item | too many bullet cards without active item |
| 02:45-03:45 | 60s | white document/webpage screens with side labels and yellow/purple highlights | evidence: docs, browser pages, workflow screens | single evidence window with small PIP, occasional side label | highlight labels readable partly; doc text too small at contact-sheet scale | subtitle under evidence | PIP, left labels, yellow highlights | evidence_window, crop_focus, highlight_box, scroll_screen | screen scrolling/static docs | hard_cut | medium | very_high | highlighted active line | prove workflow with real pages | define active evidence window before showing full page | full-page doc with no highlight |
| 03:45-04:45 | 60s | more pages/forms, side rail labels, summary card | work summaries and lesson material examples | single evidence window, side rail labels | yellow highlighted terms visible | subtitle under evidence | PIP and labels | crop_focus, side_label, summary_card | screen changes and occasional scroll | hard_cut | medium | high | active form field / label | show concrete setup and outputs | use side label as orientation, not decoration | side labels covering content |
| 04:45-05:45 | 60s | mobile skill store screens + host + daily workflow card | skills can upgrade; social media daily 8:00 collection; AI chat | phone PIP and host bridge | large yellow terms readable | subtitles present | colored social icons, phone frame | phone_pip, keyword_card, host_bridge | moderate | hard_cut | medium | medium | yellow claim / phone screen | move from tool concept to daily routine | use phone view if real mobile operation is required | using phone UI for desktop-only workflows |
| 05:45-06:04 | 19s | host close with bullet/keyword strip | closing: stable output / reusable process / repeated tasks | host full with side bullet sticker | side bullets visible partly | subtitles | small bullet card | host_close, keyword_badge | host gestures | hard_cut | medium | low_medium | host and 2-3 bullets | wrap the mechanism | end with concise retention rule | stuffing final screen with all previous labels |

## low_confidence_items
- exact spoken narration and small UI text require OCR / transcript / human review.
- platform UI numbers and creator captions are not migration targets.
