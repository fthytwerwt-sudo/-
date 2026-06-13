# 多项目仓库入口规则

## 1. 当前仓库身份

当前这是【多项目仓库】。

必须明确：
- 不能再把整个仓库直接写死成单一项目入口
- 不能再把所有新会话默认接成 `AI 直播前台验证项目`
- 不能再把《视频工厂》误判成直播项目的历史残片

当前仓库至少同时承载以下两条入口：
1. 《视频工厂》
2. `AI 直播前台验证项目`

默认规则：
- 命中《视频工厂》时，走《视频工厂》入口
- 命中 `AI 直播前台验证项目` 时，走直播入口
- 未命中任一项目时，不得擅自继承任何业务事实，必须先阻断并做路由判断

## 2. 默认项目分流规则

### 2.1 永远先读
进入当前仓库后，固定先读：
1. `AGENTS.md`

### 2.2 《视频工厂》命中规则
若任务命中以下任一关键词，默认按《视频工厂》接手：
- `视频工厂`
- `API 生成真人`
- `用户录制素材`
- `录制素材`
- `少量 PPT`
- `云端剪辑`
- `GPT数据源`
- `GPT 数据源`
- `豆包 prompt`
- `current_publish_target`
- `场景化专业输出工作包`
- `证明壳`
- `入口壳`
- `产品单元`
- `reference`
- `样片`
- `参考图`
- `参考视频`
- `参考声音`
- `参考效果`

命中《视频工厂》后，默认先读：
1. `GPT数据源/00_项目总述.md`
2. `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
3. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
4. `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
5. `GPT数据源/01_项目系统提示词.md`
6. `GPT数据源/03_总索引与阅读顺序.md`
7. `GPT数据源/08_当前正式事实.md`
8. `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
9. `codex_source/00_codex_readme.md`
10. `codex_source/19_project_state_action_router.md`
11. `codex_source/20_reference_to_execution_contract.md`
12. `codex_log/latest.md`

当前《视频工厂》正式来源顺序：
1. `GPT数据源/` 当前 10 份基础执行包 + `10_OPC一人公司闭环与多AI协作机制.md` + `11_项目状态动作总控器_机制推理层.md` + `12_参考到执行落地契约_reference_to_execution_contract.md`
2. `codex_log/latest.md`
3. `dist/latest_review_pack/summary.json`
4. `dist/latest_review_pack/review_manifest.md`
5. `codex_source/00_codex_readme.md`

GPT Project 上传包地址规则：
- ChatGPT 不得凭聊天记忆给 GPT Project 本地上传地址。
- 需要 GPT Project 上传包地址时，必须先读取 `codex_log/current_local_artifact_paths.md` 或由 Codex 本地审计后给出。
- 用户上传时只使用 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）`。
- 规范上传包目录必须包含：`上传说明_UPLOAD_MANIFEST.md`。
- 旧 `GPT 数据源/` 只按历史静态包理解；`GPT数据源/` 只按 GitHub 动态事实目录理解；两者都不等于默认上传包目录。

`project_source/` 只作为历史 / 辅助主题化镜像，不得默认高于 `GPT数据源/` 当前 10 份基础执行包 + `10_OPC一人公司闭环与多AI协作机制.md` + `11_项目状态动作总控器_机制推理层.md`、`codex_log/latest.md` 或 `dist/latest_review_pack/`。

`归档删除区_archive_delete_zone/` 只作为旧口径隔离、旧入口隔离、旧产物候选和清单区使用，不得作为默认读取入口，不得高于 `GPT数据源/` 当前 10 份基础执行包 + `10_OPC一人公司闭环与多AI协作机制.md` + `11_项目状态动作总控器_机制推理层.md`、`codex_log/latest.md`、`dist/latest_review_pack/` 或当前执行规则层。

