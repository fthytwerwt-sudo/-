# 锁定参考登记表 locked_reference_registry

## 1. 文件定位

本文件登记《视频工厂》可继承 reference。

配套规则见：

- `codex_source/14_locked_reference_inheritance_rules.md`

当前 registry 的硬规则：

- `已确认` 当前初始 registry 中没有 `locked` reference。
- `已确认` 本轮只登记 candidate / failed / historical，不把任何候选写成已确认锁定参考。
- `已确认` PR 自评、技术通过、候选片 pass_for_candidate_review，不等于用户 / ChatGPT 明确确认。
- `待验证` 若用户 / ChatGPT 后续明确说“这个以后默认按这个走”，才允许升级为 `locked`。

## 2. 状态字段

| 字段 | 中文备注 |
| --- | --- |
| `reference_id` | 参考编号 |
| `name` | 中文名称 |
| `type` | 类型，如 opening / subtitle / tts / zoom / sassy_card |
| `status` | locked / candidate / failed / deprecated / historical |
| `confirmation_state` | candidate_reference_pending_confirmation / locked_reference_confirmed_by_user / locked_reference_confirmed_by_chatgpt / locked_reference_formal_synced / failed_or_pending_reference / candidate_or_rule_reference |
| `source_pr_or_log` | 来源 PR 或日志 |
| `artifact_path` | 产物路径 |
| `evidence_path` | 证据路径，如 contact sheet / clip / audio |
| `confirmed_by` | 确认方：user / ChatGPT / Codex technical only |
| `confirmation_quote_or_record` | 确认依据 |
| `applies_to` | 适用范围 |
| `does_not_apply_to` | 不适用范围 |
| `inheritance_rule` | 后续如何继承 |
| `allowed_changes` | 允许修改范围 |
| `blocked_if` | 阻断条件 |
| `last_verified_at` | 最近验证时间 |
| `notes` | 备注 |

## 3. 初始 registry

### 3.1 round34 中段剪辑语法候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `middle_editing_round34_candidate_20260425` |
| `name` | round34 中段剪辑语法候选 |
| `type` | `middle_editing` |
| `status` | `candidate` |
| `confirmation_state` | `candidate_reference_pending_confirmation` |
| `source_pr_or_log` | `codex_log/latest.md`; `codex_log/current_publish_target.md`; `GPT数据源/08_当前正式事实.md`; `dist/latest_review_pack/review_manifest.md` |
| `artifact_path` | `dist/latest_review_pack/middle_preview.mp4` |
| `evidence_path` | `dist/latest_review_pack/cut_map.md`; `dist/latest_review_pack/timeline.json`; `dist/latest_review_pack/cut_contact_sheet.jpg`; `dist/latest_review_pack/summary.json`; `dist/latest_review_pack/review_manifest.md` |
| `confirmed_by` | `user_partial_middle_segment_review` |
| `confirmation_quote_or_record` | `已确认` 用户反馈 round34 中段“现在中段没什么问题了”；`待验证` 这只代表中段暂定收束，不等于所有后续中段剪辑语法已锁定。 |
| `applies_to` | 同类 AI 知识视频的中段真实录屏证据展示；需要反面 / 正面分段提示、真实录屏主体、结果差辅助卡时。 |
| `does_not_apply_to` | 无中段录屏证据的视频；纯探索新剪辑语法；用户明确要求重做中段；需要完全不同节奏结构的题材。 |
| `inheritance_rule` | 真实录屏是主体；提示卡只做段落标识和辅助；可以继承“反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡”的语法，但不得要求所有视频秒级复刻。 |
| `allowed_changes` | 可根据新素材时长、文案节奏和平台比例调整时间码、字幕文字、卡片文字和压缩比例。 |
| `blocked_if` | 把该候选写成 locked；卡片替代真实录屏主体；完整成片未输出继承对照；放大位置与证据点对不上且未获授权。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 当前可作为候选继承参考，但需要用户 / ChatGPT 明确确认后才可升级为 locked。 |

