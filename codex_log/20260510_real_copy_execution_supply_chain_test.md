# 20260510｜真实文案全执行供料链测试

## 1. 测试口径

本文件只记录一轮小范围结构化供料链测试。

- `technical_validation（技术验证）`: 只验证供料链结构、request 和 controller 可运行。
- `mechanism_validation（机制验证）`: 验证真实文案能否进入全执行供料包族。
- `content_validation（内容验证）`: 未验证，不得写成 passed。
- `api_generation_validation（API 生成验证）`: 未调用阿里 API，未生成真实图片。
- `video_generation_validation（视频生成验证）`: 未生成真实视频。

## 2. real_copy_execution_supply_chain_test

```yaml
real_copy_execution_supply_chain_test:
  source_copy:
    path: dist/latest_review_pack/timeline.json
    status: closest_available_repo_copy
    why_selected: 当前 v3.1 基线时间线包含逐段 voice_text、时间码、承载类型和视觉路由，是仓库内最接近当前真实口播脚本的文本入口；本轮只读取文本，不读取媒体文件。
    excerpt:
      - "先看这两个结果。左边，是我第一次让 AI 帮我做 PPT。右边，是我改完问法以后。我先说结论：差的不是工具，是我第一句话。"
      - "第一次，我把最新方案 PDF 丢进豆包，只写了一句：帮我把这个方案整理一下。"
      - "第二次，我没有一上来就说帮我做个 PPT。我先让它判断一件事：这份内容，能不能变成一版可交付初稿。"
      - "先定义交付，再让 AI 生成。"
  content_route_card:
    content_type: AI 职场任务现场拆解
    validation_goal: 测试观众能否看懂“普通整理问法”与“可交付初稿问法”的结果差。
    core_evidence:
      - 反面录屏：PDF 与宽泛口令可见。
      - 反面录屏：战略执行总案 / 产品矩阵 / 30 天落地计划，看似完整但不是 PPT 初稿。
      - 正面录屏：可交付初稿方法词出现。
      - 正面录屏：PPT 页面设计指令、PPT 生成过程、16 页预览。
    middle_carrier: user_recording
    ppt_usage: 少量 PPT / 信息卡用于结果差、方法拆解和低压收束。
    prompt_tail_card_usage: 低压尾卡可用，但不承担主证据。
    flow_flex_reason: 本轮不套固定流程，只基于当前真实口播和证据角色判断承载。
```

## 3. visual_asset_requirement_pack（视觉素材需求包）

| segment | viewer_task | required_asset_type | evidence_role | can_be_api_generated | fallback_if_missing | blocked_if |
| --- | --- | --- | --- | --- | --- | --- |
| `shot01_result_diff_opening` | 看懂左右结果差与主判断 | `info_card` | `auxiliary_explanation` | `true`，只做辅助视觉壳 | 少量 PPT / 静态信息卡 | 把卡片当真实结果证据 |
| `shot02_negative_input` | 看懂旧做法只给了“整理”动作 | `user_recording` | `primary_evidence` | `false` | 补录 / 截图 / blocked | 用 API 图替代真实录屏 |
| `shot04_negative_result_text_plan` | 看懂“完整但不能交”的反面结果 | `user_recording` | `primary_evidence` | `false` | 补录 / 截图 / blocked | 剪掉可读结果导致证据断裂 |
| `shot06_cause_turning_point` | 看懂问题在交付定义不清 | `info_card` | `reasoning_support` | `true`，只做辅助表达 | 少量 PPT | 写成证据结论 |
| `shot07_deliverable_draft_keyword` | 看懂可交付初稿方法词 | `user_recording` | `primary_evidence` | `false` | 补录 / 截图 / blocked | 用信息卡冒充方法词出现 |
| `shot09_positive_title_specific` | 看懂标题变具体 | `user_recording` | `primary_evidence` | `false` | 截图 / blocked | API 图抢走录屏主体 |
| `shot10_positive_constraints` | 看懂周期、预算、渠道、目标约束 | `user_recording` | `primary_evidence` | `false` | 截图 / blocked | 口播说有约束但画面不支撑 |
| `shot11_ppt_page_instruction` | 看懂从文档往 PPT 走 | `user_recording` | `primary_evidence` | `false` | 截图 / blocked | 只用卡片解释，缺真实页面 |
| `shot13_ppt_completed_preview` | 看懂完成 PPT 生成和 16 页预览 | `user_recording` | `primary_evidence` | `false` | 截图 / blocked | 把预览写成最终成品 |
| `shot15_result_diff_card` | 总结第一种问法 vs 第二种问法 | `info_card` | `summary_support` | `true`，只做辅助视觉壳 | 少量 PPT | 写成内容验证通过 |
| `shot16_low_pressure_ending` | 带走最小动作 | `prompt_tail_card` | `action_summary` | `true`，背景 / 图标可生成 | 少量 PPT / 纯文字卡 | 强卖课或抢主结尾 |

