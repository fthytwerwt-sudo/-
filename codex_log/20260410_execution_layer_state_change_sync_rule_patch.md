# 20260410_execution_layer_state_change_sync_rule_patch

## 本轮目标

- 把“只要当前已知状态变了就必须回流主读取分支”的规则正式补进仓库执行层
- 不再让这条规则依赖 GPT Project 数据源文件
- 不再让这条规则依赖聊天记忆
- 不扩写 `project_source/`

## 为什么这轮必须补

当前仓库已经有：

- 新会话最小接手入口：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
- 固定主读取分支：
  - `codex/user-readable-map`
- `latest.md + commit + push + 回流` 的基础规则

但还缺一条更硬的补丁：

- 不是只有“成功达标”才回流
- `blocked` / 半成功 / `technical_validation` 通过但 `content_validation` 未通过，也可能改变下个聊天框默认应该知道的当前状态
- 这些状态如果不回流，就会继续出现：
  - 任务分支已 push
  - reading branch 仍旧
  - 新聊天默认口径不准

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/latest.md`

## 实际改动文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/latest.md`
- `codex_log/20260410_execution_layer_state_change_sync_rule_patch.md`

## 每个文件补了什么

### `AGENTS.md`

- 在顶层入口补了短规则版
- 明确：
  - 只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论成功、失败、半成功还是 `blocked`，都必须：
    - 更新 `codex_log/latest.md`
    - 必要时补执行日志
    - commit
    - push
    - 同步回 `codex/user-readable-map`

### `codex_source/00_codex_readme.md`

- 在执行层入口补了入口版规则
- 明确：
  - 这不是只针对“成功达标”轮次
  - `content_validation` 未通过，不等于不能同步
  - `blocked` / 半成功 / `technical_validation` 通过但 `content_validation` 未通过，也属于必须同步的执行层正式状态

### `codex_source/08_branch_sync_and_reading_branch_rules.md`

- 在“何时必须同步回主读取分支”处补了正式硬规则
- 明确适用：
  - 成功
  - 失败
  - 半成功
  - `blocked`
- 明确“状态变化”本身就是必须回流条件
- 明确：
  - `technical_validation` 通过但 `content_validation` 未通过，仍然要如实同步
  - `blocked` 只要改变当前正式已知状态，也必须同步
- 同时补了：
  - `formal_synced` 的解释不要求“成功达标”
  - `task_branch_only` 不能因为“还没完全达标”而长期滞留
  - 推荐收尾顺序里的第 6 步改成“只要状态变了就同步回主读取分支”

### `codex_log/latest.md`

- 改写为这轮规则补丁的最新接手摘要
- 明确：
  - 以后默认不再依赖 GPT Project 数据源补这条
  - 以后默认只要状态变了就必须回流主读取分支
  - 同步必须如实写状态，不能把半成功写成已达标

## 这轮之后默认行为如何变化

- 过去的错误默认：
  - 只有成功达标才同步
  - `blocked` / 半成功可以只停在任务分支
  - `content_validation` 未通过就先不回流
- 这轮之后的新默认：
  - 只要当前已知状态变了，就必须同步
  - 同步不是“庆功动作”，而是“更新仓库正式已知”
  - `blocked` / 半成功 / `technical_validation` 通过但 `content_validation` 未通过，都必须如实回流

## 本轮边界

- `已确认` 没有修改任何 `project_source/*`
- `已确认` 没有修改任何代码文件
- `已确认` 没有修改任何测试文件
- `已确认` 没有新增任何 GPT Project 数据源文件

## 本轮完成后应有的默认理解

- “任务分支已 push”不等于“正式接手口径已更新”
- “content_validation 未通过”不等于“先别同步”
- 只要当前已知状态变了，就要进入：
  - `latest.md`
  - 必要时完整执行日志
  - commit
  - push
  - `codex/user-readable-map`
