# project_source 导航

## 1. 这套 project_source 的用途

`project_source/` 是当前仓库的项目脑目录。

它服务的对象是：

- ChatGPT
- 第二大脑层
- 项目总控层

当前这套项目脑服务的项目口径，应理解为：

- 个人内部使用
- Prompt 驱动协作
- Codex 可执行
- 视频内核优先
- 质量判断口径统一

而不是前端页面或工作台优先。

它负责解决的是：

- 这个项目到底是什么
- 当前阶段该优先做什么
- demo 的身份到底是什么
- 质量基线怎么定
- “抖音 90 分标准”该怎么理解
- 火山引擎 TTS 当前为什么是第一优先
- 展示路由该怎么分层判断
- Perplexity 怎么高频接入
- 回审怎么做
- 心理机制层怎么用

它不负责：

- 代码运行说明
- Codex 执行边界
- 文件修改权限
- 命令级操作说明
- 交付格式或执行单模板

这些内容属于 `codex_source/` 的执行层。

## 2. 每个文件解决什么问题

### `project_source/00_project_brief.md`

- 解决什么问题：
  - 项目定义是什么
  - 当前阶段是什么
  - demo 的真实身份是什么
  - 当前第一优先质量路线是什么
  - 当前不该再混淆什么

### `project_source/01_project_system_prompt.md`

- 解决什么问题：
  - ChatGPT 接手项目时应如何理解项目身份、边界、分工、默认工作流和质量判断口径

### `project_source/02_scene_mode_templates.md`

- 解决什么问题：
  - 不同视频场景分别适合讲什么、用什么结构
  - 给展示路由提供场景前置判断

### `project_source/03_perplexity_prompt_library.md`

- 解决什么问题：
  - 什么时候优先走 Perplexity
  - 走 Perplexity 时具体怎么问
  - 如何查询“90 分标准”“质量增强 API 优先级”“火山引擎 TTS”这类高频问题
  - 查回来之后怎么接回 ChatGPT

### `project_source/04_review_templates.md`

- 解决什么问题：
  - 内容、结构、画面、节奏、心理机制等各层如何回审
  - “抖音 90 分水位”如何作为项目内部质量简称落成 checklist

### `project_source/05_psychology_execution_rules.md`

- 解决什么问题：
  - 心理机制层为什么正式接入
  - 哪些机制适合常用、哪些需要谨慎
  - 怎么把机制落到标题、开头、结构、字幕、配音、画面和结尾

### `project_source/06_project_index.md`

- 解决什么问题：
  - 整套项目脑文件如何阅读、如何使用、如何与执行层分工

### `project_source/07_user_readable_repo_map.md`

- 解决什么问题：
  - 用户如何快速看懂仓库分层
  - 非技术视角下如何先判断问题落在哪一层

### `project_source/08_quality_baseline_and_90_score_rules.md`

- 解决什么问题：
  - 统一 demo 身份、质量基线、“抖音 90 分标准”和当前第一优先增强路线
  - 为 GPT 侧所有质量判断提供统一母版

### `project_source/10_formal_api_demo_current_route_patch_20260402.md`

- 解决什么问题：
  - 当前 `formal_api_demo` 默认主线的 assembly 路径是什么
  - 北京区 `OSS + 云剪工程` 为什么已经是唯一 assembly 主路径
  - 哪些旧的“pure PPT 默认主线 / local default / cloud optional / local fallback”口径已经失效

### `project_source/10_video_review_record_template.md`

- 解决什么问题：
  - 单条视频回审记录该怎么写
  - 如何把展示路由、切路由判断和下一轮动作正式落字段

### `project_source/13_stage_and_acceptance_gates.md`

- 解决什么问题：
  - 当前阶段有哪些闸门
  - 展示路由何时算过内容阶段闸门

### `project_source/14_content_review_and_loop_governance_rules.md`

- 解决什么问题：
  - 内容回审循环如何收口
  - 路由错误时下一轮如何切，不许怎么混改

### `project_source/16_presentation_routing_rules.md`

- 解决什么问题：
  - 展示路由的四层判断架构是什么
  - PPT / 真人 / 录屏 / 案例图 / 混合该怎么按 block 判断
  - 回退、回审和阶段边界怎么写死

