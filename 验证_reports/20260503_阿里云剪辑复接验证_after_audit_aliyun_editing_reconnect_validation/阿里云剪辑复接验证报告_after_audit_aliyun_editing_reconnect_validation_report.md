# 阿里云剪辑复接验证报告 after audit

## 1. 当前结论

- `状态`：已确认。
- `结论`：阿里云 OSS + ICE / 云剪最小云端总装链路已完成一次真实复接验证。
- `适合接入 vNext`：可以作为 vNext 云端总装候选继续评估。
- `边界`：本轮只证明最小链路可跑通，不代表正式链路已稳定，不代表 v3.1 正片改用阿里云剪辑。

## 2. 前置顺序修复

- `已确认` PR #34 已合并到 `codex/user-readable-map`。
- `已确认` PR #34 合并提交：`edbe61e512c972d75c786a53f82c9e3db53ecfb2`。
- `已确认` PR #35 已关闭并标记 `Superseded`，未合并。
- `已确认` 本轮从合并 PR #34 后的最新 `codex/user-readable-map` 创建新分支：`codex/aliyun-editing-reconnect-validation-after-audit-20260503`。

## 3. 已读取文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/阿里云剪辑使用审计报告_aliyun_edit_usage_audit.md`
- `formal_api_demo_cloud_assembly.py`
- `formal_api_demo_core.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `codex_log/current_local_artifact_paths.md`

## 4. 配置检查

- `OSS 配置`：已确认存在，assembly gate 相关字段全部通过。
- `ICE / IMS 配置`：已确认存在，assembly gate 相关字段全部通过。
- `敏感凭据`：本轮只读使用本地配置，未写入报告、日志或 Git。
- `配置缺失项`：0。

## 5. 最小样片输入

本轮使用唯一正式工作区内部的既有素材，不修改 v3.1 正片或 `dist/latest_review_pack/`：

| 类型 | 路径 | 用途 |
| --- | --- | --- |
| 录屏类短视频 | `dist/formal_api_demo/visual/seg02_video.mp4` | 0-6 秒主视觉段 |
| 结果卡图片 | `dist/formal_api_demo/visual/result_card_ai_report_rewrite_trap_cn.png` | 6-12 秒卡片段 |
| 既有 TTS | `dist/formal_api_demo/tts/formal_voiceover.mp3` | 12 秒样片音轨 |
| 既有字幕 | `dist/formal_api_demo/captions.srt` | 云端 timeline 字幕输入 |

样片结构：

- 9:16 竖屏。
- 12 秒。
- 两段 timeline：录屏类短视频 6 秒 + 结果卡 6 秒。

## 6. 执行结果

- `真实阿里云 API 调用`：已确认。
- `OSS 上传`：已确认，上传对象数量 5。
- `ICE / 云剪任务提交`：已确认。
- `ICE 轮询`：已确认。
- `云端导出 MP4`：已确认。
- `ICE 请求链`：`ListEditingProjects`、`UpdateEditingProject`、`SubmitMediaProducingJob`、`GetMediaProducingJob`。

输出：

- `OSS 输出路径`：`oss://zvip1-video-beijing/video-factory/final/20260502T191452Z/formal_api_demo.mp4`
- `本地下载验证路径`：`/Users/fan/Documents/视频工厂/dist/验证样片_validation_samples/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/cloud_export_final.mp4`
- `说明`：裸 HTTPS 对象路径为私有读，直接 ffprobe 返回 403；本轮仅在本地忽略目录生成短期签名链接完成下载验证，签名链接未写入报告或 Git。

## 7. ffprobe 验证

- `ffprobe`：通过。
- `duration`：12.000000 秒。
- `video`：H.264，1080x1920。
- `audio`：AAC。
- `file_size`：1591179 bytes。

## 8. vNext 判断

- `可以作为候选`：是。
- `原因`：当前代码可以使用既有素材完成 OSS 上传、ICE 工程更新、云剪任务提交、轮询和 MP4 导出。
- `仍需后续验证`：
  - 更完整的 vNext timeline 是否兼容。
  - 多段真实录屏、卡片动效和音轨长度不一致时的裁剪策略。
  - OSS 私有读下的成片下载 / 分发策略。
  - 是否需要为 vNext 建立独立云剪工程或保留现有工程。

## 9. 状态边界

- 未修改 v3.1 正片。
- 未修改 `dist/latest_review_pack/` 既有产物。
- 未修改 `current_publish_target`。
- 未生成正式视频。
- 未写新文案。
- 未处理 HyperFrames 中段录屏。
- 内容验证字段未提升为最终通过态。
- 发送状态字段未提升。
- 本地样片与原始运行结果均位于唯一正式工作区内部，且不进入 Git。