### 3.2 PR #7 A 版骚萌卡视觉候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `sassy_card_pr7_a_candidate_20260428` |
| `name` | PR #7 A 版骚萌卡视觉候选 |
| `type` | `sassy_card` |
| `status` | `candidate` |
| `confirmation_state` | `candidate_reference_pending_confirmation` |
| `source_pr_or_log` | PR #7 `方案 B V3 骚萌表情版独立反应预览`; `origin/pr/7:codex_log/20260428_方案B独立反应片段V3骚萌表情迭代.md` |
| `artifact_path` | `origin/pr/7:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page.png` |
| `evidence_path` | `origin/pr/7:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3说明_preview_report.md`; `origin/pr/7:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/run_summary.json`; `origin/pr/7:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/sassy_expression_candidates_result_sanitized.json`; `origin/pr/7:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg` |
| `confirmed_by` | `Codex technical only` |
| `confirmation_quote_or_record` | `已确认` PR #7 A 版被选中进入技术预览；`待验证` 用户 / ChatGPT 尚未明确确认“以后骚萌卡就按这版走”。 |
| `applies_to` | 需要“贱萌 / 得瑟 / 小坏笑 / wink / 捂嘴偷笑”方向的骚萌反应卡候选复审。 |
| `does_not_apply_to` | 用户明确要求更成熟、更克制、更写实、更非表情包的视觉方向；不需要骚萌卡的位置。 |
| `inheritance_rule` | 可作为骚萌卡视觉候选对照，但完整成片中不得直接写成 locked reference；必须在继承报告中标注为 candidate。 |
| `allowed_changes` | 可微调文案、构图、表情夸张度、卡片时长和动效节奏。 |
| `blocked_if` | 把 PR #7 A 版写成用户已确认 locked；忽略用户后续对骚萌感的负反馈；只照搬角色却没有搞笑反应功能。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | PR #15 使用它作为 reference，但 PR #15 后续仍待复审，不能反推 PR #7 A 版已 locked。 |

### 3.3 PR #8 三类骚萌卡规则候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `sassy_card_three_type_rules_pr8_candidate_20260428` |
| `name` | PR #8 三类骚萌卡机制与节奏预算候选规则 |
| `type` | `sassy_card_rule` |
| `status` | `candidate` |
| `confirmation_state` | `candidate_or_rule_reference` |
| `source_pr_or_log` | PR #8 `方案 B 三类骚萌卡机制与节奏预算`; `origin/pr/8:codex_log/20260428_方案B骚萌卡结构机制与节奏预算.md`; `origin/pr/8:GPT数据源/05_文案路由规则.md` |
| `artifact_path` | `origin/pr/8:GPT数据源/05_文案路由规则.md#8A` |
| `evidence_path` | PR #8 body; `origin/pr/8:codex_log/20260428_方案B骚萌卡结构机制与节奏预算.md` |
| `confirmed_by` | `Codex technical only / current_execution_sheet` |
| `confirmation_quote_or_record` | `已确认` PR #8 是三类骚萌卡规则 draft；`待验证` 未合并前不能写成主读取分支正式已知。 |
| `applies_to` | 需要 problem hook / negative reversal / positive reversal 三类骚萌卡的结构设计和节奏预算讨论。 |
| `does_not_apply_to` | 已锁定其他卡片结构；用户明确要求本轮不用骚萌卡；不含反转点或不适合插卡的素材。 |
| `inheritance_rule` | 可作为当前任务条件已知的规则候选；完整成片使用时必须标注为 candidate_or_rule_reference，不能写成 locked。 |
| `allowed_changes` | 可按片长、素材节奏和用户确认后的风格调整卡片数量、时长和触发点。 |
| `blocked_if` | 未合并或未确认时写成正式规则；把三类卡固定成所有视频必须都有；挤占真实录屏主体。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 本条是机制候选，不是视觉成片样板。 |

