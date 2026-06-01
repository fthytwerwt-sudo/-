# 参考角色分类 Reference Role Classification

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

| reference_id | main_role | secondary_roles | confidence | reason | strongest_reference_points | weak_or_not_relevant_points | should_migrate_to_new_fourth_episode | should_not_migrate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `main_style_reference` | `split_screen_reference, rhythm_transition_reference, screen_packaging_reference` | `medium_high` | 整片最完整展示 host bridge + AI video examples + reference/generated comparison + chapter cards；适合作为综合剪辑语言参考。 | Seedance 2.0、参考/成片对比、章节 1/2/3、PIP host、电影感示例 | 平台 UI、真人身份、具体片段和 logo 不可复制 | `conditional_migrate` | `copy creator identity / platform shell / exact assets` |
| `reference_02` | `keyword_subtitle_reference` | `icon_motif_reference, screen_packaging_reference, rhythm_transition_reference` | `medium` | 手机 PIP、绿色关键词/check list、短标签和 AI 视频结果展示最突出；适合做关键词与手机录屏包装参考。 | 绿色关键词块、check marks、手机框、账号/工具流程、横向多案例 | 分屏体系较弱，更多是 phone-in-phone 与示例轮播 | `conditional_migrate` | `do not make every keyword a sticker; do not copy UI chrome` |
| `reference_03` | `screen_packaging_reference` | `keyword_subtitle_reference, split_screen_reference, workflow_explanation_reference` | `high` | Agent Skills 教学结构最清楚，包含概念类比、步骤框、文档证据、工作流屏幕、移动技能商店，适合作为知识类流程讲解主参考。 | 炒菜类比、技能盒子、步骤 1/2/3、黄绿高亮、文档/网页证据窗口 | 文本很密，需注意横屏化后证据可读性 | `directly_for_mechanism_draft_conditionally_for_video` | `do not copy chef character / exact Coze UI as own asset` |
| `reference_04` | `evidence_window_reference` | `subtitle_highlight_reference, phone_screen_packaging_reference, rhythm_transition_reference` | `high` | 长期记忆主题用手机聊天/文本证据 + 黄色高亮 + host bridge 解释抽象能力，最适合作为证据窗口和高亮阅读参考。 | 手机聊天页、长文本黄高亮、AI 记忆库步骤、实用方法卡、城市/情绪 B-roll | 依赖竖屏平台 UI 和真人出镜；直接照搬会变成平台截图复刻 | `conditional_migrate` | `do not copy creator face, comment UI, platform shell, exact memory UI` |

## classification_boundary

- `user_confirmation_required = true`
- `classification_is_draft = true`
- `reference role != formal project mechanism`，本轮只给 ChatGPT / 用户复审。
