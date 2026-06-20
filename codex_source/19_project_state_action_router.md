# Project State Action Router 项目状态动作总控器

## 0A. formal_operation current route

当前状态默认识别为 `formal_operation_active（正式运营中）`。

运营数据链路：

`operation_data_intake -> operation_review -> operation_next_variable_decision`

旧 `gray_test_data_intake / post_publish_gray_test` 只作为历史兼容别名。缺 `codex_log/current_operation_target.md` 或 `review_loop/operation_records_index.md` 时，运营数据任务必须 blocked。

## 1. 文件定位

本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。

它解决的问题不是“任务属于哪个项目”，而是：路由已确定后，当前项目处于什么状态、应该触发哪条机制、下一步该做什么、做到哪里算完成。

它不替代：

- `AGENTS.md` 的 `route_decision（路由判断）`
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` 的 `workflow_route_decision（工作流归位判断）`
- `codex_source/01_execution_rules.md` 的执行规则
- `Completion Relay Gate（补全接力闸门）`
- `Reference-to-Execution Contract（参考到执行落地契约）`
- `GPT数据源/08_当前正式事实.md`
- `dist/latest_review_pack/summary.json`

## 2. 每轮执行前必须输出 state_action_router

每次 Codex 任务必须先输出 `route_decision（路由判断）`。

在 `route_decision` 成立后，必须先读取 `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` 并输出：

```text
workflow_route_decision:
  workflow_type:
  reason:
  must_read:
  required_handoff:
  forbidden_status:
  blocked_if:
```

随后、进入具体执行前，必须再输出：

```text
state_action_router:
  input_signal:
  current_project_state:
  fact_source_arbitration:
    primary_source:
    secondary_sources:
    conflict_detected:
    conflict_resolution:
  inferred_state:
  confidence:
  trigger_mechanism:
  selected_action:
  forbidden_action:
  must_read_files:
  done_when:
  blocked_if:
  feedback_update_required:
```

字段规则：

- `input_signal`：本轮触发信号，来自用户输入、仓库状态、执行结果、复盘数据、素材或冲突。
- `current_project_state`：从 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 的 `project_state_table` 中选择，必要时可写多个状态。
- `fact_source_arbitration`：说明以哪个事实源为准；若冲突，写裁决结果。
- `inferred_state`：对当前状态的判断，不是动作名。
- `confidence`：只能写 `high / medium / low`。
- `trigger_mechanism`：触发的下层机制，例如 `review_loop`、`content_route_card`、`editing_inference_function`、`quality_issue_classifier`、`Reference-to-Execution Contract`、`Completion Relay Gate`。
- `selected_action`：本轮最小可执行动作。
- `forbidden_action`：本轮明确禁止动作，尤其是状态推进、API、secret、媒体产物修改。
- `done_when`：本轮动作完成标准。
- `blocked_if`：必须阻断的条件。
- `feedback_update_required`：执行结果是否需要更新 latest、dated log、路径索引、机制文件或 missing fields。

`workflow_route_decision` 缺失时，`state_action_router` 不得把任务推进到具体执行；必须先补工作流归位或 blocked。

## 3. 触发优先级

```text
P0:
  - status_conflict
  - old_branch_or_old_source_residue
  - technical_preview_not_delivery
  - completion_truth_preflight_router
  - voice_route_conflict_gate
  - publish_candidate_required
  - formal_operation_delivery_blocked
  - missing_gray_test_data
  - forbidden_status_promotion_risk
  - evidence_missing_for_content_claim
  - user_current_instruction_conflicts_with_repo

P1:
  - mechanism_written_but_unverified
  - Codex partial completion risk
  - workflow_route_decision_missing
  - workflow_entry_routing_index_needed
  - material_delta_type_router
  - ambiguous_goal_clarification_needed
  - reference_contract_needed
  - missing inference function
  - data_goal_anchor_needed
  - current_data_goal_anchor_required
  - current_data_goal_anchor_missing
  - current_data_goal_anchor_waiting_data
  - codex_execution_structure_drift_risk
  - GPT Project package stale

P2:
  - path stale
  - historical mirror noise
  - efficiency / repeated explanation risk
```

处理顺序：

1. 先处理 P0 状态冲突、旧口径残留、灰度数据缺失和禁止状态推进风险。
2. 再处理 P1 机制未验证、推理函数缺失、GPT Project 静态包落后。
3. 最后处理 P2 路径过期、历史镜像噪声和重复解释效率问题。

如果 P0 未解决，不得进入 P1 / P2 的执行动作。

## 4. Codex 动作策略

```text
if state = gray_test_waiting_data:
  action = ask for / ingest data, update missing fields, do not write new copy

if state = mechanism_repair_needed:
  action = repair specified mechanism only, do not touch video status

if state = workflow_route_decision_missing:
  action = read codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md, output workflow_route_decision with workflow_type / reason / must_read / required_handoff / forbidden_status / blocked_if, and block write / video / audio / status promotion until it exists

if state = workflow_entry_routing_index_needed:
  action = repair the Codex entry routing index only, keep it short, update affected entry files and minimal fixtures/logs, do not add a new big mechanism or promote project status

if state = ambiguous_goal_clarification_needed:
  action = stop concrete execution, list 2-5 possible user-goal layers, require ChatGPT/user confirmation of the primary target or write explicit default assumptions / risks / allowed changes / blocked_if before creating any Codex execution prompt

if state = implementation_design_needed:
  action = require implementation_design_layer before Codex execution; verify target_effect / codex_capability_boundary / confirmed_capabilities / unverified_capabilities / preferred_execution_route / fallback_routes / capability_probe_tasks / done_when / blocked_if; if missing and this task affects tool choice, execution route, visual quality, API calls, fallback, validation, or project mechanism, output blocked_need_implementation_design_layer or implementation_design_request instead of guessing

if state = engineering_line_collaboration_gate_needed（需要工程线协作闸门）:
  action = classify engineering_depth_router（工程深度路由器） first; then apply decision_authority_matrix（决策权矩阵）; if file changes are needed, require per_file_detail_plan_gate（单文件细节方案闸门） before implementation; finish with execution_budget_gate（执行预算闸门） and collaboration_effectiveness_check（协作有效性检查）

if state = per_file_detail_plan_required（需要单文件细节方案）:
  action = output purpose / inputs / outputs / core_decisions / route_rules / blocked_if / examples / validation / user_review_points for every new or modified file before claiming completed

if state = engineering_overdesign_risk（工程化过度风险）:
  action = downgrade to L0 / L1 / L2 if task does not need full system line; block if simple task is forced into L3 without evidence

if state = supply_source_arbitration_required:
  action = create retrieval_manifest, run repo source_readback, create retrieval_gap_report, and decide deepseek_trigger_decision before file modification

if state = rag_engineering_line_required:
  action = require executable RAG engineering line before RAG / vector / retrieval / supply / DeepSeek-risk-review mechanism writes; verify contract_layer, builder_layer, validator_layer, router_hook_layer, acceptance_test_layer, failure_route_layer, and trace_log_layer before completed

if state = pre_supply_pack_required:
  action = run scripts/rag_supply_pack_builder.py --task-request <task_request.json> --out <pre_supply_pack.json>, then run scripts/rag_supply_pack_validator.py --pack <pre_supply_pack.json>; block write if source_path, line_range, chunk_id, exact snippet, or readback is missing

if state = mid_task_supply_required:
  action = run scripts/rag_mid_task_supply_builder.py --child-task-state <child_task_state.json> --out <mid_task_supply_pack.json> when missing_context, validation_failure_logs, conflict_points, or high-risk writes appear; continue only if continue_allowed = true

if state = failure_route_required:
  action = run scripts/rag_failure_route_resolver.py --failure-event <failure_event.json> --out <failure_route.json>; route failures to RAG_supply_bus, RAG_sync_bus, fact_source_arbitration, validation_repair, human_decision_gate, completion_truth_check, or git_sync_gate, never just retry

if state = trace_event_required:
  action = run scripts/rag_trace_event_writer.py --event <trace_event.json> --out codex_log/rag_engineering_line/trace_events.jsonl; record input_signal, supply_used, files_read, files_modified, validation_result, failure_route_if_any, and next_safe_step

if state = post_commit_vector_sync_gate_required:
  action = after any source commit that changes indexable text files, run scripts/post_commit_vector_sync_gate.py --mode finish without asking the user; if sync is required, build source_inventory and chunk_manifest, call Alibaba embedding API, upsert DashVector, run retrieval_probe with source_readback, write sync evidence, then commit/push evidence; if sync fails, write vector_sync_blocked and do not claim RAG current

if state = deepseek_review_conditionally_required:
  action = create_supply_request, run DeepSeek review / risk audit / conflict second opinion, and read review pack before high-risk file modification

if state = deepseek_deep_file_supply_required:
  action = only after deepseek_trigger_decision = true, create_supply_request with deep_supply_mode enabled, run deep_file_prefetch, require relevant_file_bundle / exact_snippet_pack / dependency_map / risk_and_conflict_report / codex_next_input, then let active_write_executor continue with source readback

if state = deepseek_mid_task_incremental_supply_required:
  action = create incremental_supply_request with current_child_task, files_already_read, will_modify_files, conflict_points, and failed_validation_logs; run mid_task_incremental_supply before continuing

if state = deepseek_not_deeply_participated:
  action = mark blocked or deepseek_not_deeply_participated when user required deep participation but DeepSeek real call, relevant_file_bundle, exact_snippet_pack, or mid-task/post risk supply is missing

if state = deepseek_pre_supply_missing:
  action = run_deepseek_pre_supply or mark fallback_local_only / blocked before write

if state = deepseek_post_review_missing:
  action = run_deepseek_post_risk_review before completion claim

if state = deepseek_claim_without_token_usage:
  action = run token_usage_expectation_check; do not write DeepSeek deep participation

if state = codex_vertical_completion_missing:
  action = run_codex_vertical_completion across affected files, schema, fixture, logs, and package

if state = process_boot_required:
  action = read_full_process_entries, output process_boot_report, treat GPT prompt as prompt_delta only, build required_output_inventory, detect locked_items / allowed_changes / forbidden_changes, and block if complete flow is not loaded

