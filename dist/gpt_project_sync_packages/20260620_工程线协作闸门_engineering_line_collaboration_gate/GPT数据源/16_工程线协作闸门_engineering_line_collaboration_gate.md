# 16｜工程线协作闸门 engineering_line_collaboration_gate

## 1. 文件定位

`engineering_line_collaboration_gate（工程线协作闸门）` 是《视频工厂》长期协作机制入口。

它解决的问题不是“把所有规则都塞进 prompt（提示词）”，而是让用户、ChatGPT 和 Codex 按工程线分工：

- `用户（User）`：负责目标、核心红线、业务验收、人工拍板点。
- `ChatGPT`：负责总控判断，把用户目标压成工程线，判断任务属于哪一层、缺哪一层、能不能下发 Codex。
- `Codex`：负责把工程线落成文件、节点、`Schema（数据契约）`、`Tool Registry（工具注册表）`、`Evaluator（评估器）`、`Failure Route（失败路由）`、`Trace（链路记录）`、测试样例和执行报告。

核心原则：

```yaml
core_principle（核心原则）:
  value（值）: simple_tasks_stay_simple_complex_tasks_become_engineering_line（简单任务保持简单，复杂任务进入工程线）
  meaning（含义）: 不允许把所有任务都拖进完整 13 层流程，避免过度工程化。
```

本机制写入只代表协作闸门已落库，不代表长期稳定验证通过，不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）` 或 `production_readiness（生产可用状态）`。

## 2. AI 工程线 13 层

```yaml
ai_engineering_line_13_layers（AI 工程线 13 层）:
  0_project_goal_layer（项目目标层）: 目标、业务红线、验收口径和不做什么。
  1_current_task_awareness_layer（当前任务意识层）: 当前任务属于聊天、任务卡、节点契约还是系统工程线。
  2_process_node_layer（流程节点层）: 把任务拆成可进入、可退出、可验证的节点。
  3_cleaning_layer（清洗层）: 清洗用户输入、仓库事实、旧口径、外部资料和冲突信号。
  4_structuring_layer（结构化层）: 输出字段、表格、状态、Schema 和可机器检查的结构。
  5_retrieval_layer（资料召回层）: 判断需要 RAG / DashVector / 仓库原文 / 外部资料中的哪一种。
  6_tool_connection_layer（工具连接层）: 选择工具、API、脚本、运行时或明确不调用外部接口。
  7_execution_node_layer（执行节点层）: Codex 落地文件、脚本、节点、样例、日志和同步包。
  8_evaluation_layer（判断评估层）: Evaluator、validator、lint、测试、人工复审点。
  9_failure_route_layer（失败路由层）: 错了回哪一层，blocked、fallback、human review 或重判。
  10_human_in_the_loop_layer（人工兜底层）: 用户 / ChatGPT 必须拍板的目标、红线、降级和交付判断。
  11_state_record_layer（状态记录层）: latest、dated log、manifest、trace、路径索引和 Git 事实。
  12_review_iteration_layer（复盘迭代层）: 把执行结果、失败原因、用户反馈和下一轮改动写回机制。
```

五问法：

```yaml
five_questions（五问法）:
  1_goal（要什么）: 目标、验收、红线是什么。
  2_state（到哪了）: 当前状态、节点、缺口和阻断在哪里。
  3_supply（吃什么）: 需要哪些资料、事实源、工具和输入。
  4_failure_route（错了去哪）: 失败后回目标、机制、执行、评估、人工兜底还是复盘。
  5_record（留没留记录）: 是否留下日志、trace、manifest、Git 和同步包证据。
```

第六个入口判断：

```yaml
engineering_worth_question（值不值得工程化的入口问题）:
  question（问题）: 本轮值不值得工程化？
  use_when（使用场景）:
    - 任务可能新增机制、脚本、节点、schema、validator、同步包或长期入口。
    - 任务可能反复发生，且失败会让用户重复解释。
    - 任务涉及多个角色、多个文件、多个状态或高风险边界。
  do_not_engineer_if（不进入工程化条件）:
    - 一次性解释、临时判断或简单聊天足够解决。
    - 机制文件比任务本身更重。
    - 自动化会增加用户审查成本。
  output（输出）:
    - engineering_depth（工程深度）
    - reason（理由）
    - chosen_gate（选择闸门）
    - not_chosen_gate（未选择闸门）
