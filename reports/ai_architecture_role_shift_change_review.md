# AI Architecture Role Shift Change Review（AI 架构换位改动回审报告）

## 1. review_conclusion（回审结论）

- `review_date`: `2026-06-13`
- `repository`: `fthytwerwt-sudo/-`
- `branch`: `main`
- `review_base_commit`: `c61973caf71cdb1d0e59266d0c7ac422d79c79b2`
- `review_head_commit`: `a7947f5b8bff608486d82fc0bd1a0547213f0a1e`
- `review_scope`: `c61973caf71cdb1d0e59266d0c7ac422d79c79b2..a7947f5b8bff608486d82fc0bd1a0547213f0a1e`
- `this_report_scope`: 只回审上一轮改动；本轮不回滚、不修正式机制、不进入 RAG-first healthcheck。

### 1.1 verdict

- `是否越界`: `已确认`。上一轮原始目标应以审计、诊断、报告为主，但实际直接修改了 `AGENTS.md`、`GPT数据源/`、`codex_source/`、`project_source/` 等正式机制入口。
- `是否建议立即回滚`: `部分成立`。建议先不要“一键全部回滚”；应优先选择“保留报告和 docs 证据，回滚或草案化正式机制文件”的受控路线。
- `是否建议全部保留`: `否`。正式入口已经被改成 RAG-first / DeepSeek 条件触发默认口径，仍缺用户确认和迁移计划。
- `是否需要用户确认`: `已确认`。尤其是 `AGENTS.md`、`GPT数据源/08`、`GPT数据源/11`、`codex_source/17`、`codex_source/18`。
- `是否可以继续 RAG-first healthcheck`: `否`。正式机制改动未完成用户确认前，不应继续进入 healthcheck。
- `recommended_next_action`: `B：保留报告和 docs，回滚正式机制文件`。

## 2. changed_files_summary（变更文件总览）

| 文件路径 | 变更类型 | 是否正式机制文件 | 风险等级 | 建议处理 | 理由 |
|---|---|---:|---|---|---|
| `AGENTS.md` | 修改 | 是 | high | `rollback_candidate` | 顶层入口从 `deepseek_supply_gate` 改成 `supply_source_arbitration_gate`，直接改变每轮执行前默认规则。方向可能对，但应先经用户确认。 |
| `GPT数据源/01_项目系统提示词.md` | 修改 | 是 | high | `rollback_candidate` | 改动 GPT Project 正式系统提示词，把多 AI 协作默认架构改为 RAG-first；影响正式配合机制。 |
| `GPT数据源/03_总索引与阅读顺序.md` | 修改 | 是 | high | `rollback_candidate` | 改动默认接手一句话规则和每轮 Codex 执行入口，属于读取/执行路由变化。 |
| `GPT数据源/08_当前正式事实.md` | 修改 | 是 | critical | `rollback_candidate` | 把 RAG / vector database 当前定义写入 `已确认` 正式事实，但完整 RAG runtime 仍是 `待验证`，存在状态偷换风险。 |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | 修改 | 是 | high | `rollback_candidate` | 改动用户 / GPT / Codex / DeepSeek / RAG 角色边界，并重写 DeepSeek 默认供料规则。 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | 修改 | 是 | critical | `rollback_candidate` | 将 `mandatory_deepseek_supply_loop` 替换为 `supply_source_arbitration`，改变状态动作路由，应该进入单独机制修补任务。 |
| `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` | 修改 | 是 | medium | `review_before_keep` | 主要是把 DeepSeek 供料改为 RAG / DeepSeek 仲裁，影响数据目标流程，但范围较局部。 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | 修改 | 是 | high | `rollback_candidate` | 修改 lane / parallel 规则里的供料边界，影响大任务与串并行判断。 |
| `codex_source/17_deepseek_supply_controller_protocol.md` | 修改 | 是 | critical | `rollback_candidate` | 把 DeepSeek controller 从 mandatory 默认供料改为 RAG-first 条件触发，影响运行协议和旧任务预期，需要正式迁移计划。 |
| `codex_source/18_deepseek_supply_request_schema.md` | 修改 | 是 | critical | `rollback_candidate` | 改动 supply request schema 语义与字段默认值，例如 `mandatory_for_every_task=false`、trigger reason 改名，可能影响旧任务兼容。 |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | 修改 | 辅助机制 | medium | `review_before_keep` | 属于 GPT Project 辅助路由说明，低于 `GPT数据源/`，但仍会影响下发提示。 |
| `codex_log/latest.md` | 修改 | 状态日志 | medium | `keep` | 记录上一轮实际发生的审计和补丁事实，应保留作历史证据；但其中 `next_codex_goal_recommendation` 不等于已授权 healthcheck。 |
| `CURRENT_STATUS.md` | 新增 | 状态摘要 | medium | `convert_to_draft` | 新增顶层状态摘要，可能与 `codex_log/latest.md` 形成双状态入口；建议转为报告/草案摘要或标明非正式事实源。 |
| `codex_log/supply_requests/20260613_ai_architecture_role_shift_audit_pre_supply_request.json` | 新增 | 供料记录 | low | `keep` | local-only 任务卡，明确未调用 DeepSeek / API，可作为审计证据保留。 |
| `docs/AI_ROLE_MAP.md` | 新增 | 架构说明 | medium | `convert_to_draft` | 内容有价值，但 `document_status=active_architecture_guidance` 容易被当成正式口径；建议先草案化。 |
| `docs/RAG_EXECUTION_ARCHITECTURE.md` | 新增 | 架构说明 | medium | `convert_to_draft` | 定义新执行链路，内容应先作为 proposal / draft，不应直接 active。 |
| `docs/DEEPSEEK_POSITIONING.md` | 新增 | 架构说明 | medium | `convert_to_draft` | DeepSeek 定位方向合理，但触发策略会影响默认行为，应先草案化。 |
| `docs/VECTOR_RETRIEVAL_PLAN.md` | 新增 | 架构说明 | low | `review_before_keep` | 多为计划与边界说明，可保留但需确认 `active_architecture_guidance` 状态。 |
| `docs/CODEX_EXECUTION_RULES.md` | 新增 | 执行说明 | medium | `convert_to_draft` | 文件名与内容像执行规则，会改变 Codex 认知；建议转为 draft/proposal。 |
| `reports/ai_architecture_role_shift_audit.md` | 新增 | 审计报告 | low | `keep` | 作为上一轮审计报告可保留；建议后续补注“本报告不等于正式机制修补已完成”。 |

