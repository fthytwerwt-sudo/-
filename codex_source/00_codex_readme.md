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

当前 `latest_review_pack` 已确认指向 `round34_中段双展示提示卡_正反分段提示修复`；`technical_validation`、`border_residue_validation`、`jump_cut_validation` 为 `通过`，`content_validation` 仍为 `待用户 / ChatGPT 最终复审`，`send_ready = no`。

若任务命中“execution lane / parallel gate / 是否适合提速 / 是否适合并发 / lane recommendation / parallel recommendation”，则在 `codex_log/latest.md` 之后优先补读：

4. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
5. `codex_source/13_execution_lane_and_parallel_rules.md`

若任务命中“当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容”，则在 `codex_log/latest.md` 之后优先补读：

6. `codex_log/current_publish_target.md`
7. 若需要快速复核当前样片结构与轻量证据，再补读 `codex_log/current_publish_target_light_evidence.md`

若任务偏执行规则，再补读：

8. `codex_source/01_execution_rules.md`
9. `codex_source/02_current_execution_context.md`
10. `codex_source/03_research_findings_bridge.md`

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
- 不允许用户未最终确认前写 `send_ready = yes`
- 不允许旧 `round` 状态继续覆盖最新 `latest_review_pack`
- 只要改动会影响新会话默认接手判断，就必须同步到 `codex/user-readable-map`

## 6. GPT 数据源与仓库不同步时的硬规则

当前必须写死：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 当任务命中“核验 GPT 数据源原文 / 对照本地 GPT 数据源同步文本”时，优先读取 repo 内 `GPT数据源/` 镜像目录
- 当前仓库主读目录为 `GPT数据源/`；本分支未发现并行存在的 `GPT 数据源/` 目录
- 若未来 `GPT数据源/` 与 `GPT 数据源/` 同时存在，必须先对照差异并明确主读目录，不得猜测
- `project_source/` 是历史 / 辅助主题化镜像，不是当前正式事实源
- 只有写进仓库文件，并同步到 `codex/user-readable-map`，才算新聊天默认正式已知

执行层里对“什么算已知”的正式分层，统一看：

- `codex_source/12_codex_known_state_three_layer_rules.md`

## 7. 入口一句话

命中《视频工厂》后，新会话默认先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`，再按 10 份执行包最小顺序补读 `GPT数据源/00`、`GPT数据源/01`、`GPT数据源/03`、`GPT数据源/08`、`GPT数据源/06`；当前正式事实以 `GPT数据源/` 当前 10 份执行包、`dist/latest_review_pack/summary.json`、`dist/latest_review_pack/review_manifest.md` 和 `codex_log/latest.md` 为准，`project_source/` 只作历史 / 辅助镜像；当前 `latest_review_pack` 指向 round34，`send_ready = no`；若任务命中当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容，再优先读 `codex_log/current_publish_target.md`，需要轻量证据时再读 `codex_log/current_publish_target_light_evidence.md`；当前正式默认主线按“API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑”理解，结构跟着文案走，`API生成真人段` 次数由 block 路由决定，`云端剪辑 / cloud-only` 只能写成正式方向，不能写成 runtime 已稳定跑通。
