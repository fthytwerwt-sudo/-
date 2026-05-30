# 剪辑参考深度重解析报告 Deep Editing Reference Reparse Report

## 0. status_boundary（状态边界）

- `analysis_id = 20260531_deep_editing_reference_reparse`
- `task_result.status = completed_reference_analysis_artifact_synced`
- `target_delivery = whole_video_editing_system_map + second_level_timeline_analysis + subtitle_system_breakdown + split_screen_system_breakdown + screen_design_system + transition_and_rhythm_map + non_human_migration_plan + current_vs_reference_gap_report + transformation_plan`
- `已确认` 本轮只做参考视频深度解析、当前差距判断、下一轮执行规格和日志同步。
- `已确认` 本轮未生成新视频、未修改当前正片、未调用视频 / 图片 / TTS / 外部 API、未读取 `.env` / API key / token / secret。
- `已确认` 本轮未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `已确认` 上轮 5 秒抽帧 `83` 张、scene-change 帧 `16` 张、人工关键帧 `17` 张、contact sheet 均可复核；本轮已重新查看 contact sheet 和关键帧，足够支撑二次视觉系统解析。
- `部分成立` 参考 MP4 可用于视觉 / 剪辑 reference 分析：`ffprobe` 可读，单帧解码可读，完整 decode 过程可跑完但持续出现 `non monotonically increasing dts` 警告。
- `待验证` 本报告提出的迁移方案尚未进入真实 30-45 秒片段验证；不能写成项目剪辑系统已经稳定升级。

## 1. route_decision（路由判断）

```yaml
route_decision:
  repository: /Users/fan/Documents/视频工厂
  current_branch: codex/daily-tutorial-editing-profile
  project: 视频工厂
  project_route: video_factory
  task_type:
    - deep_reference_reparse
    - whole_video_editing_system_analysis
    - non_human_migration_plan
    - review_diagnosis_audit
    - project_file_change_report_and_log_only
  responsibility_layer:
    - entry_routing_layer
    - project_judgment_layer
    - execution_layer
    - validation_layer
    - sync_layer
  status: allowed_to_write_reference_analysis_reports_only
  blocked_if:
    - reference_video_unreadable
    - key_frames_unobservable
    - unable_to_separate_real_person_function_from_real_person_footage
    - only_subjective_words_without_timeline_or_screen_mechanism
    - need_external_api_or_secret
    - attempt_to_modify_core_rules_or_current_video
```

## 2. state_action_router（项目状态动作总控器）

```yaml
state_action_router:
  input_signal: user attached a Codex execution order to reparse the editing reference as a whole editing language
  current_project_state:
    - formal_operation_active
    - reference_contract_needed
    - editing_inference_needed
    - quality_review_needed
    - reference_deviation_issue
    - visual_system_reparse_needed
  fact_source_arbitration:
    primary_source:
      - AGENTS.md
      - GPT数据源/
      - codex_source/
      - codex_log/latest.md
      - local reference video artifacts
    secondary_sources:
      - user attached execution prompt
      - previous reference analysis report and manifest
      - dist/latest_review_pack/summary.json
      - dist/latest_review_pack/review_manifest.md
    conflict_detected: true
    conflict_resolution:
      - current prompt overrides the previous "good enough" interpretation
      - reference real-person footage is analyzed only as function, not as Video Factory default route
      - core mechanism files remain unchanged until user / ChatGPT review
  inferred_state: reference reparse allowed, video delivery and core-rule update forbidden
  confidence: high
  trigger_mechanism:
    - Reference-to-Execution Contract
    - editing_inference_function
    - quality_issue_classifier
    - large_task_gate
    - Completion Relay Gate
  selected_action: write a deeper report, standalone decision pack, manifest, dated log, latest summary, and git sync
  forbidden_action:
    - generate_video
    - modify_current_video
    - call_external_api
    - read_secret
    - default_real_person_shooting
    - promote_forbidden_status
  done_when:
    - previous_report_gap_audit_done
    - whole_video_system_mapped
    - timeline_5_to_10s_observations_done
    - subtitle_split_screen_design_transition_non_human_gap_plan_done
    - latest_dated_log_manifest_updated
    - commit_push_remote_verified
  blocked_if:
    - no_reproducible_reference_evidence
    - cannot_compare_or_explain_gap
    - cannot_commit_push_repo_changes
  feedback_update_required: true
```

## 3. actual_read_status（实际读取文件）

