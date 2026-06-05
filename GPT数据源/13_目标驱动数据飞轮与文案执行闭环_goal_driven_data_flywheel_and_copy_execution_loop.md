# 目标驱动数据飞轮与文案执行闭环

## 0A. 正式运营数据飞轮口径

当前数据飞轮运行在 `formal_operation_active（正式运营中）` 阶段。

发布数据不再作为“灰度测试项目”数据理解，而作为 `operation_records（运营记录）` 和 `operation_review（运营复盘）` 的输入。`data_goal_anchor（数据目标锚点）` 继续服务正式运营变量判断，但当前实例仍为 `partial_data_recorded`，不到 7d、需求侧字段和人审前不得写 `ready`。

`已确认` 运营判断层必须由 `operation_decision_system（运营决策系统）` 输出报告后才算进入。当前可运行入口为 `scripts/运营决策系统_operation_decision_system.py`；系统输出统一写入 `review_loop/decision_engine/latest_operation_decision_report.json`、`review_loop/decision_engine/latest_operation_decision_report.md` 和 `review_loop/decision_engine/final_user_operation_result.md`。

硬规则：

- 只有机制文字、复盘卡或人工聊天判断，不等于数据飞轮进入运营判断层。
- 缺 `operation_decision_system` 最终报告时，不得生成正式下一条视频执行 prompt。
- 系统判断 `blocked_for_formal_next_episode_execution` 时，只允许低置信度准备，不允许进入正式视频执行。
- `operation_decision_system` 落地只代表决策系统可运行，不代表内容成功、方向成立、商业验证成立或数据飞轮真实跑通。

## 0A-0. operation_learning_ledger gate（运营学习台账闸门）

数据飞轮不能只输出运营报告。

每次复盘必须写入：

- `review_loop/learning_ledger/operation_learning_memory.md`
- `review_loop/learning_ledger/next_episode_bet_card.md`
- `review_loop/learning_ledger/current_copy_revision_handoff.md`

否则数据没有进入文案层，不算闭环完成。

ChatGPT 在下一次选题和文案判断中必须承担建设性判断责任：

- 必须给出下一期创作下注。
- 必须写清押什么、不押什么、为什么、验证什么。
- 必须说明继承上一期什么有效信号、修复上一期什么失败信号。
- 不得只输出泛泛建议或纯数据解释。

Codex 的责任不是定稿下一期文案，而是把复盘结果写成文案层可读取的交接物。缺 `next_episode_bet_card` 或 `current_copy_revision_handoff` 时，不得写复盘闭环完成。

## 0A-1. copy_iteration_decision gate（文案迭代决策闸门）

数据反馈到文案之前，必须先输出 `copy_iteration_decision（文案迭代决策）`，不能只靠 ChatGPT / Codex 临场判断“改开头还是改方向”。

当前可运行入口：

- `scripts/文案迭代决策系统_copy_iteration_decision_system.py`
- `review_loop/copy_iteration/latest_copy_iteration_report.json`
- `review_loop/copy_iteration/latest_copy_iteration_report.md`
- `review_loop/copy_iteration/V003/V003_copy_iteration_decision.json`
- `review_loop/copy_iteration/V003/V003_next_copy_revision_brief.md`

硬规则：

- 每期、每版文案必须进入 `copy_registry.json`，并绑定发布数据窗口、运营记录和运营决策报告。
- `raw_copy（原始文案）` 必须保真；疑似错字只进入 `suspected_typos（疑似错字）`，不得覆盖原文。
- `copy_iteration_decision` 必须判断问题层级：`opening_packaging / bridge_3_8s / middle_structure / evidence_expression / tone_and_language / topic_angle / target_audience`。
- V003 当前仍是 `partial_data_recorded / post_72h_pre_7d_snapshot`，只能输出 `low_confidence_prepare_allowed = true`，不得输出正式文案 ready。
- 当前默认问题层级为 `opening_packaging`，辅助关注 `bridge_3_8s`；不得直接判 `topic_angle` 失败或 `target_audience` 错误。
- ChatGPT 后续改稿前必须读取 `V003_next_copy_revision_brief.md`；Codex 不负责最终定稿。

## 0B. 正式运营交付停止线

目标驱动文案、`next_video_execution_prompt（下一条视频执行 prompt）`、`content_structure_feedback_card（内容结构反馈卡）` 和执行前补全包，只能作为进入视频执行的前置条件。它们不能替代正式运营视频交付。

当下一条视频进入 Codex 执行链时，交付结果必须是 `publish_candidate_ready_for_human_review（可发布候选片，待人工复审）` 或 `blocked_publish_candidate_unavailable（可发布候选片不可交付阻断）`。如果只能输出技术预览、无声预览、横屏技术包、JSON / Markdown route card 或 preflight package，必须 blocked，不得写数据飞轮内容推进。

