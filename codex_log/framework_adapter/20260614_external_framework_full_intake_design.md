# 20260614 External Framework Full Intake Design

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - external_framework_full_intake_install_plan（外部框架完整接入安装计划）
  - sandbox_install_probe_design（沙盒安装探测设计）
  - executor_abstraction_repair_plan（执行器抽象修正方案）
  - retrieval_coexistence_design（检索机制并存设计）
  - cleaning_layer_gap_audit（清洗层缺口审计）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
responsibility_layer（责任层级）:
  - project_judgment_layer（项目判断层）
  - mechanism_fix_layer（机制修补层）
  - validation_layer（验收复审层）
  - sync_layer（同步回写层）
large_task_gate（大任务闸门）:
  triggered（是否触发）: true
  lane_recommendation（执行车道建议）: audit_lane_to_standard_lane
  parallel_recommendation（并发建议）: read_parallel_for_audit_serial_only_for_writes
execution_permission（执行权限）: design_report_and_latest_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
install_executed（是否已安装）: false
sandbox_created（是否创建沙盒）: false
runtime_enabled（是否启用运行时）: false
external_code_copied（是否复制外部代码）: false
frontend_started（是否启动前端）: false
```

本轮只完成设计层报告和 `latest.md` 更新，不安装依赖、不创建 sandbox、不复制上游代码、不启用 runtime、不创建 minimal router prototype。

## 2. files_read（已读取文件）

### 2.1 current_repo_readback（当前仓库回读）

```yaml
current_repo_read_status（当前仓库读取状态）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/01_execution_rules.md: read_ok
  codex_source/13_execution_lane_and_parallel_rules.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
  codex_source/schema_contracts/00_schema_contracts_index.md: read_ok
  project_source/20_codex_multi_agent_routing_note_for_gpt_project.md: read_ok
  codex_log/framework_adapter/20260613_agent_service_toolkit_full_intake_design.md: read_ok
  codex_log/framework_adapter/20260613_deepseek_positioning_for_rag_first_adapter.md: read_ok
  codex_log/framework_adapter/20260613_write_executor_abstraction_plan.md: read_ok
  codex_log/framework_adapter/20260614_schema_contract_fix_plan.md: read_ok
  codex_log/framework_adapter/20260614_schema_contract_static_validation.md: read_ok
missing_files（缺失文件）: []
```

`codex_log/latest.md` 顶部已确认：

```yaml
static_validation（静态验证）: passed
install_preflight_ready（安装前准入）: true
next_safe_step（下一步安全动作）: sandbox_intake_no_write_prompt
runtime_enabled（运行时启用）: false
sandbox_created（沙盒创建）: false
minimal_router_prototype_created（最小路由原型创建）: false
dependency_installed（依赖安装）: false
external_code_copied（外部代码复制）: false
```

### 2.2 upstream_read_status（上游读取状态）

```yaml
upstream_repo（上游仓库）: JoshuaC215/agent-service-toolkit
repo_url（仓库地址）: https://github.com/JoshuaC215/agent-service-toolkit
upstream_read_status（上游读取状态）: read_ok_with_api_tree_fallback
api_tree_status（GitHub API tree 状态）: partial_403
fallback_used（是否使用兜底）: codeload_tarball_stream_and_raw_github_urls
external_code_persisted（是否持久化外部代码）: false
not_verified（未验证项）:
  - runtime_startup（运行时启动）
  - dependency_resolution（依赖解析）
  - docker_startup（Docker 启动）
  - chroma_db_runtime_creation（Chroma DB 运行时创建）
```

上游必读文件 / 目录只读回读：

```yaml
README.md: read_ok
pyproject.toml: read_ok
compose.yaml: read_ok
docs/RAG_Assistant.md: read_ok
scripts/create_chroma_db.py: read_ok
src/agents/tools.py: read_ok
src/agents/rag_assistant.py: read_ok
src/agents/safeguard.py: read_ok
src/schema/schema.py: read_ok
src/service/service.py: read_ok
src/client/client.py: read_ok
src/agents/: read_ok_via_tarball_listing_and_key_files
src/core/: read_ok_via_settings_and_llm_files
docker/: read_ok_via_Dockerfile.service_and_Dockerfile.app
tests/: read_ok_via_tarball_listing_and_selected_service_client_tests
```

上游读取来源：

- `https://github.com/JoshuaC215/agent-service-toolkit`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/README.md`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/pyproject.toml`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/compose.yaml`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/docs/RAG_Assistant.md`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/scripts/create_chroma_db.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/agents/tools.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/agents/rag_assistant.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/agents/safeguard.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/schema/schema.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/service/service.py`
- `https://raw.githubusercontent.com/JoshuaC215/agent-service-toolkit/main/src/client/client.py`
- `https://codeload.github.com/JoshuaC215/agent-service-toolkit/tar.gz/refs/heads/main`

