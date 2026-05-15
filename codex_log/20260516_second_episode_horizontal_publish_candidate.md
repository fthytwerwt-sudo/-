# 20260516 第二期横屏发布候选片

## 本轮结论

- `已确认` 本轮根据用户最新拍板，将正式运营默认出片比例修正为 `horizontal_16_9（横屏 16:9）` / `1920x1080`。
- `已确认` 本轮生成结果为 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`，不是 `technical_preview（技术预览）`。
- `已确认` 本轮未生成竖屏视频、无声视频、1280x720 技术包或 JSON / Markdown-only 交付。

## 输出目录

- `publish_candidate_dir`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/`
- `main_video`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/第二期_KPI到判断系统_horizontal_publish_candidate_v1.mp4`
- `voice_track`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/voice_track.wav`
- `subtitle_ass`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/subtitle.ass`
- `subtitle_srt`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/subtitle.srt`
- `review_manifest`：`dist/第二期KPI到判断系统发布候选横屏_second_episode_kpi_to_judgment_system_horizontal_publish_candidate/review_manifest.md`

## 源素材比例核验

### video_1

- `path`：`/Users/fan/Documents/视频工厂/素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4`
- `width`：`3338`
- `height`：`1644`
- `calculated_ratio`：`2.0304`
- `display_aspect_ratio`：`not_reported_by_ffprobe`
- `sample_aspect_ratio`：`not_reported_by_ffprobe`
- `rotation`：`none`
- `orientation`：`horizontal_widescreen`

### video_2

- `path`：`/Users/fan/Documents/视频工厂/素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4`
- `width`：`3248`
- `height`：`1626`
- `calculated_ratio`：`1.9975`
- `display_aspect_ratio`：`not_reported_by_ffprobe`
- `sample_aspect_ratio`：`not_reported_by_ffprobe`
- `rotation`：`none`
- `orientation`：`horizontal_widescreen`

## 最终媒体核验

- `width`：`1920`
- `height`：`1080`
- `display_aspect_ratio`：`16:9`
- `sample_aspect_ratio`：`1:1`
- `rotation`：`none`
- `fps`：`30/1`
- `duration`：`81.800000s`
- `audio_present`：`true`
- `audio_codec`：`aac`
- `audio_sample_rate`：`48000`
- `audio_channels`：`1`
- `audio_duration`：`81.920000s`
- `subtitle_stream`：`mov_text / chi`
- `sidecar_subtitles`：`subtitle.ass`、`subtitle.srt`
- `can_decode`：`true`

## TTS / 声音链路

- `provider`：`aliyun_bailian`
- `api_route_family`：`aliyun_qwen_realtime_websocket_voice_clone`
- `model`：`qwen3-tts-vc-realtime-2026-01-15`
- `voice`：`qwen-t...ac19（脱敏）`
- `local_say_fallback_used`：`false`
- `api_key_printed`：`false`
- `api_key_written`：`false`
- `voice_validation`：`pending_human_review`

## 内容与数据目标边界

- `topic`：别再让 AI 给你 KPI 了，它真正该帮你判断下一步改哪。
- `primary_variable`：`opening_route_or_first_5s_packaging`
- `supporting_variables`：`evidence_compression`、`result_diff_display`
- `formal_data_driven_execution_ready`：`false`
- `data_goal_not_claimed_as_real_flywheel_passed`：`true`
- `v003_review_claimed_complete`：`false`

## 未推进状态

- `content_validation`：`pending_human_review` / 未写 `passed`
- `send_ready`：`false`
- `publish_status_success`：`not_advanced`
- `voice_validation`：`pending_human_review`
- `final_voice_validated`：`false`
- `visual_master_locked`：`false`

## 下一个目标

ChatGPT / 用户复审 horizontal 16:9 publish candidate，判断是否能进入 `send_ready` 或需要局部回炉。
