# v3.1 视觉路由规则 v31 visual routing rules

## 1. 文件定位

本文件是《视频工厂》v3.1 当前基线及后续升级必须读取的视觉路由规则。

它规定后续生成 / 修改前的 routing gate（路由门）和 reference inheritance（参考继承）。当前 v3.1 已成为视频基线，但这不代表可发送，不代表内容验证通过，不代表视觉母版已锁定。

## 2. 当前 v3.1 基线硬边界

- `已确认` 当前最新视频基线为 v3.1：`current_video_baseline = v3.1`。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1：`future_iteration_base = v3.1`。
- `已确认` v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` v3.1 技术验证已通过，但技术线未锁定，必须保持 `technical_line_locked = false（技术线未锁定）`。
- `已确认` 下一步仍需要 `technical_upgrade_next = true（技术升级）`。
- `已确认` v3.1 内容没有新的通过确认，必须写 `content_validation = pending_user_chatgpt_review_or_not_passed_copywriting_side（仍待用户 / ChatGPT 内容复审；不得写成内容通过）`。
- `已确认` `send_ready = false（不可发送）`。
- `已确认` `visual_master_locked = false（视觉母版未锁定）`。
- `已确认` `voice_validation = pending_user_chatgpt_review`，`final_voice_validated = false`。
- `已确认` `visual_route_map.json（视觉路由表）` 与 `visual_route_validation_report.json（视觉路由验证报告）` 已进入 `dist/latest_review_pack/`。
- `已确认` PR #7 B 是后续骚萌卡唯一执行参考；PR #7 A 只能作为历史 / candidate 对照。

## 3. 三条视觉路由

### 3.1 `cute_prompt_card_route（可爱段落提示卡路由）`

适用 segment：

- `negative_display_prompt_card（反面展示提示卡）`
- `positive_display_prompt_card（正面展示提示卡）`

继承来源：

- `cute_prompt_card_route_locked_20260501（可爱段落提示卡路由锁定参考）`
- `prompt_card_pink_sakura_round34_candidate_20260430（round34 粉色樱花提示卡候选）`
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png`
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png`

必须继承：

- 粉色樱花柔和展示牌
- 白粉圆角主卡
- 细线边框
- 轻花边 / 蕾丝边感
- 樱花枝、少量花瓣、小蝴蝶结、柔光
- 中心大标题
- 一句短副标题
- 少信息量、温柔提示、段落提示职责

禁止：

- 承载复杂字段
- 堆长段说明
- 变成科技 UI
- 变成骚萌 reaction card
- 变成真实 App UI
- 抢真实录屏主体

### 3.2 `cute_info_card_route（可爱信息卡路由）`

适用 segment：

- `shot01_result_diff_opening（结果差开头卡）`
- `shot06_cause_turning_point（归因转折卡）`
- `shot08_prompt_architecture_card（Prompt 架构功能卡）`
- `shot15_result_diff_card（结果差卡）`
- `shot16_low_pressure_ending（低压尾卡 / Prompt 引用尾卡）`

继承来源：

- `cute_info_card_route_locked_20260501（可爱信息卡路由锁定参考）`
- 主皮肤：粉色樱花柔和展示牌方向
- 结构规则：`card_visual_quality_clean_ui_texture_candidate_20260430（功能卡 / 结果差卡 / Prompt 引用尾卡清晰质感候选参考）`
- 用户确认文字锚点：粉色樱花柔和展示牌 + 清晰信息层级

必须继承：

- 可爱、柔和、亲和
- 白粉圆角主卡
- 清晰分组
- 大标题清楚
- 重点内容高亮
- 一屏最多 2-3 个信息模块
- 结果差卡可做两列对比
- Prompt 尾卡可做引用框结构
- 足够留白、层级清楚、可读性高

禁止：

- 深蓝冷静科技 UI
- 冷静硬商务 UI
- 电商筛选页
- `More Filters` 式 CTA
- 黑色底部按钮
- 假 App 导航
- 一堆分类筛选项
- 英文乱码
- 小字堆叠
- 和骚萌卡共用外壳

### 3.3 `sassy_reaction_card_route（骚萌反应卡路由）`

适用 segment：

- `shot03_problem_hook_sassy_card（问题钩子骚萌卡）`
- `shot05_negative_reversal_sassy_card（反面反转骚萌卡）`
- `shot14_positive_reversal_sassy_card（正面反转骚萌卡）`

继承来源：

- `sassy_card_pr7_b_visual_locked_20260501（PR #7 B 骚萌卡视觉锁定参考）`
- `sassy_card_three_type_rule_locked_20260428（三类骚萌卡放置规则锁定参考）`
- `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png`

