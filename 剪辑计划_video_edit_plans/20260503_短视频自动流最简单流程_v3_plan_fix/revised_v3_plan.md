# 《短视频自动流的最简单流程》V3 修正版执行计划

## 1. 任务目标

`已确认` 本计划只服务下一轮执行判断，不生成视频、音频、图片，不调用 API，不调用云剪，不调用 HyperFrames 渲染，不 commit，不 push，不创建 PR。

本计划修正旧 V3 plan 的核心偏差：不要把“正式主线四件套”机械理解成“本轮必须一次性真实跑通所有能力，否则一律 blocked”。下一轮执行必须先判断样片等级，再决定能否 render。

## 2. 当前背景

- 项目：`《视频工厂》`
- 仓库：`fthytwerwt-sudo/-`
- 主读取分支：`codex/user-readable-map`
- 唯一正式本地工作区：`/Users/fan/Documents/视频工厂`
- 当前样片基线：`v3.1`
- `latest_review_pack`：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- `content_validation`：`pending_user_chatgpt_review` 或灰度测试中，不能写成 `passed`
- `send_ready`：`false`
- `voice_validation`：`pending_user_chatgpt_review`
- `final_voice_validated`：`false`

## 3. 样片等级裁决

下一轮执行前必须先输出 `sample_level_decision.md`，并按以下等级裁决：

| 样片等级 | 定义 | 是否可写主线候选 |
| --- | --- | --- |
| `mainline_inheritance_candidate` | API 生成真人 / 主持壳、项目 TTS / custom voice、visual route、locked reference、真实云端剪辑、用户录制素材主体推进、信息卡辅助全部成立 | 可以 |
| `flow_proof_sample` | 用户录制素材能证明豆包 -> Trae -> 项目骨架 -> Codex 检查流程，但 API 主持壳 / 云剪 / 项目 TTS 有部分未完整跑通 | 不可以写主线候选 |
| `technical_flow_sample` | 只证明装配链路、素材可用、视频可解码，不证明内容有效或样片口径成立 | 不可以写内容样片 |
| `blocked` | 用户目标要求主线候选，但关键能力缺失、关键规则读不到、样片等级无法判断或会造成事实误写 | 不可 render |

`已确认` 当前用户目标更接近 `mainline_inheritance_candidate`。
`部分成立` 仓库已有流程证据、视觉路由、locked reference、云剪候选链路历史报告。
`待验证` API 主持壳 runtime、完整项目 TTS、V3 云剪实跑是否可用于本条 V3。
因此下一轮默认 render gate 不是直接 mainline ready，而是 `blocked_need_user_decision`。

## 4. 必读文件

下一轮执行必须先读：

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/current_local_artifact_paths.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
- `dist/latest_review_pack/locked_reference_inheritance_report.md`
- `dist/latest_review_pack/video_metadata_probe_report.json`
- `dist/latest_review_pack/*timeline*.json`
- `dist/latest_review_pack/*cut_map*.md`
- `codex_source/14_locked_reference_inheritance_rules.md`
- `codex_source/locked_reference_registry.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`

分支来源文件必须标明来源分支：

- `codex/vnext-recorded-material-intake-20260503`：素材采集汇报、素材清单、推荐装配输入。
- `codex/vnext-material-detail-recapture-20260503`：素材细节复采、豆包到 Trae 流程证据、ChatGPT 文案输入。
- `codex/short-video-auto-flow-script-pack-20260503`：旧文案包和旧分段承载表。
- `codex/short-video-auto-flow-v2-video-sample-20260503`：PR #41 失败参考。
- `codex/short-video-auto-flow-v21-render-20260503`：PR #42 失败参考。

## 5. 执行前检查

下一轮执行必须先生成或更新以下计划文件，不得直接 render：

- `sample_level_decision.md`
- `block_segment_carrier_map.md`
- `script_to_visual_carrier_map.md`
- `visual_route_plan.md`
- `locked_reference_inheritance_plan.md`
- `hyperframes_motion_plan.md`
- `hyperframes_motion_validation_report.md`
- `render_ready_gate.md`

## 6. 文案保真要求

- 完整文案语义必须保真。
- 可为了 TTS 停顿、字幕断句做最小标点和分段适配。
- 不得删掉用户关键判断。
- 不得把完整文案全压到信息卡。
- 不得让主持壳长时间连续讲解。
- 不得把完整文案全交给 TTS 而缺少画面推进。

