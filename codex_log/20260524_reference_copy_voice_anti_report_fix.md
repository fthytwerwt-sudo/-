# 20260524｜对标文案话语机制反报告腔修正

## 1. 本轮任务目标

`已确认` 本轮只修正 `reference_copy_voice_mechanism（对标文案话语机制）` 的表达风险：防止后续最终文案把后台检查字段、机制标签、路由说明写成前台口播。

本轮不写新第四期最终文案，不生成视频 / 音频 / 图片，不修改素材，不提交第三方逐字稿全文，不推进任何内容状态。

## 2. route_decision（路由判断）

```text
project_route = video_factory
task_type = project_file_change + mechanism_repair_needed + copywriting_mechanism_update + anti_report_voice_fix
responsibility_layer = mechanism_fix_layer + validation_layer + sync_layer
selected_action = add_anti_report_voice_fix_to_reference_copy_voice_mechanism
forbidden_action = write_final_script / generate_video / advance_status / commit_full_transcript
execution_permission = granted
```

`large_task_gate（大任务闸门）`：

```text
triggered = true
reason = 本轮涉及 04 / 05 / 07 / latest / dated log 多文件机制修补和验证
lane_recommendation = standard_lane
lane_reason = 目标明确，但影响后续 ChatGPT 默认写稿与 Codex 文案进入视频前检查
parallel_recommendation = serial_only
parallel_reason = 写入范围集中在核心机制文件，必须由 Codex Integrator 单点整合，避免共享文件冲突
write_owner = Codex Integrator only
read_only_lanes = local file audit + existing reference audit packs
integration_owner = Codex
```

`DeepSeek 供料闸门`：

```text
supply_request_created = false
deepseek_call_attempted = false
fallback_status = fallback_local_only
not_deepseek_conclusion = true
reason = 本轮无 DeepSeek 工具可调用，且用户把允许写入范围锁定为 5 个文件；不额外新增 supply_request 文件
```

## 3. state_action_router（项目状态动作总控器）

```text
input_signal = 用户指出 reference_copy_voice_mechanism 仍可能回到报告腔，要求改成真正说人话机制
current_project_state = formal_operation_active + mechanism_repair_needed
fact_source_arbitration = 用户本轮执行单 + GPT数据源/04/05/07 + codex_log/latest + reference audit / previous mechanism log
selected_action = update_copywriting_mechanism
done_when = 04 / 05 / 07 + latest + dated log 完成同步并 push main
blocked_if = 无法安全插入、关键文件缺失、误推进状态、把后台标签写成前台稿、提交完整逐字稿或媒体文件
```

## 4. 影响面检查

- `已确认` `GPT数据源/04_选题与文案规则.md` 已存在 `reference_copy_voice_mechanism（对标文案话语机制）`。
- `已确认` `GPT数据源/05_文案路由规则.md` 已存在 `reference_copy_voice_gate（对标文案话语闸门）`。
- `已确认` `GPT数据源/07_AI知识类视频价值规则.md` 已存在 `对标话语价值标准`。
- `已确认` 本轮是补 `anti_report_voice_fix（反报告腔保护层）`，不是推翻上一轮对标话语机制。
- `已确认` 本轮不误导 Codex 自己写新第四期最终文案；Codex 只做机制修补、检查、日志和 Git 收尾。
- `已确认` 本轮明确后台验收字段不得出现在前台文案，防止 `copy_voice_function` 被误用成最终稿结构。
- `已确认` 本轮不照搬对标原文，不提交第三方完整逐字稿。
- `已确认` 本轮不把机制修补写成新第四期内容通过。

## 5. 为什么上一轮机制仍需修正

上一轮 `reference_copy_voice_mechanism（对标文案话语机制）` 已经把“普通人复杂问题、旧方法痛点、AI / Codex 救场、坑点细节、能力定义、低压收尾”写入规则，方向是正确的。

