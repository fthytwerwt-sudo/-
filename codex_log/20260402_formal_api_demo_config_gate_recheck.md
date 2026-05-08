# 2026-04-02 formal_api_demo 本地配置阻塞复核

## 本轮目标

- 不从 TTS 子线重新开始
- 以上一轮真实完成状态为准，继续推进 `formal_api_demo` 正式链路
- 先核对本地 `config/formal_api_demo.local.toml` 是否已补齐当前最小硬阻塞字段
- 若已补齐，则继续打正式视觉生成 + 云端 assembly
- 若未补齐，则把最小硬阻塞压到明确字段 / 明确语义，不猜值、不假装成功

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

### 1. 本地配置复核

只读检查本地 `config/formal_api_demo.local.toml`，不回显真实值。

核对目标字段：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

同时补核：

- `provider.name`
- `provider.region`
- `auth.api_key`

### 2. 复核结论

已存在且有效：

- `provider.name`
- `provider.region`
- `auth.api_key`

仍缺失 / 仍是 placeholder：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

## 当前最小硬阻塞顺序

### 第一层：用户必须手填的本地真实值

1. `image_generation.model`
   - 作用：正式视觉生成里的图片素材模型标识
   - 当前缺失时，图片段落无法进入正式远端视觉生成

2. `video_generation.model`
   - 作用：正式视觉生成里的视频素材模型标识
   - 当前缺失时，视频段落无法进入正式远端视觉生成

3. `storage.space_name`
   - 作用：正式云端组装阶段的素材上传 / 存储空间定位
   - 当前缺失时，assembly 无法进入正式云端存储与资源引用链路

4. `assembly.template_id`
   - 作用：正式云端组装模板定位
   - 当前缺失时，assembly 无法进入正式模板化拼接

### 第二层：下游阻塞，不是当前首层问题

- `visual_assets_not_ready`
  - 当前不是独立首层问题
  - 只是由 `image_generation.model` / `video_generation.model` 未补齐导致的下游阻塞

### 第三层：不是本轮第一手该先处理的项

以下项仍存在，但不是当前用户第一手应先填的本地字段阻塞：

- `image_generation_provider_implementation`
- `video_generation_provider_implementation`
- `provider_assembly_implementation`

原因：

- 当前连首层配置值都还没补齐
- 在用户本地真实值仍缺失前，不应把问题写散到更后层实现缺口

## 本轮没有继续硬跑的原因

本轮按用户要求进入分支 B：

- 本地关键字段仍缺失
- 因此不继续硬跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

原因不是路线回退，而是：

- 继续硬跑不会产生新的有效云端事实
- 只会重复已有 blocked 结果

## 当前仍保留的已确认事实

- generation 已真实接上：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/visual_generation_plan.json`
- assembly 已真实接上本地 preview：
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

必须继续明确：

- 本地 preview 仍可用
- 但这不能写成正式云端视频链路已跑通

## 本轮结论

本轮属于次优完成：

- 没有伪造成功
- 没有把问题写散
- 已把最小硬阻塞继续压在明确字段和明确语义上

当前用户必须先补的本地真实值只有 4 个：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

补齐这 4 项后，再继续正式视觉生成 / 云端 assembly 才有意义。
