# codex_source 总入口

## 1. 这份文件是什么

本文件是《视频工厂》当前 Codex 执行层入口。

它是《视频工厂》子入口，不是整个仓库的总入口；仓库总入口与项目分流规则统一看 `AGENTS.md`。

它负责回答：

- `codex_source/` 是干什么的
- 新会话最小先读什么
- 当前正式默认主线是什么
- 当前主读取分支是什么
- GPT 数据源与仓库不同步时，谁算源事实
- 当前 10 份执行包默认该怎么读

## 2. `codex_source/` 负责什么

`codex_source/` 负责：

- 读取顺序
- 执行边界
- 仓库同步规则
- 已知状态分层
- 验证与汇报口径

它不负责：

- 项目脑正文
- 单条脚本内容
- 代码实现细节

当前项目正式事实正文属于 `GPT数据源/` 当前 10 份执行包；`project_source/` 只作为历史 / 辅助主题化镜像，不再作为当前主事实源。代码实现细节仍归代码层。

## 3. 新会话最小接手入口

新 Codex 会话默认最少先读：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `GPT数据源/00_项目总述.md`
5. `GPT数据源/01_项目系统提示词.md`
6. `GPT数据源/03_总索引与阅读顺序.md`
7. `GPT数据源/08_当前正式事实.md`
8. `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`

当前正式来源优先级：
1. `GPT数据源/` 当前 10 份执行包
2. `dist/latest_review_pack/summary.json`
3. `dist/latest_review_pack/review_manifest.md`
4. `codex_log/latest.md`
5. `codex_source/` 执行规则
6. `project_source/` 历史 / 辅助镜像

本地可打开路径读取规则：
- 当 ChatGPT / Codex 需要给用户本地可打开路径时，必须优先读取 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`。
- 如果该索引中没有 `path_exists = true（路径存在）` 的记录，只能说“路径待本地复核”，不能直接把 `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径当成真实可打开路径。
- `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径只能作为线索，必须经 Codex 本地复核后才能输出给用户。

当前 `latest_review_pack` 已确认指向 `20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`；`current_video_baseline = v3.1`，后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1；v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。v3.1 技术验证已通过，但 `technical_line_locked = false（技术线未锁定）`，下一步仍需技术升级；v3.1 已发片并进入 `post_publish_gray_test（发布后灰度测试阶段）`，`publish_status = gray_test_published`，`gray_test_status = active`，`post_publish_review_required = true`；当前发布后内容状态写为 `content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`，`send_ready = false`，`visual_master_locked = false`。

若任务命中“完整成片 / 成品候选片 / 技术预览升级成候选片 / 样片回炉 / 开头重做 / 中段剪辑 / 字幕修正 / TTS 修正 / 功能卡修正 / 结果差卡修正 / 骚萌卡修正 / 录屏放大修正 / 视觉母版修正”，则在 `codex_log/latest.md` 之后必须先补读：

4. `codex_source/14_locked_reference_inheritance_rules.md`
5. `codex_source/locked_reference_registry.md`
6. 若任务涉及 v3.1 / 卡片视觉路由 / 段落提示卡 / 信息卡 / 骚萌卡，则还必须读 `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

硬规则：
- 任一文件读不到，必须 `blocked`，不得直接生成完整片或写成成片候选完成。
- v3.1 生成前读不到视觉路由规则，或未先输出并验证 `visual_route_map.json（视觉路由表）`，必须 `blocked`，不得生成全片。
- 完整成片 / 成品候选片 / 样片回炉完成时，必须输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`。
- summary 必须写 `locked_reference_registry_read`、`locked_reference_inheritance_validation`、`locked_reference_inheritance_report`、`unapproved_reference_changes`、`reference_deviation_blockers`、`candidate_references_used`、`locked_references_used`。

若任务命中“execution lane / parallel gate / 是否适合提速 / 是否适合并发 / lane recommendation / parallel recommendation”，则在 `codex_log/latest.md` 之后优先补读：

4. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
5. `codex_source/13_execution_lane_and_parallel_rules.md`

若任务命中“当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容”，则在 `codex_log/latest.md` 之后优先补读：

6. `codex_log/current_publish_target.md`
7. 若需要快速复核当前样片结构与轻量证据，再补读 `codex_log/current_publish_target_light_evidence.md`

若任务命中“灰度测试 / 发片 / 发布后 / 复盘 / 数据记录 / 24h / 72h / 播放量 / 完播率 / 留存 / 下一轮只改一个变量”，则在 `codex_log/latest.md` 和 `codex_log/current_publish_target.md` 之后优先补读：

8. `codex_log/current_gray_test_target.md`
9. `review_loop/00_review_loop_readme.md`
10. `review_loop/02_video_record_template.md`
11. `review_loop/03_result_dashboard_template.md`
12. `review_loop/04_diagnosis_template.md`
13. `review_loop/05_dual_review_handoff_template.md`
14. `review_loop/06_next_round_task_template.md`
15. `project_source/14_content_review_and_loop_governance_rules.md`

发布后复盘规则：
- 灰度测试只是当前阶段名称，不另起独立灰度系统
- 单条记录、结果看板、诊断初检、双层交接和下轮草稿均走 `review_loop/`
- 24h / 72h 数据窗口、一次只改一个变量、小样本状态、异常样本和规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`
- Codex 只做记录、初检、归档和下轮草稿；ChatGPT / 用户负责最终内容判断和下一轮唯一改点拍板
- 发片不等于内容过线，灰度测试不等于验证成功，不得跳过数据直接设定下一条文案

