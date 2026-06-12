# 20260613 Vector Ingestion Policy Check Report

- status: `passed`
- required_metadata_fields: `project, repo, branch, file_path, section_title, chunk_index, content_hash, source_type, updated_at, batch_id`

## checks

- whitelist_present: `true`
- blacklist_present: `true`
- source_priority_present: `true`
- chunking_strategy_present: `true`
- metadata_strategy_present: `true`
- rebuild_strategy_present: `true`
- hard_blacklist_present: `true`
- runtime_required_metadata_superset_present: `true`

## boundary

- 向量库只作为 retrieval_index（检索索引）/ cache_layer（缓存层）。
- 仓库文件仍是 source_of_truth（主事实源）。
- 入库策略不允许 `.env*`、本地配置、secret、媒体、`public/` 或未跟踪无关文件进入向量库。
