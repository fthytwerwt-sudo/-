# 20260614 LangGraph / RAG / Cleaning Integration Probe

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - sandbox_architecture_probe（沙盒架构探测）
  - langgraph_structure_audit（LangGraph 结构审计）
  - langchain_position_fit_audit（LangChain 定位适配审计）
  - rag_mechanism_probe（RAG 机制探测）
  - cleaning_layer_slot_design（清洗层位置设计）
  - video_factory_integration_shape_simulation（视频工厂接入形态模拟）
  - no_main_pollution_check（不污染主线检查）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
execution_permission（执行权限）: sandbox_architecture_probe_report_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
```

本轮只在已安装完成的 sandbox 内做只读 / 无服务启动的结构探测，并把结论写回报告和 `latest.md`。本轮不代表视频工厂主仓库正式接入、不代表 runtime 启用、不代表 Chroma / DashVector 入库完成。

## 2. files_read（已读取文件）

```yaml
files_read（已读取文件）:
  current_repo（当前仓库）:
    AGENTS.md: read_ok
    codex_log/latest.md: read_ok
    codex_source/00_codex_readme.md: read_ok
    codex_source/19_project_state_action_router.md: read_ok
    codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
    codex_log/framework_adapter/20260614_goal_mode_sandbox_install_completion.md: read_ok
    codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
    codex_log/framework_adapter/20260614_uv_install_and_sandbox_dependency_probe.md: read_ok
  sandbox_upstream（沙盒上游项目）:
    README.md: read_ok
    pyproject.toml: read_ok
    uv.lock: read_ok_partial
    docs/RAG_Assistant.md: read_ok
    scripts/create_chroma_db.py: read_ok
    src/agents/agents.py: read_ok
    src/agents/rag_assistant.py: read_ok
    src/agents/tools.py: read_ok
    src/agents/safeguard.py: read_ok
    src/service/service.py: read_ok
    src/client/client.py: read_ok
    src/core/settings.py: read_ok
    src/core/llm.py: read_ok
    src/schema/schema.py: read_ok
    src/agents/: read_ok_by_find_and_ast_probe
    tests/: read_ok_by_find_and_pytest_collect_only
  skills_used（使用技能）:
    langchain-architecture: read_ok
    rag-implementation: read_ok
    data-quality-frameworks: read_ok
  memory_context（记忆上下文）: read_ok
  missing_files（缺失文件）: []
```

## 3. sandbox_install_ready_check（沙盒安装就绪检查）

```yaml
sandbox_install_ready_check（沙盒安装就绪检查）:
  sandbox_path（沙盒路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  sandbox_path_exists（沙盒路径存在）: true
  inside_main_repo（是否在主仓库内）: false
  pyproject_exists（pyproject 是否存在）: true
  uv_lock_exists（uv.lock 是否存在）: true
  venv_exists（.venv 是否存在）: true
  uv_available_by_absolute_path（uv 绝对路径可用）: true
  uv_path（uv 路径）: /Users/fan/.local/bin/uv
  current_shell_uv_on_path（当前 shell PATH 是否直接找到 uv）: false
  uv_pip_check（uv 依赖一致性检查）: passed_checked_241_packages
  compileall_src（src 编译）: passed
  minimal_import_probe（最小导入探测）: passed
  pytest_collect_only（pytest 收集探测）: passed_128_tests_collected
  sandbox_install_ready（沙盒安装是否就绪）: true
```

最小导入结果：

```yaml
minimal_import_probe（最小导入探测）:
  schema_import（schema 导入）: passed
  client_import（client 导入）: passed
  service_import（service 导入）: passed
  rag_tools_import（RAG 工具导入）: passed
  agents_registry_import（agents 注册表导入）: passed
  rag_assistant_graph_import（RAG 智能体图导入）: passed
  settings_import（设置层导入）: passed
  llm_provider_layer_import（LLM provider 层导入）: passed
  fake_env_written_to_file（是否把假环境变量写入文件）: false
  external_api_call（是否调用外部 API）: false
