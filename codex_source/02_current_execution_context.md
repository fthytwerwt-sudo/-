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

## 3A. 当前阶段优先级与主线边界

当前阶段新增拍板如下：

- 当前正式默认主线已切到：
  - 人物判断
  - 用户自己的真实录制素材
  - 少量 PPT / 图片辅助
- 当前先把这条线压稳，优先压“更像真人会发 / 更少 demo 感 / 更容易稳定复用”
- pure PPT / 信息卡母版仍可保留，但只作为次级支路推进
- AI talking avatar / 数字人口播当前不再作为默认主承载
- 必须把以下问题正式写成高风险边界：
  - 口型和语音不同步
  - 性别与文案不匹配
  - 动作与文案不匹配
  - 视觉人物与内容判断不一致
- OSS 已具备
- 阿里云剪已具备
- 当前正式默认主线 assembly 路径继续固定为“北京区 OSS + 云剪唯一主路径”
- `local assembly` 已移出正式默认主线，不再保留 fallback / 兜底语义

## 3B. 当前 pure PPT 次级支路风格口径

当前 pure PPT / 信息卡次级支路默认按以下口径理解：

- 默认走“白领咨询报告感 / 体面专业感 / 信息高效感”
- 默认不走培训班感、模板货感、学生作业感、低质 AI 感
- 当前只是把这套规则作为次级支路默认口径，不是全项目默认主线，也不是未来唯一审美
- 具体默认规则、默认值、黑名单、回审口径和母版骨架统一以 `project_source/17_white_collar_ppt_style_rules.md` 为准

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
- 当前暂不考虑动态 PPT
- 不得把“需要动态 PPT”写成当前前置条件
- 若当前纯 PPT 主线走云剪，第一轮不得以动态 PPT 为目标
- 不以复杂 motion design / 高成本视觉特效为当前路线

这些方向不是永久不做，而是当前不允许抢走视频主线。

## 5. 当前正式主路径

当前执行层默认采用的正式主路径是：

`文本需求 → 脚本 → 配音 API → 人物判断段 / 自录过程段 / 少量结果卡素材 → 北京区 OSS + 云剪工程 assembly → 成片导出 → 人工上传`

执行含义必须写清：

- 当前内容主承载优先走“人物 + 自录素材 + 少量 PPT / 图片”
- 配音 API 继续是正式 generation 主链
- 默认人物段、自录段和结果卡段优先吃用户真实素材；缺素材时必须诚实 `blocked`
- 正式默认主线唯一 assembly 主路径固定为北京区 OSS + 云剪工程
- `local assembly` 已移出正式默认主线路由，不再作为 fallback / 兜底 / 应急正常交付
- 当前允许云端组装后人工上传；若缺密钥、缺云端参数或缺 provider implementation，必须如实标记 `待注入` / `待验证`
- pure PPT / 信息卡支路继续保留，但默认不再承担正式主承载
- AI talking avatar / 数字人口播若继续保留，只能作为可选 / 待验证支线
- 当前不把“只差平台 API”当项目成立前提
- 当前不把动态 PPT 写成现阶段正式主路径
- visual plan / preview 只能算辅助产物，不得写成 generation success
- 不得再把本地 preview / 本地 mp4 写成正式默认主线的 fallback、兜底或默认主交付路径

当前免费优先模型路线也已经明确：

- 少量辅助图片段可继续走：`wan2.6-image`
- 辅助视频段可继续走：`wan2.6-image -> wan2.7-i2v`
- 真人开口实验分支前置检测：`liveportrait-detect`
- 真人开口实验分支生成：`liveportrait`
- `wan2.6-image` 负责少量结果卡 / 背景 / 人像底图辅助生成
- 需要修图时走：`qwen-image-edit-plus`
- `wan2.7-i2v` 只承担辅助视频段，不再默认承担正式人物主承载
- `wan2.7-videoedit` 只用于后期修补 / 编辑增强，不是主生成模型
- `liveportrait` 只用于实验性固定背景 / 人物开口分支，且必须先过 `liveportrait-detect`
- 当前普通图片 / 视频辅助链 provider implementation 已接入：
  - `wan2.6-image` 会真实创建阿里异步任务、轮询并下载图片到本地 `dist`
  - `wan2.7-i2v` 当前默认作为辅助视频段的图生视频模型，执行口径改为先图后视频
