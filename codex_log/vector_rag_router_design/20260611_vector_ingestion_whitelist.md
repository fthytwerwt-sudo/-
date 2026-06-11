# 20260611 Vector Ingestion Whitelist

## 0. purpose

This whitelist defines what can be indexed in a future RAG layer for 《视频工厂》. It is a design artifact only. It does not create a vector index and does not upload any content.

Core principle: RAG should retrieve the latest project facts, mechanisms, current state, review evidence, and conflict metadata. RAG must not become a blind full-repo memory dump.

## 1. default_metadata_schema

Every indexed chunk should carry:

```yaml
metadata:
  project_route: video_factory
  source_path:
  source_type:
    - formal_rule
    - current_fact
    - latest_log
    - runtime_gate
    - fixture
    - review_pack
    - operation_record
    - historical_reference
    - conflict_map
  authority_level:
    - canonical_current
    - current_runtime_evidence
    - current_auxiliary
    - reference_only
    - legacy_demoted
    - conflict_pending
  status_label:
    - confirmed_by_repo
    - partial
    - pending_validation
    - recommendation
    - deprecated
  effective_date:
  supersedes:
  superseded_by:
  route_tags:
  workflow_type:
  task_type:
  validation_required:
  do_not_use_for_completion_claim: true_or_false
```

## 2. priority_1_canonical_current_sources

| source | ingestion_scope | authority_level | reason |
|---|---|---|---|
| `AGENTS.md` | project route, single workspace, route decision, status boundaries | canonical_current | top-level working contract |
| `GPT数据源/01_项目系统提示词.md` | current system prompt and mandatory gates | canonical_current | defines prompt-delta, process boot, DeepSeek boundary |
| `GPT数据源/02_术语定义与状态边界.md` | status vocabulary and forbidden status swaps | canonical_current | prevents `technical_validation`/`content_validation` confusion |
| `GPT数据源/03_总索引与阅读顺序.md` | reading order and route map | canonical_current | default retrieval seed |
| `GPT数据源/08_当前正式事实.md` | current facts only | canonical_current | primary fact source |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | role split and OPC mechanism | canonical_current | collaboration model |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | Project State Action Router | canonical_current | routing logic |
| `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` | reference contract | canonical_current | prevents reference misuse |
| `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` | data-goal to copy/execution bridge | canonical_current | data-driven content chain |
| `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` | data goal bus | canonical_current | execution alignment |
| `codex_source/19_project_state_action_router.md` | Codex-side state/action router | canonical_current | concrete Codex routing spec |
| `codex_source/21_codex_judgment_permission_matrix.md` | Codex judgment permissions | canonical_current | decide/block/escalate boundaries |
| `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` | workflow entry index | canonical_current | task-to-workflow dependency |

## 3. priority_2_execution_and_validation_sources

| source | ingestion_scope | authority_level | reason |
|---|---|---|---|
| `codex_source/00_codex_readme.md` | Codex entry and source order | current_auxiliary | implementation orientation |
| `codex_source/01_execution_rules.md` | executable rules and preflight definitions | canonical_current | completion validation |
| `codex_source/13_execution_lane_and_parallel_rules.md` | lane and parallel rules | canonical_current | large task routing |
| `codex_source/20_reference_to_execution_contract.md` | Codex reference contract | canonical_current | execution translation |
| `codex_source/fixtures/*.json` | only schema-like fixture cases for current gates | current_runtime_evidence | validates router/gate behavior |
| `scripts/发片候选预检套件_publish_candidate_preflight_suite.py` | CLI interface, gate list, inputs/outputs | current_runtime_evidence | runtime preflight |
| `scripts/素材证据闸门_material_evidence_gate.py` | CLI interface and validation fields | current_runtime_evidence | material evidence |
| `scripts/素材解析包复用闸门_material_parse_pack_reuse_gate.py` | CLI interface and validation fields | current_runtime_evidence | parse-pack reuse |
| `scripts/卡片判断闸门_card_decision_gate.py` | card decision interface | current_runtime_evidence | card route validation |
| `scripts/运营决策系统_operation_decision_system.py` | operation decision interface | current_runtime_evidence | review loop routing |
| `scripts/文案迭代决策系统_copy_iteration_decision_system.py` | copy iteration interface | current_runtime_evidence | copy/data bridge |

## 4. priority_3_latest_state_and_review_sources