```

pytest collect-only 结果：

```yaml
pytest_collect_only（pytest 收集探测）:
  command（命令）: uv run pytest --collect-only -q
  success（是否成功）: true
  tests_collected（收集测试数）: 128
  tests_executed（是否执行测试主体）: false
  warnings（警告）:
    - langgraph_supervisor 内部 create_react_agent 弃用警告
    - tests/service/test_service.py 从 langgraph.pregel.types 导入 StateSnapshot 弃用警告
    - tests/agents/test_lazy_agent.py 中带 __init__ 的 helper class 不作为 test class 收集
```

## 4. langgraph_structure_audit（LangGraph 结构审计）

```yaml
langgraph_structure_audit（LangGraph 结构审计）:
  conclusion（结论）: LangGraph 是上游项目的主编排层 / workflow runtime layer。
  registry_path（注册表路径）: src/agents/agents.py
  default_agent（默认智能体）: research-assistant
  graph_type_alias（图类型别名）:
    AgentGraph: CompiledStateGraph | Pregel
    AgentGraphLike: CompiledStateGraph | Pregel | LazyLoadingAgent
  registry_agents（注册智能体）:
    - chatbot
    - research-assistant
    - rag-assistant
    - command-agent
    - bg-task-agent
    - langgraph-supervisor-agent
    - langgraph-supervisor-hierarchy-agent
    - interrupt-agent
    - knowledge-base-agent
    - github-mcp-agent
  runtime_features_found（发现的运行时特征）:
    - StateGraph / CompiledStateGraph
    - Pregel entrypoint function
    - ToolNode
    - Command branch / resume
    - interrupt
    - checkpointer / store injection in service lifespan
    - supervisor / nested supervisor graphs
    - deferred GitHub MCP agent loading
  langgraph_probe_done（LangGraph 探测完成）: true
```

静态取图结果：

| agent | graph type | core nodes | probe note |
| --- | --- | --- | --- |
| `chatbot` | `Pregel` | `chatbot` | `@entrypoint()` 函数图，可作为最小单节点示例。 |
| `research-assistant` | `CompiledStateGraph` | `guard_input`, `model`, `tools`, `block_unsafe_content` | 与 RAG agent 同结构，工具为 web search + calculator。 |
| `rag-assistant` | `CompiledStateGraph` | `guard_input`, `model`, `tools`, `block_unsafe_content` | RAG 主候选；工具节点绑定 `database_search`。 |
| `command-agent` | `CompiledStateGraph` | `node_a`, `node_b`, `node_c` | 展示 `Command` 动态路由能力。 |
| `bg-task-agent` | `CompiledStateGraph` | `bg_task`, `model` | 展示后台任务节点与模型节点串联。 |
| `langgraph-supervisor-agent` | `CompiledStateGraph` | `supervisor:*`, `sub-agent-research_expert:*`, `sub-agent-math_expert:*` | 多 agent supervisor 示例，可学习但不宜直接进入视频工厂主线。 |
| `langgraph-supervisor-hierarchy-agent` | `CompiledStateGraph` | nested supervisor + nested sub-agent | 嵌套 supervisor 示例，适合后续机制验证，不适合首轮闭环。 |
| `interrupt-agent` | `CompiledStateGraph` | `background`, `determine_birthdate`, `generate_response` | 展示人工中断 / 信息补齐位置。 |
| `knowledge-base-agent` | `CompiledStateGraph` | `retrieve_documents`, `prepare_augmented_prompt`, `model` | Amazon Bedrock Knowledge Base RAG 示例，不作为当前默认检索。 |
| `github-mcp-agent` | deferred wrapper | skipped | 未加载 deferred agent；本轮禁止 GitHub MCP 外部连接。 |

视频工厂接入判断：

```yaml
video_factory_langgraph_fit（视频工厂 LangGraph 适配判断）:
  keep_as_orchestration_layer（保留为编排层）: true
  preferred_first_agent_for_probe（首轮优先探测 agent）: rag-assistant
  human_review_interrupt_reference（人工复审中断参考）: interrupt-agent
  multi_agent_reference（多智能体参考）:
    - langgraph-supervisor-agent
    - langgraph-supervisor-hierarchy-agent
  disabled_by_default（默认禁用）:
    - github-mcp-agent
    - knowledge-base-agent
    - streamlit app
  not_runtime_enabled（未启用正式 runtime）: true