```

## 3. engineering_depth_router（工程深度路由器）

```yaml
engineering_depth_router（工程深度路由器）:
  L0_light_chat（轻量聊天）:
    scope（适用范围）: 解释、判断、临时讨论。
    required_outputs（必需输出）:
      - concise_answer（简洁回答）
    forbidden（禁止）:
      - 不落库
      - 不生成 Codex prompt（Codex 执行单）
      - 不跑完整工程线

  L1_task_card（任务卡）:
    scope（适用范围）: 小修、小文案、小机制判断。
    required_outputs（必需输出）:
      - goal（目标）
      - boundary（边界）
      - done_when（完成标准）
      - blocked_if（阻断条件）

  L2_node_contract（节点契约）:
    scope（适用范围）: 一个稳定节点、一个脚本、一个机制文件。
    required_outputs（必需输出）:
      - purpose（用途）
      - inputs（输入）
      - outputs（输出）
      - core_decisions（核心判断）
      - route_rules（路由规则）
      - blocked_if（阻断条件）
      - examples（样例）
      - validation（验证方式）

  L3_system_line（系统工程线）:
    scope（适用范围）: 视频工厂、数字人直播、剪辑自动流、RAG 供料总线、长期多节点系统。
    required_outputs（必需输出）:
      - goal_contract（目标契约）
      - state_contract（状态契约）
      - node_contracts（节点契约）
      - schema_contracts（数据契约）
      - tool_registry（工具注册表）
      - evaluator（评估器）
      - failure_route（失败路由）
      - human_in_the_loop（人在回路中）
      - checkpoint（检查点）
      - trace_report（链路记录）
      - review_update（复盘更新）
```

硬规则：

- 简单任务不得强制 L3。
- 复杂任务不得停在 L0 / L1。
- 用户要求“直接做”不等于允许跳过必需工程深度判断。
- 工程深度判断必须服务效率，不得制造流程负担。

## 4. decision_authority_matrix（决策权矩阵）

```yaml
decision_authority_matrix（决策权矩阵）:
  user_must_decide（用户必须决定）:
    - project_goal_change（项目目标改变）
    - business_red_line_change（业务红线改变）
    - client_delivery_standard_change（客户交付标准改变）
    - degradation_authorization（降级授权）
    - publish_or_delivery_decision（发布或交付决策）
    - high_risk_live_reply_auto_send（高风险直播回复是否自动发送）

  chatgpt_can_decide（ChatGPT 可决定）:
    - task_layer（任务层级）
    - engineering_depth（工程深度）
    - missing_anchor_check（缺失锚点判断）
    - whether_codex_prompt_can_be_issued（是否能下发 Codex）
    - codex_report_truth_review（Codex 回报真实性复审）

  codex_can_auto_fill（Codex 可自动补齐）:
    - file_internal_fields（文件内部字段）
    - schema（数据契约）
    - fixture（测试样例）
    - validator（校验器）
    - failure_route（失败路由）
    - trace_log（链路记录）
    - low_risk_code_implementation（低风险代码实现）

  forbidden_authority_swap（禁止权限偷换）:
    - Codex 不得替用户改变目标。
    - Codex 不得替用户改变验收标准。
    - Codex 不得把 technical_validation（技术验证）写成 content_validation（内容验证）。
    - ChatGPT 不得把推测写成用户已确认。
```

## 5. per_file_detail_plan_gate（单文件细节方案闸门）

```yaml
per_file_detail_plan_gate（单文件细节方案闸门）:
  trigger（触发）:
    - 新增机制文件
    - 修改机制文件
    - 新增脚本
    - 修改脚本
    - 新增 schema（数据契约）
    - 新增 validator（校验器）
    - 新增 workflow node（工作流节点）

  each_file_must_output（每个文件必须输出）:
    - purpose（用途）: 这个文件解决什么问题。
    - layer（所属层级）: 属于目标、状态、节点、资料、工具、执行、评估、失败路由、人工兜底、记录或复盘中的哪一层。
    - inputs（输入）: 读取哪些文件 / 字段。
    - outputs（输出）: 生成哪些文件 / 字段。
    - core_decisions（核心判断）: 里面有哪些判断。
    - trigger_conditions（触发条件）: 每个判断什么时候触发。
    - route_rules（路由规则）: 判断后走哪条路径。
    - missing_info_policy（缺信息处理）: 缺信息时 blocked、fallback、还是请求用户。
    - conflict_policy（冲突处理）: 仓库事实、用户输入、外部资料冲突时怎么裁决。
    - blocked_if（阻断条件）: 什么情况下不能继续。
    - examples（样例）: 至少 3 个，复杂节点至少 5 个。
    - validation（验证方式）: 怎么证明判断是对的。
    - user_review_points（用户复审点）: 用户只需要看哪些业务判断。

  forbidden（禁止）:
    - 只给文件名清单。
    - 只写“新增脚本”但不写内部判断。
    - 只写技术实现，不写业务触发条件。
    - 没有样例就写完成。
