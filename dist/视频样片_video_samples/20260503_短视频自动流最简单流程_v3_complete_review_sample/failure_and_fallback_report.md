# failure_and_fallback_report

## 1. 样片等级

- `sample_type`：`flow_proof_sample`
- 降级原因：API 主持壳 / 项目 TTS / V3 云剪任一能力缺少本轮安全 runtime 证明。

## 2. 逐项降级

| 能力 | 状态 | 处理 |
| --- | --- | --- |
| API 主持壳 | `missing_api_human_runtime` | fallback 到主持壳判断卡 / 信息卡 |
| 项目 TTS | `project_tts_not_safely_executed` | 使用 macOS say 临时 TTS，`audio_validation=temporary_preview` |
| V3 云剪 | `not_used_this_round` | 使用本地 assembly fallback，`cloud_assembly_runtime=not_used_fallback_local_preview` |
| locked reference | `registry_read` | 主线继承不足，输出 flow proof 继承报告 |
| 火山引擎素材 | `not_used` | API 段信息卡 fallback |

## 3. 边界

- 不写 `mainline_inheritance_candidate`。
- 不写 `content_validation=passed`。
- 不写 `send_ready=true`。
- 不写云剪正式稳定。
