# 20260504 fresh clone体积对照验证 fresh_clone_size_comparison

## 本轮定位

- `已确认` 本轮先后合并 PR #48 与 PR #49。
- `已确认` 本轮执行 fresh clone / clean clone 对照验证。
- `已确认` 本轮未替换正式工作区，未删除正式工作区。
- `已确认` 本轮未执行 `git gc`、`git prune`、`git repack`、`git lfs migrate`、`filter-repo`、`filter-branch`、BFG 或 force push。
- `已确认` 本轮未修改当前发布状态。

## PR 合并记录

- PR #48：`Pre-upgrade delete old Video Factory assets`
  - 合并状态：`已合并`
  - merge commit：`d2df313920e1d7e4f720db279964d6a2324b06a1`
- PR #49：`Audit Git history large files without cleanup`
  - 合并状态：`已合并`
  - merge commit：`a1981935e404a78377e121b0643601cad01e483a`

## fresh clone 对照记录

- fresh clone 目录：`/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504`
- fresh clone 分支：`codex/user-readable-map`
- 正式工作区总大小：`33G`
- 正式工作区 `.git`：`21G`
- 正式工作区 `.git/objects/pack`：`19G`
- 正式工作区 `tmp_pack_*`：`28` 个，约 `15.49 GiB`
- fresh clone 总大小：`980M`
- fresh clone `.git`：`896M`
- fresh clone `.git/objects/pack`：`896M`
- fresh clone `tmp_pack_*`：`0` 个
- fresh clone `git count-objects -vH`：`garbage = 0`，`size-garbage = 0 bytes`

## 关键判断

- `已确认` 正式工作区 `.git` 约 `21G` 主要来自当前本地 `.git/objects/pack/tmp_pack_*` garbage，而不是远端当前主读取分支本身。
- `已确认` fresh clone 明显变小：`.git` 从 `21G` 降到 `896M`。
- `已确认` 当前更安全的瘦身路线不是 history rewrite，而是先迁移 / 切换到 clean clone 工作区。
- `待验证` `素材录制/` 仍约 `11G`，属于用户录制原始素材；若继续瘦身，需要另起“原始录屏素材外置 / 删除确认”任务。

## 报告

- `治理_reports/20260504_fresh_clone体积对照验证_fresh_clone_size_comparison/fresh_clone体积对照验证报告_fresh_clone_size_comparison_report.md`
