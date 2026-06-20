# Schema Contracts Index

## 1. status

- `project_route = video_factory`
- `document_type = schema_contract_index`
- `status = draft`
- `runtime_enabled = false`
- `sandbox_created = false`
- `minimal_router_prototype_created = false`
- `dependency_installed = false`
- `external_code_copied = false`
- `active_write_executor = codex`

This directory defines draft schema contracts and static fixtures for the future adapter contract layer. It does not install, enable, or run `agent-service-toolkit`.

## 2AD. 20260621 RAG cleaning layer gap fill update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: rag_cleaning_layer_gap_fill（RAG 清洗层补缺）
  status（状态）: contract_schema_validator_fixture_landed（契约 / schema / validator / fixture 已落地）
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: main（主分支）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  production_readiness（生产可用状态）: not_claimed（未声称）
```

本阶段把 RAG 供料前后的清洗判断补成可执行机制：

- `source_authority_classifier（资料权重分类器）`
- `stale_context_detector（旧口径检测器）`
- `conflict_cleaner（冲突清洗器）`
- `decision_authority_router（判断权路由器）`
- `supply_pack_cleaner（供料包清洗器）`
- `completion_claim_cleaner（完成声明清洗器）`
- `user_minimal_review_panel（用户最小复审面板）`

### 2AD.1 added_schema_family（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `rag_cleaning_layer` | 规定 RAG 清洗层七个节点、资料优先级、用户判断面板、完成声明清洗和失败路由。 | `schemas/rag_cleaning_layer.schema.yaml` |

### 2AD.2 added_validator_and_fixtures（新增校验器与样例）

| validator | fixture directory | coverage |
|---|---|---|
| `scripts/rag_cleaning_layer_validator.py --fixtures` | `codex_log/rag_cleaning_layer/fixtures/` | 当前仓库回读、用户最小面板、summary-only、旧口径覆盖当前、技术预览冒充完成、stale index 冒充当前、缺 readback。 |

### 2AD.3 supply_pack_cleaning_fields（供料包清洗字段）

`scripts/rag_supply_pack_builder.py` 与 `scripts/rag_supply_pack_validator.py` 必须为执行供料包维护以下字段：

- `authority_level`
- `stale_status`
- `conflict_status`
- `readback_required`
- `can_feed_codex`
- `can_claim_completed`

### 2AD.4 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - RAG_cleaning_layer_passed 不等于 content_validation 通过
  - RAG_cleaning_layer_passed 不等于 send_ready
  - 供料包通过不等于 completed
  - DashVector 检索结果仍必须仓库原文 readback
  - 历史文件保留但降权，不删除
```

## 2AC. 20260620 RAG sync / supply bus and DashVector ingestion guard update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: rag_sync_supply_bus_and_vector_ingestion_guard（RAG 同步 / 供料总线与向量入库护栏）
  status（状态）: mechanism_landed_vector_ingestion_guarded（机制已落地，向量入库受护栏控制）
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: main（主分支）
  local_first_execution（本地优先执行）: true（是）
  github_audit_after_push（GitHub 推送后审核）: true（是）
  dashvector_only_formal_store（DashVector 是唯一正式向量库）: true（是）
  alibaba_embedding_api（阿里向量大模型 API）: formal_embedding_model（正式向量化模型）
  chroma_status（Chroma 状态）: disabled_not_used（停用，不使用）
  chroma_ingestion_run（Chroma 入库）: false（未运行）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  production_readiness（生产可用状态）: not_claimed（未声称）
```

本阶段把 RAG 从“默认判断链 / 资料地图”补齐为两条可执行总线：

- `RAG_sync_bus（RAG 同步总线）`：判断本地项目、GitHub 审核快照和 DashVector 索引是否同步；索引必须绑定 `commit_sha / file_hash / chunk_hash / line_range`；本地脏文件不得进入正式向量库。
- `RAG_supply_bus（RAG 供料总线）`：给执行前、高风险写入前、验证失败后、完成前生成资料包；资料包必须包含精确原文片段、`source_path`、`line_range`、`chunk_id` 和 readback（原文回读），不能只有文件地图或摘要。

### 2AC.1 Chroma disabled boundary（Chroma 停用边界）

```yaml
chroma_boundary（Chroma 边界）:
  status（状态）: disabled_not_used（停用，不使用）
  meaning（含义）: 只保留历史兼容说明和阻断样例，不再作为正式路线，也不再作为默认 sandbox_reference（沙盒参考）。
  hard_rules（硬规则）:
    - Chroma cannot replace DashVector（Chroma 不得替代 DashVector）
    - Chroma not used in formal RAG supply（Chroma 不进入正式 RAG 供料）
    - Chroma ingestion not run（本阶段不运行 Chroma 入库）
