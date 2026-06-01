# reference_02 Timeline Full Parse

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
- `frame_sampling`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_02/frames_5s/`
- `contact_sheets`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_02/contact_sheet_5s_page_*.jpg`
- `ocr_note`: 本机 OCR 不可用；能读出的少量大字为人工视觉观察，小字统一低置信度。

| timecode | duration | visual_layout | screen_content | split_screen_state | keyword_state | subtitle_state | icon_or_sticker_state | editing_action | camera_or_motion | transition_type | rhythm_density | information_density | viewer_attention_target | function_in_story | possible_migration_rule | not_allowed_to_copy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:25 | 25s | host plus phone PIP and neon-green keyword tags | opens with Seedance 2.0 and phone-based workflow | phone-in-phone PIP; not classic split | green keyword labels such as 出镜 and short claims visible | short lower subtitle | round creator icon, phone frame, green stickers | phone_pip, keyword_pop, hard_cut | host gestures, phone screen changes | hard_cut | high | medium | green keyword tag and phone screen | hook by tool value and mobile operation | use green check/keyword only for key action/result words | copying phone app UI / exact sticker style |
| 00:25-00:55 | 30s | host beside mobile app account screens and keyboard | account/profile/search/input flow | PIP phone dominates; host small/side | small UI text not reliably readable | subtitles visible | phone frame, arrow/check elements | screen_record_insert, crop_focus | static phone pages | hard_cut | medium | high | phone UI active field | show operation path step by step | use phone frame for mobile workflow evidence | forcing mobile frame when source is desktop |
| 00:55-01:20 | 25s | generated person/scene examples and green checklist | prompt/result examples and capability list | single vertical examples, occasional host | green checklist readable as category markers; exact all words low confidence | subtitles present | green check icons | example_montage, checklist_pop | generated clips motion | hard_cut | high | medium | checklist items | turn scattered examples into 2-3 capability claims | use checklist as result summary, max 3 items | overloading every sentence with checkmarks |
| 01:20-02:00 | 40s | full-frame generated clips, test bars, host reset | show output diversity and transition reset | mostly single clips, no dense split | few big labels, low text density | subtitles continue | platform UI and avatar | montage, color_bar_reset, host_bridge | fast clips, then host pause | hard_cut + reset card | medium_high | medium | clip itself then host | show quality range and reset attention | use one visual reset between clusters only if it clarifies | copying test-card gag as default template |
| 02:00-02:45 | 45s | multi-clip dark panels and host explanations | various style examples then product/brand return | multi-panel comparison appears briefly | some large labels visible, exact details low confidence | subtitles under host/clip | round icon and platform controls | multi_panel, host_bridge, title_card | moderate | hard_cut | medium | medium | example cluster | show breadth without tutorial detail | use multi-panel only for quick option scan | unreadable 3+ video panels in horizontal delivery |
| 02:45-03:20 | 35s | brand/title + host close | close and reinforce product categories | single host/title | Seedance 2.0 and category words visible | subtitle present | product logo/avatar | logo_card, host_close | host gestures | hard_cut | medium | low | brand/title | wrap summary | end with own project CTA/card if reused | copying product branding |

## low_confidence_items
- exact spoken narration and small UI text require OCR / transcript / human review.
- platform UI numbers and creator captions are not migration targets.
