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

if state = reference_contract_needed:
  action = create or require Reference-to-Execution Contract before concrete execution

if state = editing_inference_needed:
  action = run editing_inference_function, then generate editing_decision_pack if evidence is sufficient

if state = content_route_needed:
  action = run content_route_inference_function, then generate content_route_card before video execution

if input_signal includes opening_route / 开头路线 / 元素娃娃开头 / 梗图 GIF 开场 / 开头参考图:
  action = run content_route_inference_function, produce opening_route_decision, then generate opening

if state = quality_review_needed:
  action = run quality_issue_classifier before changing assets or status wording

if state = gpt_project_sync_needed:
  action = regenerate static upload package, do not treat as UI uploaded

if state = blocked_need_user_input:
  action = stop and report exact missing user input
```

补充策略：

- `gray_test_data_intake`：只做截图 / 数据录入、缺失字段标记和证据归档，不做最终内容判断。
- `post_publish_review`：必须有足够数据再判断 6000 门槛、短板层和下一轮唯一变量。
- `material_audit_needed`：先判断素材用途、证据强度和缺口，不直接生成或改动媒体。
- `voice_review_needed`：只做声音问题归因和候选复审，不写最终声音通过，不调用 TTS / voice cloning API。
- `reference_contract_needed`：只把 reference / 样片 / 目标效果转换为 `reference_anchor`、`effect_targets`、`function_fields`、`deviation_check`、`done_when`，不得直接执行媒体、文案终稿或状态推进。

## 4A. 三大机制推理函数执行侧调用规则

Codex 进入具体执行前，凡命中剪辑、内容承载或质量复审信号，必须先输出对应推理函数结果。没有对应函数结果，不得生成卡片 / 决策包，不得进入视频执行，不得写 `completed（已完成）`。

### 4A.1 editing_inference_function（剪辑推理函数）

触发信号：

- 任务涉及中段剪辑、录屏放大、裁切、定格、插卡、左右对比、证据窗口或 `editing_decision_pack（剪辑决策包）`。
- 用户反馈中段不顺、看不清、硬拼接、上下文断裂。
- reference / visual route 要求保留某个证据窗口或剪辑节奏。
- 素材被标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）`，需要判断是否保留原始运镜并按文案直接剪辑。

执行侧输出必须包含：

```text
editing_inference_function:
  input_signal:
  observed_evidence:
  state_inference:
  action_policy:
  validation_rule:
  blocked_if:
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
action_policy:
  - direct_cut_by_script
  - keep_original_focusee_motion
  - trim_dead_time
  - align_to_narration
  - preserve_evidence_window
  - blocked_if_key_evidence_unclear
not_allowed:
  - default_zoom_in
  - default_crop_focus
  - reframe_without_reason
  - second_camera_motion_over_focusee_motion
```

完成判断：

- `editing_decision_pack（剪辑决策包）` 必须引用本函数的 `state_inference` 和 `action_policy`。
- 如果素材不可读、时间码不清、证据点不可见、放大会切断必要上下文，必须 `blocked` 或 `keep_full_frame`，不得凭感觉剪。
- 卡片、放大、裁切、定格只能服务真实证据清晰，不得替代真实录屏证据。
- 当素材已经自带 FocuSee `3D Motion（3D 运镜）`、自动跟随或观看引导时，默认完成标准不是“再放大一次”，而是按最终文案完成时间码识别、段落切分、冗余删除、口播 / 字幕 / 卡片衔接，并保留原始运镜节奏。

### 4A.2 content_route_inference_function（内容路由推理函数）

触发信号：

- 任务涉及 `content_route_card（内容路由卡）`、内容表达文案进入执行、主体承载、API 生成真人次数、PPT / 信息卡 / Prompt 引用尾卡是否出现。
- 任务涉及 `opening_route_decision（开头路由判断）`、元素娃娃开头、梗图 GIF 开场、直接问题标题卡、录屏现场先行开头或开头参考图。
- 需要判断本轮是只做内容验证，还是值得沉淀三层 prompt 包 / 工作包。
- reference 质量点可能和当前文案目标冲突。

执行侧输出必须包含：

```text
content_route_inference_function:
  input_signal:
  observed_evidence:
  state_inference:
  action_policy:
  validation_rule:
  blocked_if:
  feedback_update:
```

完成判断：

- `content_route_card（内容路由卡）` 必须由本函数生成或引用本函数判断。
- 缺 `validation_goal / opening_route_decision / core_evidence / middle_carrier / flow_flex_reason` 时，不得进入视频执行。
- 不得先定人物次数、PPT 数量或尾卡数量，再把文案硬塞进去。
- 涉及开头时，不得绕过 `opening_route_decision（开头路由判断）` 直接生成开头。
- 不得把 `element_doll_opening（元素娃娃开头）` 或 `meme_gif_opening_hook（梗图 GIF 开场钩子）` 写成所有内容唯一默认。
- 若开头 reference 不完整，只能继承 `effect_targets（效果目标）` 和机制字段，不得复刻人物、头像、字体、构图或第三方可识别资产。

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
```

### 4A.3 quality_issue_classifier（质量短板分类器）

触发信号：

- 用户反馈“不对 / 怪 / 不顺 / demo 感”。
- 技术通过但内容、人感、证据、声音、卡片密度或剪辑节奏不舒服。
- 需要生成或复核 `quality_lock_card（质量锁卡）`。

执行侧输出必须包含：

```text
quality_issue_classifier:
  input_signal:
  observed_evidence:
  issue_categories:
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

### 4A.4 与 Completion Relay Gate 的关系

本轮或后续任务一旦触发三个函数之一，`Completion Relay Gate（补全接力闸门）` 的 `required_output_inventory（必须交付清单）` 必须纳入：

1. 对应推理函数输出。
2. 对应卡片 / 决策包是否引用该函数。
3. 入口规则是否要求先输出该函数。
4. fixture / 最小样例是否覆盖正常判断与 blocked 判断。
5. `remaining_work_check（剩余工作检查）` 是否确认没有剩余 must-fix。

## 5. 事实源裁决规则

默认事实源优先级：

1. GitHub / 本地 `main` 上的当前仓库文件。
2. `GPT数据源/` 当前正式机制包和事实文件。
3. `codex_log/latest.md`，但重要结论要回查直接源文件。
4. `dist/latest_review_pack/summary.json` 和 `review_manifest.md` 作为当前复审包状态证据。
5. 用户本轮明确指令，只对本轮有效；若要成为下一聊天事实，必须写回仓库。
6. GPT Project 静态上传包，只是协作包，不是实时事实库。
7. DeepSeek / Perplexity 输出只做供料或研究参考，不直接拍板项目事实。

必须裁决的冲突：

| conflict | Codex decision |
| --- | --- |
| GPT Project static package vs GitHub main | GitHub main wins |
| User current explicit instruction vs repo old fact | current instruction guides this round; sync to repo to become durable fact |
| DeepSeek supply vs original repo files | original repo files win |
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
| `completed` | 必交付项全部完成、验证通过、日志 / 路径 / 包同步完成、无禁止状态推进、无剩余 must-fix | 任一 required item 未完成 |
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

**Codex 每轮先用 `state_action_router` 判状态和动作，再用 `Completion Relay Gate` 把动作做完；没有状态动作判断不得执行，没有补全接力复核不得写 completed。**
