# 新第四期成片视觉 / TTS 路线只读诊断摘要

## 结论状态

- status: completed_read_only_diagnosis
- diagnostic_object: `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4`
- narration_object: `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/narration.wav`
- captions_object: `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/captions.srt`
- video_regenerated: false
- tts_regenerated: false
- scripts_modified: false
- media_modified: false
- content_validation: pending_user_chatgpt_review
- send_ready: false
- voice_validation: failed_user_feedback
- visual_master_locked: false

## 视觉主因

已确认：源素材 V001 / V003 / V004 同类时间段没有成片里这种大面积洗白。`visual_with_captions.mp4` 与 `visual_no_audio.mp4` 中多处画面仍可读，但最终 `full.mp4` 出现大面积白屏 / 洗白和边缘遮挡。

最可能主因：最终装配阶段的 strengthened privacy redaction / whiteout layer 过强、范围过大或叠加到了主体信息区。审片包 `privacy_risk_check.json` 也明确记录 `product names, prices, commission/monthly sales and table values are masked or washed out`，这与抽帧观察一致。

- gray_border_origin: privacy edge masks + canvas/edge padding / left-top protective bands
- whiteout_origin: final-stage strengthened redaction / whiteout privacy mask over product and table body
- black_block_origin: right account/sidebar privacy mask
- source_material_has_issue: false for the reported large whiteout/black block pattern
- render_pipeline_added_issue: true

## TTS 主因

已确认：本片实际走的是阿里 / 百炼普通 realtime TTS 路线：`qwen3-tts-instruct-flash-realtime` + `Serena`。这不等于项目预定 B 语音。

项目里的 B 语音路线应区分两层：

- B pacing reference: `tts_15s_b_pacing_locked_20260427`，对应 `B_15秒文案_停顿梗感.wav`，锁的是停顿梗感 / 语速节奏。
- voice candidate: `voice_sample2_cute_guide_voice_candidate_20260426`，脱敏 custom voice 标识 `qwen-t...ac19`，目标模型记录为 `qwen3-tts-vc-realtime-2026-01-15`，仍是 candidate / pending，不是最终声音通过。

本次 runtime 没有证据显示加载了上述 custom voice 或 B pacing 音频对照；只把通用韵律分句和 pause 参数传给了普通 `Serena` voice。

## 最小修复优先级

1. 先修视觉层：关闭或重做 final-stage broad whiteout，把隐私遮挡从“大面积洗白主体”改为定点模糊 / 遮挡敏感字段，同时保持表格机制可读。
2. 再修 TTS route：把 TTS provider 从 `qwen3-tts-instruct-flash-realtime + Serena` 切到 B 路线所需的 custom voice / voice clone runtime，并把 B pacing reference 真正接入生成节奏。

本轮未执行修复。下一轮不得直接继续发布，必须先重生成修复候选并重新人审。
