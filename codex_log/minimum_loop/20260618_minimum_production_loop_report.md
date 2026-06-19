# 20260618 Minimum Production Loop Report

```yaml
report_type（报告类型）: minimum_production_loop（最小产出闭环）
project_route（项目路由）: video_factory（视频工厂）
task_result.status（任务结果状态）: blocked_with_missing_inputs（因缺输入而阻断）
meaning（含义）: 已用当前视频工厂真实入口跑到执行前判断；当前不能生成新最小候选，必须先补齐用户侧最小输入和授权。
branch（分支）: main
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

## 1. Route Decision（路由判断）

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory（视频工厂）
  task_type（任务类型）:
    - minimum_production_loop（最小产出闭环）
    - real_task_preflight_to_candidate（真实任务从执行前检查到候选产出）
    - framework_usage_validation（框架使用验证）
    - blocked_gap_report_if_needed（必要时输出阻断缺口报告）
  responsibility_layer（责任层级）:
    - project_judgment_layer（项目判断层）
    - validation_layer（验收复审层）
    - mechanism_fix_layer（机制修补层）
    - sync_layer（同步回写层）
  workflow_route_decision（workflow 归位判断）: mechanism_repair_flow（机制修补流）为主，data_review_flow（数据复盘流）提供事实输入
  large_task_gate（大任务闸门）:
    triggered（是否触发）: true（触发）
    reason（原因）: 读取多份项目事实、运营记录、复审包和工程规则，并需要报告 / latest / Git 同步。
  execution_permission（执行权限）: report_latest_only（只允许报告、latest、验证和 Git 同步）
```

## 2. Source Readback Manifest（原文回读清单）

```yaml
source_readback_manifest（原文回读清单）:
  required_sources_read（已读取必需来源）:
    - path（路径）: AGENTS.md
      purpose（用途）: 读取多项目路由、视频工厂单工作区、状态边界和 Git 规则。
    - path（路径）: codex_log/latest.md
      purpose（用途）: 读取上一轮真实任务干跑状态与下一步输入缺口。
    - path（路径）: codex_source/00_codex_readme.md
      purpose（用途）: 读取 Codex 正式接手入口和视频交付状态边界。
    - path（路径）: codex_log/engineering_line_plain_manual/05_项目总规则_用户决策版.md
      purpose（用途）: 读取用户决策版权限边界。
    - path（路径）: codex_log/engineering_line_audit/20260618_goal_mode_safe_engineering_fusion_report.md
      purpose（用途）: 读取安全工程融合后允许 / 禁止状态。
    - path（路径）: codex_log/engineering_line_audit/20260618_real_task_dry_run_preflight_report.md
      purpose（用途）: 读取上一轮真实任务干跑的输入缺口和验证边界。
    - path（路径）: codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
      purpose（用途）: 读取本地 preflight 探测要求。
    - path（路径）: codex_source/schema_contracts/schemas/rag_default_decision.schema.yaml
      purpose（用途）: 读取 RAG 默认判断边界。
    - path（路径）: codex_source/schema_contracts/schemas/engineering_state_map.schema.yaml
      purpose（用途）: 读取工程状态地图边界。
    - path（路径）: codex_source/schema_contracts/schemas/evaluator_result.schema.yaml
      purpose（用途）: 读取评估结果边界。
    - path（路径）: codex_source/schema_contracts/schemas/failure_route.schema.yaml
      purpose（用途）: 读取失败路由边界。
    - path（路径）: codex_source/schema_contracts/schemas/human_decision_gate.schema.yaml
      purpose（用途）: 读取人工决策闸门边界。
    - path（路径）: codex_source/schema_contracts/schemas/guardrail_result.schema.yaml
      purpose（用途）: 读取护栏边界。
  optional_sources_read（已读取可选来源）:
    - path（路径）: codex_log/current_operation_target.md
      purpose（用途）: 判断当前运营目标和是否可进入下一期正式执行。
    - path（路径）: codex_log/current_publish_target.md
      purpose（用途）: 判断是否已有发布候选以及候选状态边界。
    - path（路径）: codex_log/current_data_goal_anchor.md
      purpose（用途）: 判断当前数据目标锚点和下一期执行是否 ready。
    - path（路径）: review_loop/operation_records_index.md
      purpose（用途）: 判断 V001-V005 样本状态与当前 target。
    - path（路径）: review_loop/decision_engine/latest_operation_decision_report.md
      purpose（用途）: 读取系统对下一期正式执行的自动阻断结论。
    - path（路径）: review_loop/decision_engine/final_user_operation_result.md
      purpose（用途）: 读取用户侧运营结果结论和缺失字段。
    - path（路径）: dist/latest_review_pack/summary.json
      purpose（用途）: 判断最新复审包是否可作为当前新候选输入。
    - path（路径）: dist/latest_review_pack/review_manifest.md
      purpose（用途）: 判断复审清单状态边界。
    - path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/review_manifest.md
      purpose（用途）: 判断既有 V006 候选是否可复用为本轮候选。
    - path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/locked_copy_contract.md
      purpose（用途）: 判断既有 V006 锁定文案是否属于本轮输入。
    - path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/material_inventory.json
      purpose（用途）: 判断既有 V006 素材清单是否属于本轮输入。
    - path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/summary.json
      purpose（用途）: 判断既有 V006 候选状态与剩余人审问题。
    - path（路径）: review_loop/learning_ledger/next_episode_bet_card.md
      purpose（用途）: 判断下一期低置信度方向。
    - path（路径）: review_loop/learning_ledger/current_copy_revision_handoff.md
      purpose（用途）: 判断下一期文案是否已可执行。
    - path（路径）: review_loop/learning_ledger/operation_learning_memory.md
      purpose（用途）: 判断运营学习是否足以触发新片执行。
    - path（路径）: review_loop/copy_iteration/latest_copy_iteration_report.md
      purpose（用途）: 判断文案迭代状态。
    - path（路径）: review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md
      purpose（用途）: 判断 V003 下一版简报是否可作为正式脚本。
    - path（路径）: review_loop/copy_iteration/V005/V005_copy_structure_map.json
      purpose（用途）: 判断 V005 学习样本是否可作为正式脚本。
  source_readback_status（事实源回读状态）: read_ok（已回读）
  real_rag_call_status（真实 RAG 调用状态）: not_called（未调用）
```

