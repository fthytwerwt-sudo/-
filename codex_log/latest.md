# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-03 本轮已把 `formal_api_demo` 的普通图片 / 视频主线 provider implementation 真实接通：
  - `wan2.6-image`
  - `wan2.6-t2v`
- 当前图片 / 视频主线已不再停留在“模型名占位 + visual plan / preview”语义：
  - 会真实创建阿里 DashScope 异步任务
  - 会轮询 `/api/v1/tasks/{task_id}`
  - 会把临时结果 URL 下载转存到本地 `dist`
  - 会把本地素材路径写回 manifest / result_summary / segment outputs
- 本轮没有继续做 preview 画面 round2，也没有继续扩 cloud assembly。
- 本轮仍然没有伪造真人开口分支：
  - `liveportrait-detect -> liveportrait` 继续诚实 `blocked`

## 当前真实状态

- TTS API：
  - `success`
  - 当前已有真实请求实现与测试覆盖
- 图片 API：
  - `success`
  - `wan2.6-image` provider implementation 已接入
  - 已覆盖创建任务 / 轮询成功 / 下载本地文件 / 缺结果 URL / 轮询超时等测试
- 通用视频 API：
  - `success`
  - `wan2.6-t2v` provider implementation 已接入
  - 已覆盖创建任务 / 轮询成功 / 下载本地文件 / 下载失败等测试
- 真人开口分支：
  - `blocked`
  - 路线仍是 `liveportrait-detect -> liveportrait`
  - 当前仍缺前置检测与开口视频 provider implementation
- local assembly：
  - `blocked`
  - 当前只有辅助 `preview`
  - 正式本地素材拼接 implementation 仍未接入
- overall：
  - `blocked`
  - 普通图片 / 视频 generation 主线已通
  - 当前主要卡在正式本地 assembly；真人开口分支也仍未接入

## 最近一次真正完成了什么

- 更新了：
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [tests/test_formal_api_demo_pipeline.py](/Users/fan/Documents/视频工厂/tests/test_formal_api_demo_pipeline.py)
  - [codex_source/02_current_execution_context.md](/Users/fan/Documents/视频工厂/codex_source/02_current_execution_context.md)
  - 本日志入口
- 已把普通图片 / 视频主线从“provider implementation missing”改成“真实 create / poll / download”：
  - 图片结果通过本地文件路径落入 `segment_assets[*].image_asset_path`
  - 视频结果通过本地文件路径落入 `segment_assets[*].video_asset_path`
  - `segments[*].task_slots.image_task_id / video_task_id` 也会同步写回
- `generation success` 继续严格要求：
  - TTS success
  - captions success
  - `wan2.6-image` / `wan2.6-t2v` 主线真实成功

## 当前最关键下一步

- 当前最高优先级不再是普通图片 / 视频 provider，而是：
  - 正式本地 assembly implementation
- 次高优先级仍是：
  - 真人开口分支 `liveportrait-detect -> liveportrait`
- 在这两步成立前：
  - 不要把 `preview` 写成正式 assembly success
  - 不要把 liveportrait 写成已接通

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_mainline_realign.md`
- `codex_log/20260403_formal_api_demo_free_model_route.md`
- `codex_log/20260403_formal_api_demo_wan_provider_impl_round1.md`
- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