```

旧 `Chroma_sandbox` / `Chroma fixture` 只作为历史契约回溯或 blocked case（阻断样例）解释；凡试图把 Chroma 写成 formal vector store（正式向量库）、sandbox_reference（默认沙盒参考）或 RAG_supply_bus 的正式 provider（供应商），均按 `chroma_still_active` 阻断。

### 2AC.2 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `rag_sync_bus` | 记录 repo / branch / commit / source inventory / chunk manifest / index manifest / DashVector collection / stale files / deleted files。 | `schemas/rag_sync_bus.schema.yaml` |
| `vector_index_manifest` | 绑定 `commit_sha / file_hash / chunk_hash / line_range`，用于索引过期阻断和原文回读。 | `schemas/vector_index_manifest.schema.yaml` |
| `rag_supply_pack` | 定义四个供料节点和统一供料包字段，禁止只有 retrieval map。 | `schemas/rag_supply_pack.schema.yaml` |
| `pre_supply_pack` | 执行前资料包，必须包含精确原文片段和执行约束。 | `schemas/pre_supply_pack.schema.yaml` |
| `mid_task_supply_pack` | 执行中增量资料包，绑定已读、待改、缺上下文、失败日志和是否允许继续。 | `schemas/mid_task_supply_pack.schema.yaml` |
| `post_risk_review_pack` | 完成前风险复核包，检查漏同步、漏日志、漏验证、状态偷换和过期索引。 | `schemas/post_risk_review_pack.schema.yaml` |
| `small_probe_run` | 小跑探测结构，输出 `can_execute / missing_context / conflict_points / blocked_if`。 | `schemas/small_probe_run.schema.yaml` |
| `rag_failure_route` | 把 RAG / 向量 / 供料失败路由到具体修复层，禁止只写重试。 | `schemas/rag_failure_route.schema.yaml` |
| `rag_trace_event` | 定义 trace event（追踪事件）字段，并禁止 secret / vector 值进入日志。 | `schemas/rag_trace_event.schema.yaml` |

### 2AC.3 added_fixture_families（新增 fixture 家族）

| fixture family | passing fixture | blocked fixture |
|---|---|---|
| `rag_sync_bus` | `fixtures/passing/rag_sync_bus.passing.yaml` | `fixtures/blocked/rag_sync_bus.blocked.yaml` |
| `rag_supply_bus` | `fixtures/passing/rag_supply_bus.passing.yaml` | `fixtures/blocked/rag_supply_bus.blocked.yaml` |
| `rag_failure_trace` | `fixtures/passing/rag_failure_trace.passing.yaml` | `fixtures/blocked/rag_failure_trace.blocked.yaml` |

### 2AC.4 added_probe_families（新增探测脚本家族）

| probe | purpose |
|---|---|
| `probes/rag_sync_bus_probe.py` | 验证 RAG_sync_bus、vector_index_manifest、DashVector-only、Chroma disabled、dirty file block 和 stale index block。 |
| `probes/rag_supply_bus_probe.py` | 验证 pre / mid / post / small probe 供料包必须包含精确原文片段、来源路径、行号和 chunk_id。 |
| `probes/rag_failure_trace_probe.py` | 验证五问执行控制卡、失败路由目标和三层日志策略。 |

### 2AC.5 runtime_scripts（运行脚本）

| script | purpose |
|---|---|
| `scripts/rag_build_source_inventory.py` | 构建 source_inventory（源文件清单），执行 allowlist / denylist / secret scan，不打印密钥。 |
| `scripts/rag_chunk_project_sources.py` | 生成 chunk_manifest（分块清单），每个 chunk 绑定 `source_path / line_range / chunk_id / chunk_hash / file_hash / commit_sha / indexed_at`。 |
| `scripts/rag_dashvector_sync.py` | 调用 Alibaba embedding API 生成向量并 upsert 到 DashVector；向量值不得写入 Git。 |
| `scripts/rag_sync_guard.py` | 比较 index_manifest 与当前文件 hash，发现 stale / deleted / dirty indexed source 必须阻断。 |
| `scripts/rag_retrieval_probe.py` | 对固定问题跑 DashVector 检索，验证 metadata、source readback 和 stale index check。 |
| `scripts/rag_supply_pack_builder.py` | 基于检索结果和原文回读生成 pre / mid / post / small probe 供料包。 |

### 2AC.6 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - schema / fixture / probe 通过不等于向量入库完成
  - source_inventory / chunk_manifest 通过不等于 DashVector 已写入
  - DashVector 检索结果不等于项目正式事实；必须 source_readback（原文回读）
  - RAG_supply_bus 供料完成不等于允许推进 content_validation / send_ready / production_readiness
  - trace_event / dated_log / latest 不得写入 secret、API key、token 或 vector 值
  - `codex_log/rag_vector_sync/` 是本轮审计产物目录，不作为正式索引源，避免 manifest/log 自引用造成 commit 绑定不稳定
```

