# 研究结论桥接

## 1. 文件定位

本文件用于把“会影响执行的外部结论或新拍板”桥接进 Codex 执行层。

它负责收纳：

- Perplexity 调研结论
- ChatGPT 判断后的执行性结论
- 用户新拍板
- 因真实执行偏差而升级进执行层的长期结论

它不负责：

- 代替项目脑定义项目身份
- 代替当前任务的详细实施步骤
- 代替完成回报

## 2. 什么时候必须写入本文件

凡是满足以下两个条件的内容，都必须先写入本文件，或在本轮执行单中显式带入：

1. 来源是 Perplexity / ChatGPT 判断 / 用户新拍板 / 执行偏差升级
2. 该结论会影响 Codex 的读取、执行、验证、回报或后续默认判断

未满足这两个条件的内容，不必强行写入本文件。

## 3. 来源类型

本文件统一使用以下来源类型：

- `Perplexity`
- `ChatGPT 判断`
- `用户新拍板`
- `执行偏差升级`

补充原则：

- Perplexity 默认提供资料与备选，不自动等于最终拍板
- ChatGPT 判断不会自动同步到 Codex
- 用户聊天里的新拍板，若未写入本文件或未在当前执行单中明确带入，也不视为长期已同步事实

## 4. 状态定义

每条桥接结论必须带状态，不允许裸写结论。

- `待验证`
  - 已进入执行层视野，但还没有被当前轮正式采用
- `已采用`
  - 当前执行层必须遵守
- `部分采用`
  - 只采用其中一部分，或只在当前阶段成立
- `待本轮执行验证`
  - 已允许进入本轮执行，但结果还要靠真实运行或改动验证
- `已被偏差覆盖`
  - 原结论已被执行现实修正，不得继续按旧版本默认执行
- `已失效`
  - 结论不再成立，仅保留历史记录价值

## 5. 单条记录硬字段

每条记录至少包含以下字段：

- `记录编号`
- `来源类型`
- `状态`
- `结论摘要`
- `对项目的影响`
- `原计划需要改哪里`
- `本轮执行必须遵守项`
- `暂未确认项`
- `建议落点文件`

推荐写法如下：

```text
### BRIDGE-YYYYMMDD-序号
- 来源类型：
- 状态：
- 结论摘要：
- 对项目的影响：
- 原计划需要改哪里：
- 本轮执行必须遵守项：
- 暂未确认项：
- 建议落点文件：
```

## 6. 录入规则

### BRIDGE-001：影响执行的外部结论不自动同步

必须明确：

- Perplexity 结果不会自动同步到 Codex
- ChatGPT 判断不会自动同步到 Codex
- 用户新拍板不会自动变成长期执行事实

只有以下两种情况，Codex 才能把它当成已知：

1. 已写入本文件
2. 已在本轮执行单中被明确写出且不超出当前轮范围

否则 Codex 不得假设已知。

### BRIDGE-002：来源与采用权必须分开写

必须区分：

- 谁提出了这个结论
- 当前执行层是否已经采用

例如：

- Perplexity 可以给路线参考，但默认状态应是 `待验证`
- ChatGPT 可以完成收束，但若未进入执行层文件，Codex 不能默认长期知道
- 用户明确拍板后，才可以写成 `已采用` 或 `待本轮执行验证`

### BRIDGE-003：执行偏差可反向升级进本文件

若真实执行发现：

- 原想法只部分成立
- 原方案前提已失效
- 某个资源 / 权限 / 接口限制会持续影响后续执行

则必须先按 `codex_source/05_execution_deviation_and_reality_sync.md` 判断影响范围；
若会影响后续默认执行，再把偏差升级写入本文件，并把旧结论改为 `已被偏差覆盖` 或 `已失效`。

## 7. 当前已录入桥接结论

