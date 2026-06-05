# 数据目标执行总线

## 0A. formal_operation bus mode

当前总线服务 `formal_operation_active（正式运营中）`：DeepSeek 供料、Codex 执行、发布后数据回流和运营复盘，都必须围绕 `operation_records` 与 `current_data_goal_anchor` 工作。

旧 `gray_test` 只作为历史兼容别名；新数据默认进入 `operation_data_intake`。当前锚点仍是 `partial_data_recorded`，不能写 `ready`。

## 0A-1. operation_decision_system gate

`data_goal_alignment_check（数据目标对齐检查）` 之前必须先有 `operation_decision_system（运营决策系统）` 的最终判断报告。

当前入口：

- `scripts/运营决策系统_operation_decision_system.py`
- `review_loop/decision_engine/latest_operation_decision_report.json`
- `review_loop/decision_engine/final_user_operation_result.md`

硬规则：

- 若最终报告为 `blocked_for_formal_next_episode_execution`，不得继续生成正式下一条视频执行 prompt。
- 若 V002 被识别为 `policy_limited_abnormal_operation_sample`，不得把它纳入正常自然分发归因。
- 若 V003 仍缺 7d、3s 留存、V003 单条视频主页访问、私信、有效私信、有效咨询或清晰需求客户，不得把当前锚点写成 `ready`。
- 本闸门只负责运营决策，不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。

## 0A-2. next_copy_revision_brief gate（下一版文案修改简报闸门）

正式下一条视频执行前，必须先读取最新 `next_copy_revision_brief（下一版文案修改简报）`，并确认它不是正式执行 prompt。

当前入口：

- `review_loop/copy_iteration/latest_copy_iteration_report.md`
- `review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md`
- `review_loop/learning_ledger/current_copy_revision_handoff.md`
- `review_loop/learning_ledger/next_episode_bet_card.md`
- `review_loop/learning_ledger/operation_learning_memory.md`
- `scripts/文案迭代决策系统_copy_iteration_decision_system.py`

硬规则：

- `next_copy_revision_brief` 只给 ChatGPT 做汇报、判断和改稿；不是 Codex 视频执行单。
- 每次复盘后的数据目标，必须回写到文案层交接卡。
- 下一次 ChatGPT 写文案前必须读取 `current_copy_revision_handoff.md` 和 `next_episode_bet_card.md`。
- Codex 不生成正式文案，但必须把复盘结果喂给文案层。
- 当 `formal_copy_revision_allowed = false` 时，Codex 不得生成 `next_video_execution_prompt（下一条视频执行 prompt）`。
- 当 brief 只允许 `opening_0_3s + bridge_3_8s` 时，不得改目标用户、核心选题方向、offer 或全片结构。
- 缺 `copy_iteration_decision` 或缺 `next_copy_revision_brief` 时，不得进入正式下一条视频执行。
- brief 被 ChatGPT / 用户确认并升级为正式文案后，仍需重新建立 `locked_copy_contract（锁定文案契约）` 和 `data_goal_alignment_check（数据目标对齐检查）`，才能进入 Codex 执行。

## 0A-3. bridge_to_copy_learning_memory（桥接到文案学习记忆）

```yaml
bridge_to_copy_learning_memory:
  trigger:
    - operation_review_completed
    - operation_data_intake_completed
    - before_next_copy_revision
    - user_requests_next_episode_from_data
    - user_feedback_review_is_not_constructive
  required_writeback:
    - review_loop/learning_ledger/operation_learning_memory.md
    - review_loop/learning_ledger/next_episode_bet_card.md
    - review_loop/learning_ledger/current_copy_revision_handoff.md
  required_before_chatgpt_copy:
    - current_copy_revision_handoff
    - next_episode_bet_card
    - operation_learning_memory
    - latest_copy_structure_map
  blocked_if:
    - missing_next_episode_bet_card
    - missing_current_copy_revision_handoff
    - only_review_report_without_copy_layer_handoff
```

## 0B. publish_candidate delivery gate

数据目标执行总线只负责把目标接到文案、供料、剪辑、编排、装配和验收。它不能把执行前补全包、路由卡、时间线、TTS 韵律锚点、剪辑 / 装配决策包或技术预览升级成用户交付物。

正式运营视频执行完成前必须同时满足：

1. `data_goal_alignment_check（数据目标对齐检查）` 已输出。
2. `delivery_baseline_gate（交付基线闸门）` 已输出。
3. 结果是 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 或 `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`。

