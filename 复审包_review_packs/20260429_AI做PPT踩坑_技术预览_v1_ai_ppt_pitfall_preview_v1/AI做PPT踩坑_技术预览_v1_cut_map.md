# AI 做 PPT 踩坑｜技术预览 v1 cut map

`preview_type = technical_preview`，本文件只说明本轮技术预览剪辑结构，不代表内容验证通过。

## 镜头表

| shot | time | carrier | source | note |
| --- | --- | --- | --- | --- |
| `shot00_opening_hello_wave` | `0.0-2.0s` | 元素娃娃开场素材 | `/Users/fan/Documents/视频工厂/素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | 字幕：hello，大家好；不讲方法 |
| `shot01_result_gap_opening` | `2.0-9.0s` | 分屏对比卡 | `negative_035 + positive_720` | 先给结果差 |
| `shot02_negative_input_wrong_prompt` | `9.0-17.0s` | 反面录屏 | `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4` | 最新方案.pdf + 帮我把这个方案整理一下 |
| `shot03_problem_hook_sassy_card` | `17.0-18.6s` | 骚萌卡 | `generated_card` | 只做轻吐槽 |
| `shot04_negative_result_text_plan` | `18.6-31.6s` | 反面录屏 | `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4` | 标题/产品矩阵/30天计划/最终执行铁律 |
| `shot05_negative_reversal_sassy_card` | `31.6-33.1s` | 骚萌卡 | `generated_card` | Word/PPT 落差吐槽 |
| `shot06_attribution_turn` | `33.1-44.1s` | 判断卡 | `generated_card` | AI 没偷懒，是交付没说清 |
| `shot07_positive_method_deliverable_draft` | `44.1-53.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | 放大可交付初稿检查项 |
| `shot08_prompt_architecture` | `53.1-69.1s` | Prompt 架构卡 | `generated_card` | 三层：交付物/检查/生成结构 |
| `shot09_positive_title_specific` | `69.1-81.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | AI 时间管理小程序 7 天种子用户拉新营销方案 |
| `shot10_positive_constraints_clear` | `81.1-93.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | 周期/预算/渠道/目标 |
| `shot11_positive_ppt_page_instruction` | `93.1-105.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | 页面设计/XML/核心指标 |
| `shot12_ppt_generation_process` | `105.1-119.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | 正在生成 PPT + 缩略图逐页出现 |
| `shot13_result_preview_6m31_16pages` | `119.1-129.1s` | 正面录屏 | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | 已完成PPT生成(6m31s) + 16 页预览 |
| `shot14_positive_reversal_sassy_card` | `129.1-130.7s` | 骚萌卡 | `generated_card` | 正向反转但保留边界 |
| `shot15_result_diff_card` | `130.7-138.7s` | 结果差卡 | `generated_card` | 普通问法 vs 交付标准 |
| `shot16_low_pressure_ending` | `138.7-150.7s` | 总结卡 | `generated_card` | 不是一步到位，进入可检查初稿 |
| `shot17_prompt_tail_card` | `150.7-154.7s` | Prompt 引用尾卡 | `generated_card` | 经验承接尾卡 |

## 边界

- `content_validation = pending_user_chatgpt_review`。
- `send_ready = false`。
- 16 页 PPT 预览只代表结果形态变化，不代表最终 PPT 已通过验收。
- 本轮未调用 voice cloning，声音状态为 `temporary_no_voice_preview`。