### BRIDGE-20260402-01

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：凡是来自 Perplexity / ChatGPT 判断 / 用户新拍板且会影响执行的结论，不能只停在聊天框里，必须先写入本文件或在本轮执行单显式带入。
- 对项目的影响：Codex 以后不能再把外部结论、研究收束和聊天拍板默认当成长期已知背景。
- 原计划需要改哪里：补齐执行层桥接机制，并把读取顺序与执行前置判断写回 `codex_source/01_execution_rules.md`。
- 本轮执行必须遵守项：若结论尚未进入本文件或本轮执行单，Codex 不得假设已知。
- 暂未确认项：后续是否需要把本文件再拆成“当前有效 / 历史归档”双区。
- 建议落点文件：
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - 本文件

### BRIDGE-20260402-02

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：执行中若因资源、权限、环境、依赖、接口、成本、素材质量或外部服务偏差导致原方案无法按想法落地，必须触发正式回写机制，不能继续把旧方案当成立。
- 对项目的影响：执行现实从此不再只是“当前回复里的说明”，而是会反向改写执行层事实与原方案状态。
- 原计划需要改哪里：新增偏差回写文件，并把“发现偏差后写到哪里、如何改标状态”写回执行总规则。
- 本轮执行必须遵守项：发现执行现实与原方案不一致时，不得假装原方案仍成立。
- 暂未确认项：不同类型偏差的长期归档频率，后续可再细化。
- 建议落点文件：
  - `codex_source/05_execution_deviation_and_reality_sync.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/04_completion_and_review_contract.md`

### BRIDGE-20260402-03

- 来源类型：`用户新拍板`
- 状态：`已被 BRIDGE-20260405-01 覆盖`
- 结论摘要：该条记录反映的是 2026-04-02 时的旧口径：主路径默认仍走本地 assembly，cloud assembly 只是后续增强项。
- 对项目的影响：仅保留为历史桥接记录，不再作为当前正式执行事实。
- 原计划需要改哪里：执行前上下文必须显式写清当前主路径和当前不做事项。
- 本轮执行必须遵守项：任何新任务如果与该主路径冲突，必须先回到项目脑和执行层规则重新确认。
- 暂未确认项：无；后续正式口径已由 BRIDGE-20260405-01 接管。
- 建议落点文件：
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

### BRIDGE-20260405-01

- 来源类型：`用户新拍板`
- 状态：`已被 BRIDGE-20260405-02 覆盖`
- 结论摘要：该条记录反映的是 2026-04-05 上半轮的旧升级口径：主线已切到 OSS + 云剪优先，但仍保留 local fallback。
- 对项目的影响：仅保留为过渡历史记录，不再作为当前正式执行事实。
- 原计划需要改哪里：当前执行前上下文、项目脑与代码主线必须继续收口到 cloud-only。
- 本轮执行必须遵守项：不得再把该条记录误读为“local fallback 仍然合法”。
- 暂未确认项：无；当前正式口径已由 BRIDGE-20260405-02 接管。
- 建议落点文件：
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

### BRIDGE-20260405-02

