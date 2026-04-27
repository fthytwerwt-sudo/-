# 音频参考说明 audio_reference_note

## 结论

- `已确认` 原素材包含 AAC stereo 音频，采样率 `44100 Hz`。
- `已确认` 已抽取音频副本：`/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio/reference_audio.m4a`。
- `已确认` 已生成波形证据：`/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio_waveform.png`。
- `待验证` 本轮没有可靠 ASR 转写稿。

## 无可靠转写的原因

- `已确认` 当前仓库未发现可复用 ASR / Whisper 转写流程。
- `已确认` 当前 PATH 未发现 `whisper`、`mlx-whisper`、`faster-whisper`。
- `已确认` 本轮任务要求不能硬编台词，因此不把听不清或未转写的口播写成已确认。
- `已确认` `silencedetect=noise=-35dB:d=0.25` 未输出可用静音段；不能仅靠该算法切出台词停顿。

## 可引用范围

- `已确认` 可以引用画面中看得清的字幕或大字卡，例如 `00:00:27` 的“再要一个呗”、`00:00:31` 的“最没有天赋的”。
- `待验证` 完整口播内容、具体音效、配乐变化、笑点音效是否存在，需要用户或 ChatGPT 结合原视频音频复核。

## 使用提醒

本文件只说明音频证据状态，不是 transcript。后续迁移到《视频工厂》中段时，只能把本轮已确认的视觉/节奏规律作为参考，不能把未转写的口播句当作项目正式文案。
