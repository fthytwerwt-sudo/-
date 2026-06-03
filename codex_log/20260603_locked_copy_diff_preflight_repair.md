# 20260603 locked_copy_diff_preflight 修复记录

## route_decision

- project_route: video_factory
- task_type: code_execution_debug + mechanism_repair + project_file_change
- selected_state: locked_copy_diff_preflight_required + self_repair_audit_required + mandatory_commit_push_required
- write_allowed: preflight script + tests + fixture + this dated log
- forbidden: 不改 locked_final_script / final copy / full.mp4 / TTS audio / final.srt / final.ass / cards / source material / dist/latest_review_pack / content_validation / send_ready / voice_validation / visual_master_locked

## root cause repaired

已确认：旧 `locked_copy_diff_preflight()` 只读取 `summary / content_route / tts_map` 里的 `actual_subtitle_text / actual_tts_text / actual_card_text` 字段。

问题是它没有真实读取并比较：

- `script_to_timeline_map.line_groups[].narration_text`
- TTS route report 的 `segment_reports[].tts_text`
- `final.srt`
- `final.ass`
- burned subtitle overlay source / function output text
- `card_placement_decision.card_groups[].card_text`
- title card text

因此第五期候选片里 `subtitle_lines()` 把六行字幕截到四行时，旧预检仍能写成 passed。

## implemented

- `scripts/发片候选预检套件_publish_candidate_preflight_suite.py`
  - 新增 SRT / ASS parser。
  - 新增 TTS input text extractor。
  - 新增 `script_to_timeline_map.narration_text` comparison。
  - 新增 card text extractor 与 card semantic overreach check。
  - 新增 title card / opening line subcheck。
  - `locked_copy_diff_preflight` 现在输出 `subchecks` 与 `failed_subchecks`。
  - `run()` / CLI 新增：
    - `--tts-route-report`
    - `--card-placement-decision`
    - `--final-srt`
    - `--final-ass`
    - `--burned-subtitle-text`
  - 任一 locked copy 子检查缺失或失败，都会让 `locked_copy_diff_preflight.status = blocked`，并通过总 suite 的 `failed_gates` 阻断总报告。

## regression coverage

- `tests/test_publish_candidate_preflight_tolerance.py`
  - 新增 `test_locked_copy_subtitle_truncation_blocks`
  - 新增 `test_locked_copy_split_subtitle_full_text_passes`

- `codex_source/fixtures/publish_candidate_preflight_suite_cases.json`
  - 新增 `locked_copy_subtitle_truncates_six_lines_blocks`
  - 新增 `locked_copy_split_subtitle_full_text_passes`

## local verification

- `python3 -m unittest tests.test_publish_candidate_preflight_tolerance.PublishCandidateToleranceTests.test_locked_copy_subtitle_truncation_blocks tests.test_publish_candidate_preflight_tolerance.PublishCandidateToleranceTests.test_locked_copy_split_subtitle_full_text_passes`
  - result: passed

- `python3 -m py_compile scripts/发片候选预检套件_publish_candidate_preflight_suite.py`
  - result: passed

- `python3 -m unittest tests.test_publish_candidate_preflight_tolerance`
  - result: passed, 6 tests

- `python3 -m json.tool codex_source/fixtures/publish_candidate_preflight_suite_cases.json >/dev/null`
  - result: passed

- `python3 -m unittest tests.test_publish_candidate_voice_gate tests.test_minimax_b_voice_identity_lock tests.test_publish_candidate_preflight_tolerance`
  - result: passed, 28 tests

## readonly check against fifth episode artifact

只读调用新 `locked_copy_diff_preflight()` 读取第五期本地候选片产物，未写回 `dist/`。

结果：

- status: blocked
- failed_subchecks:
  - subtitle_copy_match
  - ass_copy_match
  - burned_subtitle_copy_match
  - card_text_semantic_match
- subtitle missing_text: `有人整理素材。有人做下一版测试。`

说明：修复后的 preflight 能抓到第五期现有字幕截断问题；本轮未修视频、不重生成字幕、不重生成 TTS。

## status boundary

- did_not_modify_video: true
- did_not_modify_copy: true
- did_not_regenerate_tts: true
- did_not_modify_subtitles: true
- did_not_modify_cards: true
- did_not_change_mechanism_files: true
- content_validation_not_advanced: true
- send_ready_not_advanced: true
- voice_validation_not_advanced: true
- visual_master_locked_not_advanced: true