```

## 5. langchain_position_fit_audit（LangChain 定位适配审计）

```yaml
langchain_position_fit_audit（LangChain 定位适配审计）:
  conclusion（结论）: LangChain 在上游项目里主要是模型 / 工具 / retriever / loader / document 适配层，不应替代视频工厂的状态总控和闭环机制。
  upstream_langchain_positions（上游 LangChain 位置）:
    model_provider_layer（模型供应商层）: src/core/llm.py
    tool_layer（工具层）: src/agents/tools.py
    retriever_layer（检索器层）:
      - src/agents/tools.py
      - src/agents/knowledge_base_agent.py
    loader_layer（加载器层）: scripts/create_chroma_db.py
    runnable_layer（Runnable 层）:
      - src/agents/rag_assistant.py
      - src/agents/research_assistant.py
      - src/agents/bg_task_agent/bg_task_agent.py
  video_factory_fit（视频工厂适配定位）:
    keep_langgraph_for_workflow（用 LangGraph 承接流程编排）: true
    keep_langchain_for_integrations（用 LangChain 承接适配器）: true
    do_not_use_langchain_as_state_router（不让 LangChain 替代状态路由器）: true
    do_not_use_langchain_as_completion_proof（不把 LangChain 输出当完成证明）: true
```

建议分层：

```yaml
recommended_layering（推荐分层）:
  project_router_layer（项目状态路由层）: video_factory existing mechanism
  workflow_runtime_layer（工作流运行层）: LangGraph
  adapter_layer（模型/工具/检索适配层）: LangChain
  retrieval_store_layer（向量库层）:
    current_project（当前项目）: DashVector
    upstream_sandbox（上游 sandbox）: Chroma
  truth_check_layer（真实性检查层）: source_readback + human_review + completion_truth_check
```

## 6. rag_mechanism_probe（RAG 机制探测）

```yaml
rag_mechanism_probe（RAG 机制探测）:
  upstream_rag_agent（上游 RAG agent）: src/agents/rag_assistant.py
  upstream_rag_tool（上游 RAG 工具）: src/agents/tools.py
  upstream_ingestion_script（上游入库脚本）: scripts/create_chroma_db.py
  upstream_rag_docs（上游 RAG 文档）: docs/RAG_Assistant.md
  vector_store（向量库）: Chroma
  vector_store_path（向量库路径）: ./chroma_db
  embedding_provider（向量模型）: OpenAIEmbeddings
  runtime_retriever_k（运行时检索数量）: 5
  ingestion_probe_retriever_k（入库脚本示例检索数量）: 3
  supported_ingestion_file_types（入库脚本支持文件类型）:
    - pdf
    - docx
  loader_used（加载器）:
    pdf: PyPDFLoader
    docx: Docx2txtLoader
  splitter_used（切分器）: RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
  tool_output_format（工具输出格式）: concatenated_page_content_only
  metadata_preserved_in_model_context（metadata 是否保留进模型上下文）: false
  source_readback_required（是否必须补原文回读）: true
  retrieval_result_not_completion_proof（检索结果不是完成证明）: true
  rag_probe_done（RAG 探测完成）: true
```

无网络 metadata 格式化探测：

```yaml
metadata_format_probe（metadata 格式化探测）:
  tested_function（测试函数）: agents.tools.format_contexts
  input_documents（输入文档）: Document(page_content + source/page/chunk_id metadata)
  output_contains_page_content（输出包含正文片段）: true
  output_contains_source_metadata（输出包含 source metadata）: false
  conclusion（结论）: 当前上游工具把检索文档压成纯正文，丢弃 source/page/chunk_id；不满足视频工厂 source readback / retrieval manifest 要求。
