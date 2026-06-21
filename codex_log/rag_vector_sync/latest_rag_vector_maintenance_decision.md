# RAG Vector Maintenance Decision

- status: `passed`
- case_id: `current_reports`
- action_id: `run_retrieval_active_filter_and_stale_cleanup_plan`
- action_label: `final_manifest_written_but_probe_failed -> run_retrieval_active_filter_and_stale_cleanup_plan`
- reason: Final manifest exists but retrieval found stale or inactive raw candidates.
- current_git_head: `bad20f1f74522a770c2f13b61a64d74c8ff95698`
- source_commit_sha: `b14d9a6eab7d3de059bbf2072beec7ccf1252438`
- current_RAG_index_latest_claim_allowed: `false`
- retrieval_probe_passed: `false`
- clean_top_k_passed: `false`
- stale_or_inactive_docs_detected: `true`
- alibaba_embedding_api_called: `false`
- dashvector_upsert_called: `false`
- dashvector_delete_called: `false`

## Next Script

`python3 scripts/rag_retrieval_probe.py --dry-run-active-filter && python3 scripts/rag_dashvector_stale_doc_cleanup.py`
