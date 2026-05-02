# HyperFrames 卡片边界写入报告 hyperframes_card_boundary_report

## 1. 本轮范围

- `已确认` 本轮在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内执行。
- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/hyperframes-card-routing-and-aliyun-edit-audit-20260503`。
- `已确认` 本轮只做 HyperFrames 三类卡片动效接入规则设计，不生成视频、音频、图片，不修改 v3.1 正片，不修改 `dist/latest_review_pack/` 既有产物。
- `已确认` HyperFrames 当前定位为 `card_motion_layer（卡片动效层）`。
- `已确认` HyperFrames 当前不是 `new_visual_route（新视觉路由）`，不是 `middle_recording_overlay_layer（中段录屏叠层）`，不是 `full_video_generation_layer（整条视频生成层）`，也不是 `cloud_editing_replacement（云端剪辑替代品）`。

## 2. 读取与判断依据

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_local_artifact_paths.md`
- `package.json`
- `package-lock.json`
- `README.md`

`已确认` `visual_route_validation_report.json` 中 `passed = true`，三类卡片 route 分配与本轮接入判断一致。

## 3. route mapping table

| HyperFrames motion_id | 中文名 | 必须挂载 route | 允许 segment | 禁止 segment / 禁止用途 | 判断 |
| --- | --- | --- | --- | --- | --- |
| `data_or_result_diff_card_motion` | 数据卡 / 结果差卡动效 | `cute_info_card_route` | `shot15_result_diff_card`；未来灰度测试数据卡 / 指标卡只能作为 `cute_info_card_route` 扩展 | 用户录制素材中段、反面录屏、正面录屏、录屏证据段、API 生成真人段、云端剪辑总装 | `已确认` 与 route map 对齐 |
| `prompt_tail_card_motion` | Prompt 引用尾卡动效 | `cute_info_card_route` | `shot16_low_pressure_ending` | 主结尾、长 prompt、长代码、强卖课 CTA、复杂教程页、中段录屏 | `已确认` 与 route map 对齐 |
| `sassy_reaction_card_motion` | 骚萌卡动效版 | `sassy_reaction_card_route` | `shot03_problem_hook_sassy_card`、`shot05_negative_reversal_sassy_card`、`shot14_positive_reversal_sassy_card` | `cute_info_card_route` 白粉信息卡外壳、普通信息卡、贴纸、PR #7 A、中段录屏 | `已确认` 与 route map 对齐 |

## 4. 三类卡片边界

### 4.1 数据卡 / 结果差卡动效

可以做：

- 数字轻动效
- 两列对比入场
- 结果差箭头
- 关键指标显影
- 轻微强调动画
- 一屏最多 2-3 个信息模块

不能做：

- 深蓝科技 UI
- 密集数据大屏
- 电商筛选页
- 复杂 dashboard
- 小字堆叠
- 假 App 页面
- 抢真实录屏证据
- 让卡片变成工具广告

内容职责：

- 帮观众看懂“普通问法 vs 工作流 / 工作包后”的结果差。
- 不替代真实录屏证据。
- 不新增素材里没有的数据结论。

### 4.2 Prompt 引用尾卡动效

可以做：

- Prompt 引用框轻入场
- 关键词高亮
- 1-2 行核心提示词显影
- 低压收束动效
- 轻微卡片呼吸感

不能做：

- 做成第二个主结尾
- 堆完整 prompt
- 堆长段代码
- 变成强卖课 CTA
- 做成复杂教程页
- 抢前面结果差卡的总结职责

内容职责：

- 只负责把用户从视频引到工作包 / prompt 包 / 咨询承接。
- 不承担主叙事。
- 不补充视频里没有讲过的新观点。

### 4.3 骚萌卡动效版

可以做：

- 角色轻动效
- 表情反应
- punchline 大字冲击
- 漫画冲击背景轻动
- 轻微弹跳 / 眨眼 / 得瑟动作
- 同一角色体系下的三张卡片动效统一

不能做：

- 使用 `cute_info_card_route` 的白粉信息卡外壳
- 变成普通信息卡
- 变成贴纸
- 变成纯可爱不搞笑
- 使用 PR #7 A
- 在 PR #7 B 读不到时回退 PR #7 A
- 抢真实录屏主体证据
- 让三张骚萌卡变成不同角色体系

内容职责：

- `shot03_problem_hook_sassy_card`：问题钩子，帮观众进入“这说的不就是我吗”。
- `shot05_negative_reversal_sassy_card`：反面反转，把旧做法“看起来有东西，实际不能用”变成笑点。
- `shot14_positive_reversal_sassy_card`：正面反转，放大“这回真的能用了”的爽点。

## 5. 当前明确禁止接入

HyperFrames 当前不接入：

- 用户录制素材中段
- 反面录屏
- 正面录屏
- 录屏证据段
- 录屏动态标注
- 录屏包装框
- 录屏叠层
- 整条视频生成
- API 生成真人段
- 云端剪辑总装
- 任何会遮挡或抢走真实录屏证据主体的动效

未来如果要接中段录屏，必须另起任务，先过 `route gate（路由门）`，并明确不会抢真实录屏证据；本轮规则不得自动放开。

## 6. 写入结果

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
  - 新增 `HyperFrames card_motion_layer 当前边界`。
  - 写入三类卡片到现有 route 的映射。
  - 写入 HyperFrames 禁止新增 route、禁止把中段录屏纳入默认接入范围、禁止替代云端剪辑或真实录屏证据。
- `GPT数据源/05_文案路由规则.md`
  - 新增 HyperFrames 卡片动效承载边界。
  - 明确 HyperFrames 不改变 block / segment 的文案职责。
- `GPT数据源/07_AI知识类视频价值规则.md`
  - 新增 HyperFrames 动效与真实证据边界。
  - 明确动效必须服务问题、反转、结果差。

## 7. 结论

`已确认` HyperFrames 当前最适合《视频工厂》的接入方式是：只作为三类卡片的 `card_motion_layer（卡片动效层）`，并且必须绑定现有 `cute_info_card_route` 与 `sassy_reaction_card_route`。未发现 route map 冲突。
