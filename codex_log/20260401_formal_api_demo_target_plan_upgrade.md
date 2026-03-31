# 20260401 Formal Api Demo Target Plan Upgrade

## 本轮目标

- 把“正式版目标态执行计划”正式落进当前仓库
- 同步补齐新会话接手入口与日志机制
- 明确拆开“当前仓库已确认事实”与“正式版目标态计划”

## 执行前已确认事实

- 新会话默认最小接手集合仍是：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
- 当前仓库已确认跑通的真实链路仍是本地 demo：
  - `cases/demo.md` → `generate_demo.py` → `say / afconvert / ffmpeg-static` → `video_builder.swift` → `dist/demo/` 四件套
- 旧 demo 只保留运行锚点价值，不再作为质量样片或质量基线
- 当前不能把“正式版云端链路”写成已跑通事实

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- 全局 skill：
  - `~/.codex/skills/context-driven-development/SKILL.md`
  - `~/.codex/skills/verification-before-completion/SKILL.md`
- 额外检查：
  - `codex_source/` 与 `codex_log/` 下是否已有 `formal_api_demo / target_plan / 目标态 / 修正循环` 近似文件

## 实际改动

### 新建

- `codex_source/07_formal_api_demo_target_plan.md`
  - 新增正式版 API demo 的目标态执行计划
  - 明确加入文件定位、当前状态 vs 目标状态、执行前提 / Gate、交接规则
  - 系统化写入标准先锁死、一票否决项、可继续复审水位、修正循环、最小回归样本集、机器硬校验与人工复审

- `codex_log/20260401_formal_api_demo_target_plan_upgrade.md`
  - 记录本轮目标、读取、改动、结果与下一步建议

### 修改

- `AGENTS.md`
  - 在当前阶段判断中补入“正式版目标态搭建阶段”
  - 在默认最小接手集合补读规则中补入 `codex_source/07_formal_api_demo_target_plan.md`
  - 明确该文件是目标态计划，不是当前仓库已跑通事实

- `codex_source/00_codex_readme.md`
  - 在新会话最小接手入口补入正式版目标态任务的补读规则
  - 在已有文件清单中加入 `codex_source/07_formal_api_demo_target_plan.md`
  - 明确当前仓库事实仍以 `codex_source/05_runtime_and_artifact_rules.md` 为准

- `codex_log/latest.md`
  - 更新为“正式版目标态搭建阶段”
  - 明确目标态文件已落仓库，但正式版云端链路仍未视为已跑通
  - 更新新会话接手建议文件列表

## 实际执行

- 检查并确认仓库中不存在与 `formal_api_demo_target_plan` 同义的现有文件，避免重名冲突
- 选定新文件路径为 `codex_source/07_formal_api_demo_target_plan.md`
- 仅修改本轮授权范围内的入口文件与日志文件，避开当前工作区中已存在的 `project_source/*` 用户改动

## 当前结果

- 正式版 API demo 的目标态计划已正式落入仓库
- 新会话接手入口已能明确区分：
  - 当前仓库已确认事实
  - 正式版目标态计划
- 当前仍缺以下真实前提，不能写成已跑通：
  - 火山正式凭证配置
  - 空间名 / 资源存储配置
  - 关键接口可用性
  - 组装导出参数与权限状态

## 为什么这轮必须这样改

- 必须新增“目标态计划文件”，因为当前正式版主线已经从“低配验证”切换成“标准先锁死、差距进入修正循环”，但仓库里此前没有一份执行层文件专门承载这条目标态。
- 必须把“当前仓库事实”和“目标态计划”拆开，因为当前仓库真实跑通的仍是本地 demo 链路；若不拆开，新会话极易把目标态误读成已跑通事实。
- 必须同步更新 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`，因为这三者是新会话最小接手入口；只新增目标态文件但不接入口，会导致下一轮仍靠聊天记忆接手。

## 下一步建议

- 若后续继续执行正式版主线，下一步应按 `codex_source/07_formal_api_demo_target_plan.md` 落正式版最小文件骨架、执行 Gate 与校验框架，但在真实前提补齐前仍不得声称正式版云端链路已跑通。
