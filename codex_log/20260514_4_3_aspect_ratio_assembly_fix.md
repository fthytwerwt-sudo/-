# 20260514｜4:3 画面比例技术装配修正

## route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - video_sample_or_assembly
    - code_debug_or_config_change
  responsibility_layer:
    - execution_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: true
    reason: 本轮涉及当前视频对象、素材宽高验证、装配脚本、时间线配置、卡片 / 字幕安全区和日志同步
    lane_recommendation: audit_lane -> standard_lane after target and material locked
    parallel_recommendation: serial_only
  completion_relay_gate:
    triggered: true
    reason: 本轮不能只改比例参数，必须检查素材、画布、字幕、卡片、输出和日志
  execution_permission: allowed_after_current_target_and_4_3_material_verified
```

## state_action_router

```text
state_action_router:
  input_signal: 用户要求将当前画面比例调整为 4:3，并确认素材本身就是 4:3
  current_project_state:
    - video_assembly_ratio_fix_needed
    - content_route_needed
    - editing_inference_needed
  fact_source_arbitration:
    primary_source: 用户本轮明确指令 + GitHub main 当前机制文件 + 实际素材宽高读取结果
    conflict_detected:
      - 旧 9:16 竖屏模板与本轮 4:3 FocuSee 素材冲突
      - latest_review_pack 时间线中的旧正反录屏源路径当前缺失
    conflict_resolution:
      - 本轮不覆盖 latest_review_pack，不沿用 9:16 crop 坐标；锁定最新可读 FocuSee 4:3 素材做 4:3 本地技术装配验证
  inferred_state:
    - target_aspect_ratio_4_3
    - source_material_verified_as_4_3
    - old_vertical_layout_should_not_be_reused_directly
  confidence: high after material_probe_passed
  trigger_mechanism:
    - content_route_card V2
    - editing_inference_function
    - card_placement_decision
    - Completion Relay Gate
  selected_action:
    - 验证素材比例
    - 调整画布 / 装配比例为 4:3
    - 重排字幕安全区和卡片布局
    - 输出技术验证报告
  forbidden_action:
    - 不推进 content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked
    - 不修改原始素材
    - 不读取 secret
  done_when:
    - 当前目标对象锁定
    - 素材比例验证通过
    - 输出装配比例为 4:3
    - 字幕 / 卡片不压住主体证据
    - technical_validation 完成
  blocked_if:
    - 当前目标对象不明确
    - 素材路径不明确
    - 素材不是 4:3
    - 输出链路不支持 4:3 且无法最小修复
