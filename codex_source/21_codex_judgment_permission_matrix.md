# Codex 判断权限表 codex_judgment_permission_matrix

## 1. 文件定位

`已确认` 本文件是《视频工厂》Codex 执行层的判断权限表。

它回答四个问题：

1. 哪些判断 Codex 必须自己做，并可以直接执行。
2. 哪些判断 Codex 必须自己做，但只能输出 `copy_change_request（文案修改请求）`。
3. 哪些判断 Codex 必须自己做，并在命中风险时 `blocked（阻断）`。
4. 哪些判断必须升级给 ChatGPT / 用户，Codex 不得擅自拍板。

本文件不授权 Codex 改写 `locked_topic（锁定选题）`、`locked_title（锁定标题）`、`locked_opening_line（锁定开头句）`、`locked_final_script（锁定最终口播稿）` 的语义、核心判断、数据目标、发布状态或内容通过状态。

## 2. 权限四层

```text
codex_judgment_permission_layers:
  must_decide_and_execute:
    meaning: Codex 必须判断，并可在不改变锁定文案语义和项目状态的前提下执行。
    examples:
      - opening_route_decision
      - card_placement_decision
      - script_to_timeline_map
      - subtitle_segmentation
      - tts_prosody
      - aspect_ratio_resolution

  must_decide_but_request_change:
    meaning: Codex 必须判断问题是否存在，但一旦需要改文案语义、标题、核心观点或数据目标，只能输出 copy_change_request。
    examples:
      - copy_change_request
      - visual_mismatch
      - material_evidence insufficiency
      - data_goal_alignment conflict

  must_decide_and_block:
    meaning: Codex 必须判断是否命中阻断线；命中后不得用技术预览、fallback、普通静态卡片或局部产物冒充完成。
    examples:
      - publish_candidate_readiness failed
      - material_evidence missing
      - HyperFrames required but runtime missing
      - high severity subtitle/card overlap

  must_escalate_to_chatgpt_or_user:
    meaning: 涉及内容方向、核心观点、标题语义、数据目标拍板、是否可发或主观审美最终判断时，Codex 必须升级。
    examples:
      - human_review_required
      - semantic copy rewrite
      - send_ready
      - content_validation
      - data_goal strategy conflict
```

## 3. Perplexity 参考修正

```text
perplexity_reference_correction:
  opening_route:
    external_pack_claim: Codex 不应自主判断 opening route
    project_decision: 本项目中 Codex 必须通过 content_route_inference_function 判断 opening_route_decision
    boundary: Codex 可判断开头路线，但不能改 locked_opening_line / locked_title / core_claim

  judgment_card:
    external_pack_claim: Codex 只能根据判断句触发，不应决定不需要 judgment_card
    project_decision: 本项目中 Codex 必须判断是否需要 judgment_card；加与不加都必须说明依据
    boundary: 不得让 judgment_card 替代真实录屏证据，不得改写判断句语义

  summary_card:
    project_decision: Codex 必须判断是否需要 summary_card；如果结尾一句话已自然收住，可不强行插卡，但必须说明理由
    boundary: 总结卡不得写成 content_validation 通过证据
```

Perplexity 只能作为 `external_research_reference（外部研究参考）`，不得直接升级为仓库事实。若 Perplexity 与本文件、`content_route_inference_function（内容路由推理函数）` 或当前正式事实冲突，以仓库文件为准。

## 4. 判断对象权限矩阵

### 4.1 opening_route_decision（开头路由判断）

```text
judgment_object: opening_route_decision
codex_permission: must_decide_and_execute
codex_must_do:
  - 通过 content_route_inference_function 判断 element_doll_opening / meme_gif_opening_hook / direct_question_title_card / screen_first_opening
  - 说明 route_reason、fallback_route、not_allowed
  - 确认开头只负责抓眼、抛问题或建立情绪，不替代中段真实证据
codex_must_not_do:
  - 不得把元素娃娃、梗图 GIF 或任一 reference 写成所有内容唯一默认
  - 不得改 locked_opening_line、locked_title、core_claim
change_request_if:
  - 锁定开头句太长、无法被画面承载、或和素材证据冲突
blocked_if:
  - opening_route_unclear
  - selected route requires visual hook but opening_visual_hook_spec missing
record_to:
  - content_route_card V2.opening_route_decision
  - codex_log dated log if route rule changed
validation_rule:
  - route_reason 清楚，且没有把开头 hook 写成 proof
```

