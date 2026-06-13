# Vector Retrieval Plan（向量检索计划）

> document_status: draft_architecture_proposal（架构草案 / 待确认提案）
> authority_level: proposal_only（仅供后续机制修补参考，不是当前正式执行规则）
> active_runtime_rule: false（当前不作为 Codex 默认执行规则）

## 1. status

- `document_status`: `draft_architecture_proposal`
- `created_at`: `2026-06-13`
- `project_route`: `video_factory`

## 2. current confirmed assets

- `已确认` `scripts/probe_dashscope_embedding_dimension.py` 可探测 DashScope embedding dimension，且不打印密钥或向量。
- `已确认` `scripts/vector_sync/向量同步空跑_vector_sync_dry_run.py` 支持向量同步 dry-run。
- `已确认` `scripts/vector_sync/最小RAG链路验证_minimal_rag_chain_validation.py` 支持最小 embedding + DashVector + retrieval readback 验证。
- `已确认` 20260613 报告记录 `text-embedding-v4`、dimension `1024`、DashVector collection `video_factory_docs_test`、最小 261 chunks 写入和 5 个问题 readback。
- `部分成立` 这些证明最小 RAG 链路可用；不证明完整 RAG runtime 已成为默认执行链。

## 3. target retrieval requirements

每个可用于执行的召回结果必须包含：

- `chunk_id`
- `source_path`
- `heading_path / section_title`
- `content_hash`
- `commit_sha / branch`
- `authority_level`
- `status_label`
- `retrieval_score`
- `readback_status`
- `do_not_use_for_completion_claim`

## 4. quality checks

最小检索质量检查：

1. 召回结果必须能回读原文件。
2. 召回 chunk 必须带 `content_hash`。
3. 当前事实类查询必须优先命中 canonical/current sources。
4. 旧口径命中时必须有 `legacy_demoted / deprecated / reference_only / conflict_pending`。
5. 检索结果不足时不得让 LLM 猜。
6. 检索和仓库原文件冲突时，仓库原文件优先，Router 仲裁。

## 5. next implementation stages

| stage | goal | status |
|---|---|---|
| P0 | 保留当前最小 RAG 链路报告和 readback 证据 | `已确认` |
| P1 | 把 RAG-first 供料仲裁接入正式入口 | `部分成立` |
| P2 | 增加 chunk metadata validator 和 retrieval quality fixtures | `待验证` |
| P3 | 建立 main collection 正式同步前的 dry-run + human approval | `待验证` |
| P4 | 让 Codex 每轮先读 RAG retrieval manifest，再回读原文件 | `待验证` |

## 6. do not do yet

- 不全仓入库。
- 不把 DeepSeek supply pack 当事实源入库。
- 不把 vector result 当 completion proof。
- 不在没有 commit/push/remote readback 时同步 main collection。
- 不读取 `.env*`、local auth、raw media、private screenshots 或 secret values。
