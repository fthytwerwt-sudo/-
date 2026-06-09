# 参考到执行落地契约 Reference-to-Execution Contract

## 1. 文件定位

本文件负责把用户目标、`reference（参考）`、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考，转换成 Codex 可执行函数字段和可验证标准。

它不是 reference 仓库，不替代当前事实，不直接推进内容验证。

`Reference-to-Execution Contract（参考到执行落地契约）` 是一层中间机制：

```text
reference / 样片 / 用户目标
-> reference_anchor
-> effect_targets
-> function_fields
-> deviation_check
-> done_when
-> feedback_update
```

它解决的问题是：用户和 ChatGPT 已经给了 reference、样片或目标效果，但执行层只抓到表面风格，缺少可执行、可验证、可纠偏的字段。

## 2. 触发条件

出现以下任一情况，必须触发 `Reference-to-Execution Contract（参考到执行落地契约）`：

- 用户说“按这个参考做”。
- 用户给参考视频 / 参考图 / 参考声音 / 样片 / 原感稿 / 外部资料。
- 用户说“像这个效果”。
- 用户说“这次不要和 reference 偏离”。
- 任务涉及 `reference / locked reference / visual route / quality sample`。
- 任务涉及文案风格、剪辑效果、声音感觉、视觉外壳、卡片结构、节奏和人感。
- Codex 需要根据 reference 生成或修改产物。

如果触发条件成立，ChatGPT 不得把 reference 原样平移给 Codex，必须先生成本契约字段。

## 3. Ambiguous Reference Goal Gate（参考目标歧义闸门）

当 reference 任务出现“像 / 1:1 / 高级感 / 还原 / 不是一回事 / 按这个效果做 / 完全不像 / 差点意思 / 对标观感 / 参考视频观感”等表达时，必须先进入 `ambiguous_reference_goal_gate（参考目标歧义闸门）`。

先判断用户要继承的是哪一层：

```text
ambiguous_reference_goal_gate:
  trigger_terms:
    - 像
    - 1:1
    - 高级感
    - 还原
    - 不是一回事
    - 按这个效果做
    - 完全不像
    - 差点意思
    - 对标观感
    - 参考视频观感
  must_clarify_target_layer:
    - visual_look（第一眼视觉观感）
    - editing_rhythm（剪辑节奏）
    - layout_composition（构图布局）
    - subtitle_typography（字幕 / 字体）
    - highlight_motion（高亮 / 动效）
    - information_density（信息密度）
    - proof_logic（证明方式）
    - content_structure（内容结构）
    - emotional_tone（情绪 / 人感）
    - whole_piece_similarity（整体观感）
```

如果用户要视觉还原，必须进一步触发：

```text
visual_reference_contract:
  primary_reference_video:
  keyframe_set:
  composition_map:
  typography_map:
  motion_map:
  density_map:
  hierarchy_map:
  pacing_map:
  side_by_side_deviation_check:
```

缺这些字段，不得进入 Codex 成片执行。

```text
blocked_if:
  - 只有机制词，没有关键帧视觉标准
  - 多个参考视频未指定唯一主参考
  - 没有并排偏离检查
  - 没有说明哪些像、哪些不能像
  - 需要复制第三方资产才能像
  - 当前素材无法承载参考画面结构
  - 用户想要整体观感，但只下发了局部机制迁移

not_allowed:
  - 不得把“学到分屏 / 高亮 / 关键词”写成“接近参考”
  - 不得用机制名代替画面观感
  - 不得在 visual_reference_contract 缺失时下发完整成片执行
  - 不得把 reference_analysis draft 当成 formal reference execution standard
```

## 4. Reference Anchor（参考锚点）

`reference_anchor（参考锚点）` 用来锁住 reference 的来源、类型、可用性和继承边界。

```text
reference_anchor:
  reference_id:
  reference_type:
    - visual_reference
    - editing_reference
    - copywriting_reference
    - voice_reference
    - quality_reference
    - raw_feeling_reference
    - external_research_reference
  source_layer:
    - user_provided
    - repo_locked_reference
    - perplexity_reference_pack
    - previous_output_sample
  exact_reference_available:
  reference_path_or_description:
  must_preserve:
  can_vary:
  must_not_copy:
  fail_if_missing:
  blocked_if_reference_missing:
```

字段要求：

