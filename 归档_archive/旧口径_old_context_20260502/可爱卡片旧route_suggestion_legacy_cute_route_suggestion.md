# 可爱卡片旧 route_suggestion 归档

## 归档原因

可爱卡片参考分支最初的 `route_suggestion` 仍把 `sassy_reaction_card_route` 指向 PR #7 A。该建议产生于用户确认 PR #7 B 之前。

用户 2026-05-01 已确认 PR #7 B 为后续骚萌卡执行参考，因此旧 route suggestion 只能保留为历史判断。

## 旧判断摘录

- branch：`codex/cute-card-reference-audit-20260430`
- 文件：`复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/视觉判断_cute_card_visual_review.md`
- 旧建议：`sassy_reaction_card_route` 继续独立继承 PR #7 A 版骚萌 reaction card。

## 当前覆盖口径

三条视觉路由已拆开：

1. `cute_prompt_card_route（可爱段落提示卡路由）`
2. `cute_info_card_route（可爱信息卡路由）`
3. `sassy_reaction_card_route（骚萌反应卡路由）`

其中 `sassy_reaction_card_route` 的后续执行参考为 PR #7 B，不是 PR #7 A。

## 后续规则

v3.1 生成前必须先输出并验证 `visual_route_map.json（视觉路由表）`。route map 未通过前不得生成全片。
