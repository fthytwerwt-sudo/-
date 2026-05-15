# codex_source 总入口

## 0A. 2026-05-15 formal_operation current entry

`已确认` 《视频工厂》当前阶段已迁移为 `formal_operation_active（正式运营中）`。

Codex 后续默认先读：

- `codex_log/current_operation_target.md`
- `review_loop/operation_records_index.md`
- `codex_log/current_data_goal_anchor.md`

`codex_log/current_gray_test_target.md` 只作为 `legacy_compatibility_pointer（历史兼容指针）`；旧 `gray_test_*` 状态不得继续作为当前默认路由。新数据录入走 `operation_data_intake`，复盘走 `operation_review`，下一轮变量判断走 `operation_next_variable_decision`。

## 0A-1. formal_operation delivery baseline gate

`已确认` 项目进入 `formal_operation_active（正式运营中）` 后，凡任务目标指向做视频、产视频、发片候选、运营内容、下一条视频或发布候选，默认交付结果只能是：

1. `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`
2. `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`
3. `not_applicable（本轮不适用视频交付）`

`technical_preview（技术预览）`、`technical_preview_candidate（技术预览候选）`、`preflight package（执行前补全包）`、`silent preview（无声预览）`、无音轨视频、横屏技术包、只交 JSON / Markdown / route card，只能写为 `internal_diagnostic_only（内部诊断产物）` 或 `historical_internal_diagnostic_only（历史内部诊断产物）`，不得写成用户交付物、阶段完成、内容推进或视频执行完成。

`已确认` 从 2026-05-16 起，正式运营默认出片比例改为 `horizontal_16_9（横屏 16:9）`，默认交付分辨率为 `1920x1080`。原因是用户明确拍板“以后发横屏视频”，且屏幕录制、文档、表格、指标分层和客资评分内容更适合横屏观看。

若缺音轨、字幕、横屏 16:9 / 1920x1080 装配、清楚开头、中段证据、结尾收束、基础人感质量、平台风险检查、API 授权或装配能力，Codex 必须 blocked 或修到满足 `publish_candidate`，不得把“技术能跑”偷换成“项目能交付”。`publish_candidate` 仍需 ChatGPT / 用户按发布标准复审，不能自动推进 `send_ready（可发送状态）`。

## 0A-2. user_feedback_boundary and no_degrade_completion gate

`已确认` 正式运营阶段，用户只负责：

1. `goal_correction（目标修正）`
2. `page_aesthetic_reference（页面 / 美观 / 观感对标）`
3. `result_quality_feedback（结果是否合格的如实反馈）`

用户不负责替 GPT / Codex 排查内部执行原因。用户说“不合格 / 不对 / 不顺 / 不美观 / 不是我要的 / 文案画面对不上 / 标题被改 / 比例错 / 声音不行 / 字幕不对”时，Codex 必须触发 `self_repair_audit（自修审计）`，自行回查：

- locked goal / locked title 是否被改写
- final script 是否被 Codex 越权改写
- script_to_timeline_map 是否逐句成立
- subtitle / card / audio / TTS / aspect_ratio / final_media_probe 是否达标
- data_goal_alignment_check 与 publish_candidate_checklist 是否真实通过
- Git commit / push / GPT Project sync 是否按任务完成
- 是否存在 fallback、internal diagnostic、local-only output、partial result 冒充 completed

`no_degrade_completion_gate（禁止降级完成闸门）`：

- Codex 不得把 fallback 当完成。
- Codex 不得把 `internal_diagnostic_only` 当完成。
- Codex 不得把 `partial result（局部结果）` 当完整交付。
- Codex 不得把本地生成当已 push。
- Codex 不得把技术成功当内容成功。
- Codex 不得把“没有明确失败”当完成。
- 做不到仓库写明的目标时，必须 `blocked`，不得包装成 `completed`。

`completion_truth_check（完成真实性检查）`：

- 对照用户原目标、仓库基线、required_output_inventory、验证命令、日志、commit / push / sync 逐项核验。
- 任何“目标未达成但产物存在”“验证未跑但看起来能用”“本地有文件但未同步”“中间层完整但交付物缺失”的结果，都不能写 `completed`。

`fallback_requires_user_authorization（降级需要用户授权）`：