```

最小样例：

```yaml
examples（样例）:
  simple_l1_copy_fix（简单 L1 文案小修）:
    engineering_depth（工程深度）: L1_task_card（任务卡）
    why（原因）: 目标和边界清楚，不需要新增机制文件。
    done_when（完成标准）: 文案小修完成且不改变 locked copy 核心语义。

  stable_validator_node（稳定校验节点）:
    engineering_depth（工程深度）: L2_node_contract（节点契约）
    why（原因）: 需要固定 inputs / outputs / blocked_if / examples / validation。
    done_when（完成标准）: validator、fixture、passing / blocked 样例和报告存在。

  multi_node_rag_or_video_system（多节点 RAG 或视频系统）:
    engineering_depth（工程深度）: L3_system_line（系统工程线）
    why（原因）: 涉及状态、工具、评估、失败路由、人工兜底和 trace。
    done_when（完成标准）: 目标契约、状态契约、节点契约、Schema、Tool Registry、Evaluator、Failure Route、Trace 和复盘更新齐全。
```

## 6. execution_budget_gate（执行预算闸门）

```yaml
execution_budget_gate（执行预算闸门）:
  purpose（用途）: 防止工程线过度设计，避免一次任务比人工还重。

  check_items（检查项）:
    - 本轮是否值得落库？
    - 本轮是否值得新增脚本？
    - 是否值得调用外部 API？
    - 是否值得跑完整 RAG / 检索？
    - 是否值得生成完整同步包？
    - 是否可以只做 L1 / L2，不上 L3？
    - 是否有更低成本的人工确认点？

  blocked_if（阻断条件）:
    - 简单任务被强行升级成完整工程线。
    - 机制文件比任务本身更复杂。
    - 为了自动化反而增加用户审查成本。
```

默认判断：

- `L0_light_chat（轻量聊天）`：不落库，不生成同步包。
- `L1_task_card（任务卡）`：只写任务卡 / 小日志，通常不新增脚本。
- `L2_node_contract（节点契约）`：可新增机制文件、schema、validator 或样例。
- `L3_system_line（系统工程线）`：才允许完整工程线、Tool Registry、Evaluator、Failure Route、Trace 和同步包。

## 7. collaboration_effectiveness_check（协作有效性检查）

```yaml
collaboration_effectiveness_check（协作有效性检查）:
  purpose（用途）: 验证机制是否真的提升协作，而不是只增加文件。

  check_questions（检查问题）:
    - 是否减少用户重复解释？
    - 是否减少 Codex 漏项？
    - 是否让失败回到明确节点？
    - 是否让用户只看关键业务判断？
    - 是否让下一次新聊天更容易接手？
    - 是否避免把简单任务过度工程化？

  failure_if（失败判定）:
    - 文件变多但 Codex 仍不知道下一步。
    - 报告变长但用户仍要排查内部原因。
    - 工程线写了但没有样例、验证和失败路由。
    - 每个任务都被拖进复杂流程。
```

## 8. Codex 执行要求

Codex 收到机制 / 项目文件 / 自动化 / 多节点任务时，必须先判断：

```yaml
codex_execution_gate（Codex 执行闸门）:
  required_before_write（写入前必需）:
    - engineering_worth_question（值不值得工程化）
    - engineering_depth_router（工程深度路由器）
    - decision_authority_matrix（决策权矩阵）
    - execution_budget_gate（执行预算闸门）
  required_if_file_change（文件变更时必需）:
    - per_file_detail_plan_gate（单文件细节方案闸门）
  required_before_completed（完成前必需）:
    - examples（样例）
    - validation（验证）
    - failure_route（失败路由）
    - trace_or_log（链路记录或日志）
    - collaboration_effectiveness_check（协作有效性检查）
```

完成禁止：

- 缺 `engineering_depth_router（工程深度路由器）`，不得直接执行复杂任务。
- 缺 `per_file_detail_plan_gate（单文件细节方案闸门）`，不得写项目文件修改完成。
- 缺 `Node Contract（节点契约）`、`Schema（数据契约）`、`Evaluator（评估器）`、`Failure Route（失败路由）` 或 `Trace（链路记录）` 时，L3 任务不得写 `completed（已完成）`。
- 简单任务不得被强制升级为完整工程线。

## 9. 状态边界

```yaml
status_boundary（状态边界）:
  mechanism_written（机制写入）: true（本文件写入后为真）
  long_term_stability（长期稳定性）: pending_real_task_validation（待真实任务验证）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  publish_status（发布状态）: not_promoted（未推进）
  voice_validation（声音验证）: not_promoted（未推进）
  final_voice_validated（最终声音验证）: false（未通过）
  visual_master_locked（视觉母版锁定）: false（未锁定）
  production_readiness（生产可用状态）: not_claimed（未声称）
```

## 10. 一句话规则

**以后不是把所有规则塞进 prompt 里赌 AI 不忘，而是先问“值不值得工程化”，再按 L0 / L1 / L2 / L3 选择协作深度：简单任务保持简单，中等任务用五问法补齐，复杂任务进入完整工程线，高风险任务必须 Human-in-the-loop（人在回路中）。**
