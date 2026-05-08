# 2026-04-02 formal_api_demo 双审核 round1

## 本轮目标

- 回到《视频工厂》视频主线
- 在当前 `formal_api_demo` 主链基础上真实重跑一轮本地出片
- 落出一版本地可审样片
- 做一轮执行审核 + 质量审核
- 不继续补机制文件，不继续扩 `project_source/`

## 执行前已确认事实

- 当前正式主路径仍是：
  - 文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传
- 当前代码 / 测试 / 配置口径已经统一为：
  - generation 继续接 API
  - local assembly 默认交付
  - cloud assembly 是 optional / skipped
  - 缺 `image_generation.model` / `video_generation.model` 时，generation 继续记 `blocked`
- 本地 `formal_api_demo.local.toml` 现状：
  - TTS 所需字段已存在
  - `image_generation.model` / `video_generation.model` 仍缺
  - `storage.space_name` / `assembly.template_id` 仍缺
- 上述事实说明：
  - 这轮最值的是先直接重跑现有本地主链
  - 不需要先改代码才能知道当前真实状态

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `project_source/00_project_brief.md`
- `project_source/04_review_templates.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `codex_log/20260402_formal_api_demo_generation_and_assembly.md`
- `codex_log/20260402_formal_api_demo_local_assembly_default_generation_required.md`
- `codex_log/20260402_formal_api_demo_local_first_delivery.md`
- `codex_log/20260402_formal_api_demo_latest_alignment.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `cases/formal_api_demo.md`
- `video_builder.swift`

## 实际改动

### 代码 / 脚本 / 配置

- 本轮没有改：
  - `formal_api_demo_core.py`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `config/formal_api_demo.example.toml`

### 日志

- 更新 `codex_log/latest.md`
- 新增本日志，记录本轮真实执行和双审核结果

## 实际执行

### 1. 执行前安全检查

- 只读确认本地配置字段是否存在，不回显真实 secret
- 结果：
  - 已有：`provider.region`、`auth.api_key`、`tts.voice`、`tts.model`
  - 仍缺：`image_generation.model`、`video_generation.model`、`storage.space_name`、`assembly.template_id`

### 2. generation

执行命令：

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

真实结果：

- `overall_status = blocked`
- `generation_status = blocked`
- `tts_probe_status = success`
- `voiceover_status = success`
- `captions_status = success`
- `visual_generation_status = blocked`
- `blocked_reason = 缺少视觉生成前提：image_generation_model、video_generation_model`

### 3. assembly

执行命令：

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

真实结果：

- `overall_status = blocked`
- `generation_status = blocked`
- `assembly_status = success`
- `local_assembly_status = success`
- `cloud_assembly_status = blocked`
- `assembly_preview_status = success`
- `blocked_reason = 缺少本地组装前提：visual_assets_not_ready`

### 4. 产物核验

已确认以下文件真实存在且非空：

- `dist/formal_api_demo/script.txt`
- `dist/formal_api_demo/captions.srt`
- `dist/formal_api_demo/tts/formal_voiceover.mp3`
- `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- `dist/formal_api_demo/assembly/preview_manifest.json`
- `dist/formal_api_demo/result_summary.json`

### 5. 元数据核验

- `formal_voiceover.mp3` 实际时长约：`18.22s`
- `formal_api_demo_preview.mp4` 实际时长：`15.0s`
- 三段配音单段时长均超出时间预算：
  - `seg01`：计划 `4.0s`，实际约 `5.11s`
  - `seg02`：计划 `6.0s`，实际约 `7.25s`
  - `seg03`：计划 `5.0s`，实际约 `5.81s`
- `video_builder.swift` 当前会在导出时取 `CMTimeMinimum(videoAsset.duration, audioAsset.duration)`，所以本轮 preview 会按 15 秒视频时长截掉更长的配音

## 产物路径

- 脚本：`dist/formal_api_demo/script.txt`
- 字幕：`dist/formal_api_demo/captions.srt`
- 整段配音：`dist/formal_api_demo/tts/formal_voiceover.mp3`
- 本地样片：`dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 本地样片清单：`dist/formal_api_demo/assembly/preview_manifest.json`
- 结果摘要：`dist/formal_api_demo/result_summary.json`