若任务偏执行规则，再补读：

16. `codex_source/01_execution_rules.md`
17. `codex_source/02_current_execution_context.md`
18. `codex_source/03_research_findings_bridge.md`

若任务命中展示路由，再补读：

9. `project_source/16_presentation_routing_rules.md`
10. `project_source/24_human_self_footage_light_ppt_routing_rules.md`

若任务命中选题 / 文案 / 价值判断，再补读：

11. `project_source/21_topic_selection_and_copywriting_rules.md`
12. `project_source/22_copy_mode_routing_rules.md`
13. `project_source/25_ai_knowledge_video_value_rules.md`
14. `codex_source/11_ai_knowledge_video_value_bridge.md`

若任务命中“项目价值 / 场景工作包 / 文案交付 / 录制素材 / 豆包 prompt 职责”，再补读：

15. `project_source/26_scene_work_package_mainline_rules.md`
16. `project_source/27_recording_assets_and_prompt_delivery_rules.md`

若任务命中“内容生产 / vNext 外壳 / Minecraft-inspired / Docker 工作台 / 录制减负 / 三层 prompt / Prompt 引用尾卡”，再补读：

17. `GPT数据源/04_选题与文案规则.md`
18. `GPT数据源/05_文案路由规则.md`
19. `GPT数据源/07_AI知识类视频价值规则.md`
20. `GPT数据源/09_目标态计划.md`

若任务命中“当前正式事实 / 目标态计划 / 术语边界”，再补读：

21. `project_source/02_term_definitions_and_state_boundaries.md`
22. `project_source/07_current_formal_facts.md`
23. `project_source/09_target_state_plan.md`

若任务命中“什么算已知”，再补读：

24. `codex_source/12_codex_known_state_three_layer_rules.md`

## 4. 当前正式默认主线

当前正式默认主线 `已确认` 为：

- API 生成真人
- 用户录制素材
- 少量 PPT
- 云端剪辑

必须同时默认理解：

- 结构跟着文案走
- `API生成真人段` 出现 1 次还是 2 次，是 block 路由结果
- pure PPT / 信息卡，不再是默认主线
- AI talking avatar / 数字人口播，不再是默认主线
- `云端剪辑 / cloud-only` 是当前正式方向，不等于 runtime 已稳定跑通
- `local preview` / `local mp4` 只能算辅助
- demo 只是链路锚点，不是质量样片

## 5. 当前主读取分支

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

只有同步回这个分支，才算：

- 新聊天默认正式已知
- 仓库正式状态已更新

## 5A. 执行层默认同步补丁

当前执行层必须默认理解：

只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论本轮是成功、失败、半成功还是 blocked，都必须：
1. 更新 `codex_log/latest.md`
2. 若有真实执行结果，补 `codex_log/YYYYMMDD_任务名.md`
3. commit
4. push
5. 同步回 `codex/user-readable-map`

注意：
- `content_validation` 未通过，不等于不能同步
- 只要当前已知状态变了，就必须同步
- 同步时必须如实写状态，不能把半成功写成已达标

这条规则不是只针对“成功达标”轮次；凡是改变新聊天默认接手口径的 `blocked` / 半成功 / `technical_validation` 通过但 `content_validation` 未通过，也属于必须同步的执行层正式状态。

## 5B. 视频修改必须同步口径规则

以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。

默认必须同步检查：
1. `codex_log/latest.md`
2. `codex_log/current_publish_target.md`
3. `codex_log/current_publish_target_light_evidence.md`
4. `GPT数据源/08_当前正式事实.md`
5. `dist/latest_review_pack/summary.json`
6. `dist/latest_review_pack/review_manifest.md`
7. 如改变入口 / 分支 / 读取顺序，还必须同步 `AGENTS.md` 和 `codex_source/00_codex_readme.md`

硬规则：
- 不允许只改视频、不改口径
- 不允许只在工作分支改口径、不同步默认主读取分支
- 不允许把历史样片写成当前最新样片
- 不允许把 `technical_validation` 写成 `content_validation`
- 不允许用户未最终确认前把当前片子写成可发送状态
- 不允许旧 `round` 状态继续覆盖最新 `latest_review_pack`
- 只要改动会影响新会话默认接手判断，就必须同步到 `codex/user-readable-map`

## 5C. 旧口径与归档读取规则

当前《视频工厂》已完成 v3.1 当前基线切换。新 Codex 会话不得再让旧 round、v3、旧 PR 草稿或旧分支报告覆盖当前主事实。

默认降权：