## 3. Minimum Loop Input Check（最小闭环输入检查）

```yaml
minimum_loop_input_check（最小闭环输入检查）:
  target_or_topic（目标或选题）:
    status（状态）: partial_found_but_not_executable（部分找到但不可执行）
    source（来源）:
      - codex_log/current_operation_target.md
      - review_loop/decision_engine/latest_operation_decision_report.md
      - review_loop/learning_ledger/next_episode_bet_card.md
    readback（原文回读结论）: 当前运营目标仍是 V003 数据回流；下一期方向只有低置信度准备，不是正式新视频任务输入。
  copy_or_script（文案或脚本）:
    status（状态）: missing_for_current_minimum_loop（当前闭环缺失）
    source（来源）:
      - review_loop/learning_ledger/current_copy_revision_handoff.md
      - review_loop/copy_iteration/latest_copy_iteration_report.md
      - dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/locked_copy_contract.md
    readback（原文回读结论）: V006 有既有锁定文案，但它属于已生成候选；当前下一期只有低置信度准备，不能当作正式 locked copy（锁定文案）。
  material_or_gap（素材或素材缺口）:
    status（状态）: missing_for_next_task（下一条任务缺失）
    source（来源）:
      - dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/material_inventory.json
      - review_loop/decision_engine/final_user_operation_result.md
    readback（原文回读结论）: V006 有既有素材清单，但与当前下一期新任务未绑定；不能用旧候选素材冒充新任务素材证据。
  rag_authorization（RAG 授权）:
    status（状态）: not_authorized_for_real_call（未授权真实调用）
    source（来源）:
      - codex_log/latest.md
      - codex_log/engineering_line_plain_manual/05_项目总规则_用户决策版.md
    readback（原文回读结论）: RAG 默认进入判断链，但本轮没有 DashVector / Chroma 真实调用授权。
  tts_api_media_authorization（TTS / API / 媒体授权）:
    status（状态）: not_authorized（未授权）
    source（来源）:
      - codex_log/latest.md
      - codex_log/engineering_line_plain_manual/05_项目总规则_用户决策版.md
    readback（原文回读结论）: 本轮未授权 TTS、外部 API 或媒体生成。
```

