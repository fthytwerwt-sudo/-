# 关键词 / 字幕 / 小图标系统地图 Keyword Subtitle Icon Map

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

## A. keyword system（关键词系统）

| reference_id | timecode | observed_keyword_or_label | keyword_type | position | size_level | color_or_style | motion | duration | sync_with_voice | function | migrate_condition | failure_line |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `00:00-01:40` | `Seedance 2.0`, chapter / numbered labels | `action_word / number / product_label` | center or side card | large | white/yellow on black, product logo | pop / cut-in | `2-6s` | yes | anchor product and chapter | replace with project-owned term or task step | product/logo copied as own asset |
| `reference_01` | `01:45-03:20` | `参考 / 成片 / 编辑万物` visible in parts | `contrast_word / conclusion_word` | top/side of panels | medium-large | white/yellow tags | cut-in | `3-10s` | yes | mark comparison role | only when panels compare real states | label says comparison but panels do not compare |
| `reference_02` | `00:10-01:15` | green tags / check items, e.g. 出镜, 情节/分镜/剪辑-like terms | `action_word / result_word` | right of host or beside phone | medium-large | neon green with black/white outline | pop / highlight | `2-5s` | yes | turn feature into remembered words | max 1-3 tags per beat | every sentence becomes a sticker |
| `reference_03` | `00:00-01:15` | `Agent Skills`, `炒菜`, boxes / steps | `concept_word / metaphor_word` | center title or box | large | yellow highlight, white dashed boxes | build / pop | `3-8s` | yes | explain abstract concept | one core term per concept | term not tied to example |
| `reference_03` | `02:00-05:30` | yellow highlighted document/list labels | `step_marker / conclusion_word` | side rail or over evidence | medium | yellow/green highlight | highlight | `5-20s` | yes | tell viewer where to look on dense page | only if active evidence window exists | highlight floats over unreadable page |
| `reference_04` | `00:25-04:20` | `AI长期记忆`, `AI对你的回忆库`, yellow text highlights | `pain_word / evidence_word / conclusion_word` | title card or inside phone text | large for title, small/medium for evidence | white/yellow, black stage | pop / highlight | `5-30s` | yes | convert long text into one claim | crop and highlight one active passage | too many yellow blocks without hierarchy |

## B. subtitle system（字幕系统）

| reference_id | observed_pattern | subtitle_position | line_count | word_density | subtitle_role | break_rule | keyword_highlight_inside_subtitle | motion | readability_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | host/video has lower short subtitles; platform captions below are outside source video | lower third inside content area | 1 line mostly | medium | transcription + attention_guide | follows speech beat/cut | sometimes separate keyword card | cut/replace | medium; platform UI reduces clean-room readability |
| `reference_02` | short lower subtitles while phone/keyword tags handle emphasis | lower third | 1 line | low-medium | transcription + rhythm card | short phrases | green tags separate from subtitle | cut/replace | high inside source, but phone text needs crop |
| `reference_03` | subtitles stay under host/evidence; big terms live in cards | lower third | 1 line | medium | explanation + transition_bridge | one idea per cut | yellow/green labels separate | cut/replace | high for subtitles, document text lower |
| `reference_04` | subtitle continues under dense phone evidence; yellow highlights guide reading | lower third, separate from phone text | 1 line | medium | transcription + attention_guide | host explanation beat | evidence highlight inside phone, not subtitle | cut/replace | subtitle readable; phone text requires zoom/crop |

判断：这些字幕不是纯转写。它们承担 `attention_guide + rhythm_bridge + explanation`，但不负责承载全部信息；关键词和证据高亮另成一层。

## C. icon / sticker / motif system（小图标 / 贴纸 / 视觉符号系统）

| reference_id | timecode | icon_or_sticker_description | position | size | motion | visual_role | duration | supports_information | can_migrate | do_not_copy_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | throughout | round host/avatar PIP, product logo, chapter pills | edge / corner / card center | small-medium | mostly static / pop | attention_marker + continuity_marker | recurring | yes when it tells source/section | conditionally | creator avatar, product logo, platform buttons are third-party/context-bound |
| `reference_02` | `00:00-01:20` | green checkmarks and phone frame | beside phone/host | medium | pop | step_marker + result_marker | short | yes | yes as original project checkmark style | exact sticker/phone UI should not be copied |
| `reference_03` | `00:25-01:20` | chef cartoon, AI circle, boxes, small emoji-like marks | center stage | medium-large | build/pop | metaphor_marker + step_marker | medium | yes when teaching analogy | conditionally | cartoon assets and exact icons may be third-party |
| `reference_03` | `02:45-05:30` | side rail labels and colored highlights | left/top/side | small-medium | static/highlight | orientation_marker | long | yes | yes | must redesign for horizontal evidence windows |
| `reference_04` | `00:30-04:20` | phone frame, PIP face, yellow highlight bars, occasional emoji/test card | side/evidence area | small-medium | highlight/pop | evidence_marker + emotion_marker | medium-long | yes when marking active passage | conditionally | exact creator/PIP/platform UI and emoji cards not reusable |

## density_rule_draft

- `keyword_max`: 1 large keyword or 2 small tags per 5s beat.
- `subtitle_max`: 1-2 lines; do not stack with a title card at the same vertical safe zone.
- `icon_max`: 1 functional icon motif per 10s unless it is a persistent PIP/avatar.
- `failure_line`: if the viewer cannot tell whether to read subtitle, keyword, icon, or evidence first, the screen fails.
