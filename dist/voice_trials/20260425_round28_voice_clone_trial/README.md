# round28 声音复刻最小试配说明

## 本轮目标

- `已确认` 本轮目标是基于用户授权的合规裁剪样本，走阿里百炼 `voice cloning（声音复刻）` 路线创建 1 个测试 custom voice，并生成 1 条 10-15 秒 round28 复刻试配音频。
- `已确认` 本轮不修改视频、不替换全片音轨、不生成新视频 round。
- `已确认` 本轮不再使用 `Serena` 系统音色冒充复刻。

## 用户授权摘要

- `已确认` 用户已明确授权：允许将用户语音样本中裁剪出的 10-20 秒合规音频片段上传到阿里百炼声音复刻接口，仅用于《视频工厂》本项目的最小声音复刻试配。
- `已确认` 授权边界：
  - 只允许创建测试 custom voice。
  - 只允许用于《视频工厂》内部声音试配。
  - 不允许替换全片音轨。
  - 不允许写成最终音色已定。
  - 不允许写成声音验证通过。
  - 不允许写成 `content_validation` 通过。
  - 不允许写成 `send_ready = yes`。

## 复刻输入样本

- 原始样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
- 复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`
- 裁剪策略：避开开头 / 结尾静音，从原样本 `1.000s -> 18.000s` 裁出连续人声。
- 复刻输入样本参数：
  - `duration = 17.00s`
  - `format = wav`
  - `codec = pcm_s16le`
  - `sample_rate = 24000 Hz`
  - `channels = mono`
  - `bitrate = 384 kb/s`
  - `file_size_bytes = 816078`
- 验证日志：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输入_ffmpeg_create.txt`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输入_ffmpeg_check.txt`

## 使用的 API / model / target_model

- 创建音色 API：`POST https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization`
- 创建模型：`qwen-voice-enrollment`
- 目标合成模型：`qwen3-tts-vc-realtime-2026-01-15`
- 用户 prompt 指定 `preferred_name`：`vf_r28_clone_20260426`
- 实际使用 `preferred_name`：`vfr28clone0426`
- 调整原因：官方 `preferred_name` 只允许数字 / 大小写字母 / 下划线且不超过 16 字符；原名超长，首次重试返回 `InvalidParameter`，缩短后成功。
- 请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
- 合成请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- custom voice 脱敏标识：`qwen-t...de43`

## round28 文案

```text
最费时间的，不是做汇报页。
是第一行，根本写不出来。
后来我换上调好的提示词，直接砍掉空转。
区别不是豆包，是那段提示词。
```

- 来源路径：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`
- 说明：本轮按最小 TTS 断句版生成，不新增观点，不改成播音稿。

## 当前结果

- `voice_clone_input_status`：已生成合规复刻输入样本。
- `custom_voice_status`：已创建测试 custom voice。
- `custom_voice_id`：`qwen-t...de43`（脱敏标识）。
- `output_audio_status`：已生成 1 条声音复刻 trial。
- 输出音频：`dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`
- 实际时长：`12.96s`
- 音频格式：`wav / pcm_s16le / 24000 Hz / mono`
- 文件大小：`622124 bytes`
- `ffmpeg` 解码验证：通过。
- `volumedetect.mean_volume`：`-23.5 dB`
- `volumedetect.max_volume`：`-5.8 dB`
- `loudnorm.input_i`：`-23.57 LUFS`
- `loudnorm.input_lra`：`2.20 LU`
- 验证日志：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_ffmpeg_decode_check.txt`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_volumedetect.txt`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_loudnorm_measure.txt`

## 当前状态

- `voice_clone_trial_status`：已生成，待用户 / ChatGPT 听感复审。
- `voice_validation_status`：待验证。
- `tts_vendor_status`：待验证。
- `content_validation`：仍待用户 / ChatGPT 最终复审。
- `full_content_validation`：仍待用户 / ChatGPT 最终复审。
- `send_ready`：仍为 `no`。

## 禁止误写

- 本轮只创建测试 custom voice，用于《视频工厂》内部最小声音复刻试配。
- 这不是最终音色。
- 这不代表声音验证已通过。
- 这不代表 `content_validation` 已通过。
- 这不替换当前全片音轨。
- 这不改变 `dist/latest_review_pack/` 或 round34 视频状态。