if state = publish_candidate_inventory_required:
  action = build publish_candidate_required_inventory, verify locked_copy_contract / content_route_card_v2 / card_placement_decision / script_to_timeline_map / tts_prosody_anchor_map / visual_evidence_check / subtitle_card_overlap_check / publish_candidate_checklist / data_goal_alignment_check / review_pack / remaining_blockers, and block or continue if any required item is missing without not_applicable_reason

if state = publish_candidate_preflight_suite_required:
  action = run scripts/发片候选预检套件_publish_candidate_preflight_suite.py in --no-render mode before export; require line_level_alignment_preflight / line_visual_tolerance_preflight / near_equivalent_material_substitution_preflight / tts_route_and_prosody_preflight / publish_candidate_voice_gate / b_voice_feel_minimax_preflight / card_decision_preflight / forbidden_action_preflight / visual_evidence_readability_preflight / locked_copy_diff_preflight / publish_candidate_user_standard_preflight / completion_truth_preflight; write reports into review_pack requirement; block export and completion if any required gate is missing or failed

if state = line_level_alignment_preflight_required:
  action = verify script_to_timeline_map is line_group-level and each line_group has narration, source_timecode, expected/actual visual, allowed/forbidden visuals, evidence strength, alignment status, mismatch reason, and repair action; block paragraph-only mapping or unresolved visual mismatch

if state = line_visual_tolerance_preflight_required:
  action = verify line_visual_tolerance_rule; allow at most 5% local near-equivalent substitution only for non-core evidence line_groups where the substitute is extremely close, proves the same claim, preserves viewer inference, and does not change locked copy meaning; block core evidence mismatch, whole-video drift, guessing, non-close replacement, repeated substitutions, or missing user material

if state = near_equivalent_material_substitution_preflight_required:
  action = generate near_equivalent_material_substitution_report with total_line_group_count / exact_match_count / near_equivalent_count / near_equivalent_ratio / consecutive_near_equivalent_max / core_evidence_mismatch_count / whole_video_drift_detected / substitutions / final_decision; block if final_decision is blocked_need_user_material

if state = tts_route_and_prosody_preflight_required:
  action = verify expected TTS provider/model/voice route and prosody anchors against actual TTS route; block unauthorized fallback, route mismatch, silent audio, or unknown route marked passed

if state = publish_candidate_voice_gate_required:
  action = require tts_route_report; verify actual_tts_provider = minimax, actual_tts_model in [speech-2.8-hd, MiniMax/speech-2.8-hd], selected_route in [minimax_official_api, aliyun_bailian_proxy_to_minimax], audio_present = true, non_silent = true, fallback_tts_used = false; block publish candidate completion for aliyun_qwen_tts / Serena / macOS say / local fallback / missing MiniMax route

if state = b_voice_feel_minimax_preflight_required:
  action = require b_voice_feel_minimax_formal_voice_rule and b_voice_identity_lock; treat B scheme as formal_voice_feel_reference plus concrete voice identity, not old Qwen/Aliyun provider; verify light_companion / low_pressure / natural_spoken_chinese / b_pacing_feel / subtle_pause_joke_rhythm / game_guide_feeling and not_broadcast / not_sales / not_customer_service / not_childish_cute_voice; additionally require actual_voice_id == expected_b_minimax_voice_id, actual_voice_id not in forbidden_voice_ids, actual_gender_direction = male_or_male_leaning, timbre_change_allowed = false, human_voice_review_status = user_confirmed; block if actual model is not MiniMax speech-2.8-hd, fallback used, audio missing/silent, B feel not reflected, expected voice id missing, actual voice id mismatch, actual voice id is forbidden, gender direction mismatch, or B voice not user-confirmed

if state = old_aliyun_qwen_b_voice_restoration_required:
  action = audit old Aliyun/Qwen B route as reference anchor before any new voice generation; verify provider = aliyun_bailian, api_route_family = aliyun_qwen_realtime_websocket_voice_clone, model = qwen3-tts-vc-realtime-2026-01-15, masked custom voice = qwen-t...ac19, and reference audio paths exist; block MiniMax system voice replacement, including male/neutral system candidates; after 2026-05-27 22:48 user correction, old Qwen is not the formal route and the next route is route_b_migrate_old_b_to_minimax

if state = old_b_to_minimax_voice_migration_required:
  action = use old Aliyun/Qwen B only as reference_anchor_only and MiniMax as final_generation_provider; check MiniMax voice clone/reference audio capability, whether current route needs public audio_url or authorized file upload, and whether generated_minimax_voice_id exists; block if reference_audio_url_or_upload_authorization_missing, generated_minimax_voice_id_missing, system voice candidate is used as old B, old Qwen route is selected as formal route, or human_voice_review_status is not user_confirmed

if state = card_decision_preflight_required:
  action = verify judgment_card / summary_card / result_diff_card / boundary_card / prompt_tail_card needed/not-needed decisions, reasons, line_group binding, evidence dependency, and interrupt risk

if state = forbidden_action_preflight_required:
  action = audit locked copy changes, removed required cards, TTS route changes, fallback use, default masking/whiteout, technical preview as delivery, missing inventory completion, and forbidden status promotion

if state = visual_evidence_readability_preflight_required:
  action = verify key evidence windows remain visible and are not covered by subtitles/cards, masks, whiteout, black blocks, gray residues, or unauthorized ratio changes; mark structural-only checks separately from future visual probes

if state = locked_copy_diff_preflight_required:
  action = compare locked_title / locked_opening_line / locked_final_script against actual subtitle text, TTS text, and card text; allow punctuation/line breaks/subtitle segmentation/TTS pause markers only; block semantic diffs

if state = publish_candidate_user_standard_preflight_required:
  action = verify publish_candidate_user_standard_rule; allow only minor flaws that do not affect publishing; block locked copy/title changes, wrong voice route, fallback/silent audio, whole-video drift, core evidence mismatch, subtitle/card blocking evidence, obvious borders/blocks/masks, internal diagnostic only, technical preview only, missing review_pack/preflight, or completion claim without validation; keep send_ready false until user or ChatGPT final confirmation

if state = completion_truth_preflight_required:
  action = verify required_output_inventory, all preflight reports, all gates passed, review_pack contains reports, media probes if media generated, latest updated if mechanism changed, no forbidden status promotion, and publish_candidate_ready_for_human_review does not imply send_ready

if state = mandatory_commit_push_required:
  action = explicitly stage only this round's relevant files, run staged secret scan, create commit, push to current reading branch or locked target branch, verify remote HEAD / remote commit readback, and write git_sync_status before any completed claim

if state = git_sync_incomplete:
  action = mark partial_completed with reason local_changes_done_but_not_pushed or blocked with exact git blocker; do not write completed

if state = repair_session_required:
  action = read_or_create current_repair_session before repairing an existing candidate, recover previous state from latest.md / review pack / summary.json / review_manifest.md if missing, lock one primary_issue_this_round, and update remaining_blockers after execution

if state = data_goal_anchor_needed:
  action = create_data_goal_anchor or block_execution_if_goal_anchor_missing before video execution

if state = current_data_goal_anchor_required:
  action = read codex_log/current_data_goal_anchor.md before copy, video execution, editing, assembly, or DeepSeek supply

if state = current_data_goal_anchor_missing:
  action = create codex_log/current_data_goal_anchor.md as current instance template; status must be draft, waiting_data, or blocked, not ready

if state = current_data_goal_anchor_waiting_data:
  action = allow hypothesis-only wiring or blocked; do not claim data-driven ready execution

if state = operation_decision_system_required:
  action = run scripts/运营决策系统_operation_decision_system.py and read latest_operation_decision_report before operation judgment, next-variable decision, or data_goal_alignment_check

if state = operation_decision_system_missing:
  action = build or repair operation_decision_system with schema/config/report outputs; do not stop at concept docs

if state = operation_decision_report_required:
  action = read review_loop/decision_engine/latest_operation_decision_report.json; if missing or invalid, generate it before deciding next execution

if state = copy_iteration_system_required:
  action = run scripts/文案迭代决策系统_copy_iteration_decision_system.py, then read latest_copy_iteration_report and V003_next_copy_revision_brief before any ChatGPT-facing copy revision judgment

if state = copy_version_record_missing:
  action = create review_loop/copy_iteration registry, raw copy record, copy quality notes, suspected typos, structure map, and data links; preserve raw copy exactly

if state = material_audit_needed:
  action = read skills/视频素材解析_video_material_audit/SKILL.md, run video material audit only, generate material_index / material_detail_report / timecode map / evidence and risk judgment, and do not generate final copy or video

if state = edgeguard_black_border_required:
  action = run scripts/边缘防护_EdgeGuard_edge_residue_guard.py for input_edge_preflight / safe_fit_policy / output_edge_scan; replace default black scale+pad with minimal safe fit; block candidate claim if output_edge_scan.pass != true

if input_signal includes 素材录制 / 录制素材 / 解析视频 / 素材审计 / 第几期素材 / 给 ChatGPT 写素材报告:
  action = require project video_material_audit skill, keep status_boundary unchanged, and block completion if only file existence or metadata is reported without timecode-level content analysis

if state = next_copy_revision_brief_required:
  action = generate V003_next_copy_revision_brief for ChatGPT only; do not generate formal next video execution prompt, and keep target audience / topic direction unchanged

if state = publish_candidate_required:
  action = check publish_candidate requirements before any formal-operation video delivery claim

if state = technical_preview_not_delivery:
  action = mark silent preview / 720p horizontal preview / no-audio preview / JSON or Markdown route package as internal_diagnostic_only or historical_internal_diagnostic_only; do not mark completed; do not promote content state

if state = publish_candidate_blocked or state = formal_operation_delivery_blocked:
  action = stop current video execution line, report missing capability, and do not continue producing low-standard preview as delivery

if state = current_data_goal_anchor_ready:
  action = allow Codex preflight only after locked fields and data_goal_alignment_check requirement are present

if state = data_goal_execution_bus_needed:
  action = wire data_goal_anchor into copy, DeepSeek supply, Codex execution, editing, assembly, validation, logs, and GPT Project package