## 4. Preflight Result（执行前检查结果）

```yaml
preflight_result（执行前检查结果）:
  route_decision（路由判断）: passed_for_report_only（仅报告链路通过）
  engineering_state_map_check（工程状态地图检查）: passed_with_blocked_execution（状态地图允许阻断，不允许执行产出）
  RAG_default_decision（RAG 默认判断）:
    default_route_enabled（默认路线启用）: true（已启用为判断链）
    real_external_call_allowed（是否允许真实外部调用）: false（不允许）
    source_readback_required（是否必须原文回读）: true（必须）
  source_readback_requirement（原文回读要求）: satisfied_by_local_repo_files（已由本地仓库文件满足）
  tool_permission_check（工具权限检查）:
    runtime（运行时）: forbidden（禁止）
    service（服务）: forbidden（禁止）
    external_api（外部 API）: forbidden_without_authorization（未授权禁止）
    dashvector_real_call（DashVector 真实调用）: forbidden_without_authorization（未授权禁止）
    chroma_ingestion（Chroma 入库）: forbidden_without_authorization（未授权禁止）
    media_generation（媒体生成）: forbidden_without_authorization（未授权禁止）
  copy_permission_check（文案权限检查）:
    can_format_existing_locked_copy（能否格式化既有锁定文案）: true（可在授权范围内格式化）
    can_change_semantics（能否改语义）: false（不可）
    current_executable_copy_found（是否找到当前可执行文案）: false（未找到）
  card_decision_check（卡片判断检查）:
    current_card_generation_allowed（当前是否允许生成卡片）: false（不允许）
    reason（原因）: 无当前新任务 locked copy（锁定文案）和素材证据绑定。
  material_evidence_check（素材证据检查）:
    existing_v006_material_manifest_found（找到既有 V006 素材清单）: true（找到）
    material_bound_to_current_new_task（素材是否绑定当前新任务）: false（否）
    weak_or_old_material_may_replace_evidence（弱相关或旧素材能否替代证据）: false（不能）
  evaluator_failure_guardrail_check（评估失败护栏检查）:
    technical_success_as_content_success_forbidden（禁止技术成功冒充内容成功）: true（禁止）
    dry_run_as_output_forbidden（禁止干跑冒充真实产出）: true（禁止）
    old_candidate_as_new_candidate_forbidden（禁止旧候选冒充本轮新候选）: true（禁止）
  human_decision_gate（人工决策闸门）:
    required（是否需要人工决策）: true（需要）
    decision_needed（需要决策）:
      - 选择本轮到底使用既有 V006 候选继续人审，还是选择下一条新视频任务。
      - 如果做下一条新视频，提供目标 / 选题、locked copy（锁定文案）或可执行草稿。
      - 明确素材路径或允许无素材候选包。
      - 明确是否授权真实 RAG、TTS、外部 API 或媒体生成。
```

## 5. Candidate Decision（候选判断）

```yaml
candidate_decision（候选判断）:
  can_enter_minimum_candidate_attempt（是否能进入最小候选尝试）: false（不能）
  final_allowed_result（本轮允许结果）: blocked_with_missing_inputs（因缺输入而阻断）
  candidate_path（候选产出路径）: not_applicable（不适用）
  existing_candidate_disambiguation（既有候选澄清）:
    v006_candidate_exists（V006 候选是否存在）: true（存在）
    v006_can_be_claimed_as_this_round_output（V006 能否写成本轮产出）: false（不能）
    reason（原因）: V006 是既有候选，且仍需人审；本轮目标是用当前真实任务入口跑最小闭环，不能把历史产物改写成本轮新产出。
```

## 6. Blocked Result（阻断结果）

