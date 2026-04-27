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

- `status`: `technical_preview_generated_content_pending`
- `blocked_reason`: ``
- `image_model`: `wan2.7-image-pro`
- `video_model`: `wan2.7-i2v`
- `candidate_A_task_id`: `0e572645-7897-412c-a82a-9fdf0dbd13e3`
- `candidate_A_request_id`: `fe31cbcb-a834-94b6-b52a-f4a8d17ab335`
- `candidate_B_task_id`: `1e0bb603-4978-48cc-8c29-358297faae0b`
- `candidate_B_request_id`: `eaa3dec2-b5dc-92de-91fc-76dd0912f6a0`
- `selected_candidate`: `A`
- `selection_reason`: `A 版挑眉 wink + 捂嘴偷笑更接近贱萌得瑟；B 版吐舌更强但略偏低幼 / 暧昧。`
- `sassy_video_task_id`: `00843322-0685-4eb2-a2ca-d9802ddc11b0`
- `sassy_video_request_id`: `bb5a7a91-d3f9-9588-8aa6-1c7cd10ab680`

## 输出

- `sassy_candidate_a`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page.png`
- `sassy_candidate_b`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌B_static_reaction_page.png`
- `sassy_candidate_contact_sheet`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg`
- `sassy_reaction_clip`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip.mp4`
- `sassy_raw_reaction_clip`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip_raw_from_wan.mp4`
- `sassy_preview_video`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_scheme_b_standalone_reaction_v3_sassy_cute.mp4`
- `sassy_contact_sheet`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_contact_sheet.jpg`
- `sassy_before_after_contact_sheet`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_before_after_contact_sheet.jpg`
- `sassy_candidates_result_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/sassy_expression_candidates_result_sanitized.json`
- `official_config_preflight_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/official_config_preflight_sanitized.json`
- `prompts`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3_prompts.json`
- `attempts_sanitized`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/wan_generation_attempts_sanitized.json`
- `preview_report`: `/private/tmp/视频工厂_scheme_b_v3_diagnostics/dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3说明_preview_report.md`

## 骚萌表情迭代说明

- 当前选中 A 版：挑眉、wink、捂嘴偷笑、得瑟手势。
- 相比上一版，已从 `崩溃 / 大哭 / 惊恐 / 抱头 / X 眼 / 旋涡眼 / 尖叫` 改为 `贱萌 / 得瑟 / 戏精 / 小坏笑 / GIF 感`。
- A 版基础检查：无胸口 `AI` 字样，无平台 UI，无版权角色，无性感擦边，画质仍为万相高质量 3D Q 版角色。
- B 版保留为候选参考，不进入 i2v；原因是吐舌更强，但整体更容易偏低幼 / 暧昧。
- 本轮仍是技术预览，表情是否足够“骚萌”、GIF 感是否到位，仍待用户 / ChatGPT 复审。

## 技术验证

- `preview_duration`: `15.00s`
- `preview_resolution`: `720x1280`
- `reaction_clip_duration`: `1.52s`
- `reaction_clip_resolution`: `720x1280`
- `ffmpeg_decode_preview`: `passed`
- `ffmpeg_decode_reaction_clip`: `passed`
- `edit_structure`: `round34 录屏片段 A -> 骚萌独立 reaction clip -> round34 录屏片段 B`
- `not_overlay_compositing`: `true`
- `preview_audio`: `silent_preview`

## 边界

- 未泄露 key。
- 未提交本地私有配置。
- 未本地绘图兜底。
- 未改正式正片。
- 未改 `send_ready`。
