# review_manifest｜新第四期选品初筛发布候选阻断包

## 结论
- status: `blocked_publish_candidate_unavailable_remote_tts_authorization_missing`
- publish_candidate_ready_for_human_review: `false`
- content_validation: `not_advanced_due_blocked`
- send_ready: `false`

## 已完成检查
- locked copy source checked: `locked_by_user_and_chatgpt_via_current_prompt`
- preflight dir exists: `/Users/fan/Documents/视频工厂/codex_log/script_preflight/新第四期_选品初筛_20260524_231118`
- script_to_timeline_map JSON parse: `passed`
- content_route_card_v2 JSON parse: `passed`
- tts_prosody_anchor_map JSON parse: `passed`
- material dir exists: `/Users/fan/Documents/视频工厂/素材录制/新第四期`
- V001/V003/V004/V002 metadata probe: `passed`

## 阻断证据
- `DASHSCOPE_API_KEY_present = false`
- `ALIYUN_API_KEY_present = false`
- `authorized_runtime_config_exists = true`
- `authorized_runtime_config_read = false`，原因是本轮禁止读取 / 打印 / 写入 secret。
- 正式项目 TTS 不能降级为 macOS say、无声或本地低质 fallback。

## 为什么不能交 publish candidate
发布候选片必须包含 `narration.wav`、音轨、字幕、完整 `full.mp4` 与验证通过的审片包。本轮缺正式 TTS 授权，因此不能生成正式音轨；继续生成视频只会变成无声或降级技术预览，违反执行单。

## 下一步安全动作
将正式 TTS 授权以 process environment 注入当前执行进程，例如只暴露变量名可用、值不打印不落盘；然后重跑本执行单。不要要求 Codex 读取本地 secret 文件。