## 7. script_to_visual_carrier_map 要求

必须逐段写：

- `script_section_id`
- 原文摘要
- 主要画面承载
- 是否需要字幕
- 是否需要信息卡
- 是否需要 HyperFrames
- 对应素材 / 卡片 / 主持壳
- 证明点
- 不能证明点
- 是否可删减
- 是否必须保留
- 是否适合作为口播
- 是否适合作为信息卡

## 8. block_segment_carrier_map 要求

必须逐个 block / segment 写：

- `block_id`
- `segment_id`
- 文案范围
- 主要承载
- 辅助承载
- 是否需要信息卡
- 信息卡职责
- 不生成信息卡的原因
- 证明点
- 不能证明点
- 是否会抢主叙事

硬规则：用户录制素材承担主体推进；信息卡只服务关键词、结构整理、状态边界、转场和总结。

## 9. API 生成真人 / 主持壳要求

不得把 `formal_api_demo` 文件名直接等同于 API 生成真人 / 主持壳链路。

只有同时找到以下内容，才能写 API 主持壳可用：

- 可执行入口
- 输入参数
- 输出路径
- 使用的模型 / API
- 最近一次成功报告或最小验证证据
- 与当前 vNext 主持壳方向的匹配关系

如果只找到 `formal_api_demo` 文件名或历史技术路线，必须写 `missing_api_human_runtime`。若用户目标保持 `mainline_inheritance_candidate` 且该项缺失，则 blocked。若用户确认降级为 `flow_proof_sample`，可继续，但必须标记 `degraded_no_api_human`。

## 10. TTS / API 配音要求

- 优先使用项目 API TTS / custom voice。
- 可参考 `tts_15s_b_pacing_locked_20260427` 的节奏，但不得写最终音色已验证。
- `voice_validation` 必须保持 `pending_user_chatgpt_review`。
- `final_voice_validated` 必须保持 `false`。
- 若下一轮是 `mainline_inheritance_candidate`，必须真实生成完整口播配音。
- 若下一轮是 `flow_proof_sample`，可不生成项目 TTS，但必须标记 `degraded_no_project_tts` 并由用户授权。

## 11. 用户录制素材要求

用户录制素材承担主体推进，至少包含：

- `豆包素材.mp4` `00:00:16-00:00:24`：一句简单需求。
- `豆包素材.mp4` `00:01:28-00:02:00`：豆包拆流程。
- `豆包素材.mp4` `00:02:40-00:04:08`：豆包生成 Trae prompt。
- `trae 素材.mp4` `00:00:32-00:01:04`：进入 Trae SOLO。
- `trae 素材.mp4` `00:01:20-00:01:52`：prompt 进入 Trae 并 plan。
- `trae 素材.mp4` `00:02:00-00:02:40`：项目骨架。
- `codex 素材.mp4` `00:02:56-00:03:08`：Codex 检查。

不得写成：Trae 代码已运行成功、API 已接通、云剪稳定、Codex 已证明内容过线。

## 12. 少量 PPT / 信息卡要求

信息卡数量由承载映射决定，不固定 8 张。信息卡只允许承担：

- 关键词显影
- 状态边界
- 工位解释
- 转场
- 总结

信息卡不得替代真实录屏主叙事，Prompt 引用尾卡不得承担主结尾。

## 13. HyperFrames card_motion_layer 要求

HyperFrames 当前定位：

- `card_motion_layer`：允许。
- `new_visual_route`：禁止。
- `middle_recording_overlay_layer`：禁止。
- `full_video_generation_layer`：禁止。
- `cloud_editing_replacement`：禁止。

只允许三类 motion：

- `data_or_result_diff_card_motion` -> `cute_info_card_route`
- `prompt_tail_card_motion` -> `cute_info_card_route`
- `sassy_reaction_card_motion` -> `sassy_reaction_card_route`

不得接入用户录制素材中段，不得做录屏动态标注、包装框、叠层，不得替代真实录屏、云端剪辑或 API 主持壳。

## 14. visual route 要求

- 段落提示卡：`cute_prompt_card_route`
- 信息卡 / 结果差卡 / Prompt 引用尾卡：`cute_info_card_route`
- 情绪反应卡 / 骚萌卡：`sassy_reaction_card_route`