- `round34`：只作为中段剪辑语法、放大方式和可爱提示卡参考，不作为当前最新样片状态。
- PR #22 原始状态：只代表 v3 PR 创建时的草稿口径；v3 已降为历史候选 / 对照，不再作为后续默认基础。
- PR #23 原始状态：只代表 2026-04-30 只读判断；其中 PR #7 A 优先判断已被用户最新确认覆盖，PR #23 只能作为历史样本包。
- PR #24 原始状态：只代表基于 PR #22 head 生成的 v3.1 候选 PR；有效 v3.1 产物已安全回流到最新主读取分支，PR #24 不得再直接合并。
- PR #7 B 是后续骚萌卡唯一执行参考；PR #7 A 只能作为历史 / candidate 对照，不能作为任何后续骚萌卡执行参考。
- 读不到 PR #7 B 必须 `blocked`，不得回退 PR #7 A。
- `归档_archive/旧口径_old_context_*/`：只供复盘旧判断来源，默认不参与当前事实裁决。

当前事实裁决顺序仍为：

1. 用户最新执行单中明确写入并已同步到 `codex/user-readable-map` 的口径。
2. `GPT数据源/08_当前正式事实.md`、`dist/latest_review_pack/summary.json`、`codex_log/current_publish_target.md`。
3. registry、v3.1 视觉路由规则、`dist/latest_review_pack/visual_route_map.json` 与 `dist/latest_review_pack/visual_route_validation_report.json`。
4. 归档目录和旧 PR 报告，仅作历史证据。

## 6. GPT 数据源与仓库不同步时的硬规则

当前必须写死：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 当任务命中“核验 GPT 数据源原文 / 对照本地 GPT 数据源同步文本”时，优先读取 repo 内 `GPT数据源/` 镜像目录
- 当前仓库同时存在 `GPT数据源/` 与 `GPT 数据源/`
- 当前仓库主读动态事实目录为无空格 `GPT数据源/`
- 有空格 `GPT 数据源/` 是 GPT Project 静态协作包，不承载当前 v3 / v3.1 动态状态；除非用户明确要求，不得在仓库清理或视频执行任务中修改它
- 若两者内容冲突，当前动态事实以无空格 `GPT数据源/`、`dist/latest_review_pack/`、`codex_log/current_publish_target.md` 和用户最新同步口径为准
- `project_source/` 是历史 / 辅助主题化镜像，不是当前正式事实源
- 只有写进仓库文件，并同步到 `codex/user-readable-map`，才算新聊天默认正式已知

执行层里对“什么算已知”的正式分层，统一看：

- `codex_source/12_codex_known_state_three_layer_rules.md`

## 7. v3.1 视觉路由入口补丁

以后凡任务命中“骚萌卡 / 信息卡 / 段落提示卡 / v3.1 / visual_route_map”，必须先读取：

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

并在后续任何基于 v3.1 的生成 / 修改 / 技术升级前先读取并验证：

- `visual_route_map.json（视觉路由表）`

读不到 PR #7 B 或 route map 未通过时，必须 `blocked`，不得回退 PR #7 A，不得生成或修改全片。

## 8. 入口一句话

命中《视频工厂》后，新会话默认先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`，再按 10 份执行包最小顺序补读 `GPT数据源/00`、`GPT数据源/01`、`GPT数据源/03`、`GPT数据源/08`、`GPT数据源/06`；当前正式事实以 `GPT数据源/` 当前 10 份执行包、`dist/latest_review_pack/summary.json`、`dist/latest_review_pack/review_manifest.md` 和 `codex_log/latest.md` 为准，`project_source/` 只作历史 / 辅助镜像；当前 `latest_review_pack` 指向 v3.1，`current_video_baseline = v3.1`，`future_iteration_base = v3.1`，`publish_status = gray_test_published`，`gray_test_status = active`，`current_phase = post_publish_gray_test`，`content_validation = gray_testing_not_final_passed`，`send_ready = false`；若任务命中完整成片 / 成品候选片 / 技术预览升级 / 样片回炉 / 字幕 / TTS / 卡片 / 放大 / 剪辑 / 视觉母版修正，必须先读 `codex_source/14_locked_reference_inheritance_rules.md` 和 `codex_source/locked_reference_registry.md`，读不到即 blocked；若任务命中 v3.1 / 段落提示卡 / 信息卡 / 骚萌卡 / visual_route_map，还必须先读 `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`，并先验证 `visual_route_map.json`；PR #7 B 是后续骚萌卡唯一执行参考，读不到必须 blocked，不得回退 PR #7 A；若任务命中灰度测试 / 发片 / 发布后 / 复盘 / 数据记录，必须读取 `codex_log/current_gray_test_target.md` 与 `review_loop/`，先记录 24h / 72h 数据，再做 Codex 初检和 ChatGPT 判断，不得跳过数据直接设定下一条文案；当前正式默认主线按“API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑”理解，结构跟着文案走，`API生成真人段` 次数由 block 路由决定，`云端剪辑 / cloud-only` 只能写成正式方向，不能写成 runtime 已稳定跑通。