当前正式运营默认出片比例为 `horizontal_16_9（横屏 16:9）`、默认分辨率为 `1920x1080`。旧 `vertical_9_16（竖屏 9:16）` 只保留为历史样片、历史提示卡或用户另行指定竖屏策略时的特殊口径；不得把旧竖屏默认带入屏幕录制、文档、表格和指标分层类内容。

## 0C. 数据目标不得通过降级产物完成

数据目标执行不能通过降级产物完成。如果当前变量要求发布候选片，实际产物必须满足正式运营 `publish_candidate（可发布候选片）` 基线；缺声音、字幕、横屏 16:9 / 1920x1080、文案画面逐句对应、关键素材证据、时间线、TTS、卡片或导出验证时，必须 `blocked`。

`content_route_card（内容路由卡）`、`next_video_execution_prompt（下一条视频执行 prompt）`、`script_to_timeline_map（文案到时间线映射表）`、`editing_decision_pack（剪辑决策包）`、`assembly_decision_pack（装配决策包）`、`data_goal_alignment_check（数据目标对齐检查）`、路由卡、时间线、决策包和对齐检查都只是中间层，不是完成结果。

降级方案只允许作为 `blocked` 后待用户授权的修复建议。Codex 可以提出 fallback，但不能用 fallback、技术预览、无声视频、比例错误视频、局部结果或只读报告完成数据目标。

## 0D. locked copy and visual alignment in data-goal execution

数据目标只能约束文案和执行方向，不能授权 Codex 改写已锁定文案。视频执行前必须有 `locked_copy_contract（锁定文案契约）`，包含 `locked_topic / locked_title / locked_final_script / locked_opening_line / allowed_copy_changes / forbidden_copy_changes / copy_change_request_required_if_needed`。

Codex 可以围绕数据目标调整素材映射、剪辑节奏、字幕分句、卡片位置、音轨和证据窗口，但不得为了服务数据目标擅自改标题、选题、核心判断、人味表达或视觉标题卡。若数据目标与文案可执行性冲突，必须输出 `copy_change_request（文案修改请求）` 或 blocked。

`script_to_timeline_map` 必须按 `line_level_script_visual_alignment_gate（逐句文案画面对齐闸门）` 输出；每个 `line_group` 都要绑定数据目标、口播、画面证据、字幕、卡片和禁用画面。导出前还必须完成 `subtitle_card_overlap_check（字幕卡片重叠检查）`，避免字幕 / 卡片遮挡证据。

用户明确说视频已经发了 / 已发布时，当前视频不再默认进入回炉，改走 `operation_data_intake / operation_review`；机制暴露问题时修机制和下一轮执行规则，不修已发布片。

## 1. goal_driven_data_flywheel_spec_v1（目标驱动数据飞轮规格 V1）

本文件解决的问题是：把《视频工厂》从“记录规则 / 做单条视频”推进到“目标 -> 数据 -> 文案修改 -> 内容结构反推 -> Codex 动态执行 -> 发布复盘 -> 下一轮更新”的可执行闭环。

硬边界：

- `已确认` 项目缺的不是单纯技术，也不是单条视频质量，而是目标驱动执行链。
- `已确认` 视频发布数据必须加速数据飞轮，不能只沉淀为描述性日志。
- `已确认` ChatGPT 不能凭感觉改文案；每次正式文案修改前必须读取目标、阶段目标、上一条 / 同类视频数据、复盘结论和主短板。
- `已确认` Codex 不能只把机制记录进仓库；Codex 执行视频前必须读取动态执行 prompt、目标、数据短板、主变量、协同变量、内容结构计划和执行约束。
- `待验证` 本机制已写入，不代表目标飞轮已经真实跑通，不代表阈值已被真实样本验证。

```yaml
goal_driven_data_flywheel_spec_v1:
  north_star_goal:
    value: "3-6 个月内，验证《视频工厂》能否通过真实 AI 使用内容，稳定产生高质量需求信号，并沉淀出可承接的服务 / 工作包 / 咨询方向。"
    status: "stage_hypothesis"
    note: "这是阶段工作假设，不是已验证事实。"

  project_goal:
    value: "用每条视频的数据反推下一条视频的选题、内容结构、执行方式和承接策略。"
    status: "stage_hypothesis"

  flywheel:
    - "目标"
    - "单条视频实验"
    - "发布数据"
    - "复盘诊断"
    - "下一条内容结构计划"
    - "Codex 动态执行 prompt"
    - "发布验证"
    - "需求 / 客资 / 产品化沉淀"
    - "目标更新"

  metric_layers:
    touch_layer:
      metrics:
        - play_count
        - recommendation_traffic
        - three_second_retention
        - five_second_retention
        - completion_rate
        - avg_watch_time
    recognition_layer:
      metrics:
        - like_count
        - save_count
        - share_count
        - follow_count
        - profile_visit
    interaction_layer:
      metrics:
        - comment_count
        - comment_quality
        - pain_restatement
        - detail_questions
    demand_layer:
      metrics:
        - dm_count
        - valid_dm_count
        - workflow_questions
        - clear_business_problem
    lead_layer:
      metrics:
        - lead_score
        - weak_leads
        - medium_leads
        - high_intent_leads
        - convertible_leads
    commercial_validation_layer:
      metrics:
        - paid_consulting
        - custom_video_need
        - ai_workflow_build_need
        - workpack_need
        - repeat_potential
```