- 降级方案只允许作为 `blocked` 后的修复建议。
- 输出降级建议时必须写清原目标为什么做不到、缺少哪一层能力、降级会损失什么、是否需要用户授权。
- 用户明确授权前，任务状态必须是 `blocked`，不是 `completed`。

## 1. 这份文件是什么

本文件是《视频工厂》当前 Codex 执行层入口。

它是《视频工厂》子入口，不是整个仓库的总入口；仓库总入口与项目分流规则统一看 `AGENTS.md`。

它负责回答：

- `codex_source/` 是干什么的
- 新会话最小先读什么
- 当前正式默认主线是什么
- 当前主读取分支是什么
- GPT 数据源与仓库不同步时，谁算源事实
- 当前 10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线默认该怎么读

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

当前项目正式事实正文属于 `GPT数据源/` 当前 10 份基础执行包 + OPC 总纲 + 状态动作总控器 + 参考到执行落地契约 + 目标驱动数据飞轮与文案执行闭环 + 数据目标执行总线；`project_source/` 只作为历史 / 辅助主题化镜像，不再作为当前主事实源。代码实现细节仍归代码层。

`归档删除区_archive_delete_zone/` 只用于隔离旧口径、旧入口、旧产物候选与清单；默认不得读取，不得作为当前事实、当前执行入口或当前复审入口。

## 3. 新会话最小接手入口

新 Codex 会话默认最少先读：

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `GPT数据源/00_项目总述.md`
5. `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
6. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
7. `codex_source/19_project_state_action_router.md`
8. `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
9. `codex_source/20_reference_to_execution_contract.md`
10. `GPT数据源/01_项目系统提示词.md`
11. `GPT数据源/03_总索引与阅读顺序.md`
12. `GPT数据源/08_当前正式事实.md`
13. `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`

每次 Codex 执行前必须先通过 `route_decision（路由判断）`；未输出项目路由、任务类型、责任层级、必读文件与读取状态前，不得执行。

`route_decision（路由判断）` 通过后、进入具体执行前，必须再读取 `codex_source/19_project_state_action_router.md` 并输出 `state_action_router（项目状态动作总控器）`，判断当前状态、事实源裁决、触发机制、选择动作、完成标准和阻断条件。

若任务命中长视频、大信息量、多文件、多步骤、多验证，或用户明确提到多 agent / 并发 / 提速，Codex 必须在 `route_decision（路由判断）` 阶段触发 `large_task_gate（大任务闸门）`，并读取 `codex_source/13_execution_lane_and_parallel_rules.md` 与 `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`。

若任务命中文案修改、下一条视频、根据数据改、播放低 / 收藏低 / 客资弱、复盘后重写、数据飞轮、目标驱动、数据目标、单主变量、内容结构反馈、视频执行、剪辑、编排、DeepSeek 供料或 GPT Project 静态包同步，Codex 必须补读：

- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
- `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`
- `review_loop/` 当前视频复盘记录
- 当前 `video_goal_card（视频目标卡）`
- 当前 `post_publish_review_card（发布后复盘卡）`
- 当前 `data_flywheel_memory（数据飞轮记忆）`
- 当前 `content_structure_feedback_card（内容结构反馈卡）`

缺 `threshold_config_v1（阈值配置 V1）`、`video_goal_card（视频目标卡）`、`post_publish_review_card（发布后复盘卡）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`next_video_execution_prompt（下一条视频执行 prompt）`、`data_goal_anchor（数据目标锚点）` 或 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）` 时，不得声称“根据数据正式改文案”，也不得进入视频执行。

`codex_log/current_data_goal_anchor.md` 若为 `draft / waiting_data`，只能做假设版、机制接线、供料任务卡或 blocked，不得写正式数据驱动执行 ready。

缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写 Codex 视频执行完成。

## 3A-0. Project State Action Router 执行入口

命中任何复杂任务、机制修补、文案执行、视频执行、发布复盘、数据回填、GPT Project 静态包同步、Codex 执行结果回审时，Codex 都必须先读：

- `codex_source/19_project_state_action_router.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`

并在具体执行前输出 `state_action_router（项目状态动作总控器）`。

最小判断链：

