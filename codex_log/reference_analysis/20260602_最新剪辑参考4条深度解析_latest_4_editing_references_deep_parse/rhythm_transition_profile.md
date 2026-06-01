# 节奏与转场画像 Rhythm Transition Profile

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

## observed_profile_by_reference

| reference_id | average_shot_length_estimate | fast_sections | slow_sections | breathing_points | visual_change_frequency_per_10s | keyword_frequency_per_10s | icon_frequency_per_10s | split_screen_frequency | card_frequency | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `3-8s` in visible source video, sampled every 5s | AI video examples, reference/generated comparisons, chapter transitions | host explanations and prompt pages | chapter/title cards and host reset | `2-4` | `1-2` | `0-1` | high in comparison clusters | medium_high | medium |
| `reference_02` | `4-10s` | examples and green-check claims | mobile operation screens | host returns and test-card reset | `1-3` | `1-2` | `1` | low-medium; mostly phone PIP | medium | medium |
| `reference_03` | `5-15s` | hook and analogy build | document evidence sections | host bridge every dense cluster | `1-2` in doc sections, `2-3` in concept sections | `1` | `0-1` | medium through boxes/side panels | high | medium_high |
| `reference_04` | `8-20s` in evidence blocks, `3-8s` in hooks | opening/title and practical close | phone/text evidence with yellow highlights | host reset after 2-3 dense screens | `1-2` | `0-1` | `0-1` | low; phone evidence dominates | medium | medium_high |

## cross_reference_answers

1. 对标视频总体是 `medium_fast`，不是无脑快剪。快的是例子切换和概念转场，慢的是证据阅读窗口。
2. 必须快的地方：开头 0-10s、章节切换、例子轮播、结果对比出现前后。
3. 必须停的地方：文档/聊天/网页证据、黄高亮段、步骤列表、before/after 对比。
4. 每 10 秒视觉变化：hook/例子段约 2-4 次；证据段约 1-2 次。
5. 关键词 / 小图标密度：参考里通常只在关键词层出现 1-2 个，不会每句话都贴；小图标必须是 step/result/emotion marker。
6. 卡片职责：多数卡片是在讲内容或 reset 语义，不是纯转场装饰。
7. 转场职责：转场主要帮助观众理解“进入下一能力/下一证据”，不是炫技。

## migration_rhythm_rule

- Dense evidence cluster 最多连续 `15-30s`，之后要有 host/guide/bridge reset。
- Hook 段可 `2-4 changes / 10s`；证据段应降到 `1-2 changes / 10s`。
- 如果一屏同时有证据、字幕、关键词、PIP、图标，必须明确主视线顺序。
