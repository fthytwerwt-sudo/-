# 20260616 workflow_first_pre_integration_audit_report（工作流优先正式接入前审核报告）

## 1. executive_summary（执行摘要）

```yaml
task_result（任务结果）:
  status（状态）: pre_formal_integration_audit_completed（正式接入前审核已完成）
  project_route（项目路由）: video_factory（视频工厂）
  branch（分支）: adapter/agent-service-toolkit-sandbox
  execution_permission（执行权限）: report_and_matrix_only（只允许报告与接入表）
  formal_integration_allowed_now（当前是否允许正式接入整个项目）: no（不允许）
  runtime_enablement_allowed_now（当前是否允许启用运行时）: no（不允许）
  main_merge_allowed_now（当前是否允许合并 main）: no（不允许）
  service_start_allowed_now（当前是否允许启动服务）: no（不允许）
  stopline（停止线）: pre_formal_integration_stopline（正式接入前停止线）
```

本轮结论：

- 已确认《视频工厂》正式接入前必须按 workflow-first（工作流优先）处理，而不是把 agent-service-toolkit 当成一个整体直接塞入项目。
- 当前可继续的是：报告级审核、接入矩阵回审、后续 workflow contract 补丁或 no-service / no-write probe。
- 当前必须阻断的是：正式运行时启用、服务启动、真实 DashVector / Chroma / 外部 API 调用、main 合并、把 fake graph 成功写成正式运行时成功。
- 当前最关键缺口不是“是否能跑一个最小闭环”，而是剪辑执行 workflow 缺少专属 contract / fixture / probe，无法证明换聊天框后稳定执行到可发布候选片或合法阻断。

## 2. route_decision（路由判断）

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory（视频工厂）
  task_type（任务类型）:
    - mechanism_review_task（机制审核任务）
    - adapter_pre_integration_audit_task（适配正式接入前审核任务）
    - workflow_registry_audit_task（工作流注册表审核任务）
    - integration_matrix_report_task（接入表报告任务）
  workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
  execution_permission（执行权限）: pre_formal_integration_audit_only（只允许正式接入前审核）
  stopline（停止线）: pre_formal_integration_stopline（正式接入前停止线）
  missing_files（缺失文件）: []
```

## 3. files_read（已读取文件）

```yaml
core_files（核心文件）:
  - AGENTS.md
  - codex_log/latest.md
  - codex_source/00_codex_readme.md
  - codex_source/01_execution_rules.md
  - codex_source/13_execution_lane_and_parallel_rules.md
  - codex_source/19_project_state_action_router.md
  - codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md
  - project_source/20_codex_multi_agent_routing_note_for_gpt_project.md

adapter_reports（适配报告）:
  - codex_log/framework_adapter/20260614_agent_service_toolkit_sandbox_branch_context.md
  - codex_log/framework_adapter/20260615_formal_adapter_patch_plan.md
  - codex_log/framework_adapter/20260616_agent_service_toolkit_full_integration_master_plan.md
  - codex_log/framework_adapter/20260616_user_decision_record_and_contract_scope.md
  - codex_log/framework_adapter/20260616_contract_schema_phase_validation_report.md
  - codex_log/framework_adapter/20260616_no_service_graph_probe_report.md

schema_fixture_files（结构契约与验证样例文件）:
  schema_files_read（已读取 schema 文件数量）: 16
  passing_fixture_files_read（已读取通过样例数量）: 16
  blocked_fixture_files_read（已读取阻断样例数量）: 36
  probe_script（探测脚本）: codex_source/schema_contracts/probes/no_service_graph_probe.py

