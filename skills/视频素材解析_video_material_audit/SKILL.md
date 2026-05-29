# 视频素材解析 video_material_audit

## name
视频素材解析 video_material_audit

## description
当任务涉及“素材录制、解析视频、审计素材、第几期素材、给 ChatGPT 写素材报告、判断素材证据链、平台风险、隐私风险”时使用。本 skill 用于把用户录制的视频素材解析成 ChatGPT 可用于写稿、复审和内容判断的结构化报告。

本 skill 只做素材层审计和证据层判断，不替代 ChatGPT / 用户的内容判断，也不把素材存在、媒体可解码或抽帧成功写成 `content_validation（内容验证）` 通过。

## when_to_use
命中以下任一场景时使用：
- 用户说“我录好素材了”
- 用户说“帮我解析视频”
- 用户说“第几期素材”
- 用户给出素材目录
- 用户要求 Codex 看素材后给 ChatGPT 报告
- 用户要求判断素材能不能支撑文案
- 用户要求判断素材里的平台风险 / 隐私风险

关键词包括但不限于：
- `素材录制`
- `录制素材`
- `解析视频`
- `素材审计`
- `第几期素材`
- `素材细节报告`
- `给 ChatGPT 写素材报告`
- `素材证据链`
- `平台风险`
- `隐私风险`

## not_for
本 skill 不用于：
- 生成最终视频
- 写最终文案
- 生成正式下一条视频执行 prompt
- 修改已发布视频
- 推进 `content_validation（内容验证）`
- 推进 `send_ready（可发送状态）`
- 推进 `publish_candidate（发布候选片）`
- 推进 `current_data_goal_anchor ready（当前数据目标锚点 ready）`
- 判断商业验证成立
- 判断账号方向已成立

## required_inputs
- `material_root（素材目录）`
- `expected_material_count（预期素材数量，可选）`
- `target_content_direction（本轮内容方向，可选）`
- `audit_goal（审计目标）`
- `output_root（输出目录）`

## default_outputs
- `material_parse_pack.json（素材解析包；后续剪辑唯一可消费的一次性解析结果）`
- `material_index.json（素材索引）`
- `material_detail_report.md（素材细节报告）`
- `source_segment_inventory.json（素材片段清单）`
- `material_evidence_contract.json（素材证据契约，可由素材细节报告生成）`
- `dated_log.md（日期日志）`
- `latest.md update（最新日志更新）`
- `contact_sheet（联系表 / 抽帧图，仅本地审计辅助，默认不提交 Git）`

## execution_steps
1. 输出 `route_decision（路由判断）`，确认本轮是素材审计，不是视频生成或状态推进。
2. 输出 `state_action_router（项目状态动作总控器）`，确认事实源、当前状态、允许动作和禁止动作。
3. 检查 `material_root` 是否存在，并按 `expected_material_count` 做数量检查。
4. 用 `ffprobe（媒体信息检查工具）` 读取每个视频的元信息。
5. 用 `ffmpeg（媒体处理工具）` 做基础可解码检查。
6. 对每个素材生成 contact sheet，保存到项目内 `dist/material_audit/<episode>/`。
7. 基于 contact sheet 和关键帧，按时间码解析可见内容、用户动作、可读文字和不确定点。
8. 判断素材能证明什么、不能证明什么，以及是否足以支撑目标内容方向。
9. 检查平台风险和隐私风险，并给出可规避建议。
10. 生成 `material_parse_pack.json（素材解析包）` 和 `source_segment_inventory.json（素材片段清单）`，把本次一次性解析结果锁成后续剪辑唯一输入。
11. 生成或保证可生成 `material_evidence_contract.json`，让后续剪辑可以逐句引用素材证据，而不是只给 ChatGPT 阅读。
12. 生成 `material_index.json`、`material_detail_report.md` 和 dated log。
13. 更新 `codex_log/latest.md`，但不得推进内容、发布或数据目标状态。
14. 做 JSON parse、Markdown 非空、核心脚本 py_compile、Git source media 未 staged 等验证。

