# Latest

## 20260502｜单工作区统一治理

- `已确认` 本轮在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内创建分支 `codex/single-workspace-unification-20260502`，未新建外部 worktree。
- `已确认` 已完成 `/Users/fan/Documents/视频工厂*` 与 `/private/tmp/视频工厂_*` 历史散工作区审计；`/Users/fan/Desktop`、`/Users/fan/Downloads` 未发现匹配目录。
- `已确认` 审计报告已落入 `/Users/fan/Documents/视频工厂/治理_reports/20260502_单工作区审计_single_workspace_audit/单工作区审计报告_single_workspace_audit_report.md`。
- `已确认` 唯一文件安全复制回收目录为 `/Users/fan/Documents/视频工厂/归档_archive/外部工作区回收_external_workspace_recovery_20260502/`；本轮复制并校验 113 个文件，失败项 0。
- `已确认` 本轮未移动源文件，未永久删除任何文件，未运行 `rm -rf`；只生成待删候选清单 `/Users/fan/Documents/视频工厂/归档_archive/外部工作区回收_external_workspace_recovery_20260502/待删候选_delete_candidates.md`。
- `已确认` 已在 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md` 写入 `single_workspace_rule（单工作区硬规则）`：后续只能以 `/Users/fan/Documents/视频工厂` 为唯一正式工作区；不得默认创建 `/Users/fan/Documents/视频工厂_*` 或外部 `git worktree`。
- `已确认` 已更新 `codex_log/current_local_artifact_paths.md`：首选 `canonical_local_path` 改为正式工作区内部路径；旧外部路径降级为 `historical_source_path` / `fallback_path`。
- `已确认` 本轮未生成视频 / 音频 / 图片，未写新文案，未修改 v3.1 正片内容，未修改 `content_validation`，未修改 `send_ready`。
- `下一个目标`：用户确认 `delete_candidate` / `migrate_then_delete_candidate` 后，进入第二轮安全删除候选目录与 `git worktree` 清理。

## 20260502｜HyperFrames 录屏动态标注叠层验证

- `已确认` 本轮只做 `shot07_deliverable_draft_keyword` 的 10.5 秒技术样片；未重新生成或修改 v3.1 正片，未修改 `dist/latest_review_pack`，未写新文案，未改变灰度测试状态。
- `已确认` 源录屏来自 `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4`，`source_start = 30.0`；本轮只截取竖屏预合成底片，不回写正片。
- `已确认` HyperFrames 环境可运行：`doctor` 显示 FFmpeg / FFprobe / Chrome / Docker 可用；同时提示本机内存偏低，因此本轮使用 `-w 1` 单 worker 渲染。
- `已确认` 透明叠层已输出：`/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_screencast_annotation_20260502/shot07_deliverable_draft_keyword_hyperframes_overlay_alpha.mov`
- `已确认` 预合成 MP4 已输出：`/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_screencast_annotation_20260502/shot07_deliverable_draft_keyword_screencast_plus_hyperframes_overlay_10_5s.mp4`
- `已确认` 技术核验：透明 MOV 为 `prores (4444) / yuva444p12le / 1080x1920 / 30fps / 10.500s`，MP4 为 `h264 / 1080x1920 / 30fps / 10.500s`；两者均通过 `video-metadata-probe` 和 `ffmpeg -v error ... -f null -`。
- `已确认` 路径已写入 `codex_log/current_local_artifact_paths.md`，`path_exists = true`；样片均在 `/Users/fan/Documents/视频工厂` 内部稳定目录。
- `部分成立` 接入判断：本地透明通道与预合成链路成立；云端剪辑是否直接吃 `ProRes 4444 alpha MOV` 仍需在下一轮云端导入实测。若不支持透明 MOV，可使用预合成 MP4 作为备选。
- `已确认` `content_validation` 未改，`send_ready` 未改；本轮技术验证不代表 v3.1 内容通过。

## 20260502｜HyperFrames 样片路径同步

- `已确认` 本轮只核验并同步 HyperFrames 结果差提示卡 10 秒样片路径；未重新生成 v3.1 成片、未修改 `dist/latest_review_pack`、未写新文案。
- `已确认` 用户可打开路径：`/Users/fan/Documents/视频工厂/HyperFrames测试_hyperframes_result_card_component_20260502/结果差提示卡_hyperframes_result_card_10s.mp4`
- `已确认` 路径已写入 `codex_log/current_local_artifact_paths.md`，`artifact_id = hyperframes_result_diff_card_10s_sample`，`path_exists = true`。
- `已确认` 技术核验：`test -f` 通过；`ffprobe` 显示 `1080x1920 / 10.000s / 30fps / h264 / 720968 bytes`；`ffmpeg -v error ... -f null -` 解码通过。
- `已确认` 样片已在 `/Users/fan/Documents/视频工厂` 内部稳定目录，无需复制；未使用 `/private/tmp`。
- `已确认` `content_validation` 未改，`send_ready` 未改；本轮路径同步不代表 v3.1 内容通过。
- `下一个目标`：ChatGPT / 用户可直接打开该 MP4 复看，判断 HyperFrames 是否作为云端剪辑插入素材层继续试接入。

## 20260429｜AI 做 PPT 踩坑技术预览 v1

- `已确认` 本轮只生成 `technical_preview（技术预览）`，不是合格样片、正式成片、内容验证通过或可发送状态。
- `已确认` 已生成本地复审包：
  - `/Users/fan/Documents/视频工厂/复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/`
- `已确认` 关键输出：
  - `AI做PPT踩坑_技术预览_v1_full.mp4`
  - `shot00_opening_hello_wave_preview.mp4`
  - `AI做PPT踩坑_技术预览_v1_contact_sheet.jpg`
  - `AI做PPT踩坑_技术预览_v1_review_manifest.md`
  - `AI做PPT踩坑_技术预览_v1_summary.json`
  - `AI做PPT踩坑_技术预览_v1_timeline.json`
  - `AI做PPT踩坑_技术预览_v1_cut_map.md`
  - `AI做PPT踩坑_技术预览_v1_run_summary.json`
- `已确认` 完整技术预览为 `1080x1920 / 25fps / 00:02:34.70`，可被 FFmpeg 解码打开，带静音音轨和烧录字幕。
- `已确认` `shot00_opening_hello_wave` 使用元素娃娃开场锚点素材，单段 `00:00:02.00`，字幕包含 `hello，大家好`。
- `已确认` 本轮包含反面录屏、正面录屏、三张骚萌卡、结果差卡、低压收束和可选尾卡。
- `temporary_no_voice_preview（临时无声音预览）`：本轮未使用稳定 TTS，未调用 voice cloning，视频仅保留静音音轨 + 字幕节奏版。
- `已确认` `content_validation = pending_user_chatgpt_review`，`send_ready = false`，`technical_validation = generated_for_preview`。
- `已确认` 本轮没有修改 `dist/latest_review_pack/`；前后 checksum 对比一致。
- `已确认` 本轮没有修改正式 `content_validation（内容验证）` 或 `send_ready（可发送状态）` 文件。
- `下一个目标`：ChatGPT / 用户基于技术预览复审内容、节奏、字幕与证据可读性，再决定是否进入声音试配和正式样片修正。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260429_AI做PPT踩坑技术预览v1.md`
- `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/AI做PPT踩坑_技术预览_v1_review_manifest.md`

