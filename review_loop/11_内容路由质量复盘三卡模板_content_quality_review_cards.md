# 内容路由质量复盘三卡模板 content quality review cards

## 1. 文件定位

本文件是《视频工厂》后续视频 / 文案 / 复盘任务的三张机制卡模板。

三张卡用于执行前判断，不是视频镜头脚本，也不是最终内容复审结论。

本文件包含：

1. `content_route_card（内容路由卡）`
2. `quality_lock_card（质量锁卡）`
3. `review_variable_card（复盘变量卡）`

通用边界：

- 三张卡用于说明目标、质量底线和反馈变量。
- 三张卡不能替代 ChatGPT / 用户的最终判断。
- 三张卡不能把 `technical_validation（技术验证）` 写成 `content_validation（内容验证）`。
- 三张卡不能把 `fallback_local_only（本地兜底）` 写成 DeepSeek 结论。

## 2. content_route_card（内容路由卡）

### 2.1 字段

```markdown
## content_route_card（内容路由卡）

- content_type（内容类型）：
- validation_goal（本轮验证目标）：
- core_evidence（核心证据）：
- middle_carrier（中段主体承载）：
- api_human_usage（API 生成真人使用方式）：1 次 / 2 次 / 不确定待判断
- ppt_usage（少量 PPT 使用方式）：
- prompt_tail_card_usage（Prompt 引用尾卡是否使用）：
- reference_inheritance（继承哪些质量点）：
- flow_flex_reason（为什么本条不照搬旧流程）：
- platform_risk_note（平台风险提示）：
```

### 2.2 填写说明

- `validation_goal` 必须写清这条内容验证什么。
- `core_evidence` 必须能回到真实素材、截图、结果差或平台数据。
- `api_human_usage` 只能按文案目标和素材证据判断，不先预设次数。
- `reference_inheritance` 只写质量点、风格边界、展示边界，不写旧镜头流程照搬。
- `flow_flex_reason` 必须说明结构变化的依据。

### 2.3 不能写成什么

- 不能写成先定人物段、卡片数、PPT 数，再倒塞文案。
- 不能写成已有 reference 就自动沿用旧镜头流程。
- 不能写成不看素材证据也能进入执行。

### 2.4 完成标准

- 已说明本轮验证目标。
- 已说明中段由什么承担主体证据。
- 已说明继承哪些质量点，不继承哪些旧流程。
- 已说明平台风险是否需要发布前检查。

### 2.5 blocked 条件

- 缺 `validation_goal`。
- 缺 `core_evidence`。
- 无法说明 `flow_flex_reason`。
- 必须修改禁止文件或状态字段才能继续。

## 3. quality_lock_card（质量锁卡）

### 3.1 字段

```markdown
## quality_lock_card（质量锁卡）

- viewer_takeaway（用户看完能拿走什么）：
- proof_type（证明类型）：真实录屏 / 前后对比 / 步骤截图 / 结果截图 / 平台数据
- result_diff（结果差）：
- minimum_action（最小行动）：
- voice_quality_line（声音质量底线）：
- host_role_line（主持壳职责底线）：
- ppt_density_line（PPT 密度底线）：
- reference_quality_points（继承的 reference 质量点）：
- one_vote_fail_items（一票否决项）：
- not_validated_yet（仍未验证项）：
```

### 3.2 填写说明

- `viewer_takeaway` 写观众能拿走的具体判断或动作。
- `proof_type` 必须有对应证据，不够就写 `待验证`。
- `result_diff` 写前后变化，不写泛泛价值。
- `one_vote_fail_items` 要能阻止进入成片执行。
- `not_validated_yet` 必须保留声音、动作、平台反馈等未验证项。

### 3.3 不能写成什么

- 不能写成质量锁卡通过就等于内容通过。
- 不能写成技术生成成功就等于质量过线。
- 不能写成旧 reference 已存在就自动继承全部流程。

### 3.4 完成标准

- 已写清用户收获、证明类型、结果差和最小行动。
- 已列出声音、主持壳、PPT 密度和 reference 质量点。
- 已列出一票否决项和仍未验证项。

### 3.5 blocked 条件

- 没有真实证据支撑核心价值。
- 存在一票否决项。
- 把 `technical_validation` 写成 `content_validation`。
- 把候选 reference 写成 locked reference。

## 4. review_variable_card（复盘变量卡）

### 4.1 字段

```markdown
## review_variable_card（复盘变量卡）

- video_id（视频编号）：
- publish_window（观察窗口）：24h / 72h / 7d
- main_variable（本轮主变量）：选题 / 开头 / 文案结构 / 中段证据 / 声音 / 卡片 / 标题封面 / 平台包装
- controlled_variables（尽量保持不变的变量）：
- target_signal（目标信号）：播放 / 完播 / 收藏 / 评论 / 私信 / 咨询
- failure_interpretation（失败说明什么）：
- success_interpretation（成功说明什么）：
- next_round_rule（下一轮怎么只改一个变量）：
```

### 4.2 填写说明

- `main_variable` 只选一个主变量。
- `controlled_variables` 写本轮尽量不变的部分。
- `target_signal` 写具体观察信号。
- `failure_interpretation` 和 `success_interpretation` 只能围绕主变量解释。
- `next_round_rule` 必须能直接进入下一轮任务草稿。

### 4.3 不能写成什么

- 不能写成数据记录越多，结论越确定。
- 不能写成多个变量一起改后还能单因果归因。
- 不能写成异常样本已经证明正常规律。

### 4.4 完成标准

- 已分清视频编号和观察窗口。
- 已锁定一个主变量。
- 已列出保持不变项。
- 已写清目标信号。
- 已写清下一轮只改一个变量的规则。

### 4.5 blocked 条件

- 缺 `video_id`。
- 缺 `publish_window`。
- 缺 `main_variable`。
- 上一轮同时改了多个变量却试图下单因果结论。
- 样本异常但未标记异常。

## 5. 一句话规则

三张卡的作用是让《视频工厂》先判断“这次验证什么、质量底线是什么、复盘只看哪个变量”，再决定视频和文案承载方式；它们不证明机制已经稳定，也不证明任一视频内容已通过。
