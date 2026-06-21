# 20260621 RAG 向量同步收尾重跑报告

## 1. 本轮结论

```yaml
task_result.status（任务结果状态）: vector_sync_blocked_with_clear_reason（向量同步阻断但原因清楚）
vector_sync_status（向量同步状态）: vector_sync_blocked_external_sync_timeout（外部同步超时阻断）
current_RAG_index_latest_claim（是否声明当前 RAG 最新）: false（不声明）
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - vector_sync_finish_retry（向量同步收尾重跑）
  - RAG_sync_bus_finish（RAG 同步总线收尾）
  - post_commit_vector_sync_gate_recovery（提交后向量同步闸门恢复）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
attached_route（附加路由）: rag_engineering_line_required（RAG 工程线必需）
one_sentence_summary（一句话总结）: finish 重跑进入 rag_dashvector_sync.py 的 embedding / upsert 外部阶段，但 30 分钟窗口内没有写出 source commit a5b8e668... 对应的 final index manifest，因此本轮只能写阻断，不能声明 RAG 最新。
```

## 2. 本轮没有做什么

- 未改清洗层主体机制。
- 未修改 `rag_cleaning_layer.schema.yaml`、`rag_cleaning_layer_validator.py` 或 7 个清洗层 fixture。
- 未生成视频 / 音频 / 图片。
- 未调用 TTS。
- 未推进 `content_validation / send_ready / voice_validation / final_voice_validated / visual_master_locked / production_readiness`。
- 未打印 API key、未写入 API key、未写入 vector values。

## 3. 读取与事实源

```yaml
source_commit_target（本轮同步目标提交）: a5b8e6687813210cc0caccebcf475055b7df7dab
previous_index_commit_sha（上一索引提交）: 44b25ce9c0abf800fb7397746520b62e1dee7708
previous_blocked_source_commit（上一轮阻断源提交）: 8804852a2a10c5686079363aa2d38c6f6ee6a80b
vector_blocked_commit（上一轮向量阻断记录提交）: a5b8e6687813210cc0caccebcf475055b7df7dab
remote_head_before_retry（重跑前远端 HEAD）: a5b8e6687813210cc0caccebcf475055b7df7dab
source_commit_target_decision（目标提交判断）: post_commit_vector_sync_gate.py --mode check 以当前 HEAD / origin main 自动判定需要同步 a5b8e668...
fact_source_arbitration（事实源裁决）: 以仓库脚本 check 输出、latest_vector_sync_gate_report、latest_source_inventory、latest_chunk_manifest、latest_index_manifest 和 validator 输出为准；不使用聊天记忆拍板。
```

## 4. 运行命令 commands_run（运行命令）

| command | result | duration |
| --- | --- | --- |
| `python3 -m py_compile scripts/post_commit_vector_sync_gate.py scripts/rag_common.py scripts/rag_dashvector_sync.py scripts/rag_retrieval_probe.py scripts/rag_index_manifest_validator.py` | passed | < 1s |
| `python3 scripts/post_commit_vector_sync_gate.py --mode check` | passed, `sync_required` | < 1s |
| `python3 scripts/post_commit_vector_sync_gate.py --mode finish` | blocked / interrupted after no final index manifest | 30 minutes |
| `python3 scripts/rag_index_manifest_validator.py` | blocked, `index_chunk_count_mismatch` | < 1s |
| `python3 scripts/rag_index_manifest_validator.py --check-current-worktree` | blocked, `stale_index_detected` + `index_chunk_count_mismatch` | < 1s |

## 5. 向量同步结果 vector_sync_result（向量同步结果）

```yaml
mode（模式）: finish
source_commit_sha（源语料提交）: a5b8e6687813210cc0caccebcf475055b7df7dab
previous_index_commit_sha（上一索引提交）: 44b25ce9c0abf800fb7397746520b62e1dee7708
changed_indexable_file_count（变化的可索引文件数量）: 23
indexed_file_count（已索引文件数）: null（本轮未写出最终索引清单）
indexed_chunk_count（已索引分块数）: null（本轮未写出最终索引清单）
latest_chunk_manifest_chunk_count（最新分块清单分块数）: 5657
existing_index_manifest_indexed_file_count（现存索引清单已索引文件数）: 875
existing_index_manifest_indexed_chunk_count（现存索引清单已索引分块数）: 5597
final_index_manifest（最终索引清单）: missing_for_source_commit（没有写出 a5b8e668... 对应最终清单）
retrieval_probe（检索探测）: not_run_for_source_commit（缺最终索引清单，未对新 source commit 运行）
source_readback（原文回读）: blocked（缺最终索引清单）
stale_index_check（过期索引检查）: blocked（stale_index_detected + index_chunk_count_mismatch）
alibaba_embedding_api_called（是否调用阿里向量 API）: true
dashvector_upsert_called（是否写入 DashVector）: true
dashvector_query_called（是否查询 DashVector）: false
key_printed（是否打印密钥）: false
key_written（是否写入密钥）: false
vector_values_written（是否写入向量值）: false
```

## 6. 失败原因 blocked_reason（如有）

```yaml
blocked_reason（阻断原因）: post_commit_vector_sync_gate finish 等待 rag_dashvector_sync.py 的 embedding / upsert 阶段 30 分钟后，仍未写出 source commit a5b8e668... 对应 final index manifest。
failed_stage（失败阶段）: embedding_upsert_stage_rag_dashvector_sync
why_not_completed（为什么不能写完成）:
  - final_index_manifest_written=false
  - retrieval_probe_passed=false
  - source_readback_passed=false
  - stale_index_check_passed=false
  - latest_index_manifest 仍指向 44b25ce9...，不是 a5b8e668...
next_retry_recommendation（下次重试建议）:
  - 先把同步拆成更小 source scope 或 changed files 子集
  - 给 rag_dashvector_sync.py 增加 per-batch progress 和阶段超时
  - 重跑前检查 DashVector collection 状态 / 延迟
  - 没有 final index manifest 和 retrieval probe passed 前不得声明 RAG 最新
```

## 7. 文件变更 files_changed（修改文件）

- `codex_log/rag_vector_sync/latest_source_inventory.json`
- `codex_log/rag_vector_sync/latest_source_inventory.md`
- `codex_log/rag_vector_sync/latest_chunk_manifest.json`
- `codex_log/rag_vector_sync/latest_chunk_manifest.md`
- `codex_log/rag_vector_sync/latest_secret_scan_report.json`
- `codex_log/rag_vector_sync/latest_vector_sync_gate_report.json`
- `codex_log/rag_vector_sync/latest_vector_sync_gate_report.md`
- `codex_log/rag_cleaning_layer/vector_sync_blocked_20260621_162310.json`
- `codex_log/rag_vector_sync/20260621_vector_sync_finish_retry_report.md`
- `codex_log/rag_vector_sync/trace_event_20260621_vector_sync_finish_retry.json`
- `codex_log/latest.md`
- `codex_log/rag_engineering_line/trace_events.jsonl`

## 8. 状态边界 status_boundary（状态边界）

```yaml
content_validation（内容验证）: not_promoted（未推进）
send_ready（可发送状态）: false（未开启）
voice_validation（声音验证）: not_promoted（未推进）
final_voice_validated（最终声音验证）: false（未通过）
visual_master_locked（视觉母版锁定）: false（未锁定）
production_readiness（生产可用状态）: not_claimed（未声称）
```

## 9. 下一步 next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: before_next_full_finish_retry_add_or_use_smaller_batch_progress_timeout_then_retry_dashvector_sync（下次完整重跑前，先增加或使用更小批次 / 进度超时，再重试 DashVector 同步）
```
