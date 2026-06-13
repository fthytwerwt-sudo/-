# 20260613 DeepSeek Positioning For RAG-First Adapter

## 1. status

- `project_route`: `video_factory`
- `document_type`: `adapter_design`
- `formal_runtime_rule`: `false`
- `deepseek_triggered_this_round`: `false`
- `not_deepseek_conclusion`: `true`

This file defines the target DeepSeek position for the future agent-service-toolkit adapter. It does not modify the current formal DeepSeek controller or request schema.

## 2. old_position_to_repair

DeepSeek must be moved away from:

- `default_file_supplier`
- `default_context_reader`
- `default_project_memory`
- `mandatory_by_default_for_every_task`
- `deep_file_prefetch_as_default`

Reason:

- GitHub repo files are still `source_of_truth`.
- DashVector / Vector RAG is now the intended retrieval/cache layer.
- DeepSeek should reason over supplied evidence, not act as a project memory or file reader.

## 3. target_position

DeepSeek should become:

| Role | Meaning | Allowed use |
|---|---|---|
| `reasoning_reviewer` | Reviews reasoning after retrieval/readback | advisory |
| `risk_auditor` | Checks status, execution, and boundary risks | advisory/blocker suggestion |
| `conflict_second_opinion` | Reviews conflicts between sources or mechanisms | escalation to Router/GPT |
| `fallback_context_synthesizer` | Summarizes known local evidence if true call unavailable | must mark fallback |
| `external_deep_supply_optional` | Supplies external deep reasoning only when asked/needed | must be sourced/reviewed |

## 4. trigger_policy

DeepSeek can trigger only when one or more are true:

- `rag_empty`
- `rag_low_confidence`
- `source_conflict`
- `mechanism_conflict`
- `high_risk_execution`
- `pre_execution_risk_review`
- `post_execution_discrepancy_review`
- `user_explicit_request`
- `external_deep_reasoning_needed`

DeepSeek should not trigger for:

- ordinary project file lookup;
- normal `AGENTS.md / GPT数据源 / codex_source / codex_log/latest.md` reading;
- default context stuffing;
- replacing DashVector search;
- replacing source readback;
- proving completion.

## 5. input_contract

DeepSeek input should be a bounded review package:

```yaml
deepseek_review_input:
  retrieval_manifest:
    required: true
  source_readback:
    required: true
  retrieval_gap_report:
    required: true
  user_goal:
    required: true
  risk_questions:
    required: true
  forbidden_actions:
    - write_files
    - commit
    - push
    - status_promotion
    - source_of_truth_replacement
```

## 6. output_contract

DeepSeek output should be structured:

```yaml
deepseek_review_output:
  provenance:
    enum:
      - deepseek_reasoning
      - risk_review
      - external_deep_supply
      - conflict_second_opinion
      - fallback_local_only
      - not_deepseek_conclusion
  reasoning_review:
  risk_report:
  conflict_report:
  missing_context_report:
  executor_handoff_suggestions:
  must_not_be_used_as:
    - source_of_truth
    - completion_proof
    - write_permission
```

## 7. forbidden_actions

DeepSeek must never:

- write files;
- edit files;
- delete files;
- commit;
- push;
- replace GitHub repo facts;
- replace DashVector / Vector RAG retrieval;
- put unresolved conclusions into formal project facts;
- decide final business/content validation alone;
- read `.env`, API keys, token files, raw media, or Git internals;
- let local fallback be reported as true DeepSeek participation.

## 8. adapter_graph_position

Target position inside agent-service-toolkit style graph:

```text
retrieval_manifest
-> source_readback
-> retrieval_gap_report
-> deepseek_trigger_decision
   -> if false: skip_deepseek
   -> if true: deepseek_review_node
-> blocked_if_check
-> human_review_interrupt
-> write_executor_handoff
```

DeepSeek is after RAG/readback and before risky handoff. It is not before repository reading.

## 9. formal_patch_needed_later

A later controlled formal patch should update:

- `AGENTS.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`

Patch should replace mandatory default supply with conditional review policy while preserving backward compatibility for older DeepSeek supply logs as historical evidence.