### 4.2 card_placement_decision（卡片位置判断）

```text
judgment_object: card_placement_decision
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断 card_type、copy_function、selected_position、evidence_dependency、interrupt_risk
  - 判断是否需要 judgment_card / summary_card / result_diff_card / boundary_card / prompt_tail_card
  - 判断是否要求 HyperFrames 动效基线
codex_must_not_do:
  - 不得先固定旧 shot、旧 template 或旧 reference 时间点
  - 不得让卡片抢中段真实证据窗口
change_request_if:
  - 卡片文案需要语义改写才能承载
blocked_if:
  - card_position_unclear
  - card overlaps subtitles or key evidence
  - HyperFrames required but runtime missing and no user authorization for fallback
record_to:
  - content_route_card V2.card_placement_decision
  - script_to_timeline_map.card_text_if_any
validation_rule:
  - 每张卡片必须有 copy_function、evidence_dependency、interrupt_risk 和 blocked_if
```

### 4.3 judgment_card（判断卡）

```text
judgment_object: judgment_card
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断是否需要强化核心判断句 / 关键定性句
  - 若选择 judgment_card，默认触发 hyperframes_card_motion_baseline
  - 绑定 line_group_id 与 copy_function = core_claim / judgment / boundary_statement
codex_must_not_do:
  - 不得改写判断句语义
  - 不得把 judgment_card 写成真实证据、平台数据或 content_validation 通过
change_request_if:
  - 判断句本身需要改写、缩短或换语气
blocked_if:
  - judgment_card 会打断证据窗口
  - HyperFrames runtime missing and HyperFrames required
record_to:
  - card_placement_decision.card_plan
  - hyperframes_card_motion_baseline
validation_rule:
  - 加与不加都必须说明依据；加卡必须通过 card_text_semantic_match
```

### 4.4 summary_card（总结卡）

```text
judgment_object: summary_card
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断是否需要收束观点、给最小行动、帮助观众记住本条内容
  - 若选择 summary_card，默认触发 hyperframes_card_motion_baseline
  - 如果结尾一句话已自然收住，可不强插，但必须说明理由
codex_must_not_do:
  - 不得每条视频固定强插 summary_card
  - 不得替代 Prompt 尾卡职责
  - 不得写成内容通过或可发送证据
change_request_if:
  - 结尾句需要语义重写才能成立
blocked_if:
  - summary_card 会覆盖关键证据、字幕或 OCR
  - HyperFrames required but unavailable
record_to:
  - content_route_card V2.card_placement_decision.summary_card_usage
validation_rule:
  - evidence_window_closed = true，且不新增素材里没有的数据结论
```

### 4.5 result_diff_card（结果差卡）

```text
judgment_object: result_diff_card
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断是否需要翻译前后差异、普通做法 vs 改进做法
  - 只呈现素材已经证明的可感知差异
codex_must_not_do:
  - 不得新增素材里没有的数据结论
  - 不得冒充真实平台数据或密集 dashboard
change_request_if:
  - 口播结果差和素材证据不一致
blocked_if:
  - result_diff_is_claimed_but_evidence_missing
record_to:
  - card_placement_decision.card_plan
  - material_evidence
validation_rule:
  - 差异必须回指素材、截图、时间码或真实数据来源
```

### 4.6 boundary_card（边界卡）

