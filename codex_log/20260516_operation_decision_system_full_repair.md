# 20260516｜运营决策系统完整修补

## 1. route_decision

- `project_route`: `video_factory`
- `task_type`: `mechanism_or_route_fix + code_execution_or_debug + project_file_change + review_diagnosis_audit + operation_review_system`
- `current_project_state`: `formal_operation_active + operation_review_pending + data_decision_system_missing`
- `large_task_gate`: `triggered`
- `lane_recommendation`: `audit_lane -> standard_lane`
- `parallel_recommendation`: `serial_only`
- `reason`: 本轮同时读取 / 写入脚本、schema/config、三期记录报告、机制文件和日志；写入范围集中在同一组核心入口，必须单点整合。

## 2. state_action_router

- `input_signal`: 用户要求把数据目标锚点 / 数据飞轮 / 运营复盘从概念规则修成可运行运营决策系统。
- `inferred_state`: `operation_decision_system_missing`
- `trigger_mechanism`: `operation_decision_system_full_repair`
- `selected_action`: 实现可运行系统，读取 V001 / V002 / V003，生成三期归纳、V003 判断和最终用户报告。
- `forbidden_action`: 不生成新视频，不改已发布视频，不推进内容、发送、发布成功、声音、最终声音或视觉母版状态，不把 V003 / current_data_goal_anchor 写 ready。
- `done_when`: 三期记录被读取、分类、归纳、判断；缺数据自动 blocked；最终用户报告生成并通过验证。

## 3. system_built

- `script_path`: `scripts/运营决策系统_operation_decision_system.py`
- `schema_path`: `review_loop/decision_engine/operation_decision_schema.json`
- `threshold_config`: `review_loop/decision_engine/threshold_config_stage_hypothesis.json`
- `sample_rules`: `review_loop/decision_engine/sample_classification_rules.json`
- `deepseek_supply_request`: `review_loop/decision_engine/operation_decision_system_supply_request.json`

## 4. report_outputs

- `review_loop/decision_engine/latest_operation_decision_report.json`
- `review_loop/decision_engine/latest_operation_decision_report.md`
- `review_loop/decision_engine/V001_V002_V003_operation_synthesis_report.json`
- `review_loop/decision_engine/V001_V002_V003_operation_synthesis_report.md`
- `review_loop/decision_engine/final_user_operation_result.md`
- `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_operation_decision_result.json`
- `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/V003_operation_decision_result.md`

## 5. records_processed

- `V001`: `historical_operation_record`；历史样本，只作旧阶段参考，不能参与当前归因。
- `V002`: `policy_limited_abnormal_operation_sample`；平台审核减推异常样本，不进入正常自然流量归因。
- `V003`: `current_operation_target`；当前目标样本，只有 `interim_36h_snapshot`，状态仍为 `partial_data_recorded`。

## 6. final_user_result

- `one_sentence_conclusion`: 当前还不能进入下一期正式执行；V003 只有约 37 小时早期数据，系统判断只能继续补数据，并允许低置信度准备开头 / 前 5 秒方向草稿。
- `current_primary_bottleneck`: `opening_retention_and_initial_distribution_weak / draft_low_confidence`
- `can_enter_next_episode_execution`: `false`
- `blocked_reason_if_not`: V003 缺 72h / 7d、3s 留存、主页访问、私信、有效私信、有效咨询和清晰需求客户等关键字段。
- `recommended_next_route`: 先补 V003 关键数据，补齐后重跑 `operation_decision_system`，再判断唯一主变量。

## 7. DeepSeek supply gate

- `supply_request`: `review_loop/decision_engine/operation_decision_system_supply_request.json`
- `output_dir`: `review_loop/decision_engine/deepseek_pre_supply/`
- `deepseek_actual_participation`: `deepseek_passed`
- `fallback_status`: `not_used`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `env_file_read_by_controller`: `false`
- `not_deepseek_conclusion`: `false`

## 8. validation

- `python3 scripts/运营决策系统_operation_decision_system.py --root /Users/fan/Documents/视频工厂`: passed
- JSON 输出可解析：passed
- V001 / V002 / V003 均被读取：passed
- V002 被识别为异常样本：passed
- V003 被识别为 `partial_data_recorded`：passed
- 未生成正式下一条视频执行 prompt：passed
- forbidden status scan：passed

## 9. status_boundary

- `content_validation advanced`: no
- `send_ready advanced`: no
- `publish_status_success advanced`: no
- `voice_validation advanced`: no
- `final_voice_validated advanced`: no
- `visual_master_locked advanced`: no
- `current_data_goal_anchor ready`: no
- `next formal video prompt generated`: no

## 10. remaining_work

- V003 仍缺：`72h_final_data`、`7d_final_data`、`3s_retention`、`profile_visit_count`、`dm_count`、`effective_dm_count`、`effective_consult_count`、`clear_need_customer_count`。
- 下一个安全触发：补齐 V003 72h / 7d 和需求侧字段后，重跑 `scripts/运营决策系统_operation_decision_system.py`。

## 11. final pre-push review

- `已回审修正`: V003 保持 `current_operation_target`，但当前只有 `interim_36h_snapshot` 且缺 72h / 7d 与需求侧字段，因此本轮输出中 `normal_attribution_eligible = false`。
- `decision_assertions`: V001 = `historical_operation_record`；V002 = `policy_limited_abnormal_operation_sample` 且不进入正常归因；V003 = `current_operation_target / partial_data_recorded` 且下一期正式执行 blocked。
- `final_user_report_quality`: `final_user_operation_result.md` 保持用户可直接阅读；不要求用户自行拼接中间 JSON。
- `validation`: `py_compile`、脚本重跑、`--validate-only`、JSON parse、三期分类断言和 forbidden status scan 均通过。
