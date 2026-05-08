# 20260509｜一步瘦身

## 本轮定位

- `已确认` 本轮执行的是《视频工厂》主工作区“一步到位瘦身”。
- `已确认` 目标是把不再直接服务当前执行的旧媒体、旧产物、旧归档、旧缓存外移到 archive-only 外部目录。
- `已确认` 不删除业务文件，不做 history rewrite，不 force push。

## 关键结果

- 主工作区从 `32G` 降到 `1.1G`
- `.git` 从 `21G` 降到 `927M`
- `素材录制/` 从 `11G` 降到 `55M`
- 外部归档删除区增至 `28G`

## 本轮已外移

- 非 current `素材录制/` 历史录制
- 历史 `voice_trials`
- 历史 `reference_packs`
- 历史完整成片 / 本地归档 / 旧样片报告 / 旧素材检查报告
- 内部 archive zone 的旧媒体 payload
- `.git` 的 `tmp_pack_*` 与异常 garbage objects

## 本轮保留

- 当前 `latest_review_pack` 正式入口
- 当前 `v3.1` 基线包
- 当前 reference 包
- 当前 `voice candidate` 与 `pacing reference`
- 当前语音样本锚点
- 当前规则层、日志层、复盘层、动态事实层

## 指针

- `外部 archive-only 目录`：`/Users/fan/Documents/视频工厂归档+删除`
- `仓库指针文件`：`外部归档删除区指针_external_archive_delete_pointer.md`
- `原始素材外移清单`：`codex_log/素材录制_外移清单_raw_recordings_externalized_manifest.md`

## 下一个目标

继续清理内部 lightweight archive manifests，并单独处理 `dist/voice_trials` 剩余 2 组 current reference 与后续降权时机。
