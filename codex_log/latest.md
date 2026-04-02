# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- 执行层现在已补上两条正式机制：
  - 外部结论桥接：Perplexity / ChatGPT / 用户新拍板若会影响执行，必须先进入 `codex_source/03_research_findings_bridge.md` 或本轮执行单
  - 执行偏差回写：真实执行若已证明原方案与现实不一致，必须按 `codex_source/05_execution_deviation_and_reality_sync.md` 回写并改标
- 当前执行层新增了 4 个正式文件：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/04_completion_and_review_contract.md`
  - `codex_source/05_execution_deviation_and_reality_sync.md`

## 最近一次完成了什么

- 新建执行前上下文文件，明确：
  - 当前阶段
  - 当前主目标
  - 当前不做什么
  - 当前正式主路径
  - demo 身份与质量判断核心
- 新建研究结论桥接文件，明确：
  - 来源类型
  - 状态
  - 结论摘要
  - 影响范围
  - 原计划改动点
  - 本轮必须遵守项
  - 暂未确认项
  - 建议落点文件
- 新建完成与回审契约，固定最终汇报格式：
  - 读取结果
  - 实际改动
  - 未改动项
  - 完成标准对照
  - 当前状态
  - 阻断 / 风险 / 待确认
  - 下一步建议
- 新建执行偏差回写文件，明确：
  - 什么叫执行偏差
  - 偏差分级
  - 原方案如何改标
  - 偏差写回哪里
- 同步更新：
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`

## 当前已确认事实

- Perplexity 结果不会自动同步到 Codex。
- ChatGPT 判断不会自动同步到 Codex。
- 用户聊天里的新拍板若未写入桥接文件或本轮执行单，也不会自动变成长期执行事实。
- 真实执行若已证明原方案不完整成立，Codex 不能只在回复里轻描淡写说明，必须回写执行层文件或本轮日志。

## 当前最关键的下一步

- 后续凡是用户、ChatGPT 或 Perplexity 形成了新的执行性结论，先写进 `codex_source/03_research_findings_bridge.md`，再让 Codex 默认采用。
- 后续凡是真实执行发现原方案与现实不一致，先按 `codex_source/05_execution_deviation_and_reality_sync.md` 改标并回写，再决定是否继续执行或重拍板。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_source/02_current_execution_context.md`
- 若任务涉及外部结论桥接：
  - `codex_source/03_research_findings_bridge.md`
- 若任务涉及完成回报或验收口径：
  - `codex_source/04_completion_and_review_contract.md`
- 若任务涉及执行现实偏差：
  - `codex_source/05_execution_deviation_and_reality_sync.md`
