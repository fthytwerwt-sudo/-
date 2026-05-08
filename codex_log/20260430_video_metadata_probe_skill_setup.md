# 20260430｜video-metadata-probe skill 安装与配置日志

## 任务边界

- `已确认` 本轮目标是补齐 `Homebrew（Mac 包管理器）`、`ffmpeg（音视频工具套件）`、`ffprobe（视频信息读取工具）` 与 `video-metadata-probe（视频元数据检查）` skill。
- `已确认` 本轮不生成视频，不修改视频 / 音频 / 图片产物。
- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`、`content_validation（内容验证）`、`send_ready（可发送状态）`。
- `已确认` 本轮不修改 `locked_reference_registry.md（锁定参考登记表）` 和 `current_local_artifact_paths.md（当前本地产物路径索引）`。

## 安装前状态

- `已确认` `brew（Homebrew 包管理器）` 安装前不可用。
- `已确认` `ffmpeg（音视频工具套件）` 安装前不可用。
- `已确认` `ffprobe（视频信息读取工具）` 安装前不可用。
- `已确认` `mdls（macOS 元数据读取工具）` 可用，但只能作为 fallback（兜底），不能替代正式视频元数据验证主工具。

## Homebrew 安装

- `已确认` 使用 Homebrew 官方安装脚本安装：
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- `已确认` 安装过程中出现官方安装确认页；用户在可见 Terminal 中完成确认 / 密码输入，密码未进入聊天、未被记录、未被回显。
- `已确认` 安装后 `brew（Homebrew 包管理器）` 可用：
  - path：`/opt/homebrew/bin/brew`
  - version：`Homebrew 5.1.8`

## ffmpeg / ffprobe 安装

- `已确认` 使用命令安装：
  - `brew install ffmpeg`
- `已确认` 安装后 `ffmpeg（音视频工具套件）` 可用：
  - path：`/opt/homebrew/bin/ffmpeg`
  - version：`ffmpeg version 8.1`
- `已确认` 安装后 `ffprobe（视频信息读取工具）` 可用：
  - path：`/opt/homebrew/bin/ffprobe`
  - version：`ffprobe version 8.1`

## skill 创建结果

- `已确认` 已创建全局 skill：
  - `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md`
  - `/Users/fan/.codex/skills/video-metadata-probe/scripts/probe_video.sh`
  - `/Users/fan/.codex/skills/video-metadata-probe/examples/README.md`
- `已确认` `probe_video.sh（视频元数据检查脚本）` 已设为可执行。
- `已确认` skill 规则明确：
  - 优先使用 `ffprobe（视频信息读取工具）`。
  - 使用 `ffmpeg -v error（音视频解码检查命令）` 做解码验证。
  - `mdls（macOS 元数据读取工具）` 只能作为 fallback（兜底）。
  - 技术验证不等于 `content_validation（内容验证）`。
  - TTS 任务生成视频没有音轨时必须 `blocked（阻断）`。

## smoke test（冒烟测试）结果

- `已确认` 使用已验证存在的 `round34_middle_preview（round34 中段预览样片）` 做真实验证。
- `已确认` 视频路径：
  - `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`
- `已确认` 冒烟测试报告：
  - `codex_log/20260430_video_metadata_probe_smoke_test.md`
- `已确认` 关键结果：
  - `ffprobe_available = true（ffprobe 可用）`
  - `ffmpeg_available = true（ffmpeg 可用）`
  - `duration_seconds = 28.520000`
  - `resolution = 720x1280`
  - `fps = 25.000`
  - `video_codec = h264`
  - `audio_present = true（有音轨）`
  - `audio_codec = aac`
  - `audio_channels = 2`
  - `decodable = true（可解码）`
  - `fallback_used = false（未使用兜底）`
  - `validation_status = passed（技术验证通过）`

## 状态说明

- `已确认` 本轮只证明 `middle_preview（中段预览样片）` 的基础视频元数据和解码技术验证通过。
- `已确认` 本轮不代表 `content_validation（内容验证）` 通过。
- `已确认` 本轮不代表 v3 已完成。

## 下一个目标

后续所有视频生成 / 审片 / TTS 入片任务默认先使用 `video-metadata-probe（视频元数据检查）` 做基础验证，再进入内容复审或 locked reference（锁定参考）继承检查。
