# 20260604｜16:9 社交编辑感卡片机制补丁

- `task_result.status = mechanism_repair_completed_no_video_generation`
- `target_delivery = social_editorial_card_v1_mechanism`
- `branch = main`
- `route_decision.project_route = video_factory`
- `route_decision.task_type = project_file_modification_task + mechanism_repair_task + routing_repair_task`
- `large_task_gate.triggered = true`
- `write_lane = serial_only`
- `visual_reference_image_readable = true`
- `approved_visual_reference = references/card_style/social_editorial_card_v1_reference.png`
- `historical_local_source_path = 素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png`
- `reference_path_corrected_by = codex_log/20260604_社交编辑感卡片参考图与DeepSeek后置复核补修.md`

## 20260604 补修说明

- 上一版日志中的 `素材录制/卡盘参考/ChatGPT Image 2026年6月4日 02_29_58.png` 只在本地存在，未进入 `origin/main`，不能继续作为 remote readable reference。
- 已改为 repo 内固定参考路径：`references/card_style/social_editorial_card_v1_reference.png`。
- 旧路径只保留为 `historical_local_source_path（历史本地来源路径）`，不得再写成远端可读默认路径。

## 已确认

- 已将后续正式运营卡片默认方向补为 `social_editorial_card_v1（社交编辑感卡片 V1）`。
- 默认比例为 `horizontal_16_9（横屏 16:9）`，默认分辨率为 `1920x1080`；旧 `vertical_9_16（竖屏 9:16）` 只保留为历史样片 / 历史提示卡 / 用户明确授权的竖屏任务口径。
- `judgment_card / summary_card / result_diff_card / prompt_tail_card` 已补职责、适用场景、密度规则、视觉质量判断、内容边界和失败路由。
- `card_placement_decision` 明确不固定旧 shot、不固定模板位置；按 `copy_function / evidence_window / result_diff / narrative_main_story_finished` 判断。
- `card_budget_gate` 明确按信息簇插卡，不按句子机械插卡；卡片密度不得高于真实证据密度。
- `card_visual_quality_gate` 明确卡片必须像横屏短视频里的社交编辑感视觉组件，而不是 PPT、机械游戏 UI、工程后台、HUD、赛博面板或低质模板。
- `card_failure_route` 已覆盖 `card_ratio_mismatch / card_aesthetic_issue / card_density_issue / card_evidence_interruption / card_text_semantic_mismatch / card_hyperframes_runtime_missing / card_reference_deviation`。
- `card_feedback_update` 明确机制文件、索引、latest、dated log、fixture 和 review note 的回写要求。

## 边界

- 本轮没有生成完整视频，没有修改任何最终视频成片。
- 本轮没有推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- 卡片视觉质量只属于 `pre-publish human quality gate（发布前人工质量闸门）`，不等于内容验证通过。
- 卡片只能辅助理解，不得替代中段真实录屏证据，不得新增素材里没有的数据、结论、平台指标或结果差。
- Codex 不得改写 locked copy；卡片文案需要语义修改时，必须输出 `copy_change_request（文案修改请求）`。
- 不得复用官方 Minecraft logo、字体、texture、model、sound 或可识别官方资产；体素 / 像素 / 方块元素只能做原创轻点缀。

## 修改入口

- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `codex_log/latest.md`

## DeepSeek 供料

- `pre_supply_request = codex_log/supply_requests/20260604_社交编辑感卡片机制_social_editorial_card_pre_supply_request.json`
- `pre_supply_pack = dist/deepseek_supply_controller/20260604_social_editorial_card_pre_supply/latest_supply_pack.md`
- `deepseek_actual_participation = deepseek_passed`
- `fallback_status = not_used`
- `not_deepseek_conclusion = false`
- `api_key_printed = false`
- `api_key_written = false`
- `token_usage_expectation_check = token_decrement_expected / not_available_user_check_required`
- `post_risk_review_request = codex_log/supply_requests/20260604_社交编辑感卡片机制_social_editorial_card_post_risk_review_request.json`
- `post_risk_review_pack = dist/deepseek_supply_controller/20260604_social_editorial_card_post_risk_review/latest_supply_pack.md`
- `post_risk_review.deepseek_actual_participation = not_attempted_policy_violation`
- `post_risk_review.blocked_reason = invalid_context_pack`
- `post_risk_review.not_deepseek_conclusion = true`
- `post_risk_review.api_key_printed = false`
- `post_risk_review.api_key_written = false`
- `post_risk_review_next_action = Codex local validation for status promotion / forbidden change / missed sync / fixture JSON / secret scan`

## Codex 本地验证

- `json_validation = passed`：`codex_source/fixtures/mechanism_inference_function_cases.json` 与本轮两份 `codex_log/supply_requests/*.json` 均可解析。
- `mechanism_grep_check = passed`：`social_editorial_card_v1 / card_visual_quality_gate / card_failure_route / card_feedback_update / card_budget_gate / prompt_tail_card / result_diff_card` 已命中本轮机制入口。
- `status_boundary_check = passed`：禁止状态推进窄匹配无命中；没有写入内容验证通过、可发送为真、视觉母版锁定、声音验证通过、最终声音验证为真或发布成功这类状态推进。
- `diff_check = passed`：`git diff --check` 无尾随空格或 whitespace error。
- `secret_scan = passed`：本轮 diff 未命中常见 API key / token 模式。
- `forbidden_path_check = passed`：本轮 diff 未修改视频 / 音频 / 图片媒体文件，未修改 `dist/latest_review_pack/` 或 `public/`。
- `not_tested = npm test`：当前 `package.json` 无 test script；本轮也未生成视频、未运行 HyperFrames runtime。

## 待验证

- 后续真实视频执行时，仍需按具体 locked copy、素材证据、line_group、subtitle overlap 和 HyperFrames runtime 状态逐片复核。
- 本机制通过不代表后续任意卡片自动美观通过；用户审美反馈仍是正式复审输入。