解释边界：

- 播放是前置入口，不是最终目标。
- 点赞不是需求。
- 私信总数不是客资质量。
- 客资必须评分。
- 商业验证必须有重复需求或付费 / 强付费信号，不得凭感觉写成立。

## 1A. data_goal_execution_bus_handoff（数据目标执行总线交接）

本文件负责定义目标、阈值、数据诊断、文案修改闸门和 `next_video_execution_prompt（下一条视频执行 prompt）`。

`GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md（数据目标执行总线）` 负责把这些目标字段继续接到 DeepSeek 供料、Codex 剪辑 / 编排 / 装配、发布后复盘和执行完成验收。

`codex_log/current_data_goal_anchor.md（当前数据目标锚点）` 是当前这一条 / 下一条视频实际使用的实例锚点入口。它不替代本文件，也不替代 `14_数据目标执行总线`；它只负责承接当前任务的 `data_goal_anchor` 实例，供 ChatGPT、Codex、DeepSeek 和 GPT Project 读取。

硬规则：

- `next_video_execution_prompt（下一条视频执行 prompt）` 不只是给文案执行使用。
- 它也是 `content_route_card（内容路由卡）`、`script_to_timeline_map（文案到时间线映射表）`、`editing_decision_pack（剪辑决策包）`、`assembly_decision_pack（装配决策包）`、DeepSeek 供料和发布后复盘的统一锚点。
- 正式文案修改后，必须生成或更新 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`，再进入 Codex 执行。
  - 缺 `data_goal_anchor（数据目标锚点）` 时，不得进入 Codex 视频执行。
  - 缺 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）` 当前实例入口时，不得进入正式视频执行；如果状态为 `draft / waiting_data`，只能写假设版或 blocked。
  - 缺 `data_goal_alignment_check（数据目标对齐检查）` 时，不得写执行完成。
  - 缺 `delivery_baseline_gate（交付基线闸门）` 时，不得写正式运营视频交付完成。
  - `next_video_execution_prompt / content_route_card / script_to_timeline_map / tts_prosody_anchor_map / editing_decision_pack / assembly_decision_pack / data_goal_alignment_check` 只是执行前必备条件，不是用户最终视频交付物。
  - Codex 可以调整 segment 拆分、画面顺序、卡片位置、剪辑节奏、TTS 分句、装配顺序；降级方案只能作为 blocked 后待用户授权的修复建议，不能作为完成结果。
- Codex 不得调整 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）`、`success_metric（成功指标）`、`failure_metric（失败指标）`、`post_publish_validation_metric（发布后验证指标）`。

最小交接字段：

```yaml
data_goal_execution_bus_handoff:
  source_file: "13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md"
  bus_file: "14_数据目标执行总线_data_goal_execution_bus.md"
  required_before_codex_execution:
    - current_data_goal_anchor_path
    - current_data_goal_anchor_status
    - data_goal_anchor
    - next_video_execution_prompt
    - main_bottleneck
    - primary_variable
    - forbidden_variables
    - success_metric
    - failure_metric
    - post_publish_validation_metric
  required_before_completion:
    - data_goal_alignment_check
  status_boundary:
    confirmed: "目标驱动机制与执行总线已写入。"
    pending_validation: "真实任务中是否稳定先读取 current_data_goal_anchor，再把剪辑、编排、供料锚定到数据目标。"
```

字段模板：

```yaml
video_goal_card:
  video_id:
  topic:
  current_north_star_goal:
  current_stage_goal:
  target_user:
  experiment_type:
  primary_variable:
  supporting_variables:
  forbidden_variables:
  success_metric:
  failure_metric:
  expected_signal:
  status: "draft / ready / blocked"

post_publish_review_card:
  video_id:
  review_window:
    - 24h
    - 72h
    - 7d
    - 30d
  raw_metrics:
    play_count:
    three_second_retention:
    five_second_retention:
    completion_rate:
    avg_watch_time:
    save_rate:
    like_rate:
    effective_comments:
    valid_leads:
    high_quality_leads:
    convertible_leads:
  threshold_check:
  main_bottleneck:
  data_confidence:
  human_review_required:
