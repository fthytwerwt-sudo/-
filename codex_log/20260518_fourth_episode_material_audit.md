# 20260518｜第四期素材审计与项目内视频素材解析 skill

## route_decision

```yaml
project_route: video_factory
task_type:
  - mechanism_or_route_fix
  - project_file_change
  - review_diagnosis_audit
  - material_audit
current_project_state:
  - formal_operation_active
  - material_audit_needed
  - copy_iteration_prepare
execution_permission: audit_only
large_task_gate:
  triggered: true
  reason: "项目内 skill + 入口同步 + 4 个视频素材审计 + ffprobe/ffmpeg + contact sheet + JSON/Markdown/log + commit/push"
  lane_recommendation: audit_lane -> standard_lane
  parallel_recommendation: serial_only
  write_owner: Codex Integrator only
deepseek_supply_gate:
  supply_request: codex_log/supply_requests/20260518_fourth_episode_material_audit_pre_supply_request.json
  external_api_call_allowed: false
  fallback_status: fallback_local_only
  not_deepseek_conclusion: true
```

## state_action_router

```yaml
input_signal: "用户要求先新增项目内视频素材解析 skill，再按该 skill 审计第四期 4 个录制素材"
current_project_state:
  - formal_operation_active
  - material_audit_needed
  - copy_iteration_prepare
  - formal_next_execution_blocked
fact_source_arbitration:
  primary_source:
    - AGENTS.md
    - codex_source/00_codex_readme.md
    - codex_source/01_execution_rules.md
    - codex_source/19_project_state_action_router.md
    - codex_log/current_operation_target.md
    - codex_log/current_data_goal_anchor.md
  secondary_sources:
    - codex_log/material_audit/third_episode/20260517_third_episode_material_detail_report.md
    - review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md
  conflict_detected: true
  conflict_resolution: "仓库已有 DeepSeek 相关未提交改动；本轮不覆盖，后续提交前分开处理或明确同步。"
inferred_state:
  - project_skill_missing_repaired
  - fourth_episode_material_audit_completed_as_audit_only
confidence: high
trigger_mechanism:
  - Project State Action Router
  - large_task_gate
  - video_material_audit skill
selected_action: "创建项目内 skill，并用该 skill 生成第四期素材索引、时间码解析、证据强度和风险判断报告。"
forbidden_action:
  - final_copy
  - new_video_generation
  - publish_candidate_promotion
  - content_validation_advanced
  - send_ready_advanced
done_when: "skill 已创建并被第四期报告引用；4 个素材完成媒体检查、时间码解析、证据/风险判断；报告、JSON、latest 和 dated log 完成；验证和 Git 收尾完成。"
```

## material_root

`/Users/fan/Documents/视频工厂/素材录制/第四期`

## materials_found

| material_id | file_name | duration | resolution | audio_present | decodable |
| --- | --- | ---: | --- | --- | --- |
| `material_01` | `内建视网膜显示器 2026-05-17 23-59-42.mp4` | 91.50s | 2870x1676 | false | true |
| `material_02` | `内建视网膜显示器 2026-05-18 00-08-22.mp4` | 122.80s | 2872x1646 | false | true |
| `material_03` | `内建视网膜显示器 2026-05-18 00-12-15.mp4` | 59.47s | 2882x1726 | false | true |
| `material_04` | `内建视网膜显示器 2026-05-18 00-17-06.mp4` | 114.20s | 2906x1646 | false | true |

## files_created

- `skills/视频素材解析_video_material_audit/SKILL.md`
- `skills/视频素材解析_video_material_audit/README.md`
- `skills/视频素材解析_video_material_audit/templates/material_detail_report_template.md`
- `skills/视频素材解析_video_material_audit/templates/material_index_template.json`
- `codex_log/supply_requests/20260518_fourth_episode_material_audit_pre_supply_request.json`
- `codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_index.json`
- `codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md`
- `codex_log/20260518_fourth_episode_material_audit.md`
- `dist/material_audit/fourth_episode/material_01_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_02_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_03_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_04_contact_sheet_labeled.jpg`

## files_updated

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_log/latest.md`

## material_role_summary

- `material_01`: 说明当前不是马上写下一条，而是先做数据、文案、素材、风险和下一变量复盘。
- `material_02`: 最强主素材，展示一个 prompt 被拆成配置、字段、模板、报告和验收标准。
- `material_03`: 辅助证明执行单和 forbidden action，但隐私风险最高。
- `material_04`: 最强开头素材，直接支持“一句糊话变执行单”的新方向。

## strongest_evidence_segments

- `opening_evidence`: `material_04 00:55-01:30`
- `main_middle_evidence`: `material_02 00:20-01:50`
- `execution_boundary_evidence`: `material_03 00:05-00:25`
- `least_recommended_public_segment`: `material_03 00:30-00:55`

## verification

- `ffprobe`: 4 个素材均可读取。
- `ffmpeg_decode`: 4 个素材均可解码。
- `blackdetect`: 未观察到明显黑屏事件。
- `freezedetect`: 有少量阅读停留静帧，不视为素材损坏。
- `contact_sheet`: 4 个 labeled contact sheet 已生成。
- `skill_used`: 第四期报告已写明 `skill_used = skills/视频素材解析_video_material_audit/SKILL.md`。

## status_boundary

```yaml
new_video_generated: false
published_video_modified: false
final_copy_written: false
formal_next_video_prompt_generated: false
content_validation_advanced: false
send_ready_advanced: false
publish_candidate_advanced: false
current_data_goal_anchor_ready_advanced: false
source_media_committed: false
deepseek_actual_participation: false
deepseek_fallback_status: fallback_local_only
not_deepseek_conclusion: true
```

## next_target

ChatGPT 读取 `codex_log/material_audit/fourth_episode/20260518_fourth_episode_material_detail_report.md` 后，判断这 4 个素材最适合写哪条文案。当前最稳候选方向是：

```text
我用 AI 做视频，第一步不是写文案，而是拆任务
```
