# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-04 已切回《视频工厂》A 线普通主线质量修正，并完成 2 轮真实 generation + assembly + 回审。
- 当前工作分支是 `codex/round1`，不是用户给出的默认读取分支 `codex/user-readable-map`。
- 当前工作区仍有用户侧未提交改动：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `.omx/`
- 本轮没有触碰以上用户侧改动。

## 本轮主路线

- 继续走普通图片 / 视频主线，不切真人开口。
- 选择原因：
  - 当前工作区已经具备 `wan2.6-image` / `wan2.6-t2v` 的真实 generation 能力。
  - 当前工作区没有可直接复用的 liveportrait 成品目录或成片。
  - 本轮质量缺口集中在 `seg02` 的“散乱 -> 结构化 SOP”视觉证明，不需要扩真人开口支线。

## 本轮实际改动

- 修改：
  - [cases/formal_api_demo.md](/Users/fan/Documents/视频工厂/cases/formal_api_demo.md)
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [tests/test_formal_api_demo_pipeline.py](/Users/fan/Documents/视频工厂/tests/test_formal_api_demo_pipeline.py)
  - [video_builder.swift](/Users/fan/Documents/视频工厂/video_builder.swift)
- 新增 / 更新日志：
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
  - [codex_log/20260404_formal_api_demo_mainline_quality_round2.md](/Users/fan/Documents/视频工厂/codex_log/20260404_formal_api_demo_mainline_quality_round2.md)

## 当前真实产物

- 正式本地成片：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- 预览组装：
  - [dist/formal_api_demo/assembly/formal_api_demo_preview.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/assembly/formal_api_demo_preview.mp4)
  - [dist/formal_api_demo/assembly/preview_manifest.json](/Users/fan/Documents/视频工厂/dist/formal_api_demo/assembly/preview_manifest.json)
- 本轮关键视觉素材：
  - [dist/formal_api_demo/visual/seg02_video.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_video.mp4)
  - [dist/formal_api_demo/review_frames/final_02_seg02_before.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_02_seg02_before.png)
  - [dist/formal_api_demo/review_frames/final_03_seg02_after.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_03_seg02_after.png)

## 当前结论

- 当前最终状态：`still_blocked`
- 最具体 blocker：
  - `seg02` 仍没有把“散乱现场 -> 可交接 SOP 接手链路”做成一眼看懂的结构化证据。
  - 当前观众更容易看到“便签重排 + 覆盖说明层”，而不是“字段齐了、顺序定了、这条链现在能接手”。

## 质量线判定

- 1. `seg02` 变化是否真正被看见：`failed`
- 2. 中段文案是否还像说明书：`failed`
- 3. demo / PPT 感是否明显下降：`partial_but_not_enough`
- 4. Hook 是否仍成立：`passed`
- 5. 结尾落点是否仍成立：`passed`

## 额外说明

- 用户要求先读的 `codex_log/20260403_formal_api_demo_quality_review_and_liveportrait_round1.md` 在当前分支不存在。
- 当前本地 assembly 已恢复为当前阶段真实交付：
  - `assembly_status = success`
  - `local_assembly_status = success`
  - `artifact_paths.final_video = dist/formal_api_demo/final.mp4`

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
- [codex_log/20260404_formal_api_demo_mainline_quality_round2.md](/Users/fan/Documents/视频工厂/codex_log/20260404_formal_api_demo_mainline_quality_round2.md)
- [cases/formal_api_demo.md](/Users/fan/Documents/视频工厂/cases/formal_api_demo.md)
- [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
- [video_builder.swift](/Users/fan/Documents/视频工厂/video_builder.swift)
