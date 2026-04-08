# Codex 执行规则

## 1. 文件定位

本文件规定 Codex 在《视频工厂》仓库中的默认执行方式。

它负责：

- 默认读取顺序
- 什么时候必须先审计
- 什么范围可以改
- GPT 数据源与仓库不同步时如何处理
- 仓库型任务的日志、提交、推送与回流规则
- 完成前最小验证要求

## 2. 默认读取顺序

每次任务默认按以下顺序读取：

1. `AGENTS.md`
2. 当前仓库本地 `skills/` 是否存在
3. 若本地无相关 skill，再检查全局 `~/.codex/skills`
4. `codex_source/00_codex_readme.md`
5. `codex_log/latest.md`
6. `codex_source/01_execution_rules.md`
7. `codex_source/02_current_execution_context.md`
8. `codex_source/03_research_findings_bridge.md`
9. 当前任务直接相关的 `project_source/*`
10. 命中价值 / 文案 / 结尾卡时，读 `codex_source/11_ai_knowledge_video_value_bridge.md`
11. 命中“什么算已知”时，读 `codex_source/12_codex_known_state_three_layer_rules.md`
12. 命中 commit / push / reading branch 回流时，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`

当前仓库现实 `已确认`：

- 仓库本地 `skills/` 目录不存在
- 相关 skills 需回退检查全局 `~/.codex/skills`

## 3. skill 检查硬规则

执行前必须：

1. 先检查当前仓库本地 `skills/`
2. 若无，再检查全局 `~/.codex/skills`
3. 命中相关 skill 时必须使用
4. 若未找到或不适用，必须如实说明

当前这类“项目口径 / 接手口径 / 文档维护”任务，至少要优先检查：

- `using-superpowers`
- `context-driven-development`
- `verification-before-completion`

## 4. 哪些情况必须先审计

出现以下任一情况，必须先审计再改：

1. 用户明确要求先看仓库现实
2. 任务目标是“同步源事实 / 修复接手口径 / 改默认主线”
3. 任务涉及 `project_source` 与 `codex_source` 的交叉修改
4. 任务涉及主读取分支 `codex/user-readable-map`
5. 当前仓库文件与聊天里的说法可能不一致

## 5. 默认允许修改范围

只有在用户明确授权时，才允许修改：

- 当前任务点名的 `project_source/*`
- 当前任务点名的 `codex_source/*`
- `codex_log/*`

没有明确授权时，默认不改：

- 代码文件
- 测试文件
- 配置 / 密钥文件
- `dist/*`
- 不在本轮范围内的文档

## 6. GPT 数据源不会自动同步到 Codex 仓库

这是执行层硬规则：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 外部资料、Perplexity 结论、ChatGPT 收束结果，若会影响执行，必须先回写仓库或显式带入执行单

未回写前，它们最多只能算：

- `GPT 已知`
- 或 `Codex 条件已知`

不能直接写成：

- `Codex 正式已知`

## 7. 仓库型任务默认线路

命中以下任一条件，默认按仓库型任务处理：

- 改仓库文件
- 修项目口径 / 执行口径 / 路由口径 / 接手口径
- 需要 commit / push / 回流主读取分支

默认线路：

先审计现状 -> 改文件 -> 更新日志 -> 验证 -> commit -> push 当前分支 -> 同步回 `codex/user-readable-map`

## 8. 执行日志硬规则

只要本轮出现以下任一事实，就必须写 `codex_log/`：

- 改了仓库文件
- 跑了命令
- 完成了 commit / push / 同步
- 形成了新的阻塞点 / 交接点

至少要做两件事：

1. 刷新 `codex_log/latest.md`
2. 新增一条 `codex_log/YYYYMMDD_任务名.md`

## 9. 主读取分支与状态分类

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

状态分类必须显式标记为：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

硬规则：

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“仓库正式状态已同步”
- 只有同步回 `codex/user-readable-map`，才算主读取分支正式已知

## 10. 这类任务的最小验证

这类文档 / 规则 / 接手口径修复任务，完成前至少要做：

1. `git diff --check`
2. 重新读取关键目标文件，确认口径一致
3. 若声称已同步回主读取分支，使用 `git show codex/user-readable-map:路径` 做实际读取验证

## 11. 完成口径硬规则

不得把以下两件事写成同一件事：

- 仓库口径已同步
- 新主线样片已验证成立

本轮如果只完成了文档 / 规则 / 桥接 / latest / reading branch 回流，只能写：

- 仓库口径已同步

不能写：

- 样片验证通过
- 新主线已被质量验证成立

## 12. 收尾时必须回报的 4 个同步锚点

每轮仓库型任务收尾时，必须明确回报：

1. 当前工作分支
2. 最新提交 SHA
3. 是否已 push
4. 是否已同步回 `codex/user-readable-map`
