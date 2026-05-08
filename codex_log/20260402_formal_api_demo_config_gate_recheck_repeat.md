# 2026-04-02 formal_api_demo 本地配置阻塞复核（重复确认）

## 本轮目标

- 继续推进 `formal_api_demo` 正式链路
- 先只读核对本地 `config/formal_api_demo.local.toml`
- 若正式视觉生成 / 云端 assembly 的首层字段仍未补齐，则不硬跑、不猜值，直接把阻塞继续压到最小层

## 本轮读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_source/08_tts_style_execution_rules.md`
- `project_source/09_tts_voice_target_v1.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_generation_and_assembly.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `cases/formal_api_demo.md`

## 本轮执行

### 1. 本地配置只读复核

优先核对：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

同时补核：

- `provider.name`
- `provider.region`
- `auth.api_key`
- `output.dist_dir`
- `polling.interval_seconds`
- `polling.timeout_seconds`

### 2. 复核结论

已存在且有效：

- `provider.name`
- `provider.region`
- `auth.api_key`
- `output.dist_dir`
- `polling.interval_seconds`
- `polling.timeout_seconds`

仍缺失 / 仍是 placeholder：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

## 当前最小硬阻塞顺序

### 第一层：用户必须手填的本地真实值

1. `image_generation.model`
   - 作用：正式视觉生成中的图片素材模型标识
   - 未补齐时，图片侧远端视觉生成无法成立

2. `video_generation.model`
   - 作用：正式视觉生成中的视频素材模型标识
   - 未补齐时，视频侧远端视觉生成无法成立

3. `storage.space_name`
   - 作用：正式云端 assembly 的存储空间定位
   - 未补齐时，素材无法进入云端存储 / 引用链路

4. `assembly.template_id`
   - 作用：正式云端 assembly 的模板定位
   - 未补齐时，无法进入模板化云端拼装

### 第二层：下游阻塞，不是当前首层问题

- `visual_assets_not_ready`
  - 这次仍只是下游阻塞
  - 根因仍是 `image_generation.model` / `video_generation.model` 未补齐
  - 不应把它写成新的独立首层问题

### 第三层：不是当前第一阻塞的实现缺口

- `image_generation_provider_implementation`
- `video_generation_provider_implementation`
- `provider_assembly_implementation`

这些项仍存在，但在首层本地字段仍缺失的情况下，不是本轮最先该处理的用户侧问题。

## 本轮没有继续硬跑正式云端层

本轮继续走分支 B：

- 不继续跑 `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 不继续跑 `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

原因：

- 首层本地字段仍未补齐
- 继续硬跑不会产生新的正式云端事实
- 只会重复已有的 blocked 结果

## 当前仍保留的已确认事实

- generation 已真实落出：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/visual_generation_plan.json`
- assembly 已真实落出本地 preview：
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

必须继续明确：

- 本地 preview 仍可用
- 正式云端视频生成 / 云端 assembly 仍未跑通

## 本轮结论

这次复核结果与上一轮一致，没有出现新的更前置阻塞。

当前最小硬阻塞仍收敛在 4 个用户本地真实值：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

下一轮若要继续正式视觉生成 / 云端 assembly，最先应补齐这 4 项，而不是回头扩声音实验。
