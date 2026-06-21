# 20260621 用户可读 RAG 决策运行图与 LangGraph 审查说明

## 1. 先说清楚：文件不等于自动判断

现在仓库里已经有设计报告、审查指南、trace 和 latest 记录，但这些文件本身不是自动驾驶系统。

```yaml
files_vs_runtime:
  文件_files: 只是规则、契约、检查表、字段说明和审查入口。
  自动判断_runtime_decision: 必须由 runner / graph / validator 真正执行，把输入、状态、分支和输出串起来。
  结论: 只有文件存在，不代表 Codex 每次都会自动判断；必须把文件接进运行图，才能稳定触发判断。
```

换成人话就是：文件像交通规则，runner / graph 像实际路口红绿灯。只有规则写在纸上，车不会自动停；规则被接进运行图，Codex 才能按节点一步一步判断。

## 2. LangGraph 是什么

```yaml
LangGraph:
  meaning: 把一个复杂判断拆成多个节点，每个节点只做一件事，然后根据结果决定下一步去哪。
  why_needed: 防止 Codex 一次性凭感觉判断，也防止旧口径、过期索引、目标态计划混进当前事实。
  can_be_replaced_by: 第二轮可以先用 Python runner 实现等价状态机，不一定一开始就引入 LangGraph 库。
```

人话解释：

- 普通 prompt 像“请你综合判断一下”，容易把很多层混在一起。
- LangGraph / 状态机像“先过安检，再进候机区，再登机”，每一步有入口、出口、阻断条件和失败去向。
- 对当前 RAG 决策工程线来说，最重要的不是一开始就上框架，而是先把“每一步怎么判断、失败去哪、留下什么证据”固定下来。

## 3. RAG 决策运行图

```text
用户任务输入
-> 任务分类
-> 检查 RAG 是否过期
-> 检索候选资料
-> 回读仓库原文
-> 清洗旧口径
-> 检查冲突组
-> 先过硬闸门
-> 再做加权决策
-> 选出当前最优动作
-> 输出决策审计报告
-> 生成 Codex 供料包
-> Codex 才能执行
```

关键边界：

```yaml
runtime_boundary:
  hard_gate_before_weight: true
  source_readback_before_claim: true
  stale_index_can_reference_but_cannot_directly_decide_high_risk_task: true
  decision_audit_required_before_codex_execution: true
  implementation_status: design_review_only_not_implemented
```

## 4. 运行节点说明

### 4.1 task_classifier

```yaml
runtime_node:
  node_name: task_classifier
  plain_explanation: 先判断用户这次到底是在修机制、跑代码、做视频、查历史，还是要 Codex 执行任务。
  input: 用户任务、当前 project_route、AGENTS.md 路由规则、latest 状态。
  decision: 任务类型、风险等级、是否需要 RAG / readback / 用户拍板。
  output: task_context、risk_level、required_readback_files、allowed_next_nodes。
  blocked_if: 项目路由不清、任务类型不清、允许和禁止范围不清。
  failure_route: route_decision_gate 或 human_decision_gate。
  user_check: 看最终报告里是否先写清 project_route、task_type、round_scope，而不是直接动文件。
```

### 4.2 stale_index_checker

```yaml
runtime_node:
  node_name: stale_index_checker
  plain_explanation: 检查当前 RAG 索引是不是跟仓库最新事实一致。
  input: latest_index_manifest、latest_chunk_manifest、latest_vector_sync_gate_report、当前 Git HEAD。
  decision: RAG 是否最新、能不能只作为参考、是否必须回读原文。
  output: stale_index_result、allowed_usage_level、required_notice。
  blocked_if: 高风险任务依赖过期索引直接拍板，或 manifest 对不上且没有原文回读。
  failure_route: RAG_sync_bus 或 source_readback_checker。
  user_check: 看报告里是否明确写 current_RAG_index_latest_claim=false 或 true，并给出证据。
```

### 4.3 vector_retriever

```yaml
runtime_node:
  node_name: vector_retriever
  plain_explanation: 从向量库里找可能相关的资料，但这一步只负责“找候选”，不负责直接拍板。
  input: 用户问题、task_context、检索配置、DashVector 查询结果。
  decision: 哪些候选资料可能相关、是否命中不足、是否需要扩大 top-k 或改走原文读取。
  output: retrieved_candidates、retrieval_confidence、rag_empty_or_low_confidence_flag。
  blocked_if: 检索为空、低置信、或检索结果全是旧口径且任务需要当前事实。
  failure_route: source_readback_checker 或 RAG_supply_bus。
  user_check: 看决策审计报告里有没有列 retrieved_candidates，而不是只写“查到了资料”。
```

### 4.4 source_readback_checker

```yaml
runtime_node:
  node_name: source_readback_checker
  plain_explanation: 对关键候选资料回到 Git 仓库原文件验证，防止 RAG 摘要或旧索引误导。
  input: retrieved_candidates、required_readback_files、仓库文件路径和行号。
  decision: 关键事实是否能从原文读回、原文是否比 RAG 更新、是否缺文件。
  output: readback_status、source_quotes_or_line_refs、missing_readback_items。
  blocked_if: 高风险结论缺原文回读，或 RAG 说法和仓库原文冲突。
  failure_route: fact_source_arbitration 或 human_decision_gate。
  user_check: 看报告里是否有具体文件路径和 readback_status，而不是只凭 RAG 摘要。
```

