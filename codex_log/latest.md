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
    - 任务分支最新提交是 `a8f07e1`
    - 主读取分支最新提交是 `bfba58f`
    - 当前 round2 blocked 日志已同步回 `codex/user-readable-map`

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
  - `liveportrait-detect -> liveportrait` 的代码 / 契约 / 测试层 round1 已补到位
  - 但当前 round2 worktree 真实缺少 `config/formal_api_demo.local.toml`
  - 因此本轮没有执行任何真实 `liveportrait-detect -> liveportrait` 线上实调
  - 当前最具体 blocker 已收口为“整个本地正式配置文件缺失”，不是“provider implementation 未实现”
- local assembly：
  - `success`
- overall：
  - `blocked`
  - 技术主链当前唯一最高优先级 blocker 仍是真人开口分支缺真实线上验证
  - A 线普通主线质量问题继续后置，不在本轮处理

## 本轮实际完成了什么

- 进入真实任务分支对应 worktree：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 确认 `config/formal_api_demo.local.toml`：
  - 当前不存在
- 确认正式入口：
  - `scripts/generate_formal_api_demo.py`
  - 当前只是核对入口与参数，没有执行真人开口线上实调
- 确认当前不能在“不伪造 local config”的前提下改写 B 线专属 `manifest / result_summary`：
  - `config/formal_api_demo.example.toml` 中 `portrait_detect.enabled = false`
  - `portrait_video_generation.enabled = false`
  - 若缺 local config 直接强跑正式入口，只会得到主线默认语义，不能代表真人开口 round2 真实验证
- 因此本轮按 honest blocked 路径收口：
  - 不伪造配置
  - 不伪造 `success`
  - 只更新日志与同步事实

## 当前剩余最高优先级 blocker

- 缺 `config/formal_api_demo.local.toml`
- 因而无法在当前 worktree 做带真实 API Key 的 `liveportrait-detect -> liveportrait` 实调

## 下一轮唯一最关键一步

- 先补可用的 `config/formal_api_demo.local.toml`
- 并确保其中显式提供：
  - `provider.name`
  - `auth.api_key`
  - `tts.api_route_family`
  - `tts.model`
  - `tts.voice`
  - `image_generation.model`
  - `video_generation.model`
  - `portrait_detect.enabled`
  - `portrait_detect.model`
  - `portrait_video_generation.enabled`
  - `portrait_video_generation.model`
- 然后用正式入口跑一轮真实 `liveportrait-detect -> liveportrait`