## 20260429｜文案样本视频节奏提取

- `已确认` 本轮只做本地 `文案样本` 视频保真提取；未写新文案、未剪视频、未生成新 round。
- `已确认` 找到样本视频：
  - `/Users/fan/Documents/视频工厂/素材录制/文案样本.MP4`
- `已确认` 视频信息：
  - 时长 `00:03:40.94`
  - 分辨率 `1180x2556`
  - 视频 `HEVC`
  - 音频 `AAC`
- `已确认` 已生成报告目录：
  - `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
- `已确认` 关键输出：
  - `文案样本节奏报告_copy_sample_rhythm_report.md`
  - `文案样本转写_transcript.md`
  - `文案样本结构_segments.json`
  - `run_summary.json`
- `blocked_no_asr_available（阻塞：缺少可用转写工具）`：未找到本地 Whisper / faster-whisper / paraformer 等 ASR；macOS 系统语音识别被 TCC 隐私权限中断。
- `已确认` 本轮报告基于可见字幕和画面节奏，不冒充全量口播转写。
- `已确认` 本轮没有修改 `dist/latest_review_pack/`、`content_validation`、`send_ready`。
- `下一个目标`：ChatGPT 基于本轮样本节奏报告，写《AI 做 PPT 踩坑》的正式文案初稿，并继续保留“不是最终验收稿、不可直接发布”的边界。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/文案样本节奏报告_copy_sample_rhythm_report.md`

