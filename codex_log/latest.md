# Latest

## 20260424｜不放大完整可读布局修复

- `已确认` 本轮已在 `fix/no-zoom-completeness-layout` 分支完成 `no_zoom_completeness` 最小代码修复。
- `已确认` 当前真实改动范围：
  - `generate_demo.py`
  - `video_builder.swift`
  - `tests/test_generate_demo.py`
  - `.gitignore`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - `codex_log/20260424_不放大完整可读_no_zoom_completeness_layout.md`
- `已确认` 机制层新增：
  - 渲染前先计算 1x 默认视图正文高度。
  - 当正文超过 `safe_area` 可用高度时，先拆成多拍，再进入渲染。
  - `zoom_used_for_completeness = false`，放大不参与完整性判定。
  - 每拍输出 `layout_metrics`，记录 `canvas_size / safe_area / title_bbox / body_bbox / footer_bbox / text_total_height / safe_area_available_height / overflow / split_required / split_count`。
- `已确认` 最小验证样例已自动拆成 2 拍：
  - `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/02_1x默认视图_no_zoom.png`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json`
- `已确认` 验证结果：
  - `python3 -m unittest tests/test_generate_demo.py` 通过，3 个测试通过。
  - `python3 generate_demo.py --layout-fixture` 通过，生成 2 张 1x review 图。
  - `python3 generate_demo.py` 通过，默认 demo 链路仍可生成 `final.mp4`。
  - `git diff --check` 通过。
- `部分成立` 内容验证口径：
  - 本轮生成的最小验证样例在 1x 默认视图下未见标题、标签、正文、底部说明裁切。
  - 但用户截图对应的专用 `当前在看 / 正确做法 / 拆两拍` 真实生产代码未在当前 `main` 可追踪代码中找到；本轮修复落在当前仓库可确认的最小渲染入口。
- `待验证` 后续人工复审：
  - 请优先复看上述两张 1x 默认视图 review 图。
  - 若实际 vNext 截图链路另有未提交脚本，需把同一 `no_zoom_completeness` 规则接入该真实入口。

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，同步到 `origin/main`。
- GitHub baseline 分支为 `main`，且 `main` 已跟踪 `origin/main`。
- 后续仓库型任务默认在新分支推进，而不是长期直接在 `main` 上执行。
- 顶层入口规则、GitHub 协作基线和执行日志机制都已在仓库内落位。

## 最近一次完成了什么

- 已固定新 Codex 会话默认最小接手集合：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`；若任务偏执行规则，再补读 `codex_source/01_execution_rules.md`。
- 已固定仓库型任务在形成可判断小闭环后，默认先更新 `codex_log/latest.md`、命中条件时补完整日志，再 commit 并 push 当前分支 / 当前 PR，供 ChatGPT 直接去 GitHub 复审。

## 当前最关键的下一步

- 后续仓库型任务继续在功能分支推进；每轮一旦形成可判断小闭环，就先更新 `codex_log/latest.md`，再按规则 commit、push 并交给 ChatGPT 复审。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- 若任务偏执行规则，再补读 `codex_source/01_execution_rules.md`