## 3. upstream_project_map（上游项目地图）

| layer（层） | upstream_path（上游路径） | upstream_function（上游职责） | video_factory_need（视频工厂是否需要） | intake_advice（接入建议） |
|---|---|---|---|---|
| service_layer（服务层） | `src/service/service.py` | FastAPI app；`/info`、`/invoke`、`/stream`、`/feedback`、`/history`、`/health`；支持 bearer auth、interrupt resume、SSE streaming、LangSmith feedback。 | 需要，但只作为 adapter service shell。 | `keep + adapt`；只允许 route / retrieve / validate / interrupt / handoff；不得直接写仓库。 |
| agent_layer（智能体层） | `src/agents/`、`src/agents/agents.py` | 多 agent registry；LangGraph agents；RAG、research、GitHub MCP、interrupt、supervisor 示例。 | 需要完整学习，但正式接入要收窄。 | `keep + adapt`；优先映射为 video_factory workflow routers；GitHub MCP agent 默认禁用。 |
| retrieval_layer（检索层） | `docs/RAG_Assistant.md`、`scripts/create_chroma_db.py`、`src/agents/tools.py`、`src/agents/rag_assistant.py` | Chroma + OpenAIEmbeddings + PDF/DOCX loader + RecursiveCharacterTextSplitter；RAG assistant 使用 database_search tool。 | 需要并存评估。 | `coexist_then_decide`；Chroma 保留为 sandbox 学习对象，DashVector 仍是当前项目主检索路线。 |
| memory_layer（记忆层） | `src/memory/`、`compose.yaml` postgres、`src/service/service.py` lifespan | SQLite checkpointer、Postgres saver/store、Mongo saver、InMemoryStore；thread/user persistence。 | 部分需要。 | 第一阶段禁用 Postgres/Mongo；只允许 sandbox 内 SQLite/InMemory；不得替代 repo facts 或 DashVector。 |
| client_layer（客户端层） | `src/client/client.py` | 同步/异步 invoke、stream、feedback、history client；支持 `AUTH_SECRET` bearer header。 | 需要。 | `keep + adapt`；作为 no-write closed loop probe client。 |
| frontend_layer（前端层） | `src/streamlit_app.py`、`docker/Dockerfile.app`、`compose.yaml` `streamlit_app` | Streamlit chat UI、voice input/output、client app。 | 当前不需要。 | `disable_by_default`；本轮不删除，未来闭环稳定且确认无人工控制台价值后再 prune。 |
| docker_layer（Docker 层） | `compose.yaml`、`docker/Dockerfile.service`、`docker/Dockerfile.app` | Postgres + agent_service + streamlit_app；Dockerfile 使用 `uv sync`。 | 只在未来 sandbox 需要。 | 本轮禁用；未来若用户授权，先只启动 service 或 mock/service，默认不启动 Streamlit。 |
| test_layer（测试层） | `tests/` | service、client、agent、voice、Docker e2e、settings 等测试。 | 需要。 | `keep + adapt`；优先复用 service/client contract 测试形状，补 video_factory schema/fixture tests。 |
| cleaning_layer（清洗层） | `scripts/create_chroma_db.py` | PDF/DOCX 基础读取、chunk、写入 Chroma。 | 当前不足。 | `basic_ingestion_only`；必须补 `video_factory_cleaning_adapter`。 |

## 4. full_intake_plan（完整接入计划）

