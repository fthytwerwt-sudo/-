# 20260618 V006 Human Review Minimum Loop Report

```yaml
report_type（报告类型）: V006_human_review_minimum_loop（V006 人审最小闭环）
task_result.status（任务结果状态）: V006_human_review_minimum_loop_completed（V006 人审最小闭环已完成）
project_route（项目路由）: video_factory（视频工厂）
selected_path（已选择路径）: continue_V006_human_review（继续 V006 人审）
not_selected_path（未选择路径）: start_new_video_task（启动下一条新视频）
candidate_created（是否生成候选）: false（未生成）
new_video_started（是否启动新视频）: false（未启动）
human_review_ready（是否可进入人审）: true（可以进入用户 / ChatGPT 人审）
send_ready（可发送状态）: false（未开启）
content_validation（内容验证）: pending_user_chatgpt_review（等待用户 / ChatGPT 复审）
production_readiness（生产可用状态）: not_claimed（未声称）
runtime_enabled（运行时启用）: false（未启用）
service_started（服务启动）: false（未启动）
external_api_called（外部 API 调用）: false（未调用）
tts_called（TTS 调用）: false（未调用）
dashvector_real_call（DashVector 真实调用）: false（未调用）
chroma_ingestion_run（Chroma 入库）: false（未运行）
media_generated（媒体生成）: false（未生成）
```

## 1. Minimum Loop Path Decision（最小闭环路径判断）

```yaml
minimum_loop_path_decision（最小闭环路径判断）:
  selected_path（已选择路径）: continue_V006_human_review（继续 V006 人审）
  not_selected_path（未选择路径）: start_new_video_task（启动下一条新视频）
  reason（原因）: 用户要求先继续跑最小闭环，上一轮 4 个入口问题只记录，之后再和 ChatGPT 商议；本轮不启动下一条新视频。
  current_round_boundary（本轮边界）:
    - 不生成新视频。
    - 不改 V006 锁定文案语义。
    - 不改 V006 素材。
    - 不重新生成媒体。
    - 不推进 content_validation / send_ready / production_readiness。
```

## 2. V006 Human Review Input Inventory（V006 人审输入清单）

```yaml
V006_human_review_input_inventory（V006 人审输入清单）:
  candidate_video（候选片路径）:
    path（路径）: /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/full.mp4
    status（状态）: exists（存在）
    metadata（元数据）: 1920x1080, 290.993s, audio=true, codec=h264/aac
  narration_audio（口播音频）:
    path（路径）: /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/narration.wav
    status（状态）: exists_non_silent（存在且非静音）
  captions（字幕）:
    path（路径）: /Users/fan/Documents/视频工厂/dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/captions.srt
    status（状态）: exists（存在）
  review_manifest（复审清单）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/review_manifest.md
    status（状态）: exists（存在）
  summary（摘要）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/summary.json
    status（状态）: exists（存在）
  locked_copy_contract（锁定文案契约）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/locked_copy_contract.md
    status（状态）: exists_locked_copy_changed_false（存在，且 locked_copy_changed=false）
  material_inventory（素材清单）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/material_inventory.json
    status（状态）: exists_new_material_used_true_old_material_reused_false（存在，新素材使用，旧素材未复用）
  script_to_timeline_map（脚本到时间线映射）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/script_to_timeline_map.json
    status（状态）: exists_38_line_groups（存在，38 个 line_group）
  gpt_icon_exposure_check（GPT 图标暴露检查）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/gpt_icon_exposure_check.md
    status（状态）: passed_for_human_review（已通过本地抽帧检查，仍需人审全片）
  privacy_platform_risk_report（隐私平台风险报告）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/privacy_platform_risk_report.md
    status（状态）: passed_with_human_review_required（通过但仍需人审小字 / 路径 / 平台风险）
  publish_candidate_preflight_report（可发布候选执行前检查报告）:
    path（路径）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/publish_candidate_preflight_report.md
    status（状态）: publish_candidate_ready_for_human_review（可进入人审）
  current_content_validation（当前内容验证）: pending_user_chatgpt_review（等待用户 / ChatGPT 复审）
  current_send_ready（当前可发送状态）: false（未开启）
  remaining_human_review_items（剩余人审项）:
    - overall viewing rhythm（全片观看节奏）
    - small source text readability（小字可读性）
    - remaining card visual deviation（卡片视觉风格偏差）
    - partial project-relative path visibility（局部项目相对路径可见）
    - final platform-risk watch-through（最终平台风险全片观看）
```

