# OPC 一人公司闭环与多 AI 协作机制

## 0A. 正式运营数据回流阶段

`已确认` OPC 闭环已进入真实运营数据回流阶段：每条已发布内容都作为 `operation_record（运营样本）` 被记录、观察和复盘。

后续不再把当前项目称为“灰度测试项目”；旧 `gray_test` 仅作为历史路径 / legacy alias。当前默认链路是：

`formal_operation_active -> operation_data_intake -> operation_review -> operation_next_variable_decision`

DeepSeek 仍只读供料，Codex 仍是唯一写入执行层；正式运营不代表内容、商业、数据飞轮或 multi-agent runtime 已验证成功。

## 1. 文件定位

本文件是《视频工厂》的上位机制文件。

它负责把项目从单一“视频生产流程项目”升级为：

`OPC 一人公司 AI 闭环验证系统`

它不负责：
- 当前视频发布状态推进
- `content_validation（内容验证）` 通过判断
- `send_ready（可发送状态）` 修改
- DeepSeek API 接入证明
- 多 agent runtime 跑通证明
- 任一条视频的最终内容复审

## 2. OPC 一人公司 AI 闭环定义

`OPC 一人公司 AI 闭环验证系统` 指的是：用一个人主导、多 AI 分工协作、真实业务问题驱动、内容发布反馈验证、再沉淀产品 / 服务 / 工作包的循环系统。

一句话：

**《视频工厂》不是只为了做视频，而是用视频作为内容化出口和反馈入口，验证一人公司如何借助 AI 完成“问题 -> 表达 -> 发布 -> 复盘 -> 产品化沉淀”的闭环。**

## 3. 当前闭环结构

当前闭环默认按 7 层理解：

1. `真实问题输入`
   - 来自用户真实工作、创业、内容生产、工具使用、AI 提效或平台反馈中的具体问题。
2. `AI 协作处理`
   - 多 AI 按角色分工，完成判断、研究、读取、执行、验证、复盘。
3. `内容化表达`
   - 把真实问题和 AI 处理结果转成视频、文案、提示词、工作包或展示层。
4. `平台发布验证`
   - 把内容放进真实平台环境，观察小样本流量、互动、留存、评论、私信和咨询信号。
5. `发布后复盘`
   - 通过 `review_loop/（复盘闭环）` 记录数据、判断短板、只选一个下一轮变量。
6. `产品 / 服务 / 工作包沉淀`
   - 只有当真实需求、可复用流程、强结果差或咨询线索出现时，才沉淀为产品化单元。
7. `下一轮内容与产品验证`
   - 基于复盘继续选题、表达、发布或产品化试验。

## 3A. 最高机制层：Project State Action Router

OPC 闭环不再只是 7 层描述，必须由 `Project State Action Router（项目状态动作总控器）` 驱动。

每轮先读取：

- `GPT数据源/11_项目状态动作总控器_机制推理层.md`

状态动作总控器负责先判断：

1. `current_project_state（当前项目状态）`
2. `fact_source_arbitration（事实源裁决）`
3. `trigger_routing_table（触发路由表）`
4. `Mechanism Inference Layer（机制推理层）`
5. `completion_state_inference（完成状态判断）`
6. `feedback_update_rule（反馈更新机制）`

它的职责是把 OPC 闭环从“问题 -> 表达 -> 发布 -> 复盘 -> 产品化沉淀”的抽象链条，转换成每轮可执行判断：

`input_signal -> inferred_state -> selected_action -> validation_rule -> feedback_update`

边界：

- 它不替代当前正式事实。
- 它不替代 Codex 执行规则。
- 它不替代发布后复盘数据。
- 它不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。
- 它只决定当前应触发哪条机制路，以及执行结果如何回写下一轮默认判断。

## 4. 视频在闭环中的位置

视频在新口径下是：
- `内容化出口`
- `真实经验展示载体`
- `提效证据入口`
- `分发验证样本`
- `发布后复盘对象`
- `产品化线索观察入口`

视频不是：
- 项目的全部目标
- 每轮闭环的唯一产物
- 当前商业模式已经成立的证明
- `content_validation（内容验证）` 已通过的自动证据

## 4A. 目标驱动数据飞轮

OPC 闭环必须由目标和数据驱动，不得停留在“写了一套项目规则”。

本项目当前新增目标飞轮入口：

- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
- `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`

目标链路：

