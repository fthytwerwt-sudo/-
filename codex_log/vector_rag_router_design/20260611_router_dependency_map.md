# 20260611 Router Dependency Map

## 0. purpose

This file defines what a future RAG Router must retrieve before it calls skills or allows Codex execution. It is design preparation only.

## 1. proposed_router_pipeline

```text
user_task
-> route_decision
-> workflow_route_decision
-> task_delta_extraction
-> RAG context retrieval
-> conflict arbitration
-> material_delta_type classification
-> skill graph selection
-> dynamic_task_graph build
-> completion_validation_plan
-> execute_or_block
```

## 2. layer_responsibilities

| layer | responsibility | examples |
|---|---|---|
| RAG Layer | retrieve latest project facts, rules, logs, candidates, review packs, material inventories, conflicts | current formal facts, latest log sections, current data goal, locked copy |
| Router Layer | decide workflow, conflicts, material delta type, required skills, blocked conditions | copy flow vs material flow vs mechanism repair |
| Skill Registry | expose stable repeatable actions with inputs/outputs/validation | material inventory, locked copy diff, preflight suite |
| Dynamic Task Graph | assemble this round's skill sequence and dependencies | process boot -> context rebuild -> material merge -> preflight |
| Completion Validation | verify outputs and forbid false completion | preflight reports, secret scan, git sync, no status promotion |

## 3. workflow_dependency_table

| workflow_type | trigger_signals | required_retrieval_set | required_skills_or_gates | block_if_missing |
|---|---|---|---|---|
| `copy_testing_flow` | final copy, rewrite, next video script | current facts, copy rules, data goal anchor, material report, latest copy decision | prewrite decision, content route card, script anchor extraction | data goal missing, material support unknown, final copy source unclear |
| `material_evidence_flow` | new recordings, screenshots, material audit | material inventory, current script/copy goal, material parse rules, evidence gates | material inventory, material evidence gate, missing material report | source segment inventory missing, timecodes missing, cannot_support selected |
| `aesthetic_editing_flow` | make it polished, edit, repair visual rhythm | latest candidate, review pack, locked copy, material parse pack, current card route, visual route map | material parse reuse, line alignment, card decision, overlap check | parse pack stale, locked copy mismatch, core evidence unreadable |
| `quality_review_flow` | review, not good, send_ready, content validation | latest log, current formal facts, review pack summary/manifest, user feedback | quality issue classifier, completion truth, no-degrade check | technical/content status mixed, missing review pack, user final review absent |
| `data_review_flow` | 24h/72h/7d data, replay, next variable | operation target, records index, current data goal anchor, per-video record | operation decision system, threshold check, next variable draft | video_id/time_window unknown, fields missing, multiple variables changed |
| `mechanism_repair_flow` | rule repair, route repair, vector/RAG design | AGENTS, codex readme, execution rules, router, latest log, affected rule surfaces | impact check, conflict map, fixture/keyword check, git sync | formal status would be changed, media/API required, dirty unrelated changes cannot be isolated |

## 4. material_delta_router

```yaml
material_delta_router:
  input_signals:
    - user_added_material
    - user_replaced_material
    - user_said_only_new_material
    - old_candidate_exists
    - locked_copy_exists
    - latest_review_issues_exist
  output:
    material_delta_type:
      - additive_merge
      - replacement_merge
      - exclusive_new_only
      - unclear_blocked
```

| material_delta_type | condition | retrieval_required | allowed_action |
|---|---|---|---|
| `additive_merge` | user adds material without saying replace/only use new | old material inventory, new material inventory, latest candidate, locked copy, latest review issues | merge inventory and rebuild timeline context |
| `replacement_merge` | user specifies what old material is replaced | old inventory, new inventory, replacement scope, affected line groups | replace only declared scope, keep other context |
| `exclusive_new_only` | user explicitly says only use new material | new inventory, locked copy, latest review issues, exclusion confirmation | ignore old material only after explicit confirmation |
| `unclear_blocked` | relationship is unclear or old candidate state missing | ask/block with missing fields | no edit or generation |

Default: `additive_merge`.

## 5. skill_registry_candidates

These are candidates for a future Skill Registry. They should be stable, repeatable, and verifiable.

| skill_name | inputs | outputs | validation |
|---|---|---|---|
| `process_boot_skill` | user task, current route, must-read entries | `process_boot_report`, `prompt_delta`, blocked lines | all mandatory entries read or blocked |
| `full_context_rebuild_skill` | current facts, latest log, current candidate, review pack, task delta | `current_context_pack` | source priority and conflict tags present |
| `material_inventory_skill` | material paths/reports | `material_inventory`, `source_segment_inventory` | paths exist, media not uploaded, timecodes extracted or missing marked |
| `material_delta_merge_skill` | old inventory, new inventory, task delta | `material_delta_type`, merged inventory | additive/replacement/exclusive/blocked classification |
| `locked_copy_diff_skill` | locked copy, actual subtitles/TTS/card text | `locked_copy_diff_report` | semantic diff blocked |
| `component_decision_skill` | script, route, data goal, material support | `component_decision_table` | needed/not-needed reasons present |
| `card_decision_skill` | line groups, card route, visual reference | `card_placement_decision` | card route, text authority, motion wrapper status |
| `tts_audio_music_skill` | TTS route, voice lock, prosody anchors | `tts_route_report`, `prosody_report` | actual provider/model/voice and non-silent audio if generated |
| `publish_candidate_preflight_skill` | candidate pack and reports | preflight report and subreports | all required gates passed or blocked |
| `completion_truth_skill` | required inventory, outputs, git status | completion truth report | no false completion/status promotion |
| `git_sync_skill` | changed files, branch policy | commit, push, remote readback | path-limited staging and remote HEAD verified |

## 6. non_skill_items

These should not become fixed skills because they change too often:

| item | keep_as | reason |
|---|---|---|
| specific video topic/title/final script | Task Delta / locked copy | user/ChatGPT controlled |
| visual taste target for one video | Task Delta + reference contract | not stable enough |
| temporary card text | Task Delta | content-specific |
| data target for a single video | Config/current data goal instance | changes by operation stage |
| new material list | Task Delta + material inventory | dynamic |
| exact provider credentials | secure local env/config | secret, not skill |
| Alibaba vector store choice | Config | deployment decision |
| embedding dimensions | Config | cost/quality tuning |

## 7. completion_validation_plan

Router should attach a validation plan before execution:

| task_type | required_completion_validation |
|---|---|
| mechanism report | file existence, structure check, diff check, secret scan, branch push, remote HEAD readback |
| video publish candidate | preflight suite, media probe, audio non-silent, subtitle/card overlap, locked copy diff, completion truth |
| material audit | inventory, metadata probe, timecode evidence, missing/uncertain report |
| data intake | video_id/time_window separation, missing fields, no final judgment if data insufficient |
| copy handoff | source check, data goal anchor, material support, locked copy boundary |

## 8. minimal_future_router_fixture

Before any real vector ingestion, build three fixture tasks:

1. `new_material_additive_merge_fixture`: old candidate + new material + latest review -> must retrieve all and classify additive.
2. `technical_preview_false_completion_fixture`: generated preview + missing preflight -> must block completion.
3. `voice_route_conflict_fixture`: old Qwen reference + MiniMax voice lock -> must select current MiniMax route and preserve old Qwen as reference only.
