# 20260503｜短视频自动流正式参考质量完整片

## 任务结果

- `result_status`：`full_reference_quality_video_completed_cloud_exported`
- `video_type`：`full_reference_quality_video`
- `technical_validation`：`passed`
- `content_precheck_for_reference_quality`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`

## 已确认

- 已继续使用 PR #46 分支：`codex/short-video-auto-flow-formal-full-reference-video-20260503`。
- 已复用完整 case：`cases/短视频自动流最简单流程_full_reference_quality_video.md`。
- 已复用用户确认完整 `FINAL_SCRIPT_V2`，未压缩文案，未复用 PR #43 145 秒稿。
- 已复用项目正式 TTS 重提音轨：`tts_retry_20260503_attempt2/tts/formal_voiceover.mp3`。
- 已将本地正式 TTS 音轨接入正式 generation，跳过远程 voiceover 重复读取。
- 已将 v3.1 元素娃娃主持壳按 `opening_reference_element_doll_no_text_locked_20260428` 做 locked reference inheritance。
- 已确认 liveportrait / portrait quota 不再作为元素娃娃主持壳 blocker。
- 已通过本地 renderer / reference inheritance 完成卡片和主持壳视觉资产；本轮未新增 PDF / 图片 API 生成需求。
- 已将中段录屏从静态 `cover` 修正为 `middle_reference_zoom*` 动态 `crop_x` 证据窗口，并从云剪导出后的 `full_video.mp4` 重抽帧复核通过。
- 已复核总结卡 / 即梦对比卡：`seg15`、`seg16` 均走 `cute_info_card_route`，只做边界说明和总结辅助。
- 已读取骚萌卡唯一参考 `PR7_B_骚萌反应页.png`；本片未使用独立骚萌反应页，未回退 PR #7 A，未误写骚萌卡已入片。
- 已复核 HyperFrames 边界：本片未启用，未进入中段录屏，未替代真实素材证据，未替代云剪。
- 已执行 `scripts/generate_formal_api_demo.py`，generation 成功。
- 已执行 `scripts/assemble_formal_api_demo.py`，OSS + ICE / 云剪 cloud-only assembly 成功。
- 已生成并本地下载：`full_video.mp4`。
- 已用 ffprobe / 解码检查验证：1080x1920，H.264，AAC，742.849 秒，可解码。
- 未使用 macOS `say`。
- 未使用 local assembly fallback。
- 未修改 `dist/latest_review_pack/`。
- 未修改当前 v3.1 publish target。

## 产物路径

- 输出目录：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video`
- `full_video.mp4`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/full_video.mp4`
- `manifest.json`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/manifest.json`
- `runtime_full_script.md`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/runtime_full_script.md`
- `cloud_assembly_report.md`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/cloud_assembly_report.md`
- `render_report.md`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/render_report.md`
- `middle_zoom_contact_sheet.jpg`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/middle_zoom_contact_sheet.jpg`
- `card_route_contact_sheet.jpg`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/card_route_contact_sheet.jpg`
- `视觉机制完整复核报告_visual_mechanism_full_check_report.md`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/视觉机制完整复核报告_visual_mechanism_full_check_report.md`

## 保留边界

- `content_validation` 仍为 `pending_user_chatgpt_review`。
- `send_ready` 仍为 `false`。
- 本轮技术完成不等于内容最终过线。
- 大媒体文件、原始素材、TTS 音频和云剪导出 MP4 不提交进 Git。

## 20260504 本地回炉修正版

- `result_status`：`local_reference_fix_completed`
- `video_type`：`local_reference_quality_fix`
- `technical_validation`：`passed`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `assembly_mode`：`local_reference_quality_fix`
- `cloud_assembly_used`：`false`
- `local_assembly_used`：`true`
- `macos_say_used`：`false`

`已确认` 用户指出云剪版存在中段左右晃、总结卡未用 HyperFrames、TTS 不符合 v3.1 参考等问题后，本轮按用户最新口径生成本地参考修正版，不继续走阿里云剪辑 / ICE / OSS。

`已确认` 已重新尝试阿里 `qwen3-tts-vc-realtime-2026-01-15`。原参考声音 `qwen-t...ac19` 直连异常后，已从 `语音样本 2.MP4` 复刻出同一参考底子的可用声音 `qwen-t...af51`，并按 B 版停顿梗感策略生成完整音轨。声音最终听感仍待用户 / ChatGPT 复审。

`已确认` 开头元素娃娃只保留约 2 秒“大家好”；后续元素娃娃画面已移除。原元素娃娃段按适配度改由骚萌卡、用户录制素材、稳定录屏或信息卡承载；骚萌卡已按 PR #7 B route 复核，不使用 PR #7 A，不硬塞不贴文案的卡。

`已确认` 中段已移除周期性 `crop_x` 左右晃，改为固定证据窗口；总结卡已接入 HyperFrames `card_motion_layer`；新增素材 `阿里云剪辑.mp4` 已用于 `seg12` 本地装配说明段。

- 本地修正版目录：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality`
- `full_video_local_fix.mp4`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/full_video_local_fix.mp4`
- `render_summary_local_fix.json`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/render_summary_local_fix.json`
- `sassy_card_contact_sheet.jpg`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/sassy_card_contact_sheet.jpg`
- `summary_card_hyperframes_contact_sheet.jpg`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/summary_card_hyperframes_contact_sheet.jpg`
- `captions_local_fix.srt`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/captions_local_fix.srt`

`部分成立` 字幕已生成并对齐为独立 SRT；本机 ffmpeg 缺少 `subtitles` filter，本轮未把字幕烧录进 MP4。

## 下一个目标

用户 / ChatGPT 对 `full_video_local_fix.mp4` 做声音、节奏和画面适配复审，并决定是否作为新的内容候选继续只改一个变量。

## 2026-05-04 local_reference_quality_fix_v2

- 本轮按用户要求不继续云剪，输出本地参考修正版 v2。
- 中段重剪、画布对齐、骚萌卡、HyperFrames 总结卡和 v3.1 TTS 均有独立证据报告。
- `content_validation = pending_user_chatgpt_review`，`send_ready = false`。
- `full_video_local_fix_v2`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality_v2/full_video_local_fix_v2.mp4`
