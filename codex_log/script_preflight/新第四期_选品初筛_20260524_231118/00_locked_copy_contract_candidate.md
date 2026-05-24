# 新第四期 locked_copy_contract_candidate

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


## 状态边界
- 本文件是 `locked_copy_contract_candidate（锁定文案契约候选）`，不是最终锁稿。
- `content_validation = not_advanced`
- `send_ready = false`
- `video_generated = false`
- `audio_generated = false`
- `formal_video_execution_ready = false`

## locked_topic_candidate
Codex / AI 参与精选联盟商品初筛：从手动翻商品卡，变成先把商品字段、风险、理由和下一步复查项整理成判断表。

## locked_title_candidate
我让 Codex 帮我跑了一轮选品初筛，最后它给我回了一张商品判断表

## locked_opening_line_candidate
朋友们，你有没有发现，现在做带货，最贵的已经不是拍一条视频了，而是你前面测错商品的成本。

## locked_final_script_candidate
- source = `draft_script_v0.2（用户本轮提供的新第四期长文案候选稿）`
- Codex action = 未重写核心语义，只做句组拆分、证据映射、风险标注和执行前置包。
- contract rule = 下一轮如要正式成片，必须先由 ChatGPT / 用户确认本包里的 `copy_change_request`，再把确认后的文案作为真正 `locked_final_script`。

## allowed_copy_changes
- 调整标点、换行、字幕分句、TTS 停顿。
- 将“直接操作电脑 / 最值得 / 过表再拍”等可能过满表达，按 `10_copy_change_request_if_any.md` 降级为更安全的经验句或复查句。
- 将长字段列举拆成 2-3 个字幕屏和信息卡。
- 把不可读的小字改为字段卡 / 判断卡表达，但不能伪造画面中没有的结论。

## forbidden_copy_changes
- 不得把本稿改写成“Codex 已经选出爆品”。
- 不得写“商品一定能卖”“佣金一定覆盖成本”“自动赚钱”“商业闭环已成立”。
- 不得写 Codex 自动点击确认、无人值守完整选品成功。
- 不得把复查对象写成最终拍摄对象。
- 不得公开未确认可公开的商品名、账号、路径、Google Drive 文件信息。

## copy_change_request_required_if_needed
如果正式成片前仍无法补录 R001/R003 或无法遮挡隐私，必须先处理 `10_copy_change_request_if_any.md`，不得硬剪。
