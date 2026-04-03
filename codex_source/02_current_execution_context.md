# 当前执行前上下文

## 1. 文件定位

本文件用于写清“当前阶段长期有效、但 Codex 不能靠聊天记忆默认知道”的执行前上下文。

它解决的是：

- 当前项目处于什么阶段
- 当前主目标是什么
- 当前明确不做什么
- 当前正式主路径是什么
- demo 在当前阶段到底算什么
- 质量判断该抓什么，不该抓什么
- 新会话进入执行前默认还要补哪些文件
- 哪些内容可以自动补全，哪些不能擅自拍板

它不是：

- 项目脑正文
- 外部研究结论收纳文件
- 完成汇报模板
- 运行事实清单

一句话：

本文件负责把“进入执行前必须先站稳的当前上下文”写死在执行层。

## 2. 当前阶段

当前项目已经不是“技术可不可行”的阶段，而是：

- 技术闭环已跑通
- 当前重点转向内容质量、结构稳定、可复用、可回审、可持续压质量
- 当前仍只围绕视频项目推进
- 当前执行层处于“正式版目标态搭建阶段”，但这不等于云端正式链路已经跑通

必须同时明确：

- 当前 demo 仍是项目锚点
- 但 demo 不是整个项目未来的永久定义

## 3. 当前主目标

当前执行层的主目标不是继续证明“能不能生成视频”，而是把视频内核做成：

- 可重复执行
- 可回审
- 可持续压质量
- 可稳定协作

当前更关心的是：

- 脚本是否成立
- 结构是否选对
- 配音 / 字幕 / 画面是否不过线不交付
- ChatGPT / Perplexity / Codex / 用户之间的结论和执行现实，能否稳定回写到仓库

## 4. 当前明确不做什么

当前阶段默认不主动展开：

- 直播
- 售卖
- 获客
- 增长
- 商业化包装
- 自动化运营闭环
- 大而全平台化
- 以前端工作台为优先的路线
- 把平台发布 API 写成当前前置依赖
- 把 cloud assembly 写成当前主线硬阻塞

这些方向不是永久不做，而是当前不允许抢走视频主线。

## 5. 当前正式主路径

当前执行层默认采用的正式主路径是：

`文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传`

执行含义必须写清：

- generation 层继续接 API
- assembly 层当前默认走本地
- cloud assembly 属于后续增强项，不是当前硬前置
- 当前允许本地生成 + 人工上传
- 当前不把“只差平台 API”当项目成立前提
- visual plan / preview 只能算辅助产物，不得写成 generation success
- local assembly 只负责拼接真实生成素材，不得替代图片 / 视频生成本身

当前免费优先模型路线也已经明确：

- 通用图像主线：`wan2.6-image`
- 通用视频主线：`wan2.6-t2v`
- 真人开口分支前置检测：`liveportrait-detect`
- 真人开口生成分支：`liveportrait`
- `wan2.6-image` 负责首帧 / 背景 / 人像底图补位
- `wan2.6-t2v` 负责普通视频主线
- `liveportrait` 只用于固定背景 / 人物开口分支，且必须先过 `liveportrait-detect`
- 当前普通图片 / 视频主线 provider implementation 已接入：
  - `wan2.6-image` 会真实创建阿里异步任务、轮询并下载图片到本地 `dist`
  - `wan2.6-t2v` 会真实创建阿里异步任务、轮询并下载视频到本地 `dist`
- 真人开口分支仍只保留路线与语义：
  - `liveportrait-detect -> liveportrait` 仍未接入真实 provider implementation
  - 当前必须继续诚实 `blocked`

## 6. 当前 demo 身份

当前 demo 的身份必须固定理解为：

- demo 只证明链路跑通
- demo 是最小闭环验证件 / 运行锚点
- demo 不是质量样片
- demo 不能继续被拿来定义质量下限

当前仍有效的 demo 锚点包括：

- 输入锚点：`cases/demo.md`
- 目标：15 秒中文 PPT / 卡片页 / 幻灯片风格案例讲解
- 最小闭环产物：
  - `dist/demo/script.txt`
  - `dist/demo/captions.srt`
  - `dist/demo/voice.mp3`
  - `dist/demo/final.mp4`（若环境允许）

## 7. 当前质量判断核心

当前质量判断的核心不是“有没有产物”，而是：