```text
目标
-> 单条视频实验
-> 发布数据
-> 复盘诊断
-> 下一条内容结构计划
-> Codex 动态执行 prompt
-> 发布验证
-> 需求 / 客资 / 产品化沉淀
-> 目标更新
```

执行边界：

- ChatGPT 每次正式改文案前，必须先读取目标、阶段目标、阈值、上一条 / 同类视频数据、复盘结论和主短板。
- 内容结构调整必须根据数据反推下一条视频每一段放什么内容，不得只写“优化一下”。
- Codex 执行前必须读取 `next_video_execution_prompt（下一条视频执行 prompt）`，并按目标、数据短板、主变量、协同变量、内容结构计划和执行约束落地。
- 视频执行前必须先读取 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`；缺当前实例锚点时不得进入正式视频执行，状态为 `draft / waiting_data` 时只能做假设版或 blocked。
- 缺 `threshold_config_v1（阈值配置 V1）`、`video_goal_card（视频目标卡）`、`post_publish_review_card（发布后复盘卡）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）` 或 `next_video_execution_prompt（下一条视频执行 prompt）` 时，必须 blocked。
- 本机制写入不代表目标飞轮已经真实跑通，不代表阈值已经被真实样本验证，不推进任何发布状态。

## 4B. Data Goal Anchored Execution System（数据目标锚定执行系统）

OPC 闭环主轴补强为：

```text
目标 -> 数据 -> 执行 -> 发布 -> 复盘 -> 目标更新
```

最终架构：

```text
数据目标定方向
素材证据定能做什么
人感质量定能不能发
Codex 负责编排和执行
DeepSeek 负责供料和风险提醒
ChatGPT / 用户负责最终判断
```

硬规则：

- 视频、DeepSeek、Codex、Perplexity 都围绕 `data_goal_anchor（数据目标锚点）` 工作。
- 当前实例锚点优先看 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`，它只存当前这一条 / 下一条视频的实际锚点卡。
- DeepSeek 供料必须输出和数据目标相关的文件地图、风险、缺口和执行建议。
- Codex 是执行结构调度者，但不是目标改写者。
- Codex 可变的是执行结构，不可变的是 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）` 和验证指标。
- 数据目标是最高决策锚点，不是唯一判断来源；素材证据和人感质量仍必须单独验收。
- 本总线写入只代表机制补全，不代表数据目标闭环已经真实跑通。

## 5. 多 AI 协作默认架构

当前多 AI 协作默认架构：

| 角色 | 默认定位 | 权限边界 |
| --- | --- | --- |
| `ChatGPT` | 总控脑 / 判断层 | 负责方向判断、内容复审、下一轮唯一变量拍板 |
| `Codex` | 唯一写入执行层 / `Integrator` | 负责读仓库、整合 DeepSeek 供料、改文件、补齐字段 / 脚本 / schema / fixture / 日志 / 上传包、验证、Git 收尾 |
| `DeepSeek` | 每轮默认只读供料层 / `Explorer` | 默认通过 `DeepSeek runtime provider（DeepSeek 运行时供应商）` 加载；负责每轮执行前供料、压缩上下文、输出文件地图和风险冲突报告，并在执行后做风险复核；不写文件 |
| `Perplexity` | 外部研究层 | 负责外部资料检索、事实线索、竞品 / 技术参考，不直接写成项目事实 |
| 其他 AI / 工具 | 按任务补位 | 只在明确任务、权限和验证边界后接入 |

## 5A. GPT -> Codex 补全接力机制

`ChatGPT` 的职责不是只写 prompt，而是把用户需求横向补全成可执行任务地图，至少包含目标、边界、范围、产物、风险、验收、失败判定、必须读取、禁止修改和同步要求。

`Codex` 的职责不是只按第一眼任务改文件，而是把任务地图纵向拆成 `child_task_graph（子任务树）`，建立 `required_output_inventory（必须交付清单）`，逐项执行到底，并在结束前完成 `remaining_work_check（剩余工作检查）` 与 `sync_back_check（同步回写检查）`。

`DeepSeek` 每轮默认只读供料，不替代 Codex 的原文件复核和执行后反查。`Perplexity` 只做外部研究线索，不直接成为项目正式事实。

### 5A-1. DeepSeek runtime provider（DeepSeek 运行时供应商）

`DeepSeek runtime provider（DeepSeek 运行时供应商）` 是 DeepSeek 只读供料层的项目级运行时入口。

默认规则：

1. Codex 每轮需要 DeepSeek 供料时，默认先调用 `scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py`。
2. provider 的授权加载顺序为：`process_env -> .env.local -> .env -> 本地运行配置_local_runtime/deepseek_runtime_authorization.local.json`。
3. provider 只允许读取 `DEEPSEEK_API_KEY`，且只把 key 注入 DeepSeek 子进程 env；不得把 key 放进 prompt、stdout、stderr、supply pack、manifest、日志或 Git。
4. controller / explorer 不直接读取 `.env` 或本地授权文件；它们只接收 provider 注入后的子进程 env。
5. 用户明确要求 DeepSeek 必须真实参与时，`fallback_local_only（本地兜底）` 不得视为完成。
6. provider not ready 时，任务进入 `runtime_setup_required（需要运行时安装）` 或 blocked；不得每轮重复报同一个 process env 缺 key 错。
7. DeepSeek 仍只供料和提醒风险，不写文件、不 commit、不 push、不拍板项目事实。

Codex 二次补全责任：

1. 必须把 DeepSeek 供料转成可执行改动，不得只复制摘要。
2. 必须扫描受影响文件，区分 `must_update / should_update / must_not_update`。
3. 必须补齐字段、函数、schema、fixture、脚本输出、日志、路径索引和 GPT Project 上传包。
4. 必须在最终回报写 `deepseek_participation_report（DeepSeek 参与报告）` 与 `token_usage_expectation_check（token 使用预期检查）`。
5. 只写协议文件、未接入脚本 / schema / fixture / 验收链，不得写完成。

Codex 不得把“写入某个机制文件”当成“多 AI 协作机制已经长期稳定”。接力完成必须同时满足：

1. 任务树已拆。
2. 必改文件已改。
3. 禁止状态未偷换。
4. 验证已做。
5. 日志已回流。
6. 新聊天能按新事实接手。

## 5B. Reference-to-Execution Contract 参考到执行落地契约

当用户给 reference、样片、原感稿、目标效果、外部资料、参考图、参考视频或参考声音时，多 AI 分工必须先进入 `Reference-to-Execution Contract（参考到执行落地契约）`。

分工如下：

| 角色 | reference contract 职责 | 不得做 |
| --- | --- | --- |
| `ChatGPT` | 负责 reference 保真提取与契约化，把用户目标拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when` | 不得只把 reference 原样平移给 Codex，不得只写“风格类似” |
| `Codex` | 负责按契约执行、验证、偏离检查、日志和 Git 收尾 | 不得在没有契约时直接执行带 reference 的任务，不得把偏离结果写成 completed |
| `DeepSeek` | 只读辅助供料，可整理文字化 reference 样料、文件地图、风险冲突和候选字段 | 不得替代 reference contract，不得写文件，不得拍板项目事实 |
| `Perplexity` | 形成外部 reference pack / raw feeling draft，供 ChatGPT 契约化 | 不得直接升级成仓库已确认事实，不得绕过 ChatGPT / Codex 验证 |

