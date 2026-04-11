# 执行车道与并发规则

## 1. 文件定位

本文件把《视频工厂》当前执行层的提速机制正式写成可执行规则。

它负责：

- 定义 `fast_lane` / `standard_lane` / `audit_lane`
- 定义 `serial_only` / `read_parallel` / `explore_plus_integrate` / `true_multi_task_parallel`
- 定义 lane 的触发条件、一票否决项、降级路径、失效条件
- 定义 parallel 的允许闸门、一票否决项、降级路径、失效条件
- 定义强制回报字段
- 提供 lane 和 parallel 的 prompt skeleton

它不负责：

- 项目脑正式事实
- 当前样片内容结论
- provider / runtime 运行契约
- 替用户或 ChatGPT 拍板项目方向

一句话：

**本文件解决的是“这轮该怎么快、能不能并发、快到什么程度、失效时怎么退”，不是“把任何任务都推成更激进的执行方式”。**

---

## 2. 当前总原则

本文件必须先写死 6 条：

1. 项目优先
2. 风险先行
3. 满足条件才提速
4. 条件失效就降级
5. 满足条件才并发
6. 提速 / 并发只提升读取 / 对齐 / 下发时间，不承诺 runtime 一定更快

更直白地说：

- `lane` 是节奏控制
- `parallel` 是结构控制
- 它们都不是“为了快而快”

---

## 3. 判定顺序

默认顺序固定如下：

1. 先判当前任务属于哪条 `lane`
2. 再判当前任务能不能 `parallel`
3. 若允许并发，再判适合哪一种 `parallel mode`
4. 过程中持续检查失效条件
5. 一旦失效，立刻降级

明确禁止：

- 先想并发，再补 lane
- 先假设 `fast_lane`，再补 veto
- 把“读起来很多”自动等于“适合并发”

---

## 4. Lane 定义总表

| lane | 适用情况 | 默认动作 | 默认风险姿态 |
| --- | --- | --- | --- |
| `fast_lane` | 当前对象、状态、blocker、验收都已固定，且本轮只做低分支数局部任务 | 快速读取固定入口后直接执行 | 保守提速 |
| `standard_lane` | 当前目标已基本锁定，但仍有样片输出、局部运行验证、`local_only` 重证据或局部链路风险 | 正常读取、正常验证、正常回写 | 默认执行 |
| `audit_lane` | 边界未锁、指针未新鲜、冲突未消、当前结论仍依赖重审 | 先审计再决定是否进入执行 | 风险最高、速度最低 |

---

## 5. `fast_lane`

### 5.1 Trigger Gate

只有以下全部成立，才允许推荐 `fast_lane`：

1. 当前对象已固定
2. 当前正式状态已固定
3. 当前唯一最高优先级 blocker 已固定
4. 当前验收目标已固定
5. 本轮只改单条内容 / 单个对象 / 单个局部任务
6. 不改 `project_source/*`
7. 不涉及跨多层 provider / runtime / 配置层重新验证
8. 轻量证据包足以支撑判断
9. 当前聊天与仓库状态没有明显冲突

### 5.2 Default Action

默认动作：

1. 读固定入口
2. 读当前对象指针
3. 只补本轮最小必要上下文
4. 直接落地
5. 做最贴近本轮的最小验证
6. 更新 `latest.md` / 指针 / dated log

### 5.3 Veto Conditions

出现以下任一项，`fast_lane` 立即否决：

- 当前对象指针未刷新或已过期
- 当前 blocker 不止一个
- 当前状态仍严重依赖本地重证据才能判断
- 本轮会碰 `project_source/*`
- 本轮其实还在重判“这是规则问题还是内容问题”
- 当前聊天说法与仓库状态可能冲突
- 本轮虽然改一个对象，但实际牵涉 provider / runtime / 配置层风险

### 5.4 Downgrade Path

- 若只是轻度失效，降级到 `standard_lane`
- 若边界 / 指针 / 结论本身都不稳，降级到 `audit_lane`

