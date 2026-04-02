# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-03 已完成“本地 preview 画面层优化 round1”的真实重跑核验：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 本轮接手时，当前分支工作区里已经存在未提交的 visual round1 代码改动：
  - `formal_api_demo_core.py`
  - `video_builder.swift`
  - `tests/test_formal_api_demo_pipeline.py`
- 本轮按仓库事实重新核验后的真实结果：
  - 本地 preview 已重新生成，时长仍为 `15.0s`
  - 整段配音仍约 `14.064s`
  - preview manifest 已稳定为 `hook / process / outcome` 三种画面角色
  - 画面里已去掉显式 `PPT Demo / formal_api_demo / 本地预览` 标签
  - 第 1 段 hook 已是“主句 + 冲突对比卡”的首屏表达
  - 第 2 / 第 3 段已具备更清楚的层级卡片与底部轻量进度动效
- 当前 pipeline 仍未整体 success：
  - generation 继续因缺 `image_generation.model` / `video_generation.model` 记 `blocked`
  - 但这不是本轮画面层 round1 的剩余问题

## 最近一次真正完成了什么

- 本轮只围绕一个目标收口：
  - 让 `formal_api_demo` 当前本地 preview 的画面层比上一轮更不像 demo，更像可审的短视频 preview
- 本轮没有再扩画面代码范围，而是沿用当前工作区已有的 visual round1 改动，完成：
  - 真实重跑 generation
  - 真实重跑 assembly
  - 全量单测回归
  - preview 抽帧复审
- 当前可确认的关键产物：
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/assembly/preview_manifest.json`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  - `dist/formal_api_demo/result_summary.json`

## 质量审核结论

- 本轮只审“画面层”。
- 当前主结论：
  - 画面层比上一轮明显更不像 demo
  - 第 1 段 hook 画面更有效
  - 页面层级和切换感更像短视频 preview，而不是本地演示页
  - 但当前 preview 仍主要是纯信息卡构图，真正的“散乱 -> SOP”变化还不够强

## 当前最关键下一步

- 不回头改时长，不继续扩视觉模型或 cloud assembly。
- 下一轮如果只改一个点，优先切到：
  - `seg02` 的“散乱 -> 收束”变化表达，让页面不只是在静态步骤卡里说明流程，而是真正看见流程被收束

## 新会话建议先读

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_visual_layer_round1.md`
- `formal_api_demo_core.py`
- `video_builder.swift`
- `tests/test_formal_api_demo_pipeline.py`
