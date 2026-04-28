# 素材清单 material_inventory

`已确认` 本清单只覆盖用户本轮指定的三处目录，不扫描桌面、下载目录、临时目录或历史 round。

## 检查目录

| 目录 | 状态 | 候选文件数 | 备注 |
| --- | --- | ---: | --- |
| `/Users/fan/Documents/视频工厂/素材录制/正面/` | exists | 1 | 本轮正面素材目录。 |
| `/Users/fan/Documents/视频工厂/素材录制/反面/` | exists | 1 | 本轮反面素材目录。 |
| `/Users/fan/Documents/视频工厂/素材录制/正面-反面/` | missing | 0 | 合并目录不存在。 |

## 候选素材

| group | path | file_type | size | modified_time | duration | resolution | fps | codecs | audio | open_status | material_guess | technical_notes |
| --- | --- | --- | ---: | --- | ---: | --- | ---: | --- | --- | --- | --- | --- |
| positive | `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4` | MP4 / ISO Media | 1.7G / 1841063031 bytes | 2026-04-16 23:16:19 +0800 | 745.68s | 3420x2214 | 59.9169 | HEVC + MPEG-4 AAC | AAC stereo 48000 Hz | OpenCV 可打开，采样 0 失败 | 疑似横向录屏；正面 AI 调整/PPT 生成过程 | 未发现黑屏候选；存在大量静态等待/生成画面；非低分辨率；未见方向错误；无明显损坏。 |
| negative | `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4` | MP4 / ISO Media | 156M / 163435781 bytes | 2026-04-16 22:42:39 +0800 | 67.08s | 3420x2214 | 59.8807 | HEVC + MPEG-4 AAC | AAC stereo 48000 Hz | OpenCV 可打开，采样 0 失败 | 疑似横向录屏；反面宽泛问法/文本结果 | 未发现黑屏候选；存在静态等待画面；非低分辨率；未见方向错误；无明显损坏。 |

## 工具说明

- `ffmpeg / ffprobe`: 当前 PATH 未找到，未使用。
- `mdls`: 用于读取 codec、duration、resolution、creation date。
- `afinfo`: 用于确认 AAC 音轨、采样率和声道。
- `OpenCV / Python`: 用于打开视频、抽帧、生成联系表和基础视觉采样。

## 深读素材选择

`已确认` 本轮只有 2 个候选视频，且分别来自正面/反面目录，因此两个都深读；没有因素材过多做二次筛选。
