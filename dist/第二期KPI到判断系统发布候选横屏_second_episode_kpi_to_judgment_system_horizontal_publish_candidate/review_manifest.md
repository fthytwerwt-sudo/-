# review_manifest

status: `publish_candidate_ready_for_human_review`
content_validation: `pending_human_review`
send_ready: `false`

## 主视频

- path: `dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/第二期_KPI到判断系统_horizontal_publish_candidate_v1.mp4`
- resolution: `1920x1080`
- display_aspect_ratio: `16:9`
- sample_aspect_ratio: `1:1`
- fps: `30/1`
- audio_codec: `aac`
- audio_duration: `81.920000`
- subtitles: `embedded mov_text + subtitle.ass / subtitle.srt sidecar`

## 交付边界

- `publish_candidate != send_ready`
- `publish_candidate != content_validation passed`
- `voice_validation` 未推进；本轮只确认阿里 / 百炼 TTS 音轨已生成、可解码、可供人审。
- `visual_master_locked` 未推进。
- 不写 V003 已完成 72h / 7d 复盘。
- 不写数据飞轮已跑通。

## 人审重点

1. 开头 0-5 秒是否足够直接。
2. 阿里 / 百炼 TTS 音轨是否达到发布候选听感最低线。
3. 中段表格卡片是否足够清楚。
4. 是否需要补录完整 `video_goal_card / post_publish_review_card` 后再升级。
