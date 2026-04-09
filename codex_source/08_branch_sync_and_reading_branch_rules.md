# 分支同步与主读取分支规则

## 1. 文件定位

本文件用于写死当前仓库关于：

- commit
- push
- PR
- `codex_log/latest.md`
- 主读取分支回流
- `.gitignore` / `local_only`

的执行层硬规则。

它不是理念说明，默认按可执行规则理解。

## 2. 固定主读取分支

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

新聊天 / 新 Codex 会话按仓库接手时，默认以该分支为准。

## 3. 正式状态判定

只有同步回 `codex/user-readable-map` 的结果，才默认算仓库正式状态。

以下情况都不等于仓库正式状态：

- 只在本地完成
- 只在任务分支完成
- 只开 PR 未回流主读取分支
- 只在聊天里说完成
- `codex_log/latest.md` 未更新

必须显式写清：

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“正式状态已同步”
- “聊天汇报完成”不等于“仓库正式事实已更新”

## 4. 上传 / 同步硬规则

### 4.1 何时必须 commit + push

凡本轮存在 Git 跟踪的仓库文件改动，且本轮结果不是 `local_only`、不是 `no_repo_change`，必须：

1. 更新 `codex_log/latest.md`
2. commit
3. push

### 4.2 何时必须同步回主读取分支

凡本轮形成了新的仓库正式事实，且该结果应成为新聊天默认接手口径，除 `commit + push` 外，还必须：

4. 同步回 `codex/user-readable-map`

信息同步任务补充规则：

- 若本轮改的是 `project_source/`、`codex_source/`、`codex_log/latest.md`
- 且这些改动会改变新聊天默认接手口径
- 则本轮默认属于“必须同步回主读取分支”的仓库正式事实更新

### 4.3 不得误报

若未满足对应条件，不得写：

- “已完成上传”
- “已同步”
- “仓库正式状态已更新”

## 5. 收尾必须回报的 4 个同步锚点

每轮仓库型任务收尾时，必须明确回报：

1. 当前工作分支
2. 最新提交 SHA
3. 是否已 push
4. 是否已同步回 `codex/user-readable-map`

## 6. 状态分类必须显式标记

每轮仓库型任务收尾时，必须显式分类为以下之一：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

分类口径固定如下：

### `formal_synced`

同时满足：

- 已更新 `codex_log/latest.md`
- 已 commit
- 已 push
- 已同步回 `codex/user-readable-map`

### `task_branch_only`

同时满足：

- 已 commit
- 已 push 到任务分支
- 但主读取分支还没更新

### `pr_open_not_merged_to_reading_branch`

同时满足：

- 已有 PR
- PR 尚未回流 `codex/user-readable-map`

### `local_only`

满足以下任一情况：

- 结果只存在本地
- 文件被 `.gitignore` 忽略
- 文件不应进入 GitHub

### `no_repo_change`

满足：

- 本轮没有 Git 跟踪的仓库文件改动

## 7. `.gitignore` / `local_only` 边界

若文件被 `.gitignore` 忽略，必须同时说明 3 件事：

1. 该结果标记为 `local_only`
2. 它不会上传到 GitHub
3. 它是否影响新聊天按仓库接手

必须同时保留以下保护边界：

- 本地配置
- secrets
- 私有凭证
- 其他不应进 Git 的本地文件

不得因为“每轮都必须上传”而错误提交这些文件。

## 8. 推荐收尾顺序

仓库型任务收尾时，默认顺序如下：

1. 确认本轮状态分类
2. 更新 `codex_log/latest.md`
3. 命中写日志条件时补完整日志
4. commit
5. push 当前任务分支
6. 若结果应成为正式接手口径，则同步回 `codex/user-readable-map`
7. 回报 4 个同步锚点

## 9. 允许例外

只有以下两类例外允许不走完整上传 / 回流链路：

- `local_only`
- `no_repo_change`

除此之外，默认按：

- `latest.md`
- commit
- push
- 必要时回流主读取分支

执行。

## 10. 当前一句话规则

凡本轮存在 Git 跟踪的仓库改动，且不是 `local_only` / `no_repo_change`，必须完成 `latest.md + commit + push`；凡本轮结果应成为仓库正式状态，还必须同步回 `codex/user-readable-map`；未满足这些条件时，不得写“已完成上传”或“已同步”。
