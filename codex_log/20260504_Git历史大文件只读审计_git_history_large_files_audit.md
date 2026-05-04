# 20260504 Git历史大文件只读审计 git_history_large_files_audit

## 本轮定位

- `已确认` 本轮只做 `.git` 历史大文件只读审计。
- `已确认` 未删除、未移动、未重命名任何文件。
- `已确认` 未执行 `git gc`、`git prune`、`git repack`、`git lfs migrate`、`filter-repo`、`filter-branch`、BFG 或 force push。
- `已确认` 未修改当前发布状态。

## 关键结论

- `.git` 当前约 `21G`。
- `.git/objects` 约 `21G`。
- `.git/objects/pack` 约 `19G`。
- `git count-objects -vH` 报告 `size-garbage = 15.51 GiB`，是本地 `.git` 过大的最大直接来源。
- `.git/objects/pack/tmp_pack_*` 数量 `28`，合计约 `15.5 GiB`。
- 正式 pack 约 `3.99 GiB`，仍包含旧视频、旧音频、旧图片、旧复审包和旧 dist 产物历史对象。

## 推荐路线

- 主路线：下一轮先做 fresh clone / clean clone 对照验证。
- 备选路线：如果远端历史仍大，再设计 Git LFS / history rewrite 方案。

## 已知冻结未追踪文件

- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`
- 状态：`untracked / frozen / untouched`
- 本轮处理：未纳入、未删除、未移动、未重命名、未修改。

## 报告

- `治理_reports/20260504_Git历史大文件只读审计_git_history_large_files_audit/Git历史大文件只读审计报告_git_history_large_files_audit_report.md`
