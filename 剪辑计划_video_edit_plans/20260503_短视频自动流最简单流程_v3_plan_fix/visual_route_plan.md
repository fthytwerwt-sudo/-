# 视觉路由计划 visual_route_plan

## 1. 总原则

`已确认` 不得把所有卡片统一写成 `cute_info_card_route`。
`已确认` 卡片 route 由卡片职责决定。
`已确认` HyperFrames 只作为 motion layer 挂到既有 route。

## 2. route 规则

| card_role | assigned_route | 使用规则 |
| --- | --- | --- |
| 段落提示卡 | `cute_prompt_card_route` | 少信息量，中心大标题，一句短副标题，不承载复杂字段 |
| 信息卡 / 结果差卡 / Prompt 引用尾卡 | `cute_info_card_route` | 信息层级、关键词、结果差、引用尾卡，一屏最多 2-3 个模块 |
| 情绪反应卡 / 骚萌卡 | `sassy_reaction_card_route` | 继承 PR #7 B 独立 reaction page，不得回退 PR #7 A |

## 3. 卡片 route 分配

| card_id | card_role | assigned_route | why_this_route | forbidden_route | 是否使用 HyperFrames | motion_id |
| --- | --- | --- | --- | --- | --- | --- |
| opening_prompt_card | 段落提示卡 | `cute_prompt_card_route` | 只显影“自动流不是一键生成” | `cute_info_card_route`, `sassy_reaction_card_route` | 可选 | 无或轻提示 motion |
| process_keywords_card | 信息卡 | `cute_info_card_route` | 整理选题 / 脚本 / 分镜 / 素材 / 剪辑 / 发布 | `sassy_reaction_card_route` | 可选 | `data_or_result_diff_card_motion` |
| prompt_tail_card | Prompt 引用尾卡 | `cute_info_card_route` | 只引用 1-2 行 Trae prompt 关键词 | `cute_prompt_card_route`, `sassy_reaction_card_route` | 是 | `prompt_tail_card_motion` |
| api_station_card | 信息卡 | `cute_info_card_route` | 解释 API 是外部能力入口 | `sassy_reaction_card_route` | 可选 | `data_or_result_diff_card_motion` |
| cloud_station_card | 信息卡 | `cute_info_card_route` | 解释云剪是装配台，不是总控脑 | `sassy_reaction_card_route` | 可选 | `data_or_result_diff_card_motion` |
| codex_boundary_card | 状态边界卡 | `cute_info_card_route` | 标出 Codex 检查不等于内容过线 | `sassy_reaction_card_route` | 否 | 不使用，避免抢 Codex 录屏 |
| jimeng_compare_card | 结果差 / 对比卡 | `cute_info_card_route` | 两列对比抽素材 vs 搭流程 | `sassy_reaction_card_route` | 可选 | `data_or_result_diff_card_motion` |
| sassy_hook_card | 情绪反应卡 | `sassy_reaction_card_route` | 如需要问题钩子笑点，必须独立 reaction page | `cute_info_card_route`, `cute_prompt_card_route` | 可选 | `sassy_reaction_card_motion` |
| closing_tail_card | 低压尾卡 | `cute_info_card_route` | 引导“顺序对了，自动化才有地方落脚” | `sassy_reaction_card_route` | 可选 | `prompt_tail_card_motion` |

## 4. blocked 条件

- 骚萌卡使用 PR #7 A。
- 骚萌卡套 `cute_info_card_route` 外壳。
- 信息卡走 `sassy_reaction_card_route`。
- 段落提示卡承载复杂字段。
- 信息卡堆长段说明。
- 卡片替代用户录制素材主体。
- 未输出 route validation 即进入 render。
