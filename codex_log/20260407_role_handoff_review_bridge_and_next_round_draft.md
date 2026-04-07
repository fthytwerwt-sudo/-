# 20260407_role_handoff_review_bridge_and_next_round_draft

## 本轮目标

- 把“45 秒 role handoff 样片这轮回审收束结论”正式写入项目资料
- 把“已收束采用的 Perplexity 外部参考”正式桥接进 Codex 执行层
- 生成下一轮只围绕 `分步 reveal + 关键词显影节奏` 的修改单草稿
- 不改项目主线、不改代码、不改 case、不重写整条视频执行方案

## 当前工作分支

- `codex/round1-visual-pass-conservative`

## 执行前已确认事实

- 当前目录：
  - `/Users/fan/Documents/视频工厂`
- 本轮任务属于仓库型文档更新任务，允许修改范围已被用户限制为：
  - 新建 1 份 `project_source` 稳定判断层文件
  - 更新 `codex_source/03_research_findings_bridge.md`
  - 生成 1 份下一轮修改单草稿
- 当前仓库本地 `skills/`：
  - 不存在
- 本轮已检查并实际采用的全局 skill：
  - `context-driven-development`
  - `verification-before-completion`
- 本轮用户已明确给出正式输入，不允许 Codex 重判项目方向。
- 当前工作树存在与本轮无关的既有修改：
  - `project_source/03_perplexity_prompt_library.md`
  - 本轮未触碰该文件

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/04_review_templates.md`
- `project_source/05_psychology_execution_rules.md`
- `project_source/06_project_index.md`
- `project_source/10_video_review_record_template.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- `project_source/17_white_collar_ppt_style_rules.md`
- `/Users/fan/.codex/skills/context-driven-development/SKILL.md`
- `/Users/fan/.codex/skills/verification-before-completion/SKILL.md`

## 实际改动

- 新建：
  - `project_source/18_visual_motion_and_information_density_rules.md`
    - 把当前这轮 45 秒样片的视觉动效 / 信息密度判断，正式写成阶段性稳定判断层
    - 明确区分 `已确认` / `建议判断` / `外部参考`
- 更新：
  - `codex_source/03_research_findings_bridge.md`
    - 新增 `BRIDGE-20260407-01`
    - 新增 `BRIDGE-20260407-02`
    - 把本轮回审收束结论和“已收束采用的外部参考”正式桥接进执行层
- 新增：
  - `codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md`
    - 记录本轮真实读取、改动和下一轮修改单草稿
- 更新：
  - `codex_log/latest.md`
    - 刷新为当前最新的仓库交接摘要

## 实际执行

- 只对用户允许的文档落点做了手工更新
- 未修改：
  - 代码文件
  - case 文件
  - 其他无关 `project_source/*`
  - 其他无关 `codex_source/*`
- 本轮未生成新样片，也未对现有视频做重新导出

## 实际验证

- 已执行：
  - `git diff --check -- project_source/18_visual_motion_and_information_density_rules.md codex_source/03_research_findings_bridge.md codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md codex_log/latest.md`
  - `git diff -- project_source/18_visual_motion_and_information_density_rules.md codex_source/03_research_findings_bridge.md codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md codex_log/latest.md`
  - `git status --short --branch`
- 验证结果：
  - 目标文件 `git diff --check` 通过
  - 本轮 Git 跟踪改动只落在：
    - `codex_log/latest.md`
    - `codex_source/03_research_findings_bridge.md`
    - `project_source/18_visual_motion_and_information_density_rules.md`
    - `codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md`
  - 已再次确认存在与本轮无关的既有工作树改动：
    - `project_source/03_perplexity_prompt_library.md`
  - 本轮未触碰 `.gitignore` / `local_only` 产物目录

## 当前结果

- 已形成 1 份可复用的稳定判断层文件
- 已把本轮收束结论写入 Codex 执行桥接层
- 已生成 1 份只围绕 `分步 reveal + 关键词显影节奏` 的下一轮修改单草稿
- 已把状态显式区分为：
  - `已确认`
  - `建议判断`
  - `外部参考`
- 已避免把单轮外部资料写成长期已成立规律

## 下一轮修改单草稿

### 修改目标

- 只修 1 个最高优先级问题：
  - 把当前整页静态切换，改成“跟着旁白推进的分步 reveal + 关键词显影节奏”
- 目标不是把画面做得更花，而是让画面开始承担信息推进

### 允许改什么

- 每页信息出现顺序
- 关键词 / 结果句 / 数字的显影节奏
- 局部高亮 / 框选 / 单点放大
- 与旁白停顿点对应的 reveal 拍点
- 只为配合上述节奏而做的最小视觉强调

### 禁止改什么

- 不重写整条视频结构
- 不改 case
- 不把旁白全文搬上屏
- 不把 `bounce / 回弹` 替换当成这轮主目标
- 不同时新增多种花哨动效
- 不为了“更有看头”乱加无关素材
- 不改成营销广告式快节奏

### 验收标准

- 每页至少能看出“信息是跟着旁白逐步推进”的，而不是整页一次性给完
- 关键词、结果句或数字有明确的出场时点，不再与正文同权重同时铺开
- 观众能更清楚地感到“这一页在推进一个判断”，而不是只是在换页
- 画面增强没有引入新的模板感、课件感或炫技感
- 第二优先和第三优先问题仍保持克制，未喧宾夺主

### 做到哪算完成

- 当这条 45 秒样片的主要观感，从“画面不承担信息推进”变成“画面已经开始跟着旁白推进信息”时，算完成本轮修改目标
- 若只做了稳转场、字号统一，但 reveal 节奏仍未建立，不算完成

## 下一步建议

- 下一轮执行时，只允许围绕上述修改单草稿开工
- 若 reveal 节奏已成立，再单独开下一轮讨论：
  - 稳转场替换
  - 固定字号层级
- 当前仓库状态分类：
  - `task_branch_only`
