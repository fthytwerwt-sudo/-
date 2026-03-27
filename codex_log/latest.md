# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，同步到 `origin/main`。
- GitHub baseline 分支为 `main`，且 `main` 已跟踪 `origin/main`。
- 后续仓库型任务默认在新分支推进，而不是长期直接在 `main` 上执行。
- 顶层入口规则、GitHub 协作基线和执行日志机制都已在仓库内落位。

## 最近一次完成了什么

- 已固定新 Codex 会话默认最小接手集合：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`；若任务偏执行规则，再补读 `codex_source/01_execution_rules.md`。
- 已固定仓库型任务在形成可判断小闭环后，默认先更新 `codex_log/latest.md`、命中条件时补完整日志，再 commit 并 push 当前分支 / 当前 PR，供 ChatGPT 直接去 GitHub 复审。

## 当前最关键的下一步

- 后续仓库型任务继续在功能分支推进；每轮一旦形成可判断小闭环，就先更新 `codex_log/latest.md`，再按规则 commit、push 并交给 ChatGPT 复审。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- 若任务偏执行规则，再补读 `codex_source/01_execution_rules.md`
