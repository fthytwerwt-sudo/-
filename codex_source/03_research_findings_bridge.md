# 研究结论桥接

## 1. 文件定位

本文件用于把“会影响执行的外部结论或新拍板”桥接进 Codex 执行层。

本文件当前只保留“仍然有效、必须继续遵守”的桥接结论；历史细节统一以 Git 记录追溯。

## 2. 总规则

桥接硬规则 `已确认`：

- Perplexity 结果不会自动同步到 Codex
- ChatGPT 判断不会自动同步到 Codex
- GPT Project 数据源不会自动同步到 Codex 仓库
- 用户聊天里的新拍板，若未写入仓库文件或本轮执行单，不视为长期已同步事实

## 3. 当前有效桥接

### BRIDGE-20260409-01

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：GPT 数据源与 Codex 仓库不同步是当前必须正式写清的机制事实。
- 对项目的影响：新聊天不得把 GPT Project 数据源、聊天背景或外部资料自动当成仓库正式事实。
- 本轮执行必须遵守项：
  - 聊天里说过，不等于 Codex 已知
  - GPT 数据源里有，不等于 Codex 已知
  - 只有写进仓库文件，并同步到 `codex/user-readable-map`，才算新聊天默认正式已知
- 建议落点文件：
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/12_codex_known_state_three_layer_rules.md`
  - `codex_log/latest.md`

### BRIDGE-20260409-02

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：当前正式默认主线改为“人物 + 用户自己的真实录制素材 + 少量 PPT / 图片辅助”。
- 对项目的影响：项目脑、执行层、路由规则、接手口径都必须同步改写；pure PPT / 信息卡与 AI talking avatar / 数字人口播都不得继续写成默认主线。
- 本轮执行必须遵守项：
  - 结构跟着文案走
  - 人物出现 1 次还是 2 次，是 block 路由结果
  - 中段主体默认优先给真实素材承担
  - 北京区 `OSS + 云剪 cloud-only` 继续是正式 assembly 主路径
  - `local preview` / `local mp4` 只能算辅助
- 建议落点文件：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/16_presentation_routing_rules.md`
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

### BRIDGE-20260409-03

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：AI 知识类视频当前不能只说问题、只给观点、没有动作、没有证据，且 generation / assembly 成功不等于内容过线。
- 对项目的影响：进入样片执行前，必须先锁清“用户能做什么 / 能判断什么 / 证据是什么 / 最小行动或自检句是什么 / 结尾总结卡类型是什么”。
- 本轮执行必须遵守项：
  - 4 类内容不再共用一种价值交付
  - 4 类内容不再共用一种证据结构
  - 4 类内容不再共用一种结尾总结卡
- 建议落点文件：
  - `project_source/21_topic_selection_and_copywriting_rules.md`
  - `project_source/22_copy_mode_routing_rules.md`
  - `project_source/25_ai_knowledge_video_value_rules.md`
  - `codex_source/11_ai_knowledge_video_value_bridge.md`

### BRIDGE-20260409-04

- 来源类型：`用户新拍板`
- 状态：`已采用`
- 结论摘要：当前必须诚实区分“仓库口径已同步”与“新主线样片已验证成立”。
- 对项目的影响：这轮即使完成文档修复、日志更新、commit、push 和 reading branch 回流，也不能把结果写成样片已验证通过。
- 本轮执行必须遵守项：
  - 文档 / 规则 / 接手口径同步完成，只能写仓库口径已同步
  - 真实样片验证必须依赖样片与回审结果
- 建议落点文件：
  - `project_source/00_project_brief.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_log/latest.md`
