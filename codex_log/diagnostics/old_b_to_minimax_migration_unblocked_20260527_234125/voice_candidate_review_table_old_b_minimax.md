# voice_candidate_review_table_old_b_minimax

本轮未生成可试听样本；原因是缺少 MiniMax 官方 `MINIMAX_API_KEY`，不能调用官方 `/v1/files/upload` 获取 `file_id`，也不能创建 cloned `voice_id`。

| candidate_id（候选 ID） | voice_id（声音 ID） | sample_path（试听路径） | similar_to_old_b（是否像旧 B，待人工判断） | pause_feel（停顿感，待人工判断） | emotional_richness（情绪丰富度，待人工判断） | upward_tone（上扬感，待人工判断） | too_system_voice（是否系统音色替代，待人工判断） | user_choice（用户选择） | generation_status（生成状态） | lock_status（锁定状态） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1_identity_match | pending_minimax_official_auth | - | - | - | - | - | - | - | not_generated | blocked |
| V2_prosody_optimized | pending_minimax_official_auth | - | - | - | - | - | - | - | not_generated | blocked |
| V3_emotion_rich | pending_minimax_official_auth | - | - | - | - | - | - | - | not_generated | blocked |