```

视频工厂接入判断：

```yaml
video_factory_rag_fit（视频工厂 RAG 适配判断）:
  chroma_keep_in_sandbox（Chroma 在 sandbox 保留）: true
  dashvector_replace_for_project_runtime（项目 runtime 是否倾向 DashVector）: likely_yes_after_adapter_probe
  forced_replacement_now（是否本轮强制替换）: false
  missing_contracts（缺失契约）:
    - retrieval_manifest
    - source_readback
    - chunk_id / source_id / page_or_timecode metadata propagation
    - retrieval_gap_report
    - retrieval_result_truth_check
  first_safe_patch_direction（第一安全修补方向）: add_adapter_contract_before_replacing_vector_store
```

## 7. cleaning_layer_slot_design（清洗层位置设计）

```yaml
cleaning_layer_slot_design（清洗层位置设计）:
  upstream_cleaning_layer_status（上游清洗层状态）: basic_ingestion_only
  upstream_basic_ingestion（上游基础入库）: exists_in_scripts_create_chroma_db
  full_cleaning_layer_exists（是否已有完整清洗层）: false
  deduplication（去重）: missing
  chunk_quality_check（切片质量检查）: missing
  secret_scan_before_ingestion（入库前密钥扫描）: missing
  metadata_normalization（元数据标准化）: partial_or_missing
  source_readback（原文回读）: missing
  document_type_router（资料类型路由）: minimal_by_suffix_only
  cleaning_layer_slot_done（清洗层位置设计完成）: true
```

应补位置：

```yaml
video_factory_cleaning_adapter（视频工厂清洗适配层）:
  position（位置）: before_vector_store_write_and_before_retriever_runtime
  input（输入）:
    - local source file
    - source manifest
    - document type
    - project route
    - retrieval purpose
  required_steps（必需步骤）:
    - source_manifest_registration（源文件登记）
    - file_type_router（文件类型路由）
    - safe_loader_selection（安全加载器选择）
    - secret_scan_before_ingestion（入库前密钥扫描）
    - content_normalization（正文规范化）
    - metadata_standardization（元数据标准化）
    - deduplication（去重）
    - chunking_policy（切片策略）
    - chunk_quality_check（切片质量检查）
    - source_readback_index（原文回读索引）
    - retrieval_manifest_output（检索清单输出）
  output_to_retrieval（输出到检索层）:
    - normalized_documents
    - chunk_manifest
    - source_readback_map
    - ingestion_decision_report
  compatible_targets（兼容目标）:
    - Chroma sandbox
    - DashVector project runtime
  blocked_if（阻断条件）:
    - source file cannot be read safely
    - secret-like content detected before ingestion
    - chunk metadata cannot preserve source readback
    - document type requires unsupported parser
```

结论：

```yaml
cleaning_layer_gap_audit（清洗层缺口审计）:
  cleaning_layer_status（清洗层状态）: basic_ingestion_only
  conclusion（结论）: 上游项目已有基础入库脚本，但没有足够的清洗 / 去重 / 元数据 / source readback / secret scan 契约；接入视频工厂前必须补 `video_factory_cleaning_adapter`。
```

## 8. video_factory_integration_shape_simulation（视频工厂接入形态模拟）

```yaml
video_factory_integration_shape_simulation（视频工厂接入形态模拟）:
  integration_goal（接入目标）: 把上游框架作为可控 agent service / workflow runtime 候选，而不是直接改写视频工厂主机制。
  first_shape（第一形态）: sandbox_runtime_probe_only
  second_shape（第二形态）: isolated_adapter_package_inside_main_repo_after_authorization
  third_shape（第三形态）: video_factory_agent_service_contract
  fourth_shape（第四形态）: closed_loop_probe_before_runtime_enable