```yaml
full_intake_plan（完整接入计划）:
  intake_goal（接入目标）: 将 agent-service-toolkit 作为完整外部框架进入视频工厂 adapter 设计，保留完整性，先禁用不适用模块，再以闭环效果决定替换或删除。
  intake_mode（接入模式）: full_intake_first_then_disable_or_prune
  preserve_integrity_rule（保留完整性规则）:
    - 先完整理解 service / agent / retrieval / memory / client / frontend / docker / tests / cleaning 层。
    - 第一阶段不拆碎上游，不直接删除 Streamlit、Chroma、Postgres、GitHub MCP 等模块。
    - 不适配视频工厂当前闭环的模块先 `disable_by_default`，不写成废弃。
  no_direct_main_pollution_rule（不污染主仓库规则）:
    - 不在 `/Users/fan/Documents/视频工厂` 主环境安装上游依赖。
    - 不修改当前 `pyproject.toml / compose.yaml / package.json / .env*`。
    - 不把上游 sample code 复制进 tracked files。
    - 不把 sandbox 成功写成视频工厂 runtime 已跑通。
  phase_1（第一阶段）: readonly_intake（只读完整理解）
  phase_2（第二阶段）: sandbox_install（用户另行确认后，隔离目录安装探测）
  phase_3（第三阶段）: minimal_closed_loop_probe（只用文本/规则任务做 no-write 闭环）
  phase_4（第四阶段）: adapt_replace_disable（按闭环证据决定适配、替换或继续禁用）
  phase_5（第五阶段）: prune_after_verified（确认长期无用且不破坏闭环后再删除）
```

阶段准入：

| phase（阶段） | allowed（允许） | forbidden（禁止） | exit_evidence（退出证据） |
|---|---|---|---|
| Phase 1 readonly_intake | 只读分析上游和当前仓库；写设计报告。 | 安装、复制代码、runtime、sandbox、prototype。 | 本报告 + latest 同步 + Git readback。 |
| Phase 2 sandbox_install | 用户确认后，在隔离目录安装；只用 fake/mock 或显式授权密钥。 | 主仓库安装、tracked code copy、Streamlit 默认启动、真实状态写入。 | dependency lock readback、service health 或 blocked report。 |
| Phase 3 minimal_closed_loop_probe | 文本/规则任务；route -> retrieval manifest -> source readback -> handoff。 | 视频任务、外部 API、真实业务状态推进。 | structured probe report；no-write handoff 可读。 |
| Phase 4 adapt_replace_disable | 逐项适配 DashVector、schema、write_executor、human interrupt。 | 未经证据直接 prune；让 runtime 写仓库。 | Codex 执行器闭环一次成功。 |
| Phase 5 prune_after_verified | 删除长期无用模块。 | 删除仍在闭环或测试中有价值的模块。 | prune impact report + regression tests。 |

## 5. sandbox_install_scope（沙盒安装范围）

```yaml
sandbox_install_scope（沙盒安装范围）:
  sandbox_location_recommendation（沙盒位置建议）:
    preferred（首选）: /Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/agent_service_toolkit_sandbox/
    reason（原因）: 遵守单工作区规则，避免在 Documents 顶层新建外部散工作区；sandbox 必须加入本地 exclude，不得作为 tracked source。
  install_method_options（安装方式候选）:
    - uv_sync
    - docker_compose
    - local_venv
  recommended_first_install_method（推荐首选安装方式）: uv_sync
  recommended_reason（推荐原因）: 上游原生使用 `uv sync --frozen`；比 Docker 更少服务面，能先验证 Python/FastAPI/LangGraph 基础，不默认启动 Postgres 或 Streamlit。
  env_required（需要的环境变量）:
    minimal_no_external_api_probe（最小无外部 API 探测）:
      - USE_FAKE_MODEL=true
      - DATABASE_TYPE=sqlite
      - SQLITE_DB_PATH=<sandbox-local-checkpoints.db>
    service_auth_optional（服务鉴权可选）:
      - AUTH_SECRET=<local-only-secret-if-needed>
    rag_runtime_only_if_authorized（仅 RAG 运行时探测且获授权时）:
      - OPENAI_API_KEY=<never_commit>
    disabled_by_default（默认禁用）:
      - GITHUB_PAT
      - LANGCHAIN_API_KEY
      - LANGFUSE_PUBLIC_KEY
      - LANGFUSE_SECRET_KEY
      - POSTGRES_PASSWORD
  secrets_policy（密钥策略）:
    - 不复制上游 `.env.example` 为 tracked `.env`。
    - 不把真实 key 写入 Git。
    - 优先使用 `USE_FAKE_MODEL=true` 做服务闭环探测。
    - 需要真实 embedding / LLM / GitHub MCP 时另起用户授权任务。
  docker_services_to_start（建议启动的 Docker 服务）:
    first_probe（第一轮）: []
    later_if_authorized（后续如授权）:
      - agent_service
      - postgres
  docker_services_disabled_by_default（默认禁用的 Docker 服务）:
    - streamlit_app
  frontend_disabled（前端默认禁用）: true
  forbidden_in_sandbox_probe（沙盒探测禁止项）:
    - 不在视频工厂主仓库根目录运行 `uv sync`。
    - 不运行 `docker compose watch` 作为第一轮。
    - 不启动 Streamlit。
    - 不启用 GitHub MCP write tools。
    - 不把 sandbox runtime 输出写成项目正式状态。
    - 不推进 `runtime_enabled / sandbox_created / minimal_router_prototype_created`，除非该轮明确授权并完成验证。
```

