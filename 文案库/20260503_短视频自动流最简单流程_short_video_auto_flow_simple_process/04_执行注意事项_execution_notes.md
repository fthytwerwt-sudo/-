# 执行注意事项：短视频自动流的最简单流程 full flow quality sample

- `已确认` 本轮目标为 `full_flow_quality_sample`，不是 PR #43 短样片。
- `已确认` 不设置 90-150 秒目标，不设置 180 秒上限。
- `已确认` 低于 600 秒必须判定失败。
- `已确认` runtime 使用用户最新 `FINAL_SCRIPT_V2`，默认不删句。
- `已确认` 火山引擎素材不安全时使用 API 信息卡 fallback。
- `已确认` 不把豆包方案写成工程跑通，不把 Trae 骨架写成 app 跑通。
- `已确认` 不把阿里云剪辑写成正式稳定，不把 Codex 检查写成内容过线。
- `已确认` `content_validation=pending_user_chatgpt_review`，`send_ready=false`。