missing_files（缺失文件）: []
```

## 4. four_layer_audit（四层审核）

### 4.1 workflow_registry（工作流注册表）

当前仓库已有 6 类正式 workflow 索引：`copy_testing_flow`、`material_evidence_flow`、`aesthetic_editing_flow`、`quality_review_flow`、`data_review_flow`、`mechanism_repair_flow`。用户本轮提出的核心判断是“项目核心其实是几个 workflow”，因此本报告按业务执行链重新审核 6 个 workflow-first 注册候选。

#### 4.1.1 workflow_review_items（工作流审核项）

| workflow_name（工作流名称） | purpose（用途） | current_repo_support（当前仓库支持情况） | required_inputs（必需输入） | required_outputs（必需输出） | required_steps（必经步骤） | blocked_if（阻断条件） | done_when（完成标准） | current_status / current_gap（当前状态 / 缺口） | integration_decision（接入判断） |
|---|---|---|---|---|---|---|---|---|---|
| copy_to_video_workflow（文案到视频工作流） | 从锁定文案走到候选片或阻断。 | 部分由 copy_testing_flow、material_evidence_flow、aesthetic_editing_flow 共同覆盖。 | locked_copy_contract、material_detail_report、data_goal_anchor。 | publish_candidate_ready_for_human_review 或 blocked_publish_candidate_unavailable。 | 锁稿检查、素材证据、句组映射、TTS、字幕卡片、review_pack、completion_truth_check。 | 缺素材细节、缺数据目标锚点、缺 line_group 映射、只能交技术预览。 | 候选片可人工复审，或阻断原因完整。 | current_status: partial（部分支持）；current_gap: 缺端到端 workflow contract。 | contract_required（需要契约）：先补文案到视频工作流契约和 fixture。 |
| material_audit_workflow（素材解析工作流） | 把用户素材转成可剪辑的证据包。 | material_evidence_flow 支持，但与 cleaning / retrieval adapter 尚未真实桥接。 | 用户素材、录屏、图片、音频或路径说明。 | material_detail_report、material_evidence_contract、line_group_evidence_gate_report。 | 素材解析、时间码、证据强度、隐私风险、source_readback。 | 缺素材解析 skill、时间码、关键证据不可见、source_path 缺失。 | 素材报告能支撑后续句组级剪辑判断。 | current_status: partial（部分支持）；current_gap: 缺清洗/检索适配后的真实 metadata 保真探测。 | adapter_required（需要适配器）：需要 cleaning_adapter 与 source_readback_adapter。 |
| editing_execution_workflow（剪辑执行工作流） | 执行剪辑、字幕、音频、卡片和审片包。 | aesthetic_editing_flow 和 execution_rules 有强规则，但缺独立 workflow contract。 | script_to_timeline_map、tts_prosody_anchor_map、card_placement_decision、material_evidence_contract。 | timeline、subtitle、audio、cards、review_pack。 | line_group 映射、素材复用检查、TTS 路线、字幕卡片重叠、画面可读性、候选片预检。 | 缺任一剪辑输入、核心证据不可读、字幕卡片 high severity overlap、只产技术预览。 | 收口到可发布候选片待复审，或合法阻断。 | current_status: blocked_before_formal_integration（正式接入前阻断）；current_gap: 缺 editing_execution_contract 等专属契约。 | blocked_before_formal_integration（正式接入前阻断）：这是最优先补契约的 workflow。 |
| operation_data_review_workflow（运营数据复盘工作流） | 记录运营数据、复盘、决定下一变量。 | data_review_flow、operation_data_intake、operation_review 已存在。 | 截图、播放数据、评论、私信、咨询信号。 | operation_data_intake、operation_review、operation_next_variable_decision。 | 数据录入、缺口标记、阈值检查、下一变量草案。 | video_id / 时间窗不明、字段缺失、一次改多个变量、memory 替代仓库事实。 | 数据记录完整，下一变量只改一个。 | current_status: partial（部分支持）；current_gap: 缺运行时 memory 与 review_loop 边界回归探测。 | adapter_required（需要适配器）：只能做验证和 handoff，不改写事实。 |
| reference_to_execution_workflow（参考到执行工作流） | 把参考资料转成可执行锚点和偏离检查。 | AGENTS 与 codex_readme 要求 Reference-to-Execution Contract，但 workflow registry 未单列。 | 参考视频、图、声音、样片、原感稿、外部资料。 | reference_anchor、effect_targets、function_fields、deviation_check。 | 参考来源回读、可执行字段拆解、偏离检查、旧 reference 降权。 | 参考样本被锁死成固定流程、旧口径覆盖当前事实、缺偏离检查。 | 参考变成可执行目标，不替代正式事实。 | current_status: partial（部分支持）；current_gap: 缺独立 workflow contract 和 fixture。 | contract_required（需要契约）：先补参考到执行工作流契约。 |
| adapter_infrastructure_workflow（适配基础设施工作流） | 承载 adapter 设计、schema、fixture、probe 和矩阵。 | 已作为 candidate 登记，未启用。 | agent-service-toolkit 适配目标、schema / fixture、no-service probe。 | pre-integration audit、adapter boundary、integration matrix。 | 四层审核、状态边界、接入表、回审停止线。 | 未经确认就写入正式 workflow 索引、缺准入 fixture。 | 用户 / ChatGPT 回审后决定是否转正式候选补丁。 | current_status: candidate（候选）；current_gap: 缺 workflow_registry_schema 和准入 blocked case。 | blocked_before_formal_integration（正式接入前阻断）：本轮只作为候选，不启用。 |

### 4.2 contract_schema（契约结构）

#### 4.2.1 contract_schema_review_items（契约结构审核项）

| contract_name（契约名称） | current_status（当前状态） | meaning（含义） | covered_by_files（由哪些文件覆盖） | missing_fields（缺失字段） | risk_if_missing（缺失风险） | recommendation（建议） |
|---|---|---|---|---|---|---|
| graph_runtime_adapter（图运行时适配器） | exists（已存在） | 已有 schema / fixture / fake graph probe。 | `graph_runtime_adapter.schema.yaml`、相关 fixtures、`no_service_graph_probe.py`。 | 真实 LangGraph runtime 行为未验证。 | fake runner 被误读成正式运行时。 | 下一步只做 no-service runtime probe，不启服务。 |
| retrieval_manifest（检索清单） | exists（已存在） | 已要求 source_path、chunk_id、content_hash、source_readback_required。 | `retrieval_manifest.schema.yaml`、DashVector / Chroma fixtures。 | 真实 DashVector adapter 未验证。 | page_content-only 退化，RAG 摘要冒充事实。 | 进入 retrieval_cleaning_adapter_probe。 |
| source_readback_map（原文回读映射） | exists（已存在） | 已覆盖 missing / conflict / stale source blocked case。 | `source_readback_map.schema.yaml`、source_readback fixtures。 | 大规模文件行号回读未验证。 | 旧分支或摘要冒充当前事实。 | 增加真实路径回读 probe。 |
| cleaning_adapter（清洗适配器） | exists（已存在） | 已覆盖 secret scan、metadata、legacy blocker。 | `cleaning_adapter.schema.yaml`、cleaning fixtures。 | 自然语言任务包、文件类型路由真实链路未验证。 | 入库前泄露 secret 或丢 source metadata。 | 优先做 cleaning metadata preservation probe。 |
| service_contract_no_write（服务不写仓库契约） | exists（已存在） | 已规定 service 只能 route / retrieve / validate / handoff。 | `service_contract_no_write.schema.yaml`、service blocked fixtures。 | 真实 service no-write probe 未做。 | service 绕过 Codex 写仓库。 | 授权后才做 service no-write real probe。 |
| runtime_memory_boundary（运行时记忆边界） | exists（已存在） | 已规定 repo facts win。 | `runtime_memory_boundary.schema.yaml`、memory blocked fixtures。 | 与 operation_records 的动态回归未探测。 | memory 替代 Git / review_loop 事实。 | 保持 direct_embed，但加回归探测。 |
| completion_truth_check_node（完成真实性检查节点） | exists（已存在） | 已覆盖 false completion、sandbox runtime、RAG fact、technical-content 混淆。 | `completion_truth_check_node.schema.yaml`、completion blocked fixtures。 | 剪辑 workflow 的专属交付物清单未绑定。 | 文件存在或技术成功冒充最终完成。 | 绑定 editing / review_pack 专属 contract。 |
| editing_execution_contract（剪辑执行契约） | missing（缺失） | 用户最关心的剪辑 workflow 还没有独立契约。 | 目前散落在 `aesthetic_editing_flow` 与 `execution_rules`。 | timeline、subtitle、audio、cards、review_pack、media probe、done_when。 | Codex 只交 technical preview 或 route card。 | 下一轮优先补。 |
| timeline_assembly_contract（时间线装配契约） | missing（缺失） | 缺少时间线装配输入输出结构。 | 无独立文件。 | track、timecode、source segment、line_group binding。 | 文案画面对不上、素材重复或错位。 | 随 editing contract 一起补。 |
| subtitle_card_overlap_contract（字幕卡片重叠契约） | partial（部分） | execution_rules 有闸门，schema / fixture 缺失。 | `codex_source/01_execution_rules.md`。 | overlap severity、evidence region、repair action。 | 字幕卡片遮挡核心证据。 | 补 schema 和 blocked fixture。 |
| tts_route_contract（TTS 路线契约） | partial（部分） | 执行规则有 B 方案和 TTS 路线要求，适配契约未落。 | `codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`。 | provider、model、voice_id、fallback flag、non_silent check。 | 未授权 fallback 冒充正式音频。 | 补 TTS route contract。 |
| review_pack_contract（审片包契约） | missing（缺失） | 缺少候选片审片包结构契约。 | 现有 review_pack 规则散落在执行规则。 | media probe、preflight reports、remaining blockers、human review fields。 | 审片包不完整却声明完成。 | 补 review_pack contract。 |
| workflow_registry_schema（工作流注册表结构契约） | missing（缺失） | 没有正式 workflow / candidate workflow 注册结构。 | 当前只有 workflow entry routing index。 | workflow id、scope、input、output、admission fixture、blocked cases。 | 候选 workflow 被误启用。 | 补 workflow registry schema。 |

### 4.3 adapters（适配器）

#### 4.3.1 adapter_review_items（适配器审核项）

| adapter_name（适配器名称） | role（角色） | current_status（当前状态） | proven_scope（已证明范围） | not_proven_scope（未证明范围） | allowed_actions（允许动作） | forbidden_actions（禁止动作） | required_next_probe（下一步所需探测） | integration_decision（接入判断） |
|---|---|---|---|---|---|---|---|---|
| cleaning_adapter（清洗适配器） | 源文件安全加载、清洗、切片、元数据保真。 | schema / fixture exists；真实链路未探测。 | fixture 可表达 secret scan、metadata、source_readback index。 | 自然语言输入转 task packet、真实文件 loader、真实 metadata 保真。 | 安全加载、secret scan、输出 task_type / route / must_read / blocked_if。 | 未扫描就入库、丢 source_path、旧事实覆盖当前事实。 | retrieval_cleaning_adapter_probe。 | adapter_required（需要适配器）：先写边界，不进入正式运行。 |
| retrieval_adapter（检索适配器） | DashVector / Chroma 输出转 RetrievalManifest。 | schema / fixtures exists。 | DashVector fixture 与 Chroma sandbox fixture 可转 manifest。 | 真实 DashVector 调用、collection / dimension / score 校验。 | 输出 provider、source_path、chunk_id、score、authority。 | Chroma 替代 DashVector、page_content-only。 | DashVector fixture-to-manifest probe。 | adapter_required（需要适配器）。 |
| source_readback_adapter（原文回读适配器） | 检索结果回到仓库原文和行号。 | schema / fixtures exists。 | missing / conflict / stale source blocked case 已覆盖。 | 多文件、复杂行号、旧分支冲突的真实回归。 | 读取当前分支源文件、生成 exact_excerpt。 | RAG 摘要替代 repo facts。 | source readback conflict probe。 | adapter_required（需要适配器）。 |
| langgraph_adapter（LangGraph 图编排适配器） | 将 graph 作为 workflow runtime layer。 | candidate；本地未证明真实 LangGraph 可用。 | fake_graph_runner_no_dependency 可跑 7 节点和 9 阻断。 | 真实 LangGraph runtime、interrupt、state persistence。 | 后续 no-service / no-write / runtime probe。 | 替代 Project State Action Router、直接写仓库。 | real LangGraph no-service probe。 | probe_required（需要探测）。 |
| codex_executor_adapter（Codex 执行器适配器） | 保持 Codex 为唯一写入执行层。 | exists as policy and handoff shape。 | active_write_executor = codex 在报告、schema、fixtures 中一致。 | service/runtime 到 Codex 的真实 handoff 自动化。 | 接收 handoff、限定路径写入、验证、commit、push。 | service/runtime/memory 绕过 Codex 写文件。 | executor handoff regression probe。 | direct_embed（可直接嵌入）。 |
| deepseek_supply_adapter（DeepSeek 供料适配器） | 条件只读供料和风险复核。 | policy exists；本轮未触发。 | 只读、不写文件、不拍板事实边界清楚。 | 真实 DeepSeek 供料包与 token 使用观察。 | 预读取、风险报告、冲突二次意见。 | 写文件、替代 ChatGPT / 用户判断、替代仓库事实。 | conditional supply readback probe。 | direct_embed（可直接嵌入）。 |

### 4.4 policy_rules（策略规则）

#### 4.4.1 policy_rule_review_items（策略规则审核项）

| policy_name（策略名称） | current_status（当前状态） | protected_risk（保护的风险） | current_coverage（当前覆盖情况） | gap（缺口） | must_hold_before_formal_integration（正式接入前必须满足） |
|---|---|---|---|---|---|
| no_degrade_completion_gate（禁止降级完成闸门） | exists（已存在） | 技术预览、fallback、route card 冒充完成。 | AGENTS、codex_readme、execution_rules、completion truth fixtures。 | 剪辑 workflow 的完整交付物清单还未契约化。 | 必须绑定 editing_execution_contract 和 review_pack_contract。 |
| status_promotion_guardrail（状态推进护栏） | exists（已存在） | 技术成功、沙盒成功、报告生成偷换成更高状态。 | workflow index、schema fixtures、probe report。 | 后续每个 workflow 需要专属状态扫描。 | 每次接入前都跑 forbidden status scan。 |
| main_merge_gate（main 合并闸门） | exists（已存在） | adapter 分支结果自动进入 main。 | branch context、latest、用户决策记录。 | 缺 main merge candidate review contract。 | 用户 / ChatGPT 回审、secret scan、远端 HEAD 证据齐全。 |
| external_api_gate（外部 API 闸门） | exists（已存在） | 未授权调用 DashVector、Chroma ingestion、model API。 | 报告和 schema 均要求不调用外部 API。 | 授权流程 contract 未单列。 | 未授权时只允许 fixture / local probe。 |
| service_runtime_write_boundary（服务 / 运行时写入边界） | exists（已存在） | service/runtime/memory 写仓库或替代事实。 | service_contract_no_write、runtime_memory_boundary、write_executor_handoff。 | 真实 service probe 未做。 | service 只能 handoff，Codex 才能写。 |
| fallback_authorization_gate（降级授权闸门） | exists（已存在） | fallback 未经用户授权冒充完成。 | AGENTS、codex_readme、execution_rules。 | 缺 fallback-specific blocked fixture。 | fallback 只能作为 blocked 后建议，用户授权前不得完成。 |

## 5. editing_workflow_focus（剪辑工作流重点审核）

### 5.1 why_focus（为什么单独重点审核）

用户最新判断强调：项目核心是几个 workflow，尤其要让 Codex 在执行阶段能完整执行，最关心剪辑阶段。当前最小闭环只能证明局部契约链路能检查，不能证明真实剪辑产物能稳定完成，也不能证明换聊天框后仍能按同一套输入、输出、阻断和完成标准执行。

### 5.2 required_inputs（剪辑阶段当前需要哪些输入）

```yaml
editing_required_inputs（剪辑阶段必需输入）:
  - script_to_timeline_map（文案到时间线映射表）: 必须 line_group 级别，不得只有段落级。
  - tts_prosody_anchor_map（TTS 韵律锚点表）: 必须写清 provider / model / voice / fallback 边界。
  - card_placement_decision（卡片位置判断）: 必须说明卡片是否需要、绑定哪一句、是否遮挡证据。
  - material_evidence_contract（素材证据契约）: 每个 line_group 的素材证据或卡片承接必须明确。
  - material_usage_ledger（素材使用台账）: 必须防止重复使用、弱相关素材冒充直接证据。
  - subtitle_card_overlap_check（字幕卡片重叠检查）: 必须有 severity 和 repair action。
  - review_pack_requirement（审片包要求）: 必须包含媒体探针、预检报告、remaining blockers。