当前已确认：
- `current_reading_branch = main（当前唯一远端主线 / 默认主读取分支）`
- `current_project_upper_identity = OPC 一人公司 AI 闭环验证系统（当前项目上位身份）`
- `latest_review_pack` 当前指向 `20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- `current_video_baseline = v3.1（当前视频基线）`
- `future_iteration_base = v3.1（后续升级 / 修改 / 技术优化 / GPT 文案侧回炉的默认基础）`
- `current_project_core_value = 真实 AI 使用经验 + 工作提效实录`
- 当前视频是内容化与反馈出口，不是项目全部目标。
- 当前视频四件套主线 `API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑` 是内容化输出默认执行载体，不是每条内容不可变死流程。
- 当前多 AI 协作默认架构为：
  - `ChatGPT（总控脑 / 判断层）`
  - `write_executor（写入执行器边界）`
    - `active_write_executor = codex（当前激活写入执行器）`
    - `executor_type = codex / trae / future_ide_agent（未来候选执行器类型）`
    - `trae` 与 `future_ide_agent` 当前只作为 future candidate，未启用、未授权、未验证。
  - `Vector RAG / DashVector（检索索引 / 缓存层）`
  - `DeepSeek（条件触发的只读审查 / 风险复核 / 冲突二次意见）`
  - `Perplexity（外部研究层）`
- 当前最高机制入口已包含 `Project State Action Router（项目状态动作总控器）`：命中复杂任务、机制修补、文案执行、视频执行、复盘、数据回填、GPT Project 静态包同步或 Codex 执行结果回审时，先读 `GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md`，输出 `state_action_router（项目状态动作总控器）` 后再执行。
- 当前最高机制入口已包含 `Reference-to-Execution Contract（参考到执行落地契约）`：命中 reference / 样片 / 参考图 / 参考视频 / 参考声音 / 参考效果 / 原感稿 / 外部资料 / “按这个做”时，先读 `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` 与 `codex_source/20_reference_to_execution_contract.md`，输出 `reference_to_execution_contract（参考到执行契约）` 后再执行。
- 当前供料 / 检索默认顺序为：`Vector RAG / DashVector retrieval（向量检索） -> GitHub / 仓库原文件 readback（事实回读） -> DeepSeek trigger decision（是否需要 DeepSeek 条件审查）`。
- `DeepSeek（条件触发的只读审查层）` 只在 `rag_empty / rag_low_confidence / source_conflict / mechanism_conflict / high_risk_execution / pre_execution_risk_review / post_execution_discrepancy_review / user_explicit_request / external_deep_reasoning_needed` 等条件成立时参与；不作为每轮默认文件供应商、默认项目记忆或默认执行入口；不写文件、不拍板项目事实。
- `active_write_executor = codex` 当前负责复核原文件、整合 RAG / readback / 必要 DeepSeek 审查结果、补齐受影响文件 / 字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、日志和 Git 收尾。未来如需启用 `trae` 或其他 IDE agent，必须另做执行器契约验证，不得由外部 runtime 直接写入。
- Codex 收到 ChatGPT 完整执行单、横向补全包、多文件机制修补或“不要只做一半 / 执行到底”类任务时，必须触发 `Completion Relay Gate（补全接力闸门）`，先生成 `required_output_inventory（必须交付清单）` 与 `child_task_graph（子任务树）`，再执行并做 `remaining_work_check（剩余工作检查）`。
- `reference（参考）`、`reference_quality_sample（参考质量样片）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 当前默认锁的是质量机制，不锁死每条内容的固定流程。
- reference 仍用于防止质量漂移，locked reference 仍用于质量继承，visual route 仍用于防止卡片外壳混用；但不能把它们理解为每条内容都必须机械照搬同一流程。
- `场景化专业输出工作包` 当前降级为：`可选沉淀单元 / 产品化承接单元`
- 当前视频默认优先服务：真实 AI 使用经验、工作提效实录、真实录屏证据、前后变化、小样本平台反馈与发布后复盘
- v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` 2026-05-15 起，《视频工厂》当前项目阶段迁移为 `formal_operation_active（正式运营中）`。
- `已确认` 当前运营方式为 `data_driven_operation_iteration（数据驱动运营迭代）`，三期内容数据统一纳入 `operation_records（运营记录）`。
- 当前 canonical 运营入口看 `codex_log/current_operation_target.md`；正式运营记录索引看 `review_loop/operation_records_index.md`。
- `codex_log/current_gray_test_target.md` 仅作为 `legacy_compatibility_pointer（历史兼容指针）`；旧 `gray_test` 不再作为当前默认项目阶段。
- `technical_validation = passed（v3.1 技术验证通过）`，但 `technical_line_locked = false（技术线未锁定）`
- `technical_upgrade_next = true（下一步仍需技术升级）`
- `content_validation = not_advanced_by_formal_operation（正式运营不等于内容最终通过；不得写成内容通过）`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `visual_route_map.json（视觉路由表）` 与 `visual_route_validation_report.json（视觉路由验证报告）` 已随 v3.1 基线进入 `dist/latest_review_pack/`
- `publish_status = published_in_formal_operation（已发布，进入正式运营数据回流；不是发布成功口径升级）`
- `operation_status = active（正式运营观察中）`
- `post_publish_review_required = true（需要发布后复盘）`
- `current_phase = formal_operation_active（正式运营中）`
- 上述 `content_validation` 是当前发布后阶段口径；不得把它写成 `passed`
- `formal_operation_delivery_baseline = publish_candidate_or_blocked（正式运营视频交付基线 = 可发布候选片或阻断）`
- `technical_preview_not_delivery = true（技术预览不是用户交付物）`
- `formal_operation_delivery_ratio = horizontal_16_9（正式运营默认出片比例 = 横屏 16:9）`
- `formal_operation_default_resolution = 1920x1080（正式运营默认交付分辨率）`
- `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）` 是正式运营阶段的合法停止结果；如果缺声音、字幕、横屏 16:9 构图、1920x1080 装配、剪辑节奏、素材证据、TTS、卡片、人感质量、平台风险、API 授权或装配能力，必须 blocked，不得降级交技术预览。
- 发布后复盘默认走 `review_loop/`，当前不另起独立灰度系统
- 当前运营目标看 `codex_log/current_operation_target.md`
- 当前运营记录索引看 `review_loop/operation_records_index.md`
- 旧灰度测试目标看 `codex_log/current_gray_test_target.md（legacy compatibility pointer）`
- 旧灰度测试指标体系 V1 看 `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md（legacy metrics / historical reference）`
- 当前 7 天播放量 6000 是小样本阶段基础测试流量门槛，不是最终商业目标
- 当前指标体系不是运营数据大表，而是下一轮改动定位器
- 当前截图优先录入规则看 `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 当前 v3.1 主记录目录看 `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- 当前 v3.1 截图证据目录看 `review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- 当前下一步不是先写新文案，而是先记录 24h / 72h / 7 天数据，回答四个复盘问题，再由 ChatGPT / 用户判断下一轮只改一个变量

