# 剪辑参考视频解析报告 Editing Reference Parse Report

## 0. status_boundary（状态边界）

- `task_result.status = reference_analysis_completed_with_decode_warning`
- `target_delivery = editing_reference_contract + reference_style_parse_report + editing_decision_pack_vNext_draft`
- `已确认` 本轮只解析用户提供的剪辑参考视频，不生成新成片、不修改当前正片、不调用视频 / 图片 / TTS / 外部付费 API。
- `已确认` 本轮未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `部分成立` 参考视频可用于视觉 / 剪辑机制分析：`ffprobe` 可读、抽帧成功、关键画面可观察。
- `待验证` 该参考机制能否稳定迁移到《视频工厂》真实下一条视频，仍需后续以真实 `locked_copy_contract / material_parse_pack / script_to_timeline_map` 跑一次最小片段验证。
- `注意` `video-metadata-probe` 的严格解码检查为 `failed`，原因是 ffmpeg 报告 `non monotonically increasing dts`。本轮只把该文件作为 reference 视觉样本，不把它写成可交付媒体源或技术验证通过。

## 1. route_decision（路由判断）

```yaml
route_decision:
  repository: /Users/fan/Documents/视频工厂
  current_branch: codex/daily-tutorial-editing-profile
  project: 视频工厂
  project_route: video_factory
  task_type:
    - review_diagnosis_audit
    - video_sample_or_assembly_related_readonly_reference_analysis
    - project_file_change_report_and_log_only
  responsibility_layer:
    - entry_routing_layer
    - project_judgment_layer
    - execution_layer
    - validation_layer
    - sync_layer
  status: allowed_to_analyze_reference_and_write_report_only
  blocked_if:
    - reference_folder_missing
    - no_readable_video_file
    - ffprobe_unreadable
    - frame_sampling_failed
    - key_effects_not_observable
    - need_external_api
    - need_secret
    - attempt_to_modify_current_video
```

## 2. large_task_gate（大任务闸门）

```yaml
large_task_gate:
  triggered: true
  reason:
    - reference video duration is 416.740114s, longer than 180s
    - task touches reference, material scanning, timeline parsing, frame sampling, report, log, and git closure
    - multiple repository files are checked and updated
  lane_recommendation: audit_lane_to_standard_lane
  lane_reason: first validate reference availability and project boundaries, then write bounded report/log artifacts
  lane_invalid_if:
    - source video cannot be sampled
    - reference effects are not observable
    - writing scope expands into core mechanism files or media outputs
  parallel_recommendation: explore_plus_integrate
  parallel_reason: independent reads/probes can run in parallel, but report/log writes must be single-owner
  parallel_invalid_if:
    - multiple writers touch the same report/log/core file
    - source decode issue changes the task from analysis to repair
  write_owner: Codex integrator
  read_only_lanes:
    - required file reads
    - video metadata probe
    - frame extraction / visual inspection
  integration_owner: Codex integrator
```

## 3. workflow_route_decision（工作流归位判断）

```yaml
workflow_route_decision:
  workflow_type:
    - aesthetic_editing_flow
    - material_evidence_flow
    - quality_review_flow
  reason: user provided a cutting/style reference and asked Codex to parse editing mechanism, not produce a finished video
  must_read:
    - AGENTS.md
    - codex_source/00_codex_readme.md
    - codex_log/latest.md
    - GPT数据源/00_项目总述.md
    - GPT数据源/01_项目系统提示词.md
    - GPT数据源/03_总索引与阅读顺序.md
    - GPT数据源/08_当前正式事实.md
    - GPT数据源/10_OPC一人公司闭环与多AI协作机制.md
    - GPT数据源/11_项目状态动作总控器_机制推理层.md
    - GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md
    - GPT数据源/05_文案路由规则.md
    - GPT数据源/07_AI知识类视频价值规则.md
    - codex_source/19_project_state_action_router.md
    - codex_source/20_reference_to_execution_contract.md
    - codex_source/13_execution_lane_and_parallel_rules.md
    - project_source/20_codex_multi_agent_routing_note_for_gpt_project.md
  required_handoff:
    - reference_to_execution_contract
    - reference_timeline_parse
    - editing_style_parse_report
    - editing_decision_pack_vNext_draft
  forbidden_status:
    - content_validation
    - send_ready
    - publish_status
    - voice_validation
    - final_voice_validated
    - visual_master_locked
  blocked_if:
    - only_style_words_without_function_fields
    - reference_key_effects_not_observable
    - strict_decode_failure_treated_as_delivery_pass
```

