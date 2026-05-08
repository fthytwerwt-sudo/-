# 20260329 Prompt Driven Internal Positioning

## 1. 本轮目标

- 把当前仓库的项目口径正式收束为“个人内部使用的、Prompt 驱动的、Codex 可执行的视频内核”。
- 明确前端页面不是当前阶段重点，不再按产品化工作台方向默认推进。

## 2. 执行前已确认事实

- 当前项目名仍是“视频工厂：AI 垂类场景化视频内核”。
- 当前项目已经过了技术可不可行验证阶段。
- 当前正式阶段仍是：
  - 内容可发
  - 质量优化
  - 可复用工作流
  - Codex 可重复执行
- 当前只处理视频项目，不展开直播、增长、商业化、售卖、API 中控或大而全产品化扩展。
- 当前工作分支是 `codex/user-readable-map`。
- 当前分支已跟踪 `origin/codex/user-readable-map`。

## 3. 实际读取

- 顶层与执行层入口：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
- 项目脑核心文件：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/06_project_index.md`
- 为判断是否需要同步改口径而补读：
  - `project_source/02_scene_mode_templates.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
- 实际审查：
  - `rg` 搜索“前端 / 页面 / 工作台 / 产品化 / platform / Prompt / Codex / 内部使用”等关键词
  - `git status --short --branch`
  - `git branch -vv`

## 4. 实际改动

- 修改 `project_source/00_project_brief.md`
  - 明确项目是“个人内部使用的、Prompt 驱动、Codex 可执行”的内部视频项目。
  - 明确当前不是前端页面 / 工作台优先项目。
  - 明确当前判断标准是 prompt 是否能稳定驱动出想要结果。
- 修改 `project_source/01_project_system_prompt.md`
  - 明确项目正式理解、用户 / ChatGPT / Codex 在 Prompt 驱动协作中的角色。
  - 明确默认不是先做页面，而是先把 prompt、结构、执行任务和回审口径压清楚。
- 修改 `project_source/03_perplexity_prompt_library.md`
  - 在固定背景前置块中补入“个人内部使用 + Prompt 驱动 + 不以前端页面为重点”。
- 修改 `project_source/06_project_index.md`
  - 明确 `project_source/` 服务的是“个人内部使用的 Prompt 驱动型视频工厂 / 视频内核”，不是前端产品工作台。
- 修改 `codex_source/00_codex_readme.md`
  - 明确执行层服务的是 Prompt 驱动视频内核，而不是前端页面优先项目。
- 修改 `codex_source/01_execution_rules.md`
  - 在最小必要背景包里补入“个人内部使用 / Prompt 驱动 / 非前端页面优先”。
  - 在禁止事项中补入“不得把项目导向前端页面 / 工作台优先”。
- 刷新 `codex_log/latest.md`
  - 同步本轮新的项目正式口径。

## 5. 实际执行

- 先按用户给定读取范围读取顶层入口、执行层入口和项目脑核心文件。
- 再用关键词审查确认当前仓库中并不存在大面积“前端工作台”残留，而是少数核心定位文件需要进一步收紧口径。
- 只改与项目身份、Prompt 协作方式、Codex 执行背景包直接相关的文档。
- 未改代码链路、未新增前端方案、未扩展直播 / 增长 / 商业化方向。
- 已完成本地提交：
  - `379072b docs: tighten prompt-driven project positioning`
- 已推送当前工作分支：
  - `codex/user-readable-map -> origin/codex/user-readable-map`

## 6. 当前结果

- 当前项目文档已更明确体现：
  - 个人内部使用
  - Prompt 驱动
  - Codex 可执行
  - 视频内核优先
  - 前端页面不是当前重点
- 当前项目没有被改写成对外平台，也没有被改写成前端工作台优先项目。
- 场景主轴仍保持不变：
  - AI 项目讲解
  - AI 方法分享
  - AI 学习实操
  - AI 案例拆解
- 当前这轮结果已同步到 GitHub 当前工作分支，可供 ChatGPT 直接复审。

## 7. 下一步建议

- 后续凡涉及项目定位、系统理解、Perplexity 固定背景或执行层背景包，都以本轮口径为准。
- 若后续用户只想让 Codex 按 prompt 稳定出片，不应再默认扩出页面方案讨论。
- 若将来真的进入前端页面阶段，应作为新阶段单独立项，而不是继续沿用当前默认口径。
