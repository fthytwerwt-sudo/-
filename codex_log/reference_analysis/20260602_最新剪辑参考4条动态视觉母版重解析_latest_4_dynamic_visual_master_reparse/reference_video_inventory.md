# Reference Video Inventory

status_boundary:
- `task_result.status = dynamic_visual_master_parse_evidence_generated`
- `content_validation = not_applicable`
- `send_ready = false`
- `video_rendered = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`

| reference_id | source_path | duration | resolution | fps | video_codec | audio_present | ffprobe | ffmpeg_smoke | opencv |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-01-2026 23-49-21_1.MP4` | `345.827s` | `1180x2556` | `60.091` | `hevc` | `True` | `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/metadata/reference_01_ffprobe.json` | `passed` | `True` |
| `reference_02` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-03-59_1.MP4` | `200.392s` | `1180x2556` | `60.098` | `hevc` | `True` | `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/metadata/reference_02_ffprobe.json` | `passed` | `True` |
| `reference_03` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-07-32_1.mov` | `363.745s` | `1180x2556` | `60.094` | `hevc` | `True` | `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/metadata/reference_03_ffprobe.json` | `passed` | `True` |
| `reference_04` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-16-59_1.mov` | `294.198s` | `1180x2556` | `60.096` | `hevc` | `True` | `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/metadata/reference_04_ffprobe.json` | `passed` | `True` |

## Evidence Outputs

- `ffprobe_json`: `codex_log/reference_analysis/.../metadata/reference_XX_ffprobe.json`
- `probe_video_report`: `codex_log/reference_analysis/.../metadata/reference_XX_video_metadata_probe.md`
- `ffmpeg_smoke`: `dist/reference_analysis/.../ffmpeg_smoke/reference_XX/t0001s.jpg`
- `frames_5s`: `dist/reference_analysis/.../reference_XX/frames_5s/`
- `scene_candidates`: `dist/reference_analysis/.../reference_XX/scene_candidates/`
- `dynamic_1s_clips`: `dist/reference_analysis/.../reference_XX/dynamic_1s_clips/`
- `contact_sheets`: `dist/reference_analysis/.../reference_XX/contact_sheet_*.jpg`