### 5.5 Invalidation Conditions

执行过程中，只要出现以下任一情况，`fast_lane` 建议立即失效：

- 当前对象变化
- 当前 blocker 变化
- 当前验收变化
- 新增第二个 blocker
- 需要把更多本地重证据拉进来才能继续判断
- 当前任务从局部任务扩成跨文件层 / 跨方向判断

---

## 6. `standard_lane`

### 6.1 Trigger Gate

以下任一情况成立，默认建议 `standard_lane`：

- 目标和边界已经锁定
- 当前对象 / 当前状态 / 当前 blocker 已知
- 但执行仍会触到样片、输出、局部链路或 `local_only` 重证据
- 本轮不是纯审计，但也不够低风险到走 `fast_lane`

### 6.2 Default Action

默认动作：

1. 读固定入口
2. 读当前对象指针
3. 读与本轮最相关的执行层文件
4. 再落地
5. 验证必须完整看输出，不靠推测
6. 按仓库规则更新日志、commit、push、回流

### 6.3 Veto Conditions

以下情况会让 `standard_lane` 失效并降级：

- 当前对象并未真正锁定
- 当前样片状态与日志冲突
- 本轮仍需先判“这轮到底该不该做”
- 本轮实际上会改 `project_source/*` 正式边界

### 6.4 Downgrade Path

- 默认降级到 `audit_lane`

### 6.5 Invalidation Conditions

- 当前对象、状态、blocker 或验收任一项失真
- 执行中发现本轮实际是边界重判任务
- 执行中发现风险从局部链路升到 provider / runtime / 配置层

---

## 7. `audit_lane`

### 7.1 Trigger Gate

以下任一情况成立，默认建议 `audit_lane`：

- 当前对象指针未刷新或已过期
- 当前 blocker 不止一个
- 当前状态严重依赖本地重证据
- 本轮会碰 `project_source/*`
- 当前聊天和仓库状态可能冲突
- 任务慢在判断，不慢在执行
- 当前会牵连 provider / runtime / 配置层风险

### 7.2 Default Action

默认动作：

1. 先读入口
2. 先读现状
3. 先分层标记：
   - `已确认`
   - `部分成立`
   - `待验证`
   - `推测`
4. 先定是否允许进入执行
5. 不允许直接提速

### 7.3 Exit Condition

只有当以下都成立，才允许退出 `audit_lane`：

- 当前对象已锁定
- 当前状态已锁定
- 当前 blocker 已收口到一个
- 当前验收目标已明确
- 当前风险已经从判断风险降到执行风险

### 7.4 Downgrade / Upgrade Path

- `audit_lane` 不再向下降级
- 条件满足时升级到 `standard_lane`
- 非常少数低风险局部任务可再升级到 `fast_lane`

---

## 8. Parallel Allowed Gate

并发只在以下全部成立时才允许：

1. 当前对象 / 目标 / 验收都已锁定
2. 子任务之间可以清楚拆分
3. 多个子任务不会同时写同一批核心文件
4. 多个子任务不会共享同一高风险输出路径
5. 当前慢点主要在读取 / 定位 / 结构化整理，而不是判断本身
6. 当前不是项目边界重判任务

---

## 9. Parallel Veto Conditions

出现以下任一项，并发立即否决：

- 同时改同一个 `project_source/*`
- 同时改同一个 `codex_source/*`
- 同时改同一条样片 / 同一份成片输出
- 当前对象还没锁定
- 当前 blocker 还没锁定
- 当前任务慢在判断，不慢在执行
- 当前会牵连 provider / runtime / 配置层风险

---

## 10. Parallel Mode Definitions

### 10.1 `serial_only`

#### 适用场景

- 当前任务会写同一条样片
- 当前任务会写同一组输出路径
- 当前任务虽然范围小，但验证必须单点收束
- 当前慢点主要不在读取，而在真实执行 / 组装 / 复核