```

## actual_read_files

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_timeline.json`
- `dist/latest_review_pack/visual_route_map.json`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_log/current_local_artifact_paths.md`
- `scripts/元素娃娃线_round34_中段双展示提示卡_正反分段提示修复.py`
- `formal_api_demo_cloud_assembly.py`

## current_target_locked

- `已确认` 当前复审对象仍为《我用 AI 做 PPT 踩过的坑》v3.1 / `dist/latest_review_pack/`。
- `已确认` 本轮不覆盖 `dist/latest_review_pack/`，不改变 `publish_status`，不把 4:3 技术输出写成最新正式复审包。
- `发现` 当前 latest timeline 中旧正反录屏源文件路径已缺失；因此本轮不沿用旧 9:16 crop 坐标重剪旧片。

## source_material_probe

```text
path: /Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4
width: 2498
height: 1874
ratio: 1.332978
is_4_3: true
duration: 33.133333
fps: 30
```

## impact_check

- `已确认` 当前 `dist/latest_review_pack/full.mp4` 为 `720x1280`，旧复审包仍是 9:16，不作为本轮 4:3 源素材。
- `已确认` 旧 round34 脚本存在 `TARGET_WIDTH = 720` / `TARGET_HEIGHT = 1280` 和 9:16 卡片样式，属于历史 v3.1 链路，本轮不直接重写以免污染旧基线。
- `已确认` `formal_api_demo_cloud_assembly.py` 仍支持从配置读取 `assembly.resolution`，但云端路径涉及 OSS / 阿里云接口，本轮禁止调用外部 API，因此不走云剪验证。
- `已确认` 新增本地 4:3 技术装配路径，使用 `scale + pad` 保留源画面，不做默认二次 zoom / crop / 重新运镜。
- `已确认` 本轮输出不烧字幕、不插卡，后续正式执行再按 `content_route_card V2` 的 4:3 安全区放置字幕和卡片。

## changed_files

- `scripts/四比三装配验证_4_3_assembly_validation.py`
- `codex_log/latest.md`
- `codex_log/20260514_4_3_aspect_ratio_assembly_fix.md`
- `dist/20260514_4_3_aspect_ratio_assembly_fix/4_3_assembly_validation_preview.mp4`（本地技术验证输出，dist 目录被 Git 忽略）
- `dist/20260514_4_3_aspect_ratio_assembly_fix/content_route_card_v2.json`（本地输出，dist 目录被 Git 忽略）
- `dist/20260514_4_3_aspect_ratio_assembly_fix/assembly_summary.json`（本地输出，dist 目录被 Git 忽略）

## content_route_card_v2_summary

- `target_aspect_ratio`: `4:3`
- `source_material_aspect_ratio`: `2498x1874`, ratio `1.332978`, `is_4_3 = true`
- `selected_opening_route`: `screen_first_opening`
- `middle_carrier`: `用户录制素材`
- `focusee_middle_editing_decision`: `recording_layer_motion_baked_in = true`, `no_secondary_zoom_by_default = true`
- `card_placement_decision`: 本轮技术验证不插总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡；后续正式内容执行按 4:3 安全区判断
- `subtitle_safe_area`: 1440x1080 输出下建议字幕控制在底部安全区，最多 2 行，不压主体证据

## output_validation

```text
output_path: /Users/fan/Documents/视频工厂/dist/20260514_4_3_aspect_ratio_assembly_fix/4_3_assembly_validation_preview.mp4
output_width: 1440
output_height: 1080
output_ratio: 1.333333
is_4_3: true
duration: 33.166667
fps: 30
```

## subtitle_and_card_safe_area_check

- `已确认` 本轮技术验证输出未烧字幕，因此没有字幕遮挡证据窗口。
- `已确认` 本轮技术验证输出未插总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡，因此没有卡片抢真实录屏证据。
- `已写入` V2 卡片安全区建议：4:3 输出后续插卡需避开左右 `96px`、上下 `72px`，字幕建议控制在 `y=876-1008` 的底部安全区。

## forbidden_status_check

- `content_validation`: 未推进，仍不得写成 `passed`
- `send_ready`: 未推进，仍不得写成 `true`
- `publish_status`: 未修改
- `voice_validation`: 未修改
- `final_voice_validated`: 未修改
- `visual_master_locked`: 未修改
- `.env` / `.env.swp` / API key / token / secret: 未读取
- DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API: 未调用
- 用户原始 FocuSee 素材: 未修改

## remaining_work_check

- `无剩余 must-fix`：4:3 素材 probe、4:3 输出、V2 卡、字幕 / 卡片安全区记录、日志同步均已完成。
- `待验证`：真实内容执行效果、最终文案时间码、开头选择、正式卡片位置仍待下一轮内容执行验证。

## sync_back_check

- `已同步`：`codex_log/latest.md`
- `已新增`：`codex_log/20260514_4_3_aspect_ratio_assembly_fix.md`
- `已输出`：`dist/20260514_4_3_aspect_ratio_assembly_fix/content_route_card_v2.json`
- `未同步到 latest_review_pack`：本轮不覆盖当前正式复审包，避免把技术验证输出误写成发布包。

## next_target

下一轮真实内容执行时，用最终文案时间码把 4:3 FocuSee 素材切成正式段落，并按 4:3 安全区重新判断开头、字幕、卡片和证据窗口。
