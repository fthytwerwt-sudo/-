# MiniMax speech-2.8-hd 双路线最小试听测试报告

- `task_status = blocked`
- `selected_route = route_b`
- `blocked_reason = generated_audio_failed_technical_validation`
- `actual_endpoint_or_sdk = https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`
- `actual_model_name = MiniMax/speech-2.8-hd`
- `is_real_minimax_speech_2_8_hd = true`
- `product_activation_status = activated`
- `audio_generated = true`
- `voice_id_used_masked = female-tianmei`
- `auth_source_masked = authorized_runtime_config:formal_api_demo.local.toml`
- `api_key_printed = false`
- `api_key_written = false`

## Route Check

```json
{
  "route_a": {
    "route": "minimax_official_api",
    "endpoint": "https://api.minimax.io/v1/t2a_v2",
    "model": "speech-2.8-hd",
    "auth_available": false,
    "auth_source_masked": "none"
  },
  "route_b": {
    "route": "aliyun_bailian_proxy_to_minimax",
    "endpoint": "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "model": "MiniMax/speech-2.8-hd",
    "auth_available": true,
    "auth_source_masked": "authorized_runtime_config:formal_api_demo.local.toml",
    "auth_report": {
      "DASHSCOPE_API_KEY_present": false,
      "ALIYUN_API_KEY_present": false,
      "authorized_runtime_config_checked": true,
      "authorized_runtime_config_exists": true,
      "authorized_runtime_config_key_nonempty": true,
      "authorized_runtime_config_in_repo": false,
      "api_key_printed": false,
      "api_key_written": false
    },
    "official_capability_check": {
      "minimax_speech_tts_model_exists": true,
      "speech_2_8_hd_or_equivalent_exists": true,
      "supports_text_to_speech_audio_output": true,
      "supports_voice_id": true,
      "supports_speed": true,
      "supports_pitch": true,
      "supports_pause_tags": "tested_by_pause_tag_generation_when_audio_generated",
      "expected_audio_response_field": "output.data.audio (hex when output_format=hex)",
      "aliyun_bailian_minimax_text_only_not_tts": false
    },
    "voice_query_report": {
      "request_status_code": 200,
      "base_resp_status_code": 0,
      "base_resp_status_msg": "success",
      "request_id": "b6e5bc3a-d10a-914f-9970-3ce481d10561",
      "system_voice_count": 303,
      "preferred_voice_found": true,
      "selected_voice_id": "female-tianmei"
    },
    "actual_audio_response_observed": true,
    "aliyun_bailian_minimax_text_only_not_tts": false
  }
}
```

## Output Files

```json
{
  "activation_check": "/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/minimax_speech_2_8_hd_activation_check.mp3",
  "pause_tag": "/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/minimax_speech_2_8_hd_pause_tag.mp3",
  "plain": "/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/minimax_speech_2_8_hd_plain.mp3",
  "aliyun_b_voice_reference_10_15s": "/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/aliyun_b_voice_reference_10_15s.wav"
}
```

## Technical Validation

