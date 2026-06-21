# Post-Commit Vector Sync Gate Report

- status: `blocked`
- task_result_status: `vector_sync_blocked_with_clear_reason`
- vector_sync_status: `vector_sync_blocked_delta_embedding_upsert_timeout`
- mode: `finish`
- source_commit_sha: `4874d430bac38ae4b42f3d5ba17d6d7d358319f1`
- previous_index_commit_sha: `44b25ce9c0abf800fb7397746520b62e1dee7708`
- sync_required: `true`
- changed_indexable_file_count: `53`
- active_chunk_count: `5764`
- delta_chunks_to_embed: `652`
- final_index_manifest_written: `false`
- existing_index_manifest_source_commit_sha: `44b25ce9c0abf800fb7397746520b62e1dee7708`
- existing_index_manifest_indexed_chunk_count: `5597`
- retrieval_probe_passed: `false`
- source_readback_passed: `false`
- stale_index_check_passed: `false`
- alibaba_embedding_api_called: `true`
- dashvector_upsert_called: `possibly_started_not_provable_without_batch_checkpoint`
- dashvector_query_called: `false`
- key_printed: `false`
- key_written: `false`
- vector_values_written: `false`

## Blocked Reasons

- `delta_embedding_upsert_no_final_manifest`
- `checkpoint_resume_not_effective`
- `stale_index_detected`
- `index_chunk_count_mismatch`

## Sync Progress

- batch_size: `8`
- total_batches: `unknown_not_emitted; estimated_about_82_for_652_chunks`
- completed_batches: `unknown_not_observable`
- failed_batch: `unknown_not_observable`
- checkpoint_path: `codex_log/rag_vector_sync/latest_delta_sync_checkpoint.json`
- checkpoint_resume_cursor: `0`
- elapsed_time: `about_5m23s_before_interrupt`

## Next Safe Step

- `make per-batch checkpoint/resume and stage timeout effective before next real delta sync retry`
