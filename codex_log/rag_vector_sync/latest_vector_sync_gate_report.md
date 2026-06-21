# Post-Commit Vector Sync Gate Report

- status: `blocked_retrieval_probe_failed`
- task_result.status: `vector_sync_blocked_with_actionable_reason`
- mode: `sync`
- source_commit_sha: `b14d9a6eab7d3de059bbf2072beec7ccf1252438`
- previous_index_commit_sha: `4874d430bac38ae4b42f3d5ba17d6d7d358319f1`
- sync_required: `true`
- changed_indexable_file_count: `None`
- delta_chunks_to_embed: `257`
- active_chunk_count: `5785`
- batch_sync_enabled: `true`
- batch_size: `8`
- batch_count: `48`
- completed_batch_count: `48`
- failed_batch_count: `0`
- pending_batch_count: `0`
- completed_chunk_count: `257`
- indexed_file_count: `911`
- indexed_chunk_count: `5785`
- final_index_manifest_written: `true`
- index_manifest_validator_passed: `true`
- current_worktree_stale_index_check_passed_before_evidence_write: `true`
- current_worktree_stale_index_check_after_evidence_write: `blocked_stale_index_detected_on_codex_log_latest_md`
- retrieval_probe_passed: `false`
- source_readback_passed: `false`
- retrieval_stale_index_check_passed: `false`
- active_filter_dry_run_passed: `true`
- current_RAG_index_latest_claim: `false`
- secret_scan_this_round: `passed`
- alibaba_embedding_api_called: `true`
- dashvector_upsert_called: `true`
- dashvector_query_called: `true`
- key_printed: `false`
- key_written: `false`
- vector_values_written: `false`
- blocked_report: `codex_log/rag_vector_sync/vector_sync_blocked_actionable_20260622_022130.json`

## Blocked Reason

- `retrieval_probe_failed_stale_or_inactive_dashvector_doc_returned_in_top_k`
- real retrieval probe query `Chroma 是否仍然使用` returned a stale/inactive top-k chunk before the active manifest readback passed.

## Failed Retrieval Evidence

- query: `Chroma 是否仍然使用`
  - rank `1` chunk `vf_497748f222067851ac7b6d5defc381703e698618` source `codex_source/schema_contracts/00_schema_contracts_index.md:41-54` reason `source_path_line_range_or_chunk_id_missing`

## Next Safe Step

- `delete_or_tombstone_stale_dashvector_docs_or_fix_retrieval_probe_post_filter_before_reclaiming_RAG_latest`
