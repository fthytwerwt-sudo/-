# voice_candidate_review_table_old_b_minimax

本表只用于旧 B 参考音频迁移到 MiniMax 后的人工试听复审。所有样本必须以旧 B 音色相似度为第一判断，不能把系统音色、男声方向或情绪更强直接等同于旧 B。

| candidate_id（候选 ID） | voice_id（声音 ID） | sample_path（试听路径） | prosody_version（韵律版本） | similar_to_old_b（是否像旧 B，待人工判断） | pause_feel（停顿感，待人工判断） | emotional_richness（情绪丰富度，待人工判断） | upward_tone（上扬感，待人工判断） | too_system_voice（是否系统音色替代，待人工判断） | non_silent（是否非静音，待复核） | user_choice（用户选择） | lock_status（锁定状态） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1_identity_match | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V1_identity_match.mp3` | V1_identity_match | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待用户选择 | pending_user_review |
| V2_prosody_optimized | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V2_prosody_optimized.mp3` | V2_prosody_optimized | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待用户选择 | pending_user_review |
| V3_emotion_rich | oldBMinimax20260528010200 | `codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/samples/V3_emotion_rich.mp3` | V3_emotion_rich | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待人工判断 | 待用户选择 | pending_user_review |
