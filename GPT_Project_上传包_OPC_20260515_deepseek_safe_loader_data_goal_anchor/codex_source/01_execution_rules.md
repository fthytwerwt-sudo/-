# Codex 执行规则

## 1. 文件定位

本文件规定 Codex 在《视频工厂》仓库中的默认执行方式。

它负责：

- 默认读取顺序
- 什么时候必须先审计
- 什么范围可以改
- GPT 数据源与仓库不同步时如何处理
- 仓库型任务的日志、提交、推送与回流规则
- 完成前最小验证要求

## 2. 默认读取顺序

每次任务默认按以下顺序读取：

1. `AGENTS.md`
2. 当前仓库本地 `skills/` 是否存在
3. 若本地无相关 skill，再检查全局 `~/.codex/skills`
4. `codex_source/00_codex_readme.md`
5. `codex_log/latest.md`
6. 若任务命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审，在 `codex_log/latest.md` 之后优先读：
   - `codex_source/19_project_state_action_router.md`
   - `GPT数据源/11_项目状态动作总控器_机制推理层.md`
7. 若任务命中 `reference（参考）`、样片、参考图、参考视频、参考声音、参考效果、“按这个做”、原感稿或外部资料并要求落地，在 `state_action_router（项目状态动作总控器）` 之后、具体执行前必须读：
   - `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
   - `codex_source/20_reference_to_execution_contract.md`
8. 若任务命中“execution lane / parallel gate / 是否适合提速 / 是否适合并发 / lane recommendation / parallel recommendation”，在 `codex_log/latest.md` 之后优先读：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
9. 若任务命中“当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容”，在 `codex_log/latest.md` 之后优先读：
   - `codex_log/current_publish_target.md`
   - 若需要快速复核当前样片的 Git 可追踪轻量证据，再读 `codex_log/current_publish_target_light_evidence.md`
10. 若任务命中“截图 / 数据截图 / 截图数据录入 / 灰度测试 / 发片 / 发布后 / 复盘 / 数据记录 / 24h / 72h / 7 天 / 播放量 / 完播率 / 留存 / 私信 / 咨询 / 下一轮只改一个变量”，在 `current_publish_target` 之后优先读：
   - `codex_log/current_gray_test_target.md`
   - `review_loop/00_review_loop_readme.md`
   - `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
   - `review_loop/02_video_record_template.md`
   - `review_loop/03_result_dashboard_template.md`
   - `review_loop/04_diagnosis_template.md`
   - `review_loop/05_dual_review_handoff_template.md`
   - `review_loop/06_next_round_task_template.md`
   - `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
   - `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
   - `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
   - `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
   - `project_source/14_content_review_and_loop_governance_rules.md`
11. 若任务命中“文案修改 / 下一条视频 / 根据数据改 / 播放低 / 收藏低 / 客资弱 / 复盘后重写 / 数据飞轮 / 目标驱动 / 数据目标 / 单主变量 / 内容结构反馈 / 视频执行 / 剪辑 / 编排 / DeepSeek 供料 / GPT Project 静态包同步”，在 `state_action_router` 后优先读：
   - `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
   - `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
   - `review_loop/` 当前视频复盘记录
   - 当前 `video_goal_card（视频目标卡）`
   - 当前 `post_publish_review_card（发布后复盘卡）`
   - 当前 `data_flywheel_memory（数据飞轮记忆）`
   - 当前 `content_structure_feedback_card（内容结构反馈卡）`
12. `codex_source/01_execution_rules.md`
13. `codex_source/02_current_execution_context.md`
14. `codex_source/03_research_findings_bridge.md`
15. 当前任务直接相关的 `project_source/*`
16. 命中价值 / 文案 / 结尾卡时，读 `codex_source/11_ai_knowledge_video_value_bridge.md`
17. 命中“什么算已知”时，读 `codex_source/12_codex_known_state_three_layer_rules.md`
18. 命中“完整成片 / 成品候选片 / 技术预览升级成候选片 / 样片回炉 / 开头重做 / 中段剪辑 / 字幕修正 / TTS 修正 / 功能卡修正 / 结果差卡修正 / 骚萌卡修正 / 录屏放大修正 / 视觉母版修正”时，读：
   - `codex_source/14_locked_reference_inheritance_rules.md`
   - `codex_source/locked_reference_registry.md`
19. 命中 v3.1 / 卡片视觉路由 / 段落提示卡 / 信息卡 / 骚萌卡三路拆分时，再读：
   - `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
20. 命中 commit / push / reading branch 回流时，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`

当前仓库现实 `已确认`：

- 仓库本地 `skills/` 目录不存在
- 相关 skills 需回退检查全局 `~/.codex/skills`

## 2A. 执行前 route_decision 闸门

每次任务必须先输出 `route_decision（路由判断）`，再执行默认读取顺序。

`route_decision（路由判断）` 是执行许可，不是可选说明。

如果没有 `route_decision（路由判断）`，或 `route_decision（路由判断）` 中任一关键字段缺失，Codex 必须停止，不得执行。

`route_decision（路由判断）` 至少包含：

1. `project_route（项目路由）`
2. `task_type（任务类型）`
3. `responsibility_layer（责任层级）`
4. `large_task_gate（大任务闸门）`
5. `must_read_files（本轮必读文件）`
6. `read_status（读取状态）`
7. `allowed_changes（允许修改范围）`
8. `forbidden_changes（禁止修改范围）`
9. `blocked_if（阻断条件）`
10. `execution_permission（执行许可）`
11. `deepseek_supply_gate（DeepSeek 供料闸门）`
12. `data_goal_anchor_gate（数据目标锚点闸门，命中视频执行 / 剪辑 / 编排 / DeepSeek 供料时必填）`

执行前输出格式必须为：

```text
route_decision:
  project_route:
  task_type:
  responsibility_layer:
  large_task_gate:
    triggered:
    reason:
    lane_recommendation:
    lane_reason:
    lane_invalid_if:
    parallel_recommendation:
    parallel_reason:
    parallel_invalid_if:
    write_owner:
    read_only_lanes:
    integration_owner:
  must_read_files:
    - path:
      reason:
      read_status:
  allowed_changes:
  forbidden_changes:
  blocked_if:
  execution_permission:
  data_goal_anchor_gate:
    required:
    data_goal_anchor_exists:
    next_video_execution_prompt_exists:
    data_goal_alignment_check_required:
    codex_may_adapt:
    codex_must_not_adapt:
```

若任何关键文件 `missing（文件不存在）` 或 `unreadable（无法读取）`，必须输出 blocked，不得继续执行。

不得用聊天记忆、GPT Project 静态资料、旧 PR 印象或 Codex 自己的推测补齐当前事实。

最终回报必须包含：

1. 本轮 `route_decision（路由判断）`
2. 实际读取文件清单
3. 哪些文件 `read_ok（已读取）`
4. 哪些文件 `missing（文件不存在）` / `unreadable（无法读取）` / `not_applicable（本轮不适用）`
5. 本轮允许修改范围
6. 本轮禁止修改范围
7. 是否触发 blocked
8. 命中视频执行 / 剪辑 / 编排 / DeepSeek 供料时，必须回报 `data_goal_anchor_gate（数据目标锚点闸门）`

每次最终回报必须新增栏目：

1. `route_decision（本轮路由判断）`
2. `read_status（实际读取状态）`
3. `execution_permission（执行许可是否成立）`
4. `data_goal_anchor_used（使用的数据目标锚点，命中视频执行 / 剪辑 / 编排时必填）`
5. `execution_structure_adjustments（执行结构调整）`
6. `why_adjustments_do_not_break_primary_variable（为什么调整不破坏主变量）`
7. `forbidden_variables_avoided（已避开的禁止变量）`
8. `post_publish_validation_metric（发布后验证指标）`

不得只回报“已完成”。

## 2A-1. Project State Action Router Gate 项目状态动作总控闸门

`Project State Action Router Gate（项目状态动作总控闸门）` 必须放在 `route_decision（路由判断）` 之后、具体执行之前。

它不替代 `route_decision（路由判断）`，而是补充回答：

**当前状态是什么 -> 应触发什么机制 -> 下一步动作是什么 -> 做到哪里算完成 -> 结果如何更新下一轮判断。**

命中以下任一任务时，必须读取：

