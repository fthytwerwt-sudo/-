# 20260618 Goal Mode Safe Engineering Fusion Report

## route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - goal_mode_engineering_fusion（目标模式工程融合）
  - engineering_state_map_and_acceptance_contract（工程状态地图与验收契约）
  - state_node_edge_no_service_contract（状态 / 节点 / 边无服务契约）
  - rag_tool_retriever_fixture_adapter（RAG / 工具 / 检索器测试样例适配）
  - evaluator_failure_guardrail_matrix（评估器 / 失败路由 / 护栏矩阵）
  - trace_report_log_validator（追踪 / 报告 / 日志校验器）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
execution_permission（执行权限）: no_service_fixture_first_engineering_fusion（无服务 / 测试样例优先工程融合）
```

本轮执行到安全停止线：只落 schema（结构契约）、fixture（测试样例）、probe（探测脚本）、索引、latest（最新日志）和报告，不安装依赖，不启动服务，不调用外部 API（外部接口），不调用 TTS（语音合成），不真实调用 DashVector（阿里向量数据库）或 Chroma（本地向量库），不读取真实媒体，不生成媒体。

## user_confirmed_decisions_applied（用户确认决策已应用）

已更新 `codex_log/engineering_line_plain_manual/05_项目总规则_用户决策版.md`，新增 `## 10. 当前 8 个关键决策｜已确认版`：

1. `project_goal（项目目标）`: 《视频工厂》优先，先不升级成通用 AI（人工智能）工程平台，但结构兼容未来复用。
2. `current_stage（当前阶段）`: 只允许规则、状态地图、验收契约、接口层和 no-service / no-render（无服务 / 无渲染）验证。
3. `adapter_role（adapter 身份）`: adapter（适配器）是执行框架候选，不替代原《视频工厂》主线。
4. `rag_default_strategy（RAG 默认策略）`: RAG（检索增强生成）进入默认判断链和检索准备链，但不默认真实调用 DashVector / Chroma。
5. `runtime_boundary（运行时边界）`: State / RAG / Tool / Evaluator / Failure / Trace（状态 / 检索增强生成 / 工具 / 评估器 / 失败 / 追踪）接清楚后，才允许 runtime hardening（运行时加固）。
6. `card_decision_boundary（卡片决策边界）`: AI（人工智能）默认判断卡片类型、位置、数量；重大审美变化返回用户。
7. `copy_permission_boundary（文案权限边界）`: 融合完成前 Codex（写入执行器）只能改格式、断句、标点和 TTS 停顿，不能改语义、标题、核心判断。
8. `failure_return_rule（失败返回规则）`: 低风险自动回退修；影响目标、权限、成本、审美、语义、状态升级、外部调用的，必须返回用户确认。

## fusion_outputs（本轮融合产物）

### schema_files_created（已创建结构契约）

| file（文件） | purpose（用途） |
|---|---|
| `codex_source/schema_contracts/schemas/engineering_state_map.schema.yaml` | 定义 formal / candidate / probe_only / documented_only / missing / conflict / blocked 状态地图。 |
| `codex_source/schema_contracts/schemas/acceptance_contract.schema.yaml` | 定义每个模块的完成标准、证据、验证、未推进状态和下一步安全动作。 |
| `codex_source/schema_contracts/schemas/state_node_edge_contract.schema.yaml` | 定义 no-service（无服务）State / Node / Edge（状态 / 节点 / 边）契约。 |
| `codex_source/schema_contracts/schemas/rag_default_decision.schema.yaml` | 定义 RAG 默认判断链与真实外部调用边界。 |
| `codex_source/schema_contracts/schemas/tool_registry.schema.yaml` | 定义工具能否外呼、写仓库、产生成本、读取隐私文件。 |
| `codex_source/schema_contracts/schemas/retriever_adapter.schema.yaml` | 定义 fixture-first（测试样例优先）检索器输出到 retrieval_manifest（检索清单）。 |
| `codex_source/schema_contracts/schemas/vector_store_adapter.schema.yaml` | 定义 DashVector 主路线和 Chroma sandbox（沙盒）边界。 |
| `codex_source/schema_contracts/schemas/evaluator_result.schema.yaml` | 定义评估器结果，拆开技术验证、内容验证、发送状态和生产可用状态。 |
| `codex_source/schema_contracts/schemas/failure_route.schema.yaml` | 定义失败原因到回退层、处理方和下一步安全动作的映射。 |
| `codex_source/schema_contracts/schemas/human_decision_gate.schema.yaml` | 定义必须人工确认的目标、权限、成本、审美、语义、状态升级和外部调用。 |
| `codex_source/schema_contracts/schemas/guardrail_result.schema.yaml` | 定义密钥扫描、no-write（不写仓库）、禁止状态和全量暂存护栏。 |
| `codex_source/schema_contracts/schemas/report_contract.schema.yaml` | 定义报告必须包含读取、修改、验证、未推进状态和下一步安全动作。 |
| `codex_source/schema_contracts/schemas/trace_event.schema.yaml` | 定义本地追踪事件字段，不接外部观测服务。 |

### fixture_files_created（已创建测试样例）