```text
judgment_object: boundary_card
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断是否需要标记适用边界、风险边界、不能证明什么
  - 绑定 copy_function = boundary_statement
codex_must_not_do:
  - 不得把边界声明包装成结论或证明
change_request_if:
  - 边界声明需要改文案才能避免误导
blocked_if:
  - 缺 boundary_card 会导致观众误以为素材证明了更多结论
record_to:
  - card_placement_decision.card_plan
  - script_to_timeline_map
validation_rule:
  - boundary_card 只能降误读，不得新增 claim
```

### 4.7 prompt_tail_card（Prompt 尾卡）

```text
judgment_object: prompt_tail_card
codex_permission: must_decide_and_execute
codex_must_do:
  - 判断是否需要低压承接 prompt / 工作包 / 资料包入口
  - 保持 1-2 行核心提示，不承担主叙事
codex_must_not_do:
  - 不得做第二个主结尾、强卖课 CTA 或完整教程页
change_request_if:
  - 尾卡文字需要新增文案语义
blocked_if:
  - prompt_tail_card 抢 summary_card 或 result_diff_card 的职责
record_to:
  - content_route_card V2.prompt_tail_card_usage
validation_rule:
  - prompt_tail_card 只引用，不做主结论
```

### 4.8 script_to_timeline_map（文案到时间线映射）

```text
judgment_object: script_to_timeline_map
codex_permission: must_decide_and_execute
codex_must_do:
  - 按每 1-2 句一个 line_group 建立映射
  - 填写 line_group_id / narration_text / source_timecode / expected_visual / allowed_visuals / forbidden_visuals / subtitle_text / card_text_if_any / evidence_strength / alignment_status / blocked_if_visual_mismatch
codex_must_not_do:
  - 不得只做段落级素材分配
  - 不得用画面 B 支撑口播 A
change_request_if:
  - 某句没有素材可承载，但可通过改文案修复
blocked_if:
  - script_to_timeline_map missing before video execution
  - paragraph_level_mapping_only
  - visual_mismatch remains
record_to:
  - script_anchor_extraction_function output
  - review pack
validation_rule:
  - line_level_script_visual_alignment_gate 必须通过
```

### 4.9 subtitle_segmentation（字幕分句）

```text
judgment_object: subtitle_segmentation
codex_permission: must_decide_and_execute
codex_must_do:
  - 按 TTS 停顿、句意和画面证据分句
  - 避免字幕遮挡标题卡、解释卡、总结卡、画面 OCR 和关键证据区域
codex_must_not_do:
  - 不得为了好看删改文案语义
change_request_if:
  - 原句过长，字幕无法在不改语义的前提下可读
blocked_if:
  - high severity subtitle/card overlap
record_to:
  - subtitle_card_overlap_check
  - script_to_timeline_map.subtitle_text
validation_rule:
  - 字幕可读、不卡证据、不与卡片抢位
```

### 4.10 tts_prosody（TTS 韵律）

```text
judgment_object: tts_prosody
codex_permission: must_decide_and_execute
codex_must_do:
  - 生成 tts_prosody_anchor_map
  - 判断分句、停顿、重音、禁用上扬词和音高走势
codex_must_not_do:
  - 不得因 TTS 不顺擅自改写文案语义
  - 不得把候选音色写成 voice_validation passed
change_request_if:
  - 某句必须改语义才读得顺
blocked_if:
  - tts_generation_requested and tts_prosody_anchor_map missing
record_to:
  - tts_prosody_anchor_map
validation_rule:
  - 韵律调整不改变 locked_final_script 语义
```

### 4.11 material_evidence（素材证据）

```text
judgment_object: material_evidence
codex_permission: must_decide_but_request_change / must_decide_and_block
codex_must_do:
  - 判断素材能证明什么、不能证明什么、缺哪些时间码或截图
  - 标记 evidence_strength
codex_must_not_do:
  - 不得用卡片、AI 图、HyperFrames 或口播替代真实证据
change_request_if:
  - 文案 claim 超出素材但可通过删改文案解决
blocked_if:
  - 核心结论无素材支撑且不可本轮补齐
record_to:
  - evidence_plan
  - script_to_timeline_map
  - material audit / review pack
validation_rule:
  - 核心 claim 必须回指真实录屏、前后对比、步骤截图、结果截图或平台数据
```

