# codex_source 总入口

## 1. 这份文件是什么

本文件是当前仓库的 Codex 执行层入口文件。

它用于回答 5 个最基础的问题：

- `codex_source/` 是干什么的
- 它和 `project_source/` 怎么分层
- 新任务进来时默认先读什么
- 发生冲突时按什么顺序裁决
- 什么情况下继续执行，什么情况下先停下汇报

当前还要额外帮 Codex 站稳一个执行事实：

- 当前默认主承载已不是 pure PPT / 信息卡全片承载
- 当前默认主线已切到“人物 + 用户真实录制素材 + 少量 PPT / 图片”
- 当前结构跟着文案走，不先预设整条视频的固定载体顺序
- 当前人物出现 1 次还是 2 次，是 block 路由结果，不是预设模板
- `AI talking avatar / 数字人口播` 当前不是默认主线
- 正式组装继续固定为北京区 `OSS + 云剪 cloud-only`
- 当前 AI 知识类内容还必须显式判断“看完后用户能做什么 / 能判断什么 / 证据是什么 / 最小行动或自检句是什么”
- AI 项目讲解、AI 方法分享、AI 学习实操、AI 案例拆解不再共用同一种价值交付和同一种结尾总结卡

它不是：

- 项目身份说明书
- 场景模式定义文件
- Perplexity 使用手册
- 回审模板正文
- 心理机制项目原则文件
- 代码实现说明书

这些内容分别属于 `project_source/`、代码层或更细的执行规则文件。

## 2. `codex_source/` 负责什么，不负责什么

### 负责什么

`codex_source/` 负责 Codex 的执行层规则，包括：

- 接到任务后的默认读取顺序
- 执行边界与停止线
- 运行事实与产物规则
- 验证要求
- 最终汇报口径

一句话：

`codex_source/` 负责“Codex 怎么稳定接手、怎么稳妥落地、怎么如实汇报”。

### 不负责什么

`codex_source/` 不负责定义：

- 这个项目是什么
- 当前阶段做什么、不做什么
- 内容边界
- 场景模式与结构原则
- Perplexity 的外层路由
- 回审模板正文
- 心理机制层项目原则

一句话：

这些属于 `project_source/` 的项目脑，不属于执行层。

## 3. `codex_source/` 与 `project_source/` 的分层关系

### `project_source/`

解决的是：

- 项目身份
- 当前阶段
- 内容边界
- 场景模式
- 结构原则
- Perplexity 高频接入
- 回审模板
- 心理机制项目规则

一句话：

`project_source/` 负责“这个项目是什么，内容怎么判断”。

### `codex_source/`

解决的是：

- Codex 先读什么
- 哪些任务能直接做，哪些要先审计
- 哪些文件能改，哪些不能改
- 当前运行链路怎么判断
- 最终结果如何验证和汇报

一句话：

`codex_source/` 负责“这个项目怎么执行、怎么落地、怎么验收”。

### 分层底线

- 不把 `project_source/` 写成执行说明书
- 不把 `codex_source/` 写成项目脑总结
- 执行前必须读取 `project_source/`
- 但 `project_source/` 不能被当成执行单正文

## 4. 新会话最小接手入口