## required_checks
1. 目录存在性检查
2. 素材数量检查
3. `ffprobe` 元信息检查
4. `ffmpeg` 可解码检查
5. contact sheet 生成
6. 时间码级内容解析
7. 证据强度判断
8. 平台风险判断
9. 隐私风险判断
10. ChatGPT 写稿建议
11. 状态边界检查：不推进 `content_validation / send_ready / publish_candidate / current_data_goal_anchor ready`
12. 素材解析包字段检查：`parse_pack_id / source_files / material_detail_report_path / source_segment_inventory_path / reuse_policy / stale_if`
13. 素材片段清单字段检查：`segment_id / material_id / source_file / timecode_start / timecode_end / can_support / cannot_support / evidence_strength`
14. 素材证据契约字段检查：`can_support / cannot_support / best_use / not_allowed_use / privacy_risk / public_safe`
15. Git 检查：不提交原始视频素材

## technical_probe_fields
每个素材至少记录：
- `material_id`
- `file_name`
- `source_path`
- `size`
- `duration`
- `resolution`
- `aspect_ratio`
- `fps`
- `codec`
- `audio_present`
- `decodable`
- `rotation`
- `color_space`
- `technical_status`
- `contact_sheet_path`

## timecode_parse_schema
每段时间码必须包含：
- `timecode`
- `visible_content`
- `user_action`
- `readable_text`
- `possible_copy_value`
- `evidence_strength`
- `platform_risk`
- `privacy_risk`
- `uncertainty`

## timecode_granularity
- 重要片段按 5-15 秒一段解析。
- 非重要片段可按 15-30 秒一段解析。
- 每个素材至少拆 5 段。
- 素材很短时，优先拆关键动作点。
- 画面读不清时，写 `low_readability / uncertain_need_human_check`，不得脑补。

## evidence_strength_levels
- `high`
- `medium`
- `low`
- `not_evidence`
- `unclear_need_human_check`

## support_judgment_fields
每个素材必须回答：
- `can_support`
- `cannot_support`
- `best_use`
- `not_allowed_use`
- `needs_reshoot`

## material_parse_pack_schema
每轮素材审计必须把原始素材的一次性解析结果落成 `material_parse_pack（素材解析包）`；后续剪辑阶段只能读取该解析包和它引用的结构化产物，不得重新解析原始素材作为主要判断来源。

```text
material_parse_pack:
  parse_pack_id:
  material_root:
  source_files:
    - path:
      size:
      mtime:
      material_id:
  material_index_path:
  material_detail_report_path:
  contact_sheet_paths:
  source_segment_inventory_path:
  parse_timestamp:
  parse_scope:
  skill_used: skills/视频素材解析_video_material_audit/SKILL.md
  reuse_policy: reuse_only
  stale_if:
    - source_file_added_deleted_or_renamed
    - source_file_size_or_mtime_changed
    - script_target_changed_and_pack_cannot_support
    - user_requested_reaudit
    - missing_key_timecode_or_evidence_fields
```

`source_segment_inventory（素材片段清单）` 至少包含：

```text
source_segment_inventory:
  segments:
    - segment_id:
      material_id:
      source_file:
      timecode_start:
      timecode_end:
      visible_content:
      readable_text:
      user_action:
      evidence_strength:
      can_support:
      cannot_support:
      best_use:
      not_allowed_use:
      privacy_risk:
      platform_risk:
      public_safe:
```

硬规则：

- 原始素材只解析一次；同一轮后续剪辑不得重新扫素材后覆盖本报告判断。
- `material_parse_pack` 缺失、过期或缺关键时间码 / 证据字段时，后续剪辑必须 blocked。
- 文案目标变化导致旧解析包无法支撑时，必须 blocked 或重新进入素材审计；不得在剪辑阶段临时补理解。
- contact sheet 只作为审计证据引用，不是剪辑阶段重新判断素材能证明什么的入口。

## material_evidence_contract_schema
后续视频执行默认需要从本报告生成：

