# 剪辑参数包与镜头选择标准 Editing Profile And Shot Selection Rules

## 1. 文件定位

本文件只定义 `editing_profile_system（剪辑参数包系统）`，服务剪辑层。

它参考 `GPT数据源/05_文案路由规则.md（文案路由规则）` 的组织方式，但不复制文案规则内容，不替代文案路由，不生成视频，不改最终文案，不推进任何内容 / 发布 / 声音 / 视觉状态。

固定关系：

```text
shot_selection_quantitative_rules（镜头选择量化规则）
= 通用评分尺

editing_profile（剪辑参数包）
= 当前片型的剪辑偏好

script_to_shot_execution_map（文案到镜头执行表）
= 当前这条片子的具体镜头安排
```

固定原则：

```text
通用底线少动
类型参数可调
单条镜头表负责落地
```

## 2. 剪辑类型分类

```yaml
editing_video_type:
  general_content:
    profile_id: default_general_content_v1
    status: active_default

  daily_tutorial:
    profile_id: daily_tutorial_profile_v1
    status: draft_profile_ready_for_first_real_video_test

  ecommerce:
    profile_id: ecommerce_profile_v1
    status: placeholder_pending_detail

  tutorial_or_tool_process:
    profile_id: tutorial_profile_v1
    status: placeholder_pending_detail

  daily_vlog:
    profile_id: daily_vlog_profile_v1
    status: placeholder_pending_detail
```

`daily_tutorial（日常化教学）` 不等于 `daily_vlog（日常 / Vlog）`：

- `daily_tutorial`：用日常真实场景降低压力，用教学结构交付一个可模仿的小动作。
- `daily_vlog`：以日常记录、陪伴、情绪和生活流为主，本轮仍只占位，不填完整参数。

## 3. 当前默认剪辑交付包

```yaml
default_editing_delivery_pack:
  editing_profile_selected: 剪辑前已选择参数包。
  material_parse_pack: 复用同一份素材解析包。
  source_segment_inventory: 从素材片段清单选择镜头。
  script_to_shot_execution_map: 逐 line_group 写明 profile_id 和镜头安排。
  material_usage_ledger: 记录每段素材使用位置和复用理由。
  duplicate_material_check: 检查无理由复用、连续复用、核心证据复用。
  editing_decision_pack: 汇总剪辑选择和阻断原因。
  visual_readability_report: 检查核心画面、字幕、卡片可读性。
  review_pack: 交给用户 / ChatGPT 复审，不等于内容通过。
```

缺任一项，不得写剪辑完成。这些是剪辑前 / 剪辑后交接件，不代表 `content_validation（内容验证）`、`send_ready（可发送状态）` 或真实审美效果通过。

## 4. editing_profile_schema（剪辑参数包结构）

```text
editing_profile_schema:
  profile_id（参数包编号）: 唯一编号，必须写入 script_to_shot_execution_map。
  profile_name（参数包名称）: 人类可读名称。
  video_type（视频类型）: 当前参数包服务的内容形式。
  target_viewer_action（观众目标动作）: 观众看完后应做的动作或判断。
  rhythm_density（节奏密度）: low / medium_low / medium / high；控制镜头切换与信息推进速度。
  evidence_requirement（证据强度要求）: low / medium / medium_high / high；控制画面证据硬度。
  readability_priority（可读性优先级）: low / medium / high；控制表格、页面、字幕、卡片是否优先可读。
  emotion_priority（情绪优先级）: low / medium / medium_high / high；控制人感、吐槽、陪伴感权重。
  card_density_limit（卡片密度限制）: low / low_to_medium / medium / high；限制解释卡、判断卡、总结卡密度。
  material_reuse_limit（素材复用限制）: 限制同一素材片段和核心证据复用。
  music_beat_weight（音乐卡点权重）: low / low_to_medium / medium / high；控制音乐节拍对剪辑的影响。
  motion_intensity（运动强度）: low / low_to_medium / medium / high；控制放大、裁切、转场、动效强度。
  text_density_limit（文字密度限制）: low / low_to_medium / medium / high；限制同屏文字数量和叠层。
  shot_selection_threshold（镜头选择阈值）: 最低可选镜头分数；低于阈值必须替换或 blocked。
  fallback_policy（兜底策略）: 缺素材、参数冲突或 profile 占位时如何处理。
  blocked_if（阻断条件）: 触发后不得进入剪辑、装配或完成态。
```

## 5. default_editing_profile（默认剪辑参数包）

`default_general_content_v1（默认通用内容参数包）` 只作为 v1 通用兜底，不代表所有片型最终标准。具体片型可以覆盖参数。

