# 20260607｜实现设计层机制升级 implementation_design_layer

## 1. 任务定位

- `project_route = video_factory`
- `task_type = mechanism_or_route_fix + project_file_change + gpt_project_sync_package_update`
- `current_project_state = formal_operation_active`
- `inferred_state = requirement_alignment_needed + implementation_design_needed + mechanism_repair_needed + gpt_project_sync_needed`
- `large_task_gate.triggered = true`
- `lane = audit_lane -> standard_lane`
- `parallel = serial_only`

## 2. 本轮新增机制

本轮新增 `implementation_design_layer（实现设计层）`，位置固定在：

```text
目标层
-> 机制层
-> 实现设计层
-> 流程层
-> 判断标准层
-> 反馈层
```

以后所有需要 Codex 落地的方案，ChatGPT / GPT Project 在生成 Codex prompt 前必须先补：

1. `target_effect（目标效果）`
2. `codex_capability_boundary（Codex 当前能力边界）`
3. `confirmed_capabilities（已确认能力）`
4. `unverified_capabilities（待验证能力）`
5. `preferred_execution_route（首选执行路线）`
6. `fallback_routes（替代路线 / fallback）`
7. `capability_probe_tasks（能力探测任务）`
8. `done_when（完成标准）`
9. `blocked_if（阻断条件）`

缺实现设计层时，不得把审美方向、机制名、工具名或“高级感”直接交给 Codex 猜实现。

## 3. 卡片类示例边界

卡片视觉任务不得只写“高级感 / 社交编辑感 / 好看一点”。

默认实现路线：

- 首选路线：HyperFrames。仅当 runtime 可用且能满足目标卡片质感时使用；最小 runtime 通过不等于审美长期稳定。
- 替代路线 A：`image2 / 图片生成能力`。必须先做能力探测；未探测通过不得写成已确认可用。
- 替代路线 B：HTML/CSS 截图或 PIL 生成 `1920x1080` 静态卡片。只能作为 fallback，不得冒充 HyperFrames 动效。
- 阻断线：静态卡片仍像 PPT / 机械 UI、会改 locked copy、遮挡证据、fallback 损失目标效果或需要用户授权但未授权时，必须 blocked。

## 4. 已接入文件

- `GPT数据源/01_项目系统提示词.md`：六层确认链和 GPT Project 侧实现设计层硬规则。
- `GPT数据源/03_总索引与阅读顺序.md`：Codex 落地方案进入前必须读取并输出实现设计层。
- `GPT数据源/05_文案路由规则.md`：卡片落地前的实现设计字段、路线、fallback 和 blocked。
- `GPT数据源/07_AI知识类视频价值规则.md`：卡片实现路线的价值边界，防止把技术成功写成审美 / 内容通过。
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`：新增 `implementation_design_needed` 状态，并把 `requirement_alignment_needed` 升级为六层。
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`：卡片视觉参考契约接入实现设计层字段。
- `codex_source/00_codex_readme.md`：Codex 侧新增 `implementation_design_required gate`。
- `codex_source/19_project_state_action_router.md`：Codex 状态动作策略接入 `implementation_design_needed`。
- `codex_source/20_reference_to_execution_contract.md`：reference 任务缺实现设计层时阻断。
- `codex_source/21_codex_judgment_permission_matrix.md`：Codex 判断权限表新增实现设计层权限边界。
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`：机制修补流补充实现路线缺失 / fallback 未写的入口。

## 5. DeepSeek 参与报告

### 5.1 执行前供料

- `supply_request = codex_log/supply_requests/20260607_implementation_design_layer_pre_supply_request.json`
- `supply_pack = dist/deepseek_supply_controller/implementation_design_layer_20260607_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `api_key_printed = false`
- `api_key_written = false`
- `env_file_read = false`
- `token_usage_expectation_check = token_decrement_expected`
- `boundary = 本轮只证明执行前供料真实参与；不写成 multi-agent runtime 长期稳定，也不把 DeepSeek 供料替代 Codex 原文件复核。`

### 5.2 后置风险复核

- `post_risk_request = codex_log/supply_requests/20260607_implementation_design_layer_post_risk_review_request.json`
- `post_risk_pack = dist/deepseek_supply_controller/implementation_design_layer_20260607_post_risk_review/latest_supply_pack.md`
- `post_risk_controller_status = blocked_invalid_context_pack`
- `deepseek_actual_participation = not_attempted_policy_violation`
- `fallback_status = not_used`
- `not_deepseek_conclusion = true`
- `api_key_printed = false`
- `api_key_written = false`
- `boundary = 后置风险结论来自 Codex 本地验证；不得写成 DeepSeek 已完成后置风险审查。`

## 6. GPT Project 同步包

- `package_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/上传说明_UPLOAD_MANIFEST.md`
- `ready_for_user_upload = true_after_manifest_and_path_verification`
- `user_uploaded_to_gpt_project_ui = false / not_claimed`

## 7. 状态边界

本轮不生成视频、不生成音频、不调用 TTS API、不调用图片 / 视频生成 API、不修改 `dist/latest_review_pack/`、不修改 `public/`。

未推进：

- `content_validation`
- `send_ready`
- `publish_status_success`
- `voice_validation`
- `final_voice_validated`
- `visual_master_locked`
- `current_data_goal_anchor ready`

## 8. 验证结果

- `git diff --check = passed`
- `rg implementation_design_layer / implementation_design_needed / 实现设计层 = passed`
- `rg 目标层 -> 机制层 -> 实现设计层 -> 流程层 -> 判断标准层 -> 反馈层 = passed`
- `rg image2 / HyperFrames / blocked_need_implementation_design_layer / 上传说明_UPLOAD_MANIFEST.md = passed_with_boundary_language`
- `DeepSeek pre-supply request / supply pack JSON = passed`
- `DeepSeek post-risk-review request / blocked output JSON = passed`
- `package_forbidden_file_path_scan = passed`
- `dist/latest_review_pack / public / GPT数据源/08_当前正式事实.md diff check = passed`
- `secret_value_scan = passed`
- `status_assignment_scan = passed`
- `package_file_count = 23`
- `path_limited_stage_commit_push_readback = pending_current_task_git_sync`
