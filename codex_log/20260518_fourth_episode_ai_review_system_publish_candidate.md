# 20260518｜第四期 AI 短视频复盘系统发布候选片生成记录

## 0. 本轮 TTS 授权修复后完成记录

```yaml
status: publish_candidate_ready_for_human_review
previous_blocked_commit: a06ef14
previous_blocked_reason: remote_tts_authorization_unavailable_under_secret_read_ban
tts_auth_source: authorized_runtime_config
api_key_printed: false
api_key_written: false
secret_file_staged: false
local_tts_fallback_used: false
macos_say_used: false
silent_video_generated: false
technical_preview_as_delivery: false
```

本轮用户明确授权 Codex 为阿里 / 百炼远程 TTS 读取项目既有 runtime config 中的 `auth.api_key` 字段。Codex 只将授权来源记录为 `authorized_runtime_config`，未把 key 值写入任何 JSON、Markdown、debug 文件、prompt、日志或 Git 暂存内容。

## 0.1 route_decision

```yaml
project_route: video_factory
task_type:
  - video_sample_or_assembly
  - publish_candidate_delivery
  - TTS_authorization_unblock
  - project_file_change
responsibility_layer:
  - execution_layer
  - validation_layer
  - sync_layer
current_project_state:
  - formal_operation_active
  - publish_candidate_requested
  - remote_tts_authorized_for_this_turn
execution_permission: conditional_execute_after_tts_auth_check -> executed
large_task_gate:
  triggered: true
  reason: "本轮同时命中完整成片、远程 TTS、字幕、卡片、素材证据、审片包、平台风险、隐私风险和多文件验证。"
lane_recommendation: "audit_lane -> standard_lane"
parallel_recommendation: serial_only
write_owner: "Codex Integrator only"
not_allowed:
  - "本地 TTS fallback"
  - "macOS say"
  - "无声视频"
  - "技术预览冒充发布候选片"
  - "打印 / 写入 / 提交 API key"
  - "推进 content_validation / send_ready / current_data_goal_anchor ready / visual_master_locked / voice_validation"
```

## 0.2 state_action_router

```yaml
input_signal: "用户明确授权阿里 / 百炼远程 TTS，要求继续生成第四期完整发布候选正片。"
current_project_state:
  formal_operation: formal_operation_active
  requested_delivery: publish_candidate_ready_for_human_review
  data_goal_anchor_status: partial_data_recorded / not_ready
fact_source_arbitration:
  primary_source:
    - "用户当轮 TTS 授权与 locked copy contract"
    - "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md"
    - "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_index.json"
    - "codex_source/00_codex_readme.md"
    - "codex_source/01_execution_rules.md"
  secondary_sources:
    - "codex_log/latest.md"
    - "skills/视频素材解析_video_material_audit/SKILL.md"
    - "codex_source/19_project_state_action_router.md"
conflict_detected: true
conflict_resolution: "本轮只授权 TTS 所需 key；不读取无关 secret，不推进 send_ready 或 content_validation passed。"
inferred_state: remote_tts_authorization_check_required_before_video_assembly
confidence: high
selected_action: "使用授权远程 TTS 生成 narration.wav，并继续完成 full.mp4 / subtitles / cards / review pack / validation。"
forbidden_action:
  - "local_tts_fallback"
  - "macOS say"
  - "silent preview"
  - "technical preview as delivery"
  - "secret value logging"
```

## 0.3 tts_auth_check

```yaml
DASHSCOPE_API_KEY_present: false
ALIYUN_API_KEY_present: false
authorized_runtime_config_checked: true
authorized_runtime_config_exists: true
authorized_runtime_config_in_repo: false
tts_auth_available: true
tts_auth_source: authorized_runtime_config
key_printed: false
key_written: false
secret_file_staged: false
```

## 0.4 full_video_output

