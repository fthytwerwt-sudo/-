# RAG Decision State Machine Run

- status: `passed`
- case_id: `current_blocked_sync_decision_case`
- selected_action: `fix_incremental_sync_plus_authority_overlay`
- dry_run: `true`
- langgraph_implemented: `false`
- alibaba_embedding_api_called: `false`
- dashvector_upsert_called: `false`

## Nodes

- `task_classifier`: `passed`
- `rag_vector_maintenance_router`: `passed`
- `stale_index_checker`: `passed`
- `vector_retriever_or_repo_readback`: `passed`
- `source_readback_checker`: `passed`
- `authority_overlay_filter`: `passed`
- `conflict_group_resolver`: `passed`
- `hard_gate_checker`: `passed`
- `weighted_decision_engine`: `passed`
- `decision_audit_reporter`: `passed`
- `codex_supply_pack_emitter`: `passed`
- `failure_router`: `passed`
