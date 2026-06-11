# 20260611 Conflict Map

## 0. purpose

This file records conflicts that a future RAG Router must arbitrate before handing work to skills or Codex execution. It is not a deletion list and does not change formal rules.

## 1. conflict_summary

| metric | count |
|---|---:|
| total_conflict_groups | 18 |
| high_risk_conflicts | 10 |
| mostly_legacy_conflicts | 5 |
| pending_validation_conflicts | 3 |

## 2. high_risk_top_10

| rank | conflict | stale_or_risky_reading | current_preferred_reading | router_action |
|---:|---|---|---|---|
| 1 | Prompt as complete workflow | Use only current GPT prompt to execute | Prompt is `prompt_delta`; read full process entries | trigger `process_boot_required` |
| 2 | New material equals only new material | Cut only newly added materials | Default `additive_merge`; rebuild full context | classify `material_delta_type` before edit |
| 3 | Technical preview as delivery | Deliver silent/preview/route-card output | Formal delivery is `publish_candidate` or `blocked` | require completion validation |
| 4 | `full.mp4` as completion | File exists, therefore completed | Need preflight suite, review pack, completion truth | trigger `completion_truth_preflight` |
| 5 | `technical_validation` as `content_validation` | Technical pass means content pass | Content requires human/ChatGPT review boundary | block status promotion |
| 6 | `publish_candidate_ready_for_human_review` as `send_ready` | Candidate can be sent | `send_ready=false` until final confirmation | keep final status locked |
| 7 | Old Qwen/Aliyun B as formal TTS route | Restore old provider as default | Old Qwen is reference anchor; MiniMax route/voice lock is current | route to voice conflict gate |
| 8 | MiniMax system voice as old B replacement | Pick any close system voice | Only locked `oldBMinimax20260528010200` after user confirmation | block system substitution |
| 9 | HyperFrames runtime pass as full chain stable | Runtime found means video route solved | Runtime proof is not full publish chain integration | require task-specific runtime gate |
| 10 | `current_data_goal_anchor` as ready | Treat partial data as ready | Current anchor remains partial unless explicitly ready | block data-driven execution ready |

## 3. full_conflict_table

| conflict_id | conflict_type | current_authority | stale_or_competing_source | resolution_status | recommended_router_rule |
|---|---|---|---|---|---|
| C01 | phase | `formal_operation_active` | `gray_test` | resolved_current_wins | demote `gray_test` to historical alias |
| C02 | delivery_baseline | `publish_candidate` or `blocked` | `technical_preview` | resolved_current_wins | block previews as delivery |
| C03 | aspect_ratio | `horizontal_16_9 / 1920x1080` default | old vertical 9:16 samples | resolved_current_wins | use vertical only if user explicitly selects |
| C04 | prompt_boundary | `prompt_delta` only | prompt-as-full-flow behavior | active_risk | require process boot context rebuild |
| C05 | material_delta | additive by default | new-only assumption | active_risk | require material delta classification |
| C06 | completion_truth | preflight + truth check | file/field existence | active_risk | retrieve validation evidence |
| C07 | content_status | human/ChatGPT final review | technical validation | active_risk | block status swap |
| C08 | send_status | final confirmation required | candidate-ready | active_risk | keep send_ready separate |
| C09 | B_voice_provider | MiniMax final provider with old B reference anchor | old Qwen/Aliyun as formal route | resolved_with_history | index old route only as reference lineage |
| C10 | B_voice_identity | `oldBMinimax20260528010200` | MiniMax system voice candidates | resolved_current_wins | block system voice substitution |
| C11 | female_voice_candidates | rejected/forbidden | prior female candidate facts | resolved_current_wins | blacklist as default B voice |
| C12 | HyperFrames_role | optional card motion wrapper | replacement for evidence/mid-section | active_risk | require card route and runtime gate |
| C13 | image2_role | visual base only | exact Chinese text authority | active_risk | route text to Codex overlay/exact layer |
| C14 | reference_role | quality/effect anchor | copying external assets/person/UI | active_risk | require reference-to-execution contract |
| C15 | DeepSeek_status | real call + token/evidence required | fallback local supply | active_risk | tag fallback as not DeepSeek conclusion |
| C16 | project_source_authority | auxiliary/historical | current formal facts | mostly_legacy | lower authority unless explicit archaeology |
| C17 | GPT_static_package | upload package snapshot | dynamic repo facts | mostly_legacy | use only when task is GPT Project sync |
| C18 | data_goal_ready | `partial_data_recorded` unless updated | assumed ready | pending_validation | require current anchor status retrieval |

## 4. router_arbitration_order

When retrieved chunks disagree, the future Router should resolve in this order:

1. User's current explicit task boundary for this turn.
2. `AGENTS.md` project route, safety, and stop lines.
3. `GPT数据源/08_当前正式事实.md` current facts.
4. Newest relevant section in `codex_log/latest.md`.
5. `codex_source/19_project_state_action_router.md`.
6. `codex_source/21_codex_judgment_permission_matrix.md`.
7. Workflow-specific formal rule files.
8. Runtime evidence and fixtures.
9. Reference-only/historical sources.

If there is still conflict after step 8, Router must output `conflict_pending` and block status promotion.

## 5. required_conflict_tags_for_vector_chunks

Future ingestion should tag chunks with:

```yaml
conflict_tags:
  phase_conflict:
  delivery_baseline_conflict:
  tts_provider_conflict:
  voice_identity_conflict:
  material_delta_conflict:
  prompt_boundary_conflict:
  completion_truth_conflict:
  status_promotion_conflict:
  reference_role_conflict:
  data_goal_conflict:
```

## 6. recommended_cleaning_actions

| action | destructive? | next_validation |
|---|---:|---|
| Add metadata to chunks instead of deleting old files | no | validate retrieval ranking |
| Demote historical sources from default search | no | conflict fixture |
| Keep old voice/reference facts as lineage only | no | voice router fixture |
| Add material delta policy to Router | no | new-material fixture |
| Add completion truth as final Router layer | no | completion fixture |