## 执行审核结论

### 本轮真实做到了什么

- 按当前仓库事实重新跑了一轮 `formal_api_demo`
- generation 没崩，真实落出了：
  - 脚本
  - 字幕
  - 整段配音
- assembly 没崩，真实落出了一版本地 preview mp4
- 当前阻塞没有散着写，已经压到最小点：
  - `image_generation.model`
  - `video_generation.model`

### 本轮没做到什么

- 没有让 generation 进入 success
- 没有让整体 `overall_status` 进入 success
- 没有补齐真实图片 / 视频生成 API 配置
- 没有让 cloud assembly 成立

### 本轮卡在哪

- 当前最小执行阻塞仍在 generation 前提层：
  - 本地配置缺 `image_generation.model`
  - 本地配置缺 `video_generation.model`
- 当前不是代码坏掉，也不是 assembly 跑不动

### 当前执行状态判定

- `部分完成`

理由：

- 本地可审样片已真实产出
- 但整体状态仍 blocked，正式 generation 前提未补齐

## 质量审核结论

### 1. 脚本是否像短视频，而不是说明书 / 项目汇报

- `部分成立`
- 开头有短视频式问题抛出，但中段仍偏抽象说明，像“方法说明”多于“真实案例冲突推进”

### 2. 开头 3 秒是否有效

- `有一定作用，但不够强`
- “很多 AI 项目不是做不动，而是说不清”能立住问题，但还不够具体，不是强钩子

### 3. 配音是否还有明显系统播报感

- `当前环境下不能给出已过线结论`
- 本轮没有新增听感优化，仍沿用旧 A 基线；再叠加配音时长超线，当前只能判断“仍有系统播报 / 匀速播读风险”，不能判已过线

### 4. 字幕 / 配音 / 画面是否基本协同

- `当前未过线`
- 证据：
  - 配音总时长 `18.22s`
  - 样片总时长 `15.0s`
  - 三段配音都超出各自计划时长
  - 当前 preview 合成会裁掉更长音频
- 这意味着本轮样片即使能看，也已经存在明显节奏失真和结尾被截断风险

### 5. 当前画面是否还有 demo 感

- `明显有`
- 当前 preview 仍是静态卡片轮播，且显式带：
  - `PPT Demo`
  - `formal_api_demo / 本地预览`
- 画面层仍符合“本地预览 / demo 样片”，不符合“接近可发布测试版”

### 6. 前后变化是否可见

- `文案层有，画面层不够`
- 文案在说“散乱 -> SOP -> 稳定样片”，但画面仍主要是信息卡切页，变化感偏概念，不够可视化

### 7. 结尾是否有落点

- `文案有落点，但样片层不稳`
- 结尾文案本身有“先稳定样片，再修正”的落点，但当前配音超时，结尾表达可能被截断

### 8. 当前是否达到“可发布测试水位”

- `未达到`

### 质量收口

- 当前最大问题层：
  - `字幕 / 配音 / 画面协同层`
- 当前最大质量问题不是 cloud assembly，也不是“缺视觉模型”本身，而是：
  - 现有 15 秒时间线和实际配音长度不匹配，导致本地样片协同失真

## 当前最大问题层

- `字幕 / 配音 / 画面协同层`

## 下一轮唯一最优先改点

- 先把整段配音和 15 秒 timeline 压齐

原因：

- 这是当前最直接、最可验证、且最影响质量判断准确性的单点
- 如果不先对齐时长，后续继续审画面或继续补视觉素材，都会被当前被截断的声画关系干扰
- 视觉 demo 感仍重，但它是下一层问题，不是本轮唯一最值改点

## 当前结果

- 本轮已真实产出一版本地可审样片
- 该样片可作为首轮质量审核输入
- 当前整体状态仍是 `blocked`
- 当前阻塞最小点已压清到本地视觉模型配置缺失
- 当前质量最大问题已压清到字幕 / 配音 / 画面协同层

## 下一步建议

- 下一轮不要继续补机制文件
- 下一轮如果只做一个动作：
  - 优先把配音时长压回 15 秒时间线内，并重跑 preview