```text
input_signal
-> fact_source_arbitration
-> current_project_state
-> trigger_mechanism
-> selected_action
-> done_when
-> blocked_if
-> feedback_update_required
```

`state_action_router` 不替代 `route_decision（路由判断）`；它只补充“当前状态 -> 下一动作”。

`state_action_router` 也不替代 `Completion Relay Gate（补全接力闸门）`；前者判断该做什么，后者保证做到底并反查剩余工作。

## 3A-1. Reference-to-Execution Contract 执行入口

命中 `reference（参考）`、样片、参考图、参考视频、参考声音、参考效果、“按这个做”、“像这个效果”、原感稿或外部资料并要求落地时，Codex 必须先读：

- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/20_reference_to_execution_contract.md`

并在具体执行前输出：

```text
reference_to_execution_contract:
  reference_anchor:
  effect_targets:
  function_fields:
  execution_mapping:
  deviation_check:
  done_when:
  blocked_if:
```

硬规则：

- 没有契约，不得执行带 reference 的任务。
- 没有 `deviation_check（偏离检查）`，不得写 `completed（已完成）`。
- DeepSeek / Perplexity 摘要只能辅助供料，不得替代 reference contract。
- reference 与当前项目事实冲突时，以 `Project State Action Router（项目状态动作总控器）` 和当前仓库正式事实裁决。

## 3A-2. 目标驱动数据飞轮与文案执行闭环入口

命中以下任一信号时，Codex 必须先读取 `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`、`GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md` 与 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`：

- 文案修改
- 下一条视频
- 根据数据改
- 播放低 / 收藏低 / 客资弱
- 复盘后重写
- 数据飞轮
- 目标驱动
- 数据目标
- 单主变量
- 内容结构反馈
- 视频执行 / 剪辑 / 编排 / 装配
- DeepSeek 供料
- GPT Project 静态包同步

执行链：

```text
current_goal / threshold_config_v1 / previous_video_data
-> data_goal_copy_revision_gate
-> content_structure_feedback_card
-> single_primary_variable_rule
-> next_video_execution_prompt
-> current_data_goal_anchor
-> data_goal_anchor
-> Codex video execution preflight
-> data_goal_alignment_check
```

硬规则：

- 没有 `threshold_config_v1（阈值配置 V1）`，不得做数据驱动判断。
- 没有 `video_goal_card（视频目标卡）`，不得进入正式文案修改。
- 没有 `post_publish_review_card（发布后复盘卡）`，不得声称“根据数据修改文案”。
- 没有 `main_bottleneck（主短板）`，不得重写正式文案。
- 没有 `primary_variable（主验证变量）`，不得生成 Codex 执行 prompt。
- 没有 `next_video_execution_prompt（下一条视频执行 prompt）`，不得进入视频执行。
- 没有 `data_goal_anchor（数据目标锚点）`，不得进入视频执行、剪辑、编排或装配。
- 没有 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）` 当前实例入口，不得进入正式视频执行。
- 没有 `data_goal_alignment_check（数据目标对齐检查）`，不得写执行完成。
- 没有 `delivery_baseline_gate（交付基线闸门）`，不得把正式运营视频任务写成交付完成。
- `content_route_card / script_to_timeline_map / tts_prosody_anchor_map / editing_decision_pack / assembly_decision_pack / data_goal_alignment_check` 是视频执行前必备条件，不是用户最终交付物。
- 如果本轮目标是视频交付，最终结果必须回到 `publish_candidate_ready_for_human_review` 或 `blocked_publish_candidate_unavailable`；不得以技术预览、无声横屏预览或 JSON / Markdown 包收尾。
- 4 个变量必须标记 `major_revision（大改版）`；超过 4 个变量不得写成单变量实验。
- 本机制写入不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。

Codex 可以调整 segment 拆分、画面顺序、卡片位置、剪辑节奏、TTS 分句和装配顺序；降级方案只能作为 `blocked` 后待用户授权的修复建议，不能作为完成结果。Codex 不得调整 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）` 或发布后验证指标。

## 3A. OPC 上位身份与多 AI 协作入口

`已确认` 当前《视频工厂》上位身份已升级为：

`OPC 一人公司 AI 闭环验证系统`

命中《视频工厂》后，除原入口外，应补读：

- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`

当前多 AI 协作默认边界：
- `ChatGPT` = 总控脑 / 判断层
- `Codex` = 唯一写入执行层 / `Integrator`
- `DeepSeek` = 每轮默认只读供料层 / `Explorer`
- `Perplexity` = 外部研究层
- 其他 AI / 工具 = 按任务补位

硬规则：
- DeepSeek 是每轮 Codex 任务默认进入的只读 `Explorer（探索器）` / 供料层，输出上下文包、必读文件地图、风险冲突报告、执行后风险复核和 Codex 下一步输入。
- DeepSeek 不得写文件，不得拍板项目事实，不得替代 Codex 验证。
- Codex 仍是唯一写入 `Integrator（统一执行者）`，负责把 DeepSeek 供料整合为可执行改动，并补齐字段、脚本、schema、fixture、日志、上传包、验证和 Git 收尾。
- `reference（参考）`、`reference_quality_sample（参考质量样片）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 默认锁质量机制，不锁死每条内容的固定流程。

DeepSeek 供料中控最小入口：
- 每轮任务在 `route_decision（路由判断）` 后必须输出 `deepseek_supply_gate（DeepSeek 供料闸门）`，并默认运行或准备运行 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py（DeepSeek 安全供料运行器）` 或 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`。
- Codex 必须先生成或使用 `supply_request（供料请求任务卡）`，并通过 `--request-file` 传入，例如：`python3 scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py --request-file codex_source/fixtures/deepseek_supply_request_file_map_example.json`。
- 任务卡是 DeepSeek 获取当前任务上下文的正式输入；不得让 DeepSeek 自己猜任务、猜当前阶段或默认读取全仓库。
- 当任务涉及 `reference（参考）`、`locked reference（锁定参考）`、`visual route（视觉路由）`、`fixed_material_anchor（固定素材锚点）`、旧 SOP 风险或质量机制锁时，Codex 必须先生成或使用对应 `supply_request（供料请求任务卡）`，再运行 `scripts/deepseek_supply_controller.py --request-file <request_path>`。
- 推荐 safe runner 默认调用 `DeepSeek runtime provider（DeepSeek 运行时供应商）`，由 provider 按 `process_env -> .env.local -> .env -> 本地运行配置_local_runtime/deepseek_runtime_authorization.local.json` 的顺序自动加载授权 key source，并只注入 DeepSeek 子进程 env。
- controller / explorer 不直接读取 `.env` 或本地授权文件；它们只接收 provider 注入后的子进程 env，且必须保持 `env_file_read = false`、`api_key_printed = false`、`api_key_written = false`。
- controller 结果必须回流到 `dist/deepseek_supply_controller/latest_supply_pack.md` 与 `dist/deepseek_supply_controller/latest_supply_pack.json`。
- Codex 后续执行必须读取供料包后再复核原文件；若供料来源是 `fallback_local_only（本地兜底）`，只能把它当作本地资料包，不得写成 DeepSeek 真实生成通过或 DeepSeek 结论。
- controller 通过不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- 后续任何任务必须先输出 `deepseek_readiness_check（DeepSeek 就绪检查）` 与 `deepseek_participation_report（DeepSeek 参与报告）`：`deepseek_passed` 才能写真实参与；`fallback_local_only` 必须写 `not_deepseek_conclusion = true`；provider 缺 key 时必须写 `runtime_setup_required（需要运行时安装）`，不得每轮重复退回 process env 缺 key。
- 用户明确要求 DeepSeek 必须真实参与时，DeepSeek blocked 或 fallback = 整体任务 blocked，不能写 completed。
- `token_usage_expectation_check（token 使用预期检查）` 必须进入最终回报；如果 token 未观察到减少，不得写 DeepSeek 已深度参与。

