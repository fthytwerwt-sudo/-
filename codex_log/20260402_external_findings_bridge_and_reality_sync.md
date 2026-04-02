# 2026-04-02 外部结论桥接与执行偏差回写机制补齐

## 本轮目标

- 在 `codex_source/` 里正式补齐两套机制：
  - 外部结论桥接
  - 执行偏差回写
- 让 Codex 以后能明确知道：
  - Perplexity / ChatGPT / 用户新拍板的结论如何进入执行层
  - 真实执行中的现实偏差如何回写并阻止旧方案继续被误当成立

## 执行前已确认事实

- 当前仓库路径是 `/Users/fan/Documents/视频工厂`。
- 当前目录是 Git 仓库，且 `origin` 已存在。
- 当前分支是 `codex/user-readable-map`。
- 开始前 working tree 不是干净状态，已有与本轮无关的未提交改动：
  - `formal_api_demo_core.py`
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
- 当前仓库无本地 `skills/` 目录。
- `project_source/07_chatgpt_project_instructions_backup.md` 当前不存在。
- `codex_source/02_current_execution_context.md`、`03_research_findings_bridge.md`、`04_completion_and_review_contract.md` 开始前都不存在。

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/04_review_templates.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/06_execution_gate_and_parallel_rules.md`
- `codex_source/02_codex_index.md`
- 全局 skill：
  - `using-superpowers`
  - `writing-plans`
  - `brainstorming`
  - `verification-before-completion`
  - `context-driven-development`
- 仓库与 Git 检查：
  - `ls -la`
  - `git status --short --branch`
  - `git branch --show-current`
  - `git remote -v`
  - 指定文件存在性检查
  - `git diff`
  - `rg`

## 实际改动

- 新建 `codex_source/02_current_execution_context.md`
  - 固定当前阶段、当前主目标、当前不做事项、当前主路径、demo 身份、质量判断核心、默认先读文件、可自动补全项与禁止擅自拍板项。
- 新建 `codex_source/03_research_findings_bridge.md`
  - 固定来源类型、状态定义、硬字段模板和录入规则。
  - 明确 Perplexity / ChatGPT / 用户新拍板不会自动同步到 Codex。
  - 补录本轮已采用的桥接结论。
- 新建 `codex_source/04_completion_and_review_contract.md`
  - 固定最终汇报栏目、状态定义和禁止事项。
- 新建 `codex_source/05_execution_deviation_and_reality_sync.md`
  - 固定执行偏差定义、偏差分级、原方案改标、默认动作与回写落点。
- 更新 `codex_source/01_execution_rules.md`
  - 更新默认读取顺序。
  - 新增研究结论桥接规则。
  - 新增执行偏差回写规则。
  - 把最终汇报栏目改为与完成契约一致。
- 更新 `codex_source/00_codex_readme.md`
  - 把新文件纳入执行层入口与文件清单。
  - 明确外部结论不会自动同步，现实偏差必须回写。
- 更新 `codex_log/latest.md`
  - 把这轮机制补齐结果写成最新交接摘要。
- 新建本日志 `codex_log/20260402_external_findings_bridge_and_reality_sync.md`
  - 记录本轮读取、改动、结果与下一步。

## 实际执行

- 先按任务要求读取执行层与项目脑正式文件，确认本轮不是靠猜测补规则。
- 真实检查文件存在性，确认：
  - `02 / 03 / 04` 三个目标文件确实不存在
  - `01_execution_rules.md` 里此前没有把“研究结论桥接”和“执行偏差回写”写成正式机制
- 在不改 `project_source/*` 和代码文件的前提下，只对 `codex_source/*` 与 `codex_log/*` 做增量补丁。
- 对照项目脑口径与执行层职责，避免把“项目身份 / 内容边界”误写成“Codex 操作说明”。

## 当前结果

- 当前执行层已真实补齐：
  - 执行前上下文
  - 研究结论桥接
  - 完成与回审契约
  - 执行偏差与现实同步
- `codex_source/01_execution_rules.md` 已同步补上桥接与偏差回写规则。
- `codex_source/00_codex_readme.md` 已同步补上新的入口与文件定位。
- 本轮未修改：
  - `project_source/*`
  - 代码文件
  - 测试文件
- 本轮暂未处理已有旧文件 `codex_source/02_codex_index.md` 的历史过时内容。

## 下一步建议

- 从下一轮开始，凡是外部结论要进入执行层，先补 `codex_source/03_research_findings_bridge.md`，不要再让 Codex 靠聊天记忆接手。
- 从下一轮开始，凡是执行现实已经证明原方案不完整成立，先按 `codex_source/05_execution_deviation_and_reality_sync.md` 回写，再决定是否继续执行。
- 若后续要继续清理执行层索引，可单独补一轮把 `codex_source/02_codex_index.md` 更新到与当前执行层文件体系一致。