| source | ingestion_scope | authority_level | note |
|---|---|---|---|
| `codex_log/latest.md` | latest mechanism facts and landing history | current_runtime_evidence | chunk by date heading; latest sections higher priority |
| `codex_log/current_operation_target.md` | current operation target | current_auxiliary | index as latest-only pointer |
| `codex_log/current_data_goal_anchor.md` | current data-goal instance | current_auxiliary | do not promote `partial_data_recorded` to ready |
| `codex_log/current_publish_target.md` | current publish target pointer | current_auxiliary | use only with status boundary |
| `codex_log/current_publish_target_light_evidence.md` | light evidence pointer | current_auxiliary | useful for current target lookup |
| `review_loop/operation_records_index.md` | operation record index | current_auxiliary | route to per-video records |
| `review_loop/decision_engine/latest_operation_decision_report.md` | latest operation decision report | current_runtime_evidence | current decision evidence |
| `dist/latest_review_pack/summary.json` | latest review pack summary only | current_runtime_evidence | metadata only, no media |
| `dist/latest_review_pack/review_manifest.md` | latest review manifest only | current_runtime_evidence | review pack pointer |
| `dist/latest_review_pack/visual_route_map.json` | visual route map | current_runtime_evidence | current route evidence |
| `dist/latest_review_pack/visual_route_validation_report.json` | visual route validation | current_runtime_evidence | validation evidence |

## 5. priority_4_domain_rules

| source | ingestion_scope | authority_level |
|---|---|---|
| `GPT数据源/04_选题与文案规则.md` | topic/copy rules, prewrite decision card | canonical_current |
| `GPT数据源/05_文案路由规则.md` | content route, card route, script anchor function, HyperFrames boundary | canonical_current |
| `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | mainline carrier, not fixed dead workflow | canonical_current |
| `GPT数据源/07_AI知识类视频价值规则.md` | AI knowledge video value and publish standard | canonical_current |
| `GPT数据源/09_目标态计划.md` | target-state planning | current_auxiliary |
| `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md` | copy reference and human language standard | canonical_current |

## 6. reference_only_sources

| source | ingestion_scope | rules |
|---|---|---|
| `project_source/` | historical/auxiliary project source | index only when router asks for historical reference or conflict archaeology |
| `codex_log/reference_analysis/` | reference analysis reports | `reference_only=true`; never supersede current facts |
| `codex_log/material_audit/` | material parse packs and handoff reports | use for material evidence tasks; require latest/candidate metadata |
| `review_loop/records/` | per-video operation records | route by `video_id` and time window; do not average across videos blindly |
| `review_loop/learning_ledger/` | learning ledger | auxiliary trend evidence; not current fact by itself |
| `codex_log/deepseek_supply/*/latest_supply_pack.md` | readonly supply packs | index as supply evidence only; `not_deepseek_conclusion` if fallback |

## 7. chunking_policy

| document_type | chunking |
|---|---|
| formal rules | split by heading; preserve heading path |
| latest log | split by date section; prefer newest sections when status conflicts |
| JSON fixtures | one case per chunk with `case_id` |
| scripts | index top docstring, CLI args, constants, output schema, blocked conditions; skip generated media paths |
| review pack JSON | index stable metadata fields only; skip frame lists and media hashes unless needed |
| operation records | one `video_id + time_window` chunk |

## 8. retrieval_priority

Default retrieval order for future RAG Router:

1. `AGENTS.md` route and boundary.
2. `GPT数据源/08_当前正式事实.md`.
3. `codex_log/latest.md` latest relevant date sections.
4. `codex_source/19_project_state_action_router.md`.
5. `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`.
6. Workflow-specific formal rule files.
7. Runtime gate/script/fixture entries.
8. Review pack or operation record pointers.
9. Reference-only sources, only if explicitly required.

## 9. material_delta_metadata

Future ingestion should tag all material-related chunks with:

```yaml
material_context:
  material_batch_id:
  candidate_id:
  source_segment_inventory_path:
  material_parse_pack_path:
  related_locked_copy_path:
  latest_review_pack_path:
  material_delta_type:
    - additive_merge
    - replacement_merge
    - exclusive_new_only
    - unclear_blocked
  old_material_status:
  new_material_status:
  replacement_scope:
  requires_full_context_rebuild: true
```

Default policy:

- `additive_merge` is default.
- `replacement_merge` requires explicit replacement scope.
- `exclusive_new_only` is allowed only when the user explicitly says only new materials may be used.
- `unclear_blocked` applies when the relationship between old and new materials is unclear.
