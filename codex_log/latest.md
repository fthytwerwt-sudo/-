# Latest

## 当前项目执行状态

- `formal_api_demo` 当前正式主路径已统一为：
  - 文本需求
  - 脚本
  - 配音 API
  - 图片 / 视频生成 API
  - 本地 assembly
  - 本地 mp4
  - 人工上传
- generation 仍保留正式主链身份：
  - `image_generation.model`
  - `video_generation.model`
  不是可删除摆设；缺失时 `generation` 不能写成 `success`
- assembly 当前默认走本地交付：
  - `storage.space_name`
  - `assembly.template_id`
  已降级为 cloud assembly optional，不再阻断当前阶段本地出片

## 最近一次完成了什么

- 统一了 `formal_api_demo_core.py` 的口径：
  - 缺 `image_generation.model` / `video_generation.model` 时，`generation_status = blocked`
  - generation 成功 + local assembly 成功时，`overall_status = success`
  - cloud assembly 未配置时，`cloud_assembly_status = skipped`
- 更新了 `tests/test_formal_api_demo_pipeline.py`：
  - 本地主链成立时不再把整体写成 blocked
  - generation 缺图片 / 视频前提时才允许整体 blocked
- 更新了 `config/formal_api_demo.example.toml` 注释：
  - generation 主链继续保留图片 / 视频 API
  - cloud assembly 字段改成 optional 说明

## 当前最关键的下一步

- 若继续推进 generation，优先补真实图片 / 视频生成 provider implementation，而不是再把 assembly 拉回云端硬前置。
- 若继续推进交付质量，优先复审本地 mp4 的视觉和节奏表现。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_local_assembly_default_generation_required.md`
- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
