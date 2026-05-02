# v3.1 视觉路由规则 v31 visual routing rules

## 1. 文件定位

本文件是《视频工厂》v3.1 之前必须读取的视觉路由前置规则。

它只规定后续生成前的 routing gate（路由门）和 reference inheritance（参考继承），不代表本轮已经生成 v3.1，不代表视觉母版已锁定，也不代表内容验证通过。

## 2. v3 用户复审后的硬边界

- `已确认` v3 技术层只能写为 `v3_technical_milestone = reached_for_current_stage（当前阶段技术里程碑达成）`。
- `已确认` v3 技术线未锁定，必须保持 `technical_line_locked = false（技术线未锁定）`。
- `已确认` v3 技术线没有最终锁死，必须保持 `technical_baseline_locked = false（技术基线未锁定）`。
- `已确认` 下一步仍需要 `technical_upgrade_next = true（技术升级）`。
- `已确认` v3 内容未过线，主要问题在 GPT 文案侧，必须写 `content_validation = not_passed_user_review_gpt_copywriting_side（用户复审未过线，主要在 GPT 文案侧）`。
- `已确认` `send_ready = false（不可发送）`。
- `已确认` `visual_master_locked = false（视觉母版未锁定）`。

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

## 4. v3.1 生成前置 gate

后续任何 v3.1 生成任务必须先输出：

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

## 6. 一句话规则

**下一轮 v3.1 生成前，必须先输出并验证 `visual_route_map.json（视觉路由表）`；route map 通过前不得生成全片；PR #7 B 是骚萌反应卡执行参考，段落提示卡走可爱段落提示卡路由，信息卡走可爱信息卡路由，三者不得共用外壳。**
