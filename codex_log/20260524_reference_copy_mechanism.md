# 20260524｜对标文案话语机制落库

## 1. 本轮任务目标

`已确认` 本轮只把用户确认的“对标文案话语机制”写入《视频工厂》的文案规则体系，让后续 ChatGPT 写稿默认从“普通人复杂问题救场”切入，而不是从工具功能介绍切入。

本轮不写新第四期最终文案，不生成视频 / 音频 / 图片，不修改素材，不提交第三方逐字稿全文，不推进内容状态。

## 2. route_decision（路由判断）

```text
project_route = video_factory
task_type = project_file_change + mechanism_route_fix + copywriting_mechanism_update + reference_quality_mechanism_landing
responsibility_layer = entry_routing_layer + project_judgment_layer + execution_layer + validation_layer + sync_layer + mechanism_fix_layer
selected_action = land_reference_copy_voice_mechanism
forbidden_action = write_final_script / generate_video / advance_status / commit_full_third_party_transcript
execution_permission = granted_after_read_ok_and_deepseek_supply_attempt
```

`large_task_gate（大任务闸门）`：

```text
triggered = true
reason = 本轮涉及 04 / 05 / 07 / latest / dated log 多文件机制修补和验证
lane_recommendation = standard_lane
lane_reason = 目标明确但影响后续文案默认机制，需要正常读取、写入、验证、日志和 Git 收尾
lane_invalid_if = 插入位置不安全 / 发现状态推进风险 / 发现完整逐字稿或媒体误提交风险
parallel_recommendation = serial_only
parallel_reason = 写入范围集中在核心机制文件，需 Codex Integrator 单点整合
parallel_invalid_if = 写入范围重叠、输出路径重叠、状态边界不清
write_owner = Codex Integrator only
read_only_lanes = DeepSeek readonly supply + local file audit
integration_owner = Codex
```

`DeepSeek 供料闸门`：

```text
supply_request_created = true
deepseek_call_attempted = true
deepseek_actual_participation = deepseek_passed
fallback_status = not_used
not_deepseek_conclusion = false
token_usage_expectation_check = token_decrement_expected
api_key_printed = false
api_key_written = false
env_file_read = false
multi_agent_runtime_validation = not_started
```

DeepSeek 本轮只读供料，不写文件、不拍板项目事实、不替代 Codex 原文件复核。供料临时目录仅作 local-only 执行输入，不纳入本轮提交。

## 3. state_action_router（项目状态动作总控器）

```text
input_signal = 用户要求把对标文案设置成以后默认文案机制，但结构不能写死
current_project_state = formal_operation_active + mechanism_repair_needed + reference_contract_needed + deepseek_supply_required
fact_source_arbitration = 用户本轮执行单 + GPT数据源/04/05/07 + reference audit / material audit + codex_log/latest
trigger_mechanism = reference_copy_voice_mechanism + reference_copy_voice_gate + copy_granularity_mixture_rule
selected_action = update_copywriting_mechanism
done_when = 04 / 05 / 07 + latest + dated log 完成同步并 push main
blocked_if = 关键文件缺失、插入位置不安全、误写固定 SOP、提交完整逐字稿、推进内容状态、无法 push main
```

## 4. 影响面检查

- `已确认` `GPT数据源/04_选题与文案规则.md` 已存在 `copy_granularity_mixture_rule（文案颗粒度配比规则）`。
- `已确认` `GPT数据源/05_文案路由规则.md` 已存在 `copy_granularity_mixture_gate（文案颗粒度配比闸门）`。
- `已确认` `GPT数据源/07_AI知识类视频价值规则.md` 已存在 `精彩点颗粒度价值标准`。
- `已确认` reference audit 报告存在：`12_chatgpt_handoff_pack.md`、`15_reference_vs_new_fourth_copy_gap.md`、`16_transcript_driven_chatgpt_handoff_pack.md`。
- `reference_audit_files_missing_but_user_confirmed_mechanism_provided_in_prompt = false`
- `已确认` 本轮应在已有颗粒度机制上补“对标话语机制”，不是替换已有规则。
- `已确认` 本机制影响后续 ChatGPT 最终文案写作、Reference-to-Execution Contract、`content_route_card V2（内容路由卡 V2）`、`script_anchor_extraction_function（文案锚点提取函数）` 和 `script_to_timeline_map（文案到时间线映射表）`。
- `已确认` 本轮不误导 Codex 直接写最终文案；Codex 只负责机制落库、验证、日志和 Git 收尾。
- `已确认` 本轮明确写入“结构不写死”，不得把 reference 结构机械固定成 SOP。
- `已确认` 本轮不提交对标逐字稿全文，只沉淀机制摘要和可继承话语功能。
- `已确认` 本轮不把文案机制误写成新第四期已经完成。