if state = codex_execution_structure_drift_risk:
  action = run_data_goal_alignment_check and allow only structure changes that preserve primary_variable and validation metrics

if state = editing_or_assembly_without_data_goal_anchor:
  action = block editing / assembly until data_goal_anchor_used and data_goal_alignment_check fields exist

if input_signal includes 1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 差点意思 and target layer is unclear:
  action = infer state ambiguous_goal_clarification_needed, do not generate video / media / full Codex execution prompt, and require clarification of visual_look / editing_rhythm / layout_composition / subtitle_typography / highlight_motion / information_density / proof_logic / content_structure / emotional_tone / whole_piece_similarity

if state = reference_contract_needed:
  action = create or require Reference-to-Execution Contract before concrete execution; if the reference goal is ambiguous, run ambiguous_goal_clarification_needed first

if state = editing_inference_needed:
  action = run editing_inference_function, then generate editing_decision_pack if evidence is sufficient

if state = content_route_needed:
  action = run content_route_inference_function, then generate content_route_card before video execution

if final_script exists and task requests video execution:
  action = run script_anchor_extraction_function, then generate script_to_timeline_map before video execution

if tts_generation_requested:
  action = require tts_prosody_anchor_map before TTS generation

if input_signal includes opening_route / 开头路线 / 元素娃娃开头 / 梗图 GIF 开场 / 开头参考图:
  action = run content_route_inference_function, produce opening_route_decision, then generate opening

if opening_route in [meme_gif_opening_hook, high_emotion_hook] or input_signal includes 抖音抓眼 / 高情绪开头 / 抽象动效:
  action = require opening_visual_hook_spec before opening generation

if input_signal includes summary_card / 总结卡 / reversal_card / 反转卡 / result_diff_card / 结果差卡 / Prompt 引用尾卡 / 卡片位置:
  action = run content_route_inference_function and editing_inference_function, produce card_placement_decision before video execution

if input_signal includes data_result_card / 数据成果卡 / 卡片预算 / card_budget_gate / cluster_merge_rule / 卡片太密 / PPT 感过重:
  action = run card_budget_gate, cluster_merge_rule, evidence_window_protection, and data_result_card_priority before video execution; choose cards by information cluster and budget, not by every sentence

if input_signal includes judgment_card / 判断卡 / summary_card / 总结卡 / Codex 判断权限 / 判断权限表:
  action = read codex_source/21_codex_judgment_permission_matrix.md, produce codex_judgment_permission_gate, and decide execute / change_request / blocked / escalation boundary before editing or status claim

if card_placement_decision selects judgment_card or summary_card:
  action = require card_visual_route_selected, visual_base_route, text_authority_route, motion_wrapper_route, post_overlay_locked_copy_check, card_visual_quality_gate, subtitle_card_overlap_check, card_text_semantic_match, and evidence_window_not_interrupted; if motion_wrapper_route = HyperFrames_motion_wrapper, require hyperframes_card_motion_baseline and hyperframes_runtime_gate; if HyperFrames motion wrapper runtime is missing and no fallback is authorized, block only the motion wrapper route
  default_card_execution_route_after_user_approval = image2_visual_base_route_candidate -> codex_post_overlay_locked_copy -> optional HyperFrames_motion_wrapper; image2_long_term_stable_passed = false; visual_master_locked = false

if state = quality_review_needed:
  action = run quality_issue_classifier before changing assets or status wording

if state = gpt_project_sync_needed:
  action = regenerate static upload package, do not treat as UI uploaded

if input_signal includes 文案修改 / 下一条视频 / 根据数据改 / 播放低 / 收藏低 / 客资弱 / 复盘后重写:
  action = read goal-driven data flywheel, check threshold_config_v1, diagnose main_bottleneck, lock primary_variable before copy revision

if input_signal includes 文案版本 / 文案记录 / 文案迭代 / next_copy_revision_brief / 文案哪里好 / 文案哪里不好 / 数据反馈到文案:
  action = require copy_iteration_system_required, preserve raw copy, classify problem layer, generate ChatGPT-readable copy iteration report, and block formal next video execution prompt

if input_signal includes 根据数据推算下一段放什么 / 内容结构反馈 / 留存下滑 / 收藏低 / 评论弱 / 私信弱:
  action = generate content_structure_feedback_card and next_video_structure_plan before revised script

if input_signal includes Codex 执行下一条视频 / 根据数据执行 / 动态 prompt:
  action = require next_video_execution_prompt, codex_log/current_data_goal_anchor.md, and data_goal_anchor before video execution

if input_signal includes 视频执行 / 剪辑 / 编排 / 装配 / editing_decision_pack / assembly_decision_pack:
  action = require current_data_goal_anchor, then run data_goal_alignment_check before completion

if input_signal includes 黑边 / 灰边 / 左侧阴影 / 顶部阴影 / 边缘残留 / transparent padding / canvas 露底 / edge_residue_bug:
  action = trigger edgeguard_black_border_required; repair only Layer 0 EdgeGuard; do not add Remotion effects, highlight boxes, floating cards, 3D visuals, transition bridges, copy/audio/subtitle changes, or status promotion

if input_signal includes 做视频 / 产视频 / 发片候选 / 运营内容 / 下一条视频 / 发布候选:
  action = require delivery_baseline_gate and resolve to publish_candidate_ready_for_human_review or blocked_publish_candidate_unavailable

if input_signal includes 新增素材 / 补了素材 / 素材录好了 / 新素材路径 / 重新剪 / 重做中段 / 替换素材:
  action = trigger material_delta_type_router（素材增量类型路由器）; default material_delta_type = additive_merge（补充合并） unless user explicitly says only new material, old material should be discarded, or A replaces B; require latest_log / current_candidate / locked_copy / old_material_inventory / new_material_inventory / material_parse_pack / latest_review_issues / current_data_goal_anchor; output material_delta_type / material_delta_reason / old_context_required / replacement_scope / blocked_if_unclear / selected_next_gate; block as unclear_blocked if old candidate, locked copy, material inventory, or old-new relationship is unclear

if input_signal includes 发片候选 / 候选片 / 修片 / 视频执行 / 重新生成 / 发布前修复 / final_script_to_video / TTS / subtitle / card / timeline / review_pack / privacy_mask / aspect_ratio / visual_evidence:
  action = trigger process_boot_required; prompt is prompt_delta only; require process_boot_report before execution

if input_signal includes 发片候选 / 候选片 / 修片 / 视频执行 / 重新生成 / 发布前修复:
  action = trigger publish_candidate_inventory_required; missing required items must be blocked or continue, not completed

if input_signal includes 发片候选 / 候选片 / 修片 / 视频执行 / 重新生成 / 发布前修复 / final_script_to_video / TTS / subtitle / card / timeline / review_pack:
  action = trigger publish_candidate_preflight_suite_required before export; run material_parse_pack_reuse_preflight plus required preflight gates including publish_candidate_voice_gate; add preflight reports to review_pack requirement; block if any gate is missing, failed, or only documented

if input_signal includes 修片 / 修复片 / repair_candidate / pre_publish_fix / regenerate_video_for_existing_candidate:
  action = trigger repair_session_required; do not guess previous repair state from prompt

if output includes technical_preview / silent preview / 无音轨视频 / 横屏技术包 / JSON route card / Markdown route card:
  action = mark technical_preview_not_delivery; treat as internal_diagnostic_only; cannot satisfy formal operation delivery

if input_signal includes 做视频 / 发片候选 / 完整成片 / 修片 / 重新导出 / 视频执行 or codex is about to write completed or output includes full.mp4 only / route card / preflight package / technical_preview:
  action = trigger completion_truth_preflight_router（完成真实性预检路由器） before any completed（已完成） claim; require publish_candidate_required_inventory / publish_candidate_preflight_suite / locked_copy_diff_preflight / line_level_alignment_preflight / tts_route_and_prosody_preflight / card_decision_preflight / visual_evidence_readability_preflight / forbidden_action_preflight / completion_truth_check / review_pack / git_sync_status; output completion_status / completed_allowed / internal_diagnostic_only / blocked_reason / missing_required_outputs / selected_next_gate; block or mark internal_diagnostic_only if publish candidate baseline, preflight, review pack, audio, subtitles, evidence, cards, or completion truth report is missing

if input_signal includes 声音 / TTS / B 方案声音 / 旧声音 / Qwen / 阿里 / 百炼 / MiniMax / 恢复以前声音 or codex will generate/replace audio or judge voice pass:
  action = trigger voice_route_conflict_gate（声音路线冲突闸门）; set old_qwen_role = reference_anchor_only（仅参考锚点）, formal_tts_provider = MiniMax（MiniMax 语音）, formal_voice_id = oldBMinimax20260528010200, system_voice_substitution_allowed = false; require GPT数据源/08_当前正式事实.md / codex_source/00_codex_readme.md / codex_source/01_execution_rules.md / codex_source/21_codex_judgment_permission_matrix.md / codex_log/latest.md / 20260611_conflict_map.md / 20260611_vector_ingestion_blacklist.md; output old_qwen_role / formal_tts_provider / formal_voice_id / old_qwen_as_formal_provider_allowed / system_voice_substitution_allowed / voice_validation_allowed / blocked_if_conflict / selected_next_gate; block old Qwen formal provider restoration, MiniMax system voice substitution, old female candidate substitution, voice pass without user listening confirmation, or final_voice_validated without actual audio validation

if state = pre_execution_read_contract_gate_required:
  action = require mandatory_read_manifest（强制必读清单） and read_proof_report（读取证明报告） before execution; block if required items are unread, conflict unresolved, or any execution-required item is only represented by MISSING_REPORT（缺失报告）; allow diagnostic / missing report only, not real execution, when required inputs are missing

if state = no_degrade_completion_required:
  action = check exact target, required deliverables, real verification, sync status, and completion truth; if any required item is missing, continue or blocked instead of degraded completion

if input_signal includes commit / push / Git 收尾 / completed / sync_back_check / 远端校验 / remote HEAD / 仓库文件改动:
  action = trigger mandatory_commit_push_required; completed is forbidden until commit + push + remote verification succeeds

