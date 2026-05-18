# 20260519｜card_budget_gate 与 data_result_card 路由补强

## 本轮结论

- `已确认` 本轮只做《视频工厂》卡片判断机制补强，不重做第四期视频，不改变 HyperFrames 展示形式、视觉路线、动效路线、卡片皮肤或现有生成方式。
- `已确认` 新规则目标不是增加卡片数量，而是让 Codex 在视频执行前按最终文案、`script_to_timeline_map（文案到时间线映射表）` 和证据窗口，少量、准确、克制地判断卡片。
- `已确认` 第四期当前已有 4 张卡：`lg_001 judgment_card`、`lg_010 process_summary_card`、`lg_014 boundary_card`、`lg_030 ending_summary_card`。
- `已确认` 第四期时长约 `174.3s`，新 `card_budget_gate（卡片预算闸门）` 对 90-180 秒视频给出 `max_main_cards = 4`，当前总数不超预算。

## route_decision

- `project_route = video_factory`
- `task_type = mechanism_or_route_fix + project_file_change + code_debug + validation_dry_run`
- `large_task_gate = triggered`
- `lane = serial_only`
- `DeepSeek = fallback_local_only`
- `not_deepseek_conclusion = true`

## state_action_router

- `input_signal = 用户要求补强 data_result_card / card_budget_gate / cluster_merge_rule / evidence_window_protection，不改变 HyperFrames`
- `current_project_state = formal_operation_active + data_driven_operation_iteration`
- `trigger_mechanism = content_route_inference_function + card_placement_decision + codex_judgment_permission_gate`
- `selected_action = 补强机制文件、执行规则、可复用 helper、fixture/test、第四期 dry-run`
- `forbidden_action = regenerate_full_mp4 / change_HyperFrames_visual_motion_skin / advance_content_validation_or_send_ready`
- `done_when = dry-run report generated and validation passed`

## 机制补强

- `card_budget_gate（卡片预算闸门）`：写入 `GPT数据源/05_文案路由规则.md`，90 秒以内最多 3 张主卡，90-180 秒最多 4 张主卡，180 秒以上最多 6 张主卡；主卡间距默认 25 秒，硬下限 18 秒。
- `cluster_merge_rule（信息簇合并规则）`：写入 `GPT数据源/05_文案路由规则.md`，连续 1-5 个同一文案功能的 `line_group` 先合并为 `card_cluster`，不得每句数据 / 判断 / 总结单独插卡。
- `evidence_window_protection（证据窗口保护规则）`：写入 `GPT数据源/05_文案路由规则.md`，`middle_evidence / opening_evidence / ending_support` 证据窗口不得被卡片打断。
- `data_result_card_priority（数据成果卡优先级）`：写入 `GPT数据源/05_文案路由规则.md` 与 `codex_source/21_codex_judgment_permission_matrix.md`，只有同时具备真实数据、AI 判断、下一步变量和验证指标，才可选中 `data_result_card`。
- `card_type_selection_policy（卡片类型选择策略）`：写入 `GPT数据源/05_文案路由规则.md`，明确 `data_result_card / judgment_card / summary_card / boundary_card / process_summary_card` 的使用和避用条件。

## 可运行判断层

- `已新增` `scripts/卡片判断闸门_card_decision_gate.py`：只做 dry-run 判断，输出 `card_decision_dry_run`，不生成视频，不写 HyperFrames 视觉实现。
- `已新增` `codex_source/fixtures/卡片判断闸门_card_decision_gate_cases.json`：覆盖 7 个样例，包括数据簇合并、连续指标不拆卡、超预算优先保留数据成果卡、证据窗口保护、HyperFrames 不变、无真实数据不生成数据成果卡、数据来源不清不得生成确定判断卡。
- `已新增` `tests/test_card_decision_gate.py`：验证 helper 行为。

## 第四期 dry-run

- `报告路径`：`dist/fourth_episode_ai_review_system_publish_candidate/card_decision_dry_run.json`
- `original_cards = lg_001 judgment_card / lg_010 process_summary_card / lg_014 boundary_card / lg_030 ending_summary_card`
- `new_rule_selected_cards = 仍保留当前 4 张卡`
- `spacing_result`：`lg_001 -> lg_010` passed；`lg_010 -> lg_014` soft_spacing_warning（19.72s，大于硬下限 18s 但小于默认 25s）；`lg_014 -> lg_030` passed。
- `add_data_result_card_candidate`：识别到 `lg_019-lg_023` 可作为数据成果卡候选信息簇，但当前只包含指标名称 / 问题层 / 下一步变量 / 验证指标，没有真实数值，因此 `candidate_blocked_missing_real_metric_values`。
- `recommended_adjustment`：如果后续用户授权重做第四期并补齐真实数值，优先把 `lg_010 process_summary_card` 替换或合并为更高价值的 `data_result_card`；在当前素材和文案下不得新增确定数据结论。
- `evidence_window_protection_result = passed`
- `hyperframes_unchanged_check = passed_no_visual_motion_skin_change`
- `no_video_regenerated = true`

## 状态边界

- `content_validation = not_advanced`
- `send_ready = false`
- `current_data_goal_anchor_ready = false`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `video_regenerated = false`
- `hyperframes_visual_changed = false`