- 来源类型：`用户新拍板`
- 状态：`已被 BRIDGE-20260408-03 部分覆盖`
- 结论摘要：pure PPT / 信息卡主线从 cloud-first 正式升级为 cloud-only；北京区 OSS + 云剪工程成为唯一 assembly 主路径，`local assembly` 不再保留为 fallback / 兜底 / 应急正常交付。
- 对项目的影响：执行层、项目脑、配置示例、组装脚本、assembly gate、result summary 和测试都必须同步移除 `local fallback` 合法性；缺密钥、缺云端参数或缺 provider implementation 时，必须如实标记 `待注入` / `待验证`，不得再用本地 mp4 补位。
- 原计划需要改哪里：当前执行前上下文、formal_api_demo 路线补丁、config example、assembly 主线代码、测试断言、latest log 与执行日志都必须同步改口，并把北京区 OSS / IMS / 云剪工程状态包桥接回仓库。
- 本轮执行必须遵守项：这次升级只适用于纯 PPT / 信息卡主线；动态 PPT 仍暂不考虑；数字人继续并行修但不阻塞主线；云剪第一轮仍只服务转场统一、字幕安全区与模板化 assembly。
- 暂未确认项：AccessKey / Secret 仅保存在用户本地，尚未进入 repo；正式云端导出仍待本地注入密钥后验证；provider assembly implementation 当前仍未真实跑通。
- 建议落点文件：
  - `codex_source/02_current_execution_context.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `codex_log/latest.md`

### BRIDGE-20260405-03

- 来源类型：`执行偏差升级`
- 状态：`已采用`
- 结论摘要：北京区 OSS / IMS / 云剪工程的外部状态包已确认：bucket=`zvip1-video-beijing`、region=`cn-beijing`、endpoint=`oss-cn-beijing.aliyuncs.com`、bucket_domain=`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`、ACL=`private`、RAM 用户=`video-factory-oss-1`、IMS storage=`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`、云剪工程=`video-factory-ppt-master-v1`、状态=`草稿`、编辑器可打开。
- 对项目的影响：repo 可以直接写入非密钥的北京区 OSS / IMS / 云剪工程参数；用户本地只需要补 AccessKey / Secret 即可继续推进真实云端导出验证。
- 原计划需要改哪里：config example、current execution context、latest log 与 formal_api_demo 路线补丁必须写清这些字段已确认，且不能再继续使用 `space_name` / `template_id` 旧占位。
- 本轮执行必须遵守项：AccessKey / Secret 不得写入 repo；当前真实边界必须保留为“待本地注入密钥后验证真实云端导出”。
- 暂未确认项：真实云端导出成片成功回执、任务 ID、资源 ID、output ID 仍待本地注入密钥后验证。
- 建议落点文件：
  - `config/formal_api_demo.example.toml`
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

## 8. 2026-04-07 role handoff 样片回审桥接

### BRIDGE-20260407-01

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：45 秒 role handoff 样片这轮回审已正式收束为以下执行口径：
  - 当前最主要问题层是 `表现层`
  - 次主要问题层是 `字幕与配音节奏层`
  - 当前更根本的问题不是“转场不好看”，而是“画面没有承担信息推进”
  - 当前唯一最优先改点是：把整页静态切换改成“跟着旁白推进的分步 reveal + 关键词显影节奏”
  - 第二优先才是：把 `bounce / 回弹` 替换为更稳的直切 / 轻推进 / 轻淡入淡出
  - 第三优先才是：建立固定字号层级，让每页只有 1 个主判断被视觉突出
- 对项目的影响：下一轮不得再把重点放在重做整条、扩主线或平均发力；回审与执行单都应收口到“画面是否承担信息推进”。
- 原计划需要改哪里：
  - 新增稳定判断层文件，明确当前场景下的视觉动效与信息密度规则
  - 生成只围绕 `分步 reveal + 关键词显影节奏` 的下一轮修改单草稿
  - 刷新 `latest.md`，让新会话默认能读到这轮收束口径
- 本轮执行必须遵守项：
  - 不得把“替换 bounce”误写成当前第一优先
  - 不得把“画面信息太少”直接误判为“画面文字不够多”
  - 不得把这轮收束结论写成长期已成立规律
- 这轮不要误改的方向：
  - 不重做整条视频
  - 不改项目主线
  - 不改 case
  - 不把回审结论扩写成新的长期路线
- 这些结论如何落到下一轮执行：
  - 下一轮先只改每页的信息出现顺序
  - 让关键词、结果句、局部高亮跟着旁白分拍出现
  - 先证明“画面开始承担信息推进”，再讨论稳转场与字号层级的第二轮修正
- 暂未确认项：具体 reveal 节奏如何映射到每一页、每句旁白和每个停顿点，仍待下一轮按实际片段落执行单。
- 建议落点文件：
  - `project_source/18_visual_motion_and_information_density_rules.md`
  - `codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md`
  - `codex_log/latest.md`

### BRIDGE-20260407-02

- 来源类型：`Perplexity`
- 状态：`部分采用`
- 结论摘要：以下内容属于“这轮已收束采用的外部参考”，当前允许作为下一轮判断依据，但不等于项目天然已确认事实：
  - `bounce / 回弹` 类动效容易带来模板感、课件感、样机感，不适合当前知识类 / AI 类 / PPT 信息卡母版
  - 画面信息太少，本质不一定是字少，更可能是：
    - 视觉层级没建立
    - 视觉证据不够
    - 页面变化太少
    - 画面与旁白断连
  - 当前高性价比且适合该项目的可看性增强手法优先为：
    - 分步 reveal
    - 关键词显影
    - 结果句 / 数字强调
    - 局部高亮 / 框选
    - 停顿点设计
  - 当前不建议的方向包括：
    - 粒子 / 发光 / 3D 炫技
    - 把旁白全文搬到画面上
    - 全页同时强化多个重点
    - 为了可看性乱加素材填时间
    - 套营销广告式快节奏
- 对项目的影响：当前可以把这些外部参考作为“如何增强可看性”的辅助判断，但不能越权写成长期稳定规则，也不能盖过用户已拍板的问题层排序。
- 原计划需要改哪里：
  - 在稳定判断层文件里把这些内容显式标记为 `外部参考`
  - 在下一轮修改单中只借用其中与 `分步 reveal + 关键词显影节奏` 直接相关的部分
- 本轮执行必须遵守项：
  - 引用这些内容时，必须注明它们是“已收束采用的外部参考”
  - 不得把外部参考直接升级为“项目长期已确认规律”
- 这轮唯一最优先改点：
  - 仍然是 `分步 reveal + 关键词显影节奏`
- 这些结论如何落到下一轮执行：
  - 用它们约束下一轮的视觉增量，只允许做低成本、高信息推进收益的修正
  - 不允许借“增强可看性”之名把片子改成花哨动效片
- 暂未确认项：这些参考对其他时长、其他展示路由、其他人群场景是否仍然成立，后续需逐条视频再验证。
- 建议落点文件：
  - `project_source/18_visual_motion_and_information_density_rules.md`
  - `codex_log/20260407_role_handoff_review_bridge_and_next_round_draft.md`

## 9. 一句话规则

会影响执行的外部结论，只有在本文件或本轮执行单里被显式桥接后，Codex 才能把它当成已知并据此执行。

## 10. 2026-04-08 写汇报翻车 45 秒样片桥接

### BRIDGE-20260408-01

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：本轮正式主题不再是泛化 AI 吐槽，也不是教工具技巧；而是白领真实职场失败痛点：“我明明用了 AI，怎么最后还是自己重写了一遍？”当前固定主场景为“让 AI 写汇报 / 周报材料，发给领导前才发现全是套话”，正式内容源固定采用“版本 A”口播文案，不得擅自切到 B / C 或重新发散版本。
- 对项目的影响：本轮 case、脚本、字幕、manifest、样片和回审都必须围绕“写汇报看起来能交，最后发现根本不能直接交”的失败体验展开，不能做成工具说明、AI 教程、产品销售片或纯观点吐槽。
- 原计划需要改哪里：
  - 新建当前主题的独立 45 秒 case，而不是静默覆盖现有 `cases/formal_api_demo.md`
  - 在执行层日志中明确写清本轮采用的是“版本 A”口播文案
  - 若正式主链 blocked，必须把 blocker 写到执行日志和 `latest.md`
- 本轮执行必须遵守项：
  - 核心情绪固定为“不是 AI 没用，而是它写得太像对的了，害你以为可以直接交”
  - 主场景固定为“AI 写汇报 / 周报，发给领导前才发现全是套话”
  - 当前场景模式固定为：
    - 主场景：`AI 方法分享`
    - 辅助理解：`AI 问题拆解 / 真实工作失败场景`
  - 当前默认服务的心理机制固定为：
    - `身份命中 / 自我代入`
    - `认知减负`
    - `自我效能感`
    - `最小行动`
  - 不得把这条内容做成泛化焦虑、空洞说教或讲功能说明
- 暂未确认项：
  - 当前正式主链是否具备本轮需要的 DashScope API Key / TTS voice，仍待真实执行验证
  - 若正式主链 blocked，本轮 local preview 只能算辅助验收件，不能冒充正式主链完成态
- 建议落点文件：
  - `cases/ai_report_fluff_trap_45s.md`
  - `codex_log/latest.md`
  - 本轮执行日志

### BRIDGE-20260408-02

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：本轮 45 秒样片必须吸收已拍板的外部研究结论，但这些结论当前只对这条样片和这类纯 PPT / 信息卡母版成立，不自动升级为长期项目规律。当前默认优先手法为：`分步 reveal`、`关键词显影`、`结果句 / 数字句强调`、`局部高亮 / 框选`、`停顿点设计`；当前默认避免：`bounce / 回弹类转场`、`粒子 / 发光 / 3D 炫技`、`把旁白全文搬到屏幕上`、`一页同时强化多个重点`、`为了更可看乱加素材填时间`。
- 对项目的影响：本轮视觉层任务不是“更花哨”，而是承担信息推进、建立视觉层级、显影前后变化；若画面、字幕、转场和配音发生冲突，必须优先服从“命中真实失败体验 / 让前后变化可见 / 让用户一眼看懂哪里不对”。
- 原计划需要改哪里：
  - 当前主题的 case 必须显式写出“前后差值”“表面正确 vs 项目真实为空”“可以交了 -> 其实要重写”的视觉意图
  - 本轮样片若有辅助预览，必须按 6–8 张信息卡去做 reveal 节奏，而不是整页静态切换
  - 执行日志和 `latest.md` 必须明确写清这轮采用了哪些外部研究结论
- 本轮执行必须遵守项：
  - 当前最主要问题层按 `表现层` 理解
  - 当前视觉默认走“白领咨询报告感 / 体面专业感 / 信息高效感”
  - 总体结构优先按 4 段推进、总卡数控制在 6–8 张
  - 重点句必须被画面接住，而不是只靠旁白说明
- 暂未确认项：
  - 当前这套 reveal / 显影口径对其他主题、其他时长是否仍然成立，后续要逐条视频验证
  - 当前正式主链若缺 provider 配置，是否只能先落 local-only 预览样片，仍待真实运行判定
- 建议落点文件：
  - `cases/ai_report_fluff_trap_45s.md`
  - `codex_log/latest.md`
  - 本轮执行日志

### BRIDGE-20260408-03

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：项目正式默认主线从“pure PPT / 信息卡主承载”切到“人物 + 用户自己的真实录制素材 + 少量 PPT / 图片辅助”；正式 assembly 继续固定为北京区 OSS + 云剪 cloud-only；AI talking avatar / 数字人口播因口型、性别、动作和文案匹配风险，不再承担默认主承载。
- 对项目的影响：项目脑、执行层、formal_api_demo case、route_plan、manifest、config example、review 模板和日志口径都必须同步改写；pure PPT 只能保留为次级支路，不再是默认主线；若缺真实素材，只能诚实写成“待素材注入验证”，不得伪造已跑通。
- 原计划需要改哪里：
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `codex_source/02_current_execution_context.md`
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `cases/formal_api_demo_human_self_footage.md`
  - `scripts/generate_formal_api_demo.py`
- 本轮执行必须遵守项：
  - 人物承担开头命中、关键判断、收束 / 最小行动
  - 用户自己的真实录制素材承担现场感、过程感、证据感
  - 少量 PPT / 图片只负责关键词显影、前后对比、结果句 / 数字句收束和局部说明
  - AI talking avatar / 数字人口播若继续保留，只能作为可选 / 待验证支线
  - 正式 assembly 不得回退到 local fallback
- 暂未确认项：
  - 当前仓库只完成了“路由 / schema / case / config 占位与最小执行入口”层面的收口
  - 真实人物素材、自录素材和结果卡是否已经全部注入并完成正式云端导出，仍待本地继续验证
- 建议落点文件：
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `config/formal_api_demo.example.toml`
  - `codex_log/latest.md`

### BRIDGE-20260408-04

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：这轮要求把 GPT Project 最新已拍板口径正式同步进 Codex 侧入口文件、执行前上下文、bridge 与 latest。当前 Codex 侧必须明确：默认主线是“人物 + 用户真实录制素材 + 少量 PPT / 图片”；人物出现 1 次还是 2 次由 block 路由决定；中段主体默认优先给真实录制素材承担；`AI talking avatar / 数字人口播` 当前不是默认主线。
- 对项目的影响：新会话不得再因为旧 `AGENTS` / `00` / `02` / `latest` 口径而把项目误读为 pure PPT 默认主线，也不得继续把 talking avatar 当成默认人物层。
- 原计划需要改哪里：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_log/latest.md`
- 本轮执行必须遵守项：
  - 正式 assembly 继续固定为北京区 OSS + 云剪 `cloud-only`
  - `local preview / local mp4` 只能作为辅助存在，不得写成正式默认交付
  - GPT 侧新主线已桥接进 Codex 侧，不等于“已用真实素材稳定出片验证完成”
