# V002 复盘到文案调整桥接 review to copy revision bridge

## 文件定位

- 本文件承接 V002《自动流的最简单流程》的发布后复盘结论。
- 本文件把复盘结论转成 V002b 安全版文案结构草案。
- 本文件不是 V002 原始数据记录。
- 本文件不是 V002b 最终正式脚本。
- 本文件不生成视频、不进入发布准备。

## V002 样本判断

- sample_decision = reference_abnormal_sample（可参考异常样本）
- reason：播放数据被平台减推污染，不能作为自然流量样本；但点赞率和收藏率显示小样本兴趣信号强。
- source_facts（来源事实）：
  - play_count（播放量）= 39
  - like_count（点赞数）= 5
  - favorite_count（收藏数）= 8
  - distribution_status（分发状态）= policy_distribution_limited（平台审核减推 / 分发受限）
  - abnormal_sample_status（异常样本状态）= abnormal_distribution_sample（异常分发样本）

## V002 问题层判断

- main_problem_layer = platform_risk + publish_packaging（平台风险 + 发布包装）
- secondary_problem_layer = copy_structure + footage_carrier（文案结构 + 录屏承载）
- status = 部分成立 / 待确认
- Codex 边界：以上是结构化桥接判断，不是最终内容拍板；最终问题层与 V002b 是否采用仍交给 ChatGPT / 用户确认。

## V002 文案结构状态

- copy_structure_status = not_locked（文案结构未锁定）
- reason：
  - 主结构待验证。
  - 开头钩子待验证。
  - 结尾动作缺失。
  - 录屏承载未和文案结构绑定。
  - 安全版文案结构未生成。

## V002b 修订目标

- revision_target = publish_packaging_and_copy_structure（发布包装 + 文案结构）
- 主变量：发布包装 / 风险表达。
- 辅助变量：文案结构安全化。
- 说明：平台风险词替换必须和开头、结尾、画面文字同步改，不能只改单个标题。
- 状态：draft_pending_chatgpt_user_confirmation（草案，待 ChatGPT / 用户确认）

## V002b 安全文案方向

### 核心判断句候选

1. AI 工作流最难的不是工具，而是顺序。
2. 我复盘了一次真实 AI 工作流，发现最容易踩坑的是流程顺序。
3. AI 不是一键替你做完，而是先帮你少走重复步骤。

### 标题候选

1. 我用 AI 复盘了一次真实工作流，最容易错的是顺序
2. AI 做流程不是一键完成，真正麻烦的是这几步
3. 我试着用 AI 拆一个视频流程，发现难点不在工具

### 开头钩子

- 我今天不讲一键自动化，只复盘一次真实 AI 工作流。
- 这条我只看一个问题：AI 到底能不能减少重复步骤？

### block 结构

1. 开头判断：AI 工作流难点不是工具，是顺序。
2. 真实问题：很多人一上来就堆工具，结果流程更乱。
3. 录屏证据：展示自己的演示工作台如何拆步骤。
4. 结果差：从一团操作变成可复用步骤。
5. 收束：先把顺序理出来，再谈自动化。

### 录屏承载

- 录屏只证明真实过程。
- 不展示下载入口。
- 不展示第三方软件引导。
- 不展示“自动化生产流 / 生成成片 / 运营物料导出”等高风险词。
- 命令行不作为开头第一屏。
- 工具界面需要遮挡 URL、账号、下载入口、敏感信息。

### 风险词替换

| 原表达 | 安全替换方向 |
| --- | --- |
| 自动流 | 真实工作流复盘 |
| 自动化生产流 | 搭流程踩坑 |
| 批量生成 | 减少重复步骤 |
| 生成成片 | 整理出一版初稿 / 草稿 |
| 运营物料导出 | 发布素材整理 |
| 第三方软件 | 我的工作台 / 演示环境 |

### 结尾动作

- 下一条我继续拆：这套流程里最容易翻车的一步。
- 这条先讲顺序，下一条我拆输入怎么写才不跑偏。

### 禁止结尾

- 私信领取
- 评论区打 1
- 加我
- 主页联系方式
- 工具包发你
- 想要自动流找我

## 发布前检查

- V002b 进入发布前，必须跑 `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md（发布前平台风险检查规则）`。
- 若结果为 hard_block 或 rewrite_required，不得发布。
- 只有 allowed 或 caution 且已完成改写，才允许进入发布准备。

## 下一轮执行包草案

- 下一轮目标：产出 V002b 安全版内容表达文案结构，不生成视频。
- 完成标准：安全标题、开头、block、录屏承载、结尾、风险词替换全部齐。
- 后续由 ChatGPT / 用户确认后，再进入 Codex 成片执行。

## blocked_items（阻断项）

- 未确认 V002b 结构前，不得写成最终正式脚本。
- 未完成发布前平台风险检查前，不得进入发布准备。
- 若检查结果为 hard_block 或 rewrite_required，不得发布。
- 若录屏素材无法遮挡 URL、账号、下载入口或敏感信息，不得进入成片执行。
- 若需要修改 V002 原始数据、`content_validation（内容验证）`、`send_ready（可发送状态）`、`current_publish_target（当前发布目标）` 或 `dist/latest_review_pack/（最新复审包）` 才能继续，则必须 blocked。