契约最小链路：

```text
user goal / reference / sample / raw feeling / external pack
-> Reference-to-Execution Contract
-> Codex executable function fields
-> Deviation Check
-> completion_state_inference
```

硬规则：

- reference 锁的是质量效果、执行边界和偏离检查，不是把旧流程机械复制到每条内容。
- 只有 reference 可用、效果目标已填、执行函数字段已填、偏离检查已做，才允许写完成。
- reference 与当前项目状态冲突时，以 `Project State Action Router（项目状态动作总控器）` 和当前仓库正式事实裁决。
- 本机制不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`voice_validation（声音验证）` 或 `visual_master_locked（视觉母版锁定）`。

## 6. DeepSeek 每轮默认只读供料层规则

`DeepSeek` 在本项目中的默认身份是：

`mandatory readonly explorer（每轮默认只读探索器）`

标准链路：

```text
route_decision
-> deepseek_supply_gate
-> create_supply_request
-> run_deepseek_pre_supply
-> Codex execute
-> Codex vertical_completion
-> run_deepseek_post_risk_review
-> Codex validation / sync
```

允许输出：
- `prefetch_context_pack（预读取上下文包）`
- `must_read_file_map（必读文件地图）`
- `risk_and_conflict_report（风险与冲突报告）`
- `candidate_summary（候选摘要）`
- `file_map（文件地图）`
- `risk_report（风险报告）`
- `context_summary（上下文摘要）`
- `missing_files（缺失文件）`
- `visual_asset_requirement_pack（视觉素材需求包）`
- `api_asset_generation_pack（API 素材生成包）`
- `image_prompt_pack（图片 prompt 包）`
- `asset_validation_pack（素材验收包）`
- `assembly_decision_pack（装配决策包）`
- `editing_decision_pack（剪辑决策包）`

