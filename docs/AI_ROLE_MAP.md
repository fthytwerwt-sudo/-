# AI Role Map（AI 职责分工图）

> document_status: draft_architecture_proposal（架构草案 / 待确认提案）
> authority_level: proposal_only（仅供后续机制修补参考，不是当前正式执行规则）
> active_runtime_rule: false（当前不作为 Codex 默认执行规则）

## 1. status

- `document_status`: `draft_architecture_proposal`
- `created_at`: `2026-06-13`
- `project_route`: `video_factory`
- `audit_source`: `reports/ai_architecture_role_shift_audit.md`

本文件用于校准《视频工厂》里用户、GPT、Codex、DeepSeek、embedding、vector database、RAG 和主 LLM 的职责边界。

## 2. role map

| role | correct responsibility | must not do |
|---|---|---|
| 用户 | 方向、业务判断、最终验收、是否接受降级方案 | 不负责排查 Codex / provider / RAG 内部实现原因 |
| GPT / ChatGPT | 目标拆解、阶段规划、Codex 下发单、冲突裁决、结果复盘 | 不凭聊天记忆替代仓库事实或 RAG 证据 |
| Codex | 读仓库、改代码/文档、跑测试、写报告、更新状态、Git 收尾 | 不擅自改业务目标、内容验证、发送状态或最终验收结论 |
| DeepSeek | 推理、总结、改写、风险复核、冲突二次意见、外部深度供料 | 不作为资料库、向量库、文件读取器、长期记忆层或完成证明 |
| embedding 模型 | 把允许入库的资料切块后转成向量 | 不做业务判断，不决定事实优先级 |
| vector database | 存储 chunk、metadata、source、commit、content_hash、版本与召回结果 | 不反向覆盖仓库事实，不保存密钥、媒体或未授权资料 |
| RAG 检索层 | 根据任务召回相关资料、证据路径、chunk id、source path 和 readback 线索 | 不拍板、不生成完成结论、不替代 Codex 原文件复核 |
| Qwen / 其他主 LLM | 基于召回内容生成、分析、改写或执行文本任务 | 不绕过 RAG 直接吞全量项目资料 |
| 人工兜底 | 检索不准、模型冲突、验收失败、授权/API/审美判断时介入 | 不替 AI 系统承担内部链路排障 |

## 3. source priority

`已确认` 仓库文件仍是 `source_of_truth（主事实源）`。

```text
GitHub / local repo
-> RAG retrieval evidence
-> LLM reasoning output
-> DeepSeek risk/reasoning second opinion
-> human / GPT arbitration
```

任何 RAG、DeepSeek 或主 LLM 输出与仓库原文件冲突时，默认先回读仓库原文件，再由 Router / GPT / 用户裁决。
