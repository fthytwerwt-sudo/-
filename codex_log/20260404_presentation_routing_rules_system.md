# 2026-04-04 展示路由分层判断系统落库

## 本轮目标

- 把《视频工厂》的“展示路由规则”正式写成仓库内的分层判断系统，而不是固定模板。
- 让项目以后可以根据文案 / prompt / 场景 / 目标，判断哪些 block 更适合：
  - `ppt`
  - `human`
  - `screen_demo`
  - `case_visual`
  - `mixed`

## 执行前已确认事实

- 当前默认主读取分支固定为：
  - `codex/user-readable-map`
- 当前项目正式阶段已从技术阶段进入内容阶段，正往试发阶段过渡。
- 当前必须写死：
  - 路由单位是 `block`
  - 先判断，再路由
  - 写死职责和比例，不写死固定秒数
- 当前工作分支在本轮开始前已经存在未提交文档改动：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/02_scene_mode_templates.md`
- `project_source/04_review_templates.md`
- `project_source/05_psychology_execution_rules.md`
- `project_source/06_project_index.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/13_stage_and_acceptance_gates.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 全局 skill：
  - `verification-before-completion`
  - `context-driven-development`

本轮按点名清单核对后，以下目标文件当前仓库不存在：

- `project_source/09_review_loop_system_v1.md`
- `project_source/10_video_review_record_template.md`（本轮开始时缺失，已补建）
- `project_source/11_result_diagnosis_map.md`
- `project_source/12_review_role_split_and_workflow.md`
- `project_source/15_distribution_and_commercialization_rules.md`

## 实际改动

- 新增：
  - [project_source/16_presentation_routing_rules.md](/Users/fan/Documents/视频工厂/project_source/16_presentation_routing_rules.md)
  - [project_source/10_video_review_record_template.md](/Users/fan/Documents/视频工厂/project_source/10_video_review_record_template.md)
  - [codex_log/20260404_presentation_routing_rules_system.md](/Users/fan/Documents/视频工厂/codex_log/20260404_presentation_routing_rules_system.md)
- 修改：
  - [project_source/01_project_system_prompt.md](/Users/fan/Documents/视频工厂/project_source/01_project_system_prompt.md)
  - [project_source/02_scene_mode_templates.md](/Users/fan/Documents/视频工厂/project_source/02_scene_mode_templates.md)
  - [project_source/04_review_templates.md](/Users/fan/Documents/视频工厂/project_source/04_review_templates.md)
  - [project_source/06_project_index.md](/Users/fan/Documents/视频工厂/project_source/06_project_index.md)
  - [project_source/13_stage_and_acceptance_gates.md](/Users/fan/Documents/视频工厂/project_source/13_stage_and_acceptance_gates.md)
  - [project_source/14_content_review_and_loop_governance_rules.md](/Users/fan/Documents/视频工厂/project_source/14_content_review_and_loop_governance_rules.md)
  - [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)

## 新增 / 改写的展示路由系统规则

- 新增正式主规则文件：
  - `project_source/16_presentation_routing_rules.md`
- 把展示路由正式写成 4 层：
  - `L1`: `video_scene / video_goal / primary_value / audience_need_first / video_route_strategy`
  - `L2`: `block_id / block_goal / block_need_first / block_carrier / asset_requirement / why_this_carrier`
  - `L3`: fallback rules
  - `L4`: review / diagnosis
- 把判断顺序写死为：
  - 先判场景
  - 再判主价值
  - 再判观众优先需求
  - 再判 block 职责
  - 最后才判载体
- 把触发信号、资产闸门、失败回退、回审字段和阶段边界正式落仓
- 明确写死：
  - 15 秒只是当前示例，不是长期统一时长
  - 混合不等于固定顺序
  - 不能因为真人更“高级”或 PPT 更“稳”就直接默认

## 实际执行

- 读取并核对项目脑、执行层、日志与当前分支状态
- 确认本地无仓库级 `skills/` 目录，按执行层规则补读全局 skill
- 新建展示路由主规则文件和视频回审记录模板
- 用最小入口修改把 `16` 接入：
  - 项目系统 Prompt
  - 场景模板
  - 回审模板
  - 项目导航
  - 阶段闸门
  - 回审循环治理
  - `AGENTS.md`
- 校验命令：
  - `git diff --check -- AGENTS.md project_source/01_project_system_prompt.md project_source/02_scene_mode_templates.md project_source/04_review_templates.md project_source/06_project_index.md project_source/10_video_review_record_template.md project_source/13_stage_and_acceptance_gates.md project_source/14_content_review_and_loop_governance_rules.md project_source/16_presentation_routing_rules.md`
  - `rg -n "16_presentation_routing_rules|10_video_review_record_template|展示路由" AGENTS.md project_source/01_project_system_prompt.md project_source/02_scene_mode_templates.md project_source/04_review_templates.md project_source/06_project_index.md project_source/13_stage_and_acceptance_gates.md project_source/14_content_review_and_loop_governance_rules.md`

## 当前结果

- 当前仓库里已经存在正式的展示路由系统规则。
- 路由单位已明确写死为 `block`，不是整条视频固定模板。
- 当前正式口径已经包含：
  - 判断顺序
  - 输入字段
  - 触发信号
  - 资产闸门
  - 失败回退
  - 回审 / 复盘字段
  - 阶段边界

## 下一步建议

- 下一条最值得验证的样片，应优先做“展示路由判断样片”。
- 重点不是再出一条任意视频，而是验证：
  - prompt 能不能先判断结构主导 / 信任主导 / 混合承载
  - 路由系统能不能选对
