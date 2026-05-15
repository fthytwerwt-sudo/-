# DeepSeek supply controller 协议

## 1. 文件定位

本文件定义《视频工厂》的 `DeepSeek supply controller（DeepSeek 供料中控）` 最小机制。

它负责：
- 规定 Codex 每轮任务如何默认进入 DeepSeek 供料闸门
- 规定 DeepSeek 执行前供料和执行后风险复核的固定输出
- 规定每次供料只能做什么小动作
- 规定 DeepSeek 允许读取和禁止读取的范围
- 规定供料包如何回流给 Codex

它不负责：
- 启动后台常驻服务
- 证明 `multi-agent runtime（多 agent 运行时）` 已跑通
- 让 DeepSeek 写文件
- 让 DeepSeek 拍板项目事实
- 修改视频、声音、发布状态

## 2. mandatory_deepseek_supply_loop（强制 DeepSeek 供料循环）

当前默认机制从 `if_needed_trigger（按需触发）` 升级为 `mandatory_by_default（默认强制）`。

标准链路：

```text
Codex route_decision（路由判断）
-> deepseek_supply_gate（DeepSeek 供料闸门）
-> create_supply_request（创建供料请求任务卡）
-> run_deepseek_pre_supply（执行前 DeepSeek 供料）
-> Codex read / audit / execute（Codex 读取 / 审计 / 执行）
-> Codex vertical_completion（Codex 二次补全）
-> run_deepseek_post_risk_review（执行后 DeepSeek 风险复核）
-> Codex validation / sync（Codex 验证 / 同步）
```

硬规则：

1. 每轮 Codex 任务默认必须创建 `supply_request（供料请求任务卡）`。
2. 每轮默认必须尝试安全真实调用 DeepSeek；安全调用默认由 `DeepSeek runtime provider（DeepSeek 运行时供应商）` 加载授权 key source，并只注入 DeepSeek 子进程 env。
3. DeepSeek 执行前供料必须输出：`file_map`、`risk_report`、`context_summary`、`missing_files`、`codex_next_input`，且命中视频执行、剪辑、编排或下一条视频时必须围绕 `data_goal_anchor（数据目标锚点）` 回答。
4. DeepSeek 执行后风险复核必须输出：`status_promotion_risk`、`forbidden_change_risk`、`missed_sync_files`、`fallback_mislabel_risk`、`remaining_work`。
5. 如果 DeepSeek 未真实调用，controller 必须写出原因：`runtime_setup_required`、`fallback_local_only`、`blocked_missing_process_env_api_key`、`blocked_invalid_api_key`、`blocked_network_or_timeout` 或 `not_attempted_policy_violation`。
6. 如果 DeepSeek token 未观察到减少，不能写 DeepSeek 已深度参与；应写 `token_usage_observed_or_user_check_required = user_check_required`。
7. Codex 不得凭“我觉得本轮不用 DeepSeek”跳过供料闸门；跳过且无 blocked 原因，视为执行失败。
8. DeepSeek 仍只供料，不写文件、不 commit、不 push、不拍板项目事实、不替代 Codex 验证。
9. DeepSeek 不得改写 `current_stage_goal（当前阶段目标）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）`、`forbidden_variables（禁止变量）` 或验证指标。
10. controller / explorer 不直接读取 `.env`、`.env.local` 或本地授权文件；只有 provider 可在授权范围内读取，并且不得打印、写出、提交 key。

以下旧触发原因只保留为供料请求的具体原因标签，不再代表“是否触发”的默认裁量：

1. `missing_context（缺上下文）`
2. `rule_conflict（规则冲突）`
3. `stale_context_risk（旧口径污染风险）`
4. `large_context（上下文过大）`
5. `before_write_gate（写入前依据不足）`
6. `after_read_gap（读完仍有缺口）`
7. `user_explicit_deepseek（用户明确要求 DeepSeek 参与）`
8. `mandatory_pre_supply（强制执行前供料）`
9. `mandatory_post_risk_review（强制执行后风险复核）`

