# 20260404_motion_issue_assembly_fps_fix

## 本轮目标

- 只排查《视频工厂》当前样片“有点卡卡的”主因。
- 只判断问题更像来自：
  - generation 段本身
  - 还是 assembly / final 成片阶段
- 若确认是 assembly 问题，只做最小修正，不改文案、不改结构、不重开质量大修。

## 执行前已确认事实

- 当前工作分支：`codex/round1`
- 起始提交：`cd667d951641578e651ea23137d97c0cf3c8e15b`
- 当前仓库存在与本轮无关的用户改动：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
- 本轮目标产物均存在：
  - `dist/formal_api_demo/visual/seg02_video.mp4`
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/assembly/preview_manifest.json`

## 实际读取

- 规则 / 上下文：
  - `AGENTS.md`
  - `codex_log/latest.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 代码：
  - `formal_api_demo_core.py`
  - `video_builder.swift`
  - `tests/test_formal_api_demo_pipeline.py`
  - `config/formal_api_demo.example.toml`
  - `config/formal_api_demo.local.toml`
- 产物 / 清单：
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/assembly/preview_manifest.json`
  - `dist/formal_api_demo/visual/seg02_video.mp4`
  - `dist/formal_api_demo/final.mp4`

## 实际执行

### 1. 技术信息采集

- 用 `mdls` 与临时 Swift 探针读取视频轨道信息、时长和时间点分布。
- `seg02_video.mp4`：
  - 编码：`H.264` + `MPEG-4 AAC`
  - 分辨率：`720x1280`
  - 时长：`6.004329s`
  - 视频时间点：`180`
  - 实际视频帧率：`30 fps`
- 修正前 `final.mp4`：
  - 编码：`H.264` + `MPEG-4 AAC`
  - 分辨率：`1080x1920`
  - 时长：`15.000000s`
  - 全片视频时间点：`150`
  - 实际视频帧率：`10 fps`
  - `seg02` 对应窗（`4.0s-10.0s`）：
    - 视频时间点：`60`
    - 实际视频帧率：`10 fps`

### 2. 连续帧辅助证据

- 导出源 `seg02` 连续帧：
  - `dist/formal_api_demo/review_frames/motion_probe/seg02_source_native_*.png`
  - 时间窗：`2.000s` 起，步长 `1/30s`
- 导出修正前 final 中 `seg02` 连续帧：
  - `dist/formal_api_demo/review_frames/motion_probe/final_seg02_native_*.png`
  - 时间窗：`6.000s` 起，步长 `1/10s`
- 导出修正后 final 中 `seg02` 连续帧：
  - `dist/formal_api_demo/review_frames/motion_probe/final_seg02_native_postfix_*.png`
  - 时间窗：`6.000s` 起，步长 `1/25s`

### 3. 装配逻辑定位

- `video_builder.swift` 的 `buildVideoOnly()` 按 manifest 固定 `fps` 逐帧写出视频。
- `formal_api_demo_core.py` 原逻辑在生成 preview/final manifest 时把 `fps` 硬编码为 `10`。
- 但配置文件实际已写：
  - `config/formal_api_demo.example.toml`：`assembly.fps = 25`
  - `config/formal_api_demo.local.toml`：`assembly.fps = 25`
- 结论：
  - 当前 final 的卡顿不是因为 `seg02` 源视频只有低帧率。
  - 主因是 assembly 侧把 `30 fps` 源素材压成了 `10 fps` 输出。

## 实际改动

- `tests/test_formal_api_demo_pipeline.py`
  - 先补回归断言：`preview_manifest["fps"] == 25`
- `formal_api_demo_core.py`
  - 给 `execute_local_preview_assembly()` 传入现有 `config`
  - preview/final manifest 的 `fps` 改为读取 `assembly.fps`
  - 不再硬编码 `10`

## 实际验证

### TDD 红绿

- 红灯：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_keeps_local_delivery_when_generation_is_still_blocked`
  - 失败信息：`AssertionError: 10 != 25`
- 绿灯：
  - 同一条测试修后通过

### 回归验证

- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `28` 个测试全部通过

### 最小 assembly 重跑

- 通过 `run_assembly_pipeline(...)` 重跑当前 `dist/formal_api_demo` 的本地 assembly
- 新 `preview_manifest.json`：
  - `fps = 25`
- 新 `final.mp4`：
  - 文件大小从约 `4.0M` 升至约 `15M`
  - 全片视频时间点：`375`
  - 全片帧率：`25 fps`
  - `seg02` 对应窗视频时间点：`150`
  - `seg02` 对应窗帧率：`25 fps`

## 当前结果

- 当前主因判断：
  - `assembly_side`
- 不是：
  - `generation_side`
- 本轮最小修正已完成：
  - `10 fps -> 25 fps`
- 当前状态：
  - `motion_fix_passed`

## 当前结果解释

- `seg02` 源片本身是正常的 `30 fps` 视频，不属于“生成段只有低帧率”的问题。
- 当前样片“卡卡的”更像是 final 装配层把源视频时间分辨率压粗了。
- 修正后 final 的 `seg02` 从 `60` 帧提升到 `150` 帧，技术上已经显著更接近源视频的运动连续性。
- 本轮没有改内容结构、文案、镜头规划，也没有开新一轮质量大修。

## `.gitignore` / local_only

- `dist/formal_api_demo/` 属于 `.gitignore` / `local_only`
- 因此以下文件不会上传 GitHub：
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  - `dist/formal_api_demo/review_frames/motion_probe/*`
- 但它们已在本地生成，足以完成当前验收与复审。

## 下一步建议

- 下一轮唯一最关键一步：
  - 直接复审新的 `dist/formal_api_demo/final.mp4`
- 若用户仍感觉 `seg02` 轻微发涩，下一轮只继续做 assembly 侧优化：
  - 更接近源帧率采样
  - 或对 `seg02` 背景视频做直通
- 当前不需要回到文案层或结构层重做。
