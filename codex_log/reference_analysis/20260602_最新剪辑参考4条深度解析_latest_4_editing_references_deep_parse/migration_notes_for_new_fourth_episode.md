# 迁移到新第四期注意事项 Migration Notes For New Fourth Episode

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

## 最值得迁移的 5 个机制

1. `active_evidence_window（主动证据窗口）`: 每个真实录屏 / 文档 / 商品表 / 工具界面必须先圈定观众该看哪一块。
2. `guided_split_screen（有比较理由的分屏）`: 只在 before/after、prompt/result、source/output、option A/B 时使用。
3. `subtitle_as_attention_guide（字幕作为注意力引导）`: 字幕不只是转写，要服务节奏和视线。
4. `functional_keyword_badge（功能型关键词标签）`: pain/action/result/number/conclusion 词才值得弹出。
5. `low_density_bridge_after_dense_proof（密集证据后的低密度桥接）`: 连续证据后用 host/guide/bridge card 帮观众换气。

## 需要新第四期素材支持的机制

- 分屏：需要同时有 source/output 或 before/after 的可读素材。
- 证据窗口：需要原始录屏足够清楚，关键字段能被 crop 到可读。
- 手机 PIP：只有当真实素材是手机页面或平台页面时使用。
- 高亮：需要知道哪一句/哪一行/哪个字段证明当前口播。
- 桥接卡：需要 locked copy 里有明确章节或转折点。

## 素材不支持必须 blocked 的情况

- 没有 `active_evidence_window` 却要做证据解释。
- 只有主题相近素材，没有能证明口播的直接画面。
- 分屏两侧不能证明同一对比命题。
- 字幕/卡片会压住 prompt、表格、聊天、按钮或高亮段。
- 只能产出技术预览，却被要求写成可发布候选片。

## 只能做边缘辅助的机制

- 小图标、PIP、表情、绿色 check、测试卡 reset、城市/情绪 B-roll。
- 它们可以做节奏或情绪，但不能抢真实证据和核心判断。

## 容易做成 PPT / demo / 花活感的机制

- 每屏都塞大标题 + 多图标 + 多关键词。
- 分屏没有比较理由。
- 整页文档缩小展示但没有高亮。
- 用卡片替代真实录屏证据。
- 只学黑底黄字，不学证据窗口和节奏桥。

## 下一轮 30-45 秒验证片优先验证哪一段

优先选 `one_dense_evidence_segment（一个密集证据段）`：含 1 个真实录屏/文档证据、1 个 before/after 或 prompt/result 对比、1 次 bridge reset、1 个关键词 badge、1 段安全字幕。

## 下一轮验证片必须准备的输入

- `locked_copy_contract`
- `script_to_timeline_map` line_group 级版本
- `material_parse_pack` / `source_segment_inventory`
- `active_evidence_window_map`
- `subtitle_safe_zone_plan`
- `split_screen_use_reason`（如使用分屏）
- `not_allowed_to_copy_asset_list`

## 下一轮不能直接做什么

- 不能直接剪完整新第四期。
- 不能把这 4 条参考的真人/平台 UI/Logo/字体/贴纸当模板复制。
- 不能新增正式机制文件或函数，除非用户/ChatGPT 审过本草案。
- 不能把本轮 draft 写成 `content_validation = passed`。
