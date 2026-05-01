# Codex 执行规则

## 1. 文件定位

本文件规定 Codex 在《视频工厂》仓库中的默认执行方式。

它负责：

- 默认读取顺序
- 什么时候必须先审计
- 什么范围可以改
- GPT 数据源与仓库不同步时如何处理
- 仓库型任务的日志、提交、推送与回流规则
- 完成前最小验证要求

## 2. 默认读取顺序

每次任务默认按以下顺序读取：

1. `AGENTS.md`
2. 当前仓库本地 `skills/` 是否存在
3. 若本地无相关 skill，再检查全局 `~/.codex/skills`
4. `codex_source/00_codex_readme.md`
5. `codex_log/latest.md`
6. 若任务命中“execution lane / parallel gate / 是否适合提速 / 是否适合并发 / lane recommendation / parallel recommendation”，在 `codex_log/latest.md` 之后优先读：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
7. 若任务命中“当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容”，在 `codex_log/latest.md` 之后优先读：
   - `codex_log/current_publish_target.md`
   - 若需要快速复核当前样片的 Git 可追踪轻量证据，再读 `codex_log/current_publish_target_light_evidence.md`
8. 若任务命中“灰度测试 / 发片 / 发布后 / 复盘 / 数据记录 / 24h / 72h / 播放量 / 完播率 / 留存 / 下一轮只改一个变量”，在 `current_publish_target` 之后优先读：
   - `codex_log/current_gray_test_target.md`
   - `review_loop/00_review_loop_readme.md`
   - `review_loop/02_video_record_template.md`
   - `review_loop/03_result_dashboard_template.md`
   - `review_loop/04_diagnosis_template.md`
   - `review_loop/05_dual_review_handoff_template.md`
   - `review_loop/06_next_round_task_template.md`
   - `project_source/14_content_review_and_loop_governance_rules.md`
9. `codex_source/01_execution_rules.md`
10. `codex_source/02_current_execution_context.md`
11. `codex_source/03_research_findings_bridge.md`
12. 当前任务直接相关的 `project_source/*`
13. 命中价值 / 文案 / 结尾卡时，读 `codex_source/11_ai_knowledge_video_value_bridge.md`
14. 命中“什么算已知”时，读 `codex_source/12_codex_known_state_three_layer_rules.md`
15. 命中“完整成片 / 成品候选片 / 技术预览升级成候选片 / 样片回炉 / 开头重做 / 中段剪辑 / 字幕修正 / TTS 修正 / 功能卡修正 / 结果差卡修正 / 骚萌卡修正 / 录屏放大修正 / 视觉母版修正”时，读：
   - `codex_source/14_locked_reference_inheritance_rules.md`
   - `codex_source/locked_reference_registry.md`
16. 命中 v3.1 / 卡片视觉路由 / 段落提示卡 / 信息卡 / 骚萌卡三路拆分时，再读：
   - `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
17. 命中 commit / push / reading branch 回流时，再读 `codex_source/08_branch_sync_and_reading_branch_rules.md`

当前仓库现实 `已确认`：

- 仓库本地 `skills/` 目录不存在
- 相关 skills 需回退检查全局 `~/.codex/skills`

## 3. skill 检查硬规则

执行前必须：

1. 先检查当前仓库本地 `skills/`
2. 若无，再检查全局 `~/.codex/skills`
3. 命中相关 skill 时必须使用
4. 若未找到或不适用，必须如实说明

当前这类“项目口径 / 接手口径 / 文档维护”任务，至少要优先检查：

- `using-superpowers`
- `context-driven-development`
- `verification-before-completion`

当前这类“execution lane / parallel mechanism”任务，额外必须检查：

- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`

## 4. 哪些情况必须先审计

出现以下任一情况，必须先审计再改：

1. 用户明确要求先看仓库现实
2. 任务目标是“同步源事实 / 修复接手口径 / 改默认主线”
3. 任务涉及 `project_source` 与 `codex_source` 的交叉修改
4. 任务涉及主读取分支 `codex/user-readable-map`
5. 当前仓库文件与聊天里的说法可能不一致

