# 2026-04-04 branch sync / reading branch rules 固化

## 本轮目标

- 把“每轮执行后必须 commit / push / latest / 回流主读取分支”的要求写成仓库正式硬规则。
- 不再只靠聊天提醒“记得上传”。

## 执行前已确认事实

- 当前仓库默认主读取分支是：
  - `codex/user-readable-map`
- 现有规则只明确写到了：
  - `latest.md`
  - commit
  - push 当前分支
- 但还没有把以下内容写死：
  - 主读取分支回流
  - 4 个同步锚点
  - 5 类状态分类
  - `.gitignore` / `local_only` 边界
- 用户要求先读的
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  当前仓库不存在。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `.gitignore`

## 实际改动

- 修改：
  - [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
  - [codex_source/01_execution_rules.md](/Users/fan/Documents/视频工厂/codex_source/01_execution_rules.md)
  - [codex_source/02_current_execution_context.md](/Users/fan/Documents/视频工厂/codex_source/02_current_execution_context.md)
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
- 新增：
  - [codex_source/08_branch_sync_and_reading_branch_rules.md](/Users/fan/Documents/视频工厂/codex_source/08_branch_sync_and_reading_branch_rules.md)
  - [codex_log/20260404_branch_sync_and_reading_branch_rules.md](/Users/fan/Documents/视频工厂/codex_log/20260404_branch_sync_and_reading_branch_rules.md)

## 新增 / 改写的硬规则

- 主读取分支固定为：
  - `codex/user-readable-map`
- 凡本轮存在 Git 跟踪的仓库文件改动，且结果不是 `local_only` / `no_repo_change`，必须：
  - 更新 `codex_log/latest.md`
  - commit
  - push
- 凡本轮形成新的仓库正式事实，还必须：
  - 同步回 `codex/user-readable-map`
- 每轮仓库型任务收尾必须回报 4 个同步锚点：
  - 当前工作分支
  - 最新提交 SHA
  - 是否已 push
  - 是否已同步回 `codex/user-readable-map`
- 每轮仓库型任务必须显式分类为以下之一：
  - `formal_synced`
  - `task_branch_only`
  - `pr_open_not_merged_to_reading_branch`
  - `local_only`
  - `no_repo_change`
- `.gitignore` 忽略文件必须显式标记为 `local_only`，并说明：
  - 不会上 GitHub
  - 是否影响新聊天按仓库接手
- 明确禁止偷换：
  - 任务分支已 push != 主读取分支已更新
  - 已开 PR != 正式状态已同步
  - 聊天汇报完成 != 仓库正式事实已更新

## 实际执行

- 文本规则检索：
  - `rg -n "user-readable-map|latest.md|formal_synced|local_only|no_repo_change|.gitignore" AGENTS.md codex_source codex_log`
- 读取：
  - `sed -n ... AGENTS.md`
  - `sed -n ... codex_source/00_codex_readme.md`
  - `sed -n ... codex_source/01_execution_rules.md`
  - `sed -n ... codex_source/02_current_execution_context.md`
  - `sed -n ... codex_log/latest.md`
  - `sed -n ... .gitignore`

## 当前结果

- 当前仓库里已经存在明确写死的上传 / `latest.md` / 主读取分支回流规则。
- 本轮把原先缺失的：
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  补成了正式执行层文件。

## 下一步建议

- 后续仓库型任务结束前，先判断本轮状态分类，再决定：
  - 是 `formal_synced`
  - 还是 `task_branch_only`
  - 或 `pr_open_not_merged_to_reading_branch`
- 若还没回流 `codex/user-readable-map`，不得写成仓库正式状态已更新。
