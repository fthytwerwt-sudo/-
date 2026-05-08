# codex_source 建设计划

## 计划定位

这份文件只回答一件事：

- 后续为什么要单独建设 `codex_source/`
- 应该先建哪些 Codex 执行层文件
- 每个文件分别解决什么问题

它不是执行规则正文，也不是任务模板正文。

## A. 为什么要单独建 codex_source

### 1. `project_source` 和 `codex_source` 解决的是两种不同问题

`project_source` 的职责应该是：

- 项目身份
- 当前阶段
- 内容边界
- 场景模式
- 项目脑导航
- 上层策略、回审、心理机制

`codex_source` 的职责应该是：

- Codex 先读什么
- 本地仓库能改什么、不能改什么
- 任务怎么落单
- skill 在什么场景下用
- 运行依赖是什么
- 产物放哪里
- 最终怎么汇报

### 2. 为什么不能混写

如果把两层混在一起，会出现三个问题：

- 上层项目脑会被执行细节污染
  - 例如把目录路径、产物规则、运行依赖塞进项目定位文档
- 执行层会被抽象策略稀释
  - Codex 需要的是“现在该读什么、该产出什么”，不是大段愿景陈述
- 后续维护会失真
  - 你会越来越难分清“这是项目原则”还是“这是当前仓库约束”

### 3. Codex 需要、但 ChatGPT 项目脑不一定需要的文件类型

Codex 更需要这些类型的本地文档：

- 读取顺序
- 仓库边界
- 文件修改权限
- 输入输出约定
- 产物目录规范
- 任务单模板
- 交付汇报格式
- skill 使用边界
- 运行环境说明

这些信息属于执行层，不适合混进项目脑层。

## B. 后续建议建立的 codex_source 文件清单

以下是建议版目标结构。本轮不创建正文，只做规划。

### 1. 可选的根入口

- `AGENTS.md`
  - 仅当后续需要一个“仓库根入口”时再处理
  - 作用应是薄入口，而不是把所有规则都堆进去
  - 当前仓库已有一个 demo 向的 `AGENTS.md`，不建议下一轮立刻重写

### 2. `codex_source/` 建议文件

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_codex_task_templates.md`
- `codex_source/03_skill_integration_rules.md`
- `codex_source/04_delivery_and_report_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/06_codex_index.md`

说明：

- 启动期导航 `codex_source/02_codex_index.md` 已隔离到 `归档删除区_archive_delete_zone/旧入口隔离_legacy_entrypoint_quarantine/codex_source/02_codex_index.md`
- 若后续仍需要回看启动期导航，只能按历史参考读取，不得再作为当前默认入口
- 等后续文件补齐后，可以保留当前命名，也可以整体重排到上面的完整编号体系

## C. 每个未来文件分别解决什么问题

### `AGENTS.md`

- 解决：仓库根入口怎么把 Codex 导向正确阅读路径
- 边界：只做入口，不堆执行细节全文

### `codex_source/00_codex_readme.md`

- 解决：Codex 层是什么、和 `project_source` 什么关系、当前阶段要做什么
- 作用：成为 Codex 执行层的总说明

### `codex_source/01_execution_rules.md`

- 解决：执行边界、可改范围、禁改范围、默认工作方式
- 作用：把“怎么做任务”从聊天上下文变成本地规则

### `codex_source/02_codex_task_templates.md`

- 解决：常见任务如何落单
- 例如：
  - 审计任务
  - 新视频案例任务
  - 链路优化任务
  - 仅修文档任务

### `codex_source/03_skill_integration_rules.md`

- 解决：什么时候用哪个 skill，什么时候不能乱借 skill
- 作用：避免把写作 skill、执行 skill、调试 skill 混用

### `codex_source/04_delivery_and_report_rules.md`

- 解决：做完以后如何汇报、汇报必须包含什么
- 作用：统一结果说明、风险说明、待确认项说明

### `codex_source/05_runtime_and_artifact_rules.md`

- 解决：输入文件、输出路径、运行依赖、中间产物、清理规则、验证规则
- 作用：让 Codex 在运行链路时不需要每次重新猜

### `codex_source/06_codex_index.md`

- 解决：最终稳定导航
- 作用：告诉 Codex 收到任务后先读什么、再读什么

## D. 先后顺序

### 下一轮最优先建议先写的 3 个文件

1. `codex_source/00_codex_readme.md`
   - 原因：先把 Codex 层身份、作用、与项目脑的分层说清楚
   - 没有这份文件，后续其它规则容易失去总框架

2. `codex_source/01_execution_rules.md`
   - 原因：当前仓库最缺的就是“Codex 应如何接手”的本地规则
   - 这会直接决定后续任务是否稳定

3. `codex_source/05_runtime_and_artifact_rules.md`
   - 原因：当前最小闭环已存在，最需要被沉淀的是运行依赖、输入输出、产物和验证规则
   - 这份文件能把“demo 可跑”变成“Codex 可重复执行”

### 暂时可以后置的文件

- `codex_source/02_codex_task_templates.md`
  - 先等执行规则和运行规则稳定后再写模板，更不容易返工
- `codex_source/03_skill_integration_rules.md`
  - 重要，但不如执行边界和运行规则紧急
- `codex_source/04_delivery_and_report_rules.md`
  - 可以在前两层稳定后补
- 根入口 `AGENTS.md`
  - 当前不宜急着动，避免把现有 demo 规则和未来 Codex 入口混写

## E. 当前已知风险

### 1. 如果没有本地 AGENTS / 本地 skill，会有什么问题

当前事实是：

- 本地有 `AGENTS.md`
- 本地没有 `skills/` 和本地 skill

风险在于：

- Codex 执行方式容易继续依赖会话上下文，而不是依赖仓库内规则
- 每次换任务都要重新解释读取顺序与执行边界
- skill 选择可能持续漂移，难以形成本地稳定做法

### 2. 如果继续借父目录别的项目 AGENTS，会有什么污染风险

- 会把别的项目目标、风格、目录约定误带进当前仓库
- 会让当前仓库的真实现状被覆盖
- 会制造“本地明明没有的规则却被当作存在”的假象

这类污染对执行层最危险，因为它会直接导致：

- 读错文件
- 改错目录
- 建错结构
- 错判项目阶段

### 3. 如果 `project_source` 和 `codex_source` 不分层，会有什么理解混乱

- 项目脑会被路径、命令、工单格式污染
- 执行层会被愿景描述、场景抽象、心理机制规则稀释
- 最终两边都不够好用

更具体地说：

- ChatGPT 层会变得过重
- Codex 层会变得过虚
- 后续维护者很难判断“这是要执行的规则”还是“这是理解项目的背景”

## 计划结论

后续 `codex_source` 的建设顺序不该是“大而全模板化”，而应该是：

1. 先把 Codex 层身份立住
2. 再把执行边界立住
3. 再把运行与产物规则立住
4. 最后再补任务模板、skill 规则、汇报规则

这样做的好处是：

- 不会把 demo 仓库一下子扩成复杂平台
- 能先服务当前最需要的“Codex 接手”
- 也更符合当前仓库仍是最小闭环 demo 的真实阶段