质量与反馈三卡执行闸门：
- 命中内容表达文案、视频样片 / 成片、发布前检查、发布后复盘、`reference / locked reference / visual route` 继承或大任务 / 多文件任务时，Codex 必须在 `route_decision（路由判断）` 中判断三张机制卡是否必需。
- `content_route_card（内容路由卡）` 负责解释这条内容为什么这样承载，防止先锁死人物段次数、卡片数量或 PPT 数量。
- `quality_lock_card（质量锁卡）` 负责锁执行前质量底线，不等于 `content_validation（内容验证）` 已通过。
- `review_variable_card（复盘变量卡）` 负责把发布前 / 发布后复盘收束到单变量观察，不等于最终内容判断。
- 三张卡是判断机制，不是固定 SOP；若供料来源为 `fallback_local_only（本地兜底）`，仍必须写 `not_deepseek_conclusion = true` 并复核原文件。
- 上述卡片、时间线映射、TTS 韵律锚点、剪辑 / 装配决策包和数据目标对齐检查只属于 `preflight_required_inputs（执行前必备输入）`，不能替代正式运营阶段的视频交付；视频交付仍必须是 `publish_candidate` 或 `blocked`。

三大机制推理函数执行入口：
- `content_route_card（内容路由卡）` 必须由 `content_route_inference_function（内容路由推理函数）` 生成或引用其判断；缺 `validation_goal / core_evidence / flow_flex_reason` 时不得进入视频执行。
- `editing_decision_pack（剪辑决策包）` 必须由 `editing_inference_function（剪辑推理函数）` 生成或引用其判断；缺素材证据、时间码或上下文保护判断时不得写完成。
- `quality_lock_card（质量锁卡）` 必须调用 `quality_issue_classifier（质量短板分类器）`；用户反馈“不对 / 怪 / 不顺 / demo 感”时先分类最高优先级短板，再决定下一轮只改一个变量。
- 三个函数统一使用 `input_signal -> observed_evidence -> state_inference -> action_policy -> validation_rule -> blocked_if -> feedback_update`，不是固定 SOP，不推进动态状态。

## 3B. ChatGPT -> Codex 补全接力入口

当 Codex 收到 ChatGPT 的完整执行单、横向补全包或包含 `Goal` / `Context` / `Constraints` / `Impact check` / `Must read` / `Execution steps` / `Done when` / `Blocked if` / `Output` 的任务时，不得只按显性用户点名动作执行。

Codex 必须先触发 `Completion Relay Gate（补全接力闸门）`，把上游栏目转成：

- `completion_map（补全地图）`
- `required_output_inventory（必须交付清单）`
- `child_task_graph（子任务树）`

执行后必须反查：

- `remaining_work_check（剩余工作检查）`
- `sync_back_check（同步回写检查）`

最终回报不得只写“已完成”。如果 `required_output_inventory（必须交付清单）` 中仍有未完成项，Codex 必须继续执行；若命中阻断条件则写 `blocked（阻断）`。`partial_completed（部分完成）` 只允许用于用户明确接受的分阶段任务，不得替代完整交付任务里的 `blocked`。

Codex 的纵向补全不能替 ChatGPT 偷懒；ChatGPT 仍必须在上游提供足够完整的目标、上下文、边界、验收和阻断条件。但 Codex 不能因为 ChatGPT prompt 已经完整，就省略自己的任务树拆解和执行后反查。

2026-05-04 项目升级前清库覆盖口径：

- 当前唯一固定素材锚点是 `v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）`。
- `v31_element_doll_opening_preview（v3.1 元素娃娃开头预览）` 只保留为开头预览证据。
- `fixed_material_anchor（固定素材锚点）` 只有 v3.1 元素娃娃开头；但这不等于元素娃娃是唯一 reference。
- PR #7 B、cute card、round34 中段剪辑、TTS 节奏参考、TTS 语音 / 音色候选参考、`visual_route_map.json`、`locked_reference_registry.md` 仍属于 `reference_whitelist（参考白名单）`，后续按任务类型读取路径索引和 registry 复核后可继续使用。
- TTS 必须拆开：`tts_pacing_reference（TTS 节奏参考）` 管语速、停顿、轻吐槽、梗感和句间节奏；`tts_voice_reference（TTS 语音 / 音色参考）` 管声音质感、可爱向导音方向和 custom voice 底子。
- TTS voice reference 当前包括 `voice_sample2_cute_guide_voice_candidate_20260426`、脱敏 custom voice `qwen-t...ac19`、`target_model = qwen3-tts-vc-realtime-2026-01-15`；该项仍是 candidate / pending，不得写成 final voice passed、`voice_validation = passed` 或 `final_voice_validated = true`。
- round34、v3、PR #7 B、cute card、TTS 不得再被默认输出成当前固定素材锚点；其中 v3 仍只作历史候选 / 对照，其他 reference whitelist 项不得因清库口径被误判为废弃。
- PR #46 只保留为未来流程 / 教学 / 操作拆解类视频升级方向资料，不作为当前 reference。
- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 目录本轮冻结不动。