每张卡必须写 `card_id`、`card_role`、`assigned_route`、`why_this_route`、`forbidden_route`、是否使用 HyperFrames、`motion_id`。

## 15. locked reference 继承要求

必须检查：

- `opening_reference_element_doll_no_text_locked_20260428`
- `tts_15s_b_pacing_locked_20260427`
- `cute_info_card_route_locked_20260501`
- `cute_prompt_card_route_locked_20260501`
- `sassy_card_pr7_b_visual_locked_20260501`
- `visual_master_voxel_element_doll_candidate_20260430`
- `middle_editing_round34_locked_20260425`
- `middle_zoom_reference_confirmed_middle_preview_20260430`

candidate 不得写成 locked；失败 PR 的局部元素不得写成 locked；PR 自评 pass 不得写成用户确认。

## 16. 云端剪辑要求

若下一轮目标是 `mainline_inheritance_candidate`：

- 必须真实执行阿里云 OSS + ICE / 云剪链路。
- 不得用本地预览冒充。
- 无法执行则 `blocked_missing_cloud_assembly`。

若下一轮目标是 `flow_proof_sample`：

- 可以不真实调用云剪。
- 必须写 `cloud_assembly_status = not_executed_this_round`。
- 必须写 `sample_type = flow_proof_sample`。
- 必须写 `send_ready = false`。
- 不得写云剪正式稳定。

PR #36 / PR #37 只能证明云剪候选链路曾跑通，不能证明本轮 V3 已执行云端总装。

## 17. 火山引擎 API 特写 / 脱敏要求

火山引擎素材未脱敏前不得入片。若下一轮要尝试 API 特写，必须先抽取安全局部并遮挡手机号、验证码、API Key、资源 ID、账号、URL、任何敏感信息。不能确认安全时使用 API 信息卡 fallback。

API 特写不能证明 API 已接通。

## 18. 输出文件要求

下一轮 render 前，必须先存在并通过检查：

- `sample_level_decision.md`
- `block_segment_carrier_map.md`
- `script_to_visual_carrier_map.md`
- `hyperframes_motion_plan.md`
- `hyperframes_motion_validation_report.md`
- `visual_route_plan.md`
- `locked_reference_inheritance_plan.md`
- `render_ready_gate.md`

若进入 render，按样片等级另行决定是否生成媒体文件。

## 19. 验证要求

本计划修正轮只验证计划文件：

- 10 个 Markdown 文件存在。
- 没有视频、音频、图片生成。
- 没有 API、云剪、HyperFrames 调用。
- 没有 commit、push、PR。
- `render_ready_gate.md` 明确下一轮 render 等级和是否需要用户确认降级。

## 20. 状态字段

下一轮默认状态边界：

- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`

仅当所有 mainline 门槛真实通过，才可写：

- `sample_type = mainline_inheritance_candidate`
- `full_mainline_candidate = pending_user_chatgpt_review`

若降级：

- `sample_type = flow_proof_sample`
- `cloud_assembly_status = not_executed_this_round`
- `degraded_no_api_human` / `degraded_no_project_tts` 按实际写入

## 21. blocked 条件

出现以下任一情况，不得进入 mainline render：

- 读不到主线锚点。
- 读不到 HyperFrames 边界报告。
- 读不到视觉路由规则。
- 读不到 locked reference registry。
- 无法判断样片等级。
- 无法区分 `mainline_inheritance_candidate` 与 `flow_proof_sample`。
- 无法输出 `script_to_visual_carrier_map.md`。
- 无法输出 `block_segment_carrier_map.md`。
- 无法输出 `hyperframes_motion_plan.md`。
- 无法输出 `locked_reference_inheritance_plan.md`。
- 无法判断 `formal_api_demo` 是否真实等于 API 主持壳能力。
- 用户要求 mainline 但 API 主持壳 / 项目 TTS / 云剪未跑通。
- 需要生成视频才能判断计划是否成立。

## 22. 最终回报格式

下一轮执行最终只回报：

1. 任务结果
2. 实际读取
3. 修正后的关键结论
4. 与旧 V3 plan 的主要差异
5. 是否允许进入 render
6. 产物路径
7. blocked 项
8. 下一个目标
