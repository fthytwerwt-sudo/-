# V3 Plan Fix 差异报告

## 1. 对比对象

- 旧 V3 plan：上一轮对《短视频自动流的最简单流程》V3 主线样片候选片的执行计划。
- 修正版 V3 plan：本目录 `revised_v3_plan.md`。

## 2. 修正了什么

| 旧 plan 偏差 | 修正后口径 | 原因 |
| --- | --- | --- |
| 把正式主线四件套理解成“本轮必须一次性真实跑通所有能力，否则 blocked” | 先裁决样片等级，再决定是否 blocked | 仓库需要区分 `mainline_inheritance_candidate`、`flow_proof_sample`、`technical_flow_sample`、`blocked` |
| 可能把 `formal_api_demo` 文件名当成 API 主持壳能力 | 增加 API 主持壳 runtime 审计门槛 | 文件名不是能力证明，必须有入口、参数、输出、模型/API、成功报告和 vNext 主持壳匹配关系 |
| 缺云剪时默认 blocked | 按样片等级判断 | mainline 必须云剪；flow proof 可不云剪但要标记 `not_executed_this_round` |
| 固定要求 8 张信息卡 | 信息卡数量由 block / segment 承载映射决定 | 防止信息卡抢主叙事，避免再次变成 PPT 念稿 |
| 所有卡片倾向归入 `cute_info_card_route` | 按卡片职责拆成三条 route | v3.1 视觉路由已确认三条卡片 route 必须分离 |
| 漏掉 HyperFrames 最新能力 | 新增 `card_motion_layer` 计划和验证报告 | HyperFrames 只能做卡片动效层，不能成为新 route 或中段录屏叠层 |
| 缺完整文案到画面承载映射 | 新增 `script_to_visual_carrier_map.md` | 完整文案保真不等于同一种画面形式承载 |
| 未明确样片等级 | 新增 `sample_level_decision.md` | 防止把 flow proof 写成 mainline candidate |

## 3. 删除了什么

- 删除“缺云剪一律 blocked”的单一路径。
- 删除“信息卡固定 8 张”的机械要求。
- 删除“所有辅助卡统一走 `cute_info_card_route`”的错误倾向。
- 删除“发现 formal_api_demo 即可假设 API 主持壳可用”的隐含判断。

## 4. 新增了什么

- `sample_level_decision.md`
- `block_segment_carrier_map.md`
- `script_to_visual_carrier_map.md`
- `hyperframes_motion_plan.md`
- `hyperframes_motion_validation_report.md`
- `visual_route_plan.md`
- `locked_reference_inheritance_plan.md`
- `render_ready_gate.md`

## 5. 为什么这样修

`已确认` 当前仓库正式主线是 API 生成真人 / 主持壳 + 用户录制素材 + 少量 PPT / 信息卡 + 云端剪辑。
`已确认` 当前 v3.1 已有三条视觉 route 和 locked reference registry。
`已确认` HyperFrames 最新定位只是 `card_motion_layer`。
`待验证` API 主持壳 runtime、完整项目 TTS、V3 云剪实跑是否能支撑主线候选。

因此修正版 plan 的关键不是直接出片，而是先把等级、承载、route、reference 和 render gate 写清楚。
