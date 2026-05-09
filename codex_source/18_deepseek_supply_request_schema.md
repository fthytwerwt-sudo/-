# DeepSeek supply request schema

## 1. 文件定位

本文件定义《视频工厂》里 `DeepSeek supply request（DeepSeek 供料请求任务卡）` 的标准结构。

它解决的问题是：

- DeepSeek 每次供料前必须知道当前任务
- 这个“知道”来自 Codex / controller 显式传入的任务卡
- 不靠长期记忆
- 不靠猜测
- 不靠读取全仓库

本文件不代表：

- `multi-agent runtime（多 agent 运行时）` 已跑通
- DeepSeek 已稳定供料
- DeepSeek 可以写文件
- DeepSeek 可以拍板项目事实

## 2. 使用规则

Codex 触发 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）` 前，应优先生成或选择一张 `supply_request（供料请求任务卡）`。

推荐运行方式：

```bash
python3 scripts/deepseek_supply_controller.py \
  --request-file codex_source/fixtures/deepseek_supply_request_file_map_example.json
```

旧 CLI 参数仍可用于兼容测试和临时低风险任务，但后续正式供料优先使用 `--request-file`。

## 3. request identity（请求身份）

任务卡必须包含：

- `request_id（请求编号）`
- `created_at（创建时间）`
- `project_route（项目路由）`
  - 当前固定支持：`video_factory`
- `task_id（任务编号）`
- `task_type（任务类型）`
- `trigger_reason（触发原因）`
- `action（供料动作）`

`trigger_reason` 只允许：

- `missing_context`
- `rule_conflict`
- `stale_context_risk`
- `large_context`
- `before_write_gate`
- `after_read_gap`
- `user_explicit_deepseek`

`action` 只允许：

- `file_map`
- `risk_report`
- `context_summary`
- `missing_files`
- `visual_asset_requirement_pack`
- `api_asset_generation_pack`
- `image_prompt_pack`
- `asset_validation_pack`
- `assembly_decision_pack`
- `editing_decision_pack`
- `auto`

## 4. task state（任务状态）

任务卡必须包含：

- `current_goal（当前目标）`
- `current_step（当前步骤）`
- `known_context（已知上下文）`
- `missing_context（缺失上下文）`
- `decision_needed（需要判断什么）`

要求：

- `known_context` 可以为空数组，但字段必须存在。
- `missing_context` 可以为空数组，但字段必须存在。
- `decision_needed` 可以为空字符串，但字段必须存在。
- 不允许让 DeepSeek 自己猜当前任务阶段。

## 5. reading scope（读取范围）

任务卡必须包含：

- `candidate_files（候选读取文件）`
- `must_read_files（必须读取文件）`
- `optional_files（可选读取文件）`
- `forbidden_paths（禁止读取路径）`
- `max_context_files（最大上下文文件数）`
- `max_context_chars（最大上下文字数）`

默认禁止路径必须至少覆盖：

- `.env`
- `.env.*`
- `.env.swp`
- `.git/`
- `dist/latest_review_pack/`
- 视频 / 音频 / 图片等媒体文件
- archive-only 外部目录

controller 必须在读取前做路径安全检查。候选文件、必读文件、可选文件里只要命中禁止路径，就必须 blocked。

## 6. output contract（输出契约）

任务卡必须包含：

- `expected_output（期望输出）`
- `output_format（输出格式）`
- `codex_next_input（给 Codex 的下一步输入）`
- `return_to_codex（如何交回 Codex）`

`return_to_codex` 应说明输出目录和固定文件：

- `dist/deepseek_supply_controller/latest_supply_pack.md`
- `dist/deepseek_supply_controller/latest_supply_pack.json`
- `dist/deepseek_supply_controller/latest_supply_manifest.json`

Codex 后续执行必须读取供料包后再继续。

## 7. safety and stop（安全与停止线）

任务卡必须包含：

- `not_allowed（禁止事项）`
- `stop_condition（停止条件）`
- `blocked_if（阻断条件）`
- `fallback_allowed（是否允许本地兜底）`
- `fallback_policy（本地兜底策略）`

`not_allowed` 必须包含以下语义：

- 不让 DeepSeek 写文件
- 不让 DeepSeek 拍板项目事实
- 不把 `fallback_local_only（本地兜底）` 写成 DeepSeek 结论
- 不写 `multi-agent runtime（多 agent 运行时）` 已跑通

## 8. 最小校验规则

controller 必须检查：

- 顶层必须是 object
- 必填字段必须存在
- `project_route = video_factory`
- `trigger_reason` 必须合法
- `action` 必须合法
- `candidate_files / must_read_files / optional_files` 不得命中 `forbidden_paths`
- `.env`、`.git`、媒体文件、`dist/latest_review_pack/` 必须 blocked
- `known_context` 和 `missing_context` 字段必须存在
- `not_allowed` 必须包含四条安全语义

校验失败时：

- `supply_source = blocked`
- `request_validation_status = blocked`
- 必须写 `latest_supply_manifest.json`
- 不得读取 forbidden path

## 8A. real execution usage（真实执行用法）

Codex 每次执行复杂任务前，应先生成或选择一张 `supply_request（供料请求任务卡）`，再运行 controller。

真实执行时的用法：

1. `current_goal（当前目标）`
   - 写本轮要解决的机制、路由、复盘或执行缺口。
   - 不写泛泛“优化项目”。
2. `current_step（当前步骤）`
   - 写执行前供料、执行中补读、执行后风险复核等具体步骤。
3. `known_context（已知上下文）`
   - 只能写 Codex 已读取或用户本轮明确给出的事实。
   - 不把聊天记忆、旧 PR 印象或 fallback 摘要写成仓库已确认事实。
4. `missing_context（缺失上下文）`
   - 写当前卡住 Codex 判断的缺口，例如旧口径冲突、三卡是否接入、状态字段是否会误写。
5. `decision_needed（需要判断什么）`
   - 写供料要帮助 Codex 判断的问题，不让 DeepSeek 自己猜任务。
6. `candidate_files / must_read_files / optional_files`
   - 只放文本类候选文件。
   - 不放 `.env`、媒体文件、`dist/latest_review_pack/` 或 Git 内部目录。
7. `expected_output（期望输出）`
   - 写成文件地图、风险报告、上下文摘要、缺失文件报告或剪辑决策包，不要求 DeepSeek 写最终结论。

如果执行中出现缺口，可以生成 follow-up request：

- `trigger_reason = after_read_gap`
- `current_step = 执行中补读` 或 `执行后风险复核`
- `missing_context` 写本轮读完后仍无法判断的具体点

DeepSeek 不靠长期记忆、不靠猜测、不靠读全仓库。controller 输出若为 `fallback_local_only（本地兜底）`，Codex 可以继续低风险机制任务，但必须写 `not_deepseek_conclusion = true`，并以原文件复核和验证结果为准。

## 8B. editing_decision_pack（剪辑决策包）任务卡扩展

当 `action = editing_decision_pack（剪辑决策包）` 时，任务卡用于把视频执行现场的剪辑判断转成 DeepSeek / fallback 可处理的文字样料。

用途：

- 判断哪里放大。
- 判断哪里保留原画面。
- 判断哪里插卡。
- 判断哪里框选 / 高亮。
- 判断哪里不动以保护真实证据链。
- 判断哪些 reference 只继承质量，不照搬流程。
- 提醒哪些剪辑动作会导致 demo 感、说明书感、硬拼接感。

边界：

- DeepSeek 不直接剪视频。
- DeepSeek 不直接读取视频、音频、图片或媒体文件。
- DeepSeek 不拍板最终画面好不好。
- DeepSeek / fallback 只基于 Codex 提供的文字化样料生成建议。
- Codex 执行前仍必须复核素材证据和原文件。
- 最终内容判断仍由 ChatGPT / 用户完成。

任务卡可选字段：

```json
{
  "source_segments": [],
  "narration_lines": [],
  "contact_sheet_description": "",
  "ocr_text": [],
  "frame_descriptions": [],
  "reference_quality_points": [],
  "editing_question": ""
}
```

这些字段不能设为所有 action 的必填字段，以保持旧 fixture 向后兼容。只有 `action = editing_decision_pack` 时，文档规则要求尽量提供。

若 `source_segments / narration_lines / frame_descriptions / editing_question` 缺失，controller 不一定 blocked，但必须在供料包中标记：

- `missing_context（缺失上下文）`
- `blocked_if_insufficient_editing_sample（文字化剪辑样料不足时阻断）`

`editing_decision_pack（剪辑决策包）` 最小输出字段：

```text
editing_decision_pack:
  source_segment:
    file_reference:
    time_range:
    visible_content:
    evidence_role:
  narration_intent:
    line:
    function:
    viewer_should_understand:
  visual_action:
    action_type:
      - full_frame
      - zoom_in
      - crop_focus
      - highlight_box
      - freeze_frame
      - insert_card
      - split_compare
      - do_not_touch
    target_area:
    timing:
  reason:
  reference_quality_point:
  risk:
  blocked_if:
  codex_execution_note:
