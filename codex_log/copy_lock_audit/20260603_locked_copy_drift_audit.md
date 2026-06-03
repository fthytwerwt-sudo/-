# 20260603 locked copy drift audit

## 1. Route decision（路由判断）

- `project_route`: `video_factory`
- `task_type`: `review_diagnosis_audit + readonly_audit + copy_lock_drift_diagnosis`
- `selected_state`: `self_repair_audit_required + locked_copy_diff_preflight_required`
- `write_allowed`: `audit_report_only`
- `large_task_gate`: `triggered=true`; selected lane `audit_lane`; parallel mode `read_parallel_for_reads + serial_integrator`
- `deepseek_supply_gate`: `fallback_local_only_for_this_audit`; 本轮用户只允许创建本报告文件，因此未新增 supply request 文件；未把任何本轮结论写成 DeepSeek 结论。
- `final_status`: `audit_report_committed_pending_git_sync_at_report_write_time`

## 2. Files read（实际读取）

### Required entry files

| file | status | note |
| --- | --- | --- |
| `AGENTS.md` | `read_ok` | 路由、只读审计、单工作区、locked copy、commit/push 规则 |
| `codex_log/latest.md` | `read_ok` | 确认第五期候选片 canonical dist 路径 |
| `codex_source/00_codex_readme.md` | `read_ok` | locked copy、process boot、no degrade、commit/push gate |
| `GPT数据源/01_项目系统提示词.md` | `read_ok` | locked copy、Codex 不改稿、preflight 要求 |
| `GPT数据源/03_总索引与阅读顺序.md` | `read_ok` | locked copy、self repair audit、DeepSeek 边界 |
| `GPT数据源/05_文案路由规则.md` | `read_ok` | locked copy、subtitle/card/TTS/preflight 接入 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | `read_ok` | self repair audit、locked_copy_diff_preflight_required |
| `codex_source/19_project_state_action_router.md` | `read_ok` | Codex 执行层 state router 与 locked_copy_diff_preflight 动作 |
| `codex_source/21_codex_judgment_permission_matrix.md` | `read_ok` | Codex 判断权限、locked copy diff gate |

### Target local artifacts