#### 禁用场景

- 当任务已经纯化成只读审计
- 当任务的子问题只读且能清楚拆分

#### 谁可以写文件

- 只有主执行者

#### 谁不能写文件

- 所有并发读取角色

#### 何时必须保持串行

- 当前任务会写同一条样片
- 当前任务会写同一份 `current_publish_target.md`
- 当前任务会写同一组核心入口文件

### 10.2 `read_parallel`

#### 适用场景

- 多条读取线互不阻塞
- 最终由单点整合
- 并发只为了压缩读取和定位时间

#### 禁用场景

- 任何并发读取角色需要顺手写文件
- 当前任务真正慢在判断

#### 谁可以写文件

- 单点整合者

#### 谁不能写文件

- 所有读取者

#### 何时必须降级回串行

- 读到的新信息改变了对象 / 状态 / blocker
- 需要立刻写同一个核心文件

### 10.3 `explore_plus_integrate`

#### 适用场景

- 当前项目里最常见的提速结构
- 2 条探索线只读并行
- 1 条整合线独占写权

#### 禁用场景

- explorers 也要写文件
- 多条线会同时改同一批核心文件
- 任务本质是多写手实现，不是并行探索

#### 谁可以写文件

- integrator / executor

#### 谁不能写文件

- explorers

#### 何时必须降级回串行

- explorers 输出互相冲突且需要重判边界
- 写入范围开始重叠
- 当前任务从探索收敛变成运行链路风险排查

### 10.4 `true_multi_task_parallel`

#### 适用场景

- 多个子任务彼此独立
- 写入范围完全可拆分
- 各自可以独立验收
- 合并成本清楚可控

#### 禁用场景

- 多个子任务同时写同一条样片
- 多个子任务同时写同一批入口文件
- 多个子任务共享同一高风险输出路径

#### 谁可以写文件

- 各自被明确授权的写手

#### 谁不能写文件

- 未被分配写入范围的角色

#### 何时必须降级回串行

- 写入范围开始交叠
- 当前对象、blocker 或验收发生变化
- 合并成本开始高于并发收益

---

## 11. Parallel Downgrade

并发结构默认按以下方式降级：

1. `true_multi_task_parallel` -> `explore_plus_integrate`
2. `explore_plus_integrate` -> `read_parallel`
3. `read_parallel` -> `serial_only`

降级原则：

- 只要共享写入风险上升，就先砍写入并发
- 只要判断风险上升，就直接退回更保守结构

---

## 12. Parallel Invalidation

当前并发建议出现以下任一项时立即失效：

- 当前对象变化
- 当前 blocker 变化
- 当前验收变化
- 写入文件开始重叠
- 输出路径开始重叠
- 当前任务从执行问题重新变成判断问题

---

## 13. Mandatory Reporting

命中 lane / parallel 机制时，强制回报字段至少包括：

1. `lane_recommendation`
2. `lane_reason`
3. `lane_invalid_if`
4. `parallel_recommendation`
5. `parallel_reason`
6. `parallel_invalid_if`

若当前任务进入并发，还必须额外回报：

7. 当前写文件唯一 owner 是谁
8. 当前是否共享高风险输出路径
9. 当前若失效会降级到什么结构

明确禁止：

- 只写“建议并发”
- 不写为什么
- 不写失效条件

---

## 14. Current Publish Target 字段规则

`codex_log/current_publish_target.md` 中的以下字段属于当前对象级建议：

- `lane_recommendation`
- `lane_reason`
- `lane_invalid_if`
- `parallel_recommendation`
- `parallel_reason`
- `parallel_invalid_if`

写法规则：

- 这是建议，不是绝对命令
- 若当前对象不适合更快或更并发，可以如实写：
  - `standard_lane`
  - `audit_lane`
  - `serial_only`
- 不得为了显得更快，硬写成：
  - `fast_lane`
  - `read_parallel`
  - `true_multi_task_parallel`

