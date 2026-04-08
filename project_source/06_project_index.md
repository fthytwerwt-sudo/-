# project_source 导航

## 1. 目录用途

`project_source/` 是《视频工厂》的项目脑目录。

它负责：

- 项目身份
- 当前阶段
- 默认主线
- 展示路由
- 内容价值底线
- 选题 / 文案 / 结尾卡判断

它不负责：

- 代码实现
- 执行步骤
- Git / 分支 / 提交规则

这些属于 `codex_source/`。

## 2. 当前最关键文件

### `project_source/00_project_brief.md`

- 项目当前是什么
- 当前阶段是什么
- 当前默认主线是什么
- demo 当前身份是什么

### `project_source/01_project_system_prompt.md`

- ChatGPT 接手项目时应按什么默认理解项目
- GPT 数据源与仓库事实冲突时，谁优先

### `project_source/08_quality_baseline_and_90_score_rules.md`

- demo 身份
- 质量基线
- 质量闸门与样片交付规则

### `project_source/16_presentation_routing_rules.md`

- 展示路由的四层判断框架
- block 级路由与回退规则

### `project_source/17_white_collar_ppt_style_rules.md`

- pure PPT / 信息卡次级支路的风格与黑名单

### `project_source/21_topic_selection_and_copywriting_rules.md`

- 选题与文案进入样片前要先锁什么

### `project_source/22_copy_mode_routing_rules.md`

- 4 类内容为什么不能共用一种结构 / 证据 / 结尾卡

### `project_source/24_human_self_footage_light_ppt_routing_rules.md`

- 当前正式默认主线为什么切到“人物 + 自录素材 + 少量 PPT / 图片”
- 三类承载各自负责什么
- 人物出现 1 次还是 2 次为什么是 block 路由结果

### `project_source/25_ai_knowledge_video_value_rules.md`

- AI 知识类内容的价值底线是什么
- 什么样的内容不够格进样片

## 3. 建议阅读顺序

### 第一次接手本项目

1. `project_source/06_project_index.md`
2. `project_source/00_project_brief.md`
3. `project_source/01_project_system_prompt.md`
4. `project_source/16_presentation_routing_rules.md`
5. `project_source/24_human_self_footage_light_ppt_routing_rules.md`
6. `project_source/21_topic_selection_and_copywriting_rules.md`
7. `project_source/22_copy_mode_routing_rules.md`
8. `project_source/25_ai_knowledge_video_value_rules.md`
9. `project_source/08_quality_baseline_and_90_score_rules.md`
10. 命中 pure PPT 次级支路时，再补读 `project_source/17_white_collar_ppt_style_rules.md`

### 命中展示路由任务

优先读：

1. `project_source/16_presentation_routing_rules.md`
2. `project_source/24_human_self_footage_light_ppt_routing_rules.md`

### 命中选题 / 文案 / 价值判断任务

优先读：

1. `project_source/21_topic_selection_and_copywriting_rules.md`
2. `project_source/22_copy_mode_routing_rules.md`
3. `project_source/25_ai_knowledge_video_value_rules.md`

### 命中 pure PPT 次级支路任务

优先读：

1. `project_source/16_presentation_routing_rules.md`
2. `project_source/17_white_collar_ppt_style_rules.md`

## 4. 当前导航一句话

当前项目脑默认先按“人物 + 用户真实录制素材 + 少量 PPT / 图片”理解主线；命中展示路由看 `16 + 24`，命中价值 / 选题 / 文案看 `21 + 22 + 25`，命中 pure PPT 次级支路再看 `17`。