### 4.5 authority_overlay_filter

```yaml
runtime_node:
  node_name: authority_overlay_filter
  plain_explanation: 给每条资料贴标签，判断它是当前正式事实、最新日志、执行规则、目标态计划，还是历史资料。
  input: readback_candidates、authority_overlay、source_path、source_commit_sha。
  decision: 资料是否能喂给 Codex、能不能声明完成、是否只可做历史背景。
  output: cleaned_candidates、blocked_context、authority_notes。
  blocked_if: archive_only、target_state_only、superseded 资料被当成 current_formal_fact 使用。
  failure_route: fact_source_arbitration。
  user_check: 看是否区分 current_formal_fact、latest_log、target_state_plan、historical_log。
```

### 4.6 conflict_group_resolver

```yaml
runtime_node:
  node_name: conflict_group_resolver
  plain_explanation: 把互相打架的新旧口径放到同一组里，选当前赢家；选不出来就阻断。
  input: cleaned_candidates、conflict_group_registry、用户最新指令、当前正式事实。
  decision: current_winner 是谁、loser 怎么降权、是否 pending_conflict。
  output: resolved_conflict_groups、winner_candidates、pending_conflicts。
  blocked_if: 必须用的执行事实没有 current_winner，或用户最新指令和仓库正式事实冲突但未落库。
  failure_route: human_decision_gate 或 fact_source_arbitration。
  user_check: 看报告里是否解释“为什么这个口径赢、旧口径怎么处理”。
```

### 4.7 hard_gate_checker

```yaml
runtime_node:
  node_name: hard_gate_checker
  plain_explanation: 先做一票否决检查；硬闸门过不了，后面的权重分再高也不能继续。
  input: task_context、readback_status、resolved_conflict_groups、stale_index_result、cleaned_candidates。
  decision: 是否存在密钥风险、原文回读缺失、当前正式事实冲突、未授权降级、高风险过期索引等。
  output: hard_gate_result、failed_gates、blocked_reason。
  blocked_if: 任一 hard_gate 失败。
  failure_route: secret_handling、RAG_sync_bus、source_readback_checker、human_decision_gate 或 completion_truth_check。
  user_check: 看报告里是否先列 hard_gate_result，再列 weighted_score_breakdown。
```

### 4.8 weighted_decision_engine

```yaml
runtime_node:
  node_name: weighted_decision_engine
  plain_explanation: 硬闸门通过后，才给多个候选动作打分，选当前最稳的动作。
  input: task_type_weight_profile、candidate_actions、cleaned_candidates、resolved_conflict_groups。
  decision: 哪个动作分最高，哪些动作因为风险、旧口径、同步慢或验证不足被降权。
  output: weighted_score_breakdown、selected_action、why_not_others。
  blocked_if: 缺 task_type_weight_profile、所有候选动作低于阈值、或分数最高动作仍违反硬闸门。
  failure_route: chatgpt_review_or_human_decision_gate。
  user_check: 看是否能回答“为什么选这个，不选另外两个”。
```

### 4.9 decision_audit_reporter

```yaml
runtime_node:
  node_name: decision_audit_reporter
  plain_explanation: 把 Codex 的判断过程写成用户能复核的审计报告。
  input: task_context、retrieved_candidates、readback_status、hard_gate_result、weighted_score_breakdown、selected_action。
  decision: 解释是否足够、阻断条件是否写清、是否需要用户复审。
  output: decision_audit_report。
  blocked_if: selected_action 没有理由、why_not_others 缺失、或硬闸门结果没有写入报告。
  failure_route: completion_truth_check。
  user_check: 看报告是否同时包含 selected_action、why_selected、why_not_others、blocked_if。
```

### 4.10 codex_supply_pack_emitter

```yaml
runtime_node:
  node_name: codex_supply_pack_emitter
  plain_explanation: 只有前面检查都过了，才把清洗后的资料和决策报告打包给 Codex 执行。
  input: decision_audit_report、cleaned_candidates、authority_overlay、readback_refs。
  decision: 哪些资料可以喂给 Codex，哪些只能当背景，哪些不能用于声明完成。
  output: pre_supply_pack、mid_task_supply_pack、post_risk_review_pack。
  blocked_if: supply pack 里包含 stale/superseded 资料却没有标记，或缺 readback 还允许 claim completed。
  failure_route: RAG_supply_bus。
  user_check: 看 supply pack 是否引用 decision_audit_report，并标明 can_feed_codex / can_claim_completed。
```

### 4.11 failure_router

