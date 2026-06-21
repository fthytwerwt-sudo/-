# Post-Commit Vector Sync Gate Report

- status: `blocked`
- task_result_status: `vector_sync_blocked_with_clear_reason`
- vector_sync_status: `vector_sync_blocked_external_sync_timeout`
- mode: `sync`
- source_commit_sha: `a5b8e6687813210cc0caccebcf475055b7df7dab`
- previous_index_commit_sha: `44b25ce9c0abf800fb7397746520b62e1dee7708`
- sync_required: `true`
- changed_indexable_file_count: `23`
- failed_stage: `embedding_upsert_stage_rag_dashvector_sync`
- timeout_window_minutes: `30`
- final_index_manifest_written: `false`
- retrieval_probe_passed: `false`
- source_readback_passed: `false`
- stale_index_check_passed: `false`
- indexed_file_count: `None`
- indexed_chunk_count: `None`
- alibaba_embedding_api_called: `true`
- dashvector_upsert_called: `true`
- dashvector_query_called: `false`
- key_printed: `false`
- key_written: `false`
- vector_values_written: `false`
- current_RAG_index_latest_claim: `false`

## Validator Results

- `python3 scripts/rag_index_manifest_validator.py`: `blocked`
  - blocked_reasons: `index_chunk_count_mismatch`
  - chunk_manifest_count: `5657`
  - indexed_chunk_count: `5597`
  - index_commit_sha: `44b25ce9c0abf800fb7397746520b62e1dee7708`
- `python3 scripts/rag_index_manifest_validator.py --check-current-worktree`: `blocked`
  - blocked_reasons: `stale_index_detected`, `index_chunk_count_mismatch`
  - stale_file_count: `17`

## Blocked Reasons

- `vector_sync_blocked_external_sync_timeout`
- `failed_stage:embedding_upsert_stage_rag_dashvector_sync`
- `final_index_manifest_not_written_for_source_commit`
- `retrieval_probe_not_run_for_source_commit`
- `current_RAG_index_not_claimed_latest`

## Next Retry Recommendation

- `split_sync_by_smaller_source_scope_or_changed_files_instead_of_full_corpus`
- `add per_batch_progress_and_timeout_to_rag_dashvector_sync_before_next_long_retry`
- `verify DashVector collection latency/status before re-running full upsert`
- `do_not_claim_RAG_latest_until_index_manifest_and_retrieval_probe_pass`