### 2.2A 视频修改必须同步口径规则

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
- 只要改动会影响新会话默认接手判断，就必须同步到 `main`

### 2.2B 《视频工厂》旧口径降权规则

当前《视频工厂》接手时，必须先应用以下覆盖规则：

2026-05-04 项目升级前清库覆盖口径：

- 当前唯一固定素材锚点收束为 `v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）`。
- `v31_element_doll_opening_preview（v3.1 元素娃娃开头预览）` 只作为开头预览证据保留。
- `fixed_material_anchor（固定素材锚点）` 只有 v3.1 元素娃娃开头；但这不等于元素娃娃是唯一 reference。
- PR #7 B、cute card、round34 中段剪辑、TTS 节奏参考、TTS 语音 / 音色候选参考、`visual_route_map.json`、`locked_reference_registry.md` 仍属于 `reference_whitelist（参考白名单）`，后续按任务类型读取路径索引和 registry 复核后可继续使用。
- TTS 必须拆开：`tts_pacing_reference（TTS 节奏参考）` 管语速、停顿、轻吐槽、梗感和句间节奏；`tts_voice_reference（TTS 语音 / 音色参考）` 管声音质感、可爱向导音方向和 custom voice 底子。
- TTS voice reference 当前包括 `voice_sample2_cute_guide_voice_candidate_20260426`、脱敏 custom voice `qwen-t...ac19`、`target_model = qwen3-tts-vc-realtime-2026-01-15`；该项仍是 candidate / pending，不得写成 final voice passed、`voice_validation = passed` 或 `final_voice_validated = true`。
- round34、v3、PR #7 B、cute card、TTS 不得被默认输出成“当前固定素材锚点”；其中 v3 仍只作历史候选 / 对照，其他 reference whitelist 项不得因清库口径被误判为废弃。
- PR #46 只保留为未来流程 / 教学 / 操作拆解类视频升级方向资料，不作为当前 reference，不写成主读取分支正式状态，不写成内容通过。
- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 目录本轮冻结不动；不得纳入、删除、移动或改名。

- `round34` 只能作为历史中段剪辑 / 提示卡参考，不是当前最新样片状态。
- PR #22 仍是 v3 历史候选草稿 PR；v3 不再作为后续默认修改基础，不得直接合并覆盖当前 v3.1 基线。
- PR #23 的“PR #7 A 优先”是旧只读判断，已被用户最新确认覆盖；PR #23 只能作为历史样本包。
- PR #24 的 v3.1 有效产物已安全回流到主读取分支；PR #24 本身不得再直接合并，以免回退 PR #25 清理结果。
- 后续骚萌卡唯一执行参考是 `PR7_B_骚萌反应页.png`；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- PR #7 A 只能作为历史 / candidate 对照，不能出现在任何未来执行 reference 字段里。
- `归档_archive/旧口径_old_context_*/` 只保存旧判断证据，不作为默认事实入口。
- 后续所有 v3.1 基线升级必须保留并复核 `visual_route_map.json（视觉路由表）`，不得让段落提示卡、信息卡、骚萌卡共用同一套外壳。

### 2.2C 《视频工厂》单工作区硬规则 single_workspace_rule

`已确认` 《视频工厂》唯一正式工作区固定为：

- `/Users/fan/Documents/视频工厂`

硬规则：