DeepSeek 供料范围从“文件地图 / 风险冲突”扩展为每轮默认供料：

1. 执行前文件地图。
2. 执行中缺口补读。
3. 执行后风险复核。
4. 视频执行现场的 `editing_decision_pack（剪辑决策包）`。
5. 文案进入执行后的完整 `execution_supply_pack family（执行供料包族）`，包括视觉素材需求、API 素材生成计划、图片 prompt、素材验收和装配决策。

`editing_decision_pack（剪辑决策包）` 只能基于 Codex 提供的文字化素材样料工作，例如 `source_segments（素材片段）`、`narration_lines（口播句子）`、`frame_descriptions（抽帧描述）`、`ocr_text（OCR 文字）` 和 `editing_question（剪辑问题）`。它不直接读取视频、音频、图片或媒体文件。

`execution_supply_pack family（执行供料包族）` 也只能基于 Codex 提供的文字化任务样料工作，例如 `script_blocks（脚本块）`、`segments（段落）`、`content_route_card（内容路由卡）`、`visual_asset_requirements（视觉素材需求）`、`api_generation_targets（API 生成目标）`、`image_prompt_specs（图片 prompt 规格）`、`asset_validation_criteria（素材验收标准）` 和 `assembly_slots（装配槽位）`。

API 调用不由 DeepSeek 决定。真实 API 调用必须由用户明确授权；DeepSeek 不读取 `.env`、API key、token 或密钥文件，不调用阿里 API，不生成真实图片。DeepSeek 可以帮助 Codex 判断“需不需要图、图怎么生成、素材怎么验收、怎么装配”，但最终执行判断在 Codex，内容质量判断在 ChatGPT / 用户。

DeepSeek 安全真实参与的唯一允许方式是：Codex / controller 不读取 `.env` 文件，只在用户或运行环境已把 `DEEPSEEK_API_KEY` 注入为 process environment（进程环境变量）时，用它做 HTTP Authorization。该 key 不得打印、不得写入日志、不得进入 prompt、不得传给 DeepSeek 上下文。如果 process environment 中没有 key，只能记录 `deepseek_actual_participation = blocked_missing_process_env_api_key`，不得读取 `.env` 补救，也不得写成 DeepSeek passed。

每轮默认安全入口是 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py（DeepSeek 安全供料运行器）`：只设置 `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1` 与 `DEEPSEEK_DISABLE_ENV_FILE=1`，只使用当前 process environment，不读取 `.env`。历史 live smoke runner 可以在用户本轮明确授权后用于安全子进程注入验证，但不得被 ChatGPT / Codex 默认当成每轮可自动读取 `.env` 的通道。

后续任何任务必须先做 `deepseek_readiness_check（DeepSeek 就绪检查）`、`deepseek_participation_report（DeepSeek 参与报告）` 和 `token_usage_expectation_check（token 使用预期检查）`：区分 `deepseek_passed（真实供料通过）`、`fallback_local_only（本地兜底）` 和 blocked 状态。其中 `fallback_local_only` 必须写 `not_deepseek_conclusion = true`；blocked 必须写缺 key、无权限、网络 / timeout、禁止路径或输出不合格等具体原因。token 未观察到减少时，不得写 DeepSeek 已深度参与。

最终执行判断仍在 Codex。方向、内容、人感、下一轮变量仍由 ChatGPT / 用户拍板。该机制不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，也不代表 DeepSeek 已稳定真实供料。

禁止：
- 修改仓库文件
- 生成最终事实判断
- 替 ChatGPT / 用户拍板项目方向
- 替 Codex 做 Git 收尾
- 把外部资料直接升级成 `已确认`
- 把只读摘要当作仓库原文件证据

若 DeepSeek 输出与仓库原文件冲突，默认以仓库原文件为准，并由 Codex 标记冲突。

## 7. Codex 唯一写入 Integrator 规则

`Codex` 在本项目中的默认身份是：

`Integrator（统一执行者 / 唯一写入层）`

Codex 负责：
- 复核关键原文件
- 读取 DeepSeek 供料包并复核原文件
- 执行 `codex_vertical_completion（Codex 二次补全）`
- 补齐受影响字段、函数、schema、fixture、脚本、日志、路径索引和 GPT Project 上传包
- 修改允许范围内的仓库文件
- 更新 `codex_log/latest.md（最新日志）`
- 命中条件时新增 dated log
- 做 diff / 状态字段 / 禁止项检查
- commit / push / PR 收尾

Codex 不得：
- 把 DeepSeek、Perplexity 或任何 explorer 的摘要直接当成当前正式事实
- 未复核原文件就写入状态推进
- 多写手并发修改核心入口文件
- 把技术跑通写成内容通过

## 8. Perplexity 外部研究层规则

`Perplexity` 在本项目中的默认身份是：

`external research layer（外部研究层）`

允许：
- 做外部事实检索
- 整理技术方案、平台规则、竞品信息、工具能力
- 形成 `reference pack（参考包）`
- 形成 `raw feeling draft（原感初稿）`

禁止：
- 直接成为项目正式事实源
- 替代仓库正式状态
- 替代用户 / ChatGPT 的内容判断
- 把外部建议写成已验证项目能力

## 9. reference / 样片质量从流程锁升级为机制锁

当前新口径：

`reference（参考）`、`reference_quality_sample（参考质量样片）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 的核心价值是：

