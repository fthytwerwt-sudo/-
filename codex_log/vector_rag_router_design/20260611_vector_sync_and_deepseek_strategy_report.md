# 20260611 向量同步与 DeepSeek（深度供料） / RAG（检索增强）边界策略总报告

## 1. execution_status（执行状态）

- `task_status（任务状态）`: `strategy_design_completed（策略设计完成）`
- `project_route（项目路由）`: `video_factory（视频工厂）`
- `branch（分支）`: `feature/vector-rag-router-design-20260611`
- `external_api_called（是否调用外部 API）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `secrets_read_or_printed（是否读取或打印密钥）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`
- `media_generated（是否生成媒体）`: `false`

## 2. files_created（新增文件）

| file_path（文件路径） | role（作用） | status（状态） |
|---|---|---|
| `codex_log/vector_rag_router_design/20260611_vector_sync_policy.md` | Vector Sync Policy（向量同步策略） | created（已创建） |
| `codex_log/vector_rag_router_design/20260611_deepseek_rag_boundary_strategy.md` | DeepSeek（深度供料） / RAG（检索增强） Boundary（边界） | created（已创建） |
| `codex_log/vector_rag_router_design/20260611_project_logic_line_map.md` | Project Logic Line Map（项目逻辑线总图） | created（已创建） |
| `codex_log/vector_rag_router_design/20260611_source_arbitration_policy.md` | Source Arbitration Policy（事实源仲裁策略） | created（已创建） |
| `codex_log/vector_rag_router_design/20260611_vector_sync_and_deepseek_strategy_report.md` | Strategy Summary Report（策略总报告） | created（已创建） |

## 3. summary_decision（总策略结论）

| item（项目） | decision（结论） |
|---|---|
| `source_of_truth（主事实源）` | GitHub / local repo（GitHub / 本地仓库）永远是主事实源 |
| `vector_db_role（向量库职责）` | `retrieval_index（检索索引）` / `cache_layer（缓存层）`，不能成为事实源 |
| `rag_role（RAG 职责）` | 从白名单文件和 Vector DB（向量数据库）召回上下文，输出证据路径，不拍板 |
| `deepseek_role（DeepSeek 职责）` | external_deep_supply（外部深度供料）、risk_review（风险复审）、external_research（外部调研） |
| `router_role（Router 职责）` | 选择 workflow（工作流）、检索范围、skill graph（技能图）、冲突仲裁、blocked / execute |
| `codex_role（Codex 职责）` | 复核原文件、执行修改、验证、path-limited stage、commit、push、remote HEAD 校验 |
| `chatgpt_role（ChatGPT 职责）` | 用户需求判断、关键冲突裁决、是否进入正式机制修补、是否允许向量入库 |

## 4. deepseek_rag_conflict（DeepSeek 和 RAG 是否冲突）

- `conflict_exists（是否存在冲突）`: `potential_conflict（存在潜在冲突）`
- `conflict_type（冲突类型）`: 两者都可能输出上下文、风险判断和文件建议；若无边界，Codex 可能把供料当事实源。
- `resolution（解决方式）`: RAG（检索增强）负责项目内检索；DeepSeek（深度供料）负责深文件供料、外部研究和风险复审；Router（路由器）负责冲突仲裁；GitHub / local repo（GitHub / 本地仓库）优先。

## 5. vector_sync_strategy（向量同步策略）

- `sync_mode（同步模式）`: `incremental_sync（增量同步）`、`full_reindex（全量重建索引）`、`demote_or_delete_sync（降权或删除同步）`。
- `branch_collection_policy（分支集合策略）`: `main（主分支） -> video_factory_main（正式集合）`；`feature/*（功能分支） -> video_factory_branch_staging（测试集合）`。
- `metadata_required（必须元数据）`: repo_full_name、branch、commit_sha、source_path、heading_path、content_hash、authority_level、status_label、updated_at、supersedes、superseded_by、conflict_tags、do_not_use_for_completion_claim。
- `delete_demote_policy（删除 / 降权策略）`: 旧规则优先标记 legacy_demoted（历史降权）/ deprecated（已过时）/ reference_only（仅参考）；文件删除用 tombstone（墓碑记录）或删除 chunk（切块）。
- `sync_after_git_policy（Git 后同步策略）`: commit / push / remote HEAD verified 后才能进入 vector_sync_dry_run（向量同步空跑）；确认后才能 vector_sync_apply（正式同步）。

## 6. project_logic_line（项目逻辑线）

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

## 7. hidden_risks_and_guardrails（隐性风险与防线）

| risk（风险） | guardrail（防线） |
|---|---|
| 向量库召回旧规则覆盖当前事实 | metadata（元数据）必须含 authority_level / status_label / superseded_by；GitHub 当前文件优先 |
| DeepSeek 供料被误当仓库事实 | supply_pack（供料包）只标 reference_only（仅参考），不得直接入正式事实 |
| RAG（检索增强）和 DeepSeek（深度供料）给出不同结论 | Router（路由器）输出 conflict_arbitration（冲突仲裁），未裁决则 blocked（阻断） |
| feature（功能分支）污染 main（主分支）正式向量集合 | feature 只同步 staging collection（测试集合） |
| 删除 / 降权规则后旧 chunk（切块）仍留在向量库 | demote_or_delete_sync（降权或删除同步）必须输出 demoted_chunks / deleted_chunks |
| metadata（元数据）缺失导致 Router 不知道哪个规则更新 | 缺 commit_sha / source_path / authority_level 时不得用于完成判断 |
| 向量同步先于 Git commit（提交）导致无法追溯 | 强制 commit / push / remote HEAD verified 后再 sync |
| secret（密钥）/ signed URL（签名 URL）/ 原始媒体误入库 | 黑名单过滤 + secret scan（密钥扫描）+ media exclusion（媒体排除） |
| Codex 把 RAG（检索增强）检索结果当完成证明 | `do_not_use_for_completion_claim（禁止用于完成判断）` 默认检查 |
| DeepSeek fallback_local_only（本地兜底）被写成真实 DeepSeek 参与 | 必须标 `not_deepseek_conclusion = true（不是 DeepSeek 结论）` |
| 向量库变成另一个旧规则仓库 | 定期 full_reindex（全量重建索引）和冲突标签清理 |
| sync 脚本失败但 Codex 写 completed（已完成） | completion_truth（完成真实性）必须检查 sync_status（同步状态） |
| RAG（检索增强）召回正确但无法解释路径 | Router（路由器）必须输出 evidence_paths（证据路径） |
| DeepSeek（深度供料）读取媒体或私密截图 | DeepSeek 只接收文本上下文；媒体判断由 Codex 本地工具完成 |
| branch staging（分支测试集合）被真实任务使用 | collection metadata（集合元数据）标 `allowed_for_real_tasks=false` |

## 8. next_readiness（是否可以进入下一步）

- `ready_for_vector_sync_dry_run_design（是否可进入向量同步空跑设计）`: `true`
- `ready_for_alibaba_vector_db_integration（是否可进入阿里向量库接入）`: `false`
- `reason（原因）`: 当前策略、白名单、黑名单、冲突图、三项 Router（路由器）fixture（测试用例）已具备 dry-run（空跑）设计基础；但尚无 chunk schema validator（切块元数据校验器）、source arbitration fixture（事实源仲裁测试用例）、secret/media chunk filter（密钥 / 媒体切块过滤器），因此不应直接接阿里向量库。

## 9. validation_plan_completed（本轮验证计划）

本轮应验证：

- 新增文件只在 `codex_log/vector_rag_router_design/`。
- 未修改 `GPT数据源/`、`codex_source/`、`codex_log/latest.md` 等正式机制入口。
- 未调用 DeepSeek（深度供料）、阿里、DashScope、DashVector API。
- 未读取或打印密钥。
- 未创建向量索引。
- 未生成媒体。
- `git diff --check` 通过。
- path-limited stage（按路径暂存），不得 `git add .`。
- staged diff secret scan（暂存差异密钥扫描）通过。
- commit / push / remote HEAD verification（远端 HEAD 校验）完成后才能写 completed（已完成）。

## 10. status_boundary（状态边界）

- 本轮不代表 RAG（检索增强）已接入。
- 本轮不代表 DeepSeek（深度供料）已调用。
- 本轮不代表向量库已创建。
- 本轮不代表同步脚本已实现。
- 本轮只是策略设计。
- 下一步应先做 `vector_sync_dry_run_design（向量同步空跑设计）`，不是直接接入阿里向量库。