必须继承：

- 独立 reaction page
- 大面积角色
- 明确表情
- 表情 / 动作方向以 PR #7 B 为准
- 漫画冲击背景
- 大字 punchline
- 9:16 竖屏整页反应卡
- 三张骚萌卡角色体系统一
- 和信息卡、段落提示卡完全不同

禁止：

- 使用 `cute_prompt_card_route`
- 使用 `cute_info_card_route`
- 使用白粉展示牌外壳
- 使用信息卡排版
- 使用冷静科技 UI
- 只是可爱展示牌 + 小人物
- 像普通信息卡
- 抢真实录屏证据
- 读不到 PR #7 B 时回退 PR #7 A

### 3.4 HyperFrames `card_motion_layer（卡片动效层）` 当前边界

`已确认` HyperFrames 当前只允许作为 `card_motion_layer（卡片动效层）` 接入，不是新视觉路由，不是中段录屏增强层，不是整条视频生成层，也不是云端剪辑替代品。

HyperFrames 当前允许接入的 3 类卡片动效：

| motion_id | 中文名 | 必须挂载的现有 route | 允许 segment | 内容职责 |
| --- | --- | --- | --- | --- |
| `data_or_result_diff_card_motion` | 数据卡 / 结果差卡动效 | `cute_info_card_route` | `shot15_result_diff_card`；未来灰度测试数据卡 / 指标卡如需新增，也只能作为 `cute_info_card_route` 扩展 | 帮观众看懂“普通问法 vs 工作流 / 工作包后”的结果差，不替代真实录屏证据，不新增素材里没有的数据结论 |
| `prompt_tail_card_motion` | Prompt 引用尾卡动效 | `cute_info_card_route` | `shot16_low_pressure_ending` | 只做引用、低压收束和工作包 / prompt 包 / 咨询承接，不承担主叙事，不做第二个主结尾 |
| `sassy_reaction_card_motion` | 骚萌卡动效版 | `sassy_reaction_card_route` | `shot03_problem_hook_sassy_card`、`shot05_negative_reversal_sassy_card`、`shot14_positive_reversal_sassy_card` | 继承 PR #7 B 独立 reaction page 路线，服务问题钩子、反面反转、正面反转，不变成普通信息卡 |

数据卡 / 结果差卡动效可以做：

- 数字轻动效
- 两列对比入场
- 结果差箭头
- 关键指标显影
- 轻微强调动画
- 一屏最多 2-3 个信息模块

数据卡 / 结果差卡动效禁止：

- 深蓝科技 UI
- 密集数据大屏
- 电商筛选页
- 复杂 dashboard
- 小字堆叠
- 假 App 页面
- 抢真实录屏证据
- 让卡片变成工具广告

Prompt 引用尾卡动效可以做：

- Prompt 引用框轻入场
- 关键词高亮
- 1-2 行核心提示词显影
- 低压收束动效
- 轻微卡片呼吸感

Prompt 引用尾卡动效禁止：

- 把尾卡做成第二个主结尾
- 堆完整 prompt
- 堆长段代码
- 变成强卖课 CTA
- 做成复杂教程页
- 抢前面结果差卡的总结职责

骚萌卡动效版可以做：