```

## 2. threshold_config_v1（阈值配置 V1）

本节是阶段工作假设，用于帮助复盘裁决，不是行业定论，也不是内容验证已经通过。

```yaml
threshold_config_v1:
  status: "stage_hypothesis"
  note:
    - "所有数字都是当前阶段工作假设，不是行业定论。"
    - "如果没有历史数据，默认保守设定。"
    - "数字作用是帮助判断，不是自我绑架。"
    - "数据不足时不得强行判断方向成立或失败。"

  single_video_play_thresholds:
    fail:
      play_count: "< 1000"
      meaning: "触达不及格。优先检查选题、标题、开头、封面 / 首屏。"
      route_decision: "rework_or_retest"

    baseline_observe:
      play_count: "1000-3000"
      meaning: "基础观察区。不能下最终结论，只能结合留存、收藏、评论、私信看局部信号。"
      route_decision: "observe_more"

    positive_signal:
      play_count: "3000-8000"
      meaning: "有一定分发信号。可以结合收藏、评论、私信判断内容价值。"
      route_decision: "continue_or_rework"

    breakout_observe:
      play_count: "8000+"
      meaning: "小爆观察。重点判断是不是泛流量，不能只因播放高就放大。"
      route_decision: "diagnose_quality_before_scale"

  retention_thresholds:
    three_second_retention:
      weak: "明显低于账号同类内容基线，或出现首屏快速滑走"
      meaning: "开头 / 首屏 / 选题钩子可能不成立。"
      next_action: "优先改 opening_0_3s"

    five_second_retention:
      weak: "3 秒留存尚可但 5-10 秒明显下滑"
      meaning: "开头能拦住，但承接没有给继续看的理由。"
      next_action: "优先改 bridge_3_8s / problem_expand_8_15s"

    avg_watch_time:
      weak: "明显低于视频关键信息出现所需时长"
      meaning: "中段节奏、证据展示或结构承接可能有问题。"
      next_action: "优先改 evidence_middle / content_structure"

  value_signal_thresholds:
    save_rate:
      weak: "< 1%"
      observable: "1%-2%"
      strong: "> 2%"
      meaning:
        weak: "复用价值弱，内容可能爽但不能留下。"
        observable: "有初步可复用价值，继续观察同类题。"
        strong: "有方法 / 步骤 / 模板 / 结果差价值，值得重点复盘。"

    like_rate:
      weak: "< 2%"
      observable: "2%-5%"
      strong: "> 5%"
      meaning:
        weak: "观点或表达没有被认可。"
        observable: "有基本认同，但不代表需求成立。"
        strong: "观点认同强，但仍需结合收藏 / 评论 / 私信判断需求。"

    effective_comments:
      weak: "0-2 条"
      observable: "3-5 条"
      strong: "> 5 条"
      meaning:
        weak: "互动信号弱。"
        observable: "可以观察用户是否复述痛点。"
        strong: "可能出现真实共鸣或需求线索。"

  lead_signal_thresholds:
    valid_lead_definition:
      valid_lead: "lead_score >= 3"
      high_quality_lead: "lead_score >= 4"
      convertible_lead: "lead_score = 5"

    thirty_day_signal:
      fail: "< 3 个 3 分以上客资"
      baseline: "3-7 个 3 分以上客资"
      strong: ">= 8 个 3 分以上客资，且至少 2 个 4 分以上客资"
      excellent: "出现 1 个 5 分客资"

    meaning:
      fail: "需求信号不足，不要急着产品化。"
      baseline: "有需求苗头，继续发同类内容验证。"
      strong: "可以进入需求类型归纳。"
      excellent: "可以考虑轻咨询 / 工作包 / 服务雏形。"

  stage_thresholds:
    day_0_30:
      stage_goal: "验证哪类真实 AI 使用内容能让目标用户停下来，并产生内容价值信号。"
      main_metrics:
        - three_second_retention
        - five_second_retention
        - save_rate
        - effective_comments
        - lead_score_2_plus

      pass_line:
        - "7-10 条视频中，至少 2 条达到 baseline_observe 以上播放，并出现收藏 / 有效评论 / 复述痛点。"
        - "至少出现 1 条 save_rate > 1% 的视频。"
        - "至少出现 3 条有效评论，或出现 2 分以上需求信号。"

      excellent_line:
        - "至少 1 条视频达到 8000+ 播放，且不是纯泛流量。"
        - "至少 1 条视频 save_rate > 2%。"
        - "至少出现 1 个 3 分以上客资。"

      fail_line:
        - "连续 7 条视频播放 < 1000，且无收藏、无有效评论、无 2 分以上需求信号。"
        - "连续 7 条视频 3 秒 / 5 秒留存弱，说明选题或开头未成立。"

    day_31_90:
      stage_goal: "验证哪些内容能稳定产生 3 分以上客资和重复需求。"

      pass_line:
        - "每月 >= 8 个 3 分以上客资。"
        - "至少 2 个 4 分以上客资。"
        - "至少出现 1 类重复需求。"

      excellent_line:
        - "每月 >= 15 个 3 分以上客资。"
        - ">= 5 个 4 分以上客资。"
        - "出现 1 个 5 分客资。"

      fail_line:
        - "连续 30 天无 3 分以上客资。"
        - "私信多但 80% 以上为 0-1 分。"

    day_90_180:
      stage_goal: "验证能否沉淀成服务 / 工作包 / 咨询方向。"

      pass_line:
        - "至少形成 1 个可描述的服务 / 工作包方向。"
        - "出现真实付费或强付费意向。"

      excellent_line:
        - "形成 1-2 个可复用服务包。"
        - "同类咨询重复出现。"
        - "内容能稳定带来 4 分以上客资。"

      fail_line:
        - "有播放但无法沉淀需求。"
        - "有私信但无法转成服务。"
        - "需求长期分散，无法形成承接方向。"

  metric_decision_rules:
    - if: "play_count < 1000 and three_second_retention weak"
      diagnosis: "触达失败，优先判断选题 / 开头失败。"
      next_action: "改 opening_0_3s 或选题表达。"

    - if: "play_count 1000-3000 and save_rate > 2%"
      diagnosis: "小流量高价值，继续同方向测试。"
      next_action: "优化标题 / 开头，不急着换方向。"

    - if: "play_count >= 8000 and save_rate weak and comments weak and dm weak"
      diagnosis: "疑似泛流量，不得直接放大。"
      next_action: "提高目标用户门槛或需求场景。"

    - if: "save_rate < 1%"
      diagnosis: "可复用价值弱。"
      next_action: "补步骤、模板、判断表、结果差。"

    - if: "save_rate > 2%"
      diagnosis: "内容有沉淀价值。"
      next_action: "重点复盘该选题结构。"

    - if: "valid_leads = 0"
      diagnosis: "不得写需求成立。"
      next_action: "继续观察或改需求场景 / 承接。"

    - if: "high_quality_lead >= 1"
      diagnosis: "必须记录需求类型。"
      next_action: "进入需求信号复盘。"

    - if: "convertible_lead >= 1"
      diagnosis: "进入 offer_validation。"
      next_action: "考虑轻咨询 / 工作包 / 服务雏形。"

  threshold_status_boundary:
    - "所有数字都是当前阶段工作假设，不是行业定论。"
    - "数据不足时不得强行判断方向失败或成立。"
    - "只有 1-2 条样本时，只能写待验证。"
    - "多条同类样本重复出现后，才允许写部分成立。"
    - "不得把一次播放高写成方向成立。"
    - "不得把一次客资高写成商业模式成立。"
