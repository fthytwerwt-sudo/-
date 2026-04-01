# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- `formal_api_demo` 当前主路径已切到“本地优先出片”：
  - generation 会真实落出脚本、整段配音、字幕和视觉计划
  - local assembly 会真实落出本地 mp4
  - cloud visual generation / cloud assembly 已降级为可选增强项
  - 未配置 `storage.space_name` / `assembly.template_id` 不再把整条链路压成失败

## 最近一次完成了什么

- 改了 `formal_api_demo` 的状态口径：
  - `generation`
  - `local_assembly`
  - `cloud_assembly`
  - `overall_status`
- 把 cloud assembly 从当前阶段硬阻塞改成可选增强项：
  - 未配置云端字段时，`cloud_assembly = skipped`
  - 只要本地 generation 成功且本地 assembly 成功，`overall_status = success`
- 把本地 mp4 明确抬成当前默认交付件：
  - `manifest.assembly.delivery_video_path`
  - `result_summary.artifact_paths.final_video`
  - 当前都指向 `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 真实执行已完成：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

## 当前已确认事实

- 当前真实状态：
  - `manifest.current_status = success`
  - `manifest.status_summary = {"generation":"success","local_assembly":"success","cloud_assembly":"skipped","overall_status":"success"}`
  - `result_summary.overall_status = success`
  - `result_summary.local_assembly_status = success`
  - `result_summary.cloud_assembly_status = skipped`
- 当前本地默认交付件已真实落出：
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 当前 cloud 增强项仍未接入：
  - `cloud_visual_generation_status = skipped`
  - `cloud_assembly_status = skipped`

## 当前最关键的下一步

- 不要再把 `storage.space_name` / `assembly.template_id` 当成本地主线硬前置。
- 下一步最值的是继续提升本地成片质量：
  - 收口 `video_builder.swift` 的视觉呈现质量
  - 再决定是否回头接 cloud visual generation / cloud assembly

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- 若继续推进 `formal_api_demo`：
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/result_summary.json`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
