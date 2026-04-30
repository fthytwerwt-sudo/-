# 20260430｜video-metadata-probe 冒烟测试报告

## 测试对象

- `artifact_id（产物编号）`：`round34_middle_preview`
- `中文名称`：round34 中段预览样片
- `video_path（视频路径）`：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`
- `source_index（来源索引）`：`codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`
- `test_command（测试命令）`：`/Users/fan/.codex/skills/video-metadata-probe/scripts/probe_video.sh "/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4"`

## 检查结果

| field（字段） | value（结果） |
| --- | --- |
| `file_path（文件路径）` | `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4` |
| `exists（是否存在）` | `true` |
| `file_size_bytes（文件大小）` | `1548882` |
| `duration_seconds（时长）` | `28.520000` |
| `width（宽）` | `720` |
| `height（高）` | `1280` |
| `fps（帧率）` | `25.000` |
| `video_codec（视频编码）` | `h264` |
| `audio_present（是否有音轨）` | `true` |
| `audio_codec（音频编码）` | `aac` |
| `audio_channels（音频声道）` | `2` |
| `decodable（是否可解码）` | `true` |
| `ffprobe_available（ffprobe 是否可用）` | `true` |
| `ffmpeg_available（ffmpeg 是否可用）` | `true` |
| `fallback_used（是否使用兜底）` | `false` |
| `validation_status（验证状态）` | `passed` |

## 验证口径

- `已确认` 本次成功调用 `ffprobe（视频信息读取工具）`。
- `已确认` 本次成功调用 `ffmpeg（音视频处理工具）` 做解码检查。
- `已确认` 本次未使用 `mdls（macOS 元数据读取工具）` fallback（兜底）。
- `已确认` `middle_preview（中段预览样片）` 有音轨且可解码。
- `已确认` 这只是 `technical_validation（技术验证）` / `metadata_validation（元数据验证）` / `audio_validation（音频验证）`，不代表 `content_validation（内容验证）` 通过。

## 边界确认

- `已确认` 本轮未生成新视频。
- `已确认` 本轮未修改 `dist/latest_review_pack（最新审片包）`。
- `已确认` 本轮未修改 `content_validation（内容验证）`。
- `已确认` 本轮未修改 `send_ready（可发送状态）`。
