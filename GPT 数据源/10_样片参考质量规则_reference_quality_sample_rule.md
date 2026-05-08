# 样片参考质量规则 reference_quality_sample_rule

## 1. 文件定位

本文件是可直接放进 GPT Project 的同步规则文本。

它只同步一条核心规则：

以后在《视频工厂》中，用户默认说的“样片”不是流程证明片、技术流程片、复审短样片、短预览片或本地拼装演示片，而是：

`reference_quality_sample（参考质量样片）`

## 2. 触发条件

以后在《视频工厂》中，只要用户要求：

- 做样片
- 出片
- 完整片
- 按参考做
- 按仓库口径做
- 按 locked reference 做
- 按当前样片标准做

默认样片等级必须是：

`reference_quality_sample（参考质量样片）`

## 3. 默认动作

触发后，GPT / Codex 默认必须按参考质量样片处理，而不是自动降级。

`reference_quality_sample（参考质量样片）` 的含义是：

1. 必须按仓库当前正式主线执行：

   `API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`

2. 必须按 `locked reference（锁定参考）` 继承。

3. 必须按 `visual route（视觉路由）` 执行。

4. 必须输出完整视频，而不是短预览。

5. 必须达到“可作为参考继续迭代”的质量，不是技术拼装证明。

## 4. 禁止默认降级

默认禁止把样片解释为：

- `flow_proof_sample（流程证明降级片）`
- `technical_flow_sample（技术流程样片）`
- `review_sample（复审短样片）`
- `short_preview（短预览片）`
- `local_assembly_demo（本地拼装演示片）`

除非用户明确授权降级，否则：

- 不允许输出 flow proof 交差。
- 不允许输出 technical sample 交差。
- 不允许输出 2 分钟短样片交差。
- 不允许输出 145 秒压缩片交差。
- 不允许把完整文案压缩成短 runtime 冒充完整片。
- 不允许用普通信息卡冒充 API 生成真人。
- 不允许把卡片 / PPT 做成主叙事。
- 不允许把技术验证通过写成内容验证通过。
- 不允许把 `send_ready` 写成 true。
- 不允许把 TTS trial 写成声音通过。
- 不允许把云剪未实跑写成云剪稳定。

## 5. API 生成真人要求

`API 生成真人` 必须承担：

- 开头进入
- 关键判断
- 转折衔接
- 结尾收束

硬边界：

- 不能被普通信息卡默认替代。
- 不能被 PPT 卡片默认替代。
- 不能被 HyperFrames 卡片默认替代。
- 不能用“主持壳占位卡”冒充 API 生成真人。
- 不能长时间抢中段主体推进。

如果 API 生成真人无法达到参考质量，默认先尝试补齐；补不齐则 blocked。

## 6. 主线四件套职责

### 6.1 API 生成真人

负责：

- 开头进入
- 关键判断
- 转折衔接
- 结尾收束

不得：

- 被普通信息卡默认替代
- 被主持壳占位卡冒充
- 抢走用户录制素材的中段主体叙事

### 6.2 用户录制素材

负责：

- 中段主体推进
- 真实操作过程
- 工作流证据
- 前后差值 / 流程证据

不得：

- 被 PPT 抢主叙事
- 被卡片抢主叙事
- 被 HyperFrames 抢主叙事
- 被主持壳抢主叙事

### 6.3 少量 PPT / 信息卡

只能负责：

- 关键词显影
- 结构整理
- 状态边界
- 总结辅助

不得：

- 承担主叙事
- 把完整片做成 PPT 念稿
- 替代用户录制素材
- 替代 API 生成真人

### 6.4 云端剪辑

`云端剪辑` 是正式组装方向。

硬边界：

- 如果本轮未实跑，必须如实标记。
- 不得把本地 assembly fallback 写成云剪正式稳定。
- 不得把“方向已确定”写成“链路已稳定跑通”。

## 7. locked reference / visual route 读取要求

完整片 / 样片回炉 / 成品候选片必须读取：

- `codex_source/14_locked_reference_inheritance_rules.md`
- `codex_source/locked_reference_registry.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`

并且必须输出：

- `locked_reference_inheritance_report.md（锁定参考继承报告）`

没有继承报告，不得写成参考质量样片完成。

## 8. blocked 条件

如果以下任一关键项无法满足参考质量：

- API 生成真人
- 项目 TTS / 声音节奏
- 云端剪辑
- locked reference 继承
- visual route
- 用户录制素材主体承载
- 完整文案保真入片
- 敏感信息脱敏

默认处理是：

1. 先尝试补齐。
2. 补不齐则 blocked。
3. 输出：

   `blocked_reference_quality_sample_not_completed`

4. 不得交一个“能播放但不是参考质量”的片子冒充完成。

## 9. 失败判定

以下情况默认判定为未完成参考质量样片：

- 输出的是 flow proof，而不是参考质量样片。
- 输出的是 technical sample，而不是参考质量样片。
- 输出的是 review sample，而不是完整视频。
- 输出的是 short preview，而不是完整视频。
- 输出的是 local assembly demo，而不是正式组装方向下的参考质量样片。
- 完整文案被压缩成短 runtime。
- API 生成真人被普通信息卡或占位卡替代。
- 用户录制素材没有承担中段主体推进。
- 卡片 / PPT 成为主叙事。
- 云剪未实跑却写成云剪稳定。
- 没有读取 locked reference 规则和 registry。
- 没有读取 visual route 规则、视觉路由表或视觉路由验证报告。
- 没有输出 locked reference inheritance report。
- 只写 `technical_validation`，没有 reference inheritance validation。
- 把 `technical_validation` 写成 `content_validation`。
- 把 `send_ready` 写成 true。
- 把 TTS trial 写成声音通过。

## 10. Codex 下发默认要求

以后给 Codex 的视频执行单必须在开头写：

```md
本轮样片等级：
reference_quality_sample（参考质量样片）
```

并写明禁止默认降级为：

- `flow_proof_sample（流程证明降级片）`
- `technical_flow_sample（技术流程样片）`
- `review_sample（复审短样片）`
- `short_preview（短预览片）`

如果无法达到参考质量，必须输出：

```md
blocked_reference_quality_sample_not_completed
```

不得输出残片冒充完成。

## 11. 一句话规则

以后《视频工厂》的“样片”默认就是 `reference_quality_sample（参考质量样片）`：必须按当前正式主线、locked reference、visual route、API 生成真人、用户录制素材、少量 PPT 和云端剪辑完整执行；做不到就 blocked，不交降级片。
