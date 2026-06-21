# RAG / DashVector 向量同步重跑报告

## 1. 本轮结论

- task_result.status（任务结果状态）: `vector_sync_blocked_with_actionable_reason`
- vector_sync_status（向量同步状态）: `blocked_at_real_retrieval_probe_after_final_manifest`
- current_RAG_index_latest_claim（是否声明当前 RAG 最新）: `false`
- one_sentence_summary（一句话总结）: 真实差量 embedding / upsert 已完成并写出当前 HEAD 的 final index manifest，但真实 DashVector retrieval probe 仍返回旧 / 非活跃 top-k chunk，原文回读失败，因此不能声明 RAG 最新。

## 2. 本轮没有做什么

- 未改清洗层主体机制。
- 未修改清洗层 schema / validator / fixtures。
- 未生成视频 / 音频 / 图片。
- 未调用 TTS。
- 未推进 content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / production_readiness。

## 3. 读取与事实源

- files_read（已读取文件）: AGENTS.md, codex_log/latest.md, latest vector sync reports/manifests, post_commit_vector_sync_gate.py, rag_dashvector_sync.py, rag_index_manifest_validator.py, rag_retrieval_probe.py, rag_common.py, rag_delta_* validators。
- previous_blocked_status（上一轮阻断状态）: `vector_sync_blocked_delta_embedding_upsert_timeout`。
- source_commit_target（本轮同步目标提交）: `b14d9a6eab7d3de059bbf2072beec7ccf1252438`。
- fact_source_arbitration（事实源裁决）: 以脚本重建后的 source inventory / chunk manifest / delta manifest / index manifest / retrieval probe report 为准，不用聊天记忆拍板。

## 4. 运行命令 commands_run（运行命令）

- `python3 -m py_compile ...`: passed。
- `python3 scripts/post_commit_vector_sync_gate.py --mode check --batch-size 8`: sync_required，目标 `b14d9a6...`。
- `python3 scripts/rag_index_manifest_validator.py --check-current-worktree`: 同步前 blocked，确认旧索引 stale。
- delta batch / checkpoint / partial validators: passed。
- dry-run interruption / resume / timeout probes: passed。
- small real batch probe: passed，完成 batch 0 后受控终止。
- small real resume probe: passed，观察到 `skipped_completed_batch_indexes=[0]` 后受控终止。
- `python3 scripts/rag_dashvector_sync.py --batch-size 8 --resume ...`: completed first catch-up to `4874d430...`，107/107 batch 完成。
- `python3 scripts/rag_build_source_inventory.py && python3 scripts/rag_chunk_project_sources.py && python3 scripts/rag_vector_delta_planner.py`: rebuilt current HEAD manifests，delta 257 chunks。
- `python3 scripts/post_commit_vector_sync_gate.py --mode finish --real-delta-sync --batch-size 8`: passed at sync layer，48/48 batch 完成。
- `python3 scripts/rag_retrieval_probe.py`: blocked。
- `python3 scripts/rag_index_manifest_validator.py`: passed；`--check-current-worktree` 在写入本轮 latest 前 passed，写入本轮证据后因 `codex_log/latest.md` 新变更再次 stale，所以最终不声明 RAG 最新。
- `python3 scripts/rag_retrieval_probe.py --dry-run-active-filter`: passed。

## 5. 向量同步结果 vector_sync_result（向量同步结果）

- mode（模式）: `real_delta_sync_with_checkpoint_resume_then_gate_finish`
- source_commit_sha（源语料提交）: `b14d9a6eab7d3de059bbf2072beec7ccf1252438`
- previous_index_commit_sha（上一索引提交）: `4874d430bac38ae4b42f3d5ba17d6d7d358319f1`
- indexed_file_count（已索引文件数）: `911`
- indexed_chunk_count（已索引分块数）: `5785`
- final_index_manifest（最终索引清单）: `written`
- retrieval_probe（检索探测）: `blocked`
- source_readback（原文回读）: `failed_in_real_retrieval_probe`
- stale_index_check（过期索引检查）: `index_manifest_passed_before_evidence_write / current_worktree_stale_after_latest_log / retrieval_probe_failed`
- alibaba_embedding_api_called（是否调用阿里向量 API）: `true`
- dashvector_upsert_called（是否写入 DashVector）: `true`
- dashvector_query_called（是否查询 DashVector）: `true`
- key_printed（是否打印密钥）: `false`
- key_written（是否写入密钥）: `false`
- vector_values_written（是否写入向量值）: `false`

## 6. 失败原因 blocked_reason（如有）

- `retrieval_probe_failed_stale_or_inactive_dashvector_doc_returned_in_top_k`。
- 具体失败 query: `Chroma 是否仍然使用`。
- 失败 top result: `codex_source/schema_contracts/00_schema_contracts_index.md:41-54` / chunk `vf_497748f222067851ac7b6d5defc381703e698618`，不在当前 active manifest allowlist，readback hash 不匹配。
- 可执行解释: 当前 delta sync 只 upsert 新 / 变化 chunks，未删除或 tombstone 已删除 / 已替换的 DashVector 旧 docs；真实 query 仍可能先召回旧 doc，所以 retrieval probe 阻断。

## 7. 文件变更 files_changed（修改文件）

- `codex_log/rag_vector_sync/latest_*` manifests / reports。
- `codex_log/rag_vector_sync/vector_sync_blocked_actionable_20260622_022130.json`。
- `codex_log/rag_vector_sync/20260622_RAG_DashVector真实差量同步重跑报告.md`。
- `codex_log/latest.md`。
- trace event JSON / JSONL。

## 8. Git 同步状态 git_sync_status（Git 同步状态）

- current_branch（当前分支）: `main`
- files_staged（暂存文件）: pending_git_stage
- commit_sha（提交号）: pending_git_commit
- pushed（是否推送）: pending_git_push
- remote_head_verified（远端 HEAD 是否校验）: pending_remote_verify
- unrelated_dirty_files（无关脏文件）: `public/` kept_untracked
- secret_scan（密钥扫描）: `passed`，报告 `codex_log/rag_vector_sync/latest_vector_sync_secret_scan_this_round.json`
- completed_allowed（是否允许写完成）: `false`

## 9. 状态边界 status_boundary（状态边界）

- content_validation（内容验证）: `not_promoted`
- send_ready（可发送状态）: `false`
- voice_validation（声音验证）: `not_promoted`
- final_voice_validated（最终声音验证）: `false`
- visual_master_locked（视觉母版锁定）: `false`
- production_readiness（生产可用状态）: `not_claimed`

## 10. 下一步 next_safe_step（下一步安全动作）

- `delete_or_tombstone_stale_dashvector_docs_or_fix_retrieval_probe_post_filter_before_reclaiming_RAG_latest`