本轮 sandbox 状态：

```yaml
install_preflight_ready（安装前准入已就绪）: true
install_authorized（已授权安装）: false
sandbox_created（是否创建 sandbox）: false
runtime_enabled（是否启用 runtime）: false
```

## 6. module_keep_disable_prune_matrix（模块保留 / 禁用 / 删除矩阵）

| module_name（模块名） | upstream_path（上游路径） | upstream_function（上游功能） | intake_decision（接入判断） | decision_reason_cn（中文原因） | video_factory_role（视频工厂角色） | risk（风险） | first_probe（第一轮探测） | delete_allowed_later（后续是否允许删除） |
|---|---|---|---|---|---|---|---|---|
| LangGraph Agent（LangGraph 智能体） | `src/agents/*`、`src/agents/agents.py` | 多 agent graph、registry、interrupt、supervisor、RAG/GitHub 示例。 | adapt | 图式流程和 interrupt 很适合视频工厂 route/retrieve/readback/block/handoff，但不能直接写仓库。 | workflow router + validation graph + human interrupt。 | 节点权限过大时绕过 write_executor。 | 用 fake model 跑一个文本规则任务，输出 handoff，不写文件。 | false，核心框架不删。 |
| FastAPI Service（FastAPI 服务） | `src/service/service.py` | `/info`、`/invoke`、`/stream`、`/feedback`、`/history`、`/health` 服务壳。 | keep | 是上游完整服务边界，可作为 sandbox adapter shell。 | no-write adapter service。 | service 接入外部 tracing/auth/history 后扩大秘密和状态面。 | `/info` + one `/invoke` fake-model no-write probe。 | false，除非未来完全不用服务化。 |
| Streamlit App（Streamlit 前端） | `src/streamlit_app.py`、`docker/Dockerfile.app`、`compose.yaml` `streamlit_app` | Web chat UI + voice client。 | disable | 用户当前不需要网页前端，但完整 intake 阶段不删除。 | 暂无；未来可作为人工复审 console 候选。 | 启动 UI 会引入无关端口、voice、client 状态和误验收。 | 不启动；仅保留文件结构记录。 | true，闭环稳定且确认无人工 console 价值后可删。 |
| Client（客户端） | `src/client/client.py` | sync/async invoke、stream、feedback、history。 | keep | 可作为 closed loop probe 的调用器和 contract test 形状。 | probe client / future CLI bridge。 | 默认 base_url、AUTH_SECRET、stream 解析需适配本地规则。 | mock service 或 fake service 的 invoke/stream contract test。 | false。 |
| Chroma RAG（Chroma 检索增强） | `docs/RAG_Assistant.md`、`scripts/create_chroma_db.py`、`src/agents/tools.py`、`src/agents/rag_assistant.py` | Chroma vector store、OpenAIEmbeddings、PDF/DOCX ingestion、database_search tool。 | adapt | 用户要求并存评估，不强制改成 DashVector；Chroma 可做 sandbox 学习对象。 | upstream RAG reference / sandbox comparison module。 | 需要 OpenAI key；无 source readback；不能作为视频工厂事实源。 | 静态 fixture 模拟 Chroma output，再和 DashVector manifest 字段对齐。 | true，DashVector adapter 证明后可删除或保留为 sample。 |
| DashVector Adapter（DashVector 适配） | upstream: not_present；current project: DashVector RAG reports/schema contracts | 上游没有阿里 DashVector adapter。 | adapt | 当前项目已接 DashVector，必须新建 project-owned adapter，而不是让 Chroma 覆盖现有机制。 | formal retrieval/cache layer。 | 维度、embedding、collection、source readback 不一致会导致假召回。 | 不调用真实 DashVector；先用 fixture 验证 manifest/source_readback contract。 | false。 |
| Postgres / Checkpoint（数据库 / 检查点） | `compose.yaml` postgres、`src/memory/postgres.py` | LangGraph checkpointer/store persistence。 | disable | 第一轮闭环不需要数据库服务；项目事实仍在 Git/repo/log。 | future thread state / runtime state only。 | Postgres 容器和 secret 扩大运行面；可能被误当长期事实库。 | 不启动；只读 schema/config。 | true，若 SQLite/InMemory 足够可长期禁用。 |
| Memory Store（记忆存储） | `src/memory/sqlite.py`、`src/memory/__init__.py` | SQLite saver + InMemoryStore；Postgres/Mongo optional。 | adapt | 可保存 runtime thread state，但不能取代仓库事实或 DashVector。 | ephemeral runtime memory / interrupt resume。 | memory drift；把 runtime state 写成 project fact。 | SQLite/InMemory fake-model task only。 | false，保留但限权。 |
| Safeguard（安全拦截） | `src/agents/safeguard.py` | Prompt injection detection via Groq model；未设 `GROQ_API_KEY` 时跳过。 | adapt | 可学习为 prompt injection / unsafe request gate，但第一轮不能依赖 Groq。 | optional pre-handoff safety gate。 | 需外部 API；skip 时可能被误认为已审查。 | 静态 input classifier contract；真实 Groq 调用禁用。 | true，若另有安全层可删。 |
| Schema / Pydantic（结构校验） | `src/schema/schema.py`、`src/schema/models.py` | UserInput、StreamInput、ChatMessage、ServiceMetadata、Feedback 等 API schema。 | keep | 与当前 schema_contracts 可对齐，用于 adapter contract。 | API contract / validation shell。 | 原 schema 面向聊天，不含视频工厂 route/readback/handoff 真值字段。 | 映射到 WorkflowRouteDecision / RetrievalManifest / WriteExecutorHandoff。 | false。 |
| Docker Compose（Docker 编排） | `compose.yaml`、`docker/Dockerfile.service`、`docker/Dockerfile.app` | Postgres + service + Streamlit；Dockerfile 用 uv sync。 | disable | 本轮和第一轮 probe 不需要 Docker；Docker 适合后续隔离。 | future sandbox runtime only。 | 默认启动 Streamlit/Postgres；`.env` 和端口暴露风险。 | 不运行；后续如授权只启动 service/postgres。 | true，若不走容器可删除本地适配层。 |
| Tests（测试） | `tests/` | service/client/agents/settings/voice/Docker tests。 | adapt | 测试结构可复用，是闭环证明必须项。 | schema/route/service/client regression tests。 | 原测试不覆盖视频工厂禁止状态、source readback、write_executor。 | 先加 no-write schema/service tests，后续再集成。 | false。 |
| Cleaning Layer（清洗层） | `scripts/create_chroma_db.py` | PDF/DOCX loader、splitter、Chroma write。 | blocked | 只有基础入库，不具备视频工厂所需清洗、去重、source readback、secret scan。 | 必须补 `video_factory_cleaning_adapter`。 | 未清洗资料会污染检索；secret/旧口径/重复 chunk 风险。 | 静态样本通过 cleaning adapter fixture，不写 Chroma/DashVector。 | false，先补齐再裁决。 |
| LangSmith / Feedback（反馈追踪） | `src/service/service.py` `/feedback`、settings LangSmith/Langfuse | Run feedback、tracing、observability。 | disable | 外部观测和反馈有价值，但当前不需要外部遥测。 | future diagnostics / human feedback trace。 | 需要外部 key；可能泄露任务内容。 | 禁用；只保留 schema 字段。 | true，若本地日志足够可删。 |