## 2AB. 20260618 real task dry run preflight update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: new_framework_real_task_dry_run（新框架真实任务干跑验证）
  status（状态）: real_task_dry_run_preflight_landed（真实任务干跑执行前检查已落地）
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: main（主分支）
  runtime_enabled（运行时启用）: false（未启用）
  service_started（服务启动）: false（未启动）
  external_api_called（外部 API 调用）: false（未调用）
  tts_called（TTS 调用）: false（未调用）
  dashvector_real_call（DashVector 真实调用）: false（未调用）
  chroma_ingestion_run（Chroma 入库）: false（未运行）
  media_generated（媒体生成）: false（未生成）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  production_readiness（生产可用状态）: not_claimed（未声称）
```

本阶段用一个真实《视频工厂》产出前任务做 dry run（干跑）输入，验证安全工程融合框架能否输出 route_decision（路由判断）、engineering_state_map_check（工程状态地图检查）、RAG 默认判断、source_readback（原文回读）要求、tool permission（工具权限）、copy permission（文案权限）、card decision（卡片判断）、material evidence（素材证据）、evaluator / failure / guardrail（评估 / 失败 / 护栏）、human decision gate（人工决策闸门）、allowed_actions（允许动作）、blocked_actions（阻断动作）和 next_safe_step（下一步安全动作）。

### 2AB.1 added_fixture_family（新增测试样例家族）

| fixture family | passing fixture | blocked fixture |
|---|---|---|
| `real_task_dry_run_preflight` | `fixtures/passing/real_task_dry_run_preflight.passing.yaml` | `fixtures/blocked/real_task_dry_run_preflight.blocked.yaml` |

### 2AB.2 added_probe_family（新增探测脚本家族）

| probe | purpose |
|---|---|
| `probes/real_task_dry_run_preflight_probe.py` | 验证真实任务执行前干跑的 13 个判断点和 8 个阻断场景，只读取本地 YAML fixture，不外呼、不读真实媒体、不启动服务、不启用运行时。 |

### 2AB.3 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - dry run 通过不等于真实内容产出完成
  - preflight 通过不等于视频已生成
  - RAG 默认进入判断链不等于真实调用 DashVector 或运行 Chroma
  - 文案权限检查通过不等于允许 Codex 改语义、标题或核心判断
  - 卡片判断检查通过不等于本轮生成卡片图片
  - 素材证据检查通过不等于读取了真实媒体
  - evaluator / guardrail 检查通过不等于内容验证、可发送状态或生产可用状态推进
  - 本阶段不启动 service，不调用外部 API，不调用 TTS，不生成媒体
```

## 2AA. 20260618 goal mode safe engineering fusion update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: goal_mode_safe_engineering_fusion（目标模式安全工程融合）
  status（状态）: no_service_fixture_first_framework_landed（无服务 / 测试样例优先框架已落地）
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: main（主分支）
  runtime_enabled（运行时启用）: false（未启用）
  service_started（服务启动）: false（未启动）
  external_api_called（外部 API 调用）: false（未调用）
  dashvector_real_call（DashVector 真实调用）: false（未调用）
  chroma_ingestion_run（Chroma 入库）: false（未运行）
  media_generated（媒体生成）: false（未生成）