- 角色轻动效
- 表情反应
- punchline 大字冲击
- 漫画冲击背景轻动
- 轻微弹跳 / 眨眼 / 得瑟动作
- 同一角色体系下的三张卡片动效统一

骚萌卡动效版禁止：

- 使用 `cute_info_card_route` 的白粉信息卡外壳
- 变成普通信息卡
- 变成贴纸
- 变成纯可爱不搞笑
- 使用 PR #7 A
- 在 PR #7 B 读不到时回退 PR #7 A
- 抢真实录屏主体证据
- 让三张骚萌卡变成不同角色体系

当前明确禁止 HyperFrames 接入：

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

未来如果要让 HyperFrames 接中段录屏，必须另起任务，先过 `route gate（路由门）`，并明确不会抢真实录屏证据；本节规则不得自动放开中段录屏。

## 4. v3.1 生成前置 gate

后续任何基于 v3.1 的生成 / 修改 / 技术升级任务必须先读取或输出：

`visual_route_map.json（视觉路由表）`

route map 必须至少包含：

1. `negative_display_prompt_card`
2. `positive_display_prompt_card`
3. `shot01_result_diff_opening`
4. `shot06_cause_turning_point`
5. `shot08_prompt_architecture_card`
6. `shot15_result_diff_card`
7. `shot16_low_pressure_ending`
8. `shot03_problem_hook_sassy_card`
9. `shot05_negative_reversal_sassy_card`
10. `shot14_positive_reversal_sassy_card`

每个 segment 必须包含：

- `segment_id`
- `card_type`
- `assigned_route`
- `primary_reference`
- `secondary_reference`
- `forbidden_references`
- `renderer_function`
- `validation_gate`
- `can_share_shell_with`
- `must_not_share_shell_with`

## 5. blocked 条件

- `blocked_route_map_missing（阻塞：视觉路由表缺失）`：未生成 `visual_route_map.json`。
- `blocked_sassy_route_misassigned（阻塞：骚萌卡路由错误）`：任意骚萌卡使用 `cute_prompt_card_route` 或 `cute_info_card_route`。
- `blocked_info_card_route_misassigned（阻塞：信息卡路由错误）`：任意信息卡使用 `sassy_reaction_card_route`。
- `blocked_prompt_card_route_misassigned（阻塞：段落提示卡路由错误）`：任意段落提示卡使用复杂信息卡路由且未重审。
- `blocked_pr7_b_reference_missing（阻塞：PR #7 B 参考图缺失）`：读不到 PR #7 B 原始文件或证据路径。
- `blocked_pr7_a_fallback_forbidden（阻塞：禁止回退 PR #7 A）`：PR #7 B 缺失时试图回退 PR #7 A。
- `blocked_visual_route_not_separated（阻塞：三条视觉路由未拆开）`：段落提示卡、信息卡、骚萌卡仍共用外壳。
- `blocked_hyperframes_new_route_forbidden（阻塞：禁止 HyperFrames 新增并列 route）`：HyperFrames 试图新增与 `cute_info_card_route` / `sassy_reaction_card_route` 并列的新视觉路由。
- `blocked_hyperframes_middle_recording_default_forbidden（阻塞：禁止 HyperFrames 默认进入中段录屏范围）`：HyperFrames 试图把用户录制素材、反面录屏、正面录屏、录屏证据段、录屏叠层或录屏包装框纳入默认接入范围。

## 6. 一句话规则

**当前视频基线是 v3.1；后续任何生成 / 修改 / 技术升级前，必须先读取或输出并验证 `visual_route_map.json（视觉路由表）`；route map 通过前不得生成或修改全片；PR #7 B 是后续骚萌反应卡唯一执行参考，PR #7 A 只能作为历史 / candidate 对照；段落提示卡走可爱段落提示卡路由，信息卡走可爱信息卡路由，三者不得共用外壳；HyperFrames 当前只作为三类卡片的 `card_motion_layer`，不得新增视觉路由，不得把中段录屏纳入默认接入范围，不得替代云端剪辑或真实录屏证据。**
