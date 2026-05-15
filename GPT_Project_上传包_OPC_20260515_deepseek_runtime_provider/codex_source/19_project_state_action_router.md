# Project State Action Router 项目状态动作总控器

## 1. 文件定位

本文件是 Codex 执行层的 `Project State Action Router（项目状态动作总控器）`。

它解决的问题不是“任务属于哪个项目”，而是：路由已确定后，当前项目处于什么状态、应该触发哪条机制、下一步该做什么、做到哪里算完成。

它不替代：

- `AGENTS.md` 的 `route_decision（路由判断）`
- `codex_source/01_execution_rules.md` 的执行规则
- `Completion Relay Gate（补全接力闸门）`
- `Reference-to-Execution Contract（参考到执行落地契约）`
- `GPT数据源/08_当前正式事实.md`
- `dist/latest_review_pack/summary.json`

## 2. 每轮执行前必须输出 state_action_router

每次 Codex 任务必须先输出 `route_decision（路由判断）`。

在 `route_decision` 成立后、进入具体执行前，必须再输出：

```text
state_action_router:
  input_signal:
  current_project_state:
  fact_source_arbitration:
    primary_source:
    secondary_sources:
    conflict_detected:
    conflict_resolution:
  inferred_state:
  confidence:
  trigger_mechanism:
  selected_action:
  forbidden_action:
  must_read_files:
  done_when:
  blocked_if:
  feedback_update_required:
```

字段规则：

- `input_signal`：本轮触发信号，来自用户输入、仓库状态、执行结果、复盘数据、素材或冲突。
- `current_project_state`：从 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 的 `project_state_table` 中选择，必要时可写多个状态。
- `fact_source_arbitration`：说明以哪个事实源为准；若冲突，写裁决结果。
- `inferred_state`：对当前状态的判断，不是动作名。
- `confidence`：只能写 `high / medium / low`。
- `trigger_mechanism`：触发的下层机制，例如 `review_loop`、`content_route_card`、`editing_inference_function`、`quality_issue_classifier`、`Reference-to-Execution Contract`、`Completion Relay Gate`。
- `selected_action`：本轮最小可执行动作。
- `forbidden_action`：本轮明确禁止动作，尤其是状态推进、API、secret、媒体产物修改。
- `done_when`：本轮动作完成标准。
- `blocked_if`：必须阻断的条件。
- `feedback_update_required`：执行结果是否需要更新 latest、dated log、路径索引、机制文件或 missing fields。

## 3. 触发优先级

```text
P0:
  - status_conflict
  - old_branch_or_old_source_residue
  - missing_gray_test_data
  - forbidden_status_promotion_risk
  - evidence_missing_for_content_claim
  - user_current_instruction_conflicts_with_repo

P1:
  - mechanism_written_but_unverified
  - Codex partial completion risk
  - reference_contract_needed
  - missing inference function
  - data_goal_anchor_needed
  - current_data_goal_anchor_required
  - current_data_goal_anchor_missing
  - current_data_goal_anchor_waiting_data
  - codex_execution_structure_drift_risk
  - GPT Project package stale

P2:
  - path stale
  - historical mirror noise
  - efficiency / repeated explanation risk
```

处理顺序：

1. 先处理 P0 状态冲突、旧口径残留、灰度数据缺失和禁止状态推进风险。
2. 再处理 P1 机制未验证、推理函数缺失、GPT Project 静态包落后。
3. 最后处理 P2 路径过期、历史镜像噪声和重复解释效率问题。

如果 P0 未解决，不得进入 P1 / P2 的执行动作。

## 4. Codex 动作策略