- 配音是否还像系统播报
- 字幕与配音是否基本同步
- 开头 3 秒是否有效
- 内容是否还像说明书 / demo 演示
- 画面是否只有静态轮播
- 前后变化是否能被看懂
- 结尾是否有落点

必须同时明确：

- “抖音 90 分标准”是项目内部质量简称，不是平台官方规则
- 当前不要再围绕旧 demo 定质量下限
- 当前第一优先质量增强路线仍是先打掉最致命的 demo 感，而不是扩更多能力

## 8. 新会话默认先读

新会话进入当前仓库并准备执行时，默认读取顺序是：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_source/01_execution_rules.md`
5. 本文件 `codex_source/02_current_execution_context.md`
6. 若涉及 commit / push / PR / 主读取分支 / `latest.md` / `.gitignore` 边界，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`
7. 若涉及外部结论 / 新拍板 / 研究桥接，再读 `codex_source/03_research_findings_bridge.md`
8. 若涉及完成回报 / 状态判断 / 验收口径，再读 `codex_source/04_completion_and_review_contract.md`
9. 若涉及执行现实偏差 / 原方案失效 / 资源权限环境问题，再读 `codex_source/05_execution_deviation_and_reality_sync.md`
10. 再补读与当前任务直接相关的 `project_source/*`、代码、测试与产物

## 8A. 当前主读取分支与正式状态

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

执行层必须按以下口径理解“正式状态”：

- 任务分支上的本地改动，不等于仓库正式状态
- 任务分支已 push，不等于主读取分支已更新
- 已开 PR，不等于正式状态已同步
- 聊天里说完成，不等于仓库正式事实已更新
- 只有结果同步回 `codex/user-readable-map`，才默认成为新聊天的仓库接手口径

## 8B. 当前仓库型任务的同步硬规则

凡本轮存在 Git 跟踪的仓库文件改动，且本轮结果不是 `local_only`、不是 `no_repo_change`，必须：

1. 更新 `codex_log/latest.md`
2. commit
3. push

凡本轮形成了新的仓库正式事实，除上面 3 步外，还必须：

4. 同步回 `codex/user-readable-map`

若未满足以上条件，不得写：

- “已完成上传”
- “已同步”
- “仓库正式状态已更新”

## 8C. 当前仓库型任务的状态分类

每轮仓库型任务收尾时，必须显式分类为以下之一：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

分类含义必须固定：

- `formal_synced`
  - 已更新 `codex_log/latest.md`
  - 已 commit
  - 已 push
  - 已同步回 `codex/user-readable-map`
- `task_branch_only`
  - 已 commit / push 到任务分支
  - 但主读取分支还没更新
- `pr_open_not_merged_to_reading_branch`
  - 已有 PR
  - 但 PR 还没回流主读取分支
- `local_only`
  - 结果只存在本地，或文件被 `.gitignore` 忽略，不会上 GitHub
- `no_repo_change`
  - 本轮没有 Git 跟踪的仓库文件改动

## 8D. `.gitignore` / `local_only` 边界

若文件被 `.gitignore` 忽略：

- 必须显式标记为 `local_only`
- 必须明确说明它不会上传到 GitHub
- 必须明确说明它是否影响新聊天按仓库接手

同时必须保留的边界：

- 本地配置
- secrets
- 私有凭证
- 其他不应进 Git 的本地文件

不得因为“每轮都必须上传”而被错误提交。

## 9. 可自动补全项

在当前已确认边界内，Codex 可以自动补全：

- 已明确任务下的执行性结构补齐
- 执行层文件里的字段、模板、状态说明补全
- 已拍板主线下的低风险重写
- 已确认范围内的日志、回报、读取顺序补齐
- 当前主线不变前提下的执行机制收口

## 10. 禁止擅自拍板项

Codex 不得擅自拍板：

- 是否改项目主线
- 是否扩到直播 / 商业化 / 获客 / 平台化
- 是否把 cloud assembly 升回当前主线
- 是否把外部研究结论直接当成已采用事实
- 是否把用户模糊表达自动升格为长期规则
- 是否把“部分成立”的现实写成“已成立”
- 是否把项目脑判断偷换成执行层事实

## 11. 当前一句话执行前上下文

当前项目已经从“能不能生成”转到“质量能不能过线、结构能不能稳定、协作能不能复用”；执行层默认按“generation 接 API、assembly 走本地、cloud assembly 暂不当前置”的主路径推进，任何影响执行的新结论和现实偏差都不能只停在聊天里。
