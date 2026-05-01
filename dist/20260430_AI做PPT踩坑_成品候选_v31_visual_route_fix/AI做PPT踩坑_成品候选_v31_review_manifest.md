# AI 做 PPT 踩坑成品候选 v3.1 审片入口

`已确认` 本包是 `finished_quality_candidate_v31（成品质量候选片 v3.1）` 与当前视频基线；后续升级、修改、技术优化、GPT 文案侧回炉默认基于 v3.1。

`已确认` 本包不是可发送版本，不代表内容验证通过，不代表视觉母版 locked。

## 先看文件

1. `AI做PPT踩坑_成品候选_v31_full.mp4`：v3.1 完整成品候选片。
2. `AI做PPT踩坑_成品候选_v31_contact_sheet.jpg`：全片关键帧联系表。
3. `visual_route_map.json`：视觉路由表。
4. `visual_route_validation_report.json`：视觉路由验证报告。
5. `locked_reference_inheritance_report.md`：锁定参考继承报告。
6. `video_metadata_probe_report.json`：video-metadata-probe 检查报告 JSON。
7. `AI做PPT踩坑_成品候选_v31_summary.json`：状态摘要。
8. `AI做PPT踩坑_成品候选_v31_timeline.json`：时间线。
9. `AI做PPT踩坑_成品候选_v31_cut_map.md`：镜头说明。

## 当前边界

- `content_validation = pending_user_chatgpt_review_or_not_passed_copywriting_side`
- `send_ready = false`
- `subtitle_enabled = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `visual_master_candidate = true`，但 `visual_master_locked = false`。
- `sassy_card_execution_reference = PR7_B_骚萌反应页.png`
- `sassy_card_reference_locked = true`

## 本轮重点

- 先输出并校验 `visual_route_map.json`，再生成视频。
- 补回 `negative_display_prompt_card` 与 `positive_display_prompt_card`。
- 将三张骚萌卡改走 PR #7 B 的独立 reaction page 路线。
- 将信息卡改走粉色樱花柔和展示牌皮肤 + 清晰信息层级路线。
- 保留“反面结果露馅 -> 方法词出现 -> 字段拆解 -> 正面操作 -> 结果预览 -> 边界收束”的主线。
- 保留正反录屏素材事实，以真实录屏作为中段主体。
- 保留核心方法词：`可交付初稿`。
- 使用 custom voice TTS 入片，但声音仍待用户 / ChatGPT 听感复审。
- v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- PR #7 A 只能作为历史 / candidate 对照，不能作为后续骚萌卡执行参考。
- 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。

## 本地路径

- 复审包：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- full video：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4`
- duration_seconds：`149.993`
- resolution：`720x1280`
- audio_codec：`aac`
