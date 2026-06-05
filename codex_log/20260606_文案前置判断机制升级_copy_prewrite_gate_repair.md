# 20260606｜文案前置判断机制升级 copy_prewrite_gate_repair

## 1. task_status

- `task_result.status = copy_prewrite_gate_repair_completed_git_sync_required`
- `project_route = video_factory`
- `current_phase = formal_operation_active`
- `task_type = mechanism_or_route_fix + project_file_change + copy_mechanism_repair + validation_sync_repair`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`

## 2. route_decision

- `project_route = video_factory`
- `responsibility_layer = mechanism_fix_layer + project_judgment_layer + validation_layer + sync_layer`
- `allowed_changes`: `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`、`review_loop/learning_ledger/current_copy_revision_handoff.md`、`review_loop/learning_ledger/next_episode_bet_card.md`、`review_loop/learning_ledger/operation_learning_memory.md`、`codex_log/latest.md`、本日志。
- `forbidden_changes`: raw_copy、records、screenshots、dist、public、视频 / 音频 / 字幕 / 卡片 / 成片候选片、API key / token / secret、本地隐私配置。
- `deepseek_supply_gate`: 当前无可调用 DeepSeek 工具入口，本轮标记 `fallback_local_only`、`not_deepseek_conclusion = true`、`token_usage_expectation_check = not_observable`。

## 3. mechanism_gap_found

- 已有规则：风格偏好、文案生产流程、颗粒度配比、对标文案话语机制、说人话标准、素材证据闸门、locked copy 契约。
- 缺口：已有规则没有强制压成写稿前判断顺序；复盘词、机制词、制作词容易直接进入最终口播；正式文案可以过早进入 locked copy 或执行 prompt。
- 本轮修复：补齐 `copy_type_router`、`plain_language_translation_gate`、`human_problem_first_gate`、`copy_from_review_handoff_gate` 和 `prewrite_copy_decision_card`。

## 4. files_changed

- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`
- `review_loop/learning_ledger/current_copy_revision_handoff.md`
- `review_loop/learning_ledger/next_episode_bet_card.md`
- `review_loop/learning_ledger/operation_learning_memory.md`
- `codex_log/latest.md`
- `codex_log/20260606_文案前置判断机制升级_copy_prewrite_gate_repair.md`

## 5. mechanism_updates

- `copy_type_router`: 写稿前先判断教学视频、经验口播、真实项目复盘、带噱头观点稿、执行展示稿、经验口播 + 少量证据展示。
- `plain_language_translation_gate`: 后台词转人话词表进入 04 和 15；最终口播裸出后台词默认 `AI_tone_risk`。
- `human_problem_first_gate`: 15 新增“先讲人的麻烦，再让工具出现”的验收问题和阻断条件。
- `copy_from_review_handoff_gate`: 复盘数据先转成保留、只改、不改、人话说法，再进入文案层。
- `prewrite_copy_decision_card`: 04 内嵌写稿前判断卡模板；05 明确卡先于 `locked_copy_contract`。

## 6. V005_followup_default

- `copy_type = hybrid_experience_with_evidence（经验口播 + 少量证据展示）`
- `why_not_teaching_video = 下一期默认讲真实判断和具体麻烦，不是教完整 Codex 剪辑教程。`
- `what_to_keep = Codex + 普通人赚钱题眼、真实项目经验、诚实边界。`
- `single_change_this_round = 把大题眼压到一个具体证明场景，优先修前 0-8 秒承接。`
- `forbidden_voiceover_terms = 开头 / 中段 / 承接 / 变量 / 指标 / 机制 / 文案层 / 数据闭环 / 字幕断句 / 文案画面对齐`

## 7. validation

- `grep_copy_type_router = passed`
- `grep_plain_language_translation_gate = passed`
- `grep_human_problem_first_gate = passed`
- `grep_prewrite_copy_decision_card = passed`
- `git_diff_check = passed`
- `forbidden_path_diff_check = passed`
- `no_raw_copy_modified = true`
- `no_formal_script_generated = true`
- `no_next_video_prompt_generated = true`
- `no_forbidden_status_promotion = true`

## 8. not_advanced

- 未生成下一期正式文案。
- 未生成下一条视频执行 prompt。
- 未修改 `review_loop/copy_iteration/*/*_copy_v1_raw.md`。
- 未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。
- 未修改 `dist/`、`public/`、`review_loop/records/`、`review_loop/screenshots/`。

## 9. git_sync_note

- 本轮仍需 path-limited stage、staged secret scan、commit、push 和 remote HEAD readback 后，最终才允许在 Codex 回报中写 `completed_allowed = true`。
- `unrelated_dirty_files = public/`