| file | read_status | purpose |
| --- | --- | --- |
| `AGENTS.md` | `read_ok` | 项目路由、单工作区、large_task_gate、Git 收口 |
| `codex_source/00_codex_readme.md` | `read_ok` | 正式运营交付边界、no-degrade、视频执行入口 |
| `codex_log/latest.md` | `read_ok` | 最近剪辑参考解析与当前边界 |
| `GPT数据源/00_项目总述.md` | `read_ok` | OPC 身份、reference 锁质量机制 |
| `GPT数据源/01_项目系统提示词.md` | `read_ok` | reference、DeepSeek、视频执行禁止降级 |
| `GPT数据源/03_总索引与阅读顺序.md` | `read_ok` | 必读顺序与 reference / data / DeepSeek 入口 |
| `GPT数据源/08_当前正式事实.md` | `read_ok` | 当前正式事实和禁止状态推进 |
| `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | `read_ok` | OPC 分工与 reference-to-execution 边界 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `read_ok` | state_action_router、editing inference、commit/push gate |
| `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md` | `read_ok` | reference contract 字段 |
| `GPT数据源/05_文案路由规则.md` | `read_ok` | 字幕、卡片、逐句映射、API 真人边界 |
| `GPT数据源/07_AI知识类视频价值规则.md` | `read_ok` | 证据可读性、人感质量、卡片和字幕边界 |
| `codex_source/19_project_state_action_router.md` | `read_ok` | Codex 执行侧 router |
| `codex_source/20_reference_to_execution_contract.md` | `read_ok` | Codex reference contract 禁止项 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | `read_ok` | large_task_gate lane / parallel |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | `read_ok` | GPT Project 侧 lane / DeepSeek 边界 |
| `codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/reference_editing_analysis_report.md` | `read_ok` | 上轮报告缺口审计 |
| `codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/analysis_manifest.json` | `read_ok` | 上轮 manifest 与 frame artifacts |
| `dist/latest_review_pack/summary.json` | `read_ok` | 当前 v3.1 review pack 状态与媒体元信息 |
| `dist/latest_review_pack/review_manifest.md` | `read_ok` | 当前 v3.1 审片入口和边界 |
| `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md` | `read_ok` | 本地视频探测规则 |
| `/Users/fan/.codex/attachments/17f02590-a9f9-4e62-a281-00037c1f30b1/pasted-text.txt` | `read_ok` | 用户本轮执行单 |

## 4. previous_report_gap_audit（上轮报告缺口审计）

```yaml
previous_report_gap_audit:
  previous_report_path: codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/reference_editing_analysis_report.md
  what_it_did_well:
    - locked reference source, status boundary and decode warning
    - produced first-pass reference_to_execution_contract
    - extracted metadata, 5s frames, scene frames and contact sheets
    - identified context reset card, evidence card, split-screen comparison and guide bridge as candidate actions
  what_it_missed:
    - whole_video_system: did not clearly say this is a whole editing method change, not element decoration
    - subtitle_system: treated captions as support text, not as an active screen-language layer
    - split_screen_system: named split screen but did not map appearances, roles, transitions, and limits
    - transition_smoothness: said hard cuts are softened, but did not explain the full bridge system
    - screen_layout_design: did not answer why the reference looks finished and why rough invented diagrams fail
    - non_human_migration: did not fully separate real-person function from real-person footage
    - visual_aesthetic_quality: did not set a minimum aesthetic line for Video Factory migration
    - micro_details: did not document the repeated label, safe-area, highlight, subtitle, PiP and panel rules
  why_previous_output_is_insufficient:
    - it was an editing action draft, not a full screen-language analysis
    - it risked making the next step "add a few cards" instead of changing the whole viewing grammar
    - it did not give ChatGPT/user enough concrete levers to reject bad page design before implementation
  how_this_round_will_fix:
    - parse whole-video structure first
    - then map 5-10 second timeline observations
    - then split subtitle, split-screen, screen design, transition rhythm and non-human migration into separate systems
    - then compare with current v3.1 pack and output a next-round implementation spec
```

User's four feedback points are handled explicitly:

- `当前项目没有真人出镜`: reference person is analyzed as `human_bridge_function`, not as default shooting route.
- `之前页面设计很丑`: this report does not invent a new PPT mockup; it extracts the reference's own design grammar.
- `不是加几个元素`: final judgment is `is_this_a_minor_element_upgrade = false` and `is_this_a_full_editing_method_change = true`.
- `字幕 / 分屏 / 顺滑 / 细节`: these are independent sections and required execution fields.

## 5. whole_video_editing_system_map（整片剪辑系统地图）

```yaml
whole_video_editing_system_map:
  source_video: /Users/fan/Documents/视频工厂/素材录制/剪辑参考/ScreenRecording_05-24-2026 21-12-50_1.MP4
  total_duration: 416.740114s
  global_editing_method:
    - open_with_person_and_big_hook
    - alternate dense proof windows with low-density reset or human bridge
    - package screen/document evidence inside a repeated dark-matte + white-card container
    - use labels/highlights/subtitles to tell the viewer where to look before the raw screen becomes hard to parse
    - use split screen only when comparison/input variants are the point
  global_visual_language:
    - dark platform background and phone capture frame
    - white document / screen card as central proof object
    - orange section label for "chapter/function"
    - green/yellow badges for mode, status or key distinction
    - yellow highlight for the exact evidence line
    - small PiP/avatar at edge for human continuity
  global_pacing_logic:
    - frequent hard cuts
    - dense proof blocks run in clusters
    - each dense cluster is preceded or followed by a reset card, person shot, title sticker or simplified label
    - the viewer is not asked to read the whole document, only the active evidence window
  global_attention_guidance:
    - face / big text grabs entry
    - section label says what category this proof belongs to
    - highlight says the current claim
    - subtitle gives the spoken beat
    - PiP/guide reminds the viewer there is a person explaining, not just a document dump
  global_subtitle_logic:
    - subtitles sit mainly in lower third, short and high-contrast
    - subtitles change with speech beats and cut points
    - large on-screen words / badges handle keywords separately from narration subtitles
    - subtitle is part of the visual rhythm, not only transcription
  global_split_screen_logic:
    - split screen appears for multiple documents, before/after states, input variants and option comparisons
    - panels carry labels, highlights or simplified claims
    - split screen is not a decoration layer
  global_transition_logic:
    - the video uses many hard cuts
    - smoothness comes from repeated containers, recurring labels, subtitle continuity, PiP/human bridge and context reset cards
    - there are few "fancy transitions"; most smoothness is semantic and layout continuity
  global_human_continuity_logic:
    - real person / PiP supplies trust, rhythm reset and emotional connection
    - person does not need to be copied; the function can be replaced by API human, guide, bridge card, voice and subtitle rhythm
  why_it_feels_better_than_current_video:
    - it has one consistent screen grammar across the whole video
    - every dense evidence screen has an orientation system
    - subtitles, labels, highlights and PiP cooperate instead of competing
    - hard cuts feel intentional because the next screen's role is labeled immediately
  what_cannot_be_copied:
    - creator face / identity
    - Douyin/TikTok platform wrapper and UI
    - exact fonts, stickers, templates or third-party media
    - real-person shooting as a default Video Factory route
    - dense full-page scale when Video Factory evidence would become unreadable
  what_can_be_translated_to_video_factory:
    - active_evidence_window
    - screen_evidence_container
    - one_claim_one_highlight
    - subtitle_as_attention_guide
    - split_screen_for_comparison_only
    - non_human_bridge_between_dense_blocks
    - hard_cut_softened_by_layout_continuity
