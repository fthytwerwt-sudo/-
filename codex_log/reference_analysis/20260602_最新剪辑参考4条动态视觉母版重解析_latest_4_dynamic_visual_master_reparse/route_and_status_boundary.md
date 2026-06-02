# Route And Status Boundary

## route_decision

- `project_route = video_factory`
- `task_type = review_diagnosis_audit + reference_analysis_only + local_file_governance + project_file_change`
- `selected_state = dynamic_visual_master_parse`
- `responsibility_layer = project_judgment_layer + validation_layer + sync_layer`
- `why_not_video_task = user prompt explicitly forbids generating video, validation clip, full candidate, or modifying new fourth episode; this round only reparses source reference videos`
- `execution_permission = allowed_after_route_read_and_source_video_count_confirmed`

## state_action_router

- `input_signal = latest editing reference videos + prior parse rejected as insufficient visual standard`
- `current_project_state = reference_contract_needed + ambiguous_reference_goal_resolved_by_user_as_visual_look_dynamic_master + deepseek_supply_required + mandatory_commit_push_required`
- `fact_source_arbitration.primary_source = source videos under 素材录制/剪辑参考/最新剪辑参考`
- `fact_source_arbitration.prior_parse = diagnostic_reference_only`
- `trigger_mechanism = Reference-to-Execution Contract + dynamic visual master parse`
- `selected_action = generate frame evidence, timelines, visual maps, failure report, contract draft, migration notes, latest update`
- `forbidden_action = generate new video, edit source videos, update formal mechanisms, touch dist/latest_review_pack, promote validation/send states`
- `done_when = 4/4 probe + extraction passed, required reports exist, validation passes, path-limited commit/push/readback done`

## large_task_gate

- `large_task_gate.triggered = true`
- `large_task_gate.reason = 4 reference videos, each longer than 180 seconds or near it, with frame extraction, scene candidates, timelines, maps, validation, commit/push`
- `lane_recommendation = audit_lane -> standard_lane after source video evidence generated`
- `parallel_recommendation = serial_only`
- `parallel_reason = outputs share one report package and final judgment must integrate visual observations consistently`
- `write_owner = Codex integrator`
- `read_only_lanes = DeepSeek pre-supply attempted; source videos read-only; prior parse read via git show only`
- `integration_owner = Codex`

## deepseek_supply_gate

- `supply_request = codex_log/supply_requests/20260602_最新剪辑参考4条动态视觉母版重解析_pre_supply_request.json`
- `runner_output = codex_log/deepseek_supply/20260602_latest_4_dynamic_visual_master_reparse_pre_supply/latest_supply_pack.md`
- `deepseek_participation_report = blocked_invalid_context_pack`
- `fallback_status = fallback_local_only`
- `not_deepseek_conclusion = true`
- `token_usage_expectation_check = token_decrement_expected_if_real_call_succeeds / not_observable_by_codex`
- `api_key_printed = false`
- `api_key_written = false`

## source_videos

| reference | source_path | duration | resolution | fps | ffmpeg_smoke | opencv_open |
| --- | --- | --- | --- | --- | --- | --- |
| `reference_01` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-01-2026 23-49-21_1.MP4` | `345.827s` | `1180x2556` | `60.091` | `passed` | `True` |
| `reference_02` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-03-59_1.MP4` | `200.392s` | `1180x2556` | `60.098` | `passed` | `True` |
| `reference_03` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-07-32_1.mov` | `363.745s` | `1180x2556` | `60.094` | `passed` | `True` |
| `reference_04` | `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考/ScreenRecording_06-02-2026 00-16-59_1.mov` | `294.198s` | `1180x2556` | `60.096` | `passed` | `True` |

## allowed_changes

- `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `scripts/最新剪辑参考动态视觉母版重解析_generate_dynamic_visual_evidence.py`
- `scripts/最新剪辑参考动态视觉母版重解析_write_reports.py`
- `codex_log/supply_requests/20260602_最新剪辑参考4条动态视觉母版重解析_pre_supply_request.json`
- `codex_log/deepseek_supply/20260602_latest_4_dynamic_visual_master_reparse_pre_supply/`
- `codex_log/latest.md`

## forbidden_changes

- 不生成新第四期视频、验证片、完整候选片。
- 不修改 `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考` 源视频。
- 不修改 `GPT数据源/` 正式机制、`codex_source/` 正式规则、`dist/latest_review_pack/`。
- 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。
- 不把旧解析报告当正式视觉标准。

## actual_read_files

- `AGENTS.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/00_codex_readme.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_log/latest.md`
- `git show 191f02f431f424af42979830c3194305fb7b5e93:codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/...`
- `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md`

## status_boundary_check

- `video_rendered = false`
- `source_videos_modified = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`
- `dist_latest_review_pack_modified = false`
- `content_validation = not_applicable`
- `send_ready = false`
- `visual_master_locked = false`
