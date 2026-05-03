# HyperFrames 卡片动效计划

## 1. 定位

`已确认` HyperFrames 只能作为 `card_motion_layer（卡片动效层）`。
`已确认` HyperFrames 不是新视觉 route，不是中段录屏叠层，不是整条视频生成层，不是云端剪辑替代品。

## 2. motion 计划表

| card_id | assigned_route | motion_id | motion_role | allowed | blocked_if | why_not_recording_overlay | why_not_new_route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| api_station_card | `cute_info_card_route` | `data_or_result_diff_card_motion` | 轻量信息显影，说明 API 是外部能力入口 | 是 | 出现未证明 API 已接通、复杂 dashboard、密集小字 | API 段不是录屏证据，不能叠在用户素材上 | 已有 `cute_info_card_route` 足够承载 |
| cloud_station_card | `cute_info_card_route` | `data_or_result_diff_card_motion` | 云剪装配台状态边界 | 是 | 写成云剪正式稳定或替代真实云剪 | 云剪状态解释应独立成卡，不遮挡录屏 | 挂载现有信息卡 route |
| prompt_tail_card | `cute_info_card_route` | `prompt_tail_card_motion` | 1-2 行 prompt 关键词引用 | 是 | 堆完整 prompt、做第二个主结尾、强卖课 | Prompt 引用不应盖在 Trae 录屏证据上 | 现有 Prompt 尾卡属于信息卡 route |
| jimeng_compare_card | `cute_info_card_route` | `data_or_result_diff_card_motion` | 两列对比：抽素材 vs 搭流程 | 可选 | 贬低即梦、写成评测结论、信息过密 | 对比卡不是录屏叠层 | 现有信息卡 route 足够 |
| sassy_hook_card | `sassy_reaction_card_route` | `sassy_reaction_card_motion` | 问题钩子情绪反应 | 可选 | 使用 PR #7 A、套白粉信息卡外壳、抢录屏证据 | 反应卡必须独立整页，不叠录屏 | 已有骚萌反应卡 route |
| sassy_reversal_card | `sassy_reaction_card_route` | `sassy_reaction_card_motion` | 反转笑点 / 停顿 | 可选 | 不继承 PR #7 B、变普通信息卡 | 反转卡不应压缩真实证据段 | 不能新增 route |
| closing_tail_card | `cute_info_card_route` | `prompt_tail_card_motion` | 低压尾卡，收住“顺序对了” | 可选 | 变成第二个主结尾或强 CTA | 结尾卡独立承载，不叠主持壳主体 | 使用现有信息卡尾卡能力 |

## 3. 禁止事项

- 不得接入用户录制素材中段。
- 不得接入豆包 / Trae / Codex 录屏证据段。
- 不得做录屏动态标注。
- 不得做录屏包装框或叠层。
- 不得替代真实录屏主体证据。
- 不得替代云端剪辑。
- 不得替代 API 生成真人 / 主持壳。
- 不得新增并列视觉 route。
- 不得让卡片动效抢主叙事。