## 4. state_action_router（项目状态动作总控器）

```yaml
state_action_router:
  input_signal: user supplied a Codex execution prompt to parse editing reference video in 素材录制/剪辑参考
  current_project_state:
    - formal_operation_active
    - reference_contract_needed
    - editing_inference_needed
    - material_audit_needed
  fact_source_arbitration:
    primary_source:
      - AGENTS.md
      - GPT数据源/
      - codex_source/
      - codex_log/latest.md
    secondary_sources:
      - user attached execution prompt
      - local reference video
    conflict_detected: true
    conflict_resolution: the attached prompt requests analysis only and forbids external APIs, so DeepSeek is marked fallback_local_only instead of called
  inferred_state: reference analysis allowed, media delivery forbidden
  confidence: high
  trigger_mechanism:
    - Reference-to-Execution Contract
    - editing_inference_function
    - large_task_gate
    - Completion Relay Gate
  selected_action: parse reference video, extract frames, write report and logs, do not edit current video
  forbidden_action:
    - generate new finished video
    - call video/image/TTS/external paid APIs
    - read secrets
    - copy third-party identifiable assets
    - promote delivery/content states
  done_when:
    - reference_source_inventory complete
    - reference_to_execution_contract complete
    - timeline parse complete
    - style parse complete
    - vNext editing decision draft complete
    - latest and dated log updated if repository files changed
  blocked_if:
    - reference missing
    - key visual mechanisms unobservable
    - only subjective adjectives can be produced
  feedback_update_required: true
```

## 5. deepseek_supply_gate（DeepSeek 供料闸门）

```yaml
deepseek_supply_gate:
  supply_request: codex_log/supply_requests/20260530_editing_reference_parse_pre_supply_request.json
  deepseek_actual_participation: not_attempted_policy_constraint
  fallback_status: fallback_local_only
  not_deepseek_conclusion: true
  token_usage_expectation_check: no_token_decrement_expected_because_external_api_forbidden
  reason: 本轮执行单禁止调用任何外部付费 API；因此只创建任务卡并以本地只读分析完成。
```

## 6. read_status（实际读取文件）

| file | read_status | purpose |
| --- | --- | --- |
| `AGENTS.md` | `read_ok` | 项目路由、单工作区、禁止状态推进、Git 收口规则 |
| `codex_source/00_codex_readme.md` | `read_ok` | 正式运营交付边界、no-degrade、reference/视频执行入口 |
| `codex_log/latest.md` | `read_ok` | 当前最近机制状态、素材解析复用标准、剪辑参数包状态 |
| `GPT数据源/00_项目总述.md` | `read_ok` | OPC 身份、主线、reference 锁质量机制 |
| `GPT数据源/01_项目系统提示词.md` | `read_ok` | Reference contract、DeepSeek、视频执行禁止降级规则 |
| `GPT数据源/03_总索引与阅读顺序.md` | `read_ok` | 必读顺序、reference/DeepSeek/数据目标入口 |
| `GPT数据源/08_当前正式事实.md` | `read_ok` | 正式事实、状态边界、不能推进的字段 |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | `read_ok` | OPC 分工、reference-to-execution 角色边界 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `read_ok` | state_action_router、editing_inference_function、DeepSeek fallback 边界 |
| `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` | `read_ok` | contract 字段与 done_when |
| `GPT数据源/05_文案路由规则.md` | `read_ok` | 真实录屏证据、卡片/字幕/素材证据保护 |
| `GPT数据源/07_AI知识类视频价值规则.md` | `read_ok` | 证据可读性、人感质量、publish_candidate 边界 |
| `codex_source/19_project_state_action_router.md` | `read_ok` | Codex 执行侧 router 与 reference/editing 动作 |
| `codex_source/20_reference_to_execution_contract.md` | `read_ok` | Codex 执行侧 reference contract 禁止项 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | `read_ok` | large_task_gate lane/parallel 判断 |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | `read_ok` | GPT Project 侧 lane/parallel 与 DeepSeek 边界 |
| `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md` | `read_ok` | 本地视频元数据验证规则 |
| `/Users/fan/.codex/attachments/.../pasted-text.txt` | `read_ok` | 用户本轮 Codex 执行单 |