```

推荐结构形态：

```yaml
recommended_integration_shape（推荐接入形态）:
  video_factory_router（视频工厂路由层）:
    role（角色）: 判断任务状态、检索需求、DeepSeek 是否触发、写入执行器边界。
    source（来源）: existing codex_source / GPT数据源 mechanisms
  graph_runtime_adapter（图运行适配层）:
    role（角色）: 封装 LangGraph agent 的 invoke/stream/interrupt/checkpointer/store。
    upstream_reference（上游参考）:
      - src/agents/agents.py
      - src/service/service.py
  retrieval_adapter（检索适配层）:
    role（角色）: 统一 Chroma sandbox 与 DashVector project runtime 的检索输入输出。
    required_contracts（必需契约）:
      - retrieval_manifest
      - source_readback_map
      - gap_report
  cleaning_adapter（清洗适配层）:
    role（角色）: 在入库前补齐清洗、去重、metadata、secret scan、source readback。
  write_executor_adapter（写入执行器适配层）:
    role（角色）: 把 Codex / Trae / future_ide_agent 抽象为 active_write_executor。
  human_review_gate（人工复审闸门）:
    role（角色）: 对应 LangGraph interrupt，但最终以视频工厂机制文件为准。
```

最小闭环模拟不做视频、不调用外部 API：

```yaml
minimal_closed_loop_shape（最小闭环形态）:
  input_task（输入任务）: 文本规则一致性检查任务
  route_decision（路由判断）: video_factory mechanism route
  cleaning_adapter（清洗适配）: manifest + metadata + source readback map
  retrieval_adapter（检索适配）: Chroma sandbox or DashVector adapter stub
  rag_agent（RAG agent）: rag-assistant graph as reference
  human_review_interrupt（人工复审中断）: interrupt-agent pattern as reference
  executor_handoff（执行器交接）: active_write_executor contract
  completion_truth_check（完成真实性检查）: source readback + no forbidden status promotion
  output_report（输出报告）: probe report only
```

## 9. future_patch_plan（后续修补计划）

本轮未直接修改正式机制文件。后续若用户授权正式 patch，建议按以下顺序推进：

```yaml
future_patch_plan（后续修补计划）:
  phase_1_contract_first（第一阶段：契约先行）:
    - define graph_runtime_adapter contract
    - define retrieval_manifest schema
    - define source_readback_map schema
    - define cleaning_adapter input/output schema
    - define active_write_executor handoff schema
  phase_2_no_service_probe（第二阶段：无服务探测）:
    - import selected graph
    - inspect graph nodes/edges
    - run fake model invoke on non-RAG or patched fake retriever path
    - produce completion_truth_check report
  phase_3_retrieval_adapter_probe（第三阶段：检索适配探测）:
    - keep Chroma sandbox as upstream baseline
    - add DashVector adapter candidate behind same interface
    - compare retrieval_manifest and source_readback behavior
  phase_4_cleaning_adapter_probe（第四阶段：清洗适配探测）:
    - run against small non-secret local fixture
    - verify metadata / dedup / chunk quality / source readback
  phase_5_service_contract_probe（第五阶段：服务契约探测）:
    - inspect FastAPI service without starting server first
    - only start sandbox service after explicit authorization
  blocked_if（阻断条件）:
    - requires real API key
    - requires Chroma ingestion against real files without secret scan
    - requires Docker / Postgres / Streamlit / FastAPI service start without authorization
    - requires main repo dependency edit
    - cannot preserve source readback
