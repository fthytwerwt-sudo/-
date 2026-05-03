# 样片等级裁决 sample_level_decision

## 1. 当前用户目标更接近哪一级

`已确认` 当前用户目标更接近：

`mainline_inheritance_candidate`

原因：

- 用户要求纳入正式主线四件套：API 生成真人 / 主持壳、用户录制素材、少量 PPT / 信息卡、云端剪辑。
- 用户要求继承 visual route 和 locked reference。
- 用户要求完整文案保真，并要求下一轮不能做“能看但不像仓库样片”的技术预览。

## 2. 本轮仓库能力实际支持哪一级

`部分成立` 当前已确认支持：

- 用户录制素材可证明豆包 -> Trae -> 项目骨架 -> Codex 检查流程。
- visual route 规则和 validation report 可读。
- locked reference registry 可读。
- HyperFrames card_motion_layer 边界可读。
- PR #36 / PR #37 证明云剪候选链路曾跑通。

`待验证` 当前仍需下一轮真实确认：

- API 生成真人 / 主持壳 runtime 是否可用于本条 V3。
- 项目 TTS / custom voice 是否可生成完整文案配音。
- 云端剪辑是否能真实执行本条 V3 timeline。

因此实际支持等级暂定为：

`flow_proof_sample_ready_for_user_decision`

它不能直接写成 `mainline_inheritance_candidate`。

## 3. 如果二者不一致，是否 blocked

`已确认` 二者不一致。

当前 render gate 应为：

`blocked_need_user_decision`

不是能力彻底不可做，而是需要用户确认下一轮是否允许降级为 `flow_proof_sample`，或先补齐 API 主持壳 / 项目 TTS / V3 云剪能力后再冲 `mainline_inheritance_candidate`。

## 4. 是否需要用户确认降级

`已确认` 需要。

若用户仍要求 `mainline_inheritance_candidate`：

- 必须先补 API 主持壳 runtime 证据。
- 必须先补完整项目 TTS / custom voice 实跑证据。
- 必须先补 V3 云剪真实执行能力。

若用户明确允许 `flow_proof_sample`：

- 可不真实调用 API 主持壳。
- 可不真实调用云剪。
- 可不生成项目 TTS。
- 必须标记 degraded，不得写成完整主线候选片。

## 5. 不能直接把 flow_proof_sample 写成 mainline_inheritance_candidate

`已确认` 禁止。

`flow_proof_sample` 只能证明：

- 一句需求进入豆包。
- 豆包拆流程。
- 豆包生成 Trae prompt。
- prompt 进入 Trae SOLO。
- Trae plan 并生成项目骨架。
- Codex 做执行检查。

它不能证明：

- API 主持壳已生成。
- 项目 TTS 已完整覆盖文案。
- V3 云端剪辑已执行。
- 内容已过线。
- 可发送。
