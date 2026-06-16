# 20260614 Sandbox Install Probe

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - sandbox_install_probe（沙盒安装探测）
  - external_framework_full_intake_probe（外部框架完整接入探测）
  - no_main_pollution_install_check（不污染主线安装检查）
  - closed_loop_probe_preparation（闭环探测准备）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
execution_permission（执行权限）: sandbox_install_probe_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
```

本轮允许在隔离 sandbox 中 clone 和探测 `JoshuaC215/agent-service-toolkit`。本轮不允许把外部项目代码合并进主仓库，不允许修改主仓库依赖配置，不允许启动前端 / Docker / Postgres，不允许把 sandbox 探测写成正式 runtime 启用。

## 2. files_read（已读取文件）

### 2.1 current_repo_readback（当前仓库回读）

```yaml
current_repo_read_status（当前仓库读取状态）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
  codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
  codex_log/framework_adapter/20260614_schema_contract_static_validation.md: read_ok
  codex_source/schema_contracts/00_schema_contracts_index.md: read_ok
  skill_uv_package_manager（uv-package-manager 技能）: read_ok
missing_files（缺失文件）: []
blocked_if_missing_critical_file（关键文件缺失是否阻断）: false
```

`codex_log/latest.md` 顶部准入状态：

```yaml
external_framework_full_intake_design_completed（完整接入设计已完成）: true
next_safe_step（下一步安全动作）: sandbox_install_probe_prompt_after_user_confirmation
install_executed（是否已安装）: false
sandbox_created（是否创建沙盒）: false
runtime_enabled（是否启用运行时）: false
external_code_copied（是否复制外部代码）: false
```

### 2.2 upstream_readback_after_download（下载后上游回读）

```yaml
upstream_repo（上游仓库）: JoshuaC215/agent-service-toolkit
upstream_commit（上游提交）: 5b3945f48e41a193816d7710b275eb89b90568ee
upstream_read_status（上游读取状态）:
  README.md: read_ok
  pyproject.toml: read_ok
  uv.lock: read_ok
  compose.yaml: read_ok
  .env.example: read_ok
  docs/RAG_Assistant.md: read_ok
  scripts/create_chroma_db.py: read_ok
  src/agents/tools.py: read_ok
  src/agents/rag_assistant.py: read_ok
  src/service/service.py: read_ok
  src/client/client.py: read_ok
  src/core/settings.py: read_ok
  docker/Dockerfile.service: read_ok
  docker/Dockerfile.app: read_ok
  tests/: read_ok
```

## 3. sandbox_workspace（沙盒工作区）

```yaml
sandbox_workspace（沙盒工作区）:
  path（路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  parent_path（父路径）: /Users/fan/Documents/视频工厂_sandbox
  inside_main_repo（是否在主仓库内）: false
  tracked_by_git（是否被主仓库 Git 跟踪）: false
  gitignore_needed（是否需要 gitignore）: false
  safe_to_create（是否安全创建）: true
  sandbox_workspace_created（沙盒工作区已创建）: true
```

说明：

- 该路径是本轮执行单明确授权的优先 sandbox 路径。
- 它不在 `/Users/fan/Documents/视频工厂` 主仓库内部，因此不会被主仓库 Git 跟踪。
- 主仓库仍只有既有未跟踪 `public/`，本轮未触碰。

## 4. upstream_fetch_result（上游获取结果）

```yaml
upstream_fetch_result（上游获取结果）:
  method（方式）: git_clone
  repo_url（仓库地址）: https://github.com/JoshuaC215/agent-service-toolkit
  sandbox_path（沙盒路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  success（是否成功）: true
  commit_or_archive_ref（commit 或归档引用）: 5b3945f48e41a193816d7710b275eb89b90568ee
  blocked_reason（阻断原因）: null