## 20260429｜素材保真检查与细节证据报告

- `已确认` 本轮只做用户录制素材保真检查；未剪视频、未生成新 round、未调用视频生成 API、未调用 TTS / voice cloning。
- `已确认` 本轮素材来源只读检查：
  - `/Users/fan/Documents/视频工厂/素材录制/正面/录制于 2026-04-16 23.03.53.mp4`
  - `/Users/fan/Documents/视频工厂/素材录制/反面/录制于 2026-04-16 22.41.32.mp4`
  - `/Users/fan/Documents/视频工厂/素材录制/正面-反面/` 不存在。
- `已确认` 已生成素材证据报告目录：
  - `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/`
- `已确认` 关键输出：
  - `素材保真检查报告_material_faithful_report.md`
  - `素材清单_material_inventory.md`
  - `素材联系表_material_contact_sheet.jpg`
  - `关键帧证据_keyframes_evidence.jpg`
  - `时间码截图_timecode_frames/`
  - `run_summary.json`
- `已确认` 本轮没有修改 `dist/latest_review_pack/`、`content_validation`、`send_ready`。
- `已确认` 本轮报告结论只作为 `ChatGPT（最终落稿与复审入口）` 的素材事实包，不是最终脚本，不代表内容已过线。
- `fact_conflict_detected（事实冲突已发现）` 当前工作树 `dist/latest_review_pack/summary.json` 指向 `round32`，而 `origin/codex/user-readable-map:GPT数据源/08_当前正式事实.md` 指向 `round34`；本轮只标记冲突，不覆盖状态。
- `待验证` 用户本轮“真实 AI 使用经验 + 工作提效实录”新口径是否已完全同步到主读取分支；本轮按用户 / ChatGPT 给定执行口径处理。
- `下一个目标`：ChatGPT 基于本轮素材事实包写最终脚本，并继续把可写事实、不能写 claims、补录缺口分开。

## 20260424｜PR #4 交接口径修正与状态清理

- `已确认` 当前 PR #4 分支是 `fix/no-zoom-completeness-layout`，base 是 `main`，PR 仍保持 draft，不合并。
- `已确认` PR #4 的正确交接口径不是“round27 项目产物缺失”，而是三层并列：
  - `no_zoom_completeness` 不放大完整可读最小链路技术修复；
  - `round27_首拍完整信息块修复` 的分支接手口径纠偏；
  - `content_validation` 仍待基于正确视频工作分支继续复审。
- `已确认` `no_zoom_completeness` 最小链路技术修复已在本 PR 分支落地：
  - `generate_demo.py` 渲染前高度估算、safe_area 容量检查、自动拆拍、layout_metrics 输出；
  - `video_builder.swift` 按真实文字高度绘制，并支持 1x 默认视图 PNG；
  - `tests/test_generate_demo.py` 覆盖 no_zoom validation fixture；
  - `dist/20260424_不放大完整可读_no_zoom_completeness/` 保留 1x review 图与 layout_metrics。
- `已确认` `no_zoom_completeness` 最小验证证据：
  - `python3 -m unittest tests/test_generate_demo.py`
  - `python3 generate_demo.py --layout-fixture`
  - `python3 generate_demo.py`
  - `git diff --check`
  - `layout_metrics: split_count = 2 / any_overflow = false`
