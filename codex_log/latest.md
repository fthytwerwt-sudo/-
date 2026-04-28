# Latest

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
