# 十五秒文案语速停顿试配 15s Copy Pacing Trial

## 本轮目标

- `已确认` 本轮只做《视频工厂》声音文案适配试听。
- `已确认` 不换音色、不重做 voice cloning、不重新裁剪 / 上传样本、不替换全片音轨。
- `已确认` 生成 A / B 两条 15 秒左右试听，用于判断语速、停顿和文案搭配。

## 用户确认状态

- 新样本2的音色底子可以继续用。
- 后续主要调语速、停顿和文案搭配。
- 用户喜欢“微反转 + 说话带梗 + 自然口语”。
- 已避开 `下一步从哪打`，使用真人更自然的表达。

## A / B 文案全文

### A 版：自然节奏

```text
我发现，做方案最痛苦的不是 PPT。
是你坐了一下午，资料开着，咖啡也开着，就第一行没开。
最后憋出一句：建议提升用户体验。
它永远不会错，也永远没用。
Prompt 调对，豆包才给能接着改的初稿。
```

### B 版：停顿梗感

```text
你以为做方案慢，是 PPT 难。
其实不是，是你在陪资料加班。
屏幕开着，文档开着，第一行死活不动。
你问豆包写方案，它也努力，给一堆看着像方案、用起来像空气的东西。
Prompt 调对，才有能接着改的初稿。
```

## A / B 风格差异

- A 版：更直接，信息更清楚，微反转保留，适合判断短内容自然度。
- B 版：停顿更清楚，梗感略强，适合判断轻吐槽和留白是否适配声音。

## model / voice / instructions

- synthesis model：`qwen3-tts-vc-realtime-2026-01-15`
- target_model：`qwen3-tts-vc-realtime-2026-01-15`
- create model：`qwen-voice-enrollment`（本轮未调用 create）
- voice：`qwen-t...ac19`（脱敏）
- 是否重新 create_custom_voice：`no`
- 是否使用 Serena：`no`
- 是否使用上一轮 A / B custom voice：`no`
- language_type：`Chinese`
- response_format：`pcm`
- sample_rate：`24000`
- optimize_instructions：`true`

### A instructions

```text
请参考新样本2的说话方式，保持自然口语、真人分享感和解释型节奏。
语气平实亲近，不要播音腔，不要广告腔，不要刻意表演。
整体节奏稍微利落一点，但不要赶。
重点句“永远不会错，也永远没用”要有一点轻吐槽感。
请控制在 15 秒左右自然说完。
```

### B instructions

```text
请参考新样本2的说话方式，保持自然口语、轻吐槽和熟人式分享感。
语气不要太嗨，不要夸张带货，不要综艺腔。
“陪资料加班”“看着像方案，用起来像空气”这些地方可以稍微停一下，让梗自然落地。
整体控制在 15 到 17 秒之间，停顿清楚，但不要拖沓。
```

## atempo

- A 版是否使用 atempo：`false`
- B 版是否使用 atempo：`false`

## 输出文件路径

- `A_15秒文案_自然节奏.txt`
- `B_15秒文案_停顿梗感.txt`
- `A_15秒文案_自然节奏.wav`
- `B_15秒文案_停顿梗感.wav`
- `A_voice_clone_tts_request_debug_sanitized.json`
- `B_voice_clone_tts_request_debug_sanitized.json`
- `run_summary.json`

## 技术验证结果

| 版本 | duration | codec | sample_rate | channels | mean_volume | loudnorm.input_i | ffmpeg 解码 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | `17.20s` | `pcm_s16le` | `24000 Hz` | `mono` | `-23.9 dB` | `-23.92` | `通过` |
| B | `16.32s` | `pcm_s16le` | `24000 Hz` | `mono` | `-23.4 dB` | `-23.67` | `通过` |

## 当前状态

- `technical_generation`：通过。
- `copy_pacing_status`：待用户听审。
- `voice_validation_status`：待用户 / ChatGPT 听感复审。
- `content_validation`：待用户 / ChatGPT 最终复审。
- `send_ready`：no。

## 禁止误写

- 本轮不等于声音通过。
- 本轮不等于最终音色已定。
- 本轮不等于文案最终定稿。
- 本轮不可替换全片音轨。
- 本轮不改变 `content_validation`。
- 本轮不改变 `send_ready`。
- 本轮未修改 `dist/latest_review_pack/full.mp4`。
- 本轮未修改 `dist/latest_review_pack/middle_preview.mp4`。
