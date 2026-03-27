# project_source 导航

## 1. 这套 project_source 的用途

`project_source/` 是当前仓库的项目脑目录。

它服务的对象是：

- ChatGPT
- 第二大脑层
- 项目总控层

它负责解决的是：

- 这个项目到底是什么
- 当前阶段该优先做什么
- 内容边界在哪里
- 场景怎么分
- Perplexity 怎么高频接入
- 回审怎么做
- 心理机制层怎么用

它不负责：

- 代码运行说明
- Codex 执行边界
- 文件修改权限
- 命令级操作说明
- 交付格式或执行单模板

这些内容后续属于 `codex_source/` 的执行层。

## 2. 每个文件解决什么问题

### `project_source/00_project_brief.md`

- 解决什么问题：
  - 项目定义是什么
  - 当前阶段是什么
  - 现在明确做什么、不做什么
  - 当前最小技术闭环事实是什么

### `project_source/01_project_system_prompt.md`

- 解决什么问题：
  - ChatGPT 接手项目时应如何理解项目身份、边界、分工、默认工作流和停止线

### `project_source/02_scene_mode_templates.md`

- 解决什么问题：
  - 不同视频场景分别适合讲什么、用什么结构、用什么表现方式

### `project_source/03_perplexity_prompt_library.md`

- 解决什么问题：
  - 什么时候优先走 Perplexity
  - 走 Perplexity 时具体怎么问
  - 查回来之后怎么接回 ChatGPT

### `project_source/04_review_templates.md`

- 解决什么问题：
  - 内容、结构、画面、节奏、心理机制等各层如何回审

### `project_source/05_psychology_execution_rules.md`

- 解决什么问题：
  - 心理机制层为什么正式接入
  - 哪些机制适合常用、哪些需要谨慎
  - 怎么把机制落到标题、开头、结构、字幕、配音、画面和结尾

### `project_source/06_project_index.md`

- 解决什么问题：
  - 整套项目脑文件如何阅读、如何使用、如何与后续执行层分工

## 3. 建议阅读顺序

建议的标准阅读顺序：

1. `project_source/06_project_index.md`
2. `project_source/00_project_brief.md`
3. `project_source/01_project_system_prompt.md`
4. `project_source/02_scene_mode_templates.md`
5. `project_source/03_perplexity_prompt_library.md`
6. `project_source/05_psychology_execution_rules.md`
7. `project_source/04_review_templates.md`

原因：

- 先看导航
- 再看项目定义与阶段
- 再看系统理解框架
- 再看场景与外部扩展
- 再看心理机制层
- 最后看回审模板

## 4. ChatGPT 接手项目时应先读什么、再读什么

### 如果是第一次接手本项目

先读：

1. `project_source/06_project_index.md`
2. `project_source/00_project_brief.md`
3. `project_source/01_project_system_prompt.md`

再读：

4. `project_source/02_scene_mode_templates.md`
5. `project_source/03_perplexity_prompt_library.md`
6. `project_source/05_psychology_execution_rules.md`
7. `project_source/04_review_templates.md`

### 如果当前任务是“判断一条视频该怎么讲”

优先读：

1. `project_source/00_project_brief.md`
2. `project_source/02_scene_mode_templates.md`
3. `project_source/05_psychology_execution_rules.md`

### 如果当前任务是“先做外部调研”

优先读：

1. `project_source/01_project_system_prompt.md`
2. `project_source/03_perplexity_prompt_library.md`

### 如果当前任务是“成片回审或脚本回审”

优先读：

1. `project_source/01_project_system_prompt.md`
2. `project_source/04_review_templates.md`
3. `project_source/05_psychology_execution_rules.md`

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

### 想去 Perplexity 查资料、拿首稿、找表达参考

看：

- `project_source/03_perplexity_prompt_library.md`

### 想做脚本或成片回审

看：

- `project_source/04_review_templates.md`

### 想看心理机制层到底怎么用、有哪些边界

看：

- `project_source/05_psychology_execution_rules.md`

### 想知道整套项目脑文件怎么配合

看：

- `project_source/06_project_index.md`

## 6. 哪些内容属于项目脑，哪些内容后续会在执行层另建

### 属于项目脑的内容

- 项目身份
- 当前阶段
- 内容边界
- 场景模式
- 结构原则
- Perplexity 接入原则
- 回审模板
- 心理机制规则
- 四方协作分工

### 后续会在执行层另建的内容

这些内容不在 `project_source/` 里展开，而应后续在 `codex_source/` 里处理：

- Codex 读取顺序
- Codex 执行边界
- 任务单模板
- skill 接入规则的执行面
- 运行依赖与产物规则
- 交付与汇报规则

## 7. 当前一句话导航

如果你只记一句话：

`project_source/` 负责“这个项目是什么、为什么这样做、内容怎么判断”，而 `codex_source/` 未来负责“具体怎么执行、怎么落地、怎么交付”。

这两层必须分开，不能混写。
