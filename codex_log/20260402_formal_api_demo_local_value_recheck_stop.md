# 2026-04-02 formal_api_demo 本地字段复核后停止执行

## 本轮目标

- 不复述旧 gate 结论
- 先只读判断本地 4 个首层字段现在是否已经是有效真实值
- 若都有效，则立刻继续执行正式视觉生成 + 云端 assembly
- 若其中任一仍无效，则把结论压到该字段本身并立即停止，不继续硬跑

## 执行前已确认事实

- generation 已真实落出：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/visual_generation_plan.json`
- assembly 已真实落出本地 preview：
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 上一轮最小硬阻塞是：
  - `image_generation.model`
  - `video_generation.model`
  - `storage.space_name`
  - `assembly.template_id`

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_generation_and_assembly.md`
- `codex_log/20260402_formal_api_demo_config_gate_recheck.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `cases/formal_api_demo.md`

## 实际执行

### 1. 本地字段有效性检查

只读检查本地 `config/formal_api_demo.local.toml`，不回显真实值。

核对目标：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

执行后结论：

- `image_generation.model`：无效
- `video_generation.model`：无效
- `storage.space_name`：无效
- `assembly.template_id`：无效

### 2. 最小补充诊断

继续做了不泄露真实值的最小诊断，只确认：

- local config 文件存在
- 这 4 个键在 local config 中都能被读到
- 但它们当前仍都被解析逻辑判定为“空值 / placeholder 风格值”

因此本轮按用户要求立即停止，不继续执行：

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

## 当前结果

- 本轮没有进入新的 generation 执行
- 本轮没有进入新的 assembly 执行
- 当前阻塞已经收口到 4 个字段本身，而不是更后层 provider / 模板 / 存储语义

当前最小硬阻塞：

- `image_generation.model`
- `video_generation.model`
- `storage.space_name`
- `assembly.template_id`

## 下一步建议

- 先重新检查本地 `config/formal_api_demo.local.toml` 里上述 4 个字段的实际值格式
- 确保它们不再被当前解析逻辑判成空值或 placeholder
- 仅在这 4 项都变成有效值后，再继续真实执行正式视觉生成 + 云端 assembly
