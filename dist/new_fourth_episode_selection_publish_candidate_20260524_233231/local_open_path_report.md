# local_open_path_report

status = blocked_publish_candidate_unavailable_remote_tts_authorization_missing

## 本地路径
- review_pack_dir: `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260524_233231`
- full_video_path: `not_generated`
- narration_path: `not_generated`
- captions_path: `not_generated`

## 阻断原因
当前进程没有 `DASHSCOPE_API_KEY` / `ALIYUN_API_KEY`，项目正式 TTS 需要远程授权。`/Users/fan/.config/video-factory/formal_api_demo.local.toml` 存在，但本轮禁止读取 API key / token / secret，因此没有读取，也没有用它生成 TTS。

## 安全边界
- 未生成无声预览。
- 未使用 macOS say。
- 未使用本地低质 TTS fallback。
- 未生成 `full.mp4` 冒充成片。
