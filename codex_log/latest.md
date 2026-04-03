# Latest

## 当前展示路由系统状态

- 2026-04-04 本轮不是再做样片，而是把《视频工厂》的“展示路由规则”正式写成仓库内的分层判断系统。
- 当前结论：
  - `presentation_routing_rules_formalized`

## 当前主判断

- 展示路由单位正式写死为：
  - `block`
  - 即段落块 / 镜头块
- 展示路由正式写成 4 层：
  - `L1`: 整条视频层
  - `L2`: block 层
  - `L3`: 回退层
  - `L4`: 回审层
- 正式判断顺序已写死为：
  - 先判场景
  - 再判整条视频主价值
  - 再判观众最需要先接住什么
  - 再判 block 职责
  - 最后才判 block 用什么展示形式
- 当前已明确：
  - 15 秒样片只是当前示例，不是长期统一时长
  - 混合承载不是固定顺序
  - 当前阶段优先做“路由正确”，不是“真人优先主义”

## 本轮实际改动

- 新增主规则：
  - [project_source/16_presentation_routing_rules.md](/Users/fan/Documents/视频工厂/project_source/16_presentation_routing_rules.md)
- 新增回审记录模板：
  - [project_source/10_video_review_record_template.md](/Users/fan/Documents/视频工厂/project_source/10_video_review_record_template.md)
- 同步更新入口文件：
  - [project_source/01_project_system_prompt.md](/Users/fan/Documents/视频工厂/project_source/01_project_system_prompt.md)
  - [project_source/02_scene_mode_templates.md](/Users/fan/Documents/视频工厂/project_source/02_scene_mode_templates.md)
  - [project_source/04_review_templates.md](/Users/fan/Documents/视频工厂/project_source/04_review_templates.md)
  - [project_source/06_project_index.md](/Users/fan/Documents/视频工厂/project_source/06_project_index.md)
  - [project_source/13_stage_and_acceptance_gates.md](/Users/fan/Documents/视频工厂/project_source/13_stage_and_acceptance_gates.md)
  - [project_source/14_content_review_and_loop_governance_rules.md](/Users/fan/Documents/视频工厂/project_source/14_content_review_and_loop_governance_rules.md)
  - [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
- 新增 / 更新日志：
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
  - [codex_log/20260404_presentation_routing_rules_system.md](/Users/fan/Documents/视频工厂/codex_log/20260404_presentation_routing_rules_system.md)

## 当前缺失但已如实确认的目标文件

- 这轮按你点名清单核对后，当前仓库不存在以下目标文件名：
  - `project_source/09_review_loop_system_v1.md`
  - `project_source/11_result_diagnosis_map.md`
  - `project_source/12_review_role_split_and_workflow.md`
  - `project_source/15_distribution_and_commercialization_rules.md`
- `project_source/10_video_review_record_template.md` 在本轮开始时也不存在，现已补建为正式模板。

## 当前最关键下一步

- 下一条最值得验证的样片，不是“再出一条随便的视频”，而是：
  - 展示路由判断样片
- 优先验证 prompt 是否能先判断：
  - 这条是结构主导
  - 还是信任主导
  - 还是需要混合承载
