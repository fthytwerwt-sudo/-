# 20260601｜恢复素材证据闸门 material_evidence_gate

## task_result

- `status`: `mechanism_connected_not_video_delivery`
- `target_delivery`: `material_evidence_gate_restored_and_connected_to_publish_candidate_preflight_suite`
- `branch`: `codex/restore-material-evidence-gate-20260601`
- `base_ref`: `origin/main`

## restored_scope

- `已确认` 本轮从 `stash@{0}^3` 选择性恢复了 `scripts/素材证据闸门_material_evidence_gate.py`。
- `已确认` 本轮从 `stash@{0}^3` 选择性恢复了 `tests/test_material_evidence_gate.py`。
- `已确认` 本轮从 `stash@{0}^3` 选择性恢复了 `codex_source/fixtures/素材证据闸门_material_evidence_gate_cases.json`。
- `已确认` 本轮没有整包 `git stash apply`，没有恢复整个 `stash@{0}^3`。

## preflight_connection

- `已确认` `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` 新增 `material_evidence_gate_preflight`。
- `已确认` 预检套件会调用 `scripts/素材证据闸门_material_evidence_gate.py`，生成 `material_evidence_contract.json`、`line_group_evidence_gate_report.json` 与 `auto_storyboard_preflight_report.json`。
- `已确认` 若 `auto_edit_allowed != true` 或素材证据闸门返回阻断原因，整体 `publish_candidate_preflight_suite` 会进入 `blocked`。
- `已确认` `material_detail_report` 可由 `--material-detail-report` 显式传入；若未传，则从 `material_parse_pack.material_detail_report_path` 读取，避免破坏现有调用方。

## status_boundary

- `video_generated`: `false`
- `audio_generated`: `false`
- `image_generated`: `false`
- `tts_api_called`: `false`
- `external_api_called_for_media`: `false`
- `copy_changed`: `false`
- `content_validation_advanced`: `false`
- `send_ready_advanced`: `false`
- `voice_validation_advanced`: `false`
- `final_voice_validated_advanced`: `false`
- `visual_master_locked_advanced`: `false`
- `dist_latest_review_pack_modified`: `false`
- `public_untracked_committed`: `false`

## deepseek_supply_gate

- `supply_request_created`: `true`
- `deepseek_call_attempted`: `true`
- `deepseek_actual_participation`: `deepseek_passed`
- `fallback_status`: `not_used`
- `not_deepseek_conclusion`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `token_usage_expectation_check`: `token_decrement_expected`
- `token_usage_observed_by_codex`: `not_available_user_check_required`
- `note`: `临时供料输出未纳入本轮提交范围；本轮允许提交范围仍只限恢复脚本、测试、fixture、预检套件与日志。`

## validation_plan

必须验证：

1. `python3 -m py_compile scripts/素材证据闸门_material_evidence_gate.py`
2. `python3 -m py_compile scripts/发片候选预检套件_publish_candidate_preflight_suite.py`
3. `python3 -m unittest tests.test_material_evidence_gate`
4. `python3 -m unittest tests.test_material_parse_pack_reuse_gate`
5. `python3 -m unittest tests.test_publish_candidate_preflight_tolerance`
6. `git diff --cached --check`
7. staged diff secret scan

## done_when

本轮只有在相关验证通过、显式暂存范围不含 `public/`、`dist/`、媒体文件或 secret，并且 commit + push + remote readback 完成后，才能写 `completed`。
