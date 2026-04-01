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

- 再次只读复核了本地 `config/formal_api_demo.local.toml`，确认当前正式视觉生成 / 云端 assembly 的首层本地字段是否已补齐。
- 复核结果这次没有变化：
  - 已存在且有效：
    - `provider.name`
    - `provider.region`
    - `auth.api_key`
    - `output.dist_dir`
    - `polling.interval_seconds`
    - `polling.timeout_seconds`
  - 仍缺失 / 仍是 placeholder：
    - `image_generation.model`
    - `video_generation.model`
    - `storage.space_name`
    - `assembly.template_id`

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

- 首层阻塞仍是用户本地真实值未补齐：
  - `image_generation.model`
  - `video_generation.model`
  - `storage.space_name`
  - `assembly.template_id`
- `visual_assets_not_ready` 当前仍只是下游阻塞：
  - 它由 `image_generation.model` / `video_generation.model` 未补齐导致
  - 不是独立首层问题
- provider implementation 仍存在，但当前不是用户第一手应先处理的配置阻塞：
  - `image_generation_provider_implementation`
  - `video_generation_provider_implementation`
  - `provider_assembly_implementation`

## 当前最关键的下一步

- 下一轮不要回头再做大范围声音实验。
- 最省事的推进顺序仍是：
  - 先在本地 `config/formal_api_demo.local.toml` 填真实有效的 `image_generation.model`
  - 再填 `video_generation.model`
  - 再填 `storage.space_name`
  - 再填 `assembly.template_id`
- 上述 4 项补齐后，再继续打正式视觉生成 / 云端 assembly。

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
