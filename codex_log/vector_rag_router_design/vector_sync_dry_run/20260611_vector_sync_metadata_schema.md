# 20260611 Vector Sync Metadata Schema（向量同步元数据结构）

## status_boundary

- document_status: `dry_run_schema_only`
- external_api_called: `false`
- vector_index_created: `false`
- embedding_generated: `false`
- vector_written: `false`
- deepseek_called: `false`

## required_chunk_metadata

每个 `would_index_chunks` 条目必须包含：

| field | required | note |
|---|---:|---|
| `repo_full_name` | yes | 固定为 `fthytwerwt-sudo/-` |
| `project_route` | yes | 固定为 `video_factory` |
| `branch` | yes | 当前执行分支 |
| `commit_sha` | yes | dry-run 的 head ref SHA |
| `source_path` | yes | 仓库内相对路径 |
| `heading_path` | yes | Markdown heading / JSON pointer / Python pseudo section |
| `content_hash` | yes | chunk 文本的 SHA-256 |
| `authority_level` | yes | `canonical_current` / `current_runtime_evidence` / `current_auxiliary` / `reference_only` / `legacy_demoted` / `conflict_pending` |
| `status_label` | yes | `confirmed_by_repo` / `partial` / `pending_validation` / `recommendation` / `deprecated` |
| `updated_at` | yes | commit timestamp |
| `conflict_tags` | yes | list，允许为空 |
| `do_not_use_for_completion_claim` | yes | boolean |

## collection_policy

| branch | target_collection | allowed_for_real_tasks |
|---|---|---:|
| `main` | `video_factory_main` | `true` |
| `feature/*` | `video_factory_branch_staging` | `false` |

## source_authority_defaults

| source | authority_level | status_label | completion_claim |
|---|---|---|---|
| `AGENTS.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `GPT数据源/08_当前正式事实.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `codex_source/19_project_state_action_router.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `codex_source/21_codex_judgment_permission_matrix.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` | `canonical_current` | `confirmed_by_repo` | allowed only with validation |
| `codex_log/latest.md` | `current_runtime_evidence` | `confirmed_by_repo` | allowed only with validation |
| `codex_log/vector_rag_router_design/*.md` | `current_auxiliary` | `recommendation` | `do_not_use_for_completion_claim=true` |
| `codex_log/vector_rag_router_design/fixtures/*.json` | `current_runtime_evidence` | `confirmed_by_repo` | `do_not_use_for_completion_claim=true` |
| `project_source/` | `legacy_demoted` | `deprecated` | `do_not_use_for_completion_claim=true` |
| `codex_log/deepseek_supply/` | `reference_only` | `partial` | `do_not_use_for_completion_claim=true` |

## apply_boundary

本 schema 只服务 `vector_sync_dry_run（向量同步空跑）`。任何真实同步必须另起执行单，且必须在 commit / push / remote HEAD verification 后，经用户授权进入 `vector_sync_apply`。
