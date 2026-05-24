# 06 Audio SFX Rhythm Audit｜音效 / BGM / 节奏解析

## audio_analysis_status

```text
audio_analysis_status = limited
reason = local ASR unavailable; no SFX classifier; no separate music stem; analysis uses ffprobe, volumedetect, silencedetect, and visual rhythm.
```

## technical audio facts

- `audio_present = true`
- codec: `AAC LC`
- sample_rate: `44100 Hz`
- channels: `2`
- bitrate: about `125 kb/s`
- mean_volume: about `-14.3 dB`
- max_volume: `0.0 dB`
- detected silence pockets: around `03:05-03:06`, `04:52-04:55` 等少量位置；整体是持续音频流。

## audio_sfx_map

| timestamp | audio_event | sfx_type | visual_event_matched | rhythm_function | transfer_suggestion | risk |
| --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:08 | dense opening audio | unknown/likely title hit + voice | big title/host gesture | attention hook | use original-free soft hit only | copyright/SFX source unknown |
| 00:45-01:25 | continuous narration over document | voice + possible light BGM | document highlight | explain while proof visible | voiceover + subtle click on highlight | avoid noisy SFX over dense table |
| 02:05-02:55 | steady narration | voice | comparison card | method explanation | one soft pop per card change | do not turn comparison into game show |
| 02:55-03:35 | brief pauses around table scenes | silence pockets detected nearby | spreadsheet/result table | let viewer read | lower BGM / pause after table appears | table needs breathing room |
| 04:35-05:45 | continuous narration + slower proof screens | voice + likely BGM | research documents | longer proof phase | quiet bed, no dramatic impact | avoid making research/doc proof feel like ad hype |

## transfer guidance

- 可迁移的是“音效服务动作”的原则，不是原 BGM / 原音效。
- 新第四期可用：搜索框输入用轻 click / typing；商品卡被选中用 soft pop；候选表生成用 restrained ding；聊天框结论出现用轻微 settle sound。
- 不建议：强 glitch、过密 whoosh、强节奏鼓点、任何会抢表格阅读的音效。
- 若后续成片执行，必须重新使用可商用 / 自制 / 授权音效，不得从 reference 抽取音频。