- Codex 后续不得默认新建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees` 作为外部散工作区。
- 如果需要新分支，必须在 `/Users/fan/Documents/视频工厂` 内执行 `git switch -c <branch>` 或切换既有分支。
- 不得默认使用 `git worktree add` 创建外部 Git 工作区；除非用户当轮明确授权。
- 不得默认新建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区。
- 如果 Codex 判断确实需要 fresh clone / 外部对照 / 外部 worktree / 任何外部目录，必须先停止，回报 `reason（原因）`、`target_path（目标路径）`、`risk（风险）`、`internal_alternative（唯一正式工作区内替代方案）`，等待用户本轮明确确认后才能继续。
- 所有最终产物、样片、复审包、截图归档、治理报告、路径索引、执行日志和清理记录，都必须落在 `/Users/fan/Documents/视频工厂` 内部。
- `/Users/fan/Desktop`、`/Users/fan/Downloads`、`/private/tmp`、`/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*` 不得作为最终交付路径。
- 如果必须临时读取外部路径，只能作为 `source（来源）` 只读读取；必须回收到唯一正式工作区后，才能写入路径索引或默认执行口径。
- 已经产生的外部工作区必须收回到唯一正式工作区内部的 `本地归档_local_archive/` 或 `本地隔离区_local_quarantine/`；不得继续散落在 `/Users/fan/Documents` 顶层。
- `已确认` 用户已明确授权 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除`。该路径只用于归档 / 删除候选池，不是执行工作区，不是 fresh clone，不是 worktree，不得作为默认读取入口。
- `codex_log/current_local_artifact_paths.md` 的 `canonical_local_path（首选本地路径）` 只能指向 `/Users/fan/Documents/视频工厂` 内部。
- 旧外部路径最多只能写为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）`，不得作为默认执行路径。
- 后续清理、归档、迁移任务也必须从 `/Users/fan/Documents/视频工厂` 发起、记录和提交。

若任务继续命中《视频工厂》的内容生产，再补读：
8. `GPT数据源/04_选题与文案规则.md`
9. `GPT数据源/05_文案路由规则.md`
10. `GPT数据源/07_AI知识类视频价值规则.md`

若任务继续命中《视频工厂》的阶段 / 复盘 / 商业化，再补读：
11. `GPT数据源/09_目标态计划.md`

若任务命中《视频工厂》的截图 / 数据截图 / 24h / 72h / 7 天 / 运营数据 / 发片复盘 / 发片 / 发布后 / 复盘 / 数据记录 / 私信 / 咨询，再补读：
12. `codex_log/current_operation_target.md`
13. `review_loop/operation_records_index.md`
14. `codex_log/current_data_goal_anchor.md`
15. `codex_log/current_gray_test_target.md（legacy compatibility pointer）`
16. `review_loop/00_review_loop_readme.md`
17. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
18. `review_loop/02_video_record_template.md`
19. `review_loop/03_result_dashboard_template.md`
20. `review_loop/04_diagnosis_template.md`
21. `review_loop/05_dual_review_handoff_template.md`
22. `review_loop/06_next_round_task_template.md`
23. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md（legacy metrics）`

截图优先录入机制硬规则：
- 命中“截图 / 数据截图 / 24h / 72h / 7 天 / 运营数据 / 发片复盘 / 私信 / 咨询”时，默认进入 `operation_data_intake（运营数据录入）`。
- 必须按 `video_id` 分开记录；不同视频不得混写。
- 必须按 `24h / 72h / 7d` 分开记录；不同时间窗不得互相覆盖。
- 必须按数据类型分开归档；平台数据、留存完播、互动、账号增长、评论、私信、咨询不得混写。
- Codex 只做截图归档、字段提取、缺失标记、初检和交接，不做最终内容判断。

后续复盘默认先回答四个问题：
1. 这条有没有达到 6000 播放基础门槛？
2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
3. 下一轮只改哪一个变量？
4. 为什么先改它，改完看哪个指标？