```text
material_evidence_contract:
  material_id:
  source_file:
  timecode_start:
  timecode_end:
  visible_content:
  readable_text:
  user_action:
  evidence_claims:
    - claim_id:
      claim_text:
      claim_type:
        - data_visible
        - workflow_step
        - ui_action
        - ai_judgment_visible
        - report_structure_visible
        - result_page_visible
        - background_context_only
      evidence_strength:
        - direct
        - partial
        - weak
        - not_evidence
      can_support:
      cannot_support:
      best_use:
      not_allowed_use:
  platform_risk:
  privacy_risk:
  public_safe:
```

硬规则：

- `background_context_only` 不能当 direct evidence。
- `privacy_risk = high` 的素材不得默认入片。
- `cannot_support` 中明确禁止的文案点不得绑定该素材。
- 后续 `line_group_evidence_gate` 必须能引用这里的 `material_id / timecode / claim_id`。

## platform_risk_signals
- 全自动
- 一键生成
- 无人值守
- 自动发布
- 直接复制粘贴
- 可运行脚本
- 批量做号
- 起号
- 引导私信领取
- 引导下载工具
- 引导站外跳转
- 账号交易 / 代运营暗示
- 收益承诺
- 工具界面停留过长且没有用途解释
- 命令行 / 代码 / 第三方工具画面被平台误判为风险引导

## platform_risk_levels
- `low`
- `medium`
- `high`
- `blocked_for_publish_use`

平台风险输出必须说明：
- 风险出现在哪个素材和时间码
- 是画面风险还是文案风险
- 如果用于公开视频，应如何规避
- 是否建议裁切、打码、改成卡片解释或不使用

## privacy_risk_signals
- 本地路径
- 用户名
- 桌面文件
- 下载目录
- 浏览器侧栏
- 聊天记录中的敏感内容
- API key
- token
- 邮箱
- 手机号
- 客户信息
- 私信内容
- 未打码头像
- 未打码账号名

隐私风险输出必须包含：
- `timecode`
- `risk_type`
- `risk_level`
- `recommended_action`

## blocked_if
- `material_root` 不存在
- 素材无法解码
- 素材数量无法确认且用户任务依赖固定数量
- 发现高危隐私信息且无法确认是否可打码
- 只能确认文件存在，无法解析画面内容
- 用户要求直接生成视频，但缺文案 / 证据 / 时间线 / 审片标准
- 入口文件更新会覆盖或混淆既有未提交改动
- Git 无法确认原始素材未 staged

## not_allowed
- 不提交原始视频素材到 Git
- 不提交大体积抽帧视频 / 大量图片到 Git，除非用户明确授权且仓库已有规则允许
- 不把素材存在写成内容通过
- 不把素材可用写成方向成立
- 不把技术检查通过写成内容验证通过
- 不生成正式下一条视频执行 prompt
- 不写最终口播文案
- 不调用外部生成 API
- 不读取 `.env / API key / token / secret`
- 不推进 `content_validation / send_ready / publish_candidate / current_data_goal_anchor ready`

## final_report_required_sections
1. 本轮结论
2. 素材清单
3. 媒体基础信息
4. 逐素材时间码解析
5. 证据强度判断
6. 可支撑的文案点
7. 不能证明 / 禁止写入的内容
8. 平台风险与隐私风险
9. 是否需要补录
10. 给 ChatGPT 的写稿建议
11. 下一步建议

## chatgpt_summary_required_sections
报告末尾必须包含 `ChatGPT 快速写稿输入包`：
- 推荐主标题方向
- 推荐开头证据
- 推荐中段证据
- 推荐结尾判断
- 不能写的内容
- 需要用户确认的内容

## acceptance_criteria
- skill 已在项目仓库内读取和引用。
- 每个素材都有媒体基础信息、contact sheet、时间码解析、证据强度、平台风险、隐私风险和补录判断。
- 报告足够 ChatGPT 直接判断写稿方向，不需要重新猜素材内容。
- 报告明确 `skill_used = skills/视频素材解析_video_material_audit/SKILL.md`。
- 报告明确素材审计不等于内容通过、方向成立或发布 ready。
- 验证记录包含 JSON parse、Markdown 非空、核心脚本 py_compile、source media not staged。
