# 2026-04-03 formal_api_demo 画面层优化 round1

## 本轮目标

- 只推进 `formal_api_demo` 当前本地 preview 的画面层
- 不回头改配音时长
- 不补机制文件
- 不扩 cloud assembly
- 不补视觉模型配置
- 修完后真实重跑 generation + local preview

## 执行前已确认事实

- 当前工作分支是：
  - `codex/user-readable-map`
- 上一轮已确认事实仍成立：
  - `seg01 / seg02 / seg03` 已全部回到各自 slot 内
  - 整段配音约 `14.06s`
  - 本地 preview 仍为 `15.0s`
  - 协同层尾巴已经清干净
- 当前最关键下一步已明确：
  - 切到画面层，降低本地 preview 的 demo / 静态卡片感，尤其第 1 段 hook 的画面表达
- 本轮接手时的仓库事实还有两点必须单列：
  - 当前工作区已经存在未提交的 visual round1 代码改动，集中在：
    - `formal_api_demo_core.py`
    - `video_builder.swift`
    - `tests/test_formal_api_demo_pipeline.py`
  - `codex_log/latest.md` 和本日志草稿在接手时已经写成“画面层 round1 已完成”的口径，但尚未经过我这轮重新核验
- 以仓库事实为准，本轮采用的最小路线是：
  - 不再扩散代码范围
  - 直接沿用当前工作区已有的 visual round1 改动
  - 真实重跑 generation + assembly
  - 再用产物和静帧做画面层双审核

## 当前画面层最小问题确认

- 当前 demo 感最主要来自：
  - 旧 preview 的信息卡表达过于“本地演示页”
  - 第 1 段 hook 首屏虽然已不是旧 demo 字段结构，但仍容易显得太平
  - 第 2 段更像在静态说明流程，而不是让人看见“散乱 -> SOP”的变化
- 当前最小可行路线是：
  - 去掉显式 demo / 本地预览标识
  - 强化第 1 段 hook 的首屏冲突表达
  - 让三页分工更清楚，至少更像短视频 preview，而不是统一卡片模板

## 实际改动

### 接手时已存在且本轮沿用的画面层改动

- `formal_api_demo_core.py`
  - preview slide 数据已从旧的 `title/body/badge/footer` 结构切到：
    - `sequence`
    - `total`
    - `role`
    - `eyebrow`
    - `headline`
    - `support`
    - `detail`
    - `chips`
  - 三页角色已明确为：
    - `hook`
    - `process`
    - `outcome`
- `video_builder.swift`
  - 已去掉显式 `PPT Demo / formal_api_demo / 本地预览` 标签
  - 本地 preview 已改成“主句 + 支撑句 + 角色化卡片”的布局
  - 第 1 段已是“想法很多 / 流程没拉齐”的冲突对比卡
  - 第 2 段已是目标 / 输入 / 输出步骤卡
  - 第 3 段已是结果 / 下一步收束卡
  - 已补上底部轻量进度动效
- `tests/test_formal_api_demo_pipeline.py`
  - 已增加 preview manifest 结构回归检查：
    - 第一页必须是 `hook`
    - 第二页必须是 `process`
    - 第三页必须是 `outcome`
    - slide 数据里不再允许旧的 `badge` / `footer`

### 本轮新增收口改动

- 更新 `codex_log/latest.md`
- 重写本日志，使其与这轮真实重跑结果一致

## 实际执行

### 1. 真实重跑 generation

- 执行：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 结果：
  - `overall_status = blocked`
  - `generation_status = blocked`
  - `voiceover_status = success`
  - `captions_status = success`
  - `visual_generation_status = blocked`
- 当前阻塞仍是：
  - `image_generation_model`
  - `video_generation_model`

### 2. 真实重跑 assembly

- 执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 结果：
  - `assembly_status = success`
  - `local_assembly_status = success`
  - `assembly_preview_status = success`
  - 本地 preview 已重新生成

### 3. 回归测试

- 执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 结果：
  - `Ran 21 tests`
  - `OK`

### 4. 产物核验

