# Codex 多 Agent 执行模板库

## 1. 文件定位

本文件用于把《视频工厂》当前明确采用的 Codex 多 agent 执行方式，正式写成项目内可复用模板库。

它负责解决：

- 什么时候值得用多 agent 提速
- 当前项目默认该怎么分工
- 为什么当前默认不是“多个 agent 一起改文件”
- 后续要给 Codex 下多 agent 任务时，可以直接复制什么模板

它不负责：

- 改项目主线
- 替 ChatGPT 拍板项目结论
- 代替代码、测试或 case 本身
- 扩写成大而全 agent 框架

一句话：

本文件是《视频工厂》当前执行层的多 agent 模板库，核心模式固定为 `2 个 explorers 并行只读 + 1 个 integrator 统一落地`。

## 2. 适用场景

当前更适合用本文件的情况：

- 任务已经收口，剩下主要是 Codex 执行问题，不是继续拍板问题
- 读仓库、找规则、找现状、找验收口径这部分时间明显大于真正落文件时间
- 任务边界明确，但上下文分散在 `AGENTS.md`、`codex_source/*`、`codex_log/*`、代码、产物和全局 skill 里
- 需要把“读清楚现状”和“真正落地执行”拆开
- 本轮允许的最终写文件范围清楚，且不希望多个 agent 同时改核心文件

当前不适合的情况：

- 任务仍在摇摆，还需要 ChatGPT / 用户继续拍板方向
- 任务非常小，一个 agent 直接做更快
- 任务强耦合，两个 explorers 也拆不出独立读线
- 希望多个 agent 同时改同一批核心文件
- 任务本质上是 `team` / 多工位外部并行，而不是 Codex 内部多 agent

## 3. 为什么这套结构最适合当前项目

《视频工厂》当前默认分工已经明确：

- ChatGPT 负责：
  - 判断
  - 纠偏
  - 收口
  - 定下一轮最该改什么
- Codex 负责：
  - 执行
  - 记录
  - 初检
  - 归档
  - 生成执行单草稿

因此当前项目里，多 agent 的主要价值不是“并行写文件”，而是并行压缩以下时间：

- 读仓库
- 找规则
- 找现状
- 找验收口径
- 找与当前任务最相关的执行边界

当前之所以固定采用 `2 explorers + 1 integrator`，原因是：

1. explorers 只读，更适合快速探路，不会把执行层和判断层混掉
2. integrator 独占写权限，更适合保护 `codex_source/*`、`codex_log/*` 这类核心文件
3. 当前项目里最常见的慢点不是“写不动”，而是“读不全、找不准、边界没踩稳”
4. 这套结构天然符合当前项目的真实协作关系：
   - ChatGPT 已收口
   - Codex 进入已确认边界内执行
   - explorers 帮 integrator 更快拿齐上下文

## 4. 默认多 Agent 结构：2 Explorers + 1 Integrator

### Explorer A

- 默认职责：
  - 读规则
  - 读导航
  - 读与当前任务最相关的仓库文档
  - 归纳“必须遵守项 / 禁止项 / 验收项”
- 默认只读：
  - 不改文件
  - 不开新结论
  - 不替项目拍板

### Explorer B

- 默认职责：
  - 读现状
  - 读目标文件
  - 读相关代码 / 测试 / 产物 / 全局 skills
  - 归纳“已有内容 / 缺失内容 / 可复用内容 / 冲突点”
- 默认只读：
  - 不改文件
  - 不定项目方向
  - 不越权把外部参考写成已确认事实

### Integrator

- 默认职责：
  - 吸收两条 explorer 结果
  - 统一执行路径
  - 真正落文件
  - 运行最贴近本轮改动的验证
  - 更新 `codex_log/latest.md`
  - 命中条件时补完整日志
  - 按仓库规则 commit / push / PR
- 独占权限：
  - 只有 integrator 可以真正改仓库文件
  - 只有 integrator 可以决定最终提交哪些文件
  - 只有 integrator 可以汇总最终对用户的真实结果

## 5. 每个角色的职责边界

### Explorer 的硬边界

- 只读，不改文件
- 不拍板项目主线
- 不重判 ChatGPT 已收束结论
- 不把“建议判断”说成“已确认”
- 不绕开 integrator 私自决定最终执行方案

### Integrator 的硬边界

- 必须先吸收 explorer 结果，再决定是否真正落地
- 不允许把 explorer 的总结直接当成已验证事实
- 必须自己做最终 diff / 验证 / 日志 / Git 收尾
- 若 explorer 之间有冲突，必须在落地前显式化，而不是静默选边

## 6. 什么时候适合用多 Agent

- 需要同时读：
  - 仓库规则
  - 当前目标文件
  - 全局 skill
  - Git / PR / 日志状态
- 文档任务范围明确，但仓库上下文很多
- 代码任务边界明确，但要先并行读：
  - 现有实现
  - 测试
  - 错误输出
  - 执行规则
