# 回滚说明 rollback_guide

## 1. 单文件回滚

以下移动都可直接用 `git mv` 回滚：

- `project_source/07_current_formal_facts.md`
- `codex_source/00_current_repo_audit.md`
- `codex_source/02_codex_index.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/` 下的全部旧 `v3` / 旧 `v31` 副本
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/`

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
