# process_boot_report

- 本轮是正片候选生成任务，不是机制修补。
- 本轮 prompt 是增量目标，但仓库完整流程仍必须执行。
- 不能停在前置包；如果不能生成正片候选，必须输出 `blocked_publish_candidate_unavailable`。
- 不能交技术预览。
- 不能交内部诊断。
- 不能交旧稿。
- 不能交非 MiniMax 语音。
- 达不到正片候选就 blocked。
- 本轮实际判断：素材证据闸门和声音候选闸门未通过，禁止生成 `full.mp4` 冒充候选片。
