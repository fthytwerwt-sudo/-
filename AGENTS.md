# AGENTS.md

## 1. 文件定位

本文件是 Codex 进入《视频工厂》仓库后的顶层入口规则。

它负责回答三类问题：

- 当前项目处于什么阶段
- 进入仓库后默认先读什么、再读什么
- 命中执行任务时，按什么线路推进、何时必须停下如实汇报

它不是：

- 项目脑正文
- 执行层细则全文
- 代码实现说明

分工必须保持清楚：

- `project_source/` 是项目脑，负责项目身份、阶段、边界、场景、结构、Perplexity、回审、心理机制
- `project_source/` 也负责展示路由判断
- `codex_source/` 是执行层，负责读取顺序、执行边界、运行规则、验证口径、汇报方式
- `AGENTS.md` 只做顶层入口，不替代 `project_source/` 和 `codex_source/`

## 2. 当前阶段判断

《视频工厂》当前已经不是“技术可不可行”的阶段，而是：

- 技术闭环已跑通
- 当前重点是内容质量、结构稳定、场景清楚、可复用、可由 Codex 重复执行
- 当前主阶段是内容阶段，正往试发阶段过渡
- 当前优先把“内容过线 / 路由正确 / 模板稳定”压实，不做人优先主义
- 当前正式默认主线已切到：
  - API 生成真人
  - 用户本地录制素材
  - 少量 PPT / 图片辅助
  - 云端剪辑
- 当前结构跟着文案走，不先预设整条视频的固定载体顺序
- 当前人物出现 1 次还是 2 次，是 block 路由结果，不是预设模板
- 当前不再把 pure PPT / 信息卡全片承载当默认主线
- 当前不再把 AI talking avatar / 数字人口播当默认主线
- 当前正式组装继续固定为北京区 `OSS + 云剪 cloud-only`
- 当前仍只围绕视频项目推进，不主动扩到直播、增长、售卖、商业化、大而全产品化
- 当前执行层已进入“正式版目标态搭建阶段”：
  - 要把正式版 API demo 的目标标准、云端主链、修正循环与接手入口正式写入仓库
  - 这表示目标态规划已进入执行层，不表示正式版云端链路已经跑通

当前 demo 是项目锚点，不是整个项目的永久定义。

## 3. 当前 demo 锚点与硬约束

以下内容在当前仓库里仍然有效，不能误删或写丢：

- 当前 demo 目标仍是 15 秒中文 PPT 演示风格视频
- 当前 demo 输入锚点仍是 `cases/demo.md`
- 当前 demo 硬约束仍包括：
  - 中文
  - 15 秒
  - PPT / 卡片页 / 幻灯片风格
  - 案例讲解，不是广告片
  - 默认添加“AI配音 / demo案例”标识
- 当前最小闭环产物要求仍成立：
  - `dist/demo/script.txt`
  - `dist/demo/captions.srt`
  - `dist/demo/voice.mp3`
  - `dist/demo/final.mp4`（若环境允许）
- 后续替换 `cases/demo.md` 可继续复用当前链路的方向仍成立

必须同时明确：

- 这组约束只代表当前最小 demo 锚点
- 不得把它们写成整个项目未来永久只能如此

## 4. 默认最小接手集合

