# AI 做 PPT 踩坑｜成品标准候选 v2 cut map

`preview_type = finished_quality_candidate_v2`，本文件说明 v2 候选片剪辑结构；不代表内容验证通过。

| shot | 成片时间 | 承载方式 | 文件来源 | 审片判断 |
| --- | --- | --- | --- | --- |
| `shot00_opening_hello_wave` | `0.000-2.000s` | 元素娃娃开场素材 | `/Users/fan/Documents/视频工厂/素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | 约 2 秒 hello 开场，不承担方法和总结。 |
| `shot01_result_gap_opening` | `1.880-6.880s` | 结果差开头卡 | `negative_035 + positive_720 screenshots` | 先给结果差，不先讲理论。 |
| `shot02_negative_input_wrong_prompt` | `6.760-13.260s` | 反面录屏 | `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4 15.000s-21.500s` | 最新方案.pdf 与“帮我把这个方案整理一下”清楚出现。 |
| `shot03_problem_hook_sassy_card` | `13.140-14.740s` | 独立骚萌 reaction card | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/problem_hook_sassy_card.png` | 问题钩子，只做轻吐槽。 |
| `shot04_negative_result_text_plan` | `14.620-25.620s` | 反面录屏 | `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4 35.000s-46.000s` | 战略执行总案、产品矩阵等文字方案露出。 |
| `shot05_negative_reversal_sassy_card` | `25.500-27.000s` | 独立骚萌 reaction card | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/negative_reversal_sassy_card.png` | 翻车吐槽，不讲方法。 |
| `shot06_attribution_turn` | `26.880-32.880s` | 短判断卡 | `generated layout card` | AI 没偷懒，是交付没说清；避免长篇 judgment_card。 |
| `shot07_positive_standard_and_constraints` | `32.760-45.760s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4 30.000s-43.000s` | 可交付初稿、对象/目标/动作/节奏等检查标准和标题约束出现。 |
| `shot08_positive_ppt_generation_start` | `45.640-53.640s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4 570.000s-578.000s` | 进入 PPT 生成界面，正在生成。 |
| `shot09_positive_6m31_16page_preview` | `53.520-67.520s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4 712.000s-726.000s` | 已完成PPT生成(6m31s) 与 16 页预览。 |
| `shot10_positive_reversal_sassy_card` | `67.400-69.000s` | 独立骚萌 reaction card | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/sassy_cards/positive_reversal_sassy_card.png` | 正向反转但保留边界。 |
| `shot11_result_diff_card` | `68.880-74.880s` | 结果差卡 | `generated layout card` | 一屏左右对比，不做多屏总结。 |
| `shot12_low_pressure_ending` | `74.760-81.760s` | 低压结尾卡 | `generated layout card` | 低压收束，不进入第二主结尾。 |

## 边界

- `content_validation = pending_user_chatgpt_review`。
- `send_ready = false`。
- 16 页 PPT 预览只代表结果形态变化，不代表最终 PPT 已通过验收。
- 本轮未调用 voice cloning，声音状态为 `temporary_no_voice_preview`。
