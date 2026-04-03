# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-04 已正式切回《视频工厂》A 线普通主线质量修正，并只围绕 `seg02` 完成一轮真实改动、真实 generation、真实 assembly 与回审。
- 当前质量结论：
  - `quality_passed`
- 当前默认主读取分支仍是：
  - `codex/user-readable-map`

## 本轮主路线

- 继续走普通图片 / 视频主线，不切真人开口。
- 选择原因：
  - 当前 `seg02_video.mp4` 已具备正确方向的主动作雏形。
  - 真正的问题不在技术链，而在 `seg02` 被拆成“说明卡 + 说明层”后削弱了证明力。
  - 本轮最短路径是让 `seg02` 变成一个单一视频主镜头，由画面自己完成“散乱 -> 可交接 SOP 接手链路”的证明。

## 本轮实际改动

- 修改：
  - [cases/formal_api_demo.md](/Users/fan/Documents/视频工厂/cases/formal_api_demo.md)
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [tests/test_formal_api_demo_pipeline.py](/Users/fan/Documents/视频工厂/tests/test_formal_api_demo_pipeline.py)
  - [video_builder.swift](/Users/fan/Documents/视频工厂/video_builder.swift)
- 新增 / 更新日志：
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
  - [codex_log/20260404_formal_api_demo_seg02_quality_pass.md](/Users/fan/Documents/视频工厂/codex_log/20260404_formal_api_demo_seg02_quality_pass.md)

## 当前真实产物

- 正式本地成片：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- 当前 `seg02` 主承载素材：
  - [dist/formal_api_demo/visual/seg02_video.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_video.mp4)
- 回审帧：
  - [dist/formal_api_demo/review_frames/final_02_seg02_mid.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_02_seg02_mid.png)
  - [dist/formal_api_demo/review_frames/final_03_seg02_late.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_03_seg02_late.png)

## 质量线判定

- 1. `seg02` 变化真正被看见：
  - `passed`
- 2. 中段文案不再像说明书：
  - `passed`
- 3. demo / PPT 感明显下降：
  - `passed`
- 4. Hook 仍成立：
  - `passed`
- 5. 结尾落点仍成立：
  - `passed`

## `.gitignore` 边界

- `dist/formal_api_demo/` 当前仍被 `.gitignore` 忽略。
- 这意味着：
  - 本地生成的 `final.mp4`、`seg02_video.mp4`、回审帧不会上传到 GitHub
  - 这些二进制产物属于 `local_only`
  - 它不阻断本轮代码 / 规则 / 日志同步回主读取分支
  - 但只看 GitHub 的新会话无法直接复审这些本地二进制文件

## 当前最关键下一步

- 下一轮若继续提质，优先从：
  - Hook 与结尾的卡片覆盖层继续轻量化
  入手，而不是再回头修技术链。

## 新会话建议先读

- `AGENTS.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
- [codex_log/20260404_formal_api_demo_seg02_quality_pass.md](/Users/fan/Documents/视频工厂/codex_log/20260404_formal_api_demo_seg02_quality_pass.md)