## 7. reference_source_inventory（参考素材清单）

```yaml
reference_source_inventory:
  folder_path: /Users/fan/Documents/视频工厂/素材录制/剪辑参考
  files_found:
    - file_path: /Users/fan/Documents/视频工厂/素材录制/剪辑参考/ScreenRecording_05-24-2026 21-12-50_1.MP4
      file_name: ScreenRecording_05-24-2026 21-12-50_1.MP4
      file_type: mp4
      duration: 416.740114s
      resolution: 1180x2556
      fps: 60.000
      video_codec: hevc
      audio_present: true
      audio_codec: aac
      readable: partial_readable_for_visual_analysis
      strict_decode: failed_non_monotonic_dts
  selected_reference_video: ScreenRecording_05-24-2026 21-12-50_1.MP4
  selection_reason: only readable video file in the folder and key frames were extractable
  blocked_if: no readable video file, ffprobe unreadable, frame extraction failed
```

## 8. reference_to_execution_contract（参考到执行契约）

```yaml
reference_to_execution_contract:
  reference_anchor:
    reference_id: editing_reference_screenrecording_20260524_211250
    reference_type:
      - editing_reference
      - visual_reference
      - quality_reference
    source_layer:
      - user_provided
    exact_reference_available: true
    reference_path_or_description: /Users/fan/Documents/视频工厂/素材录制/剪辑参考/ScreenRecording_05-24-2026 21-12-50_1.MP4
    must_preserve:
      - smoother_screen_recording_flow
      - split_screen_for_comparison_or_alternatives
      - screen_recording_as_framed_evidence_card
      - persistent_information_hierarchy_labels
      - talking_head_or_avatar_bridge_for_human_continuity
      - highlight_marks_that_point_to_evidence_instead_of_replacing_it
      - section_cards_that_reset_context_before dense evidence
    can_vary:
      - colors
      - exact timing
      - exact layout
      - exact presenter/avatar form
      - decorative elements
      - card copy
      - platform wrapper
    must_not_copy:
      - Douyin/TikTok platform UI
      - account identity / creator face / avatar
      - third_party_logo
      - exact font/template/sticker
      - identifiable stock/person footage
      - copyrighted visual assets
    fail_if_missing:
      - split_screen_mechanism_not_analyzed
      - screen_recording_presentation_not_analyzed
      - pacing_and_transition_not_analyzed
      - visual_polish_elements_not_analyzed
      - evidence_window_safety_not_analyzed
    blocked_if_reference_missing: true

  effect_targets:
    viewer_feeling: faster orientation, less hard-cut fatigue, clearer "where to look" guidance, more human continuity
    information_hierarchy: creator/host or section card sets context, framed screen/document carries evidence, colored labels highlight one decision at a time
    pacing: frequent but purposeful cuts; hard cuts feel softer because the same visual grammar repeats across sections
    visual_weight: central white evidence card/document dominates; small avatar/label layers are secondary
    evidence_clarity: highlights, tags and split screens should point to evidence, not cover it
    human_like_comfort: talking head / avatar returns between dense evidence segments so it does not feel like a document dump
    reference_quality_points:
      - repeated orange/green/yellow label grammar
      - picture-in-picture host continuity
      - dark matte background around white documents
      - before/after or option comparison via split panels
      - section reset cards before dense proof
    emotional_tone: urgent but organized, expert explanation with light creator presence
    not_allowed_effects:
      - unreadable tiny document text
      - over-dense stickers
      - platform UI copied into Video Factory output
      - decorative overlays stealing screen evidence
      - stock footage replacing real process evidence

  function_fields:
    input_signal: user asked Codex to parse editing reference video and explain smoother/better presentation mechanics
    evidence_role: quality/editing reference, not current project fact
    importance_type: must inherit mechanism, must not copy assets
    target_area:
      - editing
      - visual_layout
      - screen_recording_presentation
      - split_screen
      - transition
      - quality_review
    selected_action: produce editing_reference_contract, style parse report, and vNext decision draft
    action_reason: convert reference feelings into executable layout, pacing, hierarchy and validation fields before any real edit
    validation_rule: each proposed edit action must name use_when, do_not_use_when, required inputs, evidence safety rule and blocked_if
    blocked_if:
      - key evidence window would be covered
      - document text becomes unreadable
      - action only copies platform/account assets
      - effect cannot be mapped to Video Factory material
    fallback_action: keep as ChatGPT review brief; do not modify core mechanisms or videos
    feedback_update: write this report, dated log, latest summary and manifest

  execution_mapping:
    editing_task:
      require_editing_reference_contract: true
      validate_pacing: true
      validate_cut_points: true
      validate_evidence_windows: true
      validate_split_screen: true
      validate_zoom_crop_card_decisions: true

  deviation_check:
    differs_from_reference_where:
      - Video Factory must not copy platform wrapper, creator identity, exact fonts, or third-party footage
      - Video Factory should prefer source material readability over reference's sticker density
    acceptable_variation:
      - use project-native colors and HyperFrames card language
      - use horizontal or source-native layouts based on target video rules
      - replace creator PiP with approved API human / avatar / small guide card if needed
    unacceptable_deviation:
      - keeps only color/sticker look while losing evidence clarity
      - adds visual polish that covers real recording evidence
      - uses split screen where it does not clarify comparison
    repair_required: true if evidence window safety, label hierarchy or pacing bridge is missing in a future implementation
    cannot_compare_reason: none for visual mechanism; audio beat alignment not deeply analyzed because no transcript/audio beat extraction was requested
    human_review_required: true for aesthetic fit before writing core mechanism rules

  done_when:
    reference_anchor_locked: true
    effect_targets_filled: true
    function_fields_filled: true
    deviation_check_done: true
    user_goal_preserved: true
    no_forbidden_status_promotion: true
    remaining_deviation_list_empty_or_explained: true

  blocked_if:
    - reference_missing
    - effect_targets_missing
    - function_fields_missing
    - unable_to_compare_reference
    - key_effects_not_observable
```