触发 controller 不等于自动通过 DeepSeek 生成；controller 必须如实记录供料来源。

## 2A. runtime provider（运行时供应商）

DeepSeek 真实供料默认入口：

```text
scripts/DeepSeek运行时供应商_deepseek_runtime_provider.py
-> scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py
-> scripts/deepseek_supply_controller.py
-> scripts/deepseek_readonly_explorer.py
```

provider 规则：

```text
load_order:
  - process_env
  - project_env_local
  - project_env
  - local_runtime_authorization
allowed_key_name:
  - DEEPSEEK_API_KEY
never_print_key: true
never_write_key: true
inject_to_child_process_only: true
redact_stdout_stderr: true
```

如果 provider 找不到 key，任务必须输出 `runtime_setup_required（需要运行时安装）`，并引导一次性配置；不得每轮重复退回 `blocked_missing_process_env_api_key`。

## 3. action mechanism（行动机制）

DeepSeek 每次只做一个小动作，不能一次吞掉完整项目任务。

controller 当前支持完整 `execution_supply_pack family（执行供料包族）`：

1. `file_map（文件地图）`
   - 输出本轮应该读哪些文件，为什么读。
2. `risk_report（风险报告）`
   - 输出旧口径、冲突、误写、越权风险。
3. `context_summary（上下文摘要）`
   - 把已读文件压缩成 Codex 可用摘要。
4. `missing_files（缺失文件）`
   - 判断还缺哪些文件，下一轮应该补读什么。
5. `visual_asset_requirement_pack（视觉素材需求包）`
   - 判断一条最终文案进入执行后，需要哪些视觉素材，哪些必须是真实证据，哪些只能做辅助表达。
6. `api_asset_generation_pack（API 素材生成包）`
   - 判断哪些素材可以由阿里 API / 豆包 / 其他供应商生成，以及生成计划、降级路线和禁止调用边界。
7. `image_prompt_pack（图片 prompt 包）`
   - 为每张候选生成图片写 prompt、negative prompt、构图、风格锚点和验收标准，不生成真实图片。
8. `asset_validation_pack（素材验收包）`
   - 判断 API 生成图、卡片或素材是否可进入装配，必要时要求 revise / reject / pending_human_review。
9. `assembly_decision_pack（装配决策包）`
   - 决定文案、真实录屏、API 生成图、PPT 卡片、人物段、TTS、字幕如何进入时间线。
10. `editing_decision_pack（剪辑决策包）`
   - 用于视频剪辑、录屏放大、卡片插入、中段承载、画面证据链保护等任务。
   - 只基于 Codex 提供的文字化素材样料生成建议，不直接读取视频 / 音频 / 图片等媒体文件。
11. `auto（自动）`
   - 只能在上述非 `auto` action 中选择，不允许生成自由任务。

Codex 后续执行仍必须复核原文件；供料包只是输入，不是最终判断。

### 3A. `execution_supply_pack family（执行供料包族）`

`execution_supply_pack family（执行供料包族）` 用来承接“最终文案进入执行后”的全链路供料。标准链路是：

```text
content_route_card（内容路由卡）
-> visual_asset_requirement_pack（视觉素材需求包）
-> api_asset_generation_pack（API 素材生成包）
-> image_prompt_pack（图片 prompt 包）
-> asset_validation_pack（素材验收包）
-> assembly_decision_pack（装配决策包）
-> editing_decision_pack（剪辑决策包）
-> review_pack（审片包回流）
```

凡任务命中以下任一情况，Codex 必须判断是否触发本供料包族：

- Codex 收到最终文案。
- 需要生成视频。
- 需要卡片 / 图片 / 背景 / 角色 / 图标。
- 需要调用阿里 API 或其他图片 API。
- 需要判断素材是否足够。
- 需要装配时间线。
- 需要剪辑录屏。
- 需要判断素材是否会抢真实证据。

硬边界：

