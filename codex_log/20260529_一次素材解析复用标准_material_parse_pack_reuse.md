# 20260529｜一次素材解析复用标准接入

## 本轮结论

- `task_result.status = mechanism_connected_not_video_delivery`
- `target_delivery = material_parse_pack_reuse_standard + no-render gate`
- 本轮制定并接入“一次素材解析，后续剪辑复用解析包”标准。
- 本轮未生成视频、未生成音频、未重新解析真实素材、未改最终文案、未推进项目状态。
- 后续真实剪辑任务仍需验证该标准是否稳定生效；本轮不写成“剪辑问题已解决”，也不写成“素材复用机制长期稳定”。

## double_parse_risk_audit（二次解析风险审计）

```text
double_parse_risk_audit:
  material_audit_outputs:
    - 已有 material_detail_report / material_evidence_contract / line_group_evidence_gate / auto_storyboard_preflight_report
    - 本轮补 material_parse_pack / source_segment_inventory 标准
  editing_flow_inputs:
    - 既有 editing_inference_function / editing_decision_pack / script_to_timeline_map
    - 本轮补 script_to_shot_execution_map / material_usage_ledger / duplicate_material_check
  does_editing_reparse_raw_media:
    - before: 部分成立；规则禁止硬配，但没有把 material_parse_pack 锁成唯一输入
    - after: blocked；剪辑阶段不得重新解析原始素材作为主要判断来源
  does_editing_require_material_parse_pack:
    - before: false
    - after: true
  current_duplicate_material_protection:
    - before: near_equivalent_material_substitution_preflight 可挡近似漂移与核心证据错位，但没有素材使用台账
    - after: duplicate_material_check 检查重复片段、连续重复、核心证据复用、主题相近硬配、cannot_support 和报告引用
  current_gap:
    - 后续真实剪辑任务需提供真实 material_parse_pack / source_segment_inventory / script_to_shot_execution_map / material_usage_ledger 并跑 gate
```

## 接入文件

- `skills/视频素材解析_video_material_audit/SKILL.md`：新增 `material_parse_pack` 与 `source_segment_inventory` 输出标准、过期条件和只读复用规则。
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`：`material_evidence_flow` 输出解析包；`aesthetic_editing_flow` 禁止二次解析并要求台账与重复检查。
- `codex_source/01_execution_rules.md`：新增 `material_parse_pack_reuse_gate`，接入发片候选预检套件前置 gate。
- `codex_source/19_project_state_action_router.md`：将素材解析包复用 gate 接入 `material_evidence_preflight_required` 和 `publish_candidate_preflight_suite_required`。
- `scripts/素材解析包复用闸门_material_parse_pack_reuse_gate.py`：新增 no-render 检查脚本。
- `scripts/发片候选预检套件_publish_candidate_preflight_suite.py`：新增 `material_parse_pack_reuse_preflight` 子报告。
- `codex_source/fixtures/素材解析包复用闸门_material_parse_pack_reuse_gate_cases.json`：新增 4 个最小 blocked fixture。
- `tests/test_material_parse_pack_reuse_gate.py`：覆盖 JSON parse、缺解析包、无理由重复片段、`cannot_support` 选中、主题相近硬配。

## 状态边界

- `video_generated = false`
- `audio_generated = false`
- `real_material_reparsed = false`
- `copy_changed = false`
- `content_validation = not_advanced`
- `send_ready = false`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor_ready = not_advanced`
