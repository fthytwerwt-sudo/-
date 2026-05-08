# 20260508｜主工作区与外部归档删除区彻底分离

## 本轮定位

- `已确认` 本轮不是继续泛审计，而是执行主工作区与 archive-only 外部目录的物理分离。
- `已确认` 外部 archive-only 目录：`/Users/fan/Documents/视频工厂归档+删除`
- `已确认` 该目录只用于归档 / 删除候选池，不是执行工作区。

## route_decision 摘要

- `project_route = video_factory`
- `task_type = local_file_governance + mechanism_or_route_fix + review_diagnosis_audit + project_file_change`
- `large_task_gate.triggered = true`
- `lane_recommendation = audit_lane`
- `parallel_recommendation = serial_only`
- `execution_permission = granted_for_workspace_vs_external_archive_split`

## 本轮已完成

- 已把以下 tracked 历史媒体 / 旧产物外移到外部 archive-only 目录：
  - `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/`
  - `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`
  - `dist/voice_trials/20260425_round28_10s_voice_trial/`
  - `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`
- 已把以下 untracked 大目录外移到外部 archive-only 目录：
  - `dist/完整成片_full_videos/`
  - `本地归档_local_archive/`
  - `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
  - `样片报告_sample_reports/`
  - `dist/prototypes/`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - 内部 `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/` 里的旧 probe/provider 输出

## 本轮保留不动

- `dist/latest_review_pack/` 当前正式入口
- `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/` 当前 v31 基线包与 reference 包
- `素材录制/`
- `素材库_assets/`
- `dist/voice_trials/20260425_round28_voice_clone_trial/`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`

## 已更新指针

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/latest.md`
- 各类 archive manifests / move log / rollback guide

## 报告路径

- `治理报告`：`治理_reports/20260508_主工作区与外部归档删除区彻底分离_workspace_vs_external_archive_split/主工作区与外部归档删除区彻底分离报告_workspace_vs_external_archive_split_report.md`

## 下一个目标

先处理 `dist/voice_trials/20260425_round28_voice_clone_trial/` 的文档解耦，再把它从主工作区外移；之后统一把内部 archive manifests 改成“外部真实物理路径优先”。
