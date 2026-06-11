# 20260611 Mechanism Retention Audit Report

## 0. audit_scope

- `project_route`: `video_factory`
- `branch`: `feature/vector-rag-router-design-20260611`
- `execution_mode`: `design_audit_only`
- `repo_write_scope`: `codex_log/vector_rag_router_design/`
- `not_done`: no RAG implementation, no vector upload, no Alibaba / DashScope / DashVector API call, no media generation, no formal rule deletion.
- `cleaning_meaning`: classification and demotion advice only. This report does not physically delete old rules.

## 1. route_decision

```yaml
route_decision:
  project_route: video_factory
  task_type:
    - mechanism_or_route_fix
    - review_diagnosis_audit
    - external_research_bridge
  responsibility_layer:
    - entry_routing_layer
    - project_judgment_layer
    - validation_layer
    - mechanism_fix_layer
  large_task_gate:
    triggered: true
    reason: multi-file mechanism audit plus six design reports and git verification
    lane_recommendation: read_parallel_plus_single_integrator
    write_owner: Codex single integrator
  deepseek_supply_gate:
    attempted: false
    status: fallback_local_only
    reason: this branch task forbids external API/secret access and only needs local repository audit
    not_deepseek_conclusion: true
  allowed_changes:
    - codex_log/vector_rag_router_design/
  forbidden_changes:
    - GPT数据源/
    - codex_source/
    - scripts/
    - tests/
    - dist/
    - media/audio/image generation
    - secret files or secret values
    - main branch edits
```

## 2. must_read_status

