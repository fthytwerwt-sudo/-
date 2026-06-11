# 20260611 Hidden Risk Report

## 0. purpose

This report lists hidden risks before vectorizing 《视频工厂》 project knowledge or designing the RAG Router. It is advisory and does not modify execution chains.

## 1. risk_summary

| metric | count |
|---|---:|
| hidden_risks_identified | 14 |
| high_severity | 7 |
| medium_severity | 7 |
| requires_minimal_validation | 8 |

## 2. risk_table

| risk_id | severity | risk | why_hidden | mitigation |
|---|---|---|---|---|
| R01 | high | Vector search retrieves stale but semantically similar rules | old rules use similar terms as current rules | require authority metadata and conflict tags |
| R02 | high | Router treats current prompt as full source | prompt often contains only a delta | `process_boot_skill` must always rebuild context |
| R03 | high | New material causes context reset | "new material" sounds like a new task | default `additive_merge`; require old/new/current review retrieval |
| R04 | high | Completion validation remains video-specific | preflight suite is strong for publish candidates, less generalized | add generic completion validation layer |
| R05 | high | Skill Registry becomes a dead fixed workflow | video projects are dynamic | skills should be callable actions, not a hard-coded flow |
| R06 | high | Secret or signed URL enters vector DB | logs mention API route and auth presence | blacklist secret-like chunks and signed URLs |
| R07 | high | Media/privacy data enters text index | screenshots and media may contain platform/private data | index manifests and extracted records, not raw media |
| R08 | medium | Current facts and latest log disagree | latest log may contain newer mechanism than formal facts | retrieval arbitration must prioritize source/date |
| R09 | medium | DeepSeek supply packs look authoritative | supply packs may be fallback or readonly | tag `not_deepseek_conclusion` unless real call evidence exists |
| R10 | medium | HyperFrames capability overgeneralizes | minimal runtime pass can be mistaken for full chain stability | require task-specific runtime integration proof |
| R11 | medium | Voice route lineage confuses current provider | old Qwen facts are valid history but not current default | store as `reference_only` with current MiniMax lock |
| R12 | medium | Data goal anchor readiness is overpromoted | partial record can be semantically close to ready | block unless current anchor explicitly ready |
| R13 | medium | `dist/latest_review_pack` media overwhelms index | mixed media and metadata in one directory | whitelist summary/manifest/json only |
| R14 | medium | Router cannot explain why it selected skills | retrieval may be correct but opaque | require `router_decision_trace` with evidence paths |

## 3. hidden_failure_case: new_material_only_editing

Failure pattern:

1. User adds several new material files.
2. Codex reads only the new files.
3. Codex ignores old material inventory, old candidate, locked copy, latest review blockers, and current data goal.
4. Codex edits/generates a result that diverges from the real task state.

Required future prevention:

```yaml
new_material_prevention:
  always_retrieve:
    - latest_log
    - current_candidate
    - locked_copy
    - material_parse_pack
    - old_material_inventory
    - new_material_inventory
    - latest_review_issues
    - current_data_goal_anchor
  classify:
    - additive_merge
    - replacement_merge
    - exclusive_new_only
    - unclear_blocked
  default: additive_merge
  blocked_if:
    - old_candidate_missing
    - locked_copy_missing_for_video_execution
    - replacement_scope_unclear
    - user_intent_only_new_unclear
```

## 4. risk_to_validation_mapping

| risk | minimal_validation |
|---|---|
| stale retrieval | conflict fixture with `gray_test` vs `formal_operation_active` |
| prompt overreliance | prompt-delta fixture requiring process boot retrieval |
| material reset | additive material fixture |
| false completion | preview-only fixture requiring completion truth block |
| skill overuse | fixture where same task chooses different skill graph based on delta |
| secret leakage | staged-diff and chunk-level secret scan |
| media ingestion | file extension and allowlist test |
| voice conflict | Qwen reference vs MiniMax lock fixture |

## 5. recommended_guardrails_before_vectorization

1. Build ingestion metadata before embeddings.
2. Run blacklist filters before chunking.
3. Chunk by mechanism heading, not by whole file.
4. Add conflict tags at ingestion time.
5. Make Router output `retrieved_evidence_paths`.
6. Keep `Task Delta` separate from `Config`.
7. Force material delta classification before any material-consuming skill.
8. Force completion validation plan before execution.
9. Store reference-only chunks with lower retrieval priority.
10. Run three router fixtures before any real task uses RAG.

## 6. status_boundary

- This report does not mean RAG is implemented.
- This report does not mean vector ingestion is safe yet.
- This report does not mean Skill Registry exists.
- This report does not mean old rules were cleaned or deleted.
- This report does not call any Alibaba, DashScope, DashVector, OpenSearch, Milvus, or other external API.
- Future implementation must be a separate authorized mechanism patch.