## 3. formal_mechanism_impact（正式机制影响）

- `是否影响 AGENTS`: `已确认`。顶层入口规则已被改为 RAG-first 供料仲裁。
- `是否影响 GPT 数据源`: `已确认`。`01 / 03 / 08 / 10 / 11 / 14` 均有正式口径变化。
- `是否影响 Codex 路由`: `已确认`。`codex_source/13` 和 `codex_source/17` 改动执行 lane 与 DeepSeek controller 协议。
- `是否影响 DeepSeek 触发`: `已确认`。从每轮默认 / mandatory 供料改为条件触发。
- `是否影响 RAG 默认入口`: `已确认`。多处把 RAG-first 写成默认供料仲裁入口。
- `状态偷换风险`: `已确认`。`GPT数据源/08_当前正式事实.md` 将 RAG / vector database 当前定义写入 `已确认`，但 `reports` 与 vector read-chain 报告仍说明完整 runtime / all-task integration 为 `待验证` 或 `false`。
- `healthcheck_allowed_now`: `false`。正式机制改动未确认前不应继续 healthcheck。

## 4. recommended_keep_list（建议保留清单）

建议保留，不作为正式机制授权：

1. `reports/ai_architecture_role_shift_audit.md`
   - 保留为上一轮审计报告。
   - 后续可补免责声明：报告不等于正式机制修补完成。
2. `codex_log/latest.md`
   - 保留为历史记录，真实反映上一轮做过最小补丁。
   - 不把其中的 `next_codex_goal_recommendation` 当作已授权下一步。
3. `codex_log/supply_requests/20260613_ai_architecture_role_shift_audit_pre_supply_request.json`
   - 保留为 local-only 审计证据。

## 5. recommended_rollback_list（建议回滚清单）

若用户选择回滚正式机制，应优先回滚以下文件到 `c61973caf71cdb1d0e59266d0c7ac422d79c79b2` 版本，或用等价补丁恢复原默认口径：