```

## 6. second_level_timeline_analysis（秒级时间线分析）

This timeline is based on re-reading the `83` sampled frames, contact sheets, selected individual frames, and ffprobe metadata. Time ranges are approximate because this pass uses frame sampling, not a transcript-aligned edit decision list.

| time_range | visual_layout | main_carrier | subtitle_behavior | split_screen_status | screen_recording_treatment | label_and_highlight | transition_behavior | attention_target | why_it_works | transferable_to_video_factory | not_transferable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:10 | real person on purple studio, phone UI wrapper | person / hook | lower subtitle, short spoken line | none | none | large luminous hook word, account UI | direct start / hard cut | face + hook word | starts with human trust and a big promise | replace with API human, guide card or voice+subtitle hook | real creator face, platform UI |
| 00:10-00:20 | person continues, large keyword stickers | person / hook | lower subtitle synced to gesture | none | none | keyword sticker and small avatar | jump cut within same setup | claim and hand gesture | same setup makes early cuts non-disruptive | keep one opening visual system | real studio look as default |
| 00:20-00:30 | document / pricing / app screenshots collage | evidence preview | lower subtitle tells what to see | multi-panel collage | screenshots placed as cards | minimal labels, PiP avatar | hard cut from person to proof | proof scope | quickly expands topic from person to evidence | use as "evidence preview board" only if each panel is readable | 4 dense panels if target is 16:9 and text too small |
| 00:30-00:40 | document card with orange section tag | evidence card | lower subtitle supports explanation | no split, single evidence | white card on dark matte | orange section label, small PiP | hard cut | section title + active line | section tag prevents raw-document confusion | standardize section tag and active evidence window | copying exact tag style |
| 00:40-00:50 | black reset/problem card | problem framing | short line under card | text-card only | no raw screen | big text, contrast label | hard cut to reset | problem statement | viewer breathes before next dense proof | low-density bridge card | making every bridge a PPT slide |
| 00:50-01:00 | option/solution title cards | structural orientation | subtitle below card | partial side text | cards, not raw screen | red/white/orange labels | hard cuts | plan category | creates chapter map before evidence | use for section reset | overusing text cards |
| 01:00-01:10 | white web/document card, orange "1." label | screen/document proof | lower subtitle, one line | none | framed web page | orange section label | hard cut into proof | document header | the visual role is obvious immediately | framed evidence card | full-page unreadable scale |
| 01:10-01:20 | document evidence with highlight | proof line | subtitle and highlight reinforce each other | none | white card cropped to useful zone | yellow highlighted line, small badges | hard cut / slight hold | highlighted sentence | one claim has one active highlight | one_claim_one_highlight | highlighting unrelated text |
| 01:20-01:30 | document/card with PiP host | proof + human continuity | subtitle lower, close to spoken beat | none | screen remains central | yellow/green labels | hard cuts within same container | highlighted area | PiP softens document-only feel | non-human guide/PiP can replace | PiP covering evidence |
| 01:30-01:40 | person returns briefly | human bridge | subtitle becomes main spoken anchor | none | none | small text stickers | hard cut from document | face reset | breaks dense proof fatigue | API human/guide/bridge card | real-person default |
| 01:40-01:50 | document card, colored badges | proof | lower subtitle | none | white card on dark matte | orange tag, yellow highlight | hard cut back | key field | repeated grammar preserves context | reuse same card system | platform UI wrapper |
| 01:50-02:00 | table/document with large highlight | proof/table | subtitle under evidence | none | table framed and cropped | yellow row highlight | hard cut/hold | highlighted row | table is navigable because highlight narrows focus | active table row highlight | too-small unhighlighted table |
| 02:00-02:10 | phone-like panel / document mix | input example | subtitle stays bottom | partial | screen as phone/card | green/yellow tags | hard cut | source type | labels explain why new screen appears | input/source label | decorative split without comparison |
| 02:10-02:20 | multiple document panels | comparison / input variants | subtitle bridges panels | true | several sources shown together | green/yellow labels | hard cut into split | differences between sources | split is functional: compare variants | split for before/after, prompt/result | more than 2 dense panels by default |
| 02:20-02:30 | screenshot/PDF/scan labels | comparison | lower subtitle + big labels | true | each source in own panel | bright labels name source types | hard cut / panel replacement | source category labels | each panel has a role | require panel_role labels | copying exact sticker look |
| 02:30-02:40 | split panels continue | input system | subtitle clarifies conclusion | true | panel grid / card stack | high-contrast labels | cut within same motif | selected comparison point | continuity comes from same split grammar | side-by-side with label and evidence | unreadable tiny panels |
| 02:40-02:50 | document / option card | comparison resolution | subtitle one line | partial | card focused | highlight on chosen area | hard cut out | conclusion of comparison | resolves the split with one proof area | end split with one chosen evidence window | leaving panels unresolved |
| 02:50-03:00 | person on studio | human bridge | subtitle dominates lower third | none | none | small text labels | hard cut | human explanation | attention reset after dense split block | low-density bridge card or API human | real studio footage default |
| 03:00-03:10 | person + big keyword list | bridge / section marker | subtitle + big keywords | none | none | large tags, side keywords | jump cut | next topic | person sets next chapter | guide + subtitles can carry this | copied face |
| 03:10-03:20 | real-world/office footage | emotional or example cutaway | subtitle lower | none | none | few labels | hard cut | emotional context | adds relief, but weak as proof | only use B-roll as metaphor, not proof | stock person as fake evidence |
| 03:20-03:30 | document proof returns | proof | subtitle lower | none | white card | orange/green labels | hard cut | evidence line | returns to same proof grammar | keep consistent container | raw full screen without labels |
| 03:30-03:40 | document with dense paragraph | proof | subtitle at bottom, not covering highlight | none | card cropped to middle | yellow highlights | hard cut/hold | highlighted text | viewer reads only the marked line | one active evidence cluster | multi-highlight chaos |
| 03:40-03:50 | document with PiP/side avatar | proof + continuity | subtitle under card | none | framed card | avatar edge, orange tag | hard cut | highlighted phrase | human continuity without changing proof role | small guide outside evidence | covering OCR/buttons |
| 03:50-04:00 | table / document evidence | proof | subtitle maps to current claim | none | framed table/card | row highlight | hard cut | active row | proof remains central | row/field specific crop | full dashboard screenshot |
| 04:00-04:10 | document with side labels | proof | subtitle + labels | none | white card on dark | yellow highlight, red/orange badge | hard cut | a single result detail | labels reduce cognitive load | section label + evidence label | label overload |
| 04:10-04:20 | document proof continues | proof | lower subtitle | none | framed document | highlight cluster | cut/hold | highlighted paragraph | hold time supports one claim | hold one claim long enough | requiring full-page reading |
| 04:20-04:30 | document proof and PiP | proof | subtitle line | none | screen card | PiP avatar | hard cut | proof + guide | PiP prevents monotony | guide as rhythm not evidence | guide as main evidence |
| 04:30-04:40 | person / issue transition | bridge / new issue | subtitle supports spoken transition | none | none | problem label | hard cut | new issue | starts a new problem section | bridge card or API human | real person default |
| 04:40-04:50 | real-world footage / stock-like scene | example or emotional relief | subtitle lower | none | none | few labels | hard cut | analogy/emotion | gives breath but is weaker evidence | use only when labeled as illustration | stock footage proving claim |
| 04:50-05:00 | black problem card | section reset | subtitle and card text align | none | card only | big problem text, orange outline | hard cut | problem statement | sharp reset before explanation | problem bridge card | too much body text |
| 05:00-05:10 | document / report proof | proof | subtitle lower | none | framed document | highlights and labels | hard cut | key claim | resets back to proof after problem | evidence card sequence | copying reference topic |
| 05:10-05:20 | document with multiple highlights | proof | subtitle anchors current claim | none | white card | yellow highlights | hard cut/hold | highlighted row | highlights explain current line | one claim per hold | many claims at once |
| 05:20-05:30 | document / comparison card | proof / comparison | subtitle line | partial | two areas visible | labels | hard cut | compare point | slight split supports contrast | prompt/result or before/after split | decorative double card |
| 05:30-05:40 | card/text explanation | bridge / compression | subtitle supports card | none | card, not raw screen | colored label | hard cut | compressed conclusion | reduces dense proof load | short summary bridge | summary replacing evidence |
| 05:40-05:50 | document proof returns | proof | subtitle lower | none | framed document | highlight cluster | hard cut | exact proof | consistent proof grammar | same evidence container | raw page dump |
| 05:50-06:00 | document with red/yellow highlight | proof | subtitle at bottom | none | card crop | highlight / badge | hard cut | current field | marked line directs attention | active_evidence_window | covering UI |
| 06:00-06:10 | document proof / small avatar | proof + continuity | subtitle bridge | none | framed screen | avatar edge | hard cut | proof area | recurring avatar softens cuts | optional guide layer | avatar too large |
| 06:10-06:20 | more document proof | proof | subtitle lower | none | white card | yellow highlight | hard cut | highlighted phrase | evidence cluster continues but stays structured | repeat container grammar | overlong proof run without reset |
| 06:20-06:30 | person / summary-like return | bridge / summary | subtitle becomes main anchor | none | none | large word sticker | hard cut | summary phrase | human bridge closes dense run | API human/guide/low-density card | copied face |
| 06:30-06:40 | title / AI / city / hand closeups | outro texture / CTA | subtitle and large words | partial | not proof | big keyword title | fast hard cuts | final impression | emotional texture closes video | only if clearly decorative | treating B-roll as evidence |
| 06:40-06:56 | person/keyword ending | closing bridge | subtitle lower, short | none | none | large keyword wordmark | hard cut/outro | takeaway | ends with human continuity instead of raw document | non-human outro bridge | creator identity |
```

