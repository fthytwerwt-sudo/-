# 20260611 Read Proof Gate Policy（读取证明闸门策略）

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `rag_runtime_implemented（RAG 运行时是否实现）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `embedding_generated（是否生成向量嵌入）`: `false`
- `external_api_called（是否调用外部 API）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`

本策略只定义 Codex 执行前必须输出的读取证明，不代表 Codex 已完成任何视频、音频、图片或正式生产任务。

## 2. purpose（目的）

`read_proof_gate（读取证明闸门）` 用来阻止 Codex 只看本轮 prompt、只看 RAG 摘要、只看新增素材或只看中间产物就进入执行。读取证明必须回到原始仓库文件、章节和缺失报告。

## 3. read_proof_report_schema（读取证明报告结构）

```yaml
read_proof_report:
  manifest_id:
  all_required_files_read:
  all_required_sections_read:
  missing_required_items:
  conflicts_found:
  conflict_arbitration:
  blocked_if_unread:
  diagnostic_allowed:
  real_execution_allowed:
  missing_report_items:
  execution_required_missing_items:
  gate_status: passed | blocked_missing_read | blocked_conflict_unresolved | blocked_source_not_found | blocked_stale_source | blocked_required_input_missing
  read_items:
    - item_id:
      source_path:
      required_section:
      read_status:
      evidence_summary:
      decision_supported:
      missing_or_conflict:
      proof_level: file_read | section_read | schema_checked | metadata_checked | insufficient
```

## 4. pre_execution_read_gate_schema（执行前读取闸门结构）

```yaml
pre_execution_read_gate:
  mandatory_read_manifest_loaded:
  read_proof_report_loaded:
  all_required_files_read:
  missing_required_files:
  missing_required_sections:
  conflicts_found:
  missing_report_items:
  execution_required_missing_items:
  diagnostic_allowed:
  real_execution_allowed:
  gate_status:
  execution_allowed:
  blocked_reason:
```

## 5. gate_rules（闸门规则）

| condition（条件） | gate_status（闸门状态） | execution_allowed（是否允许执行） |
|---|---|---|
| manifest 和 proof 均加载，必读项全部已读，且无未解冲突 | `passed` | `true` |
| 任一禁止跳过项未读 | `blocked_missing_read` | `false` |
| 必读文件不存在且无 missing report | `blocked_source_not_found` | `false` |
| 必读章节未读 | `blocked_missing_read` | `false` |
| source arbitration 未完成 | `blocked_conflict_unresolved` | `false` |
| technical preview 被当 completed | `blocked_conflict_unresolved` | `false` |
| old Qwen / 阿里 B 被当正式 TTS provider | `blocked_conflict_unresolved` | `false` |
| 旧规则高于当前正式事实 | `blocked_stale_source` | `false` |
| `MISSING_REPORT:` 出现在 `execution_required_items` 或 `forbidden_to_skip` | `blocked_required_input_missing` | `false` |

当 `blocked_required_input_missing` 触发时：

```yaml
diagnostic_allowed: true
real_execution_allowed: false
execution_allowed: false
blocked_reason: execution-required input is represented only by MISSING_REPORT
```

## 6. proof_level_rules（证明级别规则）

- `file_read`: 已读取全文。
- `section_read`: 已读取指定章节。
- `schema_checked`: 已检查 JSON / fixture / schema 结构。
- `metadata_checked`: 只允许用于 Git 状态、review pack pointer、路径指针等元数据；如果对象是 `MISSING_REPORT:`，只能证明缺失已识别，不能证明真实输入已读取。
- `insufficient`: 不足以继续执行，必须进入 blocked。

## 7. failure_handling（失败处理）

读取证明失败时，Codex 必须输出：

- `blocked_reason（阻断原因）`
- `missing_required_items（缺失必读项）`
- `conflicts_found（发现冲突）`
- `safe_next_step（安全下一步）`

不得把以下内容写成 completed：

- RAG 摘要。
- DeepSeek 供料。
- technical preview。
- `full.mp4` 存在。
- route card / preflight package。
- 未经用户确认的声音验证。
- 未 push / 未 remote HEAD verified 的本地修改。