```text
if state = gray_test_waiting_data:
  action = ask for / ingest data, update missing fields, do not write new copy

if state = mechanism_repair_needed:
  action = repair specified mechanism only, do not touch video status

if state = deepseek_supply_required:
  action = create_supply_request, run_deepseek_pre_supply, and read supply pack before file modification

if state = deepseek_pre_supply_missing:
  action = run_deepseek_pre_supply or mark fallback_local_only / blocked before write

if state = deepseek_post_review_missing:
  action = run_deepseek_post_risk_review before completion claim

if state = deepseek_claim_without_token_usage:
  action = run token_usage_expectation_check; do not write DeepSeek deep participation

if state = codex_vertical_completion_missing:
  action = run_codex_vertical_completion across affected files, schema, fixture, logs, and package

if state = data_goal_anchor_needed:
  action = create_data_goal_anchor or block_execution_if_goal_anchor_missing before video execution

if state = current_data_goal_anchor_required:
  action = read codex_log/current_data_goal_anchor.md before copy, video execution, editing, assembly, or DeepSeek supply

if state = current_data_goal_anchor_missing:
  action = create codex_log/current_data_goal_anchor.md as current instance template; status must be draft, waiting_data, or blocked, not ready

if state = current_data_goal_anchor_waiting_data:
  action = allow hypothesis-only wiring or blocked; do not claim data-driven ready execution

if state = current_data_goal_anchor_ready:
  action = allow Codex preflight only after locked fields and data_goal_alignment_check requirement are present

if state = data_goal_execution_bus_needed:
  action = wire data_goal_anchor into copy, DeepSeek supply, Codex execution, editing, assembly, validation, logs, and GPT Project package

if state = codex_execution_structure_drift_risk:
  action = run_data_goal_alignment_check and allow only structure changes that preserve primary_variable and validation metrics

if state = editing_or_assembly_without_data_goal_anchor:
  action = block editing / assembly until data_goal_anchor_used and data_goal_alignment_check fields exist

if state = reference_contract_needed:
  action = create or require Reference-to-Execution Contract before concrete execution

if state = editing_inference_needed:
  action = run editing_inference_function, then generate editing_decision_pack if evidence is sufficient

if state = content_route_needed:
  action = run content_route_inference_function, then generate content_route_card before video execution

if final_script exists and task requests video execution:
  action = run script_anchor_extraction_function, then generate script_to_timeline_map before video execution

if tts_generation_requested:
  action = require tts_prosody_anchor_map before TTS generation

if input_signal includes opening_route / 开头路线 / 元素娃娃开头 / 梗图 GIF 开场 / 开头参考图:
  action = run content_route_inference_function, produce opening_route_decision, then generate opening

if opening_route in [meme_gif_opening_hook, high_emotion_hook] or input_signal includes 抖音抓眼 / 高情绪开头 / 抽象动效:
  action = require opening_visual_hook_spec before opening generation

if input_signal includes summary_card / 总结卡 / reversal_card / 反转卡 / result_diff_card / 结果差卡 / Prompt 引用尾卡 / 卡片位置:
  action = run content_route_inference_function and editing_inference_function, produce card_placement_decision before video execution

if state = quality_review_needed:
  action = run quality_issue_classifier before changing assets or status wording

if state = gpt_project_sync_needed:
  action = regenerate static upload package, do not treat as UI uploaded

if input_signal includes 文案修改 / 下一条视频 / 根据数据改 / 播放低 / 收藏低 / 客资弱 / 复盘后重写:
  action = read goal-driven data flywheel, check threshold_config_v1, diagnose main_bottleneck, lock primary_variable before copy revision

if input_signal includes 根据数据推算下一段放什么 / 内容结构反馈 / 留存下滑 / 收藏低 / 评论弱 / 私信弱:
  action = generate content_structure_feedback_card and next_video_structure_plan before revised script

if input_signal includes Codex 执行下一条视频 / 根据数据执行 / 动态 prompt:
  action = require next_video_execution_prompt, codex_log/current_data_goal_anchor.md, and data_goal_anchor before video execution

if input_signal includes 视频执行 / 剪辑 / 编排 / 装配 / editing_decision_pack / assembly_decision_pack:
  action = require current_data_goal_anchor, then run data_goal_alignment_check before completion

if state = blocked_need_user_input:
  action = stop and report exact missing user input
```

补充策略：

- `gray_test_data_intake`：只做截图 / 数据录入、缺失字段标记和证据归档，不做最终内容判断。
- `post_publish_review`：必须有足够数据再判断 6000 门槛、短板层和下一轮唯一变量。
- `material_audit_needed`：先判断素材用途、证据强度和缺口，不直接生成或改动媒体。
- `voice_review_needed`：只做声音问题归因和候选复审，不写最终声音通过，不调用 TTS / voice cloning API。
- `reference_contract_needed`：只把 reference / 样片 / 目标效果转换为 `reference_anchor`、`effect_targets`、`function_fields`、`deviation_check`、`done_when`，不得直接执行媒体、文案终稿或状态推进。
- `deepseek_supply_required`：每轮默认成立；不得由 Codex 主观跳过 DeepSeek 供料闸门。
- `deepseek_pre_supply_missing`：写入前必须先补 `supply_request` 和执行前供料；无法真实调用时写 fallback / blocked。
- `deepseek_post_review_missing`：修改后必须复核状态偷换、禁止修改、遗漏同步、fallback 误标和剩余工作。
- `deepseek_claim_without_token_usage`：token 未观察到减少时不得写 DeepSeek 已深度参与。
- `codex_vertical_completion_missing`：只写文档不算完成，必须补脚本、schema、fixture、日志、上传包和验证链。
- `data_goal_anchor_needed`：缺数据目标锚点时，不得进入视频执行、剪辑、编排或装配。
- `data_goal_execution_bus_needed`：13 已定义目标但未接到全执行链时，必须补 14 总线或同步执行规则；不得只扩写说明。
- `codex_execution_structure_drift_risk`：Codex 可以改结构，不能改目标、主短板、主变量、禁止变量和验证指标。
- `editing_or_assembly_without_data_goal_anchor`：缺 `data_goal_anchor_used` 时，不得生成 `editing_decision_pack` 或 `assembly_decision_pack`。

