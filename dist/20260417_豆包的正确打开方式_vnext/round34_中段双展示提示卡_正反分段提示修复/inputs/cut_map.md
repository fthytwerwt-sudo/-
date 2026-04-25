# round34 cut map

`已确认` 本审片包指向 `round34_中段双展示提示卡_正反分段提示修复`。

| shot | 成片时间 | 承载方式 | 文件来源 | 审片判断 |
| --- | --- | --- | --- | --- |
| shot01_intro_host | 0.000s-10.264s | API生成真人 | /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/renders/主持壳正式正片_round31_一镜到底录屏证据链重构.mp4 0.000s-10.424s | 沿用 round31 / round30 开头主持壳，不重新生成元素娃娃。 |
| transition_01 | 10.264s-10.424s | 轻过渡 | shot01_intro_host -> shot02_negative_prompt_card | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot02_negative_prompt_card | 10.424s-11.704s | 卡片 | round34 generated 9:16 prompt card | 《反面展示》提示卡，图二粉色樱花柔和展示牌风格，副标题仅提示即将进入反面真实录屏，1.6s。 |
| transition_02 | 11.704s-11.864s | 轻过渡 | shot02_negative_prompt_card -> shot03_negative_recording | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot03_negative_recording | 11.864s-19.944s | 用户录制素材 | 素材录制/反面/录制于 2026-04-16 22.41.32.mp4 32.000s-40.400s | 反面连续录屏，证据链保持不变。 |
| transition_03 | 19.944s-20.104s | 轻过渡 | shot03_negative_recording -> shot04_positive_prompt_card | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot04_positive_prompt_card | 20.104s-21.384s | 卡片 | round34 generated 9:16 prompt card | 《正面展示》提示卡，插入于反面录屏和正面录屏之间，副标题仅提示即将进入正面真实录屏，1.6s。 |
| transition_04 | 21.384s-21.544s | 轻过渡 | shot04_positive_prompt_card -> shot05_positive_recording | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot05_positive_recording | 21.544s-37.224s | 用户录制素材 | 素材录制/正面/录制于 2026-04-16 23.03.53.mp4 610.000s-626.000s | 正面连续录屏，30-32 秒仍落在这一镜头内部。 |
| transition_05 | 37.224s-37.384s | 轻过渡 | shot05_positive_recording -> shot06_result_diff_card | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot06_result_diff_card | 37.384s-38.504s | 卡片 | round31 result_diff_card | 结果差提示卡保留，不新增解释卡。 |
| transition_06 | 38.504s-38.724s | 轻过渡 | shot06_result_diff_card -> shot07_clean_host | 0.22s crossfade，用于降低硬切 / 跳屏感。 |
| shot07_clean_host | 38.724s-43.680s | API生成真人 | /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/renders/主持壳正式正片_round31_一镜到底录屏证据链重构.mp4 38.620s-43.956s | 回场主持壳沿用干净源片段，不重新生成。 |
| transition_07 | 43.680s-43.840s | 轻过渡 | shot07_clean_host -> shot08_judgment_card | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot08_judgment_card | 43.840s-49.600s | judgment_card | /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/renders/主持壳正式正片_round31_一镜到底录屏证据链重构.mp4 43.956s-50.036s | 结尾总结卡保持信息密度不变。 |
| transition_08 | 49.600s-49.760s | 轻过渡 | shot08_judgment_card -> shot09_prompt_tail | 0.16s crossfade，用于降低硬切 / 跳屏感。 |
| shot09_prompt_tail | 49.760s-55.920s | Prompt引用尾卡 | /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/renders/主持壳正式正片_round31_一镜到底录屏证据链重构.mp4 50.036s-end | Prompt 引用尾卡不承担主叙事和中段证据。 |

## round34 修复说明

- `已确认` 原段首提示卡已替换为《反面展示》提示卡。
- `已确认` 已在反面录屏之后、正面录屏之前新增《正面展示》提示卡。
- `已确认` 两张提示卡均为 9:16 竖屏展示牌，时长 `1.6s`。
- `已确认` 中段主要切点使用 `0.16s` 轻 crossfade，结果差卡回主持壳使用 `0.22s` 轻 crossfade。
- `已确认` 反面录屏和正面录屏源片段未裁短、未重录、未替换。
- `已确认` 结果差提示卡、主持壳、judgment_card、Prompt 引用尾卡均未重做。
- `未发生` 阿里 API 调用、元素娃娃重生成、原始录屏修改、额外解释卡新增。
- `待验证` 内容最终是否过线仍需用户 / ChatGPT 人工复审。
