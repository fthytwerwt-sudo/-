# PR #23 骚萌卡 A 优先旧判断归档

## 归档原因

PR #23 是 2026-04-30 的骚萌卡历史样本复审包。该 PR 的只读判断曾认为 PR #7 A 是优先候选，PR #7 B 不优先。

用户 2026-05-01 已明确确认：后续骚萌卡执行参考改为 `PR7_B_骚萌反应页.png`。因此，PR #23 原始 A 优先判断被覆盖。

## 旧判断摘录

- PR：`https://github.com/fthytwerwt-sudo/-/pull/23`
- head：`codex/sassy-card-reference-review-20260430`
- base：`codex/user-readable-map`
- 状态：draft
- 旧判断：PR #7 A 是 preferred candidate；PR #7 B 作为对比，不优先。

## 当前覆盖口径

- PR #7 B 是后续骚萌卡执行参考。
- PR #7 B 已进入 registry：`sassy_card_pr7_b_visual_locked_20260501`。
- PR #7 A 保留为历史 / candidate 对照，不删除、不升级、不作为后续执行参考。
- 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。

## 后续规则

后续 v3.1 不得使用本归档旧判断作为执行依据。若需要复盘 PR #7 A/B 差异，只能作为历史对照阅读。