- DeepSeek / controller / explorer 不读取 `.env`、`.env.*`、API key、token 或密钥文件；runtime provider 可在用户授权范围内读取 key source 并只注入子进程 env。
- 不调用阿里、豆包或任何真实生成 API。
- 不读取视频、音频、图片或 `dist/latest_review_pack/` 媒体产物。
- 不把 API 生成图片当真实录屏证据。
- 不把 DeepSeek / fallback 供料当最终内容判断。
- 若任务卡禁止 `.env / secret`，controller / explorer 仍不得读取真实 `.env`；需要真实 DeepSeek 参与时必须通过 runtime provider 注入子进程 env，否则写 `runtime_setup_required` 或 blocked。

数据目标供料硬规则：

- 命中视频执行、剪辑、编排、下一条视频或发布后复盘时，`supply_request（供料请求任务卡）` 必须包含 `current_data_goal_anchor_path（当前数据目标锚点路径）`、`current_data_goal_anchor_status（当前数据目标锚点状态）` 和 `data_goal_anchor（数据目标锚点）`，或明确写出缺失并 blocked。
- 当前实例锚点优先来源固定为 `codex_log/current_data_goal_anchor.md（当前数据目标锚点）`。
- 若 `current_data_goal_anchor_status = draft / waiting_data`，DeepSeek / fallback 只能输出假设版风险供料或 blocked，不得写正式数据驱动执行 ready。
- DeepSeek 输出必须回答：
  - 这轮目标要求读哪些文件？
  - 哪些旧口径会破坏目标？
  - 哪些执行选择支持主变量？
  - 哪些执行选择会引入禁止变量？
  - 哪些剪辑 / 编排风险会影响发布后验证指标？
- DeepSeek 可以建议 `segment_order / card_position / editing_style / assembly_sequence / material_binding / tts_segmentation / fallback_visuals`，但不能改写目标。
- `fallback_local_only（本地兜底）` 可以作为低风险机制任务的本地参考，但不得写成 DeepSeek 数据目标供料已通过。

各包最小输出字段：

```text
visual_asset_requirement_pack:
  script_block:
  segment:
  viewer_task:
  required_asset_type:
  evidence_role:
  why_needed:
  can_be_api_generated:
  must_be_real_evidence:
  fallback_if_missing:
  blocked_if:

api_asset_generation_pack:
  generation_needed:
  vendor_candidate:
  model_or_service:
  asset_count:
  aspect_ratio:
  resolution:
  style_constraints:
  segment_usage:
  prompt_needed:
  negative_prompt_needed:
  api_call_allowed_this_round:
  secret_required:
  fallback_plan:
  blocked_if:

image_prompt_pack:
  asset_id:
  segment:
  purpose:
  positive_prompt:
  negative_prompt:
  style_anchor:
  composition:
  text_policy:
  must_not_include:
  acceptance_criteria:
  rejected_if:

asset_validation_pack:
  asset_id:
  source:
  intended_use:
  validation_result:
  style_fit:
  evidence_fit:
  readability:
  platform_risk:
  copyright_or_official_asset_risk:
  human_feel:
  required_fix:
  blocked_if:

assembly_decision_pack:
  current_data_goal_anchor_source:
  data_goal_anchor_used:
  segment_goal:
  carrier_reason:
  metric_supported:
  variable_preserved:
  forbidden_variable_avoided:
  post_publish_validation_metric:
  segment:
  primary_carrier:
  secondary_carrier:
  asset_to_use:
  timing:
  transition:
  tts_relation:
  subtitle_relation:
  evidence_chain_note:
  needs_editing_decision_pack:
  blocked_if:
```

### 3B. `editing_decision_pack（剪辑决策包）`

`editing_decision_pack（剪辑决策包）` 专门回答视频执行现场的剪辑判断问题：

- 哪些片段要放大。
- 哪些片段保持原画面。
- 哪些片段需要局部框选 / 高亮。
- 哪些地方适合插提示卡。
- 哪些地方不该动，避免破坏真实证据。
- 哪些 reference 只继承质量，不照搬流程。
- 哪些剪辑动作会让视频像 demo / 说明书 / 硬拼接。

