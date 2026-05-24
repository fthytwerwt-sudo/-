# TTS 实际路线审计

## 实际路线

读取 `narration_tts_debug_sanitized.json` 和 `summary.json` 后确认：

```text
tts_actual_route:
  provider: aliyun_bailian
  api_route_family: aliyun_qwen_realtime_websocket
  model: qwen3-tts-instruct-flash-realtime
  voice: Serena
  voice_reference: not_loaded
  pacing_reference: generic pause map only; B audio pacing reference not loaded
  custom_voice_id_masked: not_present_in_runtime_debug
  target_model: not qwen3-tts-vc-realtime-2026-01-15
  used_b_voice: false
  used_b_pacing: false_or_only_weakly_reflected_by_pause_after
  local_tts_fallback_used: false
  macos_say_used: false
```

## 预期 B 路线

来自 `codex_source/locked_reference_registry.md`：

- `tts_15s_b_pacing_locked_20260427`：锁的是 B 版“停顿梗感”节奏，不是最终音色。
- `voice_sample2_cute_guide_voice_candidate_20260426`：可爱女生向导音候选，脱敏 custom voice 标识 `qwen-t...ac19`，目标模型记录为 `qwen3-tts-vc-realtime-2026-01-15`，仍未写成 final voice passed。

## 结论

本次 TTS 没有降级到 macOS say 或本地 fallback；它确实调用了阿里 / 百炼。但它不是预定 B 语音路线，而是普通 realtime TTS + 默认 voice `Serena`。