```

获取命令只在 sandbox 路径执行，没有把上游源码复制进主仓库正式路径。

## 5. dependency_probe_result（依赖探测结果）

```yaml
dependency_probe_result（依赖探测结果）:
  uv_available（uv 是否可用）: false
  uv_lock_exists（uv.lock 是否存在）: true
  requirements_txt_exists（requirements.txt 是否存在）: false
  command_run（运行命令）: not_run_uv_missing
  success（是否成功）: false
  status（状态）: blocked_uv_required_but_missing_and_install_not_authorized
  failure_reason（失败原因）: 当前 PATH 中没有 `uv`；执行单禁止自动全局安装 uv。已用现有 Python 做只读依赖文件解析，但未安装依赖。
  dependency_installed_in_sandbox（是否只在沙盒安装依赖）: false
  main_repo_dependency_modified（主仓库依赖是否被修改）: false
  parsed_with_python（是否用 Python 解析依赖文件）: true
  bundled_python_version（Codex bundled Python 版本）: 3.12.13
  system_python_version（系统 python3 版本）: 3.9.6
  requires_python（项目 Python 要求）: ">=3.11,<3.14"
  project_dependency_count（主依赖数量）: 41
  dev_dependency_count（dev 依赖数量）: 8
  client_dependency_count（client 依赖数量）: 4
  uv_lock_package_entries（uv.lock package 条目数）: 249
```

边界说明：

- 没有运行 `uv sync --frozen`，因为 `uv` 不存在且本轮未授权安装 `uv`。
- 没有使用 `pip install` 替代安装，避免绕过执行单中对 `uv` 缺失的阻断逻辑。
- 没有创建 `.venv`。
- 没有修改 `pyproject.toml / uv.lock`。

## 6. minimal_import_probe（最小导入探测）

```yaml
minimal_import_probe（最小导入探测）:
  compileall_src（src 语法编译）:
    command（命令）: python3.12 -m compileall -q src
    success（是否成功）: true
  import_service_module（导入服务模块）:
    module（模块）: service.service
    success（是否成功）: false
    failure_reason（失败原因）: ModuleNotFoundError: No module named 'fastapi'
  import_client_module（导入客户端模块）:
    module（模块）: client.client
    success（是否成功）: false
    failure_reason（失败原因）: ModuleNotFoundError: No module named 'httpx'
  import_agents_registry（导入 agents registry）:
    module（模块）: agents.agents
    success（是否成功）: false
    failure_reason（失败原因）: ModuleNotFoundError: No module named 'langgraph'
  import_rag_tools（导入 RAG tools）:
    module（模块）: agents.tools
    success（是否成功）: false
    failure_reason（失败原因）: ModuleNotFoundError: No module named 'langgraph'
  import_schema_module（导入 schema 模块）:
    module（模块）: schema.schema
    success（是否成功）: true
  minimal_import_probe_result（最小导入探测结果）: partial_static_compile_passed_runtime_imports_blocked_by_missing_dependencies
```

解释：

- `compileall src` 通过，说明源码语法层可编译。
- `schema.schema` 可以在未安装项目依赖的情况下导入。
- service/client/agents/RAG tools 的失败原因是依赖未安装，不是服务启动失败。
- 本轮没有启动 FastAPI service，没有启动 Streamlit，没有创建 Chroma DB，没有调用真实 LLM API。

## 7. env_requirements（环境变量需求）

```yaml
env_requirements（环境变量需求）:
  required_for_runtime（运行时需要）:
    - OPENAI_API_KEY 或其他至少一个 LLM provider key，除非使用 USE_FAKE_MODEL=true
    - USE_FAKE_MODEL=true 可用于无外部 API 的本地测试
    - DATABASE_TYPE 可选，默认 sqlite
  required_for_rag（RAG 需要）:
    - OPENAI_API_KEY
    - chroma_db 本地目录
  required_for_safeguard（安全拦截需要）:
    - GROQ_API_KEY
  required_for_github_mcp（GitHub MCP 需要）:
    - GITHUB_PAT
  required_for_observability（观测/反馈需要）:
    - LANGCHAIN_API_KEY
    - LANGFUSE_PUBLIC_KEY
    - LANGFUSE_SECRET_KEY
  safe_fake_env_possible（是否可用 fake env 做测试）: true
  secret_written（是否写入密钥）: false
  secret_printed（是否打印密钥）: false
  env_file_created（是否创建 .env）: false
```

本轮只读取 `.env.example`，没有创建 `.env`，也没有打印或写入真实密钥。

## 8. disabled_services_check（禁用服务检查）

```yaml
disabled_services_check（禁用服务检查）:
  streamlit_started（Streamlit 是否启动）: false
  docker_compose_started（Docker Compose 是否启动）: false
  postgres_started（Postgres 是否启动）: false
  service_server_started（服务端是否启动）: false
  docker_started（是否启动 Docker）: false
