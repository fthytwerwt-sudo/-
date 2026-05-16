# 20260516｜Codex 判断权限表与 HyperFrames 判断卡 / 总结卡基线

## 1. 本轮范围

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补、项目文件修改、判断权限补全和 HyperFrames 卡片执行基线补强。
- `已确认` 本轮不生成视频、不修改已发布视频、不修改 `dist/latest_review_pack/`，不推进 `send_ready（可发送状态）`、`content_validation（内容验证）`、`publish_status_success（发布成功口径）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。
- `已确认` 本轮使用 `explore_plus_integrate（探索 + 单点整合）`：Lane A 只读研究判断权限表，Lane B 只读研究 HyperFrames 卡片基线，Integrator 是唯一写入 owner。

## 2. route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - mechanism_or_route_fix
    - route_repair
    - project_file_change
    - codex_execution_permission_matrix
    - hyperframes_card_baseline_repair
  responsibility_layer:
    - Codex execution layer
    - route layer
    - validation layer
    - sync layer
  large_task_gate:
    triggered: true
    reason: 本轮同时涉及判断权限、HyperFrames 卡片基线、多文件规则同步、日志回流
    lane_recommendation: audit_lane -> standard_lane
    parallel_recommendation: explore_plus_integrate
    write_owner: Codex Integrator only
    read_only_lanes:
      - lane_A_permission_matrix_research
      - lane_B_hyperframes_card_baseline_research
    integration_owner: Codex single write owner
  execution_permission: allowed_after_impact_check
```

## 3. state_action_router

```text
state_action_router:
  input_signal: 用户要求补齐 Codex 判断权限，并把 HyperFrames 设为判断卡 / 总结卡强制执行基线
  current_project_state: formal_operation_active
  fact_source_arbitration:
    primary_source: 当前仓库文件
    secondary_sources:
      - Perplexity 外部资料包摘要
      - ChatGPT 本轮桥接说明
    conflict_detected: true
    conflict_resolution:
      - 外部资料中 opening_route 权限判断与项目现有规则冲突时，以项目现有规则为准
      - 外部资料只作参考，不直接升级成项目事实
  inferred_state:
    - codex_judgment_permission_matrix_needed
    - hyperframes_judgment_summary_card_baseline_needed
    - route_permission_boundary_repair_needed
  selected_action:
    - 建立 Codex 判断权限表
    - 扩展 HyperFrames 卡片动效基线
    - 更新入口引用和完成检查
  blocked_if:
    - 关键入口文件缺失
    - HyperFrames 插件 / 运行入口被写成已接入但实际不存在
    - 修改会推进视频状态或数据目标 ready
```

## 4. impact_check_report

### 4.1 已发现的卡片判断

- `GPT数据源/05_文案路由规则.md` 已定义 `content_route_card V2（内容路由卡 V2）` 与 `card_placement_decision（卡片位置判断）`，覆盖总结卡、反转卡、结果差卡、Prompt 尾卡。
- `codex_source/19_project_state_action_router.md` 已把卡片位置判断接入 `content_route_inference_function（内容路由推理函数）` 和 `editing_inference_function（剪辑推理函数）`。
- 本轮补强后，判断卡、边界卡、判断卡 / 总结卡的 HyperFrames 字段已接入 `content_route_card V2` 与 `card_placement_decision`。

### 4.2 已发现的 HyperFrames 边界