### 4.12 visual_mismatch（画面错位）

```text
judgment_object: visual_mismatch
codex_permission: must_decide_but_request_change / must_decide_and_block
codex_must_do:
  - 判断口播、字幕、卡片和画面是否逐句对齐
  - 给出修复路径：换素材、改位置、改节奏、请求改文案或 blocked
codex_must_not_do:
  - 不得硬剪通过
change_request_if:
  - 文案和素材冲突可通过改句子解决
blocked_if:
  - 文案说 A、画面显示 B，且无法修复
record_to:
  - line_level_script_visual_alignment_gate
validation_rule:
  - visual_mismatch high severity 时不得生成视频或写完成
```

### 4.13 aspect_ratio_resolution（比例与分辨率）

```text
judgment_object: aspect_ratio_resolution
codex_permission: must_decide_and_execute / must_decide_and_block
codex_must_do:
  - 正式运营视频交付默认检查 horizontal_16_9 与 1920x1080
codex_must_not_do:
  - 不得把旧 9:16 或低清横屏预览写成正式交付
change_request_if:
  - 用户明确要求特殊比例但与当前默认口径冲突
blocked_if:
  - publish_candidate task 输出不符合 16:9 / 1920x1080
record_to:
  - delivery_baseline_gate
  - final media probe
validation_rule:
  - probe 通过才可进入 publish_candidate readiness
```

### 4.14 publish_candidate_readiness（可发布候选片准备状态）

```text
judgment_object: publish_candidate_readiness
codex_permission: must_decide_and_block
codex_must_do:
  - 检查音轨、字幕、横屏 16:9 / 1920x1080、剪辑节奏、素材证据、TTS、卡片、人感质量、平台风险、API 授权和装配能力
codex_must_not_do:
  - 不得用 technical_preview、silent preview、JSON / Markdown route card 冒充交付
change_request_if:
  - 缺口只涉及锁定文案需改
blocked_if:
  - 任一发布候选硬条件缺失且未修复
record_to:
  - delivery_baseline_gate
  - completion_truth_check
validation_rule:
  - publish_candidate_ready_for_human_review 不等于 send_ready
```

### 4.15 data_goal_alignment（数据目标对齐）

```text
judgment_object: data_goal_alignment
codex_permission: must_decide_but_request_change / must_escalate_to_chatgpt_or_user
codex_must_do:
  - 检查 current_data_goal_anchor、main_bottleneck、primary_variable、forbidden_variables、post_publish_validation_metric
  - 判断执行结构是否仍服务主变量
codex_must_not_do:
  - 不得改写当前阶段目标、主短板、主变量、禁止变量、成功 / 失败 / 发布后验证指标
change_request_if:
  - 文案或执行结构会破坏数据目标
blocked_if:
  - data_goal_anchor missing or current anchor not ready but task requires formal execution
record_to:
  - data_goal_alignment_check
  - content_route_card V2.data_goal_alignment
validation_rule:
  - 结构可变，目标锁死
```

### 4.16 copy_change_request（文案修改请求）

```text
judgment_object: copy_change_request
codex_permission: must_decide_but_request_change / must_escalate_to_chatgpt_or_user
codex_must_do:
  - 明确需要改什么、为什么执行层做不到、改动会影响哪些画面 / 字幕 / TTS / 卡片
  - 区分 allowed_copy_changes 与 forbidden_copy_changes
codex_must_not_do:
  - 不得自行改标题、选题、开头句、核心判断、人味表达、文案语义或视觉标题卡标题
change_request_if:
  - 标题太长、文案太长、TTS 不适配、素材无法支撑、卡片文字需要语义改写
blocked_if:
  - ChatGPT / 用户未确认且改动超出 allowed_copy_changes
record_to:
  - locked_copy_contract
  - dated log / review pack
validation_rule:
  - 未确认前不得把请求当成已执行修改
```

### 4.17 human_review_required（需要人工复审）