- 已确认以下文件存在且非空：
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  - `dist/formal_api_demo/result_summary.json`
  - `dist/formal_api_demo/assembly/preview_manifest.json`
- 已确认关键时长：
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`：`14.064s`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`：`15.0s`

### 5. 静帧复审

- 额外执行了精确抽帧，分别核对：
  - `seg01` hook 首屏
  - `seg02` process 首屏
  - `seg03` outcome 首屏
- 目的：
  - 避免只看代码脑补画面效果
  - 直接依据样片静帧判断 hook 是否更有效、页级层次是否成立

## 产物路径

- 脚本：`dist/formal_api_demo/script.txt`
- 字幕：`dist/formal_api_demo/captions.srt`
- 整段配音：`dist/formal_api_demo/tts/formal_voiceover.mp3`
- preview manifest：`dist/formal_api_demo/assembly/preview_manifest.json`
- 本地样片：`dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
- 结果摘要：`dist/formal_api_demo/result_summary.json`

## 执行审核结论

- 本轮真实改动文件范围是：
  - 已沿用并核验的代码改动：
    - `formal_api_demo_core.py`
    - `video_builder.swift`
    - `tests/test_formal_api_demo_pipeline.py`
  - 本轮新增收口：
    - `codex_log/latest.md`
    - 本日志
- 本轮真实执行了：
  - generation 重跑
  - assembly 重跑
  - 全量单测
  - preview 抽帧复审
- 本轮已重新产出 preview：
  - `是`
- 当前状态判定：
  - `已完成`

说明：

- 对本轮唯一目标“本地 preview 画面层优化 round1”来说，已经完成
- `formal_api_demo` 整体 pipeline 仍因视觉模型缺失保持 `blocked`，但那不是本轮目标，也不是本轮剩余执行问题

## 质量审核结论

- 本轮只审“画面层”
- 当前主结论：
  - 画面层已经明显比上一轮更不像 demo，但仍未到接近正式样片的程度

### 1. 当前画面是否比上一轮更不像 demo

- `是`
- 证据：
  - 显式 `PPT Demo / formal_api_demo / 本地预览` 标识已经去掉
  - 页面不再是统一的演示模板页
  - 三页已分成问题 / 动作 / 结果三种角色

### 2. 第 1 段 hook 画面是否更有效

- `是`
- 证据：
  - 首屏现在直接打主句
  - 并用 `想法很多` vs `流程没拉齐` 的冲突对比卡承接文案
  - 比上一轮更容易在 3 秒内读懂“卡点在哪里”

### 3. 页面层级 / 切换是否更像短视频 preview

- `是，但还只是 round1`
- 证据：
  - headline / support / 信息卡层级已经分开
  - 底部进度动效让切页不再完全静止
  - 第 2 / 第 3 页的视觉职责已分开，不再全都像同一种说明卡

### 4. 当前仍残留的最大画面问题是什么

- 当前最大问题仍在：
  - `seg02`
- 具体表现：
  - 这页现在只是更好看的步骤卡
  - 还没有真正把“散乱 -> 收束”画出来
  - 所以中段仍带着较强的信息说明感

### 5. 如果下一轮只能再改一个点，画面层最该继续改什么

- 继续只改一个点的话，最值的是：
  - 让 `seg02` 真正出现从散乱便签 / 信息块到 SOP 流程卡的动态变化

## 当前最大画面问题

- `seg02` 仍然在“说明流程”，而不是“让人看见流程被收束”

## 下一轮唯一最优先改点

- 让 `seg02` 的“散乱 -> SOP”变化可视化，优先用页内元素重排或前后状态切换来承接中段动作

## 仓库事实冲突说明

- 本轮接手时，`codex_log/latest.md` 和本日志草稿已经提前写成“画面层 round1 已完成”的口径
- 但这些内容在接手时还没有经过我这轮重跑核验
- 因此本轮以仓库事实为准：
  - 沿用当前工作区已有未提交代码改动
  - 用 fresh 的 generation / assembly / unittest / 抽帧结果重新收口
- 最终保留的是这轮核验后的结果，而不是接手时的草稿口径