## 3. V006 Status Check（V006 状态检查）

```yaml
V006_status_check（V006 状态检查）:
  candidate_exists（候选是否存在）: true（存在）
  can_be_claimed_as_new_output（能否写成本轮新产出）: false（不能）
  current_status（当前状态）: publish_candidate_ready_for_human_review（可发布候选片，待人工复审）
  content_validation（内容验证）: pending_user_chatgpt_review（等待用户 / ChatGPT 复审）
  send_ready（可发送状态）: false（未开启）
  voice_validation（声音验证）: pending_user_chatgpt_review / not_advanced（等待复审，未推进）
  final_voice_validated（最终声音验证）: false（未验证）
  visual_master_locked（视觉母版锁定）: false（未锁定）
  remaining_blockers（剩余阻断项）:
    - 用户 / ChatGPT 尚未完成最终内容复审。
    - 用户 / ChatGPT 尚未确认声音是否可接受。
    - 报告 / 复盘画面小字可读性仍需人审。
    - 卡片视觉风格仍有 deviation（偏差），需判断是否可接受。
    - 局部项目相对路径可见，需最终平台风险确认。
```

## 4. Human Review Checklist（人审需要看什么）

```yaml
human_review_checklist（人审清单）:
  must_watch（必须观看）:
    - item（项目）: full_video_watch_through（全片通看）
      focus（重点）: 节奏是否顺、是否像可发布作品、是否存在主观不适。
      file（文件）: dist/V006_codex_real_use_rant_publish_candidate_no_gpt_icon_20260607_172300/full.mp4
    - item（项目）: opening_platform_risk（开场平台风险）
      focus（重点）: 00:00-00:20 是否仍有平台图标、浏览器标识、安装 / 下载 / 绕过使用风险。
      source（来源）: review_manifest.md + gpt_icon_exposure_check.md
    - item（项目）: chopper_case_claim_boundary（切菜器案例表达边界）
      focus（重点）: 01:12-01:45 是否只表达失败 / 候选 / 拆解，不误导成成功案例。
      source（来源）: review_manifest.md + locked_copy_contract.md
    - item（项目）: dense_text_readability（密集文字可读性）
      focus（重点）: 02:40-03:55 报告 / 工作流画面小字是否可读，是否影响观感。
      source（来源）: visual_evidence_readability_preflight.md
    - item（项目）: subtitle_card_overlap（字幕卡片遮挡）
      focus（重点）: 字幕、卡片、画面 OCR 和关键证据区域是否互相抢位置。
      source（来源）: subtitle_card_overlap_check.md
    - item（项目）: voice_feel_review（声音听感复审）
      focus（重点）: 复用的 MiniMax narration 是否适合发布，语气、停顿、情绪是否能接受。
      source（来源）: summary.json + publish_candidate_preflight_report.md
  minimum_user_chatgpt_decisions（用户 / ChatGPT 最少需要判断）:
    - V006 是否作为候选片继续推进人审。
    - V006 目前的卡片视觉偏差是否可接受。
    - 小字可读性和项目路径可见是否可接受。
    - 声音是否可接受。
    - 是否允许进入下一轮 send_ready 判断；本轮 Codex 不自动推进。
```

## 5. Codex Auto Checked（Codex 已自动检查）