1. `codex_source/19_project_state_action_router.md`
2. `GPT数据源/11_项目状态动作总控器_机制推理层.md`

触发场景包括：

- 复杂任务
- 机制修补 / 路由修补
- 文案执行
- 视频执行
- 发布复盘 / 数据回填
- GPT Project 静态包同步
- Codex 执行结果回审
- reference / 样片 / 参考效果落地
- 用户反馈“不对 / 怪 / 不顺”
- 发现旧口径残留、事实源冲突、灰度数据缺失、供料不足

执行前必须输出：

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

硬规则：

1. 如果 `state_action_router（项目状态动作总控器）` 没输出，Codex 不得进入具体执行。
2. 如果事实源冲突未裁决，Codex 不得写入机制或状态。
3. 如果 `blocked_if（阻断条件）` 命中，Codex 必须停止并输出 blocked。
4. 如果本轮改变下一轮默认判断，必须更新 `codex_log/latest.md`、dated log 或相关机制入口。
5. `state_action_router` 先判断该做什么；`Completion Relay Gate（补全接力闸门）` 再保证做到底。两者缺一不可。
6. 如果 `Completion Relay Gate（补全接力闸门）` 没输出，Codex 不得写 `completed`。

## 2A-1A. Data Goal Anchor Gate 数据目标锚点闸门

命中文案修改、下一条视频、视频执行、剪辑、编排、装配、DeepSeek 供料或 GPT Project 静态包同步时，Codex 必须先检查：

```text
data_goal_anchor_gate:
  data_goal_anchor_exists:
  next_video_execution_prompt_exists:
  data_goal_alignment_check_required:
  required_fields:
    - current_stage_goal
    - main_bottleneck
    - primary_variable
    - forbidden_variables
    - success_metric
    - failure_metric
    - post_publish_validation_metric
  codex_may_adapt:
    - segment_split
    - editing_rhythm
    - visual_order
    - card_position
    - api_image_needed_or_not
    - ppt_density
    - tts_segmentation
    - assembly_sequence
    - fallback_plan
  codex_must_not_adapt:
    - current_stage_goal
    - main_bottleneck
    - primary_variable
    - forbidden_variables
    - success_metric
    - failure_metric
    - post_publish_validation_metric
    - user_or_chatgpt_locked_data_goal_judgment
```

阻断规则：

- `data_goal_anchor_exists = false` 时，不得进入视频执行、剪辑、编排或装配。
- `next_video_execution_prompt_exists = false` 时，不得进入视频执行。
- `data_goal_alignment_check_required = true` 但执行后缺失时，不得写执行完成。
- Codex 只能调整执行结构，不能改写目标、主短板、主变量、禁止变量和验证指标。
- 数据目标不能替代素材证据；素材无法证明的内容仍必须删改、补录、降级或 blocked。
- 数据目标不能替代人感质量验收；不得据此推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。

## 2A-2. Reference-to-Execution Contract Gate 参考到执行落地契约闸门

`Reference-to-Execution Contract Gate（参考到执行落地契约闸门）` 必须放在 `Project State Action Router Gate（项目状态动作总控闸门）` 之后、具体执行之前。

命中以下任一信号时，必须触发本闸门：

- 用户给 `reference（参考）`。
- 用户给样片、参考图、参考视频、参考声音、原感稿或外部资料。
- 用户说“按这个做”“像这个效果”“不要偏离 reference”。
- 任务涉及 `locked reference（锁定参考）`、`visual route（视觉路由）`、`quality sample（质量样片）`、文案风格、剪辑效果、声音感觉、视觉外壳、卡片结构、节奏和人感。

执行前必须输出：

```text
reference_to_execution_contract:
  reference_anchor:
  effect_targets:
  function_fields:
  execution_mapping:
  deviation_check:
  done_when:
  blocked_if:
```

判断规则：

```text
if task_contains_reference = true:
  require reference_to_execution_contract

if reference_missing = true:
  blocked unless user explicitly allows no-reference mode

if effect_targets_missing = true:
  do not execute, ask ChatGPT/user to fill

if function_fields_missing = true:
  do not execute, create contract first

if deviation_check_missing = true:
  do not claim completed
```

硬规则：

1. 没有 `reference_to_execution_contract（参考到执行契约）`，不得执行带 reference 的任务。
2. 只写“参考某图 / 参考某视频 / 参考某样片”不算契约。
3. 只写“风格类似”不算 `effect_targets（效果目标）`。
4. 如果 reference 缺失，不能说“已按参考执行”。
5. 如果执行结果与 reference 关键效果偏离，不能写 `completed（已完成）`。
6. DeepSeek / Perplexity 摘要只能辅助供料，不得替代原 reference contract。
7. 本闸门不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）`。

## 2B. 任务类型与必读文件映射

### 项目文件修改 / 机制修补 / 路由修补

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_log/latest.md（最新摘要）`
5. 本轮点名要修改的文件

缺任一关键文件：blocked。

### 视频样片 / 成片 / 样片回炉

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_log/latest.md（最新摘要）`
5. `codex_log/current_publish_target.md（当前复审 / 发布目标）`
6. `codex_log/current_publish_target_light_evidence.md（当前复审轻证据）`
7. `dist/latest_review_pack/summary.json（状态摘要）`
8. `dist/latest_review_pack/review_manifest.md（复审入口）`
9. `codex_source/14_locked_reference_inheritance_rules.md（锁定参考继承规则）`
10. `codex_source/locked_reference_registry.md（锁定参考登记表）`
11. 如涉及 v3.1 / 卡片 / 视觉路由，再读 `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md（v3.1 视觉路由规则）`
12. 如涉及本地路径，再读 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`

缺 locked reference 或 visual route 关键文件：blocked。

### 文案写作 / 改写

必读：

1. `AGENTS.md（仓库入口规则）`
2. `GPT数据源/04_选题与文案规则.md（选题与文案规则）`
3. `GPT数据源/05_文案路由规则.md（文案路由规则）`
4. `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`
5. 本轮用户给出的文案 / reference / 素材说明

若缺少用途、对象、目标动作、风格边界、长度边界或验收标准：不得直接出正式稿，必须 blocked 或输出待确认位。

### 复盘 / 诊断 / 审核

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_log/latest.md（最新摘要）`
3. 当前复盘对象对应的报告 / 产物 / 日志
4. 若是发布后复盘，再读 `review_loop/` 对应文件
5. 若是视频内容复审，再读当前 `summary.json（状态摘要）` 与 `review_manifest.md（复审入口）`

缺复盘对象或当前结果状态：blocked。

### 数据记录 / 灰度复盘

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_log/current_gray_test_target.md（当前灰度测试目标）`
3. `review_loop/00_review_loop_readme.md（复盘循环入口）`
4. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md（截图数据录入规则）`
5. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md（v3.1 灰度测试指标体系）`
6. 当前视频记录目录

缺 `video_id`、时间窗或数据类型：blocked。

### 本地文件治理 / 工作区治理

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_log/latest.md（最新摘要）`
5. `.gitignore（Git 忽略规则）`
6. 与本轮治理对象相关的报告或路径索引

需要新建外部工作区、删除原始素材、替换正式工作区或执行 Git 高风险操作时：blocked，等待用户明确确认。
`已确认` 用户已单独授权的 `/Users/fan/Documents/视频工厂归档+删除` 只作为 archive-only 外部目录例外存在；不得把它当执行工作区或默认读取入口。

### execution lane / multi-agent / parallel 机制

必读：

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（多执行器路由说明）`
5. `codex_source/13_execution_lane_and_parallel_rules.md（执行 lane 与并行规则）`

默认单 Codex 执行器。

只有任务天然拆成互不抢文件、输入输出清楚、验收独立的 lane，才允许建议 multi-agent。

未明确 lane 边界时，不得开启 multi-agent。

## 2C. large_task_gate 大任务闸门

`large_task_gate（大任务闸门）` 是每次 `route_decision（路由判断）` 必须判断的字段。

执行前输出格式必须补充：

```text
large_task_gate:
  triggered:
  reason:
  lane_recommendation:
  lane_reason:
  lane_invalid_if:
  parallel_recommendation:
  parallel_reason:
  parallel_invalid_if:
  write_owner:
  read_only_lanes:
  integration_owner:
```