当前正式运营硬边界：
- 发片不等于内容过线
- 正式运营不等于验证成功
- 正式运营不等于商业验证成立
- 正式运营不等于数据飞轮跑通
- 正式运营默认出片比例为 `horizontal_16_9（横屏 16:9）`，默认交付分辨率为 `1920x1080`；这是用户为后续发布体验明确拍板的新口径。
- 旧 `vertical_9_16（竖屏 9:16）`、`1080x1920` 只保留为历史样片 / 历史提示卡 / 历史平台适配记录，不再作为当前正式运营视频交付默认比例。
- 正式运营视频交付任务默认只接受 `publish_candidate（可发布候选片）` 或 `blocked（阻断）`
- `technical_preview（技术预览）`、`technical_preview_candidate（技术预览候选）`、`preflight package（执行前补全包）`、`silent preview（无声预览）`、无音轨视频、横屏技术包、只交 JSON / Markdown / route card，只能作为 `internal_diagnostic_only（内部诊断产物）`，不能写 `completed`、不能写内容推进、不能写视频执行完成
- `已确认` 正式运营阶段用户只负责目标修正、页面 / 美观 / 观感对标，以及如实反馈结果是否合格；用户不负责替 GPT / Codex 排查内部执行原因。
- 当用户反馈“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，GPT / Codex 必须触发 `self_repair_audit（自修审计）`，自行回查 locked goal、locked title、final script、文案到画面映射、字幕 / 卡片、音轨 / TTS、比例、时间线、导出参数、数据目标锚点、交付基线、Git 同步和是否存在降级冒充完成；不得要求用户诊断内部原因。
- `Codex` 后续不得降级完成任何正式运营交付任务。凡仓库写明的目标、产物、验证、同步、回报未全部完成，必须 `blocked` 或继续修到满足基线，不得用 fallback、技术预览、局部结果、内部诊断、无声视频、比例错误视频、本地未同步产物或只读报告冒充 `completed`。
- 降级方案只能作为 `blocked` 后待用户确认的修复建议；必须写清原目标为什么做不到、缺哪层能力、降级会损失什么、是否需要用户授权。未经用户明确授权，不得把降级方案当成交付。
- `completed` 只能用于仓库写明的目标、产物、验证、同步和回报全部完成；`partial_completed` 只允许用于用户明确接受的分阶段任务；`internal_diagnostic_only` 只用于内部诊断产物，不能作为用户交付物。
- 进入做视频 / 产视频 / 发片候选 / 运营内容 / 下一条视频任务时，必须先判断是否具备 `publish_candidate` 条件；不具备则写 `blocked_publish_candidate_unavailable`，不得继续生成低标准产物冒充交付
- 视频执行前必须建立 `locked_copy_contract（锁定文案契约）`，至少包含 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。
- `Codex` 是视频执行层，不是重新定稿层；可以调整标点、换行、字幕分句、TTS 停顿、素材映射、剪辑节奏、卡片位置、比例和导出，但不得擅自改 `locked_topic`、`locked_title`、`locked_opening_line`、核心判断、人味表达、文案语义或视觉标题卡标题。
- 如果 `Codex` 判断标题太长、文案太长、句子不适合画面、TTS 不适配或素材无法支撑，必须输出 `copy_change_request（文案修改请求）` 或 `blocked`，不得自行改稿。
- 视频执行不得只做段落级映射；`script_to_timeline_map（文案到时间线映射表）` 必须做到 `line_group` 级别，通常每 1-2 句一个 `line_group`，并包含 `line_group_id / narration_text / source_timecode / expected_visual / allowed_visuals / forbidden_visuals / subtitle_text / card_text_if_any / evidence_strength / alignment_status / blocked_if_visual_mismatch`。
- 缺 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）`、只有段落级素材分配、或出现“口播说 A，画面显示 B”且未修复时，不得生成视频或写完成；必须改映射、请求文案变更或 blocked。
- 导出前必须做 `subtitle_card_overlap_check（字幕卡片重叠检查）`；口播字幕、标题卡、解释卡、总结卡、画面 OCR 和关键证据区域不得出现 high severity overlap。修不了则 blocked，不得完成。
- 用户明确说“视频已经发了 / 已发布”时，触发 `post_publish_no_rework_boundary（已发布视频不默认回炉边界）`：当前视频进入 `operation_data_intake / operation_review` 数据回流，只允许记录反馈、复盘诊断、修补机制或下一轮规则；不得默认重做、回炉或修改已发布视频。
- `send_ready` 仍保持 `false`
- `visual_master_locked` 仍保持 `false`
- PR #7 B 仍是后续骚萌卡唯一执行参考，PR #7 A 仍只作历史 / candidate 对照
- 下一轮文案前必须先看当前运营目标、运营记录索引、当前数据目标锚点和正式运营复盘四问

### 2.3 `AI 直播前台验证项目` 命中规则
若任务命中以下任一关键词，默认按 `AI 直播前台验证项目` 接手：
- `AI 直播前台`
- `直播前台`
- `数字人前台`
- `抖音高分直播间`
- `阿里数字人`
- `ASR`
- `TTS`
- `RTC`
- `推流`
- `云直播`
- `多房间扩容`
- `1 台阿里云服务器带 5 个直播间`

命中直播项目后，默认先读：
1. `项目资料_docs/系统协议_system/00_协作协议_collaboration_protocol.md`
2. `项目资料_docs/直播前台项目_live_frontend_project/00_项目总说明_project_brief.md`
3. `项目资料_docs/直播前台项目_live_frontend_project/01_执行合同与验收_execution_contract.md`
4. `项目资料_docs/直播前台项目_live_frontend_project/02_当前任务与研究问题_current_task.md`

### 2.4 未命中时的阻断规则
若任务未命中《视频工厂》或 `AI 直播前台验证项目` 任一关键词，则必须：
1. 先阻断，不得直接进入任一项目业务判断
2. 先把当前任务标记为：`待路由`
3. 先做项目分流判断，再继续执行

### 2.5 双命中或冲突命中
若同一任务同时命中两个项目关键词，默认先按“路由层冲突”处理：
1. 先识别任务到底是在修入口 / 修分流 / 修接手机制，还是在处理某一项目业务
2. 若属于入口 / 分流 / 接手机制，先只修路由层，不扩写业务规则
3. 若属于业务任务，再按显式目标对象选择唯一项目入口
4. 先输出当前冲突点
5. 再给一个最小路由判断

若任务命中不清，也按同一规则处理：
1. 先输出冲突点
2. 再给一个最小路由判断
3. 未完成路由前，不直接拍板进入任一项目

## 2.6 Codex 执行前路由闸门 route_decision_gate

每次执行任何任务前，Codex 必须先完成并输出 `route_decision（路由判断）`。

没有完成 `route_decision（路由判断）`，不得修改文件、不得生成产物、不得删除文件、不得提交 commit、不得 push。

`route_decision（路由判断）` 必须包含：

1. `project_route（项目路由）`
   - `video_factory（视频工厂）`
   - `live_frontend（AI 直播前台验证项目）`
   - `unrouted（待路由）`
   - 若未命中任一项目，必须 blocked，不得继承任何项目事实。
2. `task_type（任务类型）`
   - 必须从 `project_file_change（项目文件修改）`、`copywriting（文案写作 / 改写）`、`video_sample_or_assembly（视频样片 / 成片）`、`review_diagnosis_audit（复盘 / 诊断 / 审核）`、`code_debug（代码执行 / 调试）`、`external_research_bridge（外部调研 / 收束）`、`mechanism_or_route_fix（机制修补 / 路由修补）`、`local_file_governance（本地文件治理 / 工作区治理）`、`data_review_loop（数据记录 / 灰度复盘）` 中选择一项或多项。
3. `responsibility_layer（责任层级）`
   - 必须从 `entry_routing_layer（入口路由层）`、`project_judgment_layer（项目判断层）`、`execution_layer（执行落地层）`、`validation_layer（验收复审层）`、`sync_layer（同步回写层）`、`mechanism_fix_layer（机制修补层）`、`multi_agent_lane_layer（多执行器 / 多 lane 层）` 中选择。
4. `large_task_gate（大任务闸门）`
   - 每次执行前必须判断是否触发；触发后必须读取 lane / parallel 规则并输出 lane / parallel 判断。
5. `supply_source_arbitration（供料来源裁决）`
   - 每轮任务默认先判断 `Vector RAG / DashVector retrieval -> GitHub / 仓库原文件 readback -> DeepSeek trigger decision`，不得把 DeepSeek 当作每轮默认文件供应商或项目记忆。
   - 必须输出 `retrieval_manifest（检索清单）`、`source_readback_status（事实源回读状态）`、`deepseek_trigger_decision（DeepSeek 触发判断）` 和 `not_deepseek_conclusion（是否不是 DeepSeek 结论）`。
   - 只有 DeepSeek 被条件触发或用户明确要求时，才需要创建 `supply_request（供料请求任务卡）` 并输出 `deepseek_participation_report（DeepSeek 参与报告）`、`token_usage_expectation_check（token 使用预期检查）`、`fallback_status（fallback 状态）`；token 未观察到减少时，不得写 DeepSeek 已深度参与。
6. `must_read_files（本轮必读文件）`
   - 必须列出本轮执行前要读的文件，并说明为什么要读；不允许只读 `AGENTS.md` 就开始执行。
7. `read_status（读取状态）`
   - 每个必读文件必须标记 `read_ok（已读取）`、`missing（文件不存在）`、`unreadable（无法读取）` 或 `not_applicable（本轮不适用）`。
8. `allowed_changes（允许修改范围）`
   - 必须列出本轮允许修改的文件或目录；未列入允许范围的文件，默认不得修改。
9. `forbidden_changes（禁止修改范围）`
   - 必须列出本轮禁止修改的文件、目录、状态字段或高风险动作；任务涉及《视频工厂》时，默认禁止误改 `content_validation（内容验证）`、`send_ready（可发送状态）`、当前发布状态和 `dist/latest_review_pack/（最新复审包）`，除非用户本轮明确授权。
10. `blocked_if（阻断条件）`
   - 项目未路由清楚、任务类型未判断清楚、责任层级未判断清楚、关键必读文件 missing / unreadable、允许 / 禁止范围不清楚、需要新建外部工作区但未授权、需要删除 / 移动 / 替换高风险文件但未授权、需要把技术验证写成内容验证、需要把中间态写成完成态时，必须 blocked。
11. `execution_permission（执行许可）`
   - 只有项目路由、任务类型、责任层级、必读文件、关键读取状态、允许修改范围、禁止修改范围均明确，且未触发 `blocked_if（阻断条件）`，才允许执行。

最终回报必须复述本轮实际 `route_decision（路由判断）` 和实际读取文件，不得只写“已完成”。

### 2.6A 大任务闸门 large_task_gate

`large_task_gate（大任务闸门）` 是 `route_decision（路由判断）` 的子闸门。

Codex 每次执行前，除了判断项目路由、任务类型和责任层级，还必须判断本轮是否触发 `large_task_gate（大任务闸门）`。

触发条件：

1. 视频任务中，目标视频、样片、成片、剪辑对象或复审对象超过 `3 分钟 / 180 秒`。
2. 本轮同时涉及脚本、素材、reference、时间线、TTS、字幕、验证、日志中的三项或以上。
3. 本轮需要写入或检查 3 个以上仓库文件。
4. 本轮同时涉及规则文件、执行文件、日志文件或报告文件。
5. 本轮需要先做大量只读审计、定位、结构化整理，再统一写入。
6. Codex 判断单执行器可能遗漏段落、漏读文件、混淆内容层与执行层。
7. 用户明确提到“长视频”“大任务”“多文件”“多步骤”“多 agent”“并发”“提速”“检查很多文件”等。

触发后必须读取：

1. `codex_source/13_execution_lane_and_parallel_rules.md（执行车道与并发规则）`
2. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（给 GPT Project 用的多执行器路由说明）`

