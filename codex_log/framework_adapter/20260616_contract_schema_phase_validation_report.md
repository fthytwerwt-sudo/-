# 20260616 Contract Schema Phase Validation Report

## 1. route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - contract_schema_patch_task（契约与 schema 补丁任务）
  - fixture_validation_task（样例验证任务）
  - adapter_pre_code_guardrail_task（代码接入前护栏任务）
workflow_route_decision（workflow 归位判断）: mechanism_repair_flow（机制修补流）
execution_permission（执行权限）: contracts_schemas_fixtures_only（仅契约 / schema / fixture）
branch（分支）: adapter/agent-service-toolkit-sandbox
runtime_enabled（是否启用正式运行时）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
```

## 2. validation_report（验证报告）

```yaml
schema_files_created（已创建 / 更新 schema 文件）:
  created（新增）:
    - codex_source/schema_contracts/schemas/graph_runtime_adapter.schema.yaml
    - codex_source/schema_contracts/schemas/source_readback_map.schema.yaml
    - codex_source/schema_contracts/schemas/cleaning_adapter.schema.yaml
    - codex_source/schema_contracts/schemas/service_contract_no_write.schema.yaml
    - codex_source/schema_contracts/schemas/runtime_memory_boundary.schema.yaml
    - codex_source/schema_contracts/schemas/completion_truth_check_node.schema.yaml
  updated（更新）:
    - codex_source/schema_contracts/schemas/retrieval_manifest.schema.yaml

fixture_files_created（已创建 / 更新 fixture 文件）:
  new_fixture_files_created（新增 fixture 文件数量）: 34
  target_passing_fixtures_validated（已验证通过样例数量）: 8
  target_blocked_fixtures_validated（已验证阻断样例数量）: 27
  total_schema_files_after_update（更新后 schema 总数）: 16
  total_passing_fixtures_after_update（更新后 passing fixture 总数）: 16
  total_blocked_fixtures_after_update（更新后 blocked fixture 总数）: 36

yaml_parse_result（YAML 解析结果）:
  status（状态）: passed
  parsed_yaml_files（已解析 YAML 文件数量）: 68
  parser（解析器）: ruby YAML / Psych（系统自带，只读验证，未安装依赖）

required_fields_result（必填字段结果）:
  status（状态）: passed
  schema_families_checked（已检查 schema 家族）:
    - graph_runtime_adapter
    - retrieval_manifest
    - source_readback_map
    - cleaning_adapter
    - service_contract_no_write
    - runtime_memory_boundary
    - completion_truth_check_node
  hard_rule_checks（硬规则检查）:
    graph_runtime_adapter.runtime_write_allowed（图 runtime 是否允许写仓库）: false_required
    retrieval_manifest.source_readback_required（检索清单是否必须原文回读）: true_required
    service_contract_no_write.service_can_write_repo（服务是否能写仓库）: false_required
    runtime_memory_boundary.memory_can_replace_repo_facts（memory 是否能替代仓库事实）: false_required

passing_fixture_result（通过样例结果）:
  status（状态）: passed
  checked（已检查）:
    - graph_runtime_adapter.passing.yaml
    - retrieval_manifest_dashvector_fixture.passing.yaml
    - retrieval_manifest_chroma_sandbox_fixture.passing.yaml
    - source_readback_map.passing.yaml
    - cleaning_adapter.passing.yaml
    - service_contract_no_write.passing.yaml
    - runtime_memory_boundary.passing.yaml
    - completion_truth_check.passing.yaml