新 Codex 会话进入当前仓库后，默认先读这 3 个文件：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`

这 3 个文件构成当前仓库的最小接手入口。

补充规则：

- 若任务明显偏执行规则，再补读 `codex_source/01_execution_rules.md`
- 若任务已经进入执行层落地，再默认补读：
  - `codex_source/02_current_execution_context.md`
  - 它用于写清当前阶段长期有效、但 Codex 不能默认知道的执行前上下文
- 若任务涉及外部结论、用户新拍板、Perplexity / ChatGPT 收束结果是否已进入执行层，再补读：
  - `codex_source/03_research_findings_bridge.md`
- 若任务涉及当前正式默认主线的职责分工、人物出现次数、真人与录屏如何按 block 路由理解，再补读：
  - `codex_source/02_current_execution_context.md`
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - 若当前仓库里的 `project_source` 文件名尚未同步到 `24_*`，以 `codex_log/latest.md` 与 `codex_source/03_research_findings_bridge.md` 的现口径为准
- 若任务涉及脚本写法、block 路由、结尾总结卡选择、样片是否值得进入执行、或样片验收，再补读：
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
- 若任务涉及“GPT 已知 / Codex 条件已知 / Codex 正式已知”的区分，再补读：
  - `codex_source/12_codex_known_state_three_layer_rules.md`
- 若任务涉及最终汇报、完成状态、失败说明或验收口径，再补读：
  - `codex_source/04_completion_and_review_contract.md`
- 若任务涉及执行现实与原方案不一致、资源 / 权限 / 环境 / 接口 / 成本 / 素材等偏差，再补读：
  - `codex_source/05_execution_deviation_and_reality_sync.md`
- 若任务明显偏项目判断或内容边界，再补读相关 `project_source/*`
- 若任务命中“正式版 API demo / 正式版目标态 / 云端组装 / 修正循环 / 质量达标反推”，则在默认入口之外补读：
  - `codex_source/07_formal_api_demo_target_plan.md`
  - 且必须明确：该文件定义的是正式版目标态，不是当前仓库已跑通事实
- 若任务命中协作方式调整、自动补全边界、是否进入执行或是否适合并行，则除默认入口外，再补读：
  - `project_source/07_collaboration_adaptation_rules.md`（若存在）
  - `codex_source/06_execution_gate_and_parallel_rules.md`
- 若任务涉及真实代码、测试或产物，再继续读对应代码、测试与现有产物
- 若任务依赖 skill，则进入实际执行前检查当前仓库本地 `skills/`；若本地没有相关 skill，再检查全局 `~/.codex/skills`
- 若仓库型任务已形成可判断小闭环，默认先更新 `codex_log/latest.md`，再 commit 并 push 当前分支，供 ChatGPT 复审

## 5. 任务冲突时的默认裁决顺序

当前仓库内发生规则冲突时，默认按以下顺序裁决：

1. 用户本轮明确任务与硬约束
2. 根目录 `AGENTS.md`
3. 已验证的真实仓库事实
   - 代码
   - 已存在文件
   - 真实产物
4. `project_source/`
   - 负责项目身份、阶段、边界、场景判断
5. `codex_source/`
   - 负责执行顺序、运行规则、验证口径
6. `README.md`
   - 作为快速说明，不高于已验证代码事实

进一步细化：

- 若 `README.md` 与真实代码或产物冲突，以真实仓库事实为准
- 若 `project_source/` 与代码运行事实冲突，运行文档必须以真实仓库事实为准，同时明确汇报冲突
- 若 `project_source/` 与 `codex_source/` 冲突：
  - 项目定位、阶段、内容边界，以 `project_source/` 为准
  - 读取顺序、执行边界、验证与汇报，以 `codex_source/` 为准

任何冲突都不能静默吞掉，必须显式写出。

## 6. 什么情况下可以继续执行

同时满足以下条件时，可以继续执行：

1. 当前任务边界清楚
2. 相关文件可读取
3. 已完成本地 / 全局 skill 检查
4. 当前任务属于明确层级
   - 项目脑
   - 执行层
   - 代码层
5. 不存在会影响动作选择的未解决冲突
6. 本轮动作在用户授权范围内

## 7. 什么情况下必须先停下汇报

出现以下任一情况，默认先停下汇报，而不是继续硬做：

1. 根目录 `AGENTS.md` 无法读取或缺失
2. 当前任务依赖的关键文件缺失、无法读取或无法确认真伪
3. 项目脑、执行层与真实仓库事实发生冲突，且冲突会影响本轮动作
4. 用户当前任务实质上在要求扩项目边界
   - 直播
   - 售卖
   - 获客
   - 增长
   - 商业包装
   - 大而全平台化
5. 本轮需要声称“已完成”或“已成功”，但缺少验证依据

补充说明：

- “没找到相关 skill”本身不一定构成停止条件
- 但必须在最终汇报中如实说明已检查、未命中、如何回退处理

## 8. 当前 `codex_source/` 已有哪些文件

### 审计 / 规划类

- `codex_source/00_current_repo_audit.md`
  - 当前仓库真实状态与最小闭环审计
- `codex_source/01_codex_source_plan.md`
  - 执行层建设规划
- `codex_source/01_missing_files_and_next_steps.md`
  - 缺失文件与下一步顺序
- `codex_source/02_codex_index.md`
  - 当前 Codex 文档导航

### 核心执行类

- `codex_source/00_codex_readme.md`
  - Codex 执行层总入口
- `codex_source/01_execution_rules.md`
  - 读取顺序、执行边界、skill 硬规则、汇报规则
- `codex_source/02_current_execution_context.md`
  - 当前阶段长期有效的执行前上下文
  - 用于防止 Codex 只靠聊天记忆开工
- `codex_source/03_research_findings_bridge.md`
  - Perplexity / ChatGPT / 用户新拍板与执行偏差升级的桥接文件
  - 不进本文件或本轮执行单的结论，Codex 不得假设已知
- `codex_source/04_completion_and_review_contract.md`
  - 执行后固定汇报格式与状态口径
  - 用于防止把建议、计划、分析写成完成
- `codex_source/05_execution_deviation_and_reality_sync.md`
  - 执行偏差分级、原方案改标与现实回写规则
  - 用于防止旧假设继续污染后续执行
- `codex_source/05_runtime_and_artifact_rules.md`
  - 当前最小闭环的真实输入、依赖、运行链路、产物与成功判定
- 说明：
  - 当前目录下同时存在两个 `05_*` 文件
  - `05_runtime_and_artifact_rules.md` 负责“运行事实”
  - `05_execution_deviation_and_reality_sync.md` 负责“现实偏差回写”
  - 两者不可互相替代
- `codex_source/06_execution_gate_and_parallel_rules.md`
  - 顶层收口闸门、自动补全边界与多 Codex 并行规则
- `codex_source/07_formal_api_demo_target_plan.md`
  - 正式版 API demo 的目标态执行计划
  - 用于定义目标标准、执行 Gate、修正循环与交接规则
- `codex_source/11_ai_knowledge_video_value_bridge.md`
  - GPT Project 新增价值底线、4 类内容交付差异、证据线与结尾卡映射的 codex 侧桥接文件
  - 用于防止后续 Codex 在脚本、路由、样片执行与验收时继续按旧口径误读项目
- `codex_source/12_codex_known_state_three_layer_rules.md`
  - GPT 已知 / Codex 条件已知 / 当前分支正式已知 / 主读取分支正式已知的分层规则
  - 用于防止把 bridge 摘要、当前分支状态和主读取分支状态混写
- `codex_source/10_codex_multi_agent_prompt_library.md`
  - 当前项目内的多 agent 执行模板库
  - 用于快速复用 `2 explorers + 1 integrator` 的执行 prompt
  - 不是当前仓库已跑通事实，当前真实运行事实仍以 `codex_source/05_runtime_and_artifact_rules.md` 为准

## 9. 当前最优先要遵守的执行原则

### 原则 1：先读再做

当前仓库已不适合靠聊天上下文裸奔执行。

### 原则 2：先分层再动手

先判断问题属于项目脑、执行层还是代码层，再决定改哪里。

### 原则 3：只围绕视频项目推进

当前阶段只做视频项目本身，不主动扩到直播、商业化、增长等方向。

进一步说，当前执行层服务的是“个人内部使用的 Prompt 驱动型视频工厂 / 视频内核”，不是前端页面或工作台优先项目。

### 原则 4：仓库事实高于想象

没读到、没确认、没验证的内容，不能写成已确认事实。

补充到外部结论与现实偏差：

- Perplexity / ChatGPT / 用户聊天里的结论不会自动同步进 Codex
- 必须通过 `codex_source/03_research_findings_bridge.md` 或本轮执行单显式带入
- 真实执行若已证明原方案不完整成立，必须按 `codex_source/05_execution_deviation_and_reality_sync.md` 回写并改标

补充到正式版 API demo 目标态：

- `codex_source/07_formal_api_demo_target_plan.md` 只能定义目标态
- 当前已确认仓库事实仍是本地 demo 运行链路
- 两者不得混写，更不得把目标态计划写成已跑通结论

补充到当前默认主线：

- 当前 Codex 执行层默认必须按“人物 + 用户真实录制素材 + 少量 PPT / 图片”理解项目
- 人物出现 1 次还是 2 次，是 block 路由结果，不是预设模板
- 中段主体默认优先交给真实录制素材承担
- pure PPT / 信息卡当前只保留为次级支路
- AI talking avatar / 数字人口播默认不再承担主承载

### 原则 5：有停线就停，不硬冲

只要冲突、缺文件或无法验证已经影响动作选择，就先汇报，不假装能继续。

### 原则 6：仓库型任务默认走 GitHub 审核线

凡是命中“仓库改动 / 文件修改 / 需要 PR 回审”的任务，默认流程不是直接改 `main`，而是：

先看现状 → 开分支改 → 提 PR → 跑 checks → AI 复审 → 用户拍板

补充边界：

- 这条线路只适用于仓库型任务
- 不适用于纯聊天判断、Perplexity prompt、单次小文本成品
- 若当前仓库尚未完成第一次 GitHub 基线同步，可把“当前仓库基线 + 本轮必要执行层改动”作为例外先推到 `main`
- 一旦基线建立，后续仓库改动默认不得直接 push `main`

## 10. 当前一句话入口

如果 Codex 这轮只记一句话：

**新会话默认先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`；当前默认主线按“人物 + 用户真实录制素材 + 少量 PPT / 图片”理解，结构跟着文案走、人物出现次数由 block 路由决定，`AI talking avatar` 不是默认主线，cloud assembly 继续是正式主路径；若任务偏执行规则，再补读 `codex_source/01_execution_rules.md`；命中仓库型任务默认走 GitHub / PR 线路，无法安全推进就先停下汇报。**

若任务偏正式版 API demo 目标态，则再补读 `codex_source/07_formal_api_demo_target_plan.md`，并同时回到 `codex_source/05_runtime_and_artifact_rules.md` 核对当前仓库已确认事实。
