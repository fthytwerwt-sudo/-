# 20260329 User Readable Repo Map

## 1. 本轮目标

- 在不改原执行规则含义的前提下，为当前仓库补一层“用户可讨论定位层”。
- 让非技术用户更容易看懂仓库结构、判断问题大概落在哪一层，并更准确地向 ChatGPT 描述修改点。

## 2. 执行前已确认事实

- 当前仓库已完成 GitHub baseline。
- 当前仓库已建立 `codex_log/` 日志机制。
- 当前仓库分层已经明确：
  - `project_source/` 负责项目脑
  - `codex_source/` 负责执行层
  - `codex_log/` 负责执行日志
- 当前仓库内无本地 `skills/` 目录。
- 当前工作分支已切到 `codex/user-readable-map`。

## 3. 实际读取

- 顶层与执行入口：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
- 项目脑索引与关键判断文件：
  - `project_source/06_project_index.md`
  - `project_source/00_project_brief.md`
  - `project_source/04_review_templates.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/02_scene_mode_templates.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/05_psychology_execution_rules.md`
- 执行层补充文件：
  - `codex_source/05_runtime_and_artifact_rules.md`
  - `codex_source/02_codex_index.md`
- 仓库状态：
  - `git status --short --branch`
  - `git remote -v`
- 已检查的 skill：
  - 仓库本地 `skills/`：不存在
  - 全局 `using-superpowers`
  - 全局 `brainstorming`
  - 全局 `context-driven-development`
  - 全局 `verification-before-completion`

## 4. 实际改动

- 新增 `project_source/07_user_readable_repo_map.md`
  - 用用户能直接讨论的方式解释仓库关键文件、分层关系、常见问题表象与问题类型。
- 新增 `codex_source/01_execution_rules.user_guide.md`
  - 把原执行规则翻成人话，重点解释读取顺序、分支 / PR 线路、日志规则、push 节奏和验证口径。
- 刷新 `codex_log/latest.md`
  - 让新会话能优先知道本轮已经补了“用户可读定位层”。

## 5. 实际执行

- 先按仓库入口规则读取最小接手集合与原执行规则，确认本轮是仓库型任务。
- 补读项目脑索引、项目 brief、回审模板与运行 / 产物规则，避免把“用户说明层”写成空泛摘要。
- 检查本地 / 全局 skill，并确认本轮以仓库事实和说明层落地为主，不改原规则含义。
- 在新分支 `codex/user-readable-map` 上落两份用户说明文件，并同步更新 `codex_log/latest.md`。

## 6. 当前结果

- 当前仓库已新增一份用户版仓库地图：
  - 帮用户判断问题更像项目边界、结构、文案、节奏、画面、执行还是产物。
- 当前仓库已新增一份执行规则用户说明：
  - 帮用户理解为什么仓库型任务会先读文件、走分支、写日志、在小闭环后 push 当前分支。
- 原 `codex_source/01_execution_rules.md` 的规则含义未被改写。

## 7. 下一步建议

- 后续与 ChatGPT 协作时，优先先用 `project_source/07_user_readable_repo_map.md` 定位问题层级，再决定进入哪一层细聊。
- 若用户觉得问题在仓库推进方式，而不是内容本身，优先看 `codex_source/01_execution_rules.user_guide.md`。
- 若后续要继续整理执行层导航，可单独评估是否同步更新仍带早期状态表述的 `codex_source/02_codex_index.md`，本轮未改它。
