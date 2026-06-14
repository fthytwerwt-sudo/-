# 20260614 UV Install And Sandbox Dependency Probe

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - local_tool_preflight_check（本机工具预检查）
  - uv_install_authorized（uv 安装已授权）
  - sandbox_dependency_probe_rerun（重新运行沙盒依赖探测）
  - no_main_pollution_install_check（不污染主线安装检查）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
execution_permission（执行权限）: install_uv_user_level_then_rerun_sandbox_dependency_probe
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
```

本轮用户已授权在本机用户环境安装 `uv`。本轮只允许把 `agent-service-toolkit` 的依赖安装探测限制在既有 sandbox 中，不允许污染视频工厂主仓库，不启动前端、Docker、Postgres、FastAPI 服务，不调用外部 LLM / DashVector / Groq / GitHub MCP / LangSmith / Langfuse API。

## 2. files_read（已读取文件）

```yaml
files_read（已读取文件）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
  codex_log/framework_adapter/20260614_sandbox_install_probe.md: read_ok
  codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
  skill_uv_package_manager（uv-package-manager 技能）: read_ok
  missing_files（缺失文件）: []
```

上一轮阻断状态已确认：

```yaml
previous_blocked_reason（上一轮阻断原因）: blocked_uv_required_but_missing_and_install_not_authorized
sandbox_workspace_created（沙盒工作区已创建）: true
upstream_project_downloaded（上游项目已下载）: true
dependency_installed_in_sandbox（是否在沙盒安装依赖）: false
main_repo_dependency_modified（主仓库依赖是否被修改）: false
external_code_copied_to_main（是否复制外部代码到主线）: false
frontend_started（是否启动前端）: false
docker_started（是否启动 Docker）: false
runtime_enabled（是否启用正式运行时）: false
```

## 3. uv_preflight_check（uv 预检查）

```yaml
uv_preflight_check（uv 预检查）:
  commands_run（运行命令）:
    - which uv || true
    - command -v uv || true
    - uv --version || true
  uv_found（是否找到 uv）: false
  uv_path（uv 路径）: null
  uv_version（uv 版本）: null
  needs_install（是否需要安装）: true
```

## 4. uv_install_result（uv 安装结果）

```yaml
uv_install_result（uv 安装结果）:
  install_attempted（是否尝试安装）: true
  brew_available（Homebrew 是否可用）: true
  brew_path（Homebrew 路径）: /opt/homebrew/bin/brew
  brew_version（Homebrew 版本）: 5.1.14
  brew_install_attempted（是否尝试 brew 安装）: true
  brew_install_result（brew 安装结果）: interrupted_after_download_stall_exit_130
  install_method（安装方式）: standalone_installer
  standalone_installer_command（独立安装命令）: curl -LsSf https://astral.sh/uv/install.sh | env UV_NO_MODIFY_PATH=1 UV_INSTALL_DIR="$HOME/.local/bin" sh
  success（是否成功）: true
  uv_path_after_install（安装后 uv 路径）: /Users/fan/.local/bin/uv
  uv_version_after_install（安装后 uv 版本）: uv 0.11.21 (5aa65dd7a 2026-06-11 aarch64-apple-darwin)
  shell_profile_modified（是否修改 shell 配置）: false
  restart_shell_required（是否需要重启 shell）: not_required_for_current_session_after_export
  future_shell_path_note（后续 shell PATH 提醒）: 如果用户 shell 配置未包含 $HOME/.local/bin，新终端需手动加入 PATH 或重新 export。
  sudo_used（是否使用 sudo）: false
  blocked_reason（阻断原因）: null
```

说明：

- Homebrew 存在，但 `brew install uv` 长时间停在下载阶段，已中断该尝试，未完成 brew 安装。
- 官方 standalone installer 使用 `UV_NO_MODIFY_PATH=1`，明确禁止自动修改 shell profile。
- 本轮 shell 通过 `export PATH="$HOME/.local/bin:$PATH"` 使用新安装的 `uv`。

## 5. sandbox_ready_check（沙盒就绪检查）

```yaml
sandbox_ready_check（沙盒就绪检查）:
  sandbox_path（沙盒路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  sandbox_path_exists（沙盒路径存在）: true
  pyproject_exists（pyproject.toml 是否存在）: true
  uv_lock_exists（uv.lock 是否存在）: true
  upstream_commit（上游提交）: 5b3945f48e41a193816d7710b275eb89b90568ee
  inside_main_repo（是否在主仓库内）: false
  sandbox_git_status（沙盒 Git 状态）: clean_before_uv_sync_except_ignored_generated_files
```

## 6. sandbox_dependency_probe（沙盒依赖探测）

```yaml
sandbox_dependency_probe（沙盒依赖探测）:
  command_run（运行命令）: uv sync --frozen
  workdir（运行目录）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  success（是否成功）: false
  status（状态）: blocked_uv_sync_download_stalled_or_timed_out_in_sandbox
  exit_code（退出码）: 130
  interrupted_by_codex（是否由 Codex 中断）: true
  reason_for_interrupt（中断原因）: 长时间停留在依赖下载/同步阶段，.venv 未进入完整安装状态，避免无限挂起。
  python_downloaded_by_uv（uv 下载 Python）: cpython-3.13.14-macos-aarch64-none
  venv_created（是否创建 .venv）: true
  venv_size_after_interrupt（中断后 .venv 大小）: 68K
  dependency_installed_in_sandbox（是否在沙盒安装依赖）: partial_not_usable
  lockfile_update_required（是否要求更新 lock）: false
  secret_required（是否要求密钥）: false
  failure_reason（失败原因）: uv sync --frozen 下载/同步耗时过长，最后 60 秒无输出或完成信号；已中断并记录现场。