### 3.4 PR #15 v2 字幕失败或待复盘参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `subtitle_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 字幕失败或待复盘参考 |
| `type` | `subtitle` |
| `status` | `failed` |
| `confirmation_state` | `failed_or_pending_reference` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; `origin/pr/15:codex_log/20260430_AI做PPT踩坑成品标准候选v2.md`; 当前执行单用户反馈 |
| `artifact_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_captions.srt` |
| `evidence_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_review_manifest.md`; `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json` |
| `confirmed_by` | `user_negative_feedback_from_current_execution_sheet` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “字幕样式不是标准”。 |
| `applies_to` | 复盘 PR #15 v2 为什么不能作为字幕标准。 |
| `does_not_apply_to` | 后续完整成片默认字幕继承。 |
| `inheritance_rule` | 不得继承为字幕标准；后续字幕需另找或新建被确认的 subtitle_reference。 |
| `allowed_changes` | 只能作为反例分析，不得作为默认样式微调起点，除非用户明确要求基于它修改。 |
| `blocked_if` | 把 PR #15 v2 字幕写成 locked；完整片沿用该字幕样式却声明继承通过。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | PR #15 自评 candidate review 不等于用户确认。 |

### 3.5 PR #15 v2 layout / 背景风格失败或待复盘参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `layout_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 layout / 背景风格失败或待复盘参考 |
| `type` | `visual_master` |
| `status` | `failed` |
| `confirmation_state` | `failed_or_pending_reference` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; 当前执行单用户反馈 |
| `artifact_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/layout_gate_report.md` |
| `evidence_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/layout_gate_report.md`; `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/quality_gates_report.md`; `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_cut_map.md` |
| `confirmed_by` | `user_negative_feedback_from_current_execution_sheet` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “背景风格被换掉”。 |
| `applies_to` | 复盘 PR #15 v2 layout / 背景为什么不能作为当前视觉母版标准。 |
| `does_not_apply_to` | 后续完整成片默认视觉母版继承。 |
| `inheritance_rule` | 不得继承为 visual_master_reference；需要另行锁定已确认视觉母版。 |
| `allowed_changes` | 只能作为失败样本复盘。 |
| `blocked_if` | 把 PR #15 layout gate pass 写成用户确认；后续成片继续换背景风格且未授权。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | layout gate 是候选审核工具输出，不代表最终内容 / 风格通过。 |

### 3.6 PR #15 v2 TTS 缺失失败参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `tts_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 TTS 缺失失败参考 |
| `type` | `tts` |
| `status` | `failed` |
| `confirmation_state` | `failed_or_pending_reference` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; 当前执行单用户反馈 |
| `artifact_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json` |
| `evidence_path` | `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json`; `origin/pr/15:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/quality_gates_report.md` |
| `confirmed_by` | `user_negative_feedback_from_current_execution_sheet` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “没有 TTS”；PR #15 summary 也标记 `temporary_no_voice_preview=true`、`voice_cloning_used=false`。 |
| `applies_to` | 复盘无 TTS 候选片不能作为 TTS 参考。 |
| `does_not_apply_to` | 后续完整成片默认 TTS 节奏继承。 |
| `inheritance_rule` | 不得继承；完整成片若需要 TTS，必须读取已确认 TTS reference 或 blocked。 |
| `allowed_changes` | 可作为“缺失 TTS”反例记录。 |
| `blocked_if` | 后续完整片无 TTS 却声明 TTS 通过；把 temporary_no_voice_preview 写成 TTS reference。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 本条不是声音风格参考，是失败状态参考。 |