- `已确认` `round27_首拍完整信息块修复` 的 4 个关键复审产物存在于正确视频工作分支：
  - `codex/doubao-vnext-direct-fix-20260417`
  - `fix/no-zoom-completeness-layout` 未携带这些二进制产物，只能说明 PR 分支缺产物，不能写成 `round27` 项目事实缺失。
- `已确认` 当前 vNext 活动线已在正确视频工作分支推进到：
  - `round29_中段图片页风格与正反差修复`
  - `origin/codex/doubao-vnext-direct-fix-20260417` 当前对象：`8bb7ef37afe73077c3493a25e6b1885ca7192036`
  - `send_ready = no`
- `待验证` PR #4 不包含 round27 / round28 / round29 内容最终验收，不声明可直接发送。
- `待验证` `content_validation` 只能写为：待基于正确分支继续复审；不得把 no_zoom 最小技术验证成功写成 vNext 全链路内容过线。

## 20260424｜round27 产物接手审计纠偏

- `已确认` 本轮只做 GitHub 分支产物找回与接手审计口径纠偏；没有重新生成视频，没有修改任何 `round27` 视频内容。
- `已确认` 当前工作分支仍是 `fix/no-zoom-completeness-layout`，并跟踪 `origin/fix/no-zoom-completeness-layout`。
- `已确认` 正确复审分支是 `codex/doubao-vnext-direct-fix-20260417`。
- `已确认` 上一轮 `round27 artifact handoff audit` 的不准确点是：把 `fix/no-zoom-completeness-layout` 分支没有携带 round27 可见产物，误写成了 `round27` 产物缺失。
- `已确认` 正确口径必须改为：
  - `round27_首拍完整信息块修复` 的 4 个关键复审产物在 `codex/doubao-vnext-direct-fix-20260417` 分支真实存在。
  - `fix/no-zoom-completeness-layout` 分支同路径未携带这些二进制复审产物。
  - 当前问题是分支 / 接手审计口径错误，不是视频内容失败，也不是 `round27` 项目事实缺失。

## round27 产物确认

- `已确认` 已在本地分支对象与远端分支对象中确认以下 4 个路径存在于 `codex/doubao-vnext-direct-fix-20260417`：
  - `dist/20260417_豆包的正确打开方式_vnext/round27_首拍完整信息块修复/renders/主持壳正式正片_round27_首拍完整信息块修复.mp4`
  - `dist/20260417_豆包的正确打开方式_vnext/round27_首拍完整信息块修复/renders/中段preview_round27_首拍完整信息块修复.mp4`
  - `dist/20260417_豆包的正确打开方式_vnext/round27_首拍完整信息块修复/audit/中段_before_after_round26_vs_round27.mp4`
  - `dist/20260417_豆包的正确打开方式_vnext/round27_首拍完整信息块修复/audit/中段旧新联系表_round27.jpg`
- `已确认` 同样的 4 个路径在 `origin/fix/no-zoom-completeness-layout` 中没有 tree entry；这只能说明审计 PR 分支未携带产物。
- `已确认` `codex/doubao-vnext-direct-fix-20260417` 当前对象为 `b4a34fa5ec33a8296c43c07f9fa6be7c11b55fca`。
- `已确认` `origin/fix/no-zoom-completeness-layout` 当前对象为 `1adfec25367dc210babdc099c36bfadfbc09db43`。

## 后续接手规则

- `已确认` GPT / Codex 若要复审 `round27_首拍完整信息块修复`，必须从 `codex/doubao-vnext-direct-fix-20260417` 分支读取产物。
- `已确认` 不得再把 `fix/no-zoom-completeness-layout` 分支的产物缺口写成 `round27` 项目事实缺失。
- `待验证` 本轮只确认产物存在与审计口径纠偏，不声明 `content_validation` 已过线。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260424_round27_artifact_handoff_audit.md`
- `codex_log/20260424_round27_artifact_handoff_audit_correction.md`
