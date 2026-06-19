# 20260620 RAG Vector Sync Report

```yaml
task_result.status（任务结果状态）: completed（已完成）
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）: mechanism_repair_and_vector_ingestion（机制修补 + 向量入库）
source_commit_sha（源语料提交）: 6a7417fb856cdd91f3777d7348e367d2ce12b3c9
embedding_provider（向量模型供应商）: Alibaba DashScope / text-embedding-v4
embedding_dimension（向量维度）: 1024
vector_store（向量库）: DashVector
dashvector_collection（集合）: video_factory_docs_test
indexed_file_count（已索引文件数）: 867
indexed_chunk_count（已索引分块数）: 5569
content_storage_policy（正文存储策略）: source_readback_only（DashVector 只存向量和定位 metadata，不存正文）
media_indexed（媒体是否入库）: false（否）
key_printed（是否打印密钥）: false（否）
key_written（是否写入密钥）: false（否）
vector_values_written（是否写入向量值）: false（否）
```

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - mechanism_or_route_fix（机制 / 路由修补）
  - code_debug（代码执行 / 调试）
  - project_file_change（项目文件修改）
  - mechanism_repair_and_vector_ingestion（机制修补 + 向量入库）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
state_action_router（项目状态动作总控器）:
  current_project_state（当前项目状态）:
    - mechanism_repair_needed（机制修补需要）
    - supply_source_arbitration_required（供料来源裁决必需）
    - mandatory_commit_push_required（必须 commit / push）
  not_promoted（未推进）:
    content_validation（内容验证）: not_promoted
    send_ready（可发送状态）: false
    production_readiness（生产可用状态）: not_claimed
```

## 2. mechanism_repair（机制修补）

- `Chroma（本地向量库）`: `disabled_not_used（停用，不使用）`；只保留历史兼容说明和 blocked fixture，不进入正式 RAG 供料。
- `RAG_sync_bus（RAG 同步总线）`: 已新增 schema / passing fixture / blocked fixture / probe，并绑定 source_inventory、chunk_manifest、index_manifest、commit_sha、file_hash、chunk_hash、line_range。
- `RAG_supply_bus（RAG 供料总线）`: 已新增 pre / mid / post / small probe 供料包 schema、fixture、probe；供料包包含 exact snippet、source_path、line_range、chunk_id 和 source readback。
- `failure_route（失败路由）`: 已新增 RAG failure route、trace event、五问执行控制卡和 trace_event / dated_log / latest 三层记录策略。

## 3. vector_ingestion（向量入库）

```yaml
source_inventory（源文件清单）: codex_log/rag_vector_sync/latest_source_inventory.json
chunk_manifest（分块清单）: codex_log/rag_vector_sync/latest_chunk_manifest.json
index_manifest（索引清单）: codex_log/rag_vector_sync/latest_index_manifest.json
secret_scan（密钥扫描）: passed（通过）
allowlist_check（允许清单检查）: passed（通过）
denylist_check（禁止清单检查）: passed（通过）
excluded_by_secret_or_privacy_scan（因密钥或隐私扫描排除）: 13
indexed_secret_hit_count（进入索引的密钥命中数）: 0
dashvector_upsert（DashVector 写入）: passed（通过）
```

本轮只索引文本信息；`.env*`、secret/token/key 命名文件、视频、音频、图片、zip、`dist/**`、`public/**`、`.git/**`、archive/delete zone、raw reference 和第三方原文全文均未进入索引。DashVector 文档字段不存正文，只存 `source_path / line_range / chunk_id / hash / commit_sha / indexed_at`，正文事实必须回到仓库原文读取。

## 4. retrieval_validation（检索验证）

```yaml
retrieval_probe（检索探测）: passed（通过）
queries_tested（已测试问题）: 6
source_readback_passed（原文回读）: true
stale_index_check（过期索引检查）: true
page_content_only（只有正文无来源）: false
report（报告）: codex_log/rag_vector_sync/latest_retrieval_probe_report.md
```

已测试固定问题：
- RAG 默认判断链是什么
- Chroma 是否仍然使用
- DashVector 在当前项目中的角色是什么
- Codex 执行前如何获得资料包
- 失败后应该回到哪一层
- 本轮向量索引同步到了哪个 commit

## 5. supply_validation（供料验证）

```yaml
supply_bus_report（供料总线报告）: codex_log/rag_vector_sync/latest_supply_bus_report.md
pre_supply_pack（执行前资料包）: passed（通过）
mid_task_supply_pack（执行中增量资料包）: passed（通过）
post_risk_review_pack（完成前风险复核包）: passed（通过）
small_probe_run（小跑探测）: passed（通过）
```

## 6. validation_result（验证结果）

```yaml
py_compile（Python 编译检查）: passed（通过）
schema_probe（结构契约探测）: passed（通过）
secret_scan（密钥扫描）: passed（通过）
retrieval_probe（检索探测）: passed（通过）
sync_guard（同步护栏）: passed（通过）
external_call_report（外部调用报告）:
  provider（供应商）: Alibaba / DashVector
  call_type（调用类型）: embedding / upsert / query
  alibaba_embedding_api_called（是否调用阿里向量 API）: true
  dashvector_upsert_called（是否写入 DashVector）: true
  dashvector_query_called（是否查询 DashVector）: true
  key_printed（是否打印密钥）: false
  key_written（是否写入文件）: false
  vector_values_written（是否写入向量值）: false
```

## 7. next_safe_step（下一步安全动作）

下一步可在 Codex 执行前调用 `scripts/rag_retrieval_probe.py` 或 `scripts/rag_supply_pack_builder.py` 生成资料包；任何召回结果仍必须通过 `source_path + line_range + chunk_id + readback_hash_match` 回到仓库原文验证，不能把向量召回直接写成正式事实。
