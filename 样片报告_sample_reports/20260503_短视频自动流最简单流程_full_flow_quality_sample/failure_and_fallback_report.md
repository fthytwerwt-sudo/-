# failure_and_fallback_report

## 本轮目标

- `sample_type`：`full_flow_quality_sample`
- `flow_proof_sample_used`：`false`
- `technical_flow_sample_used`：`false`
- `short_review_sample_used`：`false`

## 替代项

| 能力 | 本轮状态 | 替代处理 | 是否冒充正式能力 |
|---|---|---|---|
| API 生成真人 / 主持壳 | `api_human_runtime_not_executed_this_round` | 使用原创体素主持壳 fallback 卡承担开头、判断、转折、收束 | `false` |
| 项目 TTS / custom voice | `project_tts_not_safely_executed_this_round` | 使用 macOS `say` 临时完整旁白 | `false` |
| 云端剪辑 / ICE / 云剪 | `cloud_assembly_not_executed_this_round` | 使用本地 assembly fallback 生成完整视频 | `false` |
| 火山引擎 API 特写 | `unsafe_without_manual_redaction_review` | API 信息卡 fallback | `false` |
| HyperFrames | `not_rendered_this_round` | 仅按 card_motion_layer 边界写报告 | `false` |

## 边界

- 不写 `content_validation=passed`。
- 不写 `send_ready=true`。
- 不写 API 已接通。
- 不写 Trae app 已跑通。
- 不写云剪正式稳定。
- 不写 Codex 证明内容过线。
