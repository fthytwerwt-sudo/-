# 20260611 Mandatory Read Manifest Policy（强制必读清单策略）

## 1. status_boundary（状态边界）

- `document_status（文档状态）`: `strategy_design_only（仅策略设计）`
- `rag_runtime_implemented（RAG 运行时是否实现）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `embedding_generated（是否生成向量嵌入）`: `false`
- `external_api_called（是否调用外部 API）`: `false`
- `deepseek_called（是否调用 DeepSeek）`: `false`
- `formal_rules_modified（是否修改正式规则）`: `false`

本策略只定义 RAG / Router 未来必须交给 Codex 的读取契约，不接入真实 RAG runtime，不写入向量库，不替代仓库原文件读取。

## 2. purpose（目的）

`mandatory_read_manifest（强制必读清单）` 是从检索结果到执行动作之间的硬桥。RAG 可以返回 `evidence_paths（证据路径）` 和 `retrieved_chunks（召回片段）`，但 Router 必须把它们收敛成 Codex 本轮必须读取的原文件、章节和阻断条件。

没有 `mandatory_read_manifest` 时，Codex 不得进入具体执行。

## 3. required_schema（必填结构）

```yaml
mandatory_read_manifest:
  manifest_id:
  task_type:
  workflow_type:
  user_prompt_summary:
  route_decision_source:
  generated_by: router_or_rag_bridge
  source_arbitration_required:
  conflict_arbitration_required:
  must_read_items:
    - item_id:
      source_path:
      required_section:
      why_required:
      expected_decision_supported:
      authority_level:
      status_label:
      conflict_tags:
      required_read_depth: full_file | section_only | metadata_only | schema_only
      blocked_if_missing:
      blocked_if_conflict:
  optional_read_items:
    - source_path:
      why_optional:
  forbidden_to_skip:
    - item_id:
  done_when:
  blocked_if:
```

## 4. generation_rules（生成规则）

| trigger（触发） | required_manifest_behavior（清单行为） |
|---|---|
| 新增素材 / 重新剪 / 补素材 | 必须读取旧上下文、锁定文案、当前候选片、review pack、素材解析包或缺失报告，默认 `additive_merge` |
| technical preview / full.mp4 / route card 准备写 completed | 必须读取正式事实、执行规则、完成真实性预检、发片候选预检、review pack 和 Git 同步证据 |
| old Qwen / 阿里 B / MiniMax / 恢复以前声音 | 必须读取当前事实、最新日志、声音锁、冲突图和黑名单；旧声音只能作 reference anchor |
| RAG 召回结果冲突 | 必须标记 `conflict_arbitration_required=true`，冲突未解不得执行 |
| 关键路径不存在 | 必须生成 missing report 或直接 blocked，不得静默跳过 |

## 4A. missing_report_execution_boundary（缺失报告执行边界）

`MISSING_REPORT（缺失报告）` 只表示系统知道某个必需输入缺失。它不等于真实文件已读、不等于真实证据存在、不等于可以执行。

允许用于：

- `diagnostic_report（诊断报告）`
- `blocked_report（阻断报告）`
- `missing_input_list（缺失输入清单）`
- `next_step_request（下一步补齐请求）`
- `safe_next_step（安全下一步）`

禁止用于：

- `real_video_execution（真实视频执行）`
- `editing_execution（剪辑执行）`
- `tts_generation（TTS 生成）`
- `media_export（媒体导出）`
- `publish_candidate_completion（可发布候选片完成）`
- `content_validation_passed（内容验证通过）`
- `send_ready（可发送）`
- `voice_validation_passed（声音验证通过）`

如果执行必需项只由 `MISSING_REPORT:` 表示，则：

```yaml
diagnostic_allowed: true
real_execution_allowed: false
execution_allowed: false
gate_status: blocked_required_input_missing
```

## 5. authority_rules（权威规则）

读取项必须带 `authority_level（权威等级）` 和 `status_label（状态标签）`。默认优先级为：

1. `AGENTS.md`
2. `GPT数据源/08_当前正式事实.md`
3. `codex_log/latest.md`
4. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
5. `codex_source/19_project_state_action_router.md`
6. `codex_source/21_codex_judgment_permission_matrix.md`
7. `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
8. runtime evidence / fixture / dry-run result
9. `reference_only（仅参考）` / historical（历史）资料

如果 feature 分支策略和 main 当前事实冲突，Router 必须把 feature 结论标为 staging，不得写入 main 事实。

## 6. blocked_if（阻断条件）

必须 blocked 的情况：

- manifest 未生成。
- 必读文件缺失，且没有明确的 missing report。
- 必读章节未读。
- `forbidden_to_skip（禁止跳过项）` 中任一项未读。
- 召回片段和当前仓库文件冲突但未仲裁。
- metadata 缺 `source_path / authority_level / status_label / conflict_tags`。
- technical preview 被用作 completed 证明。
- 新增素材被默认当成 exclusive_new_only。
- old Qwen / 阿里 B 被恢复成正式 TTS provider。
- `execution_required_items（执行必需项）` 或 `forbidden_to_skip（禁止跳过项）` 中任一项只由 `MISSING_REPORT:` 表示。

## 7. done_when（完成标准）

`mandatory_read_manifest` 只在以下条件满足时可交给 Codex 执行：

1. 所有 must-read 项都有明确 `source_path`。
2. 所有 must-read 项都有 `required_section` 与 `required_read_depth`。
3. 所有禁止跳过项都列入 `forbidden_to_skip`。
4. 缺失项可以以 missing report 形式进入读取证明，但只能放行诊断 / 阻断报告，不能放行真实执行。
5. Router 明确输出 `source_arbitration_required` 和 `conflict_arbitration_required`。
