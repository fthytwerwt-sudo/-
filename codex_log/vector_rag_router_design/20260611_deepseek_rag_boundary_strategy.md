# 20260611 DeepSeek（深度供料） / RAG（检索增强）边界策略

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `rag_runtime_implemented（RAG（检索增强）运行时是否实现）`: `false`
- `external_api_called（是否调用外部 API）`: `false`
- `secrets_read_or_printed（是否读取或打印密钥）`: `false`

本文件不废弃 DeepSeek（深度供料），也不把 RAG（检索增强）升级为事实源。它只定义两条线如何共存。

## 2. core_boundary（核心边界）

| layer（层） | role（职责） | must_not_do（禁止事项） |
|---|---|---|
| RAG（检索增强） | 从 Vector DB（向量数据库）和白名单文件中召回项目内上下文 | 不拍板、不创建规则、不替代 Router（路由器）、不作为完成证明 |
| DeepSeek（深度供料） | `external_deep_supply（外部深度供料）`、`risk_review（风险复审）`、`external_research（外部调研）` | 不写文件、不拍板项目事实、不替代仓库读取、不直接进入向量库 |
| Router（路由器） | 判断是否需要 RAG（检索增强）和是否触发 DeepSeek（深度供料） | 不把召回文本直接当执行结论 |
| Codex（执行器） | 读取原文件、整合上下文、执行修改、验证、commit / push | 不把 RAG（检索增强）或 DeepSeek（深度供料）结论升级成正式事实 |
| ChatGPT（总控判断） | 用户需求判断、冲突裁决、是否进入正式机制修补 | 不把未落库的聊天判断写成仓库事实 |

## 3. DeepSeek_trigger_policy（DeepSeek 触发策略）

DeepSeek（深度供料）只在以下情况触发：

1. RAG（检索增强）检索不到关键上下文。
2. RAG（检索增强）召回结果互相冲突。
3. Router（路由器）输出 `conflict_pending（冲突待裁决）`。
4. 任务涉及跨很多文件的深度审计。
5. 任务涉及外部事实、官方文档、模型能力边界或工具路线。
6. Codex（执行器）中途发现依赖文件太深，需要 `deep_file_supply（深文件供料）`。
7. Codex（执行器）修改后需要 `post_risk_review（后置风险复审）`。
8. 用户明确要求 DeepSeek（深度供料）深度参与。

DeepSeek（深度供料）不应该触发：

1. 普通当前事实检索。
2. 读取 `main（主分支）`、`latest（最新日志）`、当前正式事实等基础文件。
3. RAG（检索增强）已能准确召回且无冲突的规则。
4. 简单文档修改。
5. 单文件机制补丁。
6. 视频导出、剪辑、TTS 生成、媒体探测。
7. 需要密钥或 API 的任务，除非用户明确授权。

## 4. provenance_policy（来源标记策略）

DeepSeek（深度供料）输出必须标记为以下之一：

| provenance（来源） | meaning（含义） | may_enter_vector_db（是否可入向量库） |
|---|---|---|
| `supply_pack（供料包）` | DeepSeek 基于任务卡输出的上下文供料 | 只能摘要入库，且 `reference_only（仅参考）` |
| `risk_review（风险复审）` | 执行前 / 后风险检查 | 可摘要入库，必须携带 `not_completion_proof（不是完成证明）` |
| `reference_only（仅参考）` | 外部供料或冲突辅助 | 可入库但降权，不参与事实拍板 |
| `fallback_local_only（本地兜底）` | 没有真实 DeepSeek 调用 | 不得写成 DeepSeek 结论；默认不入库，最多入库为失败案例 |
| `not_deepseek_conclusion（不是 DeepSeek 结论）` | 明确非真实 DeepSeek 结果 | 不得用于证明 DeepSeek 参与 |

## 5. conflict_policy（冲突处理）

| conflict（冲突） | resolution（解决方式） |
|---|---|
| DeepSeek（深度供料）结果和 GitHub 当前文件冲突 | GitHub 当前文件优先；DeepSeek 结果标记 `reference_only（仅参考）` 或 `conflict_pending（冲突待裁决）` |
| DeepSeek（深度供料）结果和 RAG（检索增强）召回冲突 | Router（路由器）必须输出 `conflict_arbitration（冲突仲裁）`，Codex 不得自行拍板 |
| RAG（检索增强）召回旧规则覆盖当前事实 | 使用 metadata（元数据）中的 `authority_level（权威等级）`、`status_label（状态标签）`、`superseded_by（被替代者）` 降权 |
| DeepSeek fallback_local_only（本地兜底）被误当真实参与 | 必须写 `not_deepseek_conclusion = true（不是 DeepSeek 结论）` |
| DeepSeek（深度供料）发现仓库规则缺口 | 只能生成 supply / risk report（供料 / 风险报告），由 ChatGPT / 用户决定是否进入机制修补 |

## 6. relationship_after_rag（RAG 进入后的 DeepSeek 定位）

RAG（检索增强）进入后，DeepSeek（深度供料）从“每轮默认项目内检索辅助”收缩为：

1. `external_deep_supply（外部深度供料）`
2. `deep_file_supply（深文件供料）`
3. `risk_review（风险复审）`
4. `external_research（外部调研）`
5. `conflict_second_opinion（冲突二次意见）`

保留原因：

- RAG（检索增强）擅长召回项目内已落库事实，不擅长外部能力边界和新资料审计。
- DeepSeek（深度供料）可做结构化风险复核，但不能直接替代 GitHub / Codex 验证。
- 两者冲突时，Router（路由器）做仲裁，不让两个供料系统互相抢事实源。

## 7. safety_requirements（安全要求）

1. DeepSeek runtime provider（运行时供应商）只能把 key 注入子进程 env（环境变量），不得打印、写入、提交密钥。
2. RAG（检索增强）与向量同步不得读取 `.env`、`.env.local`、本地授权文件。
3. DeepSeek（深度供料）不得读取原始媒体、私密截图、样本音频；需要媒体判断由 Codex 本地工具完成。
4. DeepSeek（深度供料）供料不等于完成验证。
5. RAG（检索增强）召回结果不等于完成证明。

## 8. formal_patch_recommendation（正式补丁建议）

后续正式机制可增加一个 `supply_source_arbitration_gate（供料来源仲裁闸门）`，但本轮不直接修改正式入口。建议字段：

```yaml
supply_source_arbitration:
  rag_retrieval_status: available | unavailable | conflict
  deepseek_triggered: true_or_false
  deepseek_trigger_reason: []
  github_fact_priority: always_primary
  conflict_arbitration: repo_wins | router_blocks | user_decision_required
  not_deepseek_conclusion: true_or_false
```
