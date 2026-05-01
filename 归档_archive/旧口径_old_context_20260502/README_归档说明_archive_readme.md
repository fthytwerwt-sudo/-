# 旧口径归档说明 archive readme

## 1. 归档目的

本目录保存《视频工厂》v3 用户复审前的旧判断摘录，防止这些旧口径继续混在默认入口里影响 Codex 执行。

本目录内容只用于复盘，不作为当前事实入口，不作为后续 v3.1 执行参考。

## 2. 后续默认不读的旧口径

后续 Codex 默认不得把以下旧口径当成当前事实：

1. PR #22 创建时的 `content_validation = pending_user_chatgpt_review`。
2. PR #23 创建时的 “PR #7 A 是 preferred candidate / PR #7 B 不优先”。
3. 可爱卡片参考分支中旧 `route_suggestion` 里把骚萌卡继续指向 PR #7 A 的建议。
4. 任何把 `round34` 当成当前最新样片状态的旧摘要。

## 3. 当前正式覆盖口径

当前正式口径以主读取分支中的以下文件为准：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_source/01_execution_rules.md`
4. `codex_source/locked_reference_registry.md`
5. `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
6. `codex_log/current_publish_target.md`
7. `dist/latest_review_pack/summary.json`

当前已确认：

- v3 技术层是当前阶段里程碑达成，不是技术线最终锁定。
- 下一步仍需技术升级。
- v3 内容未过线，主要在 GPT 文案侧。
- `send_ready = false`。
- 后续骚萌卡执行参考为 `PR7_B_骚萌反应页.png`。
- 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- v3.1 生成前必须先输出并验证 `visual_route_map.json（视觉路由表）`。

## 4. 本目录文件

- `PR22_v3原始待复审口径_legacy_pr22_v3_pending_status.md`
- `PR23_骚萌卡A优先旧判断_legacy_pr23_a_preference.md`
- `可爱卡片旧route_suggestion_legacy_cute_route_suggestion.md`

这些文件保留旧判断来源和替换关系。后续默认不按它们执行。