- `reference_id`：能复核的参考编号、文件名、路径、用户描述或外部资料标题。
- `reference_type`：必须选出 reference 的实际用途，不得只写“参考一下”。
- `source_layer`：必须说明它来自用户、仓库锁定 reference、Perplexity 外部资料包，还是上一轮样片。
- `exact_reference_available`：必须写 true / false；看不到原 reference 时不得写已按参考执行。
- `must_preserve`：必须保留的效果、功能或质量点。
- `can_vary`：允许变化的表达、尺寸、素材、段落、镜头或话术。
- `must_not_copy`：不能照抄、不能侵权、不能机械复刻、不能迁移的点。
- `fail_if_missing`：缺了就不算完成的 reference 要点。
- `blocked_if_reference_missing`：reference 缺失时是否阻断。

## 5. Effect Targets（效果目标）

`effect_targets（效果目标）` 用来把 reference 的“感觉像”拆成可验收目标。

```text
effect_targets:
  viewer_feeling:
  information_hierarchy:
  pacing:
  visual_weight:
  evidence_clarity:
  human_like_comfort:
  reference_quality_points:
  emotional_tone:
  not_allowed_effects:
```

字段要求：

- `viewer_feeling`：观众看完应该产生什么感受，例如清楚、轻松、有真实感、有结果差、有陪伴感。
- `information_hierarchy`：主信息、辅助信息、证据、情绪点的层级。
- `pacing`：节奏、停顿、镜头切换或文案推进速度。
- `visual_weight`：画面重心、卡片密度、人物 / 录屏 / 信息卡权重。
- `evidence_clarity`：真实证据是否清楚可见，是否被装饰素材抢走。
- `human_like_comfort`：声音、文案、节奏和画面是否让人舒服，不像硬播报或硬拼接。
- `reference_quality_points`：reference 真正有价值的质量点，不只写颜色或形状。
- `emotional_tone`：情绪口径，例如低压、轻吐槽、平静、可爱但不幼稚。
- `not_allowed_effects`：不允许出现的效果，例如 AI 感、水印感、说明书感、过度 PPT 感、假证据感。

## 6. Function Fields（执行函数字段）

`function_fields（执行函数字段）` 用来让 Codex 在执行前知道：输入信号是什么、该做什么、为什么做、怎么验收、失败时怎么回退。

```text
function_fields:
  input_signal:
  evidence_role:
  importance_type:
  target_area:
  selected_action:
  action_reason:
  validation_rule:
  blocked_if:
  fallback_action:
  feedback_update:
```

字段要求：

- `input_signal`：触发本契约的用户表达、reference、样片、素材或外部资料。
- `evidence_role`：reference 在本轮是质量锚点、执行样式、反例、语气锚点、节奏锚点还是研究线索。
- `importance_type`：必须继承、可选继承、只作反例、只作外部参考。
- `target_area`：作用到视觉、文案、声音、剪辑、质量复审、素材验收、装配或复盘。
- `selected_action`：执行侧要采取的具体动作。
- `action_reason`：为什么这个动作能保护 reference 的关键效果。
- `validation_rule`：执行后如何检查是否达到效果目标。
- `blocked_if`：什么情况必须停。
- `fallback_action`：reference 缺失、冲突或不可比时的降级动作。
- `feedback_update`：结果如何写回 latest、dated log、review pack 或下一轮任务。

## 7. Execution Mapping（执行映射）

不同任务类型必须先生成对应 contract，再进入具体执行：

```text
editing_task:
  must produce editing_reference_contract before editing

copywriting_task:
  must produce copy_reference_contract before final draft

visual_task:
  must produce visual_reference_contract before image / card / layout generation

card_visual_reference_task:
  must produce card_visual_reference_contract before judgment_card / summary_card / result_diff_card / prompt_tail_card generation or validation
  must bind social_editorial_card_v1 when user confirms 16:9 Douyin + Ins social editorial direction
  must separate reference quality points from copied text / copied character / copied layout

voice_task:
  must produce voice_reference_contract before TTS / voice validation

quality_review_task:
  must produce quality_reference_contract before pass / fail judgment
```

执行映射要求：

- `editing_task（剪辑任务）`：先说明 reference 的节奏、切点、证据窗口、不能偏离的观感，再决定放大、裁切、定格、插卡或不动。
- `copywriting_task（文案任务）`：先提取原感、句式、情绪、信息层级和不可丢失的用户目标，再写成稿。
- `visual_task（视觉任务）`：先锁视觉外壳职责、密度、角色权重、卡片层级和禁用效果，再生成图片 / 卡片 / layout。
- `card_visual_reference_task（卡片视觉参考任务）`：先锁 `social_editorial_card_v1（社交编辑感卡片 V1）` 的横屏比例、信息密度、字体层级、社交编辑感、证据保护和失败路由，再生成或验收判断卡 / 总结卡 / 结果差卡 / Prompt 尾卡。
- `voice_task（声音任务）`：先拆 `tts_pacing_reference（TTS 节奏参考）` 与 `tts_voice_reference（TTS 音色参考）`，不得把候选音色写成最终通过。
- `quality_review_task（质量复审任务）`：先用 reference contract 定义 pass / fail 的对照点，再做质量判断。