### `project_source/17_white_collar_ppt_style_rules.md`

- 解决什么问题：
  - 当前 pure PPT / 信息卡次级支路该呈现什么气质
  - 默认视觉、文案、字幕、转场和页面结构该怎么落
  - 哪些低质信号当前必须明确禁止
  - “白领风是否成立”回审时该怎么看

### `project_source/19_human_self_footage_hybrid_mainline_rules.md`

- 解决什么问题：
  - 当前正式默认主线为什么改成“人物 + 自录素材 + 少量 PPT / 图片”
  - 三层职责分工是什么
  - AI talking avatar / 数字人口播为什么降级为非默认路线
  - 缺真实素材时当前仓库该如何诚实落到“待素材注入验证”

## 3. 建议阅读顺序

建议的标准阅读顺序：

1. `project_source/06_project_index.md`
2. `project_source/08_quality_baseline_and_90_score_rules.md`
3. `project_source/00_project_brief.md`
4. `project_source/01_project_system_prompt.md`
5. `project_source/02_scene_mode_templates.md`
6. `project_source/05_psychology_execution_rules.md`
7. `project_source/16_presentation_routing_rules.md`
8. `project_source/19_human_self_footage_hybrid_mainline_rules.md`
9. `project_source/17_white_collar_ppt_style_rules.md`
10. `project_source/04_review_templates.md`
11. `project_source/10_video_review_record_template.md`
12. `project_source/03_perplexity_prompt_library.md`
13. `project_source/07_user_readable_repo_map.md`

原因：

- 先看导航
- 再看质量基线总口径
- 再看项目定义与阶段
- 再看系统理解框架
- 再看场景、心理机制、展示路由、正式默认主线与 pure PPT 次级支路
- 再看回审模板与回审记录
- 最后看用户视角地图

## 4. ChatGPT 接手项目时应先读什么、再读什么

### 如果是第一次接手本项目

先读：

1. `project_source/06_project_index.md`
2. `project_source/08_quality_baseline_and_90_score_rules.md`
3. `project_source/00_project_brief.md`
4. `project_source/01_project_system_prompt.md`

再读：

5. `project_source/02_scene_mode_templates.md`
6. `project_source/05_psychology_execution_rules.md`
7. `project_source/16_presentation_routing_rules.md`
8. `project_source/19_human_self_footage_hybrid_mainline_rules.md`
9. `project_source/17_white_collar_ppt_style_rules.md`
10. `project_source/04_review_templates.md`
11. `project_source/10_video_review_record_template.md`
12. `project_source/03_perplexity_prompt_library.md`
13. `project_source/07_user_readable_repo_map.md`

### 如果当前任务命中“质量标准 / demo 身份 / 火山引擎 TTS 优先级”

默认优先读：

1. `project_source/00_project_brief.md`
2. `project_source/08_quality_baseline_and_90_score_rules.md`
3. `project_source/01_project_system_prompt.md`
4. `project_source/04_review_templates.md`

### 如果当前任务是“判断一条视频该怎么讲”

优先读：

1. `project_source/00_project_brief.md`
2. `project_source/02_scene_mode_templates.md`
3. `project_source/05_psychology_execution_rules.md`
4. `project_source/16_presentation_routing_rules.md`
5. `project_source/08_quality_baseline_and_90_score_rules.md`

### 如果当前任务是“判断该用 PPT、真人、录屏、案例图还是混合”

优先读：

1. `project_source/02_scene_mode_templates.md`
2. `project_source/05_psychology_execution_rules.md`
3. `project_source/16_presentation_routing_rules.md`
4. `project_source/04_review_templates.md`

### 如果当前任务是“纯 PPT 母版风格 / 信息卡视觉气质 / 字幕与转场克制规则”

优先读：

1. `project_source/17_white_collar_ppt_style_rules.md`
2. `project_source/16_presentation_routing_rules.md`
3. `project_source/05_psychology_execution_rules.md`
4. `project_source/04_review_templates.md`
5. `project_source/08_quality_baseline_and_90_score_rules.md`

### 如果当前任务是“纯 PPT 主线 assembly 默认走哪条 / OSS 与云剪现在算什么”

优先读：

