# 2026-04-11 execution lane 与 parallel 机制补全

## 本轮目标

- 把 `execution lane`（执行车道）与 `parallel gate`（并发判定闸门）正式补进仓库
- 让后续 ChatGPT / Codex 协作不只会判断 `fast_lane` / `standard_lane`
- 让当前对象指针能直接给出 lane / parallel 建议
- 明确条件失效时必须降级

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/12_codex_known_state_three_layer_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260411_current_publish_target_pointer_and_light_evidence_patch.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_source/06_execution_gate_and_parallel_rules.md`
- `codex_source/10_codex_multi_agent_prompt_library.md`

## skill 检查

- `已确认` 仓库本地 `skills/`：不存在
- `已确认` 全局 `~/.codex/skills` 已检查并实际采用：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`

## 当前仓库里原本已有但不够的部分

### 已有

- 有：
  - 当前对象固定指针
  - 轻量证据包
  - 多 agent 路由短说明
  - 多 agent 模板库
  - “执行闸门与并行规则”的粗粒度说明

### 缺口

本轮前，仓库还没有正式补全下面这 9 项：

1. `lane trigger gate`
2. `lane veto conditions`
3. `lane downgrade path`
4. `lane invalidation conditions`
5. `parallel allowed gate`
6. `parallel veto conditions`
7. `parallel modes`
8. `parallel downgrade`
9. `mandatory reporting`

也就是说：

- 之前能说“适合多 agent”
- 但还不能系统地说：
  - 先不先提速
  - 先不先并发
  - 提速到哪一级
  - 失效时退回哪一级

## 本轮实际新增 / 修改文件

### 新增

- `codex_source/13_execution_lane_and_parallel_rules.md`
- `codex_log/20260411_execution_lane_and_parallel_mechanism_patch.md`

### 修改

- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/current_publish_target.md`
- `codex_log/latest.md`

## GPT Project 路由层最终补了什么

`project_source/20...` 现在只保留短路由说明，不塞完整正文。

它现在明确补出：

- `fast_lane`
- `standard_lane`
- `audit_lane`
- `parallel gate`
- `parallel veto`
- `parallel mode`
- ChatGPT 命中时必须输出：
  - `lane_recommendation`
  - `lane_reason`
  - `lane_invalid_if`
  - `parallel_recommendation`
  - `parallel_reason`
  - `parallel_invalid_if`

同时写清：

- 多 agent 只是并发结构之一
- 不是所有提速都靠多 agent
- GPT Project 只放短路由说明
- 完整规则正文统一去 `codex_source/13_execution_lane_and_parallel_rules.md`

## Codex 执行层最终补了什么

`codex_source/13_execution_lane_and_parallel_rules.md` 现在完整落了：

- `fast_lane` 触发条件 / 默认动作 / veto / downgrade / invalidation
- `standard_lane` 触发条件 / 默认动作 / invalidation
- `audit_lane` 触发条件 / 退出条件 / 升降级
- `parallel allowed gate`
- `parallel veto`
- 4 类 `parallel mode`：
  - `serial_only`
  - `read_parallel`
  - `explore_plus_integrate`
  - `true_multi_task_parallel`
- 每种并发模式的：
  - 适用场景
  - 禁用场景
  - 谁可以写文件
  - 何时必须降级
- `mandatory reporting`
- lane 与 parallel 的 prompt skeleton
- “提速只提读取 / 对齐 / 下发，不承诺 runtime 一定更快”的边界

## `current_publish_target.md` 新增了什么

新增字段：

- `lane_recommendation`
- `lane_reason`
- `lane_invalid_if`
- `parallel_recommendation`
- `parallel_reason`
- `parallel_invalid_if`

当前对象现在明确写成：

- `lane_recommendation = standard_lane`
- `parallel_recommendation = serial_only`

## 当前对象为什么不是 `fast_lane`

- 对象、状态、blocker 已固定
- 但当前对象任务仍会碰同一条样片、同一组输出路径和 `local_only` 重证据
- 当前样片级任务很容易触到组装 / 导出 / 本地重证据验证
- 因此当前对象不适合被默认写成无条件 `fast_lane`

## 当前对象为什么不是并发

- 当前对象级任务一旦进入执行，通常会同时写：
  - 同一条样片
  - 同一组 manifest / route / result_summary
  - 同一组输出路径
- 当前慢点也往往在真实执行和验证，不在读取本身
- 因此当前对象级默认建议保持：
  - `serial_only`

## 本轮前置阻断了哪些风险

1. 阻断了“所有提速都默认多 agent”的误判
2. 阻断了“看起来小就默认 `fast_lane`”的误判
3. 阻断了“允许并发 = 允许同时写同一条样片”的误判
4. 阻断了“提速 / 并发 = runtime 一定更快”的偷换
5. 阻断了“lane / parallel 建议只在聊天里说过就算正式已知”的偷换

## 最小验证

- `git diff --check`
- 重新读取：
  - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
  - `codex_source/13_execution_lane_and_parallel_rules.md`
  - `codex_log/current_publish_target.md`
  - `codex_log/latest.md`
- 使用 `git show codex/user-readable-map:路径` 实读验证回流后的：
  - `codex_log/current_publish_target.md`
  - `codex_log/latest.md`
  - `project_source/20...`
  - `codex_source/13...`

## 当前结果

- `已确认` 机制层已经正式成立并可默认使用
- `已确认` 本轮没有改当前样片正式结论
- `已确认` 本轮没有改项目脑正式事实
- `已确认` 本轮没有碰代码、测试或 `dist/*`