| file | status | note |
| --- | --- | --- |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/summary.json` | `read_ok` | 指向 timeline、TTS、preflight、review_pack |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/review_manifest.md` | `read_ok` | full video、字幕、TTS、preflight 路径 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/publish_candidate_preflight_report.json` | `read_ok` | 总 preflight passed，但只列报告状态 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/subtitles/final.srt` | `read_ok` | 发现 L25 缺两句 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/subtitles/final.ass` | `read_ok` | 同样发现 L25 缺两句 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/timeline/locked_copy_contract.json` | `read_ok` | locked contract source |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/timeline/script_to_timeline_map.json` | `read_ok` | 41 个 line_group |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/audio/tts_route_report.json` | `read_ok` | TTS segment text/input |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/timeline/card_placement_decision.json` | `read_ok` | 卡片文案源 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/locked_copy_diff_preflight_report.json` | `read_ok` | preflight 覆盖不足证据 |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/scripts/生成第五期Codex赚钱正片_generate_fifth_codex_money_candidate.py` | `read_ok` | 第一处漂移的生成脚本 |

### Missing / absent

| item | status | note |
| --- | --- | --- |
| `dist/fifth_episode_codex_money_publish_candidate_20260603/*copy_change_request*` | `missing` | 未发现 copy_change_request 文件 |
| target dist directory | `read_ok` | 不触发 `missing_local_artifact` |
| `locked_final_script` source | `read_ok` | 不触发 `blocked_cannot_find_locked_copy_source` |

## 3. Locked copy contract status（锁定文案契约状态）

- `found`: `true`
- `path`: `dist/fifth_episode_codex_money_publish_candidate_20260603/timeline/locked_copy_contract.json`
- `locked_copy_source`: `user_execution_order_20260603`
- `locked_topic`: `Codex 到底能不能帮普通人赚钱`
- `locked_title`: `Codex 到底能不能帮普通人赚钱？`
- `locked_opening_line`: `最近网上很多人在聊 Codex。`
- `locked_final_script_found`: `true`
- `locked_final_script_chars`: `1238`
- `line_group_count`: `41`
- `allowed_copy_changes`: `标点微调`; `字幕断句`; `TTS 停顿标记`; `极轻微错别字记录为 copy_change_request，不得直接改`
- `forbidden_copy_changes`: `改标题`; `改选题`; `改开头`; `改核心判断`; `改“没有真正赚钱 / 电商保本 / 不是赚钱机器”的诚实边界`; `把“90% 自动化”扩大成完全自动化`; `把“还在测试”写成已跑通`; `把“不赚钱”弱化成“暂时还没完全商业化”`; `把评论区 CTA 改成强关注 / 强卖课 / 强转化`
- `copy_change_request_required_if_needed`: `true`
- `missing_fields`: `none`

## 4. Copy flow map（文案流转图）

| stage | source file | text source field | consumes locked_final_script? | risk |
| --- | --- | --- | --- | --- |
| locked copy contract | `timeline/locked_copy_contract.json` | `locked_final_script` | `yes` | source is present |
| generator locked constants | `scripts/生成第五期Codex赚钱正片_generate_fifth_codex_money_candidate.py` | `LOCKED_FINAL_SCRIPT` | `yes` | source embedded in dist script |
| script_to_timeline_map | `timeline/script_to_timeline_map.json` | `line_groups[].narration_text` | `yes` | no-whitespace exact match with locked script |
| TTS input | `audio/tts_route_report.json` | `segment_reports[].tts_text` | `yes, via LINE_GROUPS` | punctuation/pause markers added; semantic text preserved after punctuation removal |
| SRT subtitle | `subtitles/final.srt` | cue text from `subtitle_lines(item["narration_text"])` | `partially` | L25 truncates after first 4 subtitle lines |
| ASS subtitle | `subtitles/final.ass` | dialogue text from same `subtitle_lines()` | `partially` | same L25 truncation |
| burned subtitle overlay | generator script | `draw_subtitle_overlay()` -> `subtitle_lines(group["text"], limit=21)` | `partially` | final video visible subtitle uses same 4-line cap |
| card text | `timeline/card_placement_decision.json` and generator `LINE_GROUPS[].card` | `card_text` | `unclear / derived` | many card strings are summary/paraphrase, not exact locked text |
| summary_json | `summary.json` | paths/status only | `no direct text` | cannot prove copy match |
| review_manifest | `review_manifest.md` | paths/status only | `no direct text` | cannot prove copy match |
| locked_copy_diff_preflight | `locked_copy_diff_preflight_report.json` | `locked_copy_exact_non_whitespace_match` | `only LINE_GROUPS vs LOCKED_FINAL_SCRIPT` | does not compare final SRT/ASS/TTS/card text |

## 5. Diff summary（差异摘要）

| compare pair | diff type | allowed or unauthorized | example before | example after | file path |
| --- | --- | --- | --- | --- | --- |
| `locked_final_script` vs `script_to_timeline_map.narration_text` | `allowed_linebreak_diff` | `allowed` | `但聊着聊着，第二个问题就来了：\n\nCodex 到底能不能帮普通人赚钱？` | same text; grouping/newline only | `timeline/script_to_timeline_map.json` |
| `locked_final_script` vs TTS input | `allowed_tts_pause_diff + allowed_punctuation_diff` | `allowed_with_quality_risk` | `第二个问题就来了：\n\nCodex 到底能不能帮普通人赚钱？` | `第二个问题就来了：。Codex 到底能不能帮普通人赚钱？` | `audio/tts_route_report.json` |
| `locked_final_script` vs `final.srt` | `unauthorized_semantic_copy_change` | `unauthorized` | `有人选品。有人剪视频。有人看数据。有人复盘。有人整理素材。有人做下一版测试。` | `有人选品。有人剪视频。有人看数据。有人复盘。` | `subtitles/final.srt` |
| `locked_final_script` vs `final.ass` | `unauthorized_semantic_copy_change` | `unauthorized` | `有人整理素材。有人做下一版测试。` | missing from dialogue 25 | `subtitles/final.ass` |
| `locked_title / locked_opening_line` vs title/opening visible text | `allowed_title_match + generated_card_overreach_risk` | `partly_allowed` | title `Codex 到底能不能帮普通人赚钱？`; opening `最近网上很多人在聊 Codex。` | title card title matches; title card subtitle adds `第五期｜真实使用 3 个月后的判断` | `timeline/card_placement_decision.json` |
| locked script relevant lines vs cards | `generated_card_overreach` | `risk / needs gate` | `但这已经很夸张了。`; `这才是我现在真正用 Codex 的方式。` | card adds `夸张在试错成本变低`; `不是等它替我赚钱，而是让它帮我多跑几次` | `timeline/card_placement_decision.json` |
| locked copy vs preflight coverage | `diff_preflight_missing` | `unauthorized gap` | rule requires subtitle/TTS/card text comparison | report only stores `locked_copy_exact_non_whitespace_match=true` | `locked_copy_diff_preflight_report.json` |

## 6. First drift point（第一处漂移点）

- `drift_stage`: `subtitle_generation_layer`
- `file_path`: `dist/fifth_episode_codex_money_publish_candidate_20260603/scripts/生成第五期Codex赚钱正片_generate_fifth_codex_money_candidate.py`
- `output_files`: `dist/fifth_episode_codex_money_publish_candidate_20260603/subtitles/final.srt`; `dist/fifth_episode_codex_money_publish_candidate_20260603/subtitles/final.ass`; final video burned subtitle overlay
- `field_or_line`:
  - source L25 in generator: lines `620-621`
  - subtitle overlay call: lines `1323-1327`
  - subtitle formatting function: lines `1446-1458`
  - SRT/ASS writer: lines `1461-1474`
  - root line: `return "\n".join(out[:4])`
- `before_text`:

```text
有人选品。
有人剪视频。
有人看数据。
有人复盘。
有人整理素材。
有人做下一版测试。
```

- `after_text`:

```text
有人选品。
有人剪视频。
有人看数据。
有人复盘。
```

- `allowed_by_contract`: `false`
- `reason`: `script_to_timeline_map` L25 and TTS L25 both contain the full six short sentences, but `subtitle_lines()` hard caps subtitle output to four lines. That deletes two locked-copy clauses from SRT/ASS and from the burned subtitle overlay. This is not punctuation, linebreak, subtitle segmentation, or TTS pause adjustment; it is visible copy deletion.

## 7. Root cause（根因）

Primary root cause:

`subtitle / TTS / card generation rewrote text` 中的 `subtitle_generation_layer_truncated_locked_script`.

More precise classification:

- `locked_copy_contract missing`: `false`
- `locked_copy_contract exists but not consumed`: `false for timeline/TTS`; `partially true for final subtitles/cards`
- `subtitle / TTS / card generation rewrote text`: `true`; first unauthorized drift is subtitle truncation
- `preflight passed but did not check semantic diff`: `true`; `locked_copy_diff_preflight` only compares `LOCKED_FINAL_SCRIPT` with `script_from_line_groups()`
- `Codex treated unsupported copy as editable instead of copy_change_request`: `not primary`; no evidence the locked口播稿 was intentionally rewritten, but card summaries should have required a stricter card semantic gate or change request when not exact/near-exact

Secondary causes:

1. `locked_copy_diff_preflight_report.json` is too shallow. It records `locked_copy_exact_non_whitespace_match=true`, but does not include independent checks for `final.srt`, `final.ass`, `tts_text`, or `card_text`.
2. `subtitle_card_overlap_check` checks layout overlap, not copy completeness.
3. `card_decision_preflight_report.json` checks card existence/roles, not whether card text is exact locked copy, allowed excerpt, or unauthorized semantic compression.
4. `completion_truth_preflight_report.json` checks media/subtitle presence, not subtitle text equivalence.

## 8. Minimum repair recommendation（最小修复建议）

下一轮只修一个主点：

`补 locked_copy_diff_preflight`.

Minimum repair scope:

1. `locked_copy_diff_preflight` must compare `locked_final_script` against:
   - `script_to_timeline_map[].narration_text`
   - `audio/tts_route_report.json segment_reports[].tts_text`
   - `subtitles/final.srt`
   - `subtitles/final.ass`
   - actual burned subtitle source, or the exact function output used to burn subtitles
   - `card_placement_decision.card_groups[].card_text`
2. The subtitle generator must not drop lines silently. If one line_group expands beyond the visual subtitle limit, it should split into multiple subtitle cues or block with `subtitle_copy_match_failed`.
3. Card text should be classified as:
   - exact quote
   - allowed shortened excerpt
   - allowed non-semantic label
   - generated semantic summary requiring `copy_change_request`
4. `publish_candidate_preflight_report` must fail if `subtitle_copy_match`, `tts_input_copy_match`, `title_diff_check`, `opening_line_diff_check`, or `card_text_semantic_match` is missing.

Do not start by rewriting the video. Fix the copy-diff gate first, then rerun only after the gate can catch L25-style deletion.

## 9. Status boundary（状态边界）

- `did_not_modify_video`: `true`
- `did_not_modify_copy`: `true`
- `did_not_regenerate_tts`: `true`
- `did_not_change_mechanism_files`: `true`
- `did_not_change_subtitles`: `true`
- `did_not_change_cards`: `true`
- `content_validation_not_advanced`: `true`
- `send_ready_not_advanced`: `true`
- `publish_status_success_not_advanced`: `true`
- `voice_validation_not_advanced`: `true`
- `visual_master_locked_not_advanced`: `true`

## 10. Git sync status（如有文件写入）

- `files_changed`: `codex_log/copy_lock_audit/20260603_locked_copy_drift_audit.md`
- `commit_sha`: `pending_at_report_write_time`
- `pushed`: `pending_at_report_write_time`
- `remote_head_verified`: `pending_at_report_write_time`
- `unrelated_dirty_files`: `public/` existed before this audit and was not touched
- `secret_scan`: `pending_at_report_write_time`
- `completed_allowed`: `pending_git_sync`
