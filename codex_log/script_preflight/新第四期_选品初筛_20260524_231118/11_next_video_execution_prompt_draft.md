# next_video_execution_prompt_draft

not_executed_this_round = true

## Goal
基于已复核的新第四期锁稿、line_group 映射和素材时间码，生成横屏 16:9 的新第四期成片候选或明确 blocked。

## Context
- 当前内容方向：Codex / AI 参与选品初筛，把精选联盟商品卡整理成候选表、明细表、复查表和聊天框结论。
- 本轮前置包路径：`codex_log/script_preflight/新第四期_选品初筛_20260524_231118/`
- 必须先复核 `10_copy_change_request_if_any.md`，由 ChatGPT / 用户确认是否接受改稿请求。

## Constraints
- 不得擅自改 locked_title、locked_opening_line、核心判断和边界句。
- 不得生成或使用未授权第三方素材、BGM、音效、字体、logo。
- 不得写爆品、一定能卖、佣金保证、自动赚钱、商业闭环。
- 必须遮挡账号、路径、商品敏感信息。
- 表格小字不可读时必须补录、局部放大或卡片重建。

## Impact check
1. 读取 locked_copy_contract。
2. 读取 script_to_timeline_map。
3. 读取 card_placement_decision。
4. 读取 privacy_and_readability_check。
5. 确认 R001/R003 是否补录。
6. 确认 content_validation 仍不推进。

## Must read
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/00_locked_copy_contract_candidate.md`
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/01_line_group_map.md`
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/02_script_to_timeline_map.json`
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/07_card_placement_decision.md`
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/09_privacy_and_readability_check.md`
- `codex_log/script_preflight/新第四期_选品初筛_20260524_231118/10_copy_change_request_if_any.md`

## Execution steps
1. 确认 ChatGPT / 用户已处理 copy_change_request。
2. 锁定最终文案和分句。
3. 建立正式 `locked_copy_contract`。
4. 按 line_group 生成时间线。
5. 对 V001/V003/V004 做隐私遮挡、局部放大和卡片排版。
6. 生成 TTS，并按 `06_tts_prosody_anchor_map.json` 调整停顿。
7. 执行字幕和卡片重叠检查。
8. 导出横屏 16:9、1920x1080 候选片。
9. 生成 review pack 和验证报告。

## Done when
- 成片候选为横屏 16:9、1920x1080。
- 每个 line_group 都能追溯到素材时间码或边界卡。
- 隐私已遮挡。
- 字幕/卡片无 high severity overlap。
- TTS、BGM、音效不过度抢信息。
- 内容状态仍需人工复审，不写 send_ready。

## Blocked if
- copy_change_request 未处理。
- 关键表格小字不可读且无补录/卡片替代。
- 账号、路径、商品敏感信息无法遮挡。
- 文案与画面不匹配。
- 缺音频、字幕、横屏构图或导出能力。
- 任何需要把 `content_validation` 或 `send_ready` 推进的情况。

## Output
- final_video_candidate 或 blocked report
- review_pack
- timeline_manifest
- privacy_mask_report
- subtitle_card_overlap_report
- status_boundary_report
