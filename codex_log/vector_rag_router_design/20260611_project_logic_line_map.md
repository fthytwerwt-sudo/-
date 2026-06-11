# 20260611 项目逻辑线总图 Project Logic Line Map

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `rag_runtime_implemented（RAG（检索增强）运行时是否实现）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`

## 2. full_logic_line（完整逻辑线）

```text
user_input（用户输入）
-> ChatGPT absolute_judgment（ChatGPT 绝对判断层）
-> Codex route_decision（Codex 项目路由判断）
-> workflow_route_decision（工作流归位判断）
-> source_arbitration（事实源仲裁）
-> RAG retrieval if available（RAG（检索增强）检索，如已可用）
-> conflict_arbitration（冲突仲裁）
-> optional DeepSeek supply（可选 DeepSeek（深度供料）供料）
-> selected_skill_graph（技能图选择）
-> dynamic_task_graph（动态任务图）
-> execution_or_block（执行或阻断）
-> completion_validation（完成验证）
-> git_commit_push（Git 提交推送）
-> vector_sync_dry_run（向量同步空跑）
-> vector_sync_apply if approved（确认后正式同步）
```

## 3. layer_contract（层级合同）

| layer（层） | owner（责任方） | input（输入） | output（输出） | stop_line（停止线） |
|---|---|---|---|---|
| User Input（用户输入） | 用户 | 目标、素材、反馈、限制 | 本轮 delta（增量） | 用户输入不是完整流程源 |
| ChatGPT Judgment（ChatGPT 判断） | ChatGPT | 用户目标 + 仓库事实摘要 | 执行单、冲突裁决、是否进入机制修补 | 不直接写仓库事实 |
| Route Decision（路由判断） | Codex | 执行单 + AGENTS | project_route / task_type / allowed_changes | 路由不清则 blocked（阻断） |
| Workflow Route（工作流归位） | Codex Router（路由器） | task_type（任务类型） | workflow_type（工作流类型） | 缺工作流不得执行 |
| Source Arbitration（事实源仲裁） | Router（路由器） | GitHub、RAG、DeepSeek、用户本轮增量 | source_priority（事实源优先级） | GitHub / local repo 永远优先 |
| RAG Retrieval（RAG 检索） | RAG（检索增强） | 检索范围、metadata（元数据） | evidence_paths（证据路径）、retrieved_chunks（召回片段） | 不拍板、不替代 Router |
| Conflict Arbitration（冲突仲裁） | Router（路由器） | 召回片段 + 当前文件 | resolved / conflict_pending | 冲突未解不得推进状态 |
| Optional DeepSeek Supply（可选 DeepSeek 供料） | DeepSeek（深度供料） | 任务卡、文本上下文 | supply_pack / risk_review | 不写文件、不进主事实 |
| Skill Graph（技能图） | Router（路由器） | workflow + context + delta | selected_skill_graph | Skill（技能）只能封稳定动作 |
| Dynamic Task Graph（动态任务图） | Codex | skill graph + dependencies | child_task_graph | 不固定死流程 |
| Execution or Block（执行或阻断） | Codex | task graph | 文件修改或 blocked report | 不能降级完成 |
| Completion Validation（完成验证） | Codex | 产物、报告、git 状态 | completion_truth_check | 没验证不得 completed（已完成） |
| Git Commit Push（Git 提交推送） | Codex | path-limited staged diff | commit + push + remote HEAD | 未 push 不算完成 |
| Vector Sync Dry Run（向量同步空跑） | future sync runner（未来同步器） | committed diff | sync plan report（同步计划报告） | dry-run 不等于 apply |
| Vector Sync Apply（正式向量同步） | approved sync runner（经授权同步器） | dry-run report + approval | collection update（集合更新） | 不能反向覆盖仓库 |

## 4. ordering_rules（顺序规则）

1. RAG（检索增强）必须发生在 `execution_or_block（执行或阻断）` 之前。
2. DeepSeek（深度供料）是 optional（可选），必须由 Router（路由器）触发。
3. Git commit / push（提交 / 推送）必须先于 vector sync（向量同步）。
4. vector sync（向量同步）失败不得影响 GitHub 主事实。
5. Vector DB（向量数据库）不能反向覆盖仓库文件。
6. `prompt_delta（本轮提示词增量）` 必须和 `current_context（当前上下文）` 分开。
7. 新增素材必须先走 `material_delta_type_router（素材增量类型路由器）`，默认 `additive_merge（补充合并）`。
8. 写 `completed（已完成）` 前必须经过 `completion_truth_preflight_router（完成真实性预检路由器）`。

## 5. selected_skill_graph_policy（技能图选择策略）

Skill（技能）只负责稳定、重复、可验证动作，例如：

- `process_boot_skill（流程启动技能）`
- `full_context_rebuild_skill（全量上下文重建技能）`
- `material_delta_merge_skill（素材增量合并技能）`
- `locked_copy_diff_skill（锁稿差异检查技能）`
- `publish_candidate_preflight_skill（发片候选预检技能）`
- `completion_truth_skill（完成真实性技能）`
- `git_sync_skill（Git 同步技能）`

不应该 skill 化的内容：

- 单条视频选题、标题、最终口播稿。
- 临时审美目标、单轮素材清单、一次性卡片文案。
- 向量库 provider（供应商）选择、embedding dimensions（向量维度）等部署配置。
- 用户本轮临时要求和替换范围。

## 6. project_logic_guardrails（逻辑线防线）

1. `source_of_truth（主事实源）` 永远是仓库。
2. RAG（检索增强）只召回，不裁决。
3. DeepSeek（深度供料）只供料 / 复审，不裁决。
4. Router（路由器）选择路径并处理冲突。
5. Codex（执行器）执行并验证。
6. ChatGPT（总控判断）处理用户目标、语义冲突和是否正式机制修补。
7. Vector DB（向量数据库）只做检索索引 / 缓存。
8. completion validation（完成验证）独立于检索和供料。

## 7. formal_patch_recommendation（正式补丁建议）

后续可把本图拆成 `project_logic_line_runtime_check（项目逻辑线运行检查）`，在每轮 route_decision（路由判断）后输出：

```yaml
logic_line_check:
  prompt_delta_separated: true_or_false
  source_arbitration_done: true_or_false
  rag_retrieval_needed: true_or_false
  deepseek_needed: true_or_false
  skill_graph_selected: true_or_false
  dynamic_task_graph_ready: true_or_false
  completion_validation_planned: true_or_false
```
