# 语音样本 audio reference report

## 1. 结论

- `已确认` 本轮找到用户语音样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
- `已确认` 该样本已记录为 `可爱女生向导音` 的 reference anchor（参考锚点）。
- `已确认` 本轮只做只读分析；未修改原始样本、未修改当前成片、未替换旁白、未生成新 round、未做 TTS 试配。
- `部分成立` `ffmpeg` 可用并完成基础分析；`ffprobe` 未在本机可执行路径中命中，本报告的容器与音视频元数据来自 `ffmpeg` 输入信息，后续如需严格 `ffprobe` JSON 可在工具可用后补跑。
- `待验证` 样本是否适合当前视频、是否能稳定指导 TTS 试配、是否达到 `content_validation V1`，仍待用户 / ChatGPT 听感复审与最小声音试配。

## 2. 样本定位

- `voice_sample_status`：已找到
- 用户原说明目录：`/Users/fan/Documents/视频工厂/素材录制/语音样本/`
- 实际命中路径：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
- 文件名：`语音样本_04-25-2026 22-19-11_1.MP4`
- 文件大小：`57779898 bytes`（约 `55 MB`）
- 修改时间：`2026-04-25 22:19:11 +0800`
- 查找说明：指定子目录未命中；按任务兜底范围在当前项目主目录下命中唯一文件名包含 `语音样本` 的 MP4 候选。

## 3. 基础音视频参数

- 容器格式：`mov,mp4,m4a,3gp,3g2,mj2`
- `major_brand`：`mp42`
- 总时长：`00:00:30.68`
- 总码率：`15064 kb/s`
- 是否含视频轨：是
- 视频编码：`hevc (Main)`
- 视频尺寸：`1180x2556`
- 视频帧率：约 `60.03 fps`
- 是否含音频轨：是
- 音频编码：`aac (LC)`
- 采样率：`44100 Hz`
- 声道数：`stereo`
- 音频采样格式：`fltp`
- 音频码率：`107 kb/s`

## 4. 分析副本

- 分析输出目录：`codex_log/audio_reference/20260425_语音样本/`
- 分析副本：`codex_log/audio_reference/20260425_语音样本/语音样本_分析副本.m4a`
- 提取方式：`ffmpeg` 从原 MP4 提取第一条音频轨，`-c:a copy`，不重编码。
- 分析副本时长：`00:00:30.67`
- 分析副本码率：约 `109 kb/s`
- 说明：该副本只用于本地分析，不是最终 TTS 产物，不替换当前视频音轨。

## 5. 音量与静音基础分析

- `volumedetect.mean_volume`：`-12.7 dB`
- `volumedetect.max_volume`：`0.0 dB`
- `volumedetect.histogram_0db`：`10198`
- `astats.Overall.Peak level dB`：`0.184321`
- `astats.Overall.RMS level dB`：`-12.729445`
- `astats.Overall.RMS peak dB`：`-5.750162`
- `astats.Overall.RMS trough dB`：`-inf`
- `astats.Overall.Noise floor dB`：`-inf`
- `loudnorm.input_i`：`-9.10 LUFS`
- `loudnorm.input_tp`：`0.22 dBTP`
- `loudnorm.input_lra`：`2.50 LU`
- `silencedetect` 阈值：`-35 dB`，最短静音：`0.25s`
- 静音段：
  - `0.000s -> 0.74254s`，持续 `0.74254s`
  - `29.1626s -> 30.6939s`，持续 `1.53138s`

## 6. 原始分析日志

- `codex_log/audio_reference/20260425_语音样本/语音样本_ffmpeg_metadata.txt`
- `codex_log/audio_reference/20260425_语音样本/语音样本_volumedetect.txt`
- `codex_log/audio_reference/20260425_语音样本/语音样本_astats.txt`
- `codex_log/audio_reference/20260425_语音样本/语音样本_silencedetect_-35dB_0.25s.txt`
- `codex_log/audio_reference/20260425_语音样本/语音样本_loudnorm_measure.txt`

## 7. 本轮不做的事

- 不做主观听感判断。
- 不写“样本已完全适合项目”。
- 不写“最终 TTS 供应商已确定”。
- 不写“声音已经通过 content_validation”。
- 不把单个约 30 秒样本写成完整 voice cloning 训练集。
- 不默认用户已授权第三方 voice cloning。
- 不替换当前全片音轨。

## 8. 下一步

- `next_voice_step`：基于该样本生成 10-15 秒最小声音试配。
- 试配对象应优先覆盖当前视频开头 / 结尾主持壳的短句，而不是直接替换全片。
- 试配后由用户 / ChatGPT 做听感复审，再决定是否进入更大范围音轨替换。
