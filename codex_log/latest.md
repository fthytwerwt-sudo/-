# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，后续仓库型任务继续默认在功能分支推进，而不是直接改 `main`。
- 当前项目已进入“正式版目标态搭建阶段”：
  - 正式版目标态文件已落入执行层
  - 但正式版云端链路仍不能视为已跑通
- 当前仓库已明确项目正式口径：
  - 个人内部使用
  - Prompt 驱动
  - Codex 可执行
  - 视频内核优先
  - 前端页面不是当前阶段重点
- 当前仓库仍保留“用户可讨论定位层”，用于帮助非技术用户判断问题落在哪一层，并更准确地向 ChatGPT 描述修改点。
- 原有三层分工保持不变：
  - `project_source/` 负责项目脑
  - `codex_source/` 负责执行层
  - `codex_log/` 负责执行日志
- 当前已确认运行事实仍是本地 demo 链路：
  - `cases/demo.md` → `generate_demo.py` → `say / afconvert / ffmpeg-static` → `video_builder.swift` → `dist/demo/` 四件套
- 当前旧 demo 仍是运行锚点，不是质量样片，不是正式版事实参考
- 当前新落仓库的正式版文件定义的是目标态：
  - 先锁质量标准
  - 再按 bug / 缺口 / 参数 / 编排问题进入修正循环
  - 不得写成“当前云端正式链路已成立”

## 最近一次完成了什么

- 已新增 `codex_source/07_formal_api_demo_target_plan.md`：
  - 把正式版 API demo 目标态、执行 Gate、修正循环、最小回归样本集、机器硬校验与人工复审正式写入仓库
  - 明确区分“当前仓库事实”与“正式版目标态”
- 已同步增补入口文件：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
- 已刷新 `codex_log/latest.md`，让新会话能直接接手正式版目标态主线
- 已新增完整执行日志：
  - `codex_log/20260401_formal_api_demo_target_plan_upgrade.md`

## 当前最关键的下一步

- 若后续继续执行正式版主线，应先按 `codex_source/07_formal_api_demo_target_plan.md` 落正式版最小文件骨架、执行 Gate 与校验框架。
- 在火山凭证、空间名、资源存储配置、关键接口可用性未补齐前，不得把正式版云端链路写成已跑通。
- 若后续继续做仓库型小闭环，仍按“先更新日志，再 commit / push 当前分支，供 ChatGPT 复审”推进。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- 若任务偏正式版 API demo / 目标态 / 云端组装 / 修正循环 / 质量达标反推，再补读：
  - `codex_source/05_runtime_and_artifact_rules.md`
  - `codex_source/01_execution_rules.md`
- 若任务偏项目定位，再补读 `project_source/00_project_brief.md` 和 `project_source/01_project_system_prompt.md`
- 必须明确：
  - `codex_source/05_runtime_and_artifact_rules.md` 记录当前仓库已确认事实
  - `codex_source/07_formal_api_demo_target_plan.md` 定义正式版目标态
  - 旧 demo 仍是运行锚点，正式版链路仍不是当前已验证跑通事实