- 真人开口实验分支仍只保留路线与语义：
  - `liveportrait-detect -> liveportrait` 仍未接入真实 provider implementation
  - 当前必须继续诚实 `blocked`

## 5A. 当前默认主线下的云剪第一轮目标

以下内容是当前第一轮云剪目标，不等于已经扩到动态 PPT：

- 人物判断段、自录过程段和结果卡段的统一时间线编排
- 字幕安全区
- 模板化 assembly
- 让云剪优先服务稳定交付，而不是把默认主线重新压回 pure PPT
- 不是动态 PPT
- 不是复杂 motion design
- 不是高成本视觉特效路线

## 5B. 当前北京区 OSS + 云剪外部已确认状态包

以下信息已被确认，可以作为当前执行层的正式上下文：

- OSS bucket：`zvip1-video-beijing`
- OSS region：`cn-beijing`
- OSS endpoint：`oss-cn-beijing.aliyuncs.com`
- OSS bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- OSS ACL：`private`
- RAM 项目专用用户：`video-factory-oss-1`
- IMS / ICE / 智能媒体服务区域：北京区
- 功能体验月包：已生效
- 体验包有效期：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 存储状态：正常
- 当前首个云剪工程：`video-factory-ppt-master-v1`
- 当前云剪工程状态：草稿
- 编辑器可打开：是

必须同时明确：

- AccessKey / Secret 已生成，但只保存在用户本地，不得写入 repo
- 当前代码与配置已经改为 cloud-only 主线
- 真实 cloud-only assembly 已在任务分支 `codex/round1` 成功跑通一次
- 当前真实成功证据已出现：
  - `project_id = a139456cf3334509b20192f3203d75bc`
  - `job_id = f45c6af448f44f0794f71ae9f26a1d1e`
  - `media_id = 47b0a400311c71f1a8c3e7f7d45b6302`
  - `output_url = oss://zvip1-video-beijing/video-factory/final/20260405T182130Z/formal_api_demo.mp4`
- 必须同时继续保持诚实：
  - 以上成功结果当前只成立于任务分支
  - 不等于 `codex/user-readable-map` 已同步
  - 当前已完成第一次成片初检，但初检结论不是“直接建议正式回流”
  - 当前更准确的状态是：
    - 任务分支导出成功
    - 成片初检仍需围绕“画面 demo 感偏重”继续做验收收口

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
11. 若涉及正式默认主线的人物判断 / 自录素材 / 轻 PPT 分工，再读 `project_source/19_human_self_footage_hybrid_mainline_rules.md`
12. 若涉及 pure PPT 次级支路风格、信息卡视觉、转场、字幕安全区或默认母版结构，再读 `project_source/17_white_collar_ppt_style_rules.md`
13. 若涉及默认主线 assembly 路径、OSS、云剪或旧 local fallback 语义，再读 `project_source/10_formal_api_demo_current_route_patch_20260402.md`

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
- 是否把 `local assembly` 再写回默认主路径
- 是否把 AI talking avatar / 数字人口播重新抬回默认主承载
- 是否把 pure PPT 次级支路重新偷换成默认主线
- 是否把动态 PPT 提前升格为当前目标
- 是否把云剪第一轮误写成动态 PPT / 复杂动效项目
- 是否把外部研究结论直接当成已采用事实
- 是否把用户模糊表达自动升格为长期规则
- 是否把“部分成立”的现实写成“已成立”
- 是否把项目脑判断偷换成执行层事实

## 11. 当前一句话执行前上下文

当前正式默认主线已切到“人物判断 + 用户自录素材 + 少量 PPT / 图片辅助”，正式组装继续统一走北京区 `OSS + 云剪工程` cloud-only；`local assembly` 已退出默认主线，AI talking avatar 不再承担默认主承载，pure PPT 只保留为次级支路，真实云端导出与真实素材注入仍待本地继续验证。