## 9. reference_timeline_parse（参考时间线解析）

```yaml
video_profile:
  duration: 416.740114s
  resolution: 1180x2556
  fps: 60.000
  audio_present: true
sampled_frames:
  frame_output_dir: codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/frames_sample_5s
  sample_policy: one scaled frame every 5 seconds
  frame_count: 83
scene_change_frames:
  frame_output_dir: codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/scene_frames
  scene_threshold: gt(scene,0.22)
  scene_frame_count: 16
manual_keyframes:
  count: 17
  timestamps_seconds:
    - 0
    - 10
    - 35
    - 55
    - 70
    - 95
    - 120
    - 150
    - 180
    - 210
    - 240
    - 275
    - 305
    - 330
    - 360
    - 390
    - 410
contact_sheets:
  - codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/contact_sheet_5s.jpg
  - codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/keyframe_contact_sheet.jpg
```

### scene_segments（场景段落）

| segment_id | start_time | end_time | dominant_layout | screen_recording_role | split_screen_present | cards_or_labels_present | motion_type | transition_in/out | information_density | viewer_attention_target | notes |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01_hook_talking_head | 00:00 | 00:20 | talking head over purple/dark studio, large expressive text | none / creator context | false | large reaction text and small badge | talking head jump-cut | opens directly on presenter | medium | presenter face + hook words | Human presence sets urgency before evidence. |
| S02_document_quad_context | 00:20 | 00:35 | multi-panel document/screen collage | evidence preview | true | small labels and PiP avatar | hard cut with persistent platform frame | talking head -> collage | high | comparison of document/screen options | Split/mosaic introduces problem scope quickly. |
| S03_problem_reset_cards | 00:35 | 01:05 | dark reset cards with big title and option cards | none / framing | occasional side-by-side text panels | red/white/orange problem labels | hard cuts | collage -> reset card -> option card | medium | problem label and section text | Section cards make hard cuts feel organized. |
| S04_document_evidence_1 | 01:05 | 01:35 | white document card on dark matte, orange section label, green/yellow highlights, PiP host | main evidence | false | section label, side label, highlighted rows | subtle scroll/cut between document positions | reset card -> evidence card | high | highlighted document line | Reference compresses dense document into highlighted evidence zones. |
| S05_labelled_proof_sequence | 01:35 | 02:10 | document/table/card sequence with floating tags | main evidence | partial | red/yellow tags, captions, avatar | hard cut sequence | evidence -> evidence | high | tagged field / highlighted result | Repeated label grammar reduces "random screenshot" feeling. |
| S06_multi_input_split | 02:10 | 02:50 | split panels: screenshots, phone-like panels, PDF/scan labels, blue/yellow callouts | input/source comparison | true | strong green/yellow labels | hard cuts / panel replacement | document sequence -> split input card | high | input types and differences | This is the clearest split-screen mechanism: show source variants side by side. |
| S07_human_bridge | 02:50 | 03:25 | presenter returns, then B-roll/office/person footage | human continuity / emotional reset | false | small labels | talking head jump cut, B-roll cutaway | dense evidence -> human bridge | low-medium | presenter or human scene | Useful as pacing relief, but stock-like B-roll should not replace project evidence. |
| S08_document_evidence_2 | 03:25 | 04:35 | repeated white document cards, yellow highlights, PiP avatar | main evidence | false | orange section labels, yellow highlights, captions | hard cuts with consistent frame | bridge -> document | high | highlighted rows | Consistency makes dense screenshots feel like one guided walkthrough. |
| S09_problem_solution_example | 04:35 | 05:35 | talking head, document card, interview/stock footage, black problem card | example framing | partial | "问题二" style card, subtitles | hard cuts / reset cards | evidence -> example reset | medium | problem statement then example evidence | Good use of problem cards; risk is stock footage being too generic. |
| S10_final_evidence_and_summary | 05:35 | 06:56 | document highlight cards, phone/text cards, AI/neon/title and presenter return | final evidence + summary | partial | colored labels, CTA-like title cards | hard cuts, final talking head return | example -> final evidence -> outro | medium-high | final card / host / evidence highlight | Ending alternates evidence and human face so the video does not end as a document dump. |