```json
{
  "pause_tag": {
    "ffprobe_result": {
      "passed": true,
      "duration_seconds": 15.768,
      "codec_name": "mp3",
      "sample_rate": 32000,
      "channels": 1,
      "bit_rate": "128870",
      "file_size_bytes": 254004
    },
    "ffmpeg_decode_result": {
      "passed": true,
      "stderr_tail": ""
    },
    "duration_check": {
      "duration_seconds": 15.768,
      "target_range_seconds": "10_to_15",
      "acceptable_range_seconds": "10_to_20",
      "passed_target": false,
      "passed_acceptable": true
    },
    "non_silent_check": {
      "passed": true,
      "mean_volume_db": "-24.0",
      "stderr_tail": "t 0.016531\n[Parsed_volumedetect_0 @ 0xae100ca80] n_samples: 0\nStream mapping:\n  Stream #0:0 -> #0:0 (mp3 (mp3float) -> pcm_s16le (native))\nPress [q] to stop, [?] for help\nOutput #0, null, to 'pipe:':\n  Metadata:\n    AIGC            : {\"Label\":\"1\",\"ContentProducer\":\"MiniMax\",\"ProduceID\":\"06649909c7a9924cacafe995ce6d4656\",\"ReservedCode1\":\"{\\\"SecurityData\\\":{\\\"Type\\\":\\\"TC260PG\\\",\\\"Version\\\":1,\\\"PubSD\\\":[{\\\"Type\\\":\\\"DS\\\",\\\"AlgID\\\":\\\"1.2.156.10197.1.501\\\",\\\"TBSData\\\":{\\\"Type\\\":\\\"LabelMataD\n    encoder         : Lavf62.12.100\n  Stream #0:0: Audio: pcm_s16le, 32000 Hz, mono, s16, 512 kb/s\n    Metadata:\n      encoder         : Lavc62.28.100 pcm_s16le\n[Parsed_volumedetect_0 @ 0xae100cf00] n_samples: 504047\n[Parsed_volumedetect_0 @ 0xae100cf00] mean_volume: -24.0 dB\n[Parsed_volumedetect_0 @ 0xae100cf00] max_volume: -8.9 dB\n[Parsed_volumedetect_0 @ 0xae100cf00] histogram_8db: 5\n[Parsed_volumedetect_0 @ 0xae100cf00] histogram_9db: 95\n[Parsed_volumedetect_0 @ 0xae100cf00] histogram_10db: 417\n[out#0/null @ 0xae100c780] video:0KiB audio:984KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown\nsize=N/A time=00:00:15.75 bitrate=N/A speed=1.97e+03x elapsed=0:00:00.00    \n"
    },
    "technical_passed": false
  },
  "plain": {
    "ffprobe_result": {
      "passed": true,
      "duration_seconds": 13.41,
      "codec_name": "mp3",
      "sample_rate": 32000,
      "channels": 1,
      "bit_rate": "129543",
      "file_size_bytes": 217140
    },
    "ffmpeg_decode_result": {
      "passed": true,
      "stderr_tail": ""
    },
    "duration_check": {
      "duration_seconds": 13.41,
      "target_range_seconds": "10_to_15",
      "acceptable_range_seconds": "10_to_20",
      "passed_target": true,
      "passed_acceptable": true
    },
    "non_silent_check": {
      "passed": true,
      "mean_volume_db": "-22.4",
      "stderr_tail": ": 0\nStream mapping:\n  Stream #0:0 -> #0:0 (mp3 (mp3float) -> pcm_s16le (native))\nPress [q] to stop, [?] for help\nOutput #0, null, to 'pipe:':\n  Metadata:\n    AIGC            : {\"Label\":\"1\",\"ContentProducer\":\"MiniMax\",\"ProduceID\":\"0664990a97ff6f5ff85edae69f4ed44a\",\"ReservedCode1\":\"{\\\"SecurityData\\\":{\\\"Type\\\":\\\"TC260PG\\\",\\\"Version\\\":1,\\\"PubSD\\\":[{\\\"Type\\\":\\\"DS\\\",\\\"AlgID\\\":\\\"1.2.156.10197.1.501\\\",\\\"TBSData\\\":{\\\"Type\\\":\\\"LabelMataD\n    encoder         : Lavf62.12.100\n  Stream #0:0: Audio: pcm_s16le, 32000 Hz, mono, s16, 512 kb/s\n    Metadata:\n      encoder         : Lavc62.28.100 pcm_s16le\n[Parsed_volumedetect_0 @ 0x8bac24900] n_samples: 429105\n[Parsed_volumedetect_0 @ 0x8bac24900] mean_volume: -22.4 dB\n[Parsed_volumedetect_0 @ 0x8bac24900] max_volume: -7.9 dB\n[Parsed_volumedetect_0 @ 0x8bac24900] histogram_7db: 5\n[Parsed_volumedetect_0 @ 0x8bac24900] histogram_8db: 60\n[Parsed_volumedetect_0 @ 0x8bac24900] histogram_9db: 248\n[Parsed_volumedetect_0 @ 0x8bac24900] histogram_10db: 1614\n[out#0/null @ 0x8bac24180] video:0KiB audio:838KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown\nsize=N/A time=00:00:13.40 bitrate=N/A speed=1.94e+03x elapsed=0:00:00.00    \n"
    },
    "technical_passed": true
  },
  "aliyun_b_voice_reference_10_15s": {
    "ffprobe_result": {
      "passed": true,
      "duration_seconds": 15.0,
      "codec_name": "pcm_s16le",
      "sample_rate": 32000,
      "channels": 1,
      "bit_rate": "512041",
      "file_size_bytes": 960078
    },
    "ffmpeg_decode_result": {
      "passed": true,
      "stderr_tail": ""
    },
    "duration_check": {
      "duration_seconds": 15.0,
      "target_range_seconds": "10_to_15",
      "acceptable_range_seconds": "10_to_20",
      "passed_target": true,
      "passed_acceptable": true
    },
    "non_silent_check": {
      "passed": true,
      "mean_volume_db": "-16.2",
      "stderr_tail": "0] Guessed Channel Layout: mono\nInput #0, wav, from '/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/aliyun_b_voice_reference_10_15s.wav':\n  Metadata:\n    encoder         : Lavf62.12.100\n  Duration: 00:00:15.00, bitrate: 512 kb/s\n  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 32000 Hz, mono, s16, 512 kb/s\n[Parsed_volumedetect_0 @ 0xc62c20480] n_samples: 0\nStream mapping:\n  Stream #0:0 -> #0:0 (pcm_s16le (native) -> pcm_s16le (native))\nPress [q] to stop, [?] for help\nOutput #0, null, to 'pipe:':\n  Metadata:\n    encoder         : Lavf62.12.100\n  Stream #0:0: Audio: pcm_s16le, 32000 Hz, mono, s16, 512 kb/s\n    Metadata:\n      encoder         : Lavc62.28.100 pcm_s16le\n[Parsed_volumedetect_0 @ 0xc62c20900] n_samples: 480000\n[Parsed_volumedetect_0 @ 0xc62c20900] mean_volume: -16.2 dB\n[Parsed_volumedetect_0 @ 0xc62c20900] max_volume: -1.1 dB\n[Parsed_volumedetect_0 @ 0xc62c20900] histogram_1db: 572\n[out#0/null @ 0xc62c20180] video:0KiB audio:938KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown\nsize=N/A time=00:00:15.00 bitrate=N/A speed=7.43e+03x elapsed=0:00:00.00    \n"
    },
    "technical_passed": true
  }
}
```