```yaml
runtime_node:
  node_name: failure_router
  plain_explanation: 出错时不要硬冲，把失败送到正确的修复路线。
  input: failed_node、blocked_reason、task_context、partial_reports。
  decision: 是回到 RAG 同步、事实源裁决、用户拍板、清洗层修复，还是 completion truth check。
  output: failure_route、safe_next_step、blocked_report。
  blocked_if: 失败原因不明，或失败后仍试图继续执行高风险动作。
  failure_route: human_decision_gate。
  user_check: 看 blocked 报告是否写清“卡在哪、影响什么、下一步安全动作是什么”。
```

## 5. 当前场景完整例子

```yaml
example:
  user_question: 当前应该继续全量同步、只修增量同步，还是修增量同步 + 权威覆盖层？
  expected_flow:
    - task_classifier 判断这是 RAG 工程线高风险任务，因为它影响 Codex 后续如何取事实、如何判断完成、如何避免旧口径污染。
    - stale_index_checker 发现当前 RAG 不最新，latest_vector_sync_gate_report 仍显示 vector_sync_blocked_external_sync_timeout。
    - vector_retriever 可以提供候选背景，但不能直接作为当前事实拍板。
    - source_readback_checker 回读 latest、manifest、sync report 和设计报告，确认 changed_indexable_file_count=23，但 chunk_manifest 约 5657 chunks。
    - authority_overlay_filter 标记旧索引和旧日志只能做背景，不能直接作为当前正式事实喂给 Codex。
    - conflict_group_resolver 处理“继续全量同步”“只修增量同步”“增量同步 + 权威覆盖层”三种口径之间的冲突。
    - hard_gate_checker 阻断“继续全量同步直接写完成”，因为当前同步已 blocked，且不能声明 RAG 最新。
    - weighted_decision_engine 给三个候选动作打分：继续全量同步降权，只修增量同步中等，增量同步 + 权威覆盖层最高。
    - decision_audit_reporter 解释为什么选择 fix_incremental_sync_plus_authority_overlay。
    - codex_supply_pack_emitter 只把通过清洗、回读和权威过滤的资料交给 Codex 进入第二轮。
```

结论：

```yaml
selected_action: fix_incremental_sync_plus_authority_overlay
why_selected: 只修增量解决速度，不解决旧口径污染；只修覆盖层不解决同步慢；两者一起才覆盖当前风险面。
why_not_continue_full_sync: 当前已出现外部同步超时，继续全量同步不能解决根因。
why_not_incremental_only: 旧口径仍可能进入 RAG 召回并污染 Codex 判断。
```

## 6. 第二轮到底会不会用 LangGraph

```yaml
implementation_route_options:
  option_A:
    name: python_state_machine_first
    meaning: 先用普通 Python runner 把节点串起来，成本低，适合当前阶段。
    pros:
      - 快
      - 可控
      - 容易验证
      - 不需要先引入新依赖
    cons:
      - 图结构不如 LangGraph 直观
      - 后续多智能体扩展需要再整理节点和边

  option_B:
    name: langgraph_runtime
    meaning: 用 LangGraph 建节点、边、状态和条件路由。
    pros:
      - 图式结构清楚
      - 条件路由更显性
      - 后续多智能体更好扩展
    cons:
      - 当前工程复杂度更高
      - 需要额外依赖和验证
      - 容易把“修 RAG 决策线”变成“先修框架集成”
```

```yaml
recommendation:
  value: python_state_machine_first_then_langgraph_if_needed
  reason: 当前核心是先让 RAG 决策工程线跑通，不要一开始为了框架增加复杂度。等节点、状态、报告和失败路由都稳定后，再升级成 LangGraph 会更稳。
```

## 7. 直接回答：有文件后 Codex 是否就能自动判断？

```yaml
user_question_answer:
  question: 有了这些文件之后，Codex 是不是每次就能自动判断，不用填充细节？
  answer: 不是。文件只是规则；只有第二轮把 runner / graph / validator / trace / decision_audit_report 接起来后，Codex 才能在这些边界内自动判断。
  boundary: 自动判断只适用于已定义任务类型和已接入运行图的场景；新任务、新口径冲突、高风险状态推进仍需要 ChatGPT / 用户拍板。
```

再压一句：现在这份文件只是在把“未来怎么跑”讲清楚；它不是 LangGraph 已实现，不是 Python 状态机已实现，也不是 Codex 已经通过真实任务自动判断验证。

## 8. 用户复审时看什么

```yaml
user_review_checklist:
  - 是否看懂文件和 runtime 的区别
  - 是否接受先 Python 状态机、后续需要再 LangGraph
  - 是否接受每个节点都有 input / decision / output / blocked_if / failure_route / user_check
  - 是否接受 hard_gate 必须先于 weighted_decision
  - 是否接受过期索引只可按风险等级使用，不能在高风险任务里直接拍板
  - 是否接受第二轮必须把 decision_audit_report 接进 Codex supply pack 后再执行
```

## 9. 状态边界

```yaml
status_boundary:
  langgraph_implemented: false
  python_state_machine_implemented: false
  true_incremental_sync_implemented: false
  authority_overlay_runtime_validated: false
  weighted_decision_engine_runtime_validated: false
  RAG_latest_claim: false
  external_api_called_this_round: false
  dashvector_upsert_called_this_round: false
```
