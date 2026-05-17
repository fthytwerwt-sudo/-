# 第四期 AI 短视频复盘系统发布候选片审片包

- `status`: `publish_candidate_ready_for_human_review`
- `skill_used`: `skills/视频素材解析_video_material_audit/SKILL.md`
- `full_mp4`: `dist/fourth_episode_ai_review_system_publish_candidate/full.mp4`
- `narration_wav`: `dist/fourth_episode_ai_review_system_publish_candidate/narration.wav`
- `captions_srt`: `dist/fourth_episode_ai_review_system_publish_candidate/captions.srt`
- `resolution`: `1920x1080`
- `aspect_ratio`: `16:9`
- `audio_validation`: `passed`
- `subtitle_validation`: `passed`
- `platform_risk_precheck`: `passed_low_risk_with_notes`
- `privacy_risk_check`: `passed_or_masked`

## 使用素材

- 开头证据：`material_04 00:55-01:30`
- 中段主体证据：`material_02 00:20-01:50`
- 结尾辅助：`material_01 01:04-01:28` / `material_04 01:30-01:50`
- 默认禁用：`material_03 00:30-00:55`

## 状态边界

- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `current_data_goal_anchor_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending`
- 本轮未生成正式下一条视频执行 prompt。
- 本轮没有提交原始素材视频。
