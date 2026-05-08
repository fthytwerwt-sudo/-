# 20260406_visual_pass_conservative

## 本轮目标

- 在 `codex/round1` 成功导出的 pure PPT / 信息卡 cloud-only 成片基础上
- 做一轮“保守型画面修正”
- 尽量少改结构和内容，只压掉最明显的 demo / 样机感
- 产出一个更稳、更体面、更接近正式样片的候选版成片

## 当前工作分支

- `codex/round1-visual-pass-conservative`

## 执行前确认

- 当前目录：`/Users/fan/Documents/视频工厂`
- 当前分支起点：`8a462a2885c5df148c8a72ba87a2f35245696e07`
- 本地仓库 `skills/`：不存在
- 本轮沿用全局：
  - `systematic-debugging`
  - `verification-before-completion`

## 本轮读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_log/20260406_cloud_assembly_acceptance_initial_review.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/04_review_templates.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/17_white_collar_ppt_style_rules.md`
- `dist/formal_api_demo/review_frames/`
- `video_builder.swift`
- `dist/formal_api_demo/assembly/preview_manifest.json`

## 本轮只修的视觉点

### 1. 开头首屏的工具演示感

- 原问题：
  - 桌面图里的红色问题字样过于抢眼
  - 叠层结构更像工具演示稿，而不是体面专业的信息卡
- 保守修法：
  - 在 hook 页改成大面积柔和信息卡面板
  - 减少强对比的小黑白块和箭头式 UI 感
  - 改成更克制的标题 / 支撑句 / chips 层级

### 2. 中段白底 SOP 卡面的 demo 感

- 原问题：
  - 当前转场页像“在演示一个界面”
  - 文字容器太像功能讲解层
- 保守修法：
  - 改成右侧更克制的结构说明卡
  - 保留底层视频推进，但把说明层收窄成“咨询式说明卡”

### 3. 结尾页的专业收束感

- 原问题：
  - 结尾虽然有落点，但 banner / box 组合仍偏样机感
- 保守修法：
  - 改成更轻的收束型白色面板
  - 保留“先做什么 / 再做什么”逻辑，但降低 demo 感

## 本轮实际修改

- `video_builder.swift`
  - 只修改了与画面表现层直接相关的 3 个媒体背景 overlay：
    - `drawHookOverlay`
    - `drawTransitionLayout`
    - `drawOutcomeOverlay`
  - 未修改：
    - `formal_api_demo_core.py`
    - `formal_api_demo_cloud_assembly.py`
    - generation / assembly 主链逻辑

## 新候选成片

- 本地候选成片：
  - `dist/formal_api_demo_visual_pass_conservative/final.mp4`
- 本地渲染中间产物：
  - `dist/formal_api_demo_visual_pass_conservative/assembly/formal_api_demo_preview.mp4`
- 候选成片技术信息：
  - 时长：`15.0s`
  - 分辨率：`1080x1920`
  - 文件大小：`15922005 bytes`
  - 视频流：存在
  - 音频流：存在

## 新证据包

- 证据目录：
  - `dist/formal_api_demo_visual_pass_conservative/review_frames/`
- 关键证据：
  - `frame_start.jpg`
  - `frame_middle.jpg`
  - `frame_end.jpg`
  - `contact_sheet.jpg`

## 一句话自检

- demo 感已明显下降，整体更接近“白领咨询报告感 / 体面专业感 / 信息高效感”，但首屏背景里红色问题字样仍稍重，当前仍不建议直接进入正式主读取分支回流。

## 本轮仓库状态

- 本轮已更新状态文件并 push 到：
  - `codex/round1-visual-pass-conservative`
- 当前状态分类：
  - `task_branch_only`
- 本轮未同步到：
  - `codex/user-readable-map`
