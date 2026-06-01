# 参考到执行契约 Reference To Execution Contract

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

## reference_anchor

| field | value |
| --- | --- |
| `reference_id` | `latest_4_editing_references_20260602` |
| `reference_type` | `editing_reference + screen_packaging_reference + keyword_subtitle_reference + split_screen_reference + rhythm_transition_reference` |
| `source_layer` | `user_provided_local_reference_videos` |
| `exact_reference_available` | `true` |
| `reference_path_or_description` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考` |
| `must_preserve` | attention guidance, evidence window clarity, host/guide bridge function, split-screen only when comparison is needed, keyword as signal not decoration |
| `can_vary` | people, platform shell, exact stickers, exact fonts, exact UI, color skin, topic material |
| `must_not_copy` | creator face/identity, platform UI chrome, third-party app wrappers, exact stickers/templates/logos/fonts, copyrighted shot sequences |
| `fail_if_missing` | no timeline parse, no split-screen map, no keyword/subtitle/icon map, no quantitative draft |
| `blocked_if_reference_missing` | true |

## effect_targets

- `viewer_feeling`: 看起来是被带着理解的证据视频，而不是随手拼屏录屏。
- `information_hierarchy`: 主信息由 host / title / section label 定向，证据窗口承载证明，字幕和关键词只做注意力引导。
- `pacing`: dense proof block 前后必须有低密度桥接；不能连续堆满屏文档。
- `visual_weight`: 真实证据与屏幕内容永远高于装饰；PIP / 小图标不能抢证据区。
- `evidence_clarity`: 每个证据窗口必须有 active evidence window，不让观众自己扫整页。
- `human_like_comfort`: host / avatar / voice / subtitles 提供节奏和陪伴，但不能复制真人出镜身份。
- `reference_quality_points`: 统一黑底舞台、白色证据容器、黄/绿关键词、圆形 PIP、短字幕、安全边距、章节标签。
- `not_allowed_effects`: PPT 感、demo 感、花活感、贴纸遮证据、只照搬平台 UI、技术预览冒充完成。

## function_fields

| field | value |
| --- | --- |
| `input_signal` | 4 个最新参考视频 |
| `evidence_role` | quality and editing mechanism reference |
| `importance_type` | optional / conditional mechanism inheritance, not direct copying |
| `target_area` | editing, screen packaging, subtitle, keyword, icon, split-screen, rhythm |
| `selected_action` | produce draft maps and standards only |
| `action_reason` | before new fourth episode editing, define what can be migrated and what must be blocked |
| `validation_rule` | each mechanism has trigger, forbidden_if, observed range and failure line |
| `blocked_if` | OCR unavailable but exact words invented; reference copied as template; formal status promoted |
| `fallback_action` | mark low confidence / needs human review, do not guess |
| `feedback_update` | analysis_manifest only; no formal mechanism file update this round |

## deviation_check

- `differs_from_reference_where`: 本轮没有执行新视频，所以只能定义 future deviation checks；不能判断新第四期是否已符合。
- `acceptable_variation`: 换成《视频工厂》自己的证据素材、卡片皮肤、非真人桥接、原创图标和横屏 16:9 承载。
- `unacceptable_deviation`: 只有大标题页、没有证据窗口；分屏只是装饰；字幕抢证据；图标只是贴纸；连续 dense 文档没有桥接。
- `repair_required`: 后续验证片若出现上述偏离，先回到 active evidence window / subtitle safe zone / split-screen trigger / bridge cadence，而不是简单加更多元素。
- `cannot_compare_reason`: 本轮未生成新片；无 OCR 自动文本；无法自动判断所有小字原文。
- `human_review_required`: true

## done_when

- reference_anchor_locked: true
- effect_targets_filled: true
- function_fields_filled: true
- deviation_check_done_for_analysis_phase: true
- user_goal_preserved: true
- no_forbidden_status_promotion: true
- remaining_deviation_list_empty_or_explained: true