- 回审后已经有收束结论，只缺下一轮定向执行

## 7. 什么时候不适合用多 Agent

- 只改一个小文件，单 agent 更快
- 还在问“到底改什么”，而不是“怎么更快落地”
- 需要多个真实写手同时改同一批核心文件
- 需要 durable tmux worker / worktree / 长周期并行，这时更像 `team` 场景
- 任务本质是并行实现多个独立写入子任务，这时更接近 `parallel-feature-development` 或 `subagent-driven-development`

## 8. 可直接复用的 Prompt 模板

以下模板默认都采用同一底层结构：

- 2 个 explorers 并行只读探路
- 1 个 integrator 统一落地
- explorers 不改文件
- integrator 独占写文件权

### 8.1 仅读探索版

```text
【任务目标】
请用多 agent 方式做一次“只读探索”，目标是更快读清当前仓库里与本任务最相关的规则、现状和约束，但这轮不要改任何文件。

【最小必要背景】
- 项目：视频工厂：AI 垂类场景化视频内核
- ChatGPT 负责判断和收口，Codex 负责执行和记录
- 这轮不要求落文件，只要求把上下文读全、结论分层

【agent 分工】
- explorer A：
  - 只读规则、导航、执行边界
  - 输出：必须遵守项 / 禁止项 / 验收项
- explorer B：
  - 只读目标文件、相关现状、已有日志 / 代码 / 产物
  - 输出：已有内容 / 缺失内容 / 可复用内容 / 风险点
- integrator：
  - 不提前改文件
  - 汇总两边结果
  - 输出统一的“已确认 / 待验证 / 不建议假设”清单

【动作边界】
- explorer 只读，不改文件
- integrator 也不改文件
- 不重判项目主线
- 不把建议说成已确认

【读取范围】
1. `AGENTS.md`
2. `codex_log/latest.md`
3. `codex_source/00_codex_readme.md`
4. `codex_source/01_execution_rules.md`
5. `codex_source/02_current_execution_context.md`
6. 与本任务最相关的仓库文件
7. 如任务依赖 skills，再补读相关 `~/.codex/skills/*`

【执行顺序】
1. explorer A、B 并行只读
2. integrator 汇总冲突点和已确认点
3. 只输出结论，不落文件

【完成标准】
- 已把最相关规则、现状、边界、风险整理清楚
- 已明确哪些是已确认、哪些还待验证
- 没有任何文件被改动

【最终输出格式】
1. 已确认
2. 待验证
3. 不建议假设
4. 若进入下一轮执行，最该先改哪一层
```

### 8.2 文档 / 规则改动版

```text
【任务目标】
请按“2 explorers + 1 integrator”结构，完成一次仓库内文档 / 规则改动任务。目标是并行压缩读取时间，但只有 integrator 可以真正落文件。

【最小必要背景】
- 项目：视频工厂：AI 垂类场景化视频内核
- 当前这轮只处理文档、执行层、日志或模板类文件
- ChatGPT 已完成判断收口；Codex 只负责在已确认边界内落地

【agent 分工】
- explorer A：
  - 只读 `AGENTS.md`、`codex_source/*` 入口规则、分支同步规则
  - 输出：必须遵守项 / 不得误报项 / 日志要求
- explorer B：
  - 只读目标文件、同类文件、全局 skills 或已有模板
  - 输出：已有结构 / 可复用内容 / 重叠风险 / 缺口
- integrator：
  - 统一写目标文件
  - 更新 `codex_log/latest.md`
  - 命中条件时补完整日志
  - 做 diff 校验、commit、push

【动作边界】
- explorer 只读，不改文件
- explorer 不得拍板项目结论
- integrator 独占写权限
- 不顺手改 `project_source/*`、代码、case、测试，除非任务明确允许

【读取范围】
1. `AGENTS.md`
2. `codex_log/latest.md`
3. `codex_source/00_codex_readme.md`
4. `codex_source/01_execution_rules.md`
5. `codex_source/02_current_execution_context.md`
6. 若涉及 Git / PR / `latest.md`，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`
7. 目标文件与同类文件
8. 命中时补读相关 `~/.codex/skills/*`

【执行顺序】
1. explorer A、B 并行只读
2. integrator 先输出极简审计结论
3. integrator 按用户允许范围落文件
4. integrator 更新 `codex_log/latest.md`
5. 命中条件时补完整日志
6. integrator 做 `git diff --check`
7. 若有 Git 跟踪改动，按仓库规则 commit + push

【完成标准】
- 目标文档已真实落文件
- 状态标注清楚
- `codex_log/latest.md` 已更新
- 命中条件时日志已补
- Git 状态如实回报

【最终输出格式】
1. 审计结果
2. 实际新建 / 修改文件
3. 每个文件写入了什么
4. 哪些是已确认 / 建议判断 / 外部参考
5. 日志是否更新
6. Git 状态与同步锚点
```

### 8.3 代码执行版

```text
【任务目标】
请按“2 explorers + 1 integrator”结构完成一次代码执行任务。多 agent 的重点是并行读实现、测试、错误和规则；真正改代码的只有 integrator。

【最小必要背景】
- 项目：视频工厂：AI 垂类场景化视频内核
- 当前代码主线涉及脚本、配音、字幕、图片 / 视频生成、assembly、日志与验证
- 这轮目标已明确，不需要 ChatGPT 重新拍板项目方向

【agent 分工】
- explorer A：
  - 只读执行规则、运行契约、目标链路相关文档
  - 输出：执行边界 / 验证要求 / 不可越线项
- explorer B：
  - 只读代码、测试、报错、现有产物
  - 输出：问题位置 / 可复用实现 / 风险与回归点
- integrator：
  - 真正改代码
  - 运行最贴近本轮的测试 / lint / py_compile / diff check
  - 更新日志并收尾 Git

【动作边界】
- explorer 只读，不改代码
- explorer 不得直接给出“项目方向已变”这类结论
- integrator 独占写代码和写日志权限
- 不允许多个 agent 同时修改同一批核心代码文件

【读取范围】
1. `AGENTS.md`
2. `codex_log/latest.md`
3. `codex_source/00_codex_readme.md`
4. `codex_source/01_execution_rules.md`
5. `codex_source/02_current_execution_context.md`
6. 与当前链路最相关的 `codex_source/*`
7. 目标代码、测试、现有产物
8. 若涉及 Git / PR，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`

【执行顺序】
1. explorer A、B 并行读
2. integrator 汇总“问题点 / 约束 / 验收”
3. integrator 修改最小必要文件
4. integrator 运行最贴近本轮改动的验证
5. integrator 更新 `codex_log/latest.md`
6. 命中条件时补完整日志
7. integrator commit + push

【完成标准】
- 真正问题已落修
- 验证结果已真实执行并如实汇报
- 没有 explorer 越权改文件
- 日志与 Git 状态同步完成

【最终输出格式】
1. 根因
2. 实际改动
3. 实际验证
4. 结果分类
5. 剩余风险
6. Git 状态与同步锚点
```

### 8.4 回审后修改版

```text
【任务目标】
请按“2 explorers + 1 integrator”结构执行一次“回审后定向修改”。ChatGPT 或用户已经完成回审收束，这轮只负责把已收束结论稳地落到仓库或代码里。

【最小必要背景】
- 项目：视频工厂：AI 垂类场景化视频内核
- 当前默认分工是：ChatGPT 收口，Codex 落地
- 本轮不是重新判断方向，而是围绕“唯一最优先改点”执行

【agent 分工】
- explorer A：
  - 只读回审结论、桥接文件、执行规则
  - 输出：本轮唯一最优先改点 / 不要误改方向 / 验收口径
- explorer B：
  - 只读当前现状、目标文件、已有日志 / 产物 / 同类实现
  - 输出：本轮可直接修改的最小落点 / 与上一轮相比的缺口
- integrator：
  - 只按已收束结论落地
  - 不重判方向
  - 完成验证、日志和 Git 收尾

【动作边界】
- explorer 不拍板项目方向
- explorer 不得把外部参考直接写成长期已确认规律
- integrator 只改当前这一轮已允许的范围
- 不平均发力，不顺手扩改

【读取范围】
1. `AGENTS.md`
2. `codex_log/latest.md`
3. `codex_source/00_codex_readme.md`
4. `codex_source/01_execution_rules.md`
5. `codex_source/02_current_execution_context.md`
6. 与当前回审结论最相关的桥接文件 / 日志 / 目标文件
7. 命中时补读相关全局 skill

【执行顺序】
1. explorer A、B 并行只读
2. integrator 先列明：
   - 已确认改点
   - 禁止误改项
   - 最小落点
3. integrator 在允许范围内落修改
4. integrator 做最小必要验证
5. integrator 更新日志并收尾 Git

【完成标准】
- 本轮只围绕已收束的最高优先级改点执行
- 没有把回审再次扩回判断层
- 验收口径清楚
- 日志和 Git 状态完整

【最终输出格式】
1. 已确认改点
2. 实际落点
3. 禁止误改项
4. 验收结果
5. 剩余待验证点
6. Git 状态与同步锚点
```

## 9. 使用注意事项

- 先确认这轮是否真的适合并行读，再决定是否上多 agent
- explorers 的输出是“供 integrator 参考的只读勘探结果”，不是最终真相
- integrator 不能把 explorer 的任何一句话直接当成已验证结论
- 如果任务只改一个很小的文件，直接单 agent 更快
- 如果任务需要多个真实写手并行改不同文件，这不是本文件的主打法，应回到其他并行技能或外部多工位方案
- 任何时候都不要让 explorer 越权拍板项目结论

## 10. 一句话规则

当前项目里的多 agent，不是让多个 agent 一起改文件，而是让两个 explorers 并行把规则和现状读清，再由一个 integrator 独占写文件权、验证权和收尾权。
