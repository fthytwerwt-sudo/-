# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，后续仓库型任务继续默认在功能分支推进，而不是直接改 `main`。
- 当前仓库已明确项目正式口径：
  - 个人内部使用
  - Prompt 驱动
  - Codex 可执行
  - 视频内核优先
  - 前端页面不是当前阶段重点
- 当前仓库仍保留“用户可讨论定位层”，用于帮助非技术用户判断问题落在哪一层，并更准确地向 ChatGPT 描述修改点。
- 当前工作分支 `codex/user-readable-map` 已同步到 `origin/codex/user-readable-map`。
- 原有三层分工保持不变：
  - `project_source/` 负责项目脑
  - `codex_source/` 负责执行层
  - `codex_log/` 负责执行日志

## 最近一次完成了什么

- 已把项目口径正式收束为“个人内部使用的、Prompt 驱动的、Codex 可执行的视频内核”，并明确当前不按前端页面 / 工作台优先推进。
- 已同步修改：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/06_project_index.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
- 已补写完整执行日志：`codex_log/20260329_prompt_driven_internal_positioning.md`。
- 本轮结果已 commit 并 push 到当前工作分支，供 ChatGPT 复审。

## 当前最关键的下一步

- 后续只要项目讨论还处于当前阶段，默认都应先沿“Prompt 驱动 + Codex 执行 + 出片链路 + 回审闭环”推进，而不是先扩成页面方案。
- 若后续要继续讨论协作表达，仍可先读 `project_source/07_user_readable_repo_map.md`。
- 若后续要核对执行层是否按当前项目口径推进，优先看 `codex_source/01_execution_rules.md` 和 `codex_source/01_execution_rules.user_guide.md`。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- 若任务偏项目定位，补读 `project_source/00_project_brief.md` 和 `project_source/01_project_system_prompt.md`
- 若任务偏用户定位与协作表达，补读 `project_source/07_user_readable_repo_map.md`
- 若任务偏执行流程判断，补读 `codex_source/01_execution_rules.user_guide.md`
- 若需要核对原执行硬规则，再补读 `codex_source/01_execution_rules.md`