## B Voice Reference Cut

```json
{
  "found": true,
  "output_path": "/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/aliyun_b_voice_reference_10_15s.wav",
  "status": "cropped",
  "validation": {
    "ffprobe_result": {
      "passed": true,
      "duration_seconds": 15.0,
      "codec_name": "pcm_s16le",
      "sample_rate": 32000,
      "channels": 1,
      "bit_rate": "512041",
      "file_size_bytes": 960078
    },
    "ffmpeg_decode_result": {
      "passed": true,
      "stderr_tail": ""
    },
    "duration_check": {
      "duration_seconds": 15.0,
      "target_range_seconds": "10_to_15",
      "acceptable_range_seconds": "10_to_20",
      "passed_target": true,
      "passed_acceptable": true
    },
    "non_silent_check": {
      "passed": true,
      "mean_volume_db": "-16.2",
      "stderr_tail": "0] Guessed Channel Layout: mono\nInput #0, wav, from '/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/minimax_route_smoke/aliyun_b_voice_reference_10_15s.wav':\n  Metadata:\n    encoder         : Lavf62.12.100\n  Duration: 00:00:15.00, bitrate: 512 kb/s\n  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 32000 Hz, mono, s16, 512 kb/s\n[Parsed_volumedetect_0 @ 0xc62c20480] n_samples: 0\nStream mapping:\n  Stream #0:0 -> #0:0 (pcm_s16le (native) -> pcm_s16le (native))\nPress [q] to stop, [?] for help\nOutput #0, null, to 'pipe:':\n  Metadata:\n    encoder         : Lavf62.12.100\n  Stream #0:0: Audio: pcm_s16le, 32000 Hz, mono, s16, 512 kb/s\n    Metadata:\n      encoder         : Lavc62.28.100 pcm_s16le\n[Parsed_volumedetect_0 @ 0xc62c20900] n_samples: 480000\n[Parsed_volumedetect_0 @ 0xc62c20900] mean_volume: -16.2 dB\n[Parsed_volumedetect_0 @ 0xc62c20900] max_volume: -1.1 dB\n[Parsed_volumedetect_0 @ 0xc62c20900] histogram_1db: 572\n[out#0/null @ 0xc62c20180] video:0KiB audio:938KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown\nsize=N/A time=00:00:15.00 bitrate=N/A speed=7.43e+03x elapsed=0:00:00.00    \n"
    },
    "technical_passed": true
  }
}
```

## Human Review Focus

- naturalness
- guide_feeling
- prosody
- pause_timing
- emotion_arc
- sentence_transition
- ai_broadcast_feeling
- cute_but_not_childish
- voice_similarity_to_b_direction

## Status Boundaries

```json
{
  "voice_validation": "not_advanced",
  "content_validation": "not_advanced",
  "send_ready": false,
  "final_voice_validated": false,
  "visual_master_locked": false
}
```