| fixture family（测试样例家族） | passing（通过样例） | blocked（阻断样例） |
|---|---|---|
| `engineering_state_map` | `fixtures/passing/engineering_state_map.passing.yaml` | `fixtures/blocked/engineering_state_map.blocked.yaml` |
| `state_node_edge` | `fixtures/passing/state_node_edge.passing.yaml` | `fixtures/blocked/state_node_edge.blocked.yaml` |
| `rag_default_decision` | `fixtures/passing/rag_default_decision.passing.yaml` | `fixtures/blocked/rag_default_decision.blocked.yaml` |
| `evaluator_failure_guardrail` | `fixtures/passing/evaluator_failure_guardrail.passing.yaml` | `fixtures/blocked/evaluator_failure_guardrail.blocked.yaml` |
| `report_trace_log` | `fixtures/passing/report_trace_log.passing.yaml` | `fixtures/blocked/report_trace_log.blocked.yaml` |

### probe_files_created（已创建探测脚本）

| probe（探测脚本） | validation（验证） |
|---|---|
| `codex_source/schema_contracts/probes/engineering_state_map_probe.py` | 验证状态枚举、证据路径、conflict（冲突）裁决、probe_only（仅探测）不能直跳 formal（正式）。 |
| `codex_source/schema_contracts/probes/state_node_edge_no_service_probe.py` | 验证节点输入 / 输出 / 验证 / 阻断 / 回退 / 追踪字段和人工中断边。 |
| `codex_source/schema_contracts/probes/rag_default_decision_probe.py` | 验证 RAG 默认判断链、source_path（来源路径）、chunk_id（分块编号）、readback（原文回读）、工具权限和 Chroma 边界。 |
| `codex_source/schema_contracts/probes/evaluator_failure_guardrail_probe.py` | 验证技术验证不冒充内容验证、人工确认不能自动跳过、护栏触发必须阻断或修复。 |
| `codex_source/schema_contracts/probes/report_trace_log_validator.py` | 验证报告、追踪、latest 顶部摘要不得缺证据或误推进状态。 |

## rag_default_strategy（RAG 默认策略落实）

本轮已把 RAG（检索增强生成）写成默认判断路线和检索准备链：

- 默认需要 retrieval_manifest（检索清单）。
- 默认要求 source_path（来源路径）、chunk_id（分块编号）、line_range（行号范围）和 readback（原文回读）。
- 默认保持 GitHub main（远端主分支）仓库事实优先。
- 默认不允许真实调用 DashVector（阿里向量数据库）或 Chroma（本地向量库）。
- Chroma（本地向量库）只能作为 sandbox / fixture（沙盒 / 测试样例）参考，不替代 DashVector 主路线。

## copy_permission_boundary（文案权限后置）

本轮没有放宽 Codex（写入执行器）文案权限。`05_项目总规则_用户决策版.md` 已明确：融合完成前，Codex 只能改格式、断句、标点和 TTS（语音合成）停顿，不能改语义、标题和核心判断。是否放宽要在后续单独讨论。

## validation_result（验证结果）

```yaml
py_compile（Python 编译检查）: passed（通过）
engineering_state_map_probe（工程状态地图探测）: passed（通过）
state_node_edge_probe（状态节点边探测）: passed（通过）
rag_default_decision_probe（RAG 默认判断探测）: passed（通过）
evaluator_failure_guardrail_probe（评估失败护栏探测）: passed（通过）
report_trace_log_validator（报告追踪日志校验）: passed（通过）
editing_workflow_no_render_probe（剪辑无渲染探测回归）: passed（通过）
no_service_graph_probe（无服务图探测回归）: passed（通过）
git_diff_check（Git 差异检查）: passed（通过）
```

## not_done_this_round（本轮未做事项）

- 未启用 runtime（运行时）。
- 未启动 service（服务）。
- 未调用 external API（外部接口）。
- 未调用 TTS（语音合成）。
- 未真实调用 DashVector（阿里向量数据库）。
- 未运行 Chroma ingestion（Chroma 入库）。
- 未读取真实媒体。
- 未生成视频、音频、字幕、卡片或图片。
- 未推进 content_validation（内容验证）、send_ready（可发送状态）或 production_readiness（生产可用状态）。
- 未放宽 Codex（写入执行器）的文案语义权限。
- 未把 adapter（适配器）升级成 formal（正式）主线入口。

## blocked_subtasks（阻断子任务）

```yaml
blocked_subtasks（阻断子任务）: []
```

本轮没有出现需要停止整个目标的阻断项。所有真实 runtime / service / API / TTS / DashVector / Chroma / media 能力仍留给后续单独授权任务。

## next_safe_step（下一步安全动作）

建议用户 / ChatGPT（总控判断层）先回审本轮新增契约和探测结果。若确认通过，下一步可以二选一：

1. 进入 runtime hardening（运行时加固）前置任务，但仍保持 no-write（不写仓库）和 no-external-call（不外呼）。
2. 进入 real RAG authorization（真实 RAG 授权）任务，单独确认 DashVector / Chroma / embedding（向量化）是否允许真实调用。

进入下一阶段前，如果需要安装依赖、启动服务、打开端口、调用外部 API、调用 TTS、真实调用 DashVector / Chroma、读取真实媒体、生成媒体、推进内容验证、推进可发送状态或声明生产可用，必须先返回用户确认。