## 5. 用户确认的对标话语机制摘要

`reference_copy_voice_mechanism（对标文案话语机制）` 的核心是：最终文案先站在普通人 / 目标用户正在被复杂问题坑住的位置说话，再用案例、坑点细节、结果变化和低压判断引出 AI / Codex 的价值。

可继承：

- 说人话方式。
- 普通人处境起手。
- 复杂问题救场逻辑。
- 坑点细节。
- 案例推进。
- 能力定义。
- 低压收尾。

不可继承：

- 第三方逐字稿原句。
- 第三方案例结构。
- 第三方品牌表达。
- 第三方人物、画面、声音、字体、BGM、卡片皮肤或其他资产。
- 固定三案例结构或固定宏观趋势起手。

## 6. 修改文件清单

- `GPT数据源/04_选题与文案规则.md`：新增 `6D. reference_copy_voice_mechanism（对标文案话语机制）`。
- `GPT数据源/05_文案路由规则.md`：新增 `3B-2. reference_copy_voice_gate（对标文案话语闸门）`。
- `GPT数据源/07_AI知识类视频价值规则.md`：新增 `2A-2. 对标话语价值标准`。
- `codex_log/latest.md`：顶部新增 `20260524｜对标文案话语机制落库`。
- `codex_log/20260524_reference_copy_mechanism.md`：新增本 dated log。

## 7. 对后续 ChatGPT 写稿的影响

- ChatGPT 写稿时不再默认先写功能介绍。
- 必须先找到普通人面对的复杂问题和旧方法痛点。
- 必须把字段翻译成坑点细节，而不是平铺字段清单。
- 必须通过具体案例展示 AI / Codex 怎么救场。
- 必须在中段或结尾加入一句能力定义，把工具能力翻译成人话。
- 必须低压收尾：它不是自动赚钱，不是替你赌商品，只是先把混乱问题整理到能判断的状态。
- 必须按素材证据、reference pack、平台风险和观众理解路径动态调整结构。

## 8. 对后续 Codex 执行前检查的影响

- `content_route_card V2（内容路由卡 V2）` 需要检查文案是否从用户问题进入，而不是工具介绍进入。
- `script_anchor_extraction_function（文案锚点提取函数）` 需要补 `copy_voice_function（话语功能）`。
- `script_to_timeline_map（文案到时间线映射表）` 需要识别用户痛点句、旧方法坑点句、AI 救场句、坑点细节句、能力定义句和低压收尾句。
- 如果文案只有字段、没有坑点，必须退回改稿。
- 如果文案只有结构、没有人话，必须退回改稿。
- 如果文案照搬 reference 原句或机械复刻结构，必须 blocked 或退回改稿。
- 如果文案把初筛写成商业验证，必须 blocked。

## 9. 不写死结构的边界

`已确认` 本机制锁的是话语质量机制，不锁死结构。

后续每条内容仍要根据真实素材、reference pack、证据出现顺序、最强画面、平台风险、观众理解路径、本轮数据目标、是否先给结果预览、是否先现场录屏、是否多案例或单案例深挖来动态调整。

不得强制每条内容都有三个案例，不得强制每条内容先讲宏观趋势，不得把“趋势压力 -> 买房 -> 装修 -> 论文”之类 reference 结构写成固定 SOP。

## 10. 禁止状态推进清单

本轮不得推进：

- `content_validation（内容验证）`
- `send_ready（可发送状态）`
- `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`
- `voice_validation（声音验证）`
- `visual_master_locked（视觉母版锁定）`
- `current_data_goal_anchor ready（当前数据目标锚点 ready）`

## 11. skill 检查

- `copywriting-cn`：已读取。其“像人话、不过度夸张、不堆套话”原则适合作为本轮话语质量参考；本轮不直接写终稿。
- `writing-router-cn`：已读取。任务类型已明确为机制落库，不需要路由分流，因此未使用。
- `video-metadata-probe`：已读取。只适合视频文件技术验证；本轮不生成或验证视频，因此未使用。
- `skills/视频素材解析_video_material_audit/SKILL.md`：已读取。它适合素材审计；本轮只使用既有素材审计报告作为只读上下文，不重新解析素材。

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
commit_sha = pending
pushed_to_main = pending
```
