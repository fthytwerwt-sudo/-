# 20260611 Router（路由器）Formal Patch Report

## 1. execution_status

- `task_status（任务状态）`: `passed`
- `branch（分支）`: `feature/vector-rag-router-design-20260611`
- `project_route（项目路由）`: `video_factory（视频工厂）`
- `patch_type（补丁类型）`: `validated_fixture_to_formal_router_bridge（已验证测试用例到正式路由桥接）`
- `formal_router_files_modified（是否修改正式 Router（路由器）文件）`: `true`
- `external_api_called（是否调用外部 API）`: `false`
- `vector_index_created（是否创建向量索引）`: `false`
- `media_generated（是否生成媒体）`: `false`
- `secrets_read_or_printed（是否读取或打印密钥）`: `false`
- `rag_runtime_implemented（RAG（检索增强）运行时是否实现）`: `false`
- `router_runtime_complete（Router（路由器）运行时是否完整落地）`: `false`

## 2. files_changed

| file_path（文件路径） | change_type（修改类型） | purpose（目的） |
|---|---|---|
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | update | 在 GPT Project / ChatGPT 侧最高 Router（路由器）入口接入 3 个 Router（路由器）判断 |
| `codex_source/19_project_state_action_router.md` | update | 在 Codex 侧 `Project State Action Router（路由器） / 项目状态动作总控器` 接入执行前动作策略 |
| `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md` | update | 将新素材、假完成、声音冲突挂到现有 workflow（工作流） |
| `scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py` | update | 复跑 fixture（测试用例）时同时输出 after-patch dry-run（空跑）结果 |
| `codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results.json` | update | 复跑后的当前 dry-run（空跑）结果 |
| `codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results_after_patch.json` | add | 本轮正式接线后的 dry-run（空跑）结果 |
| `codex_log/vector_rag_router_design/20260611_router_formal_patch_report.md` | add | 本轮 Router（路由器）正式接线报告 |

## 3. router_wiring_summary

| router_gate（路由闸门） | trigger（触发条件） | default_decision（默认判断） | blocked_if（阻断条件） |
|---|---|---|---|
| `material_delta_type_router（素材增量类型路由器）` | 新增素材、补素材、素材录好了、重新剪、重做中段、替换素材、给新素材路径、未说明旧素材是否废弃 | 默认 `material_delta_type = additive_merge（补充合并）`；只有明确只用新素材或指定替换范围才允许 `exclusive_new_only（只用新增素材）` / `replacement_merge（替换合并）` | 旧候选片、锁定文案、旧素材清单、新素材清单、素材解析包或新旧素材关系不清时 `unclear_blocked（不清楚则阻断）` |
| `completion_truth_preflight_router（完成真实性预检路由器）` | 做视频、发片候选、完整成片、修片、重新导出、视频执行、准备写 `completed（已完成）`、只有 technical preview / full.mp4 / route card / preflight package | 视频类任务不得直接写 `completed（已完成）`；必须先走 `completion_truth_preflight（完成真实性预检）` | 缺发片候选基线、预检套件、review pack（审片包）、声音、字幕、证据、卡片、完成真实性报告或 Git 同步时 `blocked（阻断）` / `internal_diagnostic_only（仅内部诊断）` |
| `voice_route_conflict_gate（声音路线冲突闸门）` | 声音、TTS、B 方案、旧声音、Qwen、阿里、百炼、MiniMax、恢复以前声音、生成 / 替换音轨、判断声音通过 | `old_qwen_role = reference_anchor_only（仅参考锚点）`；正式声音锁仍为 MiniMax + `oldBMinimax20260528010200` | 旧 Qwen / 阿里 B 恢复正式 provider、MiniMax 系统音色替代、旧女性候选替代、缺用户试听确认、缺实际音频验证时 `blocked（阻断）` |

## 4. fixture_regression

| fixture_name（测试用例名） | before_status（修改前状态） | after_status（修改后状态） | pass_or_fail（通过或失败） |
|---|---|---|---|
| `new_material_defaults_to_additive_merge（新增素材默认补充合并）` | `passed` | `passed` | `passed` |
| `technical_preview_cannot_complete（技术预览不能完成）` | `passed` | `passed` | `passed` |
| `old_qwen_b_is_reference_anchor_only（旧 Qwen / 阿里 B 仅参考锚点）` | `passed` | `passed` | `passed` |

## 5. validation_evidence

Commands run:

```bash
python3 scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py
python3 -m json.tool codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results.json
python3 -m json.tool codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results_after_patch.json
python3 -m py_compile scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py
```

After-patch result:

```json
{
  "overall_status": "passed",
  "fixture_count": 3,
  "passed_count": 3,
  "failed_count": 0,
  "external_api_called": false,
  "secrets_read_or_printed": false,
  "media_generated": false
}
```

## 6. status_boundary

- 本轮不代表 RAG（检索增强）已接入。
- 本轮不代表向量库已接入。
- 本轮不代表 Router（路由器）runtime（运行时）完整落地。
- 本轮只是把 3 个已验证 fixture（测试用例）的判断接进 Router（路由器）正式入口。
- 本轮未调用阿里 / DashScope / DashVector API（外部接口）。
- 本轮未生成视频 / 音频 / 图片 / 字幕 / 卡片。
- 本轮未推进 `content_validation（内容验证）`、`send_ready（可发送）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`。
- 下一步仍需真实任务或 RAG（检索增强）检索 dry-run（空跑）验证。