```

### 5.3 easy_to_miss_outputs（剪辑阶段最容易漏哪些交付物）

- `timeline（时间线）`: 有片段顺序还不够，必须能回到 line_group 和 source segment。
- `subtitle（字幕）`: 不能遮挡证据，不能改变 locked copy 语义。
- `audio（音频）`: 不能无声，不能用未授权 fallback 冒充正式路线。
- `cards（卡片）`: 不能替代真实证据，不能盖住关键 UI 或数据。
- `review_pack（审片包）`: 不能只给媒体文件，必须带 preflight、probe、remaining_blockers。
- `completion_truth_check（完成真实性检查）`: 必须区分候选片、内部诊断、阻断。

### 5.4 anti_technical_preview_completion（如何防止只交 technical_preview）

```yaml
anti_technical_preview_completion（防止技术预览冒充完成）:
  rule（规则）: 剪辑 workflow 的 done_when 只能是可发布候选片待人工复审，或可发布候选片不可交付阻断。
  blocked_if（阻断）:
    - 缺音频、字幕、卡片、review_pack 或关键素材证据。
    - 只有 JSON / Markdown / route card / silent preview。
    - 画面可读性或字幕卡片重叠未检查。
    - TTS fallback 未经授权。
    - 无法证明每个 line_group 的画面承接。
  required_truth_check（必需真实性检查）:
    - required_outputs_exist（必交付物存在）
    - source_readback_passed（原文回读通过）
    - blocked_cases_checked（阻断样例检查过）
    - forbidden_status_promotion_scan（禁止状态推进扫描）
