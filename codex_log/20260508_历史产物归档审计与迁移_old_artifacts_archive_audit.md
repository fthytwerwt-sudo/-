# 20260508｜历史产物归档审计与迁移

## 本轮定位

- `已确认` 本轮只做历史产物扫描、分桶和安全迁移。
- `已确认` 本轮不删除任何文件，不移动原始素材，不触碰 `dist/latest_review_pack/` 当前正式入口。

## route_decision 摘要

- `project_route = video_factory`
- `task_type = local_file_governance + mechanism_or_route_fix + review_diagnosis_audit + project_file_change`
- `large_task_gate.triggered = true`
- `lane_recommendation = audit_lane`
- `parallel_recommendation = serial_only`
- `execution_permission = granted_for_old_artifact_audit_and_safe_archive_moves`

## 本轮已完成

- 已扫描：
  - `dist/`
  - `复审包_review_packs/`
  - `验证_reports/`
  - `样片报告_sample_reports/`
  - `素材检查_reports/`
  - `本地归档_local_archive/`
- 已明确迁移 1 组 tracked 历史产物：
  - `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/`
  - 新路径：`归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/...`
- 已确认保留：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与当前 reference 包
- 已标记待用户确认：
  - `dist/reference_packs/`
  - `dist/voice_trials/`
  - `dist/完整成片_full_videos/`
  - `本地归档_local_archive/`
  - `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
- 已标记确认后可删候选：
  - `样片报告_sample_reports/`
  - `dist/prototypes/`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - `dist/.DS_Store`

## 本轮未迁移但已识别的旧本地输出

- `dist/_guardrail_probe_20260408/`
- `dist/_provider_rotation_probe/`
- `dist/_provider_rotation_realcheck/`

说明：它们是本地未跟踪历史输出；本轮不强行迁入 Git 归档轨迹。

## 报告路径

- `治理报告`：`治理_reports/20260508_历史产物归档审计与迁移_old_artifacts_archive_audit/历史产物归档审计与迁移报告_old_artifacts_archive_audit_report.md`

## 下一个目标

先拆 `voice_trials/` 和 `reference_packs/` 的 current reference / pure history 边界，再决定下一轮更细的历史产物迁移。