1. `project_source/10_formal_api_demo_current_route_patch_20260402.md`
2. `project_source/01_project_system_prompt.md`
3. `project_source/08_quality_baseline_and_90_score_rules.md`
4. `project_source/17_white_collar_ppt_style_rules.md`

### 如果当前任务是“先做外部调研”

优先读：

1. `project_source/01_project_system_prompt.md`
2. `project_source/03_perplexity_prompt_library.md`
3. `project_source/08_quality_baseline_and_90_score_rules.md`

### 如果当前任务是“成片回审或脚本回审”

优先读：

1. `project_source/08_quality_baseline_and_90_score_rules.md`
2. `project_source/04_review_templates.md`
3. `project_source/10_video_review_record_template.md`
4. `project_source/16_presentation_routing_rules.md`
5. `project_source/01_project_system_prompt.md`
6. `project_source/05_psychology_execution_rules.md`

## 5. 用户什么时候该看哪个文件

### 想快速确认项目现在到底是什么

看：

- `project_source/00_project_brief.md`

### 想确认 ChatGPT 应该怎么理解这个项目

看：

- `project_source/01_project_system_prompt.md`

### 想判断某条内容属于哪个场景、该用什么结构

看：

- `project_source/02_scene_mode_templates.md`

### 想判断某条内容该用 PPT、真人、录屏、案例图还是混合

看：

- `project_source/16_presentation_routing_rules.md`

### 想确认当前纯 PPT 母版该做成什么气质、避开什么低质信号

看：

- `project_source/17_white_collar_ppt_style_rules.md`

### 想确认当前正式默认主线为什么改成“人物 + 自录素材 + 少量 PPT / 图片”

看：

- `project_source/19_human_self_footage_hybrid_mainline_rules.md`

### 想去 Perplexity 查资料、拿首稿、找表达参考

看：

- `project_source/03_perplexity_prompt_library.md`

### 想做脚本或成片回审

看：

- `project_source/04_review_templates.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/10_video_review_record_template.md`

### 想看心理机制层到底怎么用、有哪些边界

看：

- `project_source/05_psychology_execution_rules.md`

### 想先把 demo 身份、90 分标准和火山引擎 TTS 优先级一次看清

看：

- `project_source/08_quality_baseline_and_90_score_rules.md`

### 想确认当前正式默认主线现在走云剪还是本地兜底

看：

- `project_source/10_formal_api_demo_current_route_patch_20260402.md`

当前正式口径已经不是“pure PPT 默认主线”，而是“人物 + 自录素材 + 少量 PPT / 图片”为默认主承载，同时正式组装继续固定为“北京区 OSS + 云剪工程唯一主路径”；本地 assembly 已退出默认主线。

### 想知道整套项目脑文件怎么配合

看：

- `project_source/06_project_index.md`

## 6. 哪些内容属于项目脑，哪些内容后续会在执行层另建

### 属于项目脑的内容

- 项目身份
- 当前阶段
- demo 的真实身份
- 质量基线
- “抖音 90 分标准”的解释口径
- 火山引擎 TTS 的当前优先级
- 纯 PPT 主线的 assembly 默认路线
- 内容边界
- 场景模式
- 结构原则
- 展示路由规则
- Perplexity 接入原则
- 回审模板
- 回审记录模板
- 阶段与回审循环治理
- 心理机制规则
- 正式默认主线规则
- 白领向纯 PPT 母版风格规则
- 四方协作分工

### 后续会在执行层另建的内容

这些内容不在 `project_source/` 里展开，而应后续在 `codex_source/` 里处理：

- Codex 读取顺序
- Codex 执行边界
- 任务单模板
- 运行依赖与产物规则
- 交付与汇报规则
- 分支、日志、验证与 PR 流程

## 7. 当前一句话导航

如果你只记一句话：

`project_source/` 负责“这个项目是什么、质量怎么判断、展示路由怎么选、优先级怎么定”，而 `codex_source/` 负责“具体怎么执行、怎么落地、怎么交付”；当前命中展示路由任务时补读 `project_source/16_presentation_routing_rules.md`，命中纯 PPT 母版风格任务时补读 `project_source/17_white_collar_ppt_style_rules.md`，命中纯 PPT 主线 assembly 路径任务时补读 `project_source/10_formal_api_demo_current_route_patch_20260402.md`。