触发后必须输出：

1. `large_task_gate.triggered`
2. `large_task_gate.reason`
3. `lane_recommendation`
4. `lane_reason`
5. `lane_invalid_if`
6. `parallel_recommendation`
7. `parallel_reason`
8. `parallel_invalid_if`
9. `write_owner`
10. `read_only_lanes`
11. `integration_owner`

硬规则：

- 触发 `large_task_gate（大任务闸门）` 不等于自动开启多 agent。
- 触发后必须先判断 `serial_only（串行执行）`、`read_parallel（只读并发）`、`explore_plus_integrate（探索 + 单点整合）`、`true_multi_task_parallel（真正多任务并发）` 哪个更合适。
- 若写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定，必须保持或降级为 `serial_only（串行执行）`。
- 未完成 lane / parallel 判断前，不得直接进入长视频、大文件、多步骤、多验证任务执行。

## 3. 文件与目录命名规则

从现在开始，除工具链 / 系统强制要求的固定文件名外，之后所有新建业务文件和业务文件夹默认必须使用“中文 + 英文”命名。

推荐格式：
- `中文名_english_name`

该规则默认覆盖：
- 业务文件
- 文档文件
- 日志文件
- 资料文件
- 脚本文件
- 目录名

默认禁止：
- 新建纯英文业务文件名
- 新建纯英文文档文件名
- 新建纯英文日志文件名
- 新建纯英文资料文件名
- 新建纯英文脚本文件名
- 新建纯英文目录名

