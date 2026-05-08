# 归档删除区说明 archive_delete_zone_readme

## 文件定位

- 本目录只用于隔离旧口径、旧入口、旧产物候选与治理清单。
- 本目录不是当前正式事实入口。
- 本目录不是当前执行规则入口。
- 本目录不是当前复审入口。

## 使用边界

- `旧口径隔离_stale_context_quarantine/`：只放已确认不应再作为当前事实入口的历史镜像文件。
- `旧入口隔离_legacy_entrypoint_quarantine/`：只放已确认不应再作为默认导航的旧入口文件。
- `旧产物候选_old_artifact_candidates/`：只放已确认不应继续留在默认入口目录的旧副本或旧 snapshot。
- `待归档_archive_candidates/`：只放下一轮待归档候选清单或说明，不做删除。
- `待删除_delete_candidates/`：只放下一轮待删除候选清单或说明，不做删除。
- `原始素材待确认_raw_assets_pending_confirmation/`：只放需要用户确认的原始素材清单，不移动原始素材本体。
- `清单_manifests/`：放本轮主要工作区清单、归档删除区清单、移动记录与回滚说明。

## 硬规则

- 不得把本目录当默认读取入口。
- 不得把本目录中的任何文件重新写成当前正式事实。
- 不得在本目录内直接执行删除动作。
- 如需回滚，优先按 `清单_manifests/回滚说明_rollback_guide.md` 执行。

## 2026-05-08 外部归档说明

- `已确认` `/Users/fan/Documents/视频工厂归档+删除` 是用户明确授权的 archive-only 外部目录。
- `已确认` 本仓库内保留本目录的主要作用是：清单、指针、回滚说明和最小 discoverability，而不是继续承载大体积 archive payload。
- `已确认` `/Users/fan/Documents/视频工厂` 仍是唯一正式执行工作区；`/Users/fan/Documents/视频工厂归档+删除` 只能读、不能默认执行。
