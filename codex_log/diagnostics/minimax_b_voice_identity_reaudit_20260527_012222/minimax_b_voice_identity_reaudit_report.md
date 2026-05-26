# MiniMax B 声音身份重审与候选包报告

- `status`: `completed_with_reaudited_voice_candidates`
- `video_generated`: `false`
- `full_narration_regenerated`: `false`
- `copy_changed`: `false`
- `current_video_modified`: `false`

## 上一轮女声候选

- `female-shaonv / female-shaonv-jingpin / female-yujie`: `rejected_by_user`
- `reason`: `wrong_gender_and_wrong_voice_identity`
- `future_use_allowed`: `false`

## B 声音重审结论

- `inferred_gender`: `male_or_male_leaning`
- `inferred_timbre`: `low_pressure_natural_male_leaning_companion_tone`
- `pause_style`: `moderate_to_clear_boundary_pause_with_joke_timing`
- `confidence`: `medium`
- `human_audio_reference_review_needed`: `true`

## 新候选试听

| candidate_id | voice_id | voice_name | prosody_version | sample_path | duration |
| --- | --- | --- | --- | --- | --- |
| BMALE_01_v1_identity_stable | male-qn-qingse | 青涩青年音色 | v1_identity_stable | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_01_male-qn-qingse_v1_identity_stable.mp3 | 17.388s |
| BMALE_01_v2_emotional_rich | male-qn-qingse | 青涩青年音色 | v2_emotional_rich | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_01_male-qn-qingse_v2_emotional_rich.mp3 | 19.26s |
| BMALE_02_v1_identity_stable | male-qn-daxuesheng | 青年大学生音色 | v1_identity_stable | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_02_male-qn-daxuesheng_v1_identity_stable.mp3 | 16.704s |
| BMALE_02_v2_emotional_rich | male-qn-daxuesheng | 青年大学生音色 | v2_emotional_rich | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_02_male-qn-daxuesheng_v2_emotional_rich.mp3 | 18.576s |
| BMALE_03_v1_identity_stable | Chinese (Mandarin)_Gentleman | 温润男声 | v1_identity_stable | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_03_Chinese_Mandarin_Gentleman_v1_identity_stable.mp3 | 16.38s |
| BMALE_03_v2_emotional_rich | Chinese (Mandarin)_Gentleman | 温润男声 | v2_emotional_rich | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_03_Chinese_Mandarin_Gentleman_v2_emotional_rich.mp3 | 17.46s |
| BMALE_04_v1_identity_stable | Chinese (Mandarin)_Gentle_Youth | 温润青年 | v1_identity_stable | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_04_Chinese_Mandarin_Gentle_Youth_v1_identity_stable.mp3 | 15.876s |
| BMALE_04_v2_emotional_rich | Chinese (Mandarin)_Gentle_Youth | 温润青年 | v2_emotional_rich | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_04_Chinese_Mandarin_Gentle_Youth_v2_emotional_rich.mp3 | 17.064s |
| BMALE_05_v1_identity_stable | Chinese (Mandarin)_Sincere_Adult | 真诚青年 | v1_identity_stable | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_05_Chinese_Mandarin_Sincere_Adult_v1_identity_stable.mp3 | 16.812s |
| BMALE_05_v2_emotional_rich | Chinese (Mandarin)_Sincere_Adult | 真诚青年 | v2_emotional_rich | codex_log/diagnostics/minimax_b_voice_identity_reaudit_20260527_012222/samples/BMALE_05_Chinese_Mandarin_Sincere_Adult_v2_emotional_rich.mp3 | 17.748s |

## 声音身份锁

- `status`: `pending_user_review`
- `expected_b_minimax_voice_id`: `null`
- `required_gender_direction`: `male_or_male_leaning`
- `forbidden_voice_ids`: `female-tianmei, female-shaonv, female-shaonv-jingpin, female-yujie`
- `human_voice_review_status`: `pending_user_review`
- `timbre_change_allowed`: `false`
