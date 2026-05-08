# 旧图片视频迁移清单 old_media_move_manifest

| source_path | target_path | media_type | size | tracked_status | action | reason | rollback_command |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| `dist/_guardrail_probe_20260408/` | `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_guardrail_probe_20260408/` | `mixed_probe_output` | `92K` | `untracked` | `moved` | 本地旧 guardrail probe 输出，不属于当前主线入口 | `mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_guardrail_probe_20260408' 'dist/_guardrail_probe_20260408'` |
| `dist/_provider_rotation_probe/` | `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_probe/` | `mixed_provider_probe_output` | `52K` | `untracked` | `moved` | 本地旧 provider probe 输出，不属于当前主线入口 | `mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_probe' 'dist/_provider_rotation_probe'` |
| `dist/_provider_rotation_realcheck/` | `归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_realcheck/` | `mixed_provider_probe_output` | `80K` | `untracked` | `moved` | 本地旧 provider realcheck 输出，不属于当前主线入口 | `mv '归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/_provider_rotation_realcheck' 'dist/_provider_rotation_realcheck'` |
| `dist/latest_review_pack/review_manifest.md` | `kept_in_place` | `current_review_entry` | `n/a` | `tracked` | `kept` | 当前正式复审入口，禁止移动 | `n/a` |
| `dist/latest_review_pack/summary.json` | `kept_in_place` | `current_review_entry` | `n/a` | `tracked` | `kept` | 当前正式复审入口，禁止移动 | `n/a` |
| `dist/latest_review_pack/visual_route_map.json` | `kept_in_place` | `current_review_entry` | `n/a` | `tracked` | `kept` | 当前正式复审入口，禁止移动 | `n/a` |
| `dist/latest_review_pack/visual_route_validation_report.json` | `kept_in_place` | `current_review_entry` | `n/a` | `tracked` | `kept` | 当前正式复审入口，禁止移动 | `n/a` |
| `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/` | `kept_in_place` | `current_baseline_media_package` | `53M` | `tracked_and_local` | `kept` | 当前 v3.1 基线包，仍属当前主线 | `n/a` |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/` | `kept_in_place` | `current_baseline_review_pack` | `12M` | `tracked` | `kept` | 当前 v3.1 基线本地复审包 | `n/a` |
| `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/` | `kept_in_place` | `reference_media_package` | `1.8M` | `tracked` | `kept` | 当前 still has reference value | `n/a` |
| `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/` | `kept_in_place` | `reference_media_package` | `14M` | `tracked` | `kept` | 当前 still has reference value | `n/a` |
| `dist/reference_packs/` | `kept_in_place` | `reference_media_package` | `4.6M` | `mixed` | `user_confirmation_required` | 可能仍有 reference 价值，需先拆 current / history | `n/a` |
| `dist/voice_trials/` | `kept_in_place` | `audio_trials` | `14M` | `mixed` | `user_confirmation_required` | 当前 reference 与纯历史试听混在一起 | `n/a` |
| `dist/完整成片_full_videos/` | `kept_in_place` | `full_video_candidates` | `1.2G` | `mixed` | `user_confirmation_required` | 大体积历史完整成片，需用户确认 | `n/a` |
| `素材录制/` | `kept_in_place` | `raw_assets` | `11G` | `local` | `kept` | 原始素材，禁止移动 | `n/a` |
| `素材库_assets/` | `kept_in_place` | `current_anchor_assets` | `8.9M` | `tracked_and_local` | `kept` | 当前固定素材锚点，禁止移动 | `n/a` |
