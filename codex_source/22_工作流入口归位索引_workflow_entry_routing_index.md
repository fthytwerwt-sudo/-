# 工作流入口归位索引 Workflow Entry Routing Index

## 1. 用途

本文件只是 Codex 执行入口层的短索引，不新增文案、素材、剪辑、复审或复盘大机制。

2026-06-11 补丁：本文件仅把已通过 fixture（测试用例）验证的三项 Router（路由器）判断挂到现有 workflow（工作流），不新增 workflow 类型，不接入 RAG（检索增强）运行时，不创建向量库。

用途：让 Codex 每轮在 `route_decision（路由判断）` 之后、具体执行之前，先判断任务属于哪条工作流，再读取对应文件、产出对应交接件、触发对应 blocker。

若未输出 `workflow_route_decision（工作流归位判断）`，不得进入写入、生成视频、生成音频、修改媒体或状态推进。

## 2. 每轮必须输出 workflow_route_decision

```text
workflow_route_decision:
  workflow_type:
  reason:
  must_read:
  required_handoff:
  forbidden_status:
  blocked_if:
```

允许的 `workflow_type` 只有：

- `copy_testing_flow（文案测试流）`
- `material_evidence_flow（素材证据流）`
- `aesthetic_editing_flow（审美剪辑流）`
- `quality_review_flow（质量复审流）`
- `data_review_flow（数据复盘流）`
- `mechanism_repair_flow（机制修补流）`

所有工作流默认禁止自动推进：

- `content_validation = passed（内容验证通过）`
- `send_ready = true（可发送）`
- `voice_validation = passed（声音验证通过）`
- `final_voice_validated = true（最终声音验证通过）`
- `visual_master_locked = true（视觉母版锁定）`
- `current_data_goal_anchor_ready = true（当前数据目标锚点 ready）`

除非用户 / ChatGPT 明确最终复审确认，Codex 不得推进以上状态。

## 3. 工作流归位表

### 3.1 copy_testing_flow（文案测试流）

- `input_signal（输入信号）`：最终文案、改文案、标题、开头、下一条视频、文案测试、Perplexity 初稿、ChatGPT 落稿、内容结构反馈。
- `must_read（必须读取）`：`GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`、`codex_log/current_data_goal_anchor.md`。
- `required_handoff（必须交接件）`：`material_detail_report（素材细节报告）`、`final_script_source_check（最终文案来源检查）`、`content_route_card_v2（内容路由卡 V2）`、`script_anchor_extraction_function_output（文案锚点提取结果）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：最终文案来源不明、Perplexity 初稿被当成最终稿、素材细节缺失却要定稿、Codex 被要求直接重写最终文案、数据锚点为 `draft / waiting_data` 却要写正式数据驱动执行。

### 3.2 material_evidence_flow（素材证据流）

- `input_signal（输入信号）`：用户给素材、录屏、截图、时间码、素材审计、素材能否支撑文案、隐私 / 平台风险、给 ChatGPT 写素材报告；用户说新增素材 / 补了素材 / 素材录好了 / 给新素材路径 / 替换素材但未说明旧素材是否废弃。
- `must_read（必须读取）`：`skills/视频素材解析_video_material_audit/SKILL.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`。
- `required_handoff（必须交接件）`：`material_delta_type_router_output（素材增量类型路由器输出）`、`pre_execution_read_gate_output（执行前读取闸门输出）`、`material_parse_pack（素材解析包）`、`source_segment_inventory（素材片段清单）`、`material_detail_report（素材细节报告）`、`material_evidence_contract（素材证据契约）`、`line_visual_alignment_report（文案画面对齐报告）`、`missing_material_or_blocked_report（缺素材或阻断报告）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：素材 skill 未读取、`material_parse_pack（素材解析包）` 未生成、`source_segment_inventory（素材片段清单）` 缺失、时间码缺失、关键页面 / 按钮 / 输入框 / 结果不可见、证据只能证明弱相关、需要补录却被要求继续剪、素材报告被当成最终文案；新增素材和旧素材关系不清、旧候选片 / 锁稿 / 旧素材清单缺失却要直接剪辑。

### 3.3 aesthetic_editing_flow（审美剪辑流）

