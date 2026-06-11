# 20260611 向量同步策略 Vector Sync Policy

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `project_route（项目路由）`: `video_factory（视频工厂）`
- `branch（分支）`: `feature/vector-rag-router-design-20260611`
- `external_api_called（是否调用外部 API）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `rag_runtime_implemented（RAG（检索增强）运行时是否实现）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`

本文件只定义未来 GitHub / 本地仓库与 Vector DB（向量数据库）的同步策略，不创建 collection（集合），不写入 embedding（向量嵌入），不调用阿里 / DashScope / DashVector API。

## 2. source_of_truth_policy（事实源策略）

| system（系统） | role（职责） | authority（权威性） | conflict_rule（冲突规则） |
|---|---|---|---|
| GitHub / local repo（GitHub / 本地仓库） | `source_of_truth（主事实源）` | 最高 | 所有正式规则、状态、机制、日志、报告以当前仓库文件为准 |
| Vector DB（向量数据库） | `retrieval_index（检索索引）` / `cache_layer（缓存层）` | 非事实源 | 与仓库冲突时必须降权或重建，不能反向覆盖仓库 |
| RAG（检索增强） | `context_retrieval（上下文召回）` | 非拍板层 | 只返回证据路径与片段，不创建规则、不替代 Router（路由器） |
| Router（路由器） | `source_arbitration（事实源仲裁）` | 判断层 | 必须输出 `evidence_paths（证据路径）` 与 `conflict_arbitration（冲突仲裁）` |

## 3. collection_policy（集合隔离策略）

| collection_name（集合名） | source_branch（来源分支） | purpose（用途） | allowed_for_real_tasks（是否允许真实任务） |
|---|---|---|---|
| `video_factory_main（视频工厂正式集合）` | `main（主分支）` | 服务正式检索与真实任务 | `true`，但仍需 Router（路由器）仲裁 |
| `video_factory_branch_staging（视频工厂分支测试集合）` | `feature/*（功能分支）` | 测试策略、fixture（测试用例）、dry-run（空跑） | `false`，不得污染 main（主分支）检索 |

分支合并策略：

1. feature（功能分支）只同步到 staging collection（测试集合）。
2. 合并 main（主分支）并完成远端 HEAD 校验后，才允许同步到 main collection（正式集合）。
3. 若 feature（功能分支）策略未合并，不得把分支结论写入 `video_factory_main（视频工厂正式集合）`。

## 4. sync_modes（同步模式）

| sync_mode（同步模式） | trigger（触发条件） | action（动作） |
|---|---|---|
| `full_reindex（全量重建索引）` | 第一次建库、白名单 / 黑名单大改、metadata schema（元数据结构）大改、规则清仓后首次正式入库、main（主分支）合并重大机制补丁后 | 从允许入库文件重新 chunk（切块）、重新 metadata（元数据）、重新写入集合 |
| `incremental_sync（增量同步）` | 正式规则文件修改、Router（路由器）文件修改、Skill Registry（技能注册表）修改、latest（最新日志）新增机制事实、审片 / 素材 / 运营记录需要检索 | 只同步本次 commit（提交）影响的允许文件和新增 / 修改 chunk（切块） |
| `demote_or_delete_sync（降权或删除同步）` | 旧规则被替代、标记 deprecated（已过时）、文件删除、冲突裁决、current_active 降为 reference_only（仅参考） | 更新 `authority_level（权威等级）`、`status_label（状态标签）`、`superseded_by（被替代者）`，必要时删除 chunk（切块） |

## 5. commit_first_policy（先 Git 后向量同步）

未来同步必须遵守：

```text
repo_change（仓库变更）
-> path_limited_stage（按路径暂存）
-> secret_scan（密钥扫描）
-> commit（提交）
-> push（推送）
-> remote_head_verified（远端 HEAD 校验）
-> vector_sync_dry_run（向量同步空跑）
-> human_or_chatgpt_approval（用户或 ChatGPT 确认）
-> vector_sync_apply（正式向量同步）
```

禁止：

- 在 commit（提交）前同步向量。
- 在 push（推送）前同步 main collection（正式集合）。
- 在 remote HEAD 未校验时把向量库写成当前事实。
- sync（同步）失败后把仓库状态写成 failed；向量库只是索引，不能影响 GitHub 主事实。

## 6. metadata_required（必须元数据）

每个 chunk（切块）必须携带：

```yaml
repo_full_name: fthytwerwt-sudo/-
project_route: video_factory
branch: main_or_feature_branch
commit_sha: git_commit_sha
source_path: in_repo_path
heading_path: markdown_heading_or_json_pointer
content_hash: sha256_of_chunk_text
authority_level: canonical_current | current_runtime_evidence | current_auxiliary | reference_only | legacy_demoted | conflict_pending
status_label: confirmed_by_repo | partial | pending_validation | recommendation | deprecated
updated_at: iso8601_or_commit_time
supersedes: optional_prior_chunk_id
superseded_by: optional_new_chunk_id
conflict_tags: list
workflow_type: optional_workflow_type
task_type: optional_task_type
validation_required: true_or_false
do_not_use_for_completion_claim: true_or_false
```

## 7. ingestion_scope（入库范围）

允许入库必须以 `20260611_vector_ingestion_whitelist.md（向量入库白名单）` 为准，优先包括：

- `AGENTS.md（工作区规则）`
- `GPT数据源/08_当前正式事实.md（当前正式事实）`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器）`
- `codex_source/19_project_state_action_router.md（Codex 侧路由器）`
- `codex_source/21_codex_judgment_permission_matrix.md（Codex 判断权限表）`
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md（工作流入口索引）`
- `codex_log/latest.md（最新日志）`，按日期标题切块。
- 允许的 review pack（审片包）summary / manifest / route map。
- 经过脱敏的机制报告、fixture（测试用例）和 dry-run（空跑）结果。

禁止入库必须以 `20260611_vector_ingestion_blacklist.md（向量入库黑名单）` 为准，至少包括：

- `.env`、`.env.local`、本地授权文件、任何真实 API key / token / secret。
- 原始视频、音频、图片、截图、contact sheet、样本音频。
- `public/**` 和 unrelated untracked files（无关未跟踪文件）。
- signed URL（签名 URL）或含凭证 query 的 URL。
- DeepSeek（深度供料）原始 supply pack（供料包）作为事实源；只能以 `reference_only（仅参考）` 标记入库摘要。

## 8. demote_delete_policy（降权 / 删除策略）

旧规则不默认物理删除，优先 metadata（元数据）降权：

| case（情况） | policy（策略） |
|---|---|
| 当前规则替代旧规则 | 旧 chunk（切块）标记 `legacy_demoted（历史降权）`，新 chunk 填 `supersedes（替代）` |
| 规则已明确 deprecated（已过时） | 标记 `deprecated（已过时）`，默认检索排除 |
| 冲突尚未裁决 | 标记 `conflict_pending（冲突待裁决）`，Router（路由器）必须阻断状态推进 |
| 文件删除 | 删除对应 chunk 或标记 tombstone（墓碑记录），保留删除 sync report（同步报告） |
| reference lineage（参考谱系）仍有价值 | 标记 `reference_only（仅参考）`，不得用于完成判断 |

## 9. sync_report_schema（同步报告结构）

每次 sync（同步）必须输出报告：

```yaml
sync_status: passed | blocked | failed
vector_collection: video_factory_main_or_branch_staging
repo_full_name: fthytwerwt-sudo/-
branch: branch_name
commit_sha: git_commit_sha
changed_files: []
indexed_chunks: []
skipped_chunks: []
demoted_chunks: []
deleted_chunks: []
secret_scan_result: passed_or_blocked
media_exclusion_result: passed_or_blocked
blacklist_filter_result: passed_or_blocked
metadata_validation_result: passed_or_blocked
conflict_tags_added: []
external_api_called: true_or_false
secrets_read_or_printed: false
```

## 10. formal_patch_recommendation（正式补丁建议）

后续若进入实现阶段，建议只新增向量同步 dry-run（空跑）脚本与 schema（结构），不要直接接阿里向量库：

1. 新增 `vector_sync_dry_run（向量同步空跑）`：只读取 staged / committed diff，输出将入库 / 跳过 / 降权清单。
2. 新增 `chunk_metadata_validator（切块元数据校验器）`：检查 source_path、commit_sha、authority_level、status_label、do_not_use_for_completion_claim。
3. 待 dry-run（空跑）稳定后，再单独授权 `vector_sync_apply（正式向量同步）`。
