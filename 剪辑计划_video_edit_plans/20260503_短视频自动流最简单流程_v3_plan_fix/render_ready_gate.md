# Render Ready Gate

## 1. 结论

`render_ready_gate = blocked_need_user_decision`

## 2. 为什么是这个结论

`已确认` 当前用户目标更接近 `mainline_inheritance_candidate`。
`已确认` `mainline_inheritance_candidate` 必须真实具备 API 生成真人 / 主持壳、项目 TTS / custom voice、visual route、locked reference、真实云端剪辑。
`部分成立` visual route、locked reference、HyperFrames card_motion_layer、用户录制素材流程证据已可规划。
`待验证` API 主持壳 runtime、完整项目 TTS、V3 云剪真实执行尚未在本轮验证。

因此不能直接进入 mainline render。

## 3. 如果能 render，下一轮允许的样片等级

当前不允许自动 render。

若用户确认降级，可进入：

`render_ready_for_flow_proof_sample`

前提：

- 明确写 `sample_type = flow_proof_sample`。
- 明确写 `cloud_assembly_status = not_executed_this_round`。
- 明确写 `content_validation = pending_user_chatgpt_review`。
- 明确写 `send_ready = false`。
- 明确写 degraded 原因。

若用户坚持 mainline，则必须先补齐：

- API 主持壳 runtime 证据。
- 项目 TTS / custom voice 完整文案实跑证据。
- V3 云剪真实执行证据。

## 4. 如果不能 render，缺什么

缺：

- `missing_api_human_runtime`
- `missing_project_tts_runtime_for_full_script`
- `missing_v3_cloud_assembly_runtime`
- `need_user_degrade_authorization`

## 5. 是否需要用户确认降级

`已确认` 需要。

没有用户确认降级时，不得把 `flow_proof_sample` 写成 `mainline_inheritance_candidate`。

## 6. 是否需要先补能力

| 能力 | 是否需要先补 | 说明 |
| --- | --- | --- |
| API 主持壳 | 是，如目标 mainline | 不能仅凭 `formal_api_demo` 文件名判断可用 |
| 项目 TTS | 是，如目标 mainline | 必须覆盖完整文案 |
| 云剪 | 是，如目标 mainline | PR #36 / PR #37 只证明历史候选链路 |
| HyperFrames | 否 | 只需计划层挂合法 route；不得渲染 |
| locked reference | 已有 registry，但 render 前需输出继承报告 | candidate / failed 不能误写 |

## 7. blocked 项

- `blocked_need_user_decision`
- `blocked_if_mainline_without_api_human_runtime`
- `blocked_if_mainline_without_project_tts_runtime`
- `blocked_if_mainline_without_v3_cloud_assembly_runtime`