## 7. subtitle_system_breakdown（字幕系统拆解）

```yaml
subtitle_system_breakdown:
  subtitle_position:
    - primary: lower third inside the video content area
    - secondary: large keyword stickers / section words appear near face or evidence when they carry emphasis
  subtitle_safe_area:
    - subtitles generally avoid the central document highlight
    - they sit below the active proof card or over low-detail lower areas
    - Video Factory must reserve evidence-safe subtitle zones per clip
  subtitle_line_count:
    - usually 1 line
    - sometimes 2 short lines
    - large keywords are separated from narration subtitles
  subtitle_density:
    - narration subtitles are short
    - dense information is moved to labels/highlights/cards, not stuffed into subtitle lines
  font_weight_and_size:
    - high-contrast white, medium-bold enough for phone viewing
    - keyword stickers use much larger display type
  keyword_emphasis:
    - keywords are not only bolded in subtitle
    - they become separate badges, section tags or big visual words
  background_or_shadow:
    - subtitles use dark stroke/shadow or sit on dark UI/background
    - Video Factory should use controlled shadow/backplate only when evidence remains visible
  subtitle_vs_visual_focus:
    - subtitle states the spoken beat
    - highlight points to evidence
    - label names the section/panel role
    - these three layers are different jobs
  subtitle_timing:
    - changes follow speech beats and cut points
    - short subtitle changes help hard cuts feel connected
  subtitle_transition:
    - mostly direct text replacement, not decorative animation
    - smoothness comes from timing and position consistency
  subtitle_role:
    narration_support: true
    visual_anchor: true
    punchline: true when paired with large keyword sticker
    section_marker: partly, but section labels do most section work
  what_video_factory_should_copy:
    - treat subtitle as attention guidance, not transcript dumping
    - keep subtitles short and synchronized to cut/hold beats
    - separate subtitle_text, keyword_badge_text and section_label_text
    - reserve evidence-safe zones before placing subtitles
  what_video_factory_should_avoid:
    - full sentence blocks covering prompt/table/chat evidence
    - using subtitles to introduce unverified claims
    - making every keyword a sticker
    - changing locked copy meaning while splitting subtitles
  implementation_fields_needed:
    - subtitle_safe_zone
    - subtitle_role
    - subtitle_line_count_max
    - keyword_badge_text
    - keyword_badge_reason
    - subtitle_change_sync_point
    - subtitle_overlap_with_evidence_risk
```

Direct answers:

- 字幕不是单纯底部转写。它与高亮、标签、分屏共同形成“这一秒看哪里”的视觉引导。
- 关键词强调主要由大字贴、标签和高亮承担，字幕负责口播节奏。
- 字幕承担节奏。硬切后字幕位置不乱，观众可以继续听懂下一画面。
- Video Factory 下一轮必须把 `subtitle_text` 与 `visual_focus` 绑定，不能先生成字幕再随便盖上去。

## 8. split_screen_system_breakdown（分屏系统拆解）

```yaml
split_screen_system_breakdown:
  split_screen_appearances:
    - time_range: 00:20-00:30
      layout_type: multi-panel evidence preview collage
      panel_count: 4
      panel_ratio: roughly equal small cards
      separator_style: dark matte gaps
      panel_labels: minimal, mostly visual category cues
      evidence_in_each_panel: documents/pricing/app screenshots
      subtitle_relationship: subtitle explains the scope while panels preview examples
      transition_in: hard cut from person hook
      transition_out: hard cut to single document/proof card
      why_split_screen_is_needed: introduces multiple evidence sources fast
      why_it_feels_smooth: it is immediately followed by a clearer single proof window
    - time_range: 02:10-02:45
      layout_type: source-variant comparison panels
      panel_count: 2-4 depending on moment
      panel_ratio: large central card plus smaller source panels
      separator_style: dark background and panel edges
      panel_labels: green/yellow labels such as screenshot/PDF/scan-like source roles
      evidence_in_each_panel: input/source formats and document examples
      subtitle_relationship: subtitle gives the comparison sentence, labels name panel roles
      transition_in: hard cut after a proof sequence
      transition_out: hard cut to single evidence or person bridge
      why_split_screen_is_needed: the viewer must compare source types
      why_it_feels_smooth: labels and repeated dark-card system keep the panels from feeling random
    - time_range: 05:20-05:35
      layout_type: partial comparison / card pair
      panel_count: 2
      panel_ratio: one dominant proof, one support/comparison
      separator_style: card spacing and background contrast
      panel_labels: small labels / highlight roles
      evidence_in_each_panel: current claim evidence versus supporting example
      subtitle_relationship: subtitle compresses what the comparison means
      transition_in: hard cut from document proof
      transition_out: summary / bridge card
      why_split_screen_is_needed: comparison resolves one decision
      why_it_feels_smooth: it exits quickly after the comparison has done its job
  split_screen_rules:
    use_when:
      - before_after_state
      - prompt_vs_result
      - source_vs_output
      - option_a_vs_option_b
      - multiple_input_types_need_direct_contrast
    do_not_use_when:
      - one evidence stream is enough
      - panels become unreadable
      - split is only decorative
      - labels cannot explain each panel role
      - core proof needs full context
    max_panel_count: 2 dense panels by default; 3 only for low-text labeled comparison; 4 only as a very short preview board
    readability_line: each active panel must preserve the one field/line/button needed for proof
    label_rule: every panel needs a role label, not a vague title
    evidence_rule: each panel must prove or contrast something; no filler panels
  video_factory_migration:
    allowed_use_cases:
      - before/after result difference
      - raw prompt vs fixed prompt
      - original screen vs generated output
      - candidate table vs detail table
      - old clip vs repaired clip in review pack
    forbidden_use_cases:
      - decorative collage
      - adding a guide/person panel just to fill space
      - more than two dense screen recordings in 16:9
      - split screen that forces subtitles to cover evidence
    required_fields:
      - split_screen_use_reason
      - panel_role
      - panel_source_timecode
      - panel_active_evidence_window
      - panel_label
      - comparison_claim
      - exit_condition
```

Direct answers:

- 分屏基本只在“比较 / 多输入 / 多选项 / before-after”时有效。
- 每一块必须有角色。没有 panel role 的分屏会变成乱堆。
- 分屏依赖字幕、标签和高亮一起工作：字幕说结论，标签说每块是什么，高亮说当前看哪一行。
- 进入/退出多为硬切，但因为前后都在同一套 dark matte + proof card 体系里，所以不突兀。
- Video Factory 一加分屏容易乱，是因为如果没有 `panel_role / active_evidence_window / subtitle_safe_zone`，两块屏幕会互相抢证据。

## 9. screen_design_system（屏幕设计系统）

```yaml
screen_design_system:
  background_system:
    - reference uses a stable dark phone/platform background around content
    - dense white proof cards sit on dark matte, so proof has strong contrast
  card_system:
    - proof card is usually white with rounded rectangle or document frame
    - reset/problem cards use dark or black background with big text
    - cards have one job: orient, prove, compare, or summarize
  screen_recording_container:
    - screen/document is framed, scaled and visually separated from background
    - active proof area is highlighted instead of asking viewer to inspect the whole page
  border_shadow_radius:
    - subtle separation and rounded corners, not heavy decorative card nesting
    - Video Factory should keep radius restrained and avoid "card inside card" overload
  spacing_and_margin:
    - margins protect the proof rectangle from UI, subtitles and PiP
    - dense document text is tolerable only when the active line is highlighted
  color_system:
    - orange: section/chapter/function label
    - yellow: active evidence highlight
    - green/yellow badges: mode/status/category distinction
    - dark background: continuity and contrast
    - white card: proof/evidence area
  label_system:
    - labels name role, not decoration
    - labels sit at edges or top-left, not over the proof line
  highlight_system:
    - one main highlight cluster per claim
    - highlight points to the evidence line/field, not to a topic-adjacent area
  icon_or_sticker_usage:
    - stickers / big words are used for hook, punchline or section emphasis
    - they are not the proof
  visual_density_control:
    - dense proof blocks are separated by person, reset card or low-density bridge
    - the active evidence window is smaller than the raw page
  composition_balance:
    - proof is central
    - PiP/avatar/labels are secondary
    - subtitles stay in a repeatable safe area
  why_it_looks_less_ugly:
    - every visual element has a job
    - colors have fixed meaning
    - raw screens are wrapped in a consistent proof container
    - dense pages are not presented as "please read everything"
    - hard cuts are absorbed by repeated layout grammar
  video_factory_design_translation:
    design_principles:
      - proof_first
      - one_claim_one_focus
      - repeated_container_grammar
      - low_density_bridge_between_dense_blocks
      - labels_outside_evidence
    allowed_elements:
      - dark/neutral matte background
      - clean evidence frame
      - section label
      - active highlight
      - small keyword badge
      - optional guide/PiP layer outside proof
      - subtitle safe-area
    forbidden_elements:
      - rough PPT mockup as final design
      - exact Douyin/TikTok wrapper
      - copied creator face / stickers / font
      - decorative collage with no evidence role
      - labels covering prompt/table/button/chat evidence
      - dense one-note cute card for every screen
    density_limit:
      - max one section label
      - max one active highlight cluster
      - max one guide/PiP or bridge layer
      - subtitle max 1-2 short lines
    minimum_aesthetic_line:
      - no raw full-page screenshot without focus
      - no centered text card that looks like a rough note
      - no unlabeled split panels
      - no subtitle/card overlap with evidence
      - no color role drift
```

