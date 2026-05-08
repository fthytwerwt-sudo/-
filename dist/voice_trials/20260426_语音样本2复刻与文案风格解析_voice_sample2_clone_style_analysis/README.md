# 语音样本2复刻与文案风格解析 Voice Sample2 Clone Style Analysis

## 本轮目标

- `已确认` 本轮重开《视频工厂》新语音样本链路，不沿用上一轮 A / B 声音试配结果。
- `已确认` 本轮只生成 1 条约 15 秒 voice cloning（声音复刻）试听 trial。
- `已确认` 本轮解析样本 MP4 的文案风格，并生成高保真记录，方便 ChatGPT 后续按 reference style 写文案。
- `已确认` 本轮不修改视频、不替换全片音轨、不生成新视频 round。

## 用户原始需求

用户本轮新事实：

- 用户重新放了一个样本在本地。
- 用户描述路径为：视频工厂-素材录制-语音样本 2。
- 用户希望同步执行两个任务：
  1. 解析当前语音样本，并复刻 / 克隆出来一个 15 秒左右的语音给用户听。
  2. 解析这个样本视频 MP4 的文案风格，并保真记录，方便 ChatGPT 后续查看和写文案。

## 新样本定位结果

- 命中方式：`search_latest_matching_audio_video_file`
- 新样本绝对路径：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`
- 文件名：`语音样本 2.MP4`
- 文件大小：`20614012 bytes`
- 修改时间：`2026-04-26 23:37:44 +0800`
- 搜索候选：仅命中 1 个候选文件。

已搜索路径：

1. `/Users/fan/Documents/视频工厂/素材录制/语音样本 2`
2. `/Users/fan/Documents/视频工厂/素材录制/语音样本2`
3. `/Users/fan/Documents/视频工厂/素材录制/语音样本_2`
4. `/Users/fan/Documents/视频工厂/素材录制/语音样本-2`
5. `/Users/fan/Documents/视频工厂/素材录制`

## 声音解析结果

- duration：`23.16s`
- container：`mov,mp4,m4a,3gp,3g2,mj2`
- video_codec：`hevc (Main) (hvc1 / 0x31637668)`
- audio_codec：`aac (LC) (mp4a / 0x6134706D)`
- sample_rate：`44100 Hz`
- channels：`stereo`
- bitrate：`7121 kb/s`
- audio_bitrate：`115 kb/s`
- volumedetect.mean_volume：`-13.3 dB`
- volumedetect.max_volume：`0.0 dB`
- loudnorm.input_i：`-10.26 LUFS`
- loudnorm.input_lra：`3.00`
- silencedetect：`-35dB / 0.25s` 下未检出明显静音段。

## 复刻输入样本

- 分析副本：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_分析副本.m4a`
- 复刻输入样本：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- 复刻输入裁剪：从原 MP4 `2.0s` 起，连续裁剪 `17.0s`。
- 复刻输入参数：`17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`
- 裁剪理由：`silencedetect` 未检出明显静音；为避开首尾，选取中间偏前的连续片段作为 10-20 秒 voice cloning 输入。

## custom voice

- 创建模型 model：`qwen-voice-enrollment`
- 目标合成模型 target_model：`qwen3-tts-vc-realtime-2026-01-15`
- preferred_name：`vfsample20426`
- custom voice（脱敏）：`qwen-t...ac19`
- 是否重新创建 custom voice：`yes`
- 是否使用 Serena：`no`
- 是否使用旧 custom voice：`no`
- 是否使用上一轮 A / B custom voice：`no`

## 试听 trial

- 试听 trial：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
- 本地绝对路径：`/private/tmp/视频工厂_user_readable_map_sync/dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
- API 原始输出：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_API原始.wav`
- API 原始输出时长：`13.60s`
- 本轮未做 `atempo` 节奏校准，因为 API 原始输出已在约 15 秒范围内。

## 试听文案与 instructions

试听文案状态：`临时试配文案，不代表样本文案风格原文`。

```text
其实我觉得，最容易卡住的地方，不是工具不会用。
是你一开始不知道该怎么问。
如果前面那句话问对了，后面的结果会顺很多。
所以重点不是换一个工具，而是先把问题说清楚。
```

instructions：

```text
请参考新样本里的说话方式，保持自然口语、真人分享感和解释型节奏。
语气要平实亲近，不要播音腔，不要广告腔，不要夸张带货，也不要刻意表演。
请在约 15 秒内自然说完，停顿清楚但不要拖沓。
```

## 文案风格记录

- 完整 MP4 自动转写：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`
- 文案风格高保真记录：`codex_log/20260426_语音样本2_文案风格高保真记录.md`
- ASR 模型：`paraformer-realtime-v2`
- ASR 状态：`已生成自动转写 / 待人工校对`

## 技术验证结果

试听 trial 验证：

- ffmpeg 解码：`通过`
- duration：`13.60s`
- codec：`pcm_s16le`
- sample_rate：`24000 Hz`
- channels：`mono`
- mean_volume：`-23.8 dB`
- max_volume：`-5.0 dB`
- loudnorm.input_i：`-23.72 LUFS`

验证日志：

- `ffmpeg_decode_check.txt`
- `volumedetect.txt`
- `loudnorm_measure.txt`
- `run_summary.json`

脱敏请求记录：

- `voice_clone_request_debug_sanitized.json`
- `voice_clone_tts_request_debug_sanitized.json`
- `语音样本2_ASR_attempt_debug_sanitized.json`
- `语音样本2_full_ASR_attempt_debug_sanitized.json`

## 当前状态

- `technical_generation`：通过。
- `voice_validation_status`：待验证。
- `copy_style_status`：已记录 / 自动转写待人工校对。
- `content_validation`：待用户 / ChatGPT 最终复审。
- `full_content_validation`：待用户 / ChatGPT 最终复审。
- `send_ready`：no。

## 禁止误写

- 本轮 trial 不等于声音通过。
- 本轮 custom voice 不等于最终音色。
- 本轮文案风格记录只是本轮 reference style，不是唯一标准风格。
- 本轮不替换全片音轨。
- 本轮不修改 `dist/latest_review_pack/full.mp4`。
- 本轮不修改 `dist/latest_review_pack/middle_preview.mp4`。
- 本轮不改变 `content_validation`。
- 本轮不改变 `full_content_validation`。
- 本轮不改变 `send_ready`。
