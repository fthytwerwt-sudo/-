# 20260524｜新第四期文案 line_group 与素材时间码对齐

## 1. 本轮任务目标
基于用户提供的 `draft_script_v0.2`，生成新第四期成片前置包：line_group 拆分、V001/V003/V004 时间码映射、TTS 韵律、卡片位置、剪辑决策、隐私可读性检查、copy_change_request 和下一轮成片执行 prompt 草稿。

## 2. route_decision
route_decision（路由判断）
- project_route = video_factory
- task_type = copy_execution_preflight + line_group_mapping + script_to_timeline_map_generation + content_route_card_generation + project_file_change
- responsibility_layer = execution_layer + validation_layer + sync_layer
- large_task_gate = triggered
- lane_recommendation = serial_only（单点整合写入）
- parallel_recommendation = read_only_lanes_possible_but_not_used_for_write
- deepseek_supply_gate = fallback_local_only；not_deepseek_conclusion = true
- allowed_changes = codex_log/script_preflight/新第四期_选品初筛_20260524_231118/；codex_log/20260524_new_fourth_script_line_group_preflight.md；codex_log/latest.md 顶部本轮记录
- forbidden_changes = 视频/音频生成；素材修改；dist/latest_review_pack；content_validation/send_ready/status promotion；媒体提交
- execution_permission = granted_after_required_reads


## 3. state_action_router
state_action_router（项目状态动作总控器）
- input_signal = 用户提供新第四期 draft_script_v0.2，要求拆 line_group 并对齐 V001/V003/V004 素材时间码
- current_project_state = 新第四期素材 partial_ready；V001/V003/V004 可作为句组级证据；V002 弱证据不建议入正片；current_data_goal_anchor 仍为 partial_or_not_ready
- selected_action = script_anchor_extraction + content_route_card_v2 + card_placement_preflight + script_to_timeline_map_generation
- done_when = preflight package + latest + dated log + commit/push
- blocked_if = 关键素材审计缺失 / 无法绑定时间码 / 缺风险标注 / 尝试推进内容状态


## 4. 读取文件清单
- read_ok: `AGENTS.md`
- read_ok: `codex_log/latest.md`
- read_ok: `codex_source/00_codex_readme.md`
- read_ok: `codex_source/01_execution_rules.md`
- read_ok: `GPT数据源/04_选题与文案规则.md`
- read_ok: `GPT数据源/05_文案路由规则.md`
- read_ok: `GPT数据源/07_AI知识类视频价值规则.md`
- read_ok: `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- read_ok: `codex_log/material_audit/新第四期_20260524_001649/05_timeline_segment_map.md`
- read_ok: `codex_log/material_audit/新第四期_20260524_001649/06_evidence_anchor_report.md`
- read_ok: `codex_log/material_audit/新第四期_20260524_001649/08_chatgpt_handoff_pack.md`
- read_ok: `codex_log/reference_audit/文案对标_20260524_215056/12_chatgpt_handoff_pack.md`
- read_ok: `codex_log/20260524_copy_granularity_mixture_mechanism.md`
- read_ok: `codex_source/13_execution_lane_and_parallel_rules.md`
- read_ok: `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- read_ok: `codex_source/19_project_state_action_router.md`
- read_ok: `codex_source/21_codex_judgment_permission_matrix.md`
- read_ok: `codex_log/current_data_goal_anchor.md`
- read_ok: `skills/视频素材解析_video_material_audit/SKILL.md`
- read_ok: `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md`
- read_ok: `/Users/fan/.codex/skills/copywriting-cn/SKILL.md`
- read_ok: `/Users/fan/.codex/skills/storyboard-cn/SKILL.md`

## 5. line_group 总结
- line_group_count = 21
- smooth_line_count = 3
- material_granularity_line_count = 9
- judgment_boundary_line_count = 8
- result_transition_line_count = 4
- paragraph_level_mapping_insufficient = false

## 6. 关键素材映射
- V001: 商品卡浏览、字段分散、选品页动作和 AI 分析窗口。
- V003: Google Drive 文件、候选方向表、商品明细表。
- V004: 3 个更窄方向、4 个复查商品、优先级复查表。
- V002: 弱证据，不建议入正片。

## 7. copy_change_request 摘要
- LG007: “直接操作电脑”需视补录情况降级为“先跑初筛/整理信息”。
- LG004: SKU 复杂如果无画面，只能作为待核风险。
- LG014 / LG017: “最值得”必须保留“先复查”口径。
- LG003 / LG005: 成本、转化、售后只能写可能性和风险维度。
- LG016: Drive / 云盘必须遮挡账号、路径、文件名。
- LG021: 结尾动作建议保留低压个人流程语气。

## 8. 隐私 / 可读性风险
- 商品名、搜索词、价格、佣金、月销、评分默认不公开读死。
- Google Drive 账号、路径、文件名必须遮挡。
- V003 / V004 表格小字必须局部放大，正式成片建议补录 R001 / R003。

## 9. 状态边界
- content_validation = not_advanced
- send_ready = false
- video_generated = false
- audio_generated = false
- media_committed = false
- formal_video_execution_ready = false

## 10. 验证结果
- file_exists_check = passed；13 个 required output files 均存在
- json_parse_check = passed；`02_script_to_timeline_map.json`、`04_content_route_card_v2.json`、`06_tts_prosody_anchor_map.json`、`manifest.json` 均可解析
- line_group_count_check = passed；line_group_count = 21，满足 18-26 个句组要求
- material_timecode_check = passed；所有 `material_granularity_line` 均绑定素材时间码
- judgment_boundary_check = passed；所有 `judgment_boundary_line` 均有边界说明
- media_commit_check = passed；本轮输出目录未生成视频、音频、图片或 contact sheet
- secret_scan = passed_for_new_outputs；历史 `latest.md` 中存在旧 secret-policy 字样，本轮新增 diff 未写入 secret 值
- latest_top_check = passed；`codex_log/latest.md` 顶部已新增本轮记录
- git_diff_check = passed；限定本轮路径执行 `git diff --check` 未发现空白错误

## 11. commit / push 信息
- commit_message = Prepare line-group timeline map for new fourth episode
- commit_sha = pending_git_commit
- pushed_to_main = pending_git_push
