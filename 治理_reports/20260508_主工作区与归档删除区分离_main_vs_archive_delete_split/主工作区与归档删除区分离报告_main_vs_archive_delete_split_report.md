# 主工作区与归档删除区分离报告 main_vs_archive_delete_split_report

## 1. 本轮目标

- 在唯一正式工作区内部创建 `归档删除区_archive_delete_zone/`
- 建立 `current_workspace` 与 `archive_delete_zone` 两套清单
- 先把高风险旧口径污染源从默认工作区语义里切出去
- 不做任何破坏性删除

## 2. 创建目录

- `归档删除区_archive_delete_zone/`
- `归档删除区_archive_delete_zone/待归档_archive_candidates/`
- `归档删除区_archive_delete_zone/待删除_delete_candidates/`
- `归档删除区_archive_delete_zone/旧口径隔离_stale_context_quarantine/`
- `归档删除区_archive_delete_zone/旧入口隔离_legacy_entrypoint_quarantine/`
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/`
- `归档删除区_archive_delete_zone/原始素材待确认_raw_assets_pending_confirmation/`
- `归档删除区_archive_delete_zone/清单_manifests/`

## 3. 已移动文件

### 旧口径隔离

- `project_source/07_current_formal_facts.md`

### 旧入口隔离

- `codex_source/00_current_repo_audit.md`
- `codex_source/02_codex_index.md`
- `codex_source/07_formal_api_demo_target_plan.md`

### 旧产物候选

- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_contact_sheet.jpg`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_cut_map.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_full.mp4`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_review_manifest.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_run_summary.json`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_summary.json`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_timeline.json`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_summary.json`

## 4. 未移动但已标记

- `README.md`
- `cases/demo.md`
- `generate_demo.py`
- `video_builder.swift`
- `package.json`
- `执行日志_codex_log/最新摘要_latest.md`
- `素材录制/`
- `素材库_assets/`

## 5. 主要工作区最小保留清单

统一看：

- `归档删除区_archive_delete_zone/清单_manifests/主要工作区清单_current_workspace_manifest.md`

本轮 `已确认` 保留不动：

- 当前事实入口：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_log/latest.md`、`codex_log/current_*`
- 当前动态事实包：`GPT数据源/`
- 当前复盘系统：`review_loop/`
- 当前正式复审入口：`dist/latest_review_pack/review_manifest.md`、`summary.json`、`visual_route_map.json`、`visual_route_validation_report.json`
- 当前代码 / 工作台执行层：`formal_api_demo_core.py`、`formal_api_demo_cloud_assembly.py`、`scripts/`、`tests/`、`compose.yaml`、`config/`、`工作台模板/`
- 当前素材区：`素材库_assets/`
- P1 保留：`素材录制/`

## 6. 归档删除区清单

统一看：

- `归档删除区_archive_delete_zone/清单_manifests/归档删除区清单_archive_delete_manifest.md`

## 7. 引用修正

本轮已最小修正：

- `AGENTS.md`
  - 默认摘要入口从 `执行日志_codex_log/最新摘要_latest.md` 改回 `codex_log/latest.md`
  - 明确 `归档删除区_archive_delete_zone/` 不是默认读取入口
- `codex_source/00_codex_readme.md`
  - 当前正式事实补读改回 `GPT数据源/08_当前正式事实.md`
  - 历史 `project_source/07_current_formal_facts.md` 改成仅归档参考
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/02_term_definitions_and_state_boundaries.md`
- `project_source/06_project_index.md`
- `project_source/09_target_state_plan.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/01_codex_source_plan.md`

## 8. 禁止项检查

- `已确认` 未删除任何文件
- `已确认` 未移动 `素材录制/`
- `已确认` 未移动 `素材库_assets/`
- `已确认` 未移动 `GPT数据源/`
- `已确认` 未修改 `GPT 数据源/`
- `已确认` 未移动 `dist/latest_review_pack/` 当前正式入口文件
- `已确认` 未修改 `content_validation`
- `已确认` 未修改 `send_ready`
- `已确认` 未修改 `codex_log/current_publish_target.md`
- `已确认` 未新建外部工作区
- `已确认` 未执行 Git 高风险清理命令

## 9. 下一轮建议

下一轮优先级：

1. 单独处理 `执行日志_codex_log/` 的多项目旧入口风险
2. 单独处理 root demo 入口降权或 README 改写
3. 继续细分 `dist/` 与 `复审包_review_packs/` 的 archive/delete/user-confirmation 三层清单
4. 在用户确认前，不触碰 `素材录制/`