## 7A. card_visual_reference_contract（卡片视觉参考契约）

当用户给出或确认卡片视觉参考图、卡片 reference、卡片样片或“按这个卡片效果做”时，必须先输出本契约，再进入卡片生成或卡片验收。

```text
card_visual_reference_contract:
  reference_anchor:
    reference_id:
    reference_type:
      - card_visual_reference
      - social_editorial_card_reference
    source_layer:
      - user_approved_visual_reference
      - repo_locked_reference
    exact_reference_available:
    repo_reference_path:
    historical_local_source_path:
    remote_reference_status:
    local_reference_only_allowed_for_default_claim: false
    reference_path_or_description:
    reference_role: visual_quality_anchor_only
    blocked_if_reference_missing:
  effect_targets:
    aspect_ratio_default: horizontal_16_9
    resolution_default: 1920x1080
    forbidden_default: vertical_9_16
    visual_feel:
      - douyin_retention_feel
      - instagram_clean_editorial_feel
      - low_saturation_quality
      - social_short_video_component
    typography_hierarchy:
      main_claim_readable_within_1s: true
      supporting_text_understandable_within_3s: true
      highlight_words_max: 2
    decorative_weight:
      allowed_minor_elements:
        - original_voxel_character
        - pixel_heart
        - doodle_line
        - rounded_pill_tag
      must_not_dominate_main_information: true
    must_not_feel_like:
      - ppt_page
      - engineering_dashboard
      - mechanical_game_ui
      - cyber_hud
      - cheap_template
  function_fields:
    target_cards:
      - judgment_card
      - summary_card
      - result_diff_card
      - prompt_tail_card
    card_placement_decision_required: true
    card_budget_gate_required: true
    evidence_window_protection_required: true
    locked_copy_semantic_match_required: true
    card_visual_route_selected_required: true
    visual_base_route_required: true
    text_authority_route_required: true
    motion_wrapper_route_required: true
    hyperframes_runtime_gate_required_if_motion_wrapper_selected: true
    image2_visual_only_not_text_authority: true
    post_overlay_locked_copy_check_required: true
    exact_text_fallback_required_if_image2_text_unstable: true
    implementation_design_layer_required: true
    implementation_design_layer_fields:
      - target_effect
      - codex_capability_boundary
      - preferred_execution_route
      - fallback_routes
      - capability_probe_tasks
      - done_when
      - blocked_if
    static_fallback_requires_user_authorization: true
    copy_change_request_required_if_text_needs_semantic_rewrite: true
    card_visual_implementation_example:
      preferred_visual_base_route_candidate: image2_visual_base_route_candidate
      image2_boundary: 只负责主视觉 / 底图 / 构图 / 质感 / 社交编辑感；本轮用户人工反馈样张审美可过关，但不得写成长期稳定通过。
      text_authority_route: Codex 后期叠准确 locked copy；HTML/CSS/PIL 可作为 exact_text_fallback。
      hyperframes_boundary: 仅作为 optional motion_wrapper / auxiliary_motion_route / card_motion_layer；只有 motion_wrapper_route = HyperFrames_motion_wrapper 时才检查 runtime gate。
      exact_text_fallback: HTML/CSS 截图或 PIL 生成 1920x1080 准确文字层；不得冒充 HyperFrames 动效。
      blocked_route: image2 文字无法移除或准确覆盖、会改 locked copy、生成素材没有的数据 / 结论、遮挡证据、偏离 social_editorial_card_v1、复用第三方资产或缺用户授权降级时 blocked。
  deviation_check:
    differs_from_reference_where:
    acceptable_variation:
      - different_copy
      - different_character
      - different_icon
      - different_layout_position
      - locally_adjusted_card_count
    unacceptable_deviation:
      - vertical_9_16_default
      - ppt_feel
      - mechanical_game_ui
      - dashboard_feel
      - main_information_not_readable
      - evidence_window_covered
      - copied_third_party_asset
  done_when:
    - reference_anchor_locked
    - effect_targets_filled
    - function_fields_filled
    - card_visual_quality_gate_done
    - card_content_boundary_gate_done
    - no_forbidden_status_promotion
```