## 7. executor_abstraction_patch_plan（执行器抽象修补方案）

```yaml
executor_abstraction_patch_plan（执行器抽象修补方案）:
  current_problem（当前问题）:
    - codex 被旧口径写成唯一永久写入执行器。
    - 外部 runtime / agent service 如果未来接入，容易被误解为可以直接写文件、commit、push。
    - Trae 和未来 IDE Agent 没有正式 handoff / result contract。
  target_model（目标模型）:
    write_executor（写入执行器）:
      active_write_executor（当前激活执行器）: codex
      executor_type（执行器类型）:
        - codex
        - trae
        - future_ide_agent
      allowed_runtime_role（runtime 允许角色）:
        - route
        - retrieve
        - source_readback_request
        - validate
        - block
        - human_review_interrupt
        - write_executor_handoff
      forbidden_runtime_role（runtime 禁止角色）:
        - direct_file_write
        - commit
        - push
        - status_promotion
        - secret_read
  files_likely_need_patch（后续可能要修补的文件）:
    - AGENTS.md
    - GPT数据源/08_当前正式事实.md
    - GPT数据源/10_OPC一人公司闭环与多AI协作机制.md
    - GPT数据源/11_项目状态动作总控器_机制推理层.md
    - codex_source/00_codex_readme.md
    - codex_source/13_execution_lane_and_parallel_rules.md
    - codex_source/19_project_state_action_router.md
    - codex_source/schema_contracts/schemas/write_executor_handoff.schema.yaml
    - codex_source/schema_contracts/schemas/completion_truth_check.schema.yaml
  patch_boundary（修补边界）:
    - 本轮只输出 patch plan，不修改正式机制文件。
    - `active_write_executor = codex` 继续有效。
    - `trae / future_ide_agent` 只是 future_candidate，不启用、不授权、不验证。
    - 新 executor 必须先证明 allowed_files、forbidden_files、source_readback、validation、git sync、remote readback 全部可控。
  blocked_if（阻断条件）:
    - 外部 runtime 试图直接写仓库。
    - 新 executor 无法隔离 unrelated dirty files。
    - 新 executor 不能执行 path-limited stage / commit / push / remote readback。
    - human_review_interrupt 被自动跳过。
    - forbidden status 被推进。
```