当前默认出片比例为 `horizontal_16_9（横屏 16:9）`，默认交付分辨率为 `1920x1080`。缺音轨、字幕、横屏 16:9 / 1920x1080 装配、中段证据、结尾收束、TTS、卡片、人感质量、平台风险、API 授权或装配能力时，必须 blocked，不得用 `technical_preview（技术预览）`、无声预览、横屏技术包或 JSON / Markdown route card 写完成。

## 0C. no_degrade_completion in data_goal_execution_bus

数据目标执行总线不得把对齐检查、中间包或降级产物升级成完成结果。

硬规则：

- 如果当前变量要求 `publish_candidate（可发布候选片）`，最终产物必须满足可发布候选片基线。
- 如果任何执行条件缺失，必须 `blocked`，不得用 route card、时间线、决策包、对齐检查或技术预览写完成。
- `data_goal_alignment_check（数据目标对齐检查）` 只能证明“执行结构没有偏离数据目标”，不能替代真实交付结果。
- fallback / degradation plan 只能作为 `blocked` 后待用户授权的修复建议；未经授权不得成为交付。

## 0D. locked_copy_contract in execution bus

数据目标执行总线进入视频执行前，必须同时检查：

1. `locked_copy_contract（锁定文案契约）` 已存在，且包含 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。
2. Codex 没有擅自改标题、选题、开头句、核心判断、人味表达、文案语义或视觉标题卡标题。
3. 如需改文案，已输出 `copy_change_request（文案修改请求）`，等待 ChatGPT / 用户确认。
4. `script_to_timeline_map` 已按 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 做到 `line_group` 级别，不是段落级素材分配。
5. `subtitle_card_overlap_check（字幕卡片重叠检查）` 已完成，且无 high severity overlap。

若用户明确说视频已经发了 / 已发布，总线不得把当前视频重新路由到默认回炉；应进入 `operation_data_intake / operation_review`，并把机制问题写入下一轮执行规则。

## 1. 文件定位

本文件定义 `data_goal_execution_bus（数据目标执行总线）`。

它解决的问题是：把项目架构、文案、DeepSeek 供料、Codex 剪辑编排、发布后复盘统一锚定到 `data_goal_anchor（数据目标锚点）`。

当前实例锚点的优先读取来源是：

- `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`

本文件定义执行链怎么使用 `data_goal_anchor`；`codex_log/current_data_goal_anchor.md` 存放当前这一条 / 下一条视频实际使用的锚点实例。二者职责不得混写。

硬边界：

- `已确认` 数据目标是最高决策锚点，不是唯一判断来源。
- `已确认` 素材证据决定能做什么，人感质量决定能不能发。
- `已确认` Codex 可以调整执行结构，但不得改写已锁定的数据目标判断。
- `待验证` 本总线已写入机制，不代表真实任务中已经稳定跑通。

一句话原则：

```text
目标锁死，结构可变。
```

## 2. data_goal_execution_bus（数据目标执行总线）

```yaml
data_goal_execution_bus:
  purpose:
    - "把项目架构、文案、DeepSeek 供料、Codex 剪辑编排、发布复盘统一锚定到数据目标。"
    - "防止 Codex 只按素材、画面顺序或旧视频流程自由发挥。"
    - "防止 DeepSeek 泛泛供料，不回答本轮数据目标相关风险。"

  architecture_principle:
    data_goal_sets_direction:
      meaning: "数据目标定方向。"
      locked_scope:
        - current_stage_goal
        - main_bottleneck
        - primary_variable
        - forbidden_variables
        - success_metric
        - failure_metric
        - post_publish_validation_metric
    material_evidence_sets_feasibility:
      meaning: "素材证据定能做什么。"
      rule: "素材里没有的页面、动作、结果、数据、时间码，不得被文案、剪辑或卡片编造。"
    human_quality_sets_publishability:
      meaning: "人感质量定能不能发。"
      rule: "画面顺、卡片好看、TTS 自然，只能进入发布前人感验收，不能替代数据目标验证；技术预览不能替代可发布候选片。"
    codex_controls_execution_structure:
      meaning: "Codex 负责编排和执行。"
      may_adapt:
        - segment_order
        - card_position
        - editing_style
        - assembly_sequence
        - material_binding
        - tts_segmentation
        - fallback_visuals
      must_preserve:
        - main_bottleneck
        - primary_variable
        - forbidden_variables
        - success_metric
        - failure_metric
        - post_publish_validation_metric
    deepseek_supplies_context_and_risk:
      meaning: "DeepSeek 负责只读供料和风险提醒。"
      rule: "DeepSeek 不写文件、不拍板项目事实、不替代 Codex 验证。"
```

## 3. upstream_anchor（上游锚点）

