# 剪辑参数包与镜头选择标准 Editing Profile And Shot Selection Rules

## 1. 文件定位

本文件只定义 `editing_profile_system（剪辑参数包系统）` 的基础结构。

它不生成视频、不改文案、不细化所有片型参数、不推进任何内容 / 发布 / 声音 / 视觉状态。

关系固定如下：

```text
shot_selection_quantitative_rules（镜头选择量化规则）
= 通用评分尺

editing_profile（剪辑参数包）
= 当前片型的剪辑偏好

script_to_shot_execution_map（文案到镜头执行表）
= 当前这条片子的具体镜头安排
```

原则固定为：

```text
通用底线少动
类型参数可调
单条镜头表负责落地
```

## 2. editing_profile_schema（剪辑参数包结构）

```text
editing_profile_schema:
  profile_id（参数包编号）: 唯一编号，必须写入 script_to_shot_execution_map。
  profile_name（参数包名称）: 人类可读名称。
  video_type（视频类型）: 当前参数包服务的内容形式。
  target_viewer_action（观众目标动作）: 观众看完后应做的动作或判断。
  rhythm_density（节奏密度）: low / medium / high；控制镜头切换与信息推进速度。
  evidence_requirement（证据强度要求）: low / medium / medium_high / high；控制画面证据硬度。
  readability_priority（可读性优先级）: low / medium / high；控制表格、页面、字幕、卡片是否优先可读。
  emotion_priority（情绪优先级）: low / medium / high；控制人感、吐槽、陪伴感权重。
  card_density_limit（卡片密度限制）: low / medium / high；限制解释卡、判断卡、总结卡密度。
  material_reuse_limit（素材复用限制）: 限制同一素材片段和核心证据复用。
  music_beat_weight（音乐卡点权重）: low / low_to_medium / medium / high；控制音乐节拍对剪辑的影响。
  motion_intensity（运动强度）: low / medium / high；控制放大、裁切、转场、动效强度。
  text_density_limit（文字密度限制）: low / medium / high；限制同屏文字数量和叠层。
  shot_selection_threshold（镜头选择阈值）: 最低可选镜头分数；低于阈值必须替换或 blocked。
  fallback_policy（兜底策略）: 缺素材、参数冲突或 profile 占位时如何处理。
  blocked_if（阻断条件）: 触发后不得进入剪辑、装配或完成态。
```

## 3. default_editing_profile（默认剪辑参数包）

`default_general_content_v1（默认通用内容参数包）` 只作为 v1 通用默认，不代表所有片型最终标准。后续具体片型可以覆盖这些参数。

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

## 4. profile_registry（参数包注册表）

本轮只预留入口，不展开电商 / 教学 / 日常完整参数。

```yaml
profile_registry:
  default_general_content_v1:
    video_type: general_content
    status: active_default
    parent_profile: none
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

## 5. profile_selection_rule（参数包选择规则）

```text
before_editing:
  - 必须先选择一个 editing_profile（剪辑参数包）。
  - 如果用户明确指定视频类型，优先使用对应 profile。
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
  profile_id: default_general_content_v1
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

## 6. profile_override_rule（参数覆盖规则）

```text
general_baseline（通用底线）:
  - 只在连续多个视频出现同类错误时修改。
  - 不能因为单条视频审美偏好就改通用底线。

video_type_profile（视频类型参数包）:
  - 当某类视频反复需要不同节奏 / 证据 / 卡片 / 复用限制时修改。
  - 例如电商、教学、日常分别细化。

single_video_map（单条视频镜头表）:
  - 单条视频的镜头安排默认只改 script_to_shot_execution_map（文案到镜头执行表）。
  - 不应因为单条视频某个镜头不满意就改全局标准。
```

## 7. 与 preflight 的关系

`editing_profile_preflight（剪辑参数包预检）` 只做结构检查：

- `script_to_shot_execution_map（文案到镜头执行表）` 是否包含 `profile_id（参数包编号）`。
- `profile_id（参数包编号）` 是否能在 `profile_registry（参数包注册表）` 找到。
- `placeholder_pending_detail（占位，待细化）` profile 是否继承 `default_general_content_v1（默认通用内容参数包）`。

通过该结构检查不代表剪辑审美已经稳定，也不代表真实成片效果通过。