```yaml
output_dir: "dist/fourth_episode_ai_review_system_publish_candidate/"
full_mp4: "dist/fourth_episode_ai_review_system_publish_candidate/full.mp4"
narration_wav: "dist/fourth_episode_ai_review_system_publish_candidate/narration.wav"
captions_srt: "dist/fourth_episode_ai_review_system_publish_candidate/captions.srt"
duration_seconds: 174.3
resolution: "1920x1080"
aspect_ratio: "16:9"
video_codec: h264
audio_codec: aac
subtitle_codec: mov_text
can_decode: true
```

## 0.5 material_usage

```yaml
skill_used: "skills/视频素材解析_video_material_audit/SKILL.md"
opening_evidence: "material_04 00:55-01:50"
middle_evidence: "material_02 00:20-01:50"
ending_support: "material_01 01:04-01:28 + material_04 01:30-01:50"
forbidden_default_segment: "material_03 00:30-00:55"
privacy_mitigation: "source recording clips use top and left masks; material_03 high-risk segment not used"
```

## 0.6 files_created

- `dist/fourth_episode_ai_review_system_publish_candidate/full.mp4`
- `dist/fourth_episode_ai_review_system_publish_candidate/captions.srt`
- `dist/fourth_episode_ai_review_system_publish_candidate/narration.wav`
- `dist/fourth_episode_ai_review_system_publish_candidate/review_manifest.md`
- `dist/fourth_episode_ai_review_system_publish_candidate/summary.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/media_probe.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/locked_copy_contract.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/content_route_card_v2.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/script_function_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/evidence_anchor_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/visual_anchor_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/tts_prosody_anchor_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/card_anchor_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/forbidden_visual_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/script_to_timeline_map.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/subtitle_card_overlap_check.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/publish_candidate_checklist.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/platform_risk_precheck.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/privacy_risk_check.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/narration_tts_debug_sanitized.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/secret_leak_scan_sanitized.json`
- `dist/fourth_episode_ai_review_system_publish_candidate/cover_frame.png`
- `dist/fourth_episode_ai_review_system_publish_candidate/mid_evidence_frame.png`
- `dist/fourth_episode_ai_review_system_publish_candidate/validation_contact_sheet.jpg`
- `scripts/生成第四期AI复盘系统发布候选片_generate_fourth_episode_ai_review_system_publish_candidate.py`

## 0.7 verification_result

```yaml
json_parse: passed
py_compile: passed
ffprobe_full_mp4: passed
ffmpeg_decode_full_mp4: passed
resolution_check: passed_1920x1080
aspect_ratio_check: passed_16_9
audio_stream_check: passed
subtitle_stream_check: passed
narration_volume_check: "mean_volume=-16.1 dB; max_volume=-1.0 dB"
subtitle_card_overlap_check: passed
platform_risk_precheck: passed_low_risk_with_notes
privacy_risk_check: passed_or_masked
secret_leak_scan_sanitized: passed
source_videos_staged: false
```

## 0.8 status_boundary

```yaml
publish_candidate_ready_for_human_review: true
technical_validation: passed
audio_validation: passed
subtitle_validation: passed
line_level_visual_alignment: passed
content_validation: pending_user_chatgpt_review
send_ready: false
current_data_goal_anchor_ready: false
visual_master_locked: false
voice_validation: pending
next_formal_video_execution_prompt_generated: false
dist_latest_review_pack_updated: false
```

---

# 上一轮阻断记录

## 1. route_decision

```yaml
project_route: video_factory
task_type:
  - video_sample_or_assembly
  - project_file_change
  - review_diagnosis_audit
responsibility_layer:
  - project_judgment_layer
  - execution_layer
  - validation_layer
  - sync_layer
current_project_state:
  - formal_operation_active
  - publish_candidate_requested
  - current_data_goal_anchor_not_ready
execution_permission: blocked_publish_candidate_unavailable_before_video_generation
large_task_gate:
  triggered: true
  reason: "本轮同时命中完整成片、TTS、字幕、卡片、素材证据、审片包、平台风险、隐私风险和多文件验证。"
lane_recommendation: "audit_lane -> blocked"
parallel_recommendation: serial_only
write_owner: "Codex Integrator only"
deepseek_supply_gate:
  supply_request: "codex_log/supply_requests/20260518_fourth_episode_publish_candidate_pre_supply_request.json"
  fallback_status: fallback_local_only
  not_deepseek_conclusion: true
  reason: "当前进程无 DEEPSEEK_API_KEY，且本轮不读取 secret。"
not_allowed:
  - "读取 .env / API key / token / secret"
  - "调用未授权外部 API"
  - "使用本地 TTS fallback 或 macOS say"
  - "生成无声视频或技术预览冒充发布候选片"
  - "推进 content_validation / send_ready / current_data_goal_anchor ready / visual_master_locked / voice_validation"
```

