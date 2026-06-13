# RAG Execution Architecture（RAG 执行架构）

## 1. status

- `document_status`: `active_architecture_guidance`
- `created_at`: `2026-06-13`
- `project_route`: `video_factory`

本文件定义新的执行链路：资料检索由 embedding + vector database + RAG 承担，LLM 基于召回内容推理，Codex 负责执行和验证。

## 2. recommended chain

```text
资料进入
-> 清洗
-> 切块
-> metadata 标注
-> embedding
-> 写入向量库
-> 任务触发
-> RAG 召回
-> LLM 判断 / 生成
-> Codex 执行
-> 测试验证
-> 报告落库
-> CURRENT_STATUS.md / codex_log/latest.md 更新
-> 用户验收
```

## 3. layer contracts

| layer | input | output | fallback / blocked |
|---|---|---|---|
| 资料进入 | `GPT数据源/`、`codex_source/`、`codex_log/`、review metadata | 候选资料清单 | 资料来源不清则 `blocked_source_unclear` |
| 清洗 | 文本资料、报告、fixture、schema | 可索引文本 | 命中 secret / media / private screenshot 则排除 |
| 切块 | 可索引文本 | chunk text + heading path | 切块缺 source_path/content_hash 则 blocked |
| metadata 标注 | chunk + git/context | `source_path / commit_sha / authority_level / status_label / content_hash` | metadata 不完整不得用于真实任务 |
| embedding | chunk text | vector | dimension 未确认或 API 失败则 blocked，不猜 dimension |
| vector database | vector + metadata | indexed chunk | collection/metric/dtype 不匹配则 blocked |
| RAG 召回 | task query + filters | chunks、scores、source paths、chunk ids | 召回为空或冲突时进入 DeepSeek/人工二次判断 |
| LLM 判断 / 生成 | 召回内容 + 原文件回读 | 草案、判断、摘要、任务建议 | 不足以回答时必须标 `待验证` |
| Codex 执行 | 仓库原文件 + RAG evidence + 任务单 | 文件改动、测试、报告、状态记录 | 关键原文件无法读取则 blocked |
| 测试验证 | 脚本、fixture、diff、报告 | pass/fail evidence | 验证失败继续修或 blocked |
| 报告落库 | 验证结果 | report/status/latest | 不得把中间态写 completed |
| 用户验收 | 可读报告/候选产物 | 最终确认或下一轮目标 | 人审未完成不得推进 final 状态 |

## 4. current implementation status

- `已确认` 已有 `scripts/vector_sync/` dry-run 工具。
- `已确认` 已有 `scripts/vector_sync/最小RAG链路验证_minimal_rag_chain_validation.py` 最小链路验证脚本。
- `已确认` `text-embedding-v4 / 1024 / DashVector video_factory_docs_test` 已在 20260613 最小链路报告中验证。
- `部分成立` 已有最小资料包入库与 5 个查询 readback；这不等于完整 RAG runtime 默认接入。
- `待验证` RAG 是否已经成为每轮默认资料检索层；当前仍需正式入口补丁和运行链路接入。

## 5. non-negotiable boundaries

- Vector DB 是 `retrieval_index / cache_layer`，不是事实源。
- RAG 返回证据，不返回完成证明。
- `MISSING_REPORT` 只能诊断或阻断，不能放行真实执行。
- DeepSeek 不作为长期记忆、资料库、向量库或默认文件读取器。
- Codex 执行前仍要回读关键原文件。