| file_path | read_status | role |
|---|---:|---|
| `AGENTS.md` | read_ok | top-level route, single workspace, status boundary, git discipline |
| `codex_log/latest.md` | read_ok | latest mechanism landing log and execution evidence |
| `codex_source/00_codex_readme.md` | read_ok | Codex project entry and read order |
| `codex_source/01_execution_rules.md` | read_ok | executable gate and completion rules |
| `GPT数据源/00_项目总述.md` | read_ok | project identity |
| `GPT数据源/01_项目系统提示词.md` | read_ok | system prompt, process boot, prompt delta, delivery boundary |
| `GPT数据源/02_术语定义与状态边界.md` | read_ok | status vocabulary and forbidden status swaps |
| `GPT数据源/03_总索引与阅读顺序.md` | read_ok | reading order |
| `GPT数据源/04_选题与文案规则.md` | read_ok | topic and copy prewrite rules |
| `GPT数据源/05_文案路由规则.md` | read_ok | content route, card route, script anchor and HyperFrames boundary |
| `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | read_ok | mainline content carrier |
| `GPT数据源/07_AI知识类视频价值规则.md` | read_ok | content value and user-standard boundary |
| `GPT数据源/08_当前正式事实.md` | read_ok | canonical current facts |
| `GPT数据源/09_目标态计划.md` | read_ok | target-state plan |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | read_ok | OPC and multi-AI responsibility |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | read_ok | project state action router |
| `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` | read_ok | reference-to-execution contract |
| `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` | read_ok | data-goal to copy/execution bridge |
| `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` | read_ok | data-goal execution bus |
| `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md` | read_ok | copy reference learning and plain-language standard |
| `codex_source/13_execution_lane_and_parallel_rules.md` | read_ok | large task lane decision |
| `codex_source/19_project_state_action_router.md` | read_ok | Codex state-action router implementation spec |
| `codex_source/20_reference_to_execution_contract.md` | read_ok | Codex-side reference contract |
| `codex_source/21_codex_judgment_permission_matrix.md` | read_ok | Codex judgment permission matrix |
| `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` | read_ok | workflow entry routing index |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | read_ok | GPT Project multi-agent short route note |

## 3. scan_summary

| metric | count | note |
|---|---:|---|
| must-read files checked | 26 | all available and readable |
| text/json/python files in scanned project surfaces | 936 | candidates for future RAG ingestion after filtering |
| media/binary files in scanned project surfaces | 75 | excluded from text-vector ingestion by default |
| total files in scanned surfaces | 1052 | scan target: `GPT数据源`, `codex_source`, `codex_log`, `review_loop`, `project_source`, `scripts`, `dist/latest_review_pack` |
| explicit RAG/vector implementation matches | 0 | no `rag_router`, `vector_index`, `embedding_model`, `DashVector`, `OpenSearch`, or `Milvus` implementation found in current scan |
| active core mechanisms identified | 22 | curated from current formal rules and latest log |
| active runtime/script gates identified | 13 | runnable or fixture-backed entries |
| conflict-pending groups identified | 18 | see conflict map |
| do-not-index groups identified | 12 | see blacklist |

## 4. retention_classification_legend

| classification | meaning | vector_action |
|---|---|---|
| `retain_active_core` | current formal mechanism or fact, should be retrievable | index with high priority |
| `retain_runtime_gate` | executable script, fixture, or validation entry | index metadata and interface, not logs/noisy output |
| `retain_config_or_current_state` | current target, operation state, selected voice/card route | index with latest-only pointer metadata |
| `retain_reference_only` | useful historical/reference material, not authority by itself | index only with `reference_only=true` |
| `legacy_demote` | old route retained for history but lower priority | index only if router asks for history/conflict context |
| `deprecated_do_not_use` | old rule explicitly superseded | blacklist from default retrieval |
| `conflict_pending` | current repo contains valid-looking but conflicting rules | index only with conflict tag and router arbitration |
| `do_not_index` | secret, media, generated noise, local runtime, or sensitive data | exclude |

## 5. active_core_mechanisms_to_retain

| mechanism | classification | evidence_surface | why_keep |
|---|---|---|---|
| `Project State Action Router` | retain_active_core | `GPT数据源/11`, `codex_source/19` | top-level project state/action judgment |
| `route_decision_gate` | retain_active_core | `AGENTS.md`, `codex_source/19` | prevents entering wrong project/task layer |
| `workflow_route_decision` | retain_active_core | `codex_source/22` | maps tasks to copy/material/aesthetic/review/data/mechanism flows |
| `large_task_gate` | retain_active_core | `AGENTS.md`, `codex_source/13` | prevents long multi-file tasks from being handled as one prompt |
| `DeepSeek supply gate boundary` | retain_active_core | `GPT数据源/01`, `codex_log/latest.md`, `codex_source/19` | says fallback is not a DeepSeek conclusion and secrets must not leak |
| `Completion Relay Gate` | retain_active_core | `GPT数据源/01`, `codex_source/01`, `codex_log/latest.md` | connects horizontal task inventory to vertical completion |
| `process_boot_gate` | retain_active_core | `GPT数据源/01`, `codex_source/19`, `codex_log/latest.md` | treats GPT prompt as `prompt_delta`, not complete process source |
| `prompt_delta boundary` | retain_active_core | `GPT数据源/01`, `codex_source/19` | key anti-failure rule for temporary adjustments |
| `publish_candidate_required_inventory` | retain_active_core | `GPT数据源/01`, `codex_log/latest.md` | prevents partial artifacts from becoming completion |
| `publish_candidate_preflight_suite` | retain_active_core | `codex_source/01`, `codex_source/19`, `codex_log/latest.md` | central completion validation suite |
| `completion_truth_check` | retain_active_core | `codex_source/01`, `codex_source/21` | blocks `full.mp4 exists == completed` and status swaps |
| `locked_copy_contract` | retain_active_core | `GPT数据源/08`, `codex_source/21` | locks title/topic/final script/opening line |
| `locked_copy_diff_preflight` | retain_active_core | `codex_source/01`, `codex_source/21` | validates actual subtitle/TTS/card text against locked copy |
| `line_level_script_visual_alignment_gate` | retain_active_core | `GPT数据源/08`, `codex_source/01`, `codex_source/19` | requires line_group-level visual evidence alignment |
| `material_parse_pack_reuse_gate` | retain_active_core | `codex_source/01`, `codex_source/19`, `codex_log/latest.md` | prevents re-parsing or only looking at new material during editing |
| `material_evidence_gate` | retain_active_core | `codex_source/01`, `codex_source/19`, `scripts/素材证据闸门_material_evidence_gate.py` | blocks weak or mismatched material evidence |
| `near_equivalent_material_substitution_rule` | retain_active_core | `GPT数据源/08`, `codex_source/19`, `codex_source/21` | caps near-equivalent substitutions and blocks core mismatch |
| `data_goal_execution_bus` | retain_active_core | `GPT数据源/14`, `codex_source/19` | connects data goal to copy, editing, assembly, validation |
| `current_data_goal_anchor` boundary | retain_config_or_current_state | `codex_log/current_data_goal_anchor.md`, `GPT数据源/08` | current instance is partial, not ready |
| `Codex judgment permission matrix` | retain_active_core | `codex_source/21` | defines what Codex can decide, block, or escalate |
| `Reference-to-Execution Contract` | retain_active_core | `GPT数据源/12`, `codex_source/20` | prevents reference style from becoming blind copying |
| `no_degrade_completion_gate` | retain_active_core | `GPT数据源/08`, `codex_source/19` | blocks technical preview/fallback as completion |

## 6. runtime_or_fixture_entries_to_retain

| entry | classification | note |
|---|---|---|
| `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` | retain_runtime_gate | runnable preflight suite |
| `scripts/素材证据闸门_material_evidence_gate.py` | retain_runtime_gate | material evidence validation |
| `scripts/素材解析包复用闸门_material_parse_pack_reuse_gate.py` | retain_runtime_gate | material parse pack reuse validation |
| `scripts/卡片判断闸门_card_decision_gate.py` | retain_runtime_gate | card decision gate |
| `scripts/运营决策系统_operation_decision_system.py` | retain_runtime_gate | operation decision system |
| `scripts/文案迭代决策系统_copy_iteration_decision_system.py` | retain_runtime_gate | copy iteration decision system |
| `scripts/正片候选TTS路线_publish_candidate_tts_route.py` | retain_runtime_gate | TTS route inspection |
| `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py` | retain_runtime_gate | secret-safe DeepSeek runner |
| `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py` | retain_runtime_gate | DeepSeek provider boundary |
| `codex_source/fixtures/publish_candidate_preflight_suite_cases.json` | retain_runtime_gate | blocked-case fixture |
| `codex_source/fixtures/素材证据闸门_material_evidence_gate_cases.json` | retain_runtime_gate | material evidence fixture |
| `codex_source/fixtures/素材解析包复用闸门_material_parse_pack_reuse_gate_cases.json` | retain_runtime_gate | parse pack reuse fixture |
| `codex_source/fixtures/project_state_action_router_cases.json` | retain_runtime_gate | router fixture |

## 7. legacy_or_deprecated_candidates

| item | classification | reason |
|---|---|---|
| `gray_test` as current phase | deprecated_do_not_use | current phase is `formal_operation_active`; gray test is historical alias |
| `technical_preview` as user delivery | deprecated_do_not_use | current baseline is `publish_candidate` or `blocked` |
| `vertical_9_16 / 1080x1920` as default formal delivery | legacy_demote | retained as historical/sample/special route only |
| old `v3` as default future base | deprecated_do_not_use | v3.1 and later formal-operation facts supersede it |
| `PR #7 A` as reaction card reference | deprecated_do_not_use | PR #7 B is the surviving reaction card route |
| old Qwen/Aliyun B route as formal TTS provider | deprecated_do_not_use | retained as reference anchor only after MiniMax migration |
| MiniMax system voices as old B replacement | deprecated_do_not_use | user-confirmed voice lock is `oldBMinimax20260528010200` |
| `project_source/` as higher authority than current `GPT数据源/` | legacy_demote | project_source is auxiliary/historical unless explicitly routed |
| GPT Project static package as current facts | legacy_demote | current dynamic facts live in repo formal sources and latest log |
| `full.mp4 exists` as completion | deprecated_do_not_use | must pass completion truth and preflight |