## 5. 默认允许修改范围

只有在用户明确授权时，才允许修改：

- 当前任务点名的 `project_source/*`
- 当前任务点名的 `codex_source/*`
- `codex_log/*`

没有明确授权时，默认不改：

- 代码文件
- 测试文件
- 配置 / 密钥文件
- `dist/*`
- 不在本轮范围内的文档

## 6. GPT 数据源不会自动同步到 Codex 仓库

这是执行层硬规则：

- GPT Project 数据源不会自动同步到 Codex 仓库
- 聊天里说过，不等于 Codex 已知
- GPT 数据源里有，不等于 Codex 已知
- 外部资料、Perplexity 结论、ChatGPT 收束结果，若会影响执行，必须先回写仓库或显式带入执行单

未回写前，它们最多只能算：

- `GPT 已知`
- 或 `Codex 条件已知`

不能直接写成：

- `Codex 正式已知`

## 6A. 本地审片路径读取规则

凡涉及本地审片路径、视频路径、音频路径、图片路径、复审包路径，必须先查：

- `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`

硬规则：

- 没有被 Codex 本地验证过的路径，不得当作用户可打开路径输出。
- 只有 `current_local_artifact_paths.md（当前本地产物路径索引）` 中 `path_exists = true（路径存在）` 的路径，才能作为用户可打开路径输出。
- `summary.json（状态摘要）` 和 `review_manifest.md（审片入口）` 中的路径只能作为线索，不能直接当成真实可打开路径。
- 如果本地路径索引不存在、超过 24 小时未验证，或相关记录没有 `path_exists = true（路径存在）`，必须写成“路径待本地复核”。
- `/private/tmp（系统临时目录）` 路径默认不稳定，除非本轮重新验证存在，否则不得作为首选路径。
- 旧脏 worktree（旧脏工作区）路径不得作为默认执行路径；如确实存在，只能作为历史 / 备选打开路径并明确标注。

## 7. 仓库型任务默认线路

命中以下任一条件，默认按仓库型任务处理：

- 改仓库文件
- 修项目口径 / 执行口径 / 路由口径 / 接手口径
- 需要 commit / push / 回流主读取分支

默认线路：

先审计现状 -> 改文件 -> 更新日志 -> 验证 -> commit -> push 当前分支 -> 同步回 `codex/user-readable-map`

## 8. 执行日志硬规则

只要本轮出现以下任一事实，就必须写 `codex_log/`：

- 改了仓库文件
- 跑了命令
- 完成了 commit / push / 同步
- 形成了新的阻塞点 / 交接点

至少要做两件事：

1. 刷新 `codex_log/latest.md`
2. 新增一条 `codex_log/YYYYMMDD_任务名.md`

若本轮结果会改变以下任一项，还必须同步刷新：

- `codex_log/current_publish_target.md`
  - 当前待发对象
  - 当前审核对象
  - 当前正式状态
  - 当前唯一最高优先级 blocker
  - 现在最该改的唯一一点
  - `lane_recommendation`
  - `lane_reason`
  - `lane_invalid_if`
  - `parallel_recommendation`
  - `parallel_reason`
  - `parallel_invalid_if`
- 若当前样片的 Git 可追踪轻量证据有变化，再同步刷新：
  - `codex_log/current_publish_target_light_evidence.md`

## 8A. 视频修改必须同步口径规则

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

## 8A-1. 发布后灰度测试与复盘接入规则

当前 v3.1 已进入 `post_publish_gray_test（发布后灰度测试阶段）`。

状态硬规则：

- `publish_status = gray_test_published（已发片，进入灰度测试）`
- `gray_test_status = active（灰度测试中）`
- `post_publish_review_required = true（需要发布后复盘）`
- `content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`

执行硬规则：

