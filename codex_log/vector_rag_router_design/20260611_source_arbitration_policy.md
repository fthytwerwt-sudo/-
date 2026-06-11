# 20260611 事实源仲裁策略 Source Arbitration Policy

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `formal_rules_modified（是否修改正式规则）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`

## 2. authority_order（权威顺序）

未来 Router（路由器）遇到多个事实源时，按以下顺序仲裁：

1. `user_current_explicit_boundary（用户本轮明确边界）`：只影响本轮 delta（增量），不自动成为下轮默认事实。
2. `AGENTS.md（工作区规则）`：项目路由、安全边界、单工作区和 Git 完成规则。
3. `GPT数据源/08_当前正式事实.md（当前正式事实）`：当前正式事实。
4. `codex_log/latest.md（最新日志）`：最新机制事实和落库历史。
5. `GPT数据源/11_项目状态动作总控器_机制推理层.md（状态动作总控器）`。
6. `codex_source/19_project_state_action_router.md（Codex 侧项目状态动作总控器）`。
7. `codex_source/21_codex_judgment_permission_matrix.md（Codex 判断权限表）`。
8. `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md（工作流入口索引）`。
9. runtime evidence（运行证据）、fixture（测试用例）、dry-run（空跑）结果。
10. `reference_only（仅参考）` / historical（历史）资料。

如果第 1 项和第 2-8 项冲突：

- 用户本轮明确边界可指导本轮执行。
- 但必须由 Codex 写回仓库并完成 commit / push / remote HEAD verification（远端 HEAD 校验）后，才成为下一轮默认事实。

## 3. source_roles（事实源角色）

| source（来源） | role（角色） | can_decide_project_fact（是否能拍板事实） |
|---|---|---|
| GitHub / local repo（GitHub / 本地仓库） | `source_of_truth（主事实源）` | `true` |
| Vector DB（向量数据库） | `retrieval_index（检索索引）` | `false` |
| RAG（检索增强） | `retrieval_layer（检索层）` | `false` |
| DeepSeek（深度供料） | `external_deep_supply（外部深度供料）` / `risk_review（风险复审）` | `false` |
| ChatGPT（总控判断） | `judgment_layer（判断层）` | `can_request_patch（可请求补丁）` |
| Codex（执行器） | `execution_layer（执行层）` | `can_commit_confirmed_changes（可提交已确认变更）` |

## 4. conflict_arbitration_matrix（冲突仲裁矩阵）

| conflict（冲突） | decision（裁决） | router_action（路由动作） |
|---|---|---|
| Vector DB（向量数据库）召回旧规则 vs GitHub 当前文件 | GitHub 当前文件优先 | 标记旧 chunk（切块）为 `legacy_demoted（历史降权）` 或 `superseded（已替代）` |
| RAG（检索增强）召回结果互相冲突 | 不拍板 | 输出 `conflict_pending（冲突待裁决）`，阻断状态推进 |
| DeepSeek（深度供料）结论 vs GitHub 当前文件 | GitHub 当前文件优先 | DeepSeek 结果转 `reference_only（仅参考）` |
| 用户本轮要求 vs 当前仓库默认 | 用户要求作为本轮 delta（增量） | 必须写明 `task_delta（本轮增量）`，不自动更新主事实 |
| feature（功能分支）策略 vs main（主分支）正式事实 | main（主分支）优先 | feature 只进 staging collection（测试集合） |
| technical preview（技术预览） vs completed（已完成） | 技术预览不是完成 | 触发 completion truth（完成真实性） |
| old Qwen / Aliyun B vs MiniMax voice lock | MiniMax + `oldBMinimax20260528010200` 当前锁优先 | 旧 Qwen / 阿里 B 标记 `reference_anchor_only（仅参考锚点）` |
| `publish_candidate_ready_for_human_review（可发布候选片待人工复审）` vs `send_ready（可发送）` | 不合并 | `send_ready` 仍需最终确认 |

## 5. router_required_output（Router 必须输出）

每次涉及 RAG（检索增强）或 DeepSeek（深度供料）的任务，Router（路由器）至少输出：

```yaml
source_arbitration:
  primary_source: github_local_repo
  secondary_sources:
    - rag_retrieval
    - deepseek_supply
    - latest_log
  evidence_paths: []
  retrieved_commit_sha: optional
  conflict_detected: true_or_false
  conflict_arbitration: repo_wins | user_delta_this_turn | conflict_pending | chatgpt_user_decision_required
  blocked_if_conflict_unresolved: true
```

## 6. vector_metadata_dependency（向量元数据依赖）

事实仲裁依赖以下 metadata（元数据）：

- `branch（分支）`
- `commit_sha（提交 SHA）`
- `source_path（来源路径）`
- `heading_path（标题路径）`
- `authority_level（权威等级）`
- `status_label（状态标签）`
- `effective_date（生效日期）`
- `supersedes（替代了谁）`
- `superseded_by（被谁替代）`
- `conflict_tags（冲突标签）`
- `do_not_use_for_completion_claim（是否禁止用于完成判断）`

缺任一关键元数据时，Router（路由器）不得把召回结果用于完成判断。

## 7. formal_patch_recommendation（正式补丁建议）

后续正式入口建议新增 `source_arbitration_policy_reference（事实源仲裁策略引用）`，但本轮不直接改正式规则文件。最小下一步是做 source arbitration fixture（事实源仲裁测试用例），覆盖：

1. main（主分支）当前事实 vs feature（功能分支）策略。
2. DeepSeek fallback_local_only（本地兜底） vs DeepSeek passed（真实通过）。
3. Vector DB（向量数据库）旧 chunk（切块） vs GitHub 新规则。
4. 用户本轮新增素材 vs 旧素材上下文。
5. technical preview（技术预览） vs completion truth（完成真实性）。