- `input_signal（输入信号）`：剪辑更好、像作品、不像 demo、节奏不顺、卡片不好看、字幕 / 卡片挡画面、画面不可读、做成可发布候选片；重新剪、重做中段、新素材进入剪辑。
- `must_read（必须读取）`：`material_parse_pack（素材解析包）`、`source_segment_inventory（素材片段清单）`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`、`codex_source/21_codex_judgment_permission_matrix.md`。
- `required_handoff（必须交接件）`：`pre_execution_read_gate_output（执行前读取闸门输出）`、`material_parse_pack_reuse_gate（素材解析包复用闸门）`、`script_to_shot_execution_map（文案到镜头执行表）`、`material_usage_ledger（素材使用台账）`、`duplicate_material_check（素材重复使用检查）`、`editing_inference_function_output（剪辑推理结果）`、`editing_decision_pack（剪辑决策包）`、`visual_readability_report（画面可读性报告）`、`review_pack（审片包）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：缺 `material_parse_pack（素材解析包）`、解析包过期、剪辑阶段需要重新解析原始素材、缺 `source_segment_inventory（素材片段清单）`、缺 `script_to_shot_execution_map（文案到镜头执行表）`、缺 `material_usage_ledger（素材使用台账）`、缺 `duplicate_material_check（素材重复使用检查）`、同一素材片段无 `reuse_reason（复用理由）` 重复使用、连续重复使用同一素材片段、主题相近素材冒充直接证据、选用了 `cannot_support（不能支撑）` 的素材、句组未引用素材报告、缺 line_group 级文案画面对齐、核心证据不可读、字幕 / 卡片 high severity overlap、卡片替代真实证据、只能产出技术预览却要写完成。

### 3.4 quality_review_flow（质量复审流）

- `input_signal（输入信号）`：复审、审片、质量问题、像 demo、不舒服、不合格、不顺、不美观、技术验证、内容验证、send_ready、remaining_blockers；technical_preview（技术预览）、full.mp4 exists（视频文件存在）、route card exists（路由卡存在）、preflight package exists（执行前补全包存在）、声音 / TTS / B 方案 / 旧 Qwen / 阿里 / 百炼 / MiniMax 冲突。
- `must_read（必须读取）`：`codex_log/latest.md`、`GPT数据源/08_当前正式事实.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`dist/latest_review_pack/summary.json`、`dist/latest_review_pack/review_manifest.md`、`codex_source/19_project_state_action_router.md`。
- `required_handoff（必须交接件）`：`pre_execution_read_gate_output（执行前读取闸门输出）`、`completion_truth_preflight_router_output（完成真实性预检路由器输出）`、`voice_route_conflict_gate_output（声音路线冲突闸门输出）`、`quality_issue_classifier_output（质量短板分类结果）`、`technical_validation（技术验证）`、`content_validation_boundary（内容验证边界）`、`remaining_blockers（剩余阻断）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：把技术验证写成内容验证、用户未确认却推进 send_ready、声音 / 视觉 / 内容状态边界不清、缺审片包或关键媒体证据却要裁决可发；`technical_preview（技术预览）`、`full.mp4`、route card 或 preflight package 冒充 `completed（已完成）`；旧 Qwen / 阿里 B 或 MiniMax 系统音色替代当前声音锁。

### 3.5 data_review_flow（数据复盘流）

- `input_signal（输入信号）`：24h、72h、7d、平台数据、播放 / 收藏 / 私信 / 咨询、运营数据、发布后复盘、下一轮只改一个变量。
- `must_read（必须读取）`：`review_loop/00_review_loop_readme.md`、`codex_log/current_operation_target.md`、`review_loop/operation_records_index.md`、`codex_log/current_data_goal_anchor.md`、`codex_log/current_gray_test_target.md`。
- `required_handoff（必须交接件）`：`operation_data_record（运营数据记录）`、`missing_fields_report（缺失字段报告）`、`threshold_check（阈值检查）`、`next_variable_draft（下一变量草稿）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：视频 ID 不明、时间窗不明、数据字段缺失、数据不足却要判断成败、一次改多个主变量、把历史灰度目标当成当前正式运营目标。

### 3.6 mechanism_repair_flow（机制修补流）

- `input_signal（输入信号）`：修规则、补入口、机制修补、路由修补、索引缺口、执行纪律、旧口径残留、读取顺序冲突、实现路线缺失、Codex 能力边界不清、fallback 未写。
- `must_read（必须读取）`：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`、`codex_log/latest.md`，以及被影响的具体机制文件。
- `required_handoff（必须交接件）`：`impact_check（影响面检查）`、`affected_entry_files（受影响入口文件）`、`implementation_design_layer（实现设计层，如本轮涉及 Codex 落地方案）`、`fixture_or_keyword_check（fixture 或关键词检查）`、`status_boundary_report（状态边界报告）`。
- `forbidden_status（禁止状态）`：使用第 2 节统一禁止状态。
- `blocked_if（阻断条件）`：已有等价索引会重复、必须新增大机制、必须改正式事实状态、需要生成视频 / 音频、需要推进内容 / 发布 / 声音 / 视觉状态、本地脏改无法隔离、缺实现设计层却要下发 Codex 落地执行。
