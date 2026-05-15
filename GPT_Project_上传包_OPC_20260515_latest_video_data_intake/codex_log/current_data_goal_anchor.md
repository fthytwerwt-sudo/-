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
- `已确认` 本轮已录入 V003 的 `interim_36h_snapshot（约 37 小时早期截图）`。
- `待验证` 72h / 7d 数据尚未补齐，本文件不能被写成正式数据驱动执行已 ready。

## 2. current_data_goal_anchor（当前数据目标锚点）

```yaml
current_data_goal_anchor:
  file_role: "当前这一条 / 下一条视频实际使用的数据目标锚点卡"
  instance_scope: "current_or_next_video_execution_anchor"
  current_video:
    video_id: "V003"
    video_title: "以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件"
    video_record_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md"
    structured_snapshot_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_早期数据快照_early_interim_snapshot.json"
    screenshot_manifest_path: "review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md"
    target_switch_note: "最新一期视频切换；V001 保留为 previous / historical，V002 为既有平台审核减推异常样本。"

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
    anchor_instance_status: "partial_data_recorded"
    previous_anchor_instance_status: "waiting_data"
    data_confidence: "low"
    human_review_required: true
    reason: "V003 已录入约 37 小时早期截图，但 72h / 7d 数据、3s_retention、私信和有效咨询仍缺失，不能生成 ready 级数据驱动锚点。"

  current_north_star_goal:
    value: "3-6 个月内，验证《视频工厂》能否通过真实 AI 使用内容，稳定产生高质量需求信号，并沉淀出可承接的服务 / 工作包 / 咨询方向。"
    status: "stage_hypothesis"

  current_stage_goal:
    value: "基于 V003 最新视频早期数据判断是否继续进入 72h / 7d 观察；本轮只做数据回填和早期诊断，不生成正式下一条视频执行 prompt。"
    status: "partial_data_recorded_waiting_72h_7d"

  current_state:
    active_state:
      - "post_publish_gray_test"
      - "data_intake"
      - "early_interim_observation"
    not_active_yet:
      - "official_post_publish_review"
      - "lead_quality_validation"
      - "offer_validation"
      - "scale_or_reposition"
      - "next_formal_script_execution"
    note: "当前处于 V003 post_publish_gray_test，只有 interim_36h_snapshot。"

  previous_data_summary:
    review_window:
      interim_36h_snapshot: "已录入，约发布后 37 小时"
      "72h": "missing"
      "7d": "missing"
    play_count: 141
    average_watch_time: "21秒"
    cover_click_rate: "0.00%"
    two_second_bounce_rate: "50.00%"
    average_play_ratio: "8.51%"
    completion_rate: "4.17%"
    five_second_completion_rate: "28.13%"
    like_count: 2
    like_rate: "1.42%"
    favorite_count: 3
    favorite_rate: "2.13%"
    comment_count: 0
    share_count: 0
    danmu_count: 0
    new_follow_count: 1
    fan_play_ratio: "4.3%"
    traffic_sources:
      recommendation_page: "97.2%"
      profile_page: "1.4%"
      friend_page: "1.4%"
    audience_summary:
      gender_male: "77%"
      gender_female: "23%"
      top_regions: "广东17.27%, 北京13.64%, 江苏9.09%, 湖北5.45%, 四川5.45%, 河北4.55%, 河南4.55%, 上海4.55%"
      active_distribution: "heavy 72%, medium 18%, light 6%, unknown 4%"
    missing_fields:
      - "3s_retention"
      - "profile_visit_count"
      - "dm_count"
      - "effective_dm_count"
      - "effective_consult_count"
      - "clear_need_customer_count"
      - "effective_comment_quality"
      - "72h_final_data"
      - "7d_final_data"
    uncertain_fields:
      - "exact_observation_window_from_platform"
      - "age_distribution_estimated_from_bar_chart"
      - "trend_curve_point_values"

  diagnosis:
    main_bottleneck:
      value: "opening_retention_and_initial_distribution_weak"
      status: "draft_low_confidence"
      evidence:
        - "play_count = 141，仍是早期极小样本"
        - "two_second_bounce_rate = 50.00%"
        - "five_second_completion_rate = 28.13%"
        - "completion_rate = 4.17%"
        - "recommendation_page = 97.2%，平台给过初始推荐但承接不足"
    confidence: "low"
    cannot_conclude_if:
      - "72h / 7d 核心字段未回填"
      - "3s_retention、主页访问、私信、有效咨询缺失"
      - "只有早期极小样本，不能裁决方向失败或方向成立"
      - "没有用户 / ChatGPT 对主要短板层的最终判断"

  variable_plan:
    primary_variable:
      value: "opening_route_or_first_5s_packaging"
      status: "draft_low_confidence"
      validation_metric:
        - "2s bounce"
        - "5s completion"
        - "3s retention if later available"
        - "average_watch_time"
    supporting_variables: []
    forbidden_variables:
      - "未完成复盘前不得改变 target_user（目标用户）"
      - "未完成复盘前不得改变 core_topic_direction（核心选题方向）"
      - "未完成复盘前不得改变 offer_or_monetization（承接 / 变现口径）"
      - "未完成复盘前不得把多个变量同时改写成 single_primary_variable（单主变量）"
      - "未完成复盘前不得把内容状态、发布状态、声音状态或视觉母版状态推进"
    total_change_variables: 0
    major_revision: "false_waiting_72h_7d"
    attribution_boundary: "当前只有 early_interim_snapshot，不能把下一条结果归因到任何主变量。"

  execution_anchor:
    next_video_structure_plan:
      status: "not_generated_waiting_72h_7d"
      note: "需等正式复盘回答 6000 门槛、短板层、唯一变量和验证指标后生成。"
    next_video_execution_prompt:
      status: "not_generated_this_round"
      note: "本轮不得进入正式 Codex 视频执行。"
    success_metric:
      value: "pending_72h_7d_completion"
      status: "waiting_more_data"
    failure_metric:
      value: "pending_72h_7d_completion"
      status: "waiting_more_data"
    post_publish_validation_metric:
      value: "2s_bounce_5s_completion_3s_retention_if_available_average_watch_time"
      status: "draft_low_confidence"

  codex_execution_policy:
    codex_may_adapt:
      - "screenshot_archive"
      - "field_extraction"
      - "missing_field_marking"
      - "early_interim_summary"
      - "DeepSeek supply request"
      - "GPT Project static package sync"
    codex_must_not_adapt:
      - "current_stage_goal"
      - "main_bottleneck"
      - "primary_variable"
      - "forbidden_variables"
      - "success_metric"
      - "failure_metric"
      - "post_publish_validation_metric"
      - "user_or_chatgpt_locked_data_goal_judgment"
      - "content_validation"
      - "send_ready"
      - "publish_status"
      - "voice_validation"
      - "final_voice_validated"
      - "visual_master_locked"

  blocked_if:
    - "missing_current_stage_goal"
    - "missing_main_bottleneck_when_claiming_data_driven"
    - "missing_primary_variable_before_codex_execution"
    - "missing_forbidden_variables_before_single_variable_experiment"
    - "missing_success_or_failure_metric"
    - "missing_post_publish_validation_metric"
    - "missing_required_review_data_when_claiming_post_publish_diagnosis"
    - "anchor_instance_status_is_partial_data_recorded_but_task_claims_ready"
    - "task_generates_next_formal_script_from_interim_snapshot"

  done_when:
    - "anchor_instance_status_is_ready_or_blocked_with_reason"
    - "all_locked_fields_have_status"
    - "missing_fields_are_explicit"
    - "codex_execution_policy_is_defined"
    - "data_goal_alignment_check_required"

  data_goal_alignment_check_required: true
```

