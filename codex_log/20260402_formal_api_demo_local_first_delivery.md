# 2026-04-02 formal_api_demo 本地优先交付路径落地

## 本轮目标

- 不再把阿里云付费的 cloud assembly / 模板工厂 / 云端组装当当前主线
- 把 `formal_api_demo` 改成“本地优先出片”的最小闭环
- 目标路径改成：
  - 文本需求
  - 脚本
  - 配音
  - 字幕
  - 视觉素材 / 视觉计划
  - 本地 assembly
  - 本地 mp4
  - 人工上传

## 执行前已确认事实

- 旧口径下：
  - generation 已能真实落出脚本、整段配音、字幕和视觉计划
  - assembly 已能真实落出本地 preview
  - 但 `storage.space_name` / `assembly.template_id` 会让 cloud assembly 直接压住整体状态
- 当前用户要求：
  - cloud assembly 降级为后续增强项
  - 本地 mp4 成为当前默认交付件

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`

## 实际改动

### 1. 状态口径改成本地优先

在 `formal_api_demo_core.py` 中把状态拆成：

- `generation`
- `local_assembly`
- `cloud_assembly`
- `overall_status`

并把整体成功条件改成：

- generation 成功
- local assembly 成功
- 即使 cloud 仍是 `skipped` / `blocked`，也不再把整条当前主线路判失败

### 2. cloud visual generation 降级为可选增强项

- 视觉计划仍会真实落出
- top-level `visual_generation.status` 现在按本地可用口径记为 `success`
- 新增 `cloud_visual_generation_status`
- 若未配置 `image_generation.model` / `video_generation.model`，当前记为 `skipped`
- 不再阻断本地 generation 成功

### 3. cloud assembly 降级为可选增强项

- `storage.space_name`
- `assembly.template_id`

不再是本地主线路硬阻塞。

现在的口径是：

- 本地 preview / 本地 mp4 成功 => `local_assembly = success`
- 云端字段未配置 => `cloud_assembly = skipped`
- `overall_status` 继续保持 `success`

### 4. 默认交付件改成本地 mp4

沿用当前 preview 文件作为本阶段默认交付件，不另起大架构：

- `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

并在 manifest / result_summary 中写明：

- `manifest.assembly.delivery_mode = "local_mp4"`
- `manifest.assembly.delivery_video_path = ...preview.mp4`
- `result_summary.artifact_paths.final_video = ...preview.mp4`

### 5. 配置说明更新

在 `config/formal_api_demo.example.toml` 中明确注明：

- 当前阶段本地优先
- cloud visual generation 可选
- cloud assembly 可选
- 未配置云端字段不阻断本地出片

## 测试与验证

### 1. 测试更新

更新 / 调整了 `tests/test_formal_api_demo_pipeline.py`，覆盖：

- 无 `storage.space_name`
- 无 `assembly.template_id`
- 但本地 assembly 仍成功
- 无 cloud visual 配置
- 但 generation 仍成功

### 2. 验证命令

已执行：

- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`

结果：

- `Ran 20 tests in 0.146s`
- `OK`

## 真实执行

### 1. generation

执行：

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

结果：

- `overall_status = success`
- `generation_status = success`
- `tts_probe_status = success`
- `voiceover_status = success`
- `captions_status = success`
- `visual_generation_status = success`
- `cloud_visual_generation_status = skipped`

真实产物：

- `dist/formal_api_demo/tts/voice_probe.mp3`
- `dist/formal_api_demo/tts/formal_voiceover.mp3`
- `dist/formal_api_demo/script.txt`
- `dist/formal_api_demo/captions.srt`
- `dist/formal_api_demo/visual_generation_plan.json`

### 2. local assembly

执行：

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

结果：

- `overall_status = success`
- `generation_status = success`
- `assembly_status = success`
- `local_assembly_status = success`
- `cloud_assembly_status = skipped`
- `assembly_preview_status = success`

真实产物：

- `dist/formal_api_demo/assembly/preview_manifest.json`
- `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

## 当前结果

- 本地 0-1 主链已经成立：
  - 文本需求 → 脚本 → 配音 → 字幕 → 视觉计划 → 本地 assembly → 本地 mp4
- cloud assembly / 模板工厂 / 云端组装仍未接入
- 但它们已经不再阻断当前阶段本地交付

## 下一步建议

- 下一轮优先看本地成片质量，而不是再回头做 cloud 配置 gate
- 最值的下一步是：
  - 复审 `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  - 如有必要，再收口 `video_builder.swift` 的视觉呈现质量
