# 20260524｜文案颗粒度配比机制补写

## 1. 本轮任务目标

`已确认` 本轮只把“素材颗粒度驱动文案机制”写入《视频工厂》项目规则，不写新第四期最终文案，不生成视频、音频、图片、成片或审片包。

目标是让后续 ChatGPT 写稿时不再只判断“顺不顺”，而是默认按 `copy_granularity_mixture_rule（文案颗粒度配比规则）` 同时检查：

- 顺口表达。
- 素材动作细节。
- 结果画面。
- 判断边界。

## 2. route_decision（路由判断）

```text
project_route = video_factory
task_type = project_file_change + mechanism_or_route_fix + copywriting_rule_update
responsibility_layer = entry_routing_layer + mechanism_fix_layer + execution_layer + validation_layer + sync_layer
selected_action = 局部补写文案颗粒度配比机制
forbidden_action = write_final_script / generate_video / advance_status / modify_material / modify_dist_media
large_task_gate.triggered = true
large_task_gate.reason = 多文件机制修补 + 规则文件 / 日志文件同步 + 验证 + commit/push
lane_recommendation = audit_lane -> standard_lane
lane_reason = 先审计现有 04 / 05 / 07 机制，再做局部补写
lane_invalid_if = 目标文件缺失、插入位置不清、写入会覆盖既有脏改
parallel_recommendation = serial_only
parallel_reason = 写入范围集中在核心文案机制文件，必须由 Codex Integrator 单点整合
parallel_invalid_if = 多执行器同时写 04 / 05 / 07 或 latest
write_owner = Codex Integrator only
read_only_lanes = DeepSeek readonly supply + local file audit
integration_owner = Codex
execution_permission = allowed_after_deepseek_supply_attempt
```

## 3. state_action_router（项目状态动作总控器）

```text
input_signal = 用户要求把“精彩重要处讲清素材颗粒度，普通处顺口”写成文案机制
current_project_state = formal_operation_active + mechanism_repair_needed + deepseek_supply_required
fact_source_arbitration.primary_source = GitHub/main 当前仓库文件
fact_source_arbitration.secondary_sources = codex_log/latest.md + 新第四期素材审计报告 + 用户本轮执行单
fact_source_arbitration.conflict_detected = false
trigger_mechanism = copy_granularity_mixture_rule + copy_granularity_mixture_gate + script_anchor_extraction_function
selected_action = update_copywriting_mechanism
forbidden_action = write_final_script / generate_video / content_validation promotion / send_ready promotion
done_when = 04 / 05 / 07 + latest + dated log 完成同步，验证通过，commit and push main
blocked_if = 关键文件缺失、插入点不清、误改禁止文件、规则仍无法回答什么时候顺口 / 什么时候必须颗粒度
feedback_update_required = latest + dated log + commit/push
```

## 4. DeepSeek 供料报告

供料任务卡：

- `已确认` 已按 DeepSeek gate 在本地创建供料任务卡并执行安全供料；本轮 main 提交范围按用户 allowed_changes 限定，只在本 dated log 留存供料摘要，不把 supply request 作为项目规则改动提交。

执行前供料结果：

- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `not_deepseek_conclusion = false`
- `token_usage_expectation_check = token_decrement_expected`
- `api_key_printed = false`
- `api_key_written = false`
- `env_file_read = false`
- `DeepSeek` 只读供料，不写文件、不拍板项目事实、不替代 Codex 原文件复核。

## 5. 影响面检查

`已确认` 04 / 05 / 07 已有相关但分散的规则：

- `GPT数据源/04_选题与文案规则.md` 已要求文案有判断、有人味、有动作，并且最终稿必须贴真实素材。
- `GPT数据源/05_文案路由规则.md` 已要求 Codex 素材细节报告、`material_evidence_gate（素材证据闸门）`、`script_anchor_extraction_function（文案锚点提取函数）` 和 `script_to_timeline_map（文案到时间线映射表）`。
- `GPT数据源/07_AI知识类视频价值规则.md` 已要求最终稿具体到真实操作细节和素材证据契约。

本轮判断：

- `已确认` 本轮是补充机制，不是替换原规则。
- `已确认` 新机制影响后续 ChatGPT 最终文案写作。
- `已确认` 新机制影响 Codex 素材细节报告：后续报告要支持素材颗粒度句的页面、动作、字段、结果。
- `已确认` 新机制影响 `content_route_card V2（内容路由卡 V2）`。
- `已确认` 新机制影响 `script_anchor_extraction_function（文案锚点提取函数）`。
- `已确认` 新机制影响 `script_to_timeline_map（文案到时间线映射表）`。
- `已确认` 新机制影响后续 Codex 视频执行前检查。

冲突检查：

- 与 `locked_copy_contract（锁定文案契约）` 不冲突；新机制只要求执行前标注和验收，不授权 Codex 改写锁定文案。
- 不误导 Codex 自己改写最终文案；需要语义变化时仍必须 `copy_change_request（文案修改请求）` 或 blocked。
- 已防止文案过度机械化：整篇都是操作细节、开头和过渡没有人味时也退回改稿。
- 已防止纯顺口缺细节继续过线：关键高光句缺素材动作细节时必须退回或 blocked。