```

本轮未运行：

- `streamlit run`
- `docker compose`
- `docker compose watch`
- `python src/run_service.py`
- `uvicorn`
- Chroma DB 创建脚本

## 9. main_repo_pollution_check（主仓库污染检查）

```yaml
main_repo_pollution_check（主仓库污染检查）:
  install_executed_in_main_repo（是否在主仓库安装）: false
  main_repo_dependency_modified（主仓库依赖是否被修改）: false
  external_code_copied_to_main（是否复制外部代码到主线）: false
  external_code_tracked_in_main（外部代码是否被主仓库跟踪）: false
  env_or_secret_written（是否写入 env 或 secret）: false
  forbidden_paths_modified（是否修改禁止路径）: false
  main_repo_status_before_report（报告前主仓库状态）: "## main...origin/main / ?? public/"
```

主仓库禁止路径未修改：

- `AGENTS.md`
- `GPT数据源/*`
- `codex_source/*`
- `pyproject.toml`
- `requirements.txt`
- `package.json`
- `compose.yaml`
- `docker-compose.yml`
- `dist/*`
- `public/*`
- `media/*`
- `.env*`

## 10. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  sandbox_path_exists（沙盒路径存在）: true
  upstream_project_present（上游项目存在）: true
  dependency_probe_done（依赖探测已完成）: true
  dependency_probe_status（依赖探测状态）: blocked_uv_missing
  minimal_import_probe_done（最小导入探测已完成）: true
  minimal_import_probe_status（最小导入探测状态）: partial_static_compile_passed
  no_main_repo_dependency_modified（主仓库依赖未修改）: true
  no_external_code_tracked_in_main（外部代码未被主仓库跟踪）: true
  no_env_or_secret_written（未写入 env 或 secret）: true
  no_frontend_started（未启动前端）: true
  no_docker_started（未启动 Docker）: true
  formal_runtime_enablement_absent（未启用正式运行时）: true
  latest_updated（latest 已更新）: true
  git_diff_check（Git diff 格式检查）: passed
  forbidden_path_scan（禁止路径扫描）: passed
  secret_like_pattern_scan（密钥模式扫描）: passed
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
  staged_diff_limited_to_allowed_files（暂存 diff 是否限于允许文件）: passed
```

本报告和 `latest.md` 写入后已完成前四项检查，stage 后仍需复跑 staged diff 检查：

1. `git status --short`
2. `git diff --check`
3. forbidden path scan
4. secret-like pattern scan
5. forbidden status promotion scan
6. path-limited stage / commit / push / remote readback

## 11. blocked_report（阻断报告）

```yaml
blocked_report（阻断报告）:
  blocked_reason（阻断原因）: uv_required_but_missing_and_install_not_authorized
  completed_before_block（阻断前完成了什么）:
    - sandbox_workspace_created
    - upstream_project_downloaded
    - upstream_required_files_read
    - dependency_files_parsed_readonly
    - compileall_src_passed
    - minimal_import_probe_attempted
  missing_permission（缺少什么授权）:
    - install_uv_or_provide_uv_path
    - rerun_uv_sync_frozen_in_sandbox
  safest_next_step（最安全下一步）: authorize_uv_install_or_provide_existing_uv_then_rerun_sandbox_dependency_probe
```

## 12. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - 未运行 `uv sync --frozen`，因为当前环境缺 `uv` 且本轮禁止自动全局安装。
  - 未安装依赖，因此 service/client/agents/RAG tools 的 runtime import 未通过。
  - 未启动 FastAPI service、Streamlit、Docker、Postgres。
  - 未创建 Chroma DB，未调用 OpenAI / DashVector / Groq / GitHub MCP / LangSmith / Langfuse。
  - 未进入主仓库正式接入分支，未合并主线外部代码。
```

## 13. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: authorize_uv_install_or_provide_existing_uv_then_rerun_sandbox_dependency_probe
```

下一轮若用户授权，可在同一 sandbox 路径中安装 `uv` 或提供现有 `uv` 路径，然后仅在 sandbox 内运行：

```bash
uv sync --frozen
```

仍不得启动 Streamlit、Docker、Postgres，仍不得修改主仓库依赖或复制上游代码到主线。
