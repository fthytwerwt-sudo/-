# RAG 清洗层执行契约

status: `active_contract`
project_route: `video_factory`
created_at: `2026-06-21`
scope: `RAG_cleaning_layer`

## 1. 这层解决什么

RAG 清洗层负责在 Codex 执行前、执行中和完成声明前，把资料来源、旧口径、冲突、判断权和完成口径先分流。

它不是视频生产层，不推进 `content_validation`、`send_ready`、`voice_validation`、`final_voice_validated`、`visual_master_locked` 或 `production_readiness`。

它的目标是减少 Codex 对 prompt 细节的依赖：prompt 没写细节时，Codex 先按仓库契约、schema、validator、fixture、失败路由和完成真实性检查判断。

## 2. 当前固定事实优先级

资料权重从高到低：

1. `current_repo_source`: 当前仓库正式源文件，例如 `GPT数据源/`、`codex_source/`、`AGENTS.md`、相关脚本。
2. `real_run_report`: 真实执行日志、验收报告、trace、review_loop 记录。
3. `latest_summary`: `codex_log/latest.md` 等最新摘要。
4. `rag_retrieval_result`: DashVector / RAG 检索结果。必须回读仓库原文后才能喂给 Codex 执行。
5. `chat_memory`: 聊天记忆。只能作为线索，不能作为当前事实。
6. `historical_archive`: 历史归档、旧口径、旧入口。保留但降权，不能覆盖当前事实。

## 3. 七个清洗节点

### 3.1 source_authority_classifier

判断资料属于哪一级权重，并输出：

- `authority_level`
- `source_priority_rank`
- `source_path`
- `status_label`
- `can_use_as_current_fact`
- `repo_readback_verified`

硬规则：

- `chat_memory` 和 `historical_archive` 不得直接写成当前事实。
- `rag_retrieval_result` 必须有仓库原文件 readback 后才能进入执行供料。

### 3.2 stale_context_detector

判断资料是否是旧口径、历史参考、过期索引或当前事实，并输出：

- `stale_status`
- `tries_to_override_current`
- `requires_vector_sync`

硬规则：

- `legacy_demoted`、`historical_reference`、`stale_index` 不能覆盖当前仓库事实。
- `stale_index` 必须走 `RAG_sync_bus` 或提交后向量同步闸门，不得冒充最新 RAG 事实。

### 3.3 conflict_cleaner

判断是否存在来源冲突、口径冲突或状态冲突，并输出：

- `conflict_status`
- `resolution`
- `failure_route_if_unresolved`

默认裁决：

- 当前仓库源文件高于 RAG 检索摘要。
- 最新执行日志高于旧聊天记忆。
- 历史归档只能做证据，不能做默认事实。

### 3.4 decision_authority_router

判断这件事由谁拍板：

- `system_default`: 系统默认处理。
- `codex_auto_decide`: Codex 可自动判断。
- `chatgpt_review`: ChatGPT 可替用户复审收束。
- `user_must_decide`: 用户必须拍板。

必须问用户的事项只限核心判断：目标变化、验收标准变化、外部 API / 成本 / 凭据授权、删除历史文件、降级交付、发布 / 可发送 / 生产状态推进。

### 3.5 supply_pack_cleaner

清洗执行前和执行中供料包。

执行类任务必须有：

- `source_path`
- `line_range`
- `chunk_id`
- `readback`
- `authority_level`
- `stale_status`
- `conflict_status`
- `readback_required`
- `can_feed_codex`
- `can_claim_completed`

硬规则：

- 缺 source 或 readback 的执行供料必须 blocked。
- summary-only 只能用于解释性任务，不能喂给 Codex 做执行事实。
- 供料包不能声明 completed。

### 3.6 completion_claim_cleaner

清洗完成声明。

严格 `completed` 必须同时满足：

- 文件已落地。
- schema 已落地。
- validator 已落地。
- fixture 已落地。
- `codex_log/latest.md` 已更新。
- commit 已创建。
- push 已完成。
- remote HEAD 已回读校验。
- secret scan 通过。
- 向量同步边界已说明；需要同步时必须跑 post-commit vector sync gate。

硬规则：

- 技术通过不等于内容通过。
- 机制写入不等于长期稳定通过。
- 本地写入不等于远端完成。
- 技术预览、局部结果、内部诊断不能冒充 completed。

### 3.7 user_minimal_review_panel

只把真正需要用户判断的事项交给用户。

每个用户判断项必须包含：

- `decision_item`
- `why_user_must_decide`
- `recommended_default`
- `impact_if_choose_A`
- `impact_if_choose_B`
- `blocked_if_not_decided`

普通工程细节，例如文件命名、字段补齐、schema 写法、fixture 覆盖、validator 路由、日志路径、Git 收尾，默认由 Codex 自动完成。

## 4. 默认决策表

### system_default

- 不删除历史文件，只降权和隔离旧口径。
- RAG 检索不能替代仓库原文回读。
- 缺 readback 的执行供料 blocked。
- 技术验证不得写成内容验证。
- 未完成 commit / push / remote verification 不得 claim completed。

### codex_auto_decide

- 文件命名、目录落点、字段补齐、schema 单文件聚合。
- validator 参数、fixture 命名和失败样例覆盖。
- 低风险机制文档接入。
- failure route 映射。
- trace event 和执行报告落点。
- Git 白名单 stage、secret scan、commit、push、remote readback。

### chatgpt_review

- 目标收束。
- 机制解释。
- 状态边界复述。
- 方案比较。
- 执行单补全。
- 冲突语义复核，但不替用户授权成本、删除、降级、发布或完成状态推进。

### user_must_decide

- 是否改变项目目标或验收标准。
- 是否授权外部 API、成本、凭据或第三方写入。
- 是否删除、移动、覆盖历史文件。
- 是否接受降级交付。
- 是否把内容推进到发送、发布、生产或最终验证状态。

## 5. 失败路由

- `summary_only` -> `RAG_supply_bus`
- `missing_readback` -> `RAG_supply_bus`
- `stale_index` -> `RAG_sync_bus`
- `source_conflict` -> `fact_source_arbitration`
- `authority_uncertain` -> `fact_source_arbitration`
- `user_decision_required` -> `human_decision_gate`
- `completion_claim_risk` -> `completion_truth_check`
- `git_sync_incomplete` -> `git_sync_gate`

## 6. 完成标准

清洗层补缺可以写成完成，只能在以下条件都满足后：

- 本契约、schema、validator、fixture 已落地。
- 供料包 builder / validator 已接入清洗字段。
- failure route 已识别清洗层失败。
- 入口 readme、执行规则、工作流入口、状态动作总控器和工程线闸门已接入。
- validator、fixture、供料包验证、失败路由验证通过。
- 执行报告和 trace 已落地。
- `codex_log/latest.md` 已更新。
- 白名单 commit、push、remote HEAD verification 完成。
- 提交后向量同步闸门已执行或明确 blocked。

## 7. 禁止事项

- 不删除历史文件。
- 不调用媒体生产、TTS、视频、图片、音频生成。
- 不推进内容验证、可发送、声音验证、视觉母版锁定或生产可用状态。
- 不把方案、机制写入或本地验证冒充最终 completed。
- 不把 DashVector 检索结果当成不需 readback 的当前事实。
