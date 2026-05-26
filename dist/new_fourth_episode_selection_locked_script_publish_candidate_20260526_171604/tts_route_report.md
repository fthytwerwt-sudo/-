# publish_candidate_voice_gate

- `status`: `blocked`
- `check_depth`: `structural_check_only`
- `blocked_reasons`:
  - `audio_missing_or_silent`
  - `audio_not_generated_or_missing`
- `warnings`:
  - `B 方案仅保留为 voice_feel_reference；正片候选必须使用 MiniMax speech-2.8-hd 或 MiniMax/speech-2.8-hd。`
  - `本 gate 只检查 TTS 路线与音频存在性字段；真实听感仍需要用户 / ChatGPT 人工复审。`