### 4-1. 目标驱动数据飞轮执行侧规则

命中以下任一信号时，Codex 必须先读 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 与 `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`：

- 文案修改
- 下一条视频
- 根据数据改
- 播放低 / 收藏低 / 客资弱
- 复盘后重写
- 数据飞轮
- 目标驱动
- 数据目标
- 单主变量
- 内容结构反馈
- 视频执行 / 剪辑 / 编排 / 装配
- DeepSeek 供料
- GPT Project 静态包同步

```text
data_goal_copy_revision_needed:
  trigger:
    - 用户要求修改文案
    - 用户要求根据数据调整文案
    - 用户要求写下一条视频
    - 用户要求复盘后重写
  must_read:
    - data_goal_anchor
    - threshold_config_v1
    - video_goal_card
    - post_publish_review_card
    - data_flywheel_memory
    - content_structure_feedback_card
  selected_action:
    - 先检查阈值
    - 先诊断主短板
    - 锁定 primary_variable
    - 写 supporting_variables / forbidden_variables
    - 再进入文案修改
  blocked_if:
    - 缺 data_goal_anchor
    - 缺目标
    - 缺阈值配置
    - 缺数据且声称数据驱动
    - 缺主短板
    - 缺 primary_variable

content_structure_feedback_needed:
  trigger:
    - 用户要求根据数据推算下一段放什么
    - 发布后留存 / 收藏 / 评论 / 私信出现短板
  selected_action:
    - 生成 content_structure_feedback_card
    - 生成 next_video_structure_plan
  blocked_if:
    - 缺阈值配置
    - 缺分段数据
    - 缺复盘窗口
    - 数据不足却强行下结论
```

data_goal_execution_bus_needed:
  trigger:
    - data_goal 已定义，但 content_route_card / DeepSeek supply_request / editing_decision_pack / assembly_decision_pack 未接入
    - Codex 执行可能只按素材、画面或旧流程自由发挥
  selected_action:
    - create_data_goal_anchor
    - run_data_goal_alignment_check
    - block_execution_if_goal_anchor_missing
  blocked_if:
    - 缺 data_goal_anchor
    - 缺 primary_variable
    - 缺 forbidden_variables
    - 缺 post_publish_validation_metric
    - Codex 需要改写目标而不是调整结构
    - 数据目标被用来替代素材证据或人感质量验收

执行侧硬规则：

- 没有 `threshold_config_v1（阈值配置 V1）`，不得做数据驱动判断。
- 没有 `video_goal_card（视频目标卡）`，不得进入正式文案修改。
- 没有 `post_publish_review_card（发布后复盘卡）`，不得声称“根据数据修改文案”。
- 没有 `main_bottleneck（主短板）`，不得重写正式文案。
- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。
- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，不得进入视频执行。
- 没有 `data_goal_anchor（数据目标锚点）`，不得进入视频执行、剪辑、编排或装配。
- 没有 `data_goal_alignment_check（数据目标对齐检查）`，不得写执行完成。
- 超过 3 个变量且未标 `major_revision（大改版）`，不得进入执行。
- 超过 4 个变量不得写成单变量实验，只能写方向重做观察。
- 本机制不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
Codex 可以调整 segment 拆分、剪辑节奏、画面顺序、卡片位置、TTS 分句、装配顺序和降级方案；不得改写当前阶段目标、主短板、主变量、禁止变量或发布后验证指标。

## 4A. 三大机制推理函数执行侧调用规则

Codex 进入具体执行前，凡命中剪辑、内容承载或质量复审信号，必须先输出对应推理函数结果。没有对应函数结果，不得生成卡片 / 决策包，不得进入视频执行，不得写 `completed（已完成）`。

### 4A.0 script_anchor_extraction_function（文案锚点提取函数）

触发信号：

