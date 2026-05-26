# remaining_blockers

blocked_type: blocked_publish_candidate_unavailable
blocked_reason: 核心证据句无素材支撑/需要猜测，表格证据可读性未通过，MiniMax 全片旁白未生成，preflight suite 不能全通过。
affected_line_groups: see `line_visual_alignment_report.json`
missing_material_needed:
- R001 Codex/computer-use 连续操作录屏：进入选品页面、输入品类词、逐张翻商品卡。
- R002 商品卡字段高清近景：价格、佣金、销量、店铺分、商品分、退货风险。
- R003 候选表/明细表高清近景或静态图。
- R004 复查表高清近景或静态图，含四个复查对象和下一步核验项。
- R005 SKU/规格复杂度证据，或由用户确认改稿。
can_user_fix_by_recording_video_or_image: true
recommended_next_material_to_capture: R001-R005
tts_blocker: MiniMax route_b smoke generated audio but smoke report task_status=blocked; full narration.wav not generated because upstream gates blocked.
visual_blocker: direct Codex computer-operation claim and table/readability evidence are not candidate-ready.
copy_blocker: old preflight required copy_change_request; current locked copy forbids Codex edits.
no_degraded_output_created: true