- 暂未确认项：
  - 当前新版主线的真实素材注入与正式云端导出，仍待后续真实执行验证
- 建议落点文件：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

## 11. 2026-04-09 GPT Project 价值规则桥接

### BRIDGE-20260409-01

- 来源类型：`用户新拍板`
- 状态：`已被 BRIDGE-20260409-02 覆盖`
- 结论摘要：GPT Project 侧已新增 / 重写 4 份正式规则文件，用于收紧 AI 知识类视频的价值底线、选题 / 文案口径、文案路由和上位内容价值线。当前 Codex 侧必须正式采用以下新增判断：
  - AI 知识类视频默认不能只说问题、只给观点、没有动作、没有证据、没有最小行动 / 自检句
  - generation / assembly 成功，不等于内容已过线
  - AI 项目讲解 / AI 方法分享 / AI 学习实操 / AI 案例拆解 不再共用一种价值交付、证据结构和结尾总结卡
  - 默认结尾卡映射固定为：
    - `AI 项目讲解 -> judgment_card + 最小行动`
    - `AI 方法分享 -> steps_error_card`
    - `AI 学习实操 -> steps_card + 自检句`
    - `AI 案例拆解 -> judgment_card + 可迁移句`
- 对项目的影响：Codex 后续在写脚本、做 block 路由、选结尾总结卡、判断样片是否值得进入执行、做样片验收时，不能再沿旧口径理解项目，必须先锁清“用户看完后能做什么 / 能判断什么 / 证据是什么 / 最小行动或自检句是什么”。
- 原计划需要改哪里：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
- 本轮执行必须遵守项：
  - 当前桥接依据来自 GPT Project 正式摘要，已经是 Codex 执行层正式口径
  - 但它不自动等于“当前仓库 project_source 已全部同步完成”
  - 更不自动等于“已通过样片验证成立”