```yaml
blocked_result（阻断结果）:
  blocked_reason_summary（阻断原因摘要）: 当前仓库能找到运营目标、既有候选和低置信度下一期方向，但缺少一个可执行的新视频任务包；继续生成会越过数据目标、人审和授权边界。
  missing_inputs（缺失输入）:
    - item（项目）: current_task_choice（当前任务选择）
      why_needed（为什么需要）: 需要先确认本轮是继续 V006 人审，还是启动下一条新视频最小候选。
      how_user_can_provide（用户怎么提供）: 直接说“继续 V006 人审”或“做下一条新视频，主题是 X”。
    - item（项目）: locked_copy_or_executable_draft（锁定文案或可执行草稿）
      why_needed（为什么需要）: Codex 不能擅自改标题、核心判断或语义；没有可执行文案就不能装配候选。
      how_user_can_provide（用户怎么提供）: 粘贴最终文案 / 草稿，或明确授权 ChatGPT 先定稿后交给 Codex。
    - item（项目）: material_path_or_no_material_permission（素材路径或无素材候选授权）
      why_needed（为什么需要）: 视频工厂不能伪造素材证据，也不能用旧素材冒充新任务证据。
      how_user_can_provide（用户怎么提供）: 提供本地素材目录 / 文件路径，或明确说“这轮只做无素材 preflight pass package（执行前检查通过包）”。
    - item（项目）: rag_authorization_decision（RAG 授权决定）
      why_needed（为什么需要）: RAG 已是默认判断链，但真实调用 DashVector / Chroma 仍需授权。
      how_user_can_provide（用户怎么提供）: 选择“只用本地回读”或“授权真实 DashVector / Chroma 调用范围”。
    - item（项目）: tts_api_media_authorization_decision（TTS / API / 媒体授权决定）
      why_needed（为什么需要）: 没有授权就不能调用 TTS、外部 API 或生成媒体。
      how_user_can_provide（用户怎么提供）: 明确授权范围，或说明本轮不需要声音 / 外部 API / 媒体生成。
  auto_handled_items（AI 已自动处理项）:
    - 已完成项目路由、工作流归位和大任务闸门判断。
    - 已回读当前运营目标、数据目标锚点、决策引擎结果、既有 V006 候选与文案 / 素材清单。
    - 已确认当前下一期正式执行仍被运营数据缺口阻断。
    - 已确认本轮没有 runtime、service、外部 API、TTS、真实 RAG 或媒体生成授权。
  cannot_auto_handle_items（不能自动处理项）:
    - 不能替用户选择当前是继续 V006 还是启动新任务。
    - 不能替 ChatGPT / 用户定稿新 locked copy（锁定文案）。
    - 不能伪造或替换素材证据。
    - 不能在未授权时调用真实 RAG、TTS、外部 API 或媒体生成。
  next_minimum_user_input（用户下一步最小输入）:
    - 选一条路径：继续 V006 人审，或启动下一条新视频。
    - 如果启动新视频，补一个目标 / 选题和 locked copy（锁定文案）或可执行草稿。
    - 提供素材路径，或明确允许只做无素材 preflight pass package（执行前检查通过包）。
    - 明确真实 RAG 与 TTS / API / 媒体生成授权边界。
```

## 7. Allowed Actions（允许动作）

```yaml
allowed_actions（允许动作）:
  - local_source_readback（本地原文回读）
  - formal_preflight_judgment（正式执行前判断）
  - blocked_production_package（阻断产出包）
  - latest_update（latest 更新）
  - validation_probe_run（验证探测运行）
  - whitelist_git_stage_commit_push（白名单 Git 暂存 / 提交 / 推送）
```

## 8. Blocked Actions（阻断动作）

```yaml
blocked_actions（阻断动作）:
  - minimum_candidate_package_generation（生成最小候选包）
  - locked_copy_semantic_change（修改锁定文案语义）
  - old_candidate_relabel_as_new_output（旧候选改写成本轮新产出）
  - weak_material_claimed_as_evidence（弱相关素材冒充证据）
  - runtime_enablement（启用运行时）
  - service_start（启动服务）
  - external_api_call（调用外部 API）
  - tts_call（调用 TTS）
  - dashvector_real_call（真实调用 DashVector）
  - chroma_ingestion_run（运行 Chroma 入库）
  - media_generation（生成媒体）
  - content_validation_promotion（推进内容验证）
  - send_ready_promotion（推进可发送状态）
  - production_readiness_claim（声称生产可用）
```

