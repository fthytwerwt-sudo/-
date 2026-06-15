# 20260614｜Agent Service Toolkit Sandbox Branch Context

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory
  task_type（任务类型）:
    - adapter_branch_creation
    - sandbox_branch_context_setup
    - git_sync_boundary_repair
    - main_branch_protection
    - mechanism_repair_flow
  workflow_route_decision（工作流归位判断）: mechanism_repair_flow
  execution_permission（执行权限）: create_and_push_adapter_branch_update_branch_latest_only
  active_write_executor（当前激活写入执行器）: codex
  deepseek_triggered（是否触发 DeepSeek）: false
  not_deepseek_conclusion（不是 DeepSeek 结论）: true

branch_result（分支结果）:
  branch_name（分支名）: adapter/agent-service-toolkit-sandbox
  branch_source（分支来源）: origin/main
  source_commit（来源提交）: 42954b677af5c8a21252d282f2a4846ce278a4dd
  remote_branch_created（远端分支是否创建）: true
  remote_branch_initial_sha（远端分支初始 SHA）: 42954b677af5c8a21252d282f2a4846ce278a4dd
  main_branch_modified_this_round（本轮是否修改 main 分支）: false

branch_context（分支上下文）:
  branch_purpose（分支用途）: agent-service-toolkit 沙盒接入、适配、测试、清洗层、RAG、LangGraph、DashVector adapter 实验
  external_framework（外部框架）: JoshuaC215/agent-service-toolkit
  sandbox_workspace（沙盒工作区）: /Users/fan/Documents/视频工厂_sandbox/agent-service-toolkit_probe_20260614
  sandbox_upstream_commit（沙盒上游提交）: 5b3945f48e41a193816d7710b275eb89b90568ee
  main_policy（main 分支策略）: main 只接收确认后的正式结果；本分支承载接入实验、契约补丁和报告证据
  sandbox_submission_policy（沙盒提交策略）:
    - 不提交 sandbox `.venv`
    - 不提交外部项目源码副本
    - 不提交 `video_factory_probe` 临时脚本或输出
    - 不提交 `.env`、API key、token、私密路径
  sandbox_files_committed（是否提交沙盒文件）: false
  external_code_copied_to_main（是否复制外部代码到主线）: false
  runtime_enabled（是否启用正式运行时）: false

allowed_future_work（后续允许工作）:
  - formal_adapter_patch_plan
  - schema_contract_patch
  - retrieval_manifest_source_readback_contract
  - cleaning_adapter_contract
  - DashVector adapter probe
  - graph_runtime_adapter probe
  - service contract probe after authorization

forbidden_without_new_authorization（未经新授权禁止事项）:
  - merge_to_main
  - runtime_enablement
  - FastAPI service start
  - Docker / Postgres / Streamlit start
  - Chroma ingestion script run
  - real external API call
  - secret / .env write
  - dependency file modification in main repo

current_evidence（当前证据）:
  previous_sandbox_dependency_sync_result（上一轮沙盒依赖同步结果）: completed
  previous_compile_probe_result（上一轮编译探测结果）: passed
  previous_minimal_import_probe_result（上一轮最小导入探测结果）: passed
  previous_langgraph_stability_probe（上一轮 LangGraph 稳定性探测）: passed_within_sandbox_fake_model_no_service_scope
  current_branch_scope（当前分支范围）: branch_anchor_and_context_only

status_boundaries（状态边界）:
  install_executed_in_main_repo（是否在主仓库安装）: false
  main_repo_dependency_modified（主仓库依赖是否被修改）: false
  frontend_started（是否启动前端）: false
  docker_started（是否启动 Docker）: false
  postgres_started（是否启动 Postgres）: false
  fastapi_service_started（是否启动 FastAPI 服务）: false
  chroma_ingestion_script_run（是否运行 Chroma 入库脚本）: false
  external_api_called（是否调用外部 API）: false
  runtime_enabled（是否启用正式运行时）: false

next_safe_step（下一步安全动作）: continue_agent_service_toolkit_adapter_work_on_adapter_branch
```

## 说明

本分支是 `agent-service-toolkit` 后续接入实验的隔离承载线，不是主线合并结果，也不是正式 runtime 启用结果。此前沙盒里的安装、导入、LangGraph/RAG/清洗层审计和稳定性证明只能作为 adapter branch 的证据输入；它们不能自动升级为 `main` 分支事实。

后续如果要把实验结果回灌到主线，必须另起明确执行单，限定变更范围，完成 path-limited diff review、secret scan、forbidden path scan、forbidden status promotion scan，并由用户确认是否进入 main 合并流程。