Direct answers:

- 参考视频用了统一背景和统一 proof-card 容器。
- 录屏 / 文档被放进统一容器，而不是裸屏硬贴。
- 标签和高亮有固定职责：orange 是章节，yellow 是证据，green/yellow 是状态或分类。
- 图标 / 贴纸是辅助钩子，不替代证据。
- 它不像 PPT，是因为卡片不是静态章节讲义，而是和当前证据窗口绑定。
- 它不像生硬录屏，是因为 raw screen 前后都有标签、字幕、PiP/bridge 和高亮解释。
- 它不像信息乱堆，是因为观众每一秒只被要求看一个主焦点。

## 10. transition_and_rhythm_map（转场与节奏地图）

```yaml
transition_and_rhythm_map:
  cut_frequency:
    - high
    - many sampled frames show major visual changes every 5-10 seconds
    - dense proof sequences may cut every few seconds while retaining same container grammar
  hard_cut_usage:
    - dominant transition method
    - used between person, reset card, proof card, split-screen and example footage
  soft_transition_usage:
    - low; smoothness is not mainly from soft visual transitions
    - occasional motion is secondary to semantic continuity
  motion_bridge:
    - PiP/avatar persistence
    - repeated card frame
    - highlight and label continuity
  subtitle_bridge:
    - lower subtitle remains consistent across cuts
    - speech line carries context into the next screen
  visual_repetition_bridge:
    - dark matte background
    - white proof card
    - orange section tag
    - yellow highlight
    - edge avatar/PiP
  human_or_guide_bridge:
    - person returns after dense proof blocks
    - PiP face appears on proof cards
    - function can be replaced by non-human bridge
  pause_and_hold:
    - proof cards hold long enough for highlighted claim
    - they do not require reading every word
  rhythm_pattern:
    - hook
    - preview proof
    - reset card
    - dense evidence
    - human/guide bridge
    - comparison split
    - proof resolution
    - summary/closing
  why_reference_feels_smooth:
    - hard cuts are labeled immediately
    - repeated container tells the viewer this is the same information system
    - subtitles and highlights carry attention over the cut
    - person/guide breaks document fatigue
  why_current_video_may_feel_stiff:
    - current v3.1 review pack has `subtitle_enabled = false`
    - current contact sheet relies on raw screen blocks and separate cute/PPT-like cards rather than one continuous screen language
    - current cards and raw screen evidence feel more like alternating modules than a unified guided proof system
    - current v3.1 is vertical 720x1280 while current formal-operation default has moved to horizontal 1920x1080, so future migration must be rebuilt rather than patched visually
  migration_rules:
    - keep hard cuts, but make every cut answer "why am I seeing this now"
    - use a repeated evidence container before adding transitions
    - use subtitle_bridge and section_label before fancy motion
    - insert a low-density bridge after 2-3 dense proof screens
    - never use transition motion that hides the action result
```

Key judgment:

- `已确认` 参考视频其实也有大量硬切。
- `已确认` 硬切不突兀的原因不是 fancy transition，而是 `统一容器 + 字幕承接 + 高亮指向 + 人感/小头像桥 + 上下文卡`。
- `已确认` Video Factory 下一轮应先迁移这套 continuity system，不应先堆动画转场。

## 11. non_human_migration_plan（非真人迁移方案）

```yaml
non_human_migration_plan:
  if_reference_has_real_person:
    real_person_function:
      attention_reset: dense document blocks后让观众重新看人而不是继续扫屏
      trust_anchor: 让复杂信息像有人在带路，不像自动拼接
      rhythm_break: 打断连续证据卡的疲劳
      emotional_bridge: 给问题、反转、吐槽和总结提供情绪承接
      explanation_anchor: 在进入/退出复杂证明前用口播稳定语境
  video_factory_replacements:
    - api_generated_human:
        suitable_for:
          - opening hook
          - section transition where a human-like explanation is needed
          - closing summary
        not_suitable_for:
          - replacing user recording evidence
          - proving table/chat/screen actions
          - default every transition
    - element_doll_or_guide:
        suitable_for:
          - small edge guide
          - attention reset
          - light emotional cue
          - transition after dense proof
        not_suitable_for:
          - covering proof windows
          - becoming the main narrator for all evidence
          - adding childish or demo-like feeling
    - low_density_bridge_card:
        suitable_for:
          - default replacement for real-person bridge
          - problem reset
          - "now look at this field" guidance
          - separating two dense evidence clusters
        not_suitable_for:
          - long explanations
          - claims that need direct screen proof
          - decorative pause with no function
    - voice_and_subtitle_bridge:
        suitable_for:
          - maintaining human feeling without new visuals
          - softening hard cuts
          - guiding attention to one line/field
          - carrying rhythm through proof screens
        not_suitable_for:
          - replacing visual evidence
          - covering dense evidence with long subtitle text
  forbidden_translation:
    - default_real_person_shooting
    - copied_creator_face_or_identity
    - stock_person_as_fake_evidence
    - real-person footage as proof of user's workflow
  recommended_default:
    - primary: low_density_bridge_card + voice_and_subtitle_bridge
    - secondary: element_doll_or_guide as small optional continuity layer
    - conditional: api_generated_human only for opening / transition / closing after route decision
    - never: default real-person shooting or copied creator identity
```

Short decision:

- `已确认` 《视频工厂》不应把参考里的真人实拍写成默认方案。
- `已确认` 迁移对象是人感桥接功能，不是真人素材。
- `推荐默认方案`: `低密度桥接卡 + 声音/字幕节奏桥`，必要时加小向导，API 生成人物只在开头/转折/结尾按 `opening_route_decision` 条件使用。

## 12. current_vs_reference_gap_report（当前视频与参考视频差距报告）

```yaml
current_vs_reference_gap_report:
  current_video_source:
    preferred_path: dist/latest_review_pack/full.mp4
    manifest: dist/latest_review_pack/review_manifest.md
    summary: dist/latest_review_pack/summary.json
    current_pack_round: 20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix
    current_pack_duration: 149.993s
    current_pack_resolution: 720x1280
    current_pack_subtitle_enabled: false
    note: this is v3.1 historical/current review pack, while current formal-operation default delivery has moved to horizontal 16:9 / 1920x1080
  comparison_available: partial_observable_comparison
  comparison_basis:
    - summary.json metadata
    - review_manifest.md status boundary
    - current contact sheet visual inspection
    - reference contact sheet and sampled frames
  gap_dimensions:
    whole_video_structure:
      current: alternates raw screen captures, cute card/persona card, and prompt/result cards
      reference: one continuous guided proof language across person, proof, split screen and reset cards
      gap: current feels more modular; reference feels like one editing system
    screen_design:
      current: card style and raw screen style coexist; visual shells vary more
      reference: repeated dark matte + white evidence card + label/highlight language
      gap: current lacks a single evidence container grammar
    subtitle_system:
      current: `subtitle_enabled = false` in summary; contact sheet does not show a comparable active subtitle system
      reference: subtitles are always part of timing and attention guidance
      gap: current loses a major continuity layer
    split_screen:
      current: contact sheet shows side-by-side visual route assets but not a consistent comparison-screen language
      reference: split screen appears only with source/option/comparison roles and labels
      gap: current needs functional split rules, not just side-by-side assets
    transition_rhythm:
      current: transitions depend on segment/card alternation
      reference: hard cuts are softened by subtitle, label, highlight and PiP continuity
      gap: current needs semantic bridge fields per cut
    evidence_window:
      current: real screen evidence appears but can feel like raw capture or separate module
      reference: every proof window has an active focus marker
      gap: define `active_evidence_window` before every card/subtitle/highlight
    visual_density:
      current: cute card/prompt card density and raw screen density are not governed by one hierarchy
      reference: density is high but focused by labels and resets
      gap: add density budget and bridge cadence
    human_continuity_without_real_person:
      current: relies on element doll/card/persona shell in places
      reference: uses real person/PiP for trust and rhythm
      gap: migrate the function through low-density bridge, guide layer and subtitle rhythm
  highest_priority_gap: lack_of_unified_screen_language_and_subtitle_bridge
  why_this_gap_matters: without a unified screen language, adding split screen or new cards will look like more decoration, not smoother editing
  what_to_change_first: run a 30-45s evidence segment test with active_evidence_window + subtitle_safe_zone + context_bridge_card + one_claim_one_highlight before changing full video
```

## 13. video_factory_editing_transformation_plan（视频工厂剪辑方式改造方案）

```yaml
video_factory_editing_transformation_plan:
  target_style_statement: "把真实录屏/文档证据包装成一套连续的 guided proof video, 用字幕、标签、分屏和非真人桥接持续告诉观众这一秒看哪里。"
  before_problem:
    - raw screen evidence and visual cards can feel like separate modules
    - subtitle bridge is missing or under-specified
    - split-screen has no strict role grammar
    - non-human continuity layer is not yet equivalent to reference's person/PiP rhythm
  after_goal:
    - every dense screen has an active evidence window
    - every cut has a semantic bridge
    - subtitles support timing and attention
    - split screen is only used for comparison
    - non-human bridge replaces real-person function without copying real-person footage
  core_editing_method:
    - context_bridge -> evidence_container -> one_claim_highlight -> subtitle_bridge -> optional_split_compare -> low_density_reset
  default_screen_layout:
    - 16:9 canvas for future formal-operation delivery
    - central evidence container
    - label strip at edge/top-left
    - subtitle safe zone below or sidecar based on evidence location
    - optional guide layer outside evidence rectangle
  subtitle_system:
    - subtitle_text: 1-2 short lines
    - keyword_badge_text: only for hook/punchline/section terms
    - subtitle_change_sync_point: align with cut/hold/claim transition
    - subtitle_overlap_check: mandatory before render
  split_screen_policy:
    - only if comparison is the point
    - two dense panels max by default
    - each panel has role label, source timecode and active evidence window
    - exit as soon as comparison is resolved
  evidence_window_policy:
    - every line_group must name active_evidence_window
    - highlights must point to direct evidence, not topic-adjacent material
    - cards/subtitles cannot cover proof fields
  transition_policy:
    - allow hard cut
    - require bridge reason per cut
    - smooth with repeated container, subtitle continuity and bridge card, not decorative transitions first
  non_human_bridge_policy:
    - default low-density bridge card + voice/subtitle rhythm
    - optional element doll/guide outside proof window
    - API human only after route decision for opening/transition/closing
  visual_density_policy:
    - max one section label, one highlight cluster, one guide/PiP layer, and one subtitle block per evidence window
    - after 2-3 dense proof screens, add a low-density reset
  card_system_policy:
    - context card: only before dense proof
    - result card: only compresses verified evidence
    - summary card: after proof, not replacing proof
    - prompt tail card: optional, not main evidence
  what_to_remove_from_old_style:
    - raw full-screen evidence with no active focus
    - static card sequences that do not bridge to proof
    - decorative split screens
    - over-cute guide layer covering evidence
  what_to_add_to_new_style:
    - active_evidence_window
    - subtitle_safe_zone
    - panel_role
    - comparison_claim
    - bridge_reason
    - density_budget
    - design_token_role
  what_to_test_first:
    - one 30-45s current evidence segment
    - compare current clip vs redesigned guided proof clip
    - validate subtitle readability, split readability, evidence safety and smoothness by human review
  is_this_a_minor_element_upgrade: false
  is_this_a_full_editing_method_change: true
```