```text
judgment_object: human_review_required
codex_permission: must_escalate_to_chatgpt_or_user
codex_must_do:
  - 标记需要 ChatGPT / 用户判断的对象、原因和待确认项
  - 保留 technical_validation / content_validation / send_ready 分层
codex_must_not_do:
  - 不得自行推进 content_validation、send_ready、publish_status_success、voice_validation、final_voice_validated、visual_master_locked
change_request_if:
  - 需要人审的是文案语义或审美方向
blocked_if:
  - 缺人审却要求最终发送、最终内容通过或声音最终通过
record_to:
  - review_manifest
  - codex_log/latest.md
validation_rule:
  - 人审通过前只能写待验证或 human_review_required
```

## 5. HyperFrames 相关权限补充

当 `card_placement_decision（卡片位置判断）` 选择 `judgment_card（判断卡）` 或 `summary_card（总结卡）` 时：

- `codex_permission = must_decide_and_execute`：Codex 必须判断是否触发 HyperFrames 基线。
- `hyperframes_required = true`：默认必须使用 `hyperframes_card_motion_baseline（HyperFrames 卡片动效基线）`。
- `minimal_runtime_validation = passed`：当前已通过 `npx --yes hyperframes@0.6.12 render` 完成最小判断卡 / 总结卡真实动效验证。
- `real_video_execution_chain_integration = pending`：正式视频执行链是否稳定复用该 runtime adapter 仍待验证。
- `future_video_execution_blocked_if_hyperframes_required_but_missing = true`：后续真实视频如果要求 HyperFrames 而 runtime 不可用，必须 blocked 或等待用户明确授权降级。

HyperFrames 只强化卡片动效和观感，不替代中段真实录屏证据，不改文案职责，不新增素材里没有的数据结论，也不推进 `content_validation（内容验证）`。

### hyperframes_visual_skin_permission（HyperFrames 视觉皮肤权限）

```text
hyperframes_visual_skin_permission:
  codex_permission: must_decide_and_execute
  codex_must_do:
    - 当 card_placement_decision 选择 judgment_card 或 summary_card 时，必须在 clean_soft / cute_ai_guide 中选择一个视觉皮肤。
    - 必须说明 skin_selection_reason。
    - 必须记录 visual_tokens。
    - 必须确认 card_text_semantic_match = true，不得因皮肤排版改写 locked copy 语义。
  codex_must_not_do:
    - 不得选择 sharp_judgment 作为默认皮肤。
    - 不得新增第三套皮肤作为默认选项。
    - 不得因皮肤选择改写 locked copy。
    - 不得把皮肤好看写成 content_validation 通过。
    - 不得把 clean_soft / cute_ai_guide 锁成最终视觉母版。
  change_request_if:
    - clean_soft / cute_ai_guide 都无法承载原卡片文字，且必须调整语义才能排版。
  blocked_if:
    - skin missing
    - HyperFrames runtime unavailable
    - selected skin would break subtitle / evidence window
    - selected skin changes locked copy meaning
  record_to:
    - content_route_card V2.card_placement_decision
    - hyperframes_visual_quality_gate
    - review_manifest
  validation_rule:
    - 生成产物必须为 real_hyperframes_motion。
    - visual_skin 只能来自 allowed_hyperframes_visual_skins = [clean_soft, cute_ai_guide]。
    - sharp_judgment 只能写为 not_selected_this_round。
```

## 6. 完成检查接入

```text
completion_truth_check_additions:
  route_decision_must_include:
    - codex_judgment_permission_matrix_read
    - hyperframes_card_motion_baseline_read
    - judgment_card_hyperframes_required
    - summary_card_hyperframes_required
    - hyperframes_runtime_gate
    - permission_boundary_violations

  if judgment_card or summary_card selected:
    require:
      - hyperframes_card_motion_plan
      - hyperframes_runtime_status
      - hyperframes_visual_quality_check
      - subtitle_card_overlap_check
      - card_text_semantic_match

  if HyperFrames required but fallback static card used without user authorization:
    completed: false
    status: blocked
```
