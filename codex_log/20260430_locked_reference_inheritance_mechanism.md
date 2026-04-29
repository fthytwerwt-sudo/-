# 20260430｜锁定参考继承机制修补

## 1. 本轮目标

- `已确认` 本轮只建立 `locked_reference_inheritance（锁定参考继承机制）`。
- `已确认` 本轮不生成新视频，不修改现有视频，不创建成片候选。
- `已确认` 本轮不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不修改 `content_validation`。
- `已确认` 本轮不修改 `send_ready`。

## 2. 读取结果

- `已确认` 已读取 `AGENTS.md`。
- `已确认` 已读取 `codex_source/00_codex_readme.md`。
- `已确认` 已读取 `codex_source/01_execution_rules.md`。
- `已确认` 已读取 `codex_source/12_codex_known_state_three_layer_rules.md`。
- `已确认` 已读取 `codex_log/latest.md`。
- `已确认` 已读取 PR #14 / PR #15 / PR #7 / PR #8 相关 summary、timeline、cut_map、review_manifest、layout / quality / editing inheritance 报告或对应可读材料。
- `已确认` 已读取 `dist/latest_review_pack/summary.json`、`dist/latest_review_pack/review_manifest.md`、round34 相关日志与当前正式事实。
- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已检查并使用全局相关 skills：`using-superpowers`、`context-driven-development`、`verification-before-completion`、GitHub 相关技能说明。

## 3. 现有机制审计

已搜索关键词：

- `locked_reference`
- `reference_inheritance`
- `样板继承`
- `锁定参考`
- `reference registry`
- `visual master`
- `成片母版`
- `字幕规范`
- `TTS 参考继承`
- `zoom reference`
- `放大方式继承`
- `style inheritance`
- `inheritance report`

审计结论：

- `已确认` 未发现现有 locked reference registry。
- `已确认` 未发现完整成片必须输出 locked reference inheritance report 的硬规则。
- `已确认` 未发现“局部样板确认后，完整成片默认继承，否则 blocked”的统一机制。
- `已确认` 仓库已有 reference pack、声音候选、current_publish_target、latest_review_pack 等相近机制，但它们不能阻止完整成片阶段重新换风格。

结论：

`locked_reference_inheritance_missing（缺少锁定参考继承机制）`

## 4. 本轮新增 / 修改

新增：

- `codex_source/14_locked_reference_inheritance_rules.md`
  - 中文备注：锁定参考继承规则。
  - 写入内容：定义、状态、晋升条件、三层已知关系、默认继承、强制读取、继承报告、summary 字段、blocked 条件、禁止行为。
- `codex_source/locked_reference_registry.md`
  - 中文备注：锁定参考登记表。
  - 写入内容：初始 registry、候选 / 失败 / 历史 reference、确认状态字段、更新规则。
- `codex_log/20260430_locked_reference_inheritance_mechanism.md`
  - 中文备注：本轮机制修补日志。

修改：

- `codex_source/00_codex_readme.md`
  - 接入完整成片 / 候选片 / 样片回炉 / 字幕 / TTS / 卡片 / 放大 / 剪辑 / 视觉母版修正的 locked reference 前置读取链路。
- `codex_source/01_execution_rules.md`
  - 接入 locked reference 读取顺序、继承报告、summary 字段和 blocked 条件。
- `codex_log/latest.md`
  - 刷新最新执行摘要。

## 5. 初始 registry 内容

`已确认` 当前没有任何 reference 被登记为 `locked`。

已登记为 `candidate`：

- `middle_editing_round34_candidate_20260425`
  - round34 中段剪辑语法候选。
  - 依据：用户反馈中段“现在中段没什么问题了”。
  - 限制：只代表中段暂定收束，不代表所有后续中段剪辑语法已锁定。
- `sassy_card_pr7_a_candidate_20260428`
  - PR #7 A 版骚萌卡视觉候选。
  - 限制：PR #7 A 版进入技术预览，不等于用户确认“以后骚萌卡按这个走”。
- `sassy_card_three_type_rules_pr8_candidate_20260428`
  - PR #8 三类骚萌卡规则候选。
  - 限制：PR #8 是 draft / 条件已知，未合并前不能写主读取分支正式已知。
- `tts_15s_b_pacing_candidate_20260427`
  - 20260427 B 版 15 秒停顿梗感 TTS 节奏候选。
  - 限制：用户偏好方向已记录，但不是最终成片音轨锁定标准。

已登记为 `failed`：

- `subtitle_pr15_v2_failed_20260430`
  - PR #15 v2 字幕失败或待复盘参考。
- `layout_pr15_v2_failed_20260430`
  - PR #15 v2 layout / 背景风格失败或待复盘参考。
- `tts_pr15_v2_failed_20260430`
  - PR #15 v2 TTS 缺失失败参考。

已登记为 `historical`：

- `historical_api_demo_clean_sample_20260412`
  - 历史通过样片参考。
  - 限制：历史通过不等于当前 vNext locked reference。

## 6. 后续强制规则

凡任务命中以下类型，必须先读：

1. `codex_source/14_locked_reference_inheritance_rules.md`
2. `codex_source/locked_reference_registry.md`

命中类型：

- 完整成片
- 成品候选片
- 技术预览升级成候选片
- 样片回炉
- 开头重做
- 中段剪辑
- 字幕修正
- TTS 修正
- 功能卡修正
- 结果差卡修正
- 骚萌卡修正
- 录屏放大修正
- 视觉母版修正

完整成片 / 成品候选片 / 样片回炉必须输出：

- `locked_reference_inheritance_report.md`

summary 必须写：

- `locked_reference_registry_read`
- `locked_reference_inheritance_validation`
- `locked_reference_inheritance_report`
- `unapproved_reference_changes`
- `reference_deviation_blockers`
- `candidate_references_used`
- `locked_references_used`

## 7. blocked 条件

以下情况必须 blocked：

- 找不到 locked reference 规则或 registry。
- 找不到已锁定 reference。
- 没有读取 locked reference registry。
- 继承失败或只有“类似”描述，没有对照证据。
- 字幕、TTS、放大、卡片、剪辑语法与 locked reference 不一致。
- 用户没有授权但 Codex 自行换风格、重做或替换。
- 完整片使用 candidate reference 却写成 locked reference。
- 失败 PR 的局部元素被误继承成正式参考。
- 只有 `technical_validation` 或 `content_validation`，没有 `reference inheritance validation`。

## 8. 状态说明

- `已确认` 本轮在工作分支建立机制和 registry。
- `待验证` 本机制合并或同步回 `codex/user-readable-map` 后，才算主读取分支正式已知。
- `待验证` 当前 registry 中所有 candidate 都需要用户 / ChatGPT 后续明确确认，才能升级为 locked。

## 9. 下一个目标

下一轮应由用户 / ChatGPT 复审 registry 中哪些候选 reference 可以升级为真正的 `locked_reference`，并为完整成片建立第一批锁定参考。