- 已有 `final_script（最终文案）`，且任务准备进入视频执行、时间线装配、TTS、字幕、卡片或审片包生成。
- `content_route_card V2（内容路由卡 V2）` 已存在，但只有段落级 `material_01 / material_02 / material_03` 分配。
- 用户指出文案和画面局部错位、关键句配错画面、证据句没有对应素材。
- 用户指出 TTS 字词突然上扬、停顿不自然、分句断裂或机器式重音。

执行侧输出必须包含：

```text
script_anchor_extraction_function:
  input_signal:
    - final_script
    - content_route_card_v2
    - material_detail_report
    - platform_risk_note
    - data_goal_anchor
  observed_evidence:
    - narration_line
    - claim_type
    - evidence_type
    - material_id
    - source_timecode
    - risk_phrase
    - data_goal_anchor_used
    - main_bottleneck_supported
    - primary_variable_supported
    - forbidden_variables_avoided
    - post_publish_validation_metric
  state_inference:
    - sentence_has_direct_evidence
    - sentence_has_user_experience_claim
    - sentence_is_boundary_statement
    - sentence_is_reversal_point
    - sentence_is_summary_point
    - sentence_needs_card_support
    - sentence_must_not_use_visual_claim
    - paragraph_level_mapping_insufficient
  action_policy:
    - output_script_function_map
    - output_evidence_anchor_map
    - output_visual_anchor_map
    - output_tts_prosody_anchor_map
    - output_card_anchor_map
    - output_forbidden_visual_map
    - output_script_to_timeline_map
    - output_data_goal_alignment_fields
    - blocked_if_sentence_level_mapping_missing
  validation_rule:
    - 每 1-2 句必须有 line_group_id
    - 每个 line_group_id 必须绑定素材或明确 no_direct_evidence
    - 每个 line_group_id 必须有 allowed_visuals 和 forbidden_visuals
    - 每个 line_group_id 必须说明服务哪个数据目标、主短板或主变量
    - 每个 evidence_sentence 必须能追溯素材或标记为用户经验陈述
    - 每个 boundary_statement 不得配误导性证明画面
  blocked_if:
    - data_goal_anchor missing
    - final_script missing
    - material_detail_report missing
    - script_to_timeline_map missing before video execution
    - paragraph_level_mapping_only
  feedback_update:
    - 写入 content_route_card V2
    - 写入 video_execution_preflight
    - 写入 review pack
    - 写入 dated log
```

完成判断：

- `data_goal_anchor（数据目标锚点）` 是视频执行、剪辑、编排和 DeepSeek 供料前置条件。
- `script_to_timeline_map（文案到时间线映射表）` 是视频执行、时间线装配和剪辑前置条件。
- `tts_prosody_anchor_map（TTS 韵律锚点表）` 是 TTS 生成前置条件。
- `opening_visual_hook_spec（开头视觉钩子规格）` 是高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头生成前置条件。
- `forbidden_visual_map（禁用画面表）` 必须用于阻止边界声明、经验陈述和平台风险句配误导性证明画面。
- 只有段落级 `material_01 / material_02 / material_03` 分配时，不得进入视频执行。
- `data_goal_alignment_check（数据目标对齐检查）` 是视频执行完成前置条件。

### 4A.1 editing_inference_function（剪辑推理函数）

触发信号：

- 任务涉及中段剪辑、录屏放大、裁切、定格、插卡、左右对比、证据窗口或 `editing_decision_pack（剪辑决策包）`。
- 任务涉及总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡插入位置，或需要判断卡片是否打断证据窗口。
- 用户反馈中段不顺、看不清、硬拼接、上下文断裂。
- reference / visual route 要求保留某个证据窗口或剪辑节奏。
- 素材被标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）`，需要判断是否保留原始运镜并按文案直接剪辑。
- 已有最终文案但缺 `script_to_timeline_map（文案到时间线映射表）`。
- 只有段落级素材分配，缺 `line_id / line_group_id（句子编号 / 句组编号）`。

执行侧输出必须包含：

```text
editing_inference_function:
  input_signal:
    - data_goal_anchor
  observed_evidence:
    - data_goal_anchor_used
    - line_group_goal
    - primary_variable_support
    - evidence_role_for_metric
    - forbidden_visuals_by_goal
    - post_publish_validation_metric
  state_inference:
  action_policy:
    - output_edit_action_reason_against_data_goal
  validation_rule:
    - 每个剪辑动作必须说明是否支持 primary_variable
    - 每个剪辑动作不得引入 forbidden_variables
  blocked_if:
    - data_goal_anchor missing
    - edit_action_breaks_primary_variable
    - forbidden_variable_introduced
  not_allowed:
  feedback_update:
```

FocuSee 自带运镜素材的执行侧补充：

```text
  state_inference:
    - recording_layer_motion_baked_in
    - direct_cut_required
    - keep_original_motion
    - no_secondary_zoom_by_default
    - secondary_zoom_allowed_only_if_evidence_unclear
    - sentence_level_mapping_ready
    - paragraph_level_mapping_insufficient
    - script_visual_mismatch_detected
  action_policy:
    - direct_cut_by_script
    - keep_original_focusee_motion
    - trim_dead_time
    - align_to_narration
    - preserve_evidence_window
    - blocked_if_key_evidence_unclear
    - read_script_to_timeline_map_before_assembly
    - blocked_if_paragraph_level_mapping_only
    - blocked_if_script_visual_conflict
not_allowed:
  - default_zoom_in
  - default_crop_focus
  - reframe_without_reason
  - second_camera_motion_over_focusee_motion
```

卡片插入执行侧补充：

```text
state_inference:
  - card_insertion_safe
  - card_insertion_interrupts_evidence
  - keep_evidence_window_uninterrupted
action_policy:
  - insert_card_only_if_copy_function_requires
  - preserve_focusee_motion_when_card_not_required
  - blocked_if_card_breaks_evidence_window
not_allowed:
  - fixed_card_shot_without_copy_reason
  - summary_card_as_evidence
  - reversal_card_without_reversal_point
```

完成判断：

- `editing_decision_pack（剪辑决策包）` 必须引用本函数的 `state_inference` 和 `action_policy`。
- `editing_decision_pack（剪辑决策包）` 必须包含 `data_goal_anchor_used / line_group_goal / primary_variable_support / evidence_role_for_metric / forbidden_visuals_by_goal / edit_action_reason_against_data_goal / post_publish_validation_metric`。
- 如果素材不可读、时间码不清、证据点不可见、放大会切断必要上下文，必须 `blocked` 或 `keep_full_frame`，不得凭感觉剪。
- 卡片、放大、裁切、定格只能服务真实证据清晰，不得替代真实录屏证据。
- 当素材已经自带 FocuSee `3D Motion（3D 运镜）`、自动跟随或观看引导时，默认完成标准不是“再放大一次”，而是按最终文案完成时间码识别、段落切分、冗余删除、口播 / 字幕 / 卡片衔接，并保留原始运镜节奏。
- 如果卡片会打断真实证据窗口，必须跳过、改位置或 blocked，不得为了旧 shot 结构强插。
- 剪辑动作不能只看 `material_01 / material_02 / material_03` 段落级用途，必须读取 `line_id / line_group_id（句子编号 / 句组编号）`。
- 每 1-2 句必须知道当前句子在证明什么、必须出现什么画面、不能出现什么画面、是否需要卡片辅助，以及是否是反转点 / 证据点 / 总结点。
- 如果只有段落级映射，不允许进入视频装配；如果文案句子与素材证据冲突，必须 blocked 或回到 ChatGPT 复审，不得硬剪。
- 如果缺 `data_goal_anchor_used（使用的数据目标锚点）`，不得生成 `editing_decision_pack（剪辑决策包）`。
- 如果剪辑动作改变主变量、引入禁止变量或削弱发布后验证指标，必须 blocked。

### 4A.2 content_route_inference_function（内容路由推理函数）

触发信号：

- 任务涉及 `content_route_card（内容路由卡）`、内容表达文案进入执行、主体承载、API 生成真人次数、PPT / 信息卡 / Prompt 引用尾卡是否出现。
- 任务涉及真实视频执行前的统一判断卡、`content_route_card V2（内容路由卡 V2）` 或等效完整字段。
- 任务涉及 `opening_route_decision（开头路由判断）`、元素娃娃开头、梗图 GIF 开场、直接问题标题卡、录屏现场先行开头或开头参考图。
- 任务涉及 `card_placement_decision（卡片位置判断）`、总结卡、反转卡、结果差卡、Prompt 尾卡或卡片位置路由。
- 任务涉及最终文案进入执行，需要生成 `script_anchor_map / script_to_timeline_map / tts_prosody_anchor_map / forbidden_visual_map`。
- 任务涉及高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头，需要生成 `opening_visual_hook_spec（开头视觉钩子规格）`。
- 需要判断本轮是只做内容验证，还是值得沉淀三层 prompt 包 / 工作包。
- reference 质量点可能和当前文案目标冲突。

执行侧输出必须包含：

```text
content_route_inference_function:
  input_signal:
    - data_goal_anchor
  observed_evidence:
    - data_goal_anchor_used
    - main_bottleneck_supported
    - primary_variable_supported
    - forbidden_variables_avoided
    - post_publish_validation_metric
  state_inference:
  action_policy:
  validation_rule:
    - content_route_must_support_data_goal
  blocked_if:
    - data_goal_anchor missing
  feedback_update:
```

完成判断：

- `content_route_card（内容路由卡）` 必须由本函数生成或引用本函数判断。
- 涉及内容执行 / 视频执行 / 文案进入执行时，必须输出 `content_route_card V2（内容路由卡 V2）` 或等效完整字段，不得只输出零散开头、卡片或素材判断。
- `content_route_card V2（内容路由卡 V2）` 必须包含 `data_goal_anchor_used / main_bottleneck_supported / primary_variable_supported / forbidden_variables_avoided / post_publish_validation_metric`。
- 缺 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / card_placement_decision / flow_flex_reason` 时，不得进入视频执行。
- 缺 `data_goal_anchor_used（使用的数据目标锚点）` 时，不得进入视频执行。
- `forbidden_variables_avoided（内容路由 / 时间线避开的禁止变量）`、`forbidden_visuals_by_goal（剪辑按目标禁用的画面）` 与 `forbidden_variable_avoided（装配避开的禁止变量）` 必须全部能追溯到同一组 `data_goal_anchor.forbidden_variables`；字段名不同不代表语义可分叉。
- 若素材来自 FocuSee，缺 `focusee_middle_editing_decision（FocuSee 中段剪辑判断）` 时，不得进入中段剪辑或视频执行。
- 涉及总结卡、反转卡、结果差卡或 Prompt 尾卡时，缺 `card_placement_decision（卡片位置判断）` 不得进入视频执行。
- 不得先定人物次数、PPT 数量或尾卡数量，再把文案硬塞进去。
- 涉及开头时，不得绕过 `opening_route_decision（开头路由判断）` 直接生成开头。
- 涉及高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头时，不得只输出路线判断，必须输出 `opening_visual_hook_spec（开头视觉钩子规格）`；静态两行标题页不得默认通过。
- 涉及最终文案进入执行时，必须先输出 `script_anchor_extraction_function（文案锚点提取函数）` 的结果；缺 `script_to_timeline_map（文案到时间线映射表）` 不得进入视频执行。
- 涉及 TTS 生成时，必须先输出 `tts_prosody_anchor_map（TTS 韵律锚点表）`；不得只按标点机械分句。
- 不得把 `element_doll_opening（元素娃娃开头）` 或 `meme_gif_opening_hook（梗图 GIF 开场钩子）` 写成所有内容唯一默认。
- 若开头 reference 不完整，只能继承 `effect_targets（效果目标）` 和机制字段，不得复刻人物、头像、字体、构图或第三方可识别资产。
- 不得把总结卡 / 反转卡固定为旧 shot 位置；没有明确反转点时不得强行插反转卡，结尾一句话能自然收住时不得强行堆总结卡。

开头路线执行侧补充：

```text
opening_route_decision:
  input_signal:
    - opening_duration
    - topic_emotion_level
    - controversy_level
    - evidence_start_strength
    - brand_consistency_need
    - core_question_can_be_stated_in_one_sentence
  state_inference:
    - opening_route_needed
    - element_doll_opening_suitable
    - meme_gif_opening_hook_suitable
    - direct_question_title_card_suitable
    - screen_first_opening_suitable
    - opening_route_pending_judgment
  action_policy:
    - choose_element_doll_opening
    - choose_meme_gif_opening_hook
    - choose_direct_question_title_card
    - choose_screen_first_opening
    - blocked_if_opening_route_unclear
  not_allowed:
    - element_doll_as_only_default
    - meme_gif_as_new_only_default
    - copy_user_reference_asset
    - opening_hook_as_proof
    - static_two_line_title_for_high_emotion_hook
    - plain_title_card_when_douyin_hook_required
```

开头视觉 hook 规格补充：

```text
opening_visual_hook_spec:
  opening_route:
  hook_goal:
  viewer_feeling:
  visual_motion:
    - fast_zoom
    - shake
    - speed_lines
    - abstract_shapes
    - impact_flash
  text_density:
  main_question:
  composition:
  duration:
  must_not_be:
    - static_two_line_title
    - plain_title_card
    - ppt_cover_page
    - copied_third_party_asset
  allowed_style:
    - abstract_gif_like
    - meme_energy_without_copying
    - high_contrast_question_hook
  validation_rule:
  blocked_if:
```