```

### 5.5 closeout_path（剪辑阶段如何收口）

剪辑 workflow 只能有两个合法出口：

1. `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`
   - 仅代表候选片具备人工复审条件。
   - 不代表发送状态开启。
   - 不代表内容、声音、视觉最终通过。

2. `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`
   - 必须写明缺哪一层：素材、line_group、TTS、字幕、卡片、审片包、API 授权、媒体探针或人工复审。
   - 不得用 fallback 包装成完成。

### 5.6 missing_editing_contracts（当前接入前还缺哪些剪辑 workflow contract）

```yaml
missing_editing_contracts（缺失剪辑契约）:
  - editing_execution_contract（剪辑执行契约）
  - timeline_assembly_contract（时间线装配契约）
  - subtitle_card_overlap_contract（字幕卡片重叠契约）
  - tts_route_contract（TTS 路线契约）
  - review_pack_contract（审片包契约）
  - media_probe_contract（媒体探针契约）
  - publish_candidate_or_blocked_contract（候选片或阻断收口契约）
```

## 6. pre_formal_integration_stopline（正式接入前停止线）

```yaml
pre_formal_integration_stopline（正式接入前停止线）:
  reached（本轮已经到哪里）:
    - 已完成 workflow-first 四层审核。
    - 已生成 integration_matrix（接入表）。
    - 已明确剪辑 workflow 是正式接入前最关键缺口。
  must_not_cross（还不能越过哪里）:
    - 不能正式启用运行时。
    - 不能启动服务。
    - 不能真实调用 DashVector / Chroma / 外部 API。
    - 不能把 fake graph 成功写成正式运行时成功。
    - 不能把报告生成写成项目机制长期稳定。
    - 不能合并 main。
  review_required（继续前需要复审）:
    - 用户 / ChatGPT 必须先回审本报告和接入表。
    - 下一轮只能在回审后选择 workflow_contract_patch_or_probe（工作流契约补丁或探测）。
