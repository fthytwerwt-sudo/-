# 01 Media Probe Report｜媒体基础解析

## technical facts

```json
{
  "duration_seconds": 416.740114,
  "width": 1180,
  "height": 2556,
  "aspect_ratio": "vertical_9_16_like_phone_recording",
  "fps": "15026400/250051",
  "video_codec": "hevc",
  "video_bit_rate": "7045565",
  "audio_codec": "aac",
  "audio_channels": 2,
  "audio_sample_rate": "44100",
  "audio_bit_rate": "125413",
  "subtitle_stream_present": false,
  "audio_present": true,
  "standard_probe_decodable": "failed_due_to_non_monotonic_dts_warning_in_probe_script",
  "fallback_decode_check": "passed_for_video_sample_and_audio_sample_with_fflags_genpts; full ffmpeg processing completed with non-monotonic DTS warnings",
  "likely_edited_video": true,
  "visible_cards_subtitles_motion_ui": true
}
```

## interpretation

- `已确认` 这是竖屏手机录屏式 reference，分辨率 `1180x2556`，时长约 `416.74s`，HEVC 视频 + AAC 双声道音轨。
- `已确认` `ffprobe` 可读，音轨存在，无字幕轨。
- `部分成立` 默认 `video-metadata-probe` 脚本返回 `validation_status = failed`，原因不是 ffprobe 不可读，而是全量 null muxer 检查出现 `non monotonically increasing dts` 警告。
- `已确认` 额外执行 `ffmpeg -fflags +genpts` 的视频抽样解码和音频抽样解码均返回 exit 0；contact sheet、关键帧、响度/静音检测均可生成，因此本轮可继续做 reference audit。
- `待验证` 该 MP4 若用于后续剪辑，不应直接作为素材资产使用；本轮仅用于结构解析。

## visible composition

- 抖音界面录屏，顶部搜索框和右侧互动按钮长期可见。
- 主 reference 为 @秋芝2046 第 56 集关于“豆包专家模式 / 高级 AI 军师”的视频。
- 视频内包含主持人口播、字幕、问题卡、模式对比卡、文档高亮、表格/方案截图和结果卡。

## tools

- `ffprobe`: available, metadata read passed.
- `ffmpeg`: available, frame extraction / audio analysis passed with DTS warnings.
- local OCR: unavailable.
- local ASR: unavailable.
