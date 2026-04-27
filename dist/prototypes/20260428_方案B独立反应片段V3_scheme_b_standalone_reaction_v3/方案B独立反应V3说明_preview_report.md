# 方案 B 独立反应片段 V3 说明

## 本轮性质

- 本轮只是技术预览 / 生成链路验证，不代表方案 B 最终口径。
- 本轮不代表 `content_validation` 通过，不代表 `send_ready` 更新。
- 本轮不修改正式 `full.mp4`，不修改 `dist/latest_review_pack/`。

## 配置预检

- `actual_config_path`: `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `provider`: `aliyun_bailian`
- `region`: `cn-beijing`
- `auth_api_key`: `{'present': True, 'prefix_type': 'sk_dashscope_like', 'length_range': '20-39'}`

## 生成状态

- `status`: `technical_preview_generated`
- `blocked_reason`: ``
- `image_model`: `wan2.7-image-pro`
- `video_model`: `wan2.7-i2v`
- `image_task_id`: `81eaed8f-df33-45b3-8a7e-6aa0be456463`
- `image_request_id`: `80bc045d-0d87-9e32-97cc-eeb398cfe10d`
- `video_task_id`: `2e6c54e9-39f4-4bb8-9c9f-5f38bb6d8e42`
- `video_request_id`: `ea86281a-fa9f-9b37-8305-b0805ab97ebe`

## 输出

- `static_reaction_page`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_static_reaction_page.png`
- `raw_static_reaction_page`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_static_reaction_page_raw_from_wan.png`
- `reaction_clip`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_reaction_clip.mp4`
- `raw_reaction_clip`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_reaction_clip_raw_from_wan.mp4`
- `preview_video`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_scheme_b_standalone_reaction_v3.mp4`
- `contact_sheet`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_contact_sheet.jpg`
- `before_after_contact_sheet`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_before_after_contact_sheet.jpg`
- `attempts_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/wan_generation_attempts_sanitized.json`
- `image_generation_result_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/image_generation_result_sanitized.json`
- `official_config_preflight_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/official_config_preflight_sanitized.json`
- `prompts`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3_prompts.json`
- `preview_report`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3说明_preview_report.md`

## 技术验证

- `preview_duration`: `15.00s`
- `preview_resolution`: `720x1280`
- `reaction_clip_duration`: `1.52s`
- `reaction_clip_resolution`: `720x1280`
- `ffmpeg_decode_preview`: `passed`
- `ffmpeg_decode_reaction_clip`: `passed`
- `edit_structure`: `round34 录屏片段 A -> 独立 reaction clip -> round34 录屏片段 B`
- `not_overlay_compositing`: `true`
- `static_reaction_page_no_chest_AI`: `true`
- `preview_audio`: `silent_preview`

## 边界

- 未泄露 key。
- 未提交本地私有配置。
- 未本地绘图兜底。
- 未改正式正片。
- 未改 `send_ready`。
