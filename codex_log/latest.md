# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，后续仓库型任务继续默认在功能分支推进，而不是直接改 `main`。
- 当前仓库新增了“用户可讨论定位层”，用于帮助非技术用户判断问题落在哪一层，并更准确地向 ChatGPT 描述修改点。
- 当前本地分支是 `codex/user-readable-map`，本轮文档改动已经本地 commit，但远端分支尚未确认建立。
- 原有三层分工保持不变：
  - `project_source/` 负责项目脑
  - `codex_source/` 负责执行层
  - `codex_log/` 负责执行日志

## 最近一次完成了什么

- 已新增 `project_source/07_user_readable_repo_map.md`，用中文人话说明仓库关键文件、常见表面现象、问题更像落在哪一层，以及用户该怎么向 ChatGPT 描述问题。
- 已新增 `codex_source/01_execution_rules.user_guide.md`，把原执行规则翻成用户可读说明，帮助理解读取顺序、分支 / PR 线路、日志规则、push 节奏与验证口径。
- 已补写完整执行日志：`codex_log/20260329_user_readable_repo_map.md`。

## 当前最关键的下一步

- 后续与 ChatGPT 讨论修改点时，先用 `project_source/07_user_readable_repo_map.md` 判断问题更像边界、结构、文案、节奏、画面、执行还是产物。
- 如果用户感觉“流程不对 / push 节奏不对 / 不知道该不该走 PR”，优先看 `codex_source/01_execution_rules.user_guide.md`，再决定是否进入原规则文件核对。
- 若要让 ChatGPT 直接从 GitHub 复审本轮结果，下一步先解决 `codex/user-readable-map` 的 push 验证，再确认远端分支是否已经出现。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- 若任务偏用户定位与协作表达，补读 `project_source/07_user_readable_repo_map.md`
- 若任务偏执行流程判断，补读 `codex_source/01_execution_rules.user_guide.md`
- 若需要核对原执行硬规则，再补读 `codex_source/01_execution_rules.md`
