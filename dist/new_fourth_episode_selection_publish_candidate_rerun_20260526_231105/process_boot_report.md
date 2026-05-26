# process_boot_report

- `task_type`: `publish_candidate_generation_rerun`
- `prompt_delta`: 基于 v2 证据复核继续生成正片候选，不重复阻断已解除素材 blocker。
- `locked_copy_source`: previous `locked_copy_contract.json`
- `tts_route`: MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd` only
- `forbidden`: 改文案、旧 v0.2、旧 Qwen/B 语音、fallback、无声视频、技术预览。
- `must_block_if`: MiniMax 不可用、音频静音、媒体生成失败、预检失败、Git 同步失败。