```

## 7. next_recommended_goal（下一轮建议目标）

```yaml
next_recommended_goal（下一轮建议目标）:
  recommendation（建议）: user_chatgpt_review_then_workflow_contract_patch_or_probe（用户 / ChatGPT 回审后，再做工作流契约补丁或探测）
  preferred_first_target（建议首个目标）: editing_execution_workflow_contract_patch（剪辑执行工作流契约补丁）
  not_recommended（不建议）:
    - formal runtime enablement（正式启用运行时）
    - service start（启动服务）
    - main merge（合并 main）
```

## 8. audit_summary（审核摘要）

```yaml
four_layer_audit_summary（四层审核摘要）:
  workflow_registry（工作流注册表）:
    status（状态）: partial_needs_review（部分具备，需要回审）
    meaning（含义）: 现有 6 类 workflow 可承载当前机制，但用户提出的 6 个 workflow-first 注册候选还缺 workflow registry schema。
  contract_schema（契约结构）:
    status（状态）: partial_with_critical_editing_gap（部分具备，但剪辑缺口关键）
    meaning（含义）: graph / retrieval / readback / cleaning / service / memory / truth check 已有静态契约；剪辑专属 contract 缺失。
  adapters（适配器）:
    status（状态）: adapter_boundaries_known_but_real_chain_unproven（边界已知，但真实链路未证明）
    meaning（含义）: Codex、source_readback、truth check 可直接保留；cleaning / retrieval / LangGraph / service 仍需探测。
  policy_rules（策略规则）:
    status（状态）: guardrails_exist_but_need_workflow_binding（护栏存在，但需绑定 workflow）
    meaning（含义）: 禁止降级完成、状态推进、main 合并、外部 API、服务写仓库等护栏已存在；剪辑 workflow 需要专属完成真实性检查绑定。
```
