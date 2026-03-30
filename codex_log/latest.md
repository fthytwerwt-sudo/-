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
- 当前执行层已正式补入“执行闸门 / 自动补全边界 / 多 Codex 并行”规则，不再只靠聊天说明。

## 最近一次完成了什么

- 已完成一次正式排雷检查，确认当前执行对象仍是正确的视频项目 Git 仓库，关键目录和最小闭环产物都还在。
- 已新增 `codex_source/06_execution_gate_and_parallel_rules.md`，把顶层收口闸门、自动补全边界和多 Codex 并行规则正式落到执行层。
- 已增量修改：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
- 已补写完整执行日志：`codex_log/20260330_execution_gate_and_parallel_rules.md`。

## 当前最关键的下一步

- 后续凡遇到“现在能不能下发 Codex 执行”“哪些能自动补全”“是否适合多工位并行”这三类问题，优先按 `codex_source/06_execution_gate_and_parallel_rules.md` 判断。
- 若后续还要继续优化协作表达，可再结合 `project_source/07_user_readable_repo_map.md` 使用；当前仓库尚不存在 `project_source/07_collaboration_adaptation_rules.md`。
- 若后续进入新的仓库型任务小闭环，仍按“先更新日志，再 commit / push 当前分支，供 ChatGPT 复审”推进。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- 若任务偏项目定位，补读 `project_source/00_project_brief.md` 和 `project_source/01_project_system_prompt.md`
- 若任务偏用户定位与协作表达，补读 `project_source/07_user_readable_repo_map.md`
- 若任务偏执行流程判断，补读 `codex_source/01_execution_rules.user_guide.md`、`codex_source/01_execution_rules.md`
- 若任务命中协作方式、自动补全边界、下发闸门或并行执行判断，再补读 `codex_source/06_execution_gate_and_parallel_rules.md`
- 若未来新增 `project_source/07_collaboration_adaptation_rules.md`，再把它加入这一组协作判断入口
- 若需要核对原执行硬规则，再补读 `codex_source/01_execution_rules.md`