```

本阶段把工程线第一轮安全融合落到 schema（结构契约）、fixture（测试样例）和 probe（探测脚本）：RAG（检索增强生成）成为默认判断链和检索准备链，但不默认真实外部调用；adapter（适配器）仍是执行框架候选，不替代《视频工厂》主线；runtime（运行时）和 service（服务）仍未启用。

### 2AA.1 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `engineering_state_map` | 区分 formal / candidate / probe_only / documented_only / missing / conflict / blocked，防止状态混层。 | `schemas/engineering_state_map.schema.yaml` |
| `acceptance_contract` | 规定每个模块的 done_when、证据、验证、未推进状态和下一步安全动作。 | `schemas/acceptance_contract.schema.yaml` |
| `state_node_edge_contract` | 在 no-service 条件下定义 State / Node / Edge（状态 / 节点 / 边）。 | `schemas/state_node_edge_contract.schema.yaml` |
| `rag_default_decision` | 规定 RAG 是默认判断链，但不等于真实外部调用。 | `schemas/rag_default_decision.schema.yaml` |
| `tool_registry` | 规定工具能否外呼、写仓库、产生成本、读隐私文件。 | `schemas/tool_registry.schema.yaml` |
| `retriever_adapter` | 用 fixture-first 方式把检索器输出转成 retrieval_manifest（检索清单）。 | `schemas/retriever_adapter.schema.yaml` |
| `vector_store_adapter` | 规定 DashVector 主路线和 Chroma sandbox 边界。 | `schemas/vector_store_adapter.schema.yaml` |
| `evaluator_result` | 区分技术验证、内容验证、可发送状态和生产可用状态。 | `schemas/evaluator_result.schema.yaml` |
| `failure_route` | 把失败原因映射到 fallback_layer、owner 和 next_safe_step。 | `schemas/failure_route.schema.yaml` |
| `human_decision_gate` | 规定目标、权限、成本、审美、语义、状态升级和外部调用必须人工确认。 | `schemas/human_decision_gate.schema.yaml` |
| `guardrail_result` | 汇总 secret scan、no-write、禁止状态和 git add dot 护栏。 | `schemas/guardrail_result.schema.yaml` |
| `report_contract` | 规定报告必须包含读取、修改、验证、未推进状态和下一步安全动作。 | `schemas/report_contract.schema.yaml` |
| `trace_event` | 定义本地 trace event（追踪事件）字段，不接外部 telemetry。 | `schemas/trace_event.schema.yaml` |

### 2AA.2 added_fixture_families（新增 fixture 家族）

| fixture family | passing fixture | blocked fixture |
|---|---|---|
| `engineering_state_map` | `fixtures/passing/engineering_state_map.passing.yaml` | `fixtures/blocked/engineering_state_map.blocked.yaml` |
| `state_node_edge` | `fixtures/passing/state_node_edge.passing.yaml` | `fixtures/blocked/state_node_edge.blocked.yaml` |
| `rag_default_decision` | `fixtures/passing/rag_default_decision.passing.yaml` | `fixtures/blocked/rag_default_decision.blocked.yaml` |
| `evaluator_failure_guardrail` | `fixtures/passing/evaluator_failure_guardrail.passing.yaml` | `fixtures/blocked/evaluator_failure_guardrail.blocked.yaml` |
| `report_trace_log` | `fixtures/passing/report_trace_log.passing.yaml` | `fixtures/blocked/report_trace_log.blocked.yaml` |

### 2AA.3 added_probe_families（新增 probe 家族）

| probe | purpose |
|---|---|
| `probes/engineering_state_map_probe.py` | 验证状态枚举、证据文件、conflict 裁决、probe_only 不直跳 formal。 |
| `probes/state_node_edge_no_service_probe.py` | 验证节点输入 / 输出 / 验证 / 阻断 / 回退 / trace 字段和人工中断边。 |
| `probes/rag_default_decision_probe.py` | 验证 RAG 默认判断链、source_path / chunk_id / readback、工具权限和 Chroma 边界。 |
| `probes/evaluator_failure_guardrail_probe.py` | 验证评估、失败路由、人工确认、护栏触发必须阻断或修复。 |
| `probes/report_trace_log_validator.py` | 验证报告、trace、latest 顶部摘要不得缺证据或误推进状态。 |

### 2AA.4 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - schema / fixture / probe 落地不等于 runtime 启用
  - RAG 默认判断链不等于 DashVector / Chroma 真实调用
  - Tool Registry fixture 不等于允许工具外呼或写仓库
  - Evaluator fixture 不等于内容验证通过
  - Report / Trace / Log validator 不等于工程生产可用
  - 本阶段不启动 service，不调用外部 API，不生成媒体，不推进 send_ready
```

## 2. contract order