## 14. implementation_spec_for_next_round（下一轮执行规格）

```yaml
implementation_spec_for_next_round:
  recommended_validation_scope:
    duration: 30_to_45s
    source_material: one existing dense evidence segment from the next target video or a current candidate segment if user authorizes repair testing
    why_this_scope: small enough for visual QA, large enough to test subtitle bridge, evidence container and one split/bridge decision
  required_inputs:
    - locked_copy_contract
    - material_parse_pack
    - script_to_timeline_map
    - current_data_goal_anchor
    - visual_style_decision
    - active_evidence_window_map
  minimum_output:
    - 30_to_45s_clip
    - before_after_comparison
    - review_pack
    - subtitle_card_overlap_report
    - split_screen_readability_report
    - evidence_window_safety_report
  must_validate:
    - subtitle_readability
    - split_screen_readability
    - evidence_window_safety
    - no_real_person_default
    - no_decoration_overload
    - smoother_than_current_baseline
    - locked_copy_not_changed
    - no_forbidden_status_promotion
  blocked_if:
    - current_clip_missing
    - no_locked_copy
    - no_material_parse_pack
    - no_script_to_timeline_map
    - visual_design_unclear
    - subtitle_or_card_overlap_high
    - split_screen_has_no_comparison_reason
```

## 15. standalone_editing_decision_pack（独立剪辑决策包路径）

本轮另存独立下一轮执行包：

- `codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/editing_decision_pack_for_next_round.md`

其职责不是修改核心规则，而是给下一轮 30-45 秒片段验证使用。核心判断：

- `is_this_a_minor_element_upgrade = false`
- `is_this_a_full_editing_method_change = true`
- `recommended_default_non_human_bridge = low_density_bridge_card + voice_and_subtitle_bridge`
- `split_screen_policy = comparison_only`
- `subtitle_policy = attention_guidance_not_transcript_dump`
- `screen_design_policy = evidence_container_first`

## 16. validation（验证）

```yaml
validation:
  ffprobe:
    source_reference: passed
    evidence: "416.740114s / 1180x2556 / HEVC / ~60fps / AAC"
    current_video_probe: "dist/latest_review_pack/full.mp4 = 149.993s / 720x1280 / h264 / aac"
  frame_sampling:
    status: reused_previous_artifacts_after_recheck
    sampled_frame_count: 83
    scene_change_frame_count: 16
    manual_keyframe_count: 17
    scene_frame_dir_total_jpg_count_including_manual_keys: 33
  contact_sheet:
    status: present_and_reopened
    contact_sheet_5s: codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/contact_sheet_5s.jpg
    keyframe_contact_sheet: codex_log/reference_analysis/20260530_剪辑参考解析_editing_reference_parse/contact_sheets/keyframe_contact_sheet.jpg
  decode_check:
    status: completed_with_dts_warnings
    warning: non monotonically increasing dts
    interpretation: usable for reference visual analysis, not a clean delivery media validation
  no_external_api: true
  no_secret_read: true
  no_video_generated: true
  no_audio_generated: true
  current_video_modified: false
  core_rules_modified: false
  no_status_promotion: true
```

## 17. required_output_inventory（必须交付清单）

| item | status |
| --- | --- |
| `route_decision` | `done` |
| `state_action_router` | `done` |
| `previous_report_gap_audit` | `done` |
| `whole_video_editing_system_map` | `done` |
| `second_level_timeline_analysis` | `done` |
| `subtitle_system_breakdown` | `done` |
| `split_screen_system_breakdown` | `done` |
| `screen_design_system` | `done` |
| `transition_and_rhythm_map` | `done` |
| `non_human_migration_plan` | `done` |
| `current_vs_reference_gap_report` | `done_partial_observable_comparison` |
| `video_factory_editing_transformation_plan` | `done` |
| `implementation_spec_for_next_round` | `done` |
| `editing_decision_pack_path` | `done` |
| `analysis_manifest` | `done` |
| `dated_log` | `done` |
| `latest_update` | `done` |
| `git_commit_push_remote_verify` | `pending_until_git_closure` |

## 18. remaining_work_check（剩余工作检查）

- `已确认` 本轮参考解析报告本身已补齐用户指定的字幕、分屏、顺滑、屏幕设计、非真人迁移和当前差距维度。
- `已确认` 本轮没有生成视频，所以不需要 `publish_candidate_preflight_suite`，也不得写 `publish_candidate_ready_for_human_review`。
- `待验证` 下一轮如要真正改片，必须建立 `locked_copy_contract / material_parse_pack / script_to_timeline_map / current_data_goal_anchor / visual_style_decision`。
- `待验证` 本报告提出的视觉语言需要 ChatGPT / 用户先做审美确认，再进入 30-45 秒片段验证。
- `待验证` 如果未来要把本 reference MP4 当可复用素材源而不是分析 reference，应先重封装/转码并重新跑 media validation。

## 19. next_handoff_to_chatgpt（交给 ChatGPT 的下一步）

ChatGPT 应该讨论的 3 个关键判断：

1. 是否确认下一版《视频工厂》的目标剪辑语言为 `guided proof video（被引导的证据视频）`，而不是继续在旧风格上加几个卡片。
2. 非真人人感桥默认用哪一层：`低密度桥接卡 + 声音/字幕` 是否作为默认，`小向导` 是否只做可选边缘层，`API 生成真人` 是否只用于开头/转折/结尾。
3. 30-45 秒验证片段先选哪一段真实证据：优先选最密集、最容易显得生硬的一段，而不是最轻松好看的片段。

用户需要审美确认的点：

- 是否接受 dark/neutral matte + clean evidence container + small labels/highlight 的方向。
- 是否接受字幕成为视觉引导层，而不是只做底部转写。
- 是否接受每 2-3 个 dense proof screen 后插入低密度桥接卡。
- 是否允许下一轮做一个 before/after comparison pack 给用户看。

下一轮是否进入 30-45 秒片段验证：

- `recommendation = yes_after_chatgpt_user_style_confirmation`
- 先做小片段，不直接全片迁移。
