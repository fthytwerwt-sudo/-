# 2026-04-02 formal_api_demo 口径统一：generation 继续接，本地 assembly 默认交付

## 本轮目标

- 统一 `formal_api_demo` 当前仓库里的冲突口径。
- 明确当前正式口径：
  - 视频 API 继续接入
  - TTS API 继续接入
  - 当前默认交付路径是本地 assembly
  - 本地 mp4 成功后可作为当前阶段默认交付件
  - `storage.space_name` / `assembly.template_id` 不再是当前阶段整体硬前置

## 执行前已确认事实

- `codex_log/latest.md` 已经部分切到“本地优先出片”，但旧日志仍保留“4 个字段无效 -> 继续盯云端 assembly”的旧口径。
- `formal_api_demo_core.py` 当前工作区里存在未提交修改：
  - generation gate 已尝试把图片 / 视频模型拉回正式主链
  - 但 `build_visual_generation_plan(...)` 仍会把缺视觉前提的 generation 写成 `success`
- `tests/test_formal_api_demo_pipeline.py` 里已经没有“preview 成功但 overall blocked”的旧 assembly 断言
  - 但仍保留了“缺 visual model 也能 generation success”的旧 generation 断言

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `project_source/06_project_index.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_generation_and_assembly.md`
- `codex_log/20260402_formal_api_demo_local_first_delivery.md`
- `codex_log/20260402_formal_api_demo_config_gate_recheck.md`
- `codex_log/20260402_formal_api_demo_local_value_recheck_stop.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`

## 本轮识别到的关键冲突

1. `codex_log/latest.md` 已偏向本地默认交付，但旧日志仍在强调 `storage.space_name` / `assembly.template_id` 是推进主线的首层阻塞。
2. `formal_api_demo_core.py` 的 generation gate 会把视觉前提缺失记成 blocked，但生成结果阶段又会把 `visual_generation.status` 强行写成 success，导致 `generation_status` 被错误放行。
3. `formal_api_demo_core.py` 的 assembly 逻辑已经把 cloud assembly 降成 optional，但 generation 的真实状态语义还没同步收口。
4. `tests/test_formal_api_demo_pipeline.py` 仍保留“缺 image/video model 也能 generation success”的旧口径，需要改成真正拦截。

## 实际改动

### 1. `formal_api_demo_core.py`

- 保留：
  - 视频 API / 图片 API 仍属于 generation 主链
  - local assembly + 本地 mp4 仍是当前默认交付路径
- 调整：
  - `_evaluate_visual_generation_gate(...)`
    - 缺 `image_generation.model` / `video_generation.model` 时，仍记 `blocked`
    - 模型已配置但 provider implementation 未接入时，cloud visual generation 改记 `skipped`
  - `build_visual_generation_plan(...)`
    - 缺视觉前提时，顶层 `visual_generation.status = blocked`
    - 只有前提齐时，顶层 `visual_generation.status = success`
    - 不再把“缺模型”偷偷写成 generation success
  - `build_generation_result_summary(...)`
    - `blocked_reason` 现在会带上视觉层的真实阻塞原因

### 2. `tests/test_formal_api_demo_pipeline.py`

- 用例 A：
  - 本地主链成立时显式提供 `image_generation.model` / `video_generation.model`
  - 继续断言：
    - `overall_status = success`
    - `local_assembly_status = success`
    - `cloud_assembly_status = skipped`
- 用例 B：
  - 把旧的“缺 cloud visuals 也 success”断言改成：
    - 缺 `image_generation.model` / `video_generation.model`
    - `generation_status = blocked`
    - `overall_status = blocked`
- 为稳定验证补了测试内的音频拼接 stub，避免假 mp3 依赖真 ffmpeg 行为

### 3. `config/formal_api_demo.example.toml`

- 明确写清：
  - `image_generation.model`
  - `video_generation.model`
  当前仍属于正式 generation 主链，建议继续接入，不是可删除摆设字段
- 明确写清：
  - `storage.space_name`
  - `assembly.template_id`
  当前属于 cloud assembly 增强项，未配置不阻断本地出片

### 4. 日志

- 更新了 `codex_log/latest.md`
- 新增本日志，统一记录本轮冲突、改动、验证与结论

## 当前统一后的正式口径

### generation 层

- 当前仍继续推进并保留在正式主链：
  - TTS API
  - 图片生成 API
  - 视频生成 API
  - 脚本 / 字幕 / 视觉计划
- 口径收口：
  - 缺 `image_generation.model` / `video_generation.model` 时，generation 不能写成 success
  - 模型已配置但远端 provider implementation 尚未接入时，当前先保留视觉计划并继续走本地 assembly

### assembly 层

- 当前默认交付路径：
  - local assembly
  - 本地 mp4
  - 人工上传
- cloud assembly 当前改成 optional / skipped：
  - 缺 `storage.space_name`
  - 缺 `assembly.template_id`
  不再把当前阶段整体压成 failed / blocked

### overall 判定

- generation 成功 + local assembly 成功 => `overall_status = success`
- generation 成功 + local assembly 成功 + cloud assembly 未配置 => `cloud_assembly_status = skipped`，`overall_status` 仍为 success
- generation 未成功 => `overall_status` 才允许 blocked / failed
- local assembly 未成功 => `overall_status` 才允许 blocked / failed

## 实际执行

### TDD 红灯

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_blocks_when_visual_generation_models_missing`
  - 初次运行失败
  - 暴露出当前实现仍把缺视觉模型的 generation 写成 success

### 过程性回归

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_blocks_when_visual_generation_models_missing tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_writes_preview_video_and_keeps_cloud_status_optional tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_edge_gateway_keeps_tts_success_and_local_generation_success`
  - 结果：`Ran 3 tests`
  - `OK`

### 最终验证

- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - 结果：通过
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 20 tests in 0.069s`
  - `OK`

## 当前结果

- 当前仓库已统一成最新正式口径：
  - 视频 API 继续接
  - local assembly 默认交付
  - cloud assembly optional
- `storage.space_name` / `assembly.template_id` 不再是当前整体硬阻塞
- `image_generation.model` / `video_generation.model` 继续保留 generation 主链身份：
  - 缺失时 generation 被真实拦截
  - 不再被错误写成 success

## 下一步建议

- 如果下一轮继续推进 generation，优先补真实图片 / 视频 provider implementation。
- 如果下一轮继续推进交付质量，优先复审本地 mp4 的视觉与节奏，而不是再把 assembly 拉回云端前置。