## 4. api_asset_generation_pack（API 素材生成包）

```yaml
api_asset_generation_pack:
  generation_needed: planned_only
  api_call_allowed_this_round: false
  future_real_call_requires_user_authorization: true
  secret_required: false
  api_key_read: false
  candidates:
    - asset_id: api_aux_result_diff_bg_01
      vendor_candidate: aliyun
      segment_usage: shot01_result_diff_opening
      purpose: 结果差卡背景 / 视觉壳
      aspect_ratio: 9:16
      style_constraints: Minecraft-inspired 原创体素方块风，柔和可爱信息卡，不复用官方 Minecraft 资产
      must_be_real_evidence: false
    - asset_id: api_aux_transition_icon_01
      vendor_candidate: aliyun
      segment_usage: shot06_cause_turning_point
      purpose: 从“整理”转向“定义交付”的转折图标
      aspect_ratio: 1:1
      style_constraints: 原创体素小图标，无 logo，无中文可读字
      must_be_real_evidence: false
    - asset_id: api_aux_tail_bg_01
      vendor_candidate: doubao
      segment_usage: shot16_low_pressure_ending
      purpose: 低压尾卡背景，不承担主证据
      aspect_ratio: 9:16
      style_constraints: 轻陪伴、低压、原创体素风
      must_be_real_evidence: false
  fallback_plan:
    - 少量 PPT / 信息卡
    - 真实截图
    - no_extra_asset
    - blocked
  blocked_if:
    - 需要读取 API key 或 .env
    - 需要真实调用阿里 API
    - 用 API 图替代真实录屏证据
```

## 5. image_prompt_pack（图片 prompt 包）

```yaml
image_prompt_pack:
  - asset_id: api_aux_result_diff_bg_01
    segment: shot01_result_diff_opening
    purpose: 结果差开头卡背景
    positive_prompt: "Original voxel-block inspired soft pink information-card background, two clean comparison panels, subtle office-task mood, friendly AI helper atmosphere, no readable text, vertical 9:16 composition."
    negative_prompt: "official Minecraft assets, logos, brand marks, readable Chinese text, game UI screenshots, copyrighted textures, clutter, fake evidence, photorealistic people"
    style_anchor: Minecraft-inspired 原创体素方块风
    composition: 左右对比留白，文字由后期卡片层生成
    text_policy: no_readable_text
    acceptance_criteria: 背景不抢结果差文字，不冒充真实录屏
    rejected_if: 出现可读错字、官方资产感、过强 AI 图堆砌感
  - asset_id: api_aux_transition_icon_01
    segment: shot06_cause_turning_point
    purpose: 转折图标
    positive_prompt: "Small original voxel icon showing a messy note becoming a clear delivery checklist, clean silhouette, no text, soft pastel palette."
    negative_prompt: "official Minecraft icon, logo, readable text, dense UI, fake platform screenshot"
    style_anchor: Minecraft-inspired 原创体素方块风
    composition: 居中小图标，适合信息卡角标
    text_policy: no_readable_text
    acceptance_criteria: 只辅助表达“定义交付”，不承担证据
    rejected_if: 图标像官方游戏素材或像真实软件截图
  - asset_id: api_aux_tail_bg_01
    segment: shot16_low_pressure_ending
    purpose: 低压尾卡背景
    positive_prompt: "Warm original voxel workspace background, calm guide-like mood, blank space for post-production card text, no readable text, vertical short-video layout."
    negative_prompt: "official Minecraft assets, text, logo, promotional CTA, hard sell design, dark noisy background"
    style_anchor: Minecraft-inspired 原创体素方块风
    composition: 上方留标题区，中下留一行提示词区域
    text_policy: no_readable_text
    acceptance_criteria: 低压收束，不强卖，不抢口播
    rejected_if: 像广告海报、卖课 CTA 或文本不可控
```