### 3.7 20260427 B 版 15 秒 TTS 节奏候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `tts_15s_b_pacing_candidate_20260427` |
| `name` | 20260427 B 版 15 秒停顿梗感 TTS 节奏候选 |
| `type` | `tts` |
| `status` | `candidate` |
| `confirmation_state` | `candidate_reference_pending_confirmation` |
| `source_pr_or_log` | `codex_log/20260427_十五秒文案语速停顿试配.md`; `codex_log/latest.md`; `GPT数据源/08_当前正式事实.md` |
| `artifact_path` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav` |
| `evidence_path` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/README.md`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/run_summary.json`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_ffmpeg_decode_check.txt`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_loudnorm_measure.txt` |
| `confirmed_by` | `user_preference_direction` |
| `confirmation_quote_or_record` | `已确认` 用户更喜欢 20260427 B 版“停顿梗感”方向；`待验证` B 版只是当前优先试听方向，不是最终成片音轨，不能写 `voice_validation_status = 通过`。 |
| `applies_to` | 15 秒左右中文口播节奏、停顿梗感、轻吐槽 TTS 方向候选。 |
| `does_not_apply_to` | 完整片最终 TTS 锁定标准；非中文视频；用户要求换音色、重做节奏或不用该声音底子。 |
| `inheritance_rule` | 可作为 TTS 节奏候选；后续完整片若借用，必须标注 candidate 并输出对照音频 / 时间码。 |
| `allowed_changes` | 可调语速、停顿位置、文案长度、响度和轻微后处理。 |
| `blocked_if` | 把 B 版写成 locked；没有用户 / ChatGPT 听感最终确认却写 TTS validation 通过。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 已定位最接近的 15 秒临时样本路径；若用户指的是其他 15 秒样本，需要补明确路径。 |

### 3.8 历史通过样片参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `historical_api_demo_clean_sample_20260412` |
| `name` | 20260412 API demo clean 历史通过样片 |
| `type` | `historical_video_sample` |
| `status` | `historical` |
| `confirmation_state` | `candidate_reference_pending_confirmation` |
| `source_pr_or_log` | `codex_log/latest.md`; `GPT数据源/08_当前正式事实.md` |
| `artifact_path` | `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4` |
| `evidence_path` | `GPT数据源/08_当前正式事实.md`; 历史日志记录 |
| `confirmed_by` | `historical_user_acceptance` |
| `confirmation_quote_or_record` | `已确认` 该样片在历史口径下曾被接受；`待验证` 不代表当前 vNext 完整成片默认母版。 |
| `applies_to` | 理解项目演化、历史 demo 口径和已经跑通过的技术链路。 |
| `does_not_apply_to` | 当前 vNext 的默认视觉母版、字幕标准、TTS 标准或骚萌卡标准。 |
| `inheritance_rule` | 只能作为 historical reference；不得自动继承为当前 locked reference。 |
| `allowed_changes` | 可作为历史对照被引用。 |
| `blocked_if` | 把历史通过样片直接写成当前完整成片 locked visual master。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 历史通过不等于当前机制锁定。 |

## 4. 当前缺失项

- `待验证` 尚无用户 / ChatGPT 明确确认的 `locked_reference_confirmed_by_user` 或 `locked_reference_confirmed_by_chatgpt`。
- `待验证` 尚未锁定字幕标准。
- `待验证` 尚未锁定 TTS 最终节奏标准。
- `待验证` 尚未锁定放大方式标准。
- `待验证` 尚未锁定完整视觉母版。
- `待验证` PR #7 A 版骚萌视觉是否成为默认骚萌卡标准。
- `待验证` PR #8 三类骚萌卡规则是否合并为正式规则。

## 5. 更新规则

每次新增或修改 reference，必须同步更新：

1. 本 registry。
2. 对应证据路径。
3. 对应执行日志。
4. 若升级为新聊天默认已知，必须同步回 `codex/user-readable-map`。

升级为 `locked` 时，必须把 `confirmation_state` 改为以下之一：

- `locked_reference_confirmed_by_user`
- `locked_reference_confirmed_by_chatgpt`
- `locked_reference_formal_synced`

且必须保留确认依据，不得只写“已确认”。
