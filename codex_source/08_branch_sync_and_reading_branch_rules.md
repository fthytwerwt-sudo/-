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

- `main`

新聊天 / 新 Codex 会话按仓库接手时，默认以该分支为准。

## 3. 正式状态判定

只有同步回 `main` 的结果，才默认算仓库正式状态。

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

4. 同步回 `main`

这里的“新的仓库正式事实”必须按下面这条补丁理解，不得再偷换成“只有成功达标才算”：

只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论本轮是成功、失败、半成功还是 blocked，都必须：
1. 更新 `codex_log/latest.md`
2. 若有真实执行结果，补 `codex_log/YYYYMMDD_任务名.md`
3. commit
4. push
5. 同步回 `main`

注意：
- `content_validation` 未通过，不等于不能同步
- 只要当前已知状态变了，就必须同步
- 同步时必须如实写状态，不能把半成功写成已达标

### 4.2A. 哪些“状态变化”属于必须回流条件

以下情况都默认属于“下个聊天框默认应该知道的当前状态变化”，因此必须回流主读取分支：

- `technical_validation` 结果变化
- `content_validation` 结果变化
- 从 `blocked` 变为部分成立 / 半成功 / 成功
- 从成功变为 `blocked`
- 新增或消除真实 blocker
- 样片 / 产物已落出，但内容未达标
- `technical_validation` 通过，但 `content_validation` 未通过
- 任何会改变新聊天默认接手判断的当前结论更新

信息同步任务补充规则：

- 若本轮改的是 `project_source/`、`codex_source/`、`codex_log/latest.md`
- 且这些改动会改变新聊天默认接手口径
- 则本轮默认属于“必须同步回主读取分支”的仓库正式事实更新

当前待发对象 / 当前样片任务补充规则：

- 若本轮结果改变了以下任一项：
  - 当前待发对象
  - 当前审核对象
  - 当前正式状态
  - 当前唯一最高优先级 blocker
  - 现在最该改的唯一一点
- 则除 `codex_log/latest.md` 外，还必须同步更新：
  - `codex_log/current_publish_target.md`
- 若本轮补齐、替换或确认了 Git 可追踪轻量证据包，还应同步更新：
  - `codex_log/current_publish_target_light_evidence.md`

执行车道 / 并发建议补充规则：

- 若本轮结果改变了以下任一项：
  - `lane_recommendation`
  - `lane_reason`
  - `lane_invalid_if`
  - `parallel_recommendation`
  - `parallel_reason`
  - `parallel_invalid_if`
- 则除 `codex_log/latest.md` 外，也必须同步更新：
  - `codex_log/current_publish_target.md`

必须明确：

- lane / parallel 建议属于接手口径
- 不是只在聊天里说过就算完成
- 只有回流到 `main` 才算正式已知

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
4. 是否已同步回 `main`

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
- 已同步回 `main`

补充解释：

- 不要求本轮一定“成功达标”
- `blocked` / 半成功 / `technical_validation` 通过但 `content_validation` 未通过，只要已如实回流，也属于 `formal_synced`

### `task_branch_only`

同时满足：

- 已 commit
- 已 push 到任务分支
- 但主读取分支还没更新

补充解释：

- 不得因为“本轮还没完全达标”就长期停留在 `task_branch_only`
- 只要当前已知状态已变化，继续停在 `task_branch_only` 就属于默认同步缺口

### `pr_open_not_merged_to_reading_branch`

同时满足：

- 已有 PR
- PR 尚未回流 `main`

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
3. 若本轮涉及当前待发对象 / 当前审核对象 / 当前唯一 blocker / 当前样片状态，再更新 `codex_log/current_publish_target.md`
4. 若本轮涉及轻量证据包变化，再更新 `codex_log/current_publish_target_light_evidence.md`
5. 命中写日志条件时补完整日志
6. commit
7. push 当前任务分支
8. 只要本轮结果改变了下个聊天框默认应该知道的当前状态，就同步回 `main`
9. 回报 4 个同步锚点

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

凡本轮存在 Git 跟踪的仓库改动，且不是 `local_only` / `no_repo_change`，必须完成 `latest.md + commit + push`；只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论成功、失败、半成功还是 `blocked`，都还必须同步回 `main`；当前待发对象指针里的 `lane_recommendation / parallel_recommendation` 也属于这种必须回流的接手口径；未满足这些条件时，不得写“已完成上传”或“已同步”。