```text
WorkflowRouteDecision
-> RetrievalManifest
-> SourceReadback
-> RetrievalGapReport
-> DeepSeekTriggerDecision
-> BlockedIfCheck
-> HumanReviewInterrupt
-> WriteExecutorHandoff
-> CompletionTruthCheck
```

`CrossContractTrace` is the shared trace schema across the chain. It standardizes `task_id / handoff_id / commit_sha / source_path / content_hash` style fields and keeps `runtime_enabled / sandbox_created / minimal_router_prototype_created` false in this design stage.

## 2A. 20260616 adapter contract phase update

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: contracts_and_schemas（契约与 schema 阶段）
  status（状态）: contract_schema_phase_landed（契约 / schema / fixture 已落地）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段把 `agent-service-toolkit` 接入前必须遵守的规则落成静态 schema、passing fixture 和 blocked fixture。它仍然不是 adapter runtime 代码，不启动 FastAPI / Docker / Postgres / Streamlit，不运行 Chroma ingestion，不调用 DashVector 或外部 API。

### 2A.1 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `graph_runtime_adapter` | 规定 LangGraph 只能作为 no-write workflow runtime layer，不能替代 Project State Action Router。 | `schemas/graph_runtime_adapter.schema.yaml` |
| `retrieval_manifest` | 扩展检索清单字段，要求 provider / source_path / chunk_id / source_readback_required / gap_status。 | `schemas/retrieval_manifest.schema.yaml` |
| `source_readback_map` | 把检索命中映射回当前分支原文，判断能否作为事实。 | `schemas/source_readback_map.schema.yaml` |
| `cleaning_adapter` | 规定入库前安全加载、secret scan、metadata、dedup、chunking 和 source_readback index。 | `schemas/cleaning_adapter.schema.yaml` |
| `service_contract_no_write` | 规定 FastAPI / service 只能 route / retrieve / validate / block / interrupt / handoff，不能写仓库。 | `schemas/service_contract_no_write.schema.yaml` |
| `runtime_memory_boundary` | 规定 runtime memory 只能作临时状态和非权威缓存，不得替代仓库事实。 | `schemas/runtime_memory_boundary.schema.yaml` |
| `completion_truth_check_node` | 规定完成真实性检查节点必须拦截 false completion、false runtime、状态误推进、RAG 冒充事实和 service 冒充写入。 | `schemas/completion_truth_check_node.schema.yaml` |

### 2A.2 added_fixture_families（新增 fixture 家族）

| fixture family | passing fixtures | blocked fixtures |
|---|---|---|
| `graph_runtime_adapter` | `fixtures/passing/graph_runtime_adapter.passing.yaml` | `fixtures/blocked/graph_runtime_adapter.blocked_runtime_write.yaml`、`fixtures/blocked/graph_runtime_adapter.blocked_missing_source_readback.yaml`、`fixtures/blocked/graph_runtime_adapter.blocked_completed_without_truth_check.yaml` |
| `retrieval_manifest` | `fixtures/passing/retrieval_manifest_dashvector_fixture.passing.yaml`、`fixtures/passing/retrieval_manifest_chroma_sandbox_fixture.passing.yaml` | `fixtures/blocked/retrieval_manifest_chroma_metadata_missing.blocked.yaml`、`fixtures/blocked/retrieval_manifest_page_content_only.blocked.yaml`、`fixtures/blocked/retrieval_manifest_chroma_replace_dashvector.blocked.yaml`、`fixtures/blocked/retrieval_manifest_claimed_as_fact.blocked.yaml` |
| `source_readback_map` | `fixtures/passing/source_readback_map.passing.yaml` | `fixtures/blocked/source_readback_missing.blocked.yaml`、`fixtures/blocked/source_readback_conflict.blocked.yaml`、`fixtures/blocked/source_readback_stale_source.blocked.yaml` |
| `cleaning_adapter` | `fixtures/passing/cleaning_adapter.passing.yaml` | `fixtures/blocked/cleaning_secret_like_content.blocked.yaml`、`fixtures/blocked/cleaning_missing_metadata.blocked.yaml`、`fixtures/blocked/cleaning_chunk_missing_source_path.blocked.yaml`、`fixtures/blocked/cleaning_legacy_fact_override.blocked.yaml` |
| `service_contract_no_write` | `fixtures/passing/service_contract_no_write.passing.yaml` | `fixtures/blocked/service_contract_no_write_attempt_write.blocked.yaml`、`fixtures/blocked/service_contract_no_write_attempt_commit_push.blocked.yaml`、`fixtures/blocked/service_contract_no_write_runtime_enabled.blocked.yaml`、`fixtures/blocked/service_contract_no_write_external_api_without_auth.blocked.yaml` |
| `runtime_memory_boundary` | `fixtures/passing/runtime_memory_boundary.passing.yaml` | `fixtures/blocked/runtime_memory_boundary.blocked_repo_fact_replacement.yaml`、`fixtures/blocked/runtime_memory_boundary.blocked_operation_records_replacement.yaml`、`fixtures/blocked/runtime_memory_boundary.blocked_current_data_goal_anchor_replacement.yaml` |
| `completion_truth_check_node` | `fixtures/passing/completion_truth_check.passing.yaml` | `fixtures/blocked/completion_truth_check.false_completion_blocked.yaml`、`fixtures/blocked/completion_truth_check.sandbox_as_runtime_blocked.yaml`、`fixtures/blocked/completion_truth_check.rag_as_fact_blocked.yaml`、`fixtures/blocked/completion_truth_check.technical_as_content_blocked.yaml`、`fixtures/blocked/completion_truth_check.file_exists_as_done_blocked.yaml`、`fixtures/blocked/completion_truth_check.service_as_repo_write_blocked.yaml` |