```yaml
codex_auto_checked（Codex 已自动检查）:
  file_existence（文件存在性）: passed（候选片、音频、字幕、复审清单、summary、锁定文案、素材清单、时间线和风险报告均存在）
  metadata（媒体元数据）: passed（1920x1080, 290.993s, audio=true）
  locked_copy_diff（锁定文案差异）: passed_no_semantic_change（未发现语义改写）
  material_inventory（素材清单）: passed_new_material_used_old_material_not_reused（使用新素材，未复用旧素材）
  line_group_map（脚本时间线映射）: exists_38_line_groups（存在 38 个 line_group）
  gpt_icon_exposure（GPT 图标暴露）: passed_final_sampled_frames_no_gpt_chatgpt_openai_icon_or_favicon_detected（抽帧未见相关图标）
  privacy_platform_risk（隐私平台风险）: passed_no_secret_or_token_visible_project_paths_partial_human_review_required（未见密钥，局部路径需人审）
  subtitle_card_overlap（字幕卡片遮挡）: passed_no_high_severity_overlap_detected_by_layout（未见高严重遮挡）
  completion_truth（完成真实性）: passed_for_human_review_ready（人审准备状态通过）
```

## 6. Codex Cannot Decide（Codex 不能替用户判断什么）

```yaml
codex_cannot_decide（Codex 不能替用户判断）:
  - 内容是否最终过线。
  - 声音是否符合用户主观口味。
  - 卡片视觉偏差是否可接受。
  - 小字密集画面是否影响发布体验。
  - 局部项目相对路径可见是否会影响平台风险判断。
  - 是否可以把 send_ready 改为 true。
```

## 7. Why Send Ready Cannot Auto Promote（为什么不能自动推进 send_ready）

```yaml
send_ready_guard_check（可发送状态护栏检查）:
  send_ready_current（当前 send_ready）: false（未开启）
  send_ready_auto_promotion_allowed（是否允许自动推进）: false（不允许）
  reason（原因）:
    - V006 仍是 publish_candidate_ready_for_human_review，不是最终可发送。
    - content_validation 仍等待用户 / ChatGPT 复审。
    - voice_validation 尚未用户确认。
    - remaining_card_visual_deviation 仍为 true。
    - 小字可读性与局部路径可见仍需人审。
  blocked_if_auto_promoted（如果自动推进会造成什么问题）:
    - 技术候选会被误写成内容通过。
    - 人审未完成会被误写成可发送。
    - 平台风险和审美风险会被跳过。
```

## 8. Backlog Record（4 个入口问题待商议记录）

```yaml
project_adjustment_backlog（项目调整待办）:
  status（状态）: recorded_only_pending_user_chatgpt_discussion（仅记录，等待用户 / ChatGPT 商议）
  current_round_action（本轮动作）: record_only_do_not_fix（只记录，不修复）
  items（事项）:
    - item（事项）: current_task_selector（当前任务选择器）
      problem（问题）: 需要把“继续既有候选人审”和“启动下一条新视频”拆成显式选择。
      why_affects_minimum_loop（为什么影响最小闭环）: 不拆开会导致 V006 人审和新视频生成混线。
      why_not_fix_this_round（本轮为什么不修）: 用户明确要求本轮只继续 V006 人审，不修入口问题。
      later_decision_needed（之后需要决定）: ChatGPT / 用户确认任务选择器字段和入口顺序。
    - item（事项）: prewrite_copy_decision_card（写前文案决策卡）
      problem（问题）: 新视频进入候选前必须有目标、标题、核心判断、允许改动和禁止改动。
      why_affects_minimum_loop（为什么影响最小闭环）: 缺卡会让 Codex 不知道哪些文案可改、哪些不可改。
      why_not_fix_this_round（本轮为什么不修）: 本轮不启动新视频，不需要建立新文案入口。
      later_decision_needed（之后需要决定）: ChatGPT / 用户确认写前卡字段和何时触发。
    - item（事项）: material_binding_card（素材绑定卡）
      problem（问题）: 素材必须绑定当前任务，不能默认继承旧候选素材。
      why_affects_minimum_loop（为什么影响最小闭环）: 不绑定会让旧素材、旧候选和新任务证据混淆。
      why_not_fix_this_round（本轮为什么不修）: 本轮只复审 V006 既有素材使用结果，不启动新素材绑定机制。
      later_decision_needed（之后需要决定）: ChatGPT / 用户确认素材绑定卡字段与旧素材复用规则。
    - item（事项）: authorization_card（授权卡）
      problem（问题）: 真实 RAG、TTS、外部 API、媒体生成必须逐项写明 allowed / forbidden。
      why_affects_minimum_loop（为什么影响最小闭环）: 授权不清会导致 Codex 误启外部调用或误写产出能力。
      why_not_fix_this_round（本轮为什么不修）: 本轮不调用外部 API、不启 TTS、不真实调用 RAG、不生成媒体。
      later_decision_needed（之后需要决定）: ChatGPT / 用户确认授权卡的默认 false 规则和显式授权格式。
```

