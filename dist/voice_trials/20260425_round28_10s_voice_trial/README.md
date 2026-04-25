# round28 最小声音试配说明

## 本轮目标

- `已确认` 本轮只生成 1 条 10-15 秒声音 trial（试配）音频。
- `已确认` 本轮不修改视频、不替换全片音轨、不生成新视频 round。
- `待验证` 本轮只用于用户 / ChatGPT 判断声音方向是否接近“低压、清楚、有一点可爱感的女生游戏向导音”。

## 使用的 round28 文案

```text
最费时间的，不是做汇报页。是第一行根本写不出来。后来我换上调好的提示词，直接砍掉空转。区别不是豆包，是那段提示词。
```

## 文案来源

- 来源路径：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`
- 取用范围：第 1 段 + 第 5 段首句
- 选择理由：
  - 包含判断：`最费时间的，不是做汇报页`
  - 包含问题：`第一行根本写不出来`
  - 包含动作 / 结果：`换上调好的提示词，直接砍掉空转`
  - 不依赖中段画面即可听懂，适合主持壳短句试配

## TTS 工具 / 模型 / 音色

- TTS 工具：`aliyun_bailian`
- API 路线：`aliyun_qwen_realtime_websocket`
- 模型：`qwen3-tts-instruct-flash-realtime`
- 音色：`Serena`
- 说明：该工具与音色只代表本轮 trial 使用方案，不代表最终 TTS 供应商或最终音色已确定。

## 关键参数

- `response_format`：`pcm`
- `sample_rate`：`24000`
- 输出编码：`aac (LC)`
- 输出采样率 / 声道：`48000 Hz / mono`
- 输出码率：约 `128 kb/s`
- 后处理：
  - `highpass=f=80`
  - `lowpass=f=12000`
  - `deesser=i=0.4:m=0.5:f=0.5:s=o`
  - `acompressor=threshold=-18dB:ratio=2:attack=50:release=150:makeup=1.5`
  - `loudnorm=I=-16:TP=-1.5:LRA=9`
- 风格指令摘要：低压、清楚、有一点可爱感的中文女生游戏向导；句尾自然下收；不走客服腔、新闻播音腔、AI 解说腔或幼态撒娇。
- 调用调试文件：`dist/voice_trials/20260425_round28_10s_voice_trial/tts_request_debug_sanitized.json`

## 输出音频

- 输出路径：`dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`
- 实际时长：`13.00s`
- 可解码性：`已确认` 可被 `ffmpeg` 解码

## 音量 / 响度基础信息

- `volumedetect.mean_volume`：`-16.4 dB`
- `volumedetect.max_volume`：`-1.5 dB`
- `loudnorm.input_i`：`-16.25 LUFS`
- `loudnorm.input_tp`：`-1.48 dBTP`
- `loudnorm.input_lra`：`1.70 LU`
- 验证日志：
  - `dist/voice_trials/20260425_round28_10s_voice_trial/ffmpeg_decode_check.txt`
  - `dist/voice_trials/20260425_round28_10s_voice_trial/volumedetect.txt`
  - `dist/voice_trials/20260425_round28_10s_voice_trial/loudnorm_measure.txt`

## 当前状态

- `voice_trial_status`：已生成，待用户 / ChatGPT 听感复审。
- `voice_validation_status`：待验证。
- `tts_vendor_status`：待验证。
- `content_validation`：仍待用户 / ChatGPT 最终复审。
- `send_ready`：仍为 `no`。

## 禁止误写

- 这不是最终音色。
- 这不是最终 TTS 供应商。
- 这不代表声音验证已通过。
- 这不替换当前全片音轨。
- 这不改变 `dist/latest_review_pack/` 或 round34 视频状态。