blocked_fixture_result（阻断样例结果）:
  status（状态）: passed
  blocked_case_coverage（阻断场景覆盖）:
    - graph_direct_write（graph 直接写仓库）
    - graph_missing_source_readback（graph 缺原文回读）
    - graph_completed_without_truth_check（graph 缺完成真实性检查却声明完成）
    - retrieval_missing_source_path（检索缺 source_path）
    - retrieval_missing_chunk_id（检索缺 chunk_id）
    - chroma_replace_dashvector（Chroma 试图替代 DashVector）
    - retrieval_claimed_as_fact（检索结果直接写成事实）
    - source_missing（无法回读原文件）
    - source_conflict（回读和检索摘要冲突）
    - source_stale（旧分支 / 旧口径冒充当前事实）
    - cleaning_secret（清洗前发现 secret-like 内容）
    - cleaning_metadata（清洗缺 metadata）
    - cleaning_legacy（旧 gray_test 口径覆盖正式运营事实）
    - service_write（service 尝试写仓库）
    - service_commit_push（service 尝试 commit / push）
    - service_runtime_enablement_true（service 输出 runtime enablement true）
    - service_external_api（service 未授权调用外部 API）
    - memory_repo_fact（memory 替代仓库事实）
    - memory_operation_records（memory 替代 operation_records）
    - memory_data_goal_anchor（memory 替代 current_data_goal_anchor）
    - completion_false（缺交付物却声明完成）
    - completion_sandbox_runtime（sandbox 成功冒充正式 runtime）
    - completion_rag_fact（RAG 摘要冒充事实）
    - completion_technical_content（技术成功冒充内容成功）
    - completion_file_exists（文件存在冒充任务完成）
    - completion_service_write（service output 冒充仓库写入）

forbidden_status_promotion_scan（禁止状态推进扫描）:
  status（状态）: passed
  method（方法）: 非 blocked 文件不得出现 runtime-enable true、main-branch-modified true、external-api-called true、dependency-installed true、service-started true、chroma-ingestion-run true、send-ready true、content-validation passed 等状态推进；blocked fixtures 中的负向样例允许出现并必须带 blocked: true 与 blocked_reasons
  note（说明）: `send_readiness_guard_not_falsely_promoted: true` 等护栏字段不是状态推进

secret_scan_result（密钥扫描结果）:
  status（状态）: passed
  scope（范围）: 本轮 schema / fixture / report / latest 变更
  note（说明）: 只出现 secret_scan / secret-like 规则说明，不含真实 API key、token、password 或 secret 值

forbidden_path_scan_result（禁止路径扫描结果）:
  status（状态）: passed
  forbidden_paths_touched（触碰禁止路径）: []
  unrelated_dirty_files（无关脏文件）:
    - public/（既有未跟踪目录，未触碰）

no_runtime_code_scan（无 runtime 代码扫描）:
  status（状态）: passed
  runtime_code_written（是否写 runtime 代码）: false
  code_files_created（是否创建代码文件）: false

runtime_code_written（是否写 runtime 代码）: false
runtime_enabled（是否启用 runtime）: false
main_branch_modified（是否修改 main）: false
external_api_called（是否调用外部 API）: false
dependency_installed（是否安装依赖）: false
service_started（是否启动服务）: false
chroma_ingestion_run（是否运行 Chroma 入库）: false
```

## 3. validation_commands（验证命令摘要）

```yaml
yaml_parse_check（YAML 解析检查）: ruby YAML.load_file over schema and fixture files
required_fields_check（必填字段检查）: custom read-only Ruby check over 7 target schema families
passing_fixture_check（通过样例检查）: case_type = passing and blocked != true
blocked_fixture_check（阻断样例检查）: case_type = blocked, blocked = true, blocked_reasons non-empty
forbidden_status_promotion_scan（禁止状态推进扫描）: blocked-aware status scan
secret_like_pattern_scan（密钥模式扫描）: rg over changed files
forbidden_path_scan（禁止路径扫描）: git status / path allowlist check
no_runtime_code_scan（无 runtime 代码扫描）: no .py / .ts / .js / .sh created under schema_contracts by this phase
main_branch_untouched_check（main 未修改检查）: branch remains adapter/agent-service-toolkit-sandbox
```

## 4. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）: no_service_graph_probe_after_user_chatgpt_review
blocked_before_next_phase_if（进入下一阶段前阻断条件）:
  - 用户 / ChatGPT 未复审本轮 schema / fixture
  - 需要启动 FastAPI / Docker / Postgres / Streamlit
  - 需要真实调用 DashVector / Chroma ingestion / 外部 API
  - 需要让 runtime 直接写仓库
  - 需要合并 main
  - blocked fixture 覆盖不完整
```
