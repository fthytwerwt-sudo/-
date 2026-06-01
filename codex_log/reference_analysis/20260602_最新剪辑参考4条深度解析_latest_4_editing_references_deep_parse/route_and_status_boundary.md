# 路由与状态边界 Route And Status Boundary

status_boundary:
- `task_result.status = reference_analysis_completed_pending_user_review`
- `mechanism_status = draft_pending_chatgpt_user_review`
- `content_validation = not_applicable（本轮不做内容验证）`
- `send_ready = false（不可发送）`
- `video_rendered = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`
- `code_or_function_landed = false`
- `ocr_status = unavailable_local_tesseract_not_found`
- `deepseek_actual_participation = not_attempted_policy_violation / blocked_invalid_context_pack`

## route_decision

```yaml
project_route: video_factory
task_type:
  - review_diagnosis_audit
  - local_file_governance
  - project_file_change_reference_analysis_artifacts_only
responsibility_layer:
  - entry_routing_layer
  - project_judgment_layer
  - execution_layer
  - validation_layer
  - sync_layer
large_task_gate:
  triggered: true
  reason:
    - 4 reference videos, all longer than 180 seconds
    - timeline / split-screen / keyword / subtitle / icon / rhythm / mechanism drafts all required
    - more than 3 repository output files are generated
  lane_recommendation: audit_lane_to_standard_lane
  lane_reason: first confirm source media and boundaries, then write bounded analysis artifacts
  lane_invalid_if: source video unreadable, exact text invented without OCR, output starts modifying formal mechanisms
  parallel_recommendation: serial_only
  parallel_reason: one integrator owns one shared report directory and one manifest; no Codex subagent was explicitly requested by user
  parallel_invalid_if: any worker would write shared reports or formal project files
  write_owner: Codex integrator only
  read_only_lanes:
    - local ffprobe / OpenCV sampling
    - manual visual review of generated contact sheets
  integration_owner: Codex
allowed_changes:
  - codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/
  - dist/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/
forbidden_changes:
  - source reference video files
  - new fourth episode materials or current candidate media
  - GPT数据源/
  - formal mechanism files outside this analysis directory
  - dist/latest_review_pack/
  - content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked
execution_permission: allowed_for_reference_analysis_artifacts_only
```

## workflow_route_decision

```yaml
workflow_type: aesthetic_editing_flow + quality_review_flow
reason: user supplied editing reference videos and asks for deep parsing before any edit
must_read:
  - AGENTS.md
  - codex_source/00_codex_readme.md
  - codex_source/19_project_state_action_router.md
  - codex_source/20_reference_to_execution_contract.md
  - GPT数据源/10_OPC一人公司闭环与多AI协作机制.md
  - GPT数据源/11_项目状态动作总控器_机制推理层.md
  - GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md
  - codex_log/latest.md
required_handoff:
  - reference_video_inventory
  - timeline_full_parse_files
  - split_screen_system_map
  - keyword_subtitle_icon_map
  - editing_action_taxonomy
  - rhythm_transition_profile
  - mechanism_and_quality_standards_drafts
forbidden_status:
  - content_validation = passed
  - send_ready = true
  - visual_master_locked = true
blocked_if:
  - reference_count != 4
  - frame_observation_unavailable
  - OCR missing but exact text invented
```

## state_action_router

```yaml
input_signal: user_provided_reference_videos + attached Codex execution order
current_project_state:
  - formal_operation_active
  - reference_contract_needed
  - editing_inference_needed
  - quality_review_needed
fact_source_arbitration:
  primary_source:
    - repository files under /Users/fan/Documents/视频工厂
    - the four local reference videos
    - current user prompt
  conflict_detected: false_for_scope
  conflict_resolution: write analysis artifacts only; do not promote project facts
inferred_state: reference analysis can proceed, video delivery and formal mechanism update forbidden
confidence: high
trigger_mechanism:
  - Reference-to-Execution Contract
  - Completion Relay Gate
  - large_task_gate
selected_action: generate bounded draft analysis reports and media evidence sheets
forbidden_action:
  - render or assemble video
  - modify source videos
  - modify formal mechanism files
  - call external paid API
  - read or print secrets
done_when: all required report files and manifest exist, status boundaries explicit, human review required
feedback_update_required: false_for_formal_files; true_inside_analysis_manifest
```

