# 样本索引 sassy sample index

## 状态边界

`已确认` 2026-05-01 用户最新确认覆盖本包 2026-04-30 旧只读判断：后续骚萌卡执行参考改为 `PR7_B_骚萌反应页.png（PR #7 B 版骚萌反应页）`。PR #7 A 保留为历史 / candidate 对照，不再作为下一轮 v3.1 后续执行参考。

`已确认` 若读不到 PR #7 B 原始文件或证据路径，必须 `blocked`，不得回退 PR #7 A。

- `old_preference_label`：历史只读判断中的旧优先候选标签，不等于 locked，且已被用户最新 PR #7 B 确认覆盖。
- `candidate` / `weak_candidate`：可复审、可对照，不得默认继承。
- `failed_reference`：失败参考或失败容器，只能复盘，不能默认继承。
- `historical_only`：历史演化参考，不建议作为下一轮主参考。
- `technical_preview`：技术预览产物，不代表内容或视觉最终通过。

## 样本列表

| 样本 | 状态标签 | 本地文件 | GitHub 可追溯来源 | 只读判断 |
| --- | --- | --- | --- | --- |
| PR #7 A 版骚萌反应页 | `historical_candidate_superseded_by_user_pr7_b_confirmation` | `PR7_A_骚萌反应页.png` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page.png` | 保留为历史 / candidate 对照；旧 A 优先判断已被用户最新确认的 PR #7 B 覆盖。 |
| PR #7 B 版骚萌反应页 | `locked_execution_reference_confirmed_by_user` | `PR7_B_骚萌反应页.png` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌B_static_reaction_page.png` | 用户最新确认的后续骚萌卡执行参考；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。 |
| PR #7 A/B 候选对比 | `technical_preview` | `PR7_骚萌候选对比_contact_sheet.jpg` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg` | 用于看 A/B 差异和选择理由。 |
| PR #7 15 秒骚萌预览 | `technical_preview` | `PR7_骚萌15秒预览.mp4`; `PR7_骚萌15秒预览_contact_sheet.jpg` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_scheme_b_standalone_reaction_v3_sassy_cute.mp4` | 证明 A 版作为独立 reaction clip 插入录屏主线时可看节奏；仍是静音技术预览。 |
| PR #6 整页反应版 V2 | `weak_candidate` | `PR6_整页反应版_contact_sheet.jpg`; `PR6_整页反应页_full_page_reaction.png` | `origin/codex/scheme-b-full-page-reaction-v2-20260428:dist/prototypes/20260428_方案B整页反应版15秒预览_scheme_b_full_page_reaction_v2/方案B整页反应页_full_page_reaction.png` | 方向是整页 reaction，不是贴片；但表情是崩溃 / X 眼 / 旋涡眼，不够“骚萌得瑟”。 |
| PR #5 中段吐槽技术预览 | `historical_only` | `PR5_中段吐槽_preview_contact_sheet.jpg`; `PR5_AI向导崩溃_overlay.png` | `origin/codex/scheme-b-15s-preview-20260427:dist/prototypes/20260427_方案B中段吐槽15秒预览_scheme_b_15s_reaction_preview/方案B人物反应层_ai_guide_meltdown_overlay.png` | 历史上更像 overlay / 崩溃贴图，有 `AI` 标识和本地绘图痕迹，不建议继承。 |
| PR #15 v2 三张骚萌卡 | `weak_candidate` / `failed_reference_container` | `PR15_v2_骚萌卡_contact_sheet.jpg`; `PR15_v2_sassy_cards/` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/` | 局部视觉仍可作为“PR #7 A 风格扩展”的对照，但 PR #15 整包是失败成品候选，不能默认继承。 |

## PR #7 日志证据

`已确认` PR #7 日志曾记录 A 版被选中进入 i2v；该记录只保留为历史上下文。

`已确认` 2026-05-01 用户最新确认已覆盖旧判断：PR #7 B 是后续骚萌卡执行参考。

## PR #7 视频技术信息

`已确认` `video-metadata-probe` 对本包内 `PR7_骚萌15秒预览.mp4` 的结果：

- `duration_seconds = 15.000000`
- `width = 720`
- `height = 1280`
- `fps = 25.000`
- `video_codec = h264`
- `audio_present = false`
- `decodable = true`
- `validation_status = passed`

说明：这是历史静音技术预览，不用于本轮声音验证。
