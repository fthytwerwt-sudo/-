# 20260616 workflow_first_pre_integration_matrix（工作流优先正式接入前接入表）

## 1. matrix_status（接入表状态）

```yaml
integration_matrix（接入表）:
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: adapter/agent-service-toolkit-sandbox
  matrix_type（接入表类型）: workflow_first_pre_integration_audit（工作流优先正式接入前审核）
  execution_permission（执行权限）: report_and_matrix_only（只允许报告与接入表）
  formal_integration_allowed_now（当前是否允许正式接入）: no（否）
  runtime_enablement_allowed_now（当前是否允许启用运行时）: no（否）
  main_merge_allowed_now（当前是否允许合并 main）: no（否）
  service_start_allowed_now（当前是否允许启动服务）: no（否）
  stopline（停止线）: pre_formal_integration_stopline（正式接入前停止线）
```

## 2. decision_legend（接入判断图例）

| integration_decision（接入判断） | meaning（含义） |
|---|---|
| `direct_embed（可直接嵌入）` | 可作为机制 / 节点模式直接吸收，但仍不得自动启用运行时。 |
| `adapter_required（需要适配器）` | 不能直接接，需要写适配边界、输入输出和阻断条件。 |
| `contract_required（需要契约）` | 需要先补 contract（契约结构）和 fixture（验证样例）。 |
| `probe_required（需要探测）` | 必须先做 no-service / no-write / runtime probe（无服务 / 不写仓库 / 运行时探测）。 |
| `disabled_by_default（默认禁用）` | 默认不启用，只作为未来候选或隔离能力。 |
| `blocked_before_formal_integration（正式接入前阻断）` | 当前缺关键证据，正式接入前必须停下。 |

## 3. integration_matrix（接入表）

