# Latest

## 当前主读取分支

- 当前默认主读取分支：
  - `codex/user-readable-map`
- 2026-04-03 本轮任务分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 2026-04-03 round2 核查新增事实：
  - 当前 round1 内容并不只停在任务分支
  - 本轮开始前：
    - `codex/formal-api-demo-quality-liveportrait-round1` 的 HEAD 是 `1b11c7a`
    - `codex/user-readable-map` 的 HEAD 是 `ca7cc07`
    - 两个分支 tree SHA 相同，说明 round1 内容已按内容层面回流到主读取分支
  - 本轮日志回写后：
    - 任务分支与主读取分支都已 push
    - 当前 round2 blocked 日志已同步回 `codex/user-readable-map`
- 2026-04-03 round3 前置闸门复核新增事实：
  - 当前执行位置仍是目标任务 worktree
  - 当前分支 `codex/formal-api-demo-quality-liveportrait-round1`
  - 本轮开始时 HEAD 是 `4cd0f43`
  - 工作区干净
  - `config/formal_api_demo.local.toml` 仍不存在
  - 因此前置闸门直接失败，本轮没有进入任何真人开口线上调用
  - 当前 round3 blocked 日志已同步回 `codex/user-readable-map`
- 2026-04-03 round4 真人开口最小真实闭环新增事实：
  - 当前 worktree 已使用本地正式配置做真实运行
  - 第 1 次最小实调里：
    - `liveportrait-detect` 真实执行
    - `liveportrait` 未开始创建任务
    - 当前 worktree 的 TTS 配置先返回 `AccessDenied: model Access denied.`
    - 同时 `liveportrait-detect` 对当前 `seg02` 输入图返回 `No human face detected.`
  - 修正当前 worktree 的 TTS 取值后再跑第 2 次最小实调：
    - `tts_probe = success`
    - `voiceover = success`
    - `liveportrait-detect` 仍真实返回 `No human face detected.`
    - `liveportrait` 仍未开始创建任务
  - 当前最具体真人开口 blocker 已推进为：
    - 不是“缺 local config”
    - 而是当前 `seg02` 输入图没有可检测真人脸，导致 detect reject
- 2026-04-04 round5 真人开口最小真实闭环新增事实：
  - 已定位 `seg02` 原输入图来源：
    - `dist/formal_api_demo_liveportrait_minrun_retry_tts/visual/seg02_image.png`
    - 来源于 image_generation 产物，而不是本地手工底图
    - 原 prompt 是：
      - `展示从散乱便签收束成结构化流程卡片。保持 9:16 竖版，PPT 卡片式信息层级，中文 AI 项目讲解场景，避免写实人物和广告感。`
  - 已在 `formal_api_demo_core.py` 中把 portrait 路由的视频段底图 prompt 改成真人正脸取向：
    - `单人真人正脸半身肖像，正对镜头，五官清晰完整，无遮挡，面部占画面主要区域，光线自然，背景简洁干净，真实摄影风格，9:16 竖版。`
  - 重新跑最小真实闭环后：
    - `liveportrait-detect = success`
    - `liveportrait = success`
    - `task_id = ee48c19b-80a0-41c1-88b5-80d4c6744e29`
    - 本地结果文件：
      - `dist/formal_api_demo_liveportrait_minrun_retry_face/visual/seg02_video.mp4`

## 当前 formal_api_demo 真实状态

- TTS API：
  - `success`
- 图片 API：
  - `success`
  - `wan2.6-image` 已有真实 provider implementation
- 通用视频 API：
  - `success`
  - `wan2.6-t2v` 已有真实 provider implementation
- 真人开口分支：
  - `success`
  - `liveportrait-detect` 已真实执行并通过
  - `liveportrait` 已真实创建任务并完成
  - 本地结果文件已落地：
    - `dist/formal_api_demo_liveportrait_minrun_retry_face/visual/seg02_video.mp4`
- local assembly：
  - `success`
- overall：
  - `success`
  - 当前技术主链已全部跑通
  - A 线普通主线质量修正仍是后续单独工作，不计入当前技术主链状态

## 本轮实际完成了什么

- 进入真实任务分支对应 worktree：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 确认正式入口：
  - `scripts/generate_formal_api_demo.py`
- 已真实运行三次最小真人开口闭环
- 第 3 次成功运行输出目录：
  - `dist/formal_api_demo_liveportrait_minrun_retry_face/`
  - `tts_probe = success`
  - `voiceover = success`
  - `liveportrait-detect = success`
  - `liveportrait = success`
- 本轮代码侧最小修正：
  - 仅在 portrait 路由开启且该段需要视频时，把底图 prompt 改成单人真人正脸肖像取向
- 本轮没有改动普通主线逻辑、A 线质量逻辑或 cloud assembly

## 当前剩余最高优先级 blocker

- 当前技术主链无剩余 blocker
- 若继续推进，下一步应切回 A 线普通主线质量修正

## 下一轮唯一最关键一步

- 切回 A 线普通主线质量修正
- 不再把真人开口链路当当前最高优先级技术 blocker