## 10. editing_style_parse_report（剪辑风格解析报告）

### smoothness

```yaml
smoothness:
  observed_patterns:
    - hard cuts are frequent, but repeated layout grammar makes them feel intentional
    - presenter/host returns after dense evidence runs
    - section labels stay visually consistent across document-heavy parts
    - captions and small avatar/PiP bridge context between evidence cards
  why_it_feels_smooth:
    - each new screen answers "what am I looking at" immediately through label + highlight
    - the viewer never has to parse a raw screenshot from zero
    - dense document sections are broken by human or black reset cards
  transferable_rule:
    - before showing a dense screen recording or document, add a low-density context label or problem card
    - preserve one repeated grammar across all evidence windows: section label, highlight, caption, and safe PiP/guide layer
  not_transferable:
    - copying the platform wrapper, exact creator identity, or overly dense sticker style
```

### split_screen_design

```yaml
split_screen_design:
  observed_patterns:
    - side-by-side and multi-panel screens appear when comparing inputs, options, or before/after states
    - split panels are usually paired with bright labels, not left as raw screenshots
  layout_types:
    - side_by_side
    - picture_in_picture
    - stacked_layers
    - comparison_panel
    - floating_screen_recording
  when_used:
    - to compare multiple source documents/screens
    - to show alternative plans/options
    - to maintain human presence while evidence is central
  why_it_works:
    - split screen clarifies comparison, rather than serving as pure decoration
    - PiP host keeps human continuity while the screen evidence remains primary
  transferable_rule:
    - use split screen only when the viewer must compare two states, two inputs, or two results
    - label each panel with a decision role, not just a visual title
  risks:
    - too many panels make text unreadable
    - PiP or labels can cover the evidence window if not constrained
```

### screen_recording_presentation

```yaml
screen_recording_presentation:
  observed_patterns:
    - white document/screen cards sit on dark matte background
    - highlights and labels identify the active evidence zone
    - small avatar/PiP sits near edge and does not dominate the document
  recording_frame_style: framed_card_or_phone_like_panel_on_dark_matte
  background_layer: dark neutral platform/background, sometimes purple creator studio
  shadow_or_border: subtle card edge / contrast separation
  zoom_or_crop: cropped enough to center document, but many text areas remain small
  highlight_or_pointer: yellow highlights, green/yellow badges, orange section labels
  evidence_window_clarity: good for highlighted areas, weak for small unhighlighted text
  transferable_rule:
    - crop screen recording to the single active evidence zone
    - reserve highlight color for the exact line/field being discussed
    - keep decorative layers outside the evidence rectangle
  risks:
    - if Video Factory copies the dense document scale, key UI/OCR text may become unreadable
```

