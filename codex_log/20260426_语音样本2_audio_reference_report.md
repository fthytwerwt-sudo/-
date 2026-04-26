# 20260426 语音样本2 Audio Reference Report

## 结论

- `已确认` 本轮已定位用户新样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`。
- `已确认` 原始样本只读解析已完成；未修改原始 MP4。
- `已确认` 已生成分析副本与 10-20 秒 voice cloning 复刻输入样本。
- `待验证` 该样本是否足够代表最终声音方向，仍待用户 / ChatGPT 听感复审。

## 新样本定位

- 绝对路径：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`
- 文件名：`语音样本 2.MP4`
- 文件大小：`20614012 bytes`
- 修改时间：`2026-04-26 23:37:44 +0800`
- 命中方式：搜索 `/Users/fan/Documents/视频工厂/素材录制/` 下包含 `语音样本 2` 的音视频文件。
- 候选数量：`1`

## 原始样本参数

- duration：`23.16s`
- container：`mov,mp4,m4a,3gp,3g2,mj2`
- bitrate：`7121 kb/s`
- video_codec：`hevc (Main) (hvc1 / 0x31637668)`
- audio_codec：`aac (LC) (mp4a / 0x6134706D)`
- sample_rate：`44100 Hz`
- channels：`stereo`
- audio_bitrate：`115 kb/s`

## 音量 / 响度 / 静音

- volumedetect.mean_volume：`-13.3 dB`
- volumedetect.max_volume：`0.0 dB`
- loudnorm.input_i：`-10.26 LUFS`
- loudnorm.input_tp：`0.20`
- loudnorm.input_lra：`3.00`
- silencedetect：`noise=-35dB / d=0.25` 下未检出明显静音段。

## 本轮衍生产物

- 分析副本：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_分析副本.m4a`
- 复刻输入样本：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- 完整转写输入：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_完整转写输入_24k_mono.wav`
- 复刻输入参数：`17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`
- 复刻输入裁剪：从原 MP4 `2.0s` 起，连续裁剪 `17.0s`。

## 解析日志

- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/sample_ffmpeg_decode_check.txt`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/sample_volumedetect.txt`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/sample_loudnorm_measure.txt`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/sample_silencedetect.txt`

## 边界

- 本报告只记录新样本客观音频参数和本轮分析副本 / 复刻输入。
- 本报告不代表声音验证通过。
- 本报告不代表最终 custom voice 已确定。
- 本报告不允许触发全片音轨替换。
- 本报告不改变 `content_validation`、`full_content_validation`、`send_ready`。