卡片位置执行侧补充：

```text
card_placement_decision:
  input_signal:
    - copy_function
    - reversal_point
    - conclusion_point
    - result_diff_point
    - evidence_window_active
    - prompt_handoff_needed
  state_inference:
    - card_placement_route_needed
    - summary_card_needed
    - summary_card_not_needed
    - reversal_card_needed
    - reversal_card_not_needed
    - card_interrupts_evidence_window
    - card_position_pending_judgment
  action_policy:
    - place_summary_card_after_result_diff
    - place_summary_card_at_final_closure
    - place_reversal_card_between_negative_and_positive
    - place_reversal_card_before_result_diff
    - skip_card
    - blocked_if_card_position_unclear
  not_allowed:
    - fixed_summary_card_shot
    - fixed_reversal_card_shot
    - card_as_middle_evidence_replacement
```

### 4A.3 quality_issue_classifier（质量短板分类器）

触发信号：

- 用户反馈“不对 / 怪 / 不顺 / demo 感”。
- 技术通过但内容、人感、证据、声音、卡片密度或剪辑节奏不舒服。
- 需要生成或复核 `quality_lock_card（质量锁卡）`。
- 用户指出某些字突然上扬、停顿不自然、分句断裂、重音机器感。
- 用户指出开头只是两行简单字、不抓人、不符合抖音审美。
- 用户指出文案和画面局部错位，关键句配错画面。

执行侧输出必须包含：

```text
quality_issue_classifier:
  input_signal:
  observed_evidence:
  issue_categories:
    - voice_prosody_issue
    - opening_visual_hook_issue
    - script_visual_mismatch_issue
  state_inference:
  action_policy:
  validation_rule:
  blocked_if:
  feedback_update:
```

完成判断：

- 必须先定位唯一最高优先级短板；若观察到多个问题，也只能选一个 primary issue 进入下一轮修改。
- 必须区分 `technical_validation（技术验证）` 与 `content_validation（内容验证）`。
- 缺复审对象、用户反馈对象、灰度数据或需要用户审美判断时，必须 blocked / human_review_required，不得硬写事实。
- `voice_prosody_issue（声音韵律问题）` 优先动作是生成 `tts_prosody_anchor_map（TTS 韵律锚点表）`、重写分句和韵律，不默认换音色。
- `opening_visual_hook_issue（开头视觉钩子问题）` 优先动作是生成 `opening_visual_hook_spec（开头视觉钩子规格）`，并阻断静态两行标题通过高情绪开头验收。
- `script_visual_mismatch_issue（文案画面错位问题）` 优先动作是生成 `script_to_timeline_map（文案到时间线映射表）`，并在句子级映射缺失前阻断视频执行。

### 4A.4 与 Completion Relay Gate 的关系

本轮或后续任务一旦触发三个函数之一，`Completion Relay Gate（补全接力闸门）` 的 `required_output_inventory（必须交付清单）` 必须纳入：

1. 对应推理函数输出。
2. 对应卡片 / 决策包是否引用该函数。
3. 入口规则是否要求先输出该函数。
4. fixture / 最小样例是否覆盖正常判断与 blocked 判断。
5. `remaining_work_check（剩余工作检查）` 是否确认没有剩余 must-fix。
6. 若最终文案进入执行，是否已生成 `script_anchor_extraction_function（文案锚点提取函数）`、`script_to_timeline_map（文案到时间线映射表）`、`tts_prosody_anchor_map（TTS 韵律锚点表）` 与必要的 `opening_visual_hook_spec（开头视觉钩子规格）`。

## 5. 事实源裁决规则

默认事实源优先级：

1. GitHub / 本地 `main` 上的当前仓库文件。
2. `GPT数据源/` 当前正式机制包和事实文件。
3. `codex_log/latest.md`，但重要结论要回查直接源文件。
4. `dist/latest_review_pack/summary.json` 和 `review_manifest.md` 作为当前复审包状态证据。
5. 用户本轮明确指令，只对本轮有效；若要成为下一聊天事实，必须写回仓库。
6. GPT Project 静态上传包，只是协作包，不是实时事实库。
7. DeepSeek / Perplexity 输出只做供料或研究参考，不直接拍板项目事实。
8. DeepSeek 每轮默认供料包是 Codex 执行输入，但仍必须由 Codex 复核原文件后落地。

必须裁决的冲突：

