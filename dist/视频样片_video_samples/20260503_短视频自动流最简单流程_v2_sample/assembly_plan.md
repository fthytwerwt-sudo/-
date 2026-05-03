# 装配计划 assembly_plan

## 1. 样片目标

- `已确认` 本轮只完成《短视频自动流的最简单流程》视频样片 V1。
- `已确认` 样片主线：豆包一句需求 -> 豆包拆流程 -> 豆包生成 Trae prompt -> Trae SOLO plan / 11 待办 -> Trae 项目骨架 -> API 信息卡 -> 云端总装信息卡 -> Codex 检查 -> 即梦对比 -> 总结。
- `已确认` 本轮不把 MP4 生成写成内容过线，不把样片写成可发布。

## 2. 时间线

| order | segment_id | 素材路径 | 时间码 / 时长 | 裁切 / 遮挡 | 能证明什么 | 不能证明什么 |
|---|---|---|---|---|---|---|
| 01 | `flow_overview` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/01_流程总览_flow_overview.png` | 61.14s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 02 | `doubao_simple_need` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 16.00-24.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 03 | `doubao_short_video_plan` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 88.00-120.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 04 | `doubao_to_trae_prompt` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/02_豆包到Trae_prompt_doubao_to_trae_prompt.png` | 66.26s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 05 | `doubao_vlog_prompt_request` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 160.00-176.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 06 | `doubao_copyable_trae_prompt` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 232.00-248.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 07 | `trae_solo_entry` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 32.00-64.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 08 | `trae_prompt_and_plan` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 80.00-112.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 09 | `trae_skeleton` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/03_Trae骨架_trae_skeleton.png` | 73.37s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 10 | `trae_project_skeleton` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 120.00-160.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 11 | `api_explainer` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/04_API解释_api_explainer.png` | 61.14s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 12 | `cloud_assembly` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/05_云端总装_cloud_assembly.png` | 61.14s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 13 | `codex_execution_check` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 176.00-188.00s | crop + mask | 见素材证据链 | 不证明运行成功 / 内容过线 |
| 14 | `codex_check` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/06_Codex检查_codex_check.png` | 61.14s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 15 | `jimeng_compare` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/07_即梦对比_jimeng_compare.png` | 68.26s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |
| 16 | `final_summary` | `/Users/fan/Documents/视频工厂/dist/视频样片_video_samples/20260503_短视频自动流最简单流程_v2_sample/卡片素材_cards/08_最后总结_final_summary.png` | 92.72s | 无 | 流程解释 / 状态边界 | 不证明新增执行事实 |

## 3. 火山引擎 API 段决策

- `已确认` 原素材存在手机号、验证码、API Key 管理页和资源 ID 风险。
- `已确认` 本轮没有使用火山引擎原画面。
- `已确认` API 段使用 `04_API解释_api_explainer.png` 信息卡承载。
- `已确认` redaction result：`redaction_blocked_fallback_to_info_card`。

## 4. 声音 / 字幕

- `audio_validation`：`temporary_preview` 或 `silence_placeholder`，以渲染报告为准。
- `voice_validation`：`pending_user_chatgpt_review`。
- `final_voice_validated`：`false`。
- 字幕文件：`captions.srt`，按 `FINAL_SCRIPT_V2` 段落对齐。