### 2A.3 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - schema 落地不等于 runtime 接入
  - fixture 通过不等于正式服务可用
  - Chroma fixture 不等于 Chroma 替代 DashVector
  - service no-write fixture 不等于允许启动服务
  - runtime memory fixture 不等于 memory 可替代 Git / repo / codex_log / review_loop 事实
  - completion truth fixture 不等于视频 / 声音 / 视觉 / 发布状态推进
  - adapter_infrastructure_flow 仍为 candidate，未写入正式 workflow 索引
```

## 20260616｜Editing Workflow Contract Patch

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: workflow_first_pre_integration_repair（工作流优先正式接入前修补）
  status（状态）: editing_workflow_contract_family_landed（剪辑 workflow 契约家族已落地）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段只补剪辑 workflow 契约家族和静态 fixture，用于阻断“技术预览、路由卡、报告生成、文件存在”冒充剪辑交付完成。它不执行剪辑、不生成视频、不启动 service、不启用 runtime、不合并 main。

### 2B.1 added_schema_families（新增 schema 家族）

| schema family | purpose | schema |
|---|---|---|
| `editing_execution_contract` | 约束剪辑执行必须有锁定文案、line_group 时间线、TTS、卡片、素材证据、审片包和完成真实性检查。 | `schemas/editing_execution_contract.schema.yaml` |
| `timeline_assembly_contract` | 约束时间线条目必须能回到 line_group、素材片段和时间码。 | `schemas/timeline_assembly_contract.schema.yaml` |
| `subtitle_card_overlap_contract` | 约束字幕、卡片和核心证据区不能 high severity 重叠。 | `schemas/subtitle_card_overlap_contract.schema.yaml` |
| `tts_route_contract` | 约束实际 TTS provider / model / voice_id / fallback 授权和非静音音频。 | `schemas/tts_route_contract.schema.yaml` |
| `review_pack_contract` | 约束候选片或阻断结果必须带审片包、预检报告、媒体探针和人工复审边界。 | `schemas/review_pack_contract.schema.yaml` |
| `media_probe_contract` | 约束媒体探针必须检查视频存在、音频、字幕、分辨率、时长和解码。 | `schemas/media_probe_contract.schema.yaml` |
| `publish_candidate_or_blocked_contract` | 约束剪辑 workflow 只能收口为人工复审候选片或可发布候选片不可交付阻断。 | `schemas/publish_candidate_or_blocked_contract.schema.yaml` |

### 2B.2 added_passing_fixtures（新增通过样例）

| fixture family | passing fixture |
|---|---|
| `editing_execution_contract` | `fixtures/passing/editing_execution_contract.passing.yaml` |
| `timeline_assembly_contract` | `fixtures/passing/timeline_assembly_contract.passing.yaml` |
| `subtitle_card_overlap_contract` | `fixtures/passing/subtitle_card_overlap_contract.passing.yaml` |
| `tts_route_contract` | `fixtures/passing/tts_route_contract.passing.yaml` |
| `review_pack_contract` | `fixtures/passing/review_pack_contract.passing.yaml` |
| `media_probe_contract` | `fixtures/passing/media_probe_contract.passing.yaml` |
| `publish_candidate_or_blocked_contract` | `fixtures/passing/publish_candidate_or_blocked_contract.passing.yaml` |

### 2B.3 added_blocked_fixtures（新增阻断样例）

| blocked case | blocked fixture |
|---|---|
| 缺文案到时间线映射 | `fixtures/blocked/editing_missing_script_to_timeline_map.blocked.yaml` |
| 技术预览冒充完成 | `fixtures/blocked/editing_technical_preview_as_completed.blocked.yaml` |
| 时间线画面错位 | `fixtures/blocked/timeline_visual_mismatch.blocked.yaml` |
| 字幕卡片高重叠 | `fixtures/blocked/subtitle_card_high_overlap.blocked.yaml` |
| TTS 未授权降级 | `fixtures/blocked/tts_fallback_unauthorized.blocked.yaml` |
| 审片包缺失 | `fixtures/blocked/review_pack_missing.blocked.yaml` |
| 媒体探针无效 | `fixtures/blocked/media_probe_invalid.blocked.yaml` |
| 候选片状态偷换 | `fixtures/blocked/publish_candidate_state_promotion.blocked.yaml` |

### 2B.4 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - 只补剪辑 workflow 契约，不等于正式接入整个项目
  - schema 落地不等于 runtime 接入
  - fixture 通过不等于真实剪辑可执行
  - review_pack contract 不等于真实审片包已生成
  - media_probe contract 不等于真实视频已探测
  - publish_candidate contract 不等于可发送状态开启
  - 本阶段不启动 service，不合并 main，不调用外部 API
```

