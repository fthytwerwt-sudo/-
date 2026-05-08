# 锁定参考继承规则 locked_reference_inheritance_rules

## 1. 文件定位

本文件是《视频工厂》执行层的锁定参考继承机制。

它解决的问题是：

- 局部样板已经被用户 / ChatGPT 调对并确认；
- 后续完整成片却没有继承；
- Codex 重新解释、重新生成、重新换风格；
- 完整片再次漂移。

本文件只规定机制，不代表任何新视频已经通过。

## 2. 现有机制审计结论

`locked_reference_inheritance_missing（缺少锁定参考继承机制）`

已审计关键词：

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

- `已确认` 仓库已有 reference pack、声音参考锚点、当前审片包、current_publish_target 等相近机制。
- `已确认` 这些机制能说明某些参考材料、当前样片状态、声音候选方向或审片入口。
- `已确认` 这些机制没有形成统一的 locked reference registry。
- `已确认` 这些机制没有规定“局部样板被确认后，完整成片必须默认继承”。
- `已确认` 这些机制没有规定完整成片必须输出 locked reference inheritance report。
- `已确认` 这些机制没有把未继承 locked reference 写成 blocked 条件。

因此，本轮新增独立机制文件，并配套 `codex_source/locked_reference_registry.md`。

## 3. locked_reference 定义

`locked_reference（锁定参考）` 指：

用户 / ChatGPT 已明确认可、后续完整成片默认必须继承的局部样板或效果。

可锁定的 reference 类型包括但不限于：

- `opening_reference（开头参考）`
- `middle_editing_reference（中段剪辑参考）`
- `zoom_reference（放大方式参考）`
- `subtitle_reference（字幕参考）`
- `function_card_reference（功能卡参考）`
- `result_diff_card_reference（结果差卡参考）`
- `sassy_card_reference（骚萌卡参考）`
- `tts_reference（TTS 节奏参考）`
- `ending_reference（结尾参考）`
- `visual_master_reference（视觉母版参考）`

## 4. reference 状态

registry 中必须区分以下状态：

| 状态 | 中文备注 | 使用规则 |
| --- | --- | --- |
| `candidate` | 候选参考 | 可用于复审、对照、试继承，但不得写成用户已确认。 |
| `locked` | 锁定参考 | 后续完整成片默认必须继承。 |
| `failed` | 失败参考 | 只能作为反例或复盘材料，不得默认继承。 |
| `deprecated` | 废弃参考 | 已被明确替换，不得继续使用。 |
| `historical` | 历史参考 | 可帮助理解演化，不能自动等同当前标准。 |

确认状态必须另行标注：

| confirmation_state | 中文备注 | 写入条件 |
| --- | --- | --- |
| `candidate_reference_pending_confirmation` | 候选参考，待确认 | 有产物或证据，但没有明确锁定确认。 |
| `locked_reference_confirmed_by_user` | 用户确认的锁定参考 | 用户明确说后续按此继承。 |
| `locked_reference_confirmed_by_chatgpt` | ChatGPT 复审确认的锁定参考 | ChatGPT 明确复审通过并建议后续默认继承。 |
| `locked_reference_formal_synced` | 已同步主读取分支的锁定参考 | locked reference 已进入 `main`。 |
| `failed_or_pending_reference` | 失败或待复盘参考 | 用户指出不符合，或关键口径仍待复盘。 |
| `candidate_or_rule_reference` | 候选规则参考 | 规则草案、PR 草案或当前任务条件已知。 |

硬规则：

- 候选参考不得写成锁定参考。
- 失败样片里的局部元素不得自动写成锁定参考。
- PR 自评 `pass_for_candidate_review` 不等于用户确认。
- ChatGPT / 用户没有明确说“以后默认按这个走”时，不能写 `locked`。

## 5. 晋升为 locked_reference 的条件

一个局部样板必须同时满足以下条件，才能从普通参考升级为 `locked_reference`：

1. 有明确 `artifact_path（产物路径）`。
2. 有可复审的 `evidence_path（证据路径）`，例如截图、contact sheet、video clip、音频文件、时间线或报告。
3. 有用户或 ChatGPT 明确确认。
4. 有 `applies_to（适用范围）`。
5. 有 `does_not_apply_to（不适用范围）`。
6. 有 `inheritance_rule（继承方式）`。
7. 有 `allowed_changes（允许修改范围）`。
8. 有 `blocked_if（阻断条件）`。
9. 已写入 `codex_source/locked_reference_registry.md`。
10. 如需成为新聊天默认正式已知，必须同步回 `main`。

如果任何字段无法确认：