1. 发布后复盘默认接入 `review_loop/`，不新建独立灰度系统。
2. 单条记录走 `review_loop/02_video_record_template.md`。
3. 结果看板走 `review_loop/03_result_dashboard_template.md`。
4. 诊断初检走 `review_loop/04_diagnosis_template.md`。
5. Codex 初检 / ChatGPT 判断交接走 `review_loop/05_dual_review_handoff_template.md`。
6. 下一轮只改一个变量走 `review_loop/06_next_round_task_template.md`。
7. 24h / 72h 数据窗口、一次只改一个变量、小样本状态升级 / 降级、异常样本处理、规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`。

Codex 职责边界：

- Codex 可以记录、初检、归档、标缺失、生成下轮草稿。
- Codex 不得把灰度测试写成内容通过。
- Codex 不得把已发片写成最终成功。
- Codex 不得跳过 24h / 72h 数据直接设定下一条文案。
- 最终问题层、是否继续、下一轮唯一改点由 ChatGPT / 用户拍板。

## 8B. 仓库清理与旧口径归档规则

命中“仓库清理 / 旧口径归档 / 未提交文件处理 / 执行噪音删除”时，必须先输出 `cleanup_audit（清理审计）`，再动手。

清理审计必须分为：

1. `safe_delete（可安全删除）`：确认无引用、无证据价值、可重新生成或明显临时的文件。
2. `archive_only（只归档不删除）`：旧判断、旧入口、旧 PR 报告、仍有复盘价值但不应作为默认入口的文件。
3. `rewrite_needed（需要改清楚）`：仍会被 Codex 默认读取、且可能误导当前状态的入口 / 状态 / registry / summary。
4. `keep_as_evidence（作为证据保留）`：素材、复审包、registry 引用证据、summary / manifest / timeline / cut_map 引用产物。
5. `blocked_unknown（不确定，先不动）`：无法判断是否可删的未追踪文件或目录。

未提交 / 未追踪文件处理规则：

- 不允许直接运行全仓清理命令。
- 不允许不分类就删除 `untracked` 文件。
- 不允许删除 `素材录制/`、`素材库_assets/`、当前 v3 / v3.1 可能用到的复审包、PR #7 B、可爱卡片参考图、registry 已引用 artifact / evidence。
- 只删除 `safe_delete`，且必须在 dated log 中列出相对路径和原因。
- `blocked_unknown` 一律不删，只记录后续专项清理建议。

旧口径归档规则：

- PR #22 / PR #23 / 旧 round 报告中的历史判断不得原样覆盖用户最新确认。
- 可将旧判断摘录或副本放入 `归档_archive/旧口径_old_context_YYYYMMDD/`。
- 归档目录必须有 README，说明默认不再读取哪些旧口径。
- 归档内容只作复盘证据，不作为当前事实、不作为后续执行参考。

## 8C. locked reference 继承硬规则

以后凡任务命中以下任一类型，必须先读 locked reference 机制：

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

强制读取：

1. `codex_source/14_locked_reference_inheritance_rules.md`
2. `codex_source/locked_reference_registry.md`

硬规则：

- 任一文件读不到，必须 `blocked`，不得直接生成完整片。
- `candidate_reference` 只能写成候选参考，不得写成 `locked_reference`。
- `failed_reference` 只能作为反例或复盘材料，不得默认继承。
- 用户 / ChatGPT 未明确确认前，不得把 PR 自评 pass 写成用户已确认。
- 完整成片 / 成品候选片 / 样片回炉完成时，必须输出 `locked_reference_inheritance_report.md`。
- summary 必须写 `locked_reference_registry_read`、`locked_reference_inheritance_validation`、`locked_reference_inheritance_report`、`unapproved_reference_changes`、`reference_deviation_blockers`、`candidate_references_used`、`locked_references_used`。

## 8D. v3.1 视觉路由前置硬规则

当前状态：

- `已确认` v3.1 已成为《我用 AI 做 PPT 踩过的坑》当前视频基线。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1，不再基于 v3 或 round34。
- `已确认` v3 只保留为历史候选 / 对照，不作为后续默认修改基础。
- `已确认` v3.1 已有 `dist/latest_review_pack/visual_route_map.json（视觉路由表）` 和 `dist/latest_review_pack/visual_route_validation_report.json（视觉路由验证报告）`；后续修改必须先复核并保持三条视觉路由不混。

后续任何 v3.1 生成 / 样片回炉 / 卡片视觉修正任务，若涉及段落提示卡、信息卡、骚萌卡，必须先读：

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

硬规则：

- 生成或修改 v3.1 全片前必须先读取 / 输出并验证 `visual_route_map.json（视觉路由表）`。
- `cute_prompt_card_route（可爱段落提示卡路由）` 只给反面 / 正面展示提示卡。
- `cute_info_card_route（可爱信息卡路由）` 只给结果差、归因转折、Prompt 架构、Prompt 尾卡等信息卡。
- `sassy_reaction_card_route（骚萌反应卡路由）` 只给三张骚萌反应卡。
- v3 技术状态只能写成当前阶段里程碑达成，必须保持 `technical_line_locked = false（技术线未锁定）`。
- PR #7 B 是后续骚萌卡唯一执行参考。
- PR #7 A 只能作为历史 / candidate 对照，不能作为任何后续骚萌卡执行参考。
- 读不到 `PR7_B_骚萌反应页.png` 必须 `blocked`，不得回退 PR #7 A。
- 任意骚萌卡走信息卡路由、任意信息卡走骚萌路由、任意段落提示卡走复杂信息卡路由且未重审，必须 `blocked`。

旧 PR 降噪规则：

- PR #22：v3 历史候选，不再直接合并，不再作为后续默认基础。
- PR #23：历史样本包，PR #7 A 优先判断已被 PR #7 B 覆盖，不再直接合并。
- PR #24：v3.1 有效产物已回流到最新主读取分支，PR #24 本身不得再直接合并，避免回退 PR #25 清理口径。

以下情况必须 `blocked`：

- 找不到已锁定 reference。
- 没有读取 locked reference registry。
- 继承失败或只写“类似”但没有对照证据。
- 字幕、TTS、放大、卡片、剪辑语法与 locked reference 不一致。
- 用户没有授权但 Codex 自行换风格、重做或替换。
- 完整片使用 candidate reference 却写成 locked reference。
- 只有 technical_validation / content_validation，没有 reference inheritance validation。

## 9. 主读取分支与状态分类

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

状态分类必须显式标记为：

- `formal_synced`
- `task_branch_only`
- `pr_open_not_merged_to_reading_branch`
- `local_only`
- `no_repo_change`

硬规则：

- “任务分支已 push”不等于“主读取分支已更新”
- “已开 PR”不等于“仓库正式状态已同步”
- 只有同步回 `codex/user-readable-map`，才算主读取分支正式已知

## 10. 这类任务的最小验证

这类文档 / 规则 / 接手口径修复任务，完成前至少要做：

1. `git diff --check`
2. 重新读取关键目标文件，确认口径一致
3. 重新读取 `codex_log/current_publish_target.md`，确认只靠稳定入口就能知道当前对象、状态、blocker 与下一步
4. 若本轮补了轻量证据包，再读取 `codex_log/current_publish_target_light_evidence.md`
5. 若本轮补的是 lane / parallel 机制，再读取：
   - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
   - `codex_source/13_execution_lane_and_parallel_rules.md`
6. 若声称已同步回主读取分支，使用 `git show codex/user-readable-map:路径` 做实际读取验证

## 11. 完成口径硬规则

不得把以下两件事写成同一件事：

- 仓库口径已同步
- 新主线样片已验证成立

本轮如果只完成了文档 / 规则 / 桥接 / latest / reading branch 回流，只能写：

- 仓库口径已同步

不能写：

- 样片验证通过
- 新主线已被质量验证成立

## 12. 收尾时必须回报的 4 个同步锚点

每轮仓库型任务收尾时，必须明确回报：

1. 当前工作分支
2. 最新提交 SHA
3. 是否已 push
4. 是否已同步回 `codex/user-readable-map`