```

可能需要后续修补的正式文件范围必须另行授权，不在本轮执行：

```yaml
files_likely_need_patch_later（后续可能要修补的文件）:
  - codex_source/schema_contracts/*
  - codex_source/19_project_state_action_router.md
  - codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md
  - future adapter package path inside main repo after user approval
patch_boundary（修补边界）: 本轮只写报告和 latest；正式机制文件不改。
```

## 10. disabled_services_check（禁用服务检查）

```yaml
disabled_services_check（禁用服务检查）:
  streamlit_started（Streamlit 是否启动）: false
  docker_started（Docker 是否启动）: false
  postgres_started（Postgres 是否启动）: false
  service_server_started（FastAPI 服务是否启动）: false
  chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
  external_api_called（是否调用外部 API）: false
  github_mcp_loaded（GitHub MCP 是否加载）: false
  langsmith_or_langfuse_started（LangSmith/Langfuse 是否启用）: false
```

## 11. main_repo_pollution_check（主仓库污染检查）

```yaml
main_repo_pollution_check（主仓库污染检查）:
  install_executed_in_main_repo（是否在主仓库安装）: false
  main_repo_dependency_modified（主仓库依赖是否被修改）: false
  external_code_copied_to_main（是否复制外部代码到主线）: false
  external_code_tracked_in_main（外部代码是否被主仓库跟踪）: false
  env_or_secret_written（是否写入 env 或 secret）: false
  forbidden_paths_modified（是否修改禁止路径）: false
  unrelated_untracked_public（无关未跟踪 public）: present_but_not_staged
```

## 12. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  sandbox_install_ready（沙盒安装就绪）: true
  compile_probe_done（编译探测完成）: true
  compile_probe_passed（编译探测通过）: true
  uv_pip_check_done（依赖一致性检查完成）: true
  uv_pip_check_passed（依赖一致性检查通过）: true
  minimal_import_probe_done（最小导入探测完成）: true
  minimal_import_probe_passed（最小导入探测通过）: true
  langgraph_probe_done（LangGraph 探测完成）: true
  langchain_position_audit_done（LangChain 定位审计完成）: true
  rag_probe_done（RAG 探测完成）: true
  cleaning_layer_slot_done（清洗层位置设计完成）: true
  pytest_collect_only_done（pytest collect-only 完成）: true
  pytest_collect_only_passed（pytest collect-only 通过）: true
  no_main_repo_dependency_modified（主仓库依赖未修改）: true
  no_external_code_tracked_in_main（外部代码未被主仓库跟踪）: true
  no_env_or_secret_written（未写入 env 或 secret）: true
  no_frontend_started（未启动前端）: true
  no_docker_started（未启动 Docker）: true
  no_postgres_started（未启动 Postgres）: true
  no_fastapi_service_started（未启动 FastAPI 服务）: true
  no_chroma_ingestion_run（未运行 Chroma 入库）: true
  no_formal_runtime_enabled（未启用正式运行时）: true
  no_formal_mechanism_patch_applied（未直接修改正式机制）: true
  git_diff_check（Git diff 格式检查）: passed
  path_limited_diff_review（限定路径 diff 复核）: passed_allowed_files_only
  forbidden_path_scan（禁止路径扫描）: passed_except_unrelated_untracked_public_not_staged
  secret_like_pattern_scan_added_lines（本轮新增行密钥模式扫描）: passed
  forbidden_status_promotion_scan_added_lines（本轮新增行禁止状态推进扫描）: passed
  disabled_service_process_scan（禁用服务进程扫描）: passed
```

提交前还需复核 staged diff 只包含本轮允许文件。

## 13. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - 未执行真实 agent invoke；本轮只做导入、编译、静态图结构和无网络函数探测。
  - 未启动 FastAPI service，因此未验证 HTTP contract。
  - 未运行 Chroma 入库脚本，因此未验证真实 Chroma DB 读写。
  - 未接 DashVector adapter，只完成 Chroma 与 DashVector 并存/替换边界判断。
  - 未做真实 LLM / Groq / OpenAI / LangSmith / Langfuse / GitHub MCP 调用。
  - 当前上游 RAG 未保留 source metadata 到模型上下文，必须补 retrieval_manifest 和 source_readback。
  - 当前上游 cleaning layer 只是基础入库，必须补视频工厂清洗适配层。
```

## 14. blocked_if_any（如有阻断）

```yaml
blocked_if_any（如有阻断）: null
```

## 15. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: sandbox_fake_model_no_service_graph_invoke_probe_after_user_confirmation
```

下一步建议仍保持 sandbox / fake model / no-service 边界，先做一个不依赖真实 API 的 `rag-assistant` 或最小 graph invoke 探测，并同时验证 retrieval manifest / source readback 的 adapter contract。
