# 2026-04-02 formal_api_demo 时间线对齐 round2

## 本轮目标

- 只修 `formal_api_demo` 当前本地样片里的“配音时长 > 15 秒时间线”问题
- 不补机制文件
- 不扩 cloud assembly
- 不补视觉模型配置
- 修完后真实重跑 generation + local preview

## 执行前已确认事实

- 上一轮真实结果：
  - `formal_voiceover.mp3` 约 `18.22s`
  - `formal_api_demo_preview.mp4` 为 `15.0s`
  - preview 当前会按较短视频时长截掉更长音频
- 当前最大问题层已明确是：
  - `字幕 / 配音 / 画面协同层`
- 当前正式主路径、generation / local assembly / cloud assembly 口径都不需要这轮再改

## 实际改动

### 1. `cases/formal_api_demo.md`

- 只缩短了三段配音 / 字幕文案，保留原意不变：
  - 第 1 段从“不是没思路，而是需求、步骤和结果始终说不清”
    收成“不是没思路，是流程说不清”
  - 第 2 段从“目标、输入、步骤、输出压成统一结构，再让后续生成和组装按同一份事实执行”
    收成“目标、输入、输出压成 SOP，再让生成和组装按这份事实执行”
  - 第 3 段从“先稳定出样片，再用复审和修正循环把质量逼近正式水位”
    收成“先稳住样片，再把质量逐轮压到正式水位”

### 2. `tests/test_formal_api_demo_pipeline.py`

- 新增当前 case 的时间线预算回归测试：
  - `test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
- 先看红灯，再改 case，再看绿灯

### 3. 日志

- 更新 `codex_log/latest.md`
- 新增本日志

## 实际执行

### 1. 红灯验证

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
  - 初次运行失败
  - 失败点：`seg01` 文案长度超当前 15 秒预算

### 2. 绿灯验证

- 修改 `cases/formal_api_demo.md` 后再次运行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
  - 结果：`OK`

### 3. 真实重跑 generation

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

真实结果：

- `overall_status = blocked`
- `generation_status = blocked`
- `voiceover_status = success`
- 新整段配音已重新生成

### 4. 真实重跑 assembly

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`

真实结果：

- `assembly_status = success`
- `local_assembly_status = success`
- `assembly_preview_status = success`
- 本地 preview 已重新生成

### 5. 回归测试

- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 21 tests`
  - `OK`

## 新旧时长对比

### 整段时长

- 旧 `formal_voiceover.mp3`：约 `18.22s`
- 新 `formal_voiceover.mp3`：约 `14.66s`
- 旧 `formal_api_demo_preview.mp4`：`15.0s`
- 新 `formal_api_demo_preview.mp4`：`15.0s`

### 单段时长

- `seg01`
  - 旧：约 `5.11s`
  - 新：约 `4.10s`
  - 预算：`4.0s`
  - 当前余差：`+0.10s`
- `seg02`
  - 旧：约 `7.25s`
  - 新：约 `6.07s`
  - 预算：`6.0s`
  - 当前余差：`+0.07s`
- `seg03`
  - 旧：约 `5.81s`
  - 新：约 `4.44s`
  - 预算：`5.0s`
  - 当前余差：`-0.56s`

## 产物路径

- 脚本：`dist/formal_api_demo/script.txt`
- 字幕：`dist/formal_api_demo/captions.srt`
- 整段配音：`dist/formal_api_demo/tts/formal_voiceover.mp3`
- 本地样片：`dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 结果摘要：`dist/formal_api_demo/result_summary.json`

## 执行审核结论

- 本轮真实改了：
  - `cases/formal_api_demo.md`
  - `tests/test_formal_api_demo_pipeline.py`
  - `codex_log/latest.md`
  - 本日志
- 本轮真实执行了：
  - 红灯测试
  - 绿灯测试
  - generation 重跑
  - assembly 重跑
  - 全量单测
- 本轮已重新产出 preview
- 配音时长已压下来了，而且已经回到 `15s` 时间线内
- 当前状态判定：
  - `已完成`

说明：

- 对本轮唯一目标“整段配音压回 15 秒内并重跑 preview”来说，已经完成
- `formal_api_demo` 整体 pipeline 仍因视觉模型缺失保持 `blocked`，但那不是本轮目标，也不是这轮剩余主阻塞

## 质量审核结论

- 本轮只审协同层
- 当前主结论：
  - 协同层比上一轮明显更稳
- 具体判断：
  - 字幕 / 配音 / 画面协同：比上轮更稳，整段截断主问题已解除
  - 结尾是否仍被截断：当前看不再是“整段超时导致结尾被硬截断”
  - 是否仍有明显节奏失真：仍有轻微残余，主要在 `seg01` 和 `seg02` 的单段边界
- 如果下一轮只能再改一个点：
  - 继续把第 1 / 第 2 段各再收短一点，彻底消掉单段轻微超预算

## 下一轮唯一最优先改点

- 继续收第 1 / 第 2 段单段时长，让每段都完全回到各自 slot 内
