# 当前运营目标 current_operation_target

## 1. canonical status

`已确认` 本文件是《视频工厂》当前运营阶段的 canonical 入口。

旧文件 `codex_log/current_gray_test_target.md` 已从当前默认入口降级为 `legacy_compatibility_pointer（历史兼容指针）`。后续截图、评论、私信、咨询、平台数据或复盘任务，默认进入：

- `formal_operation_active（正式运营中）`
- `operation_data_intake（运营数据录入）`
- `operation_review（运营复盘）`
- `operation_next_variable_decision（运营下一变量判断）`

## 2. current_project_stage

```yaml
current_project_stage:
  stage: "formal_operation_active"
  iteration_mode: "data_driven_operation_iteration"
  operation_loop: "data_driven_operation_loop"
  previous_stage_term:
    value: "gray_test"
    status: "legacy_previous_term"
    rule: "只保留为历史路径、历史记录或兼容别名，不再作为当前默认路由。"
  formal_operation_boundary:
    - "正式运营 = 项目进入真实发布与数据回流阶段。"
    - "正式运营 != 内容成功。"
    - "正式运营 != 商业验证成立。"
    - "正式运营 != 当前视频内容通过。"
    - "正式运营 != 数据飞轮已经跑通。"
    - "正式运营 != multi-agent runtime 长期稳定。"
    - "正式运营 != current_data_goal_anchor ready。"
```

## 3. current_operation_target

```yaml
current_operation_target:
  video_id: "V003"
  title: "以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件"
  operation_record_status: "current_operation_target"
  publish_platform: "抖音"
  publish_time_visible: "2026-05-14 04:50"
  video_duration: "04:03"
  current_observation_window: "between_24h_and_72h / interim_36h_snapshot + between_48h_and_72h / interim_65h_snapshot + post_72h_pre_7d / post_72h_pre_7d_snapshot"
  record_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md"
  structured_snapshot_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_post_72h_pre_7d_snapshot.json"
  previous_structured_snapshot_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_interim_65h_snapshot.json"
  earlier_structured_snapshot_path: "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_早期数据快照_early_interim_snapshot.json"
  screenshot_manifest_path: "review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_截图清单_screenshot_manifest.md"
  account_diagnostic_path: "review_loop/account_diagnostics/20260517_account_diagnostic_snapshot/account_diagnostic_20260510_20260516.json"
  data_completeness: "partial_post_72h_pre_7d_data_recorded"
  data_confidence: "low_to_medium_for_recording_only / low_for_diagnosis"
  next_required_data:
    - "7d_data"
    - "3s_retention"
    - "profile_visit_count"
    - "dm_count"
    - "effective_dm_count"
    - "effective_consult_count"
    - "clear_need_customer_count"
```

## 4. operation_records

| video_id | title | operation_record_status | record_path | current_status |
| --- | --- | --- | --- | --- |
| V001 | 我用 AI 做 PPT 踩过的坑 | `historical_operation_record` | `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md` | 历史运营样本，原灰度字段保留为 legacy |
| V002 | 自动流的最简单流程 | `policy_limited_abnormal_operation_sample` | `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_发布后复盘记录_post_publish_review_record.md` | 平台审核减推异常样本，不作为正常分发样本 |
| V003 | 以后会分享实用的，每天会给大家看我是怎么优化的，这个视频只用3个小时写出来的本地文件 | `current_operation_target` | `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_发布后灰度数据记录_post_publish_gray_test_record.md` | 当前运营目标，约 37 小时、65 小时和 72h 后 / 7d 前数据已录入；仍非 7d final |

## 5. current_data_goal_anchor

- anchor_path：`codex_log/current_data_goal_anchor.md`
- anchor_instance_status：`partial_data_recorded`
- data_confidence：`low_to_medium`
- main_bottleneck_draft：`opening_retention_and_initial_distribution_weak / draft_low_confidence`
- primary_variable_draft：`opening_route_or_first_5s_packaging / draft_low_confidence`
- ready_status：`not_ready`
- why_not_ready：V003 已补到 72h 后 / 7d 前快照，但仍缺 7d 数据、3s 留存、V003 单条视频主页访问、私信、有效私信、有效咨询、清晰需求客户和人审后的正式复盘判断。

## 6. not_allowed

- 不得把正式运营写成内容通过。
- 不得把正式运营写成商业模式成立。
- 不得把 V003 的 143 播放写成项目失败。
- 不得把 V003 收藏率 2.10% 写成方向成立。
- 不得把 `interim_36h_snapshot`、`interim_65h_snapshot` 或 `post_72h_pre_7d_snapshot` 写成 7d final；本轮 `post_72h_pre_7d_snapshot` 也不得写成精确 72h 截止点。
- 不得生成下一条正式视频执行 prompt。
- 不得推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。

## 7. next_target

等 V003 7d 数据和需求侧字段补齐后，进入 `operation_review（运营复盘）`，只回答运营复盘四问：是否达到阶段门槛、当前最短板层、下一轮唯一运营变量、改完看哪个指标。