已确认参考图：`素材录制-卡片参考-ChatGPT Image 2026年6月4日 02_29_58` 只锁视觉方向，不锁具体文案、具体人物、具体图标、具体排版位置或任何第三方可识别资产。默认 repo reference path 为 `references/card_style/social_editorial_card_v1_reference.png`；旧本地来源 `素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png` 只可写为 `historical_local_source_path（历史本地来源路径）`，不得在未进入远端 main 时写成 remote readable reference。

## 8. Deviation Check（偏离检查）

`deviation_check（偏离检查）` 用来判断执行结果是否偏离 reference 的关键效果。

```text
deviation_check:
  differs_from_reference_where:
  acceptable_variation:
  unacceptable_deviation:
  repair_required:
  cannot_compare_reason:
  human_review_required:
```

硬规则：

- 如果 reference 缺失，不能说“已按参考执行”。
- 如果 reference 只是外部资料，不得写成 repo 已确认事实。
- 如果执行结果与 reference 关键效果偏离，不能写 `completed`。
- 如果只是颜色 / 形状像，但效果目标不一致，必须写 `deviation（偏离）`。
- 如果 reference 与当前项目状态冲突，以当前项目事实和 `Project State Action Router（项目状态动作总控器）` 裁决为准。
- 如果无法比较，必须写 `cannot_compare_reason（无法比较原因）`，不得把无法比较写成符合 reference。
- 如果偏离需要用户审美判断，必须写 `human_review_required = true`。

## 9. Done When（完成验收）

带 reference 的任务只有满足以下条件，才能写完成：

```text
done_when:
  reference_anchor_locked:
  effect_targets_filled:
  function_fields_filled:
  deviation_check_done:
  user_goal_preserved:
  no_forbidden_status_promotion:
  remaining_deviation_list_empty_or_explained:
```

验收解释：

- `reference_anchor_locked`：reference 的来源、类型、可用性和保留边界已经写清。
- `effect_targets_filled`：效果目标不空，不只写“风格类似”。
- `function_fields_filled`：Codex 已知道执行动作、理由、验证规则和阻断条件。
- `deviation_check_done`：执行后已经检查偏离。
- `user_goal_preserved`：用户真正想要的效果没有被表面风格覆盖。
- `no_forbidden_status_promotion`：没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `remaining_deviation_list_empty_or_explained`：剩余偏离为空，或已解释为什么暂时接受 / 待用户复审。

## 10. 与现有机制的关系

`Reference-to-Execution Contract（参考到执行落地契约）` 与现有机制分工如下：

- `Project State Action Router（项目状态动作总控器）`：判断当前是否进入 `reference_contract_needed（需要参考到执行契约）` 状态。
- `Reference-to-Execution Contract`：把 reference 拆成可执行字段和可验收标准。
- `Completion Relay Gate（补全接力闸门）`：保证契约相关交付项被做完、被验证、被回写。
- `DeepSeek（只读供料层）`：可帮助压缩文字化资料、列风险和文件地图，但不替代 contract。
- `Perplexity（外部研究层）`：可形成外部 reference pack 或 raw feeling draft，但不得直接升级成项目已确认事实。
- `Codex（唯一写入执行层 / Integrator）`：按 contract 执行、偏离检查、验证、日志和 Git 收尾。

## 11. 最小输出模板

每次用户给 reference 后，ChatGPT / GPT Project 至少输出：

```text
reference_to_execution_contract:
  ambiguous_reference_goal_gate:
  reference_anchor:
    reference_id:
    reference_type:
    source_layer:
    exact_reference_available:
    reference_path_or_description:
    must_preserve:
    can_vary:
    must_not_copy:
    fail_if_missing:
    blocked_if_reference_missing:
  effect_targets:
    viewer_feeling:
    information_hierarchy:
    pacing:
    visual_weight:
    evidence_clarity:
    human_like_comfort:
    reference_quality_points:
    emotional_tone:
    not_allowed_effects:
  function_fields:
    input_signal:
    evidence_role:
    importance_type:
    target_area:
    selected_action:
    action_reason:
    validation_rule:
    blocked_if:
    fallback_action:
    feedback_update:
  execution_mapping:
  deviation_check:
  done_when:
  blocked_if:
```

## 12. 一句话规则

**凡是用户给 reference / 样片 / 原感稿 / 外部资料并要求 Codex 落地，必须先判断 reference 目标是否清楚；目标含糊时先过 `ambiguous_reference_goal_gate（参考目标歧义闸门）`，目标清楚后再生成 `Reference-to-Execution Contract（参考到执行落地契约）`；没有契约，不进入执行。**