已有文件和已有文件夹本轮不追溯改名；后续若要迁移既有命名，必须另起审计任务，先确认引用、工具链约束和迁移风险。

固定例外：
- `AGENTS.md`
  原因：Codex 固定入口文件名，不能改。
- `README.md`
  原因：常见仓库入口文件名，外部工具和 GitHub 页面可能直接识别。
- `package.json`
  原因：Node.js / npm 工具链固定清单文件名。
- `package-lock.json`
  原因：Node.js / npm 工具链固定锁文件名。
- `.gitignore`
  原因：Git 固定忽略配置文件名。
- `.git/`
  原因：Git 系统目录。
- `.github/`
  原因：GitHub 工作流与仓库配置固定目录。
- `node_modules/`
  原因：Node.js 依赖安装目录。

工具链强制例外规则：
- 若未来遇到工具链强制英文固定文件名，必须明确标注为“工具链强制例外”
- 必须写清楚为什么不能改名
- 不允许把例外范围扩大到普通业务文件

系统目录说明：
- `.git/`、`.omx/`、`.gitignore`、`package.json`、`package-lock.json` 等现有工具链 / 系统文件属于历史或工具运行要求，不作为新建业务命名范例

## 4. 默认修改权限规则

默认不要随便改：
- 协作协议类文件
- 项目总说明类文件

在任务明确要求时可以更新：
- `项目资料_docs/直播前台项目_live_frontend_project/01_执行合同与验收_execution_contract.md`
- `项目资料_docs/直播前台项目_live_frontend_project/02_当前任务与研究问题_current_task.md`

允许持续更新：
- `codex_log/latest.md`
- 其他阶段摘要 / 执行日志类文件

## 5. 默认执行规则

