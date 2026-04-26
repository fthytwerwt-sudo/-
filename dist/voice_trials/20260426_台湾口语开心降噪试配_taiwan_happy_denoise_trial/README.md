# 台湾口语开心降噪声音试配 Taiwan Happy Denoise Trial

## 本轮目标

- `已确认` 本轮只生成《视频工厂》声音第二轮最小对照 trial。
- `已确认` 不修改视频、不替换全片音轨、不生成新视频 round。
- `已确认` 本轮目标是 A / B 两组 10-15 秒声音对照音频，并保留原始输出与轻降噪输出。

## 用户反馈原文

1. 情绪上面还不够开心的那种。
2. 需要把口语改成台湾的口音。
3. 现在生成的环境音有点吵，需要降噪。

## 本轮 voice_trial_text

```text
其实最花时间的，不是做汇报页啦。
是你一开始，第一句话就卡住了。
后来我换成调好的提示词，整个空转时间就少很多。
差别不在豆包本身，是那一段提示词真的有帮上忙。
```

## 本轮 instructions

```text
整体语气更开心、更轻快，像台湾女生在轻松带朋友看一个好用的小技巧。
声音要有笑意，句尾可以自然上扬，但不要夸张卖货，不要娃娃音，不要综艺腔。
节奏比上一版稍微活一点，停顿自然，听起来像真人分享，不像机器播报。
请使用自然的台湾普通话口吻，不要大陆播音腔。
发音自然、亲切、带一点笑意，不要刻意拖音。
请在不赶、不夸张的前提下，把这段控制在 14 秒左右讲完。
```

## A / B 版本差异

- A 版：沿用当前 custom voice，使用台湾口语文本 + 开心轻快 instructions 生成；输出后做轻降噪。
- B 版：先对复刻输入样本做轻降噪，再重新创建测试 custom voice；使用同一台湾口语文本 + 同一 instructions 生成；输出后做轻降噪。

## 使用的 model / voice / target_model

- 创建模型 model：`qwen-voice-enrollment`
- 目标合成模型 target_model：`qwen3-tts-vc-realtime-2026-01-15`
- 合成模型 model：`qwen3-tts-vc-realtime-2026-01-15`
- A 版 voice：`qwen-t...de43`（脱敏）
- B 版 voice：`qwen-t...bb3b`（脱敏）
- B 版 preferred_name：`vfr2tw0426c`
- 是否重新创建 custom voice：A 版 `no`；B 版 `yes`。
- 是否做输入样本降噪：A 版 `no`；B 版 `yes`。
- 是否做输出后降噪：A 版 `yes`；B 版 `yes`。

## 输出文件路径

- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav`（未降噪，节奏校准到 10-15 秒）
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_API原始_未节奏校准.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav`（未降噪，节奏校准到 10-15 秒）
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_复刻输入样本_轻降噪.wav`

说明：API 直出因固定文案较长，未稳定落在 10-15 秒；本轮保留 API 直出审计文件，同时用 `atempo` 生成未降噪节奏校准版作为正式 10-15 秒对照 trial。

## 验证结果

| 文件 | duration | codec | sample_rate | channels | mean_volume | loudnorm.input_i | ffmpeg 解码 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav` | `14.18s` | `pcm_s16le` | `24000 Hz` | `1` | `-22.8 dB` | `-22.13` | `通过` |
| `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav` | `14.18s` | `pcm_s16le` | `24000 Hz` | `1` | `-23.3 dB` | `-22.64` | `通过` |
| `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav` | `14.20s` | `pcm_s16le` | `24000 Hz` | `1` | `-22.4 dB` | `-22.40` | `通过` |
| `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav` | `14.20s` | `pcm_s16le` | `24000 Hz` | `1` | `-22.7 dB` | `-22.65` | `通过` |

## 脱敏请求与验证记录

- `custom_voice_list_debug_sanitized.json`
- `A_voice_clone_tts_request_debug_sanitized.json`
- `B_重建音色_create_custom_voice_request_debug_sanitized.json`
- `B_voice_clone_tts_request_debug_sanitized.json`
- `run_summary.json`

## 当前状态

- `technical_generation`：通过。
- `voice_validation_status`：待验证。
- 当前状态：待用户 / ChatGPT 听感复审。
- `content_validation`：仍待用户 / ChatGPT 最终复审。
- `full_content_validation`：仍待用户 / ChatGPT 最终复审。
- `send_ready`：仍为 `no`。

## 禁止误写

- 本轮 trial 不等于声音通过。
- 本轮 custom voice 不等于最终音色。
- 本轮不替换全片音轨。
- 本轮不改变 `content_validation`。
- 本轮不改变 `send_ready`。
- 本轮未修改 `dist/latest_review_pack/full.mp4`。
- 本轮未修改 `dist/latest_review_pack/middle_preview.mp4`。