```

客资评分模型：

```yaml
lead_score_model:
  score_0:
    name: "无效私信"
    meaning: "要资源、要链接、泛泛问赚钱，不暴露具体问题。"
    action: "不进入私域，不计入有效客资。"

  score_1:
    name: "泛泛好奇"
    meaning: "问工具名、问怎么做，但没有具体场景。"
    action: "可作为 FAQ，不作为客资。"

  score_2:
    name: "弱需求"
    meaning: "表达想提效，但没有明确任务。"
    action: "可追问场景，暂不进入服务判断。"

  score_3:
    name: "明确问题"
    meaning: "说清楚自己卡在哪个任务。"
    action: "计入有效客资，可进入轻量私域。"

  score_4:
    name: "明确场景 + 明确结果诉求"
    meaning: "有业务场景和想要结果。"
    action: "高价值客资，可沉淀内容和工作包。"

  score_5:
    name: "明确场景 + 明确预算 / 时间 / 决策意愿"
    meaning: "有预算、时间要求或明确购买 / 咨询意向。"
    action: "可转化客资，可进入服务 / 咨询判断。"
```

## 3. data_goal_copy_revision_gate（数据目标驱动文案修改闸门）

正式文案修改必须先读取目标和数据，再决定怎么改。若缺数据，只能输出假设版文案，不能写成数据驱动正式改稿。

```yaml
data_goal_copy_revision_gate:
  purpose: "所有正式文案修改都必须先读取目标和数据，再决定怎么改。"

  required_before_copy_revision:
    - current_north_star_goal
    - current_stage_goal
    - threshold_config_v1
    - video_goal_card
    - post_publish_review_card
    - data_flywheel_memory
    - content_structure_feedback_card
    - main_bottleneck
    - primary_variable
    - supporting_variables
    - forbidden_variables
    - success_metric
    - failure_metric

  if_missing:
    rule: "只能输出假设版文案，不能写成数据驱动正式改稿。"

  copy_revision_output_must_include:
    - data_diagnosis
    - threshold_check
    - main_bottleneck
    - variable_plan
    - copy_revision_strategy
    - revised_script
    - next_video_execution_prompt
    - post_publish_validation_metric