## 20260616｜Editing Workflow No-Render Probe

```yaml
schema_contract_index_update（schema 契约索引更新）:
  phase（阶段）: editing_workflow_no_render_probe（剪辑工作流无渲染探测）
  status（状态）: no_render_probe_passed（无渲染探测通过）
  project_route（项目路由）: video_factory
  branch（分支）: adapter/agent-service-toolkit-sandbox
  probe_script（探测脚本）: probes/editing_workflow_no_render_probe.py
  report（报告）: codex_log/framework_adapter/20260616_editing_workflow_no_render_probe_report.md
  runtime_enabled（是否启用正式运行时）: false
  service_started（是否启动服务）: false
  media_generated（是否生成媒体）: false
  external_api_called（是否调用外部 API）: false
  main_branch_modified（是否修改 main）: false
```

本阶段新增剪辑 workflow 的本地无渲染 probe，用于验证 7 类剪辑契约家族和 15 个 passing / blocked fixture 能否形成可检查的静态链路。它不读取真实媒体、不调用 TTS、不调用 FFmpeg、不启动 service、不启用 runtime、不运行 Chroma 入库、不真实调用 DashVector。

### 2C.1 probe_inputs（探测输入）

| input family | files |
|---|---|
| `schemas` | `editing_execution_contract.schema.yaml`、`timeline_assembly_contract.schema.yaml`、`subtitle_card_overlap_contract.schema.yaml`、`tts_route_contract.schema.yaml`、`review_pack_contract.schema.yaml`、`media_probe_contract.schema.yaml`、`publish_candidate_or_blocked_contract.schema.yaml` |
| `passing fixtures` | `editing_execution_contract.passing.yaml`、`timeline_assembly_contract.passing.yaml`、`subtitle_card_overlap_contract.passing.yaml`、`tts_route_contract.passing.yaml`、`review_pack_contract.passing.yaml`、`media_probe_contract.passing.yaml`、`publish_candidate_or_blocked_contract.passing.yaml` |
| `blocked fixtures` | `editing_missing_script_to_timeline_map.blocked.yaml`、`editing_technical_preview_as_completed.blocked.yaml`、`timeline_visual_mismatch.blocked.yaml`、`subtitle_card_high_overlap.blocked.yaml`、`tts_fallback_unauthorized.blocked.yaml`、`review_pack_missing.blocked.yaml`、`media_probe_invalid.blocked.yaml`、`publish_candidate_state_promotion.blocked.yaml` |

### 2C.2 probe_result（探测结果）

```yaml
probe_result（探测结果）:
  schema_contracts_passed（schema 契约检查是否通过）: true
  passing_path_passed（通过路径是否通过）: true
  blocked_cases_passed（阻断样例是否通过）: true
  blocked_case_count（阻断样例数量）: 8
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
```