风险在于：05 文件新增了 `copy_voice_function（话语功能）` 和一组检查字段，后续 ChatGPT 或执行检查如果把这些字段当作前台段落标题，就会把文案带回“项目报告腔 / 说明书腔 / 结构标签腔”。这会让对标机制失效，因为对标稿真正可继承的是说话方式，不是字段结构。

## 6. 修改文件清单

- `GPT数据源/04_选题与文案规则.md`：新增 `6D.9 前台口播转换规则：后台标签不得出现在最终稿`。
- `GPT数据源/05_文案路由规则.md`：新增 `3B-2A. anti_report_voice_gate（反报告腔话语闸门）`。
- `GPT数据源/07_AI知识类视频价值规则.md`：新增 `2A-2A. 反报告腔价值标准`。
- `codex_log/latest.md`：顶部新增 `20260524｜对标文案话语机制反报告腔修正`。
- `codex_log/20260524_reference_copy_voice_anti_report_fix.md`：新增本 dated log。

## 7. 新增反报告腔机制摘要

- 后台检查字段只用于验收，不是最终稿结构。
- 最终稿不得出现“用户痛点句 / AI 救场句 / 能力定义句”等标签化段落。
- 最终稿不能写成机制解释、项目报告、路由说明或字段说明。
- 最终稿必须把检查字段转成自然口播链条。
- 坑点细节必须嵌入句子，让观众感到具体风险，不做字段清单。
- AI / Codex 必须作为救场工具出现，不先做产品介绍。
- 如果最终稿读起来像机制字段串联，即使字段都齐，也判为不通过。

## 8. 对 ChatGPT 后续写稿的影响

- ChatGPT 写稿时不能把 `user_pain_line / ai_rescue_line / ability_definition_line` 写成段落名。
- 先讲普通人为什么卡住，再让 AI / Codex 自然出现。
- 字段必须翻译成坑点，嵌入口播句子。
- 工具动作必须放进案例里，不做孤立功能介绍。
- 结果变化要听起来像观众利益，不像项目汇报。
- 低压边界仍保留：AI 初筛不是商业验证，不替用户拍板。

## 9. 对 Codex 后续执行检查的影响

- Codex 检查文案时可以使用 `copy_voice_function（话语功能）` 和 `anti_report_voice_check（反报告腔检查）`，但这些字段不得进入前台文案。
- 命中报告腔、字段串联、标签化输出时，Codex 只能退回改稿、输出 `copy_change_request（文案修改请求）` 或 blocked。
- Codex 不能自行把最终文案重写成新稿。
- 通过 `anti_report_voice_gate（反报告腔话语闸门）` 不代表 `content_validation（内容验证）` 通过，只表示文案话语不再明显报告腔。

## 10. 禁止状态推进清单

本轮不得推进：

- `content_validation（内容验证）`
- `send_ready（可发送状态）`
- `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`
- `voice_validation（声音验证）`
- `visual_master_locked（视觉母版锁定）`
- `current_data_goal_anchor ready（当前数据目标锚点 ready）`

## 11. skill 检查

- `copywriting-cn`：已读取，用作“像人话、不堆套话”的话语质量参考；本轮不直接写终稿。
- `writing-router-cn`：已读取；任务已明确为机制修补，不启用分流。
- `video-metadata-probe`：已读取；本轮不生成或验证视频，因此不使用。
- `skills/视频素材解析_video_material_audit/SKILL.md`：已读取；本轮不重新解析素材，只作为素材证据边界参考。
- `reference 专用 skill`：未找到独立匹配项；本轮以仓库内 reference audit 文件和用户确认机制为事实源。

## 12. 验证结果

```text
keyword_check = passed
forbidden_file_check = passed
media_file_check = passed
transcript_commit_boundary_check = passed
secret_scan = passed
status_promotion_check = passed
git_diff_check = passed
```

## 13. commit / push 信息

```text
branch = main
commit_message = Prevent reference copy voice rules from becoming report-style scripts
commit_sha = pending_until_commit
pushed_to_main = pending_until_push
```
