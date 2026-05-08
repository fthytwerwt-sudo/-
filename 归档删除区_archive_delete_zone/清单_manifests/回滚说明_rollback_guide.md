# 回滚说明 rollback_guide

## 1. 单文件回滚

以下移动都可直接用 `git mv` 回滚：

- `project_source/07_current_formal_facts.md`
- `codex_source/00_current_repo_audit.md`
- `codex_source/02_codex_index.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/` 下的全部旧 `v3` / 旧 `v31` 副本
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/`
- `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_guardrail_probe_20260408/`
- `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_probe/`
- `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_realcheck/`

示例：

```bash
git mv '归档删除区_archive_delete_zone/旧口径隔离_stale_context_quarantine/project_source/07_current_formal_facts.md' 'project_source/07_current_formal_facts.md'
git mv '归档删除区_archive_delete_zone/旧入口隔离_legacy_entrypoint_quarantine/codex_source/02_codex_index.md' 'codex_source/02_codex_index.md'
```

## 2. 批量旧副本回滚

```bash
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_contact_sheet.jpg' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_contact_sheet.jpg'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_cut_map.md' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_cut_map.md'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_full.mp4' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_full.mp4'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_review_manifest.md' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_review_manifest.md'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_run_summary.json' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_run_summary.json'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_summary.json' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_summary.json'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v3_timeline.json' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_timeline.json'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v31_review_manifest.md' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/AI做PPT踩坑_成品候选_v31_summary.json' 'dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_summary.json'
git mv '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation' '验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation'
```

## 2A. 本地未跟踪旧媒体回滚

```bash
mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_guardrail_probe_20260408' 'dist/_guardrail_probe_20260408'
mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_probe' 'dist/_provider_rotation_probe'
mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_realcheck' 'dist/_provider_rotation_realcheck'
```

## 2B. 外部 archive-only 目录回滚

```bash
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/tracked_git_media/归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots' '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/tracked_git_media/归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports' '归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/local_untracked_media/归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist' '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist'
mv '/Users/fan/Documents/视频工厂归档+删除/待用户确认_user_confirmation_required/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract' 'dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/tracked_git_media/dist/voice_trials/20260425_round28_10s_voice_trial' 'dist/voice_trials/20260425_round28_10s_voice_trial'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/tracked_git_media/dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial' 'dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial'
mv '/Users/fan/Documents/视频工厂归档+删除/待用户确认_user_confirmation_required/dist/完整成片_full_videos' 'dist/完整成片_full_videos'
mv '/Users/fan/Documents/视频工厂归档+删除/待用户确认_user_confirmation_required/本地归档_local_archive' '本地归档_local_archive'
mv '/Users/fan/Documents/视频工厂归档+删除/待用户确认_user_confirmation_required/素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract' '素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/local_untracked_media/样片报告_sample_reports' '样片报告_sample_reports'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/prototypes' 'dist/prototypes'
mv '/Users/fan/Documents/视频工厂归档+删除/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/20260424_不放大完整可读_no_zoom_completeness' 'dist/20260424_不放大完整可读_no_zoom_completeness'
```

## 3. 整个 commit 回滚

若要整轮回滚，优先使用：

```bash
git revert <this_commit_sha>
```

不要手动删除已移动文件，也不要用文件管理器直接拖回，优先保持 `git mv` / `git revert` 可追踪。

## 4. 禁止手动删除

以下对象禁止用手动删除替代回滚：

- `素材录制/`
- `素材库_assets/`
- `GPT数据源/`
- `GPT 数据源/`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
