# RAG Engineering Line Acceptance Report

```yaml
status（状态）: passed（通过）
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）: engineering_line_landing（工程线落地）
date（日期）: 2026-06-20
not_reingested（是否重新入库）: true（本轮不重新做 DashVector 入库）
content_validation（内容验证）: not_promoted（未推进）
send_ready（可发送状态）: false
production_readiness（生产可用状态）: not_claimed（未声称）
```

## Layers

| layer | status | evidence |
| --- | --- | --- |
| contract_layer | passed | 上一轮 RAG sync / supply / failure / trace schema 均已回读 |
| builder_layer | passed | `rag_supply_pack_builder.py`、`rag_mid_task_supply_builder.py`、`rag_failure_route_resolver.py`、`rag_trace_event_writer.py` 可生成样例 |
| validator_layer | passed | `rag_supply_pack_validator.py` 放行 passing pack，阻断 summary-only pack；`rag_index_manifest_validator.py` 校验 manifest metadata |
| router_hook_layer | passed | `codex_source/00`、`19`、`22` 已接入 RAG engineering line 状态 |
| acceptance_test_layer | passed | 全部 sample commands 已运行 |
| failure_route_layer | passed | `readback_missing` 样例路由到 `RAG_supply_bus` |
| trace_log_layer | passed | `trace_events.jsonl` 已写入 acceptance trace event |

## Acceptance Commands

```text
python3 scripts/rag_supply_pack_builder.py --task-request codex_log/rag_engineering_line/fixtures/task_request.sample.json --out codex_log/rag_engineering_line/pre_supply_pack.sample.json
-> status=passed

python3 scripts/rag_supply_pack_validator.py --pack codex_log/rag_engineering_line/pre_supply_pack.sample.json
-> status=passed

python3 scripts/rag_mid_task_supply_builder.py --child-task-state codex_log/rag_engineering_line/fixtures/child_task_state.sample.json --out codex_log/rag_engineering_line/mid_task_supply_pack.sample.json
-> status=passed

python3 scripts/rag_failure_route_resolver.py --failure-event codex_log/rag_engineering_line/fixtures/failure_event.sample.json --out codex_log/rag_engineering_line/failure_route.sample.json
-> route_target=RAG_supply_bus, status=passed

python3 scripts/rag_trace_event_writer.py --event codex_log/rag_engineering_line/fixtures/trace_event.sample.json --out codex_log/rag_engineering_line/trace_events.jsonl
-> status=passed
```

## Blocked Case

```text
python3 scripts/rag_supply_pack_validator.py --pack codex_log/rag_engineering_line/fixtures/blocked_pre_supply_pack.sample.json
-> status=blocked
-> exit_status=2
-> blocked_reasons:
   source_path_missing
   line_range_missing
   chunk_id_missing
   readback_missing
   only_summary_without_snippet
   conflict_points_missing_for_high_risk_task
```

## Additional Validation

```text
python3 -m py_compile scripts/rag_build_source_inventory.py scripts/rag_chunk_project_sources.py scripts/rag_dashvector_sync.py scripts/rag_sync_guard.py scripts/rag_retrieval_probe.py scripts/rag_supply_pack_builder.py scripts/rag_index_manifest_validator.py scripts/rag_supply_pack_validator.py scripts/rag_mid_task_supply_builder.py scripts/rag_failure_route_resolver.py scripts/rag_trace_event_writer.py
-> passed

python3 codex_source/schema_contracts/probes/rag_sync_bus_probe.py
-> passed

python3 codex_source/schema_contracts/probes/rag_supply_bus_probe.py
-> passed

python3 codex_source/schema_contracts/probes/rag_failure_trace_probe.py
-> passed

python3 scripts/rag_index_manifest_validator.py
-> passed, indexed_chunk_count=5569, chunk_manifest_count=5569
```

## Sync Guard Note

`python3 scripts/rag_index_manifest_validator.py --check-current-worktree` correctly returns `blocked` with `stale_index_detected` after this engineering-line patch, because this task modifies indexed text files but intentionally does not re-run DashVector ingestion.

This is expected behavior for the RAG_sync_bus: updated engineering-line files must not be treated as formally indexed until a later vector sync task runs.
