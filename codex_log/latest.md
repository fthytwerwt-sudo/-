# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- `formal_api_demo` 已不再只停在阿里 TTS 子线：
  - 阿里百炼 TTS probe 已接通
  - 正式链路默认继续沿用旧 A 作为可用 TTS 基线
  - generation 已真实落出整段配音、脚本、字幕和视觉计划
  - assembly 已真实落出本地 preview 样片
  - 但正式云端视频生成 / 云端 assembly 仍未跑通

## 最近一次完成了什么

- 按“字段有效就立刻执行、无效就立即停下”的口径，再次只读检查了本地 `config/formal_api_demo.local.toml`。
- 这次结论比上一轮更收紧：
  - `image_generation.model`：无效
  - `video_generation.model`：无效
  - `storage.space_name`：无效
  - `assembly.template_id`：无效
- 进一步确认到：
  - 这 4 个键在 local config 里都“存在”
  - 但当前解析后的值仍落在“空值 / placeholder”判定里
  - 因此本轮没有继续硬跑正式 generation / 云端 assembly

## 当前已确认事实

- generation 现状未变：
  - `generation.tts_probe.status = success`
  - `generation.voiceover.status = success`
  - `generation.captions.status = success`
  - `generation.visual_generation.status = blocked`
- assembly 现状未变：
  - `assembly.status = blocked`
  - `assembly.preview.status = success`
- 当前本地 preview 仍可用：
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`

## 当前最小硬阻塞

- 当前首层阻塞已经压到这 4 个字段本身：
  - `image_generation.model`
  - `video_generation.model`
  - `storage.space_name`
  - `assembly.template_id`
- 这轮不再展开写更后层 provider implementation / `visual_assets_not_ready`，因为还没到那一层

## 当前最关键的下一步

- 下一轮不要回头再做大范围声音实验。
- 最先该做的是重新检查本地 `config/formal_api_demo.local.toml` 里这 4 个字段的实际值格式，确保它们不再被当前解析逻辑判成空值或 placeholder。
- 只有这 4 项都变成有效值后，再继续打正式视觉生成 / 云端 assembly。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- 若继续推进 `formal_api_demo` 正式链路：
  - `config/formal_api_demo.local.toml`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/result_summary.json`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