## 2. state_action_router

```yaml
input_signal: "用户要求基于第四期素材审计直接生成 1920x1080 横屏发布候选正片。"
current_project_state:
  formal_operation: formal_operation_active
  requested_delivery: publish_candidate_ready_for_human_review
  data_goal_anchor_status: partial_data_recorded / not_ready
fact_source_arbitration:
  primary_source:
    - "用户当轮 locked copy contract"
    - "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md"
    - "codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_index.json"
    - "codex_source/00_codex_readme.md"
    - "GPT数据源/05_文案路由规则.md"
  secondary_sources:
    - "codex_log/current_operation_target.md"
    - "codex_log/current_data_goal_anchor.md"
    - "review_loop/operation_records_index.md"
    - "review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md"
    - "codex_source/08_tts_style_execution_rules.md"
  conflict_detected: true
  conflict_resolution: "用户当轮显式发布候选片目标可作为一次执行尝试，但不得推进 current_data_goal_anchor ready；若远程 TTS 不满足，则必须 blocked。"
inferred_state: publish_candidate_requested_but_remote_tts_authorization_unavailable_under_secret_read_ban
confidence: high
selected_action: "记录 blocked_publish_candidate_unavailable，不生成降级视频。"
forbidden_action:
  - "读取本地 TTS runtime config 中的 auth.api_key"
  - "使用本地 TTS 或 macOS say"
  - "生成 silent preview / technical preview / route card only 冒充完成"
```

## 3. skill_used

- `skills/视频素材解析_video_material_audit/SKILL.md`
- 使用方式：复核第四期素材审计报告与素材索引中的证据窗口、平台风险、隐私风险和素材禁用边界。
- 边界：该 skill 不推进 `publish_candidate`，本轮只引用其素材证据判断。

## 4. impact_check_result

```yaml
git_status_before: "clean; main...origin/main"
target_output_dir: "dist/fourth_episode_ai_review_system_publish_candidate/"
target_output_dir_exists_before: false
dist_latest_review_pack_overwrite: false
dist_latest_review_pack_status: "保留既有 v3.1 review pack，未覆盖。"
material_02_readable: true
material_04_readable: true
material_02_decode_probe: "ffprobe passed; ffmpeg 2s decode sample passed"
material_04_decode_probe: "ffprobe passed; ffmpeg 2s decode sample passed"
source_material_audio: "全部第四期素材均无音轨，需要另行生成口播音轨。"
remote_tts_process_env:
  DASHSCOPE_API_KEY_present: false
  ALIYUN_API_KEY_present: false
  ALIBABA_CLOUD_ACCESS_KEY_ID_present: false
  ALIBABA_CLOUD_ACCESS_KEY_SECRET_present: false
formal_runtime_config_exists: true
formal_runtime_config_read: false
why_not_read: "该配置承载 auth.api_key；用户本轮禁止读取 API key / token / secret。"
hyperframes_runtime_needed: true
hyperframes_runtime_used: false
why_hyperframes_not_used: "远程 TTS 已先行阻断，未进入卡片动效与视频装配阶段。"
```

## 5. material_usage_plan

```yaml
opening_evidence: "material_04 00:55-01:30"
middle_evidence: "material_02 00:20-01:50"
ending_support: "material_01 01:04-01:28 or material_04 01:30-01:50"
forbidden_default_segment: "material_03 00:30-00:55"
privacy_boundary: "material_03 未打码默认不用；material_02 / material_04 使用前仍需裁切浏览器侧栏和路径信息。"
platform_boundary: "弱化 全自动 / 自动流 / 一键复制 / 直接拿去用 / Trae 直接做出来。"
```