边界：

- DeepSeek 不直接剪视频。
- DeepSeek 不直接看视频或媒体文件。
- DeepSeek 不拍板最终画面好不好。
- DeepSeek / fallback 只基于文本样料生成决策建议。
- Codex 执行前必须复核素材证据和原文件。
- 最终内容判断仍由 ChatGPT / 用户完成。

数据目标边界：

- DeepSeek / fallback 必须基于 Codex 提供的 `data_goal_anchor（数据目标锚点）` 判断剪辑风险。
- 缺 `data_goal_anchor_used（使用的数据目标锚点）` 时，必须建议 Codex 阻断剪辑 / 编排执行。
- 剪辑建议只能调整执行结构，不能改写主短板、主变量、禁止变量或发布后验证指标。

Codex 触发该 action 前，必须尽量提供以下文字化样料：

- `source_segments（素材片段）`
- `narration_lines（口播句子）`
- `contact_sheet_description（联系表描述）`
- `ocr_text（OCR 文字）`
- `frame_descriptions（抽帧描述）`
- `reference_quality_points（参考质量点）`
- `editing_question（剪辑问题）`

若上述样料不足，controller 不必默认 blocked，但供料包必须显式标记：

- `missing_context（缺失上下文）`
- `blocked_if_insufficient_editing_sample（文字化剪辑样料不足时阻断）`

`editing_decision_pack（剪辑决策包）` 最小输出字段：

```text
editing_decision_pack:
  current_data_goal_anchor_source:
  data_goal_anchor_used:
  line_group_goal:
  primary_variable_support:
  evidence_role_for_metric:
  forbidden_visuals_by_goal:
  edit_action_reason_against_data_goal:
  post_publish_validation_metric:
  source_segment:
    file_reference:
    time_range:
    visible_content:
    evidence_role:
  narration_intent:
    line:
    function:
    viewer_should_understand:
  visual_action:
    action_type:
      - full_frame
      - zoom_in
      - crop_focus
      - highlight_box
      - freeze_frame
      - insert_card
      - split_compare
      - do_not_touch
    target_area:
    timing:
  reason:
  reference_quality_point:
  risk:
  blocked_if:
  codex_execution_note:
```

## 4. scope mechanism（范围机制）

DeepSeek / controller 只读范围默认允许：

- `AGENTS.md（仓库入口规则）`
- `codex_source/*.md（Codex 执行规则）`
- `codex_log/latest.md（最新摘要）`
- `codex_log/current_*.md（当前状态日志）`
- `GPT数据源/*.md（GPT 数据源规则包）`
- `review_loop/*.md（复盘闭环规则）`
- `scripts/*.py（脚本）`
- 用户显式指定的文本类文件

默认禁止读取：

- `.env（真实环境变量文件）`
- `.env.*（环境变量衍生文件）`
- `.env.swp（本地交换文件）`
- 密钥文件
- token 文件
- 任何二进制媒体文件
- 视频文件
- 音频文件
- 图片文件
- `dist/latest_review_pack/（最新审片包）` 中的大媒体文件
- archive-only 外部目录
- Git 内部文件
- `.git/`

DeepSeek 禁止：

- 写文件
- 改文件
- 删除文件
- commit
- push
- 修改项目事实
- 修改 `content_validation`
- 修改 `send_ready`
- 拍板最终判断

## 5. return mechanism（回流机制）

供料结果固定写入：

- `dist/deepseek_supply_controller/latest_supply_pack.md`
- `dist/deepseek_supply_controller/latest_supply_pack.json`
- `dist/deepseek_supply_controller/latest_supply_manifest.json`

输出必须包含：

- `supply_id（供料编号）`
- `task_type（任务类型）`
- `trigger_reason（触发原因）`
- `action（供料动作）`
- `supply_source（供料来源）`
  - `deepseek_passed`
  - `fallback_local_only`
  - `blocked`