## 8. architecture_gap_findings

| gap | status | impact |
|---|---|---|
| True RAG Router | not_found | Codex still depends on prompt plus file reading discipline, not automated retrieval/arbitration |
| Vector index | not_found | no persistent semantic memory of current facts/conflicts |
| Embedding model config | not_found | no `embedding_model` or dimensions configuration found |
| Skill Registry | not_found_as_registry | stable gates/scripts exist, but no registry mapping skill name -> trigger -> inputs -> outputs -> validation |
| Dynamic Task Graph | partial_documented | `Completion Relay Gate` and `child_task_graph` concept exists, but no runtime graph scheduler found |
| Material Delta Merge Policy | partial_documented | material reuse/evidence gates exist, but explicit additive/replacement/exclusive router policy is not yet centralized |
| Completion Validation | partially_implemented | strong preflight/check scripts exist for video candidates; not yet generalized as router validation layer |

## 9. retention_decision

The project should not directly vectorize the whole repository. It should first build a curated ingestion whitelist, blacklist, conflict map, and router dependency map.

`confirmed_by_repo`:

- Current authoritative phase is `formal_operation_active`.
- `technical_preview` is not user delivery.
- `publish_candidate_preflight_suite`, `material_evidence_gate`, `material_parse_pack_reuse_gate`, `completion_truth_check`, `locked_copy_contract`, and `Codex judgment permission matrix` are current mechanisms.
- No current `rag_router`, `vector_index`, `embedding_model`, `DashVector`, `OpenSearch`, `Milvus`, or `skill_registry` implementation was found in the scanned repo surfaces.

`recommendation`:

- Keep current mechanisms, but index them through a whitelist with metadata.
- Demote historical rules instead of deleting them.
- Add a future Router arbitration layer before any vector ingestion.
- Treat Skill Registry as a registry over stable actions, not as a fixed video workflow.

`pending_validation`:

- The later RAG Router must prove it can retrieve current facts and demote stale facts in a small fixture before production use.
- The later Skill Registry must prove each skill has declared inputs, outputs, blocked conditions, and validation evidence.