任何正式文案、视频执行、剪辑、装配、DeepSeek 供料、发布后复盘任务，必须先确认以下锚点是否存在。

```yaml
data_goal_anchor:
  current_data_goal_anchor_path: "codex_log/current_data_goal_anchor.md"
  current_data_goal_anchor_status:
  current_north_star_goal:
  current_stage_goal:
  threshold_config_v1:
  video_goal_card:
  post_publish_review_card:
  data_flywheel_memory:
  main_bottleneck:
  primary_variable:
  supporting_variables:
  forbidden_variables:
  content_structure_feedback_card:
  next_video_structure_plan:
  next_video_execution_prompt:
  success_metric:
  failure_metric:
  post_publish_validation_metric:
```

阻断规则：

- 缺 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`，不得进入正式视频执行。
- 当前实例状态为 `draft / waiting_data` 时，只能做假设版、机制接线、供料任务卡或 blocked，不得写正式数据驱动执行 ready。
- 缺 `current_stage_goal（当前阶段目标）`，不得进入数据驱动执行。
- 缺 `main_bottleneck（主短板）`，不得重写正式文案或重排内容结构。
- 缺 `primary_variable（主验证变量）`，不得进入 Codex 视频执行。
- 缺 `forbidden_variables（禁止变量）`，不得声称本轮是可归因实验。
- 缺 `success_metric / failure_metric / post_publish_validation_metric（成功 / 失败 / 发布后验证指标）`，不得写执行完成。

## 4. bridge_to_copy（桥接到文案）

`next_video_execution_prompt（下一条视频执行 prompt）` 不只是给文案使用，它也是供料、剪辑、编排和复盘的统一锚点。

```yaml
bridge_to_copy:
  required_before_copy_revision:
    - current_data_goal_anchor_path
    - current_data_goal_anchor_status
    - data_goal_copy_revision_gate
    - content_structure_feedback_card
    - next_video_structure_plan
    - main_bottleneck
    - primary_variable
    - supporting_variables
    - forbidden_variables
    - success_metric
    - failure_metric
    - post_publish_validation_metric
  required_output:
    - copy_revision_strategy
    - revised_script
    - next_video_execution_prompt
    - data_goal_anchor_used
```

硬规则：

- 内容路由不是只判断画面承载，而是先判断这条内容如何服务本轮数据目标。
- 最终文案如果没有 `data_goal_anchor_used（使用的数据目标锚点）`，不得交给 Codex 执行。

## 5. bridge_to_deepseek（桥接到 DeepSeek）

DeepSeek supply request 默认必须接收数据目标字段。

```yaml
bridge_to_deepseek:
  supply_request_must_include:
    - current_data_goal_anchor_path
    - current_data_goal_anchor_status
    - current_goal
    - current_stage_goal
    - main_bottleneck
    - primary_variable
    - supporting_variables
    - forbidden_variables
    - content_structure_feedback_card
    - next_video_execution_prompt
    - success_metric
    - failure_metric
    - post_publish_validation_metric

  supply_output_must_answer:
    - which_files_to_read_for_this_goal
    - what_risks_may_break_this_goal
    - what_old_context_may_conflict_with_this_goal
    - what_execution_choices_support_this_goal
    - what_execution_choices_violate_this_goal
    - which_editing_or_assembly_risks_may_break_post_publish_validation_metric
```

硬规则：

- DeepSeek 可以提醒旧口径风险，不能改写目标。
- DeepSeek 可以建议执行选择，不能决定项目事实。
- `fallback_local_only（本地兜底）` 不得写成 DeepSeek 结论。

## 6. bridge_to_codex_execution（桥接到 Codex 执行）

```yaml
bridge_to_codex_execution:
  current_instance_source:
    path: "codex_log/current_data_goal_anchor.md"
    rule: "Codex 先读当前实例锚点，再决定能否进入视频执行。"
  codex_must_preserve:
    - current_stage_goal
    - main_bottleneck
    - primary_variable
    - forbidden_variables
    - success_metric
    - failure_metric
    - post_publish_validation_metric

  codex_may_adapt:
    - segment_order
    - card_position
    - editing_style
    - assembly_sequence
    - material_binding
    - tts_segmentation
    - fallback_visuals
    - api_image_needed_or_not
    - ppt_density
        - degradation_plan（只能作为 blocked 后待用户授权的修复建议，不能作为完成结果）

  codex_must_not_adapt:
    - target_user_if_locked
    - current_stage_goal
    - main_bottleneck
    - primary_variable
    - forbidden_variables
    - validation_metric
    - user_or_chatgpt_locked_data_goal_judgment