```yaml
default_editing_profile:
  profile_id: default_general_content_v1
  profile_name: 默认通用内容参数包
  video_type: general_content
  target_viewer_action: understand_and_continue_review
  rhythm_density: medium
  evidence_requirement: medium_high
  readability_priority: high
  emotion_priority: medium
  card_density_limit: medium
  music_beat_weight: low_to_medium
  motion_intensity: medium
  text_density_limit: medium
  shot_selection_threshold:
    minimum_total_score: 0.70
    minimum_evidence_score: 0.75
    minimum_readability_score: 0.75
  material_reuse_limit:
    max_same_segment_usage_count: 2
    max_same_core_evidence_usage_count: 1
    max_consecutive_same_segment_count: 1
    max_reused_segment_ratio: 0.15
    require_reuse_reason: true
  fallback_policy:
    if_video_type_unspecified: use_default_general_content_v1
    if_placeholder_profile_used: inherit_default_general_content_v1_and_mark_profile_detail_pending
    if_profile_conflicts_with_user_instruction: blocked_profile_conflict
  blocked_if:
    - editing_profile_missing
    - profile_id_missing_in_script_to_shot_execution_map
    - profile_placeholder_used_without_inheritance
    - profile_conflicts_with_user_instruction
```

## 6. profile_registry（参数包注册表）

```yaml
profile_registry:
  default_general_content_v1:
    video_type: general_content
    status: active_default
    parent_profile: none
    fill_later: false

  daily_tutorial_profile_v1:
    video_type: daily_tutorial
    status: draft_profile_ready_for_first_real_video_test
    parent_profile: default_general_content_v1
    fill_later: false

  ecommerce_profile_v1:
    video_type: ecommerce
    status: placeholder_pending_detail
    parent_profile: default_general_content_v1
    fill_later: true

  tutorial_profile_v1:
    video_type: tutorial_or_tool_process
    status: placeholder_pending_detail
    parent_profile: default_general_content_v1
    fill_later: true

  daily_vlog_profile_v1:
    video_type: daily_vlog
    status: placeholder_pending_detail
    parent_profile: default_general_content_v1
    fill_later: true
```

`daily_tutorial_profile_v1（日常化教学剪辑参数包）` 已有草案参数，等待第一条真实视频验证；`ecommerce_profile_v1 / tutorial_profile_v1 / daily_vlog_profile_v1` 本轮仍为占位，不填完整参数。

## 7. profile_selection_rule（参数包选择规则）

```text
before_editing:
  - 必须先选择一个 editing_profile（剪辑参数包）。
  - 如果用户明确指定 daily_tutorial（日常化教学），优先使用 daily_tutorial_profile_v1。
  - 如果用户明确指定其他视频类型，优先使用对应 profile。
  - 如果对应 profile 仍是 placeholder_pending_detail（占位，待细化），必须继承 default_general_content_v1，并标记 profile_detail_pending（参数细节待补）。
  - 如果用户未指定视频类型，默认使用 default_general_content_v1。
  - 每条视频的 script_to_shot_execution_map（文案到镜头执行表）必须写明 profile_id（参数包编号）。

blocked_if:
  - editing_profile_missing
  - profile_id_missing_in_script_to_shot_execution_map
  - profile_placeholder_used_without_inheritance
  - profile_conflicts_with_user_instruction
```

`script_to_shot_execution_map（文案到镜头执行表）` 最小 profile 字段：

```yaml
script_to_shot_execution_map:
  profile_id: daily_tutorial_profile_v1
  profile_detail_pending: false
  profile_source: codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md
  line_groups:
    - line_group_id:
      narration_text:
      selected_segment_id:
      expected_visual:
      shot_selection_score:
      profile_constraints_checked:
      blocked_if_visual_mismatch:
```

## 8. profile_override_rule（参数覆盖规则）

```text
general_baseline（通用底线）:
  - 只在连续多个视频出现同类错误时修改。
  - 不能因为单条视频审美偏好就改通用底线。

video_type_profile（视频类型参数包）:
  - 当某类视频反复需要不同节奏 / 证据 / 卡片 / 复用限制时修改。
  - 例如电商、教学、日常化教学、日常 Vlog 分别细化。

single_video_map（单条视频镜头表）:
  - 单条视频的镜头安排默认只改 script_to_shot_execution_map（文案到镜头执行表）。
  - 不应因为单条视频某个镜头不满意就改全局标准。
```

## 9. daily_tutorial_profile_v1（日常化教学剪辑参数包）