```

硬规则：

```text
没有 threshold_config_v1，不得做数据驱动判断。
没有 video_goal_card，不得进入正式文案修改。
没有 post_publish_review_card，不得声称“根据数据修改文案”。
没有 main_bottleneck，不得重写正式文案。
没有 primary_variable，不得生成 Codex 执行 prompt。
数据不足时，只能输出假设版文案，并标注缺失数据。
```

输出字段模板：

```yaml
copy_revision_strategy:
  data_diagnosis:
  threshold_check:
  main_bottleneck:
  variable_plan:
    primary_variable:
    supporting_variables:
    forbidden_variables:
    total_change_variables:
    major_revision:
    attribution_boundary:
  revised_script:
  next_video_execution_prompt:
  post_publish_validation_metric:
```

## 4. content_structure_feedback_engine（内容结构反馈引擎）

本引擎不是泛泛优化，而是根据发布数据反推下一条视频每一段应该放什么内容，才能更可能留住目标用户并产生需求信号。

```yaml
content_structure_feedback_engine:
  purpose: "根据发布数据反推下一条视频每一段应该放什么内容。"

  segments:
    opening_0_3s:
      goal: "抓住注意力"
      metrics:
        - three_second_retention
        - first_screen_skip_signal
      if_bad:
        diagnosis:
          - topic_not_hooking
          - weak_visual_hook
          - first_sentence_too_plain
        next_structure_action:
          - use_strong_question
          - use_visual_impact
          - remove_background_explanation

    bridge_3_8s:
      goal: "给用户继续看的理由"
      metrics:
        - five_second_retention
        - continue_watch_signal
      if_bad:
        diagnosis:
          - hook_exists_but_no_relevance
          - no_result_preview
          - no_user_scenario
        next_structure_action:
          - add_specific_scene
          - add_result_gap_preview
          - connect_to_user_pain

    problem_expand_8_15s:
      goal: "让用户代入问题"
      metrics:
        - ten_second_retention
        - pain_comment_signal
      if_bad:
        diagnosis:
          - user_not_entering_scene
          - problem_too_abstract
        next_structure_action:
          - add_real_failure_case
          - add_cost_or_risk_detail
          - add_common_wrong_method

    evidence_middle:
      goal: "用真实证据撑住中段"
      metrics:
        - avg_watch_time
        - completion_rate
        - save_rate
      if_bad:
        diagnosis:
          - evidence_unclear
          - too_much_talking
          - no_visible_result_gap
        next_structure_action:
          - add_screen_recording
          - add_before_after
          - add_cost_table
          - shorten_explanation

    judgment_turn:
      goal: "给出清晰判断 / 反转"
      metrics:
        - like_rate
        - comment_quality
        - share_signal
      if_bad:
        diagnosis:
          - weak_position
          - no_new_angle
          - no_reversal
        next_structure_action:
          - add_firmer_judgment
          - add_contrast_sentence
          - add_boundary_statement

    result_diff:
      goal: "让用户看到前后差"
      metrics:
        - save_rate
        - profile_visit
        - dm_signal
      if_bad:
        diagnosis:
          - no_actionable_value
          - result_gap_not_visible
        next_structure_action:
          - show_normal_vs_ai_workflow
          - show_before_after
          - show_minimum_action

    ending_handoff:
      goal: "低压承接需求"
      metrics:
        - dm_count
        - valid_lead_count
        - lead_quality_score
      if_bad:
        diagnosis:
          - no_handoff
          - wrong_lead_filter
          - too_sales_like
        next_structure_action:
          - add_low_pressure_question
          - clarify_service_boundary
          - ask_for_specific_scenario
```

必须新增并填写的反馈卡：

```yaml
content_structure_feedback_card:
  video_id:
  topic:
  current_structure:
    opening_0_3s:
    bridge_3_8s:
    problem_expand_8_15s:
    evidence_middle:
    judgment_turn:
    result_diff:
    ending_handoff:
  segment_metrics:
    opening_0_3s:
    bridge_3_8s:
    middle:
    value_signal:
    demand_signal:
  threshold_check:
    single_video_play_threshold:
    retention_threshold:
    value_signal_threshold:
    lead_signal_threshold:
  bottleneck_segment:
  next_content_structure:
    opening_0_3s:
      what_to_place:
      why:
    bridge_3_8s:
      what_to_place:
      why:
    problem_expand_8_15s:
      what_to_place:
      why:
    evidence_middle:
      what_to_place:
      why:
    judgment_turn:
      what_to_place:
      why:
    result_diff:
      what_to_place:
      why:
    ending_handoff:
      what_to_place:
      why:
  confidence:
  human_review_required:
```

## 5. single_primary_variable_rule（单主变量规则）

“只改一个变量”不能机械化理解。正确规则是 1 个主验证变量，最多 2 个协同变量；日常总变量最多 3 个，特殊大改版最多 4 个并标记 `major_revision（大改版）`。

```yaml
single_primary_variable_rule:
  rule: "每条视频只能有 1 个主验证变量，允许 1-2 个协同变量。"

  default_limit:
    primary_variable: 1
    supporting_variables_max: 2
    total_change_variables_max: 3

  major_revision_limit:
    total_change_variables_max: 4
    must_mark_as: "major_revision"
    attribution_rule: "只能观察方向，不得归因到单一变量。"

  variable_layers:
    primary_variable:
      meaning: "本期真正验证的核心变量。"
    supporting_variables:
      meaning: "为了让主变量成立，必须一起微调的变量。"
    observed_variables:
      meaning: "本期只观察，不主动改。"
    forbidden_variables:
      meaning: "本期明确不碰，防止数据解释混乱。"

  blocked_if:
    - "没有 primary_variable 不得进入文案修改。"
    - "超过 3 个变量且未标 major_revision，不得进入执行。"
    - "超过 4 个变量，不得写成数据实验，只能写成方向重做。"
```

示例：

```yaml
example_opening_retention_bad:
  primary_variable: opening_hook
  supporting_variables:
    - first_sentence
    - first_screen_visual
  forbidden_variables:
    - target_user
    - middle_evidence_structure
    - ending_handoff

example_save_rate_low:
  primary_variable: reusable_value
  supporting_variables:
    - middle_step_structure
    - result_diff_display
  forbidden_variables:
    - opening_route
    - target_user
    - publish_title

example_low_play_high_quality_leads:
  primary_variable: reach_amplification_same_direction
  supporting_variables:
    - title
    - opening_scene_expression
  forbidden_variables:
    - target_user
    - service_direction
    - core_claim
```

归因边界：

- 1 主变量 + 2 协同变量以内，可以做日常数据实验。
- 4 个变量必须标记 `major_revision`，只能观察方向，不得归因到单一变量。
- 5 个以上变量必须 blocked 为 `direction_rebuild_observation`，不得写成单变量实验。

## 6. next_video_execution_prompt（下一条视频执行 prompt）

ChatGPT 根据目标和数据修改文案后，必须同步生成 Codex 动态执行 prompt。Codex 不得只拿 `final_script（最终文案）` 自由发挥。

```yaml
next_video_execution_prompt:
  purpose: "ChatGPT 根据目标和数据修改文案后，必须同步生成 Codex 执行 prompt。"

  required_inputs:
    - current_goal
    - threshold_config_v1
    - previous_video_data
    - post_publish_review_card
    - content_structure_feedback_card
    - primary_variable
    - supporting_variables
    - forbidden_variables
    - revised_script
    - success_metric
    - failure_metric

  required_sections:
    - previous_data_summary
    - threshold_check
    - diagnosis
    - variable_plan
    - copy_revision_strategy
    - final_script
    - edit_instruction_for_codex
    - visual_role_by_segment
    - material_binding
    - tts_direction
    - card_usage
    - forbidden_actions
    - done_when
    - blocked_if
    - output_format

  hard_rule:
    - "Codex 不得只拿 final_script 自由发挥。"
    - "Codex 必须按目标、数据短板、主变量、协同变量、文案结构意图和画面职责执行。"
    - "没有 next_video_execution_prompt，不得进入视频执行。"
```

结构计划模板：

```yaml
next_video_structure_plan:
  video_id:
  based_on_previous_video:
  main_bottleneck:
  threshold_check:
  primary_variable:
  supporting_variables:
  forbidden_variables:
  opening_0_3s:
    content_to_place:
    reason:
  bridge_3_8s:
    content_to_place:
    reason:
  problem_expand_8_15s:
    content_to_place:
    reason:
  evidence_middle:
    content_to_place:
    reason:
  judgment_turn:
    content_to_place:
    reason:
  result_diff:
    content_to_place:
    reason:
  ending_handoff:
    content_to_place:
    reason:
  expected_metric_improvement:
  validation_after_publish:
