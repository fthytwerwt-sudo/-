# 当前数据目标锚点 current_data_goal_anchor

## 1. 文件定位

本文件是《视频工厂》当前这一条 / 下一条视频实际使用的 `data_goal_anchor（数据目标锚点）` 实例卡。

它的职责是：

- 给 ChatGPT / GPT Project / Codex / DeepSeek 提供稳定的当前锚点入口。
- 防止 Codex 每次从 `video_goal_card`、`post_publish_review_card`、`data_flywheel_memory` 和 `content_structure_feedback_card` 里现场拼锚点。
- 让 `content_route_card V2`、`script_to_timeline_map`、`editing_decision_pack`、`assembly_decision_pack` 和 `data_goal_alignment_check` 都能回指同一个当前实例。

它不替代：

- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
- `review_loop/` 当前视频复盘记录
- ChatGPT / 用户的最终判断

状态边界：

- `已确认` 当前实例锚点入口已写入。
- `待验证` 真实任务中是否稳定读取本文件并完成数据目标对齐。
- `待验证` 当前灰度数据尚未回填，本文件不能被写成正式数据驱动执行已 ready。

## 2. current_data_goal_anchor（当前数据目标锚点）

```yaml
current_data_goal_anchor:
  file_role: "当前这一条 / 下一条视频实际使用的数据目标锚点卡"
  instance_scope: "current_or_next_video_execution_anchor"
  source_layers:
    - "GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md"
    - "GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md"
    - "codex_log/current_gray_test_target.md"
    - "codex_log/current_publish_target.md"
    - "review_loop 当前视频复盘记录"
    - "video_goal_card"
    - "post_publish_review_card"
    - "data_flywheel_memory"
    - "content_structure_feedback_card"

  status:
    anchor_instance_status: "waiting_data"
    data_confidence: "low"
    human_review_required: true
    reason: "当前 v3.1 灰度测试 24h / 72h / 7d 数据仍待用户回填，不能生成 ready 级数据驱动锚点。"

  current_north_star_goal:
    value: "3-6 个月内，验证《视频工厂》能否通过真实 AI 使用内容，稳定产生高质量需求信号，并沉淀出可承接的服务 / 工作包 / 咨询方向。"
    status: "stage_hypothesis"

  current_stage_goal:
    value: "等待 v3.1 灰度测试数据回填后，判断下一轮唯一主变量；数据未回填前只能生成假设版执行锚点，不得进入正式数据驱动视频执行。"
    status: "waiting_data"

  current_state:
    active_state:
      - "content_validation"
      - "demand_signal_validation"
    not_active_yet:
      - "lead_quality_validation"
      - "offer_validation"
      - "scale_or_reposition"
    note: "当前处于 post_publish_gray_test，尚未完成 24h / 72h / 7d 数据回填。"

  previous_data_summary:
    review_window:
      "24h": "待用户回填"
      "72h": "待用户回填"
      "7d": "待用户回填"
    play_count: "待填"
    retention: "待填"
    save_rate: "待填"
    comment_quality: "待填"
    dm_count: "待填"
    valid_leads: "待填"
    lead_quality_score: "待填"
    missing_fields:
      - "24h_play_count"
      - "72h_play_count"
      - "7d_play_count"
      - "3s_retention"
      - "completion_rate"
      - "average_watch_time"
      - "favorite_count"
      - "favorite_rate"
      - "comment_quality"
      - "dm_count"
      - "effective_dm_count"
      - "valid_leads"

  diagnosis:
    main_bottleneck:
      value: "待验证_waiting_gray_test_data"
      status: "waiting_data"
    confidence: "low"
    cannot_conclude_if:
      - "24h / 72h / 7d 核心字段未回填"
      - "只有播放量，没有留存 / 完播 / 收藏 / 评论 / 私信 / 有效咨询"
      - "没有用户 / ChatGPT 对主要短板层的判断"

  variable_plan:
    primary_variable:
      value: "待填_waiting_post_publish_review"
      status: "waiting_data"
    supporting_variables: []
    forbidden_variables:
      - "未完成复盘前不得改变 target_user（目标用户）"
      - "未完成复盘前不得改变 offer_or_monetization（承接 / 变现口径）"
      - "未完成复盘前不得把多个变量同时改写成 single_primary_variable（单主变量）"
      - "未完成复盘前不得把内容状态、发布状态、声音状态或视觉母版状态推进"
    total_change_variables: 0
    major_revision: "待定_waiting_data"
    attribution_boundary: "当前数据不足，不能把下一条结果归因到任何主变量。"

  execution_anchor:
    next_video_structure_plan:
      status: "待填_waiting_post_publish_review"
      note: "需等复盘回答 6000 门槛、短板层、唯一变量和验证指标后生成。"
    next_video_execution_prompt:
      status: "待填_waiting_post_publish_review"
      note: "缺当前 ready 级锚点前，不得进入正式 Codex 视频执行。"
    success_metric:
      value: "待填_waiting_post_publish_review"
      status: "waiting_data"
    failure_metric:
      value: "待填_waiting_post_publish_review"
      status: "waiting_data"
    post_publish_validation_metric:
      value: "待填_waiting_post_publish_review"
      status: "waiting_data"

  codex_execution_policy:
    codex_may_adapt:
      - "segment_order"
      - "card_position"
      - "editing_style"
      - "assembly_sequence"
      - "material_binding"
      - "tts_segmentation"
      - "fallback_visuals"
    codex_must_not_adapt:
      - "current_stage_goal"
      - "main_bottleneck"
      - "primary_variable"
      - "forbidden_variables"
      - "success_metric"
      - "failure_metric"
      - "post_publish_validation_metric"
      - "user_or_chatgpt_locked_data_goal_judgment"

  blocked_if:
    - "missing_current_stage_goal"
    - "missing_main_bottleneck_when_claiming_data_driven"
    - "missing_primary_variable_before_codex_execution"
    - "missing_forbidden_variables_before_single_variable_experiment"
    - "missing_success_or_failure_metric"
    - "missing_post_publish_validation_metric"
    - "missing_required_review_data_when_claiming_post_publish_diagnosis"
    - "anchor_instance_status_is_waiting_data_but_task_claims_ready"

  done_when:
    - "anchor_instance_status_is_ready_or_blocked_with_reason"
    - "all_locked_fields_have_status"
    - "missing_fields_are_explicit"
    - "codex_execution_policy_is_defined"
    - "data_goal_alignment_check_required"

  data_goal_alignment_check_required: true
```

## 3. 使用规则

1. 命中文案修改、下一条视频、视频执行、剪辑、编排、装配、DeepSeek 供料或 GPT Project 静态包同步时，必须先读取本文件。
2. `anchor_instance_status = waiting_data / draft` 时，只能做假设版锚点、机制接线、供料任务卡或 blocked 说明，不得写正式数据驱动执行 ready。
3. `anchor_instance_status = ready` 只能在核心复盘字段、主短板、主变量、禁止变量、成功指标、失败指标和发布后验证指标都明确后写入。
4. Codex 可调整执行结构，但不得改写本文件里已锁定的数据目标字段。
5. 缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。

## 4. 当前状态结论

- `已确认` 当前实例锚点入口已新增。
- `已确认` 当前实例锚点状态为 `waiting_data`。
- `待验证` 真实视频任务是否稳定使用本锚点。
- `待验证` 当前数据飞轮真实效果尚未跑通。
- `不适用` 本轮不做内容复审，不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