```

Codex 最终回报必须包含：

```yaml
codex_execution_structure_policy:
  current_data_goal_anchor_path:
  current_data_goal_anchor_status:
  data_goal_anchor_used:
  execution_structure_adjustments:
  why_adjustments_do_not_break_primary_variable:
  forbidden_variables_avoided:
  post_publish_validation_metric:
  data_goal_alignment_check:
```

## 7. bridge_to_editing_and_assembly（桥接到剪辑与编排）

剪辑和装配不是只回答“怎么剪 / 放哪里”，还要回答“为什么这个动作服务本轮数据目标”。

```yaml
editing_decision_pack_must_include:
  - current_data_goal_anchor_source
  - data_goal_anchor_used
  - line_group_goal
  - primary_variable_support
  - evidence_role_for_metric
  - forbidden_visuals_by_goal
  - edit_action_reason_against_data_goal
  - post_publish_validation_metric

assembly_decision_pack_must_include:
  - current_data_goal_anchor_source
  - data_goal_anchor_used
  - segment_goal
  - carrier_reason
  - metric_supported
  - variable_preserved
  - forbidden_variable_avoided
  - post_publish_validation_metric
```

字段口径统一：

```yaml
forbidden_goal_field_alias_map:
  source_of_truth: forbidden_variables
  content_route_card_field: forbidden_variables_avoided
  script_to_timeline_map_field: forbidden_variables_avoided
  editing_decision_pack_field: forbidden_visuals_by_goal
  assembly_decision_pack_field: forbidden_variable_avoided
  validation_field: no_forbidden_variable_introduced
```

解释：

- `forbidden_variables（禁止变量）` 是上游数据目标锚点的源字段。
- `forbidden_variables_avoided（避开的禁止变量）` 用于内容路由卡和文案到时间线映射，说明本段没有改目标用户、offer、主题或其他禁止变量。
- `forbidden_visuals_by_goal（按目标禁用的画面）` 用于剪辑决策包，说明哪些画面 / 卡片 / 裁切动作会间接引入禁止变量。
- `forbidden_variable_avoided（避开的禁止变量）` 用于装配决策包，说明本段装配动作保留了目标变量。
- 上述字段名可以因对象不同而不同，但必须能回指同一个 `data_goal_anchor.forbidden_variables`；无法回指时必须 blocked。

阻断规则：

- 缺 `data_goal_anchor_used（使用的数据目标锚点）`，不得生成 `editing_decision_pack（剪辑决策包）`。
- 缺 `primary_variable_support（服务的主变量）`，不得把剪辑动作写成完成。
- 缺 `metric_supported（支持的指标）`，不得把装配动作写成完成。
- 引入 `forbidden_variables（禁止变量）` 的卡片、剪辑、素材或降级方案必须 blocked；任何降级方案都只能作为 blocked 后待用户授权的修复建议，不能作为完成结果。
- `forbidden_goal_field_alias_map` 无法追溯到同一个上游 `forbidden_variables` 时，必须 blocked。

## 8. validation（验收）

视频执行完成前必须输出 `data_goal_alignment_check（数据目标对齐检查）`。

```yaml
data_goal_alignment_check:
  current_data_goal_anchor_path:
  current_data_goal_anchor_status:
  every_segment_maps_to_goal:
  every_edit_supports_primary_variable:
  no_forbidden_variable_introduced:
  success_metric_visible_in_execution_plan:
  failure_metric_visible_in_risk_boundary:
  post_publish_validation_metric_defined:
  material_evidence_supports_claims:
  human_quality_review_not_replaced_by_data_goal:
  data_goal_not_claimed_as_real_flywheel_passed:
  delivery_baseline_gate:
    target_result:
    publish_candidate_requirements_checked:
    missing_capabilities:
    blocked_publish_candidate_unavailable:
```

完成判定：

- `data_goal_alignment_check` 缺失时，不得写执行完成。
- `data_goal_alignment_check` 必须检查 `codex_log/current_data_goal_anchor.md` 当前实例，而不只是抽象规则。
- `material_evidence_supports_claims` 未确认时，不得进入成片生成。
- `human_quality_review_not_replaced_by_data_goal` 未确认时，不得写 `send_ready = true`。
- `delivery_baseline_gate` 缺失时，不得写正式运营视频交付完成。
- `publish_candidate_requirements_checked` 未确认且本轮是视频交付任务时，只能写 `blocked_publish_candidate_unavailable` 或继续修，不能写技术预览完成。
- 本机制写入只能标记为 `已确认：机制已写入`，真实任务稳定运行必须继续标记为 `待验证`。