if state = self_repair_audit_required:
  action = audit locked goal, title, final script, script_to_timeline_map, subtitles, cards, audio, ratio, final media probe, data_goal_alignment_check, publish_candidate checklist, git sync, and no-degrade rule; repair or blocked

if state = locked_copy_contract_required:
  action = check locked_topic, locked_title, locked_final_script, locked_opening_line, allowed_copy_changes, forbidden_copy_changes, and copy_change_request_required_if_needed; block if missing or if Codex changed locked copy without approval

if state = script_visual_alignment_required:
  action = require line_level_script_visual_alignment_gate and line-level script_to_timeline_map with line_group_id, narration_text, source_timecode, expected_visual, allowed_visuals, forbidden_visuals, subtitle_text, card_text_if_any, evidence_strength, alignment_status, and blocked_if_visual_mismatch; block if only segment-level mapping exists or visual mismatch remains

if state = material_evidence_preflight_required:
  action = run scripts/素材解析包复用闸门_material_parse_pack_reuse_gate.py and scripts/素材证据闸门_material_evidence_gate.py before TTS/render/assembly; require material_parse_pack_reuse_report.json, material_evidence_contract.json, line_group_evidence_gate_report.json, and auto_storyboard_preflight_report.json; continue only when material_parse_pack_reuse_preflight.status = passed and auto_edit_allowed = true

if state = subtitle_card_overlap_check_required:
  action = run subtitle_card_overlap_check across narration subtitles, title cards, explanation cards, summary cards, screen OCR, and key evidence areas; fix high severity overlap or blocked

if state = post_publish_no_rework:
  action = stop video modification route, record feedback, repair mechanism if needed, and wait for operation data; do not regenerate or rework a sent video by default

if state = fallback_requires_user_authorization:
  action = report fallback proposal, mark task blocked, and wait for explicit user authorization before using fallback as deliverable

if state = codex_judgment_permission_matrix_needed:
  action = create or read Codex judgment permission matrix and wire it into route_decision, content_route_card V2, card_placement_decision, and completion_truth_check

if state = hyperframes_judgment_summary_card_baseline_needed:
  action = require HyperFrames for selected judgment_card / summary_card; mark runtime_execution as pending unless a real plugin/script/runtime entry is found

if state = blocked_need_user_input:
  action = stop and report exact missing user input
