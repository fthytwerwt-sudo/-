# 20260503｜样片参考质量规则写入 reference_quality_sample_rule

## 1. 修改目的

本轮只把《视频工厂》“样片默认等于参考质量片”的规则写入仓库当前执行包，并生成一份可直接放进 GPT Project 的同步规则文本。

本轮不是出片任务，不是剪辑任务，不生成《短视频自动流的最简单流程》视频，不修改样片、render、TTS、云剪、API 主持壳或素材。

## 2. 修改文件

- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`
- `codex_log/20260503_样片参考质量规则写入_reference_quality_sample_rule.md`

## 3. 规则摘要

`已确认` 后续在《视频工厂》中，只要用户要求：

- 做样片
- 出片
- 完整片
- 按参考做
- 按仓库口径做
- 按 locked reference 做
- 按当前样片标准做

默认样片等级必须是：

`reference_quality_sample（参考质量样片）`

默认禁止降级为：

- `flow_proof_sample（流程证明降级片）`
- `technical_flow_sample（技术流程样片）`
- `review_sample（复审短样片）`
- `short_preview（短预览片）`
- `local_assembly_demo（本地拼装演示片）`

参考质量样片必须按当前正式主线执行：

`API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`

并且必须按 locked reference 继承、按 visual route 执行、输出完整视频、输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`。

如果 API 生成真人、项目 TTS / 声音节奏、云端剪辑、locked reference 继承、visual route、用户录制素材主体承载、完整文案保真入片或敏感信息脱敏任一关键项无法满足参考质量，默认先尝试补齐；补不齐则输出：

`blocked_reference_quality_sample_not_completed`

不得交一个“能播放但不是参考质量”的片子冒充完成。

## 4. 本轮未做事项

- `已确认` 未生成媒体文件。
- `已确认` 未生成视频。
- `已确认` 未生成音频。
- `已确认` 未生成图片。
- `已确认` 未修改任何素材文件。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前 v3.1 publish target。
- `已确认` 未把 `content_validation` 写成通过。
- `已确认` 未把 `send_ready` 写成 `true`。

## 5. 后续 Codex 视频样片任务默认执行口径

后续给 Codex 的视频执行单必须在开头写：

```md
本轮样片等级：
reference_quality_sample（参考质量样片）
```

若无法达到参考质量，必须输出：

```md
blocked_reference_quality_sample_not_completed
```

不得输出 flow proof、technical sample、review sample、short preview 或 local assembly demo 冒充完成。

## 6. 下一个目标

后续 Codex 视频样片任务默认按参考质量样片口径启动，无法满足参考质量时明确 blocked。