## 9. Project Adjustment Backlog（后续项目调整清单）

```yaml
project_adjustment_backlog（后续项目调整清单）:
  must_fix_before_next_candidate（下一次候选产出前必须修）:
    - current_task_selector（当前任务选择器）: 把“继续既有候选人审”与“启动下一条新视频”拆成显式选择。
    - prewrite_copy_decision_card（写前文案决策卡）: 新视频进入候选前必须有目标、标题、核心判断、允许改动和禁止改动。
    - material_binding_card（素材绑定卡）: 素材必须绑定到当前任务，不得默认继承旧候选素材。
    - authorization_card（授权卡）: 真实 RAG、TTS、外部 API、媒体生成必须逐项写明 allowed / forbidden。
  can_fix_after_minimum_loop（最小闭环后可修）:
    - latest_task_pointer（最新任务指针）: 在 latest 或单独索引里给出当前最小闭环入口，减少 V003 / V006 / 下一期准备混淆。
    - candidate_vs_human_review_boundary（候选与人审边界）: 把既有候选继续人审和新候选生成分成两个 route。
    - low_confidence_preparation_lane（低置信度准备车道）: 允许低置信度准备，但不得自动升成正式执行。
  do_not_fix_now（现在不要修）:
    - runtime_hardening（运行时加固）
    - service_integration（服务接入）
    - large_schema_expansion（大规模 schema 扩展）
    - fixture_family_expansion（fixture 家族扩展）
    - real_rag_call（真实 RAG 调用）
    - media_rendering_pipeline（媒体渲染链路）
    - existing_candidate_rework（既有候选回炉重做）
```

## 10. Validation Commands（验证命令）

```yaml
validation_commands（验证命令）:
  required（必需）:
    - command（命令）: python3 codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
      result（结果）: passed（通过）
      evidence（证据）: final_probe_status=passed, blocked_fixture_result=blocked_passed, runtime_enabled=false
    - command（命令）: python3 codex_source/schema_contracts/probes/engineering_state_map_probe.py
      result（结果）: passed（通过）
      evidence（证据）: final_probe_status=passed, schema_result=passed, runtime_enabled=false
    - command（命令）: python3 codex_source/schema_contracts/probes/rag_default_decision_probe.py
      result（结果）: passed（通过）
      evidence（证据）: final_probe_status=passed, real_external_call_allowed=false
    - command（命令）: python3 codex_source/schema_contracts/probes/evaluator_failure_guardrail_probe.py
      result（结果）: passed（通过）
      evidence（证据）: final_probe_status=passed, content_validation=not_promoted, send_ready=false
    - command（命令）: python3 codex_source/schema_contracts/probes/report_trace_log_validator.py
      result（结果）: passed（通过）
      evidence（证据）: final_probe_status=passed, latest_top_section_result=passed
    - command（命令）: git diff --check
      result（结果）: passed（通过）
      evidence（证据）: no whitespace errors（无空白错误）
    - command（命令）: forbidden status promotion scan（禁止状态推进扫描）
      result（结果）: passed（通过）
      evidence（证据）: no forbidden status promotion hit in latest/report（latest 和报告无禁止状态推进命中）
    - command（命令）: secret scan（密钥扫描）
      result（结果）: passed（通过）
      evidence（证据）: added lines and new report have no secret-like value; full latest broad scan only saw historical placeholder text without secret value（新增行和新报告无密钥样式值；latest 全文宽扫仅见历史占位说明，无密钥值）
  new_script_py_compile（新增脚本编译）: not_applicable（本轮没有新增脚本）
```

```yaml
validation_summary（验证摘要）:
  all_required_probes_passed（所有必需探测是否通过）: true（通过）
  git_diff_check（Git 差异检查）: passed（通过）
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed（通过）
  secret_scan（密钥扫描）: passed（通过）
  modified_scope_check（修改范围检查）: passed_only_allowed_files（仅修改允许文件）
```

## 11. Status Not Promoted（未推进状态）

```yaml
status_not_promoted（未推进状态）:
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