## 9. Validation Plan（验证计划）

```yaml
validation_plan（验证计划）:
  git_diff_check（Git 差异检查）: passed（通过）
  forbidden_status_promotion_scan（禁止状态推进扫描）: passed（通过）
  secret_scan（密钥扫描）: passed（通过）
  media_file_unchanged_check（媒体文件未改检查）: passed（通过，dist/V006 目录无 Git 变更）
  locked_copy_semantic_unchanged_check（锁定文案语义未改检查）: passed（通过，locked_copy_contract.md 未改且哈希一致）
  material_inventory_unchanged_check（素材清单未改检查）: passed（通过，material_inventory.json 未改且哈希一致）
  new_python_script_py_compile（新增 Python 脚本编译）: not_applicable（本轮没有新增 Python 脚本）
```

```yaml
validation_evidence（验证证据）:
  git_diff_check（Git 差异检查）: git diff --check exited 0（退出码 0）
  forbidden_status_promotion_scan（禁止状态推进扫描）: no_hits（无命中）
  secret_scan（密钥扫描）: no_hits_in_added_lines（新增行无命中）
  media_file_hashes（媒体文件哈希）:
    full_mp4_sha256（full.mp4 哈希）: 89bd6fa781fadc6c0432c1d9f346198eecce2568aade1185516dac0c6a43b08f
    narration_wav_sha256（narration.wav 哈希）: 66387c4d0d3bc57511e992b534caf1a7e41a8a960a4b762bf2740549b660118d
    captions_srt_sha256（captions.srt 哈希）: 60580c9339bd123bee50eed57f36363bd4dc39d6c516e01260974a1425648541
    locked_copy_contract_sha256（锁定文案契约哈希）: b257e0dc9dc9110b584d1eb766dd077205d3c7ddfdf4372044902b42613c52fc
    material_inventory_sha256（素材清单哈希）: 72bca166e9206082260492990bc80e9ef847d0b5d6deb4e3665cb7d7f137012b
```

## 10. Status Not Promoted（未推进状态）

```yaml
status_not_promoted（未推进状态）:
  runtime_enabled（运行时启用）: false（未启用）
  service_started（服务启动）: false（未启动）
  external_api_called（外部 API 调用）: false（未调用）
  tts_called（TTS 调用）: false（未调用）
  dashvector_real_call（DashVector 真实调用）: false（未调用）
  chroma_ingestion_run（Chroma 入库）: false（未运行）
  media_generated（媒体生成）: false（未生成）
  content_validation（内容验证）: pending_user_chatgpt_review_not_promoted（等待复审，未推进）
  send_ready（可发送状态）: false（未开启）
  production_readiness（生产可用状态）: not_claimed（未声称）
```