## 8. retrieval_coexistence_plan（检索机制并存方案）

```yaml
retrieval_coexistence_plan（检索机制并存方案）:
  upstream_rag（上游 RAG）:
    vector_store（向量库）: Chroma
    embedding_provider（向量模型）: OpenAIEmbeddings
    loader（加载器）:
      - PyPDFLoader
      - Docx2txtLoader
    splitter（切分器）: RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
    retriever（检索器）:
      tools.py: Chroma.as_retriever(search_kwargs={"k": 5})
      create_chroma_db.py_probe: Chroma.as_retriever(search_kwargs={"k": 3})
  current_project_rag（当前项目检索）:
    vector_store（向量库）: DashVector
    source_of_truth（事实源）: GitHub / repo source readback
    vector_result_not_completion_proof（向量结果不是完成证明）: true
  coexist_policy（并存策略）:
    - Chroma 保留为 sandbox 学习和对照模块。
    - DashVector 保留为视频工厂正式检索 / 缓存层。
    - 两者输出都必须转换成统一 `RetrievalManifest`。
    - 检索命中必须再做 `SourceReadback`，不得直接作为事实或完成证明。
  replace_policy（替换策略）:
    - 只有 DashVector adapter 在 closed loop probe 中证明 query -> manifest -> readback -> handoff 稳定后，才考虑替换 Chroma formal path。
    - 只有确认 Chroma sample 对视频工厂长期无用，且 tests/schema 不依赖它时，才进入 prune。
  source_readback_required（是否必须原文回读）: true
  retrieval_result_not_completion_proof（检索结果不是完成证明）: true
  dashvector_adapter_needed（是否需要 DashVector 适配层）: true
```

统一检索输出建议：

```yaml
retrieval_manifest_item（检索清单条目）:
  retrieval_provider（检索提供者）: dashvector | chroma_sandbox | fixture_mock
  query（查询）:
  source_path（原文路径）:
  chunk_id（切片 ID）:
  content_hash（内容哈希）:
  commit_sha（提交 SHA）:
  authority_level（权威层级）:
  status_label（状态标签）:
  retrieval_score（召回分）:
  source_readback_required（必须原文回读）: true
  vector_result_not_completion_proof（向量结果不是完成证明）: true
```