```

本次 `uv sync --frozen` 已完成的可见动作：

```yaml
observed_uv_sync_progress（观察到的 uv sync 进展）:
  python_runtime（Python 运行时）: CPython 3.13.14
  virtualenv_created_at（虚拟环境位置）: .venv
  downloads_observed（观察到的下载）:
    - pygments
    - google-ai-generativelanguage
    - sympy
    - hf-xet
    - pydeck
    - setuptools
    - primp
    - pillow
    - sqlalchemy
    - cryptography
    - psycopg-binary
    - pydantic-core
    - grpcio-tools
    - chromadb
    - grpcio
    - pandas
    - jsonschema-rs
    - tokenizers
    - google-cloud-aiplatform
    - streamlit
    - pyowm
    - pyarrow
    - onnxruntime
    - langchain-community
    - uvloop
    - ruff
    - numpy
    - shapely
    - mypy
    - kubernetes
    - botocore
    - lxml
    - virtualenv
  builds_observed（观察到的构建）:
    - pypika==0.48.9
    - forbiddenfruit==0.1.4
```

## 7. minimal_import_probe（最小导入探测）

```yaml
minimal_import_probe（最小导入探测）:
  compileall_src（src 编译）: not_run
  schema_import（schema 导入）: not_run
  client_import（client 导入）: not_run
  service_import（service 导入）: not_run
  rag_tools_import（RAG 工具导入）: not_run
  agents_registry_import（agents 注册表导入）: not_run
  status（状态）: blocked_not_run_because_uv_sync_interrupted_before_usable_dependency_environment
```

说明：执行单要求在 `uv sync --frozen` 成功后再运行 `uv run python -m compileall -q src` 和最小 import 探测。由于本轮 sync 未完成，未继续运行 import，以免把未完成依赖环境误判为上游项目 runtime 失败。

## 8. disabled_services_check（禁用服务检查）

```yaml
disabled_services_check（禁用服务检查）:
  streamlit_started（Streamlit 是否启动）: false
  docker_started（Docker 是否启动）: false
  postgres_started（Postgres 是否启动）: false
  service_server_started（服务端是否启动）: false
  external_api_called（是否调用外部 API）: false
  chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
```

未运行：

- `streamlit run`
- `docker compose`
- `uvicorn`
- `python src/run_service.py`
- `scripts/create_chroma_db.py`
- 任何真实 OpenAI / DashVector / Groq / GitHub MCP / LangSmith / Langfuse 调用

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
  sandbox_env_files_found（沙盒中发现的 env 文件）:
    - .env.example
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
  uv_available_after（安装后 uv 可用）: true
  sandbox_dependency_probe_done（沙盒依赖探测已完成）: blocked_with_reason
  minimal_import_probe_done（最小导入探测已完成）: blocked_with_reason
  no_main_repo_dependency_modified（主仓库依赖未修改）: true
  no_external_code_tracked_in_main（外部代码未被主仓库跟踪）: true
  no_env_or_secret_written（未写入 env 或 secret）: true
  no_frontend_started（未启动前端）: true
  no_docker_started（未启动 Docker）: true
  no_formal_runtime_enabled（未启用正式运行时）: true
  latest_updated（latest 已更新）: true
  report_created（报告已生成）: true
  git_diff_check（Git diff 格式检查）: passed
  forbidden_path_scan（禁止路径扫描）: passed
  secret_like_pattern_scan（密钥模式扫描）: passed
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
  staged_diff_limited_to_allowed_files（暂存 diff 是否限于允许文件）: passed
```

## 11. blocked_report（阻断报告）

```yaml
blocked_report（阻断报告）:
  blocked_reason（阻断原因）: uv_sync_download_stalled_or_timed_out_in_sandbox
  completed_before_block（阻断前完成了什么）:
    - uv_preflight_check_completed
    - uv_user_level_install_completed
    - uv_available_after_install
    - sandbox_ready_check_completed
    - uv_sync_frozen_started_in_sandbox
    - .venv_created_in_sandbox
    - partial_download_cache_created
    - no_main_repo_pollution_detected
  missing_permission（缺少什么授权）: none
  safest_next_step（最安全下一步）: rerun_uv_sync_frozen_in_same_sandbox_with_longer_network_window_or_preseed_uv_cache
```

## 12. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - `uv sync --frozen` 未完成，sandbox `.venv` 不是可用依赖环境。
  - 未运行 `uv run python -m compileall -q src`。
  - 未运行最小 import 探测。
  - sandbox 中保留了不完整 `.venv` 现场，后续可继续重跑 `uv sync --frozen`。
  - 当前 shell 已可用 `uv`，但未来新 shell 若未包含 `$HOME/.local/bin`，需要补 PATH。
```

## 13. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: rerun_uv_sync_frozen_in_same_sandbox_with_longer_network_window_or_preseed_uv_cache
```

下一轮仍应遵守：

- 不在主仓库根目录运行依赖安装。
- 不修改主仓库依赖文件。
- 不启动 Streamlit / Docker / Postgres / FastAPI 服务。
- 不创建 `.env`，不写入 secret。
- 不把 sandbox 依赖探测写成视频工厂 runtime 已启用。