---

## 15. Prompt Skeleton：Lane

### 15.1 `fast_lane`

```text
【lane】
fast_lane

【为什么现在可以快】
- 当前对象已固定
- 当前状态已固定
- 当前唯一 blocker 已固定
- 当前验收目标已固定
- 本轮只改单个对象 / 单个局部任务
- 轻量证据足够，不需要先大范围追本地重证据

【默认动作】
1. 读 AGENTS / 00_codex_readme / latest / current_publish_target
2. 补最小必要上下文
3. 直接执行
4. 做最贴近本轮的最小验证
5. 更新 latest / pointer / dated log
6. commit + push + 回流 reading branch

【立即失效条件】
- 当前对象变化
- blocker 变化
- 新增第二个 blocker
- 本轮开始碰 project_source 或 provider/runtime/config 风险
```

### 15.2 `standard_lane`

```text
【lane】
standard_lane

【为什么现在走标准执行单】
- 当前目标已锁定
- 但本轮仍会碰样片、输出、局部链路或 local_only 重证据
- 不宜假装是低风险快车道

【默认动作】
1. 读固定入口
2. 读当前对象指针
3. 读本轮最相关规则 / 现状
4. 再执行
5. 完整验证
6. 更新 latest / pointer / dated log
7. commit + push + 回流

【立即失效条件】
- 当前对象或状态不再稳定
- 任务重新变成边界重判
- 风险升到 provider/runtime/config 层
```

### 15.3 `audit_lane`

```text
【lane】
audit_lane

【为什么先审计】
- 当前对象、状态、blocker 或验收还没真正锁定
- 当前任务慢在判断，不慢在执行
- 若直接执行，容易把判断层问题误写成执行层问题

【默认动作】
1. 先读入口
2. 先读现状
3. 先分层标注：已确认 / 部分成立 / 待验证 / 推测
4. 先判断是否允许进入执行
5. 若允许，再升级到 standard_lane 或 fast_lane

【退出条件】
- 对象锁定
- 状态锁定
- blocker 收口
- 验收明确
```

---

## 16. Prompt Skeleton：Parallel

### 16.1 `serial_only`

```text
【parallel_recommendation】
serial_only

【原因】
- 当前任务会写同一条样片 / 同一组输出路径 / 同一组核心文件
- 当前慢点不在读取，而在真实执行与验证

【执行要求】
- 单写手
- 单验证线
- 不拆并发写入
```

### 16.2 `read_parallel`

```text
【parallel_recommendation】
read_parallel

【原因】
- 当前慢点主要在读规则 / 读日志 / 读现状
- 多条读取线可以并行
- 最终仍由单点整合

【执行要求】
- 所有并发角色只读
- 单点整合者独占写权
- 一旦读取结果改变边界判断，立刻降级
```

### 16.3 `explore_plus_integrate`

```text
【parallel_recommendation】
explore_plus_integrate

【结构】
- explorer A：只读规则 / 闸门 / 禁止项 / 验收项
- explorer B：只读现状 / 目标文件 / 相关产物 / 可复用内容
- integrator：统一写文件、统一验证、统一 Git 收尾

【执行要求】
- explorers 不得写文件
- integrator 独占写权
- 若 explorers 输出冲突且需要重判边界，降级回 serial_only
```

### 16.4 `true_multi_task_parallel`

```text
【parallel_recommendation】
true_multi_task_parallel

【前提】
- 子任务彼此独立
- 写入范围明确且不冲突
- 各自可独立验收

【执行要求】
- 明确每个写手的文件范围
- 不共享高风险输出路径
- 一旦文件或输出路径重叠，立刻降级
```

---

## 17. 当前一句话规则

**先判 lane，再判 parallel；`fast_lane` 和并发都不是默认总开，只有对象、状态、blocker、验收、写入范围和风险都稳定时才允许提速；一旦条件失效，就立刻退回更保守的 lane 或 `serial_only`。**