## 9. cleaning_layer_gap_audit（清洗层缺口审计）

```yaml
cleaning_layer_gap_audit（清洗层缺口审计）:
  upstream_basic_ingestion（上游基础入库）: true
  supported_file_types（支持文件类型）:
    - pdf
    - docx
  loader_used（加载器）:
    - PyPDFLoader
    - Docx2txtLoader
  splitter_used（切分器）: RecursiveCharacterTextSplitter
  metadata_handling（元数据处理）: basic_loader_metadata_only
  deduplication（去重）: not_found
  chunk_quality_check（切片质量检查）: not_found
  secret_scan_before_ingestion（入库前密钥扫描）: not_found
  source_readback（原文回读）: not_found
  document_type_router（资料类型路由）: not_found
  conclusion（结论）: 上游已有基础 RAG 入库脚本，但没有视频工厂需要的完整清洗层。
  cleaning_layer_status（清洗层状态）: basic_ingestion_only
```

缺口说明：

- 上游会遍历 `folder_path`，只处理 `.pdf` / `.docx`，其余文件跳过。
- 上游用 OpenAI embeddings 写 Chroma，依赖 `OPENAI_API_KEY`。
- 未看到文件 allowlist / blacklist、旧口径降权、路径权威级、source priority、chunk hash 去重、secret-like scan、source readback proof、legacy source blocker、资料类型路由。
- 因此它不能直接接视频工厂资料库；必须先进入 `video_factory_cleaning_adapter`。

```yaml
video_factory_cleaning_adapter_plan（视频工厂清洗适配层方案）:
  purpose（用途）: 在任何 Chroma / DashVector 入库前，把视频工厂资料转成可追溯、可回读、可阻断的 clean document chunks。
  required_steps（必需步骤）:
    - intake_manifest（入库清单）: 记录 source_path / source_type / authority_level / project_route / status_label。
    - path_allowlist_blacklist（路径白黑名单）: 阻断 `.env*`、media、public、dist、cache、privatecredentials、旧口径隔离目录。
    - document_type_router（资料类型路由）: 区分 AGENTS、GPT数据源、codex_source、codex_log、review_loop、external_upstream。
    - secret_scan_before_ingestion（入库前密钥扫描）: 扫描 API key、token、private credential、local auth path。
    - normalization（标准化）: 统一换行、标题层级、front matter、source metadata。
    - deduplication（去重）: 用 content_hash / normalized_hash 去重。
    - chunking（切片）: 按标题和语义切分，而不是只按固定长度。
    - chunk_quality_check（切片质量检查）: 检查空切片、过短/过长、无 source_path、无 heading、无 authority。
    - source_readback_proof（原文回读证明）: 每个 chunk 可回读到当前 repo file + hash。
    - legacy_and_conflict_flag（旧口径和冲突标记）: 命中历史目录或降权源时标记，不能直接放行。
  output_to_retrieval（输出到检索层）:
    - cleaned_documents.jsonl
    - retrieval_manifest_fixture.yaml
    - source_readback_index.json
    - blocked_ingestion_report.md
  blocked_if（阻断条件）:
    - source_path 缺失。
    - content_hash 缺失。
    - secret scan 命中未处理。
    - 旧口径源被当作当前正式事实。
    - chunk 无法回读原文。
    - metadata authority_level 为空。
```

## 10. closed_loop_probe_plan（闭环探测计划）

