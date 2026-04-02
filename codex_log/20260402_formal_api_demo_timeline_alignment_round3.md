# 2026-04-02 formal_api_demo 时间线对齐 round3

## 本轮目标

- 只修 `formal_api_demo` 当前 `seg01 / seg02` 仍轻微超预算的问题
- 不补机制文件
- 不扩 cloud assembly
- 不补视觉模型配置
- 修完后真实重跑 generation + local preview

## 执行前已确认事实

- 上一轮真实结果：
  - 整段配音约 `14.66s`
  - `seg01` 约 `4.10s`，预算 `4.0s`
  - `seg02` 约 `6.07s`，预算 `6.0s`
  - `seg03` 约 `4.44s`，预算 `5.0s`
- 当前主问题已不是整段超时，而是：
  - `seg01 / seg02` 还有轻微单段超预算尾巴
- 当前 generation / local assembly / cloud assembly 口径不需要这轮再改

## 实际改动

### 1. `cases/formal_api_demo.md`

- 只继续微缩 `seg01 / seg02` 文案：
  - `seg01`
    - 从：`AI 项目卡住，常常不是没思路，是流程没理清。`
    - 收成：`AI 项目卡住，不是没思路，是流程还没拉齐。`
  - `seg02`
    - 从：`先把目标、输入、输出压成 SOP，再让生成和组装按这份事实执行。`
    - 收成：`先把目标、输入、输出压成 SOP，再让生成和组装按流程跑。`

### 2. `tests/test_formal_api_demo_pipeline.py`

- 继续收紧当前 case 的预算测试：
  - `seg01` 预算从 `23` 再收紧到 `22`
  - `seg02` 保持 `29`
  - `seg03` 保持 `23`

### 3. 日志

- 更新 `codex_log/latest.md`
- 新增本日志

## 实际执行

### 1. 现有测试检查

- 先运行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
- 结果：
  - `OK`
- 说明：
  - 上一轮字符预算测试不足以直接暴露 `seg01 / seg02` 的真实单段尾巴

### 2. 真实时长复核

- 直接核对上一轮产物时长：
  - `segment_seg01.mp3`：`4.10s`
  - `segment_seg02.mp3`：`6.07s`
  - `segment_seg03.mp3`：`4.44s`
  - `formal_voiceover.mp3`：`14.66s`
- 由此确认：
  - 当前尾巴是真实存在，不是聊天复述

### 3. 第一次红灯 → 绿灯

- 先把测试预算收紧到 `seg01=23`、`seg02=29`
- 红灯：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
  - 结果：`seg01` 失败
- 修改第一次 case 文案后回绿：
  - 同一命令
  - 结果：`OK`

### 4. 第一次真实重跑

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 重跑后真实发现：
  - `seg02` 已回到预算内
  - 但 `seg01` 虽然字数更短，真实时长反而到了 `4.44s`
- 由此确认：
  - 根因不只看字数，句式停顿也会显著影响 TTS 时长

### 5. 候选句真实预跑

- 用临时 case 对 `seg01` 做真实 TTS 预跑，得到关键候选：
  - `项目卡住，往往不是没思路，是流程没理顺。` → `3.94s`
  - `项目卡住，不是没思路，是流程还没理顺。` → `3.77s`
  - `AI 项目卡住，不是没思路，是流程还没拉齐。` → `3.94s`
- 最终保留：
  - `AI 项目卡住，不是没思路，是流程还没拉齐。`
- 原因：
  - 保住了 `AI 项目` 语境
  - 同时已真实压回 `4.0s` 内

### 6. 第二次红灯 → 绿灯

- 再把 `seg01` 测试预算从 `23` 收紧到 `22`
- 红灯：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_formal_case_voiceover_copy_stays_within_current_timeline_budget`
  - 结果：`seg01` 失败
- 修改正式 case 后回绿：
  - 同一命令
  - 结果：`OK`

### 7. 最终真实重跑

- `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 回归测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 21 tests`，`OK`

## 新旧单段时长对比

### 以 round2 作为本轮起点

- `seg01`
  - 旧：`4.10s`
  - 新：`3.94s`
  - 预算：`4.0s`
  - 当前余差：`-0.06s`
- `seg02`
  - 旧：`6.07s`
  - 新：`5.64s`
  - 预算：`6.0s`
  - 当前余差：`-0.36s`
- `seg03`
  - 旧：`4.44s`
  - 新：`4.44s`
  - 预算：`5.0s`
  - 当前余差：`-0.56s`

### 整段与 preview

- `formal_voiceover.mp3`
  - 旧：`14.66s`
  - 新：`14.06s`
- `formal_api_demo_preview.mp4`
  - 旧：`15.0s`
  - 新：`15.0s`

## 产物路径

- 配音总轨：`dist/formal_api_demo/tts/formal_voiceover.mp3`
- 分段配音：
  - `dist/formal_api_demo/tts/segment_seg01.mp3`
  - `dist/formal_api_demo/tts/segment_seg02.mp3`
  - `dist/formal_api_demo/tts/segment_seg03.mp3`
- 本地样片：`dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 结果摘要：`dist/formal_api_demo/result_summary.json`

## 执行审核结论

- 本轮真实改了：
  - `cases/formal_api_demo.md`
  - `tests/test_formal_api_demo_pipeline.py`
  - `codex_log/latest.md`
  - 本日志
- 本轮真实执行了：
  - 现有测试检查
  - 两次红灯 → 绿灯
  - 两轮 generation 重跑
  - 两轮 assembly 重跑
  - 一轮临时 case 候选预跑
  - 全量单测
- 本轮已重新产出 preview
- 当前状态判定：
  - `已完成`

说明：

- 对本轮唯一目标“让 seg01 / seg02 都完全回到各自 slot 内并重跑 preview”来说，已经完成
- `formal_api_demo` 整体 pipeline 仍因视觉模型缺失保持 `blocked`，但那不是本轮目标，也不是本轮剩余问题

## 质量审核结论

- 本轮只审“协同层尾巴是否清干净”
- 当前主结论：
  - 协同层尾巴已经清干净
- 具体判断：
  - 段内节奏：比上一轮更贴合，`seg01 / seg02 / seg03` 都回到了各自 slot 内
  - 是否仍存在轻微协同尾巴：当前不再存在“单段超预算”导致的明显尾巴
  - 结尾是否仍受时长影响：当前不再受单段或整段时长超线影响

## 下一轮唯一最优先改点

- 协同层尾巴清掉后，下一轮如果只改一个点，优先切到画面层：
  - 降低当前本地 preview 的 demo / 静态卡片感，尤其是第 1 段 hook 的画面表达
