# 素材清单 assets_inventory

## 任务边界

- `已确认` 本轮只做参考素材高保真提取。
- `已确认` 本轮未修改现有视频、字幕、音轨、round、`content_validation`、`send_ready`。
- `已确认` 优先目录 `/Users/fan/Documents/视频工厂/素材录制/中段吐槽插入风格` 不存在；实际命中的是同名 MP4 文件。

## 已定位素材

| 状态 | 原始路径 | 文件名 | 类型 | 大小 | 是否可打开 |
| --- | --- | --- | --- | --- | --- |
| `已确认` | `/Users/fan/Documents/视频工厂/素材录制/中段吐槽插入风格.MP4` | `中段吐槽插入风格.MP4` | MP4 video | 50,716,126 bytes | 是；`ffmpeg` 可读取并解码首帧 |

## 媒体基础参数

| 字段 | 结果 |
| --- | --- |
| 探测工具 | `/Users/fan/Documents/视频工厂/node_modules/ffmpeg-static/ffmpeg` |
| `ffprobe` | `待验证` 当前 PATH 与本机搜索未找到可用 `ffprobe`；本轮用 `ffmpeg -i` 替代读取元数据 |
| 容器 | `mov,mp4,m4a,3gp,3g2,mj2` / `mp42` |
| 时长 | `00:00:36.24` |
| 总码率 | 约 `11195 kb/s` |
| 视频编码 | `hevc (Main)` / `hvc1` |
| 分辨率 | `1180x2556` |
| 帧率 | `60.04 fps`，`60 tbr` |
| 色彩/像素格式 | `yuvj420p(pc, bt709, progressive)` |
| 音频编码 | `aac (LC)` |
| 音频采样率 | `44100 Hz` |
| 声道 | `stereo` |
| 音频码率 | 约 `109 kb/s` |
| 是否有音频 | 是 |

## 本轮生成证据

| 路径 | 说明 |
| --- | --- |
| `/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/keyframes_contact_sheet.jpg` | 每 1 秒抽帧联系表，帧内叠加时间码 |
| `/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/frames/` | 每 1 秒单帧，文件 `t_01.jpg` 到 `t_36.jpg`，帧内叠加时间码 |
| `/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio/reference_audio.m4a` | 原素材音频只读抽取副本 |
| `/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio_waveform.png` | 全片音频波形图 |

## 转写状态

- `已确认` 当前仓库未发现本地 ASR / Whisper / transcript 脚本。
- `已确认` 当前 PATH 未发现 `whisper`、`mlx-whisper`、`faster-whisper`。
- `已确认` 本轮不调用外部云端 ASR，不编造口播台词。
- `待验证` 画面中可读字幕片段仅作为视觉证据，不等于完整 transcript。