新 Codex 会话进入当前仓库后，默认最小接手集合固定为：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`

这 3 个文件用于完成最小启动，不再默认依赖用户手动复制长背景，也不把聊天记忆当主接手源。

补充规则：

- 若任务明显偏执行规则，再补读 `codex_source/01_execution_rules.md`
- 若任务涉及 commit / push / PR / 主读取分支回流 / `latest.md` 更新 / `.gitignore` 边界，则必读：
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 若任务明显偏项目判断、内容边界或场景结构，再补读 `project_source/06_project_index.md` 与相关 `project_source/*`
- 若任务命中展示路由 / 真人与 PPT 选择 / 录屏与案例图取舍 / 混合承载判断，则在最小接手集合之外补读：
  - `project_source/16_presentation_routing_rules.md`
  - 若任务同时命中“API 真人 + 本地素材 + 少量 PPT / 图片 + 云端剪辑”的新版默认主线，再补读：
    - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - 若任务同时涉及回审记录，再补读 `project_source/10_video_review_record_template.md`
- 若任务命中“正式版 API demo / 正式版目标态 / 云端组装 / 修正循环 / 质量达标反推”，则在最小接手集合之外补读：
  - `codex_source/07_formal_api_demo_target_plan.md`
  - 且必须明确：该文件是正式版目标态计划，不是当前仓库已跑通事实
- 若任务命中协作方式、自动补全边界、下发闸门或并行执行判断，则除最小接手集合外，再补读：
  - `project_source/07_collaboration_adaptation_rules.md`（若存在）
  - `codex_source/06_execution_gate_and_parallel_rules.md`
- 若任务命中真实代码、测试或产物，再继续读对应代码、测试和现有产物
- 若任务依赖 skill，则进入实际执行前仍要检查当前仓库本地 `skills/`；若本地没有相关 skill，再检查全局 `~/.codex/skills`

## 5. 仓库型任务默认线路

凡是命中以下任一条件的任务，默认按仓库型任务处理：

- 仓库改动
- 文件修改
- 需要 PR 回审

默认线路必须写死为：

先看现状 → 开分支改 → 提 PR → 跑 checks → AI 复审 → 用户拍板

补充边界：

- 这条线路只适用于仓库型任务
- 不适用于纯聊天判断
- 不适用于 Perplexity prompt
- 不适用于单次小文本成品

关于 GitHub baseline：

- 如果当前仓库还没有完成第一次 GitHub baseline 同步，允许把首次 baseline 同步作为例外先推到 `main`
- 一旦 baseline 建立，后续仓库改动默认不得直接 push `main`

## 5A. 仓库型任务执行后默认写执行日志

命中仓库型任务且本轮出现真实执行结果时，结束前必须把结果落入 `codex_log/`，不能只停在聊天汇报。

至少遵守以下规则：

- `codex_log/` 是执行日志目录，不放进 `project_source/`
- `codex_log/latest.md` 永远保留最近一次执行的简版交接摘要
- 每次完成真实执行后，新增一条 `codex_log/YYYYMMDD_任务名.md`
- 若本轮改了仓库文件、跑了命令、生成了产物、完成了 commit / push / PR，或形成了新的阻塞点 / 交接点，就必须写日志
- 若只有纯读取、无修改、无执行、无新结论，可以不写日志
- 新聊天框 / 新 Codex 会话接手仓库型任务时，默认先读 `AGENTS.md`、相关 `codex_source/*` 关键文件和 `codex_log/latest.md`

## 5B. 可判断小闭环后默认同步当前分支，供 ChatGPT 复审

命中仓库型任务时，只要本轮已经形成“可判断的小闭环”，默认把这轮结果同步到 GitHub，供 ChatGPT 直接去看当前分支 / 当前 PR 的最新状态。

默认同步动作至少包括：

1. 先更新 `codex_log/latest.md`
2. 命中写日志条件时，同时补完整日志
3. commit 当前分支改动
4. push 到当前工作分支 / 当前 PR

必须明确：

- 这不是每轮都 merge
- 这不是每轮都 push `main`
- 默认 push 的对象是当前工作分支 / 当前 PR，不是 `main`
- 如果要让 ChatGPT 看这一轮最新结果，必须先把这一轮结果 push 到 GitHub

可以暂不 push 的情况：

- 当前仍是半成品
- 改动边界还在摇摆
- 还没形成可判断的小闭环
- 日志还没更新
- 本轮只有纯读取、无改动、无新结论

## 5C. 主读取分支与正式状态硬规则

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

对新聊天 / 新 Codex 会话生效的仓库正式状态，默认以该分支为准，而不是当前任务分支、当前 PR 或聊天汇报。

必须写死以下规则：

### 5C-1. 上传 / 同步硬规则

- 凡本轮存在 Git 跟踪的仓库文件改动，且本轮结果不是 `local_only`、不是 `no_repo_change`，必须：
  - commit
  - push
- 凡本轮形成了新的仓库正式事实，必须先更新：
  - `codex_log/latest.md`
- 凡本轮结果应成为新聊天默认接手口径，必须同步回：
  - `codex/user-readable-map`

### 5C-2. 不得偷换完成状态

以下情况都不得写成“已完成”“已同步”或“仓库正式状态已更新”：

- 只在本地完成
- 只在任务分支完成
- 只开 PR 未回流主读取分支
- 只在聊天里说完成
- `codex_log/latest.md` 未更新

必须明确：

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“正式状态已同步”
- “聊天汇报完成”不等于“仓库正式事实已更新”

### 5C-3. 每轮必须回报 4 个同步锚点

每轮仓库型任务收尾时，必须明确回报：

1. 当前工作分支
2. 最新提交 SHA
3. 是否已 push
4. 是否已同步回 `codex/user-readable-map`

### 5C-4. 状态分类必须显式标记

若本轮还未形成主读取分支正式状态，必须显式分类为以下之一：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

### 5C-5. `.gitignore` / `local_only` 边界

- 若文件被 `.gitignore` 忽略，必须显式标记为 `local_only`
- 必须明确说明该文件不会上传到 GitHub
- 必须明确说明它是否影响新聊天按仓库接手
- 本地配置、secrets、私有凭证文件，不得因为“每轮都要上传”而被错误提交

### 5C-6. “每轮执行完了必须上传”的精确口径

- 凡本轮存在 Git 跟踪的仓库改动，且不是 `local_only` / `no_repo_change`，必须完成 `commit + push`
- 凡本轮形成新的正式接手事实，除 `commit + push` 外，还必须更新 `codex_log/latest.md`
- 凡本轮结果应成为仓库正式状态，还必须同步回 `codex/user-readable-map`
- 若未满足以上条件，不得写“已完成上传”或“已同步”

## 5D. 质量过线后的样片交付硬规则

当本轮达到以下任一条件时，必须向用户交付“可见样片”：

- 项目内部“90 分水位”通过
- `quality_passed`
- 通过“可发布测试线”

这里的“可见样片”不是只写一句“已过线”，而是必须至少交付以下之一：

- 成片本地路径
- 可直接打开的样片文件
- 固定回审帧集合
- 明确的验收样片目录

当前默认样片交付物优先写死为：

1. `dist/formal_api_demo/final.mp4`
2. 若需要辅助验收，再补：
   - `dist/formal_api_demo/review_frames/`

若样片属于 `.gitignore` / `local_only`，必须同时说明：

- 它不会上传到 GitHub
- 但本地已生成
- 用户当前应优先看哪一个本地路径
- 它是否足以完成当前验收

明确禁止：

- “质量已过线”但不给样片路径
- “已经 90 分了”但用户看不到任何样片
- “本地有成片”但不告诉用户在哪
- “GitHub 上看不到是正常的”却不补交付方式

## 6. 真实性与失败处理

以下规则是硬约束：

- 未确认内容不得写成已确认
- 找不到关键文件、skill、权限、remote、PR 能力时，必须如实汇报
- 不得假装成功
- 用户要求落文件时，不得只停在建议层
- 若规范文件与真实仓库状态冲突，以真实仓库状态为准，并明确写出冲突

出现以下情况时，默认先停下汇报，而不是继续硬做：

- 关键文件缺失或无法读取
- skill 需要检查但无法确认
- 权限不足会影响动作选择
- remote / push / PR 能力不足却又影响仓库型任务推进
- 缺少验证依据却要声称“已完成”或“已成功”

## 7. 默认执行原则

当前仓库的默认执行原则是：

- 先分层，再动手
- 先最小闭环，再做美化
- 优先选择最省依赖、最稳的实现
- 不要要求用户先补一堆资料再开始
- 不能因为“顺手优化”就把当前 demo 扩成复杂平台

## 8. 当前一句话入口

如果 Codex 这轮只记一句话：

**新会话先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md` 完成最小启动；当前默认主线按“API 生成真人 + 用户本地录制素材 + 少量 PPT / 图片 + 云端剪辑”理解，结构跟着文案走、人物出现次数由 block 路由决定，cloud assembly 继续是正式主路径；若任务命中展示路由 / 真人与 PPT / 混合承载判断，则再补读 `project_source/16_presentation_routing_rules.md` 与 `project_source/24_human_self_footage_light_ppt_routing_rules.md`；若任务涉及 commit / push / PR / 主读取分支回流 / `latest.md` 更新，则再补读 `codex_source/08_branch_sync_and_reading_branch_rules.md`；命中仓库型任务时，只有同步回 `codex/user-readable-map` 才算仓库正式状态。**
