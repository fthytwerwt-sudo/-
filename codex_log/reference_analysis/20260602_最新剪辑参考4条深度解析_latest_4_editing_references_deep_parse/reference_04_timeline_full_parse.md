# reference_04 Timeline Full Parse

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
- `frame_sampling`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_04/frames_5s/`
- `contact_sheets`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_04/contact_sheet_5s_page_*.jpg`
- `ocr_note`: 本机 OCR 不可用；能读出的少量大字为人工视觉观察，小字统一低置信度。

| timecode | duration | visual_layout | screen_content | split_screen_state | keyword_state | subtitle_state | icon_or_sticker_state | editing_action | camera_or_motion | transition_type | rhythm_density | information_density | viewer_attention_target | function_in_story | possible_migration_rule | not_allowed_to_copy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:30 | 30s | host hook + phone/document inserts + big title card | AI long memory theme and question | host/phone PIP; title full screen | AI长期记忆 visible; exact doc small text low confidence | subtitles under host | phone frame, avatar, platform icons | title_card, phone_pip, host_bridge | host gestures | hard_cut | medium_high | medium | title/question | frame pain point and topic | use one big question card before evidence | copying creator identity |
| 00:30-01:10 | 40s | settings/chat screens, AI memory library card and step list | shows where memory lives and steps | phone insert and list card | AI对你的回忆库 and step labels visible | subtitles | small emoji/blue speech bubble | phone_pip, list_card, highlight_box | static phone screens | hard_cut | medium | high | phone setting / step list | establish operational evidence | use phone/doc as proof only with active highlight | tiny unreadable phone text in horizontal output |
| 01:10-01:50 | 40s | host bridge into phone document/chat evidence | personal role discovery, highlighted text blocks | left host/PIP + phone evidence | yellow highlights on long text visible | subtitles and platform caption | PIP avatar and highlight blocks | crop_focus, highlight_box, evidence_window | slow reading pace | hard_cut | medium | very_high | yellow highlighted line | convert dense chat text into readable claim | highlight one active passage per beat | showing full long text without zoom |
| 01:50-02:35 | 45s | host + red/black background + phone evidence with many yellow highlights | controversial/self-view evidence and role analysis | phone evidence, host resets | multiple yellow highlighted passages | subtitles | PIP, occasional image insert | highlight_box, host_bridge, evidence_window | mostly static screens | hard_cut | medium | very_high | current highlighted paragraph | prove subtle point through remembered text | cap highlights per screen and crop to paragraph | highlighting 5+ lines with no hierarchy |
| 02:35-03:35 | 60s | phone/text evidence continues, host and small image inserts | role / memory / self-understanding sequences | phone evidence + host; little true split | yellow highlights recurring | subtitles | PIP, small stickers/images | scroll_screen, crop_focus, highlight_box | moderate slow | hard_cut | medium | high | phone active line or host face | sustain evidence-heavy explanation | alternate 2-3 evidence screens with host reset | continuous dense phone text without rest |
| 03:35-04:20 | 45s | host + overlaid phone frames + test card reset | practical method and saved memory examples | phone overlay beside host | some large labels / UI text; exact small text low confidence | subtitles | phone frame, test card emoji | phone_pip, title_card, reset_card | moderate | hard_cut | medium | medium | practical-method card | transition from diagnosis to method | use reset card before practical method section | turning reset cards into random jokes |
| 04:20-04:54 | 34s | practical-method card, city B-roll, poetic end card and host close | closing: method and emotional wrap | single card/B-roll/host | 实用方法, 灵光一现, 梦想和天赋 visible | subtitles | platform icons only | bridge_card, b_roll, host_close, title_end | slower end pacing | hard_cut | low_medium | low_medium | big phrase card | emotional closure | use short low-density close after dense evidence | letting B-roll replace proof earlier in the video |

## low_confidence_items
- exact spoken narration and small UI text require OCR / transcript / human review.
- platform UI numbers and creator captions are not migration targets.