```

补充策略：

- `operation_data_intake`：只做截图 / 数据录入、缺失字段标记和证据归档，不做最终内容判断。
- `operation_decision_system_required`：运营判断层、下一期变量判断或 data_goal_alignment_check 前，必须先有 `operation_decision_system` 最新报告。
- `operation_decision_system_missing`：只有规则 / 卡片 / 锚点，不算系统完成；必须有可运行脚本、schema/config、三期归纳和最终用户报告。
- `operation_decision_report_required`：缺 `review_loop/decision_engine/latest_operation_decision_report.json` 或 JSON 不可解析时，不得直接拍板下一期执行。
- `operation_review`：必须有足够数据再判断阶段门槛、短板层和下一轮唯一运营变量。
- `operation_next_variable_decision`：只在运营复盘完成后选择下一轮唯一变量；缺 7d、需求侧字段或人审时只能保留 draft。
- `legacy_gray_test_data_intake`：只作为历史兼容别名，不得作为新数据默认路由。
- `material_delta_type_router（素材增量类型路由器）`：新增素材 / 补素材 / 新素材路径 / 重新剪 / 重做中段 / 替换素材任务必须先分型；默认 `additive_merge（补充合并）`，只有用户明确只用新素材或指定替换范围时才允许 `exclusive_new_only（只用新增素材）` / `replacement_merge（替换合并）`，不清楚则 `unclear_blocked（不清楚则阻断）`。
- `material_audit_needed`：先判断素材用途、证据强度和缺口，不直接生成或改动媒体。
- `voice_review_needed`：只做声音问题归因和候选复审，不写最终声音通过，不调用 TTS / voice cloning API。
- `completion_truth_preflight_router（完成真实性预检路由器）`：视频执行、发片候选、修片、重新导出或任何 `completed（已完成）` 声明前必须触发；`technical_preview（技术预览）`、`full.mp4 exists（视频文件存在）`、route card、preflight package 只能作为证据，不能替代完成真实性。
- `voice_route_conflict_gate（声音路线冲突闸门）`：声音 / TTS / B 方案 / Qwen / 阿里 / 百炼 / MiniMax 相关任务必须先裁决旧 Qwen / 阿里 B 只作 `reference_anchor_only（仅参考锚点）`，当前正式声音锁仍为 MiniMax + `oldBMinimax20260528010200`。
- `pre_execution_read_contract_gate（执行前读取契约闸门）`：RAG / Router 生成 `mandatory_read_manifest（强制必读清单）` 后，Codex 执行前必须输出 `read_proof_report（读取证明报告）`；若执行必需项只由 `MISSING_REPORT（缺失报告）` 表示，只允许诊断 / 缺失清单 / 阻断报告，不允许真实剪辑、TTS、导出或 completed 判断。
- `ambiguous_goal_clarification_needed`：用户说 `1:1`、像对标、高级感、按这个效果做、不是一回事、完全不像、感觉不像、差点意思但未锁目标层级时触发；必须先澄清视觉观感、剪辑节奏、构图布局、字幕字体、动效、信息密度、证明方式、内容结构、情绪人感或整体观感，不得把机制分析草案当正式执行标准。
- `reference_contract_needed`：只把 reference / 样片 / 目标效果转换为 `reference_anchor`、`effect_targets`、`function_fields`、`deviation_check`、`done_when`；若 reference 目标有歧义，先触发 `ambiguous_goal_clarification_needed`，不得直接执行媒体、文案终稿或状态推进。
- `engineering_line_collaboration_gate_needed`：用户要求升级协作机制、工程线、多节点自动化、Codex 下发前判断、机制修补或 GPT Project 同步包时触发；必须先问 `engineering_worth_question（值不值得工程化）`，再判 `engineering_depth_router（工程深度路由器）`，并用 `decision_authority_matrix（决策权矩阵）` 区分用户 / ChatGPT / Codex 权限。需要改文件时必须触发 `per_file_detail_plan_required（需要单文件细节方案）`；发现简单任务被强制 L3 时触发 `engineering_overdesign_risk（工程化过度风险）` 并降级到 L0 / L1 / L2。
- `supply_source_arbitration_required`：每轮默认成立；必须先输出 `retrieval_manifest / source_readback_status / retrieval_gap_report / deepseek_trigger_decision`。
- `rag_engineering_line_required`：命中 RAG、向量、DashVector、检索、供料、DeepSeek 复核边界、source_readback、stale_index 或 trace / failure route 落地时成立；不得只写 schema / fixture / probe，必须有 builder、validator、router hook、acceptance suite、failure resolver 和 trace writer。
- `pre_supply_pack_required`：Codex 写入 RAG / 向量 / 机制 / 路由文件前成立；必须生成并校验 `pre_supply_pack`，资料包必须含 source_path、line_range、chunk_id、exact snippet 和 readback。
- `mid_task_supply_required`：子任务缺上下文、验证失败、高风险写入前或 conflict_points 未清时成立；必须生成 `mid_task_supply_pack`，`continue_allowed = false` 时不得继续写。
- `failure_route_required`：任何验证失败、同步失败、事实冲突、权限缺失、完成真实性风险或 Git 同步失败时成立；必须路由到具体修复层，不得只写 retry。
- `trace_event_required`：RAG 工程线任务每轮默认成立；必须写 `trace_event`、dated log 和 latest，让下一轮能接手。
- `post_commit_vector_sync_gate_required`：Codex 修改可索引文本文件并完成 source commit 后成立；必须运行 `scripts/post_commit_vector_sync_gate.py --mode finish`。触发条件包括 allowlist 文件变化、`latest_index_manifest.source_commit_sha` 落后于当前 commit、或 `rag_index_manifest_validator --check-current-worktree` 检出 stale index。同步失败时只能写 `vector_sync_blocked`，不得写 RAG 已最新。
- `deepseek_review_conditionally_required`：仅在 `rag_empty / rag_low_confidence / source_conflict / mechanism_conflict / high_risk_execution / user_explicit_request` 等条件成立时触发；不得把 DeepSeek 当每轮默认文件供应商。
- `deepseek_pre_supply_missing`：仅当 DeepSeek 已被条件触发或用户明确要求时成立；写入前必须先补 `supply_request` 和审查包，无法真实调用时写 fallback / blocked。
- `deepseek_post_review_missing`：修改后必须复核状态偷换、禁止修改、遗漏同步、fallback 误标和剩余工作。
- `deepseek_claim_without_token_usage`：token 未观察到减少时不得写 DeepSeek 已深度参与。
- `codex_vertical_completion_missing`：只写文档不算完成，必须补脚本、schema、fixture、日志、上传包和验证链。
- `process_boot_required`：视频执行、修片、发片候选、重新生成、发布前修复或最终文案进视频时触发；必须输出 `process_boot_report`，把 GPT prompt 当 `prompt_delta`，并按仓库流程读取完整入口。缺报告、缺完整流程读取或把 prompt 当完整流程源时 blocked。
- `publish_candidate_inventory_required`：发片候选、修片候选或视频执行时触发；必须生成 `publish_candidate_required_inventory` 并逐项判断 required / not_applicable。任一必需项缺失且无 `not_applicable_reason` 时，不得写 `completed`。
- `publish_candidate_preflight_suite_required`：发片候选、修片候选、视频执行、重新生成、发布前修复、最终文案进视频或 TTS / 字幕 / 卡片 / 时间线 / review_pack 生成时触发；必须运行 `scripts/发片候选预检套件_publish_candidate_preflight_suite.py --no-render` 或等价入口，产出总报告、`material_parse_pack_reuse_report（素材解析包复用报告）` 与十二个子报告。任一 gate missing / failed / only documented 时不得导出、不得 `completed`。
- `line_visual_tolerance_preflight_required` / `near_equivalent_material_substitution_preflight_required`：允许最多约 5% 的局部非核心近似素材替代；核心证据错位、全程漂移、需要猜测、素材不极近或用户素材缺失时必须 blocked。
- `b_voice_feel_minimax_preflight_required`：B 方案是正式听感标准与声音身份锁，MiniMax 是正式生成路线；旧 Qwen / 阿里 B 语音路线不能作为正片候选完成。2026-05-27 重审后还必须执行 `b_voice_identity_lock（B 声音身份锁）`：未取得 `expected_b_minimax_voice_id` 与用户试听确认前，只能生成候选样本或 blocked，不能把 `b_voice_feel_reflected = true` 写成声音通过；候选方向必须是 `male_or_male_leaning`，不得继续从女声系统音色锁 B。
- `old_aliyun_qwen_b_voice_restoration_required`：用户要求查清以前阿里大模型 B 方案声音时触发；必须先查旧 B 事实，不得继续抽 MiniMax 系统候选。旧 B 身份为 `aliyun_bailian / aliyun_qwen_realtime_websocket_voice_clone / qwen3-tts-vc-realtime-2026-01-15 / qwen-t...ac19`；`qwen-t...ac19` 不是 MiniMax `voice_id`。2026-05-27 22:48 用户纠正后，该路线只作为 `reference_anchor_only`，不得恢复为正式默认 TTS 路线。
- `old_b_to_minimax_voice_migration_required`：用户要求用 MiniMax 复刻 / 迁移旧 B 声音时触发；MiniMax 是 `final_generation_provider`，旧 Qwen 是 `reference_anchor_only`。必须优先检查 reference audio / voice clone，缺公网 `audio_url` 或缺授权上传时写 `blocked_need_reference_audio_url`；不得使用 `female-tianmei / female-shaonv / female-shaonv-jingpin / female-yujie / male-qn-qingse / male-qn-daxuesheng / Chinese (Mandarin)_Gentleman / Chinese (Mandarin)_Gentle_Youth / Chinese (Mandarin)_Sincere_Adult` 等系统候选替代旧 B，也不得把旧 Qwen 路线恢复成正式路线。
- `publish_candidate_user_standard_preflight_required`：按用户打开后原则上可直接发的标准判断候选；小瑕疵可进人工复审，重大缺陷只能 blocked / internal_diagnostic_only，且 `publish_candidate_ready_for_human_review != send_ready`。
- `line_level_alignment_preflight_required`：`script_to_timeline_map` 不能只证明文件存在；必须逐句检查 line_group 字段、实际观察画面、证据强度和 mismatch 修复状态。
- `tts_route_and_prosody_preflight_required`：`tts_prosody_anchor_map` 不能只证明字段存在；必须检查实际 provider / model / voice route / pacing 是否使用，禁止未授权 fallback。
- `publish_candidate_voice_gate_required`：`tts_route_report` 是正片候选必填；实际 TTS 必须为 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`，B 方案只作听感参考。非 MiniMax 语音只能 `blocked_publish_candidate_unavailable` 或 `internal_diagnostic_only`，不得 `completed` 或 `publish_candidate_ready_for_human_review = true`。
- `b_voice_identity_lock_required`：B 方案正片候选必须检查 `actual_voice_id == expected_b_minimax_voice_id`、`actual_voice_id not in forbidden_voice_ids`、`actual_gender_direction = male_or_male_leaning`、`actual_voice_setting matches locked_voice_setting`、`timbre_change_allowed = false`、`human_voice_review_status = user_confirmed`；`female-tianmei / female-shaonv / female-shaonv-jingpin / female-yujie` 不得默认继续作为 B 音色，除非用户未来明确反悔并重新确认。
- `card_decision_preflight_required`：prompt 未提卡片不代表可省略；判断卡、总结卡、结果差卡、边界卡、Prompt 尾卡需要 / 不需要都必须写依据。
- `forbidden_action_preflight_required`：导出前必须审计改文案、删卡、改声音、遮挡、状态推进、technical preview 冒充交付等禁止行为。
- `visual_evidence_readability_preflight_required`：核心证据被字幕、卡片、遮挡、洗白、边缘残留或比例变化影响时必须 blocked；结构检查与未来 OCR / 视觉探针必须分开标注。
- `locked_copy_diff_preflight_required`：锁定文案与实际字幕、TTS 和卡片文案必须对齐；非语义格式变化可接受，语义差异必须 blocked。
- `completion_truth_preflight_required`：完成真实性必须检查八个预检报告、review_pack 包含关系、媒体探针（如适用）、日志和禁止状态推进；不得用 `full.mp4` 或字段存在替代完成。
- `repair_session_required`：修片、发布前修复或重生成既有候选片时触发；必须读或创建 `current_repair_session`，恢复上一轮状态，锁本轮唯一主修问题，并在执行后更新 `remaining_blockers`。
- `data_goal_anchor_needed`：缺数据目标锚点时，不得进入视频执行、剪辑、编排或装配。
- `data_goal_execution_bus_needed`：13 已定义目标但未接到全执行链时，必须补 14 总线或同步执行规则；不得只扩写说明。
- `codex_execution_structure_drift_risk`：Codex 可以改结构，不能改目标、主短板、主变量、禁止变量和验证指标。
- `editing_or_assembly_without_data_goal_anchor`：缺 `data_goal_anchor_used` 时，不得生成 `editing_decision_pack` 或 `assembly_decision_pack`。
- `publish_candidate_required`：正式运营视频交付任务必须先检查音轨、字幕、开头、中段证据、结尾、人感质量、平台风险和装配能力；用户提供录屏 / 桌面素材时，优先检查源素材比例与证据可读性，不再默认强制 16:9 / 1920x1080。
- `source_native_no_mask_visual_required`：用户素材进入视频执行、修复成片或发布候选时触发；必须默认不遮挡、不洗白、不加灰色遮罩、不加黑块、不加整屏 privacy mask、不用 padding bands 填边，并优先使用源素材比例。
- `visual_evidence_unreadable_blocked`：若商品卡、表格、聊天框结论等核心证据因遮挡、洗白、卡片、字幕、缩放或裁切不可读，必须 blocked，不得交候选片。
- `technical_preview_not_delivery`：技术预览、无声预览、横屏技术包或只交 JSON / Markdown route card 只能作为内部诊断，不得写完成或内容推进。
- `formal_operation_delivery_blocked`：无法生成可发布候选片时必须停止当前视频执行线，写 `blocked_publish_candidate_unavailable` 和缺失能力。
- `no_degrade_completion_required`：正式运营、用户可见交付、项目文件落库、GPT Project 同步、数据录入、复盘记录、素材审计、TTS / 字幕 / 卡片 / 比例 / 导出、commit / push 等任务，都必须检查目标、产物、验证、同步和回报是否真实完成；缺任一必交付项时不得写 `completed`。
- `self_repair_audit_required`：用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时触发；Codex 必须自行审计内部执行问题，修复或 blocked，不得要求用户诊断内部原因。
- `locked_copy_contract_required`：视频执行、发布候选片生成或最终文案转视频时触发；缺 `locked_topic / locked_title / locked_final_script / locked_opening_line` 或 Codex 未授权改写时 blocked。
- `script_visual_alignment_required`：最终文案进入视频、剪辑、装配或发布候选片生成时触发；必须执行 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 并逐句映射到画面证据，只有段落级映射或文案画面错位时 blocked。
- `material_evidence_preflight_required`：最终文案进入剪辑、装配、成片生成或视频修复时触发；必须先通过 `material_parse_pack_reuse_gate`，确认剪辑只消费同一份 `material_parse_pack`，并生成 / 读取 `source_segment_inventory / script_to_shot_execution_map / material_usage_ledger / duplicate_material_check`；再把 `material_detail_report` 转成 `material_evidence_contract`，逐句运行 `line_group_evidence_gate` 和 `auto_storyboard_preflight_report`。解析包缺失 / 过期、二次解析、无理由重复片段、连续重复片段、核心证据复用证明不同主张、主题相近硬配、`cannot_support` 选中或句组未引用素材报告时必须 blocked；`auto_edit_allowed` 不是 `true` 时不得生成 `full.mp4`。
- `subtitle_card_overlap_check_required`：生成字幕、标题卡、解释卡或总结卡时触发；high severity overlap 未修复时 blocked。
- `post_publish_no_rework`：用户说视频已经发了 / 已发布时触发；当前视频只进入反馈记录和数据回流，不默认回炉或重做。
- `fallback_requires_user_authorization`：原目标做不到且 Codex 想使用 fallback / 降级方案时触发；降级只能作为 blocked 后的修复建议，用户明确授权前不能作为完成结果。
- `codex_judgment_permission_matrix_needed`：任务涉及 Codex 什么时候判断 / 什么时候不判断时触发；必须读取 `codex_source/21_codex_judgment_permission_matrix.md` 并输出 execute / change_request / blocked / escalation 边界。
- `hyperframes_judgment_summary_card_baseline_needed`：`card_placement_decision` 选择 `judgment_card（判断卡）` 或 `summary_card（总结卡）` 时触发；HyperFrames 是默认动效和视觉优化基线，runtime 不存在时必须 blocked 或等待用户授权降级。

### 4-1. 目标驱动数据飞轮执行侧规则

命中以下任一信号时，Codex 必须先读 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 与 `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`：

- 文案修改
- 下一条视频
- 根据数据改
- 播放低 / 收藏低 / 客资弱
- 复盘后重写
- 数据飞轮
- 目标驱动
- 数据目标
- 单主变量
- 内容结构反馈
- 视频执行 / 剪辑 / 编排 / 装配
- DeepSeek 供料
- GPT Project 静态包同步

```text
data_goal_copy_revision_needed:
  trigger:
    - 用户要求修改文案
    - 用户要求根据数据调整文案
    - 用户要求写下一条视频
    - 用户要求复盘后重写
  must_read:
    - data_goal_anchor
    - threshold_config_v1
    - video_goal_card
    - post_publish_review_card
    - data_flywheel_memory
    - content_structure_feedback_card
  selected_action:
    - 先检查阈值
    - 先诊断主短板
    - 锁定 primary_variable
    - 写 supporting_variables / forbidden_variables
    - 再进入文案修改
  blocked_if:
    - 缺 data_goal_anchor
    - 缺目标
    - 缺阈值配置
    - 缺数据且声称数据驱动
    - 缺主短板
    - 缺 primary_variable

content_structure_feedback_needed:
  trigger:
    - 用户要求根据数据推算下一段放什么
    - 发布后留存 / 收藏 / 评论 / 私信出现短板
  selected_action:
    - 生成 content_structure_feedback_card
    - 生成 next_video_structure_plan
  blocked_if:
    - 缺阈值配置
    - 缺分段数据
    - 缺复盘窗口
    - 数据不足却强行下结论
```

