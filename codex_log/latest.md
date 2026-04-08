# Latest

## 当前主结论

- `已确认` 当前任务分支里：
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/21_topic_selection_and_copywriting_rules.md`
  - `project_source/22_copy_mode_routing_rules.md`
  - `project_source/25_ai_knowledge_video_value_rules.md`
  已经补齐。
- `已确认` codex 侧桥接也已补齐：
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_source/12_codex_known_state_three_layer_rules.md`
- `已确认` 这些规则现在已经升到“当前分支正式已知”。
- `待确认`
  - 是否已升到“主读取分支正式已知”，要看这轮是否成功同步回 `codex/user-readable-map`
- `已确认`
  - 不能把这轮写成“样片质量已经被验证成立”

## 当前新增桥接口径

- `AI 项目讲解`
  - 默认交付：判断项目卡点、关键取舍和最小下一步
  - 默认结尾：`judgment_card + 最小行动`
- `AI 方法分享`
  - 默认交付：可直接试的方法 + 易错点
  - 默认结尾：`steps_error_card`
- `AI 学习实操`
  - 默认交付：最小步骤 + 自检
  - 默认结尾：`steps_card + 自检句`
- `AI 案例拆解`
  - 默认交付：案例为什么成立 + 如何迁移
  - 默认结尾：`judgment_card + 可迁移句`

## 当前样片执行前新增要求

- `已确认` 后续 Codex 在以下任务里必须先锁清：
  - 当前内容类型
  - 用户看完后能做什么
  - 用户看完后能判断什么
  - 最关键证据是什么
  - 最小行动 / 自检句是什么
  - 对应结尾总结卡类型是什么
- `已确认` 未锁清前：
  - 不得把文案直接压进样片执行
  - 不得把 generation / assembly 成功写成内容过线

## 当前已知状态三层

- `GPT 已知`
  - 只存在于聊天、外部研究、GPT Project 替换包、还没进当前仓库正文的内容
- `Codex 条件已知`
  - 已进入 bridge / codex_source / latest，但还没进 project_source 正文或还没进主读取分支
- `当前分支正式已知`
  - 已进入当前任务分支的 `project_source` 正文与 codex 读取口径
- `主读取分支正式已知`
  - 在“当前分支正式已知”基础上，再同步回 `codex/user-readable-map`

## 当前接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_source/02_current_execution_context.md`
5. `codex_source/03_research_findings_bridge.md`
6. `codex_source/11_ai_knowledge_video_value_bridge.md`
7. `codex_source/12_codex_known_state_three_layer_rules.md`
8. 若继续做样片，再补读：
   - `project_source/08_quality_baseline_and_90_score_rules.md`
   - `project_source/21_topic_selection_and_copywriting_rules.md`
   - `project_source/22_copy_mode_routing_rules.md`
   - `project_source/25_ai_knowledge_video_value_rules.md`
   - `project_source/02_scene_mode_templates.md`
   - `project_source/16_presentation_routing_rules.md`
   - `project_source/24_human_self_footage_light_ppt_routing_rules.md`

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
  - `dist/*` 样片产物和本地配置均为 `local_only`
