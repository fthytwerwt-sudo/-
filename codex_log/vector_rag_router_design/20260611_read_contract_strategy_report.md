# 20260611 Read Contract Strategy Report（读取契约策略报告）

## 1. execution_status（执行状态）

- `task_status（任务状态）`: `fixture_validation_passed`
- `project_route（项目路由）`: `video_factory`
- `branch（分支）`: `feature/vector-rag-router-design-20260611`
- `external_api_called（是否调用外部 API）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `embedding_generated（是否生成向量嵌入）`: `false`
- `vector_written（是否写入向量库）`: `false`
- `media_content_read（是否读取媒体内容）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`

## 2. files_created（新增文件）

| file_path（文件路径） | role（作用） | status（状态） |
|---|---|---|
| `codex_log/vector_rag_router_design/20260611_mandatory_read_manifest_policy.md` | mandatory_read_manifest（强制必读清单）策略 | created |
| `codex_log/vector_rag_router_design/20260611_read_proof_gate_policy.md` | read_proof_gate（读取证明闸门）策略 | created |
| `codex_log/vector_rag_router_design/20260611_read_contract_strategy_report.md` | 本轮总报告 | created |
| `codex_log/vector_rag_router_design/fixtures/20260611_read_contract_fixtures.json` | 三个读取契约 fixture | created |
| `codex_log/vector_rag_router_design/fixtures/20260611_read_contract_dry_run_results.json` | dry-run 结果 | generated |
| `scripts/vector_rag_router_design/强制读取契约空跑_mandatory_read_contract_dry_run.py` | 本地离线读取契约空跑脚本 | created |

## 3. core_design（核心设计）

RAG / Router 不能只给 Codex `evidence_paths（证据路径）` 或 `retrieved_chunks（召回片段）`。未来 Router 必须先生成：

```text
mandatory_read_manifest（强制必读清单）
-> Codex 读取原文件 / 指定章节 / schema / metadata
-> read_proof_report（读取证明报告）
-> pre_execution_read_gate（执行前读取闸门）
-> execution_allowed=true 或 blocked
```

读取证明不等于内容完成；它只证明“可以进入下一步执行或必须阻断”。

## 4. fixture_results（测试用例结果）

| fixture_name（测试用例名） | required_items_count（必读项数） | gate_status（闸门状态） | execution_allowed（是否允许执行） | pass_or_fail（通过或失败） |
|---|---:|---|---:|---|
| `new_material_read_contract` | 11 | `passed` | `true` | `passed` |
| `technical_preview_read_contract` | 10 | `blocked_conflict_unresolved` | `false` | `passed` |
| `voice_conflict_read_contract` | 9 | `blocked_conflict_unresolved` | `false` | `passed` |

Top-level dry-run result:

```json
{
  "overall_status": "passed",
  "fixture_count": 3,
  "passed_count": 3,
  "failed_count": 0,
  "missing_read_block_test": "passed"
}
```

## 5. key_decisions（关键判断）

| case（场景） | decision（判断） |
|---|---|
| 新增素材 | 默认 `additive_merge（补充合并）`；旧上下文、锁稿、旧素材清单、review pack 和素材解析包不可跳过 |
| 技术预览 / full.mp4 | `completed_allowed=false`；只能阻断为 `blocked_publish_candidate_unavailable` 或内部诊断，不能写 completed |
| 旧 Qwen / 阿里 B vs MiniMax | 旧 Qwen / 阿里 B 只能是 `reference_anchor_only`；当前正式声音锁仍是 MiniMax + `oldBMinimax20260528010200` |
| 缺读 / 未读 | 三个 fixture 的负例均输出 `blocked_missing_read` 且 `execution_allowed=false` |

## 6. safety_boundary（安全边界）

- 未调用外部 API。
- 未调用 DeepSeek。
- 未生成 embedding。
- 未写入向量库。
- 未读取密钥。
- 未读取媒体内容。
- 未生成视频 / 音频 / 图片。
- 未修改 `GPT数据源/`、`codex_source/`、`codex_log/latest.md` 等正式机制入口。

## 7. formal_patch_recommendation（正式补丁建议）

后续如果要把本机制接入正式 Router，建议只补一层 `pre_execution_read_contract_gate（执行前读取契约闸门）` 引用，不要把 fixture 逻辑直接塞进正式规则：

```yaml
pre_execution_read_contract_gate:
  mandatory_read_manifest_required: true
  read_proof_report_required: true
  blocked_if_manifest_missing: true
  blocked_if_read_proof_missing: true
  blocked_if_forbidden_to_skip_unread: true
  blocked_if_conflict_unresolved: true
```

本轮不直接修改正式入口文件。

## 8. git_sync（Git 同步）

- `git_sync_status_at_report_write（报告写入时 Git 状态）`: `pending_final_closeout`
- `stage_mode（暂存方式）`: `path_limited`
- `note（说明）`: 实际 commit SHA、push 和 remote HEAD verification 以最终对话回报为准。

## 9. 20260612 missing_report_boundary_patch（缺失报告执行边界补丁摘要）

- `MISSING_REPORT（缺失报告）` 只能证明缺失已识别，不能证明真实文件、真实章节、真实 schema 或真实 metadata 已经存在。
- 当 `MISSING_REPORT:` 出现在 `execution_required_items（执行必需项）` 或 `forbidden_to_skip（禁止跳过项）` 中时，`diagnostic_allowed=true`，但 `real_execution_allowed=false`、`execution_allowed=false`。
- 新增素材缺旧素材清单 / 新素材清单 / 素材解析包时，读取契约只能输出诊断 / 阻断报告，不能进入真实剪辑、TTS、导出或发片候选完成。
- `pre_execution_read_contract_gate（执行前读取契约闸门）` 建议最小接入正式 Router，只做入口引用，不把 fixture 逻辑塞进正式规则。
