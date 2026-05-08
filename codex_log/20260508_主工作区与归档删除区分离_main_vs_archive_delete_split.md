# 20260508｜主工作区与归档删除区分离

## 本轮定位

- `已确认` 本轮只做《视频工厂》当前工作区的“主工作区 / 归档删除区”分离。
- `已确认` 本轮允许创建隔离目录与移动明确旧口径 / 旧入口 / 旧 dist 副本候选。
- `已确认` 本轮不删除任何文件。

## route_decision 摘要

- `project_route = video_factory`
- `task_type = local_file_governance + mechanism_or_route_fix + review_diagnosis_audit + project_file_change`
- `large_task_gate.triggered = true`
- `lane_recommendation = audit_lane`
- `parallel_recommendation = serial_only`
- `execution_permission = granted_for_internal_split_and_reference_rewire`

## 本轮已完成

- 已创建 `归档删除区_archive_delete_zone/` 及其子目录。
- 已创建：
  - `主要工作区清单_current_workspace_manifest.md`
  - `归档删除区清单_archive_delete_manifest.md`
  - `本轮移动记录_move_log_20260508.md`
  - `回滚说明_rollback_guide.md`
- 已隔离旧口径：
  - `project_source/07_current_formal_facts.md`
- 已隔离旧入口：
  - `codex_source/00_current_repo_audit.md`
  - `codex_source/02_codex_index.md`
  - `codex_source/07_formal_api_demo_target_plan.md`
- 已隔离旧 `dist/latest_review_pack/` 副本：
  - 全部 `AI做PPT踩坑_成品候选_v3_*`
  - `AI做PPT踩坑_成品候选_v31_review_manifest.md`
  - `AI做PPT踩坑_成品候选_v31_summary.json`
- 已更新默认入口引用，避免后续默认读取已隔离文件。

## 本轮未移动但已标记

- `README.md`
- `cases/demo.md`
- `generate_demo.py`
- `video_builder.swift`
- `package.json`
- `执行日志_codex_log/最新摘要_latest.md`
- `素材录制/`
- `素材库_assets/`

## 禁止项回查

- `已确认` 未删除任何文件。
- `已确认` 未移动 `素材录制/`。
- `已确认` 未移动 `素材库_assets/`。
- `已确认` 未移动 `GPT数据源/`。
- `已确认` 未修改 `GPT 数据源/`。
- `已确认` 未移动 `dist/latest_review_pack/review_manifest.md`、`summary.json`、`visual_route_map.json`、`visual_route_validation_report.json`。
- `已确认` 未修改 `content_validation`、`send_ready`、`codex_log/current_publish_target.md`。
- `已确认` 未新建外部工作区。

## 报告路径

- `治理报告`：`治理_reports/20260508_主工作区与归档删除区分离_main_vs_archive_delete_split/主工作区与归档删除区分离报告_main_vs_archive_delete_split_report.md`

## 下一个目标

先单独处理 `执行日志_codex_log/` 与 root demo 入口的降权，再决定哪些历史产物进入真正的待归档 / 待删除候选清单。
