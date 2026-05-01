# 20260430 v3.1 visual route fix generation

## 本轮目标

- 修复 v3 卡片 visual routing 没有拆开的问题。
- 生成 v3.1 完整候选片和独立复审包。

## 执行前已确认事实

- PR #7 B 是本轮骚萌卡执行参考，但仍是 candidate。
- 信息卡不再走深蓝科技 UI，改为粉色樱花柔和展示牌皮肤 + 清晰结构。
- v3 缺少反面 / 正面展示提示卡，本轮补回。
- `content_validation`、`send_ready`、`voice_validation`、`visual_master_locked` 均不得升级。

## 实际读取

- `AGENTS.md`、全局相关 skills、`codex_source/*` 执行规则、locked reference registry、当前 v3 review pack、v3 生成脚本。
- `origin/codex/sassy-card-reference-review-20260430` 中的 PR7_B 图片和样本索引。
- `origin/codex/cute-card-reference-audit-20260430` 中的可爱卡片视觉判断与 round34 提示卡图片。

## 实际改动

- 新增 v3.1 生成脚本。
- 新增 PR7_B candidate reference registry 条目。
- 新增 v3.1 dist 与复审包，并更新 `dist/latest_review_pack/`。
- 更新 current publish target、轻量证据和本地产物路径索引。

## 当前结果

- `preview_type`: `finished_quality_candidate_v31`
- `visual_master_candidate`: `true`
- `visual_master_locked`: `false`
- `content_validation`: `pending_user_chatgpt_review`
- `send_ready`: `false`
- `subtitle_enabled`: `false`
- `voice_validation`: `pending_user_chatgpt_review`
- `final_voice_validated`: `false`
- `sassy_card_execution_reference`: `PR7_B_骚萌反应页.png`
- `sassy_card_reference_locked`: `false`

## 产物

- full video: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4`
- review manifest: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_review_manifest.md`
- summary: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_summary.json`
- timeline: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_timeline.json`
- cut map: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_cut_map.md`
- contact sheet: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_contact_sheet.jpg`
- visual route map: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/visual_route_map.json`
- visual route validation: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/visual_route_validation_report.json`
- locked reference inheritance report: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/locked_reference_inheritance_report.md`
- video metadata probe report: `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/video_metadata_probe_report.json`

## 验证

- duration_seconds: `149.993`
- resolution: `720x1280`
- fps: `25.0`
- video_codec: `h264`
- audio_codec: `aac`
- audio_channels: `1`
- decodable: `True`
- audio_non_silent: `True`
- subtitle_stream_count: `0`

## 下一步建议

- 用户 / ChatGPT 复审 v3.1 的内容、声音听感与视觉母版方向；复审前不得写可发送或 locked。