data_goal_execution_bus_needed:
  trigger:
    - data_goal 已定义，但 content_route_card / DeepSeek supply_request / editing_decision_pack / assembly_decision_pack 未接入
    - Codex 执行可能只按素材、画面或旧流程自由发挥
  selected_action:
    - create_data_goal_anchor
    - run_data_goal_alignment_check
    - block_execution_if_goal_anchor_missing
  blocked_if:
    - 缺 data_goal_anchor
    - 缺 primary_variable
    - 缺 forbidden_variables
    - 缺 post_publish_validation_metric
    - Codex 需要改写目标而不是调整结构
    - 数据目标被用来替代素材证据或人感质量验收

执行侧硬规则：

- 没有 `threshold_config_v1（阈值配置 V1）`，不得做数据驱动判断。
- 没有 `video_goal_card（视频目标卡）`，不得进入正式文案修改。
- 没有 `post_publish_review_card（发布后复盘卡）`，不得声称“根据数据修改文案”。
- 没有 `main_bottleneck（主短板）`，不得重写正式文案。
- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。
- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，不得进入视频执行。
- 没有 `data_goal_anchor（数据目标锚点）`，不得进入视频执行、剪辑、编排或装配。
- 没有 `data_goal_alignment_check（数据目标对齐检查）`，不得写执行完成。
- 超过 3 个变量且未标 `major_revision（大改版）`，不得进入执行。
- 超过 4 个变量不得写成单变量实验，只能写方向重做观察。
- 本机制不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
Codex 可以调整 segment 拆分、剪辑节奏、画面顺序、卡片位置、TTS 分句和装配顺序；降级方案只能作为 `blocked` 后待用户授权的修复建议，不能作为完成结果。Codex 不得改写当前阶段目标、主短板、主变量、禁止变量或发布后验证指标。

## 4A. 三大机制推理函数执行侧调用规则

Codex 进入具体执行前，凡命中剪辑、内容承载或质量复审信号，必须先输出对应推理函数结果。没有对应函数结果，不得生成卡片 / 决策包，不得进入视频执行，不得写 `completed（已完成）`。

### 4A.0 script_anchor_extraction_function（文案锚点提取函数）

触发信号：

- 已有 `final_script（最终文案）`，且任务准备进入视频执行、时间线装配、TTS、字幕、卡片或审片包生成。
- `content_route_card V2（内容路由卡 V2）` 已存在，但只有段落级 `material_01 / material_02 / material_03` 分配。
- 用户指出文案和画面局部错位、关键句配错画面、证据句没有对应素材。
- 用户指出 TTS 字词突然上扬、停顿不自然、分句断裂或机器式重音。

执行侧输出必须包含：

```text
script_anchor_extraction_function:
  input_signal:
    - final_script
    - content_route_card_v2
    - material_detail_report
    - platform_risk_note
    - data_goal_anchor
  observed_evidence:
    - narration_line
    - claim_type
    - evidence_type
    - material_id
    - source_timecode
    - risk_phrase
    - data_goal_anchor_used
    - main_bottleneck_supported
    - primary_variable_supported
    - forbidden_variables_avoided
    - post_publish_validation_metric
  state_inference:
    - sentence_has_direct_evidence
    - sentence_has_user_experience_claim
    - sentence_is_boundary_statement
    - sentence_is_reversal_point
    - sentence_is_summary_point
    - sentence_needs_card_support
    - sentence_must_not_use_visual_claim
    - paragraph_level_mapping_insufficient
  action_policy:
    - output_script_function_map
    - output_evidence_anchor_map
    - output_visual_anchor_map
    - output_tts_prosody_anchor_map
    - output_card_anchor_map
    - output_forbidden_visual_map
    - output_script_to_timeline_map
    - output_data_goal_alignment_fields
    - blocked_if_sentence_level_mapping_missing
  validation_rule:
    - 每 1-2 句必须有 line_group_id
    - 每个 line_group_id 必须绑定素材或明确 no_direct_evidence
    - 每个 line_group_id 必须有 allowed_visuals 和 forbidden_visuals
    - 每个 line_group_id 必须说明服务哪个数据目标、主短板或主变量
    - 每个 evidence_sentence 必须能追溯素材或标记为用户经验陈述
    - 每个 boundary_statement 不得配误导性证明画面
  blocked_if:
    - data_goal_anchor missing
    - final_script missing
    - material_detail_report missing
    - script_to_timeline_map missing before video execution
    - paragraph_level_mapping_only
  feedback_update:
    - 写入 content_route_card V2
    - 写入 video_execution_preflight
    - 写入 review pack
    - 写入 dated log
```

完成判断：

- `data_goal_anchor（数据目标锚点）` 是视频执行、剪辑、编排和 DeepSeek 供料前置条件。
- `script_to_timeline_map（文案到时间线映射表）` 是视频执行、时间线装配和剪辑前置条件。
- `tts_prosody_anchor_map（TTS 韵律锚点表）` 是 TTS 生成前置条件。
- `opening_visual_hook_spec（开头视觉钩子规格）` 是高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头生成前置条件。
- `forbidden_visual_map（禁用画面表）` 必须用于阻止边界声明、经验陈述和平台风险句配误导性证明画面。
- 只有段落级 `material_01 / material_02 / material_03` 分配时，不得进入视频执行。
- `data_goal_alignment_check（数据目标对齐检查）` 是视频执行完成前置条件。

### 4A.1 editing_inference_function（剪辑推理函数）

触发信号：

- 任务涉及中段剪辑、录屏放大、裁切、定格、插卡、左右对比、证据窗口或 `editing_decision_pack（剪辑决策包）`。
- 任务涉及总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡插入位置，或需要判断卡片是否打断证据窗口。
- 用户反馈中段不顺、看不清、硬拼接、上下文断裂。
- reference / visual route 要求保留某个证据窗口或剪辑节奏。
- 素材被标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）`，需要判断是否保留原始运镜并按文案直接剪辑。
- 已有最终文案但缺 `script_to_timeline_map（文案到时间线映射表）`。
- 只有段落级素材分配，缺 `line_id / line_group_id（句子编号 / 句组编号）`。

执行侧输出必须包含：

```text
editing_inference_function:
  input_signal:
    - data_goal_anchor
  observed_evidence:
    - data_goal_anchor_used
    - line_group_goal
    - primary_variable_support
    - evidence_role_for_metric
    - forbidden_visuals_by_goal
    - post_publish_validation_metric
  state_inference:
  action_policy:
    - output_edit_action_reason_against_data_goal
  validation_rule:
    - 每个剪辑动作必须说明是否支持 primary_variable
    - 每个剪辑动作不得引入 forbidden_variables
  blocked_if:
    - data_goal_anchor missing
    - edit_action_breaks_primary_variable
    - forbidden_variable_introduced
  not_allowed:
  feedback_update:
```

FocuSee 自带运镜素材的执行侧补充：

```text
  state_inference:
    - recording_layer_motion_baked_in
    - direct_cut_required
    - keep_original_motion
    - no_secondary_zoom_by_default
    - secondary_zoom_allowed_only_if_evidence_unclear
    - sentence_level_mapping_ready
    - paragraph_level_mapping_insufficient
    - script_visual_mismatch_detected
  action_policy:
    - direct_cut_by_script
    - keep_original_focusee_motion
    - trim_dead_time
    - align_to_narration
    - preserve_evidence_window
    - blocked_if_key_evidence_unclear
    - read_script_to_timeline_map_before_assembly
    - blocked_if_paragraph_level_mapping_only
    - blocked_if_script_visual_conflict
not_allowed:
  - default_zoom_in
  - default_crop_focus
  - reframe_without_reason
  - second_camera_motion_over_focusee_motion
```

卡片插入执行侧补充：

```text
state_inference:
  - card_insertion_safe
  - card_insertion_interrupts_evidence
  - keep_evidence_window_uninterrupted
action_policy:
  - insert_card_only_if_copy_function_requires
  - preserve_focusee_motion_when_card_not_required
  - blocked_if_card_breaks_evidence_window
not_allowed:
  - fixed_card_shot_without_copy_reason
  - summary_card_as_evidence
  - reversal_card_without_reversal_point