### transition_and_pacing

```yaml
transition_and_pacing:
  observed_patterns:
    - mostly hard cuts, softened by repeated layout system and section cards
    - short talking-head bridges reset attention
    - dense evidence blocks are followed by simpler cards or presenter shots
  cut_frequency: high, roughly every few seconds in sampled frames
  motion_bridge: presenter/PiP continuity, section labels, repeated dark background
  pause_or_hold: evidence cards appear to hold long enough for highlighted portions, not full-page reading
  beat_alignment_if_audio_present: audio stream exists, but beat/prosody was not deeply analyzed in this pass
  transferable_rule:
    - do not rely on fancy transitions; make hard cuts legible with repeated labels and purpose
    - hold on highlighted evidence long enough for one claim only
```

### visual_polish_elements

```yaml
visual_polish_elements:
  observed_elements:
    - dark_matte_background
    - rounded_or_card_like_screen_frame
    - drop_shadow_or_border_separation
    - floating_label
    - yellow_highlight
    - green_or_yellow_badge
    - orange_section_tag
    - picture_in_picture_avatar
    - caption_block
    - split_screen_divider
  role:
    - guide viewer attention
    - segment dense evidence
    - make documents feel intentionally designed rather than raw pasted screenshots
  transferable_rule:
    - use at most one section tag, one active highlight cluster, and one human/guide layer per evidence window
  forbidden_if:
    - covers key prompt/table/button/chat evidence
    - adds unverified data
    - makes text unreadable
    - copies third-party creator/platform design
```

### information_hierarchy

```yaml
information_hierarchy:
  main_focus: current evidence card, document line, comparison panel, or problem statement
  secondary_focus: host/PiP, section label, caption
  text_density: high in document sections; acceptable only because highlights narrow attention
  evidence_vs_decoration_balance: mostly evidence-led, but some late B-roll/stock-like shots are less transferable
  transferable_rule:
    - define one "active evidence window" before adding subtitles/cards/labels
    - all polish layers must answer "what should the viewer notice now"
```

### compatibility_with_video_factory

```yaml
compatibility_with_video_factory:
  can_apply_to:
    - user_recording_middle_segment
    - result_diff_card
    - prompt_tail_card
    - summary_card
    - opening_hook
    - before_after_comparison
    - screen_recording_middle_segment
  should_not_apply_to:
    - exact platform UI replication
    - third-party creator identity
    - stock-footage replacement for real process evidence
    - tiny unreadable full-document screenshots
  conflict_with_current_rules:
    - Video Factory must protect source-native evidence readability
    - HyperFrames/cards cannot replace user recording evidence
    - formal-operation video delivery still requires publish_candidate or blocked, not a style report
  required_new_fields:
    - active_evidence_window
    - comparison_reason
    - screen_recording_frame_style
    - label_role
    - split_screen_use_reason
    - decoration_density_level
    - evidence_window_safety_line
```

## 11. editing_decision_pack_vNext（下一版剪辑决策包草案）

