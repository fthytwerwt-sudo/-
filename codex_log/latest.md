# Latest

## 当前主结论

- `已确认` 本轮完成的是 **执行层默认同步规则补丁**，不是代码实现任务。
- `已确认` 当前仓库正式执行层默认新增了一条硬规则：

只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论本轮是成功、失败、半成功还是 blocked，都必须：
1. 更新 `codex_log/latest.md`
2. 若有真实执行结果，补 `codex_log/YYYYMMDD_任务名.md`
3. commit
4. push
5. 同步回 `codex/user-readable-map`

注意：
- `content_validation` 未通过，不等于不能同步
- 只要当前已知状态变了，就必须同步
- 同步时必须如实写状态，不能把半成功写成已达标

- `已确认` 这条规则已经补进仓库执行层入口，不再依赖 GPT Project 数据源文件补这条，也不再依赖聊天记忆补这条。
- `已确认` 以后默认不能再把“只有成功达标才同步”当成仓库规则。
- `已确认` 以后只要当前已知状态变了，哪怕是 `blocked`、半成功、或 `technical_validation` 通过但 `content_validation` 未通过，也必须回流 `codex/user-readable-map`。
- `已确认` 当前 reading branch 已更新到这条新规则口径。

## 当前接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_source/08_branch_sync_and_reading_branch_rules.md`
5. `codex_log/20260410_execution_layer_state_change_sync_rule_patch.md`

## 本轮状态

- 当前状态标签：
  - `formal_synced`
- 当前任务性质：
  - 执行层默认同步规则补丁
- 当前影响范围：
  - 顶层入口
  - 执行层入口
  - 详细分支同步规则
  - 默认接手日志口径

## 当前默认行为变化

- 过去容易出现：
  - 任务分支已 push，但 reading branch 没更新
  - `blocked` / 半成功状态没有进入新聊天默认已知
  - `content_validation` 未通过被误当成“先别同步”
- 当前正式默认改成：
  - 只要下个聊天框默认应该知道的当前状态变了，就必须回流主读取分支
  - 同步时必须如实写明成功、失败、半成功或 `blocked`
  - 不允许把半成功写成已达标

## 当前仍需明确

- 本轮修的是执行层仓库规则，不是 `project_source/`
- 本轮没有新增任何 GPT Project 数据源文件
- 本轮规则要以仓库文件和 `codex/user-readable-map` 为准，不以聊天记忆为准