当前正式来源优先级：
1. GitHub / 本地 `main` 上的当前仓库文件
2. `GPT数据源/` 当前 10 份基础执行包 + `10_OPC一人公司闭环与多AI协作机制.md` + `11_项目状态动作总控器_机制推理层.md` + `12_参考到执行落地契约_reference_to_execution_contract.md` + `13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md` + `14_数据目标执行总线_data_goal_execution_bus.md`
3. `codex_log/latest.md`，重要结论仍需回查直接源文件
4. `dist/latest_review_pack/summary.json`
5. `dist/latest_review_pack/review_manifest.md`
6. `codex_source/` 执行规则
7. `project_source/` 历史 / 辅助镜像

本地可打开路径读取规则：
- 当 ChatGPT / Codex 需要给用户本地可打开路径时，必须优先读取 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`。
- 如果该索引中没有 `path_exists = true（路径存在）` 的记录，只能说“路径待本地复核”，不能直接把 `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径当成真实可打开路径。
- `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径只能作为线索，必须经 Codex 本地复核后才能输出给用户。
- 当需要给 GPT Project 上传包地址时，也必须优先读取 `codex_log/current_local_artifact_paths.md`。
- ChatGPT 不得凭聊天记忆直接给本地上传地址；必须以 Codex 本地审计结果或 `gpt_project_upload_package_canonical_path` 为准。
- GPT Project 规范上传包目录必须自带：`上传说明_UPLOAD_MANIFEST.md`。

单工作区硬规则 `single_workspace_rule`：
- 《视频工厂》唯一正式工作区是 `/Users/fan/Documents/视频工厂`。
- Codex 后续不得默认创建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*` 或 `/Users/fan/Documents/视频工厂-worktrees` 作为执行工作区。
- 新分支只能在 `/Users/fan/Documents/视频工厂` 内创建或切换；不得默认 `git worktree add` 到外部路径。
- 不得默认创建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区。
- 如果确实需要 fresh clone / 外部对照 / 外部 worktree / 任何外部目录，Codex 必须先停止并回报 `reason（原因）`、`target_path（目标路径）`、`risk（风险）`、`internal_alternative（唯一正式工作区内替代方案）`，等待用户本轮明确确认。
- 所有最终产物、复审包、截图归档、报告、路径索引、执行日志、清理记录都必须落在唯一正式工作区内部。
- `/Users/fan/Desktop`、`/Users/fan/Downloads`、`/private/tmp` 和外部 `/Users/fan/Documents/视频工厂*` 目录只能作为历史来源读取，不得作为最终交付路径。
- 已经产生的外部工作区必须收回到唯一正式工作区内部的 `本地归档_local_archive/` 或 `本地隔离区_local_quarantine/`；不得继续散落在 `/Users/fan/Documents` 顶层。
- `已确认` 用户已明确授权 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除`。该路径只用于归档 / 删除候选池，不是执行工作区，不是 fresh clone，不是 worktree，不得作为默认读取入口。
- `codex_log/current_local_artifact_paths.md` 的 `canonical_local_path` 只能指向 `/Users/fan/Documents/视频工厂` 内部；旧外部路径最多保留为 `historical_source_path` 或 `fallback_path`。
- 后续清理 / 归档 / 迁移任务也必须从唯一正式工作区发起和记录。

当前 `latest_review_pack` 已确认指向 `20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`；`current_video_baseline = v3.1`，后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于 v3.1；v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。v3.1 技术验证已通过，但 `technical_line_locked = false（技术线未锁定）`，下一步仍需技术升级。2026-05-15 起，当前项目阶段为 `formal_operation_active（正式运营中）`，当前运营入口为 `codex_log/current_operation_target.md`，三期数据索引为 `review_loop/operation_records_index.md`；旧 `post_publish_gray_test / gray_test_published / gray_test_status` 仅保留为 legacy_previous_term，不再作为当前默认项目阶段。正式运营不推进 `content_validation`、`send_ready`、`visual_master_locked`，也不代表商业验证成立。

若任务命中“完整成片 / 成品候选片 / 技术预览升级成候选片（只允许升级到 `publish_candidate`，不能保持 `technical_preview` 交付） / 样片回炉 / 开头重做 / 中段剪辑 / 字幕修正 / TTS 修正 / 功能卡修正 / 结果差卡修正 / 骚萌卡修正 / 录屏放大修正 / 视觉母版修正”，则在 `codex_log/latest.md` 之后必须先补读：

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

若任务命中“截图 / 数据截图 / 截图数据录入 / 灰度测试 / 发片 / 发布后 / 复盘 / 数据记录 / 24h / 72h / 7 天 / 播放量 / 完播率 / 留存 / 私信 / 咨询 / 下一轮只改一个变量”，则在 `codex_log/latest.md` 和 `codex_log/current_publish_target.md` 之后优先补读：

8. `codex_log/current_gray_test_target.md`
9. `review_loop/00_review_loop_readme.md`
10. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
11. `review_loop/02_video_record_template.md`
12. `review_loop/03_result_dashboard_template.md`
13. `review_loop/04_diagnosis_template.md`
14. `review_loop/05_dual_review_handoff_template.md`
15. `review_loop/06_next_round_task_template.md`
16. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
17. `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
18. `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
19. `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
20. `project_source/14_content_review_and_loop_governance_rules.md`