```yaml
closed_loop_probe_plan（闭环探测计划）:
  probe_scope（探测范围）: text_rule_no_write_probe
  input_task（输入任务）: 判断 `sandbox_install_scope` 是否满足 no-write / no-secret / no-runtime / no-status-promotion 规则，并输出 write_executor_handoff 草案。
  route_decision（路由判断）:
    project_route: video_factory
    workflow_route_decision: mechanism_repair_flow
    execution_permission: no_write_probe_only
  retrieval_manifest（检索清单）:
    provider: fixture_mock_or_dashvector_if_authorized_later
    required_sources:
      - AGENTS.md
      - codex_log/latest.md
      - codex_source/schema_contracts/00_schema_contracts_index.md
      - this_design_report
  source_readback（原文回读）:
    required: true
    pass_condition: 每个 retrieval hit 都能回读 source_path + content_hash。
  retrieval_gap_report（检索缺口报告）:
    required: true
    gap_types:
      - rag_empty
      - rag_low_confidence
      - source_conflict
      - missing_source_path
      - stale_or_legacy_source
  deepseek_trigger_decision（DeepSeek 触发判断）:
    default: false
    trigger_only_if:
      - source_conflict
      - mechanism_conflict
      - high_risk_execution
      - user_explicit_request
  executor_handoff（执行器交接）:
    target: active_write_executor_codex
    output: no_write_handoff_package
    allowed_files: []
    forbidden_files:
      - pyproject.toml
      - compose.yaml
      - .env*
      - dist/*
      - public/*
      - media/*
  human_review_interrupt（人工复审中断）:
    required_before:
      - sandbox_install
      - runtime_enabled
      - external_code_copy
      - executor_switch
      - formal_mechanism_patch
  completion_truth_check（完成真实性检查）:
    completed_allowed: false_for_probe_runtime
    design_probe_completed_allowed: true_if_report_only
    forbidden_false_claims:
      - external_project_runs
      - sandbox_created
      - runtime_enabled
      - video_factory_rag_runtime_complete
  output_report（输出报告）:
    - closed_loop_probe_report.md
    - retrieval_manifest.yaml
    - source_readback.yaml
    - retrieval_gap_report.yaml
    - write_executor_handoff.yaml
```

闭环限制：

- 先用文本 / 规则任务测试，不做视频。
- 不调用外部 API。
- 不写真实业务状态。
- 不推进项目状态。
- 不把 `install_preflight_ready` 写成 `install_authorized`。

## 11. formal_mechanism_patch_plan（正式机制修补方案）

本轮不修改正式机制文件。后续如用户授权，建议按以下顺序最小补丁：

1. `write_executor` 抽象补丁：把 `Codex-only` 改为 `active_write_executor = codex` + `executor_type = codex / trae / future_ide_agent`。
2. `retrieval coexistence` 补丁：把上游 Chroma 定位为 sandbox 学习 / 对照模块，DashVector 为当前正式检索，统一由 `RetrievalManifest` + `SourceReadback` 裁决。
3. `cleaning adapter` 补丁：在任何入库前增加清洗、去重、secret scan、source readback、legacy blocker。
4. `human interrupt` 补丁：sandbox install、runtime enable、executor switch、formal mechanism patch 均需人工复审中断。
5. `completion truth` 补丁：外部框架跑通不等于视频工厂闭环跑通。

## 12. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  report_created（报告是否生成）: true
  latest_updated（latest 是否更新）: true
  forbidden_path_scan（禁止路径扫描）: passed
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
  secret_like_pattern_scan（密钥模式扫描）: passed
  no_dependency_install（未安装依赖）: true
  no_sandbox_created（未创建沙盒）: true
  runtime_enablement_absent（未启用运行时）: true
  no_external_code_copied（未复制外部代码）: true
  no_formal_mechanism_patch_applied（未直接修改正式机制）: true
  git_diff_check（Git diff 格式检查）: passed
  path_limited_diff_review（限定路径 diff 复核）: passed
  git_sync_status（Git 同步状态）: pending_before_path_limited_stage_commit_push_remote_readback
```

已运行或等价检查：

1. `git diff --check`
2. path-limited diff review
3. forbidden path scan
4. secret-like pattern scan
5. forbidden status promotion scan
6. path-limited stage / commit / push / remote readback

## 13. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - 上游 GitHub API tree endpoint 返回 403，本轮用 raw URL + codeload tarball stream 完成只读回读；不影响指定文件判断，但 API metadata 未验证。
  - 未运行上游 runtime，不能声明 agent-service-toolkit 已可运行。
  - 未安装依赖，不能声明依赖解析通过。
  - 未创建 sandbox，不能声明 sandbox_created。
  - 未调用 Chroma / DashVector runtime，不能声明检索运行时已并存跑通。
  - 未修改正式机制文件；executor abstraction / retrieval coexistence / cleaning adapter 仍是 patch plan。
```

## 14. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: sandbox_install_probe_prompt_after_user_confirmation
```

下一轮只有在用户明确授权安装 / sandbox 创建后，才允许进入 sandbox 探测；否则仍保持设计层和 no-write probe 层。
