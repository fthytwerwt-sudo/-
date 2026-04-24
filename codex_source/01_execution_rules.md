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
6. 若任务命中“execution lane / parallel gate / 是否适合提速 / 是否适合并发 / lane recommendation / parallel recommendation”，在 `codex_log/latest.md` 之后优先读：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
7. 若任务命中“当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容”，在 `codex_log/latest.md` 之后优先读：
   - `codex_log/current_publish_target.md`
   - 若需要快速复核当前样片的 Git 可追踪轻量证据，再读 `codex_log/current_publish_target_light_evidence.md`
8. `codex_source/01_execution_rules.md`
9. `codex_source/02_current_execution_context.md`
10. `codex_source/03_research_findings_bridge.md`
11. 当前任务直接相关的 `project_source/*`
12. 命中价值 / 文案 / 结尾卡时，读 `codex_source/11_ai_knowledge_video_value_bridge.md`
13. 命中“什么算已知”时，读 `codex_source/12_codex_known_state_three_layer_rules.md`
14. 命中 commit / push / reading branch 回流时，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`

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

当前这类“execution lane / parallel mechanism”任务，额外必须检查：

- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`

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

若本轮结果会改变以下任一项，还必须同步刷新：

- `codex_log/current_publish_target.md`
  - 当前待发对象
  - 当前审核对象
  - 当前正式状态
  - 当前唯一最高优先级 blocker
  - 现在最该改的唯一一点
  - `lane_recommendation`
  - `lane_reason`
  - `lane_invalid_if`
  - `parallel_recommendation`
  - `parallel_reason`
  - `parallel_invalid_if`
- 若当前样片的 Git 可追踪轻量证据有变化，再同步刷新：
  - `codex_log/current_publish_target_light_evidence.md`

## 8A. 视频修改必须同步口径规则

以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。

默认必须同步检查：
1. `codex_log/latest.md`
2. `codex_log/current_publish_target.md`
3. `codex_log/current_publish_target_light_evidence.md`
4. `GPT数据源/08_当前正式事实.md`
5. `dist/latest_review_pack/summary.json`
6. `dist/latest_review_pack/review_manifest.md`
7. 如改变入口 / 分支 / 读取顺序，还必须同步 `AGENTS.md` 和 `codex_source/00_codex_readme.md`

硬规则：
- 不允许只改视频、不改口径
- 不允许只在工作分支改口径、不同步默认主读取分支
- 不允许把历史样片写成当前最新样片
- 不允许把 `technical_validation` 写成 `content_validation`
- 不允许用户未最终确认前写 `send_ready = yes`
- 不允许旧 `round` 状态继续覆盖最新 `latest_review_pack`
- 只要改动会影响新会话默认接手判断，就必须同步到 `codex/user-readable-map`

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
3. 重新读取 `codex_log/current_publish_target.md`，确认只靠稳定入口就能知道当前对象、状态、blocker 与下一步
4. 若本轮补了轻量证据包，再读取 `codex_log/current_publish_target_light_evidence.md`
5. 若本轮补的是 lane / parallel 机制，再读取：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
6. 若声称已同步回主读取分支，使用 `git show codex/user-readable-map:路径` 做实际读取验证

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