**锁定质量判断机制，不锁死每条内容的固定流程。**

具体含义：
- `reference_quality_sample（参考质量样片）` 仍然要求达到可作为后续参考的质量，不允许降级成 flow proof。
- `locked reference（锁定参考）` 仍然用于防止质量漂移、风格漂移、状态误写。
- `visual route（视觉路由）` 仍然用于拆清不同展示结构，避免提示卡、信息卡、反应卡混用外壳。
- 但它们不等于每条内容都必须机械套同一条镜头流程、同一张卡片结构、同一次数的 `API 生成真人`。
- 如果仓库其他文件仍出现 `fixed_material_anchor（固定素材锚点）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 的强约束写法，默认先按本节解释：它们锁的是质量、风格、展示边界，不直接锁定镜头流程。
- `Codex（唯一写入执行层 / Integrator）` 在后续修正规则时，若发现旧口径和本节冲突，必须优先保留“质量机制锁”解释，不得把历史强约束直接升级成新的固定 SOP。

当文案目标、素材证据、平台风险或结果差结构改变时，应先做机制判断：
- 当前目标需要什么展示结构？
- 哪些 reference 仍适用？
- 哪些 locked reference 只约束质量，不约束流程？
- 原 `visual route` 是否需要新路由或局部变体？
- 是否存在强套旧流程导致内容表达变差的风险？

## 9A. 质量与反馈总控机制

本机制 V1 的作用是把《视频工厂》后续视频 / 文案 / 复盘任务，统一接入“先判断目标，再选择承载，再用反馈反推变量”的项目机制。

每条视频允许随文案、素材、平台风险和结果差变化结构，但质量底线不能变化。后续任务开始前，默认先回答：

1. `validation_goal（本轮验证目标）`
   - 这条内容到底在验证选题、开头、文案结构、中段证据、声音、卡片、发布包装，还是产品化信号。
2. `content_route_card（内容路由卡）`
   - 解释这条内容为什么这样承载，为什么不直接沿用旧镜头流程。
3. `quality_lock_card（质量锁卡）`
   - 锁住用户能拿走什么、用什么证据证明、哪些质量点一票否决。
4. `review_variable_card（复盘变量卡）`
   - 发布前和复盘前都要锁定本轮主变量，避免下一轮同时改太多导致无法解释结果。

质量不靠固定模板保证，而靠质量底线和状态边界保证：

- `reference（参考）` 锁质量点、风格边界、证明强度和防漂移要求，不锁镜头流程。
- `locked reference（锁定参考）` 锁继承条件和不可降级项，不锁每条内容的 API 人物段次数、PPT 数量或尾卡出现方式。
- `visual route（视觉路由）` 锁展示类型和外壳职责，不锁每条内容的固定结构。
- `Reference-to-Execution Contract（参考到执行落地契约）` 把 reference 拆成 `reference_anchor / effect_targets / function_fields / deviation_check / done_when`，用于防止只学表层风格而丢掉关键效果。
- `content_route_card（内容路由卡）` 用来说明流程为什么可变，不是新的固定模板。
- `quality_lock_card（质量锁卡）` 用来约束执行前质量，不证明内容已经通过。
- `review_variable_card（复盘变量卡）` 用来把数据反馈收束到下一轮唯一主变量，不是运营大表。

发布后复盘必须反推下一轮唯一优先变量。若多个变量同时改变，只能记录观察，不得过度解释结果，也不得把异常样本当作正常规律沉淀。

DeepSeek 供料只提供资料压缩和风险提醒。Codex 必须读取供料包并复核原文件；若 `supply_source = fallback_local_only（本地兜底）`，只能写 `not_deepseek_conclusion = true`，不得写成 DeepSeek 真实结论、稳定供料或完整 `multi-agent runtime（多 agent 运行时）` 已跑通。

## 9B. 三大机制推理函数在 OPC 闭环中的位置

OPC 闭环不是固定视频 SOP，必须用三大机制推理函数把“问题 -> 表达 -> 发布 -> 复盘 -> 产品化沉淀”落成可判断链路。

| 函数 | 所在环节 | 输出 | 禁止误写 |
| --- | --- | --- | --- |
| `content_route_inference_function（内容路由推理函数）` | 内容化表达前 | `content_route_card（内容路由卡）`、承载结构、API 人物次数、PPT / Prompt 尾卡是否使用、是否沉淀工作包 | 不得先定固定流程，不得把 reference 流程照搬成每条内容 SOP |
| `editing_inference_function（剪辑推理函数）` | 云端剪辑 / 装配前 | `editing_decision_pack（剪辑决策包）`、证据窗口、放大 / 保留 / 插卡 / 定格 / 左右对比决策 | 不得用卡片或装饰抢走真实录屏证据，不得素材不清还继续剪 |
| `quality_issue_classifier（质量短板分类器）` | 发布前 / 发布后 / 用户复审 | 唯一最高优先级短板、下一轮只改一个变量、blocked / human_review_required | 不得把技术通过写成内容通过，不得同时改多个核心变量后再解释结果 |

统一结构：

```text
input_signal（输入信号）
-> observed_evidence（现场证据）
-> state_inference（状态判断）
-> action_policy（动作策略）
-> validation_rule（验证规则）
-> blocked_if（阻断条件）
-> feedback_update（反馈回写）
```

边界：

- 三个函数只让机制可执行、可验证、可阻断、可回写。
- 三个函数不代表机制长期稳定验证通过；仍需后续真实视频 / 文案 / 复盘任务继续验证。
- 三个函数不推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。

## 10. 与原视频四件套主线的关系

原视频四件套继续保留：

`API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`

但在 OPC 口径下，它的位置降级为：

`内容化输出的默认执行载体`

它不是：
- 项目总目标
- 每条内容不可变死流程
- 商业闭环已经成立的证明
- 当前云端剪辑稳定跑通的证明

`API 生成真人` 次数、卡片类型、信息密度、`visual route（视觉路由）` 和结尾承接方式，应由文案机制、素材证据、平台风险、结果差结构和发布后复盘共同决定。
- 上述决定默认逐条内容实时判断，不接受“因为已有 reference / locked reference / visual route，所以人物段次数、卡片数量、尾卡结构必须照搬”的写法。

## 11. 禁止误写

本轮及后续默认禁止把以下内容写成事实：

- DeepSeek API 已接入
- 多 agent runtime 已跑通
- 当前视频内容已通过
- 当前声音已验证通过
- 云端剪辑已稳定跑通
- V002b 已成为最终稿
- 当前项目商业模式已验证成立
- `send_ready（可发送状态） = true`
- `reference（参考）` 等于固定流程不可改
- `locked reference（锁定参考）` 等于每条内容必须用同一套卡片流程
- DeepSeek / Perplexity 摘要可以替代 `Reference-to-Execution Contract（参考到执行落地契约）`
- 只写“风格类似”就等于已按 reference 执行

## 12. 一句话规则

**《视频工厂》当前上位身份是 `OPC 一人公司 AI 闭环验证系统`：ChatGPT 做总控判断与 reference 契约化，Codex 做唯一写入整合、二次补全和偏离检查，DeepSeek 做每轮默认只读供料与执行后风险复核，Perplexity 做外部研究；视频是内容化与反馈出口，reference 必须先变成可执行契约，锁质量机制，不锁死每条内容的固定流程。**