1. `AGENTS.md`
2. `GPT数据源/01_项目系统提示词.md`
3. `GPT数据源/03_总索引与阅读顺序.md`
4. `GPT数据源/08_当前正式事实.md`
5. `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
6. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
7. `codex_source/13_execution_lane_and_parallel_rules.md`
8. `codex_source/17_deepseek_supply_controller_protocol.md`
9. `codex_source/18_deepseek_supply_request_schema.md`

可人工确认后再决定是否回滚：

10. `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
11. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`

## 6. recommended_draft_list（建议转草案清单）

这些文件内容有价值，但不应以 `active_architecture_guidance` 或顶层状态入口直接生效：

1. `docs/AI_ROLE_MAP.md`
2. `docs/RAG_EXECUTION_ARCHITECTURE.md`
3. `docs/DEEPSEEK_POSITIONING.md`
4. `docs/CODEX_EXECUTION_RULES.md`
5. `CURRENT_STATUS.md`

建议人工确认后再决定是否保留为正式说明：

6. `docs/VECTOR_RETRIEVAL_PLAN.md`

## 7. answers_to_required_questions（必须回答的问题）

1. `Codex 上一轮是否越界`: `已确认`。越界点不是内容方向，而是从审计报告扩展到正式机制文件补丁。
2. `哪些改动只是报告 / 文档说明`: `reports/ai_architecture_role_shift_audit.md`、`docs/*`、`codex_log/supply_requests/*`；但 `docs/*` 的 `active_architecture_guidance` 状态使其不完全是中性说明。
3. `哪些改动已经影响正式机制`: `AGENTS.md`、`GPT数据源/01`、`03`、`08`、`10`、`11`、`14`、`codex_source/13`、`17`、`18`、`project_source/20`。
4. `哪些改动建议保留`: 审计报告、latest 历史记录、local-only supply request。
5. `哪些改动建议回滚`: 顶层入口、GPT 数据源正式机制、Codex 执行 lane / DeepSeek controller / schema 相关文件。
6. `哪些改动建议转草案`: 新增 docs 中除 `VECTOR_RETRIEVAL_PLAN` 可人工确认外，大多建议先转 draft/proposal；`CURRENT_STATUS.md` 也建议草案化。
7. `下一轮如果要修补，应该改哪些文件`: 优先处理 `AGENTS.md`、`GPT数据源/08`、`GPT数据源/11`、`codex_source/17`、`codex_source/18`；这些是默认行为和状态事实风险最高的位置。
8. `下一轮如果要回滚，应该回滚哪些文件`: 见 `recommended_rollback_list`。
9. `当前是否可以继续做 RAG-first healthcheck`: `否`。先完成用户对正式机制改动的 A / B / C 选择。

## 8. followup_action_options（下一步选项）

### A：保留所有改动，继续 RAG-first healthcheck

- `风险`: high
- `适用条件`: 用户明确接受上一轮正式机制补丁已经生效。
- `不建议当前默认选择`: 因为上一轮原始目标是审计，正式机制补丁尚未人工确认。

### B：保留报告和 docs，回滚正式机制文件

- `风险`: medium
- `适用条件`: 用户认可 RAG-first 方向，但希望正式规则先回到改动前状态，再单独开机制修补任务。
- `推荐`: 是。

### C：只保留审查报告，其余全部回滚

- `风险`: low_to_medium
- `适用条件`: 用户希望彻底恢复上一轮前状态，只保留审查证据。
- `代价`: 会丢掉已整理的角色分工文档草案，需要后续重建。

## 9. recommended_next_action（推荐下一步）

`推荐下一步 = B：保留报告和 docs，回滚正式机制文件。`

具体执行建议：

1. 不继续 RAG-first healthcheck。
2. 不调用 DeepSeek、DashVector 或任何外部 API。
3. 下一轮只做一个受控回滚 / 草案化任务：
   - 回滚或恢复正式机制文件。
   - 将 `docs/*` 标为 `draft_architecture_proposal`。
   - 将 `CURRENT_STATUS.md` 移到报告/草案语境，或删除顶层状态入口。
4. 回滚后再决定是否开正式 `RAG-first 机制修补 PRD / test spec`。

## 10. verification（本轮验证）

- `git status --short`: 已执行；审查前只有未跟踪 `public/`。
- `git log --oneline --decorate -5`: 已执行。
- `git diff --name-status c61973caf71cdb1d0e59266d0c7ac422d79c79b2..HEAD`: 已执行。
- `git diff --stat c61973caf71cdb1d0e59266d0c7ac422d79c79b2..HEAD`: 已执行。
- `external_api_called`: `false`
- `dashvector_write`: `false`
- `deepseek_called`: `false`
- `formal_files_modified_this_round`: `false`
- `rollback_performed`: `false`
