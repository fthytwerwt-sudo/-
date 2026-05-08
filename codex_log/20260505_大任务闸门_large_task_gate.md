# 大任务闸门 large_task_gate

## 1. 本轮目标

- `已确认` 本轮只补 `large_task_gate（大任务闸门）` 机制。
- `已确认` 目标是让 Codex 在超过 3 分钟视频、多文件、多步骤、多验证、多模块任务前，自动进入 lane / parallel 判断。
- `已确认` 本轮不是修改视频，不是生成样片，不是继续项目清理，不是调整剪辑风格，不是开发真正 multi-agent 系统。

## 2. 修改文件

1. `AGENTS.md（仓库入口规则）`
2. `codex_source/00_codex_readme.md（Codex 执行层总入口）`
3. `codex_source/01_execution_rules.md（执行规则）`
4. `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）`
5. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（给 GPT Project 用的多执行器路由说明）`
6. `codex_log/latest.md（最新摘要）`
7. `codex_log/20260505_大任务闸门_large_task_gate.md（本日志）`

## 3. large_task_gate 触发条件

`large_task_gate（大任务闸门）` 在以下任一情况触发：

1. 视频 / 样片 / 成片 / 剪辑对象超过 `3 分钟 / 180 秒`。
2. 本轮同时涉及脚本、素材、reference、时间线、TTS、字幕、验证、日志中的三项或以上。
3. 本轮需要写入或检查 3 个以上仓库文件。
4. 本轮同时涉及规则文件、执行文件、日志文件、报告文件中的两类或以上。
5. 本轮需要大量只读审计、定位、结构化整理，再统一写入。
6. 本轮任务包含“写文件 + 检查 + 日志 + push / 同步”等多步骤闭环。
7. 用户明确提到“长视频”“大任务”“多文件”“多步骤”“多 agent”“并发”“提速”“检查很多文件”。

## 4. 超过 3 分钟视频的规则

- `已确认` 任何视频任务中，目标视频、样片、成片、剪辑对象或复审对象超过 `3 分钟 / 180 秒`，必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 触发后必须完成 lane / parallel 判断后，才能进入长视频、大文件、多步骤、多验证任务执行。

## 5. 多文件 / 多步骤 / 多验证任务的规则

- `已确认` 非视频任务只要变成多文件、多步骤、多验证、多模块，也必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 写文件、检查、脚本、仓库治理任务如果范围变大，也必须判断是否需要 `serial_only（串行执行）`、`read_parallel（只读并发）`、`explore_plus_integrate（探索 + 单点整合）` 或 `true_multi_task_parallel（真正多任务并发）`。

## 6. lane / parallel 必读文件

触发后必须读取：

1. `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）`
2. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（给 GPT Project 用的多执行器路由说明）`

触发后必须输出：

- `lane_recommendation`
- `lane_reason`
- `lane_invalid_if`
- `parallel_recommendation`
- `parallel_reason`
- `parallel_invalid_if`
- `write_owner`
- `read_only_lanes`
- `integration_owner`

硬规则：

- 触发 `large_task_gate（大任务闸门）` 不等于自动多 agent。
- 判断是否并发不等于默认并发。
- 写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定时，必须保持或降级为 `serial_only（串行执行）`。

## 7. blocked 条件

以下情况必须 blocked：

- 关键规则文件 missing / unreadable。
- 需要重写整份规则文件才能继续。
- 修改会让 `route_decision（路由判断）` 与 lane / parallel 规则冲突。
- 需要修改视频状态或当前复审包才能继续。
- 需要处理 `素材录制/` 才能继续。
- 需要新建外部工作区才能继续。
- 需要执行 Git 高风险操作才能继续。

## 8. 未执行的高风险动作

- `已确认` 未修改视频产物。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前发布状态。
- `已确认` 未修改 `content_validation（内容验证）`。
- `已确认` 未修改 `send_ready（可发送状态）`。
- `已确认` 未处理 `素材录制/（用户录制原始素材目录）`。
- `已确认` 未新建外部工作区。
- `已确认` 未新建 fresh clone、audit clone、clean clone、临时 clone 或外部 worktree。
- `已确认` 未执行 Git GC / prune / repack。
- `已确认` 未执行 Git LFS / history rewrite。
- `已确认` 未 force push。

## 9. 验证结果

- `已确认` 已运行 `git diff --check`，无报错输出。
- `已确认` 已运行 `git diff --cached --check`，无报错输出。
- `已确认` 已重新读取 `AGENTS.md`、`codex_source/01_execution_rules.md`、`codex_source/13_execution_lane_and_parallel_rules.md`、`project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`、`codex_source/00_codex_readme.md` 和本日志。
- `已确认` `git status --short` 只显示本轮允许修改 / 新增的规则与日志文件；另有既有冻结未跟踪文件 `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`，本轮未纳入。

## 10. 下一个目标

后续 Codex 看到超过 3 分钟视频、多文件、多步骤、多验证任务时，先自动触发 `large_task_gate（大任务闸门）` 并完成 lane / parallel 判断，再决定串行、只读并发、探索整合或真正多任务并发。
