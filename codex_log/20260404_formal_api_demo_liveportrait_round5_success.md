# 2026-04-04 formal_api_demo 真人开口 round5：技术主链真实跑通

## 本轮目标

- 不再停留在 detect 阻塞
- 找清 `seg02` 原输入图来源
- 做最小输入修正
- 跑通 `liveportrait-detect -> liveportrait -> poll -> download`

## 命中的 skill

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills`：
  - 已实际纳入：
    - `using-superpowers`
    - `systematic-debugging`
    - `verification-before-completion`
    - `using-git-worktrees`

## 当前运行基线

- worktree：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 本轮开始时 HEAD：
  - `bc1b1362403bd48b56024308984185a25e280307`

## `seg02` 原输入图来源

- 原输入图真实路径：
  - `dist/formal_api_demo_liveportrait_minrun_retry_tts/visual/seg02_image.png`
- 来源层级：
  - image_generation 产物
- 证据链：
  - `dist/formal_api_demo_liveportrait_minrun_retry_tts/manifest.json`
  - `dist/formal_api_demo_liveportrait_minrun_retry_tts/visual_generation_plan.json`
- 原 prompt：
  - `展示从散乱便签收束成结构化流程卡片。保持 9:16 竖版，PPT 卡片式信息层级，中文 AI 项目讲解场景，避免写实人物和广告感。`
- 根因判断：
  - 该 prompt 会把 seg02 底图继续导向流程卡片 / 非写实人物
  - 因而不适合作为 `liveportrait-detect` 输入

## 本轮如何修改 `seg02` 输入图

- 修改位置：
  - `formal_api_demo_core.py`
- 修改方式：
  - 仅在 portrait 路由开启且当前段 `needs_video = true` 时，覆盖该段底图 prompt
- 新 prompt：
  - `单人真人正脸半身肖像，正对镜头，五官清晰完整，无遮挡，面部占画面主要区域，光线自然，背景简洁干净，真实摄影风格，9:16 竖版。`
- 这次修正的性质：
  - 为跑通真人开口技术链路而做的最小通过素材修正
  - 不是最终审美定稿

## 实际运行命令

- 相关测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_branch_downloads_local_video_when_detect_passes tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_detect_rejects_image tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_detect_times_out tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_marks_failed_when_remote_task_fails tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_task_poll_times_out tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_marks_failed_when_local_video_file_is_missing`
- 真实运行：
  - `python3 scripts/generate_formal_api_demo.py --local-config config/formal_api_demo.local.toml --out dist/formal_api_demo_liveportrait_minrun_retry_face`

## 真实结果

- `detect`：
  - `success`
  - `request_id = 8f6905f7-0bd0-98e3-8c6f-dd7e41aa0c21`
- `liveportrait`：
  - `success`
  - `task_id = ee48c19b-80a0-41c1-88b5-80d4c6744e29`
  - `request_id = b5ba667b-86c1-95b8-a58d-cb0827a3f744`
- 轮询：
  - 成功
- 下载本地结果：
  - 成功

## 本地结果文件

- 真人开口视频已落地：
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/visual/seg02_video.mp4`
- 文件大小：
  - `1268966` bytes
- 同轮已落地的关键文件：
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/manifest.json`
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/result_summary.json`
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/visual/seg02_image.png`
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/visual/seg02_video.mp4`

## 当前状态改标

- 真人开口分支：
  - `success`
- overall：
  - `success`
- 说明：
  - 这里指当前技术主链已全部跑通
  - A 线质量优化仍是后续独立工作，不计入本轮技术链状态

## 本轮修改文件

- `formal_api_demo_core.py`
- `codex_log/latest.md`
- `codex_log/20260404_formal_api_demo_liveportrait_round5_success.md`

## 下一轮唯一最关键一步

1. 切回 A 线普通主线质量修正
2. 不再把真人开口链路视为当前最高优先级技术 blocker
