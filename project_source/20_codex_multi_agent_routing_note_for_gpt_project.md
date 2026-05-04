# 20｜Codex 执行车道与并发路由说明（给 GPT Project 用）

## 1. 文件定位

本文件放进 **GPT Project 数据源**，只负责做一层短路由说明。

它回答 5 个问题：

1. 当前这轮更适合 `fast_lane`、`standard_lane` 还是 `audit_lane`
2. 什么时候可以并发，什么时候必须保持串行
3. 允许并发时，最稳的并发结构是什么
4. ChatGPT 命中这类任务时，默认该输出什么
5. 完整执行规则和模板正文应该去哪里读

它不负责：

- 完整执行模板正文
- Codex 执行层细则全文
- 项目脑正式事实
- 当前具体样片或代码任务的完整执行单

一句话：

**本文件只负责让 GPT Project 知道“这轮该走哪条执行车道、能不能并发、该把 Codex 路由成什么结构”，不负责替代 Codex 执行层正文。**

---

## 2. 先判 lane（执行车道），再判 parallel（并发）

默认顺序必须是：

1. 先判当前任务该走哪条 `lane`
2. 再判当前任务能不能 `parallel`

不要反过来。

原因很简单：

- 如果连这轮该不该快、该不该先审计都没判清
- 直接上并发，只会更快放大跑偏风险

---

## 2A. GPT Project 侧 large_task_gate 触发提醒

ChatGPT / GPT Project 发现以下任一情况时，应提醒 Codex 在 `route_decision（路由判断）` 阶段进入 `large_task_gate（大任务闸门）`：

1. 视频、样片、成片、剪辑对象或复审对象超过 `3 分钟 / 180 秒`。
2. 任务明显是长视频、大信息量、多文件、多步骤、多验证或多模块任务。
3. 用户明确提到“长视频”“大任务”“多文件”“多步骤”“多 agent”“并发”“提速”“检查很多文件”。
4. 任务需要先做大量只读审计、定位、结构化整理，再统一写入。

ChatGPT 不必每次替 Codex 指定是否多 agent，但必须在 prompt 中提醒大任务触发 lane / parallel 判断。

最终 lane / parallel 判断由 Codex 按 `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）` 执行。

触发 `large_task_gate（大任务闸门）` 不等于默认并发；如果写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定，Codex 仍应保持或降级为 `serial_only（串行执行）`。

---

## 3. 当前默认 3 条 lane

### 3.1 `fast_lane`

只在以下同时成立时才建议：

- 当前对象已固定
- 当前正式状态已固定
- 当前唯一最高优先级 blocker 已固定
- 当前验收目标已固定
- 本轮只改单条内容 / 单个对象 / 单个局部任务
- 不改 `project_source/*`
- 不涉及跨多层 provider / runtime / 配置层重新验证
- 轻量证据包足以支撑判断
- 当前聊天与仓库状态没有明显冲突

默认动作：

- 少解释，直接执行
- 优先压缩读取 / 对齐 / 下发时间
- 条件失效就立刻降级

### 3.2 `standard_lane`

这是当前项目的默认执行车道。

适合：

- 目标和边界已经基本锁定
- 但还不能把它当成低风险快车道
- 仍需要正常读取、正常验证、正常日志回写
- 当前任务虽然聚焦，但仍可能触到样片输出、运行链路、局部验证或 `local_only` 重证据

默认动作：

- 先读固定入口
- 再按已锁定目标执行
- 过程正常验证
- 不为了显得快而跳过核对

### 3.3 `audit_lane`

命中以下任一情况时优先建议：

- 当前对象指针未刷新或已过期
- 当前 blocker 不止一个
- 当前状态仍严重依赖本地重证据才能判断
- 本轮会碰 `project_source/*`
- 本轮其实还在重判“这是规则问题还是内容问题”
- 当前聊天说法与仓库状态可能冲突
- 本轮虽然改一个对象，但实际牵涉 provider / runtime / 配置层风险

默认动作：

- 先审计
- 先分层结论
- 先判断是否允许进入执行
- 不急着提速

---

## 4. `fast_lane` 不是默认无条件可用

这条必须明确写给 GPT：

- `fast_lane` 只是一个条件成立时的提速车道
- 不是默认总开
- 不是“只要任务看起来小就自动走”

只要出现以下任一情况，就不要给 `fast_lane`：

- 指针可能过期
- blocker 未收口
- 当前状态还依赖大量本地重证据
- 本轮要动 `project_source/*`
- 这轮其实还没收清边界
- 这轮会把 provider / runtime 风险一起带进来

这时默认降级到：

- `standard_lane`
- 或 `audit_lane`

---

## 5. 先判能不能并发，再判并发结构

并发只在以下同时成立时才建议：

- 当前对象 / 目标 / 验收都已锁定
- 子任务之间可以清楚拆分
- 多个子任务不会同时写同一批核心文件
- 多个子任务不会共享同一高风险输出路径
- 当前慢点主要在读取 / 定位 / 结构化整理，而不是判断本身
- 当前不是项目边界重判任务

只要以下任一项成立，就默认不要并发：

- 同时改同一个 `project_source/*`
- 同时改同一个 `codex_source/*`
- 同时改同一条样片 / 同一份成片输出
- 当前对象还没锁定
- 当前 blocker 还没锁定
- 当前任务慢在判断，不慢在执行
- 当前会牵连 provider / runtime / 配置层风险

---

## 6. 当前默认 4 种 parallel mode

### `serial_only`

默认保守值。

适合：

- 当前任务会写同一批核心文件
- 当前任务会写同一条样片 / 同一份输出
- 风险主要在执行和验证，不在读取

### `read_parallel`

只读并发。

适合：

- 主要慢在读入口、读规则、读日志、读现状
- 多条读取线能并行
- 最终仍由单点整合

### `explore_plus_integrate`

当前项目里最常用的并发结构。

等价于：

- `2 explorers + 1 integrator`

适合：

- 并行压缩“读现状 / 找规则 / 收束改法”的时间
- explorers 只读
- integrator 独占写权

### `true_multi_task_parallel`

真正多任务并发。

只在以下成立时才建议：

- 多个子任务彼此独立
- 写入范围清楚且不冲突
- 可各自验收再汇总

---

## 7. ChatGPT 命中时默认输出什么

以后命中这类任务时，ChatGPT 默认输出至少应包含：

1. `lane_recommendation`
2. `lane_reason`
3. `lane_invalid_if`
4. `parallel_recommendation`
5. `parallel_reason`
6. `parallel_invalid_if`
7. 最省时且不增风险的执行结构
8. 一份可直接给 Codex 的 prompt

必须同时明确：

- 多 agent 只是并发结构之一
- 不是所有提速都靠多 agent
- 提速只提升读取 / 对齐 / 下发时间
- 不承诺 runtime 一定更快

---

## 8. 完整正文放哪里

GPT Project 只放短路由说明。

完整 lane / parallel 规则与 prompt skeleton 正文，统一看：

- `codex_source/13_execution_lane_and_parallel_rules.md`

当前项目已有的多 agent 模板库继续保留在：

- `codex_source/10_codex_multi_agent_prompt_library.md`

也就是说：

- 本文件负责“先选车道、再选并发结构”
- `13` 负责完整规则
- `10` 负责项目内多 agent 模板库

---

## 9. 当前一句话规则

**先判 lane，再判 parallel；满足条件才提速，满足条件才并发，条件失效就降级；当前项目最常用的并发结构仍是 `explore_plus_integrate`，但只有在读取真的比落地更慢、且写入权能单点收束时才建议启用。**