当任务命中以下任一条件时，`large_task_gate.triggered = true`：

1. 视频 / 样片 / 成片 / 剪辑对象超过 `180 秒`。
2. 本轮同时涉及脚本、素材、reference、时间线、TTS、字幕、验证、日志中的三项或以上。
3. 本轮需要写入或检查 3 个以上仓库文件。
4. 本轮同时涉及规则文件、执行文件、日志文件、报告文件中的两类或以上。
5. 本轮需要大量只读审计、定位、结构化整理，再统一写入。
6. 本轮任务包含“写文件 + 检查 + 日志 + push / 同步”等多步骤闭环。
7. 用户明确提到“长视频”“大任务”“多文件”“多步骤”“多 agent”“并发”“提速”“检查很多文件”。

触发后必须读取：

1. `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）`
2. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（给 GPT Project 用的多执行器路由说明）`

触发后必须输出 lane / parallel 判断：

- `lane_recommendation`
- `lane_reason`
- `lane_invalid_if`
- `parallel_recommendation`
- `parallel_reason`
- `parallel_invalid_if`

默认原则：

- 大任务必须判断是否并发。
- 判断并发不等于自动并发。
- 多文件 / 多检查 / 多步骤任务也必须判断。
- 写入范围不清楚时，默认 `serial_only（串行执行）`。
- 只读工作可拆时，优先考虑 `read_parallel（只读并发）` 或 `explore_plus_integrate（探索 + 单点整合）`。
- 多个写手只有在写入范围完全独立、验收独立、合并成本清楚时，才允许 `true_multi_task_parallel（真正多任务并发）`。

## 2D. DeepSeek + 三卡机制执行闸门

DeepSeek 供料闸门从 `if_needed_trigger（按需触发）` 升级为 `mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）`。

每轮 Codex 任务在 `route_decision（路由判断）` 后、文件写入或执行前，必须输出 `deepseek_supply_gate（DeepSeek 供料闸门）`。Codex 不得凭主观判断跳过 DeepSeek；如果无法真实调用 DeepSeek，必须写明 blocked 或 `fallback_local_only（本地兜底）`，不得冒充 DeepSeek 结论。

三张机制卡仍按适用场景判断，不等于所有任务都生成三张卡。DeepSeek 供料本身默认每轮都必须进入。

凡任务命中以下任一类型，Codex 必须额外判断三张机制卡是否必需：

- 视频样片
- 成片
- 内容表达文案
- 视频机制修改
- 发布前检查
- 发布后复盘
- `reference（参考）` / `visual route（视觉路由）` / `locked reference（锁定参考）`
- 大任务 / 多文件任务

`deepseek_supply_gate（DeepSeek 供料闸门）` 必须补充以下字段：

1. `supply_request_created（是否创建供料请求任务卡）`
2. `deepseek_call_required（是否要求 DeepSeek 真实供料）`
3. `deepseek_call_attempted（是否真实尝试调用）`
4. `deepseek_actual_participation（DeepSeek 实际参与状态）`
5. `supply_source（供料来源）`
6. `fallback_status（fallback 状态）`
7. `not_deepseek_conclusion（是否明确不是 DeepSeek 结论）`
8. `token_usage_expected（是否预期 token 减少）`
9. `token_usage_observed_or_user_check_required（token 是否已观察或需用户检查）`
10. `supply_request_path（供料请求路径）`
11. `supply_pack_read（是否读取供料包）`
12. `original_files_reviewed（是否复核原文件）`
13. `after_read_gap_triggered（是否触发二次补读）`

三卡适用性字段：

1. `content_route_card_required（是否需要内容路由卡）`
2. `quality_lock_card_required（是否需要质量锁卡）`
3. `review_variable_card_required（是否需要复盘变量卡）`

三张机制卡的触发规则：

| 场景 | 必须生成 |
| --- | --- |
| 内容表达文案、文案结构调整、素材承载判断 | `content_route_card（内容路由卡）` |
| 视频样片、成片、质量复审、reference 继承、visual route 继承 | `quality_lock_card（质量锁卡）` |
| 发布前变量确认、发布后复盘、下一轮只改一个变量 | `review_variable_card（复盘变量卡）` |
| 同时命中文案 + 成片 + 复盘链路 | 三张卡都必须判断，按适用范围生成 |

硬规则：

- 命中三卡场景但未生成相应卡片，不得进入执行。
- 每轮未生成 `supply_request（供料请求任务卡）`，不得写完整执行。
- Codex 跳过 DeepSeek 但无 blocked 原因，视为执行失败。
- 如果用户要求 DeepSeek 深度参与，但 `deepseek_actual_participation != deepseek_passed`，不得写 `completed（完成）` 或 DeepSeek 深度参与完成。
- 供料包为 `fallback_local_only（本地兜底）` 时，不得写 `deepseek_passed`，必须写 `not_deepseek_conclusion = true`。
- token 未观察到减少时，不得写 DeepSeek 已深度参与；必须写 `token_usage_observed_or_user_check_required = user_check_required`。
- Codex 必须读取供料包，再复核原文件；供料包不能替代原文件证据。
- 当任务卡禁止 `.env / secret（真实环境变量 / 密钥）` 时，Codex / controller 不得读取 `.env` 补救；只有显式开启 `--allow-process-env-api-key` 或 `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1` 时，才允许使用 process environment 中已存在的 `DEEPSEEK_API_KEY` 做 HTTP Authorization。
- 安全 process env key 调用必须同时保证 `env_file_read = false`、`api_key_printed = false`、`api_key_written = false`；若 process environment 没有 key，必须写 `deepseek_actual_participation = blocked_missing_process_env_api_key`，不得写成 DeepSeek passed。
- 三张卡是判断机制，不是固定 SOP。不得把它们写成所有视频都沿用同一镜头流程、同一卡片数量、同一人物段次数。
- `content_route_card（内容路由卡）` 解释流程为什么可变。
- `quality_lock_card（质量锁卡）` 锁质量底线，不证明内容通过。
- `review_variable_card（复盘变量卡）` 锁单变量反馈，不替代最终判断。
- 若执行中发现已读文件不足以判断，必须触发 `after_read_gap（读完仍有缺口）` 供料或补读；若补读仍无法排除 forbidden 修改风险，必须 blocked。

### 2D-1. deepseek_readiness_check（DeepSeek 就绪检查）

凡任务需要 DeepSeek 供料、触发 `execution_supply_pack family（执行供料包族）`、涉及 `reference（参考）` / `visual route（视觉路由）` / 多文件机制判断，Codex 必须先输出 `deepseek_readiness_check（DeepSeek 就绪检查）`。

最小字段：

```text
deepseek_readiness_check:
  env_file_read:
  process_env_key_allowed:
  process_env_key_present:
  safe_call_mode:
  request_validation_status:
  supply_request_created:
  supply_source:
  fallback_status:
  not_deepseek_conclusion:
  context_pack_validation:
  deepseek_actual_participation:
  blocked_reason:
  token_usage_expectation_check:
  deepseek_participation_report:
```

完成规则：

- 只有 `supply_source = deepseek_passed` 且 `context_pack_validation = passed` 时，才能写 DeepSeek 真实参与。
- `supply_source = fallback_local_only（本地兜底）` 时，必须写 `not_deepseek_conclusion = true`，不得写成 DeepSeek 结论、稳定供料或 `multi-agent runtime（多 agent 运行时）` 已跑通。
- process environment 中没有 `DEEPSEEK_API_KEY` 时，必须写 `deepseek_actual_participation = blocked_missing_process_env_api_key`，并把 `blocked_reason` 或说明写成 `missing_process_env_api_key`。
- 如果出现权限不足、key 无效、网络 / timeout、输出不合格，必须分别写成 `blocked_invalid_api_key`、`blocked_network_or_timeout`、`blocked_invalid_context_pack` 等可复核状态，不得伪装成 fallback 成功。
- 如果 request 或任务卡禁止 `.env / secret（真实环境变量 / 密钥）`，Codex / controller 不得读取 `.env` 补救。
- 最终回报必须包含 `deepseek_participation_report（DeepSeek 参与报告）` 和 `token_usage_expectation_check（token 使用预期检查）`。
- 后续日志、供料包和最终回报必须保留 `deepseek_readiness_check`，供下一轮先读。

## 2E. Auto-completion gate 自动补全闸门

`Auto-completion gate（自动补全闸门）` 用来阻断 Codex 只完成用户点名动作、却漏掉上游判断、供料、三卡、风险复核、日志回流或事实同步的情况。

它不是让 Codex 自行扩写业务目标；它只允许 Codex 在已确认边界内补齐完成本轮任务必须存在的机制链。

凡任务命中以下任一情况，必须触发自动补全闸门：

- 机制修补
- 路由修补
- 项目文件修改
- DeepSeek / 多 AI 协作
- 视频样片 / 成片
- 文案生产
- 发布复盘
- `reference（参考）` / `locked reference（锁定参考）` / `visual route（视觉路由）`
- 多文件任务
- 用户要求“完整流程 / 深度配合 / 自动补全 / 不要只做点名任务”

触发后，Codex 执行前必须自动检查 9 个层级：

1. `goal_layer（目标层）`：本轮目标是否只是显性动作，还是包含必须补齐的机制链。
2. `judgment_layer（判断层）`：是否需要先判断项目状态、内容边界、reference 继承或风险归属。
3. `route_layer（路由层）`：是否已完成 `route_decision（路由判断）`、lane / parallel 判断和责任层级划分。
4. `trigger_layer（触发层）`：是否触发 DeepSeek 供料、三卡机制、发布前风险检查、review_loop 或路径索引。
5. `supply_layer（供料层）`：是否需要 `supply_request（供料请求任务卡）`、供料包读取、执行中补读或执行后风险复核。
6. `execution_layer（执行层）`：是否只允许 Codex 单点写入，是否已有允许修改范围和禁止修改范围。
7. `feedback_layer（反馈层）`：执行结果是否需要进入 `review_loop/`、供料包、risk_report 或下一轮变量说明。
8. `validation_layer（验收层）`：是否有能证明本轮技术 / 机制变更成立的验证命令与输出。
9. `sync_layer（同步层）`：是否需要同步 `codex_log/latest.md`、dated log、当前事实、执行规则、schema 或入口文件。

后续触发本闸门的任务必须输出以下字段：

```text
auto_completion_gate:
  triggered:
  reason:
  explicit_user_task:
  implicit_mechanism_chain:
    goal_layer:
    judgment_layer:
    route_layer:
    trigger_layer:
    supply_layer:
    execution_layer:
    feedback_layer:
    validation_layer:
    sync_layer:
  missing_links:
  must_complete_now:
  blocked_if_not_completed:
  auto_completion_plan:
  auto_completion_result:
