# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-03 本轮已把 `formal_api_demo` 的阿里免费优先模型路线写回仓库：
  - 通用图像主线：`wan2.6-image`
  - 通用视频主线：`wan2.6-t2v`
  - 真人开口前置检测：`liveportrait-detect`
  - 真人开口生成分支：`liveportrait`
- 本轮不是继续做 preview 画面 round2，也没有继续修 `seg02` 视觉表达。
- 本轮只完成了模型路线与阻塞语义收口，不代表 provider implementation 已真实接通。

## 当前真实状态

- TTS API：
  - `success`
  - 当前已有真实请求实现与测试覆盖
- 图片 API：
  - `blocked`
  - 已明确免费优先模型为 `wan2.6-image`，但 provider implementation 仍未接入
- 通用视频 API：
  - `blocked`
  - 已明确免费优先模型为 `wan2.6-t2v`，但 provider implementation 仍未接入
- 真人开口分支：
  - `blocked`
  - 路线已明确为 `liveportrait-detect -> liveportrait`
  - 当前仍缺前置检测与开口视频 provider implementation
- local assembly：
  - `blocked`
  - 当前只能生成辅助 `preview`，正式本地素材拼接 implementation 仍未接入
- overall：
  - `blocked`

## 最近一次真正完成了什么

- 更新了：
  - [config/formal_api_demo.example.toml](/Users/fan/Documents/视频工厂/config/formal_api_demo.example.toml)
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [codex_source/02_current_execution_context.md](/Users/fan/Documents/视频工厂/codex_source/02_current_execution_context.md)
  - 本日志入口
- 已把主线通用视频模型和真人开口模型明确拆开：
  - `wan2.6-image + wan2.6-t2v` 只代表普通图片 / 视频主线
  - `liveportrait-detect + liveportrait` 只代表真人开口分支
- 已把 `liveportrait` 的前置检测依赖写进 formal_api_demo 核心语义：
  - 不得把真人开口模型和通用视频模型混成一条路线
  - provider 未接通时必须继续诚实 `blocked`

## 当前最关键下一步

- 当前最高优先级不是继续修 preview 画面，而是：
  - 先补 `wan2.6-image` / `wan2.6-t2v` 的真实 provider implementation
  - 若要推进真人开口，再补 `liveportrait-detect` / `liveportrait` 的真实 provider implementation
- 在这一步成立前：
  - 不要再把 `visual plan / preview` 写成 generation success
  - 不要再把“继续修 preview 画面”写成当前最高优先级

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_mainline_realign.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