| layer（层级） | item（项目） | current_repo_evidence（当前仓库证据） | target_role_after_integration（接入后的目标角色） | integration_decision（接入判断） | required_adapter（所需适配器） | required_contract（所需契约） | required_probe（所需探测） | blocked_before_formal_integration_if（正式接入前阻断条件） | can_merge_to_main_now（现在是否可合并 main） | user_chatgpt_review_required（是否需要用户 / ChatGPT 复审） |
|---|---|---|---|---|---|---|---|---|---|---|
| workflow_registry（工作流注册表） | copy_to_video_workflow（文案到视频工作流） | `copy_testing_flow`、`material_evidence_flow`、`aesthetic_editing_flow` 已分别覆盖文案、素材、剪辑局部。 | 作为“文案到可发布候选片”的端到端 workflow 注册候选。 | `contract_required（需要契约）` | workflow registry adapter（工作流注册适配器） | copy_to_video_workflow_contract（文案到视频工作流契约） | no-service workflow registry probe（无服务工作流注册探测） | 缺 locked_copy_contract、material_detail_report、data_goal_anchor 或 publish candidate 阻断线。 | no（否） | yes（是） |
| workflow_registry（工作流注册表） | material_audit_workflow（素材解析工作流） | `material_evidence_flow` 已要求 material_parse_pack、source_segment_inventory、material_detail_report。 | 作为素材解析、证据契约、句组证据闸门的独立 workflow。 | `adapter_required（需要适配器）` | cleaning_adapter（清洗适配器）、source_readback_adapter（原文回读适配器） | material_audit_workflow_contract（素材解析工作流契约） | material fixture and timecode probe（素材样例与时间码探测） | 缺素材解析 skill、时间码、source_path、line_group evidence。 | no（否） | yes（是） |
| workflow_registry（工作流注册表） | editing_execution_workflow（剪辑执行工作流） | `aesthetic_editing_flow` 已列出 script_to_shot_execution_map、material_usage_ledger、review_pack；执行规则列出 line_group、字幕卡片、素材证据闸门。 | 用户最关心的剪辑执行主 workflow，负责 timeline / subtitle / audio / cards / review_pack。 | `blocked_before_formal_integration（正式接入前阻断）` | codex_executor_adapter（Codex 执行器适配器）、media_handoff_adapter（媒体交接适配器） | editing_execution_contract、timeline_assembly_contract、subtitle_card_overlap_contract、tts_route_contract、review_pack_contract | editing no-render preflight probe（剪辑无渲染预检探测） | 缺任一剪辑专属契约、只能产 technical preview、无法收口到候选片或阻断。 | no（否） | yes（是） |
| workflow_registry（工作流注册表） | operation_data_review_workflow（运营数据复盘工作流） | `data_review_flow`、operation_data_intake、operation_review、operation_next_variable_decision 已存在。 | 作为运营数据录入、复盘、下一变量判断 workflow。 | `adapter_required（需要适配器）` | runtime_memory_boundary_adapter（运行时记忆边界适配器） | operation_data_review_workflow_contract（运营数据复盘工作流契约） | operation records readback probe（运营记录回读探测） | memory/store 试图替代 operation_records、current_data_goal_anchor 或 review_loop。 | no（否） | yes（是） |
| workflow_registry（工作流注册表） | reference_to_execution_workflow（参考到执行工作流） | AGENTS 与 codex readme 均要求 Reference-to-Execution Contract；当前索引未作为独立 workflow 注册。 | 把参考图 / 视频 / 声音 / 样片转为 reference_anchor、effect_targets、deviation_check。 | `contract_required（需要契约）` | reference_readback_adapter（参考回读适配器） | reference_to_execution_workflow_contract（参考到执行工作流契约） | reference anchor source_readback probe（参考锚点原文回读探测） | 参考样本被当成固定流程、旧 reference 覆盖当前事实、缺偏离检查。 | no（否） | yes（是） |
| workflow_registry（工作流注册表） | adapter_infrastructure_workflow（适配基础设施工作流） | 20260615 / 20260616 报告均将其登记为 candidate，未启用。 | 只承载 schema / fixture / probe / adapter boundary / matrix 等基础设施。 | `blocked_before_formal_integration（正式接入前阻断）` | adapter_infrastructure_adapter（适配基础设施适配器） | workflow_registry_schema（工作流注册表结构契约） | candidate workflow admission probe（候选 workflow 准入探测） | 未经用户 / ChatGPT 确认、缺正式 workflow 准入 fixture 和 blocked case。 | no（否） | yes（是） |
| contract_schema（契约结构） | graph_runtime_adapter（图运行时适配器） | `schemas/graph_runtime_adapter.schema.yaml`、passing / blocked fixtures、no_service_graph_probe 已存在。 | 约束 LangGraph 只能作为工作流运行层。 | `probe_required（需要探测）` | langgraph_adapter（LangGraph 适配器） | graph_runtime_adapter_contract（图运行适配契约） | real LangGraph no-service probe（真实 LangGraph 无服务探测） | LangGraph 替代项目路由、运行时直接写仓库、缺 completion_truth_check。 | no（否） | yes（是） |
| contract_schema（契约结构） | retrieval_manifest（检索清单） | schema、DashVector fixture、Chroma sandbox fixture、page_content-only blocked fixture 已存在。 | 把所有检索输出转成可回读清单。 | `adapter_required（需要适配器）` | retrieval_adapter（检索适配器） | retrieval_manifest_schema（检索清单结构） | retrieval_cleaning_adapter_probe（检索与清洗适配探测） | 缺 source_path、chunk_id、content_hash、line_range 或把 RAG 摘要当事实。 | no（否） | yes（是） |
| contract_schema（契约结构） | source_readback_map（原文回读映射） | schema、passing、missing/conflict/stale blocked fixtures 已存在。 | 把检索命中回到当前分支原文件和行号。 | `adapter_required（需要适配器）` | source_readback_adapter（原文回读适配器） | source_readback_map_schema（原文回读映射结构） | source readback path probe（原文路径回读探测） | 无法回读当前分支原文件、旧口径冒充当前事实。 | no（否） | yes（是） |
| contract_schema（契约结构） | cleaning_adapter（清洗适配器） | schema、secret / metadata / legacy blocked fixtures 已存在。 | 安全加载、密钥扫描、元数据保真、去重与切片。 | `adapter_required（需要适配器）` | cleaning_adapter（清洗适配器） | cleaning_adapter_contract（清洗适配契约） | cleaning metadata preservation probe（清洗元数据保真探测） | 入库前未做密钥扫描、chunk 缺 source_path / chunk_id、旧 gray_test 覆盖正式事实。 | no（否） | yes（是） |
| contract_schema（契约结构） | service_contract_no_write（服务不写仓库契约） | schema、write/commit/runtime/external API blocked fixtures 已存在。 | 约束 FastAPI / service 只能 route / retrieve / validate / handoff。 | `probe_required（需要探测）` | service_contract_adapter（服务契约适配器） | service_contract_no_write_schema（服务不写仓库结构） | service no-write real probe（服务不写仓库真实探测） | service 尝试写仓库、提交、推送、开启运行时或未授权调用外部接口。 | no（否） | yes（是） |
| contract_schema（契约结构） | runtime_memory_boundary（运行时记忆边界） | schema、repo facts / operation_records / data_goal_anchor replacement blocked fixtures 已存在。 | 允许临时线程状态，不允许成为项目事实源。 | `direct_embed（可直接嵌入）` | runtime_memory_boundary_adapter（运行时记忆边界适配器） | runtime_memory_boundary_schema（运行时记忆边界结构） | memory boundary regression probe（记忆边界回归探测） | memory 替代 Git / codex_log / review_loop / current_data_goal_anchor。 | no（否） | yes（是） |
| contract_schema（契约结构） | completion_truth_check_node（完成真实性检查节点） | schema、false completion / sandbox runtime / RAG fact / technical-content blocked fixtures 已存在。 | 成为所有完成声明前的最终检查节点。 | `direct_embed（可直接嵌入）` | completion_truth_check_adapter（完成真实性检查适配器） | completion_truth_check_node_schema（完成真实性检查节点结构） | completion truth graph regression probe（完成真实性图回归探测） | 技术成功、文件存在、报告生成或 sandbox 成功冒充完成。 | no（否） | yes（是） |
| contract_schema（契约结构） | editing_execution_contract（剪辑执行契约） | 当前仅散落在执行规则和 aesthetic_editing_flow 中。 | 规定剪辑输入、输出、必经步骤、阻断线和完成标准。 | `contract_required（需要契约）` | codex_executor_adapter（Codex 执行器适配器） | editing_execution_contract | editing workflow contract fixture（剪辑工作流契约样例） | 缺 line_group 映射、卡片字幕检查、review_pack、候选片/阻断收口。 | no（否） | yes（是） |
| contract_schema（契约结构） | workflow_registry_schema（工作流注册表结构契约） | 当前只有 6 类 workflow 索引，没有新 6 workflow 注册 schema。 | 明确正式 workflow、candidate workflow、输入输出与准入条件。 | `contract_required（需要契约）` | workflow_registry_adapter（工作流注册表适配器） | workflow_registry_schema | workflow registry static validation（工作流注册表静态验证） | 候选 workflow 被直接写成正式入口或旧 6 类被硬塞。 | no（否） | yes（是） |
| adapters（适配器） | cleaning_adapter（清洗适配器） | schema / fixture 已落地，但真实链路未探测。 | 把自然语言 / 文件输入转为 task packet 和 metadata-rich chunks。 | `adapter_required（需要适配器）` | cleaning_adapter | cleaning_adapter_contract | retrieval_cleaning_adapter_probe | 不能输出 task_type、project_route、must_read_files、blocked_if 或元数据缺失。 | no（否） | yes（是） |
| adapters（适配器） | retrieval_adapter（检索适配器） | DashVector 主线、Chroma sandbox、page_content-only blocked 已记录。 | DashVector -> RetrievalManifest；Chroma 只作 sandbox 对照。 | `adapter_required（需要适配器）` | retrieval_adapter | retrieval_manifest_schema | DashVector fixture-to-manifest probe（DashVector 样例到清单探测） | Chroma 替代 DashVector、真实调用未授权、page_content-only 退化。 | no（否） | yes（是） |
| adapters（适配器） | source_readback_adapter（原文回读适配器） | SourceReadbackMap fixtures 已存在。 | 从检索结果回到仓库原文件和行号。 | `adapter_required（需要适配器）` | source_readback_adapter | source_readback_map_schema | source readback conflict probe（原文回读冲突探测） | RAG 摘要替代仓库事实或旧分支引用当前事实。 | no（否） | yes（是） |
| adapters（适配器） | langgraph_adapter（LangGraph 图编排适配器） | no_service_graph_probe 使用 fake runner；LangGraph 本地不可用。 | 后续只作为 workflow_runtime_layer。 | `probe_required（需要探测）` | langgraph_adapter | graph_runtime_adapter_contract | real LangGraph no-service probe | 替代 router、开启正式运行时、直接写仓库。 | no（否） | yes（是） |
| adapters（适配器） | codex_executor_adapter（Codex 执行器适配器） | active_write_executor = codex 已在多份报告和 schema 中固定。 | service/runtime 输出必须交给 Codex 写入。 | `direct_embed（可直接嵌入）` | codex_executor_adapter | write_executor_handoff_contract | executor handoff regression probe（执行器交接回归探测） | service/runtime/memory 绕过 Codex 写仓库。 | no（否） | yes（是） |
| adapters（适配器） | deepseek_supply_adapter（DeepSeek 供料适配器） | DeepSeek 条件触发、只读供料边界写入执行规则和 router。 | 只读供料、风险复核、冲突二次意见。 | `direct_embed（可直接嵌入）` | deepseek_supply_adapter | deepseek_trigger_decision_schema | conditional supply readback probe（条件供料回读探测） | DeepSeek 写文件、拍板事实、替代用户 / ChatGPT 判断。 | no（否） | yes（是） |
| policy_rules（策略规则） | no_degrade_completion_gate（禁止降级完成闸门） | AGENTS、codex_readme、execution_rules 均已写入。 | 防止 technical preview / fallback / route card 冒充完成。 | `direct_embed（可直接嵌入）` | not_applicable（不适用） | completion_truth_check_node_schema | completion truth regression probe | 降级方案未经用户授权却被写成完成。 | no（否） | yes（是） |
| policy_rules（策略规则） | status_promotion_guardrail（状态推进护栏） | workflow 索引、schema fixtures、probe report 已覆盖。 | 防止技术、沙盒、报告生成偷换成更高状态。 | `direct_embed（可直接嵌入）` | not_applicable（不适用） | completion_truth_check_node_schema | forbidden status scan（禁止状态扫描） | 技术成功冒充内容成功、sandbox 冒充正式运行时。 | no（否） | yes（是） |
| policy_rules（策略规则） | main_merge_gate（main 合并闸门） | adapter branch context 与 latest 均写明 main 不修改。 | 合并前需要用户 / ChatGPT 回审、secret scan、远端 HEAD 证据。 | `blocked_before_formal_integration（正式接入前阻断）` | not_applicable（不适用） | main_merge_candidate_review_contract | main merge candidate review probe | 未完成四层复审或缺远端 HEAD 验证。 | no（否） | yes（是） |
| policy_rules（策略规则） | external_api_gate（外部 API 闸门） | schema / reports 均写明未授权不得调用外部 API。 | 防止未授权 DashVector、Chroma ingestion、model API 调用。 | `direct_embed（可直接嵌入）` | not_applicable（不适用） | service_contract_no_write_schema | external API authorization scan | 未授权真实调用或写入 secret。 | no（否） | yes（是） |
| policy_rules（策略规则） | service_runtime_write_boundary（服务 / 运行时写入边界） | service_contract_no_write、runtime_memory_boundary、write_executor_handoff 已覆盖。 | service/runtime/memory 只输出 handoff，不写仓库。 | `direct_embed（可直接嵌入）` | codex_executor_adapter | service_contract_no_write_schema、runtime_memory_boundary_schema | service no-write probe | service/runtime/memory 尝试写仓库或替代 repo facts。 | no（否） | yes（是） |
| policy_rules（策略规则） | fallback_authorization_gate（降级授权闸门） | AGENTS、codex_readme、execution_rules 均写明 fallback 需要用户授权。 | fallback 只能作为 blocked 后建议。 | `direct_embed（可直接嵌入）` | not_applicable（不适用） | blocked_if_check_schema | fallback blocked-case fixture（降级阻断样例） | 未授权 fallback 被当完成。 | no（否） | yes（是） |

## 4. review_order（建议回审顺序）

```yaml
review_order（回审顺序）:
  1_workflow_registry（工作流注册表）: 先确认是否接受 6 个 workflow-first 注册候选，尤其 editing_execution_workflow。
  2_contract_schema（契约结构）: 再确认哪些 contract 先补，重点是 editing / timeline / subtitle-card / tts / review_pack。
  3_adapters（适配器）: 再确认哪些 adapter 只做边界和 handoff，不进入项目事实层。
  4_policy_rules（策略规则）: 最后确认所有正式接入前护栏必须继续生效。
  final_decision（最终判断）: 当前不允许正式接入整个项目，不允许启用运行时，不允许合并 main。
```
