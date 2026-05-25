# 20260525 MiniMax speech-2.8-hd 默认正片候选 TTS 路线切换

## 任务边界

- `task_status`: mechanism_route_switch_only
- `media_generated`: false
- `dist_media_modified`: false
- `full_video_generated`: false
- `full_narration_generated`: false
- `voice_validation`: not_advanced
- `content_validation`: not_advanced
- `send_ready`: false
- `final_voice_validated`: false
- `visual_master_locked`: false

## route_change_summary

- `old_default_tts_route`: aliyun_bailian / qwen3-tts-vc-realtime-2026-01-15 / qwen-t...ac19 B voice route
- `new_default_tts_route`: minimax
- `required_model`: speech-2.8-hd / MiniMax/speech-2.8-hd
- `selected_route_priority`: aliyun_bailian_proxy_to_minimax first, minimax_official_api fallback when official key exists
- `b_voice_scheme_role`: voice_feel_reference_only
- `non_minimax_publish_candidate_consequence`: blocked_publish_candidate_unavailable or internal_diagnostic_only

## files_updated

- `scripts/正片候选TTS路线_publish_candidate_tts_route.py`: added default MiniMax publish-candidate TTS route constants and validator.
- `scripts/发片候选预检套件_publish_candidate_preflight_suite.py`: added `publish_candidate_voice_gate`, `tts_route_report.json/md` output, review-pack required report, fixture validation support for passed/internal diagnostic cases.
- `codex_source/fixtures/publish_candidate_preflight_suite_cases.json`: added MiniMax pass, Aliyun Qwen fail, macOS say fail, MiniMax unavailable block, internal diagnostic non-MiniMax allowed cases.
- `tests/test_publish_candidate_voice_gate.py`: added standard-library tests for the five required cases.
- `scripts/生成第四期AI复盘系统发布候选片_generate_fourth_episode_ai_review_system_publish_candidate.py`: switched default publish-candidate TTS generation route to MiniMax via Bailian proxy; outputs `tts_route_report`.
- `scripts/生成第四期数据成果卡发布候选片_generate_fourth_episode_data_result_card_publish_candidate.py`: synced wrapper metadata and review-pack route report to MiniMax default.
- `scripts/生成新第四期选品初筛源比例无遮挡B语音修复候选片_generate_new_fourth_selection_source_ratio_no_mask_b_voice_fix_candidate.py`: guarded legacy B voice route so it blocks instead of producing a publish candidate; unreachable old `publish_candidate_ready_for_human_review` literals were downgraded to blocked/reference-only wording.
- `scripts/生成第二期横屏候选片_generate_second_episode_horizontal_publish_candidate.py`, `scripts/AI赚钱正片候选装配_ai_money_final_candidate_assembly.py`: guarded older Qwen/B-route publish-candidate runners so they emit a blocked `tts_route_report` and stop instead of completing with non-MiniMax TTS.
- `GPT数据源/05_文案路由规则.md`, `GPT数据源/07_AI知识类视频价值规则.md`, `GPT数据源/08_当前正式事实.md`, `codex_source/00_codex_readme.md`, `codex_source/01_execution_rules.md`, `codex_source/19_project_state_action_router.md`, `codex_source/21_codex_judgment_permission_matrix.md`: synced MiniMax route hard gate.
- `codex_log/latest.md`: recorded this route switch.

## validation

- `python_py_compile`: passed
- `fixture_json_parse`: passed
- `unit_tests`: `python3 tests/test_publish_candidate_voice_gate.py` passed, 5 tests
- `preflight_dry_run`: `codex_log/diagnostics/minimax_default_tts_route_switch_preflight_20260525_no_render/`
- `preflight_dry_run_result`: blocked as expected because no input `tts_route_report` or media was supplied
- `fixture_validation`: passed
- `grep_old_route_residue`: passed_with_expected_historical_residue; old Aliyun/Qwen/Serena strings remain only in historical docs, negative fixtures, detection fields, or legacy scripts guarded as blocked/reference-only.
- `dist_media_diff`: none for `.mp4/.wav/.mp3/.mov/.m4a`
- `api_key_printed`: false
- `api_key_written`: false

## DeepSeek

- `pre_supply_request`: `codex_log/supply_requests/20260525_minimax_default_tts_route_switch_pre_supply_request.json`
- `pre_supply_result`: blocked_invalid_context_pack
- `post_risk_review_request`: `codex_log/supply_requests/20260525_minimax_default_tts_route_switch_post_risk_review_request.json`
- `post_risk_review_result`: deepseek_passed
- `post_risk_review_pack`: `codex_log/deepseek_supply/20260525_minimax_default_tts_route_switch_post_risk_review/latest_supply_pack.md`
- `fallback_status`: not_used for post-risk review
- `not_deepseek_conclusion`: false for post-risk review
- `api_key_printed`: false
- `api_key_written`: false

## next_safe_action

- 下一次生成正片候选时，直接按 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd` 生成语音。
- 如果 MiniMax route 不可用，正片候选必须 blocked，不能自动回退阿里 Qwen TTS、Serena、macOS say 或本地低质 TTS。