## 6. 修改文件清单

- `GPT数据源/04_选题与文案规则.md`：新增 `6C. copy_granularity_mixture_rule（文案颗粒度配比规则）`。
- `GPT数据源/05_文案路由规则.md`：新增 `3B-1. copy_granularity_mixture_gate（文案颗粒度配比闸门）`，并补充 `script_anchor_extraction_function` / `script_to_timeline_map` 字段。
- `GPT数据源/07_AI知识类视频价值规则.md`：新增 `2A-1. 精彩点颗粒度价值标准`。
- `codex_log/latest.md`：顶部新增本轮记录。
- `codex_log/20260524_copy_granularity_mixture_mechanism.md`：新增本 dated log。

## 7. 机制摘要

`copy_granularity_mixture_rule（文案颗粒度配比规则）` 的核心是：文案表层顺口，但关键价值点必须落到素材颗粒度。

默认写作检查配比：

- `30% 顺口推进`
- `50% 素材颗粒度`
- `20% 判断、边界和下一步`

后续文案必须区分：

- `smooth_line（顺口推进句）`
- `material_granularity_line（素材颗粒度句）`
- `judgment_boundary_line（判断 / 边界句）`
- `result_transition_line（结果变化句）`

关键素材颗粒度包括：

- `Codex 在屏幕上打字`
- 点击确认
- 搜索商品
- 翻商品卡
- 记录商品名、价格、佣金、销量信号、店铺分、商品分、风险
- 生成云盘表格
- 回到聊天框给结论、理由、风险和下一步

## 8. 对后续 ChatGPT 写稿的影响

- ChatGPT 写稿时不再只看顺不顺。
- 关键句必须绑定素材动作、页面、字段、结果。
- 普通过渡、轻吐槽、观众心理和收尾可以顺口。
- 高光句必须有素材颗粒度。
- 缺素材时要降级成用户经验陈述、请求补素材、退回改稿或 blocked。
- 不允许用顺口文案遮盖素材不足。
- 不允许用机械细节毁掉开头、过渡和收尾的人味。

## 9. 对后续 Codex 执行的影响

- Codex 后续执行文案时，必须检查关键句是否绑定素材动作、真实页面、真实字段、真实表格、结果变化或回到聊天框结论。
- `script_anchor_extraction_function` 必须输出 `granularity_type / detail_density / material_detail_required / must_include_detail_types / allowed_smoothness / blocked_if_key_claim_without_material_detail`。
- `script_to_timeline_map` 必须携带同一组颗粒度字段。
- 关键主张缺素材细节时，不得进入视频执行；必须退回 ChatGPT 改稿、请求补素材或 blocked。
- Codex 仍不拥有最终文案改写权，不得自行改变 `locked_title / locked_opening_line / locked_final_script / core judgment / 人味表达`。

## 10. 禁止状态推进清单

- `content_validation = not_advanced`
- `send_ready = false`
- `publish_candidate_ready_for_human_review = not_advanced`
- `voice_validation = not_advanced`
- `visual_master_locked = false`
- `current_data_goal_anchor ready = not_advanced`
- `video_generated = false`
- `media_committed = false`

## 11. 验证结果

执行后验证结果：

- `markdown_read_check = passed`：04 / 05 / 07 / latest / dated log 均可正常读取。
- `keyword_check = passed`：已确认 `copy_granularity_mixture_rule / copy_granularity_mixture_gate / 素材颗粒度 / 顺口推进句 / 素材颗粒度句 / 判断 / 边界句 / 结果变化句 / Codex 在屏幕上打字 / 云盘表格 / 回到聊天框` 均已写入。
- `forbidden_file_check = passed_path_limited`：本轮提交范围限定为 04 / 05 / 07 / latest / dated log；不提交 `dist/`、`review_loop/`、`scripts/`、`codex_log/current_data_goal_anchor.md`、`GPT数据源/08_当前正式事实.md` 或 supply request 执行中间件。
- `media_file_check = passed`：未生成或提交视频、音频、图片、关键帧、contact sheet 或审片包。
- `secret_scan = passed_sanitized`：只出现 `api_key_printed=false / api_key_written=false / token_usage_expectation_check` 等安全状态字段；未写入真实 key、token、secret 或 Authorization 值。
- `status_promotion_check = passed`：本轮只写 `content_validation = not_advanced`、`send_ready = false`；没有推进 `publish_candidate_ready_for_human_review / voice_validation / visual_master_locked / current_data_goal_anchor ready`。
- `DeepSeek_pre_supply = deepseek_passed`：执行前安全供料通过，`fallback_status = not_used`。
- `DeepSeek_post_risk_review = attempted_blocked_invalid_context_pack`：写后风险复核已尝试，但 controller 因 `invalid_context_pack` 阻断；该输出保留为本地风险提示，`not_deepseek_conclusion = true`，不写成 DeepSeek 结论。
- `git_diff_check = passed`：`git diff --check` 通过。