若任务命中“复盘后重写 / 文案结构调整 / 下一版文案 / 发布包装调整 / 风险表达改写 / 录屏承载修正”，必须读取 `review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md` 和 `review_loop/10_文案结构改版包模板_copy_revision_package_template.md`；不得从复盘数据直接跳到最终脚本或视频生成。

若任务涉及发布前检查，且内容属于 AI 工作流 / AI 教程 / 自动化流程 / 工具操作演示 / 命令行或 IDE 画面展示类视频，则还必须读 `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`，先输出平台风险检查结果，再进入发布。

发布后复盘规则：
- 灰度测试只是当前阶段名称，不另起独立灰度系统
- 单条记录、结果看板、诊断初检、双层交接和下轮草稿均走 `review_loop/`
- 24h / 72h 数据窗口、一次只改一个变量、小样本状态、异常样本和规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`
- v3.1 灰度测试指标体系 V1 看 `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- 截图数据录入任务先看 `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md` 和当前视频记录目录
- 用户可以直接给截图；Codex 负责按视频 / 时间窗 / 数据类型归档截图、提取字段、标记缺失和不确定项、更新记录
- 截图录入前必须先确认 `video_id`、`24h / 72h / 7d` 时间窗和数据类型；未确认不得入表
- `7d_play_count（7 天播放量）= 6000` 是当前小样本阶段基础测试流量门槛，不是最终商业目标
- 指标体系不是运营数据大表，而是下一轮改动定位器
- 后续复盘先回答四个问题：是否达到 6000 播放基础门槛、最短板在哪一层、下一轮只改哪一个变量、为什么先改它并看哪个指标
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
22. `GPT数据源/08_当前正式事实.md`
23. `project_source/09_target_state_plan.md`
24. 若需要历史镜像对照，再读 `归档删除区_archive_delete_zone/旧口径隔离_stale_context_quarantine/project_source/07_current_formal_facts.md`，但只能作为历史归档参考，不作为当前事实

若任务命中“什么算已知”，再补读：

25. `codex_source/12_codex_known_state_three_layer_rules.md`

## 4. 当前正式默认主线

当前正式默认主线 `已确认` 为：

- API 生成真人
- 用户录制素材
- 少量 PPT
- 云端剪辑

必须同时默认理解：

- 这条主线在 OPC 口径下是内容化输出的默认执行载体，不是项目总目标
- 结构跟着文案走
- `API生成真人段` 出现 1 次还是 2 次，是 block 路由结果
- pure PPT / 信息卡，不再是默认主线
- AI talking avatar / 数字人口播，不再是默认主线
- `云端剪辑 / cloud-only` 是当前正式方向，不等于 runtime 已稳定跑通
- `local preview` / `local mp4` 只能算辅助
- demo 只是链路锚点，不是质量样片

## 4A. 当前项目中心价值