- 字段写 `待确认`；
- status 不得写 `locked`；
- confirmation_state 不得写 `locked_reference_confirmed_by_user`、`locked_reference_confirmed_by_chatgpt` 或 `locked_reference_formal_synced`。

## 6. 和三层已知状态的关系

本机制必须服从 `codex_source/12_codex_known_state_three_layer_rules.md`。

状态对应关系：

- 聊天里说过，最多先算 `GPT 已知`。
- 当前执行单带入，最多先算 `Codex 条件已知`。
- 写入当前工作分支并 commit / push，才算 `当前分支正式已知`。
- 合并或同步回 `main`，才算 `主读取分支正式已知`。

禁止混淆：

- 不能把 GPT 已知直接写成主读取分支正式已知。
- 不能把当前 PR 草案直接写成主读取分支正式已知。
- 不能把 `candidate` 写成 `locked_reference_formal_synced`。
- 不能把失败 PR 的局部元素登记成正式继承样板。

## 7. 默认继承规则

一旦某项进入 `locked_reference`：

- 后续完整成片默认继承；
- Codex 不得自行替换；
- Codex 不得自行重做；
- Codex 不得自行换风格；
- Codex 不得只写“类似”；
- Codex 必须输出继承对照证据；
- Codex 必须在 summary 中写 `locked_reference_inheritance_validation`。

只有以下情况可以不继承：

1. 用户明确说本轮不需要这个位置。
2. 用户明确要求换风格。
3. 用户明确要求重做。
4. 素材缺失并被标记为 blocked。
5. 当前任务类型与该 reference 明确不适配。
6. 当前任务明确是探索新 reference，不是完整成片。

## 8. 完整成片类任务强制前置读取

凡任务命中以下任一类型，必须先读取本文件和 registry：

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

强制读取文件：

1. `codex_source/14_locked_reference_inheritance_rules.md`
2. `codex_source/locked_reference_registry.md`

如果任一文件读不到：

- 必须 blocked；
- 不得直接生成完整片；
- 不得写成成片候选完成。

## 9. 完整成片输出要求

完整成片 / 成品候选片 / 样片回炉任务完成时，必须输出：

`locked_reference_inheritance_report.md（锁定参考继承报告）`

报告必须逐项写：

- `reference_id`
- reference 名称
- reference 状态
- reference 路径
- 适用位置
- 本轮是否继承
- 本轮落点
- 对照截图 / 音频 / 时间码
- 是否有偏差
- 偏差是否经用户授权
- 是否通过

没有 `locked_reference_inheritance_report.md`：

- 不得写成成片候选完成；
- 不得把当前片子写成可发送状态；
- 不得只用 `technical_validation` 或 `content_validation` 替代继承验证。

## 10. summary 必填字段

以后完整成片 / 候选片 summary 必须增加：

- `locked_reference_registry_read`
- `locked_reference_inheritance_validation`
- `locked_reference_inheritance_report`
- `unapproved_reference_changes`
- `reference_deviation_blockers`
- `candidate_references_used`
- `locked_references_used`

不得只写：

- `technical_validation`
- `content_validation`

## 11. blocked 条件

以下任一情况必须 blocked：

- 找不到已锁定 reference。
- 没有读取 locked reference registry。
- 继承失败。
- Codex 自行换风格。
- Codex 只写“类似”，没有对照证据。
- 字幕、TTS、放大、卡片、剪辑语法与 locked reference 不一致。
- 用户没有授权但 Codex 自行重做。
- 只有技术验证，没有 reference inheritance validation。
- 完整片使用 candidate reference 却写成 locked reference。
- 失败 PR 的局部元素被误继承成正式参考。
- registry 字段缺失却仍声称继承通过。

## 12. 禁止行为

禁止：

- 把候选 reference 写成已确认 reference。
- 把失败 reference 写成默认继承样板。
- 把 PR 自评 pass 写成用户确认。
- 把局部样板的“可参考”写成“全片必须复刻”。
- 把当前分支新增 registry 写成主读取分支已同步，除非已经同步回 `main`。
- 在没有用户授权时重做已锁定位置。

## 13. 继承报告最低验收

Codex 做完整成片时，必须在最终汇报里明确：

1. 本轮读取了哪些 locked reference 文件。
2. registry 中哪些 locked reference 命中本轮任务。
3. 哪些 locked reference 被继承。
4. 哪些 candidate reference 被使用，且为何不能写成 locked。
5. 有没有偏差。
6. 偏差是否经用户授权。
7. 是否存在 blocked。

若存在 blocked，必须停止成片完成声明，并把 blocked 写入 summary 和执行日志。
