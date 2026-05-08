# 20260330 Execution Gate And Parallel Rules

## 1. 本轮目标

- 先做一次排雷检查，确认当前执行对象还是正确的视频项目仓库，而不是错目录或空目录。
- 在确认对象正确且风险可控后，正式把 Codex 侧“执行闸门 / 自动补全边界 / 多 Codex 并行”规则落入当前仓库。

## 2. 执行前已确认事实

- 当前绝对路径是 `/Users/fan/Documents/视频工厂`。
- 当前目录是 Git 仓库，且关键目录仍存在：
  - `project_source/`
  - `codex_source/`
  - `codex_log/`
  - `cases/`
  - `dist/`
- 当前最小闭环关键产物仍存在：
  - `dist/demo/script.txt`
  - `dist/demo/captions.srt`
  - `dist/demo/voice.mp3`
  - `dist/demo/final.mp4`
- 当前工作分支是 `codex/user-readable-map`，working tree 在开始修改前是干净的。
- 当前仓库有 `origin`，指向 `https://github.com/fthytwerwt-sudo/-.git`。
- 当前仓库无本地 `skills/` 目录。
- `project_source/07_collaboration_adaptation_rules.md` 当前不存在；现有 `project_source/07_*` 文件是 `project_source/07_user_readable_repo_map.md`。

## 3. 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/06_project_index.md`
- 全局 skill：
  - `context-driven-development`
  - `verification-before-completion`
  - `writing-plans`
  - `writing-router-cn`
  - `brainstorming`
- 仓库与 Git 检查：
  - `pwd`
  - `ls -la`
  - `git status --short --branch`
  - `git branch --show-current`
  - `git branch --list`
  - `git log --oneline -5`
  - `git remote -v`
  - 关键目录与关键文件存在性检查

## 4. 实际改动

- 新增 `codex_source/06_execution_gate_and_parallel_rules.md`
  - 正式写入执行闸门、自动补全边界、多 Codex 并行规则、与 ChatGPT 层的衔接和当前项目防跑偏护栏。
- 修改 `codex_source/00_codex_readme.md`
  - 补入“命中协作方式 / 自动补全边界 / 是否进入执行 / 是否适合并行”时的补读入口。
  - 在执行层文件清单中补入 `codex_source/06_execution_gate_and_parallel_rules.md`。
- 修改 `codex_source/01_execution_rules.md`
  - 新增 `EXEC-013 顶层收口与并行执行规则`。
  - 明确未收口不执行、自动补全边界、并行规则以及与现有规则兼容关系。
- 修改 `AGENTS.md`
  - 在默认最小接手集合后补入协作方式 / 执行闸门 / 并行判断的补读入口。
- 修改 `codex_log/latest.md`
  - 刷新最近一次完成事项、下一步和新会话接手建议。
- 新增 `codex_log/20260330_execution_gate_and_parallel_rules.md`
  - 记录本轮排雷检查、读取、改动与结果。

## 5. 实际执行

- 先做阶段 A 排雷检查，确认当前不是错目录、不是空目录、不是非 Git 环境，也没有“只剩 prompt 文本、项目结构丢失”的情况。
- 在阶段 A 通过后，再按要求读取执行层与项目脑入口文件。
- 检查本地 / 全局 skill，并读取命中的全局 skill 说明。
- 在不修改 `project_source/*`、代码文件、测试文件和 `codex_source/05_runtime_and_artifact_rules.md` 的前提下，只对指定入口与规则文件做增量补丁。

## 6. 当前结果

- 当前仓库对象确认无误，阶段 A 通过，允许进入阶段 B。
- `codex_source/06_execution_gate_and_parallel_rules.md` 已真实创建。
- `codex_source/00_codex_readme.md` 已真实增量修改。
- `codex_source/01_execution_rules.md` 已真实新增 `EXEC-013`。
- `AGENTS.md` 已补最小入口说明。
- `codex_log/latest.md` 已刷新。
- 本轮完整日志已补入 `codex_log/20260330_execution_gate_and_parallel_rules.md`。
- 已完成 commit：`3c5a254 docs: add execution gate and parallel rules`。
- 已 push 到 `origin/codex/user-readable-map`。
- 本轮未改 `project_source/*`、代码文件、测试文件，也未改 `codex_source/05_runtime_and_artifact_rules.md`。

## 7. 下一步建议

- 后续若再出现“什么时候才允许下发 Codex”“什么能自动补全”“是否适合多工位并行”的判断，先统一回到 `codex_source/06_execution_gate_and_parallel_rules.md`。
- 若未来确实需要把协作适配层单独成文，可再新增 `project_source/07_collaboration_adaptation_rules.md`，并与现有 `project_source/07_user_readable_repo_map.md` 分工清楚。
- 本轮结果已同步到当前工作分支，后续可直接基于远端分支继续回审或拆下一轮小闭环。