当前项目中心价值 `已确认` 为：

- `真实 AI 使用经验 + 工作提效实录`

必须同时默认理解：

- 视频默认是：`真实经验证明壳 / 提效证据入口壳`
- `场景化专业输出工作包` 当前是：`可选沉淀单元 / 产品化承接单元`
- 不是每条视频默认都必须生成完整工作包
- 只有出现明确可复用流程、强结果差、用户需求信号或稳定产品化承接空间时，才继续沉淀工作包

## 5. 当前主读取分支

当前仓库默认主读取分支固定为：

- `main`

只有同步回这个分支，才算：

- 新聊天默认正式已知
- 仓库正式状态已更新
- 历史文件里若仍出现 `codex/user-readable-map`，只能按 `historical_branch_reference（历史分支引用）` 理解，不得再当成当前主线

## 5A. 执行层默认同步补丁

当前执行层必须默认理解：

只要本轮结果改变了下个聊天框默认应该知道的当前状态，无论本轮是成功、失败、半成功还是 blocked，都必须：
1. 更新 `codex_log/latest.md`
2. 若有真实执行结果，补 `codex_log/YYYYMMDD_任务名.md`
3. commit
4. push
5. 同步回 `main`

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
- 只要改动会影响新会话默认接手判断，就必须同步到 `main`

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

1. 用户最新执行单中明确写入并已同步到 `main` 的口径。
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
- 只有写进仓库文件，并同步到 `main`，才算新聊天默认正式已知

执行层里对“什么算已知”的正式分层，统一看：

- `codex_source/12_codex_known_state_three_layer_rules.md`

## 7. v3.1 视觉路由入口补丁

以后凡任务命中“骚萌卡 / 信息卡 / 段落提示卡 / v3.1 / visual_route_map”，必须先读取：

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`

并在后续任何基于 v3.1 的生成 / 修改 / 技术升级前先读取并验证：

- `visual_route_map.json（视觉路由表）`

读不到 PR #7 B 或 route map 未通过时，必须 `blocked`，不得回退 PR #7 A，不得生成或修改全片。

## 8. 入口一句话

命中《视频工厂》后，新会话默认先读 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_log/latest.md`，再按 `10 份基础执行包 + OPC 总纲 + 状态动作总控器` 最小顺序补读 `GPT数据源/00`、`GPT数据源/10_OPC`、`GPT数据源/11_项目状态动作总控器`、`codex_source/19_project_state_action_router.md`、`GPT数据源/01`、`GPT数据源/03`、`GPT数据源/08`、`GPT数据源/06`；每轮先输出 `state_action_router（项目状态动作总控器）` 判断当前状态、事实源裁决、触发机制和下一动作。当前阶段为 `formal_operation_active`，运营数据任务必须读取 `codex_log/current_operation_target.md`、`review_loop/operation_records_index.md` 与 `codex_log/current_data_goal_anchor.md`；旧 `current_gray_test_target.md` 只作 legacy pointer。命中目标 / 数据 / 文案修改 / 下一条视频 / 视频执行 / 剪辑 / 编排 / DeepSeek 供料 / GPT Project 静态包同步时，必须补读 `GPT数据源/13`、`GPT数据源/14` 与 `codex_log/current_data_goal_anchor.md`；缺 `current_data_goal_anchor` 或 `data_goal_anchor` 不得进入视频执行，缺 `data_goal_alignment_check` 不得写执行完成。正式运营不等于内容通过、商业验证成立、数据飞轮跑通或 runtime 稳定；若任务命中完整成片 / 成品候选片 / 技术预览升级 / 样片回炉 / 字幕 / TTS / 卡片 / 放大 / 剪辑 / 视觉母版修正，仍必须先读 locked reference 与 visual route 规则。当前正式默认主线按“API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑”理解，结构跟着文案走，`云端剪辑 / cloud-only` 只能写成正式方向，不能写成 runtime 已稳定跑通。

正式运营视频交付任务必须额外通过 `delivery_baseline_gate（交付基线闸门）`：能做到就交 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）`，做不到就交 `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`。`technical_preview / preflight package / silent preview / 无音轨视频 / 横屏技术包 / JSON 或 Markdown route card` 只能作为内部诊断或历史证据，不得冒充用户交付。
