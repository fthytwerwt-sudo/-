# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- `formal_api_demo` 已不再只停在阿里 TTS 子线：
  - 阿里百炼 TTS probe 仍已接通
  - 正式链路默认继续沿用旧 A 作为可用 TTS 基线
  - generation 已真实落出整段配音、脚本、字幕和视觉计划
  - assembly 已真实落出本地 preview 样片
  - 但正式云端视频生成 / 云端 assembly 还没有跑通

## 最近一次完成了什么

- 修改了 `formal_api_demo_core.py`，把 `formal_api_demo` 从“TTS probe only”推进到：
  - TTS probe
  - 整段配音 `formal_voiceover.mp3`
  - `script.txt`
  - `captions.srt`
  - `visual_generation_plan.json`
  - assembly 本地 preview 输出
- 更新了：
  - `config/formal_api_demo.example.toml`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `tests/test_formal_api_demo_pipeline.py`
- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

## 当前已确认事实

- generation 真实结果：
  - `generation.status = blocked`
  - `generation.tts_probe.status = success`
  - `generation.voiceover.status = success`
  - `generation.captions.status = success`
  - `generation.visual_generation.status = blocked`
- assembly 真实结果：
  - `assembly.status = blocked`
  - `assembly.preview.status = success`
- 已真实落出：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/visual_generation_plan.json`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

## 当前最小硬阻塞

- 视频生成层当前最小硬阻塞：
  - `image_generation.model`
  - `video_generation.model`
- assembly 云端层当前最小硬阻塞：
  - `storage.space_name`
  - `assembly.template_id`
  - `visual_assets_not_ready`
- 还要明确：
  - 当前本地 preview 样片已经跑出
  - 但这不能写成“正式云端视频链路已跑通”

## 当前最关键的下一步

- 下一轮不要回头再做大范围声音实验。
- 最省事的推进顺序是：
  - 先在本地 `config/formal_api_demo.local.toml` 补齐 `image_generation.model` 与 `video_generation.model`
  - 再补 `storage.space_name` 与 `assembly.template_id`
  - 然后继续打正式视觉生成 / 云端组装

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- 若继续推进 `formal_api_demo` 正式链路：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/result_summary.json`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
