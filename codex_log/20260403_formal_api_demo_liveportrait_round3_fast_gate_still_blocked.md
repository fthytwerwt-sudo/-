# 2026-04-03 formal_api_demo 真人开口 round3：前置闸门快速止损，仍 blocked

## 本轮目标

- 以“质量保证优先、同时尽量加快进度”为原则
- 先跑最快前置闸门
- 只有 local config 过闸门，才进入最小真人开口闭环
- 若闸门不过，立刻 honest blocked，不空跑

## 本轮是否命中相关 skill

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills`：
  - 已检查
  - 本轮实际纳入：
    - `using-superpowers`
    - `systematic-debugging`
    - `using-git-worktrees`
    - `verification-before-completion`

## git / worktree 起点

- 当前工作目录：
  - `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1`
- 当前工作分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 本轮开始时 HEAD：
  - `4cd0f434f1cdc6ed96d6000257c0255aed771b0d`
- 工作区是否干净：
  - 是
- 说明：
  - 主工作区 `/Users/fan/Documents/视频工厂` 仍有无关上下文，不适合混在里面继续做
  - 因此本轮继续使用现成目标 worktree

## local config 检查结果

- `config/formal_api_demo.local.toml`：
  - 不存在
- 这是本轮最快前置闸门
- 结论：
  - 闸门未通过
  - 立即停止后续真人开口实调

## 关键字段审计结果

- 未进入字段级审计
- 原因：
  - local config 整个文件不存在
  - 在文件缺失的前提下，继续做字段审计没有意义，也不符合“最快止损”原则

## 是否真实执行了 `liveportrait-detect -> liveportrait`

- 否

## 实调结果或 blocked 原因

- 当前结果：
  - `blocked`
- 最具体原因：
  - 缺整个 `config/formal_api_demo.local.toml`
- 因此前置闸门直接失败：
  - 没有真实 API Key 可审计
  - 没有可用的 portrait 分支正式配置
  - 没有执行 detect
  - 没有执行 liveportrait
  - 没有轮询
  - 没有下载本地结果

## 本轮实际修改文件

- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_liveportrait_round3_fast_gate_still_blocked.md`

## 本轮实际运行的命令

- `pwd && rg --files -g 'AGENTS.md' -g 'skills/**'`
- `git worktree list`
- `git status --short --branch && git rev-parse HEAD && git branch --show-current && pwd`
- `sed -n ... AGENTS.md / codex_source/* / codex_log/* / formal_api_demo_core.py / tests/test_formal_api_demo_pipeline.py / scripts/generate_formal_api_demo.py`
- `test -f config/formal_api_demo.local.toml`

## 测试 / 验证结果

- 本轮未运行单元测试
- 本轮未运行真人开口线上实调
- 已完成的验证：
  - worktree / 分支 / HEAD / 工作区干净度核对
  - local config 存在性核对
  - 正式入口路径核对
- 未完成的验证：
  - 关键字段级审计
  - detect / liveportrait 真实调用
  - 本地真人开口结果文件落地验证

## 当前状态改标

- 真人开口分支：
  - `blocked`
- overall：
  - `blocked`

## Git 同步锚点

- 当前工作分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 本轮开始时最新提交 SHA：
  - `4cd0f434f1cdc6ed96d6000257c0255aed771b0d`
- 是否已 push：
  - 是
- 是否已同步回 `codex/user-readable-map`：
  - 是

## 下一轮唯一最关键一步

1. 把可用的 `config/formal_api_demo.local.toml` 放进当前目标 worktree
2. 通过字段闸门后，用正式入口只跑最小 `liveportrait-detect -> liveportrait` 闭环
