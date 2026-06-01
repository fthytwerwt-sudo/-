# 分屏系统地图 Split Screen System Map

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

## 总结

- 4 条参考里真正有迁移价值的不是“满屏分屏”，而是 `comparison_reason_first（先有比较理由再分屏）`。
- `reference_01` 和 `reference_03` 的分屏/类分屏最多：用于 `reference/generated`、`prompt/result`、`source/output`、`step/options`。
- `reference_02` 和 `reference_04` 更多是 `phone_in_phone / main_screen_plus_side_panel`，不是完整二分屏。
- 所有分屏都依赖标签、PIP、字幕和黑底安全区；脱离这些，分屏会变成 PPT 拼图。

| reference_id | timecode | split_type | layout_ratio | primary_side | secondary_side | entry_transition | exit_transition | duration | highlight_inside_split | subtitle_inside_split | keyword_inside_split | function | migrate_condition | do_not_use_if | failure_line |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `00:10-00:35` | `main_screen_plus_side_panel / option_grid` | `main 60-70%, side 30-40%` | generated result / product page | reference sample / host/PIP | hard cut from host | hard cut to title/card | `3-8s per board` | yes, labels and bordered panels | lower subtitle | title/logo tags | quickly prove tool output range | when one claim needs 2-3 visual examples | panels are unreadable in 16:9 or no comparison claim | viewer cannot name what is being compared |
| `reference_01` | `01:45-02:20` | `reference_generated / before_after` | `two panels or 2+1 collage` | generated result | reference / prompt input | hard cut | result clip or host reset | `5-15s` | yellow/white labels | lower subtitle | reference/generated labels | show capability transfer | when source and output are both visible and directly comparable | source and output prove different claims | split looks decorative |
| `reference_02` | `00:00-00:55` | `picture_in_picture / phone_frame` | `host 45-55%, phone 35-45%` | phone operation or host depending beat | host/phone complement | hard cut / phone slide implied | hard cut | `5-20s clusters` | some green tags | yes | green keyword stickers | explain mobile operation without leaving host | only if source material is mobile-first | desktop workflow is forced into phone shell | phone text too small to read |
| `reference_03` | `00:25-01:15` | `option_a_b / step_boxes` | `3 boxes across black stage` | current step box | empty/future boxes | build-in by cuts | host or icon reset | `5-10s` | active box highlighted | lower subtitle | large step words | teach abstract system through progressive boxes | when concept has clear stages | stages are arbitrary or too many | viewer sees boxes but not logic |
| `reference_03` | `02:45-04:20` | `main_screen_plus_side_panel` | `evidence page 70-85%, label/PIP 15-30%` | document/web evidence | side label + PIP guide | hard cut with label already present | hard cut to next evidence | `10-25s` | yellow/purple highlights | lower subtitle | side category tags | orient viewer inside dense document | when a dense page has one active evidence window | no active highlight or text too small | screen becomes raw document dump |
| `reference_04` | `00:30-03:35` | `phone_evidence_plus_host_pip` | `phone 55-70%, host/PIP 15-30%` | highlighted phone/chat text | host/PIP context | hard cut / crop focus | host reset or next phone page | `15-40s clusters` | strong yellow highlights | lower subtitle | section labels | make long AI memory/chat text readable | when text evidence is the proof and can be cropped | highlights exceed one claim or phone unreadable | yellow bars create visual noise |

## answer_to_required_questions

1. 分屏通常出现在“同一能力需要输入/输出、参考/成片、步骤/选项并置”时，而不是为了装饰。
2. 分屏的理由是减少口播解释成本，让观众一眼看到差异或流程位置。
3. 主信息永远是当前口播正在证明的那个面板；PIP/头像/图标只是辅助。
4. 可迁移持续时间：单个比较 `3-8s`，复杂证据 `8-15s`，长文档/聊天最多 `20-40s` 但必须中间有高亮推进。
5. 进入/退出主要靠 hard cut + 同一黑底舞台/标签保持连续，不靠花哨转场。
6. 分屏常配合关键词、字幕、小 PIP；如果缺标签，分屏很容易失焦。
7. 新第四期只有在素材能提供 `source/output`、`before/after`、`prompt/result` 或 `option A/B` 时才允许用；否则 blocked 或改成单证据窗口。