- 暂未确认项：
  - 当时桥接落下时，`project_source/21/22/25` 仍未补回当前分支
  - 后续已由 `BRIDGE-20260409-02` 接管
- 建议落点文件：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`

### BRIDGE-20260409-02

- 来源类型：`执行偏差升级`
- 状态：`已采用`
- 结论摘要：这轮已把 `project_source/21_topic_selection_and_copywriting_rules.md`、`project_source/22_copy_mode_routing_rules.md`、`project_source/25_ai_knowledge_video_value_rules.md` 真实补回当前任务分支，并与 `project_source/08_quality_baseline_and_90_score_rules.md` 一起构成当前分支完整的 AI 知识类价值口径；因此 Codex 侧不再应把 `21/22/25` 写成“当前分支缺失”。
- 对项目的影响：当前状态已从“Codex 条件已知”提升为“当前分支正式已知”；但是否提升为“主读取分支正式已知”，仍取决于是否成功同步回 `codex/user-readable-map`。
- 原计划需要改哪里：
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_log/latest.md`
  - 新增 `codex_source/12_codex_known_state_three_layer_rules.md`
- 本轮执行必须遵守项：
  - 不得再把 `project_source/21/22/25` 写成当前分支缺失
  - 不得把“当前分支正式已知”偷换成“主读取分支正式已知”
  - 不得把规则已入正文写成“样片已验证成立”
- 暂未确认项：
  - 是否已成功同步回 `codex/user-readable-map`
- 建议落点文件：
  - `project_source/21_topic_selection_and_copywriting_rules.md`
  - `project_source/22_copy_mode_routing_rules.md`
  - `project_source/25_ai_knowledge_video_value_rules.md`
  - `codex_source/12_codex_known_state_three_layer_rules.md`
  - `codex_log/latest.md`