- `GPT数据源/05_文案路由规则.md` 与 `GPT数据源/07_AI知识类视频价值规则.md` 已确认 HyperFrames 只能作为卡片动效承载层，不替代中段真实录屏证据。
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md` 已确认 HyperFrames 不是新视觉 route、不是中段录屏叠层、不是整条视频生成层，也不是云端剪辑替代品。

### 4.3 当前缺口与修正

- `已修正` 仓库此前没有专门 `Codex 判断权限表`；本轮新增 `codex_source/21_codex_judgment_permission_matrix.md`。
- `已修正` 仓库此前没有把 `judgment_card（判断卡）` 与 `summary_card（总结卡）` 明确写成 HyperFrames 强制基线；本轮已写入 `hyperframes_card_motion_baseline（HyperFrames 卡片动效基线）`。
- `已修正` `content_route_card V2` 的 `card_plan` 已补 `hyperframes_required / hyperframes_motion_type / hyperframes_runtime_status / visual_quality_gate / blocked_if`。

### 4.4 HyperFrames runtime / plugin 状态

- `已确认` 当前 Codex 会话可读取 HyperFrames skill，但这不等于仓库已有项目级 runtime。
- `已确认` `package.json` 仅发现 `ffmpeg-static`，未发现 HyperFrames SDK / runtime 依赖。
- `已确认` `scripts/` 未发现显式 HyperFrames plugin / script / runtime entry。
- `待验证` 当前仓库没有可证明长期稳定的 HyperFrames 真实运行入口；后续真实视频若要求 HyperFrames 且仓库 runtime 仍不可用，必须 `blocked` 或等待用户明确授权降级。

## 5. files_changed

- `codex_source/21_codex_judgment_permission_matrix.md`：新增 Codex 判断权限表，覆盖四层权限与 17 个判断对象。
- `codex_source/fixtures/codex_judgment_permission_matrix_cases.json`：新增最小 JSON 验证样例，覆盖 opening route 修正、判断卡 HyperFrames runtime 缺失、总结卡不强插、文案修改请求和发布候选阻断。
- `GPT数据源/05_文案路由规则.md`：补强 content_route_card V2、card_placement_decision、judgment_card、boundary_card、HyperFrames 判断卡 / 总结卡动效基线。
- `GPT数据源/07_AI知识类视频价值规则.md`：补强 HyperFrames 对判断卡 / 总结卡的价值边界。
- `GPT数据源/08_当前正式事实.md`：新增本轮机制已写入事实与待验证 runtime 边界。
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`：接入权限表、HyperFrames 基线、completion truth check。
- `codex_source/00_codex_readme.md`：入口补读权限表与判断权限 gate。
- `codex_source/01_execution_rules.md`：新增 Codex 判断权限闸门、HyperFrames 卡片动效闸门和完成真实性检查项。
- `codex_source/19_project_state_action_router.md`：接入判断权限表与 HyperFrames 判断卡 / 总结卡 baseline 状态。
- `codex_log/supply_requests/20260516_codex_judgment_permission_and_hyperframes_baseline_pre_supply_request.json`：新增本轮供料请求任务卡；因本轮禁止真实外部 API 调用，记录为 `fallback_local_only`。
- `codex_log/latest.md`：新增本轮摘要。
- `codex_log/20260516_codex_judgment_permission_and_hyperframes_baseline.md`：本日志。

## 6. codex_judgment_permission_matrix

- `已新增` 专门文件：`codex_source/21_codex_judgment_permission_matrix.md`。
- `已确认` 四层权限完整写入：
  - `must_decide_and_execute（必须判断并可执行）`
  - `must_decide_but_request_change（必须判断但只能请求修改）`
  - `must_decide_and_block（必须判断并阻断）`
  - `must_escalate_to_chatgpt_or_user（必须升级给 ChatGPT / 用户）`
- `已覆盖` 判断对象：`opening_route_decision`、`card_placement_decision`、`judgment_card`、`summary_card`、`result_diff_card`、`boundary_card`、`prompt_tail_card`、`script_to_timeline_map`、`subtitle_segmentation`、`tts_prosody`、`material_evidence`、`visual_mismatch`、`aspect_ratio_resolution`、`publish_candidate_readiness`、`data_goal_alignment`、`copy_change_request`、`human_review_required`。
- `已修正` Perplexity 资料中不适合本项目的 opening route / judgment card / summary card 权限判断。

## 7. hyperframes_baseline_result

- `已写入` `judgment_card_motion（判断卡动效）`。
- `已写入` `summary_card_motion（总结卡动效）`。
- `已确认` 当 `card_placement_decision` 选择 `judgment_card` 或 `summary_card` 时，HyperFrames 是默认强制执行基线。
- `已确认` HyperFrames 不替代真实录屏证据，不改 locked copy，不新增素材里没有的数据结论，不推进内容验证。
- `待验证` HyperFrames runtime 未验证；未来真实视频若要求 HyperFrames 且 runtime 不可用，必须 `blocked` 或等待用户明确授权降级。

## 8. validation_plan

本轮必须验证：

- `git diff --check`
- `codex_source/fixtures/codex_judgment_permission_matrix_cases.json` JSON parse
- 重新读取关键文件确认规则存在
- forbidden status scan 确认未推进禁止状态

## 9. status_boundary

- `未推进` `content_validation` 到 `passed`
- `未推进` `send_ready` 到 `true`
- `未推进` `voice_validation` 到 `passed`
- `未推进` `final_voice_validated` 到 `true`
- `未推进` `visual_master_locked` 到 `true`
- `未推进` `current_data_goal_anchor` 到 `ready`
- `未声明` HyperFrames runtime 已完成长期稳定验证

## 10. next_target

后续若进入真实视频执行，先检查是否真的存在 HyperFrames plugin / script / runtime entry；若 judgment_card / summary_card 被选中且 runtime 仍不可用，必须 blocked 或等待用户授权降级，不能静态卡片冒充 HyperFrames。