| conflict | Codex decision |
| --- | --- |
| GPT Project static package vs GitHub main | GitHub main wins |
| User current explicit instruction vs repo old fact | current instruction guides this round; sync to repo to become durable fact |
| DeepSeek supply vs original repo files | original repo files win |
| DeepSeek mandatory supply vs Codex discretion | mandatory supply wins; Codex cannot skip without blocked reason |
| fallback_local_only vs DeepSeek conclusion | fallback is not DeepSeek conclusion |
| token not decreased vs DeepSeek participation claim | no deep participation claim without token evidence or user check |
| Perplexity reference vs repo formal facts | repo formal facts win |
| Reference-to-Execution Contract vs repo formal facts | repo formal facts win |
| technical_validation vs content_validation | content_validation cannot be upgraded by technical_validation |
| target_state_plan vs current_formal_fact | current_formal_fact wins |
| latest.md vs older dated logs | latest.md wins, then verify direct source files |
| summary.json vs chat memory | summary.json / repo files win |

## 6. 与 Completion Relay Gate 联动

`state_action_router` 和 `Completion Relay Gate（补全接力闸门）` 分工如下：

1. `state_action_router` 先判断当前状态和动作。
2. `Completion Relay Gate` 再保证动作执行到底。
3. 两者缺一不可。
4. 如果 `state_action_router` 没输出，Codex 不得进入执行。
5. 如果 `Completion Relay Gate` 没输出，Codex 不得写 `completed`。

`Reference-to-Execution Contract（参考到执行落地契约）` 插入在 `state_action_router` 和具体执行之间：

```text
input_signal = reference_provided / sample_reference_given / target_effect_given
-> current_project_state = reference_contract_needed
-> trigger_mechanism = Reference-to-Execution Contract
-> selected_action = create reference_to_execution_contract before concrete execution
-> Codex execution only after reference_anchor / effect_targets / function_fields / deviation_check / done_when are complete
```

如果任务带 reference，但没有 reference contract，Codex 必须 `blocked` 或先要求补齐 contract，不得直接执行。

推荐执行链：

```text
route_decision
-> state_action_router
-> reference_to_execution_contract if reference_contract_needed
-> required_output_inventory
-> child_task_graph
-> execution
-> validation
-> remaining_work_check
-> sync_back_check
-> completion_state_inference
```

## 7. completion_state_inference 执行口径

Codex 收尾时必须按以下四态判断：

| completion_state | 可写条件 | 不可写条件 |
| --- | --- | --- |
| `completed` | 必交付项全部完成、DeepSeek 参与报告 / token 检查边界写清、验证通过、日志 / 路径 / 包同步完成、无禁止状态推进、无剩余 must-fix | 任一 required item 未完成；DeepSeek 被跳过且无 blocked 原因；fallback 被写成 DeepSeek 结论 |
| `partial_completed` | 完成了部分可验证项，但仍有必交付项未完成 | 不得对用户写成已完成 |
| `blocked` | 缺关键文件、缺用户输入、需要 secret / API、需要修改禁止状态、证据不足 | 不得用猜测继续 |
| `continue` | 无 blocked，仍有必交付项 | Codex 必须继续执行，不得结束 |

## 8. feedback_update 执行口径

执行结果改变下一轮默认判断时，必须写回相应位置：

- 改机制入口：更新 `GPT数据源/` 或 `codex_source/` 相关文件，并写 latest。
- 改 GPT Project 静态包：更新 `codex_log/current_local_artifact_paths.md`，manifest 必须写边界。
- 改复盘数据：更新 `review_loop/` 对应记录和 missing fields。
- 发现失败：写失败信号、失败原因、blocked 条件和下一安全动作。
- 用户说“不对 / 怪 / 不顺”：先分类再动手，类别包括 `direction / structure / evidence / editing / voice / quality / route / state conflict`。

## 9. 本轮禁止状态推进

默认不得推进：

- `content_validation（内容验证）`
- `send_ready（可发送状态）`
- `publish_status（发布状态）`
- `voice_validation（声音验证）`
- `final_voice_validated（最终声音验证）`
- `visual_master_locked（视觉母版锁定）`

默认不得执行：

- 读取 `.env`、API key、token、secret
- 调用 DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API
- 修改视频、图片、音频、时间线、字幕或 `dist/latest_review_pack/` 媒体产物
- 新建外部工作区

## 10. 一句话规则

**Codex 每轮先用 `state_action_router` 判状态和动作，再进入 `deepseek_supply_gate（DeepSeek 供料闸门）`，最后用 `Completion Relay Gate` 把动作做完；没有状态动作判断不得执行，没有 DeepSeek 参与报告 / token 检查边界不得写 DeepSeek 深度参与，没有补全接力复核不得写 completed。**