## 6. asset_validation_pack（素材验收包）

```yaml
asset_validation_pack:
  global_rule:
    ai_image_can_replace_real_evidence: false
    validation_result_default: pending_human_review
  checks:
    - asset_id: api_aux_result_diff_bg_01
      intended_use: 结果差卡背景
      evidence_fit: auxiliary_only
      required_fix: 如果抢真实结果差文字，降级为纯 PPT 背景
      blocked_if: 观众可能误以为这是真实录屏或真实平台页面
    - asset_id: api_aux_transition_icon_01
      intended_use: 转折角标
      evidence_fit: auxiliary_only
      required_fix: 风格过游戏官方化则 reject
      blocked_if: 出现官方 Minecraft 资产、logo、texture、model 感
    - asset_id: api_aux_tail_bg_01
      intended_use: 低压尾卡背景
      evidence_fit: auxiliary_only
      required_fix: 如果过度营销，改为纯信息卡
      blocked_if: 把尾卡做成强 CTA 或第二个主结尾
```

## 7. assembly_decision_pack（装配决策包）

```yaml
assembly_decision_pack:
  - segment: shot02_negative_input
    primary_carrier: user_recording
    secondary_carrier: none_or_small_marker
    timing: 15.112-23.666s
    evidence_chain_note: 保留输入框和宽泛口令，不用 API 图覆盖。
    needs_editing_decision_pack: true
  - segment: shot04_negative_result_text_plan
    primary_carrier: user_recording
    secondary_carrier: optional_highlight_box
    timing: 23.666-34.420s
    evidence_chain_note: 需要让“完整但不能交”的文本结果可读。
    needs_editing_decision_pack: true
  - segment: shot07_deliverable_draft_keyword
    primary_carrier: user_recording
    secondary_carrier: highlight_box
    timing: 49.389-59.955s
    evidence_chain_note: 方法词出现是核心证据，不能被卡片替代。
    needs_editing_decision_pack: true
  - segment: shot13_ppt_completed_preview
    primary_carrier: user_recording
    secondary_carrier: subtitle_or_small_note
    timing: 111.276-123.917s
    evidence_chain_note: 预览不等于最终成品，字幕 / 卡片必须保留边界。
    needs_editing_decision_pack: true
  - segment: shot16_low_pressure_ending
    primary_carrier: prompt_tail_card
    secondary_carrier: optional_api_background
    timing: 135.741-150.081s
    evidence_chain_note: 结尾总结不回写内容通过，只回流给审片。
    needs_editing_decision_pack: false
```

## 8. editing_decision_pack（剪辑决策包）