```yaml
daily_tutorial_profile_v1:
  status: draft_profile_ready_for_first_real_video_test
  parent_profile: default_general_content_v1
  video_type: daily_tutorial
  definition: 用日常真实场景降低压力，用教学结构交付一个可模仿的小动作。
  target_viewer_action:
    - 看完后能模仿一个小动作
    - 看完后知道下一步点哪里 / 怎么做 / 怎么判断
    - 感觉不是上课，而是有人在旁边顺手带着过一遍
  rhythm_density: medium_low
  evidence_requirement: medium_high
  readability_priority: high
  emotion_priority: medium_high
  card_density_limit: low_to_medium
  music_beat_weight: low
  motion_intensity: low_to_medium
  text_density_limit: low_to_medium
  shot_selection_threshold:
    primary_shot_min_total_score: 72
    teaching_action_min_evidence_score: 24/30
    teaching_action_min_readability_score: 16/20
    daily_context_min_total_score: 58
    transition_shot_min_total_score: 55
  material_reuse_limit:
    max_same_segment_usage_count: 2
    max_same_core_evidence_usage_count: 1
    max_consecutive_same_segment_count: 1
    max_reused_segment_ratio: 0.18
    max_background_context_ratio: 0.25
    require_reuse_reason: true
```

`daily_tutorial_profile_v1` 是草案参数包，只能进入第一条真实日常化教学视频测试；不得写成已验证稳定。

### daily_tutorial_structure（日常化教学结构）

```yaml
daily_tutorial_structure:
  daily_scene_hook:
    goal: 让观众觉得“这就是我会遇到的情况”
    duration_hint: 3-6s

  problem_touch:
    goal: 说清哪里卡住
    duration_hint: 4-8s

  one_small_action:
    goal: 教一个可模仿动作
    duration_hint: 10-25s

  result_or_change:
    goal: 让观众看到做完有什么不同
    duration_hint: 6-12s

  soft_summary:
    goal: 留下一句能记住的话
    duration_hint: 3-6s

  low_pressure_next_step:
    goal: 给一个很小的行动，不强卖
    duration_hint: 2-5s
```

## 10. 日常化教学镜头职责分配

```yaml
daily_tutorial_visual_role_rules:
  daily_hook:
    preferred_visual_role:
      - daily_context
      - emotion_hook
    forbidden_visual_role:
      - dense_instruction_card

  teaching_action:
    preferred_visual_role:
      - process_demo
      - direct_evidence
    blocked_if:
      - 关键按钮 / 输入 / 结果不可见
      - 只有主题相关素材

  mistake_warning:
    preferred_visual_role:
      - boundary_card
      - judgment_card
      - short_process_evidence
    rule:
      - 不用长录屏解释误区，优先短卡片 + 关键画面

  result_reveal:
    preferred_visual_role:
      - result_showcase
      - comparison
    blocked_if:
      - 没有结果画面却硬说结果差

  soft_summary:
    preferred_visual_role:
      - summary_card
      - daily_context_recall
    rule:
      - 总结卡最多 1 屏，不做多层复杂总结
```

## 11. 日常化教学素材复用限制

```yaml
daily_tutorial_reuse_policy:
  allowed_reuse_reason:
    - same_action_recap
    - before_after_comparison
    - result_recall
    - context_reestablish
    - rhythm_callback

  forbidden_reuse_reason:
    - theme_related
    - looks_good
    - no_better_material
    - convenient
    - filler

  blocked_if:
    - same_segment_reused_without_reuse_reason
    - same_core_evidence_reused_for_different_claim
    - consecutive_same_segment_used
    - background_context_used_as_direct_evidence
```

## 12. 进入日常化教学剪辑前必须回答的问题

```text
daily_tutorial_pre_edit_questions:
  1. 这条视频的日常场景是什么？
  2. 观众看完要模仿的一个小动作是什么？
  3. 哪个镜头承担教学动作？
  4. 哪个镜头承担结果变化？
  5. 哪些镜头只是日常上下文，不能当直接证据？
  6. 哪些地方需要卡片承接，而不是硬塞录屏？
  7. 是否存在无理由复用素材？
  8. 是否存在教程腔压过日常感？
```

缺这些回答时，可以准备素材或补问题，但不得写剪辑完成。

## 13. 与 preflight 的关系

`editing_profile_preflight（剪辑参数包预检）` 只做结构检查：

- `script_to_shot_execution_map（文案到镜头执行表）` 是否包含 `profile_id（参数包编号）`。
- `profile_id（参数包编号）` 是否能在 `profile_registry（参数包注册表）` 找到。
- `placeholder_pending_detail（占位，待细化）` profile 是否继承 `default_general_content_v1（默认通用内容参数包）`。
- `daily_tutorial_profile_v1（日常化教学剪辑参数包）` 是否被识别为 `draft_profile_ready_for_first_real_video_test`，且不是 `daily_vlog_profile_v1（日常 / Vlog 剪辑参数包）`。

通过该结构检查不代表剪辑审美已经稳定，也不代表真实成片效果通过。

## 14. 一句话规则

```text
先选 editing_profile，再做 script_to_shot_execution_map；
日常化教学用 daily_tutorial_profile_v1；
日常场景只负责降压，教学动作必须有可读证据；
单条不满意先改镜头表，不先改通用底线。
```
