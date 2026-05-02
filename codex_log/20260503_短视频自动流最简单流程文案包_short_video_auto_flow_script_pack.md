# 20260503 短视频自动流最简单流程文案包

## 1. 执行范围

- `已确认` 当前工作区：`/Users/fan/Documents/视频工厂`
- `已确认` 当前分支：`codex/short-video-auto-flow-script-pack-20260503`
- `已确认` 本轮只做文案执行包落仓库，不重新创作文案方向，不写教程，不生成视频 / 音频 / 图片。
- `已确认` 标题固定为：《短视频自动流的最简单流程》。

## 2. 已读取关键文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `素材检查_reports/20260503_vNext素材细节复采_vnext_material_detail_recapture/chatgpt_copywriting_input.md`（通过 `origin/codex/vnext-material-detail-recapture-20260503` 只读读取）
- `素材检查_reports/20260503_vNext素材细节复采_vnext_material_detail_recapture/素材细节复采报告_material_detail_recapture_report.md`（通过 `origin/codex/vnext-material-detail-recapture-20260503` 只读读取）
- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/material_inventory.json`（通过 `origin/codex/vnext-recorded-material-intake-20260503` 只读读取）
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`

## 3. 输出文件

- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/01_完整口播稿_full_script.md`
- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/02_分段承载表_block_segment_material_map.md`
- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/03_卡片文案_card_copy.md`
- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/04_执行注意事项_execution_notes.md`
- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/05_给Codex剪辑执行输入_codex_video_execution_input.md`
- `文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/script_pack_manifest.json`

## 4. 关键状态

- `已确认` 完整口播稿已保真保存。
- `已确认` 已补全 block -> segment -> 素材承载表，包含豆包、Trae、Codex 主证据时间码，以及 API / 阿里云剪辑 / 即梦对比 / 总结卡信息卡。
- `已确认` 已补全 7 张卡片文案：流程总览卡、豆包 -> Trae prompt 卡、API 解释卡、阿里云剪辑总装卡、Codex / Claude / Trae 执行层卡、即梦 vs 自动流对比卡、最后总结卡。
- `已确认` 已写清执行注意事项和给后续 Codex 剪辑执行输入。
- `待验证` 后续剪辑执行前必须先由 ChatGPT 复审本执行包。

## 5. 边界

- `已确认` 未生成视频 / 音频 / 图片 / 字幕 / 云端样片。
- `已确认` 未调用阿里云，未创建阿里云任务。
- `已确认` 未修改 v3.1 正片，未修改 `dist/latest_review_pack`。
- `已确认` 未修改 `content_validation`，未修改 `send_ready`。
- `已确认` 未提交素材本体或大媒体文件。
- `已确认` 火山引擎素材未打码前禁止入片；API 段使用信息卡承载。
- `已确认` 阿里云剪辑只写成云端总装方向 / 技术验证候选，不写成正式稳定链路。
- `已确认` Trae 生成项目骨架不等于代码运行成功。
- `已确认` Codex 检查不等于内容过线。

## 6. 下一个目标

ChatGPT 复审本轮文案执行包；复审通过后，再交给后续 Codex 视频执行任务按本包做剪辑执行。