```

完成判断：

- `editing_decision_pack（剪辑决策包）` 必须引用本函数的 `state_inference` 和 `action_policy`。
- `editing_decision_pack（剪辑决策包）` 必须包含 `data_goal_anchor_used / line_group_goal / primary_variable_support / evidence_role_for_metric / forbidden_visuals_by_goal / edit_action_reason_against_data_goal / post_publish_validation_metric`。
- 如果素材不可读、时间码不清、证据点不可见、放大会切断必要上下文，必须 `blocked` 或 `keep_full_frame`，不得凭感觉剪。
- 卡片、放大、裁切、定格只能服务真实证据清晰，不得替代真实录屏证据。
- 当素材已经自带 FocuSee `3D Motion（3D 运镜）`、自动跟随或观看引导时，默认完成标准不是“再放大一次”，而是按最终文案完成时间码识别、段落切分、冗余删除、口播 / 字幕 / 卡片衔接，并保留原始运镜节奏。
- 如果卡片会打断真实证据窗口，必须跳过、改位置或 blocked，不得为了旧 shot 结构强插。
- 剪辑动作不能只看 `material_01 / material_02 / material_03` 段落级用途，必须读取 `line_id / line_group_id（句子编号 / 句组编号）`。
- 每 1-2 句必须知道当前句子在证明什么、必须出现什么画面、不能出现什么画面、是否需要卡片辅助，以及是否是反转点 / 证据点 / 总结点。
- 如果只有段落级映射，不允许进入视频装配；如果文案句子与素材证据冲突，必须 blocked 或回到 ChatGPT 复审，不得硬剪。
- 如果缺 `data_goal_anchor_used（使用的数据目标锚点）`，不得生成 `editing_decision_pack（剪辑决策包）`。
- 如果剪辑动作改变主变量、引入禁止变量或削弱发布后验证指标，必须 blocked。

### 4A.2 content_route_inference_function（内容路由推理函数）

触发信号：

- 任务涉及 `content_route_card（内容路由卡）`、内容表达文案进入执行、主体承载、API 生成真人次数、PPT / 信息卡 / Prompt 引用尾卡是否出现。
- 任务涉及真实视频执行前的统一判断卡、`content_route_card V2（内容路由卡 V2）` 或等效完整字段。
- 任务涉及 `opening_route_decision（开头路由判断）`、元素娃娃开头、梗图 GIF 开场、直接问题标题卡、录屏现场先行开头或开头参考图。
- 任务涉及 `card_placement_decision（卡片位置判断）`、总结卡、反转卡、结果差卡、Prompt 尾卡或卡片位置路由。
- 任务涉及 `judgment_card（判断卡）`、`summary_card（总结卡）` 或 HyperFrames 卡片动效基线。
- 任务涉及最终文案进入执行，需要生成 `script_anchor_map / script_to_timeline_map / tts_prosody_anchor_map / forbidden_visual_map`。
- 任务涉及高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头，需要生成 `opening_visual_hook_spec（开头视觉钩子规格）`。
- 需要判断本轮是只做内容验证，还是值得沉淀三层 prompt 包 / 工作包。
- reference 质量点可能和当前文案目标冲突。

执行侧输出必须包含：

```text
content_route_inference_function:
  input_signal:
    - data_goal_anchor
  observed_evidence:
    - data_goal_anchor_used
    - main_bottleneck_supported
    - primary_variable_supported
    - forbidden_variables_avoided
    - post_publish_validation_metric
  state_inference:
  action_policy:
  validation_rule:
    - content_route_must_support_data_goal
  blocked_if:
    - data_goal_anchor missing
  feedback_update:
```

完成判断：

- `content_route_card（内容路由卡）` 必须由本函数生成或引用本函数判断。
- 涉及内容执行 / 视频执行 / 文案进入执行时，必须输出 `content_route_card V2（内容路由卡 V2）` 或等效完整字段，不得只输出零散开头、卡片或素材判断。
- `content_route_card V2（内容路由卡 V2）` 必须包含 `data_goal_anchor_used / main_bottleneck_supported / primary_variable_supported / forbidden_variables_avoided / post_publish_validation_metric`。
- 缺 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / card_placement_decision / flow_flex_reason` 时，不得进入视频执行。
- 缺 `data_goal_anchor_used（使用的数据目标锚点）` 时，不得进入视频执行。
- `forbidden_variables_avoided（内容路由 / 时间线避开的禁止变量）`、`forbidden_visuals_by_goal（剪辑按目标禁用的画面）` 与 `forbidden_variable_avoided（装配避开的禁止变量）` 必须全部能追溯到同一组 `data_goal_anchor.forbidden_variables`；字段名不同不代表语义可分叉。
- 若素材来自 FocuSee，缺 `focusee_middle_editing_decision（FocuSee 中段剪辑判断）` 时，不得进入中段剪辑或视频执行。
- 涉及总结卡、反转卡、结果差卡或 Prompt 尾卡时，缺 `card_placement_decision（卡片位置判断）` 不得进入视频执行。
- 涉及判断卡或总结卡时，`card_placement_decision（卡片位置判断）` 必须填写 `card_visual_route_selected / visual_base_route / text_authority_route / motion_wrapper_route / post_overlay_locked_copy_check / card_visual_quality_gate`；只有 `motion_wrapper_route = HyperFrames_motion_wrapper` 时才填写 `hyperframes_motion_type / hyperframes_runtime_status / hyperframes_visual_quality_gate`，HyperFrames runtime 不存在且未授权降级时只阻断该动效包装路线。
- 20260609 最小真实链路样张经用户人工通过后，后续默认卡片执行路线为 `default_card_execution_route_after_user_approval = image2_visual_base_route_candidate -> codex_post_overlay_locked_copy -> optional HyperFrames_motion_wrapper`；该默认路线不推进 `content_validation / send_ready / visual_master_locked`。
- 不得先定人物次数、PPT 数量或尾卡数量，再把文案硬塞进去。
- 涉及开头时，不得绕过 `opening_route_decision（开头路由判断）` 直接生成开头。
- 涉及高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头时，不得只输出路线判断，必须输出 `opening_visual_hook_spec（开头视觉钩子规格）`；静态两行标题页不得默认通过。
- 涉及最终文案进入执行时，必须先输出 `script_anchor_extraction_function（文案锚点提取函数）` 的结果；缺 `script_to_timeline_map（文案到时间线映射表）` 不得进入视频执行。
- 涉及 TTS 生成时，必须先输出 `tts_prosody_anchor_map（TTS 韵律锚点表）`；不得只按标点机械分句。
- 不得把 `element_doll_opening（元素娃娃开头）` 或 `meme_gif_opening_hook（梗图 GIF 开场钩子）` 写成所有内容唯一默认。
- 若开头 reference 不完整，只能继承 `effect_targets（效果目标）` 和机制字段，不得复刻人物、头像、字体、构图或第三方可识别资产。
- 不得把总结卡 / 反转卡固定为旧 shot 位置；没有明确反转点时不得强行插反转卡，结尾一句话能自然收住时不得强行堆总结卡。

开头路线执行侧补充：

```text
opening_route_decision:
  input_signal:
    - opening_duration
    - topic_emotion_level
    - controversy_level
    - evidence_start_strength
    - brand_consistency_need
    - core_question_can_be_stated_in_one_sentence
  state_inference:
    - opening_route_needed
    - element_doll_opening_suitable
    - meme_gif_opening_hook_suitable
    - direct_question_title_card_suitable
    - screen_first_opening_suitable
    - opening_route_pending_judgment
  action_policy:
    - choose_element_doll_opening
    - choose_meme_gif_opening_hook
    - choose_direct_question_title_card
    - choose_screen_first_opening
    - blocked_if_opening_route_unclear
  not_allowed:
    - element_doll_as_only_default
    - meme_gif_as_new_only_default
    - copy_user_reference_asset
    - opening_hook_as_proof
    - static_two_line_title_for_high_emotion_hook
    - plain_title_card_when_douyin_hook_required
```

开头视觉 hook 规格补充：

```text
opening_visual_hook_spec:
  opening_route:
  hook_goal:
  viewer_feeling:
  visual_motion:
    - fast_zoom
    - shake
    - speed_lines
    - abstract_shapes
    - impact_flash
  text_density:
  main_question:
  composition:
  duration:
  must_not_be:
    - static_two_line_title
    - plain_title_card
    - ppt_cover_page
    - copied_third_party_asset
  allowed_style:
    - abstract_gif_like
    - meme_energy_without_copying
    - high_contrast_question_hook
  validation_rule:
  blocked_if:
```

卡片位置执行侧补充：

```text
card_placement_decision:
  input_signal:
    - copy_function
    - reversal_point
    - conclusion_point
    - result_diff_point
    - evidence_window_active
    - prompt_handoff_needed
  state_inference:
    - card_placement_route_needed
    - summary_card_needed
    - summary_card_not_needed
    - reversal_card_needed
    - reversal_card_not_needed
    - card_interrupts_evidence_window
    - card_position_pending_judgment
  action_policy:
    - place_summary_card_after_result_diff
    - place_summary_card_at_final_closure
    - place_reversal_card_between_negative_and_positive
    - place_reversal_card_before_result_diff
    - skip_card
    - blocked_if_card_position_unclear
  not_allowed:
    - fixed_summary_card_shot
    - fixed_reversal_card_shot
    - card_as_middle_evidence_replacement
```

### 4A.3 quality_issue_classifier（质量短板分类器）

触发信号：

- 用户反馈“不对 / 怪 / 不顺 / demo 感”。
- 技术通过但内容、人感、证据、声音、卡片密度或剪辑节奏不舒服。
- 需要生成或复核 `quality_lock_card（质量锁卡）`。
- 用户指出某些字突然上扬、停顿不自然、分句断裂、重音机器感。
- 用户指出开头只是两行简单字、不抓人、不符合抖音审美。
- 用户指出文案和画面局部错位，关键句配错画面。

执行侧输出必须包含：

```text
quality_issue_classifier:
  input_signal:
  observed_evidence:
  issue_categories:
    - voice_prosody_issue
    - opening_visual_hook_issue
    - script_visual_mismatch_issue
  state_inference:
  action_policy:
  validation_rule:
  blocked_if:
  feedback_update:
```

完成判断：

- 必须先定位唯一最高优先级短板；若观察到多个问题，也只能选一个 primary issue 进入下一轮修改。
- 必须区分 `technical_validation（技术验证）` 与 `content_validation（内容验证）`。
- 缺复审对象、用户反馈对象、灰度数据或需要用户审美判断时，必须 blocked / human_review_required，不得硬写事实。
- `voice_prosody_issue（声音韵律问题）` 优先动作是生成 `tts_prosody_anchor_map（TTS 韵律锚点表）`、重写分句和韵律，不默认换音色。
- `opening_visual_hook_issue（开头视觉钩子问题）` 优先动作是生成 `opening_visual_hook_spec（开头视觉钩子规格）`，并阻断静态两行标题通过高情绪开头验收。
- `script_visual_mismatch_issue（文案画面错位问题）` 优先动作是生成 `script_to_timeline_map（文案到时间线映射表）`，并在句子级映射缺失前阻断视频执行。

### 4A.4 与 Completion Relay Gate 的关系

本轮或后续任务一旦触发三个函数之一，`Completion Relay Gate（补全接力闸门）` 的 `required_output_inventory（必须交付清单）` 必须纳入：