### 2C.3 status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  - no-render probe 通过不等于真实剪辑已执行
  - no-render probe 通过不等于视频已生成
  - no-render probe 通过不等于 TTS 已调用
  - no-render probe 通过不等于真实媒体探针已执行
  - no-render probe 通过不等于 runtime 接入
  - no-render probe 通过不等于 service 可启动
  - no-render probe 通过不等于 main 可合并
  - no-render probe 通过不等于整体代码接入已经就绪
```

## 3. contract responsibilities

| order | contract | responsibility | schema |
|---:|---|---|---|
| 1 | `WorkflowRouteDecision` | Route user input into project, task type, workflow, responsibility layer, and execution permission. | `schemas/workflow_route_decision.schema.yaml` |
| 2 | `RetrievalManifest` | Record DashVector / Vector RAG retrieval and require repo source readback. | `schemas/retrieval_manifest.schema.yaml` |
| 3 | `SourceReadback` | Confirm repo source files remain `source_of_truth`. | `schemas/source_readback.schema.yaml` |
| 4 | `RetrievalGapReport` | Convert empty, low-confidence, legacy, or conflicting retrieval into blockers or DeepSeek trigger recommendation. | `schemas/retrieval_gap_report.schema.yaml` |
| 5 | `DeepSeekTriggerDecision` | Decide if DeepSeek enters as conditional read-only reviewer after retrieval/readback. | `schemas/deepseek_trigger_decision.schema.yaml` |
| 6 | `BlockedIfCheck` | Normalize blockers from all upstream contracts into one execution gate. | `schemas/blocked_if_check.schema.yaml` |
| 7 | `HumanReviewInterrupt` | Insert human review before sandbox, runtime enablement, status promotion, source conflict override, or executor switch. | `schemas/human_review_interrupt.schema.yaml` |
| 8 | `WriteExecutorHandoff` | Package scoped write instructions for `active_write_executor = codex`. | `schemas/write_executor_handoff.schema.yaml` |
| 9 | `CompletionTruthCheck` | Decide whether completion can be claimed without false status, fallback, retrieval-only, or local-only claims. | `schemas/completion_truth_check.schema.yaml` |

## 4. fixtures

Each of the 9 core contracts has:

- one passing fixture under `fixtures/passing/`
- one blocked fixture under `fixtures/blocked/`

Fixture task ids:

- passing: `vf_schema_contract_fixture_20260614_001`
- blocked: `vf_schema_contract_fixture_20260614_blocked_001`

The passing fixtures are static examples only. They do not prove a runtime exists. The blocked fixtures show how each contract must stop execution when a critical field is missing, a source conflict exists, a forbidden status appears, or human review is required.

## 5. sandbox preconditions

All 9 contracts are required before any sandbox or minimal router prototype.

Sandbox remains blocked unless all are true in a later task:

1. schemas are reviewed and accepted;
2. fixtures pass static validation;
3. cross-contract trace fields are consistent;
4. source readback remains mandatory after retrieval;
5. DeepSeek remains conditional read-only review;
6. human review interrupts cannot be auto-resumed;
7. write handoff keeps `active_write_executor = codex`;
8. completion truth check forbids status promotion and false completion claims.

## 6. install preflight status

2026-06-14 static validation outcome:

```text
schema_contract_static_validation = passed
install_preflight_ready = true
```

This means the schema contract layer is ready for a later no-write sandbox intake prompt. It does not mean sandbox has been created, runtime has been enabled, dependencies have been installed, or external code has been copied.

## 7. why sandbox is still not created in this stage

`sandbox_entry_allowed_this_round = false`

Reasons:

- this round is static validation only;
- no install task has been authorized;
- no adapter service has been installed or run;
- no sandbox path has been created;
- no minimal router prototype has been created;
- no external code has been copied;
- no dependency has been installed.

## 8. next stage

Next safe stage:

```text
sandbox_intake_no_write_prompt
```

The next prompt must remain no-write unless the user explicitly authorizes installation in a separate task.

Static validation checklist now passed:

1. 10 schema files exist.
2. 18 fixture files exist.
3. Every schema includes `contract_name / version / status / required_fields / trace_fields`.
4. Every passing fixture contains every minimum required field for its contract.
5. Every blocked fixture contains `blocked: true` and `blocked_reasons`.
6. Fixture files do not contain credential-like values.
7. Forbidden paths remain untouched.
8. Runtime, sandbox, prototype, video, publish, voice, and visual statuses remain unadvanced.
