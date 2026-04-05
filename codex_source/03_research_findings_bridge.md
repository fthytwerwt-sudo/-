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
- 状态：`已采用`
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

## 8. 一句话规则

会影响执行的外部结论，只有在本文件或本轮执行单里被显式桥接后，Codex 才能把它当成已知并据此执行。