1. 对应推理函数输出。
2. 对应卡片 / 决策包是否引用该函数。
3. 入口规则是否要求先输出该函数。
4. fixture / 最小样例是否覆盖正常判断与 blocked 判断。
5. `remaining_work_check（剩余工作检查）` 是否确认没有剩余 must-fix。
6. 若最终文案进入执行，是否已生成 `script_anchor_extraction_function（文案锚点提取函数）`、`script_to_timeline_map（文案到时间线映射表）`、`tts_prosody_anchor_map（TTS 韵律锚点表）` 与必要的 `opening_visual_hook_spec（开头视觉钩子规格）`。
7. 若 `judgment_card（判断卡）` 或 `summary_card（总结卡）` 被选中，是否已生成 `hyperframes_card_motion_plan（HyperFrames 卡片动效方案）`、`hyperframes_runtime_status（HyperFrames 运行时状态）`、`hyperframes_visual_quality_check（HyperFrames 视觉质量检查）`、`card_text_semantic_match（卡片文字语义匹配）`，并确认未用静态卡片冒充 HyperFrames。

## 5. 事实源裁决规则

默认事实源优先级：

1. GitHub / 本地 `main` 上的当前仓库文件。
2. `GPT数据源/` 当前正式机制包和事实文件。
3. `codex_log/latest.md`，但重要结论要回查直接源文件。
4. `dist/latest_review_pack/summary.json` 和 `review_manifest.md` 作为当前复审包状态证据。
5. 用户本轮明确指令，只对本轮有效；若要成为下一聊天事实，必须写回仓库。
6. GPT Project 静态上传包，只是协作包，不是实时事实库。
7. DeepSeek / Perplexity 输出只做供料或研究参考，不直接拍板项目事实。
8. Vector RAG / DashVector 检索和仓库原文件 readback 是默认执行输入；DeepSeek 只在条件触发时提供审查 / 风险复核 / 冲突二次意见，且仍必须由当前 `active_write_executor` 复核原文件后落地。

RAG 清洗层事实优先级补充：

1. `current_repo_source（当前仓库源文件）`
2. `real_run_report（真实执行报告）`
3. `latest_summary（最新摘要）`
4. `rag_retrieval_result（RAG 检索结果）`
5. `chat_memory（聊天记忆）`
6. `historical_archive（历史归档）`

命中 RAG / DashVector / 检索 / 供料 / 旧口径 / stale_index / source_conflict / completion_claim / user_minimal_review_panel 时，当前状态必须附加：

```text
current_project_state = rag_cleaning_layer_required
trigger_mechanism = RAG Cleaning Layer Execution Contract
must_read = codex_source/24_RAG清洗层执行契约_rag_cleaning_layer_execution_contract.md
schema = codex_source/schema_contracts/schemas/rag_cleaning_layer.schema.yaml
validator = scripts/rag_cleaning_layer_validator.py --fixtures
```

清洗层动作：

- `source_authority_classifier`：低权重来源不得覆盖当前事实。
- `stale_context_detector`：旧口径、历史归档、过期索引只能降权或路由修复。
- `conflict_cleaner`：冲突先按来源权重裁决，裁不了再进 ChatGPT / 用户判断。
- `decision_authority_router`：只把目标、验收、授权、删除、降级、发布 / 生产状态交给用户。
- `supply_pack_cleaner`：执行供料缺 `source_path / line_range / chunk_id / readback` 必须 blocked。
- `completion_claim_cleaner`：缺 commit / push / remote verification / vector sync boundary 不得写 completed。
- `user_minimal_review_panel`：只列用户必须拍板事项，不把普通工程细节交给用户。

必须裁决的冲突：

| conflict | Codex decision |
| --- | --- |
| GPT Project static package vs GitHub main | GitHub main wins |
| User current explicit instruction vs repo old fact | current instruction guides this round; sync to repo to become durable fact |
| DeepSeek supply vs original repo files | original repo files win |
| DeepSeek conditional trigger vs Codex discretion | trigger decision wins; if DeepSeek is triggered or user-required, Codex cannot skip without blocked reason |
| fallback_local_only vs DeepSeek conclusion | fallback is not DeepSeek conclusion |
| token not decreased vs DeepSeek participation claim | no deep participation claim without token evidence or user check |
| Perplexity reference vs repo formal facts | repo formal facts win |
| Reference-to-Execution Contract vs repo formal facts | repo formal facts win |
| technical_validation vs content_validation | content_validation cannot be upgraded by technical_validation |
| target_state_plan vs current_formal_fact | current_formal_fact wins |
| latest.md vs older dated logs | latest.md wins, then verify direct source files |
| summary.json vs chat memory | summary.json / repo files win |
| RAG retrieval vs repo readback | repo readback wins |
| historical archive vs current repo source | current repo source wins; history is kept but demoted |
| stale_index vs current worktree | current worktree wins; route stale index to RAG_sync_bus |
| completion claim vs missing git/vector evidence | completion claim is blocked |

## 6. 与 Completion Relay Gate 联动

`state_action_router` 和 `Completion Relay Gate（补全接力闸门）` 分工如下：

1. `state_action_router` 先判断当前状态和动作。
2. `Completion Relay Gate` 再保证动作执行到底。
3. 两者缺一不可。
4. 如果 `state_action_router` 没输出，Codex 不得进入执行。
5. 如果 `Completion Relay Gate` 没输出，Codex 不得写 `completed`。

`Reference-to-Execution Contract（参考到执行落地契约）` 插入在 `state_action_router` 和具体执行之间：

```text
input_signal = reference_provided / sample_reference_given / target_effect_given
-> if target effect is ambiguous, current_project_state = ambiguous_goal_clarification_needed
-> selected_action = clarify target layer before reference contract or Codex execution
-> current_project_state = reference_contract_needed
-> trigger_mechanism = Reference-to-Execution Contract
-> selected_action = create reference_to_execution_contract before concrete execution
-> Codex execution only after reference_anchor / effect_targets / function_fields / deviation_check / done_when are complete
```

如果任务带 reference，但没有 reference contract，Codex 必须 `blocked` 或先要求补齐 contract，不得直接执行。

推荐执行链：

```text
route_decision
-> state_action_router
-> reference_to_execution_contract if reference_contract_needed
-> required_output_inventory
-> child_task_graph
-> execution
-> validation
-> remaining_work_check
-> sync_back_check
-> completion_state_inference
```

## 7. completion_state_inference 执行口径

Codex 收尾时必须按以下四态判断：

| completion_state | 可写条件 | 不可写条件 |
| --- | --- | --- |
| `completed` | 仓库写明的目标、产物、验证、同步、回报全部完成；供料来源裁决、DeepSeek 触发判断及必要参与报告 / token 检查边界写清；若本轮改了仓库文件，则相关文件已显式 stage、commit 已创建、push 已成功、远端 HEAD 已校验、unrelated dirty files 未被提交、secret scan 通过；无禁止状态推进；无剩余 must-fix | 任一 required item 未完成；DeepSeek 已触发或用户要求但被跳过且无 blocked 原因；fallback 被写成 DeepSeek 结论；internal diagnostic、local-only output、partial result、技术预览、无声视频、比例错误视频被当成交付；本地改动未 commit / 未 push / 未远端校验 |
| `partial_completed` | 仅用于用户明确接受的分阶段任务，且已完成项可验证、未完成项已列入 remaining_work_check；或本地改动完成但 push / remote verification 未完成且 reason = `local_changes_done_but_not_pushed` | 完整交付任务不得用它替代 blocked；不得对用户写成已完成；不得在仓库文件改动未完成 Git 收尾时伪装 completed |
| `blocked` | 缺关键文件、缺用户输入、需要 secret / API、需要修改禁止状态、证据不足、push 失败、当前分支不明、unrelated dirty files 无法隔离、secret scan failed、remote HEAD 无法校验 | 不得用猜测继续 |
| `continue` | 无 blocked，仍有必交付项 | Codex 必须继续执行，不得结束 |

RAG 清洗层补充完成口径：

- 命中 `rag_cleaning_layer_required` 时，`completed` 还必须满足：契约、schema、validator、fixture、供料包接入、失败路由、trace、dated log、latest、验证、commit、push、remote verification 和 post-commit vector sync boundary 全部有证据。
- 任何 `summary_only`、`missing_readback`、`stale_index_claim_current`、`legacy_overrides_current`、`completion_claim_risk`、`git_sync_incomplete` 都必须写 `blocked` 或继续修复，不得写 `completed`。
- 清洗层通过只代表机制补缺通过，不代表内容验证、可发送、声音验证、视觉母版锁定或生产可用状态推进。

## 8. feedback_update 执行口径

执行结果改变下一轮默认判断时，必须写回相应位置：

- 改机制入口：更新 `GPT数据源/` 或 `codex_source/` 相关文件，并写 latest。
- 改 GPT Project 静态包：更新 `codex_log/current_local_artifact_paths.md`，manifest 必须写边界。
- 改复盘数据：更新 `review_loop/` 对应记录和 missing fields。
- 发现失败：写失败信号、失败原因、blocked 条件和下一安全动作。
- 用户说“不对 / 怪 / 不顺”：先分类再动手，类别包括 `direction / structure / evidence / editing / voice / quality / route / state conflict`。

## 9. 本轮禁止状态推进

默认不得推进：

- `content_validation（内容验证）`
- `send_ready（可发送状态）`
- `publish_status（发布状态）`
- `voice_validation（声音验证）`
- `final_voice_validated（最终声音验证）`
- `visual_master_locked（视觉母版锁定）`

默认不得执行：

- 读取 `.env`、API key、token、secret
- 调用 DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API
- 修改视频、图片、音频、时间线、字幕或 `dist/latest_review_pack/` 媒体产物
- 新建外部工作区

## 10. 一句话规则

**Codex 每轮先用 `state_action_router` 判状态和动作，再进入 `supply_source_arbitration（供料来源裁决）`，按 Vector RAG / DashVector 检索、仓库原文件 readback 和 `deepseek_trigger_decision` 决定是否需要 DeepSeek 条件审查，最后用 `Completion Relay Gate` 把动作做完；没有状态动作判断不得执行，没有触发判断不得写 DeepSeek 缺席或参与，没有补全接力复核不得写 completed。**