## 3. 使用规则

1. 命中文案修改、下一条视频、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步时，必须先读取本文件。
2. `anchor_instance_status = waiting_data / partial_data_recorded / draft` 时，只能做数据录入、假设版锚点、机制接线、供料任务卡或 blocked 说明，不得写正式数据驱动执行 ready。
3. `anchor_instance_status = ready` 只能在核心复盘字段、主短板、主变量、禁止变量、成功指标、失败指标和发布后验证指标都明确且经过人审后写入。
4. Codex 可归档截图和整理早期数据，但不得改写本文件里已锁定的数据目标字段。
5. 缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。

## 4. 当前状态结论

- `已确认` 当前实例锚点入口已存在。
- `已确认` 当前实例锚点状态从 `waiting_data` 更新为 `partial_data_recorded`。
- `已确认` V003 早期截图数据已回填，但只属于 `interim_36h_snapshot`。
- `待验证` 72h / 7d 数据仍缺失。
- `待验证` 主短板和主变量仍是 `draft_low_confidence`，不得进入正式视频执行。
- `不适用` 本轮不做内容复审，不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。

## 5. why_not_ready

`current_data_goal_anchor` 不能写成 `ready`，原因：

1. V003 只有约发布后 37 小时的早期截图。
2. 72h / 7d 数据缺失。
3. `3s_retention`、`profile_visit_count`、`dm_count`、`effective_dm_count`、`effective_consult_count` 缺失。
4. 当前主短板只是 `draft_low_confidence`，未经过用户 / ChatGPT 最终复盘。
5. `success_metric` / `failure_metric` 仍待 72h / 7d 补足。
6. 本轮任务明确禁止生成下一条正式文案或推进执行状态。