```yaml
editing_decision_pack:
  - source_segment:
      file_reference: text_source:dist/latest_review_pack/timeline.json
      time_range: 15.112-34.420s
      visible_content: 反面录屏，宽泛口令与泛化结果
      evidence_role: negative_example_primary_evidence
    visual_action:
      action_type: crop_focus
      target_area: 输入框 / 结果标题 / 泛化计划关键词
      timing: 保留原画面节奏，只在关键词出现时轻微放大
    reason: 保护旧做法证据链，避免做成说明书感硬拆解。
    risk: 剪掉输入框会导致观众看不懂“第一句话”问题。
    blocked_if: 需要读取或重剪真实视频文件。
  - source_segment:
      file_reference: text_source:dist/latest_review_pack/timeline.json
      time_range: 49.389-91.087s
      visible_content: 正面录屏，可交付初稿、标题、周期、预算、渠道、目标
      evidence_role: positive_method_primary_evidence
    visual_action:
      action_type: highlight_box
      target_area: 可交付初稿 / 周期 / 预算 / 渠道 / 目标
      timing: 跟随口播关键词短暂停留
    reason: 放大真实结果差，不让卡片抢中段主体。
    risk: 过度高亮会变成教学说明书。
    blocked_if: 画面不可读且没有截图补证。
  - source_segment:
      file_reference: text_source:dist/latest_review_pack/timeline.json
      time_range: 111.276-123.917s
      visible_content: 已完成 PPT 生成，16 页预览
      evidence_role: result_boundary_primary_evidence
    visual_action:
      action_type: do_not_touch
      target_area: 完成状态与预览页数
      timing: 保持证据完整
    reason: 这里要保护“推进到 PPT 初稿状态，但预览不等于最终成品”的边界。
    risk: 过度包装会让观众误解成成品质量已通过。
    blocked_if: 需要把预览写成最终成品。
```

## 9. review_pack_test_summary（测试审片回流摘要）

- `已确认` 本轮找到了仓库内真实口播文本入口：`dist/latest_review_pack/timeline.json`。
- `已确认` 本轮只生成结构化测试包和 request，不生成视频、不生成图片、不调用阿里 API。
- `已确认` API 图只被规划为辅助表达、背景、图标、信息卡或尾卡视觉壳，不能替代真实录屏证据。
- `待验证` 真实素材计划是否能减少漏项，仍需下一轮在更小执行任务中继续验证。
- `待验证` 本轮不代表 DeepSeek 稳定真实供料，不代表 multi-agent runtime 跑通。

## 10. forbidden_status（禁止状态）

```yaml
forbidden_status:
  ali_api_called: false
  api_key_read: false
  image_generated: false
  video_generated: false
  audio_generated: false
  env_file_read_for_copy_test: false
  publish_status_changed: false
  content_validation_changed: false
  send_ready_changed: false
  voice_validation_changed: false
  final_voice_validated_changed: false
```

## 11. controller_request_validation（controller 请求验证）

```yaml
controller_request_validation:
  request_file: codex_log/supply_requests/20260510_real_copy_execution_supply_chain_request.json
  request_validation_status: passed
  action: visual_asset_requirement_pack
  supply_source: fallback_local_only
  context_pack_validation: fallback_local_only
  fallback_status: used
  not_deepseek_conclusion: true
  deepseek_actual_participation: false
  env_file_read: false
  process_env_key_allowed: false
  process_env_key_present: false
  api_key_printed: false
  api_key_written: false
  output_files_local:
    - dist/deepseek_supply_controller/latest_supply_pack.md
    - dist/deepseek_supply_controller/latest_supply_pack.json
    - dist/deepseek_supply_controller/latest_supply_manifest.json
  output_files_committed: false
  evidence_summary: request validation 和 execution_supply_pack 字段可运行；因未显式允许 process env key，且任务卡禁止 .env / secret，本次供料来源是本地兜底，不是 DeepSeek 结论。
```

## 12. 下一个目标

用 controller 运行真实文案 request 和安全 DeepSeek process env request，记录 `supply_source（供料来源）`、`fallback_status（兜底状态）`、`deepseek_actual_participation（DeepSeek 实际参与）`，并继续保持不生成视频、不调用阿里 API。
