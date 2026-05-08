# 2026-04-03 formal_api_demo 真人开口 round2：缺本地正式配置，honest blocked

## 本轮目标

- 不回头重做已成立普通主线
- 不提前处理 A 线质量问题
- 只推进 `liveportrait-detect -> liveportrait` 的真实线上验证 round2
- 若缺真实本地正式配置，则把 blocker 收口到最具体，并按仓库规则回写

## skill 检查结果

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills`：
  - 已检查
  - 本轮实际纳入：
    - `using-superpowers`
    - `systematic-debugging`
    - `using-git-worktrees`
    - `verification-before-completion`
- 说明：
  - 当前用户目标、边界、读取列表和完成标准已经足够清楚
  - 因此本轮未再额外展开 `brainstorming` / `writing-plans`

## git / worktree 真实起点

- 用户给定目标分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 初始工作目录 `/Users/fan/Documents/视频工厂` 的真实状态：
  - 当前分支是 `codex/round1`
  - 且存在与本轮无关的未提交改动
- 直接切换失败的真实原因：
  - `codex/formal-api-demo-quality-liveportrait-round1` 已被现成 worktree 占用
- 本轮实际执行位置：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 该 worktree 的初始状态：
  - 分支：`codex/formal-api-demo-quality-liveportrait-round1`
  - HEAD：`1b11c7a31818494e730590f052c1e49d4cc7b327`
  - 工作区：干净

## round1 是否只停在任务分支

- 结论：
  - 不是
- 本轮核对结果：
  - `codex/formal-api-demo-quality-liveportrait-round1` 的 HEAD 是 `1b11c7a`
  - `codex/user-readable-map` 的 HEAD 是 `ca7cc07`
  - 两个分支的 tree SHA 都是 `3cb17c569df70de2ad391b627ab9f334ec7db305`
- 这表示：
  - round1 的文件内容已回流到主读取分支
  - 但任务分支与主读取分支的提交 SHA 仍不同
- 所以本轮必须按真实 git 状态理解：
  - “内容已回流”
  - 不等于“当前没有新的 round2 回写动作”

## 配置检查结果

- `config/formal_api_demo.local.toml`：
  - 当前不存在
- 因此本轮最具体 blocker 已直接收口为：
  - 整个本地正式配置文件缺失
- 因为文件本身不存在，所以本轮不能诚实声称已经完成了以下字段审计：
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

## 正式入口核对结果

- 已核对正式入口：
  - `scripts/generate_formal_api_demo.py`
- 已确认：
  - 入口最终调用 `run_generation_pipeline(...)`
  - 默认 local config 路径就是 `config/formal_api_demo.local.toml`
- 已额外核对：
  - `config/formal_api_demo.example.toml`
- 关键事实：
  - example config 中：
    - `portrait_detect.enabled = false`
    - `portrait_video_generation.enabled = false`
- 这意味着：
  - 在“不伪造 local config”的前提下，直接强跑正式入口并不能产出 B 线真人开口 round2 的专属 `manifest / result_summary`
  - 它只会落回普通主线默认语义，无法代表 `liveportrait-detect -> liveportrait` 的真实线上验证

## 真人开口实调结果

- 是否真实执行了 `liveportrait-detect -> liveportrait`：
  - 否
- 当前状态：
  - `blocked`
- 最具体原因：
  - 当前 round2 worktree 缺少整个 `config/formal_api_demo.local.toml`
  - 因而没有真实 API Key，也没有开启 portrait 分支的正式本地配置可供实调
- 本轮明确没有做：
  - 不伪造 local config
  - 不伪造真人开口 `success`
  - 不把“代码 / 测试已补”偷换成“线上已成立”
  - 不回头改 A 线质量

## 为什么本轮没有改写 manifest / result_summary

- 当前已有 `dist/formal_api_demo/result_summary.json` / `manifest.json`：
  - 属于已成立普通主线与本地 assembly 产物
  - 其中 portrait 分支状态仍是 `skipped`
- 若在缺 local config 的前提下强跑正式入口：
  - 由于 example config 默认关闭 portrait 分支
  - 生成结果并不能代表 B 线 round2 的 blocked 事实
  - 反而会把“缺本地正式配置导致无法做真人开口实调”的问题混写成主线默认语义
- 因此本轮按真实边界收口：
  - 只更新日志
  - 不伪造 B 线 `manifest / result_summary`
  - 也不覆盖已成立主线产物

## 本轮实际修改文件

- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_liveportrait_round2_blocked_by_missing_local_config.md`

## 本轮实际运行的验证命令

- `git status --short --branch && git rev-parse HEAD && git branch --show-current`
- `git worktree list`
- `git rev-parse HEAD codex/user-readable-map origin/codex/user-readable-map origin/codex/formal-api-demo-quality-liveportrait-round1`
- `git rev-parse HEAD^{tree} codex/user-readable-map^{tree}`
- `git diff --name-status codex/user-readable-map..HEAD`
- `test -f config/formal_api_demo.local.toml`
- `python3 scripts/generate_formal_api_demo.py --help`

## 测试结果

- 本轮未运行单元测试 / 集成测试
- 原因：
  - 本轮没有代码改动
  - 也没有进入真实 API 实调阶段
  - 当前收口点是“本地正式配置文件缺失”，不是代码回归

## 当前状态改标

- 真人开口分支：
  - `blocked`
- overall：
  - `blocked`
- 当前最具体 blocker：
  - 缺 `config/formal_api_demo.local.toml`

## Git 同步锚点

- 当前工作分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 本轮开始前最新提交：
  - `1b11c7a31818494e730590f052c1e49d4cc7b327`
- 本轮开始前主读取分支提交：
  - `ca7cc07f12f446187ebad94d15e20aa78f5f59d9`
- 本轮开始前内容层同步关系：
  - 两边 tree SHA 已一致
- 是否已 push：
  - 是
- 是否已同步回 `codex/user-readable-map`：
  - 是

## 下一轮唯一最关键一步

1. 补可用的 `config/formal_api_demo.local.toml`
2. 在正式入口上跑一轮带真实 API Key 的 `liveportrait-detect -> liveportrait`
3. 只有 detect / liveportrait / 轮询 / 下载 / 本地结果落地都真实成功后，才允许把真人开口分支改成 `success`