```

完成判断硬规则：

- 只完成用户点名任务，不等于完成。
- 若隐性机制链有缺口，必须补齐或 `blocked（阻断）`。
- 若需要 DeepSeek 供料而未触发，不能写完整完成。
- 若需要三张机制卡而未生成，不能进入执行。
- 若供料包生成但 Codex 没读，不能写完整完成。
- 若读供料包但没复核原文件，不能写完整完成。
- 若执行后没有风险复核，不能写完整完成。
- 若没更新日志，不能写完整完成。
- 若本轮只能完成显性任务、无法补齐上游或下游机制，必须把状态写成 `部分成立` 或 `blocked`，不得写成 `已确认完成`。

### 2E-1. 文案进入执行后的执行供料包族闸门

当最终文案、内容路由卡或用户明确执行单进入 Codex 执行层时，Codex 不得直接跳到“生成视频 / 生成图片 / 装配时间线”。

必须先通过 `Auto-completion gate（自动补全闸门）` 判断是否需要以下 `execution_supply_pack family（执行供料包族）`：

```text
data_goal_anchor（数据目标锚点）
content_route_card（内容路由卡）
-> visual_asset_requirement_pack（视觉素材需求包）
-> api_asset_generation_pack（API 素材生成包）
-> image_prompt_pack（图片 prompt 包）
-> asset_validation_pack（素材验收包）
-> assembly_decision_pack（装配决策包）
-> editing_decision_pack（剪辑决策包）
-> data_goal_alignment_check（数据目标对齐检查）
-> review_pack / 审片包回流
```

触发条件：

- Codex 收到最终文案并准备执行。
- 需要生成视频、卡片、图片、背景、角色或图标。
- 需要判断是否调用阿里 API / 豆包 / 其他图片 API。
- 需要写图片 prompt 或素材验收标准。
- 需要把真实录屏、API 图、PPT 卡片、人物段、TTS、字幕装配到时间线。
- 需要判断某个素材会不会抢走真实证据位。

硬规则：

- 最终文案进入视频执行前，必须先确认 `data_goal_anchor（数据目标锚点）`。
- 最终文案进入视频执行前，必须先运行 `script_anchor_extraction_function（文案锚点提取函数）`。
- 缺 `data_goal_anchor_used（使用的数据目标锚点）`，不得生成 `content_route_card V2（内容路由卡 V2）`、`assembly_decision_pack（装配决策包）` 或 `editing_decision_pack（剪辑决策包）`。
- 缺 `script_to_timeline_map（文案到时间线映射表）`，不得进入视频执行、时间线装配或成片生成。
- 缺 `tts_prosody_anchor_map（TTS 韵律锚点表）`，不得生成 TTS；不得只按标点机械切句。
- 高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头生成前，必须先有 `opening_visual_hook_spec（开头视觉钩子规格）`；静态两行标题页不得默认通过高情绪开头验收。
- 只有 `material_01 / material_02 / material_03` 段落级素材分配时，必须写 `paragraph_level_mapping_insufficient（段落级映射不足）` 并阻断视频执行。
- 没有先判断 `visual_asset_requirement_pack（视觉素材需求包）`，不得直接列图片生成清单。
- 没有先判断 `api_asset_generation_pack（API 素材生成包）`，不得调用真实 API。
- 真实 API 调用必须由用户本轮明确授权；默认机制测试不得调用阿里 API。
- Codex 不得读取 `.env`、API key、token 或密钥文件来完成供料包测试。
- API 生成图只能做辅助表达、视觉壳、信息卡、氛围、角色或图标，不能冒充真实录屏证据。
- `image_prompt_pack（图片 prompt 包）` 默认不让图片模型生成中文可读文字；需要文字时由后期卡片层处理。
- `asset_validation_pack（素材验收包）` 未通过时，素材不得进入装配；必须 revise / reject / pending_human_review / 降级。
- `assembly_decision_pack（装配决策包）` 必须区分主证据与辅助素材；中段真实录屏主体不得被 API 图抢走。
- `assembly_decision_pack（装配决策包）` 必须包含 `segment_goal / metric_supported / variable_preserved / forbidden_variable_avoided / post_publish_validation_metric`。
- 需要具体剪辑动作时，必须回到 `editing_decision_pack（剪辑决策包）`。
- `editing_decision_pack（剪辑决策包）` 必须包含 `line_group_goal / primary_variable_support / evidence_role_for_metric / forbidden_visuals_by_goal / edit_action_reason_against_data_goal / post_publish_validation_metric`。
- 执行完成前必须输出 `data_goal_alignment_check（数据目标对齐检查）`。
- `forbidden_variables_avoided / forbidden_visuals_by_goal / forbidden_variable_avoided` 是同一组 `data_goal_anchor.forbidden_variables（数据目标锚点禁止变量）` 在不同对象里的映射；无法回指同一上游禁止变量时，必须 blocked。
- dist 供料输出若不提交 GitHub，必须另写可追溯 `codex_log/*evidence*.md`，不得只说本地文件存在。

### 2E-1A. 三大机制推理函数前置闸门

凡任务命中剪辑判断、内容承载判断或质量复审判断，Codex 必须先输出对应推理函数，再进入卡片、决策包、视频执行或完成态判断。

统一输出结构：

```text
input_signal（输入信号）
-> observed_evidence（现场证据）
-> state_inference（状态判断）
-> action_policy（动作策略）
-> validation_rule（验证规则）
-> blocked_if（阻断条件）
-> feedback_update（反馈回写）
```

#### script_anchor_extraction_function（文案锚点提取函数）

触发条件：

- 最终文案、`content_route_card V2（内容路由卡 V2）` 或用户明确执行单准备进入视频执行。
- 需要生成 TTS、字幕、卡片、时间线、剪辑决策包或审片包。
- 现有映射只有 `material_01 / material_02 / material_03` 段落级用途。
- 用户反馈 TTS 某些字突然上扬、停顿不自然、分句断裂或重音机器感。
- 用户反馈文案和画面局部错位，关键句配错画面。

执行要求：

- 必须先输出 `script_anchor_extraction_function（文案锚点提取函数）`，再进入视频执行。
- 必须输出 `script_function_map / evidence_anchor_map / visual_anchor_map / tts_prosody_anchor_map / card_anchor_map / forbidden_visual_map / script_to_timeline_map` 或等效完整字段。
- 每 1-2 句必须有 `line_group_id（句组编号）`，并绑定素材、时间码、画面职责、字幕职责、卡片职责、禁用画面和验证规则。
- `evidence_sentence（证据句）` 必须能追溯素材或标记为 `user_experience_statement / no_direct_evidence（用户经验陈述 / 无直接画面证据）`。
- `boundary_statement（边界声明）` 不得配误导性证明画面。

执行前阻断条件：

```text
video_execution_preflight_blockers:
  missing_data_goal_anchor:
    blocked_video_execution: true

  missing_data_goal_anchor_used:
    blocked_video_execution: true

  missing_script_anchor_extraction_function:
    blocked: true

  missing_script_to_timeline_map:
    blocked_video_execution: true

  missing_tts_prosody_anchor_map:
    blocked_tts_generation: true

  missing_opening_visual_hook_spec_when_high_emotion_hook:
    blocked_opening_generation: true

  paragraph_level_mapping_only:
    blocked_video_execution: true

copy_revision_preflight_blockers:
  missing_threshold_config_v1:
    blocked_data_driven_judgment: true

  missing_video_goal_card:
    blocked_formal_copy_revision: true

  missing_post_publish_review_card_when_claiming_data_driven:
    blocked_data_driven_copy_revision: true

  missing_main_bottleneck:
    blocked_copy_revision: true

  missing_primary_variable:
    blocked_copy_revision: true

  too_many_variables_without_major_revision:
    blocked_execution: true

  missing_next_video_execution_prompt:
    blocked_video_execution: true

  missing_data_goal_alignment_check_before_completion:
    blocked_completion: true

  missing_content_structure_feedback_card_when_using_data_to_change_structure:
    blocked_structure_revision: true
```

目标驱动数据飞轮执行前置：

- 命中文案修改、下一条视频、根据数据改、播放低 / 收藏低 / 客资弱、复盘后重写、数据飞轮、目标驱动、数据目标、单主变量、内容结构反馈、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步时，必须读取 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` 与 `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`。
- 没有 `threshold_config_v1（阈值配置 V1）`，不得做数据驱动判断。
- 没有 `video_goal_card（视频目标卡）`，不得进入正式文案修改。
- 没有 `post_publish_review_card（发布后复盘卡）`，不得声称“根据数据修改文案”。
- 没有 `main_bottleneck（主短板）`，不得重写正式文案。
- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。
- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，不得进入视频执行。
- 没有 `data_goal_anchor（数据目标锚点）`，不得进入视频执行、剪辑、编排或装配。
- 没有 `data_goal_alignment_check（数据目标对齐检查）`，不得写视频执行完成。
- 超过 3 个变量且未标 `major_revision（大改版）`，不得进入执行。
- 超过 4 个变量，不得写成数据实验，只能写成方向重做观察。

#### editing_inference_function（剪辑推理函数）

触发条件：

- 任务涉及中段剪辑、录屏放大、裁切、定格、插卡、左右对比、证据窗口、`editing_decision_pack（剪辑决策包）`。
- 任务涉及总结卡、反转卡、结果差卡、Prompt 尾卡的插入位置，或需要判断卡片是否会打断真实证据窗口。
- 用户反馈看不清、不顺、硬拼接、上下文断裂。
- reference / visual route / locked reference 要求保留证据窗口或剪辑节奏。
- 最终文案准备装配，但缺 `script_to_timeline_map（文案到时间线映射表）` 或只有段落级素材分配。

执行要求：

- 必须先输出 `editing_inference_function`，再生成 `editing_decision_pack（剪辑决策包）`。
- `editing_decision_pack` 必须写明每个动作对应的 `state_inference`、`action_policy`、`validation_rule` 和 `blocked_if`。
- `editing_decision_pack` 必须写明 `data_goal_anchor_used（使用的数据目标锚点）`、`primary_variable_support（服务的主变量）`、`forbidden_visuals_by_goal（按目标禁用的画面）` 和 `edit_action_reason_against_data_goal（相对数据目标的剪辑动作理由）`。
- 如果素材不可读、时间码不清、证据点不可见、放大会切断必要上下文，必须 blocked 或 keep_full_frame；不得凭感觉剪。
- 当素材被标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）` 时，Codex 不得默认二次放大，不得默认裁切重构视角，不得把“自动放大”当成中段剪辑完成标准。
- FocuSee 自带运镜素材的默认执行动作是：按最终文案识别时间码、切分段落、删除等待 / 重复 / 空白 / 失败操作、衔接口播 / 字幕 / 卡片，并保留原始 `3D Motion（3D 运镜）` 节奏。
- 若 FocuSee 运镜后的关键证据仍看不清，必须写 `blocked_or_needs_rerecording（阻断或需补录）`，不得用猜测继续剪；只有关键证据未覆盖、关键文字不可读、结果差未展示清楚或用户明确要求二次增强时，才允许判断辅助放大 / 定格 / 卡片。
- 如果卡片会打断真实证据窗口，必须跳过、改位置或 blocked，不得为了固定旧 shot 强插。
- 卡片插入只能服务明确 `copy_function（文案功能）`，不得让总结卡 / 反转卡替代真实录屏证据。
- 剪辑动作不能只看 `material_01 / material_02 / material_03` 段落级用途，必须看 `line_id / line_group_id（句子编号 / 句组编号）`。
- 每 1-2 句必须知道当前句子在证明什么、必须出现什么画面、不能出现什么画面、是否需要卡片辅助、是否是反转点 / 证据点 / 总结点。
- 如果只有段落级映射，不允许进入视频装配；如果文案句子与素材证据冲突，必须 blocked 或回到 ChatGPT 复审，不得硬剪。
- 如果剪辑动作会改变主验证变量、引入禁止变量或削弱发布后验证指标，必须 blocked。

#### content_route_inference_function（内容路由推理函数）

触发条件：

- 任务涉及内容表达文案进入执行、`content_route_card（内容路由卡）`、主体承载、API 生成人物 1 次 / 2 次、PPT / 信息卡 / Prompt 引用尾卡、是否沉淀工作包。
- 任务涉及内容执行、视频执行、文案进入执行或 `content_route_card V2（内容路由卡 V2）` 输出。
- 任务涉及开头生成、开头重做、`opening_route_decision（开头路由判断）`、元素娃娃开头、梗图 GIF 开场、直接问题标题卡、录屏现场先行开头或开头 reference。
- 任务涉及 `card_placement_decision（卡片位置判断）`、总结卡、反转卡、结果差卡、Prompt 尾卡或卡片位置路由。
- 任务涉及 `script_anchor_map / tts_prosody_anchor_map / opening_visual_hook_spec / script_to_timeline_map / forbidden_visual_map` 的执行前补全。

执行要求：

- 必须先输出 `content_route_inference_function`，再生成 `content_route_card（内容路由卡）`。
- `content_route_card` 必须引用本函数的判断，解释为什么这条内容这样承载。
- 涉及内容执行 / 视频执行 / 文案进入执行时，必须先生成 `content_route_card V2（内容路由卡 V2）` 或等效完整字段，不得只输出零散字段。
- `content_route_card V2（内容路由卡 V2）` 必须包含 `data_goal_anchor_used（使用的数据目标锚点）`、`main_bottleneck_supported（服务的主短板）`、`primary_variable_supported（服务的主变量）`、`forbidden_variables_avoided（避开的禁止变量）` 和 `post_publish_validation_metric（发布后验证指标）`。
- 涉及开头时，必须先输出 `opening_route_decision（开头路由判断）` 或等效字段；缺开头路线判断，不得直接生成视频或生成开头。
- 涉及高情绪 / 抖音抓眼 / 梗图 GIF / 抽象动效开头时，必须先输出 `opening_visual_hook_spec（开头视觉钩子规格）`；缺规格不得生成开头。
- 涉及总结卡、反转卡、结果差卡或 Prompt 尾卡时，必须先输出 `card_placement_decision（卡片位置判断）` 或等效字段；缺卡片位置判断，不得直接生成视频。
- 缺 `validation_goal（验证目标）`、`opening_route_decision（开头路由判断）`、`core_evidence（核心证据）`、`middle_carrier_decision（中段承载判断）`、`card_placement_decision（卡片位置判断）` 或 `flow_flex_reason（流程变化原因）`，不得进入视频执行。
- 缺 `data_goal_anchor_used（使用的数据目标锚点）`，不得进入视频执行。
- 缺 `script_to_timeline_map（文案到时间线映射表）`，不得进入视频执行。
- 缺 `tts_prosody_anchor_map（TTS 韵律锚点表）`，不得生成 TTS。
- 只有段落级素材分配，必须阻断为 `paragraph_level_mapping_insufficient（段落级映射不足）`。
- 若素材来自 FocuSee，必须额外填写 `focusee_middle_editing_decision（FocuSee 中段剪辑判断）`；缺该判断不得进入中段剪辑。
- 如果选择 `meme_gif_opening_hook（梗图 GIF 开场钩子）`，必须保留 `Reference-to-Execution Contract（参考到执行落地契约）`、`effect_targets（效果目标）` 和 `must_not_copy（禁止复刻）` 边界。
- 如果选择 `element_doll_opening（元素娃娃开头）`，必须说明本条内容为什么需要品牌一致性 / 轻陪伴进入。
- 不得把开头路线选择写成 `content_validation（内容验证）` 通过或 `visual_master_locked（视觉母版锁定）`。
- 不得把元素娃娃或梗图 GIF 写成所有内容唯一默认开头。
- 不得把总结卡 / 反转卡固定为旧 shot 或旧 reference 位置。
- 如果文案没有明确反转点，不得强行插反转卡。
- 如果文案没有明确结论 / 下一步，不得强行插总结卡。
- 不得把卡片位置选择写成 `content_validation（内容验证）` 通过或 `visual_master_locked（视觉母版锁定）`。

#### quality_issue_classifier（质量短板分类器）

触发条件：

- 用户反馈“不对 / 怪 / 不顺 / demo 感”。
- 技术通过但内容、人感、声音、剪辑、证据、画面、卡片密度、主持壳职责或 reference 偏离不舒服。
- 任务涉及 `quality_lock_card（质量锁卡）` 或质量复审。
- 用户反馈某些字突然上扬、停顿不自然、分句断裂或重音机器感。
- 用户反馈开头两行静态字、不抓人或不符合抖音审美。
- 用户反馈文案和画面局部错位、关键句配错画面。

执行要求：

- 必须先输出 `quality_issue_classifier`，再决定改文案、改剪辑、做声音复审、做 reference deviation check 或 blocked。
- 必须定位唯一最高优先级短板；不能同时改多个核心变量后再解释结果。
- 必须区分 `technical_validation（技术验证）` 和 `content_validation（内容验证）`。
- `voice_prosody_issue（声音韵律问题）` 优先动作是生成 `tts_prosody_anchor_map（TTS 韵律锚点表）`、重写分句和韵律，不默认换音色。
- `opening_visual_hook_issue（开头视觉钩子问题）` 优先动作是生成 `opening_visual_hook_spec（开头视觉钩子规格）`，并阻断静态标题页通过高情绪开头验收。
- `script_visual_mismatch_issue（文案画面错位问题）` 优先动作是生成 `script_to_timeline_map（文案到时间线映射表）`，并在句子级映射缺失前阻断视频执行。
- 缺复审对象、用户反馈对象、灰度数据或需要用户听感 / 审美判断时，必须 blocked 或 human_review_required。

完成判断硬规则：

1. 命中任一函数触发条件但未输出对应函数，不得写 `completed（已完成）`。
2. 三个函数或 `script_anchor_extraction_function（文案锚点提取函数）` 任一 required 字段缺失，不得写 `completed（已完成）`。
3. 只写卡片名、动作名或问题列表，不算推理函数落地。
4. 若本轮是机制修补，fixture / 最小样例必须覆盖相关函数的正常判断与 blocked 判断。

### 2E-2. Completion Relay Gate（补全接力闸门）

`Completion Relay Gate（补全接力闸门）` 用来连接：

- `ChatGPT 横向补全`
- `Codex 纵向细化`
- `执行后剩余工作反查`
- `日志 / 当前事实 / 入口规则同步`

它解决的问题是：

- Codex 只完成用户点名动作。
- Codex 完成一个局部文件就提前收工。
- Codex 没把 ChatGPT 的横向补全拆成任务树。
- Codex 没有执行后反查剩余工作。
- Codex 把 `部分完成` 写成 `已完成`。

凡出现以下任一情况，必须触发本闸门：

- ChatGPT prompt 中包含多个执行层，如 `Goal` / `Context` / `Constraints` / `Impact check` / `Must read` / `Execution steps` / `Done when` / `Blocked if` / `Output`。
- 用户明确要求“自动补全 / 补全机制 / 不要只做一半 / 深度细化 / 执行到底”。
- 任务类型为机制修补、路由修补、项目文件修改、多文件同步、视频执行、文案执行、复盘执行、DeepSeek / 多 AI 协作。
- 本轮存在 `must_complete_now（本轮必须完成项）`。
- 本轮存在多个受影响文件或多个交付物。
- 本轮会影响新聊天默认接手事实。

触发后，Codex 必须在执行前输出并维护以下字段：

```text
completion_relay_gate:
  triggered:
  reason:
  chatgpt_horizontal_context_loaded:
  completion_map:
    user_goal:
    explicit_task:
    implicit_required_work:
    affected_layers:
    required_outputs:
    forbidden_outputs:
  required_output_inventory:
    - item:
      required:
      target_path:
      done_status:
      validation:
      blocker:
  child_task_graph:
    - id:
      task:
      depends_on:
      target_files:
      validation:
      done_status:
  continuation_rule:
    continue_unless_blocked:
    stop_only_if:
  remaining_work_check:
    unchecked_items:
    incomplete_items:
    blocked_items:
    unnecessary_items:
  sync_back_check:
    latest_updated:
    dated_log_created:
    current_facts_updated_if_needed:
    entry_files_updated_if_needed:
  final_completion_status:
```

硬规则：

1. 完成一个文件 ≠ 完成本轮任务。
2. 完成显性用户点名动作 ≠ 完成隐性机制链。
3. 通过测试 ≠ 完成日志回流。
4. 写入规则 ≠ 长期机制稳定。
5. 没有 `child_task_graph（子任务树）`，不得执行。
6. 没有 `required_output_inventory（必须交付清单）`，不得写完成。
7. 没有 `remaining_work_check（剩余工作检查）`，不得写完成。
8. 只要 `required_output_inventory（必须交付清单）` 中有未完成项，最终状态只能是 `partial_completed（部分完成）` 或 `blocked（阻断）`，不得写 `completed（已完成）`。
9. 除非触发 `blocked_if（阻断条件）`，否则 Codex 不得停在建议、计划、审计或局部修改。
10. 如果执行中发现新的必要同步文件，必须加入 `required_output_inventory（必须交付清单）` 并继续处理。
11. 如果不能继续处理，必须明确写阻断原因、未完成项、为什么不能继续、需要用户确认什么。

完成状态定义：

```text
completed（已完成）:
  所有 required_output_inventory 必填项完成
  所有验证通过
  latest 已更新
  dated log 已创建
  没有禁止状态偷换
  没有剩余 must-fix 项

partial_completed（部分完成）:
  部分 required_output_inventory 完成
  但仍有未完成项或待验证项
  不得写成 completed

blocked（阻断）:
  缺关键文件
  缺权限
  允许 / 禁止范围不清
  会触发高风险状态修改
  需要用户确认
```

## 3. skill 检查硬规则

执行前必须：

1. 先检查当前仓库本地 `skills/`
2. 若无，再检查全局 `~/.codex/skills`
3. 命中相关 skill 时必须使用
4. 若未找到或不适用，必须如实说明

当前这类“项目口径 / 接手口径 / 文档维护”任务，至少要优先检查：

- `using-superpowers`
- `context-driven-development`
- `verification-before-completion`

当前这类“execution lane / parallel mechanism”任务，额外必须检查：

- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`

## 4. 哪些情况必须先审计

出现以下任一情况，必须先审计再改：

1. 用户明确要求先看仓库现实
2. 任务目标是“同步源事实 / 修复接手口径 / 改默认主线”
3. 任务涉及 `project_source` 与 `codex_source` 的交叉修改
4. 任务涉及主读取分支 `main`
5. 当前仓库文件与聊天里的说法可能不一致

## 5. 默认允许修改范围

只有在用户明确授权时，才允许修改：

- 当前任务点名的 `project_source/*`
- 当前任务点名的 `codex_source/*`
- `codex_log/*`

没有明确授权时，默认不改：

- 代码文件
- 测试文件
- 配置 / 密钥文件
- `dist/*`
- 不在本轮范围内的文档

## 6. GPT 数据源不会自动同步到 Codex 仓库

这是执行层硬规则：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 外部资料、Perplexity 结论、ChatGPT 收束结果，若会影响执行，必须先回写仓库或显式带入执行单

未回写前，它们最多只能算：

- `GPT 已知`
- 或 `Codex 条件已知`

不能直接写成：

- `Codex 正式已知`

## 6A. 本地审片路径读取规则

凡涉及本地审片路径、视频路径、音频路径、图片路径、复审包路径，必须先查：

- `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`

硬规则：

- 没有被 Codex 本地验证过的路径，不得当作用户可打开路径输出。
- 只有 `current_local_artifact_paths.md（当前本地产物路径索引）` 中 `path_exists = true（路径存在）` 的路径，才能作为用户可打开路径输出。
- `summary.json（状态摘要）` 和 `review_manifest.md（审片入口）` 中的路径只能作为线索，不能直接当成真实可打开路径。
- 如果本地路径索引不存在、超过 24 小时未验证，或相关记录没有 `path_exists = true（路径存在）`，必须写成“路径待本地复核”。
- `/private/tmp（系统临时目录）` 路径默认不稳定，除非本轮重新验证存在，否则不得作为首选路径。
- 旧脏 worktree（旧脏工作区）路径不得作为默认执行路径；如确实存在，只能作为历史 / 备选打开路径并明确标注。

## 6B. 单工作区硬规则 single_workspace_rule

《视频工厂》本地执行只能围绕唯一正式工作区：

- `/Users/fan/Documents/视频工厂`

硬规则：

1. Codex 后续不得默认新建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*` 或 `/Users/fan/Documents/视频工厂-worktrees` 作为外部散工作区。
2. 如果需要新分支，必须在 `/Users/fan/Documents/视频工厂` 内执行 `git switch -c <branch>` 或切换既有分支。
3. 不得默认使用 `git worktree add` 创建外部 Git 工作区；除非用户当轮明确授权。
4. 不得默认新建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区。
5. 如果 Codex 判断确实需要 fresh clone / 外部对照 / 外部 worktree / 任何外部目录，必须先停止，回报 `reason（原因）`、`target_path（目标路径）`、`risk（风险）`、`internal_alternative（唯一正式工作区内替代方案）`，等待用户本轮明确确认后才能继续。
6. 所有最终产物、样片、复审包、截图归档、治理报告、路径索引、执行日志和清理记录，都必须落在唯一正式工作区内部。
7. `/Users/fan/Desktop`、`/Users/fan/Downloads`、`/private/tmp`、`/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*` 不得作为最终交付路径。
8. 必须临时读取外部路径时，只能作为 `source（来源）` 只读读取；必须回收到唯一正式工作区后，才能写入路径索引或默认执行口径。
9. 已经产生的外部工作区必须收回到唯一正式工作区内部的 `本地归档_local_archive/` 或 `本地隔离区_local_quarantine/`；不得继续散落在 `/Users/fan/Documents` 顶层。
10. `codex_log/current_local_artifact_paths.md` 的 `canonical_local_path（首选本地路径）` 只能指向唯一正式工作区内部。
11. 旧外部路径最多只能作为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）`，不得作为默认执行路径。
12. 后续清理、归档、迁移任务也必须从唯一正式工作区发起、记录、提交和推送。

## 7. 仓库型任务默认线路

命中以下任一条件，默认按仓库型任务处理：

- 改仓库文件
- 修项目口径 / 执行口径 / 路由口径 / 接手口径
- 需要 commit / push / 回流主读取分支

默认线路：

先审计现状 -> 改文件 -> 更新日志 -> 验证 -> commit -> push 当前分支 -> 同步回 `main`

## 8. 执行日志硬规则

只要本轮出现以下任一事实，就必须写 `codex_log/`：

- 改了仓库文件
- 跑了命令
- 完成了 commit / push / 同步
- 形成了新的阻塞点 / 交接点

至少要做两件事：

1. 刷新 `codex_log/latest.md`
2. 新增一条 `codex_log/YYYYMMDD_任务名.md`

若本轮结果会改变以下任一项，还必须同步刷新：

- `codex_log/current_publish_target.md`
  - 当前待发对象
  - 当前审核对象
  - 当前正式状态
  - 当前唯一最高优先级 blocker
  - 现在最该改的唯一一点
  - `lane_recommendation`
  - `lane_reason`
  - `lane_invalid_if`
  - `parallel_recommendation`
  - `parallel_reason`
  - `parallel_invalid_if`
- 若当前样片的 Git 可追踪轻量证据有变化，再同步刷新：
  - `codex_log/current_publish_target_light_evidence.md`

## 8A. 视频修改必须同步口径规则

以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。

默认必须同步检查：
1. `codex_log/latest.md`
2. `codex_log/current_publish_target.md`
3. `codex_log/current_publish_target_light_evidence.md`
4. `GPT数据源/08_当前正式事实.md`
5. `dist/latest_review_pack/summary.json`
6. `dist/latest_review_pack/review_manifest.md`
7. 如改变入口 / 分支 / 读取顺序，还必须同步 `AGENTS.md` 和 `codex_source/00_codex_readme.md`

硬规则：
- 不允许只改视频、不改口径
- 不允许只在工作分支改口径、不同步默认主读取分支
- 不允许把历史样片写成当前最新样片
- 不允许把 `technical_validation` 写成 `content_validation`
- 不允许用户未最终确认前把当前片子写成可发送状态
- 不允许旧 `round` 状态继续覆盖最新 `latest_review_pack`
- 只要改动会影响新会话默认接手判断，就必须同步到 `main`

## 8A-1. 发布后灰度测试与复盘接入规则

当前 v3.1 已进入 `post_publish_gray_test（发布后灰度测试阶段）`。

状态硬规则：

- `publish_status = gray_test_published（已发片，进入灰度测试）`
- `gray_test_status = active（灰度测试中）`
- `post_publish_review_required = true（需要发布后复盘）`
- `content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`

执行硬规则：

1. 发布后复盘默认接入 `review_loop/`，不新建独立灰度系统。
2. 单条记录走 `review_loop/02_video_record_template.md`。
3. 结果看板走 `review_loop/03_result_dashboard_template.md`。
4. 诊断初检走 `review_loop/04_diagnosis_template.md`。
5. Codex 初检 / ChatGPT 判断交接走 `review_loop/05_dual_review_handoff_template.md`。
6. 下一轮只改一个变量走 `review_loop/06_next_round_task_template.md`。
7. 灰度测试指标体系 V1 走 `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`。
8. 24h / 72h 数据窗口、一次只改一个变量、小样本状态升级 / 降级、异常样本处理、规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`。
9. 7 天播放量 6000 是当前小样本阶段基础测试流量门槛，不是最终商业目标。
10. 指标体系不是运营数据大表，而是下一轮改动定位器。
11. 后续复盘默认收成四个问题：
   - 这条有没有达到 6000 播放基础门槛？
   - 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
   - 下一轮只改哪一个变量？
   - 为什么先改它，改完看哪个指标？

截图数据录入硬规则：

1. 截图录入前必须先确认 `video_id`；未确认视频归属时不得入表。
2. 截图录入前必须先确认时间窗：`24h / 72h / 7d`；未确认时间窗时不得入表。
3. 截图录入前必须先确认数据类型：`platform_metrics / audience_retention / interaction / account_growth / comments / dm / consult / other`。
4. 不同视频、不同时间窗、不同数据类型不得混写。
5. `24h` 数据不得被 `72h` 或 `7d` 覆盖；`72h` 数据不得被 `7d` 覆盖。
6. 截图字段识别不清必须标记 `uncertain_need_human_check`。
7. 截图没有提供的字段必须标记 `missing`，不得硬猜。
8. 评论截图不得当成私信截图；私信数不得自动等于有效咨询数。
9. Codex 只做截图归档、字段提取、缺失标记、初检和交接，不做最终内容判断。

Codex 职责边界：

- Codex 可以记录、初检、归档、标缺失、生成下轮草稿。
- Codex 不得把灰度测试写成内容通过。
- Codex 不得把已发片写成最终成功。
- Codex 不得跳过 24h / 72h / 7 天数据直接设定下一条文案。
- Codex 不得把所有字段都升级成硬必填；字段必须分为核心必填、辅助观察、商业线索出现时才填。
- 最终问题层、是否继续、下一轮唯一改点由 ChatGPT / 用户拍板。

## 8B. 仓库清理与旧口径归档规则

命中“仓库清理 / 旧口径归档 / 未提交文件处理 / 执行噪音删除”时，必须先输出 `cleanup_audit（清理审计）`，再动手。

清理审计必须分为：

1. `safe_delete（可安全删除）`：确认无引用、无证据价值、可重新生成或明显临时的文件。
2. `archive_only（只归档不删除）`：旧判断、旧入口、旧 PR 报告、仍有复盘价值但不应作为默认入口的文件。
3. `rewrite_needed（需要改清楚）`：仍会被 Codex 默认读取、且可能误导当前状态的入口 / 状态 / registry / summary。
4. `keep_as_evidence（作为证据保留）`：素材、复审包、registry 引用证据、summary / manifest / timeline / cut_map 引用产物。
5. `blocked_unknown（不确定，先不动）`：无法判断是否可删的未追踪文件或目录。

未提交 / 未追踪文件处理规则：

- 不允许直接运行全仓清理命令。
- 不允许不分类就删除 `untracked` 文件。
- 不允许删除 `素材录制/`、`素材库_assets/`、当前 v3 / v3.1 可能用到的复审包、PR #7 B、可爱卡片参考图、registry 已引用 artifact / evidence。
- 只删除 `safe_delete`，且必须在 dated log 中列出相对路径和原因。
- `blocked_unknown` 一律不删，只记录后续专项清理建议。

旧口径归档规则：

- PR #22 / PR #23 / 旧 round 报告中的历史判断不得原样覆盖用户最新确认。
- 可将旧判断摘录或副本放入 `归档_archive/旧口径_old_context_YYYYMMDD/`。
- 归档目录必须有 README，说明默认不再读取哪些旧口径。
- 归档内容只作复盘证据，不作为当前事实、不作为后续执行参考。

## 8C. locked reference 继承硬规则

以后凡任务命中以下任一类型，必须先读 locked reference 机制：

- 完整成片
- 成品候选片
- 技术预览升级成候选片
- 样片回炉
- 开头重做
- 中段剪辑
- 字幕修正
- TTS 修正
- 功能卡修正
- 结果差卡修正
- 骚萌卡修正
- 录屏放大修正
- 视觉母版修正

强制读取：

1. `codex_source/14_locked_reference_inheritance_rules.md`
2. `codex_source/locked_reference_registry.md`

硬规则：

- 任一文件读不到，必须 `blocked`，不得直接生成完整片。
- `candidate_reference` 只能写成候选参考，不得写成 `locked_reference`。
- `failed_reference` 只能作为反例或复盘材料，不得默认继承。
- 用户 / ChatGPT 未明确确认前，不得把 PR 自评 pass 写成用户已确认。
- 完整成片 / 成品候选片 / 样片回炉完成时，必须输出 `locked_reference_inheritance_report.md`。
- summary 必须写 `locked_reference_registry_read`、`locked_reference_inheritance_validation`、`locked_reference_inheritance_report`、`unapproved_reference_changes`、`reference_deviation_blockers`、`candidate_references_used`、`locked_references_used`。

## 8D. v3.1 视觉路由前置硬规则

当前状态：

- `已确认` v3.1 已成为《我用 AI 做 PPT 踩过的坑》当前视频基线。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1，不再基于 v3 或 round34。
- `已确认` v3 只保留为历史候选 / 对照，不作为后续默认修改基础。
- `已确认` v3.1 已有 `dist/latest_review_pack/visual_route_map.json（视觉路由表）` 和 `dist/latest_review_pack/visual_route_validation_report.json（视觉路由验证报告）`；后续修改必须先复核并保持三条视觉路由不混。

后续任何 v3.1 生成 / 样片回炉 / 卡片视觉修正任务，若涉及段落提示卡、信息卡、骚萌卡，必须先读：

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

硬规则：

- 生成或修改 v3.1 全片前必须先读取 / 输出并验证 `visual_route_map.json（视觉路由表）`。
- `cute_prompt_card_route（可爱段落提示卡路由）` 只给反面 / 正面展示提示卡。
- `cute_info_card_route（可爱信息卡路由）` 只给结果差、归因转折、Prompt 架构、Prompt 尾卡等信息卡。
- `sassy_reaction_card_route（骚萌反应卡路由）` 只给三张骚萌反应卡。
- v3 技术状态只能写成当前阶段里程碑达成，必须保持 `technical_line_locked = false（技术线未锁定）`。
- PR #7 B 是后续骚萌卡唯一执行参考。
- PR #7 A 只能作为历史 / candidate 对照，不能作为任何后续骚萌卡执行参考。
- 读不到 `PR7_B_骚萌反应页.png` 必须 `blocked`，不得回退 PR #7 A。
- 任意骚萌卡走信息卡路由、任意信息卡走骚萌路由、任意段落提示卡走复杂信息卡路由且未重审，必须 `blocked`。

旧 PR 降噪规则：

- PR #22：v3 历史候选，不再直接合并，不再作为后续默认基础。
- PR #23：历史样本包，PR #7 A 优先判断已被 PR #7 B 覆盖，不再直接合并。
- PR #24：v3.1 有效产物已回流到最新主读取分支，PR #24 本身不得再直接合并，避免回退 PR #25 清理口径。

以下情况必须 `blocked`：

- 找不到已锁定 reference。
- 没有读取 locked reference registry。
- 继承失败或只写“类似”但没有对照证据。
- 字幕、TTS、放大、卡片、剪辑语法与 locked reference 不一致。
- 用户没有授权但 Codex 自行换风格、重做或替换。
- 完整片使用 candidate reference 却写成 locked reference。
- 只有 technical_validation / content_validation，没有 reference inheritance validation。

## 9. 主读取分支与状态分类

当前仓库默认主读取分支固定为：

- `main`

状态分类必须显式标记为：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

硬规则：

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“仓库正式状态已同步”
- 只有同步回 `main`，才算主读取分支正式已知

## 10. 这类任务的最小验证

这类文档 / 规则 / 接手口径修复任务，完成前至少要做：

1. `git diff --check`
2. 重新读取关键目标文件，确认口径一致
3. 重新读取 `codex_log/current_publish_target.md`，确认只靠稳定入口就能知道当前对象、状态、blocker 与下一步
4. 若本轮补了轻量证据包，再读取 `codex_log/current_publish_target_light_evidence.md`
5. 若本轮补的是 lane / parallel 机制，再读取：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
6. 若声称已同步回主读取分支，使用 `git show origin/main:路径` 做实际读取验证

## 11. 完成口径硬规则

不得把以下两件事写成同一件事：

- 仓库口径已同步
- 新主线样片已验证成立

本轮如果只完成了文档 / 规则 / 桥接 / latest / reading branch 回流，只能写：

- 仓库口径已同步

不能写：

- 样片验证通过
- 新主线已被质量验证成立

## 12. 收尾时必须回报的 4 个同步锚点

每轮仓库型任务收尾时，必须明确回报：

1. 当前工作分支
2. 最新提交 SHA
3. 是否已 push
4. 是否已同步回 `main`
