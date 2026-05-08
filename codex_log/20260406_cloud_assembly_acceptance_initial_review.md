# 20260406_cloud_assembly_acceptance_initial_review

## 本轮目标

- 对任务分支 `codex/round1` 上这次真实 cloud-only assembly 成功导出的成片做一次初检式验收
- 形成脱敏证据、初检结论和是否建议进入正式回流讨论的建议
- 不改代码，不重跑 generation，不默认再次重跑 assembly

## 执行前确认

- 当前目录：`/Users/fan/Documents/视频工厂`
- 当前分支：`codex/round1`
- 当前 HEAD 起点：`12a33a4c107ad5786abf5335432e4ca01a6257cb`
- 当前任务目标：成片初检，不是继续修执行层

## 读取与适用规则

- 已读取：
  - `AGENTS.md`
  - `codex_log/latest.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/04_review_templates.md`
  - `project_source/17_white_collar_ppt_style_rules.md`
  - `formal_api_demo_core.py`
  - `formal_api_demo_cloud_assembly.py`
  - `scripts/assemble_formal_api_demo.py`
  - `dist/formal_api_demo/manifest.json`

## 导出产物确认

- 真实导出记录：
  - `project_id = a139456cf3334509b20192f3203d75bc`
  - `job_id = f45c6af448f44f0794f71ae9f26a1d1e`
  - `media_id = 47b0a400311c71f1a8c3e7f7d45b6302`
  - `output_url = oss://zvip1-video-beijing/video-factory/final/20260405T182130Z/formal_api_demo.mp4`
  - `media_url = https://zvip1-video-beijing.oss-cn-beijing.aliyuncs.com/video-factory/final/20260405T182130Z/formal_api_demo.mp4`
- 由于 bucket 为 private，公开 `media_url` 直接访问返回 `403 Forbidden`
- 本轮使用当前本地凭证生成签名下载链接，把真实导出文件拉到本地验收目录：
  - `dist/formal_api_demo/review_frames/cloud_export_final.mp4`

## 基础技术验收

- 文件存在：是
- 可正常读取：是
- 文件大小：`3602005 bytes`
- 时长：`15.0s`
- 分辨率：`1080x1920`
- 视频流：存在
- 音频流：存在
- 读取方式：
  - 使用本地 `ffmpeg-static`
  - 成功解析视频 / 音频流信息

## 初检证据包

本地证据目录：

- `dist/formal_api_demo/review_frames/`

本轮新增关键证据：

- `cloud_export_final.mp4`
- `frame_start.jpg`
- `frame_middle.jpg`
- `frame_end.jpg`
- `contact_sheet.jpg`

## 初检式验收判断

### 开头 3 秒

- 基本有效
- “流程没拉齐”这一问题点能快速建立语义，不是纯空泛开头

### 中段推进

- 有推进
- 画面从桌面混乱状态进入 SOP 面板，再走到结果板，前后变化可见
- 不属于完全静态轮播

### 字幕 / 配音 / 画面协同

- 从关键帧和导出结构看，字幕落点与画面主信息点基本一致
- 初检层面可判为“基本协同”

### demo 感判断

- 当前仍偏重
- 最明显体现在：
  - 开头桌面物料和大字提示偏工具演示 / 样机感
  - 中段白底 SOP 卡面仍有明显 demo / 样机界面气质
  - 结尾虽然有收束，但整体仍未完全收进“白领咨询报告感 / 体面专业感 / 信息高效感”

### 结尾落点

- 有
- “先稳住样片，再逐轮提质”的方向能被看懂

## 本轮初检结论

- 结论分类：
  - `task_branch_success_but_need_acceptance_fix`
- 当前最高优先级问题层：
  - `画面表现层`
- 原因：
  - 技术导出成功、结构推进成立、前后变化可见
  - 但画面仍带明显 demo / 样机感
  - 现阶段不建议直接进入正式主读取分支回流
- 是否建议进入正式回流讨论：
  - `暂不建议`

## 当前唯一最值下一步

- 先围绕“画面 demo 感偏重”这一最高优先级问题，做一次定向验收修正讨论，再决定是否进入正式回流讨论。

## 本轮仓库状态

- 本轮已更新状态文件并 push 到 `codex/round1`
- 当前分类应为：
  - `task_branch_only`
- 本轮未同步到：
  - `codex/user-readable-map`
