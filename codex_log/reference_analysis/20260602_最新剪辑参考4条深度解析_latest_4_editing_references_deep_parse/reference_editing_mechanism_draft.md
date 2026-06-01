# 对标剪辑机制草案 Reference Editing Mechanism Draft

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

`status = draft_pending_chatgpt_user_review`

## 目标层

把《视频工厂》的真实录屏 / 文档 / 工具使用证据，包装成 `guided proof video（被引导的证据视频）`：观众先知道看哪里，再看证据，再通过字幕、关键词、PIP / guide 和桥接卡保持节奏。

## 机制层

### split_screen_mechanism（分屏机制）

- `trigger_if`: 存在 `before/after`、`prompt/result`、`source/output`、`reference/generated`、`option A/B`。
- `forbidden_if`: 只是为了丰富画面；任一 panel 低于可读线；panel 角色没有标签。
- `fallback`: 改成单 evidence window + 1 个关键词标签。

### keyword_emphasis_mechanism（关键词强调机制）

- `trigger_if`: 当前句组有 pain/action/result/number/conclusion word。
- `forbidden_if`: 关键词与口播不一致；超过 1 个主关键词 + 1 个辅助标签；抢证据窗口。
- `fallback`: 只在字幕中轻高亮或放到 section label。

### subtitle_guidance_mechanism（字幕引导机制）

- `trigger_if`: host/voice 解释或 dense evidence 需要跟读。
- `forbidden_if`: 字幕遮挡按钮/表格/聊天/高亮段；字幕变成三行以上说明书。
- `fallback`: 拆句、换安全区或短暂停留证据画面。

### icon_motif_mechanism（小图标 / 视觉符号机制）

- `trigger_if`: 需要 step/result/emotion/warning marker。
- `forbidden_if`: 图标只是可爱装饰；使用第三方贴纸/平台模板；覆盖证据。
- `fallback`: 用原创小 badge / outline / step number。

### evidence_window_mechanism（证据窗口机制）

- `trigger_if`: 画面包含文档、聊天、网页、表格、工具界面。
- `forbidden_if`: 没有 active evidence window；整页过小；高亮超过一个主 claim。
- `fallback`: crop focus 到单段 / 单字段，或 blocked 要补素材。

### bridge_card_mechanism（桥接卡机制）

- `trigger_if`: 连续 2-3 个 dense proof screen 后，或进入新能力/章节。
- `forbidden_if`: 证据链未完成却插装饰卡；桥接卡文案改写 locked copy。
- `fallback`: host/voice reset + 1 个 section label。

### rhythm_transition_mechanism（节奏 / 转场机制）

- `trigger_if`: 进入新段、例子轮播、证据到总结。
- `forbidden_if`: 转场只是花活；没有语义承接。
- `fallback`: hard cut + repeated container + label continuity。

## 流程层

1. 锁 `reference_to_execution_contract`。
2. 为新第四期建立 `locked_copy_contract` 和 line_group 级 `script_to_timeline_map`。
3. 为每个 line_group 标 `active_evidence_window`。
4. 逐段选择：single evidence / split screen / phone PIP / bridge card / host guide。
5. 做 `subtitle_card_overlap_check`。
6. 生成 30-45s 验证片前，先做 `quantitative_quality_standards_draft` 对照。

## 判断标准层

- 分屏通过：观众 2 秒内能说出左右/上下在比较什么。
- 关键词通过：关键词和口播/证据同义，且不超过密度线。
- 字幕通过：不遮证据，1-2 行可读。
- 小图标通过：能说明 step/result/emotion，不是装饰。
- 证据窗口通过：active line/field 可见且有高亮或裁切。
- 节奏通过：dense block 后有呼吸点，hook 不拖，证据不闪。

## 反馈层

- 如果“不像参考”：先查 `evidence_window` 与 `rhythm_transition`，不是先加贴纸。
- 如果“像 PPT”：减少桥接卡密度，增加真实证据裁切和 host/guide 连续性。
- 如果“看不懂”：补 section label / active highlight / split role label。
- 如果“太花”：砍掉 decoration_only icon，保留关键词和证据高亮。
