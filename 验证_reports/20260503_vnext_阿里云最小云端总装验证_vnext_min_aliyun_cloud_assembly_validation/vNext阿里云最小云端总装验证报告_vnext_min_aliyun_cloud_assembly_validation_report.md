# vNext 阿里云最小云端总装验证报告

## 1. 当前结论

- `状态`：已确认。
- `验证性质`：technical_validation only。
- `结论`：阿里云 OSS + ICE / 云剪不仅能跑通 12 秒最小链路，也能接住更接近《视频工厂》vNext 方向的 24 秒三段最小样片结构。
- `vNext 候选判断`：可以作为 vNext 云端总装候选继续评估。
- `边界`：本轮不是内容验收，不代表正式链路已稳定，不代表 v3.1 正片改用阿里云剪辑。

## 2. PR #36 合并状态

- `已确认` PR #36「验证阿里云剪辑复接 after audit」已合并到 `codex/user-readable-map`。
- `merge_commit`：`dddad679b8cc5fd9503a6a3be05ff612b6207c7e`
- `当前分支`：`codex/vnext-min-cloud-assembly-validation-20260503`
- `分支基线`：从 PR #36 合并后的最新 `codex/user-readable-map` 创建。

## 3. 已读取文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation.md`
- `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/阿里云剪辑复接验证报告_after_audit_aliyun_editing_reconnect_validation_report.md`
- `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/run_summary.json`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_timeline.json`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`
- `formal_api_demo_cloud_assembly.py`
- `formal_api_demo_core.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `codex_log/current_local_artifact_paths.md`

## 4. 配置检查

- `OSS 配置`：已确认存在，assembly gate 通过。
- `ICE / IMS 配置`：已确认存在，assembly gate 通过。
- `缺失项`：0。
- `敏感凭据`：只在本地读取使用，未写入报告、日志、路径索引或 Git。

## 5. 素材选择

| 类型 | 本轮使用路径 | 来源 / 选择原因 |
| --- | --- | --- |
| 用户录制素材段 | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/clips/04_shot02_negative_input.mp4` | 来自 v3.1 timeline 的 `shot02_negative_input`；原始 `source_path` 为 `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4`，本轮使用已切好的 9:16 H.264 片段，避免修改或上传完整原始素材。 |
| 卡片段 A | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/cards/shot15_result_diff_card.png` | 结果差卡，归属 `cute_info_card_route`，对应当前 vNext 数据卡 / 结果差卡验证目标。 |
| 卡片段 B | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/cards/shot16_low_pressure_ending.png` | Prompt 引用尾卡，归属 `cute_info_card_route`，对应低压收束卡验证目标。 |
| 音轨 | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/tts/voiceover_v31_custom_voice_ac19.wav` | 既有 v3.1 TTS，全长约 149.99 秒，本轮仅作为 24 秒技术验证音轨来源，不重新生成声音。 |
| 字幕输入 | `dist/formal_api_demo/captions.srt` | assembly 入口需要字幕文件；本轮仅作为技术验证输入，不作为内容样片判断依据。 |

## 6. Timeline

- `0-8s`：用户录制素材段。
- `8-16s`：结果差卡片段。
- `16-24s`：Prompt 尾卡片段。
- `总时长`：24 秒。
- `目标比例`：9:16。

## 7. 阿里云执行结果

- `真实 API 调用`：已确认。
- `OSS 上传`：已确认，上传对象数量 6。
- `ICE / 云剪任务提交`：已确认。
- `ICE 轮询`：已确认。
- `请求链`：`ListEditingProjects`、`UpdateEditingProject`、`SubmitMediaProducingJob`、`GetMediaProducingJob`。
- `云端导出 MP4`：已确认。

输出：

- `OSS 输出路径`：`oss://zvip1-video-beijing/video-factory/final/20260502T192857Z/formal_api_demo.mp4`
- `本地下载验证路径`：`/Users/fan/Documents/视频工厂/dist/验证样片_validation_samples/20260503_vnext_阿里云最小云端总装验证_vnext_min_aliyun_cloud_assembly_validation/vnext_min_cloud_assembly_validation.mp4`
- `说明`：OSS 裸 HTTPS 对象为私有读；本轮只在本地忽略目录生成短期签名链接用于下载验证，签名链接未写入报告或 Git。

## 8. ffprobe 验证

- `ffprobe`：通过。
- `duration`：24.000000 秒。
- `resolution`：1080x1920。
- `video_codec`：H.264。
- `audio_codec`：AAC。
- `file_size`：952097 bytes。

## 9. vNext 候选判断

- `状态`：已确认。
- `是否可作为 vNext 云端总装候选`：可以作为候选。
- `为什么`：本轮已经验证更接近真实生产的三类素材结构：用户录制素材段 + 卡片素材段 + 既有音轨，能由 OSS + ICE / 云剪完成云端总装并导出可解码 MP4。
- `仍需验证`：
  - 完整 vNext timeline 的 10+ 段素材兼容性。
  - 多段真实录屏与卡片动效混排时的裁剪 / 适配策略。
  - 使用 HyperFrames 卡片动效版时的格式与时长兼容性。
  - OSS 私有读下的分发、下载和复审包策略。
  - 是否需要为 vNext 建立独立云剪工程。

## 10. 状态边界

- 未修改 v3.1 正片。
- 未修改 `dist/latest_review_pack/` 既有产物。
- 未修改 `current_publish_target`。
- 未写新文案。
- 未处理 HyperFrames 中段录屏。
- 未把本轮写成正式稳定链路。
- 未将本地样片、原始运行结果、签名链接、视频、音频、图片或压缩包提交进 Git。
