# Reference-to-Execution Contract 参考到执行落地契约

## 1. 文件定位

本文件是 Codex 执行层的 `Reference-to-Execution Contract（参考到执行落地契约）` 规则。

它负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段、偏离检查和完成验收。

它不负责：

- 保存所有 reference 原件。
- 直接生成视频、图片、音频或文案终稿。
- 推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。
- 替代用户 / ChatGPT 的最终内容判断。

## 2. 每个带 reference 的任务必须输出

Codex 每次执行带 reference 的任务前，必须先输出：

```text
reference_to_execution_contract:
  reference_anchor:
  effect_targets:
  function_fields:
  execution_mapping:
  deviation_check:
  done_when:
  blocked_if:
```

字段含义：

- `reference_anchor（参考锚点）`：reference 的来源、类型、可用性、必须保留、允许变化、不得复制、缺失阻断。
- `effect_targets（效果目标）`：用户真正要复现的观感、信息层级、节奏、人感、证据清晰度和质量点。
- `function_fields（执行函数字段）`：输入信号、证据角色、目标区域、执行动作、动作理由、验证规则、阻断条件、fallback 和反馈更新。
- `execution_mapping（执行映射）`：本 contract 作用到剪辑、文案、视觉、声音、质量复审还是供料链。
- `deviation_check（偏离检查）`：执行后对照 reference 的关键效果，写清可接受变化和不可接受偏离。
- `done_when（完成验收）`：能写完成的条件。
- `blocked_if（阻断条件）`：不能继续执行或不能写 completed 的条件。

## 3. Codex 执行前判断

```text
if task_contains_reference = true:
  require reference_to_execution_contract

if reference_missing = true:
  blocked unless user explicitly allows no-reference mode

if effect_targets_missing = true:
  do not execute, ask ChatGPT/user to fill

if function_fields_missing = true:
  do not execute, create contract first

if deviation_check_missing = true:
  do not claim completed
```

判断规则：

1. 用户给了 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 原感稿 / 外部资料 / “按这个效果做”，即 `task_contains_reference = true`。
2. 只写“参考某图 / 参考某视频 / 参考某样片”不算 contract。
3. 只写“风格类似”不算 `effect_targets（效果目标）`。
4. 只有颜色、形状、卡片或镜头结构相似，但用户目标效果不一致，必须写 `deviation（偏离）`。
5. 无法看到原 reference 时，必须写 `reference_missing = true` 或 `cannot_compare_reason（无法比较原因）`。

## 4. 与 state_action_router 联动

`Project State Action Router（项目状态动作总控器）` 检测到 reference 信号时，必须进入以下链路：

```text
state_action_router detects input_signal = reference_provided
-> current_project_state = reference_contract_needed
-> trigger_mechanism = Reference-to-Execution Contract
-> selected_action = create contract before concrete execution
```

Codex 执行侧状态新增：

```text
reference_contract_needed:
  trigger_signal:
    - user_provided_reference
    - sample_reference_given
    - visual_reference_given
    - editing_reference_given
    - copywriting_raw_feeling_reference_given
    - voice_reference_given
    - quality_sample_reference_given
    - external_research_reference_given
  selected_action:
    - create_reference_to_execution_contract
    - verify_reference_available
    - map_effect_targets_to_function_fields
    - execute_only_after_contract_complete
  blocked_if:
    - reference_missing_without_user_waiver
    - effect_targets_missing
    - function_fields_missing
    - deviation_check_unavailable
```

## 5. 与 Completion Relay Gate 联动

```text
Reference-to-Execution Contract 决定执行标准；
Completion Relay Gate 保证执行到底；
Deviation Check 决定是否偏离 reference；
completion_state_inference 决定能不能写 completed。
```

具体分工：

1. `Reference-to-Execution Contract` 先定义本轮 reference 的执行标准。
2. `Completion Relay Gate（补全接力闸门）` 把 contract 文件、入口同步、fixture、日志、上传包和验证加入 `required_output_inventory（必须交付清单）`。
3. `Deviation Check（偏离检查）` 在执行后判断是否符合 reference 的关键效果。
4. `completion_state_inference（完成状态判断）` 只有在 contract 字段齐全、偏离已检查、禁止状态未推进、验证通过时，才允许写 `completed`。

## 6. 与 DeepSeek / Perplexity 的边界

DeepSeek / fallback 供料包可选携带以下 reference contract 字段，辅助 Codex 判断：

```text
reference_anchor
effect_targets
function_fields
deviation_check
done_when_contract
```

边界：

- DeepSeek 只读供料，不写文件，不拍板项目事实。
- DeepSeek / fallback 只能辅助整理文字化 reference 资料、风险冲突和候选字段。
- Perplexity 只做外部研究和 reference pack，不直接成为项目正式事实。
- DeepSeek / Perplexity 摘要不得替代 `Reference-to-Execution Contract`。
- Codex 必须复核原文件和用户本轮输入，再执行和验证。

## 7. 任务类型映射

```text
editing_task:
  require editing_reference_contract
  validate pacing, cut points, evidence windows, zoom/crop/insert-card decisions

copywriting_task:
  require copy_reference_contract
  validate raw feeling, sentence rhythm, tone, information hierarchy, user goal preservation

visual_task:
  require visual_reference_contract
  validate layout role, visual weight, card density, character/evidence balance, no forbidden copy

voice_task:
  require voice_reference_contract
  validate pacing reference and voice reference separately

quality_review_task:
  require quality_reference_contract
  validate pass/fail against reference quality points before status wording
```

## 8. 禁止

```text
不得只写“参考某图 / 参考某视频 / 参考某样片”
不得只写“风格类似”
不得把 reference 当作普通背景
不得把无法比较的结果写成符合 reference
不得把 reference 关键效果偏离的输出写成 completed
不得让 DeepSeek / Perplexity 摘要替代原 reference contract
```

额外禁止：

- 不得在 reference 缺失时写“已按 reference 执行”。
- 不得把外部资料直接升级成 `已确认` 仓库事实。
- 不得因为技术生成成功就写 `content_validation = passed`。
- 不得因为声音候选存在就写 `voice_validation = passed` 或 `final_voice_validated = true`。
- 不得修改媒体文件、读取 secret 或调用 API 来补 contract。

## 9. 最小验证清单

Codex 收尾前必须检查：

```text
reference_contract_validation:
  reference_anchor_exists:
  effect_targets_exists:
  function_fields_exists:
  deviation_check_exists:
  done_when_exists:
  reference_missing_handled:
  forbidden_status_promotion_absent:
  deepseek_not_substitute_contract:
  completion_state_inference:
```

如果任一必填项缺失：

- Codex 必须继续补齐；若无法补齐，则写 `blocked（阻断）`。
- `partial_completed（部分完成）` 只允许用于用户明确接受的分阶段 reference contract，不得替代完整落地任务里的 `blocked`。
- 不得写 `completed（已完成）`。
- 必须在 `remaining_work_check（剩余工作检查）` 里列出缺口。

## 10. 一句话规则

**凡任务带 reference，Codex 必须先把 reference 拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when`；没有契约，不进入执行，不能写 completed。**
