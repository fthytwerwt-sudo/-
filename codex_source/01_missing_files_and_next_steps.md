# 缺失文件与下一步

## 说明

本文件只基于当前仓库真实状态编写。

- 已确认当前仓库没有 `project_source/`
- 已确认当前仓库有 `codex_source/`
- 下列文件均为“当前不存在、后续建议补齐”的目标文件
- 它们不是已存在文件，也不是本轮已读取文件

## 1. 当前缺失的 project_source 文件

当前 `project_source/` 整个目录都不存在。若后续要补项目脑层，建议优先考虑以下文件：

### `project_source/00_project_brief.md`

- 解决什么问题：项目到底是什么、当前阶段是什么、目标边界是什么

### `project_source/01_project_system_prompt.md`

- 解决什么问题：ChatGPT 或项目总控层应该如何理解这个项目

### `project_source/02_scene_mode_templates.md`

- 解决什么问题：不同视频场景模式的结构模板与适用边界

### `project_source/03_perplexity_prompt_library.md`

- 解决什么问题：外部信息检索时的高频提示词与调用方式

### `project_source/04_review_templates.md`

- 解决什么问题：内容回审、脚本回审、视频回审时用什么模板

### `project_source/05_psychology_execution_rules.md`

- 解决什么问题：内容表达和用户心理机制规则如何沉淀

### `project_source/06_project_index.md`

- 解决什么问题：项目脑层总导航，告诉上层先读什么再读什么

## 2. 当前缺失的 codex_source 文件

当前仓库虽然已有 `codex_source/`，但仍缺以下执行层文件：

### `codex_source/00_codex_readme.md`

- 解决什么问题：Codex 层是什么、和 `project_source` 有什么关系、当前执行目标是什么

### `codex_source/01_execution_rules.md`

- 解决什么问题：Codex 的执行边界、默认工作方式、哪些文件能改、哪些不能碰

### `codex_source/02_codex_task_templates.md`

- 解决什么问题：常见任务如何落单，例如仓库审计、案例视频生成、链路优化

### `codex_source/03_skill_integration_rules.md`

- 解决什么问题：什么时候用哪些 skill，什么时候不能混用 skill

### `codex_source/04_delivery_and_report_rules.md`

- 解决什么问题：完成任务后如何汇报、必须交代哪些内容

### `codex_source/05_runtime_and_artifact_rules.md`

- 解决什么问题：运行依赖、输入路径、输出路径、中间产物、清理规则、验证规则

## 3. 这些缺失文件的重要性判断

### 项目脑层最关键缺口

- 不是“模板库还没写完”
- 而是“项目脑根目录完全不存在”

最先要补的，是能让人和上层模型先对齐项目身份的文件。

### Codex 层最关键缺口

- 不是“任务模板数量不够”
- 而是“Codex 还没有稳定的本地接手规则”

最先要补的，是入口、执行边界、运行规则。

## 4. 下一轮最合理先建哪 2-3 个文件

### 方案一：先补最小可用分层

1. `project_source/00_project_brief.md`
   - 原因：当前项目脑层是空的，先把项目身份、目标边界、当前阶段立住

2. `codex_source/00_codex_readme.md`
   - 原因：让 Codex 层有自己的总入口，不再只靠聊天上下文

3. `codex_source/01_execution_rules.md`
   - 原因：先明确执行边界，避免后续继续混写项目脑、执行层和代码层

### 如果下一轮更偏执行落地

可以把第 3 个文件替换为：

- `codex_source/05_runtime_and_artifact_rules.md`
  - 原因：当前最小闭环已经跑通，最值得沉淀的是运行与产物规则

## 5. 推荐顺序结论

如果只选 3 个，我建议下一轮优先建：

1. `project_source/00_project_brief.md`
2. `codex_source/00_codex_readme.md`
3. `codex_source/01_execution_rules.md`

原因很简单：

- 第一个先补“项目是谁”
- 第二个先补“Codex 层是什么”
- 第三个再补“Codex 怎么做事”

在这 3 个文件补完之前，继续扩任务模板或复杂场景模板，收益都不如先把分层立住。
