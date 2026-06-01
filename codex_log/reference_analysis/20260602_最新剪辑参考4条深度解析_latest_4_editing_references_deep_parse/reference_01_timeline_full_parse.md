# reference_01 Timeline Full Parse

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
- `frame_sampling`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_01/frames_5s/`
- `contact_sheets`: `dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/reference_01/contact_sheet_5s_page_*.jpg`
- `ocr_note`: 本机 OCR 不可用；能读出的少量大字为人工视觉观察，小字统一低置信度。

| timecode | duration | visual_layout | screen_content | split_screen_state | keyword_state | subtitle_state | icon_or_sticker_state | editing_action | camera_or_motion | transition_type | rhythm_density | information_density | viewer_attention_target | function_in_story | possible_migration_rule | not_allowed_to_copy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:20 | 20s | host medium shot on purple/black studio, platform UI around it | opening hook, title/brand/AI-video examples appear quickly | mixed: host full, then collage/comparison panels | large title words and logo visible; exact small text low confidence | bottom subtitle present in native video; platform caption separate | round creator/avatar and platform buttons visible | hard cuts, logo/title card, example montage | host hand gestures, clip changes every few seconds | hard_cut + title_pop | high | medium_high | host face then big product/title words | hook and introduce AI video tool difference | use host/guide bridge then immediately show evidence examples | creator face, platform UI, exact logo/sticker |
| 00:20-01:00 | 40s | black stage with phone/PIP/product pages and cinematic examples | reference/generated comparison, white product pages, movie-like clips | picture-in-picture and side-by-side appear repeatedly | Seedance 2.0 and product logo readable; other text low confidence | short subtitles in lower part | PIP face badge, product icon, thumbs/heart platform chrome | insert screen, crop focus, title card, montage | fast visual switching | hard_cut + semantic bridge | high | high | reference/generated labels and product card | show what the tool can generate | use black matte + white evidence card + short label | exact app/logo/platform chrome |
| 01:00-01:40 | 40s | host alternates with product logo and numbered bullet list | Seedance 2.0 identity, 3 points, prompt webpage | light split/PIP between host and product page | numbered list labels visible, exact small text low confidence | host subtitle and screen labels | round PIP and product logo | keyword_pop, overlay_card, crop_focus | host gestures, webpage static | hard_cut | medium_high | medium | numbered list and product logo | organize tool claims into digestible bullets | use numbered mini-card only after tool has been introduced | copying product logo as own brand |
| 01:40-02:20 | 40s | white webpage/prompt page, then reference/generated video comparison cards | prompt/result examples, motion samples, cat and dance clips | left/right and reference/generated panels frequent | reference/generated labels are readable; detail text not | subtitles continue under sample | yellow label, PIP face badge | split_screen, picture_in_picture, comparison board | sample clips motion; panels mostly static | hard_cut with repeated panel container | high | high | comparison result panel | prove specific capability via before/after or reference/result | split only when two states must be compared | decorative split with unreadable panels |
| 02:20-03:20 | 60s | chapter cards, cinematic examples, host bridge, generated action clips | sections about editing/all-things and AI movie examples | collage and PIP; not every shot split | large section/chapter labels readable in parts | subtitles in lower third | chapter pill, PIP, platform UI | chapter_card, montage, cinematic insert, host reset | fast action clips, host pauses | hard_cut + recurring labels | high | medium_high | chapter label then example clip | shift to next capability while preserving context | insert bridge card after dense examples | copying film clips / creator media |
| 03:20-04:20 | 60s | host reset, big title card, action examples, document/prompt page | third chapter and prompt/document proof | mostly single evidence panel with PIP | large title cards; document text too small | subtitle under video | PIP face badge | bridge_card, crop_focus, evidence_window | moderate | hard_cut | medium | high | title/chapter or document active area | move from spectacle to method/proof | use active evidence window before showing dense doc | letting full doc page appear without highlight |
| 04:20-05:20 | 60s | action/game/movie generated clips and prompt pages | cinematic evidence cluster; reference closes loops | some PIP and chapter labels | chapter labels readable, small text low confidence | subtitles continue | PIP and platform chrome | montage, hard_cut, evidence_card | fast generated motion | hard_cut | high | medium | large clip frame | maintain visual energy after proof blocks | alternate generated clips with low-density host/label reset | copying copyrighted images / platform UI |
| 05:20-05:46 | 26s | host close, tool logo/title on black | closing recommendation and brand outro | mostly host/single card | logo/title visible | subtitle present | PIP/platform UI | host_close, logo_card | host gestures | hard_cut | medium | low_medium | host and final title | close with identity and CTA | end with clean title/brand card but use original project brand | copying Seedance logo/title as own asset |

## low_confidence_items
- exact spoken narration and small UI text require OCR / transcript / human review.
- platform UI numbers and creator captions are not migration targets.
