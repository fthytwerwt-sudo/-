# 20260614 Goal Mode Sandbox Install Completion

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory
task_type（任务类型）:
  - goal_mode_sandbox_install_completion（目标模式沙盒安装完成）
  - uv_environment_repair（uv 环境修复）
  - sandbox_dependency_sync_completion（沙盒依赖同步完成）
  - minimal_import_probe（最小导入探测）
  - no_main_pollution_check（不污染主线检查）
  - mechanism_repair_flow（机制修补流程）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow
execution_permission（执行权限）: goal_mode_sandbox_install_only
active_write_executor（当前激活写入执行器）: codex
deepseek_triggered（是否触发 DeepSeek）: false
not_deepseek_conclusion（不是 DeepSeek 结论）: true
```

本轮进入 goal mode，目标是在既有 sandbox 内把 `JoshuaC215/agent-service-toolkit` 安装到可用依赖环境，并完成最小导入验证。本轮不代表视频工厂主仓库正式接入、不代表服务 runtime 启用、不代表 Chroma 入库完成。

## 2. files_read（已读取文件）

```yaml
files_read（已读取文件）:
  AGENTS.md: read_ok
  codex_log/latest.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md: read_ok
  codex_log/framework_adapter/20260614_sandbox_install_probe.md: read_ok
  codex_log/framework_adapter/20260614_uv_install_and_sandbox_dependency_probe.md: read_ok
  codex_log/framework_adapter/20260614_external_framework_full_intake_design.md: read_ok
  skill_uv_package_manager（uv-package-manager 技能）: read_ok
  memory_context（记忆上下文）: read_ok
  missing_files（缺失文件）: []
```

上一轮状态确认：

```yaml
previous_state_check（上一轮状态检查）:
  uv_available_after（uv 已可用）: true
  sandbox_dependency_probe_result（沙盒依赖探测结果）: blocked_uv_sync_download_stalled_or_timed_out_in_sandbox
  main_repo_pollution（主仓库污染）: false
  next_safe_step（下一步安全动作）: rerun_uv_sync_frozen_in_same_sandbox_with_longer_network_window_or_preseed_uv_cache
```

## 3. uv_path_check（uv 路径检查）

```yaml
uv_path_check（uv 路径检查）:
  current_shell_uv_found（当前 shell 是否找到 uv）: true
  current_shell_uv_path（当前 shell uv 路径）: /Users/fan/.local/bin/uv
  current_shell_uv_version（当前 shell uv 版本）: uv 0.11.21 (5aa65dd7a 2026-06-11 aarch64-apple-darwin)
  new_shell_uv_found（新 shell 是否找到 uv）: true
  new_shell_uv_path（新 shell uv 路径）: /Users/fan/.local/bin/uv
  new_shell_uv_version（新 shell uv 版本）: uv 0.11.21 (5aa65dd7a 2026-06-11 aarch64-apple-darwin)
  path_persistence_needed（是否需要 PATH 持久化）: false
```

## 4. path_persistence_result（PATH 持久化结果）

```yaml
path_persistence_result（PATH 持久化结果）:
  path_persistence_fixed（PATH 是否已持久化修复）: false
  reason（原因）: current shell and new zsh login shell both found uv.
  shell_profile_modified（是否修改 shell 配置）: false
  zshrc_backup_created（是否创建 zshrc 备份）: false
```

## 5. sandbox_state_check（沙盒状态检查）

```yaml
sandbox_state_check（沙盒状态检查）:
  sandbox_path（沙盒路径）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  sandbox_path_exists（沙盒路径存在）: true
  inside_main_repo（是否在主仓库内）: false
  pyproject_exists（pyproject 是否存在）: true
  uv_lock_exists（uv.lock 是否存在）: true
  partial_venv_exists_before_cleanup（清理前残缺 .venv 是否存在）: true
  partial_venv_size_before_cleanup（清理前 .venv 大小）: 68K
  sandbox_git_status（沙盒 Git 状态）: clean_before_cleanup
```

## 6. partial_venv_cleanup（残缺 .venv 清理）

```yaml
partial_venv_cleanup（残缺 .venv 清理）:
  cleanup_needed（是否需要清理）: true
  cleanup_done（是否已清理）: true
  deleted_paths（删除路径）:
    - /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614/.venv
  deletion_scope_valid（删除范围是否有效）: true
```

## 7. sandbox_dependency_sync_result（沙盒依赖同步结果）

```yaml
sandbox_dependency_sync_result（沙盒依赖同步结果）:
  command（命令）: uv sync --frozen
  workdir（运行目录）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  attempts_this_round（本轮尝试次数）: 1
  success（是否成功）: true
  sandbox_dependency_sync_completed（沙盒依赖同步是否完成）: true
  sandbox_venv_usable（沙盒 .venv 是否可用）: true
  lockfile_update_required（是否要求更新 lock）: false
  pyproject_modified（pyproject 是否被修改）: false
  uv_lock_modified（uv.lock 是否被修改）: false
  dependency_install_scope（依赖安装范围）: sandbox_only
  python_runtime（Python 运行时）: CPython 3.13.14
  packages_installed（安装包数量）: 241
  venv_size_after_sync（同步后 .venv 大小）: 1.1G
  uv_pip_check（uv pip check）: passed
