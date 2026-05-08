# 历史产物归档审计与迁移报告 old_artifacts_archive_audit_report

## 1. 本轮目标

- 扫描《视频工厂》工作区里的旧视频产物、旧复审包、旧 trial、旧 provider 测试输出、旧报告包。
- 判断哪些仍属于当前主线必须保留，哪些可作为历史产物候选。
- 对明确不再作为当前入口使用、且可通过 `git mv` 保留历史的旧产物执行迁移。
- 不删除任何文件，不移动任何原始素材，不触碰 `dist/latest_review_pack/` 当前正式入口文件。

## 2. route_decision 摘要

- `project_route = video_factory`
- `task_type = local_file_governance + mechanism_or_route_fix + review_diagnosis_audit + project_file_change`
- `large_task_gate.triggered = true`
- `lane_recommendation = audit_lane`
- `parallel_recommendation = serial_only`
- `execution_permission = granted_for_old_artifact_audit_and_safe_archive_moves`

## 3. 历史产物扫描摘要

| path | type | size | current_entry | reference_value | recommendation |
| --- | --- | ---: | --- | --- | --- |
| `dist/latest_review_pack/` | 当前正式复审入口 | `24M` | `yes` | `yes` | `keep` |
| `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/` | 当前 round 对应旧 round 包 | `53M` | `partial` | `yes` | `keep_this_round` |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/` | 当前 v3.1 基线本地复审包 | `12M` | `yes` | `yes` | `keep` |
| `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/` | 当前 cute card reference 包 | `1.8M` | `no` | `yes` | `keep` |
| `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/` | 当前 sassy card reference 包 | `14M` | `no` | `yes` | `keep` |
| `dist/reference_packs/` | 历史 reference packs | `4.6M` | `no` | `partial` | `user_confirmation_required` |
| `dist/voice_trials/` | 历史 + 当前混合 voice trials | `14M` | `no` | `yes` | `user_confirmation_required` |
| `dist/完整成片_full_videos/` | 大体积历史完整成片 | `1.2G` | `no` | `partial` | `user_confirmation_required` |
| `本地归档_local_archive/` | 历史外部工作区回收区，含嵌套 `.git` | `975M` | `no` | `partial` | `user_confirmation_required` |
| `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/` | 历史技术验证报告包 | `12K` | `no` | `low` | `archive_candidate_moved` |
| `dist/_guardrail_probe_20260408/` | 本地旧 probe 输出 | `92K` | `no` | `low` | `archive_candidate_local_only_not_moved` |
| `dist/_provider_rotation_probe/` | 本地旧 provider probe 输出 | `52K` | `no` | `low` | `archive_candidate_local_only_not_moved` |
| `dist/_provider_rotation_realcheck/` | 本地旧 provider realcheck 输出 | `80K` | `no` | `low` | `archive_candidate_local_only_not_moved` |
| `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/` | 历史素材检查报告包 | `11M` | `no` | `partial` | `user_confirmation_required` |
| `样片报告_sample_reports/` | 空目录 | `0B` | `no` | `no` | `delete_candidate_after_confirm` |
| `dist/prototypes/` | 空目录 | `0B` | `no` | `no` | `delete_candidate_after_confirm` |
| `dist/20260424_不放大完整可读_no_zoom_completeness/` | 空目录 / stale path | `0B` | `no` | `no` | `delete_candidate_after_confirm` |
| `素材录制/` | 原始素材 | `11G` | `no` | `yes` | `do_not_move` |
| `素材库_assets/` | 当前固定素材锚点区 | `8.9M` | `yes` | `yes` | `do_not_move` |

## 4. 当前必须保留

- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
- `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/`
- `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/`
- `素材录制/`
- `素材库_assets/`

## 5. 已移动归档候选

- `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/`
  - 新路径：`归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/`
  - 原因：历史技术验证报告包，不再属于当前默认工作区入口

## 6. 未移动但已标记

### 待用户确认

- `dist/reference_packs/`
- `dist/voice_trials/`
- `dist/完整成片_full_videos/`
- `本地归档_local_archive/`
- `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`

### 归档候选但本轮不迁移

- `dist/_guardrail_probe_20260408/`
- `dist/_provider_rotation_probe/`
- `dist/_provider_rotation_realcheck/`

原因：这些目录是本地未跟踪历史输出；本轮不强行迁入 Git 归档轨迹。

### 确认后可删候选

- `样片报告_sample_reports/`
- `dist/prototypes/`
- `dist/20260424_不放大完整可读_no_zoom_completeness/`
- `dist/.DS_Store`

## 7. 已更新清单

- `归档删除区_archive_delete_zone/清单_manifests/归档删除区清单_archive_delete_manifest.md`
- `归档删除区_archive_delete_zone/清单_manifests/本轮移动记录_move_log_20260508.md`
- `归档删除区_archive_delete_zone/清单_manifests/回滚说明_rollback_guide.md`

## 8. 禁止项检查

- `已确认` 未删除任何文件
- `已确认` 未移动 `素材录制/`
- `已确认` 未移动 `素材库_assets/`
- `已确认` 未移动 `GPT数据源/`
- `已确认` 未修改 `GPT 数据源/`
- `已确认` 未移动 `dist/latest_review_pack/review_manifest.md`
- `已确认` 未移动 `dist/latest_review_pack/summary.json`
- `已确认` 未移动 `dist/latest_review_pack/visual_route_map.json`
- `已确认` 未移动 `dist/latest_review_pack/visual_route_validation_report.json`
- `已确认` 未修改 `content_validation`
- `已确认` 未修改 `send_ready`
- `已确认` 未修改 `codex_log/current_publish_target.md`
- `已确认` 未新建外部工作区

## 9. 下一轮建议

1. 单独处理本地未跟踪旧 probe / provider 输出是否需要保留或直接删除。
2. 单独拆分 `voice_trials/`：保留 current reference，归档纯历史试听目录。
3. 单独拆分 `reference_packs/`：保留仍有 reference 价值的包，其余再归档。
4. 用户明确确认前，继续不动 `素材录制/`、`素材库_assets/`、`dist/完整成片_full_videos/`、`本地归档_local_archive/`。
