# 主工作区与外部归档删除区彻底分离报告 workspace_vs_external_archive_split_report

## 1. 本轮目标

- 将已判定为归档 / 删除 / 旧产物 / 旧媒体 / 待用户确认的大目录，从主工作区 `/Users/fan/Documents/视频工厂` 外移到 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除`
- 让后续 Codex 默认只在 `/Users/fan/Documents/视频工厂` 工作
- 保留当前正式入口、当前基线包、当前 reference 包、原始素材和当前规则文件不动

## 2. 外部归档删除区

- `已确认` 已创建：`/Users/fan/Documents/视频工厂归档+删除`
- `已确认` 该目录只用于 archive/delete payload，不是执行工作区，不是 fresh clone，不是 worktree

## 3. 已外移对象

### tracked 历史媒体 / 旧产物

- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/dist_latest_review_pack_legacy_snapshots/`
- `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/`
- `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`
- `dist/voice_trials/20260425_round28_10s_voice_trial/`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`

### untracked 历史媒体 / 大目录

- `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/`
- `dist/完整成片_full_videos/`
- `本地归档_local_archive/`
- `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
- `样片报告_sample_reports/`
- `dist/prototypes/`
- `dist/20260424_不放大完整可读_no_zoom_completeness/`

## 4. 当前主工作区保留项

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/current_local_artifact_paths.md`
- `GPT数据源/`
- `GPT 数据源/`
- `review_loop/`
- `dist/latest_review_pack/` 当前正式入口 4 文件
- `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/`
- `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/`
- `素材录制/`
- `素材库_assets/`

## 5. 待用户确认但已外移

- `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`
- `dist/完整成片_full_videos/`
- `本地归档_local_archive/`
- `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`

## 6. 当前仍留在主工作区但待后续拆分

- `dist/voice_trials/20260425_round28_voice_clone_trial/`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`

其中：

- `20260426_语音样本2复刻...` 与 `20260427_十五秒...` 当前仍被 `codex_log/current_local_artifact_paths.md` 作为 active reference 使用
- `20260425_round28_voice_clone_trial` 当前仍被正式资料作为历史 trial 路径引用，需后续单独改写文档后再外移

## 7. 已更新清单 / 指针

- `归档删除区_archive_delete_zone/清单_manifests/归档删除区清单_archive_delete_manifest.md`
- `归档删除区_archive_delete_zone/清单_manifests/本轮移动记录_move_log_20260508.md`
- `归档删除区_archive_delete_zone/清单_manifests/回滚说明_rollback_guide.md`
- `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/manifests/旧图片视频迁移清单_old_media_move_manifest.md`
- `codex_log/current_local_artifact_paths.md`
- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`

## 8. 禁止项检查

- `已确认` 未删除任何文件
- `已确认` 未移动 `素材录制/`
- `已确认` 未移动 `素材库_assets/`
- `已确认` 未移动 `GPT数据源/`
- `已确认` 未移动 `GPT 数据源/`
- `已确认` 未移动 `dist/latest_review_pack/review_manifest.md`
- `已确认` 未移动 `dist/latest_review_pack/summary.json`
- `已确认` 未移动 `dist/latest_review_pack/visual_route_map.json`
- `已确认` 未移动 `dist/latest_review_pack/visual_route_validation_report.json`
- `已确认` 未修改 `content_validation`
- `已确认` 未修改 `send_ready`
- `已确认` 未修改 `codex_log/current_publish_target.md`
- `已确认` 未把外移的本地未跟踪大媒体纳入 Git

## 9. 下一个目标

清理并重写内部 archive 指针清单，让后续会话默认只认外部归档区的真实物理位置；然后单独处理 `dist/voice_trials/20260425_round28_voice_clone_trial/` 的文档解耦与外移。
