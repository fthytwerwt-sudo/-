# Latest

## 当前主读取分支

- 当前默认主读取分支：
  - `codex/user-readable-map`
- 2026-04-03 已完成任务分支回流：
  - `codex/formal-api-demo-wan-provider-impl`
  - 已通过 `cherry-pick` 同步回 `codex/user-readable-map`
  - 已 push 到 GitHub
- 当前主读取分支上的 `latest` 已不再停留在“wan provider 仍 blocked”的旧状态

## 当前 formal_api_demo 真实状态

- TTS API：
  - `success`
  - 当前已有真实请求实现与测试覆盖
- 图片 API：
  - `success`
  - `wan2.6-image` provider implementation 已接入并已回流主读取分支
- 通用视频 API：
  - `success`
  - `wan2.6-t2v` provider implementation 已接入并已回流主读取分支
- 真人开口分支：
  - `blocked`
  - 路线仍是 `liveportrait-detect -> liveportrait`
  - 当前仍缺前置检测与开口视频 provider implementation
- local assembly：
  - `success`
  - 正式 local assembly implementation 已接入
  - 当前会从 manifest 读取真实本地图片 / 视频素材、配音音频、字幕，并输出正式本地 `final.mp4`
  - `preview` 继续只保留为辅助产物，不再冒充 formal assembly success
- overall：
  - `blocked`
  - 普通 generation 主线与正式 local assembly 已成立
  - 当前剩余最高优先级 blocker 已收束为真人开口分支 `liveportrait-detect -> liveportrait`

## 最近一次真正完成了什么

- 已把以下任务分支结果同步回主读取分支：
  - `07ff6a1 Implement formal_api_demo wan visual providers`
  - `5aab536 docs: verify formal_api_demo wan provider status`
- 已补执行层主读取规则：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 已把正式 local assembly 从“实现未接入”推进到“可执行最小实现”：
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`

## 当前剩余最高优先级 blocker

- 真人开口分支：
  - `liveportrait-detect -> liveportrait`

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_branch_sync_and_local_assembly_round1.md`
- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
