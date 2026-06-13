# DeepSeek Positioning（DeepSeek 定位）

> document_status: draft_architecture_proposal（架构草案 / 待确认提案）
> authority_level: proposal_only（仅供后续机制修补参考，不是当前正式执行规则）
> active_runtime_rule: false（当前不作为 Codex 默认执行规则）

## 1. status

- `document_status`: `draft_architecture_proposal`
- `created_at`: `2026-06-13`
- `project_route`: `video_factory`

## 2. updated position

`已确认` DeepSeek 不应该再被当成项目资料库、向量库、文件读取器或长期记忆层。

DeepSeek 的正确位置是：

1. `reasoning_model（推理模型）`
2. `generation_model（生成/改写模型）`
3. `summary_model（总结模型）`
4. `risk_review_model（风险复核模型）`
5. `conflict_second_opinion（冲突二次意见）`
6. `external_deep_supply（外部深度供料）`

## 3. trigger policy

DeepSeek 只在以下情况触发：

- RAG 召回为空、低置信或互相冲突。
- Router 标记 `conflict_pending`。
- 任务需要外部能力边界、官方文档或工具路线判断。
- Codex 已回读原文件后仍存在复杂机制冲突。
- 执行后需要风险复核。
- 用户明确要求 DeepSeek 参与。

DeepSeek 不应触发：

- 普通项目事实检索。
- 读取 `AGENTS.md / GPT数据源 / codex_source / codex_log/latest.md` 这类基础仓库文件。
- 替代 RAG 召回。
- 替代 Codex 原文件复核。
- 替代用户/GPT 的最终验收。

## 4. output contract

DeepSeek 输出必须显式标 provenance：

| provenance | meaning | allowed use |
|---|---|---|
| `deepseek_reasoning` | 基于已给上下文的推理 | 可作为参考 |
| `risk_review` | 风险复核 | 可辅助 Codex 检查 |
| `external_deep_supply` | 外部资料/能力边界供料 | 需要来源复核 |
| `conflict_second_opinion` | 冲突二次意见 | 交 Router / GPT 裁决 |
| `fallback_local_only` | 没有真实 DeepSeek 调用 | 不得写成 DeepSeek 结论 |
| `not_deepseek_conclusion` | 明确非 DeepSeek 结论 | 不得证明 DeepSeek 参与 |

## 5. migration note

`部分成立` 审计前旧机制入口存在 `mandatory_deepseek_supply_loop`、`deep_file_prefetch` 和 `每轮默认深度文件供料` 表述；本轮已把当前正式入口降级为 `RAG-first supply arbitration（RAG 优先供料仲裁）`。历史日志、旧 fixtures 和旧上传包如保留旧表述，只按历史证据理解，不作为当前默认执行口径。
