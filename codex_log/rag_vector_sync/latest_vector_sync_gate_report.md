# Post-Commit Vector Sync Gate Report

- status: `blocked`
- mode: `sync`
- source_commit_sha: `8804852a2a10c5686079363aa2d38c6f6ee6a80b`
- previous_index_commit_sha: `44b25ce9c0abf800fb7397746520b62e1dee7708`
- sync_required: `true`
- skip_reason: ``
- changed_indexable_file_count: `23`
- deleted_indexable_file_count: `0`
- indexed_file_count: `None`
- indexed_chunk_count: `None`
- alibaba_embedding_api_called: `true`
- dashvector_upsert_called: `true`
- dashvector_query_called: `false`
- key_printed: `false`
- key_written: `false`
- vector_values_written: `false`

## Blocked Reasons

- `vector_sync_blocked_external_sync_timeout`
- `rag_dashvector_sync_interrupted_without_final_index_manifest`
- `current_RAG_index_not_claimed_latest`

## Changed Indexable Files

- `AGENTS.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/engineering_line_collaboration/20260620_工程线协作闸门_engineering_line_collaboration_gate_report.md`
- `codex_log/latest.md`
- `codex_log/rag_cleaning_layer/20260621_RAG清洗层补缺执行报告_rag_cleaning_layer_gap_fill_report.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- `codex_source/24_RAG清洗层执行契约_rag_cleaning_layer_execution_contract.md`
- `codex_source/schema_contracts/00_schema_contracts_index.md`
- `codex_source/schema_contracts/schemas/mid_task_supply_pack.schema.yaml`
- `codex_source/schema_contracts/schemas/pre_supply_pack.schema.yaml`
- `codex_source/schema_contracts/schemas/rag_cleaning_layer.schema.yaml`
- `codex_source/schema_contracts/schemas/rag_supply_pack.schema.yaml`
- `scripts/rag_cleaning_layer_validator.py`
- `scripts/rag_failure_route_resolver.py`
- `scripts/rag_mid_task_supply_builder.py`
- `scripts/rag_supply_pack_builder.py`
- `scripts/rag_supply_pack_validator.py`