```yaml
editing_decision_pack_vNext:
  source_reference: editing_reference_screenrecording_20260524_211250
  target_use_case:
    - screen_recording_middle_segment
    - split_screen_explanation
    - before_after_comparison
    - result_diff_explanation
    - card_transition
  editing_principles:
    - preserve_evidence_window
    - improve_visual_hierarchy
    - reduce_hard_cut_feeling
    - add_polish_without_covering_evidence
    - split_screen_only_when_it_clarifies_comparison

  candidate_edit_actions:
    - action_id: vnext_01_context_reset_card
      action_name: low_density_context_reset_before_dense_evidence
      use_when: next segment is a dense document, table, prompt, or screen recording that needs orientation
      do_not_use_when: it delays a clear process action or repeats an already clear label
      required_inputs:
        - line_group_goal
        - evidence_window
        - one_sentence_context_label
      implementation_hint: short black/dark card or small header strip before evidence
      validation_rule: viewer can name the problem/section before seeing dense evidence
      blocked_if: label changes locked copy meaning or introduces unverified claim

    - action_id: vnext_02_framed_screen_evidence
      action_name: framed_screen_recording_evidence_card
      use_when: user recording or screenshot has one active result/prompt/table area
      do_not_use_when: full-screen native context is necessary to prove the action
      required_inputs:
        - source_timecode
        - active_evidence_window
        - forbidden_visuals
      implementation_hint: crop to safe evidence window, place on neutral matte, keep labels outside content rectangle
      validation_rule: active evidence remains readable and unblocked
      blocked_if: crop hides context required for proof

    - action_id: vnext_03_split_compare
      action_name: split_screen_compare_only_when_needed
      use_when: before/after, option A/B, source/result, or two candidate states must be compared
      do_not_use_when: only one evidence stream is needed
      required_inputs:
        - comparison_reason
        - panel_labels
        - evidence_for_each_panel
      implementation_hint: two panels max by default; three only for very short label-based comparison
      validation_rule: split screen improves understanding versus sequential display
      blocked_if: any panel text becomes unreadable

    - action_id: vnext_04_human_bridge
      action_name: human_or_guide_bridge_between_dense_blocks
      use_when: two or more dense evidence cards appear back to back
      do_not_use_when: evidence chain would be interrupted before the claim resolves
      required_inputs:
        - bridge_sentence_or_card
        - segment_boundary
      implementation_hint: approved API human / small guide card / subtle PiP, not copied presenter identity
      validation_rule: bridge reduces document-dump feeling without covering evidence
      blocked_if: guide layer covers key UI/OCR or becomes main evidence

    - action_id: vnext_05_highlight_one_claim
      action_name: one_claim_one_highlight_cluster
      use_when: document/table/prompt contains too much text
      do_not_use_when: the whole context must be read by viewer
      required_inputs:
        - claim_text
        - evidence_line_or_field
      implementation_hint: one yellow highlight cluster + optional small label
      validation_rule: highlighted field directly supports current narration
      blocked_if: highlight points to only thematically related, not direct, evidence

  split_screen_rules:
    allowed_layouts:
      - side_by_side
      - comparison_panel
      - picture_in_picture_for_host_or_guide
      - stacked_layers_for_input_vs_output
    use_when:
      - comparison is the point
      - before/after state is needed
      - multiple input types must be contrasted
    not_allowed:
      - decorative split screen with no comparison purpose
      - more than three dense panels
      - PiP covering active evidence
    validation_rule: every panel must have a role label and readable active evidence

  screen_recording_frame_rules:
    frame_style: project-native clean frame, not copied platform UI
    background_style: neutral dark or project-approved card background
    shadow_border_rule: use separation only; no heavy bokeh/orb decoration
    highlight_rule: one active evidence highlight cluster per claim
    readability_rule: source UI text needed for proof must remain readable at target resolution
    forbidden_rule: no privacy mask, whiteout, black block, or card layer that destroys evidence readability

  transition_rules:
    allowed_transitions:
      - purposeful hard cut
      - context reset card
      - label continuity
      - brief human/guide bridge
    use_when:
      - moving between problem, evidence, comparison, conclusion
    not_allowed:
      - transition that hides action result
      - decorative motion that steals from evidence window
    validation_rule: viewer can tell why the next visual appears

  visual_polish_rules:
    allowed_elements:
      - section_label
      - active_highlight
      - small_badge
      - PiP_or_guide_layer
      - evidence_frame
      - caption_block
    max_density: one section label + one highlight cluster + one guide/PiP layer per evidence window
    evidence_safety_line: no polish layer may cover prompt/table/button/result/chat evidence
    not_allowed:
      - exact reference font/template/sticker
      - Douyin/TikTok UI replication
      - third-party identity/stock assets as proof

  review_checklist:
    - smoother_than_current_baseline: human review required
    - evidence_still_clear: must pass before real implementation
    - no_ppt_overload: card density must remain bounded
    - no_demo_feeling: must use real user recording or approved project visual layer
    - no_decoration_stealing_attention: mandatory check
    - split_screen_improves_understanding: mandatory check
```

## 12. repository_update_recommendation（仓库机制更新建议）

