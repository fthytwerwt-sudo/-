# 2026-04-02 formal_api_demo generation + assembly 推进

## 本轮目标

- 以上一轮真实完成状态为准：
  - TTS round2 已完成
  - 视频生成和 assembly 还没推进
- 本轮直接推进：
  - 视频生成层
  - assembly 层
- 目标不是继续调声音，而是把 `formal_api_demo` 从“已接通 TTS”推进到“视频生成 + assembly 已接上，并尽量落出第一版可复核视频产物”。

## 本轮读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_source/08_tts_style_execution_rules.md`
- `project_source/09_tts_voice_target_v1.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `cases/formal_api_demo.md`
- `video_builder.swift`

## 本轮前提核对

只读检查本地 `config/formal_api_demo.local.toml`，不回显真实值。

结果：

- 通过：
  - `provider.name`
  - `provider.region`
  - `auth.api_key`
- 未通过：
  - `image_generation.model`
  - `video_generation.model`
  - `storage.space_name`
  - `assembly.template_id`

## 本轮代码改动

### 1. 冻结当前 TTS 基线

- 在 `config/formal_api_demo.example.toml` 的 `[tts]` 中冻结：
  - `baseline_profile = "aliyun_old_A"`
  - `instruction = "你说话的情感是neutral。"`
  - `speech_rate = 1.18`
  - `pitch_rate = 0.92`
  - `volume = 46`
- 在 `formal_api_demo_core.py` 中补 `DEFAULT_FORMAL_TTS_BASELINE`，并把该基线写入 manifest。
- 清掉了 `DEFAULT_ALIYUN_TTS_STYLE_ROUND2_VARIANTS` 的重复常量定义，避免后段定义覆盖前段定义。

### 2. 推进 generation

- `run_generation_pipeline(...)` 不再只做 TTS probe。
- 现在 generation 会真实落：
  - `generation.tts_probe`
  - `generation.voiceover`
  - `generation.captions`
  - `generation.visual_generation`
- 新增了：
  - 整段配音生成：按分段文案逐段调用阿里 TTS，再拼成 `formal_voiceover.mp3`
  - `script.txt`
  - `captions.srt`
  - `timeline.json`
  - `visual_generation_plan.json`
  - `preview_storyboard.json`
- 顶层 `generation.status` 改为按正式链路口径汇总：
  - TTS 成功但视觉层 blocked 时，不再误报整层 success。

### 3. 推进 assembly

- `run_assembly_pipeline(...)` 不再只停在 plan。
- 顶层 assembly 仍按正式云端组装 Gate 判断。
- 同时补了本地 preview 组装路径：
  - 读取 manifest
  - 读取整段配音与字幕
  - 生成 `dist/formal_api_demo/assembly/preview_manifest.json`
  - 调用 `video_builder.swift`
  - 落出 `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- preview 只作为本地样片验证：
  - 不能写成云端正式链路成功
  - 但能证明音频、字幕、时间线和卡片画面已经真正串起来

### 4. Gate 与阻塞压缩

- generation 当前最小硬阻塞压到：
  - `image_generation.model`
  - `video_generation.model`
- assembly 当前最小硬阻塞压到：
  - `storage.space_name`
  - `assembly.template_id`
  - `visual_assets_not_ready`
- `_assembly_missing_prerequisites(...)` 不再先把 `access_key_id / secret_access_key` 当成首层阻塞，避免把问题写散。

## 测试与验证

已执行：

- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`

结果：

- 单测通过：`Ran 20 tests, OK`
- 新增覆盖：
  - generation 在视觉层 blocked 时，仍会落出整段配音、字幕、视觉计划
  - assembly 非 dry-run 会落出本地 preview 视频，同时保持云端 assembly blocked

## 真实执行

### 1. generation

执行：

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

结果：

- `overall_status = blocked`
- `generation_status = blocked`
- `tts_probe_status = success`
- `voiceover_status = success`
- `captions_status = success`
- `visual_generation_status = blocked`

真实落出的 generation 产物：

- `dist/formal_api_demo/tts/voice_probe.mp3`
- `dist/formal_api_demo/tts/formal_voiceover.mp3`
- `dist/formal_api_demo/script.txt`
- `dist/formal_api_demo/captions.srt`
- `dist/formal_api_demo/visual_generation_plan.json`

generation 最小硬阻塞：

- `image_generation.model`
- `video_generation.model`

### 2. assembly

执行：

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

结果：

- `overall_status = blocked`
- `assembly_status = blocked`
- `assembly_preview_status = success`

真实落出的 assembly 产物：

- `dist/formal_api_demo/assembly/preview_manifest.json`
- `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

assembly 最小硬阻塞：

- `storage.space_name`
- `assembly.template_id`
- `visual_assets_not_ready`

## 最终结论边界

现在可以明确写：

- `formal_api_demo` 已不再只停在 TTS probe
- generation 已真实接上整段配音、字幕和视觉计划
- assembly 已真实接上本地 preview 组装
- 已有第一版本地 preview 视频可复核

现在还不能写：

- “正式云端视频生成已跑通”
- “正式云端 assembly 已跑通”
- “整条 formal_api_demo 正式链路已成功”

## 相关文件

- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `tests/test_formal_api_demo_pipeline.py`
- `dist/formal_api_demo/manifest.json`
- `dist/formal_api_demo/result_summary.json`
- `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
