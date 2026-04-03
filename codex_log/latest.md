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
  - `blocked`
  - 当前已完成最小真实运行
  - `liveportrait-detect` 已真实执行，但对当前 `seg02` 图返回 `No human face detected.`
  - `liveportrait` 未开始创建任务，`task_id` 仍为空
  - 当前最具体 blocker 是输入图缺少可检测真人脸，不再是 local config 缺失
- local assembly：
  - `success`
- overall：
  - `blocked`
  - 技术主链当前唯一最高优先级 blocker 仍是真人开口输入图不满足 `liveportrait-detect`
  - A 线普通主线质量问题继续后置，不在本轮处理

## 本轮实际完成了什么

- 进入真实任务分支对应 worktree：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 确认正式入口：
  - `scripts/generate_formal_api_demo.py`
  - 已真实运行两次最小真人开口闭环
- 当前最有价值的一次真实结果是：
  - `dist/formal_api_demo_liveportrait_minrun_retry_tts/`
  - `tts_probe = success`
  - `voiceover = success`
  - `liveportrait-detect = blocked`
  - `liveportrait = not started`
- 本轮没有改动任何业务代码，只推进本地配置与真实运行验证

## 当前剩余最高优先级 blocker

- 当前 `seg02` 输入图没有可检测真人脸
- 因而 `liveportrait-detect` 真实返回 `No human face detected.`
- 在 detect 通过前，`liveportrait` 不会开始创建任务

## 下一轮唯一最关键一步

- 把 `seg02` 的输入素材改成有清晰真人正脸的人像底图
- 然后在当前已可用的 TTS 配置上重跑最小 `liveportrait-detect -> liveportrait`
