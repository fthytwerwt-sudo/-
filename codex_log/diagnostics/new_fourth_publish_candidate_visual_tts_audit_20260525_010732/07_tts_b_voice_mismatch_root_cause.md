# TTS B 语音不符根因

## 主因分类

```text
tts_mismatch_origin:
  wrong_model: true
  missing_voice_reference: true
  missing_pacing_reference: true
  provider_route_bypassed_voice_clone: true
  sanitized_config_missing_voice_id: true
  tts_prompt_missing_style: likely
  fallback_to_default_aliyun_voice: true
  unknown: false
```

## 解释

本次把“阿里 / 百炼 TTS 授权可用”错误等同为“B 语音可用并已执行”。实际 runtime 选择了 `qwen3-tts-instruct-flash-realtime` 的 `Serena` voice，没有加载 `voice_sample2` 候选自定义音色，也没有使用 `qwen3-tts-vc-realtime-2026-01-15`。

`tts_prosody_anchor_map` 提供的是分句、语气和停顿策略；它不能自动让 provider 继承 B 语音。B pacing reference 如果要生效，需要 TTS runner 明确读取 B 版 reference、转成节奏参数或做音频对照；本次只看到 chunk timeline 和 `pause_after`，没看到 B reference 的 runtime evidence。

## 修复原则

下一轮必须在 TTS debug 中记录脱敏字段：

- `expected_voice_route = b_voice_candidate_plus_b_pacing`
- `target_model = qwen3-tts-vc-realtime-2026-01-15`
- `custom_voice_id_masked = qwen-t...ac19`
- `b_pacing_reference_loaded = true`
- `voice = not Serena unless explicitly approved`

不得记录任何真实 key 或完整 secret。