## actual_read_status

| file | status | purpose |
| --- | --- | --- |
| `AGENTS.md` | `read_ok` | project routing, large task gate, allowed / forbidden changes |
| `codex_source/00_codex_readme.md` | `read_ok` | formal operation delivery and no-degrade boundary |
| `codex_log/latest.md` | `read_ok_relevant_sections` | previous reference analysis and current status boundary |
| `GPT数据源/00_项目总述.md` | `read_ok` | OPC identity and reference quality mechanism |
| `GPT数据源/01_项目系统提示词.md` | `read_ok` | reference, DeepSeek and video execution rules |
| `GPT数据源/03_总索引与阅读顺序.md` | `read_ok` | required reading order |
| `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | `read_ok` | current carrier boundary |
| `GPT数据源/08_当前正式事实.md` | `read_ok_relevant_sections` | forbidden status promotion and current facts |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | `read_ok` | AI role split and OPC loop |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `read_ok` | router and DeepSeek gate |
| `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` | `read_ok` | reference contract fields |
| `codex_source/13_execution_lane_and_parallel_rules.md` | `read_ok` | lane / parallel decision |
| `codex_source/17_deepseek_supply_controller_protocol.md` | `read_ok` | DeepSeek safe runner boundary |
| `codex_source/18_deepseek_supply_request_schema.md` | `read_ok` | supply request schema |
| `codex_source/19_project_state_action_router.md` | `read_ok` | Codex-side router |
| `codex_source/20_reference_to_execution_contract.md` | `read_ok` | Codex-side reference contract |
| `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` | `read_ok` | workflow route decision |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | `read_ok` | large task gate and Completion Relay Gate reminder |
| previous `deep_reference_reparse_report.md` | `read_ok` | history comparison only |
| previous `editing_decision_pack_for_next_round.md` | `read_ok` | history comparison only |
| `video-metadata-probe` skill | `read_ok` | metadata / technical validation boundary |

## impact_check

| item | result |
| --- | --- |
| repository | `/Users/fan/Documents/视频工厂` |
| branch | `codex/guided-proof-video-upgrade-20260531` |
| unrelated_dirty_files | pre-existing `?? public/`, not touched |
| reference_dir_exists | true |
| reference_count | 4 |
| ffprobe_metadata | passed for 4/4 |
| ffmpeg_single_frame_extract | passed for 4/4 |
| OpenCV_sampling | passed for 4/4 |
| video-metadata-probe_full_decode | failed for 4/4; treated as reference-only decode warning, not clean media validation |
| output_overwrite_risk | no old directory with same timestamp was overwritten |
| old_reference_reports | found and read as history only |

## completion_relay_gate

required_output_inventory:
- reference_video_inventory.md
- reference_role_classification.md
- reference_01_timeline_full_parse.md
- reference_02_timeline_full_parse.md
- reference_03_timeline_full_parse.md
- reference_04_timeline_full_parse.md
- split_screen_system_map.md
- keyword_subtitle_icon_map.md
- editing_action_taxonomy.md
- rhythm_transition_profile.md
- reference_editing_mechanism_draft.md
- quantitative_quality_standards_draft.md
- migration_notes_for_new_fourth_episode.md
- analysis_manifest.json

child_task_graph:
1. media probe and directory inventory
2. frame sampling and contact sheet generation
3. role classification
4. per-reference timeline parse
5. cross-reference mechanism extraction
6. quantitative standard draft
7. manifest / boundary / verification check

remaining_work_check:
- no video render requested or performed
- no formal mechanism update requested or performed
- exact OCR text remains low-confidence where not manually readable
- final acceptance requires ChatGPT / user review
