# 2026-04-03 formal_api_demo wan provider implementation 复核

## 本轮目标

- 按当前仓库入口规则复核 `formal_api_demo` 的普通图片 / 视频主线
- 确认 `wan2.6-image` / `wan2.6-t2v` 是否仍停留在“模型路线已定但 provider 未接入”
- 若当前 HEAD 已经真实接通，则不要重复造轮子；只把验证结果如实写回

## 读取文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_mainline_realign.md`
- `codex_log/20260403_formal_api_demo_free_model_route.md`
- `config/formal_api_demo.example.toml`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `tests/test_formal_api_demo_pipeline.py`

## skill 检查

- 仓库本地 `skills/`：
  - 不存在
- 全局 `~/.codex/skills`：
  - 已检查
  - 本轮纳入：
    - `using-superpowers`
    - `verification-before-completion`
  - 已补读但本轮未进入新实现流程：
    - `brainstorming`
    - `test-driven-development`
- 说明：
  - 当前分支 HEAD 已含目标实现，本轮没有进入新的功能设计 / 红绿重构写码阶段，因此未新增 TDD 改动

## 代码审计结论

- 当前分支：
  - `codex/formal-api-demo-wan-provider-impl`
- 当前 HEAD：
  - `07ff6a1 Implement formal_api_demo wan visual providers`
- 审计结果：
  - `formal_api_demo_core.py` 已存在普通图片 / 视频主线真实实现
  - `wan2.6-image` 已实现：
    - DashScope 异步创建任务
    - `/api/v1/tasks/{task_id}` 轮询
    - 结果 URL 提取
    - 下载到本地 `dist/formal_api_demo/visual/`
    - 写回 manifest / result_summary / `segments[*].output_slots.visual_uri`
  - `wan2.6-t2v` 已实现：
    - DashScope 异步创建任务
    - `/api/v1/tasks/{task_id}` 轮询
    - 结果 URL 提取
    - 下载到本地 `dist/formal_api_demo/visual/`
    - 写回 manifest / result_summary / `segments[*].output_slots.visual_uri`
  - 真人开口分支仍保持诚实 `blocked`
  - `generation success` 仍建立在 TTS + captions + visual_generation 全部成功之上

## 验证命令与结果

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_aliyun_bailian_downloads_local_visual_assets tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_marks_blocked_when_aliyun_visual_task_poll_times_out tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_marks_failed_when_aliyun_image_task_missing_result_url tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_marks_failed_when_aliyun_video_download_fails tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_keeps_liveportrait_branch_honestly_blocked`
  - 结果：`Ran 5 tests ... OK`
- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - 结果：通过
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 26 tests ... OK`
- `git diff --name-only -- formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py config/formal_api_demo.example.toml codex_log/latest.md codex_source/02_current_execution_context.md codex_source/03_research_findings_bridge.md`
  - 结果：除本轮日志外，没有新的目标文件改动

## 本轮实际改动

- 更新：
  - `codex_log/latest.md`
- 新增：
  - `codex_log/20260403_formal_api_demo_wan_provider_impl_verification.md`
- 未改动：
  - `formal_api_demo_core.py`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `config/formal_api_demo.example.toml`

## 当前真实状态

- TTS API：
  - `success`
- 图片 API：
  - `success`
  - `wan2.6-image` provider implementation 已在当前 HEAD
- 通用视频 API：
  - `success`
  - `wan2.6-t2v` provider implementation 已在当前 HEAD
- 真人开口分支：
  - `blocked`
- local assembly：
  - `blocked`
- overall：
  - `blocked`

## 结论

- 当前普通图片 / 视频主线已经真实接通
- 本轮没有新增代码实现，因为当前分支已包含目标 provider implementation
- 当前最高优先级 blocker 已回到：
  - 正式本地 assembly implementation
  - 真人开口分支 `liveportrait-detect -> liveportrait`