```

## 8C. execution_supply_pack family（执行供料包族）任务卡扩展

当 `action` 属于以下任一值时，任务卡用于把“最终文案进入执行后”的素材、API、prompt、验收、装配和剪辑判断转成 DeepSeek / fallback 可处理的文字供料：

- `visual_asset_requirement_pack（视觉素材需求包）`
- `api_asset_generation_pack（API 素材生成包）`
- `image_prompt_pack（图片 prompt 包）`
- `asset_validation_pack（素材验收包）`
- `assembly_decision_pack（装配决策包）`
- `editing_decision_pack（剪辑决策包）`

标准链路：

```text
content_route_card
-> visual_asset_requirement_pack
-> api_asset_generation_pack
-> image_prompt_pack
-> asset_validation_pack
-> assembly_decision_pack
-> editing_decision_pack
-> review_pack
```

任务卡可选字段：

```json
{
  "script_blocks": [],
  "segments": [],
  "content_route_card": {},
  "visual_asset_requirements": [],
  "api_generation_targets": [],
  "image_prompt_specs": [],
  "asset_validation_criteria": [],
  "assembly_slots": [],
  "fallback_plan": "",
  "vendor_constraints": {},
  "api_call_policy": "",
  "secret_policy": ""
}
```

这些字段不能设为所有 action 的必填字段，以保持旧 fixture 向后兼容。只有命中对应 action 时，文档规则要求尽量提供相关字段。

边界：

- DeepSeek / fallback 只基于文字样料供料，不读取媒体文件。
- DeepSeek / fallback 不读取 `.env`、API key、token 或密钥文件。
- 本轮机制测试不调用阿里 API 或其他真实生成 API。
- `api_asset_generation_pack（API 素材生成包）` 只能生成计划、prompt、验收和降级方案；未来真实 API 调用必须用户明确授权。
- `image_prompt_pack（图片 prompt 包）` 默认不让图片模型生成中文可读文字；如需文字，应由后期卡片层处理。
- 不得复用官方 Minecraft 资产、logo、字体、texture、model、sound。
- `asset_validation_pack（素材验收包）` 必须把 AI 图片不能替代真实录屏证据写进判断。
- `assembly_decision_pack（装配决策包）` 必须区分主证据与辅助素材；需要剪辑细化时回到 `editing_decision_pack（剪辑决策包）`。

如果任务卡禁止 `.env / secret`，controller 可以直接使用 `fallback_local_only（本地兜底）`，但必须写：

- `not_deepseek_conclusion = true`
- `deepseek_generation_status = skipped_for_forbidden_env_or_secret_policy`
- `context_pack_validation = fallback_local_only`

## 8D. model preference（模型偏好）

当前默认不要求每张 `supply_request（供料请求任务卡）` 指定模型。

默认模型由系统配置决定：

- `DEEPSEEK_MODEL=deepseek-v4-flash`
- `DEEPSEEK_ESCALATION_MODEL=deepseek-v4-pro`

后续如果任务卡扩展 `preferred_model（优先模型）` 字段，只允许：

- `deepseek-v4-flash`
- `deepseek-v4-pro`

使用规则：

- 常规 `file_map（文件地图）`、`missing_files（缺失文件）`、`context_summary（上下文摘要）`、普通 `risk_report（风险报告）` 和基于文字样料的执行供料包族默认使用 `deepseek-v4-flash`。
- 多文件冲突、复杂机制判断、长任务审计、多轮供料包合并、Flash 多次失败或 `after_read_gap（读完仍有缺口）` 且 fallback 不足时，才考虑升级到 `deepseek-v4-pro`。
- 本轮不强制修改 JSON Schema；自动模型升级仍是待后续开发与验证项。

## 9. 一句话规则

`DeepSeek supply request` 是每次供料前的任务卡：Codex 用它把当前目标、已知上下文、缺口、候选文件、禁止路径、输出契约和停止线传给 controller；DeepSeek 只按这张卡供料，不靠记忆猜项目状态。