执行前默认动作：
- 先读 `AGENTS.md`
- 执行前必须先输出并通过 `route_decision（路由判断）`；未通过前不得修改任何文件。
- 先判断当前任务命中哪个项目入口
- 先判断当前任务属于账号层、项目层、执行层还是路由层
- 未命中项目入口前，不得擅自继承任何项目业务事实
- 命中《视频工厂》后，再按《视频工厂》入口继续
- 命中《视频工厂》后，账号层长期规则仍按硬约束执行；若用户当前在问机制层 / 配合层问题，先答机制层，不直接被项目业务细节带走
- 命中直播项目后，再按直播入口继续

形成可判断小闭环后，默认动作：
1. 先更新 `codex_log/latest.md`
2. 命中条件时补完整执行日志
3. 显式 stage 本轮相关文件，禁止默认 `git add .`
4. 对 staged diff 做 secret scan
5. commit 当前改动
6. push 到当前主读取分支 / 当前任务分支
7. 校验远端 HEAD 或远端目标 commit 可读
8. 再交回 GPT 基于 GitHub 最新结果复审

不要只在本地改完就停。

### 5A. mandatory_commit_push_gate（强制提交推送闸门）

`mandatory_commit_push_gate` 默认 active。以后任何最小任务只要创建或修改了仓库文件，`completed（已完成）` 在 Git 收尾完成前一律禁止。

```text
mandatory_commit_push_gate:
  status: active
  applies_to:
    - any_minimal_task_with_repo_file_changes
    - project_file_change
    - mechanism_repair
    - code_change
    - script_change
    - fixture_or_test_change
    - log_change
    - GPT_Project_sync_package_change
    - review_pack_schema_or_rule_change
  completed_requires:
    - relevant_files_staged_explicitly
    - commit_created
    - push_succeeded
    - remote_head_verified
    - no_unrelated_dirty_files_committed
    - no_secret_committed
  completed_forbidden_if:
    - local_changes_uncommitted
    - commit_created_but_not_pushed
    - pushed_to_wrong_branch
    - remote_head_not_verified
    - unrelated_dirty_files_mixed_into_commit
    - secret_scan_failed
    - only_local_output_exists
  allowed_non_push_cases:
    - truly_read_only_task_with_no_file_changes
    - blocked_before_any_file_change
    - user_explicitly_says_do_not_commit_or_push_this_round
  non_push_status:
    - no_file_change_completed_readonly
    - blocked
    - partial_completed
  default_rule:
    - If repository files changed, completed is forbidden until commit + push + remote verification is done.
```

`completed` 的仓库改动条件固定为：

```text
completed:
  required_if_repo_files_changed:
    - relevant_files_committed = true
    - pushed_to_current_reading_branch = true
    - remote_head_verified = true
    - unrelated_dirty_files_not_committed = true
    - secret_scan_passed = true
```

如果本地任务完成但未 push，只能写：

```text
partial_completed:
  reason: local_changes_done_but_not_pushed

blocked:
  reason:
    - push_failed
    - current_branch_unclear
    - unrelated_dirty_files_cannot_be_isolated
    - secret_scan_failed
    - remote_head_not_verified
```

Codex 最终回报必须默认包含：

```text
git_sync_status:
  current_branch:
  files_changed:
  files_staged:
  commit_sha:
  pushed:
  remote_head_verified:
  unrelated_dirty_files:
  secret_scan:
  completed_allowed:
```

什么叫“可判断小闭环”：
- 已完成一轮明确文件修改
- 已形成一版可读的规则稿 / 项目骨架 / 研究稿
- 已形成新的 blocker / 冲突点 / 交接点，需要基于真实结果判断
- 已完成一轮值得复审的仓库改动

可以暂不 push 的情况：
- 当前仍是明显半成品
- 改动边界仍在摇摆
- 还没形成可判断小闭环
- 日志还没更新
- 本轮只有纯读取、无修改、无新结论

额外硬规则：
- 路由层任务只修入口、分流、接手顺序与已知边界，不擅自改业务规则

## 6. 诚实状态标记规则

凡涉及完成度、验证情况、可行性、自动化程度、能力边界，必须明确标状态。

默认只使用：
- 已确认
- 部分成立
- 待验证
- 推测
- 通用建议

禁止把中间态说成完成态。

## 7. 表达规则

- 默认中文沟通优先
- 命令、代码、配置键、字段名、环境变量、路径、报错原文、术语保留英文原词
- 先给主结论，再给最必要说明
- 需要复制的内容默认放进完整 Markdown 代码块
- 文件名、目录名、字段名、配置项若出现英文，默认使用“原文 + 中文备注”或直接换成清楚中文

## 8. 最终汇报与交接口径

- 以后最终汇报最后一栏统一使用“下一个目标”。
- 不再默认使用“下一步行动建议”。
- “下一个目标”必须表达下一轮要达成的状态，而不是泛泛行动建议。
- 如果必须写动作，动作必须服务于“下一个目标”。
