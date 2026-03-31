# 20260401 Acceptance Timing Patch

## 本轮目标

- 给 `codex_source/07_formal_api_demo_target_plan.md` 补一节“验收节奏 / 验收时机 / 阶段完成标志”
- 让正式版目标态计划明确回答：什么时候验收、每阶段做到哪算过、什么时候进入下一阶段、什么时候不能继续往下走

## 执行前已确认事实

- 当前仓库已确认事实仍是本地 demo 链路，不是正式版云端链路
- `codex_source/07_formal_api_demo_target_plan.md` 是正式版目标态计划，不是当前仓库已跑通事实
- 07 文件已经有标准、一票否决、可继续复审水位、修正循环、最小回归样本集、机器硬校验与人工复审
- 当前缺的是“阶段性什么时候验、做到哪算过、什么时候不能继续往下走”

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/20260401_formal_api_demo_target_plan_upgrade.md`
- 当前 git 状态

## 实际改动

- 修改 `codex_source/07_formal_api_demo_target_plan.md`
  - 新增正式章节“验收节奏 / 验收时机 / 阶段完成标志”
  - 补清骨架验收、接 API 前验收、首轮样片验收、修正循环验收四个时间点
  - 补清阶段完成标志与用户介入验收节点

- 修改 `codex_log/latest.md`
  - 写明本轮补的是 07 文件的验收节奏与阶段完成标志
  - 写明新会话推进正式版目标态时应优先看 07 文件这一节

- 新增 `codex_log/20260401_acceptance_timing_patch.md`
  - 记录本轮目标、读取、改动、结果与下一步建议

## 当前结果

- 07 文件现在不只定义“标准是什么”，还定义了“什么时候验、验什么、做到哪算过”
- 正式版目标态计划现在已明确区分：
  - 当前阶段验收
  - 正式成片质量验收
- 当前表述仍未把目标态误写成当前仓库已跑通事实

## 下一步建议

- 若后续继续推进正式版目标态，下一轮最适合做的是真正落正式版最小文件骨架，并按 07 文件里新增的验收节奏先完成骨架验收。