```

Codex 动态执行 prompt 最小模板：

```text
next_video_execution_prompt:
  previous_data_summary:
  threshold_check:
  diagnosis:
  variable_plan:
    primary_variable:
    supporting_variables:
    forbidden_variables:
    major_revision:
    attribution_boundary:
  copy_revision_strategy:
  final_script:
  edit_instruction_for_codex:
  visual_role_by_segment:
    opening_0_3s:
    bridge_3_8s:
    problem_expand_8_15s:
    evidence_middle:
    judgment_turn:
    result_diff:
    ending_handoff:
  material_binding:
  tts_direction:
  card_usage:
  forbidden_actions:
    - do_not_generate_media_without_authorization
    - do_not_promote_content_validation
    - do_not_change_send_ready
    - do_not_touch_dist_latest_review_pack_unless_task_explicitly_authorizes
  done_when:
    - If any repository file is created or modified, this task is not completed until relevant files are explicitly staged, commit is created, push to the current reading branch succeeds, remote HEAD is verified, unrelated dirty / untracked files are not included, and staged secret scan passes.
  git_completion_requirement:
    - relevant_files_staged_explicitly
    - commit_created
    - pushed_to_current_reading_branch
    - remote_head_verified
    - unrelated_dirty_files_not_included
    - secret_scan_passed
  git_sync_status_required:
    - current_branch
    - files_changed
    - files_staged
    - commit_sha
    - pushed
    - remote_head_verified
    - unrelated_dirty_files
    - secret_scan
    - completed_allowed
  blocked_if:
    - missing_threshold_config_v1
    - local_changes_done_but_not_pushed
    - remote_head_not_verified
    - unrelated_dirty_files_cannot_be_isolated
    - secret_scan_failed
    - missing_video_goal_card
    - missing_post_publish_review_card_when_claiming_data_driven
    - missing_main_bottleneck
    - missing_primary_variable
    - missing_content_structure_feedback_card_when_using_data_to_change_structure
  output_format:
```

## 7. data_flywheel_memory（数据飞轮记忆）

`data_flywheel_memory（数据飞轮记忆）` 用来把多条视频的阶段信号沉淀为下一轮判断输入，但不能把单条高播放或单个客资升级成方向成立。

```yaml
data_flywheel_memory:
  scope:
    - per_video
    - same_topic_cluster
    - stage_0_30
    - stage_31_90
    - stage_90_180
  entries:
    - video_id:
      topic:
      published_at:
      stage_window:
      goal_card:
      post_publish_review_card:
      threshold_check:
      main_bottleneck:
      primary_variable:
      supporting_variables:
      content_structure_feedback_card:
      lead_signal_summary:
      reusable_learning:
      not_validated_yet:
      status_boundary:
        direction_validation:
        demand_validation:
        commercial_validation:
```

记忆规则：

- 单条视频只能提供局部信号。
- 同方向多条样本重复出现，才允许写 `部分成立`。
- 数据不足时写 `待验证`，不能为了推进文案而补猜。
- 需求 / 客资 / 商业验证必须分层，不能把播放、点赞或泛私信混成商业成立。

## 8. blocked_if / done_when（阻断条件 / 完成标准）

```yaml
blocked_if:
  - missing_threshold_config_v1
  - missing_video_goal_card
  - missing_post_publish_review_card_when_claiming_data_driven
  - missing_main_bottleneck
  - missing_primary_variable
  - missing_content_structure_feedback_card_when_using_data_to_change_structure
  - missing_next_video_execution_prompt_before_video_execution
  - missing_delivery_baseline_gate_before_formal_operation_video_delivery
  - publish_candidate_unavailable_but_preview_generated_as_delivery
  - too_many_variables_without_major_revision
  - more_than_four_variables_claimed_as_single_variable_experiment
  - data_insufficient_but_claiming_direction_validated
  - single_high_play_claimed_as_direction_validated
  - single_high_lead_claimed_as_business_model_validated
  - threshold_config_written_as_industry_truth
  - static_gpt_project_package_written_as_live_fact_source

done_when:
  - goal_driven_data_flywheel_spec_v1_written
  - threshold_config_v1_written
  - lead_score_model_written
  - data_goal_copy_revision_gate_written
  - content_structure_feedback_engine_written
  - single_primary_variable_rule_written
  - next_video_execution_prompt_written
  - video_goal_card_defined
  - post_publish_review_card_defined
  - data_flywheel_memory_defined
  - content_structure_feedback_card_defined
  - next_video_structure_plan_defined
  - copy_revision_preflight_blockers_synced_to_codex_execution_rules
  - project_state_action_router_synced
  - fixture_cases_cover_normal_and_blocked_paths
  - latest_and_dated_log_updated
  - gpt_project_static_package_generated_with_manifest
  - if_video_delivery_task_then_publish_candidate_or_blocked
```

状态边界：

- 本文件写入只代表机制已落库。
- 本文件不代表下一条真实新片已经按数据飞轮执行。
- 本文件不代表阈值已被真实样本验证。
- 本文件不代表内容验证通过、可发送、发布状态推进、声音通过或视觉母版锁定。
