# 20260514｜script anchor / TTS / opening / timeline 机制修补

## 1. 本轮定位

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补，不是视频成片任务。
- `已确认` 本轮只修“下一条片进入执行前，系统自动补全和自动锚点”的机制。
- `未生成` 视频、音频、图片、字幕成品。
- `未执行` mux、TTS API、图片 / 视频生成 API、voice cloning。
- `未重做` `full.mp4`、`narration.wav`、`captions.srt` 或当前候选片。

## 2. route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - mechanism_or_route_fix
    - project_file_change
    - field_and_function_landing
  responsibility_layer:
    - mechanism_fix_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: true
    reason: 多文件机制修补、字段新增、函数接入、fixture case、执行阻断条件和日志同步
    lane_recommendation: audit_lane -> standard_lane
    parallel_recommendation: serial_only
  execution_permission: allowed_after_must_read_passed
```

## 3. 新增 / 补强字段

- `script_anchor_map（文案锚点表）`
- `script_function_map（文案功能表）`
- `evidence_anchor_map（证据锚点表）`
- `visual_anchor_map（画面锚点表）`
- `tts_prosody_anchor_map（TTS 韵律锚点表）`
- `opening_visual_hook_spec（开头视觉钩子规格）`
- `card_anchor_map（卡片锚点表）`
- `forbidden_visual_map（禁用画面表）`
- `script_to_timeline_map（文案到时间线映射表）`

## 4. 新增 / 补强函数

- `script_anchor_extraction_function（文案锚点提取函数）`：新增为最终文案进入视频执行前的句子级锚点提取函数。
- `content_route_inference_function（内容路由推理函数）`：补强为必须触发 script anchor、TTS prosody、opening hook spec 和 timeline map。
- `editing_inference_function（剪辑推理函数）`：补强为必须读取 `script_to_timeline_map`，不能只看段落级 `material_01 / material_02 / material_03`。
- `quality_issue_classifier（质量短板分类器）`：新增 `voice_prosody_issue / opening_visual_hook_issue / script_visual_mismatch_issue`。

## 5. 新增执行前阻断条件

```text
video_execution_preflight_blockers:
  missing_script_anchor_extraction_function:
    blocked: true

  missing_script_to_timeline_map:
    blocked_video_execution: true

  missing_tts_prosody_anchor_map:
    blocked_tts_generation: true

  missing_opening_visual_hook_spec_when_high_emotion_hook:
    blocked_opening_generation: true

  paragraph_level_mapping_only:
    blocked_video_execution: true
```

补充规则：

- TTS 问题诊断优先顺序为 `prosody -> pause_timing -> sentence_segmentation -> emphasis -> pitch_contour -> voice_timbre`。
- 用户反馈“某个字突然上扬”时，优先归因到 `pitch_contour / prosody`，不默认换音色。
- 开头路线判断不等于开头视觉通过；静态两行标题页不能默认通过高情绪 / 抖音抓眼开头验收。
- 每 1-2 句必须有 `line_group_id`，并绑定素材、时间码、画面职责、字幕职责、卡片职责、禁用画面和验证规则。

## 6. fixture cases

`codex_source/fixtures/mechanism_inference_function_cases.json` 已追加 5 个 case：

1. `tts_pitch_rise_ai_feel_case`
2. `static_two_line_opening_failed_case`
3. `script_visual_mismatch_partial_case`
4. `paragraph_level_mapping_insufficient_case`
5. `ai_money_script_anchor_case`

`已验证` JSON 可解析，当前 fixture case 总数为 `18`。

## 7. 同步文件

- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/01_execution_rules.md`
- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `codex_log/latest.md`

## 8. 禁止状态检查

- `未修改` `dist/latest_review_pack/`
- `未修改` 任何视频、音频、图片、字幕成品。
- `未读取` `.env`、`.env.swp`、API key、token、secret。
- `未推进` `content_validation（内容验证）`。
- `未推进` `send_ready（可发送状态）`。
- `未推进` `publish_status（发布状态）`。
- `未推进` `voice_validation（声音验证状态）`。
- `未推进` `final_voice_validated（最终声音验证状态）`。

## 9. 状态边界

- `已确认` 机制已写入、字段已落地、函数已接入、fixture 已补、执行前 blocked 条件已加。
- `待验证` 这些机制在下一条真实新片中的长期真实效果。
- `不得写成` 当前候选片声音问题已解决、开头视觉已通过、文案画面映射已在真实新片通过、内容可发布或声音最终通过。

## 10. 下一个目标

下一条新片进入执行前，先用 `script_anchor_extraction_function（文案锚点提取函数）` 生成 `script_to_timeline_map（文案到时间线映射表）`、`tts_prosody_anchor_map（TTS 韵律锚点表）` 和必要的 `opening_visual_hook_spec（开头视觉钩子规格）`，让缺字段的任务自动 blocked，而不是继续靠用户逐点补漏。