## 6. blocked_reason

`blocked_publish_candidate_unavailable`

本轮不能合法生成 `publish_candidate_ready_for_human_review`，直接原因是：

1. 当前进程没有可用远程 TTS 授权环境变量：`DASHSCOPE_API_KEY_present = false`、`ALIYUN_API_KEY_present = false`。
2. 仓库既有远程 TTS 脚本依赖 `/Users/fan/.config/video-factory/formal_api_demo.local.toml` 读取 `auth.api_key`。
3. 用户本轮明确禁止读取 `.env / API key / token / secret`。
4. 用户同时禁止本地 TTS fallback、`macOS say`、无声视频和技术预览。

因此，`narration.wav（口播音轨）` 无法在本轮合规生成；缺口播音轨即命中发布候选片硬阻断。

## 7. what_was_completed

- 已读取本轮必须文件中的核心入口、运营锚点、文案规则、价值规则、平台风险规则、第四期素材索引和第四期素材审计报告。
- 已读取 `skills/视频素材解析_video_material_audit/SKILL.md` 并按其中素材证据边界复核素材使用计划。
- 已确认第四期素材目录与关键素材仍可读：
  - `material_02`: `122.800000s`，`2872x1646`，H.264，30fps，无音轨，ffprobe passed，2 秒解码抽样 passed。
  - `material_04`: `114.200000s`，`2906x1646`，H.264，30fps，无音轨，ffprobe passed，2 秒解码抽样 passed。
- 已确认目标输出目录此前不存在。
- 已确认 `dist/latest_review_pack/` 未覆盖。
- 已确认本轮不能读取本地 TTS secret，且当前进程没有远程 TTS key。

## 8. what_was_not_completed

- 未创建 `dist/fourth_episode_ai_review_system_publish_candidate/`。
- 未生成 `full.mp4`。
- 未生成 `narration.wav`。
- 未生成 `captions.srt`。
- 未生成卡片、字幕、审片包或 `publish_candidate_checklist.json`。
- 未生成 `content_route_card_v2.json`、`script_to_timeline_map.json` 等执行前锚点文件作为完成替代物。
- 未更新 `dist/latest_review_pack/` 指针。
- 未推进任何发布、内容、声音或数据目标状态。

## 9. why_no_degrade_allowed

用户本轮明确锁定：

- 不能交 `internal_review_candidate`
- 不能交 `technical_preview`
- 不能交无声视频
- 不能交无字幕视频
- 不能交 720p 临时视频
- 不能只交 JSON / Markdown / route card
- 不能用本地 TTS 或 `macOS say`

仓库正式运营规则也要求视频交付只能是：

1. `publish_candidate_ready_for_human_review`
2. `blocked_publish_candidate_unavailable`

缺远程口播音轨时，唯一合规结果是 `blocked_publish_candidate_unavailable`。

## 10. status_boundary

```yaml
publish_candidate_ready_for_human_review: false
technical_validation: not_run_for_full_video
audio_validation: blocked_no_remote_tts
subtitle_validation: not_generated
line_level_visual_alignment: not_generated
subtitle_card_overlap_check: not_generated
platform_risk_precheck: not_generated_for_video
privacy_risk_check: not_generated_for_video
review_pack_generated: false
content_validation: pending_user_chatgpt_review_not_advanced
send_ready: false
current_data_goal_anchor_ready: false
visual_master_locked: false
voice_validation: pending_not_advanced
source_media_committed: false
dist_latest_review_pack_updated: false
```

## 11. safe_next_action

在不违反 secret 边界的前提下，下一步只有两个安全选项：

1. 用户在当前 Codex 进程中注入已授权的远程 TTS 环境变量，并明确允许本轮只由子进程使用，不打印、不写入、不提交 key。
2. 用户改任务目标为只做执行前包或人工配音装配，但这将不是本轮要求的 `publish_candidate_ready_for_human_review`，必须作为新授权任务处理。