```

下载重试记录：

```yaml
download_retry_report（下载重试报告）:
  attempts（尝试次数）: 1
  longest_wait_minutes（最长等待分钟数）: about_1_minute
  last_visible_progress（最后可见进度）: Installed 241 packages
  final_status（最终状态）: success
```

## 8. compile_probe（编译探测）

```yaml
compile_probe（编译探测）:
  command（命令）: uv run python -m compileall -q src
  success（是否成功）: true
  failure_reason（失败原因）: null
```

## 9. minimal_import_probe（最小导入探测）

第一次直接导入结果：

```yaml
direct_import_without_pythonpath（未设置 PYTHONPATH 的直接导入）:
  schema_import（schema 导入）: failed_module_path_missing
  client_import（client 导入）: failed_module_path_missing
  service_import（service 导入）: failed_module_path_missing
  rag_tools_import（RAG 工具导入）: failed_module_path_missing
  agents_registry_import（智能体注册表导入）: failed_module_path_missing
  conclusion（结论）: 上游源码布局需要 `PYTHONPATH=src`。
```

设置 `PYTHONPATH=src` 后的导入结果：

```yaml
import_with_pythonpath（设置 PYTHONPATH 后导入）:
  schema_import（schema 导入）: passed
  client_import（client 导入）: passed
  service_import（service 导入）: failed_settings_requires_llm_key_or_fake_model
  rag_tools_import（RAG 工具导入）: failed_settings_requires_llm_key_or_fake_model
  agents_registry_import（智能体注册表导入）: failed_settings_requires_llm_key_or_fake_model
```

使用 inline fake env 后的最小导入结果：

```yaml
minimal_import_probe（最小导入探测）:
  command_context（命令上下文）: USE_FAKE_MODEL=true PYTHONPATH=src uv run python
  fake_env_written_to_file（是否把假环境变量写入文件）: false
  external_api_call（是否调用外部 API）: false
  schema_import（schema 导入）: passed
  client_import（client 导入）: passed
  service_import（service 导入）: passed
  rag_tools_import（RAG 工具导入）: passed
  agents_registry_import（智能体注册表导入）: passed
  import_probe_summary（导入探测总结）: passed_with_pythonpath_and_inline_fake_model
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
  process_scan（进程扫描）: no_matching_service_process_found
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
  sandbox_env_files_found（沙盒中发现的 env 文件）:
    - .env.example
```

## 12. validation_result（验证结果）

```yaml
validation_result（验证结果）:
  uv_available（uv 可用）: true
  sandbox_dependency_sync_completed（沙盒依赖同步完成）: true
  sandbox_venv_usable（沙盒 .venv 可用）: true
  compile_probe_done（编译探测完成）: true
  compile_probe_passed（编译探测通过）: true
  minimal_import_probe_done（最小导入探测完成）: true
  minimal_import_probe_passed（最小导入探测通过）: true
  no_main_repo_dependency_modified（主仓库依赖未修改）: true
  no_external_code_tracked_in_main（外部代码未被主仓库跟踪）: true
  no_env_or_secret_written（未写入 env 或 secret）: true
  no_frontend_started（未启动前端）: true
  no_docker_started（未启动 Docker）: true
  no_formal_runtime_enabled（未启用正式运行时）: true
  report_created（报告已生成）: true
  latest_updated（latest 已更新）: true
  git_diff_check（Git diff 格式检查）: passed
  forbidden_path_scan（禁止路径扫描）: passed
  secret_like_pattern_scan（密钥模式扫描）: passed
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed
  staged_diff_limited_to_allowed_files（暂存 diff 是否限于允许文件）: passed
```

## 13. remaining_gaps（剩余缺口）

```yaml
remaining_gaps（剩余缺口）:
  - sandbox 依赖环境和 import 已可用，但没有启动 FastAPI service。
  - 没有运行 Chroma 入库脚本。
  - 没有做真实 LLM / DashVector / Groq / LangSmith / Langfuse 调用。
  - 最小导入需要 `PYTHONPATH=src` 和 `USE_FAKE_MODEL=true` 才能在无密钥环境下完整通过。
```

## 14. blocked_if_any（如有阻断）

```yaml
blocked_if_any（如有阻断）: null
```

## 15. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: sandbox_no_service_closed_loop_import_or_service_contract_probe_after_user_confirmation
```

下一步如果继续推进，仍应先保持 no-service / no-secret 边界，只做 service contract 或 no-write closed loop probe；不得直接写成视频工厂正式 runtime 已启用。
