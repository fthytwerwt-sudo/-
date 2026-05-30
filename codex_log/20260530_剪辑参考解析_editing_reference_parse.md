# 20260530｜剪辑参考视频解析与 vNext 剪辑决策包草案

- `task_result.status = reference_analysis_completed_with_decode_warning`
- `target_delivery = editing_reference_contract + reference_style_parse_report + editing_decision_pack_vNext_draft`
- `source_folder = /Users/fan/Documents/视频工厂/素材录制/剪辑参考`
- `selected_reference_video = ScreenRecording_05-24-2026 21-12-50_1.MP4`
- `已确认` 本轮只做剪辑参考解析，不生成新正片、不修改当前正片、不调用视频 / 图片 / TTS / 外部付费 API，不读取 secret。
- `已确认` 已按 reference 任务生成 `reference_to_execution_contract（参考到执行契约）`、`reference_timeline_parse（参考时间线解析）`、`editing_style_parse_report（剪辑风格解析报告）` 和 `editing_decision_pack_vNext（下一版剪辑决策包草案）`。
- `已确认` 参考视频 `ffprobe` 可读：`416.740114s / 1180x2556 / HEVC / about 60fps / AAC stereo audio`。
- `部分成立` 参考视频可用于视觉机制分析：5 秒采样抽帧 `83` 张、scene-change 缩略图 `16` 张、人工关键帧 `17` 张，并生成 contact sheets。
- `待验证` 严格解码检查失败：ffmpeg 报告 `non monotonically increasing dts`；因此本轮不把该 MP4 写成技术干净的可交付媒体源，只作为 reference 分析素材。
- `已确认` 解析出的可迁移机制包括：`context_reset_card + evidence_card`、`split_screen_only_for_comparison`、`framed_screen_recording_evidence_card`、`one_claim_one_highlight_cluster`、`human_or_guide_bridge_between_dense_blocks`。
- `已确认` 不可迁移项包括：Douyin/TikTok 平台 UI、创作者身份/人脸、第三方素材、精确字体模板、过密贴纸、不可读的整页文档缩放。
- `repository_update_recommendation.should_update_repo_rules = false`：本轮只是一轮参考解析和草案，不直接改核心机制文件；待用户 / ChatGPT 审美确认后，再考虑写入 `codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md` 或 `GPT数据源/05_文案路由规则.md`。
- `DeepSeek`：本轮执行单禁止外部 API，因此只创建供料任务卡并标记 `deepseek_actual_participation = not_attempted_policy_constraint`、`fallback_status = fallback_local_only`、`not_deepseek_conclusion = true`。
- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未生成音频、未改素材、未改当前 review pack。
- `报告`：`codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/reference_editing_analysis_report.md`
- `manifest`：`codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/analysis_manifest.json`
- `contact_sheets`：
  - `codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/contact_sheet_5s.jpg`
  - `codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/keyframe_contact_sheet.jpg`

## 下一个目标

如果用户 / ChatGPT 认可本轮参考解析，下一轮只选一个 `30-45s` 的真实录屏中段，建立 `active_evidence_window（活跃证据窗口）`、`context_reset_card（上下文重置卡）` 和 `one_claim_one_highlight_cluster（一句一个主高亮）` 的最小片段验证；通过后再扩展 split-screen 或整段剪辑风格迁移。
