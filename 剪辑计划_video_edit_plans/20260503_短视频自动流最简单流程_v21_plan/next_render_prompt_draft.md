# next_render_prompt_draft｜短视频自动流 V2.1 下一轮渲染执行单草稿

> 只写草稿，不执行渲染。

## Goal（目标）

基于已审核通过的 V2.1 计划包，生成《短视频自动流的最简单流程》流程证明型技术样片 V2.1。

## Context（上下文）

- 必须先读取计划包目录：
  `/Users/fan/Documents/视频工厂/剪辑计划_video_edit_plans/20260503_短视频自动流最简单流程_v21_plan/`
- PR #41 只能作为失败样本、素材索引、局部裁切/遮挡逻辑参考。
- PR #41 不得作为合格样片、runtime_script 来源、timeline_plan 模板或完整旁白模板。

## Constraints（边界）

- 不得使用 `reference_script.md` 生成 TTS、字幕或视频。
- 必须使用 `runtime_script.md` 作为实际入片口播稿。
- 必须按 `timeline_plan.md` 和 `timeline_manifest.json` 执行 12 段结构。
- 总时长目标 `105s`，超过 `120s` 必须 blocked。
- 卡片最长 `4s`，卡片总占比不得超过 `0.25`。
- 真实录屏占比不得低于 `0.60`。
- 不得使用未脱敏火山引擎原画面。
- 不得写内容通过态。
- 不得写可发送真值。

## Must read first（必须先读取）

1. `preflight_check.md`
2. `reference_script.md`
3. `runtime_script.md`
4. `timeline_plan.md`
5. `timeline_manifest.json`
6. `material_usage_plan.md`
7. `redaction_plan.md`
8. `guardrail_check.md`

任一文件缺失必须 blocked。

## Done when（完成标准）

- 生成 V2.1 样片 MP4。
- 生成 captions.srt，字幕来自 `runtime_script.md`。
- 生成 render_report.md。
- 生成 contact_sheet。
- ffprobe 可读、可解码。
- 状态保持：`content_validation=pending_user_chatgpt_review`，`send_ready=false`。

## Blocked if（阻断条件）

- 计划包未审核。
- 使用了 reference_script 直接入片。
- 总时长超过 120s。
- 单张卡片超过 4s。
- 卡片承担主叙事。
- 真实录屏没有承担主体流程推进。
- 需要未脱敏火山素材。
- 任何状态写成内容通过或可发送。

## Output（最终回报）

只回报样片路径、字幕路径、manifest、render_report、验证结果、blocked 项、下一个目标。