```yaml
repository_update_recommendation:
  should_update_repo_rules: false
  recommended_files:
    - path: codex_source/23_剪辑参数包与镜头选择标准_editing_profile_and_shot_selection_rules.md
      reason: later add optional fields for active_evidence_window, split_screen_use_reason, decoration_density_level
      update_type:
        - add_editing_decision_fields
        - add_split_screen_rules
        - add_screen_recording_presentation_rules
    - path: GPT数据源/05_文案路由规则.md
      reason: later reference this as a possible implementation grammar only after user/ChatGPT review
      update_type:
        - add_review_checklist
  must_not_update:
    - AGENTS.md
    - dist/latest_review_pack
    - current_publish_target
    - content_validation/send_ready/publish_status/voice_validation/visual_master_locked
  why_not_directly_modify_now:
    - this is one reference analysis pass, not a proven stable mechanism
    - strict decode warning means the source is not a clean technical validation asset
    - user/ChatGPT still needs aesthetic confirmation before core mechanism writes
```

## 13. validation（验证）

```yaml
validation:
  ffprobe:
    status: passed
    evidence: metadata read as HEVC 1180x2556, 416.740114s, about 60fps, AAC stereo audio
  strict_decode:
    status: failed
    evidence: ffmpeg reported non monotonically increasing dts; do not treat source as technically clean delivery media
  frame_sampling:
    status: passed
    evidence:
      - 83 frames sampled at 5s interval
      - 16 scene-change frames extracted
      - 17 manual keyframes extracted
      - contact sheets generated
  reference_contract_validation:
    reference_anchor_exists: true
    effect_targets_exists: true
    function_fields_exists: true
    deviation_check_exists: true
    done_when_exists: true
  no_forbidden_status_promotion: true
  no_api_or_secret_used: true
  generated_video: false
  generated_audio: false
  current_video_modified: false
```

## 14. required_output_inventory（必须交付清单）

| item | status |
| --- | --- |
| `route_decision` | `done` |
| `large_task_gate` | `done` |
| `workflow_route_decision` | `done` |
| `state_action_router` | `done` |
| `deepseek_supply_gate` | `done_fallback_local_only` |
| `reference_source_inventory` | `done` |
| `reference_to_execution_contract` | `done` |
| `reference_timeline_parse` | `done` |
| `editing_style_parse_report` | `done` |
| `editing_decision_pack_vNext` | `done_draft_only` |
| `repository_update_recommendation` | `done_no_core_update` |
| `dated_log` | `done` |
| `latest_update` | `done` |
| `git_commit_push_remote_verify` | `pending_at_report_write_time` |

## 15. remaining_work_check（剩余工作检查）

- `已确认` 本轮 reference analysis artifact 已完整。
- `已确认` 本轮没有生成可发布候选片，不需要 `publish_candidate_preflight_suite`。
- `待验证` 如果下一轮要真正改当前视频，必须重新进入视频执行链：`locked_copy_contract -> material_parse_pack -> script_to_timeline_map -> editing_decision_pack -> subtitle/card overlap check -> review pack`。
- `待验证` 严格解码失败源于 DTS 时间戳问题，后续若要把该 MP4 作为可复用素材源，需要先转码/重封装并重新跑 metadata validation；本轮不做该处理。
- `待验证` 本报告提出的 split-screen / screen-frame / highlight grammar 需要用户或 ChatGPT 审美确认后，才能写入核心规则文件。

## 16. next_handoff_to_chatgpt（交给 ChatGPT 的下一步）

最值得看 3 个剪辑机制：

1. `context_reset_card + evidence_card`：先用低密度问题/方案卡定向，再进入高密度文档或录屏证据。
2. `split_screen_only_for_comparison`：分屏只在前后对比、方案对比、输入/输出对比时出现，并且每个 panel 必须有角色标签。
3. `human_or_guide_bridge_between_dense_blocks`：密集证据段之间加短的人感桥，避免视频变成连续文档截图。

需要用户审美确认的点：

- 是否接受项目自己的深色 matte + 白色证据卡 + 少量高亮标签作为《视频工厂》下一版录屏包装方向。
- API 人物 / 小向导 / HyperFrames 卡片中，哪一种更适合替代参考里的真人 PiP。
- 高亮标签密度上限：当前参考里标签偏多，迁移时建议收敛到“一句一个主高亮”。

下一轮若要真正改当前视频，建议从最小片段开始：

- 只选一个 `30-45s` 的中段真实录屏证据片段。
- 先做 `active_evidence_window + context_reset_card + one_claim_one_highlight_cluster`。
- 人审通过后，再扩到 split-screen 对比或整段风格迁移。
