# 一步瘦身报告 one_pass_workspace_slimming_report

## 1. 本轮目标

- 将当前项目口径下不再直接服务执行的旧媒体、旧产物、旧归档、旧缓存，从主工作区 `/Users/fan/Documents/视频工厂` 外移到 archive-only 外部目录 `/Users/fan/Documents/视频工厂归档+删除`
- 对 `.git` 做本地安全瘦身
- 不删除任何业务文件，不做 history rewrite，不 force push

## 2. 瘦身前后体积

### 主工作区

- `before`：`32G`
- `after`：`1.1G`

### `.git`

- `before`：`21G`
- `after`：`927M`

### `素材录制/`

- `before`：`11G`
- `after`：`55M`

### `dist/`

- `before`：`86M`
- `after`：`85M`

### `复审包_review_packs/`

- `before`：`27M`
- `after`：`27M`

### 外部 archive-only 目录

- `after`：`28G`

## 3. 已外移大类

### 原始素材归档

- `素材录制/` 中除当前语音样本锚点外的其余历史录制

### 旧声音试配

- `dist/voice_trials/20260425_round28_10s_voice_trial/`
- `dist/voice_trials/20260425_round28_voice_clone_trial/`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`

### 旧参考包

- `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`

### 旧媒体产物 / 旧归档

- `dist/完整成片_full_videos/`
- `本地归档_local_archive/`
- `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
- `样片报告_sample_reports/`
- `dist/prototypes/`
- `dist/20260424_不放大完整可读_no_zoom_completeness/`
- `旧 probe / provider 输出`
- 内部 archive zone 中已隔离的旧 `latest_review_pack` 副本与旧验证报告 payload

### Git 临时包归档

- `.git/objects/pack/tmp_pack_*`
- `.git/objects` 中异常 `bad sha1 file ... 2` 垃圾 loose objects

## 4. 保留在主工作区的 P0 对象

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/current_local_artifact_paths.md`
- `外部归档删除区指针_external_archive_delete_pointer.md`
- `GPT数据源/`
- `GPT 数据源/`
- `review_loop/`
- `dist/latest_review_pack/` 当前正式入口 4 文件
- `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/`
- `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/`
- `素材库_assets/`
- `素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`

## 5. Git 瘦身结果

- `git fsck --full` 初次运行：发现 `.git/objects` 中存在 `bad sha1 file` 垃圾对象
- 已外移：
  - `tmp_pack_*` 到 `/Users/fan/Documents/视频工厂归档+删除/Git临时包归档_git_tmp_pack_archive/tmp_pack_objects/`
  - 异常 loose objects 到 `/Users/fan/Documents/视频工厂归档+删除/Git临时包归档_git_tmp_pack_archive/garbage_loose_objects/`
- 复查：
  - `git count-objects -vH`：`garbage = 0`、`size-garbage = 0 bytes`
  - `git fsck --full`：仅剩 `dangling blob/tree`，无 `bad sha1` 异常
- 执行：
  - `git gc --prune=now`
- 结果：
  - `packs: 1`
  - `size-pack: 925.86 MiB`

## 6. skipped / 保留原因

- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
  - 当前 voice candidate reference
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`
  - 当前 pacing reference
- `dist/latest_review_pack/` 当前正式入口
- `素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
  - 当前用户语音样本锚点

## 7. 风险说明

- `已确认` 本轮没有 history rewrite，没有 force push。
- `部分成立` `dist/voice_trials/` 仍留 2 组 current reference；若后续 current 口径变化，仍需再拆分。
- `部分成立` 内部 `归档删除区_archive_delete_zone/` 目前保留为 lightweight pointer/manifests layer，不再承载大体积 payload，但仍可在后续继续精简。