- `context_pack_validation（上下文包验证）`
- `files_considered（已考虑文件）`
- `files_recommended（建议读取文件）`
- `risks（风险）`
- `missing_files（缺失文件）`
- `execution_supply_pack（执行供料包）`，当 action 属于执行供料包族时必须出现
- `codex_next_input（给 Codex 的下一步输入）`
- `not_allowed（禁止事项）`

Codex 后续执行必须读取：

- `dist/deepseek_supply_controller/latest_supply_pack.md`
- 或 `dist/deepseek_supply_controller/latest_supply_pack.json`

供料结果不能只躺在日志里。

## 6. 状态表达规则

允许写：

- `DeepSeek supply controller 最小机制已落地`
- `supply_source = deepseek_passed`
- `supply_source = fallback_local_only`
- `supply_source = blocked`
- `pipeline_status = usable_with_fallback`

禁止写：

- DeepSeek 已稳定供料
- DeepSeek 已替代 Codex
- DeepSeek 已能拍板项目事实
- `fallback_local_only` 等于 DeepSeek 结论
- `multi-agent runtime` 已跑通
- 完整 agent 协作闭环已完成

## 7. supply request schema（供料请求任务卡）

controller 支持两种运行方式：

1. 旧 CLI 参数方式
   - 用于兼容测试和临时低风险任务。
2. `--request-file（供料请求文件）` 方式
   - 推荐作为后续默认方式。
   - 示例：

```bash
python3 scripts/deepseek_supply_controller.py \
  --request-file codex_source/fixtures/deepseek_supply_request_file_map_example.json
```

`supply_request（供料请求任务卡）` 是 DeepSeek 每次“知道当前任务”的唯一正式输入。

硬规则：

- DeepSeek 不靠长期记忆理解当前任务。
- DeepSeek 不靠猜测理解当前任务。
- DeepSeek 不默认读取全仓库。
- Codex / controller 必须每次显式传入任务卡。
- 任务卡必须写清当前目标、当前步骤、已知上下文、缺失上下文、候选文件、禁止路径、期望输出、停止条件和回流路径。
- request validation 失败时必须 `blocked`，并写 `latest_supply_manifest.json`。

任务卡结构说明见：

- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`

## 7A. execution observation loop（执行观察循环）

DeepSeek / fallback 参与机制升级时，默认允许至少两次供料观察：

1. 执行前：`trigger_reason = before_write_gate`
   - 用于检查旧口径、规则冲突、文件缺口、固定 SOP 化风险和 forbidden 修改风险。
2. 执行后：`trigger_reason = after_read_gap`
   - 用于复核本轮改动是否存在越权、状态误写、fallback 误写、死 SOP 化或遗漏供料来源记录。

如果 Codex 执行中发现读完首批文件后仍有缺口，也可以生成第二张或 follow-up `supply_request（供料请求任务卡）`：

- `trigger_reason = after_read_gap`
- `action = risk_report` / `missing_files` / `context_summary`
- `current_step` 必须写清是执行中补读还是执行后风险复核

每次供料必须记录：

- `supply_source（供料来源）`
- `request_validation_status（请求校验状态）`
- `fallback_status（兜底状态）`
- `not_deepseek_conclusion（是否不是 DeepSeek 结论）`
- `codex_next_input（给 Codex 的下一步输入）`

如果连续两次都是 `fallback_local_only（本地兜底）`，仍可继续低风险文档机制任务，但必须记录：

- `deepseek_generation_unstable = true`
- 本轮结论来自 Codex 原文件复核，不来自 DeepSeek 拍板
- 下轮应继续收紧 request 输入范围、上下文长度或输出约束

供料结果不能替代原文件复核。Codex 改文件前仍必须回读允许修改的原文件；改完后仍必须执行 diff、状态字段、forbidden path 和日志检查。

## 7B. safe DeepSeek participation（DeepSeek 安全真实参与）

当 `supply_request（供料请求任务卡）` 禁止读取 `.env / secret（真实环境变量 / 密钥）` 时，controller 不得为了调用 DeepSeek 去读取 `.env` 文件。

允许的安全真实参与方式只有一种：

```text
禁止读取 .env 文件
允许读取 process environment 中已经存在的 DEEPSEEK_API_KEY
不打印 key
不写 key
不把 key 放进 prompt / supply_pack / log
不把 .env 加入 context-file
只用 key 做 HTTP Authorization
```

实现入口：

- explorer 支持 `--no-env-file` 或 `DEEPSEEK_DISABLE_ENV_FILE=1`，启用后不读取 `.env`。
- controller 支持 `--allow-process-env-api-key` 或 `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1`，启用后只允许通过 process environment 调用 DeepSeek。
- 每轮推荐入口为 `scripts/DeepSeek安全供料运行器_deepseek_safe_supply_runner.py（DeepSeek 安全供料运行器）`：它只设置 `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1` 与 `DEEPSEEK_DISABLE_ENV_FILE=1`，只检查 process environment 中 key 是否存在，不读取 `.env`、不打印 key、不写 key。
- `dist/deepseek_supply_controller/run_live_smoke_with_safe_env_loader.py` 只保留为 20260515 活体测试的本地验证 runner；它曾在用户授权范围内读取 `.env` 声明并注入子进程，但不得自动升级为每轮默认供料入口。
- 如果 process environment 中没有 `DEEPSEEK_API_KEY`，必须写：
  - `deepseek_actual_participation = blocked_missing_process_env_api_key`
  - `env_file_read = false`
  - `api_key_printed = false`
  - `api_key_written = false`
- 该状态不得写成 `deepseek_passed`。

每轮任务安全加载策略：

```yaml
safe_loader_policy:
  mode:
    - process_env_only
    - authorized_subprocess_env_loader_required
    - local_fallback_only
  controller_or_explorer_may_read_env_file: false
  allow_env_file_loader: false
  require_user_authorization_for_env_loader: true
  blocked_if_process_env_missing: true
  api_key_printed: false
  api_key_written: false
```

解释：

- `process_env_only` 是每轮默认安全路径：只使用当前进程环境里已经存在的 `DEEPSEEK_API_KEY`。
- `authorized_subprocess_env_loader_required` 只表示“需要用户本轮明确授权后，才能由安全 loader 在限定范围读取 key 声明并注入子进程”；未授权时必须 `blocked`，不能由 controller / explorer 偷读 `.env`。
- `local_fallback_only` 只能用于低风险机制 / 文档任务，必须写 `not_deepseek_conclusion = true`，不得声称 DeepSeek 真实参与。
- 如果任务卡写 `requires_real_deepseek_participation = true` 或 `safe_loader_policy.blocked_if_process_env_missing = true`，且 process environment 没有 key，必须 `blocked_missing_process_env_api_key`，不得降级成 `fallback_local_only` 后继续写 DeepSeek 已参与。

安全边界：

- 进程环境变量只用于本地 HTTP Authorization，不属于 DeepSeek 上下文。
- DeepSeek 仍不得读取 `.env`、API key、token、密钥文件或媒体文件。
- controller / explorer 不得把 key 打印到 stdout、stderr、manifest、supply pack 或日志。
- 即使本轮 `deepseek_passed`，也只能写成本轮样例供料通过，不代表 DeepSeek 稳定真实供料。

## 7B-1. deepseek_readiness_check（DeepSeek 就绪检查）

controller 每次输出 supply pack 和 manifest 时，必须同步写 `deepseek_readiness_check（DeepSeek 就绪检查）`，让 Codex 后续任务先判断 DeepSeek 是否真的参与、是否只是本地兜底、是否必须阻断。

字段固定为：

```text
deepseek_readiness_check:
  env_file_read:
  process_env_key_allowed:
  process_env_key_present:
  safe_call_mode:
  request_validation_status:
  supply_source:
  fallback_status:
  not_deepseek_conclusion:
  context_pack_validation:
  deepseek_actual_participation:
  blocked_reason:
```

稳定状态必须能区分：

- `deepseek_passed（DeepSeek 真实供料通过）`
- `fallback_local_only（本地兜底）`
- `blocked_missing_process_env_api_key（缺少进程环境 key）`
- `blocked_invalid_api_key（key 无效或权限不足）`
- `blocked_network_or_timeout（网络或超时阻断）`
- `blocked_invalid_context_pack（输出结构不合格）`

规则：

- 只有 `deepseek_passed` 才能写 DeepSeek 真实参与。
- `fallback_local_only` 必须写 `not_deepseek_conclusion = true`。
- blocked 必须写 `blocked_reason`，不得继续包装成 DeepSeek 成功。
- 不允许通过读取 `.env` 把 `blocked_missing_process_env_api_key` 补救成通过。

## 7C. model routing（模型路由）

当前 DeepSeek 供料模型策略：

- `default_supply_model（默认供料模型） = deepseek-v4-flash`
- `escalation_model（升级模型） = deepseek-v4-pro`

使用边界：

- `deepseek-v4-flash` 默认用于常规小步供料：`file_map（文件地图）`、`missing_files（缺失文件）`、`context_summary（上下文摘要）`、普通 `risk_report（风险报告）`、基于文字样料的 `visual_asset_requirement_pack（视觉素材需求包）`、`api_asset_generation_pack（API 素材生成包）`、`image_prompt_pack（图片 prompt 包）`、`asset_validation_pack（素材验收包）`、`assembly_decision_pack（装配决策包）`、`editing_decision_pack（剪辑决策包）`、复盘文件地图和标准提取。
- `deepseek-v4-pro` 只作为复杂任务升级模型：多文件冲突、复杂机制判断、长任务审计、多轮供料包合并、Flash 多次失败后升级、或 Codex 明确标记 `after_read_gap（读完仍有缺口）` 且 fallback 不足。
- 本轮只落地默认模型口径；自动模型升级机制尚未实现，后续如要启用必须另行开发和验证。
- controller 输出必须保留底层 explorer 写出的实际 `model（模型）` 状态；如果输出来源为 `fallback_local_only（本地兜底）`，仍不得写成 DeepSeek 结论。

## 7D. DeepSeek deep collaboration flow（DeepSeek 深度配合流程）

DeepSeek 深度配合不是让 DeepSeek 替代 Codex，也不是证明 `multi-agent runtime（多 agent 运行时）` 已跑通。它只是把只读供料从单次文件地图升级为执行前、执行中、执行后的可回流流程。

标准链路：

```text
Codex route_decision（路由判断）
-> deepseek_supply_gate（DeepSeek 供料闸门）
-> 生成 supply_request（供料请求任务卡）
-> run_deepseek_pre_supply（执行前 DeepSeek 供料 / fallback）
-> 输出 supply_pack（供料包）
-> Codex 读取 supply_pack
-> Codex 复核原文件
-> Codex 执行
-> Codex vertical_completion（Codex 二次补全）
-> run_deepseek_post_risk_review（执行后 DeepSeek 风险复核）
-> latest / dated log 回流
```

硬边界：

- 供料包不能替代原文件。
- `fallback_local_only（本地兜底）` 不能替代 DeepSeek 结论。
- DeepSeek 不能替代 Codex 执行判断。
- Codex 不能替代 ChatGPT / 用户做内容最终判断。
- 本流程只表示机制落地和最小验证方向，不表示真实任务已多轮稳定验证。

## 8. 一句话规则

`DeepSeek supply controller` 是 Codex 每轮任务默认必须进入的只读供料入口：它把任务上下文、文件地图、风险复核、缺口判断和 Codex 下一步输入压缩成固定供料包；DeepSeek 失败时可以使用 `fallback_local_only`，但 fallback 必须明确标记为本地兜底，不得写成 DeepSeek 结论、DeepSeek 深度参与或 multi-agent runtime 已跑通。
