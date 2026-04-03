# Latest

## 当前仓库执行机制状态

- 2026-04-04 本轮修的是“上传 / 同步执行机制”，不是业务功能。
- 当前仓库默认主读取分支已明确固定为：
  - `codex/user-readable-map`
- 当前执行层已新增专门规则文件：
  - [codex_source/08_branch_sync_and_reading_branch_rules.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/08_branch_sync_and_reading_branch_rules.md)

## 本轮新增 / 改写的正式硬规则

- 凡本轮存在 Git 跟踪的仓库文件改动，且结果不是 `local_only` / `no_repo_change`，必须：
  - 更新 `codex_log/latest.md`
  - commit
  - push
- 凡本轮形成新的仓库正式事实，且应成为新聊天默认接手口径，还必须：
  - 同步回 `codex/user-readable-map`
- 每轮仓库型任务收尾，必须回报 4 个同步锚点：
  - 当前工作分支
  - 最新提交 SHA
  - 是否已 push
  - 是否已同步回 `codex/user-readable-map`
- 每轮仓库型任务收尾，必须显式分类为以下之一：
  - `formal_synced`
  - `task_branch_only`
  - `pr_open_not_merged_to_reading_branch`
  - `local_only`
  - `no_repo_change`
- `.gitignore` 忽略文件必须显式标记为 `local_only`，并说明：
  - 不会上传到 GitHub
  - 是否影响新聊天按仓库接手

## 当前禁止偷换

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“正式状态已同步”
- “聊天汇报完成”不等于“仓库正式事实已更新”
- `codex_log/latest.md` 未更新，不得写“已完成上传”或“已同步”

## 本轮实际修改文件

- [AGENTS.md](/private/tmp/video-factory-user-readable-map.oh1UeA/AGENTS.md)
- [codex_source/01_execution_rules.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/01_execution_rules.md)
- [codex_source/02_current_execution_context.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/02_current_execution_context.md)
- [codex_source/08_branch_sync_and_reading_branch_rules.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/08_branch_sync_and_reading_branch_rules.md)
- [codex_log/latest.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_log/latest.md)

## 当前最关键下一步

- 后续所有仓库型任务收尾时，先按 5 类状态分类，再判断：
  - 只需 `commit + push`
  - 还是还要同步回 `codex/user-readable-map`
- 未同步回主读取分支前，不得把结果写成仓库正式状态。

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- [codex_log/latest.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_log/latest.md)
- [codex_source/01_execution_rules.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/01_execution_rules.md)
- [codex_source/02_current_execution_context.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/02_current_execution_context.md)
- [codex_source/08_branch_sync_and_reading_branch_rules.md](/private/tmp/video-factory-user-readable-map.oh1UeA/codex_source/08_branch_sync_and_reading_branch_rules.md)
